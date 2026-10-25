from pathlib import Path
from collections import Counter
from PIL import Image
import hashlib,json
root=Path(__file__).resolve().parent/'dataset'
out=Path(__file__).resolve().parent/'analysis'/'dataset_audit.json'
classes={'0':'helmet','1':'no_helmet'}
result={'dataset_root':'dataset/','classes':classes,'method':'Structural audit of YOLO label rows, image readability, paired files, image dimensions and exact SHA-256 duplicates. No model training or accuracy evaluation.','splits':{},'exact_duplicate_images':[],'warnings':[]}
seen={}
for split in ('train','valid','test'):
    image_dir=root/split/'images'; label_dir=root/split/'labels'
    images=sorted(p for p in image_dir.iterdir() if p.is_file())
    labels=list(label_dir.glob('*.txt'))
    counts=Counter(); boxes=0; segments=0; malformed=0; empty=0; missing=[]; unreadable=[]; sizes=Counter(); extra_labels=[]
    stems={p.stem for p in images}
    for p in images:
        try:
            with Image.open(p) as im:
                im.verify()
            with Image.open(p) as im:
                sizes[f'{im.width}x{im.height}']+=1
        except Exception:
            unreadable.append(p.name); continue
        h=hashlib.sha256(p.read_bytes()).hexdigest(); seen.setdefault(h,[]).append(f'{split}/{p.name}')
        lab=label_dir/(p.stem+'.txt')
        if not lab.exists():
            missing.append(p.name); continue
        for line in lab.read_text(encoding='utf-8-sig').splitlines():
            if not line.strip(): continue
            vals=line.split()
            try:
                cls=float(vals[0]); nums=[float(x) for x in vals[1:]]
                if cls!=int(cls) or str(int(cls)) not in classes: raise ValueError
                if len(nums)==4:
                    xc,yc,w,h=nums
                    if any(x<0 or x>1 for x in nums) or w<=0 or h<=0: raise ValueError
                    boxes+=1; counts[str(int(cls))]+=1
                elif len(nums)>=6 and len(nums)%2==0 and all(0<=x<=1 for x in nums):
                    segments+=1; counts[str(int(cls))]+=1
                else: raise ValueError
            except Exception:
                malformed+=1
    for lab in labels:
        if lab.stem not in stems: extra_labels.append(lab.name)
    result['splits'][split]={'images':len(images),'label_files':len(labels),'bounding_box_rows':boxes,'polygon_rows':segments,'annotation_rows':boxes+segments,'class_annotations':dict(counts),'empty_label_files':sum(not p.read_text(encoding='utf-8-sig').strip() for p in labels),'missing_label_files':len(missing),'extra_label_files':len(extra_labels),'malformed_rows':malformed,'unreadable_images':len(unreadable),'image_sizes':dict(sizes)}
    if missing or extra_labels or malformed or unreadable:
        result['warnings'].append({'split':split,'missing_labels':missing[:10],'extra_labels':extra_labels[:10],'malformed_rows':malformed,'unreadable_images':unreadable[:10]})
result['exact_duplicate_images']=[v for v in seen.values() if len(v)>1]
result['total_images']=sum(v['images'] for v in result['splits'].values())
result['total_box_rows']=sum(v['bounding_box_rows'] for v in result['splits'].values())
result['total_polygon_rows']=sum(v['polygon_rows'] for v in result['splits'].values())
result['total_annotation_rows']=result['total_box_rows']+result['total_polygon_rows']
result['total_class_annotations']={k:sum(v['class_annotations'].get(k,0) for v in result['splits'].values()) for k in classes}
out.write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))

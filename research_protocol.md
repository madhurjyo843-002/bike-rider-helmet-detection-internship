# Research protocol

## Research question
How reliably can a YOLOv8 object detector distinguish objects annotated as `helmet` and `no_helmet` in the supplied 640 × 640 images, and how does performance change across crowded scenes, small objects, lighting conditions, and rider types?

## Current baseline and status
The source archive provides train, validation, and test splits. A structural audit found 636 / 179 / 88 images and 1,702 annotation rows, including 1,701 bounding-box rows and one polygon row. It found no missing image-label pairs, unreadable images, malformed rows under their respective box/polygon formats, or exact duplicate images across splits. This is a dataset QA result only. Model training and inference have not been run, so no predictive performance is known.

## Data preparation before training
1. Keep the original `dataset/` unchanged and preserve the supplied source attribution.
2. Resolve the one polygon annotation into a detection box in a derived working copy, or formally switch to segmentation and harmonize all labels. For this project, detection is the target, so polygon-to-box conversion is the practical choice. Review this specific label visually before conversion.
3. Review a stratified sample of every split, especially tiny, occluded, side-view, bicycle and motorcycle riders, and images with watermarks or generated-looking content.
4. Confirm the class meaning at object level. The dataset names classes `helmet` and `no_helmet`; document whether each label marks a head/helmet, a whole rider, or another region. Do not train until the annotation unit is consistent.
5. Check for near duplicates or related frames and group them by original source/video/capture session before splitting. Exact SHA-256 deduplication found no identical image files, but it cannot detect near duplicates or source-level leakage.
6. Confirm the license and any privacy requirements for the intended publication or deployment.

## Suggested baseline experiment
Use a small pretrained YOLOv8 detector first, then compare a larger model only if compute and validation results justify it. Record package versions, pretrained checkpoint, random seed, image size, batch size, epochs, device, training time, and dataset/config hashes. Start with 640-pixel images and a fixed seed. Select checkpoints and tune thresholds using validation only. Keep test data sealed until the method is fixed.

Example command after installing the chosen Ultralytics/PyTorch build in a separate environment and resolving the polygon annotation:

```powershell
yolo detect train data="D:\internship project\data.yaml" model=yolov8n.pt imgsz=640 epochs=100 batch=16 seed=42
```

The command is a proposed experiment, not a run result. Adapt batch size to GPU memory and record any changes. Do not report the command's default settings as a reproducible result unless the execution log is retained.

## Evaluation plan
Report validation and final test precision, recall, mAP@0.50, and mAP@0.50:0.95 per class and overall. Include a confusion matrix and PR curves. Choose confidence thresholds on validation data, with a stated reason for the trade-off between missed no-helmet cases and false alerts. Add an error review with examples of false positives, false negatives, occlusion, small distant riders, multiple riders, unusual helmets, and low-light scenes. Provide per-condition results only where labels and sample counts support them. Report uncertainty and do not claim real-world enforcement readiness from a small image test set.

## Proposed improvements
- Re-annotate with a written class/box policy and independent review of a sample.
- Add diverse, locally representative scenes and explicitly track camera, time, weather, rider type, distance, and occlusion.
- Use source-grouped splitting and a separate external test set.
- Compare the baseline to an ablation with approved augmentation, avoiding transformations that erase small helmets or distort object geometry.
- Evaluate on short videos only after image-based detection is stable; consider tracking to avoid repeated frame-level alerts.
- Test the final model on the intended camera and hardware, measure latency and failure cases, and provide a human review path before any consequential action.

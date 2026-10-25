# Internship project files

## Project objective
Assess a consented YOLO-format image dataset for helmet versus no-helmet object detection, record reproducible dataset findings, and define a defensible training and evaluation plan.

## Contents
- `Internship_Project_Report.docx` — internship report draft with fill-in fields for host organization and personal details.
- `dataset/` — extracted source archive, kept intact.
- `data.yaml` — corrected dataset configuration for the extracted folder layout.
- `audit_dataset.py` — repeatable structural data audit.
- `analysis/dataset_audit.json` — machine-readable audit results.
- `research_protocol.md` — recommended training and evaluation protocol.
- `defense_questions.md` — likely reviewer questions with concise, evidence-based answers.
- `DATASET_ATTRIBUTION.md` — attribution and license metadata for the included dataset.
- `analysis/sample_images.png` — visual sample sheet from the three data splits.

## Run the data audit
Using Python with Pillow installed:

```powershell
python audit_dataset.py
```

The script reads `dataset/` and rewrites `analysis/dataset_audit.json`. It does not modify dataset images or labels. The audit was run on 25 October 2026.

## Training status
No model training or inference was completed in this environment. PyTorch and Ultralytics were not installed, no trained weights were present in the source archive, and this workstation reports Intel UHD integrated graphics. The report therefore contains no fabricated precision, recall, mAP, or model result. Follow `research_protocol.md` on a suitable GPU or cloud runtime to train and evaluate.

## Data provenance and attribution
The supplied archive identifies the dataset as Roboflow Universe project `bike-riders-helmet-detection-bjslq`, version 3, exported 16 May 2026, and marked CC BY 4.0. It was supplied by a friend who consented to its use for this project. Preserve the original attribution and license when sharing derived work; verify the license terms for any intended publication or redistribution.

# Likely review questions and honest answers

Use these as preparation notes and answer in your own voice. Keep the distinction clear between work completed in the dataset audit and experiments that are still proposed.

## Project scope and evidence

### 1. What did you actually build or investigate?
I inspected the supplied YOLO-format dataset, checked image and label files, counted classes and image dimensions, checked exact duplicate images, and documented a reproducible baseline experiment plan. This phase is dataset assessment and research preparation; it does not include a trained detector.

### 2. Why are there no accuracy or mAP results?
The supplied archive had no trained checkpoint, and the available environment lacked PyTorch and Ultralytics. I therefore did not train or run inference. Reporting precision, recall, or mAP without predictions would be misleading. The next step is to resolve the annotation questions and run the documented baseline in a suitable runtime.

### 3. Is this enough for a complete machine-learning internship project?
It is a transparent and reproducible preparation phase. If the assessment requires a trained model or experimental results, that requirement is not met yet. I would need to complete training, validation, test evaluation, and error analysis before presenting it as a full model-development result.

### 4. What is the research contribution if no model was trained?
The contribution in this phase is a measured profile of the supplied data, identification of a mixed annotation format and unresolved label-policy questions, a corrected path configuration, and an evaluation plan designed to avoid unsupported claims. It is not a new architecture or a demonstrated detector improvement.

## Dataset and annotation

### 5. How large is the dataset and how is it split?
The archive contains 903 images: 636 training, 179 validation, and 88 test images. Every image opened successfully and had a corresponding label file. The image dimensions are consistently 640 by 640 pixels.

### 6. What do the class counts show?
The supplied class order is class 0 `helmet` and class 1 `no_helmet`. The audit counted 1,016 and 686 annotations respectively. This is a moderate difference in object counts, but object counts alone do not tell us whether the scenes or difficulty levels are balanced. Future results should be reported per class.

### 7. What is the polygon annotation issue?
There is one polygon row in the training labels and 1,701 bounding-box rows. The project target is object detection, so I recommend visually checking that specific image and converting the polygon to its enclosing box in a derived copy. I have not changed the source archive or claimed that this cleanup is complete.

### 8. Are the labels semantically correct?
The audit checks file structure and coordinate ranges; it cannot determine whether the annotator chose the right object or box boundary. The export names the classes but does not clearly state whether a box should cover a helmet/head or a whole rider. An annotation guide and a manual review sample are needed before training.

### 9. Are the training, validation, and test sets independent?
The audit found no byte-identical images by SHA-256 hash. That does not rule out near-duplicates, adjacent video frames, or images from the same capture session. Source-level grouping should be checked before relying on test metrics.

### 10. Does the data represent the intended use?
That has not been established. A visual sample included both motorcycles and bicycles and showed some watermarked or stock-style images. The intended population and image sources should be defined, then the full dataset should be reviewed for coverage of lighting, distance, occlusion, camera angle, and rider type.

### 11. Did the export apply image augmentation?
The supplied Roboflow metadata says that images were auto-oriented and stretched to 640 by 640 pixels, with no augmentation techniques applied during export. A future training run may apply controlled augmentation, but transformations should not erase or distort small helmets. Training-time augmentation settings must be logged separately from export preprocessing.

## Method and evaluation

### 12. Why use YOLOv8?
The supplied labels and project framing are compatible with a YOLO-style object-detection workflow, and YOLOv8 is the selected baseline framework in the project plan. The choice is a practical starting point, not evidence that it is the best model. A later study could compare it with another detector under the same splits and compute budget.

### 13. How would you evaluate the model?
I would fit on training data, use validation data for checkpoint and confidence-threshold choices, and reserve test data for one final assessment. I would report precision, recall, mAP@0.50 and mAP@0.50:0.95 per class and overall, add a confusion matrix and precision-recall curves, and review false positives and false negatives by scene condition.

### 14. Why not use accuracy alone?
Object detection involves both localization and classification, and the number of background regions makes simple accuracy hard to interpret. Precision, recall, and average precision describe different parts of detection performance; per-class metrics and error examples make trade-offs more visible.

### 15. Can the model be used for real-time enforcement?
No such claim is supported. There is no trained model, target-camera evaluation, latency measurement, or external validation. Even after those steps, a model should be treated as a screening aid with human review rather than as the sole basis for a consequential decision.

## Ethics, provenance, and limitations

### 16. Was the dataset use authorized?
The dataset was supplied by a friend who consented to its use for this project. The archive also identifies a Roboflow Universe source and states a CC BY 4.0 license. I would preserve attribution and verify the applicable terms before public redistribution or publication.

### 17. What privacy or fairness risks remain?
The audit did not perform a privacy or demographic fairness assessment. Before deployment, image permissions, identifiable people and license plates, local data rules, and performance across relevant rider groups and conditions should be reviewed. A data-only audit cannot establish those safeguards.

### 18. What are the main limitations of your current findings?
The dataset is small for a safety-related use, the label policy is not fully specified, one label uses polygon format, source-level leakage and representativeness have not been ruled out, and no model was trained or tested. The findings are limited to structural checks on the supplied archive.

## Short closing response

If asked to summarize the work in one sentence: “I audited and documented the supplied dataset so the next YOLOv8 experiment can be run reproducibly, while clearly separating verified data findings from model results that still need to be measured.”

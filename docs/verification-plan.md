# 9. Verification and Evaluation Plan

Version 0.2, 20 October 2026. DIP-11. Experiment plan; no training, measured metrics or user trials have been completed in this version.

## Data and Leakage Prevention

The first baseline uses APTOS 2019. EyePACS is an extension after access and rights checks. Reserve IDRiD and Messidor-2 for external evaluation; do not use them to select preprocessing, weights, thresholds or temperature. Provenance and conditions appear in docs/data-plan.md.

E01: build a manifest containing source, image_id, patient_id if available, label, SHA-256, dimensions and split. Detect identical files using SHA-256 and visually similar files using perceptual hashes and manual inspection. Group both eyes and visits of the same patient. Form groups first, then stratify into train 70%, tuning 10%, calibration 10%, test 10%; seed=42. If patient counts are small, document any ratio change before measuring metrics. If patient_id is unavailable, do not claim patient-level splitting; disclose potential performance inflation.

E02: freeze internal-test and external manifests before training. Derive preprocessing, class weights and samplers from train only. Use tuning for hyperparameters and early stopping, calibration for temperature and threshold, never weights. External sets must not influence selection. Check overlap with training sources before external evaluation. External testing is not clinical validation.

## Baseline and Comparisons

E03: a naive baseline predicts training-class frequencies. The CNN baseline is ImageNet-pretrained EfficientNet-B0, 384x384, cross-entropy, AdamW, up to 30 epochs, early stopping on tuning QWK with patience=5. Initial lr=1e-4, weight_decay=1e-4, batch=16 or maximum that fits memory; record changes. Apply augmentation to train only; no random test transforms. Compare ResNet50 on the same split/resolution using seeds 42/43/44. Record actual time, memory, versions and cost.

Change one factor at a time: weighted loss, resolution or ordinal formulation. Compare against the fixed baseline; derive class weights from train only. Limit experiments to available resources; first complete one reproducible baseline. RETFound is a literature alternative, not mandatory implementation.

## Metrics and Uncertainty

E04: the primary metric is quadratic weighted kappa for ordered classes 0..4; also report macro-F1 and the confusion matrix with counts. For binary evaluation, ground truth is y>=2 and score=p2+p3+p4. Measure AUROC and AUPRC. Select the threshold on calibration only: among thresholds with specificity >= 0.90, maximise sensitivity; break ties by higher specificity. Define threshold enumeration and equal-score handling in code. On test, report actual sensitivity/specificity at that same threshold; do not assume specificity remains 0.90. Argmax grade and the binary flag can disagree because they answer different questions.

Fit temperature T>0 on calibration by multiclass NLL. Report NLL, Brier score and top-label ECE before/after calibration using 15 equal-width bins: ECE = sum of bin fraction multiplied by |accuracy - mean confidence|. Show a separate reliability diagram and binary ECE for the binary score. ECE depends on binning and does not guarantee reliability of individual answers.

E05: estimate 95% percentile bootstrap confidence intervals using 2,000 patient resamples. If patient_id is unknown, resample images and disclose the limitation. For AUROC, skip and count degenerate resamples containing only one class. Compare models with paired bootstrap on the same observations; distinguish seed variation from sampling confidence intervals. Report separate IDRiD/Messidor-2 metrics, change relative to internal test, class distributions and cameras if known. Document label mapping before evaluation; do not invent five-grade labels. Omit metrics without suitable ground truth.

## Prototype Tests

| ID | Test | Expected result |
|---|---|---|
| T01 | Valid JPG/PNG and grayscale | 200 and valid contract |
| T02 | Empty file, disguised extension, corrupt bytes | 415 or 422 according to cause; no inference |
| T03 | >20 MiB, >40 million pixels, filename containing ../ | 413 for limit; filename does not control path |
| T04 | Fixed test logits | Finite softmax, sum 1; grade 0..4 |
| T05 | Scores below, above and equal to threshold | flag exactly matches score >= threshold |
| T06 | Missing weights, exception, new upload | 503/500 with request_id; no stale output; temporary files deleted |
| T07 | Grad-CAM on control image | Correct geometry; map failure preserves main result |
| T08 | Inspect every screen | Research-use and limitation statements |
| T09 | Re-evaluate identical data/weights | Versions, manifest and comparable result retained |
| T10 | Inspect logs/temporary directory | No images or personal information |
| P01 | 100 sequential requests after 10 warm-ups | Record p50/p95, errors, hardware; compare with 10 s target |
| U01 | Keyboard and 375 px screen | All actions reachable, clear errors, no horizontal scrolling |

## Explainability Evaluation

Select correct and incorrect examples from every class, including overconfident errors. Generate Grad-CAM for the predicted class and compare with occlusion of salient regions. Discuss maps with the adviser after obtaining consent. Qualitative judgement does not replace quantitative evaluation or prove map causality [L04].

## Stage Completion Criterion

Retain code, manifests, configurations, weights with checksums, reports of all executed experiments and limitations. Report negative results as well. QWK >= 0.85 is achieved only if measured on the actual internal test set; it is not a clinical-use threshold.

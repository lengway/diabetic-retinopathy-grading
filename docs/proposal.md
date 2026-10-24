# 1. Problem Statement and Project Proposal

**Title:** Development of an Intelligent Assistant for Grading Diabetic Retinopathy Using Fundus Images
**Degree programme:** Software Engineering, Astana IT University
**Student:** Roman Vladimirovich Kutbeyev, SE-2404 (individual project)
**Supervisor:** Marzhan Kabdykalievna Turarova
**Medical adviser:** to be confirmed
**Version:** 0.2, 20 October 2026; English translation: 24 October 2026

## 1. Problem

Diabetic retinopathy (DR) is a microvascular complication of diabetes and a leading cause of vision loss among working-age adults. Early stages are asymptomatic, making regular fundus-image screening important for people with diabetes.

- Approximately 589 million adults aged 20-79 had diabetes in 2024; the projected number is 853 million by 2050. An estimated 43% are undiagnosed (IDF Diabetes Atlas, 11th edition, 2025).
- DR affects 22.27% of people with diabetes: approximately 103 million in 2020, projected to reach 160.5 million by 2045. Vision-threatening DR affects 6.17% (Teo et al., Ophthalmology, 2021).

Manual assessment requires qualified specialists whose numbers do not grow as quickly as the patient population. Automated screening systems, including IDx-DR/LumineticsCore and EyeArt, are proprietary and cannot be freely studied, reproduced or adapted. Open models trained on one dataset often lose performance on images from other cameras and clinics. The reliability of model confidence is also rarely reported.

## 2. Users

| User | Task | Required output |
|---|---|---|
| Primary-care physician / endocrinologist | Assess referral to an ophthalmologist | Understandable recommendation and confidence |
| Ophthalmologist | Prioritise images and inspect model decisions | ICDR grade and heatmap |
| Screening operator | Upload an image and obtain a result | Simple interface and unsuitable-image message |

These user groups and needs are assumptions to be checked with the medical adviser and practising clinicians (docs/meetings/).

## 3. Aim

Develop and evaluate a research prototype that grades DR from fundus images using the ICDR scale and supports referral assessment with calibrated confidence and a visual explanation. Evaluate reliability on independent external data.

## 4. Objectives

1. Review the domain, literature and existing automated DR screening systems.
2. Prepare APTOS 2019 and EyePACS for training/validation and IDRiD and Messidor-2 for external evaluation; perform EDA, preprocessing and leakage-free splitting.
3. Train a ResNet50/EfficientNet baseline; investigate ordinal regression with threshold selection, class imbalance, augmentation and preprocessing.
4. Evaluate internal/external performance and analyse deterioration across sources.
5. Calibrate probabilities using temperature scaling and evaluate ECE.
6. Generate Grad-CAM heatmaps and review them with the medical adviser.
7. Implement a web service: upload, grade, confidence, heatmap and referral-related output.
8. Test the system and prepare documentation and the thesis.

## 5. Expected Results

| Deliverable | Criterion |
|---|---|
| Reproducible pipeline | README instructions produce comparable metrics |
| DR grading model | Internal-test QWK >= 0.85: research target, not a commitment |
| Evaluation report | Internal/external QWK, AUC, sensitivity at fixed specificity for referable DR, ECE |
| Explainability analysis | Grad-CAM review with the adviser |
| Web prototype | Upload-to-result workflow runs in Docker |
| Documentation | Requirements, architecture, ADRs, verification plan and thesis |

## 6. Scope

Included: five ICDR classes; separate binary research label DR >= 2 without independent macular-oedema detection; public datasets; external evaluation; calibration; Grad-CAM; REST API and simple web interface. Image-quality assessment is optional if time permits.

Excluded: lesion segmentation; other eye diseases such as glaucoma and AMD; mobile application; domain adaptation; clinical validation; medical-device registration; health-information-system integration.

## 7. Constraints and Assumptions

- The prototype is for research and is not a medical device. Its output supports analysis and is not a diagnosis.
- Public datasets will be used under their licences; identifiable patient data will not be processed.
- Local development uses Apple Silicon and PyTorch MPS; larger experiments may require a rented GPU.
- Public labels may contain noise, which must be considered when interpreting metrics.

## 8. Stages

| Period | Stage | Checkpoint |
|---|---|---|
| 13-24 October 2026 | Analysis, requirements, architecture, verification planning | School package |
| November-December 2026 | Data, EDA, baseline | pre-defense-1 |
| January-February 2027 | Improvements, cross-dataset evaluation, calibration, Grad-CAM | pre-defense-2 |
| March-April 2027 | Service, testing, adviser-assisted error analysis | To be scheduled |
| April-May 2027 | Thesis and final preparation | final-pre-defense |

## References

1. International Diabetes Federation. IDF Diabetes Atlas, 11th ed. Brussels, 2025. https://diabetesatlas.org/media/uploads/sites/3/2025/04/IDF_Atlas_11th_Edition_2025_Global-Factsheet.pdf
2. Teo Z.L. et al. Global prevalence of diabetic retinopathy and projection of burden through 2045: systematic review and meta-analysis. Ophthalmology, 2021, 128(11):1580-1591.
3. Wilkinson C.P. et al. Proposed international clinical diabetic retinopathy and diabetic macular edema disease severity scales. Ophthalmology, 2003, 110(9):1677-1682.

The full reference list appears in the literature review.

## Status Clarification: 20 October 2026

The proposal describes the intended thesis outcome. The current package contains analytical documents and mockups; no model or service has been implemented and no metrics have been measured. DR >= 2 defines the ground-truth binary label. The predicted flag uses p2+p3+p4 and a fixed threshold; it is not equivalent to argmax grade >= 2 and does not assess DME. Rules appear in requirements.md and verification-plan.md. Dataset usage conditions must be confirmed before downloading; public accessibility does not imply unrestricted use.

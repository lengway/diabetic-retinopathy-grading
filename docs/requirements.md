# 6. Requirements Specification

Version 0.2, 20 October 2026. DIP-8. Draft requirements for a research prototype; user validation is pending. Owner: Roman Vladimirovich Kutbeyev.

## Workflow and Terminology

An operator uploads one colour fundus image from an authorised de-identified dataset. The system validates and preprocesses the file and returns a research assessment. ICDR grades: 0, no apparent DR; 1, mild; 2, moderate; 3, severe non-proliferative; 4, proliferative [L02]. DR >= 2 defines this project's binary research label. It excludes independent diabetic macular oedema detection and is not the complete clinical referral decision.

## Functional Requirements

| ID | Priority | Requirement | Acceptance criterion |
|---|---|---|---|
| FR-01 | Must | Upload one JPG/PNG, up to 20 MiB | Valid RGB/grayscale images decode to RGB; 20 MiB + 1 byte is rejected; a valid extension alone is insufficient |
| FR-02 | Must | Validate decoding and dimensions | Empty/corrupt file: 422; unsupported format: 415; over 40 million pixels or 20 MiB: 413; no model invocation |
| FR-03 | Must | Grade 0-4 | Integer grade in 0..4; five finite probabilities in [0,1], sum 1 within 1e-5; grade = argmax |
| FR-04 | Must | Binary research flag | score = p2+p3+p4; flag = score >= threshold; response includes threshold and its version; do not replace rule with grade >= 2 |
| FR-05 | Must | Explain confidence | Display max(p), calibration status and 'model estimate, not probability of being healthy'; explicitly mark uncalibrated output |
| FR-06 | Should | CNN Grad-CAM | Overlay on the same image after reversing geometric transforms; identify selected class; map failure preserves grade and produces a warning |
| FR-07 | Must | Research-use statement | Warning on upload/result screens; a negative flag does not promise absence of other diseases |
| FR-08 | Must | State management | Upload, processing, result and error states visible; prevent resubmission during processing; hide old output after new file selection |
| FR-09 | Must | Result identification | API returns model_version, preprocessing_version, request_id and threshold; experiment report retains the same versions |
| FR-10 | Could | Automatic gradability assessment | Implement only after independent quality labels and a threshold are defined; no clinical gradability claim beforehand |

## Non-functional Requirements

| ID | Priority | Requirement | Acceptance criterion |
|---|---|---|---|
| NFR-01 | Must | Reproducibility | Retain split manifest, seed, data SHA-256, dependency versions and weights; repeated evaluation of identical weights differs in QWK by <= 0.001 |
| NFR-02 | Must | Data minimisation | No images in database/logs; delete temporary files after response and exceptions; test temporary directory |
| NFR-03 | Must | Resilience | Missing model: 503; internal error: 500 without path/stack disclosure; errors include request_id |
| NFR-04 | Should | Response time | Target CPU p95 <= 10 s over 100 sequential images after 10 warm-ups, batch=1, 384 px; record CPU, RAM, OS, threads and version before measurement; no measurements yet |
| NFR-05 | Must | Test-data isolation | No patient_id or duplicate overlap between train, tuning, calibration and test; disclose unknown patient identity |
| NFR-06 | Must | Verifiable performance | Publish QWK, 5x5 confusion matrix, AUROC, sensitivity/specificity, ECE and confidence intervals under the plan; QWK 0.85 is a target |
| NFR-07 | Should | Accessibility | Keyboard-accessible workflow, labelled file input, text errors; no horizontal scrolling at 375 px |
| NFR-08 | Must | Execution restrictions | Never execute uploads or use filenames as paths; check byte and decoded-pixel limits before inference |

## Draft API Contract

POST /api/v1/predict, multipart field image. Success 200: request_id, grade, probabilities[5], referable_score, referable_threshold, referable_flag, confidence, calibration_status, model_version, preprocessing_version, optional heatmap, warnings[]. Errors 413/415/422/503/500 contain error.code, error.message and request_id. Mockup responses are not outputs of a working model.

## Traceability

FR-01/02/08 -> UC-01 upload and UC-03 error -> T01-T03/T06. FR-03/04/05/09 -> UC-02 result -> T04/T05/T09. FR-06 -> T07. FR-07 -> T08. NFR-01/05/06 -> E01-E05. NFR-02/03/08 -> T02/T03/T06/T10. NFR-04 -> P01. NFR-07 -> U01. Test descriptions appear in the verification plan.

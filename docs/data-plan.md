# Data Plan and Access Conditions

DIP-6. 20 October 2026. Datasets were not downloaded in this session; EDA has not been completed. Figures describe published sources/plans, not local-file measurements.

| Dataset | Purpose | Primary source | Restriction |
|---|---|---|---|
| APTOS 2019 | Initial train/tuning/calibration/test | https://www.kaggle.com/competitions/aptos2019-blindness-detection/data | Check/accept competition rules in own account; availability is not redistribution permission |
| EyePACS/Kaggle 2015 | Additional training | https://www.kaggle.com/competitions/diabetic-retinopathy-detection/data | Separate rules, volume and patient identifiers; check before combining |
| IDRiD | External evaluation | https://idrid.grand-challenge.org/ ; L07 | Different subtasks; disease-grading images/labels are required, not masks alone |
| Messidor-2 | External evaluation | https://www.adcis.net/en/third-party/messidor2/ | Images and third-party labels may have different terms; confirm label source and mapping |

Before downloading, record date, version, usage terms, registration, training permission, image/weight redistribution and required citation. Rights status remains 'unconfirmed' until checked. Clinical patient data are outside current scope.

EDA must report actual file/missing/duplicate counts, class distribution 0..4, dimensions, decoding failures, class examples where publication is permitted, patient_id limitations and split protocol. If access is unavailable, leave the task open; do not substitute published frequencies for local analysis. Do not commit datasets or weights to Git.

# 4. Existing System Comparison

DIP-4. 20 October 2026. Three systems are compared against eight criteria using specific FDA documents. Characteristics apply to the cited regulatory versions.

| Criterion | IDx-DR [S1] | EyeArt [S2] | AEYE-DS [S3] |
|---|---|---|---|
| Comparison basis | De Novo DEN180001, 2018 | 510(k) K200667, 2020 | 510(k) K240058, 2024 |
| Intended use | Automated more-than-mild DR detection | mtmDR and vision-threatening DR detection | Automated mtmDR detection |
| Target population | Adults with diabetes without previously diagnosed DR | Adults with diabetes, subject to IFU restrictions | Adults with diabetes without previously diagnosed DR |
| Output level | mtmDR screening result | Screening endpoints | mtmDR screening result |
| Five ICDR grades as user output | Not stated in reviewed intended use | Not stated in reviewed intended use | Not stated in reviewed intended use |
| Equipment | Topcon NW400 | Cameras specified in document | Topcon NW400 and Optomed Aurora |
| Image gradability | Image-quality checks | Image-quality checks | Image-quality checks |
| Pre-market evaluation | Clinical evidence in De Novo | Clinical/equivalence evidence in 510(k) | Clinical/equivalence evidence in 510(k) |

For five-grade output, absence of a statement is not proof of absence from all versions. Open weights, pricing, Kazakhstan availability and user-facing calibrated probabilities were not established from these documents.

## Design Implications

Each system has a defined intended use, population and compatible equipment. A student prototype accepting arbitrary uploads cannot inherit its clinical conclusions. File-decoding checks are not clinical gradability assessment.

The project targets research reproducibility: five classes, separate DR >= 2 label, external evaluation, calibration and Grad-CAM. These are planned properties, not demonstrated advantages. Unlike regulatory mtmDR definitions, the binary label does not independently detect DME. Trial sensitivity/specificity values are not ranked because populations, reference standards and endpoints differ.

## Primary Sources

[S1] FDA. De Novo classification request for IDx-DR, DEN180001: intended use, restrictions, technical/clinical evaluation. https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN180001.pdf

[S2] FDA. EyeArt 510(k) summary, K200667: indications, system and clinical study. https://www.accessdata.fda.gov/cdrh_docs/pdf20/K200667.pdf

[S3] FDA. AEYE-DS 510(k) summary, K240058: intended use and cameras. https://www.accessdata.fda.gov/cdrh_docs/pdf24/K240058.pdf

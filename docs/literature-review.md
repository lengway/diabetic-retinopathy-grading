# 3. Literature Review

DIP-3. Version 0.2, 20 October 2026. Review of the domain and methods; no original experimental results.

## Selection Method and Scope

Sources were checked on 20 October 2026 using PubMed, publisher, PMLR and arXiv pages. Search topics: diabetic retinopathy grading, external validation, retinal foundation models, calibration, explainability and prospective screening. Fifteen scientific publications are included; eight appeared in 2022-2025, within the preceding five years. Seven earlier works establish the grading scale, methods and datasets. Sources were selected through targeted searches; this is not a systematic meta-analysis.

Analysis uses available abstracts, article pages and method descriptions. Reading every full text or reproducing experiments is not claimed. Links identify primary publications or bibliographic records. Published findings are not results of this project.

## Analysis Table

| ID / year | Study and approach | Project use | Transfer limitation |
|---|---|---|---|
| L01 / 2021 | Teo et al.; prevalence meta-analysis | Relevance | Global prevalence is not local demand |
| L02 / 2003 | Wilkinson et al.; ICDR consensus | Five ordered grades | Macular-oedema scale is separate |
| L03 / 2016 | Gulshan et al.; DL for referable DR | Task baseline and external testing | Binary detection does not establish five-class performance |
| L04 / 2017 | Selvaraju et al.; Grad-CAM | CNN region attribution | Neither lesion labels nor causal proof |
| L05 / 2017 | Guo et al.; temperature scaling | Held-out calibration | No guarantee on another camera |
| L06 / 2019 | Tan and Le; EfficientNet | Compact CNN baseline | ImageNet efficiency does not guarantee DR performance |
| L07 / 2018 | Porwal et al.; IDRiD | Independent evaluation source | Distinguish subtasks and label availability |
| L08 / 2022 | Ruamviboonsuk et al.; prospective Thai screening | Workflow and rejection analysis | Different setting, equipment and protocol |
| L09 / 2022 | Automated multidimensional platform; multicentre retrospective evaluation | Gradability and image limits | Retrospective testing does not replace deployment |
| L10 / 2024 | Wolf et al.; ACCESS randomised trial | Screening completion beyond AUC | One paediatric centre; no proof of local demand |
| L11 / 2024 | Autonomous AI in underserved populations; deployment study | Access and group differences | Observational association is not causation |
| L12 / 2024 | Dai et al.; DeepDR Plus progression prediction | External cohorts and alternative endpoint | Time-to-progression is outside scope |
| L13 / 2023 | Zhou et al.; RETFound self-supervision | CNN alternative and label efficiency | Resources and pretraining overlap complicate testing |
| L14 / 2025 | Data-efficient strategy; RETFound-DE | Data-efficient alternatives | Synthetic-data generation is outside scope |
| L15 / 2025 | Engelmann and Bernabeu; RETFound-Green | Foundation-model cost/compactness | Reported gains belong to the authors' protocol |

## Synthesis

ICDR [L02] defines ordered output, but mtmDR detection differs from five-grade classification. Report QWK and per-class errors separately from binary AUROC and sensitivity/specificity. Unlike clinical screening systems, this prototype does not assess macular oedema or provide a complete referral decision.

Deployment studies [L08-L11] show the importance of workflows, gradability and follow-up. They motivate studying the scenario but do not replace 3-5 interviews with actual prospective users.

RETFound and economical extensions [L13-L15] broaden alternatives beyond CNNs. Given time limits, start with a reproducible compact baseline [L06]. Foundation models remain a comparison direction; changing models requires measured improvement under one protocol without pretraining/test leakage.

A confident model can be wrong. Evaluate calibration [L05] separately from classification and again externally. Use Grad-CAM [L04] for error analysis and adviser discussion without assuming clinical validity.

## Research Questions

RQ1: How do QWK and binary DR >= 2 detection change from internal to independent external data? RQ2: Does temperature scaling improve NLL/ECE, and does the improvement persist externally? RQ3: Which errors and artifacts emerge through Grad-CAM analysis? These questions define a testable educational contribution without claiming a new clinical system.

## Bibliography

[L01] Teo Z.L. et al. Global Prevalence of Diabetic Retinopathy and Projection of Burden through 2045: Systematic Review and Meta-analysis. Ophthalmology, 2021, 128(11):1580–1591. https://pubmed.ncbi.nlm.nih.gov/33940045/

[L02] Wilkinson C.P. et al. Proposed international clinical diabetic retinopathy and diabetic macular edema disease severity scales. Ophthalmology, 2003, 110(9):1677–1682. DOI 10.1016/S0161-6420(03)00475-5. https://pubmed.ncbi.nlm.nih.gov/13129861/

[L03] Gulshan V. et al. Development and Validation of a Deep Learning Algorithm for Detection of Diabetic Retinopathy in Retinal Fundus Photographs. JAMA, 2016, 316(22):2402–2410. DOI 10.1001/jama.2016.17216. https://pubmed.ncbi.nlm.nih.gov/27898976/

[L04] Selvaraju R.R. et al. Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization. ICCV, 2017; preprint 2016. https://arxiv.org/abs/1610.02391

[L05] Guo C. et al. On Calibration of Modern Neural Networks. ICML, PMLR 70:1321–1330, 2017. https://proceedings.mlr.press/v70/guo17a.html

[L06] Tan M., Le Q. EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks. ICML, PMLR 97:6105–6114, 2019. https://proceedings.mlr.press/v97/tan19a.html

[L07] Porwal P. et al. Indian Diabetic Retinopathy Image Dataset (IDRiD): A Database for Diabetic Retinopathy Screening Research. Data, 2018, 3(3):25. DOI 10.3390/data3030025. https://www.mdpi.com/2306-5729/3/3/25

[L08] Ruamviboonsuk P. et al. Real-time diabetic retinopathy screening by deep learning in a multisite national screening programme: a prospective interventional cohort study. The Lancet Digital Health, 2022. https://pubmed.ncbi.nlm.nih.gov/35272972/

[L09] Zhang G. et al. Automated multidimensional deep learning platform for referable diabetic retinopathy detection: a multicentre, retrospective study. BMJ Open, 2022, 12:e060155. DOI 10.1136/bmjopen-2021-060155. https://pubmed.ncbi.nlm.nih.gov/35902186/

[L10] Wolf R.M. et al. Autonomous artificial intelligence increases screening and follow-up for diabetic retinopathy in youth: the ACCESS randomized control trial. Nature Communications, 2024, 15:421. DOI 10.1038/s41467-023-44676-z. https://www.nature.com/articles/s41467-023-44676-z

[L11] Autonomous artificial intelligence for diabetic eye disease increases access and health equity in underserved populations. npj Digital Medicine, 2024, 7:196. DOI 10.1038/s41746-024-01197-3. https://www.nature.com/articles/s41746-024-01197-3

[L12] Dai L. et al. A deep learning system for predicting time to progression of diabetic retinopathy. Nature Medicine, 2024, 30:584–594. DOI 10.1038/s41591-023-02702-z. https://pubmed.ncbi.nlm.nih.gov/38177850/

[L13] Zhou Y. et al. A foundation model for generalizable disease detection from retinal images. Nature, 2023, 622:156–163. DOI 10.1038/s41586-023-06555-x. https://www.nature.com/articles/s41586-023-06555-x

[L14] A data-efficient strategy for building high-performing medical foundation models. Nature Biomedical Engineering, 2025. DOI 10.1038/s41551-025-01365-0. https://www.nature.com/articles/s41551-025-01365-0

[L15] Engelmann J., Bernabeu M.O. Training a high-performance retinal foundation model with half-the-data and 400 times less compute. Nature Communications, 2025, 16:6862. DOI 10.1038/s41467-025-62123-z. https://www.nature.com/articles/s41467-025-62123-z

## Publication Data, Metrics and Findings

These are published findings, not project results. Numerical values absent from the checked descriptions are not reconstructed from memory.

| ID | Data / design | Evaluation | Finding and limitation |
|---|---|---|---|
| L01 | Meta-analysis of people with diabetes | Prevalence and 95% CI | DR 22.27%; no local-demand estimate |
| L02 | International expert consensus | Classification agreement | Five-grade scale, not an ML benchmark |
| L03 | Labelled fundus photos; EyePACS-1/Messidor-2 evaluation | Sensitivity, specificity, AUC | DL detects referable DR; binary task |
| L04 | Image recognition tasks | Localisation and qualitative maps | Gradient maps indicate CNN attention; no clinical endpoint |
| L05 | Image/document classification | Calibration including ECE | Temperature scaling improves calibration on studied tasks |
| L06 | ImageNet and transfer tasks | Accuracy, parameters, compute | Joint depth/width/resolution scaling works under authors' protocol |
| L07 | IDRiD images with grading/subtask labels | Dataset, annotation and task description | Research dataset, not our model result |
| L08 | 7,651 eligible Thai screening participants | Accuracy, sensitivity, specificity for vision-threatening DR | Prospective workflow evaluation; endpoint broader than DR >= 2 |
| L09 | Multicentre retrospective data; five classifiers | Accuracy, F1, sensitivity, specificity, AUROC, AUPRC | Quality and screening components evaluated; no direct prototype comparison |
| L10 | ACCESS: 81 intervention and 83 control participants | Screening completion within six months | 100% versus 22% in that study, not model accuracy |
| L11 | Integrated health-system deployment; >17,000 adults with diabetes | Screening adherence and group differences | AI use associated with access gains; confounding possible |
| L12 | Pretraining and longitudinal progression cohorts | C-index and integrated Brier score | Time to progression, not current grade |
| L13 | Self-supervision on about 1.6 million CFP/OCT images and downstream tasks | Downstream performance, label efficiency, external testing | Useful representations; no guaranteed gain on our split |
| L14 | Synthetic/real fundus data; nine public datasets | Downstream performance and label needs | Data-efficient pretraining reduces real-data needs in the study |
| L15 | 75,000 public pretraining images and external downstream sets | Performance and training/inference resources | Compact RETFound-Green reduces resources under authors' protocol; no local measurement |

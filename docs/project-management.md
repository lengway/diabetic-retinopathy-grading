# 10. Project Management and Risks

DIP-12. 20 October 2026. Sole project owner: Roman Vladimirovich Kutbeyev (GitHub: lengway). Supervisor: Marzhan Kabdykalievna Turarova.

## Work Tracking and Evidence

Repository: https://github.com/lengway/diabetic-retinopathy-grading . YouTrack: https://diabeticretinopathygrading.youtrack.cloud . Project DIP uses Kanban with the Stage field. Each issue specifies an assignee, deliverable, acceptance criteria and due date. Prepare changes in a DIP-ID branch, retain real commit dates and use Pull Requests. Do not rewrite history to imitate gradual work. Set Done only after checking criteria.

The sole student's contribution covers problem formulation, analysis, requirements, architecture and UX, followed by data/ML, service and testing. This version does not claim completed training or implementation. Match contribution statements to files/Git history before submission. Earlier verified work includes DIP-1 scaffolding, DIP-2 proposal and DIP-12 planning/YouTrack link.

## Immediate Schedule

| Date | Deliverable | Dependency |
|---|---|---|
| 20 October | Reviews, comparisons, requirements, architecture, mockups and draft report | Primary sources |
| 21 October | 3-5 user interviews or school-accepted client evidence; feedback request | Specialist availability and format agreement |
| 22 October | Authorised dataset acquisition and EDA; review corrections | Accounts/dataset terms |
| 23 October | Documents, actual statuses, committee access and screenshots | Recipient account information |
| 24 October, by 17:00 | Final check and upload of two PDFs by one representative | University account |
| 24 October, 18:00 | School form closes | Astana time / Asia/Almaty |

The one-hour reserve is internal; the official deadline is 18:00 on 24 October 2026. Completing all interviews within one day is not guaranteed and remains the main open risk.

## Thesis Milestones: Proposed Schedule

November-December 2026: data and baseline. January-February 2027: external evaluation, calibration and explainability. March-April: service and tests. April-May: thesis. Confirm defence dates with the school. Create pre-defense-1, pre-defense-2 and final-pre-defense tags at actual checkpoints; do not move them.

## Risk Register

| ID | Risk | Likelihood / impact | Mitigation and trigger | Owner |
|---|---|---|---|---|
| R1 | User need unconfirmed | High / high | Schedule interviews; report missing records by 22 October | Student |
| R2 | No supervisor feedback | High / high | Prepare a specific review package; record approval only after response | Student |
| R3 | Committee cannot access private materials | Medium / high | Identify accounts, grant read access and verify as recipient | Student |
| R4 | Licence/label restrictions | Medium / high | Rights register before download; no image redistribution; document dataset changes | Student |
| R5 | Eye/patient/duplicate leakage | High / high | Grouping, hashes, split tests; disclose unknown patient_id | Student |
| R6 | External performance drop | High / high | Untuned external test, report drop and limit conclusions | Student |
| R7 | Imbalance and weak classes | High / medium | Per-class recall, macro-F1; train-only weighted loss | Student |
| R8 | Insufficient GPU/time | Medium / medium | Start with B0; limit experiments; agree budget before renting | Student |
| R9 | Overconfidence or diagnostic reading of maps | Medium / high | Calibration, error analysis, clear research-use labels | Student |
| R10 | Form unavailable near deadline | Medium / high | Sign in early, check file sizes/fields and retain submission confirmation | Student |

## Access

The repository is private. As of 20 October 2026, the owner has accepted access and one invitation is pending. Committee access has not yet been granted.

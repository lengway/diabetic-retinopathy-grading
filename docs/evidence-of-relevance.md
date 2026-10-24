# 2. Evidence of Relevance and User Needs

Version 0.2, 20 October 2026. DIP-7. Desk research is complete; user validation remains incomplete.

## Established Evidence

The Teo et al. meta-analysis estimated DR prevalence at 22.27% among people with diabetes. This is a global estimate, not a Kazakhstan-specific estimate [L01]. A deployment study in Thailand evaluated screening workflows, including referrals caused by ungradable images [L08]. ACCESS increased screening completion in a particular paediatric clinic; applicability to Kazakhstan has not been established [L10]. Sources and limitations appear in the literature review.

These findings support the importance of the problem and examining the full workflow, including image quality and subsequent actions. They do not establish local demand for this prototype.

## Hypotheses to Validate

| ID | Hypothesis | Method | Implication |
|---|---|---|---|
| H1 | Clinicians benefit from grades 0-4 alongside a DR >= 2 flag | Discuss the mockup and three typical cases | Refine FR-03/04 |
| H2 | Grad-CAM helps inspect results | Compare discussion with/without a map | Refine FR-06; maps are not proof |
| H3 | Operators need explicit invalid-file rejection | Walk through an invalid upload | Refine FR-01/02 |
| H4 | The workflow fits a local clinic | Discuss cameras, workload, responsibility | Revisit users and scope |
| H5 | Users understand numerical confidence | Ask them to explain the value | Replace unclear labels |

## Plan for 3-5 Interviews

Plan an initial medical-adviser interview and 2-4 interviews with prospective users: an ophthalmologist, primary-care physician and screening operator. Identify repeat interviews explicitly; confirm with the supervisor whether they count. Dates, participants and a real-client agreement are not yet confirmed.

Questions cover current assessment, poor-quality images, referral information, consequential errors, positive/negative results, heatmap usefulness and permissible educational data. Do not collect identifiable patient information.

## Recording Method

For each completed interview, use docs/meetings/template.md to record the date, role, documentation consent, questions/answers, observations, confirmed needs and requirement changes. No interviews have been conducted yet.

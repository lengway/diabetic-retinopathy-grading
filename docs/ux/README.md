# 8. Key Workflow Mockups

DIP-10. 20 October 2026. Three schematic mockups, not a working ML service. Result values are illustrative; no model was run. No patient image or artificial Grad-CAM map has been inserted.

## Upload

![Upload](upload.png)

One file, 20 MiB limit and explicit research purpose. After selection, display the filename and replacement option; disable submission during analysis. Processing animation is a state of the future implementation.

## Result

![Result](result.png)

Show grade 0-4 separately from binary score. In the example, score=0.74 and illustrative threshold=0.50, so the flag is positive. The operational threshold will be selected on calibration only. Illustrative probabilities are [0.06, 0.20, 0.68, 0.04, 0.02], summing to 1. Implement map/original switching under FR-06. Confidence is model output, not the probability of being healthy. A negative flag does not exclude other diseases.

## Error

![Error](error.png)

A corrupt file receives no prediction; select another image. Implementation must additionally handle size limits, unavailable models and internal failures. A decoding error is not a clinical image-quality assessment.

## Mockup Verification

Scenarios map to UC-01/02/03 and FR-01..08. User validation has not occurred. Next, assess understanding of the binary flag, numerical confidence and limitations. Test keyboard access and 375 px responsiveness after implementation. Reproduce exports with scripts/build_visuals.py.

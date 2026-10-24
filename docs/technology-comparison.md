# 5. Technology Comparison

DIP-5. Version 0.2, 20 October 2026. Four decisions with three alternatives each. Suitability assessments are engineering judgements, not benchmarks. Dependency versions will be pinned after a trial run; training code is not yet available.

| Decision | Alternative | Strength | Constraint | Selection |
|---|---|---|---|---|
| ML framework | PyTorch | Eager execution, Apple MPS, Grad-CAM gradients [T1] | MPS operation support needs testing | Selected |
| ML framework | TensorFlow/Keras | High-level training, SavedModel [T2] | Different ecosystem; Mac testing | Reserve |
| ML framework | JAX | Autodiff and JIT [T3] | More custom training/serving code | Not selected |
| Backbone | EfficientNet-B0 | Compact CNN and scaling [L06] | Downscaling may remove small features | First baseline |
| Backbone | ResNet50 | Standard CNN and pretrained weights [T4] | Different parameter/speed trade-off | Controlled comparison |
| Backbone | RETFound | Retinal pretraining [L13] | Size and data-overlap checks | Later alternative |
| Interface/service | FastAPI + HTML/JS | Explicit API contract, OpenAPI [T5] | Separate UI implementation | Selected |
| Interface/service | Streamlit | Rapid research interface [T6] | Execution/session model | Demo reserve |
| Interface/service | Gradio | ML demo components [T7] | Less control under chosen API/UX approach | Reserve |
| Inference | PyTorch eager | Same weights/preprocessing; gradients | ML environment in service | First version |
| Inference | ONNX Runtime | Multiple device providers [T8] | Export/equivalence; separate Grad-CAM | After baseline |
| Inference | TorchScript | PyTorch execution artifact | Officially deprecated [T9] | Not selected |

## Decision Rationale

Priorities are single-author reproducibility, the available Mac, Grad-CAM and limited time. Start with PyTorch, EfficientNet-B0 and FastAPI without another inference runtime. Compare ResNet50 on the same data/resources. Adopt ONNX only after confirming maximum probability difference <= 1e-4 on a control set and a measurable time/memory improvement. ONNX requires a separate PyTorch Grad-CAM path with matching weights.

## Documentation Sources

[T1] PyTorch, MPS: https://docs.pytorch.org/docs/stable/notes/mps.html

[T2] TensorFlow, Keras: https://www.tensorflow.org/guide/keras

[T3] JAX: https://docs.jax.dev/en/latest/

[T4] Torchvision, ResNet50: https://docs.pytorch.org/vision/stable/models/generated/torchvision.models.resnet50.html

[T5] FastAPI: https://fastapi.tiangolo.com/features/

[T6] Streamlit execution model: https://docs.streamlit.io/develop/concepts/architecture

[T7] Gradio: https://www.gradio.app/guides/quickstart

[T8] ONNX Runtime: https://onnxruntime.ai/docs/execution-providers/

[T9] TorchScript: https://docs.pytorch.org/docs/stable/jit.html

Scientific references L06 and L13 appear in the literature review.

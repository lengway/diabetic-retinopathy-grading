# 5. Сравнение технологий

DIP-5. Версия 0.2, 20.10.2026. Четыре решения, по три альтернативы. Оценки соответствия проекту — инженерное суждение по выбранным ограничениям, не результаты бенчмарков. Версии зависимостей будут закреплены после пробного запуска; текущая версия кода обучения отсутствует.

| Решение | Альтернатива | Сильная сторона | Ограничение для проекта | Выбор |
|---|---|---|---|---|
| ML framework | PyTorch | eager-режим, MPS на Apple, доступ к градиентам для Grad-CAM [T1] | поддержку операций MPS нужно проверить | выбран |
| ML framework | TensorFlow/Keras | высокоуровневое обучение и SavedModel [T2] | другая экосистема и дополнительная проверка на локальном Mac | резерв |
| ML framework | JAX | автоматическое дифференцирование и JIT [T3] | больше самостоятельного кода обучения/сервинга | не выбран |
| Backbone | EfficientNet-B0 | компактный базовый CNN и масштабирование [L06] | мелкие признаки могут теряться при уменьшении | первый baseline |
| Backbone | ResNet50 | стандартный CNN baseline, готовые веса [T4] | другой баланс параметров и скорости | контролируемое сравнение |
| Backbone | RETFound | предобучение на retinal images [L13] | размер и проверка пересечений данных | дальнейшая альтернатива |
| Интерфейс/сервис | FastAPI + HTML/JS | явный API-контракт и схемы OpenAPI [T5] | интерфейс нужно реализовать отдельно | выбран |
| Интерфейс/сервис | Streamlit | быстрый исследовательский интерфейс [T6] | модель выполнения и сессии требуют учёта | резерв для демо |
| Интерфейс/сервис | Gradio | компоненты ML-демонстрации [T7] | меньше контроля итогового API/UX в рамках выбранного подхода | резерв |
| Инференс | PyTorch eager | одни веса и предобработка; градиенты доступны | зависимость сервиса от ML-окружения | первая версия |
| Инференс | ONNX Runtime | execution providers для разных устройств [T8] | экспорт и численная эквивалентность; Grad-CAM отдельно | после baseline |
| Инференс | TorchScript | артефакт для исполнения PyTorch | официально помечен deprecated [T9] | не выбран для новой реализации |

## Основание решения

Приоритеты: воспроизводимость одним автором; запуск baseline на доступном Mac; возможность вычислять Grad-CAM; ограниченное время. Сначала PyTorch + EfficientNet-B0 + FastAPI без экспорта весов в другой runtime. ResNet50 сравнивается на тех же данных и ресурсах. ONNX принимается только после проверки расхождения вероятностей (максимум 1e-4 на контрольной выборке) и измеримого выигрыша по времени/памяти. Карта Grad-CAM при ONNX требует отдельного PyTorch-пути с совпадающими весами; это дополнительная сложность.

## Источники документации

[T1] PyTorch, MPS backend: https://docs.pytorch.org/docs/stable/notes/mps.html

[T2] TensorFlow, Keras: https://www.tensorflow.org/guide/keras

[T3] JAX, documentation: https://docs.jax.dev/en/latest/

[T4] Torchvision, ResNet50: https://docs.pytorch.org/vision/stable/models/generated/torchvision.models.resnet50.html

[T5] FastAPI, features: https://fastapi.tiangolo.com/features/

[T6] Streamlit, execution model: https://docs.streamlit.io/develop/concepts/architecture

[T7] Gradio, quickstart: https://www.gradio.app/guides/quickstart

[T8] ONNX Runtime, execution providers: https://onnxruntime.ai/docs/execution-providers/

[T9] PyTorch, TorchScript: https://docs.pytorch.org/docs/stable/jit.html

Научные источники L06 и L13 — в обзоре литературы.

# 3. Обзор литературы

DIP-3. Версия 0.2, 20.10.2026. Обзор предметной области и подходов; собственных экспериментальных результатов нет.

## Метод отбора и границы

Источники проверены 20.10.2026 по страницам PubMed, издателей, PMLR и arXiv. Поисковые направления: diabetic retinopathy grading, external validation, retinal foundation model, calibration, explainability, prospective screening. Включены 15 научных публикаций; 8 опубликованы в 2022–2025 годах и заведомо входят в последние пять лет на дату отчёта. Семь более ранних работ оставлены как основания шкалы, методов и данных. Источники отобраны целевым поиском, обзор не является систематическим метаанализом.

Анализ основан на доступных аннотациях, страницах статей и описаниях методов. Полный текст всех 15 работ не заявляется прочитанным; воспроизведение экспериментов не выполнялось. Ссылки ведут к первичным публикациям или их библиографическим записям. Результаты авторов не приписываются данному проекту.

## Таблица анализа

| ID / год | Работа и подход | Что используется в проекте | Ограничение переноса |
|---|---|---|---|
| L01 / 2021 | Teo et al.; метаанализ распространённости | обоснование актуальности | глобальная оценка не равна местной потребности |
| L02 / 2003 | Wilkinson et al.; консенсусная шкала ICDR | определение пяти упорядоченных стадий | отдельная шкала макулярного отёка не входит в DR 0–4 |
| L03 / 2016 | Gulshan et al.; DL для выявления referable DR | baseline задачи и внешняя проверка | бинарное выявление не доказывает качество пяти классов |
| L04 / 2017 | Selvaraju et al.; Grad-CAM | визуализация вклада областей CNN | карта не является разметкой поражений или причинным доказательством |
| L05 / 2017 | Guo et al.; temperature scaling | калибровка на отдельном наборе | работа не гарантирует перенос калибровки на новую камеру |
| L06 / 2019 | Tan, Le; EfficientNet | компактный CNN baseline | эффективность на ImageNet не гарантирует качество ДР |
| L07 / 2018 | Porwal et al.; IDRiD | независимый источник для проверки | различать подзадачи и доступность меток |
| L08 / 2022 | Ruamviboonsuk et al.; проспективный скрининг в Таиланде | оценивать реальный процесс и отказы | иной контекст, оборудование и клинический протокол |
| L09 / 2022 | Automated multidimensional platform; многоцентровая ретроспективная оценка | учитывать пригодность и ограничения снимков | ретроспективное исследование не заменяет внедрение |
| L10 / 2024 | Wolf et al.; ACCESS, рандомизированное исследование | оценивать завершённость обследования, не только AUC | один педиатрический центр; не подтверждает потребность местной клиники |
| L11 / 2024 | Autonomous AI ... underserved populations; наблюдение внедрения | учитывать доступ и различия групп | наблюдательная связь не доказывает причинность |
| L12 / 2024 | Dai et al.; DeepDR Plus, прогноз прогрессирования | пример внешних когорт и иной конечной точки | прогноз времени до ухудшения выходит за scope |
| L13 / 2023 | Zhou et al.; RETFound, самообучение | альтернатива обучению CNN, эффективность разметки | ресурсы и происхождение pretraining могут усложнить честный test |
| L14 / 2025 | A data-efficient strategy ...; RETFound-DE | сравнение data-efficient подходов | генерация синтетических данных не входит в проект |
| L15 / 2025 | Engelmann, Bernabeu; RETFound-Green | учитывать стоимость и компактность foundation models | заявленные выигрыши проверены авторами на их протоколе |

## Синтез

Клиническая шкала [L02] задаёт порядковую структуру ответа, но задачи выявления mtmDR и классификации пяти стадий различаются. Поэтому проект сообщает QWK и ошибки по всем классам отдельно от бинарных AUROC и sensitivity/specificity. В отличие от клинических скрининговых систем, текущий прототип не оценивает макулярный отёк и не даёт полного решения о направлении.

Работы внедрения [L08–L11] показывают значимость пользовательского процесса, пригодности снимка и доведения результата до дальнейшего обследования. Их результаты служат основанием для исследования сценария, но не заменяют 3–5 бесед с реальными пользователями проекта.

RETFound и более экономичные продолжения [L13–L15] расширяют набор альтернатив за пределы CNN. Для ограниченного времени выбран воспроизводимый компактный baseline [L06], а foundation models остаются сравнительным направлением. Смена модели оправдана только измеренным улучшением на одном протоколе без утечки pretraining/test.

Модель может быть уверенной и ошибаться: калибровка [L05] оценивается отдельно от классификации и повторно на внешнем наборе. Grad-CAM [L04] применяется для анализа ошибок и обсуждения с консультантом; клиническая достоверность карты не предполагается.

## Исследовательские вопросы

RQ1: как меняется QWK и бинарное выявление DR >= 2 при переходе с внутренней выборки на независимый источник? RQ2: улучшает ли temperature scaling NLL/ECE и сохраняется ли эффект на внешних данных? RQ3: какие типы ошибок и артефактов выявляются при анализе Grad-CAM? Эти вопросы формируют проверяемый вклад учебного проекта без заявления о новой клинической системе.

## Библиография

[L01] Teo Z.L. et al. Global Prevalence of Diabetic Retinopathy and Projection of Burden through 2045: Systematic Review and Meta-analysis. Ophthalmology, 2021, 128(11):1580–1591. https://pubmed.ncbi.nlm.nih.gov/33940045/

[L02] Wilkinson C.P. et al. Proposed international clinical diabetic retinopathy and diabetic macular edema disease severity scales. Ophthalmology, 2003, 110(9):1677–1682. DOI 10.1016/S0161-6420(03)00475-5. https://pubmed.ncbi.nlm.nih.gov/13129861/

[L03] Gulshan V. et al. Development and Validation of a Deep Learning Algorithm for Detection of Diabetic Retinopathy in Retinal Fundus Photographs. JAMA, 2016, 316(22):2402–2410. DOI 10.1001/jama.2016.17216. https://pubmed.ncbi.nlm.nih.gov/27898976/

[L04] Selvaraju R.R. et al. Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization. ICCV, 2017; препринт 2016. https://arxiv.org/abs/1610.02391

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

## Данные, метрики и результаты публикаций

Это сведения публикаций, не результаты проекта. Где численные значения не извлечены из проверенного описания, они не восстанавливаются по памяти.

| ID | Данные / дизайн | Оценка | Результат и предел вывода |
|---|---|---|---|
| L01 | метаанализ исследований людей с диабетом | распространённость и 95% CI | ДР 22,27%; нет локальной оценки спроса |
| L02 | международный экспертный консенсус | согласованность классификации | предложена шкала пяти стадий; это не ML-бенчмарк |
| L03 | размеченные fundus-фотографии, EyePACS-1 и Messidor-2 для проверки | чувствительность, специфичность, AUC | DL выявляет referable DR; это бинарная задача |
| L04 | задачи распознавания изображений | локализация и качественные визуализации | градиентная карта объясняет области внимания CNN; клинический результат не оценивался |
| L05 | классификация изображений и документов | калибровка, в том числе ECE | temperature scaling улучшает калибровку на исследованных задачах |
| L06 | ImageNet и перенос на другие задачи | accuracy, параметры и вычислительная эффективность | совместное масштабирование глубины, ширины и разрешения эффективно в протоколе авторов |
| L07 | снимки IDRiD с разметкой градации и подзадач | описание набора, разметки и задач | предоставлен набор для исследований; не результат нашей модели |
| L08 | 7651 подходящих участников национального скрининга Таиланда | accuracy, sensitivity, specificity для vision-threatening DR | исследована проспективная работа в потоке; конечная точка шире DR >= 2 |
| L09 | многоцентровый ретроспективный набор, пять классификаторов | accuracy, F1, sensitivity, specificity, AUROC, AUPRC | оцениваются качество и разные компоненты скрининга; прямого сравнения с нашим прототипом нет |
| L10 | ACCESS: 81 человек в интервенции и 83 в контроле | завершённость обследования в течение 6 месяцев | 100% против 22% в конкретном исследовании; это не accuracy модели |
| L11 | внедрение в интегрированной системе здравоохранения, >17000 взрослых с диабетом | соблюдение обследований и различия групп | использование AI ассоциировано с улучшением доступности; возможны смешивающие факторы |
| L12 | предобучение и продольные когорты для прогноза прогрессирования | C-index и integrated Brier score | прогнозируется время до ухудшения; не текущая стадия |
| L13 | самообучение примерно на 1,6 млн CFP/OCT и downstream-задачи | downstream-качество, label efficiency и внешняя проверка | предобученные представления полезны для ряда задач; не гарантия выигрыша на нашем split |
| L14 | синтетические и реальные fundus-данные, девять публичных наборов | качество downstream-задач и потребность в разметке | data-efficient предобучение уменьшает потребность в реальных данных в исследовании |
| L15 | 75000 публичных снимков для предобучения и внешние downstream-наборы | качество, ресурсы обучения/инференса | компактный RETFound-Green снижает ресурсы в протоколе авторов; наш замер отсутствует |

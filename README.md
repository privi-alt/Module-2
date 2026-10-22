# BME 2315 - Module 2

### Team Members

- Prithvi Sachdeva
- Cecilia Duro-Emanuel

## Measuring Disease Progression in FSHD

This repository contains the code, data analysis, and project files for Module 2 of BME 2315: Computational Biomedical Engineering.

### Project Goal

The goal of this project is to analyze natural-history data from patients with facioscapulohumeral muscular dystrophy (FSHD) and evaluate candidate biomarkers and clinical outcome measures for use in an early-stage clinical trial.

The project focuses on identifying measurements that are sensitive to disease progression while also considering consistency, feasibility, and clinical relevance.

Our analysis focuses particularly on MRI fat fraction and quantitative STIR as potential imaging biomarkers for monitoring FSHD progression.

### Disease Background

Symptoms: Facioscapulohumeral muscular dystrophy (FSHD) is a progressive genetic disorder where severity and progression varies depending on the individual. Common symptoms include weaknesses in the face, shoulder, hip, lower leg and upper arm. Facial weaknesses appear early on, making movements like smiling, whistling and closing the eyes difficult. Weakness around the shoulder blades is an indicator of FSHD, resulting in protruded shoulder blades and causing difficulty while performing regular activities with the shoulders. Other muscular areas can affect balance, mobility due to foot drop, and seating, creating an uncomfortable quality of life for individuals living with FSHD. Roughly 20% of people living with FSHD use a wheelchair to help with mobility. Other side effects that accompany FSHD conditions include respiratory complications, blindness, and dysphagia. While symptoms vary widely among individuals, most develop symptoms from their teens, and currently there is no established cure for FSHD (Muscular Dystrophy Association, n.d.-c).

Standard-of-care treatments: Current standard-of-care treatments for FSHD focus on managing symptoms and therapy due to no effective developed medication. Physical therapy and pain management through anti-inflammatory drugs are available to help improve mobility, muscular functions and reduce pain, however results vary depending on the stage of the disease. Scapulothoracic fusion surgery can benefit patients by improving shoulder-related movements. Since conditions vary between individuals, respiratory, optical, and hearing functions are carefully monitored as certain FSHD conditions may impact pulmonary, retinal vascular, and hearing function (Aguirre et al., 2023).

Disease progression and prognosis: FSHD progresses slowly in individuals, often with symptoms appearing from the early twenties and further developing over time. The rate and severity of FSHD varies between individuals. Weakness and loss of muscle mass can occur over time and affect additional muscle groups. In severe cases where individuals are unable to maintain mobility due to muscle weakness, some patients eventually require a wheelchair (Muscular Dystrophy Association, n.d.-a).

Biological mechanisms: FSHD is associated with abnormal expression of the DUX4 gene. In FSHD1, changes involving the D4Z4 repeat region on chromosome 4q contribute to inappropriate DUX4 expression in skeletal muscle. DUX4 activity contributes to muscle-cell dysfunction and degeneration. Potential therapies aim to reduce DUX4 expression or block its harmful effects. Researchers continue investigating biomarkers that can reliably track FSHD disease activity and progression (Banerji et al., 2023; Hamel & Tawil, 2018).

Clinical trials and next-generation therapies: Current FSHD clinical trials are evaluating therapies designed to target disease mechanisms such as abnormal DUX4 expression. Delpacibart braxlosiran (del-brax) is an investigational RNA-targeting therapy designed to reduce DUX4 expression. Biomarker results have shown changes in measurements related to DUX4 activity and muscle damage, while continued research is needed to determine whether these biological changes lead to meaningful improvements in function and quality of life (FSHD Society, 2026).

Prevalence and Incidence: Estimates of FSHD prevalence vary between populations. Available estimates indicate that FSHD is a relatively common inherited muscular dystrophy, although mild or undiagnosed cases can make its true prevalence difficult to determine (FSHD Canada, n.d.; Statland & Tawil, 2016).

Diagnosis: Diagnosis of FSHD includes clinical evaluation by a neurologist or neuromuscular specialist and genetic testing. Characteristic patterns of muscle weakness, particularly involving the face and shoulder girdle, can suggest FSHD. Genetic testing can help confirm the diagnosis by examining the D4Z4 repeat region on chromosome 4q. Additional testing may be used when the diagnosis is unclear (Muscular Dystrophy Association, n.d.-b).

### Module 2 Analysis

This project includes:

- Exploration of the FSHD clinical dataset
- Analysis of measurements across baseline, Year 1, and Year 2
- MRI analysis of the tibialis anterior muscle
- Water and fat MRI image processing
- Tibialis anterior segmentation using a binary muscle mask
- Calculation of MRI fat fraction
- Comparison of MRI measurements across locations and time points
- Linear interpolation of fat fraction between sampled muscle locations
- Comparison of MRI fat fraction and quantitative STIR
- Standardized response mean calculations
- Paired statistical testing of baseline-to-Year-1 changes
- Evaluation of candidate exploratory clinical-trial endpoints

### Dataset and MRI Analysis

The primary clinical dataset contains 34 participants with FSHD who underwent assessments including lower-extremity MRI, functional testing, and bilateral tibialis anterior muscle biopsies. Participants were evaluated at baseline, Year 1, and Year 2. Because the visits were not conducted at exactly the same time for every participant, actual visit timing was recorded using `lag_months_baseline`, `lag_months_y1`, and `lag_months_y2`.

The dataset contains variables including subject ID, sex, age, D4Z4 repeat length, DUX4-related biomarkers, MRI fat fraction, quantitative STIR measurements, dorsiflexion strength, functional tests, and clinical severity scores.

A separate MRI example dataset contained one participant, UW_0020, measured at TP1 and TP2. Eight cross-sectional locations along the tibialis anterior were sampled at each time point, resulting in 16 MRI sections. Each section included a water image, fat image, and binary tibialis anterior segmentation mask.

MRI fat fraction was calculated for each valid pixel as:

**Fat Fraction (%) = 100 × Fat / (Water + Fat)**

The segmentation mask was used to isolate the tibialis anterior so that fat fraction could be summarized specifically within the muscle. Mean fat fraction was calculated at each sampled location and compared between TP1 and TP2.

Linear interpolation was then used to estimate fat fraction at locations between the directly sampled MRI sections. These interpolated values were estimates rather than new MRI measurements and were only calculated within the range of the observed data.

### Biomarker Comparison

MRI fat fraction and quantitative STIR were compared from baseline to Year 1. Nineteen participants had complete measurements for both biomarkers.

Mean MRI fat fraction increased by approximately 1.33 percentage points from baseline to Year 1. The standardized response mean (SRM) for fat fraction was approximately 0.87, indicating a relatively consistent change compared with the variability between participants.

Quantitative STIR showed substantially greater variability and little average directional change. Its SRM was approximately -0.009.

Paired t-tests were also used to evaluate baseline-to-Year-1 changes. MRI fat fraction showed a statistically significant change (p ≈ 0.0014), while quantitative STIR did not show a statistically significant change (p ≈ 0.97).

Based on this analysis, MRI fat fraction appeared to be the more consistent of the two imaging biomarkers for tracking FSHD progression in this dataset.

### Conclusions

The results suggest that MRI fat fraction may be useful as an exploratory biomarker for FSHD clinical trials. Fat fraction demonstrated measurable changes across MRI visits and showed a more consistent baseline-to-Year-1 pattern than quantitative STIR.

However, additional evidence would be needed before using MRI fat fraction as a clinical-trial endpoint. Future studies should include larger patient groups, additional follow-up visits, and comparisons with functional outcomes such as muscle strength, mobility, and quality of life.

MRI also has limitations related to cost and accessibility. For this reason, imaging biomarkers should be considered together with measurements that capture changes that are meaningful to patients.

### Future Limitations and Work

A significant limitation of this project was the relatively small sample size. Although the full dataset contained 34 participants, only 19 participants had complete baseline and Year 1 measurements for both MRI fat fraction and STIR. This limits the precision and generalizability of the biomarker comparison because FSHD severity and progression vary substantially between individuals.

Other possible sources of uncertainty include MRI measurement variability, tibialis anterior segmentation, missing measurements, and assumptions made during interpolation.

With additional time and data, future analysis could include more participants, additional follow-up visits, other muscles, and additional biomarkers such as DUX4-related transcriptomic measurements. MRI fat fraction could also be compared more directly with muscle strength and functional outcomes.

Future work could also investigate whether MRI fat fraction is sensitive to treatment response in clinical trials. Combining imaging, molecular, strength, functional, and patient-relevant measurements may provide a more complete picture of FSHD progression than relying on a single outcome measure.

### AI Usage Statement

We used ChatGPT during development of this project to troubleshoot Python code, explain coding

# BME 2315 - Module 2

### Team Members

- Prithvi Sachdeva
- Cecilia

## Measuring Disease Progression in FSHD

This repository contains the code, data analysis, and project files for Module 2 of BME 2315: Computational Biomedical Engineering.

### Project Goal
The goal of this project is to analyze natural-history data from patients with facioscapulohumeral muscular dystrophy (FSHD) and evaluate candidate biomarkers and clinical outcome measures for use in an early-stage clinical trial.

The project focuses on identifying measurements that are sensitive to disease progression while also considering consistency, feasibility, and clinical relevance.

### Disease Background

Symptoms:
Facioscapulohumeral muscular dystrophy (FSHD) is a progressive genetic disorder where severity and progression varies depending on the individual. Common symptoms include weaknesses in the face, shoulder, hip, lower leg and upper arm. Facial weaknesses appear early on, making movements like smiling, whistling and closing the eyes difficult. Weakness around the shoulder blades is an indicator of FSHD, resulting in protruded shoulder blades and causing difficulty while performing regular activities with the shoulders. Other muscular areas can affect balance, mobility due to foot drop, and seating, creating an uncomfortable quality of life for individuals living with FSHD. Roughly 20% of people living with FSHD use a wheelchair to help with mobility. Other side effects that accompany FSHD conditions include respiratory complications, blindness, and dysphagia. While symptoms vary widely among individuals, most develop symptoms from their teens, and currently there is no established cure for FSHD.
 
https://www.mda.org/disease/facioscapulohumeral-muscular-dystrophy/signs-and-symptoms

Standard-of-care-treatments:
Current standard-of-care treatments for FSHD focus on managing symptoms and therapy due to no effective developed medication. Physical therapy and pain management through anti-inflammatory drugs are available to help improve mobility, muscular functions and reduce pain, however results vary depending on the stage of the disease. Scapulothoracic fusion surgery can benefit patients by improving shoulder related movements. Since conditions vary between individuals, respiratory, opticial, and hearing functions are carefully monitored as certain FSHD conditions may impact pulmonary, retinal vascular diseases, and hearing complications. While clinical trials have identified the pathology and etiology of the disease, the effective treatment remains unknown.

https://pmc.ncbi.nlm.nih.gov/articles/PMC10316996/

Disease progression and prognosis:
FSHD progresses slowly in individuals, often with symptoms appearing from early twenties and further developing over time. The rate and severity of FSHD is dependent on the individual and varies. As researched above, the progression of FSHD is shown within the severity of symptoms, however these changes do not affect life expectancy and a majority of patients maintain a normal lifespan. In patients with FSHD, weakness and loss of muscle mass occurs over time, commonly affecting facial muscles first and later spreading to other muscle groups causing increased axillary fat and arm muscle wasting. In severe cases where individuals are unable to maintain mobility due to muscle weakness, 20% will eventually require a wheelchair. 

https://www.mda.org/disease/facioscapulohumeral-muscular-dystrophy

Biological mechanisms:
FSHD is the result of a regulatory mutation caused by the deletion of D4Z4 repeats on chromosome 4q. This deletion causes the transcription and overexpression of the DUX4 gene which is highly toxic. The overactivation of DUX4 instead of suppression in skeletal muscle, causes atrophy and protein degradation, which leads to irregular muscle function.This mechanism is hereditary, and is classified as an autosomal dominant trait. Potential therapies aim to reduce DUX4 expression or block its harmful effects on skeletal muscle cells. DUX4 target gene biomarkers in FSHD affected muscle could indicate levels of limb fat fraction. However, researchers continue investigating dependable biomarkers to monitor FSDH disease and optimal treatments.

https://pmc.ncbi.nlm.nih.gov/articles/PMC6277282/
https://pmc.ncbi.nlm.nih.gov/articles/PMC10507741/

Clinical trials and next generation therapies:
Clinical trials for FSHD are testing therapies that target causes for FSHD. Currently a clinical study on phase three has been reviewing the impact of the drug Del-brax, an investigational RNA therapy designed to reduce DUX4 expression, has shown positive biomarker results, highlighting a decrease in KHDC1L, a biomarker linked the DUX4 overexpression, and a decrease in creatine kinase, a biomarker resulting in in muscle damage. While treatments have not been developed, these results indicate potential areas of treatment development. Future trials and testing will be required to find treatments for FSHD. Current and future testing should continue to identify reliable biomarkers and determine whether these therapies improve quality of life and mobility. 

https://www.fshdsociety.org/2026/06/11/novartis-announcement/
https://www.fshdsociety.org/research-and-clinical-care/current-trials-and-studies/

Prevalence and Incidence:
The prevalence of FSHD in individuals in the United States is 1 in 15,000, and worldwide 2.03 to 6.8 per 100,000 individuals. The incidence of FSHD worldwide is 1 in 14,000 however the true estimate may be lower.

https://fshd.ca/overview/incidence-of-fshd/
https://pmc.ncbi.nlm.nih.gov/articles/PMC5898965/

Diagnosis:
Diagnosis of FSHD is done through an evaluation by a neurologist or specialist in neuromuscular disorders. A patient is encouraged to seek testing after noticeable changes in their muscle strength or function. Identifiable traits are seen through muscle weakness in the face and shoulder blades. Testing is primarily completed through genetic testing to determine if the D4Z4 repeats have been shortened on chromosome 4q. In most cases. Genetic testing is able to confirm an FSHD diagnosis, however if inconclusive, blood tests, electromyography, or a muscle biopsy may be included in testing.

https://www.mda.org/disease/facioscapulohumeral-muscular-dystrophy/diagnosis


### Module 2 Analysis
This project includes:

- Exploration of the FSHD clinical dataset
- Analysis of longitudinal measurements across baseline, Year 1, and Year 2
- MRI analysis of the tibialis anterior muscle
- Water and fat MRI image processing
- Tibialis anterior segmentation using a muscle mask
- Calculation of MRI fat fraction
- Comparison of measurements across time points
- Interpolation of measurements collected at uneven visit times
- Statistical analysis of disease progression
- Evaluation of candidate exploratory clinical-trial endpoints

### MRI Dataset
The data set was based on a study cohort of 34 participants with FSHD who underwent functional studies, lower extremity MRI and bilateral biopsy of the tibialis anterior (TA) muscles. Participants were assessed at two timepoints, year one and two. Fat infiltration was calculated for each pixel by dividing the sum of the fat series intensity and water series signal intensities. AI- based segmentation was reviewed and evaluated by researchers for continued consistency of segmentation and to provide a final three dimensional label. Fiducial markers placed on the middle portion of the TA muscle were used to identify the muscle biopsy site. Fat infiltration was measured along the length of the muscle and expressed as a percentage. The provided csv data file features measurements such as DUX4 gene signatures, sex, age, dorsiflection strength, and clinical severity scores. This data source was from Wong et al. (2024).

### AI Usage Statement
We utilized Chat GPT and (other?) tools to troubleshoot code during the development of this project and to help refine the clarity and wording of our written explanations. We used AI to determine the error that was occurring in our code and how to fix it. The AI tools also helped with some formatting and organizing of the code for better readability and maintainability.

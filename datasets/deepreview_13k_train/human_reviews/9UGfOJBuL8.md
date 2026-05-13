# Conditional Diffusion with Ordinal Regression: Longitudinal Data Generation for Neurodegenerative Disease Studies

- Decision: Accept
- Scores: 8, 6, 8

## Abstract
Modeling the progression of neurodegenerative diseases such as Alzheimer’s disease (AD) is crucial for early detection and prevention given their irreversible nature. However, the scarcity of longitudinal data and complex disease dynamics make the analysis highly challenging. Moreover, longitudinal samples often contain irregular and large intervals between subject visits, which underscore the necessity for advanced data generation techniques that can accurately simulate disease progression over time. In this regime, we propose a novel conditional generative model for synthesizing longitudinal sequences and present its application to neurodegenerative disease data generation conditioned on multiple time-dependent ordinal factors, such as age and disease severity. Our method sequentially generates continuous data by bridging gaps between sparse data points with a diffusion model, ensuring a realistic representation of disease progression. The synthetic data are curated to integrate both cohort-level and individual-specific characteristics, where the cohort-level representations are modeled with an ordinal regression to capture longitudinally monotonic behavior. Extensive experiments on four AD biomarkers validate the superiority of our method over nine baseline approaches, highlighting its potential to be applied to a variety of longitudinal data generation.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a novel conditional generative model for synthesizing longitudinal sequences to study neurodegenerative diseases such as Alzheimer’s disease. The method uses ordinal regression and a diffusion model to generate realistic disease progression imaging data.

### Strengths
1. Combing the cohort-level trend and subject-level trend for longitudinal data generation. 
2. Extensive validation on four Alzheimer's Disease biomarkers demonstrates the model's superiority over nine baseline approaches.

### Weaknesses
1. The paper lacks a comprehensive theoretical justification for the proposed method. While the method is innovative, a deeper theoretical comparison with existing models could strengthen the argument for its necessity and effectiveness. Specifically, the paper does not adequately address how the proposed diffusion model with ordinal regression theoretically improves upon existing generative models for longitudinal data, particularly in handling the complex temporal dependencies and irregular sampling intervals inherent in such data.
2. The description of the methodology, particularly the integration of cohort-level and subject-level samples, is somewhat convoluted. The paper could benefit from clearer explanations and more detailed algorithmic steps to enhance reproducibility. The precise mechanism by which the dual-sampling approach balances individual-specific features and general trends is not sufficiently detailed, making it difficult to understand the practical implications of this design choice.
3. The paper does not provide a thorough statistical analysis to support these claims. The lack of confidence intervals or significance testing weakens the robustness of the reported findings. It is unclear how the reported means and standard deviations were calculated, and whether these metrics are sufficient to demonstrate the model's generalizability across different datasets and conditions.
4. The discussion section is relatively weak in terms of interpreting the results and their implications. The paper does not adequately address the potential limitations of the proposed method or suggest directions for future research, which are crucial for a comprehensive understanding of the study’s impact. Specifically, there is a lack of discussion regarding scenarios where the proposed method might underperform, such as in cases with non-monotonic disease progression or with datasets exhibiting significant population heterogeneity.

### Questions
1. How does the proposed method theoretically ensure the accurate representation of disease progression, especially considering the complex dynamics and irregular intervals in longitudinal data?
2. How does the proposed method theoretically improve upon existing generative models for longitudinal data? Are there any theoretical limitations or assumptions that need further clarification?
3. The paper introduces a dual-sampling approach combining cohort-level and subject-level samples. How does this method compare to other state-of-the-art techniques in terms of capturing individual-specific features and general trends? Are there any potential biases introduced by this approach?
4. The experiments are conducted on four AD biomarkers from MRI and PET images. How representative are these biomarkers and datasets of the broader neurodegenerative disease population? Are there any limitations in the experimental design that could affect the generalizability of the results?
5. The paper claims superiority over nine baseline approaches. How robust are these results across different metrics and datasets? Are there any specific scenarios or conditions under which the proposed method might underperform or fail?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a conditional generative model for synthesizing longitudinal sequences. 
It first uses ordinal regression and kernel density estimation to model the conditional PDF and then interpolate gaps between consecutive observations. 
Two diffusion models are then trained to model baseline data and changes in follow-up samples. 
These diffusion models generate disease progression data by sequentially sampling.

### Strengths
The design of the proposed model's structure design is innovative, partsuch as the combination of two diffusion models and the use of both cohort and subject-level interpolation for training. 

This paper provides clear comparisons to baseline models across multiple metrics and good visualizations.

### Weaknesses
Some abnormal results are not well discussed or explained. 
For example, in Table 1, the variance in DDPM's performance is very high compared to other methods. 
Since DDPM is one of only two diffusion-based comparison methods, it would be helpful to provide an explanation for this abnormal performance.

The authors do not mention how to deploy the model. For example, how to use the trained model to generate new data. 
If my understanding of the generative process is correct, we only need to use these two diffusion models with random noise as the input when generating new data.
There is no option to allow the two diffusion models to generate samples conditioned on specific ages and disease severity, 
e.g., we can't use age as an input for these diffusion models when generating, 
although the authors claim that this model can generate data conditioned on these factors.

Some important technical details are also missing. Please refer to the questions below

RDM is designed to geneate the baseline sample $x_1$. However, during training, the authors use all the samples $x_t$ (t = 1, .., t) as independent cross-sectional data.
The justification for using such setting is not presented in the paper. 
For example, why not use only $x_1$ to train the RDM? 
Will this setting cause the RDM to be biased as some longitudinal samples have longer records or are recorded more frequently

Acoording to Table 3, the choice of hyperparameter $\lambda$ significantly impacts the performance of the proposed method. 
Howerver, how to select $\lambda$ is unclear, for example, which dataset and what metric do the author use to choose $\lambda$.
The author used 80% of the whole data for training and the rest 20% for testing for all experiments,
and it seems there is no validation dataset to optimize $\lambda$.
Therefore, the results shown in Table 3 is less convincing to me since they are propbably derived from either training or test set, 
and the results in Table 1 and 2 are also less convincing since we may not able to get the best $\lambda$ in practice.

The training strategies for the generative model are somewhat unclear to me. For example do the authors train RDM and TDM seperatedly or jointly?
$D$ seems to be another important hyperparameter, but how the authors chose $D$ is also unclear.

### Questions
RDM is designed to geneate the baseline sample $x_1$. However, during training, the authors use all the samples $x_t$ (t = 1, .., t) as independent cross-sectional data.
The justification for using such setting is not presented in the paper. 
For example, why not use only $x_1$ to train the RDM? 
Will this setting cause the RDM to be biased as some longitudinal samples have longer records or are recorded more frequently

Acoording to Table 3, the choice of hyperparameter $\lambda$ significantly impacts the performance of the proposed method. 
Howerver, how to select $\lambda$ is unclear, for example, which dataset and what metric do the author use to choose $\lambda$.
The author used 80% of the whole data for training and the rest 20% for testing for all experiments,
and it seems there is no validation dataset to optimize $\lambda$.
Therefore, the results shown in Table 3 is less convincing to me since they are propbably derived from either training or test set, 
and the results in Table 1 and 2 are also less convincing since we may not able to get the best $\lambda$ in practice.


The training strategies for the generative model are somewhat unclear to me. For example do the authors train RDM and TDM seperatedly or jointly?
$D$ seems to be another important hyperparameter, but how the authors chose $D$ is also unclear.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents ConDOR, a novel conditional diffusion model for generating longitudinal neurodegeneration data with ordinal disease progression factors. The model's architecture integrates both cohort-level and subject-level characteristics through a dual-component approach. At the cohort level, it employs Bayes' Theorem combining an ordinal regression model (capturing disease stage relationships) with a kernel-based conditional distribution. For data generation, ConDOR utilizes two diffusion models: a Regional Diffusion Model (RDM) for generating baseline measurements across brain regions, and a Temporal Diffusion Model (TDM) for generating subsequent longitudinal data. The model also incorporates a domain conditioning mechanism to integrate data from multiple sources. The authors evaluate ConDOR on multiple biomarkers (Amyloid, Cortical Thickness, and Fluorodeoxyglucose) from two prominent neurodegenerative disease datasets (ADNI and OASIS), comparing against nine baseline methods including GANs, VAEs, and other diffusion-based approaches.

### Strengths
1. The proposed model captures both spatial and temporal features through a combination of a Regional Diffusion Model and a Temporal Diffusion Model.
2. This new generative model addresses challenges associated with sparse, irregular, and widely spaced intervals in medical data.
3. The model strikes a balance between cohort-level and individual-level fitting, capturing generalized population trends while accommodating individual variability.
4. It introduces a novel integration of ordinal regression with diffusion models.
5. The experiments are comprehensive, with comparisons to nine baseline models, including GANs, VAEs, and other diffusion-based models, evaluated across three metrics. Implementation time is also compared.
6. The model is extended to a multi-domain setting, enhancing its generalizability and applicability to different data sources.

### Weaknesses
1. The ordinal regression model might oversimplify the disease progression process. Additionally, the temporal diffusion relies on linear interpolation for temporal transitions, which may not accurately capture realistic disease dynamics. Specifically, the ordinal regression assumes a monotonic progression through discrete disease stages, which may not reflect the complex, non-linear trajectories of neurodegeneration. The linear interpolation between time points for both the data and the disease labels could smooth over critical abrupt changes or non-linear patterns that are often observed in longitudinal studies, potentially leading to unrealistic synthetic data.
2. There is a lack of comparison with traditional longitudinal baseline models commonly used in medical literature. The current comparison focuses on generative models, but it would be beneficial to see how ConDOR performs against established statistical methods for longitudinal data analysis, such as mixed-effects models or growth curve models, which are specifically designed to model temporal dependencies in medical data.
3. The model evaluation has not been clearly described. Did the authors split subjects into training and test sets, keeping all observations from each subject together, or did they split individual observations, potentially placing different time points from the same subject in both training and test sets? This distinction is crucial because splitting observations could lead to information leakage, where the model learns to predict future time points based on past time points from the same subject in the training set, rather than generalizing to unseen subjects. This would inflate performance metrics and not accurately reflect the model's ability to generate realistic longitudinal data.
4. The reproducibility of this work is not guaranteed, as the code has not yet been made available.

### Questions
1. The model evaluation lacks clarity regarding whether the authors performed a subject-level or observation-level split. Specifically, did they keep all observations from each subject together, or did they split individual observations, potentially including different time points from the same subject in both training and test sets? It would be valuable to see how well the model predicts follow-up scans based on data from earlier time points, given that the Temporal Diffusion Model is a novel component. Additionally, for baseline models like DDPM that lack a temporal component, it would be interesting to understand how the authors utilize these models to generate follow-up scans over time.
2. The Temporal Diffusion Model uses linear interpolation to model progression in age and labels, which may not be ideal, as transitions between disease states are often abrupt or follow complex patterns. Furthermore, it would be beneficial to see theoretical proof that such linear interpolation preserves the properties of diffusion models.
3. Including some directions for future work in the conclusion would be beneficial for the research community.

### Soundness
3

### Presentation
2

### Contribution
3

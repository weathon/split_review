# Uncertainty-Aware PPG-2-ECG for Enhanced Cardiovascular Diagnosis using Diffusion Models

- Decision: Reject
- Scores: 6, 6, 5

## Abstract
Analyzing the cardiovascular system condition via Electrocardiography (ECG) is a common and highly effective approach, and it has been practiced and perfected over many decades.
    ECG sensing is non-invasive and relatively easy to acquire, and yet it is still cumbersome for holter monitoring tests that may span over hours and even days.
    A possible alternative in this context is Photoplethysmography (PPG): An optically-based signal that measures blood volume fluctuations, as typically sensed by conventional ``wearable devices''.
    While PPG presents clear advantages in acquisition, convenience, and cost-effectiveness, ECG provides more comprehensive information, allowing for a more precise detection of heart conditions.
    This implies that a conversion from PPG to ECG, as recently discussed in the literature, inherently involves an unavoidable level of uncertainty.
    In this paper we introduce a novel methodology for addressing the PPG-2-ECG conversion, and offer an enhanced classification of cardiovascular conditions using the given PPG, all while taking into account the uncertainties arising from the conversion process.
    We provide a mathematical justification for our proposed computational approach, and present empirical studies demonstrating its superior performance compared to state-of-the-art baseline methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper presents "Uncertainty-Aware PPG-2-ECG (UA-P2E)," a novel framework that employs diffusion models to convert photoplethysmography (PPG) signals into electrocardiography (ECG) signals for improved cardiovascular disease classification. Recognizing the ill-posed and inherently ambiguous nature of the PPG-to-ECG conversion—stemming from the loss of certain physiological information in PPG measurements—the authors propose a multi-solution approach to address this challenge. By leveraging diffusion models, UA-P2E captures the full distribution of possible ECG signals corresponding to a given PPG input, effectively modeling the uncertainty inherent in this inverse problem. This allows the framework to generate robust ECG signals that account for the variability and ambiguity of the conversion process. The authors validate their approach through experiments across multiple cardiovascular conditions, demonstrating state-of-the-art classification performance. They provide empirical evaluations, including comparisons with two baseline models, to substantiate the effectiveness of UA-P2E in both signal reconstruction and cardiovascular classification tasks.

### Strengths
Originality and Significance: This paper offers a novel approach to the challenging PPG-to-ECG conversion by applying a diffusion-based, uncertainty-aware model. This method effectively addresses the inherently ill-posed nature of the task, capturing the distribution of possible ECG outputs rather than a single solution. By doing so, it meets a main need in cardiovascular diagnostics, especially where paired data is limited.

Methodological Rigor: The paper demonstrates strong methodological rigor with a solid theoretical foundation, including proofs of the Expected Score Classifier's (ESC) optimality. This rigorous analysis, supported by detailed equations (e.g., Theorem 3.1), supports the model’s reliability, ensuring both empirical soundness and theoretical robustness.

Comprehensive Evaluation: A thorough evaluation across 11 cardiovascular conditions highlights the model's generalizability and robustness. Compared to baseline models, it shows superior performance in signal reconstruction and classification, with added metrics for uncertainty quantification. This detailed analysis strengthens the case for clinical applicability.

Clarity and Presentation: The paper is well-organized, balancing technical details with intuitive explanations, such as figures illustrating model performance and ECG visualization strategies, enhancing clarity. The emphasis on interpretability supports practical use in clinical settings.

Significance for the Field: The integration of uncertainty-aware diffusion models for physiological signal conversion represents a meaningful enhancement in machine learning for healthcare. The interdisciplinary approach bridges machine learning and biomedical engineering with the potential to drive future innovations in cardiovascular diagnostics and medical device development.

### Weaknesses
Dependence on Synthetic Data: The evaluation heavily relies on synthetic PPG data, especially for augmenting the CinC dataset (Section 5.2​). This dependence raises concerns about potential biases, as synthetic data may not fully capture the variability and complexities of real-world PPG signals. Specifically, the synthetic data generation process and its validation are not sufficiently detailed, making it difficult to assess the fidelity of the generated signals. The lack of a thorough analysis of the differences between real and synthetic PPG data, beyond classification performance, limits the confidence in the model's real-world applicability. Consequently, the model's generalizability to real clinical settings might be limited, potentially affecting its practical applicability.

Limited Baseline Comparisons: The paper compares UA-P2E primarily with two baseline models: CardioGAN and RDDM (Table 1). While these comparisons provide some insight, the limited scope restricts a comprehensive understanding of the model's performance relative to the broader range of existing methodologies. The choice of baselines seems somewhat arbitrary, and the paper does not adequately justify why other relevant state-of-the-art methods, particularly those employing similar diffusion-based or generative approaches, were not included. Including additional, especially more recent baseline models, such as those in the referenced ArXiv papers, would strengthen the evaluation and better position UA-P2E within the current state-of-the-art.

Potential for Synthetic Artifacts: The possibility of generating hallucinations or artifacts in the synthetic ECG signals produced by the diffusion models is not thoroughly examined. Since diffusion-based models can introduce unrealistic features, a lack of analysis on this front may raise concerns about the reliability and clinical validity of the generated signals. The paper lacks a detailed analysis of the frequency content and morphological characteristics of the generated ECG signals, which is crucial for identifying potential artifacts. Addressing this risk through quantitative assessments, such as comparing the power spectral density of real and synthetic ECG signals, would enhance the credibility of the proposed approach.

Limited Dataset Diversity: The study focuses on paired PPG-ECG datasets from CinC and MIMIC-III. This narrow dataset selection may not adequately demonstrate the model's flexibility or adaptability to other data sources. The paper does not explore the impact of variations in data acquisition protocols, sensor types, or patient demographics on the model's performance. Expanding the evaluation to include larger or unpaired datasets, as well as datasets from different clinical settings, would provide a more robust validation of the model's generalizability and its potential utility across diverse cardiovascular data.

### Questions
Hallucination Analysis: How does the model ensure that synthetic ECG signals do not contain unrealistic artifacts?

Baseline Comparisons: The comparison is limited to CardioGAN and RDDM. Have you considered including additional baseline models from the literature (e.g., ArXiv:2309.15375, 2012.04949, 2204.11795, 2101.02362) to provide a more comprehensive performance evaluation?

Real vs. Synthetic Data Performance: How do the model's performance metrics change when trained on real versus synthetic PPG-ECG pairs? Can you quantify the impact of synthetic data on classification accuracy?

Generalizability Across Datasets: Have you considered applying this approach to unpaired PPG-ECG datasets or datasets from different demographic groups? Would such testing be feasible within your current framework? Have you employed techniques such as cross-validation or tested on external datasets to ensure that your model generalizes well beyond the training data?

Risk of Overfitting: Given the complexity of diffusion models and the size of the datasets used, what measures have you taken to prevent overfitting?

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a methodology to convert PPG signals into ECG ones by accounting for the uncertainty of the conversion process using a diffusion-based model. The methodology is novel arguing that by using a multi-solution approach - where multiple ECG signals can generate the same PPG wave - the combined classification of the generated ECGs is more accurate in comparison to using only the PPG or using a single generated ECG from state-of-the-art methods. The authors use two datasets, one with pairs of unlabeled ECG and PPG signals and another with only labeled ECG signals. A reverse ECG-2-PPG model is used to generate synthetic PPG for classification.

### Strengths
1. This work uses a diffusion model to propose multiple generated ECG waves for a single PPG signal, instead of a single solution as in previous works.
2. The paper provides the mathematical proof of the optimality of the proposed classifier, which reassures the credibility of the approach. Also, multiple performance metrics are used to evaluate the model.
3. In general the paper is well structured, with relevant tables and figures for comparison, and explanations are thorough.
4. The use of ECG-generated waves from PPG and its improved classification accuracy could be extended to the current PPG-based widespread solutions for cardiovascular monitoring.

### Weaknesses
Despite the comprehensive methodology and appendix, some points require some clarification:
1. The authors use 3 random seeds to generate the ECG signals from the PPG ones and report the mean and standard deviation for the chosen metrics. Given the stochastic nature of the diffusion model, are 3 seeds enough to capture the full range of ECG variability, or to provide significant statistical measures? It is unclear if the reported standard deviation is across the different seeds or across the samples generated by the same seed, which is important to assess the variability of the method.
2. Although the motivation for the use of PPG-2-ECG relies on the widespread of wearable devices, no database with signals acquired in wearable settings was used. For the diffusion model, the MIMIC-III data comes from hospital facilities (to my knowledge), and for classification, this is unclear (unless the CinC2017 database for AFib was used, for example). This should be stated as a limitation of the work, or as a pointer for future work.
3. Although the paper reports the classification of the mean and random ECG diffusion-based solutions, the performance of CardioGAN and RDDM directly, which were initially used to benchmark the ECG generation performance, is not mentioned. If the end goal is to improve classification with ECG-generated signals, it would be appropriate to use the exact implementations of CardioGAN and RDDM to compare the performance, as the reported metrics might not be directly comparable due to differences in implementation details and training procedures.
4. It is not explicitly stated whether the training and test datasets contain segments from the same recording. If the same recording appears in both datasets, the generalization ability of the approach might be not properly evaluated, leading to an overestimation of the model's performance.

Also some missing information:
- The exact database(s) of CinC that was(were) used, as there are many databases from this source available on PhysioNet
- A data summary with the number of samples used to train and test the PPG conversion and classification models (and the corresponding class distributions)
- Only the AURC is used to assess the classification performance, but since the pathological labels often suffer from class imbalance, more insightful metrics such as sensitivity, specificity and F1-Score could be reported to improve the clinical relevance of the approach and facilitate comparison with other works.

### Questions
1. Given the stochastic nature of the diffusion model, are 3 seeds enough to capture the full range of ECG variability, or to provide significant statistical measures in your work?
2. Although the paper reports the classification of the mean and random ECG diffusion-based solutions, you do not mention the performance of CardioGAN and RDDM directly, which were initially used to benchmark the ECG generation performance. If the end goal is to improve classification with ECG-generated signals, don't you think that it would be appropriate to use the exact implementations of CardioGAN and RDDM to compare the performance?
3. Did you ensure that there are no segments from the same recording in both the training and test datasets? I believe this is not mentioned. If the same recording appears in both datasets, the generalization ability of the approach might be not properly evaluated.

Also some missing information:
- The exact database(s) of CinC that was(were) used, as there are many databases from this source available on PhysioNet
- A data summary with the number of samples used to train and test the PPG conversion and classification models (and the corresponding class distributions)
- Only the AURC is used to assess the classification performance, but since the pathological labels often suffer from class imbalance, more insightful metrics such as sensitivity, specificity and F1-Score could be reported to improve the clinical relevance of the approach and facilitate comparison with other works.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces a novel methodology for synthesizing Electrocardiogram (ECG) signals from Photoplethysmogram (PPG) signals, aimed at enhancing the reliability of cardiovascular disease diagnostics while avoiding the difficulties associated with ECG acquisition. By measuring the uncertainties involved in generating the ECG from PPG signals and in classifying from the generated signals, the authors convincingly demonstrate the feasibility and superiority of their proposed method.

### Strengths
1. The theoretical foundation validating the transition from PPG to ECG and then to classification is robust. The paper demonstrates that generating multiple candidate ECG sample sets can mitigate the uncertainty of ECG conversion and eliminate errors due to mismatch.
2. Quantification of uncertainties during the conversion process enhances the interpretability of the results.
3. The methodological design is well-justified through practical experiments showing the reliability of PPG-derived ECGs, surpassing state-of-the-art methods. Ablation studies further substantiate the validity of the proposed approach.
4. The paper is well-written with a clear structure, making it easy to follow.

### Weaknesses
1. The paper should specify which particular database the CinC dataset is derived from. The rationale behind choosing these 11 types of anomalies should be clarified.
2. Although the authors provide a thorough theoretical foundation and extensive analysis, the task of generating ECG from PPG lacks inherent rationale. It is unclear whether the generated ECG can reliably reflect arrhythmias, making this approach seem like an uncertain application of analytical techniques with limited practical value. The core issue is that if PPG signals do not contain sufficient information to discern specific arrhythmias, then generating an ECG from them will not magically create that missing information. The paper needs to address this fundamental limitation.
3. The authors should further compare their classification results with state-of-the-art models, as the current performance appears suboptimal for ECG classification tasks.

### Questions
1. As Figure 3 shows, the performance of the PPG-derived ECG significantly trails that of the original ECG. How do you explain this discrepancy? Is it possible that the required information for detecting certain arrhythmias is inherently absent in the PPG signals?
2. Appendix G focuses on Atrial Fibrillation (AF), which is relatively easier to detect. It would be beneficial to include results for other types of diseases to provide a broader evaluation.
3. How does pacing rhythm manifest in PPG signals? Is it feasible to accurately generate ECG signals with pacing rhythm characteristics from PPG?

### Soundness
2

### Presentation
3

### Contribution
3

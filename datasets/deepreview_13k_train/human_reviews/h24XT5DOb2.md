# A Foundation Model for Patient Behavior Monitoring and Suicide Detection

- Decision: Reject
- Scores: 3, 6, 3, 6

## Abstract
Foundation models have achieved remarkable success across various domains, yet their adoption in healthcare remains limited, particularly in areas requiring the analysis of smaller and more complex datasets. While foundation models have made significant advances in medical imaging, genetic biomarkers, and time series from electronic health records, the potential for patient behavior monitoring through wearable devices remains underexplored. Wearable device datasets are inherently heterogeneous and multisource and often exhibit high rates of missing data, presenting unique challenges. Notably, missing patterns in these datasets are frequently not-at-random, and when adequately modeled, these patterns can reveal crucial insights into patient behavior. 
This paper introduces a novel foundation model based on a modified vector quantized variational autoencoder (VQ-VAE), specifically designed to process real-world data from wearable devices. Our model excels at reconstructing heterogeneous multisource time-series data and effectively models missing data patterns. We demonstrate that our pretrained model, trained on a broad cohort of psychiatric patients with diverse mental health issues, can perform downstream tasks without fine-tuning on a held-out cohort of suicidal patients. This is illustrated through the use of a change-point detection algorithm that identifies suicide attempts with high accuracy, matching or surpassing patient-specific methods, thereby highlighting the potential of VQ-VAE as a versatile tool for behavioral analysis in healthcare.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors introduce a model based on VQ-VAE, trained in a self-supervised way with different (informative) ways of modeling missingness. The authors look at reconstruction and imputation accuracy of the model on a behavioral data set of wearable readings. Using the trained model the authors implement a Bayesian online learning procedure to infer the MAP of the presence of a change point in the data with proposed application to suicide prevention, which is benchmarked against HetMM on their behavioral data set in terms of ROC curves.

### Strengths
- Time series modeling and change point detection are important problems in clinical applications

### Weaknesses
 - A related work section for other time series models is missing, but important to place the work within the context of the broader literature
- For imputation, the model should be compared to baselines.
- Other baselines for change-point detection than HetMM would be beneficial, e.g. point process frameworks, time series foundation models
- The novelty of the work (as opposed to applying a known framework to a novel interesting problem) is not entirely clear to me.

### Questions
- What is the calibration of the pseudo-probabilities as compared to HetMM?
- How does the model deal with censoring due to loss of follow-up?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a foundation model for patient behavior monitoring and suicide detection based on a modified Vector Quantized Variational Autoencoder (VQ-VAE). This model effectively reconstructs heterogeneous time-series data from wearable devices and captures missing data patterns. The paper highlights its application in predicting suicide attempts using a probabilistic change-point detection (CPD) algorithm on data from a cohort of psychiatric patients. The model shows promise for scalable, efficient patient monitoring by outperforming patient-specific methods without requiring fine-tuning.

### Strengths
The approach is novel in integrating VQ-VAE with CPD for behavioral analysis and suicide prediction, particularly in using discrete latent representations for temporal health data. The paper is methodologically strong, with well-designed experiments and performance evaluations. The work has substantial potential in clinical monitoring and predictive modeling, addressing a critical healthcare application with an approach that could be extended to other domains. The paper is well-written, with clear articulation of concepts and objectives, making complex methodologies accessible. Figures and tables are effectively used to illustrate the architecture and experimental results.

### Weaknesses
The evaluation is conducted on a single private dataset. 
The use of a proprietary dataset limits reproducibility and prevents validation or benchmarking with public datasets, reducing transparency. Expanding to public datasets could provide a more comprehensive assessment of the model's generalization and facilitate future comparisons.

The study lacks a comparison with other generative models for reconstruction tasks, which could demonstrate the superiority or limitations of the proposed VQ-VAE model, comparisons with more generative models in the reconstruction phase could bolster the paper’s robustness. Specifically, the paper should compare the VQ-VAE against other models such as GANs or standard VAEs, evaluating not just reconstruction quality but also the quality of the learned latent space for downstream tasks. This comparison should include metrics relevant to time-series data, such as dynamic time warping distance or similar measures that capture temporal dependencies.

Although three VQ-VAE variants (A0, A1, and A2) are tested, there is limited discussion on the specific performance differences across these variants and their impact on handling missing data. It is unclear if the variants offer any significant advantage over each other, especially in scenarios with varying degrees of missingness. The paper should provide a more detailed analysis of how each variant handles different missing data patterns, and whether the explicit encoding of missingness masks in A1 and A2 provides a tangible benefit over the zero-imputation approach in A0.

Certain technical details, such as the choice of hyperparameters, could be clarified to enhance reproducibility. Specifically, the paper lacks a detailed explanation of the hyperparameter tuning process for both the VQ-VAE and the change-point detection algorithm. This includes the learning rate, batch size, number of epochs, and the specific optimization algorithm used for the VQ-VAE, as well as the parameters for the CPD algorithm, such as the window size and the hazard function parameter. The rationale behind these choices and their impact on the final results should be discussed.

A minor typo: Line 188 - The term "D" is used without prior definition or context.

### Questions
1. Could you elaborate on the performance differences among the three VQ-VAE variants (A0, A1, and A2) in terms of handling specific missing data patterns?

2. Have you considered evaluating the model on additional, publicly available behavioral datasets to better assess generalizability and facilitate reproducibility? Do the authors plan to publish or share the dataset to reproduce and enable further research validation?

3. Have you explored using alternative generative models, such as GANs or VAEs, for comparison on data reconstruction? How do you envision these models performing relative to VQ-VAE in terms of capturing behavioral patterns?

4. Can the authors clarify the rationale for choosing specific hyperparameters for CPD (e.g., the hazard function parameter λ)?

A minor typo: Line 188 - The term "D" is used without prior definition or context.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper explores patient behavior monitoring and suicide detection by adapting the vector quantized variational autoencoder (VQ-VAE) to analyze data from real-world wearable devices. By reconstructing heterogeneous multi-source time-series data and accounting for patterns of missing data, the proposed model is validated to be effective in detecting change-time events within a cohort of suicidal patients.

### Strengths
S1. This research provides significant medical potential by modeling heterogeneous, multi-source time-series data from wearable devices, aiming to develop advanced approaches for identifying potential behavioral shifts that signal serious mental health risks.

S2. The proposed model, which leverages VQ-VAE as the foundation model, captures the missing data patterns, and incorporates a change-point detection algorithm, is overall reasonable from a technical standpoint for this specific medical application.

S3. The experimental evaluation includes a demonstration of imputation performance, an assessment of downstream tasks, results from statistical tests, and several representative case studies.

### Weaknesses
W1. My primary concern regarding this paper is its technical novelty. Although the proposal adeptly uses the VQ-VAE model as the foundational framework, modifies its design to capture missing data patterns in time-series wearable device data, and connects to change-point detection as a downstream task, it relies heavily on existing techniques. This reliance diminishes the perceived novelty of the proposed model. Moreover, the paper does not sufficiently articulate the challenges and complexities associated with integrating these techniques, which is crucial for demonstrating its innovation.

W2. The evaluation of imputation performance lacks comparative baselines, which undermines the robustness of the findings. Additionally, the downstream task evaluation includes only one baseline, HetMM, which is insufficient. Incorporating a broader range of advanced and recent baselines would help demonstrate the superiority of the proposal in this research area.

W3. The evaluation relies solely on a single proprietary dataset, limiting the generalizability of the findings. Expanding the evaluation to include multiple datasets would enhance the credibility and applicability of the proposed model across different contexts.

W4. The performance improvements offered by the proposed model are marginal when compared with HetMM. Given that the proposal claims advantages in scalability and efficiency, it is essential to substantiate these claims with experiments on larger datasets or real-time analysis scenarios.

W5. As the proposal targets a specific healthcare application—suicide detection—it would be advantageous to include medical validation of the findings or to offer insights into how the proposed model could inform real-world clinical decision-making. Such contributions would significantly elevate the practical relevance of the proposal.

W6. The writing of this paper could be improved by addressing the following aspects:

(i) The paper should clearly identify which model among Model A0, Model A1, and Model A2 performs best and should be recognized as the final proposed model.

(ii) The inclusion of a detailed related work section is necessary. This section would help situate the paper within the existing body of knowledge, providing a comprehensive backdrop against which the current research can be assessed and appreciated.

### Questions
Please refer to points W1 through W6 for detailed concerns and recommendations.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a foundational model for imputing PDP data with missing MNAR values using VQ-VAE. This system aims to encode the time series into discretized embeddings that represent latent profiles, which help capture patient behavior and improve performance in downstream tasks.

The results appear comparable to existing alternatives in the literature. However, the strength of this model lies in its flexibility, as it can be applied to tasks for which it was not explicitly trained. This demonstrates that the generated embeddings capture meaningful representations of the input data, allowing their use across a broader range of objectives without requiring fine-tuning.

### Strengths
- **Model Flexibility**: One of the standout features of the proposed model is its flexibility. The embeddings learned are generalizable across different tasks, even those for which the model was not explicitly trained. This demonstrates its robustness and potential for transfer learning.

- **Potential for Interpretability**: The use of latent profile embeddings offers promise for improving interpretability in clinical and behavioral data, an essential feature for real-world healthcare applications. This adds an additional layer of value to the model beyond just predictive accuracy.

- **Description of the method**: The article presents a detailed explanation of the method.

### Weaknesses
 - **Limited Evaluation on Downstream Tasks**: Although the paper emphasizes the model’s flexibility and its applicability to a variety of downstream tasks, the evaluation is limited to only two tasks. Expanding the analysis to include a broader range of scenarios, particularly those that would highlight the benefits of the learned latent space, would have provided stronger evidence of the model's generalizability. For instance, tasks that require the model to extrapolate beyond the training data or to adapt to different data distributions would be valuable.

- **Lack of Exploration on Interpretability**: The paper asserts that the learned latent profiles enhance interpretability, yet no concrete evidence or case studies are provided to substantiate this claim. A more thorough investigation, possibly through qualitative analysis or correlations with clinically relevant features, would significantly strengthen the paper's contributions. It would be beneficial to see how these latent profiles relate to known clinical markers or patient subgroups, and whether they can provide insights beyond what is already known.

- **Omission of Spatio-Temporal Architectures**: While the authors mention that exploring spatio-temporal architectures is left for future work, the choice not to use models such as GNNs, RNNs, or Transformers, which are well-suited for these types of tasks, is not sufficiently justified. This omission limits the model's applicability to more complex time series problems, especially considering the sequential nature of the data. The authors should provide a more detailed rationale for this design choice, and perhaps consider the potential benefits of these architectures for capturing temporal dependencies.

- **Clarity in Results Presentation:** The presentation of results could be made clearer. The use of multi-line graphs can be confusing, and this would be better supplemented with numerical information in the main text. Additionally, incorporating a wider range of classification metrics beyond AUC, such as AUPRC, would provide a more comprehensive evaluation of the model's performance, especially given the potential for class imbalance in the suicide detection task.

### Questions
- When training the model, synthetic missing values are introduced. Why are these not also used during the calculation of the loss function to optimize their imputation, potentially improving the model’s capacity to handle missing values in the time series?

- What is the class imbalance in the Suicide Detection task? If there is significant imbalance, the AUC score might be misleading. In clinical settings, the AUPRC is often used as an alternative metric for imbalanced data [1]. Perhaps it could be considered for this problem as well.

- The imputation errors in Table 6 seem quite high, although this may be due to the nature of the data. Could the authors provide results from comparison techniques? It would be useful to include at least one method of a common benchmark [2], and possibly show results from methods like linear interpolation and mean interpolation.

- The paper mentions that these profile embeddings could enhance the interpretability of individual behaviors. Have the authors explored this? Were they able to find any correlation between the presence of specific embeddings and labels? If not, could they outline how they would approach this in future work, if it falls outside the scope of this paper?

- Why were more suitable architectures for capturing spatio-temporal representations not used? While it is mentioned that this is left for future work, it’s unclear why models such as GNNs, RNNs, Transformers, or even newer blocks like Mamba were not considered [2] [3].

- Figure 4 is difficult to interpret in terms of the quality of imputations and reconstructions. It would be helpful to complement this with a table, similar to Table 6.


[1] Moor, M., Rieck, B., Horn, M., Jutzeler, C. R., & Borgwardt, K. (2021). Early prediction of sepsis in the ICU using machine learning: a systematic review. Frontiers in medicine, 8, 607952.

[2] Cini, A., Marisca, I., & Alippi, C. (2021). Filling the g_ap_s: Multivariate time series imputation by graph neural networks. arXiv preprint arXiv:2108.00298.

[3] Liu, M., Huang, H., Feng, H., Sun, L., Du, B., & Fu, Y. (2023, April). Pristi: A conditional diffusion framework for spatiotemporal imputation. In 2023 IEEE 39th International Conference on Data Engineering (ICDE) (pp. 1927-1939). IEEE.

### Soundness
3

### Presentation
3

### Contribution
3

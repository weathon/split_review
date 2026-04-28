# Calibrating Video Watch-time Predictions with Credible Prototype Alignment

- Decision: Reject
- Avg Score: 6.25
- Scores: 5, 8, 6, 6

## Abstract
Accurately predicting user watch-time is crucial for enhancing user stickiness and retention in video recommendation systems. Existing watch-time prediction approaches typically involve transformations of watch-time labels for prediction and subsequent reversal, ignoring both the natural distribution properties of label and the \textit{instance representation confusion} that results in inaccurate predictions. 
In this paper, we propose ProWTP, a two-stage method combining prototype learning and optimal transport for watch-time regression prediction, suitable for any deep recommendation model. The core idea of ProWTP is to align label distribution with instance representation distribution to calibrate the instance space, thereby improving prediction accuracy. Specifically, we observe that the watch-ratio (the ratio of watch-time to video duration) within the same duration bucket exhibits a multimodal distribution. To facilitate incorporation into models, we use a hierarchical vector quantised variational autoencoder (HVQ-VAE) to convert the continuous label distribution into a high-dimensional discrete distribution, serving as credible prototypes for calibrations. Based on this, ProWTP views the alignment between prototypes and instance representations as a Semi-relaxed Unbalanced Optimal Transport (SUOT) problem, where the marginal constraints of prototypes are relaxed. And the corresponding optimization problem is reformulated as a weighted Lasso problem for solution. Moreover, ProWTP introduces the assignment and compactness losses to encourage instances to cluster closely around their respective prototypes, thereby enhancing the prototype-level distinguishability. Finally, we conducted extensive offline experiments on two industrial datasets, demonstrating our consistent superiority in real-world application.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces ProWTP, a two-stage method that combines prototype learning and optimal transport (OT) to improve watch-time prediction in video recommender systems. ProWTP uses a hierarchical vector quantized variational autoencoder (HVQ-VAE) to convert continuous labels into discrete prototypes, aligning the label distribution with the instance representation distribution via OT to enhance prediction accuracy. Offline experiments on two industrial datasets demonstrate ProWTP's superior performance.

### Strengths
Watch time prediction is a critical problem in video recommender systems. This paper presents a novel approach to solving the watch time prediction problem through prototype learning and optimal transport. In summary, the paper has the following main strengths:

+ The paper is the first to leverage optimal transport techniques to enhance watch time prediction.
+ The paper investigates the multimodal distribution properties of watch-ratio, thereby generating credible prototype vectors.
+ The paper identifies the representation confusion issue and proposes the use of prototype learning to mitigate it.

### Weaknesses
1. For Figure 1a, to the reviewer, it is unclear whether the watch-ratio distribution for videos of short and medium durations is truly multimodal, as the density of the first peak (around 1.5 for medium-duration videos) does not appear significant. The distinction between the peaks is not pronounced enough to confidently claim multimodality, especially given the variance in the data. A more rigorous statistical test for multimodality might be needed to support this claim.
2. As presented in Section 4.2, ProWTP samples a one-dimensional distribution $w$ from the multimodal distribution and claims this distribution should be near-Gaussian. However, to the reviewer, with random sampling alone, $w$ may not exhibit a near-Gaussian form. The authors are encouraged to elaborate further on any specific sampling strategies employed to achieve this distribution. The description lacks detail on how the sampling process ensures the resulting distribution approximates a Gaussian, especially given the complex nature of the underlying multimodal distribution.
3. The prototype generation process remains unclear. Specifically, does the encoder use individual watch ratios or the entire distribution as input? If it uses the distribution, does this imply that the HVA-VAE is trained on a single sample, as the reviewer assumes there is one distribution for the entire dataset? The explanation of how the encoder processes the input data is ambiguous, and the training procedure for the HVA-VAE needs clarification to understand how it handles the input data.
4. The instance representation confusion issue is not intuitive and well-defined. The concept of 'confusion' needs a more precise definition and a clear explanation of how it manifests in the instance representations. It is not clear what specific problem this 'confusion' is causing and how the proposed method addresses it.
5. In Section 4.3, further elaboration is needed on why both the instance representation distribution and the prototype representation distribution follow a uniform distribution. The justification for assuming a uniform distribution for both instance and prototype representations is not sufficiently explained, and the underlying assumptions need to be made more explicit.
6. To the reviewer, the improvement over baselines on the two datasets appears marginal, suggesting the need to test the significance of these improvements. Additionally, while the authors adopt the parameter settings from the original papers for baselines, these models may not be optimized for the MLP architecture used here, potentially making the settings sub-optimal. The authors are thus encouraged to search for optimal baseline parameters to ensure a fair comparison. The lack of statistical significance testing and the potential for sub-optimal baseline parameter settings raise concerns about the robustness of the reported improvements.
7. The authors are encouraged to include an online evaluation to better validate ProWTP’s effectiveness with real users. Offline evaluations, while useful, do not fully capture the complexities of real-world user behavior, and an online evaluation is crucial to assess the practical impact of the proposed method.
8. No empirical results demonstrate whether the representation confusion issue has been addressed. The paper lacks specific experiments or analyses that directly show how the proposed method mitigates the representation confusion issue, and this needs to be empirically validated.
9. The trend in Table 3 raises concerns for the reviewer. If there is a clustering structure in the data that benefits watch-time prediction, as suggested in the other tables, why does k-means underperform random? The poor performance of k-means compared to random selection is counterintuitive and suggests a potential flaw in the clustering approach or its application within the framework.
10. The literature review overlooks a recent work for watch-time prediction [1], which is closely related to this work.

### Questions
1. The following sentence repeats twice in the related work. "D2Q alleviates the duration bias by conducting backdoor adjustments and models watch time with direct watch-time quantile regression. "
2. The authors highlight, "However, those methods struggle to consistently maintain high predictive accuracy across different models." Could you provide more detailed explanations for why existing methods cannot maintain high predictive accuracy across different models?
3. Regarding the sampling in the pre-processing step, the process of transforming original one-dimensional multimodal distributions into D ∗ L one-dimensional near-Gaussian distributions w of length needs further clarfirication. Please provide a clear description of how the data is sampled and transformed.
4. The computation for optimal transport is expensive. Although the authors reduce the computational cost by randomly sampling 20% of the instances in a batch, could you please provide the trade-off numbers between effectiveness and efficiency? Specifically, how much does this reduction in computational cost impact the model's performance?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper presents a novel two-stage method, i.e., ProWTP, for accurately predicting user watch-time in video recommendation systems. The authors address the limitations of existing approaches by combining prototype learning and optimal transport, aligning label and instance representation distributions to improve prediction accuracy. The use of HVQ-VAE for converting continuous labels into high-dimensional discrete prototypes and formulating the alignment problem as a Semi-relaxed Unbalanced Optimal Transport (SUOT) problem are innovative contributions. The introduction of assignment and compactness losses further enhances the method's effectiveness. Extensive offline experiments demonstrate ProWTP's superiority in real-world applications, making it a valuable contribution to the field of video recommendation systems. Overall, this paper is well-written, thorough, and makes significant advancements in the area of watch-time prediction.

### Strengths
(1) The paper introduces ProWTP, a method that significantly enhances model prediction performance in the watch-time prediction (WTP) task by addressing the instance representation confusion problem. By aligning label distributions with instance representation distributions through optimal transport, ProWTP ensures that the model's predictions are more accurate and reliable. This innovation is crucial for improving user stickiness and retention in video recommendation systems.
(2) The paper is the first to investigate the multimodal distribution properties of watch-ratio across different video duration buckets. By utilizing a hierarchical vector quantized variational autoencoder (VQ-VAE) to transform these properties into credible high-dimensional prototype vectors, the paper provides a more precise reference for recommendation models calibration. This innovation allows the model to better understand user preferences and behaviors, leading to more personalized and effective recommendations.
(3) The paper conducts extensive offline experiments on two industrial datasets to validate the effectiveness of the proposed approach. The experimental results consistently demonstrate the superiority of ProWTP over existing methods, providing strong evidence for its practical applications in real-world scenarios. This innovation ensures that the proposed method is not only theoretically sound but also feasible and effective in practical use.

### Weaknesses
(1) The boundaries and logic between different modules in Figure 2 are not clearly delineated. To enhance readability and comprehension, it is recommended to add borders around each module. This will help readers better understand the structure and relationships within the figure.
(2) To ensure robustness and reproducibility, it is advisable to present the mean and variance of multiple experimental runs in Table 1. This will provide a more comprehensive evaluation of the proposed method's performance.

### Questions
(1) The observed multimodal phenomenon is intriguing. Could you elaborate on the potential user behavior or habits that may be underlying this phenomenon? Understanding the root causes could provide deeper insights into the data and its implications.
2. Did the real data used in your study undergo any preprocessing steps? If so, could you outline the specific preprocessing techniques employed and highlight any important considerations or challenges encountered during this process? This information would help replicate your results and understand the data quality.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces ProWTP, a two-stage framework for watch-time prediction. In the first stage, ProWTP employs HVQ-VAE to capture clustering structures among instances based on watch ratios. In the second stage, ProWTP uses SUOT to refine instance representations to align with the learned clusters.
ProWTP is validated in the offline evaluation. ProWTP shows improvement over baseline methods on two benchmark datasets. The ablation study also shows the effectiveness of various design choices within the framework.

The reviewer primarily has the following concerns regarding the presentation and experiments of this work.
1. For Figure 1a, to the reviewer, it is unclear whether the watch-ratio distribution for videos of short and medium durations is truly multimodal, as the density of the first peak (around 1.5 for medium-duration videos) does not appear significant.
2. As presented in Section 4.2, ProWTP samples a one-dimensional distribution $w$ from the multimodal distribution and claims this distribution should be near-Gaussian. However, to the reviewer, with random sampling alone, $w$ may not exhibit a near-Gaussian form. The authors are encouraged to elaborate further on any specific sampling strategies employed to achieve this distribution.
3. The prototype generation process remains unclear. Specifically, does the encoder use individual watch ratios or the entire distribution as input? If it uses the distribution, does this imply that the HVA-VAE is trained on a single sample, as the reviewer assumes there is one distribution for the entire dataset?
4. The instance representation confusion issue is not intuitive and well-defined.
5. In Section 4.3, further elaboration is needed on why both the instance representation distribution and the prototype representation distribution follow a uniform distribution.
6. To the reviewer, the improvement over baselines on the two datasets appears marginal, suggesting the need to test the significance of these improvements. Additionally, while the authors adopt the parameter settings from the original papers for baselines, these models may not be optimized for the MLP architecture used here, potentially making the settings sub-optimal. The authors are thus encouraged to search for optimal baseline parameters to ensure a fair comparison.
7. The authors are encouraged to include an online evaluation to better validate ProWTP’s effectiveness with real users.
8. No empirical results demonstrate whether the representation confusion issue has been addressed.
9. The trend in Table 3 raises concerns for the reviewer. If there is a clustering structure in the data that benefits watch-time prediction, as suggested in the other tables, why does k-means underperform random?
10. The literature review overlooks a recent work for watch-time prediction [1], which is closely related to this work.

[1] SWaT: Statistical Modeling of Video Watch Time through User Behavior Analysis

### Strengths
Overall, the framework presented in ProWTP is novel and interesting, and the experiments demonstrate certain advantages. However, further validation is necessary to fully conclude its effectiveness.

### Weaknesses
Please refer to the summaries for detailed weaknesses.

### Questions
Please refer to the summaries for detailed questions.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a novel two-stage method named ProWTP for predicting user watch-time in video recommendation systems. The method enhances prediction accuracy by aligning label distributions with instance representation distributions through a combination of prototype learning and optimal transport, specifically using a Hierarchical Vector Quantised Variational AutoEncoder and Semi-relaxed Unbalanced Optimal Transport. The innovation lies in calibrating the instance space by addressing the natural distribution properties of labels and the instance representation confusion, which are often overlooked in existing methods. Experiments on two datasets illustrate the effectiveness of the proposed ProWTP.

### Strengths
S1. The research question is quite interesting and meaningful for video recommendation. 

S2. The paper accurately identifies the issues of ignoring label distribution properties and instance representation confusion in watch-time prediction methods.

S3. ProWTP offers an innovative approach to calibrating watch-time predictions by combining prototype learning and optimal transport, addressing key issues in existing methods.

### Weaknesses
W1. The research question is quite good. However, the proposed method with VAE and OT seems too heavy to be implemented in the real world.  The authors should discuss the necessity of these complex designs in detail. Further, complex analysis is lacking, but it is necessary here.

W2. While performing well on two datasets, the paper does not discuss the method's generalizability to different types of recommendation systems or varying lengths of video content.

W3. The compared baselines are a bit out of date. The authors should compare with more recent SOTA recommendation models and VAE-based models.

W4. The paper lacks discussion on how to interpret prototypes and their relationship with user behavior, which may limit understanding of model predictions.

### Questions
Q1: What is the inference efficiency of the proposed model, compared with baselines?

Q2: When user behavior patterns change, how can the model be effectively updated and adjusted? Are there strategies for online learning or incremental learning?

Q3: The discussion of the impact of the number of prototypes is insufficient.

### Soundness
2

### Presentation
3

### Contribution
3

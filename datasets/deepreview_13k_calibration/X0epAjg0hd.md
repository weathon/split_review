# Reassessing How to Compare and Improve the Calibration of Machine Learning Models

- Decision: Accept
- Avg Score: 5.67
- Scores: 6, 6, 5

## Abstract
A machine learning model is calibrated if its predicted probability for an outcome matches the observed frequency for that outcome conditional on the model prediction. This property has become increasingly important as the impact of machine learning models has continued to spread to various domains. As a result, there are now a dizzying number of recent papers on measuring and improving the calibration of (specifically deep learning) models. In this work, we reassess the reporting of calibration metrics in the recent literature. We show that there exist trivial recalibration approaches that can appear seemingly state-of-the-art unless calibration and prediction metrics (i.e. test accuracy) are accompanied by additional generalization metrics such as negative log-likelihood. We then derive a calibration-based decomposition of Bregman divergences that can be used to both motivate a choice of calibration metric based on a generalization metric, and to detect trivial calibration. Finally, we apply these ideas to develop a new extension to reliability diagrams that can be used to jointly visualize calibration as well as the estimated generalization error of a model.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper critically examines current practices in evaluating model calibration, particularly for deep learning. It highlights flaws in reporting calibration metrics. The authors propose a new methodology based on the calibration-based decomposition of Bregman divergences and introduce new diagrams. These diagrams visualize calibration and generalization error jointly, allowing a more nuanced assessment. Additionally, the paper provides theoretical insights.

### Strengths
1. This paper studies a fundamental question in the ML calibration literature: how to compare and assess the model calibration performance. This is a very important question.
2. This paper is easy to follow, and the main take-away is very clear.
3. This paper points out "pitfalls" regarding calibration reporting in the current literature clearly.
4. The proposed calibration-sharpness digram is interesting and novel.
5. This paper is theoretically sound.

### Weaknesses
1. The experiment section is relatively weak. Only one dataset was examined. 
2. It would be great if the authors could open-source the code and make the new diagrams easier to use for other ML practitioners.

### Questions
n/a

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
- The authors identify key issues in current calibration performance reporting in machine learning literature, emphasizing that focusing solely on calibration error (e.g., ECE) and accuracy can lead to misleading conclusions.
- They show that simple recalibration strategies may outperform commonly used methods if calibration metrics are not presented alongside generalization metrics, such as negative log-likelihood (NLL).
- The authors develop a theoretical framework that aligns calibration metrics with generalization metrics using Bregman divergences, proposing that calibration measures should be selected based on the chosen generalization metric. They establish novel connections between full calibration error and confidence calibration error.
- They introduce “calibration-sharpness diagrams” as an extension to traditional reliability diagrams, allowing for a joint visualization of calibration and generalization errors and providing a more detailed view of the trade-offs between calibration and model sharpness.

### Strengths
- The paper systematically identifies critical issues in current reporting practices for calibration and prediction accuracy, highlighting the limitations of relying solely on metrics like ECE and accuracy.
- By utilizing Bregman divergences, the authors develop a unified framework that aligns calibration metrics with generalization metrics. This theoretical approach offers valuable insights for the development and evaluation of new calibration methods.

### Weaknesses
### Concerns for Unclear Guidelines for Selecting Calibration Metrics:
- While the paper proposes selecting calibration metrics based on generalization metrics, it does not provide clear guidelines or step-by-step procedures for applying this principle in practice. From a practical perspective, providing concrete examples and a well-defined workflow for implementing the proposed framework would enhance the paper’s contribution and make its practical applications more accessible. For instance, a detailed example showing how to derive a calibration metric from a specific generalization metric like the cross-entropy loss, and how this derived metric differs from standard calibration metrics, would be beneficial. The lack of a clear mapping between generalization metrics and their corresponding calibration metrics makes it difficult to assess the practical utility of the proposed framework.

### Sensitivity of Calibration-Sharpness Diagrams to Kernel and Hyperparameter Selection:
- In calibration-sharpness diagrams based on kernel regression estimators, the choice of kernel type and hyperparameter values appears to significantly influence the results. This concern is relevant not only to the proposed method but also to other calibration error evaluations based on Nadaraya-Watson estimators, such as smooth ECE. However, these parameters pose a risk of being adjusted arbitrarily to produce favorable calibration performance. A more in-depth discussion on minimizing this arbitrariness would help ensure fair calibration evaluation. For example, the paper should explore the impact of different kernel bandwidths on the resulting calibration-sharpness diagrams, and discuss how to choose a bandwidth that is not biased towards a specific calibration performance. A sensitivity analysis demonstrating the range of calibration errors achievable by varying these parameters would also be helpful.
- Additionally, the Appendix reveals considerable variability in calibration performance across different kernel types and hyperparameter settings, raising concerns about the reliability of calibration-sharpness diagrams produced by the proposed framework. If calibration performance assessments based on these diagrams are highly sensitive to such choices, further discussion on criteria for kernel selection and strategies for tuning hyperparameters would strengthen the paper’s contributions. The paper should provide more concrete guidelines, perhaps based on cross-validation or other principled methods, for choosing these parameters to ensure the robustness of the results.

### Concerns for Readability and Presentation Clarity:
- The presentation of certain theoretical elements in the paper could benefit from added clarity, as the connection between some propositions and the main text is not always apparent. For example, in Proposition 4.5, a more detailed explanation of the “always wrong predictor” and its implications could improve understanding. This may stem from a lack of detailed exposition rather than the inherent complexity of the material, but additional clarification would enhance accessibility. The paper should provide a more intuitive explanation of the proposition, perhaps with a simple example illustrating how an “always wrong predictor” can have low confidence calibration error but high generalization error.
### Concerns for Relatively Weak Explanation for the Motivation Behind Using Bregman Divergences:
- While the paper establishes useful calibration metrics based on Bregman divergences, it does not clearly explain why the authors hypothesized that Bregman divergence-based metrics would be effective for calibration. Specifically, the rationale behind selecting Bregman divergences over other possible metrics remains unclear, making it challenging to fully understand the motivation for the proposed framework. Although the benefits of this choice are evident in the theoretical results, a more explicit discussion on why Bregman divergences were chosen would provide valuable context. The paper should elaborate on the specific properties of Bregman divergences that make them suitable for calibration, and why other divergence measures were not considered.
- I understand that the authors’ main motivation for adopting Bregman divergences could be that they provide a general metric encompassing several proper scoring rules, allowing for a unified approach to selecting calibration evaluation metrics. Emphasizing this reasoning could facilitate a smoother transition from Section 3 to Section 4. While this is a personal suggestion and not strictly necessary, including a brief explanation in Section 2 on the basic properties of Bregman divergences and their relationship to calibration metrics might improve the clarity and flow of the presentation.

### Questions
Based on the above Weakness points, I would like to ask the following questions. If appropriate and sufficient discussion is provided on these points, I would be pleased to consider raising my score.

- Could you provide specific examples or a more detailed workflow for selecting calibration metrics based on common generalization metrics? A decision flowchart or table mapping generalization metrics to recommended calibration metrics would also be helpful for practitioners applying the proposed framework.
-  How could the arbitrariness in selecting kernel types and hyperparameters for calibration-sharpness diagrams be minimized? Could you suggest specific strategies, such as cross-validation approaches or sensitivity analyses, to guide these choices? Additionally, are there recommended default choices for kernels and hyperparameters that perform robustly across various scenarios?
- Given the variability in calibration performance across different kernel types and hyperparameter settings (as shown in the Appendix), could you provide more guidance on appropriate criteria for kernel selection and hyperparameter tuning? This would strengthen the reliability of calibration assessments based on the proposed diagrams.
- Could you clarify the relationship between some theorems and the main discussion, e.g.,  regarding the “always wrong predictor” in Proposition 4.5 and its implications? An example or illustration of how the “always wrong predictor” relates to real-world calibration scenarios would be helpful. Additionally, could you explain how this proposition supports or challenges the main arguments of the paper?
- Could you expand on the motivation behind choosing Bregman divergences for calibration metrics? Specifically, what factors led to the choice of Bregman divergences over other potential metrics? Additional context on this decision-making process would be helpful.
  - Related to the above question, would you consider adding a brief explanation of Bregman divergences and their relationship to calibration metrics in Section 2? I believe this might improve the flow from Section 3 to Section 4 and provide readers with a clearer understanding of the theoretical foundation.
- I may have overlooked or misunderstood certain aspects, but could you provide a more detailed guide on how to interpret the components of experimental figures like Figure 1? Specifically, explanations on how to read the sharpness band, density plot, and calibration curve, and what each represents in terms of model performance, would be helpful. Adding some sentences in the caption part of the figures or including a “How to read this figure” section in the paper could also improve accessibility.
- Although it might slightly deviate from the core contributions of this paper, would it be valuable to provide empirical discussions on the bias of the Nadaraya-Watson estimator? For instance, as demonstrated in [Jiang et al., ICML 2020], would it be possible to use a synthetic data setup to empirically evaluate the bias of the Nadaraya-Watson estimator by estimating the true pointwise sharpness gap with Monte Carlo estimation and comparing it to the Nadaraya-Watson estimator? If this is not feasible within the setup of [Jiang et al., ICML 2020], could a simpler experimental setting be devised where the true values of the pointwise sharpness gap are estimable?

### Citation:
[Jiang et al., ICML 2020]: Jize Zhang, Bhavya Kailkhura, and T. Yong-Jin Han. Mix-n-Match: Ensemble and Compositional Methods for Uncertainty Calibration in Deep Learning. ICML2020. (https://arxiv.org/abs/2003.07329).

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies the task of calibration: measuring how well a model predicts the class probability and improving the quality.
It begins with studying the Expected Calibration Error (ECE), a popular metric of how well a model predicts the class probability.
The authors point out that the ECE can be improved by a trivial modification to the confidence function. The authors present experiments (Table 1) showing how this metric differs from proper scoring rules such as the Mean Squared Error (MSE) and the Negative Log Loss (NLL).

The paper then moves on to the study about proper scoring rules induced by Bregman divergences. The authors explain the gap between a proper scoring rule and the calibration error using a decomposition of Bregman divergences (Lemma 4.1) with some properties of this gap (Proposition 4.2 and 4.3). The pointwise variant of the gap is also defined (Eq. (4.7)).

The authors also show that the gap between the full calibration error and its one-dimensional counterpart.

Finally, the paper presents visualization results based on the proposed metric (4.7).

### Strengths
- Theorems and propositions are interesting and seem correct. They are supported by rigorous proofs.
- The paper studies an important problem of calibration.
- The paper provides a good literature review, which motivates the direction of this work well.

### Weaknesses
 - The paper explains ECE can be improved by a trivial modification to the confidence function but does not explain why it is a bad thing. If estimating the whole class probabilities is not the objective and we only care about the confidence of the predicted class, this solution could be just fine.

 - The descriptions of the method and the results are not clear to me.

 - The benefits of the visualization are not clear from the results. In particular, I do not agree with the claim that "looking at the calibration-sharpness diagrams the differences between the two approaches becomes more clear."

 - The notation in some parts is a little confusing.

 - Some of the proofs lack details, and there are also some writing mistakes. These make the proofs a little difficult to follow.

### Questions
### Major comments
- Are some of the findings of this paper related to those of Prez-Lebel et al. (2023)?

Alexandre Perez-Lebel, Marine Le Morvan, and Gaël Varoquaux. BEYOND CALIBRATION: ESTIMATING THE GROUPING LOSS OF MODERN NEURAL NETWORKS. ICLR, 2023.

- Corollary 4.7 should be more formally stated.

- I could not understand the condition $d_{\phi}(x, y) \ge d_{\psi}(x_i, y_i)$.

- Is there any justification for thinking about the band proposed in lines 419-425? Also, the description here is not very clear to me despite its importance.

- There should be a part explaining how to read the plots. What are the read curves, red areas, and blue areas? Then, there should be explanations about how to evaluate them such as what kind of curves and areas are supposed to be good. Some explanations of them are mixed with the interpretations of the results, which is making the section difficult to read.

### Minor comments
- The notation in Eq. (2.1) feels strange. If $\mathbb{P}( \cdot | \cdot )$ denotes the regular conditional distribution, it should take an event in the first argument. It is also strange that it returns a vector, assuming $v \in \mathbb{R}^m$. Could the authors check the definition again?

- I think the sign is not correct in (A.1).

- The part of the proof obtaining (B.2) should be explained more clearly.

- The proof of Corollary C.1 could be more precise.

- Could the authors add a clear description about the standard reliability diagram?

- I suggest the authors explicitly explain all the acronyms in the paper.

### Soundness
3

### Presentation
2

### Contribution
2

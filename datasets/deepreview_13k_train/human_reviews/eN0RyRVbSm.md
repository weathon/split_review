# Double Descent Meets Out-of-Distribution Detection: Theoretical Insights and Empirical Analysis of the role of model complexity

- Decision: Reject
- Scores: 8, 6, 6, 6

## Abstract
While overparameterization is known to benefit generalization, its impact on Out-Of-Distribution (OOD) detection is less understood.
    This paper investigates the influence of model complexity in OOD detection.
    We propose an expected OOD risk metric to evaluate classifiers confidence on both training and OOD samples.
    Leveraging Random Matrix Theory, we derive bounds for the expected OOD risk of binary least-squares classifiers applied to Gaussian data.
    We show that the OOD risk depicts an infinite peak, when the number of parameters is equal to the number of samples, which we associate with the double descent phenomenon.
    Our experimental study on different OOD detection methods across multiple neural architectures extends our theoretical insights and highlights a double descent curve. 
    Our observations suggest that overparameterization does not necessarily lead to better OOD detection.
    Using the Neural Collapse framework, we provide insights to better understand this behavior.
    To facilitate reproducibility, our code will be made publicly available upon publication.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper investigates the influence of model complexity on Out-Of-Distribution (OOD) detection in machine learning models, with a specific focus on the double descent phenomenon. The authors propose a theoretical framework using Random Matrix Theory to explore OOD risks associated with binary least-squares classifiers on Gaussian data. The experimental analysis extends these theoretical insights across various neural network architectures, suggesting that overparameterization does not always enhance OOD detection.

### Strengths
- This paper provides a notable contribution by extending the concept of double descent, originally associated with generalization error, to OOD detection. This new perspective highlights a less explored aspect of model overparameterization, offering valuable insights into the robustness of overparameterized models.

- Theoretical contribution: The use of Random Matrix Theory to derive bounds for OOD risk offers valuable insights on understanding OOD detection in the over-paramterized regime.

- The experiments are quite comprehensive, particularly in the variety of OOD detection methods employed.

### Weaknesses
 - Adding the label noise (Line 305) is a bit artificial for real-world applications, probably also leads to different phenomenon in OOD detection. Is there any result on noiseless experiments for understanding the effect of model size for OOD detection?

- Could the authors provide additional remarks on connecting the derived theoretical results and the empirical OOD detection methods? E.g., is the derived lower bound in Theorem related to one/several of the practical OOD detection methods?

### Questions
See Weaknesses.

(Update: increased score from 6 to 8 after author rebuttal)

### Soundness
3

### Presentation
3

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
This paper examines the impact of model complexity on (supervised) out-of-distribution (OOD) detection, showing that, similar to in-distribution (ID) generalization, OOD detection exhibits a double descent behavior as models become overparameterized.

Theoretically, the authors show that, in a setup similar to Belkin et al. (2020), both ID and OOD detection risks follow a double descent pattern in linear least-squares regression. Empirically, they explore various datasets, architectures, and OOD detection techniques, showing that logit-based metrics produce a smoother double descent curve compared to feature-based ones. They also relate the improvement seen with overparameterization to improvements in neural collapse (NC) within the feature space.

### Strengths
The paper is written clearly. The authors discuss connections to previous work well and provide extensive experiments across various metrics, architectures, and datasets to support their claims.

### Weaknesses
The paper is written clearly. The authors discuss connections to previous work well and provide extensive experiments across various metrics, architectures, and datasets to support their claims.

(see below)

1.  Can you comment on the significance of your theoretical results? It seems that theorem 2 is a simple extension of theorem 1 applied to both ID and OOD distributions, and theorem 1 closely resembles theorem 1 in Belkin et al. (2020), with the addition of the activation function/non-linearity $\phi(\cdot)$ (as also acknowledged in the paper). But do you use $\phi(\cdot)$ to link OOD detection and overparameterization for your overall conclusion? In other words, without $\phi(\cdot)$, what is the technical challenge for extending theorem 1 in Belkin et al. (2020) to the OOD risk?

2.  Your theorem doesn’t specify assumptions on the OOD distribution. Would your theory provide any insights on how the expected behavior of the OOD risk might change with varying degrees of distributional shift between ID and OOD distributions?

3.  The trace operation in the NC1 metric is applied to $d\times d$ matrices ($d$ being the dimension of last-layer features). Thus, I suspect that the value of NC1 would be sensitive to changes in the value of $d$. Is the last-layer dimension in your experiments in both the under- and over-parameterized settings similar?  Or do you vary them as you increase the widths of the intermediate layers of the network? In the latter case, I am wondering if comparing the NC1 values when $d$ is different is fair. 

4.  The paper makes heuristic connections between how much over-parameterization improves OOD detection and how well the features align with ETF. ETF is only predictive of the last-layer's features' geometry if the training data is balanced (e.g., see [1]). Are all your training datasets balanced across classes?  If yes, would OOD detection under overparameterization behave differently if the training data were imbalanced?

### Questions
1.  Can you comment on the significance of your theoretical results? It seems that theorem 2 is a simple extension of theorem 1 applied to both ID and OOD distributions, and theorem 1 closely resembles theorem 1 in Belkin et al. (2020), with the addition of the activation function/non-linearity $\phi(\cdot)$ (as also acknowledged in the paper). But do you use $\phi(\cdot)$ to link OOD detection and overparameterization for your overall conclusion? In other words, without $\phi(\cdot)$, what is the technical challenge for extending theorem 1 in Belkin et al. (2020) to the OOD risk?

2.  Your theorem doesn’t specify assumptions on the OOD distribution. Would your theory provide any insights on how the expected behavior of the OOD risk might change with varying degrees of distributional shift between ID and OOD distributions?

3.  The trace operation in the NC1 metric is applied to $d\times d$ matrices ($d$ being the dimension of last-layer features). Thus, I suspect that the value of NC1 would be sensitive to changes in the value of $d$. Is the last-layer dimension in your experiments in both the under- and over-parameterized settings similar?  Or do you vary them as you increase the widths of the intermediate layers of the network? In the latter case, I am wondering if comparing the NC1 values when $d$ is different is fair. 

4.  The paper makes heuristic connections between how much over-parameterization improves OOD detection and how well the features align with ETF. ETF is only predictive of the last-layer's features' geometry if the training data is balanced (e.g., see [1]). Are all your training datasets balanced across classes?  If yes, would OOD detection under overparameterization behave differently if the training data were imbalanced?

[1] Thrampoulidis et al. "Imbalance trouble: Revisiting neural-collapse geometry." Advances in Neural Information Processing Systems 35 (2022)

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper investigates the influence of model complexity on the out-of-distribution (OOD) detection problem by examining its connection to the double descent phenomenon. Specifically, This paper proposes a novel OOD risk metric and establishes bounds for the excess risk of both test samples and OOD samples, assuming Gaussian data. Leveraging these theoretical findings, this paper demonstrates that the model achieves optimal performance when the number of parameters matches the number of samples. Extensive experiments have been conducted across multiple neural network architectures to validate their claims.

### Strengths
Overall, this paper presents a robust theoretical framework for analyzing the OOD detection problem and introduces a valid method supported by theoretical derivations and extensive numerical studies.

### Weaknesses
The main weakness lies in the strong assumptions on both the data and the model.

1. The model is a one-hidden-layer network with a single neuron.

2. The data is assumed to be Gaussian and isotropic. First, the Gaussian distribution may not reflect the real data application.

3. From lines 830 to 835, the nonlinear function is approximated by a linear function. However, the validity of this approximation is unclear—specifically, the conditions under which this approximation is valid and the rationale behind deriving it. Furthermore, this simplification may reduce the analysis to a purely linear case, potentially limiting the paper's contribution.

### Questions
(1) I feel that Eqn. (5) is unclear, as $z$ depends on $x$. The current format gives the impression that $z$ is fixed in both terms.

(2) Why Gaussian distribution is necessary for the proof?

(3) Could you provide more details for understanding remark 4.6? Also, how Theorems 1 & 2 are related to the OOD detection method?

### Soundness
2

### Presentation
3

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
This work focuses on exploring the Double Descent phenomenon in Out-of-Distribution (OOD) Detection. Theoretically, it proposes an expected OOD risk metric and, by leveraging Random Matrix Theory, establishes the relationship between OOD detection and the Double Descent phenomenon within a linear binary classification framework. Experimentally, the study conducts a comprehensive empirical investigation across various datasets and models. In the experiments, model complexity is indicated by different filter sizes, allowing for the observation of the Double Descent phenomenon in OOD detection under varying filter configurations. The conclusion is valid; however, the novelty of the work is not particularly significant.

### Strengths
1.	This work focuses on two recent cutting-edge concepts: OOD detection and the Double Descent phenomenon. Both concepts have significant implications for deep learning applications and the understanding of deep learning optimization.
2.	The paper provides clear and rigorous results for OOD detection and the Double Descent phenomenon.
3.	Both the theoretical and experimental results appear to be valid.

### Weaknesses
1.	Although the issues considered are cutting-edge concepts, I believe that the motivation presented is weak. The paper does not explore in depth the connections between these two concepts; it primarily provides derivations and experiments based on existing results. Maybe, the authors could discuss potential implications of their findings for model selection in OOD detection tasks, or to analyze how the double descent phenomenon might inform the design of more robust OOD detection methods.
2.	The motivation for expected OOD risk metric is unclear to me; I would appreciate a more detailed explanation. The authors could provide examples of how this metric might be used in practice, or to compare it with existing OOD detection metrics to highlight its unique contributions.
3.	Experimentally, the use of different filter sizes to represent model complexity is appropriate, but it also introduces certain limitations in the experimental results.

4.	In Section 5.2, the article states, “We report NC metrics, where lower values imply better performance in terms of both generalization and Out-of-Distribution (OOD) detection.” I find this statement insufficiently rigorous. While NC serves as a paradigm to illustrate the optimization process in deep learning, its lower values do not necessarily imply better performance regarding generalization. However, the authors carefully demonstrate the relationship between NC and generalization. Consequently, I remain skeptical of the authors' position and believe that this statement lacks the necessary rigor.
5.	I have concerns about the conclusion of Remark 4.1 of expected OOD risk metric. If the proposed expression (5) yields a lower value, it should not be possible to simultaneously derive conclusions (1) and (2). A more detailed explanation would be appreciated. I would appreciate a more detailed explanation.
6.	Since the Double Descent phenomenon is also based on a linear model, could the depth of the model be related to this phenomenon? Or does the model complexity mentioned in the context of Double Descent pertain solely to the model's width? Additionally, what is the relationship between the Double Descent phenomenon and the depth of the model?

### Questions
1.	In Section 5.2, the article states, “We report NC metrics, where lower values imply better performance in terms of both generalization and Out-of-Distribution (OOD) detection.” I find this statement insufficiently rigorous. While NC serves as a paradigm to illustrate the optimization process in deep learning, its lower values do not necessarily imply better performance regarding generalization. However, the authors carefully demonstrate the relationship between NC and generalization. Consequently, I remain skeptical of the authors' position and believe that this statement lacks the necessary rigor.
2.	I have concerns about the conclusion of Remark 4.1 of expected OOD risk metric. If the proposed expression (5) yields a lower value, it should not be possible to simultaneously derive conclusions (1) and (2). A more detailed explanation would be appreciated. I would appreciate a more detailed explanation.
3.	Since the Double Descent phenomenon is also based on a linear model, could the depth of the model be related to this phenomenon? Or does the model complexity mentioned in the context of Double Descent pertain solely to the model's width? Additionally, what is the relationship between the Double Descent phenomenon and the depth of the model?
4.	Please refer to “Weaknesses”.

### Soundness
2

### Presentation
3

### Contribution
2

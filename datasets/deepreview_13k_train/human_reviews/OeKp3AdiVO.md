# Rethinking Classifier Re-Training in Long-Tailed Recognition: A Simple Logits Retargeting Approach

- Decision: Accept
- Scores: 6, 5, 6, 8

## Abstract
In the long-tailed recognition field, the Decoupled Training paradigm has demonstrated remarkable capabilities among various methods. This paradigm decouples the training process into separate representation learning and classifier re-training. Previous works have attempted to improve both stages simultaneously, making it difficult to isolate the effect of classifier re-training. Furthermore, recent empirical studies have demonstrated that simple regularization can yield strong feature representations, emphasizing the need to reassess existing classifier re-training methods. In this study, we revisit classifier re-training methods based on a unified feature representation and re-evaluate their performances. We propose a new metric called Logits Magnitude as a superior measure of model performance, replacing the commonly used Weight Norm. However, since it is hard to directly optimize the new metric during training, we introduce a suitable approximate invariant called Regularized Standard Deviation. Based on the two newly proposed metrics, we prove that reducing the absolute value of Logits Magnitude when it is nearly balanced can effectively decrease errors and disturbances during training, leading to better model performance. Motivated by these findings, we develop a simple logits retargeting approach (LORT) without the requirement of prior knowledge of the number of samples per class. LORT divides the original one-hot label into small true label probabilities and large negative label probabilities distributed across each class. Our method achieves state-of-the-art performance on various imbalanced datasets, including CIFAR100-LT, ImageNet-LT, and iNaturalist2018.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper revisits the two-stage learning paradigm in long-tailed recognition and proposes two metrics, Logits Magnitude, and Regularized Standard Deviation, to compare different classifier re-training methods. Moreover, it develops a label over-smoothing approach to improve model performance. Experimental results on multiple long-tailed datasets demonstrate the effectiveness of the proposed method.

### Strengths
- This paper reveals some shortages in previous metrics, such as the ignoration of feature magnitude.

- The proposed label over-smoothing is interesting. Both theoretical and empirical results demonstrate the effectiveness.

- The proposed LOS outperforms most compared methods on multiple datasets. The ablation studies are well done.

### Weaknesses
 - Figure 1 is hard to follow. What do the red and blue lines mean? Why do they obey Gaussian distributions? More explanations are required.

- Since the feature magnitude and the class weight norm both have effects on prediction results, why not directly use the Cosine classifier? The Cosine classifier is quite simple and effective, which calculates Cosine similarities between the normalized features and the normalized class weights, and then divides it by a temperature to obtain the final logits. Therefore, it can directly mitigate the impact of feature magnitude. (Well, maybe the logit magnitude is different from the feature magnitude, but I suggest the authors include the Cosine classifier as a baseline.)

- Despite the superior performance. Some recent works are ignored and not compared. For example, RIDE, BCL, NCL, GML.

- The references are outdated. Among the 50 cited papers, there are no papers from 2024, only 3 papers from 2023, and 4 papers from 2022.

- Please pay attention to the format of the references. Some do not include the source (e.g. Peifeng et al., 2023); some have a URL (Huang et al., 2018) but others do not; some source names are inconsistent (e.g. "Computer Vision-ECCV ..." or "Proceedings of ... (ECCV)"? and "arXiv preprint" or "ArXiv, abs/..." or "arXiv e-prints"?)

### Questions
See "Weaknesses".

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper revisits the paradigm of classifier re-training in the context of long-tailed recognition and proposes two metrics for analyzing the efficacy of classifiers: logits magnitude (LoMa) and regularized standard deviation. Various existing methods for LTR are re-evaluated with a unified feature representation and with respect to the proposed metrics. They further use a variant of label smoothing where very strong smoothing is used to achieve better performance. Results and ablation studies are reported on multiple benchmark LTR datasets.

### Strengths
1. The performance of various methods seems to somewhat correlate to the proposed metrics.
2. The proposed method outperforms prior arts on multiple benchmarks in most of the evaluated settings.
3. The over-smoothing technique can be used as a plugin on top of existing methods.

### Weaknesses
1. The proposed LoMa metric is hard to understand due to ambiguous language and notation. The authors should use two indices in the subscript of the logits to differentiate between sample and class. In Fig. 2 it is unclear what true samples and non-true samples are. It is not clear how the mean logits are computed, specifically, if the mean is taken across samples or across classes. The definition of LoMa as the difference between these two means is also not clearly motivated. 
2. While the authors claim it is hard to optimize directly for LoMa or Regularized Standard Deviation, they don't propose any way to do this. The suggested label smoothing approach doesn't directly fit into the story of achieving uniform LoMa. It's unclear how label smoothing, which modifies the training objective, directly addresses the issue of optimizing for LoMa or RSD.
3. There are wild claims made, for instance, that classifier weight norm cannot capture a method's efficacy due to potential arbitrary lengths (Proposition 2). It is relative weight norm that matters, not absolute, thus rendering Prop. 2 meaningless. Section 3.1 on the deep dive into LoMa seems like a rambling section without concrete takeaways. The discussion lacks a clear connection to the proposed method and doesn't provide actionable insights.
4. The math in the paper could be improved. For instance, in Eq. 9, the expectation can't be decomposed like that, it looks artificial. The assumption that the terms are independent is not justified, and the approximation is not rigorously derived. The lack of clarity in the mathematical derivations undermines the validity of the analysis.
5. The proposed (over) label smoothing technique is just a minor variant of prior work. The novelty of using a higher smoothing factor is not sufficiently justified, and the connection to the long-tailed problem is not clearly established.

### Questions
Please address the points in weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a simple but effective method for long-tailed problem. They base their method in decoupled ones and first propose two new metrics, Logits Magnitude and Regularized Standard Deviation, to compare the differences and similarities between various methods. Then, they propose a simple method by softening the original one-hot labels by assigning a probability slightly higher than $1/K$ to the true class and slightly lower than $1/K$ to the other classes, where $K$ is the number of classes. In the method, they also provide the detailed analysis how the method is designed. In the experiments, the results validate the effectiveness of proposed method.

### Strengths
(1) The structure of this paper is clear, starting from the definition of problem, the background motivation and analysis to the final implementation.

(2) The experiments are good. By applying the proposed method to some existing methods, their performances can be further improved.

### Weaknesses
Although the structure is clear, the transition from last part to the next can be further improved.

Some of the explanations are also missed. See below.

(1) In Proposition 1. It is said " In all cross-entropy based methods, the aforementioned conclusion remains valid", in deep learning networks, the objective is always a non-convex optimization problem, how the conclusion is still valid in this case?

(2) The Proposition 1 is used to exclude the effect of b and to introduce Proposition 2 which illustrates that the weight norm-based method may not be reliable in some cases, am I right? But how the equation (4) is obtained? from s' to s.

(3) From line 313-314, how the assumption is determined" Consider random perturbations ∆i that independently affect each class zi and are proportional to the standard deviation of their logits, i.e., z′"?? It is said "These perturbations ∆ are commonly introduced during the training process, particularly due to factors such as overfitting in the initial stage of training and bias in the sampling of the training set.", can you clarify more on this point?

(4) if the point lies in $\Delta$ and $\sigma$ in section 3.1, what is the point to introduce definition 2?? The point in definition 2 shoule be $R_i$, right?

(5) Figure 1 is also not easy to understand for the first time until figure 2 is given.

Typo: (1) Is the parenthesis missed in line 107?

### Questions
I tried to understand the logic and the details of this paper, so some of the points in the paper require further clarification:

(1) In Proposition 1. It is said " In all cross-entropy based methods, the aforementioned conclusion remains valid", in deep learning networks, the objective is always a non-convex optimization problem, how the conclusion is still valid in this case?

(2) The Proposition 1 is used to exclude the effect of b and to introduce Proposition 2 which illustrates that the weight norm-based method may not be reliable in some cases, am I right? But how the equation (4) is obtained? from s' to s.

(3) From line 313-314, how the assumption is determined" Consider random perturbations ∆i that independently affect each class zi and are proportional to the standard deviation of their logits, i.e., z′"?? It is said "These perturbations ∆ are commonly introduced during the training process, particularly due to factors such as overfitting in the initial stage of training and bias in the sampling of the training set.", can you clarify more on this point?

(4) if the point lies in $\Delta$ and $\sigma$ in section 3.1, what is the point to introduce definition 2?? The point in definition 2 shoule be $R_i$, right?

(5) Figure 1 is also not easy to understand for the first time until figure 2 is given.

Typo: (1) Is the parenthesis missed in line 107?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper revisits the classifier re-training in long-tailed recognition, proposing a simple label over-smoothing approach to balance the logits magnitude across classes. The method achieves state-of-the-art performance on various imbalanced datasets.

### Strengths
1. The method is simple, using basic label smoothing to effectively reduce overfitting.
1. Theoretical analysis and experimental validation are comprehensive, demonstrating the method's effectiveness across various datasets.

### Weaknesses
There are no significant methodological drawbacks. It is recommended that the authors include comparisons with the latest SOTA methods^[1] and discuss related works^[2,3].

### Questions
See the weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
3

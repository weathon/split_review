# Fixed Non-negative Orthogonal Classifier: Inducing Zero-mean Neural Collapse with Feature Dimension Separation

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 6, 5

## Abstract
Fixed classifiers in neural networks for classification problems have demonstrated cost efficiency and even outperformed learnable classifiers in some popular benchmarks when incorporating orthogonality. Despite these advantages, prior research has yet to investigate the training dynamics of fixed orthogonal classifiers on neural collapse, a recently clarified phenomenon that last-layer features converge to a specific form, called simplex ETF, in training classification models involving the post-zero-error phase. Ensuring this phenomenon is critical for obtaining global optimality in a layer-peeled model, potentially leading to enhanced performance in practice. However, fixed orthogonal classifiers cannot invoke neural collapse due to their geometric limitations. To overcome the limits, we analyze a $\textit{zero-mean neural collapse}$ considering the orthogonality in non-negative Euclidean space. Then, we propose a $\textit{fixed non-negative orthogonal classifier}$ that induces the optimal solution and maximizes the margin of an orthogonal layer-peeled model by satisfying the properties of zero-mean neural collapse. Building on this foundation, we exploit a $\textit{feature dimension separation}$ effect inherent in our classifier for further purposes: (1) enhances softmax masking by mitigating feature interference in continual learning and (2) tackles the limitations of mixup on the hypersphere in imbalanced learning. We conducted comprehensive experiments on various datasets and architectures and demonstrated significant performance improvements.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper delves into the phenomenon of neural collapse, specifically in scenarios with fixed classifiers composed of orthogonal class prototypes. A central assertion of the paper is that neural collapse manifests differently when the classifier is fixed. To address this, the concept of 'zero-mean neural collapse' is introduced. This approach redefines neural collapse by centering class means to the origin in non-negative Euclidean space, rather than to their global mean. The occurrence of Zero-mean Neural Collapse (ZNC) is observed when the orthogonal Layer Peeled Model (LPM) achieves global optimality, simultaneously inducing a max-margin in decision-making. The paper further explores the implications of this phenomenon in the contexts of continual learning and imbalanced learning.

### Strengths
The paper poses an interesting problem and a good methodological choice for the substantiation of its main intentions. The work includes a comprehensive part of experiments across diverse contexts and with datasets the introduction and the related works are rich of interesting information and insights.

### Weaknesses
The manuscript's writing and structure require refinement for better clarity and flow.
The concepts of masking in continual learning and mixup in imbalanced learning emerge unexpectedly within the text and would benefit from a better introduction with an improved link with neural collapse.

The introduction and related work sections could be condensed to allow for a more comprehensive introduction of Section 6.

The significance of Zero-mean Neural Collapse (ZNC) in non-negative Euclidean space (i.e., the positive hyper-octant) is not immediately apparent. The paper should clarify whether its importance is solely due to the optimality shown in the LPM model or if there are additional factors which are outside the proof. The rationale behind constraining the representation space to the positive hyper-octant warrants further explanation.

The nature of the problem posed by the LPM model is not shown. The manuscript should specify whether it is linear, non-linear, or solvable by known matrix factorization techniques. Moreover, the discussion on the complexity of providing values for W is insufficiently developed, leaving the reader questioning where the complexity of the problem truly lies.

Could the authors provide insight into why LPM optimality does not manifest in the case of a regular fixed d-simplex, and conversely, why it appears to be present in the context of Zero-mean Neural Collapse (ZNC)?

The visual clarity and structural coherence of Figure 1 could be enhanced to better convey the intended information.

The tables detailing experimental results should more clearly differentiate the methodologies used, to avoid confusion. The complex nomenclature, such as FNODERMR++, could be simplified for better clarity.

In Remark 1 at the end of section 5, the statement regarding the inability of a fixed orthogonal classifier to address neural collapse needs further clarification. A more detailed explanation could help in understanding this assertion.

### Questions
Weaknesses and questions are grouped above to assist in the association and subsequent discussion of the issues.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces the Fixed Non-negative Orthogonal Classifier (FNO), which is a novel approach to address the issue of neural collapse in training classification models. The authors propose the concept of zero-mean neural collapse, where the class means are centered at the origin instead of their global mean. The paper empirically validates the effectiveness of these methods in tasks such as continual learning and imbalanced learning.

### Strengths
- The paper introduces a novel Fixed Non-negative Orthogonal Classifier (FNO classifier) and proposes the concept of zero-mean neural collapse. This combination of ideas is interesting.

- The paper provides theoretical analysis of the FNO classifier and proves its benefits in terms of inducing zero-mean neural collapse. The experimental results demonstrate the effectiveness of the FNO classifier in both continual learning and imbalanced learning scenarios.

- The paper is well-structured and clearly explains the motivation, methodology, and results

### Weaknesses
 - The experiments in the paper are limited to continual and imbalanced learning scenarios for the FNO classifier. It would be beneficial to see how the FNO classifier performs compared to the ETF classifier in standard classification tasks. Additionally, in Table 4, which details the imbalanced learning experiments, the ETF classifier is absent from the comparison. Including it could provide a more comprehensive evaluation of the FNO classifier's performance.

- A related work is missing for discussion. The orthogonality of the classifier in NC is explored funder MSE loss:

Zhou, Jinxin, et al. "On the optimization landscape of neural collapse under mse loss: Global optimality with unconstrained features." International Conference on Machine Learning. PMLR, 2022.

For a full comparison, we may also want to consider the incorporation of MSE loss within the ETF classifier, which is guaranteed to be orthogonal classifier (assuming no bias)

### Questions
See the weaknesses part above

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The study delves into the intricacies of "Fixed Non-negative Orthogonal Classifiers" in the realm of neural networks, emphasizing their potential in inducing "Zero-mean Neural Collapse." While fixed classifiers have historically demonstrated cost-effectiveness and even outperformed learnable ones with orthogonality, their behavior in the context of neural collapse—a phenomenon where last-layer features align to a specific form, the simplex ETF—remains underexplored. Addressing this, the paper pioneers the idea of zero-mean neural collapse within a non-negative Euclidean space and presents a novel classifier that optimally triggers this collapse. This innovation not only maximizes the margin of an orthogonal layer-peeled model but also enhances performance in continual and imbalanced learning scenarios. Through rigorous experimentation, the authors substantiate their findings, showcasing marked performance enhancements.

### Strengths
1. Effectiveness: The proposed methods improve the performance in long-tailed learning.
2. Clarity: Overall, the paper is well-written and easy to follow. Besides, the main theoretical result (Theorem 1) is clear and correct.

### Weaknesses
1. My main concern is the necessity of the new theory. The main result (Theorem 1) shares a similar formulation with Lemma 4.1 in [1], showing the zero-mean is unnecessary to achieve the neural collapse. Specifically, both results demonstrate a form of equidistribution of class means around a central point. While the paper introduces the concept of "zero-mean neural collapse," its practical advantage over the standard neural collapse as described in [1] is not clearly established. More empirical or theoretical evidence is needed to justify the need for this new definition.
2. Although the proposed methods are effective in the experiments, the connections between the theoretical analysis and the practical implementation seem unclear. For instance, how does Theorem 1 directly inform the design of the Fixed Non-negative Orthogonal (FNO) classifier? A more explicit link between the theoretical findings and the algorithmic choices would strengthen the paper.
3. The paper states that orthogonality is accessible when $d \leq K$. However, in many practical scenarios, especially in deep learning, the feature dimension $d$ often exceeds the number of classes $K$. A discussion on the implications of $d > K$ for the proposed method and potential workarounds or limitations in this regime would be valuable.
4. While the paper presents experimental results on long-tailed learning, the comparison is limited. Including more competitors, particularly on ImageNet-LT and Places-LT, would provide a more comprehensive evaluation of the proposed method's effectiveness. For instance, comparing with methods specifically designed for long-tailed learning on these large-scale datasets would be beneficial.

### Questions
Please refer to the weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The article introduces the concept of a "Fixed Non-negative Orthogonal Classifier" and its relationship with the phenomenon of "Zero-mean Neural Collapse." Fixed classifiers in neural networks have shown cost efficiency and even surpassed learnable classifiers in certain benchmarks when incorporating orthogonality. However, the dynamics of fixed orthogonal classifiers concerning neural collapse, where last-layer features converge to a specific form called simplex ETF during training, have not been deeply explored. This paper addresses this gap by introducing the concept of zero-mean neural collapse in non-negative Euclidean space. The authors propose a fixed non-negative orthogonal classifier that optimally induces this collapse, maximizing the margin of an orthogonal layer-peeled model. This classifier also offers advantages in continual learning and imbalanced learning by separating the last-layer feature dimensions. The paper provides comprehensive experiments to validate its claims, demonstrating significant performance improvements.

### Strengths
+ 1. The article is well-structured, logically sound, and skillfully written.
+ 2. This paper conduct extensive experiments to justify *zero-mean neural collapse*, which combines the orthogonality and neural collapse.

### Weaknesses
 The problem that I'm concerned about most is **unclear motivation**. Authors mentioned in the introduction: 
*However, neural collapse differently occurs in the fixed orthogonal classifier due to their limitations from geometrical feature: orthogonality.* So, I have two questions, authors should provide more discussions to demonstrate the meaning in the main text: 
  + Why do we have to fix classifier as an orthogonal matrix ?
  + Why studying neural collapse with fixed orthogonal classifier is necessary ?

### Questions
Does Remark.1 claim that zero-mean neural collapse can achieve max-margin? Consider the binary class classication, the max-margin feature should be Digon, which has the larger angle (180 degrees) than orthogonality (90 degrees).

By the way, the case that D > K is interesting. Authors can refer to [1] and [2].

[1] https://en.wikipedia.org/wiki/Thomson_problem

[2] https://arxiv.org/abs/2310.05351

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

# On the Out-of-Distribution Generalization of Self-Supervised Learning

- Decision: Reject
- Scores: 5, 6, 6

## Abstract
In this paper, we focus on the out-of-distribution (OOD) generalization of self-supervised learning (SSL). By analyzing the mini-batch construction during SSL training phase, we first give one plausible explanation for SSL having OOD generalization. Then, from the perspective of data generation and causal inference, we analyze and conclude that SSL learns spurious correlations during the training process, which leads to a reduction in OOD generalization. To address this issue, we propose a post-intervention distribution (PID) grounded in the Structural Causal Model. PID offers a scenario where the relationships between variables are free from the influence of spurious correlations. Besides, we demonstrate that if each mini-batch during SSL training satisfies PID, the resulting SSL model can achieve optimal worst-case OOD performance. This motivates us to develop a batch sampling strategy that enforces PID constraints through the learning of a latent variable model. Through theoretical analysis, we demonstrate the identifiability of the latent variable model and validate the effectiveness of the proposed sampling strategy. Experiments conducted on various downstream OOD tasks demonstrate the effectiveness of the proposed sampling strategy.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper inspects SSL from a causal perspective, which assumes a SCM for generating augmentations in both generative and discriminative approaches. To address spurious correlations between images and their non-semantic features, e.g., backgrounds and styles, the paper proposes rebalancing the training batches by sampling to decorrelate images from their non-semantic features.  Experiments show enhanced performances across various existing SSL methods.

### Strengths
1. The proposed rebalancing technique can be embedded into general SSL procedures, whether discriminative or generative, allowing for wide applicability.

2. Experiments are extensive in scope, covering both discriminative and generative SSL (appendix). Multiple learning tasks under distribution shift is considered, including semi-supervised, transfer learning and few-shot learning. A clear improvement of around 3% in accuracy is reported for most results.

### Weaknesses
In general, I am not convinced that the proposed SCM for generating augmentation, especially the characterization of spurious correlation, is relevant for OOD generalization of SSL. 

1. The proposed SCM and the rebalancing strategy does not address the identifiability of spurious variables in the context of SSL. Spurious variables $s$ in supervised machine learning are the variables rejected by the conditional independence test $Y \perp e | s$, where $e$ is the group label. However, spurious variables are generally not identifiable without labels.  Literature has introduced inductive bias, e.g., simplicity bias, to identify spurious variables for SSL [1]. However, the SCM in the paper does not consider similar assumptions to address the identifiability of $s$. For example, in Figure 1(b), $s$ and $x^{label}$ (raw image) hold symmetric roles in the SCM. Since $s$ is learned as a latent variable by variational inference, there can be infinitely many solutions of $s$.  The identifiability results in Theorem 4.3 does not resolve the identifiablity of $s$, because it depends on the condition that $p(x^+|x^{label},s)$ is learned, implying $s$ has been identified.
2. The conditional independence implied by the SCMs may not reflect practice in SSL.  The PID SCM in Fig.3 models the statistical independence between styles or backgrounds (s) and images ($X^{label}$), but the style and background can be directly identified from the image in practice. In general, $s$ is always measurable with respect to $X^{label}$. Similarly, both $X^{label}$ and $s$ are direct causes of $X^{+}$ in Fig.2, which is also inconsistent to the augmentation practice that takes as input the raw images only, since the background is just part of the raw image. Does this paper consider a special augmentation procedure? 
3. I identify a gap between self-supervised representation learning, whose target is $p(X^{label})$, and the models used in theory. The binary classification model in Proposition 3.1 learns the density ratio $p(X^{label})/p(X^{+})$, and the "alignment" model in Theroem 3.4 learns $p(X^{label}|p^{+})$. The paper has not addressed that a non-spurious classification model or "alignment" model implies a non-spurious generative model. A simple counterexample: assume that the augmentation procedure retains the style of the image. The classifier does not depend on the style to distinguish between anchor and augmentations because they share the same style. However, styles can still be learned by the generative model.

Moreover, I think this paper can be substantially improved in writing for its message to be more effectively conveyed.

4. Some concepts and statements are not well defined and formulated. 
   - The "task distribution" is not defined. In L131-132, a statement is made that "this framework involves estimating the true task distribution from discrete training tasks, enabling the SSL model to generalize to new, unseen tasks (i.e., test tasks)." Is task modeled as a random variable? What does task correspond to in the SCM? For example, if task refers to batch index in Fig.2(b), then generalization is essentially impossible because training and test batch indices do not overlap. If task refers to batches of X in Fig.2(b), than generalization is only possible when the image batches are i.i.d., which is irrelevant to OOD generalization. In L157, the author states that s, denoting the style or background, does not contain any causal semantics related to the task. This statement contradicts the SCM in Fig 1 as well, where s is a direct cause of X+. Therefore, the definition of "task" is more vague here.
   - What does the statement mean that "$x^{label}$ is regarded as the label" (L245), since $x^{label}$ is the raw image? A formulation of this equivalence may help improve clarity.
5. Models, assumptions and theorem statements are not explicitly presented.
   - I understand the benefits for deferring formal theorem statements to the appendix. However, the formal statement of Proposition 3.1 is missing in both the main text and the appendix. The assumption of mixture of gaussians, balanced labels, equal dimensions between spurious variables and images, and the model of binary classification are all woven into the proof.
   - This paper models the SSL procedure by two parts: a classification model and a conditional generative alignment model. The formulation of the classification model is mixed in the proof.  The alignment model is not formulated until Theorem 3.4. However, since the learning procedure is repeatedly mentioned throughout the theory, I suggest a clear statement of the models at the beginning.
6. Multiple notations are unexplained.
   - The notation  $L^{PID}$ in L225 is vague because PID is a family of distributions. Which distribution is the loss evaluated with respect to? 
   - Similarly, $\perp_{PI}$ in L217 is also unexplained. Is the independence condition satisfied for all PI distributions?
   - nu in L313 and mu in L315, 333.
7. The implication of the identifiability result in Theorem 4.3 is insufficiently addressed. Also related to the first point, what does the equivalance in Definition 4.2 imply for the identiability of spurious variables, and more importantly, the generative model?

Minor points:

8. Experiments are in relatively small scale. The results are presented for Imagenet-100 instead of the more popular ImageNet-1k. Models are trained with a limited number of epochs.
9. There has been theoretical and empirical analysis of the vulnerability of SSL to spurious correlation, e.g., in [1]. Related work on spurious correlation in SSL can be reviewed to establish the paper's position in the broader literature.

### Questions
1. Why does $f^\star$ maximize the loss function in L225, since the proof indicates minimization instead?

### Soundness
2

### Presentation
2

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
This paper introduces a training batch sampling strategy designed to enhance self-supervised learning and improve generalization beyond the training distribution. The approach is inspired by the concept of invariant causal structure across different environments: while causal relationships between features and labels remain consistent, spurious correlations vary across environments. The proposed methodology employs a constraint, PID, during mini-batch sampling, which disregards spurious correlations and supports out-of-distribution generalization.

### Strengths
The main strength of the paper lies

### Weaknesses
At times, the presentation is overly technical or abstract, which might be challenging for practitioners who seek to grasp the main insights of the paper. The core message is to introduce a sampling strategy combined with a distributional constraint (PID) that encourages the self-supervised method to disregard correlations that change across domains and focus on stable, causal correlations. The objective is to enhance out-of-distribution generalization by learning these invariant structures. Adding a non-technical explanation, perhaps as a remark, on how the algorithm achieves PID enforcement would be beneficial. Please refer to my questions below for further clarification.

There are also a few concerns/typos that need to be taken care of for better readability:

1. In Algorithm 1, the steps, especially the count of i, seem to be a bit confusing. It may be better to write: "Set $i \leftarrow 0$", and select the initial pair $(x_0^+, x_0^{\rm label})$. Then, for $i \ge 1$, write the two steps and finally add, "Set $i \leftarrow i + 1$".

2. The number of samples mu should be $\mu$, I guess?

3. It seems that the definition of PID is the same as assuming $x^{\rm label}$ and $s$ are independent. Maybe it would be easier to present it that way.

4. What is $\mathcal{L}^{\rm PID}$? Is it $\mathcal{L}^{\rm e}, e \in \mathcal{D}$ where $e$ satisfies PID? How is $f$ related to $F$ in Equation (1)? Is $f$ a generic function in the class of hypothesis and $F$ the true generating function?

5. Are we assuming that minimizer $f^*$ is same for all distributions in $\mathcal{D}$ that satisfies PID?

6. I am a little bit confused about Assumption 3.3. In PID, we have $x^{\rm label}$ is independent of $s$, whereas in Assumption 3.3, we also have $x^{\rm label}$ is independent of $s$ given $x^+$. Are we assuming Assumption 3.3 for all distributions in $\mathcal{D}$? A remark with some intuitive explanation of Theorem 3.4 would be helpful.

### Questions
There are also a few concerns/typos that need to be taken care of for better readability: 

1. In Algorithm 1, the steps, especially the count of i, seem to be a bit confusing. It may be better to write: "Set $i \leftarrow 0$", and select the initial pair $(x_0^+, x_0^{\rm label})$. Then, for $i \ge 1$, write the two steps and finally add, "Set $i \leftarrow i + 1$". 

2. The number of samples mu should be $\mu$, I guess? 

3. It seems that the definition of PID is the same as assuming $x^{\rm label}$ and $s$ are independent. Maybe it would be easier to present it that way. 

4. What is $\mathcal{L}^{\rm PID}$? Is it $\mathcal{L}^{\rm e}, e \in \mathcal{D}$ where $e$ satisfies PID? How is $f$ related to $F$ in Equation (1)? Is $f$ a generic function in the class of hypothesis and $F$ the true generating function? 

5. Are we assuming that minimizer $f^*$ is same for all distributions in $\mathcal{D}$ that satisfies PID? 

6. I am a little bit confused about Assumption 3.3. In PID, we have $x^{\rm label}$ is independent of $s$, whereas in Assumption 3.3, we also have $x^{\rm label}$ is independent of $s$ given $x^+$. Are we assuming Assumption 3.3 for all distributions in $\mathcal{D}$? A remark with some intuitive explanation of Theorem 3.4 would be helpful.

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
3

### Summary
This paper regards the mini-batches in the SSL training as the environments (domains) in OOD generalization problems and proposes that each mini-batch can be viewed as a multi-class classification task. Based on this formulation, the authors points out that when the similarity is measured using non-causal features, SSL will learn spurious representations. To address this issue, the authors propose to model the Post-Intervention Distribution (PID) using VAEs for each mini-batch and further propose a mini-batch sampling strategy that selects samples with similar balancing scores based on the  $p^e(s|x^{label})$ learned by the VAE. The experiments demonstrat the effectiveness of the method.

### Strengths
1. The perspective of converting the SSL training to a domain-generalization-like problem using an SCM is natrual and interesting.
2. The proposed method is built with theoretical guarantees on the identifiability of the distribution parameters and the recover of the PID.
3. The experiments cover many scenarios, including semi-supervised learning, transfer learning, and few-shot learning tasks. The improvements of the proposed method are significant.

### Weaknesses
1. Some points are not quite clear and need further clarification. For example, despite Theorem 4.7, it is a bit confusing that why sampling samples with the same propensity score would help to recover $p^{PI}$. It would be better to provide some high-level explanations. The connection between the balancing score and the post-intervention distribution (PID) is not sufficiently clear. Specifically, it is not intuitive why matching samples based on the balancing score, which is derived from a learned conditional distribution $p(s|x^{label})$, would lead to a mini-batch that effectively approximates the PID. A more detailed explanation of how this score relates to the causal mechanisms and how it ensures the mini-batch is free from spurious correlations would be beneficial.
2. The authors didn't evaluate their method on classic OOD tasks like PACS, OfficeHome, ColoredMNIST, etc. Since this work aims to improve SSL's OOD performance, it would be necessary to evaluate these tasks. Otherwise, the author should explain why not doing so. The lack of evaluation on standard OOD benchmarks makes it difficult to assess the generalizability of the proposed method. While the paper includes transfer learning experiments, these do not fully capture the challenges of domain generalization as presented in datasets like PACS or OfficeHome, where the domain shift is more pronounced and the goal is to generalize to a completely unseen domain. The absence of these evaluations limits the ability to compare the method against existing OOD techniques.

### Questions
1. Could you shed light on why using an exponential family distribution to model $p(s|x^{label})$?
2. In line 227, how does Theorem 3.4 "implies that when $\mathcal{D}$ is sufficiently large and diverse, an optimal $f^*$ trained on one distribution will perform worse than random guessing in some other environment."?
3. In line 459, why "We can observe that the performance of BYOL rapidly deteriorates with batch size."? It seems that BYOL suffers from smaller performance degradation than BYOL+ours.
4. In line 267, should it be $T_{ij}=a_{ij}\times \cdot$?

### Soundness
3

### Presentation
2

### Contribution
3

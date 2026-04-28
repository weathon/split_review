# Blind Unlearning: Unlearning Without a Forget Set

- Decision: Reject
- Avg Score: 3.60
- Scores: 3, 3, 6, 3, 3

## Abstract
Machine unlearning is the study of methods to efficiently remove the influence
of some subset of the training data from the parameters of a previously-trained
model. Existing methods typically require direct access to the “forget set” – the
subset of training data to be forgotten by the model. This limitation impedes privacy, as organizations need to retain user data for the sake of unlearning when a
request for deletion is made, rather than being able to delete it immediately. We
first introduce the setting of blind unlearning – unlearning without explicit access
to the forget set. Then, we propose a method for approximate unlearning called
RELOAD, that leverages ideas from gradient-based unlearning and neural network
sparsity to achieve blind unlearning. The method serially applies an ascent step
with targeted parameter re-initialization and fine-tuning, and on empirical unlearning tasks, RELOAD often approximates the behaviour of a from-scratch retrained
model better than approaches that leverage the forget set. Finally, we extend the
blind unlearning setting to blind remedial learning, the task of efficiently updating
a previously-trained model to an amended dataset.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes the setting of Blind unlearning. In short this setting deals with cases when the unlearning algorithm does not have access to the forget set but to some other information. The proposed algorithm in the paper requires access to the retain set, the trained model, and multiple gradient checkpoints. In essence the paper does gradient ascent on the forget set where the gradients on the forget set are computed by taking the difference of the gradients on the full set (checkpoints) and gradients on the retain set (can be computed ). The paper also proposes the setting of reemdial unlearning which also requires access to the "clean" dataset that can remedy the unlearned dataset.

### Strengths
The paper looks at the problem of unlearning without full access to the forget set. The algorithmic techniques combine few different ideas already present in the literature in a clean way - checkpointing, gradient ascent, and sparsity.

The concept of blind unlearning, where the unlearner does not have full access to the forget set could be an interesting setting to consider.

I also appreciated that the authors decided to evaluate on several metrics and across a wide array of baseline algorithms for unlearning.

### Weaknesses
There are three main weakness of the paper which I believe makes the paper unsuitable for publishing at its current stage.

1. __Theoretical claims__ There are multiple issues with the theoretical claims of the paper and unless I have misunderstood them (pleasr correct me if I am wrong), I dont think they are fixable without significantly altering the contributions of the paper.
    * The definition of _recoverability_ says is that if $f$ is injective then all datasets $D$ are recoverable. This does not mean that if $f$ is not injective then no D is recoverable. it may be possible that some Ds are recoverable.
    * The paper looks at _exact recoverability_ which may be not only be unrealistic in practice but also an unnecessarily high bar. it is often impossible to exactly recover training data points but recover them to a high degree. As such, there should be a notion of approx. recovery.
    * The theoretical intuition behind the algorithm is that the gradients on the forget set can be approximated by the difference of the gradients in the full dataset and the retain set. However, these are only true for the check point parameters save and it is difficult to argue (not done in the paper) why they should be similar after some gradient ascent steps are done.
2. _Lack of diversity of experimental results and comparisons in known baselines_ Previous works including pawelczyk et. al. and Goel et. al. have considered many relevant experimental baselines which this work must also look at.
    * For unlearning, consider the IC test in Goel et. al. and the targeted, indiscriminate, and gaussian data poisoning attacks in Pawelczyk et. al.
    * For remedial unlearning, it is easy enough to adapt the above test by using clean data points.
    * The experiments only use ResNet18 and VGG on CIFAR10 and CIFAR100. These are not sufficient to make generalisable claims especially when the paper is empirical in nature.
    In general these two papers should be discussed as relevant existing work.
3. My final relatively milder criticism is that I do not see the motivation for when this setting is realistic. When is it that the learner only has access to a large retain set (90% of the dataset), multiple gradient checkpoints during training, but not the forget set. This selectively requires the learner to not have the forget set but have all these other memory intensive data structures.

### Questions
1. SSD results look unrealistic. The accuracy seems to be 1% on CIFAR100 which is the trivial accuracy. Previous results with SSD have shown much better performance on clean test acuracy with SSD. It appears the hyper-param optimisation may not have been executed properly.
2. for MIA, what is the reported number ? Is it a fraction between 0 and 1 or a percentage between 0 and 100 (like the other columns). This number appears too low if its a percentage to be meaningful. Can the authors report AUC instead ?
3. Clarify the weaknesses above.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper addresses a critical and well-motivated setting in recent machine unlearning research: unlearning without explicit access to the forget set, termed "blind unlearning" by the authors. The paper introduces an approximate unlearning method called RELOAD, which combines a single step of gradient ascent with a selective re-initialization procedure. Additionally, the RELOAD method can be extended to a remedial learning setting, which generalizes the classical unlearning problem and aims to efficiently update a previously trained model to accommodate an amended dataset.

### Strengths
S1. The problem of "unlearning without explicit access to the forget set" is well-motivated and has attracted significant attention.

S2. The "remedial learning" setting considered in this paper is interesting.

### Weaknesses
W1. The paper lacks structure and clarity in its writing. For example:
* To the best of my knowledge, "remedial learning" seems to be a new setting introduced in this paper. If this is not the case, please provide the necessary references upon its first mention. Regardless, the authors should provide sufficient background on this setting in the Abstract, Introduction, as well as Title. Failing to do so may lead to unnecessary difficulties and confusion for readers attempting to understand the task's objective from the beginning.
* In Line 211 of Section 3.1, the statement "Recall from the relationship between ∇θL(D) and ∇θL(Dnew) in Section 3.2, …." is confusing.
* In Line 213, it appears that "the numerator ∇θk L(Dforget)" refers to the numerator in Eq. (8) (line 267). Introducing a quantity before it is first presented in the text can be confusing for readers.
* Typo in line 183: "at the instanced of unlearning"
* Typo in line 209: "\sum_{i=1}^N"

W2. The theoretical novelty of the derivations from Eq. (4) to Eq. (8) is unclear. The result $\nabla_\theta L(D_f) = \nabla_\theta L(D) - \nabla_\theta L(D_retain)$ seems simple and straightforward. I would appreciate further clarification on the contribution of this part. Specifically, while the linearity of differentiation is well-established, the paper doesn't sufficiently articulate how this particular application leads to a novel or non-obvious unlearning strategy. The connection between this derivation and the practical effectiveness of the proposed method needs to be more thoroughly justified.

W3. Please correct me if I misunderstood. From line 8 in Algorithm 1, it appears that selective re-initialization is performed on each element in the parameter vector. Intuitively, this design could increase the computational burden. Please explain this point. Additionally, in line 9 of Algorithm 1, a hyper-parameter $\alpha$ is introduced as a threshold to determine whether a parameter should be initialized. Is this hyperparameter the same for all model parameters? Ideally, it should vary, and discussing a suitable strategy for selecting an appropriate $\alpha$ for different parameters is recommended. The paper should also discuss the sensitivity of the method to the choice of $\alpha$ and provide some guidance on how to tune this parameter effectively. Furthermore, it is unclear how the knowledge values are computed and normalized to allow for a meaningful comparison with the threshold $\alpha$.

### Questions
In addition to addressing W1-W3, the authors are also expected to answer the following simple questions:

Q1: In Line 241, what do you mean by “single-based” ascent update?

Q2: What’s the impact of the Laplace smoothing constant ε in Eq (8)? How should its value be chosen?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposed RELOAD framework that aims to achieve unlearning through the following steps:

Step (1-3): Compute the gradient of the  forget set of the last round (by subtracting the gradient of the remaining data from the retained full gradient) to perform a single step of gradient ascent.

Step (4): Building on previous unlearning method that assess weight importance, the author calculates the importance of the weights and reinitializes those deemed non-important.

Step (5): Fine-tune on the remaining data.

The author empirically demonstrates that the proposed method, which does not require access to the forget dataset, outperforms existing algorithms that necessitate access to the entire dataset

### Strengths
1. The author's method does not require access to the remaining dataset and may represent a significant algorithmic contribution.

1. The author proposes a new method for calculating knowledge values (weight importance), which involves computing the ratio of the L2 norm of the forget dataset to the L2 norm of the gradient of the entire dataset on a well-optimized model. The L2 norm of the forget dataset is obtained by subtracting the gradient of the remaining data from the gradient of the entire dataset.

2. The paper provides empirical results for different datasets and models and the numerical results are impressive because they perform better than previous algorithms that required access to all the data, and the detailed description of the metrics provided by the author in the appendix is well-written.

### Weaknesses
1. Although the author's method does not require access to the forget dataset, calculating $\nabla_\theta \mathcal{L}(\mathcal{D} _ {\text{forget}}) = \nabla _ \theta \mathcal{L}(\mathcal{D}) - \nabla_\theta \mathcal{L}(\mathcal{D} \backslash D _ {\text{forget}})$  in step (1-3) requires retaining all datasets to compute $\nabla _ \theta \mathcal{L}(\mathcal{D} \backslash D _ {\text{forget}})$ since we do not know which data might need to be forgotten. I suggest the author describe potential application scenarios more in the introduction.

2. Retaining $\nabla_\theta \mathcal{L}(\mathcal{D})$  in step (1-3) is risky because prior work [B] has demonstrated that, for fully connected layers (such as the softmax mentioned by the authors), the input can theoretically always be inferred from the gradients, regardless of the layer's position. Experiments of [B] have also shown that images can be reconstructed from gradients. Therefore, when considering the retention of $\nabla_\theta \mathcal{L}(\mathcal{D})$, the authors should take additional measures to prevent unintended privacy leakage. Specifically, the authors should consider the implications of storing gradients from the final training epoch, as these gradients are known to be particularly vulnerable to inversion attacks. The risk is not just theoretical; practical demonstrations exist showing that even perturbed gradients can reveal significant information about the training data.

3. The author evaluates the importance of weights in step (4), drawing inspiration from prior unlearning work [A]. However, the paper lacks a comparison with existing methods for assessing weight importance. It’s crucial to clarify the differences between the gradient norm of the forget dataset used in previous studies and the ratio employed by the author as knowledge values. Simply stating in the appendix that their method outperforms other weight importance methods is insufficient; the author should at least report experimental results to justify the choice of knowledge values and help readers understand the contributions. Furthermore, the baseline analysis appears to overlook a comparison with the significant work [A], which should be addressed for a more comprehensive evaluation. The authors should provide a more detailed analysis of how their proposed knowledge value differs from the gradient norm used in [A], particularly in terms of its sensitivity to different types of data and model architectures. A theoretical justification for why the ratio is a better indicator of weight importance would also be beneficial.

4. In the title of this paper and contribution, the author mentions that their method does not require access to the "forget dataset." However, this is not a new problem (motivation). There are several methods, which the author has not cited (e.g., [C-F] or references listed in [G]), that also do not rely on the "forget dataset." I suggest that the author explicitly address the relevance of these existing methods when discussing the uniqueness of their approach and explain the differences and connections between their research and these methods. This would help readers better understand the author's contributions and the work done on the foundation of existing research. The authors should clarify how their method distinguishes itself from these existing approaches, especially in terms of the specific unlearning scenarios they target and the assumptions they make about the availability of data and computational resources. A table summarizing the differences in assumptions and applicability would be useful.

5. The author claims that RELOAD framework outperform existing algorithms that require access to the entire dataset, but I am concerned about the lack of either theoretical guarantees and empirical intuition behind the finds.   The paper lacks many reproducibility details regarding the hyper-parameters used (their method and the comparison methods) and the fine-tuning details. There's no way to verify the correctness of the result in the paper or to reproduce any of the results if the paper is accepted.  At a minimum, the author should provide insights to explain this phenomenon observed in the experiments, such as which key steps were missing in previous works that led to results inferior to the algorithm proposed in this paper, or how the author's framework helps enhance performance, reveal potential issues, or optimize the implementation of the algorithm. This would help readers better understand the contributions and practical significance of the research. Unfortunately, I found no explanations, and the links provided by the author contain no verifiable procedures.  I suggest that the author provide some explanations to clarify the phenomena observed in the experiments, or offer verifiable procedures to enhance the paper's persuasive power. This would help improve the credibility of the research and better showcase its algorithmic contributions.

### Questions
1. I am curious about the contribution of  step (1-3) one-step gradient ascent to the overall framework. Is step (4) (5) sufficient to satisfy unlearning? I did not see the author provide relevant explanations for step (1-3), which makes it difficult to detail the necessity of step (1-3). I suggest that the authors highlight the necessity of step (1-3) in the unlearning framework through some ablation experiments; otherwise, (4) (5) seem to be mere improvements based on previous methods.

2. Equations (4) to (7) seem unnecessary, as they occupy a significant amount of space without providing any useful information. The meaning could be effectively conveyed with just $\nabla_\theta \mathcal{L}(\mathcal{D}_{\text{forget}}) = \nabla_\theta \mathcal{L}(\mathcal{D}) - \nabla_\theta \mathcal{L}(\mathcal{D}_{\text{new}})$.

3. Blind unlearning is an interesting concept; however, given that prior work has achieved zero-shot unlearning without requiring access to any training data for the unlearning process, it is puzzling that this paper still necessitates access to the remaining dataset. The term "blind unlearning" could lead to confusion. A title like "Partially Blinded Unlearning," indicating that only a portion of the data is accessible (such as the remaining data or part of the forget dataset), might be more appropriate.

[A] SalUn: Empowering Machine Unlearning via Gradient-Based Weight Saliency in Both Image Classification and Generation. Fan, Chongyu, et al. ICLR, 2024.

[B] Inverting gradients-how easy is it to break privacy in federated learning? Geiping, Jonas, et al. NeurIPS, 2020.

[C] Eternal sunshine of the spotless net: Selective forgetting in deep networks. Golatkar et al. CVPR, 2020.

[D] Fast yet effective machine unlearning.Tarun, Ayush K., et al. TNNLS, 2023.

[E] Deep Regression Unlearning. Ayush Kumar Tarun, et al. ICML, 2023

[F] Deep Unlearning: Fast and Efficient Gradient-free Class Forgetting. Sangamesh Kodge, et al. TMLR, 2024.

[G] LLM Unlearning via Loss Adjustment with Only Forget Data

[H] Zero-Shot Machine Unlearning. Vikram S Chundawat, et al. TMLR, 2024.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper targets reducing the usage of forgetting data in machine unlearning and proposes a gradient ascent approach together with parameter selection. Due to the absence of forgetting data, the proposed method estimates the gradient of forgetting data by using the cached gradient on all training data and the gradient of the remaining data. Then, this paper conducts experiments on SVHN, Cfiar10 and Cifar100 datasets to prove the effectiveness of the proposed method.

### Strengths
1. Reducing the usage of forgetting data is an interesting problem for machine unlearning.
2. The technique and experiment part of this paper is easy to understand.

### Weaknesses
1. The motivation of this paper is to reduce the retaining of user data for unlearning. This paper only focuses on reducing the usage of forgetting data and requires the usage of remaining data. However, the size of the forgotten data is usually far smaller than the remaining data, and this also motivates other works that reduce the usage of the remaining data during unlearning [1,2,3]. Compared with such works, the proposed method required more training data to be preserved for unlearning. In addition, some methods that require both the forgetting data (10% in this paper's experiment setting ) and a subset of remaining data during unlearning (10% in this paper's experiment setting) only require 20% training to realise unlearning. However, the proposed method still requires another 90% of the remaining data during unlearning. Therefore, the proposed method does not match the motivation of reducing the data usage in unlearning
2. One previous work discussed reducing the usage of forgetting data, but this paper does not mention it in related works or compare it in experiments [4]. Other works have applied gradient-based input saliency maps for unlearning, and this paper does not mention or compare them [5,6].
3. This paper does not contain ablation studies to prove the effectiveness of the parameter selection component and different $\eta_p$ and $\alpha$.
4. This paper only conducts experiments on 10% random sample unlearning and 100 samples in class unlearning. More different experiment settings are required.
5. Some typos exist in the paper, for example, in line 147, and some notations are unclear (see questions).

### Questions
1. In experiments, why does a huge gap exist between the retrained model and $\mathcal{M}^{(\theta^{\sim})}$ under the current evaluations? What is the differences between retrained model and $\mathcal{M}^{(\theta^{\sim})}$.
2. In eq 8, does $\nabla_{\theta_k}\mathcal{L}(D)$ stand for the gradient of accumulated loss or averaged loss on $D$?
3. How to decide $\eta_p$ and $\alpha$ in the proposed method?
4. Minor question: regarding reducing the usage of forgetting data, how could users propose unlearning requests if they cannot point out that the forgetting data should be removed?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces the concept of blind unlearning, which involves unlearning without explicit access to the forget set. The authors propose the RELOAD method, which utilizes gradient-based techniques and sparsity to achieve this form of unlearning.

### Strengths
The paper is well-written.

### Weaknesses
 - The paper presents a setting where machine unlearning occurs without access to the forget dataset, which is weaker compared to zero-shot unlearning [1], where unlearning is achieved without access to either the forget or remaining datasets.

- The proposed setting is problematic. While the paper claims that blind unlearning does not access the forget dataset, it still allows access to the gradients of the entire dataset, including both the remaining and forget data. This is unreasonable because, to ensure data privacy, we typically use privacy-preserving mechanisms like DP-SGD. Gradients can leak data information, as attackers could exploit gradients to determine whether a specific data point was part of the training set. By analyzing how the gradient changes when a particular data point is used, adversaries can infer whether or not that point was included in training. Specifically, given the sum of gradients for a dataset, $\sum_{i \in S} \nabla L(w, x_i)$, it is possible to infer whether $x_j$ is part of the dataset by computing $\sum_{j \in S \backslash \{x_i\}} \nabla L(w, x_i)$.

- Step 2 in Figure 1 is confusing. If you have computed all gradients on the retained dataset, why not simply retrain the model? Fine-tuning and gradient ascent methods are typically used for efficient unlearning, but this approach seems to overlook that option. Furthermore, the re-optimization step in Figure 1.(5) is unclear. It is not specified how this optimization is conducted, and while the method claims computational efficiency, it appears to require significant memory resources to store the gradients of the entire dataset.

- The estimation of gradients on the forget dataset is not reasonable. The equations (5-7) fail when applied to average or mini-batch gradients, which makes the method problematic in practice. Specifically, when using batch gradients, the scalars $1/b$ and $1/n$ are needed, and it is not clear how the equality is derived under these conditions.

- Several evaluation metrics, such as NSKL and FSKL, are unclear. The goal of unlearning is to forget the targeted data while retaining the performance of a model trained from scratch. Evaluating the model based on its output and data seems unnecessary and could detract from the focus on model performance.

### Questions
I do not have specific question at the moment.

### Soundness
2

### Presentation
3

### Contribution
1

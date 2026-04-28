# Backdoor Contrastive Learning via Bi-level Trigger Optimization

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
\vspace{-3mm}
Contrastive Learning (CL) has attracted enormous attention due to its remarkable capability in unsupervised representation learning. However, recent works have revealed the vulnerability of CL to backdoor attacks: the feature extractor could be misled to embed backdoored data close to an attack target class, thus fooling the downstream predictor to misclassify it as the target. Existing attacks usually adopt a fixed trigger pattern and poison the training set with trigger-injected data, hoping for the feature extractor to learn the association between trigger and target class. However, we find that such fixed trigger design fails to effectively associate trigger-injected data with target class in the embedding space due to special CL mechanisms, leading to a limited attack success rate (ASR). This phenomenon motivates us to find a better backdoor trigger design tailored for CL framework. In this paper, we propose a bi-level optimization approach to achieve this goal, where the inner optimization simulates the CL dynamics of a surrogate victim, and the outer optimization enforces the backdoor trigger to stay close to the target throughout the surrogate CL procedure. Extensive experiments show that our attack can achieve a higher attack success rate (e.g., $99\%$ ASR on ImageNet-100) with a very low poisoning rate ($1\%$). Besides, our attack can effectively evade existing state-of-the-art defenses.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new method to perform poisoning-based
backdoor attacks on contrastive learning. It searches
optimal triggers by using a designed bi-level optimization
approach on the surrogate models. Experiments on three
datasets (CIFAR-10, CIFAR-100, and ImageNet-100) validate
the effectiveness of the proposed method.

### Strengths
* Backdoor attacks on contrastive learning is an important direction.

* Analysis of the reason that the proposed attack works
well is discussed in section 5.4.

### Weaknesses
 * The proposed method requires a surrogate to perform
bi-level optimization. This paper mentions it uses SimSiam
with ResNet18 as the surrogate model. The success of the
proposed method is based on the transferability of the
triggers optimized on the surrogate model. While Table 1 and
2 demonstrate the proposed method has good transferability,
the evaluation is not comprehensive. It is suggested to
include more self-supervised learning methods such as Jigsaw
[1], MoCoV2 [2], and DINO [3]. For different model
architectures, the results under modern architectures
such as ViT and RegNetY are missing (Note that ViT and RegNetY
are commonly used in self-supervised learning related
researches like
https://github.com/facebookresearch/vissl/blob/main/MODEL_ZOO.md).
Since the transferability is very important to the
performance of the method, it is suggested to conduct more
extensive experiments. For example, adding the results under
different architectures to Table 1 or adding the results
under different CL methods to Table 2 (So that it will have
a Table including the results under different combinations
of architectures and CL methods).

* The hyper-parameters such as the learning rates of the
models might also influence the performance of the proposed
method. For example, if the learning rates and the batch
sizes of the surrogate model are significantly different from
those used by the victim models, then the attack success
rates might also reduced. It is suggested to add the
discussion about this.

* In the experiments, this paper assumes that the downstream
dataset and the pre-training dataset used for self-supervised
learning is the same. Typically, the downstream users will
use different datasets to conduct the downstream training.
Many existing works such as BadEncoder [4] also mainly
investigate this practical scenario. The results under this
practical scenario are missing in this paper.

* Carlini et al. [5] is an important existing work in the
field of poisoning-based backdoor attacks on contrastive
learning. Although it mainly focuses on the vision-language
contrastive learning, the comparisons, and the discussion
about it is still important.

* The robustness under Feng et al. [6] is not discussed. Is the
backdoor samples in the proposed method have high cosine
similarity between each other?

* The usages of the surrogate models and the bi-level
optimization is not new in the field of poisoning attacks
and backdoor attacks [7,8], which somehow weaken the
contributions of this paper.

### Questions
See Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper formulates backdooring contrastive learning (CL) as a bi-level trigger encoder optimization problem. They claim that existing attacks using fixed triggers fail to maintain similarity between triggered data and target class in CL's embedding space due to data augmentation and uniformity effect, limiting their success. The proposed method formulates a bi-level optimization that simulates the victim's CL training dynamics in the inner level and optimizes a trigger generator in the outer level to keep triggered data close to the target throughout the inner CL training. This results in resilient triggers that can survive CL mechanisms. Experiments show the attack achieves success under varying victim settings and defenses. Analyses are provided on how CL mechanisms affect attack performance. The optimized triggers capture semantics related to the original input, explaining the attack's effectiveness.

### Strengths
- This work provides a formulation of the backdoor problem in contrastive learning as a bi-level optimization to identify a backdoor generator that is able to generate triggered images.

- The authors provided an approximated solution to the formulated bi-level optimization.

- The authors evaluated three datasets and compared them with two existing attacks. The attack is further evaluated with existing defenses from two lines of work (model-based backdoor trigger detection and model-based backdoor mitigation).

- The writing is clear and easy to follow.

### Weaknesses
 - The paper lacks analysis or discuss on the impact of using more accurate Hessian approximations to solve the proposed bi-level optimization, relying only on a discrete solution.

- The baseline implementations and results seem questionable based on inconsistencies with original papers and recent related work- the attack success rates for SSL backdoor and CTRL differ notably from prior reported values.

- The related work review and experiment scope is too narrow:
   1. Recent attacks using similar target-class-based trigger synthesis are not compared to.
   2. A relevant defense for detecting backdoor samples in contrastive learning is not discussed.

### Questions
The proposed bi-level optimization formulation is solved using a discrete approximation without much discussion on the impact of using more efficient yet accurate Hessian approximations or evaluates the convergence of the proposed solution. Bi-level optimization often benefits from analyzing such approximations rather than directly providing a discretized solution.

The evaluation results comparing against baselines may contain erroneous implementations. In particular, the reported attack success rate (ASR) for SSL backdoor differs notably from values in the original paper, which because the low efficacy of their work, they even used a different metric based on number of misclassified samples. Also, the ASR for CTRL is much lower than results from recent works (e.g., the original paper and [1]) that show CTRL can achieve above 80% ASR with SimCLR on CIFAR-10, contrasting the authors' significantly lower values. Additional to the original papers, another separated work [1] evaluated these two attacks also confirms the potential erroneous implementations in this work.

The related work could be expanded and compared more thoroughly. Some recent attacks [2] also leverage synthesized triggers using solely the target class, similar to the proposed approach, which is worth to be incorporated and compare. Additionally, a recent backdoor sample detection method [1] demonstrates effectiveness in detecting poisoned samples in contrastive learning unlabeled datasets, which is relevant but not discussed or evaluated.

[1] Pan, Minzhou, et al. "ASSET: Robust Backdoor Data Detection Across a Multiplicity of Deep Learning Paradigms." Usenix Security (2023).

[2] Zeng, Yi, et al. "Narcissus: A practical clean-label backdoor attack with limited information." ACM CCS (2023).

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper identifies that the current data poisoning-based backdoor attacks on contrastive learning adopt a fixed trigger design and have a limited attack success rate. To overcome this limitation, a novel bi-level optimization approach is proposed. In this framework, the inner optimization simulates the contrastive learning (CL) dynamics of a surrogate victim, while the outer optimization optimizes the trigger generator and ensures that the backdoor trigger remains close to the target throughout the surrogate CL procedure. Extensive experiments are conducted to compare the proposed methods with state-of-the-art (SOTA) attacks, such as SSL backdoor and CTRL, demonstrating superior attack effectiveness. Furthermore, the proposed methods can effectively evade existing SOTA defenses.

### Strengths
1. The proposed attack method is novel and shows superior effectiveness in comparison with the SOTA.

2. The experiments are comprehensive; the authors compare the proposed method with different attack methods, evaluate it against backdoor defenses, and also discuss the effect of various data augmentations.

3. The overall writing is good. The methodology and experimental results are not difficult to comprehend.

### Weaknesses
1. The motivation could be better articulated. The authors claim that the fixed trigger design leads to limited ASR. However, in the methodology, not only is the trigger generator adopted, but a bi-level optimization strategy is also used to optimize the trigger generator. This raises the question: Is the trigger generator alone sufficient for the success of the proposed attack? If not, it suggests that the fixed trigger is not the primary cause of the current limitation. I recommend that the authors conduct an ablation study on this matter and be cautious with their claims.

2. In the experiments, only SimSiam is adopted as the surrogate Contrastive Learning (CL)  method. The experimental results demonstrate that selecting this framework indeed achieves good performance, but it does not provide a direct rationale for choosing SimSiam. It is possible that using SimCLR or BYOL could yield better results, and it is recommended to supplement this part with additional experiments for verification.

3. The comparison with other recently developed works could enhance the contribution:
(1) PoisonedEncoder: Poisoning the Unlabeled Pre-training Data in Contrastive Learning.
(2) CorruptEncoder: Data Poisoning based Backdoor Attacks to Contrastive Learning.
Notably, in "PoisonedEncoder," a bi-level optimization strategy is also employed to formulate the attack. How does this work differ from theirs?

### Questions
1. Is the trigger generator alone sufficient for the success of the proposed attack?

2. How does this work differ from the "PoisonedEncoder"?

3. If the reference data $x_r$ is randomly sampled from the target class? does it need to be included in the downstream dataset to ensure the success of the attack?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a poisoning-based backdoor attack for Contrastive Learning (CL), targeted at the feature extractor. Through the bi-level optimization that simulates a backdoored CL pre-trained model in the inner loop, it trains a trigger generator to produce poisoned samples with *robust* triggers that survive the data augmentation of CL. These triggers also exhibit transferability across serveral victim CL training strategies and backbone architectures. Experimental validation confirms the effectiveness, transferability and robustness of the attack.

### Strengths
- The motivation behind the attack is well-described by incorporating the alignment and uniformity inherent in CL. The method for training the trigger generator is succinctly presented in an 11-line pseudocode.
- The experiments are comprehensive, including experiments of CL backdoor defense and the transferability in three aspects (i.e., CL training strategies, model architectures and datasets).
- The paper is well-written and easy to follow.

### Weaknesses
 - **Lack of details.** The implementation of the proposed attack seems to lack some details:
    - The setting of K and J are not included in the submission, and their relationship with N remains unclear. Is K large enough to ensure the convergence of the surrogate backdoored model? It is unclear how the number of inner loop steps (J) relates to the outer loop steps (N) and the overall training process. The lack of clarity on these hyperparameter settings makes it difficult to assess the practical feasibility and reproducibility of the attack.
  - Additionally, does the x-axis in Figure 4 refer to N? If it includes the inner loop updates (N*J), does it make the comparison of loss curves somewhat unfair? The plot should clarify whether the x-axis represents the number of outer loop iterations, inner loop iterations, or a combination of both. If it includes inner loop updates, the comparison with other methods becomes problematic due to the different training scales.
  - What does the expression *regularly re-initialize the surrogate feature extractor* (in section 4) mean? Does it imply that, after the initialization (line2 in Algorithm1), there is a subsequent re-initialization at some point? The frequency and the exact procedure of this re-initialization are not specified, which makes it challenging to understand the training dynamics of the surrogate model.
- What determines superior transferable ability of the chosen surrogate CL framework (SimSiam)? The fundamental factors may need further analysis and clarification in ablation experiments, such as the choices of different data augmentations. The paper should explore why SimSiam exhibits better transferability compared to other contrastive learning methods. It is crucial to understand if this is due to specific architectural choices or the training procedure itself. The impact of different data augmentations on transferability should also be investigated.
- The BLTO procedure contains both a backdoor generator and a backdoored surrogate model θ. Does the co-training surrogate backdoored model perform as well as an backdoored model actually trained on the poisoned data? It is important to verify if the surrogate model's performance is a good proxy for the actual performance of a model trained on poisoned data. The paper should provide a comparison between the surrogate model and an actual model trained on the poisoned data to validate the effectiveness of the proposed approach.

### Questions
- In the evaluation on transferability, the adopted backbone encoders are all of CNN architecture (e.g., ResNet, MobileNet, ShuffleNet, SqueezeNet), and the datasets are just CIFAR-10 and CIFAR-100. More diverse choices of backbone architecture and dataset may be necessary, such as the architurecture of ViT and more challenging datasets like ImageNet.
- Besides, though the proposed attack targets at the feature extractor, the victim settings in the experiments are limited to the classification task. I think it could be extended to more tasks to demonstrate the effectiveness of the proposed attack.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

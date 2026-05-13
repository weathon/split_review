# Theoretical Analysis of Robust Overfitting for Wide DNNs: An NTK Approach

- Decision: Accept
- Scores: 6, 6, 6, 8, 6

## Abstract
Adversarial training (AT) is a canonical method for enhancing the robustness of deep neural networks (DNNs). However, recent studies empirically demonstrated that it suffers from {\it robust overfitting}, {\it i.e.}, a long time AT can be detrimental to the robustness of DNNs. This paper presents a theoretical explanation of robust overfitting for DNNs. Specifically, we non-trivially extend the neural tangent kernel (NTK) theory to AT and prove that an adversarially trained {\it wide} DNN can be well approximated by a linearized DNN. Moreover, for squared loss, closed-form AT dynamics for the linearized DNN can be derived, which reveals a new \textit{\textbf{AT degeneration}} phenomenon: a long-term AT will result in a wide DNN degenerates to that obtained without AT and thus cause robust overfitting. Based on our theoretical results, we further design a method namely \textit{\textbf{Adv-NTK}}, the first AT algorithm for infinite-width DNNs. Experiments on real-world datasets show that Adv-NTK can help infinite-width DNNs enhance comparable robustness to that of their finite-width counterparts, which in turn justifies our theoretical findings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studied the robust overfitting issue in adversarial training. Specifically, the author studied the training dynamics of adversarial training under the NTK regime. Theoretical results show that after long training the term that captures the robustness will fade away and the trained network will degenerate to the network with standard training. The author further proposed an algorithm for adversarial training under the NTK regime and conducted experiment. Results show that the proposed algorithm outperforms standard adversarial training and vanilla NTK.

### Strengths
1. The paper provides a novel theoretical view in robust overfitting in adversarial training, and the theoretical analysis gives an intuition on why adversarial training fails on a simplified regime (NTK).
2. The paper further proposed an algorithm applicable to NTK models. Experiment results aligns with the theoretical conclusion in the paper.

### Weaknesses
My concerns are listed as the follows:

1. The proposed algorithm can only work under NTK regime. Though the corresponding results can serve as an empirical evidence of the theoretical conclusion, it seems that the proposed algorithm has limited practical application.
2. The assumption in the paper seems too strong comparing with practical setting. The author are encouraged to consider more practical setting like GD and cross entropy loss. 
3. In the studied setting, the scale of pertubation is also related to the norm of $\partial_x \mathcal{L}$, rather than depending on $S$, which introduces a discrepancy between the setting studied and real-world setting. Specifically, the constraint of the adversarial example is defined as $||x'-x|| \leq \rho$, but the paper does not explicitly guarantee that $||x_{i,t,s}-x_i|| \leq \rho$ is satisfied in their gradient flow based adversarial example search. 
4. Some missing references in convergence of DNN: [1], [2], [3]

### Questions
Please refer to the "weakness" section

### Soundness
3 good

### Presentation
3 good

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
The paper explores the issue of robust overfitting in deep neural networks (DNNs) during adversarial training (AT). It extends neural tangent kernel (NTK) theory to explain this phenomenon for infinite width deep networks, showing that a wide DNN under AT can behave like a linearized DNN, leading to AT degeneration over time (assuming squared loss). To address this, the paper introduces Adv-NTK, an novel AT algorithm for infinite-width DNNs, designed to enhance network robustness. The effectiveness of Adv-NTK is demonstrated through experiments on real-world datasets, establishing its real potential in improving DNN robustness against adversarial attacks.

### Strengths
The paper attempts to tackle an important problem of overfitting in adversarial training from a theoretical perspective, which should be relevant to the broader community.

The empirical validation of the Adv-NTK algorithm using real-world datasets like SVHN and CIFAR-10 enhances the quality of the paper. This empirical approach ensures that the theoretical findings are not only sound in theory but also applicable and effective in real-world scenarios.

### Weaknesses
Its not clearly under what conditions the small step size can lead to linearization of the adversarial training of DDN.

In the proof, it does not try to find efficient direction, does that make any difference on the proof ?

### Questions
It would improve the paper if bound on the learning rate can be provided with respect to its training (or maybe some empirical results towards that).

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the problem of robust overfitting in adversarial training using the Neural Tangent Kernel (NTK). First, the authors extend the theoretical framework of NTK to adversarial training, introducing an adversarial regularization kernel and demonstrating that adversarially trained DNNs can be well approximated by their linearized DNNs. They then derive the closed-form dynamics of adversarial training for the linearized DNN and uncover a phenomenon called adversarial training degeneration: prolonged adversarial training leads to the degradation of the wide DNN to a state similar to that of a DNN with normal training, which results in robust overfitting. Based on these theoretical findings, the authors propose an adversarial training algorithm called Adv-NTK for infinite-width DNNs, and experimental results show that it can enhance the robustness of infinite-width DNNs to a level comparable to that of finite-width DNNs.

### Strengths
This paper provides a linear model-level explanation of the adversarial training degeneration phenomenon. The designed Adv-NTK algorithm enables infinite-width NTK models to achieve robustness similar to MLPs through adversarial training.

### Weaknesses
1: This paper focuses on linearized models but lacks a detailed explanation of why linearization approximation is applicable. Theorem 1 demonstrates the convergence of two kernels for initialization. However, the properties that remain constant over time appear to be submerged in Appendix C.2. It is recommended that the authors include an informal presentation of the results from Appendix C.2 between Theorems 1 and 2 and provide corresponding discussions.

2: Section 5.1 lacks a discussion regarding the impact of $\eta S$ on the adversarial training degeneration phenomenon.

### Questions
Are the results in Section 4 of this paper valid for adversarial training of any intensity? Intuitively, if the intensity of adversarial training is too high, some of the results in Chapter 4 may not be valid.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
•	This paper theoretically explores the robust overfitting of Adversarial Training (AT). Specifically, it demonstrates that Deep Neural Networks (DNNs) trained with AT can be represented from the perspective of Neural Tangent Kernel (NTK). The paper further formulates the dynamics of Adversarial Training. Based on this formulation, it explains the reasons behind the occurrence of robust overfitting and proposes an algorithm, termed ADV-NTK, that can prevent robust overfitting in a manner akin to early stopping.

### Strengths
•	The paper tackles a critical and pressing issue: Overfitting in Adversarial Training.

•	The contribution of paper is based on a theoretically solid proof. They also offer a detailed and meticulous explanation enhancing the understandings.

### Weaknesses
 •	The paper is written based on the logical flow of formulation and comparably not focusing on the motivation of the paper. For better readability, it seems to be a need for more appeal on how important task the paper tries to solve and what is the contributions of the paper.

•	In context of DNN-NTK, they replace the constrained-spaces condition with an additional learning rate term to control the strength of adversarial examples. (in Equation 7) However, unlike many attack mechanisms, it doesn't efficiently find a significant direction of attack. Despite this, does believe that the derived formula's proof is still not too loose?

•	The additional experiments are needed. In specific, it would be better to empirically verify 1) whether theoretically proven properties actually happen similarly in real-world dataset and 2) how much the robust overfitting problem has been addressed with the proposed Adv-NTK. For instance, tracking the performance (or loss) trend across iterations between vanilla AT and Adv-NTK.

### Questions
•	In the above part.

[Overall]
•	If the authors provide further experiments on Adv-NTK and supplementary explanations for the justification for learning rates, I agree that this paper is accepted.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper applied neural tagent kernel techniques into adversarial training setting and proves that adversarial trained DNN can be approximated by a linearized DNN. For square loss it reveals a AT degreneration phenomena so that explains robust overfitting. The paper designed an algorithm AdvNTK based on the theoretical results.

### Strengths
I like the idea of analyzing robust overfitting from the time-dependent regularizer matrix that derived from adversarial NTK.

### Weaknesses
### weaknesses:
 I appreciate the novel approach of analyzing robust overfitting through the lens of the time-dependent regularizer matrix derived from the adversarial NTK. However, there are several critical points that need further clarification and strengthening.

 The claim that an adversarially trained DNN can be approximated by a linearized DNN seems to hold only under the assumption of a small perturbation size. The paper lacks a quantitative analysis of how small this perturbation should be for the approximation to remain valid. While the authors mention using an attack learning rate for a total of time S, the magnitude of this attack rate is not specified. If the attack learning rate is infinitesimally small, the resulting perturbation size might be too small to provide any meaningful generalization guarantee in terms of robustness. A more rigorous analysis of the relationship between perturbation size, attack learning rate, and the validity of the linear approximation is needed.

 Furthermore, the motivation for studying adversarial training within the NTK regime is not entirely convincing. As shown in [1], when the network is close to initialization, there may not be any robust network at all. This raises questions about the practical relevance of studying adversarial training in this specific regime. A more thorough discussion justifying the choice of the NTK regime for analyzing adversarial training would strengthen the paper's motivation.

 In the proof of Theorem 2, the dependency of  `polyt` appears to be inadequately defined. Specifically, `polyt` depends on the norm of `W_t`, which could potentially go to infinity. While it is understood that in the neural tangent kernel framework, the network weights do not deviate significantly from their initialization, allowing one to argue that the norm of `W_t` is bounded, as suggested in Lemma C.5, this lemma's proof also relies on `polyt`. Therefore, the current presentation, which omits the dependency on the norm of `W_t` or `x_t`, seems to obscure certain aspects of the proof. A more explicit and detailed treatment of these dependencies is necessary to ensure the rigor and clarity of the theoretical results.

 The connection between the experiments and the theoretical results needs to be more clearly established. How do the experiments validate the theorems? The robust accuracy achieved on both SVHN and CIFAR10 datasets appears significantly lower than that of standard adversarial training. Is this a consequence of the network architecture used? Why not employ standard architectures like ResNet, which are commonly used in practice? Additionally, the authors should provide a simple experiment to confirm the AT degeneration phenomenon. The distinction between "AT degeneration" and "robust overfitting" is not clear. If they are synonymous, using different terms is unnecessary and potentially confusing.

 In terms of the writing, the paper would benefit from a more detailed discussion of the theorems, including explanations and intuitive interpretations.

### Questions
This paper focuses on regression setting with squared loss. I’m wondering if the idea can be generalized to classification setting.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

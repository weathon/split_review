# Domain-Inspired Sharpness-Aware Minimization Under Domain Shifts

- Decision: Accept
- Scores: 5, 8, 6, 6

## Abstract
This paper presents a Domain-Inspired Sharpness-Aware Minimization (DISAM) algorithm for optimization under domain shifts. It is motivated by the inconsistent convergence degree of SAM across different domains, which induces optimization bias towards certain domains and thus impairs the overall convergence. To address this issue, we consider the domain-level convergence consistency in the sharpness estimation to prevent the overwhelming (deficient) perturbations for less (well) optimized domains. Specifically, DISAM introduces the constraint of minimizing variance in the domain loss, which allows the elastic gradient calibration in perturbation generation: when one domain is optimized above the averaging level \textit{w.r.t.} loss, the gradient perturbation towards that domain will be weakened automatically, and vice versa. Under this mechanism, we theoretically show that DISAM can achieve faster overall convergence and improved generalization in principle when inconsistent convergence emerges. Extensive experiments on various domain generalization benchmarks show the superiority of DISAM over a range of state-of-the-art methods. Furthermore, we show the superior efficiency of DISAM in parameter-efficient fine-tuning combined with the pretraining models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Due to the inconsistent convergence degree of SAM across different domains, the optimization may bias towards certain domains and thus impair the overall convergence. To address this issue, this paper considers the domain-level convergence consistency in the sharpness estimation to prevent the overwhelming perturbations for less optimized domains. Specifically, DISAM introduces the constraint of minimizing variance in the domain loss. When one domain is optimized above the averaging level w.r.t. loss, the gradient perturbation towards that domain will be weakened automatically, and vice versa.

### Strengths
They identify that the use of SAM has a detrimental impact on training under domain shifts, and further analyze that the reason is the inconsistent convergence of training domains that deviates from the underlying i.i.d assumption of SAM.

### Weaknesses
This paper considers the domain-level convergence consistency in SAM for multiple domains, and proposes to adopts the domain loss variance in training loss. The convergence consistency is a general issue, and the solution is normal, thus the novelty is not so clear for publication in ICLR.

### Questions
1.	In the definition of the variance between different domain losses, the values of loss between different domains are restricted. Which one is more import? The value of losses in different domains, or the minimization speed of loss in different domains?
2.	In the learning of multiple domains, there is Multi-Objective Optimization, so the domain-level convergence consistency is a general issue under domain shifts? Or the convergence consistency is a general issue in Multi-Objective Optimization?
3.	This paper considers the domain-level convergence consistency in SAM for multiple domains, and proposes to adopts the domain loss variance in training loss. The convergence consistency is a general issue, and the solution is normal, thus the novelty is not so clear.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a novel optimization algorithm named Domain-Inspired Sharpness Aware Minimization (DISAM) tailored for challenges arising from domain shifts. It seeks to maintain consistency in sharpness estimation across domains by introducing a constraint to minimize the variance in domain loss. This approach facilitates adaptive gradient adjustments based on the optimization state of individual domains. Theoretical and empirical findings show the proposed method offers faster convergence and superior generalization under domain shifts.

### Strengths
1.	The proposed method targets at the model generalization under domain shifts, which is a common challenge in machine learning. To date, there has been a lack of thorough investigation into sharpness-based optimization in the context of domain shifts, and the idea of constraint the variance of losses among training domains is interesting.

2.	The paper not only presents theoretical evidence showcasing the efficiency of DISAM, but it also provides empirical data to support this claim, demonstrating the improved performance across various domain generalization benchmarks.

3.	The analytical experiments conducted in this paper are comprehensive and lucid, providing evidence of DISAM's efficacy in enhancing convergence speed and mitigating model sharpness. Additionally, the study investigates the application of DISAM for fine-tuning a clip-based model, aiming to achieve improved open-class generalization.

### Weaknesses
1.	SAM-based optimization incurs twice the computational overhead and additional storage overhead in comparison to the commonly used SGD. While DISAM, the method proposed in this paper, demonstrates faster convergence under domain shift conditions when compared to SAM, it does not include a comparison with optimizers such as SGD or Adam. The absence of a direct comparison with these standard optimizers makes it difficult to assess the practical efficiency gains of DISAM, especially considering the known computational costs associated with SAM-based methods. A thorough evaluation should include a comparison of wall-clock time and resource usage to provide a complete picture of the method's performance.

2.	This paper employs multiple benchmarks to evaluate the performance of multi-source domain generalization. The article highlights the need for advancements in the domain shift perspective of the SAM method and suggests conducting comparisons between DISAM and the state-of-the-art (SOTA) method to further validate the effectiveness of the proposed approach. While the paper does compare to some existing methods, a more comprehensive comparison with a wider range of recent SOTA domain generalization techniques would strengthen the claims of the paper. Specifically, it would be beneficial to see comparisons against methods that explicitly address domain alignment or feature disentanglement, which are common strategies in domain generalization.

3.	The value of $\rho$ in DISAM significantly influences both the convergence speed and generalizability. And it needs more discussion on how to effectively determine the value to maximize the benefits of proposed method. The paper lacks a clear methodology for selecting the optimal value of $\rho$, and it would benefit from a more detailed analysis of how this parameter affects the training dynamics and final performance. A sensitivity analysis of $\rho$ across different datasets and model architectures would be valuable to provide practical guidance for users of DISAM.

### Questions
1.	The article presents a theoretical analysis suggesting that larger values of parameter $\rho$ should lead to improved generalization, given that convergence is guaranteed. It is important to reflect this aspect in the experiments to provide stronger evidence and validation.

2.	Regarding the open class generalization of the clip-based model, further experimental analysis should be conducted to elucidate the reasons behind the superior performance of DISAM.

For other questions, please refer to the weaknesses.

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces the Domain-Inspired Sharpness Aware Minimization (DISAM) algorithm, a novel approach for optimizing under domain shifts. The motivation behind DISAM is to address the issue of inconsistent convergence rates across different domains when using Sharpness Aware Minimization (SAM), which can lead to optimization biases and hinder overall convergence.

The key innovation of DISAM lies in its focus on maintaining consistency in domain-level convergence. It achieves this by integrating a constraint that minimizes the variance in domain loss. This strategy allows for adaptive gradient perturbation: if a domain is already well-optimized (i.e., its loss is below the average), DISAM will automatically reduce the gradient perturbation for that domain, and increase it for less optimized domains. This approach helps balance the optimization process across various domains.

Theoretical analysis provided in the paper suggests that DISAM can lead to faster overall convergence and improved generalization, especially in scenarios with inconsistent domain convergence. The paper supports these claims with extensive experimental results, demonstrating that DISAM outperforms several state-of-the-art methods in various domain generalization benchmarks. Additionally, the paper highlights the efficiency of DISAM in fine-tuning parameters, particularly when combined with pretraining models, presenting a significant advancement in the field.

### Strengths
As of now, there has not yet been a sharpness-aware minimization (SAM) methodology developed specifically for addressing distribution shifts. The issue of varying convergence rates across different domains, as observed in SAM, is undeniably a significant challenge.

This methodology presents an impressive degree of compatibility, as it can be integrated with a variety of sharpness-variants. An especially commendable aspect of this approach is its computational efficiency. Compared to standard SAM techniques, it does not incur additional computational costs, making it a practical option for scenarios where resource constraints are a consideration.

In summary, the development of a SAM methodology that is adept at handling distribution shifts, and particularly its implications for domain convergence, is both novel and highly relevant in the current landscape of optimization challenges.

### Weaknesses
The idea of minimizing the variance between losses, a core aspect of the presented methodology, is not entirely novel. Similar concepts have been previously explored in methods like vREX (Out-of-Distribution Generalization via Risk Extrapolation) and further extended to gradient computations in methodologies like Fishr (Invariant Gradient Variances for Out-of-Distribution Generalization). In this context, the proposed approach appears to be an incremental adaptation of vREX principles applied specifically to the challenges faced in Sharpness Aware Minimization (SAM) scenarios.

The improvement in out-of-distribution (OOD) performance using the DISAM methodology does not appear intuitive. In fact, when comparing its performance enhancements to those achieved with CLIPOOD, as reported, the difference seems marginal. This observation raises questions about the actual effectiveness of DISAM, particularly in the context of fine-tuning methodologies.

### Questions
Similar to how transitioning from ERM to vREX in optimization has been shown to enhance domain generalization performance, the application of vREX to SAM in the form of this methodology could be seen as a natural extension that brings comparable performance improvements. Furthermore, it is a valid assertion that incorporating various algorithms tailored for domain generalization (such as Fish, Fishr, gradient alignment) into the SAM optimization framework could potentially yield performance enhancements. The logic here is that these methods, when applied within the context of SAM, could enhance its ability to generalize across domains.

However, the critique that DISAM may simply be an incremental version of applying domain generalization methodologies to SAM is not without its counterarguments. It's important to consider the specific challenges and nuances of the SAM framework and how DISAM addresses these. If DISAM introduces significant modifications or adaptations that are uniquely tailored to the idiosyncrasies of SAM, then its contribution could extend beyond a mere incremental update. The key would lie in the specifics of how DISAM modifies or enhances the existing principles of SAM and domain generalization methods, making it more than just a straightforward application of known techniques.

In summary, while the perspective that DISAM is an incremental version of existing methodologies is certainly tenable, a comprehensive evaluation would require a deeper exploration of how DISAM specifically adapts or augments the SAM framework to address its unique challenges. If such adaptations are significant, they could justify the novelty and utility of DISAM beyond a simple combination of existing techniques.

Can you provide the reproducible code during the rebuttal period?

### Soundness
4 excellent

### Presentation
4 excellent

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
Targeting at domain generalization scenario with possible shifts among domains, this paper proposes to take 'per domain optimality' into consideration for finding the perturbation of SAM. The proposed DISAM is shown to have an improved convergence rate. Numerically, DISAM outperforms other SAM alternatives.

### Strengths
S1. The idea of tackling domain shift in SAM is novel. 

S2. A new algorithm, DISAM, is proposed with satisfying numerical results. DISAM improves over state-of-the-art by a large margin.

### Weaknesses
W1. Stronger motivation needed. The authors motivates the domain difference using Fig. 1 (b). While the convergence behaviors among domains are indeed inconsistent at the early stage,  the losses are similar after e.g., 30 epoch. The authors should also explain why the difference of convergence in **early phase** impact the generalization of SAM. It is not clear how the inconsistent convergence *degree* (as opposed to loss value) in the early phase directly translates to a poorer final generalization performance. The authors need to provide a more explicit link between the early-stage convergence behavior and the final generalization capability of the model. Specifically, it would be beneficial to see a more detailed analysis of how these early differences in convergence affect the optimization trajectory and the final minima reached by the model across different domains.

W2. More discussions on $\lambda$ in eq. (7) are needed. This is a critical parameter that considers the variance/domain shifts in DISAM. However, this $\lambda$ does not appear in Theorem 1. Can the authors illustrate more on this point? And how does the choice of $\lambda$ influence convergence and generalization? The current discussion lacks a clear explanation of how $\lambda$ is incorporated into the theoretical analysis, specifically within the proof of Theorem 1. Furthermore, the impact of different $\lambda$ values on the optimization process and the final generalization performance is not sufficiently explored. A more detailed analysis, possibly including a sensitivity study, is needed to understand the role of $\lambda$ in the proposed method.

### Questions
Q1. Relation with a recent work (https://arxiv.org/abs/2309.15639).

The paper above also proposes approaches to reduce variance for finding perturbations, although not designed for the domain generalization setting. How does this work relate with the proposed DISAM?


Q2. Theorem 1 illustrates that the *convergence* of DISAM benefits from $\Gamma$. Can the authors explain more on the discussion of 
> as DISAM enjoys a smaller $\Gamma$ than SAM, DISAM can permit the potential larger $\rho$ than that in SAM, thus yielding a better generalization

In particular, how does the convergence rate link with generalization?

Q3. The last sentence in Sec 3 claims that
>  ... allowing larger $\rho$ for better generalization.

Why does larger $\rho$ relate to better generalization?

Q4. (minor) The notation in e.g., eq (5) can be improved, because the multiple subscripts $i$ in $\Sigma_{i} \frac{C_i}{\sum_i C_i}$ are confusing.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

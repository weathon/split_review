# Statistical Tractability of Off-policy Evaluation of History-dependent Policies in POMDPs

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
We investigate off-policy evaluation (OPE), a central and fundamental problem
in reinforcement learning (RL), in the challenging setting of Partially Observable
Markov Decision Processes (POMDPs) with large observation spaces. Recent
works of Uehara et al. (2023a); Zhang & Jiang (2024) developed a model-free
framework and identified important coverage assumptions (called belief and outcome coverage) that enable accurate OPE of memoryless policies with polynomial sample complexities, but handling more general target policies that depend on
the entire observable history remained an open problem. In this work, we prove
information-theoretic hardness for model-free OPE of history-dependent policies in
several settings, characterized by additional assumptions imposed on the behavior
policy (memoryless vs. history-dependent) and/or the state-revealing property of
the POMDP (single-step vs. multi-step revealing). We further show that some hardness can be circumvented by a natural model-based algorithm—whose analysis has surprisingly eluded the literature despite the algorithm’s simplicity—demonstrating
provable separation between model-free and model-based OPE in POMDPs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper explores the off-policy evaluation (OPE) of history-dependent policies within partially observable Markov decision processes (POMDPs) using large observation spaces. Traditional methods for OPE in POMDPs have relied on model-free approaches and simplified memoryless policies due to computational complexity. This paper address this by examining the statistical challenges of evaluating more complex, history-dependent policies and by proposing a model-based method to circumvent limitations in model-free approaches. Key theoretical contributions include identifying scenarios where model-free methods are insufficient, as well as demonstrating how a simple model-based approach can achieve polynomial sample complexity.

### Strengths
It seems interesting to me that the model-based methods, which use synthetic data from learned models, bypass the limitations of model-free algorithms, especially in history-dependent scenarios.

### Weaknesses
1. What is the practical meaning of assumption D (multi-step outcome revealing) and how is it related to other revealing conditions in offline and online partially observable reinforcement learning, as well as the corresponding results?

2. Although it is said that $M^*$ does not necessarily satisfy the realizability, would the observable-equivalent realizability actually similar to it, and the resulting dependency on the realizability error seems actually trivial? Since the only difference is the additional gap due to the error in estimation likelihood from the misspecification of $M$.

### Questions
See weaknesses

### Soundness
2

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
This paper explores the statistical tractability of off-policy evaluation (OPE) for history-dependent policies in unconfounded partially observable Markov decision processes (POMDPs) with large observation spaces. The authors first establish information-theoretic hardness results for model-free algorithms when evaluating history-dependent policies, highlighting the increased complexity compared to memoryless policies. To address these challenges, they then propose a model-based approach that enables efficient OPE for history-dependent policies.

### Strengths
The findings in this paper are interesting. It demonstrates that no sample-efficient model-free OPE algorithm exists for POMDPs when evaluating history-dependent policies, whereas a model-based approach can achieve polynomial sample complexity. This highlights the effectiveness of model-based methods in POMDPs, and perhaps inspires future research on model-based RL for POMDPs. The theoretical analysis is solid and strong, and the writing is logically structured.

### Weaknesses
1. The writing could be improved to be more accessible to readers who may not be deeply familiar with this topic. For example, in the introduction, the authors could provide additional insights into belief and outcome coverage when these concepts are first introduced.

2. Another area for improvement in the writing would be providing a broader perspective on the paper’s contributions. Since the main contribution is extending existing results from memoryless policies to history-dependent policies, it would be helpful to include a high-level discussion in the introduction on (1) why history-dependent policies are particularly important in POMDP settings, and (2) what major challenges arise when attempting to apply existing analysis techniques for memoryless policies to history-dependent policies.

3. I have a concern regarding the MLE part. From my understanding, it seems that $\epsilon_{MLE}$ may implicitly depend on the horizon length $H$. Specifically, the model class $\mathcal{M}$ appears to be defined as $M := \cup_{h=1}^H (\mathbb{T}_h, \mathbb{O}_h, r_h)$, where different transition models and reward models are allowed at each stage $h$. If this is the case, then $|\mathcal{M}|$ would scale with $H$, and this dependence should be made explicit in the main theorem. Conversely, if the transition and reward models are assumed to be time-homogeneous, this should also be clearly stated. The current presentation leaves this point ambiguous.

### Questions
I have a concern regarding the MLE part. From my understanding, it seems that $\epsilon_{MLE}$ may implicitly depend on the horizon length $H$. Could you please clarify and elaborate on this point? If so, how would this dependence impact the main results in the paper?

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
This paper focus on OPE problems in unconfounded POMDPs with large observation spaces and history-dependent target policies. While previous work addressed the problem for memoryless target policies under certain coverage assumptions, the authors extended these results to history-dependent target policies and prove polynomial complexity.

### Strengths
1. The paper addresses an important gap in the literature by extending OPE to history-dependent target policies in POMDPs.
2. The authors provide solid theoretical results, including both hardness proofs and positive guarantees for model-based algorithm.
3. The paper is well-organized, with clear definitions, assumptions, and theorem statements that make the paper accessible.

### Weaknesses
1. The paper does not include experimental results to validate the theoretical findings or to demonstrate the practical effectiveness of the MLE-based algorithm. The absence of empirical validation makes it difficult to assess the real-world applicability of the proposed method, especially given the known computational challenges associated with MLE in latent variable models like POMDPs. It remains unclear how the algorithm would perform in practice, and whether the theoretical polynomial complexity translates to reasonable runtimes.
2. The model-based algorithm's reliance on a perfectly specified model is a significant limitation. While Theorem 8 addresses a form of state-space mismatch, it does so under a very specific interpretation of Assumption D, which requires that the model class M satisfy the revealing assumption. This is a strong assumption, and the paper does not discuss how to verify or enforce it in practice. The practical implications of Theorem 7, which shows the failure of MLE under a more general form of state-space mismatch, are not sufficiently addressed.

### Questions
1. Can authors provide any empirical or simulation results by the proposed algorithm on the setting described in the paper?
2. Are there any possibilities that can handle the state-space mismatch problem specified in Theorem 7?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper investigates off-policy evaluation in POMDPs. Compared to previous work, this paper considers more general target policies that depend on the entire observable history. The authors first provide hardness results showing that a model-free algorithm can not output a near-optimal evaluation with polynomial sample complexity. To handle this challenge, the authors adopt a model-based method based on MLE. The authors further prove that under certain assumptions, even considering more general target policies, the proposed model-based method can output near-optimal evaluation with polynomial sample complexity. Finally, the authors weaken the realization assumption under misspecification cases.

### Strengths
(1) The paper provides hardness results for model-free methods, which motivates the authors to adopt the model-based methods.

(2) This paper weakens several previous assumptions on target policies and POMDPs, and proves the polynomial sample complexity upper bound for model-based methods.

(3) The paper is well-organized and easy to follow.

### Weaknesses
It seems that the **Pre-filtering** and **MLE** parts of algorithms are not computationally efficient. **Pre-filtering** requires to verify each of the models in set $\mathcal{M}$. Is there any efficient way to implement these two steps? The pre-filtering step, in particular, appears to require an exhaustive search over the model space $\mathcal{M}$, which could be prohibitively expensive for complex POMDPs. The MLE step, while theoretically sound, often involves non-convex optimization for POMDPs, making it difficult to guarantee convergence to a global optimum in practice. Furthermore, the paper does not discuss the practical implications of these computational bottlenecks, which could limit the applicability of the proposed method in real-world scenarios.

### Questions
Should the policy $\pi$ in Eq. (1) be behavior policy $\pi_b$?

 I wonder if assumption A can be relaxed, for example, estimated via the offline data set? And how would this relax affect the MLE in Algorithm?

### Soundness
3

### Presentation
3

### Contribution
3

# Learning Differentially Private Rewards from Human Feedback

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 3, 5

## Abstract
We study the privacy of reinforcement learning from human feedback.  In particular, we focus on solving the problem of reinforcement learning from preference rankings, subject to the constraint of differential privacy, in MDPs where true rewards are given by linear functions. To achieve this, we analyze $(\epsilon,\delta)$-differential privacy (DP) for both the Bradley-Terry-Luce (BTL) model and the Plackett-Luce (PL) model. We provide a differentially private algorithm for learning rewards from human rankings. We further show that the privately learned rewards can be used to train policies achieving statistical performance guarantees that asymptotically match the best known algorithms in the non-private setting, which are in some cases minimax optimal.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The primary aim of this paper is to explore offline Reinforcement Learning in situations where the agent is limited to observing human feedback in the form of preference rankings rather than direct reward information. In contrast to prior studies, the authors incorporate the Gaussian mechanism to safeguard sensitive information and put forth a private Maximum Likelihood Estimation (MLE) algorithm. The authors contend that the proposed algorithm achieves a near-optimal sub-optimality gap with a guarantee of differential privacy.

### Strengths
1. Protecting privacy information holds paramount importance in reinforcement learning, and the proposed algorithm attains a guarantee of differential privacy without compromising performance.

2. The paper is well-written and easy to comprehend.

### Weaknesses
1. This study lacks novelty, as the algorithm essentially integrates previous Reinforcement Learning with human feedback results [1] with a Gaussian mechanism, which is a widely employed approach for ensuring differential privacy guarantees. The core idea of applying a Gaussian mechanism to the parameters of the reward model learned from human preferences is not a significant departure from existing techniques. A more detailed analysis of the specific challenges and adaptations required for the RLHF setting, beyond simply adding noise, would be necessary to establish novelty.

2. In this work, the authors assert that the sub-optimality gap is near-optimal. However, the absence of a lower bound in this study creates confusion regarding the actual near-optimality of the results. The paper should provide a clear definition of what 'near-optimal' means in the context of their algorithm and provide a comparison to a theoretical lower bound, even if that lower bound is under specific assumptions. Without this, the claim of near-optimality is not sufficiently substantiated.

3. In addressing the general Markov Decision Process (MDP) setting, the author exclusively focuses on estimating the reward function and undertaking pessimistic policy optimization. However, a fundamental challenge in learning an MDP lies in acquiring knowledge about the transition probability function  $P$. The determination of the occupancy $\rho$ for a given policy $\pi$ remains unclear. The assumption appears to presume that the transition process is already known, effectively simplifying the MDP problem to a bandit problem and streamlining the learning process. It is imperative to explicitly state all assumptions before making any claims. The paper needs to clarify how the transition dynamics are handled, or explicitly state the assumption that they are known, and discuss the implications of this assumption on the generality of the results.

4. The proposed algorithm lacks experimental results to substantiate its efficacy. The absence of empirical validation makes it difficult to assess the practical performance of the algorithm and its sensitivity to various parameters. The theoretical analysis, while important, needs to be complemented with experiments on benchmark datasets to demonstrate the algorithm's effectiveness.

### Questions
1. On page 4, in the definition of the Plackett-Luce Model, $m$ is not mentioned.  It seems more appropriate for it to be $k$.

2. The Gaussian mechanism in Algorithm 2 is commonly utilized to ensure differential privacy guarantees. Nevertheless, it would be beneficial for the author to provide additional explanations for the private process in Algorithm 1, as it appears to deviate from the standard procedure.

3. In the related work section, it appears that the author overlooked several works that also aim to provide differential privacy guarantees [1,2]. It would be valuable for the authors to provide comments on the relationship or differences between their approach and these existing works.

[1] Locally differentially private reinforcement learning for linear mixture markov decision processes.

[2] Differentially private reinforcement learning with linear function approximation.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces differential privacy (DP) to reinforcement learning with human feedback (RLHF). In RLHF, humans provide rankings for multiple (state, action) pairs (in LLM applications, (prompt, text) pairs) to train a reward model, which is used for downstream reinforcement learning tasks. This paper tries to study how to train the reward model while ensuring DP on the ranking dataset. To do this, this paper takes the theoretical model of [Zhu et al, 2023], which assumes that humans have real numerical preferences for (state, action) pair in a linear form $r_{\theta^*}(s, a) = \langle \theta^*, \phi(s, a)\rangle$ and sample rankings according to some classical probability models based on the numerical preferences (Bradley-Terry-Luce, Plackett-Luce). So, the central task is to learn the parameter $\theta^*$ differentially privately. The paper shows that this can be done by standard DP techniques. Also, the paper shows that the downstream reinforcement learning performance using a reward model with the DP-learned parameter is similar to that of the non-DP learned parameter.

### Strengths
(1) The problem is very well motivated and practically important. As RLHF is getting more popular, privacy becomes an increasingly important issue.

(2) This paper might be a good starting point for future works to explore further in the direction of "differentally private RLHF".

### Weaknesses
 (1) My major concern is the lack of experimental results. I know that this is a theoretical paper, but I do think experimental results are necessary here, for the following reasons: The purpose of introducing differential privacy to RLHF is to protect the privacy of the human data providers __in practice__. This paper's theoretical results provide upper bounds on privacy loss and the learning performance loss due to privacy guarantee, _under an idealized model_ ([Zhu et al, 2023]'s model). Humans' ranking behavior may not follow that idealized model, and the RLHF algorithms (for both the reward training and the downstream RL) used in practice are not necessarily the algorithms analyzed in this paper. Whether the theoretical results in this paper can be applied is questionable. Given that the theoretical contribution of this paper is only marginal (see below), I think an empirical contribution (trying DP on real datasets with real RLHF algorithms) is needed here.

(2) My second concern is that the technical contribution of this paper is marginal. The DP technique (adding Gaussian noises to the loss function and the solution in a convex optimization) is a standard technique from [Bassily et al, 2019a] and [Kifer et al, 2012]. The linear reward + BTL/PL model is the same as [Zhu et al, 2023]. The proofs of the theorems are basically a combination of the proofs from these two lines of previous work.

### Questions
**Questions:**

(1) How does [Zhu et al, 2023]'s idealized model capture real-world RLHF algorithms?

(2) How does adding DP to their model really inform RLHF in practice?



**Suggestions:**

Typos (that do not affect my rating):

1. Page 3, $T_h: S \times A \to \Delta(S)$
  
2. Page 4, Assumption 2.1: $r_\theta(s, a) = \langle \theta, \phi(s, a)\rangle$
  
3. Page 4, Definition 2.2: better to say that "... private if for all datasets $\mathcal D, \mathcal D'$ with $||\mathcal D - \mathcal D'||_1\le 1$, for all $\mathcal O\subseteq \mathrm{Range}(A)$, ..."
  
4. Page 8, equation (5): $\tilde \Sigma_{\mathcal{D}_K}$
  
5. Page 14, equation (8): $\langle \nabla \ell_D(\theta), \Delta) \rangle$
  
6. Page 14, Lemma A.5: "Then $f(\theta) - f(\hat \theta) \ge \frac{\gamma}{2}|| \hat \theta - \theta||_M^2$"

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims to offer DP guarantees to Zhu et al. (2023). To this end, the authors follow Zhu et al. (2023) to derive private version of estimation error bound and then use it to derive guarantees for offline RL as in Zhu et al. (2023)

### Strengths
Introducing DP is an interesting topic, especially consider private information in the labeling process

### Weaknesses
1. The techniques are quite standard and the results are straightforward
2. Only upper bounds are presented, no lower bound to show the tightness of the bound, especially in terms of the dependence of the privacy parameters.
3. No simulation results, which is somehow weird in ICLR conferences

### Questions
I do have several questions about this paper. In general, I think this paper is written in a somewhat sloppy way. 

1. In the first equation of proof of Theorem 4.2, the lambda is should be \sqrt{\lambda}.
2. The equation right above eq. 14 is not correct in terms of \gamma
3. The equation right after eq. 14 is not correct in terms of \lambda
4. More importantly, there must be some condition of the accuracy parameter \beta with respect to the privacy parameter and smoothness of the loss. This will in turn limit the value of the privacy parameter I think.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the privacy of reinforcement learning from human feedback. More specifically, given the dataset consisting of preference rankings, this paper proposes a method to learn rewards under the constraint of differential privacy. Furthermore, with the rewards satisfying DP constraints, the authors present an algorithm to learn a near-optimal policy. The sub-optimality bounds are shown to be minimax optimal.

### Strengths
1. The setting of privately learning rewards and policy from human feedback (preference rankings) is important.
2. This paper considers both the contextual bandit setting and the MDP setting.
3. The result is shown to be minimax optimal given $\epsilon$ is a constant, the proof looks correct to me.
4. The presentation is clear in general, the paper is easy to follow.

### Weaknesses
1. My main concern is about the technical difficulty. Algorithm 1 appears to be a standard application of objective perturbation, similar to the approach in [1]. Algorithm 2 seems to be a straightforward application of the Gaussian mechanism. Algorithm 3 is derived from replacing estimations with their private counterparts. The technical novelty compared to existing differentially private algorithms is not clearly articulated. Specifically, the paper should elaborate on the challenges introduced by the preference-based setting and how the proposed algorithms address them uniquely compared to standard differentially private optimization techniques.

2. The sub-optimality bound of $\tilde{O}(1/\sqrt{n\epsilon})$ is not optimal. As shown in [2], the additional cost due to DP could be of $\tilde{O}(1/n\epsilon)$ for empirical risk minimization. In addition, [3] shows that the additional cost due to DP could be of $\tilde{O}(1/n\epsilon)$ for offline RL tasks. The paper should provide a more thorough discussion on the challenges of achieving a tighter bound in this specific setting. Is the $\tilde{O}(1/\sqrt{n\epsilon})$ bound an artifact of the analysis, or is there a fundamental barrier preventing a tighter bound in the context of learning from human feedback?

3. For the MDP setting, the reward for a whole trajectory is still a linear function of $\theta$. Given that the occupancy measure $\rho$ is an input of Algorithm 3, is this setting identical to the contextual bandit setting? A clearer explanation of the differences and potential overlaps between the two settings would be beneficial.

4. It would be better if the authors could discuss more about the papers about RL with JDP or LDP guarantees and the relationship to this work. For instance, would an algorithm with JDP/LDP still be JDP/LDP if the rewards are learned privately (as in this paper)? Here are some papers regarding online RL with JDP/LDP that may be relevant. [4,5] considers RL with JDP and LDP for tabular MDP, while [6,7] considers RL with JDP and LDP for linear mixture MDPs.

5. There are many typos in the paper. Here I list the typos I find.

For the definition of $\Sigma_{D}$, the summation should go from $k=j+1$ instead of $j=k+1$ (Page 2).

The transition $T_h$ should be a mapping from $S\times A$ (Page 3).

For the occupancy measure $\rho_\pi$, where is the dependence on $h$ (Page 3)?

For the probability of the ranking, the summation should go from $j=k$ instead of $j=m$ (Page 4).

In equation (5), the '$\leq$' is missing (Page 8).

For the definition of $\hat{J}(\pi)$, the dependence on $v$ is missing (Page 9).

### Questions
Please see the weakness section. I will be willing to raise the score if my concerns (especially 1 & 2) are addressed.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

# Model-based RL as a Minimalist Approach to Horizon-Free and Second-Order Bounds

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 8, 6

## Abstract
Learning a transition model via Maximum Likelihood Estimation (MLE) followed by planning inside the learned model is perhaps the most standard and simplest Model-based Reinforcement Learning (RL) framework. In this work, we show that such a simple Model-based RL scheme, when equipped with optimistic and pessimistic planning procedures, achieves strong regret and sample complexity bounds in online and offline RL settings. Particularly, we demonstrate that under the conditions where the trajectory-wise reward is normalized between zero and one and the transition is time-homogenous, it achieves nearly horizon-free and second-order bounds. Nearly horizon-free means that our bounds have no polynomial dependence on the horizon of the Markov Decision Process. A second-order bound is a type of instance-dependent bound that scales with respect to the variances of the returns of the policies which can be small when the system is nearly deterministic and (or) the optimal policy has small values. We highlight that our algorithms are simple, fairly standard, and indeed have been extensively studied in the RL literature: they learn a model via MLE, build a version space around the MLE solution, and perform optimistic or pessimistic planning depending on whether operating in the online or offline mode. These algorithms do not rely on additional specialized algorithmic designs such as learning variances and performing variance-weighted learning and thus can easily leverage non-linear function approximations. The simplicity of the algorithms also implies that our horizon-free and second-order regret analysis is actually standard and mainly follows the general framework of optimism/pessimism in the face of uncertainty.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a minimalist approach to Model-Based Reinforcement Learning (RL) that leverages Maximum Likelihood Estimation (MLE) for learning transition models and integrates optimistic and pessimistic planning. The proposed scheme achieves strong regret and sample complexity bounds in both online and offline settings. It also provides nearly horizon-free and second-order bounds under certain conditions.

### Strengths
1. The authors provide solid theoretical analysis.

2. The methodology stands out due to its simplicity. The authors focus on using standard techniques (MLE, version space, optimistic/pessimistic planning) without introducing complex or specialized methods.

### Weaknesses
1. While the paper mentions the simplicity and standard nature of the algorithm, it lacks a direct comparison with other recent state-of-the-art Model-Based RL methods. A more explicit comparison would help highlight the contributions and potential advantages of this approach.

2. While the paper emphasizes it provides a nearly horizon-free result, I do not think it is a novel contribution with the assumption $r(s_h, a_h) \in [0,1 / H]$. I am more interested in approaches of [1,2], which also remove $\log T$ in their regret bound. Can you compare your work with these two papers?

3. The theoretical conclusions of this article are too dense and lack discussion.

### Questions
1. As I have mentioned in (2) in weaknesses, can you compare your horizon-free results with [1,2]?

2. The paper discusses the use of MLE for transition modeling. How does this choice impact the trade-offs between computational efficiency and the accuracy of the learned model in comparison to other model learning techniques (e.g., Bayesian approaches)?

3. How does the use of MLE for model learning affect the sensitivity of the model to noise in the environment, particularly in settings where the transitions are stochastic or partially observable? Can the methodology be adapted to handle such cases without compromising the theoretical bounds?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a minimalist model-based RL approach focused on achieving horizon-free and second-order bounds in both online and offline RL contexts. The authors advocate for using MLE for transition model learning, combined with optimistic planning in online RL and pessimistic planning in offline RL. The primary theoretical contribution is demonstrating that this straightforward MLE-based approach, which doesn’t require complex, variance-weighted learning procedures, achieves near-horizon-free sample complexity and second-order regret bounds. The analysis shows that this approach is effective in handling scenarios with either non-linear function approximations or time-homogeneous, low-variance policies, which benefit from the instance-dependent nature of second-order bounds.

### Strengths
1. The theoretical results show that performance does not heavily depend on the planning horizon, making this approach comparable to contextual bandits in complexity. The second-order bounds, scaling with policy variance, are particularly advantageous for nearly deterministic systems or policies with low variance.

2. The approach is designed to be versatile, working effectively in online, offline, and hybrid settings.

### Weaknesses
1. While the approach is theoretically sound, its reliance on computationally intensive MLE optimization could hinder scalability for larger or more complex model classes. To address this, it may be valuable to explore specific approximate MLE methods, such as variational inference or stochastic optimization. Alternatively, a discussion of computational complexity trade-offs could provide further clarity and practical guidance. The current analysis lacks a detailed consideration of the computational cost associated with the MLE step, particularly when dealing with high-dimensional state and action spaces or complex function approximators. This is a critical oversight, as the practical applicability of the method hinges on its computational feasibility. For instance, the paper does not discuss the number of iterations required for convergence of the MLE, nor does it provide any analysis of the time complexity as a function of the problem's dimensionality or the size of the dataset. This omission makes it difficult to assess the practical limitations of the proposed approach.

2. The paper presents strong theoretical contributions, but the lack of empirical validation on challenging RL tasks limits its practical impact. It would be helpful to evaluate the approach to environments such as tabular MDPs. Including such experiments would significantly strengthen the paper’s practical contributions. The absence of empirical results, even on simple benchmark environments, makes it difficult to assess the practical relevance of the theoretical findings. While the theoretical analysis provides guarantees on sample complexity and regret, it is unclear how these guarantees translate into actual performance in practice. For example, it would be valuable to see how the proposed method performs in comparison to existing model-based RL algorithms on standard benchmark tasks. Furthermore, the paper does not discuss the sensitivity of the algorithm to hyperparameter settings, which is crucial for practical implementation.

### Questions
1. Given that the current approach is theoretically sound but may be computationally intense, are there approximate methods that could retain accuracy while reducing computational demands?

2. What are the implications if the assumed model class does not include the true dynamics of the environment? Could the algorithm's performance degrade, and if so, how might this be mitigated?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper identifies minimalist reinforcement learning (RL) algorithms that can achieve nearly horizon-free and instance-dependent regret and sample complexity bounds,in both online and offline RL with non-linear function approximation. Based on a leverage of triangular discrimination, it demonstrates that existing standard model-based RL algorithms, using maximum likelihood estimation (MLE) for model learning and optimistic or pessimistic planning depending on the setting (online or offline), are sufficient to achieve these performance goals.

### Strengths
This paper explores horizon-free reinforcement learning (RL) within the context of general function approximations, which is a more challenging and generalized setting compared to prior work on tabular or linear MDPs. Theoretical analysis is solid, leveraging triangular discrimination to demonstrate that existing standard model-based algorithms can already achieve horizon-free regret. This analysis could be inspiring for future research in horizon-free RL. Furthermore, the paper provides a second-order instance-dependent upper bound, which can be particularly tight when the variance is low, yielding improved sample complexity in deterministic environments. Finally, the writing is logical, with ideas presented smoothly.

### Weaknesses
It's clear that this paper is purely focused on theoretical contributions. I think the primary weakness is the lack of intuitive insight into how triangular discrimination specifically assists in achieving horizon-free and second-order upper bounds. Although a proof sketch is provided, the underlying intuition remains somewhat unclear. A more detailed explanation of how the triangular discrimination is used to bound the error propagation in the Bellman updates would be beneficial. Specifically, how does this metric allow for tighter control over the error accumulation across the planning horizon, and why is it more effective than other divergence measures in this context? A concrete example, perhaps illustrating a simple MDP, could help clarify this.

### Questions
1. Are the assumptions listed on page 4 and in Definition 3 the only ones required for Theorem 2? I’m curious about this, as I would like to gain a better understanding of the factors contributing to the improved results compared to [1].

2. What do you think is the key barrier when attempting to apply a similar analysis to model-free methods? This question is not necessary to be replied.

[1] Uehara, M., & Sun, W. (2021). Pessimistic model-based offline reinforcement learning under partial coverage. arXiv preprint arXiv:2107.06226.

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
3

### Summary
The paper studies model-based RL in MDPs with possibly infinite state-action spaces and total returns bounded in [0,1]. The authors show that a simple approach consisting of learning a version space around the MLE of the transition kernel and performing optimistic/pessimistic planning on top of it achieves strong horizon-free and second-order bounds in online/offline RL.

### Strengths
1. The paper presents novel and strong results. To my knowledge, the ones studied here are the simplest algorithms to be shown to achieve both horizon-free and second-order bounds (eg, most prior works required specific algorithmic tweaks to this purpose). Due to the popularity of MLE-based approaches, I think this is a relevant result
2. The paper studies both the online and offline RL settings
3. I particularly appreciated the corollaries for MDPs with deterministic transition kernel, which I think is an understudied setting despite its practical relevance
4. Although I only skimmed through the proofs, they do seem sound
5. Relevant literature is properly discussed

### Weaknesses
1. My main concern is that the paper is quite hard to follow, extremely technical, and lacks some clarity in many points. More precisely, the paper is basically a list of theorems/lemmas/corollaries/definitions without too many explanations: several terms that may only be familiar to experts in this line of works are not introduced with sufficient detail and many choices are not motivated. For example,
- it is not clear why the assumption that trajectory returns are in [0,1] is reasonable in practice
- for offline RL, it is not clear why the assumption that the dataset contains trajectories is needed (lines 181-191). Can't you have only transitions?
- the definition of Eluder dimension is not clear (eg what's an epsilon-independent sequence?). It is clearer in prior works
- not clear why the bounds use the function class \Psi defined at lines 258-259. Eg, why not using P itself, which after all is the hypothesis space used for learning?
- In Section 4, it is never explicitly stated that the results before the paragraph "Extension to infinite class P" focus on finite P (the reader has to figure it out from the definition of beta)
- not clear why using bracketing numbers in the analysis. Eg how do they compare to the more standard covering numbers (if there is any difference)? Also, it be great to give examples of what those are for "common" function classes (eg when P is linear)
- not clear how the "single-policy coverage" of Def. 3 compares to the more standard concentrability coefficients defined as ratios between policy visitation distributions used in the offline RL literature
2. The algorithms studied here are both intractable due to the fact that they have to build a version space of transition kernels around the MLE. This is only tractable for simple function classes (eg finite) and limits the practical relevance of this work. Also, I feel this breaks a bit the overall story about the "simplicity" of the approaches. Eg, the conclusions state "we presented a minimalist approach for achieving nearly horizon-free and second-order bounds in online and offline RL: simply train transition models via Maximum Likelihood Estimation followed by optimistic or pessimistic planning", but I don't think this is properly correct: it gives the impression that all we have to do is MLE, but we do have to build version spaces around it, and that's not an easy thing.
3. Lines 171-172: "Without loss of generality, we assume V \in [0,1]". I don't think this is without loss of generality, as the filtering approach proposed in footnote 2 would require doing policy-evaluation for many policies and transition kernels, which is what we want to avoid during training in the first place with an MLE approach
4. [minor] the abstract is very verbose, and I felt many details could have been omitted without altering its quality

### Questions
1. See clarification questions above
2. The bound in Example 1 for tabular MDPs seems to have a worse dependence in SA that existing bounds for the same setting (see eg Jin et al. 2020 or Appendix C in Al-Marjani et al. 2023) despite having a better dependence in H. Any intuition why this happens?

[Jin et al. 2020] Jin, C., Krishnamurthy, A., Simchowitz, M., & Yu, T. (2020, November). Reward-free exploration for reinforcement learning. In International Conference on Machine Learning (pp. 4870-4879). PMLR.
[Al-Marjani et al. 2023] Al-Marjani, A., Tirinzoni, A., & Kaufmann, E. (2023, July). Active coverage for pac reinforcement learning. In The Thirty Sixth Annual Conference on Learning Theory (pp. 5044-5109). PMLR.

### Soundness
3

### Presentation
2

### Contribution
3

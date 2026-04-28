# Provable Offline Preference-Based Reinforcement Learning

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 6, 8, 8

## Abstract
In this paper, we investigate the problem of offline Preference-based Reinforcement Learning (PbRL) with human feedback where feedback is available in the form of preference between trajectory pairs rather than explicit rewards. Our proposed algorithm consists of two main steps: (1) estimate the implicit reward using Maximum Likelihood Estimation (MLE) with general function approximation from offline data and (2) solve a distributionally robust planning problem over a confidence set around the MLE. We consider the general reward setting where the reward can be defined over the whole trajectory and provide a novel guarantee that allows us to learn any target policy with a polynomial number of samples, as long as the target policy is covered by the offline data. This guarantee is the first of its kind with general function approximation. To measure the coverage of the target policy, we introduce a new single-policy concentrability coefficient, which can be upper bounded by the per-trajectory concentrability coefficient. We also establish lower bounds that highlight the necessity of such concentrability and the difference from standard RL, where state-action-wise rewards are directly observed. We further extend and analyze our algorithm when the feedback is given over action pairs.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper analyzes preference-based reinforcement learning in offline setting. Specifically, they propose three algorithms for Offline PbRL. One estimates the reward function using MLE, constructs confidence sets around the MLE and optimizes the policy against the worst reward model under the assumptions that the transition probabilities are known. The second algorithm is similar to the first except that it operates under the assumptions that the transition probabilities are unknown. The algorithm estimates the transition probabilities using MLE and constructs uncertainty sets around the MLE of the transition probabilities. It then optimizes the policy against the worst reward model and the transition probabilities in their respective uncertainty sets. The third algorithm considers the case where preferences are established over actions instead of trajectories. It estimates the advantage function and computes a greedy policy based on the advantage function.
While the paper does not empirically evaluate these algorithms, they theoretically analyze the sample complexity and performance error of the algorithms and show that as long as the offline data covers the target policy,  it can compete with the target policy.
They also show that even if the reward is trajectory wise, you can still efficiently learn the policy if the transition dynamics are estimated per step.
Finally, the paper establishes a partial coverage guarantees for the third algorithm and show that the sample complexity scales with a bound on the advantage function.

### Strengths
The paper is clearly written.
The paper provides several strong and novel theoretically results on preference-based RL in offline setting. Some of these results also generalize the results of Zhu et al for linear function approximators to general function approximators.

### Weaknesses
Although the main contribution is theoretical, it would be nice to see an empirical case study or two  where the given algorithm works as expected.

### Questions
No questions.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper aims to investigate preferance based offline reinforcement learning. They consider a setting where the dataset consists of trajectory pairs with a preference. They assume a preference model over the trajectories and come up with an algorithm which has two parts, the first to obtain a confidence set of reward functions using maximum likelihood estimation and the second part is to obtain the policy over this confidence set. Their algorithm provides a guarantee that allows to learn the target policy with a polynomial number of samples.

### Strengths
(1) The problem of reinforcement learning with human feedback, specifically offline preference learning is highly relevant. 

(2) Their algorithm provides a guarantee of being able to learn the target policy using polynomial number of samples.

(3) They extend their algorithm to settings with unknown transition kernel and state-action preferences.

(4) They introduce a new single-policy concentrability coefficient to measure the coverage of the target policy on the dataset.

### Weaknesses
 (1) There are no implementation details about the algorithms. These algorithms are theoretically sound but there is no intuition for the reader on how to implement them or construct a practical algorithm. 

(2) There are no experiments either. So there is no way to check how this method empirically scales. 

(3) Several terms in the paper are not well explained. For example, $\epsilon$-bracketing: what do you mean by g(.|tau1, tau2)? Is g a probability measure, or a preference? The definition of $g$ as a function mapping from trajectory pairs to $\mathbb{R}^2$ is unclear, especially how it relates to a preference model or reward function.  A more precise definition is needed to understand its role in the algorithm. 

(4) Proposition 1: For epsilon being arbitrarily small, and the bounds B and R being arbitrarily large, log N_G_r can be arbitrarily large making the sample bounds weak. The dependence on the log of the bracketing number, which itself depends on the reward function's complexity, makes the sample complexity bound less informative.  The practical implications of this dependence are not discussed.

(5) The sample bounds i.e. sample complexity N = O(..log (..1/N)). How can N be on both sides, something seems missing. The expression for sample complexity is not well-defined, as it has the sample size, N, on both sides of the equation, which is mathematically inconsistent. This needs clarification to be a valid bound.

### Questions
(1) In Section 4.1, it is mentioned the distance between r and r* is computed as total variation distance or l1 norm. Arent r and r* scalars? 

(2) Does C_tr (per trajectory concentration coefficient) not depend on \mu_1? If so, why?

(3) How does C_r(G_r, \pi_tar, \u_1) reduce to sqrt(Ctr)?

(4) It looks like pi, mu and d are used interchangeably. I recommend correcting this.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
### Contributions
* This paper proposed the first algorithm for offline trajectory-wise PbRL with general function approximation and under partial coverage.
    * The reward function can be defined over the whole trajectory, or for each state action pair.
    * Extending to the case where transition kernel is also learned, and the case where data is composed of action comparisons, rather than trajectory comparisons.
* Setting: finite horizon MDP with trajectory-wise reward.
* Preference model: known link function.
* Goal: ϵ-δ PAC offline RL: use offline dataset {(traj 1, traj 2, preference signal)} to learn the optimal policy, with unknown reward (extended to also unknown transition kernels).
* Key innovation: function approximation
    * Use a given realizable function class Gr to learn the reward function r.
    * Measure the complexity as the ϵ-bracketing number of the set of preferences induced by Gr.
* If transition kernels is known:
    * Algorithm
        * (1) MLE the reward, r\hat, using the data; (2) construct a confidence set around r\hat; (3) distributionally robust planning to jointly max total reward and stay close to some reference trajectory, under the worst-case reward in the confidence set.
    * Analysis
        * This paper developed concentrability coefficient for preference-based feedback (Sec.4.2) and discuss the relation bw per-trajectory concentrability coefficient vs per-step concentrability coefficient (Sec.4.3). This result indicates that trajectory-wise feedback is intrinsically harder than step-wise feedback in offline PbRL.
        * The resulting PAC bound (under Eq.2) depends on this coefficient and also the ϵ-bracketing number of the function class.
* If transition kernels is unknown:
    * Algorithm: also do MLE and confidence set for transition kernel.
    * Analysis: concentrability coefficient.
* If action-based comparison:
    * Assuming that the preference feedback is based on the Q value at the state with two actions.
    * Algorithm: MLE the advantage function and output the greedy policy.
    * Analysis: concentrability coefficient.

### Strengths
* The algorithm and analysis are sound.
* Considering multiple cases, e.g., unknown transition, action-based comparison, and fitting them within similar algorithmic framework.
* Nice comparison with previous work in Sec.4.1, Remark 2, 4.

### Weaknesses
 * This paper is fully focusing on theory. It would be nice to also have some empirical results.


### Questions
* It seems to me that the link function in Eq.1 is known? Would it work if the link function is unknown?
* For unknown transition kernels, would the result extend to the case where the transition kernels' data are sampled separately from the preference data?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a PbRL algorithm via computing a return utility function, based on MLE. They then construct a confidence set, based on that estimate to solve a planning problem for deriving an approximate, optimal policy. In contrast to most PbRL work, they do not assume the existence of state-action utility. 
This algorithm forms the base for analyzing the algorithms sample complexity, using a novel trajectory-based concentration coefficient. This analysis is also applied to a setting with learned transition dynamics and action preferences.

### Strengths
Most work in PbRL focuses on empirical evaluations, therefore additional work considering the theoretical background is important. This work is especially relevant, as it is not restricted to a specific class of function approximation and considers return-based utility. Reward-based utility is usually easier to handle, but can induce abnormalities in the preference setting, therefore the return-generalization is also highly interesting. Adapting the concentrability coefficient to this setting is interesting as it allows to separate (offline) optimization of the policy from the issues of exploration/exploitation.

### Weaknesses
The most substantial weakness of the paper is that the related work focuses primarily on theoretical contributions, neglecting a thorough comparison with practical algorithms. For instance, the concept of return-based utility approximation is not novel, with prior work such as "Preference-Based Policy Learning" [1] and others detailed in "A survey of preference-based reinforcement learning methods" [2] exploring similar ideas. This omission is significant for two reasons. First, it hinders the reader's ability to identify which existing algorithms fall within the proposed framework. Second, it obscures the distinctions between the proposed algorithm and prior art. Given that the algorithm is presented as a key contribution, yet likelihood-based estimation of return utility is already established, the novelty of the algorithm appears somewhat limited.

Besides that, there are several possibilities to improve the presentation:
- Reward is defined wrt. trajectories, but this is commonly denoted return in the PbRL literature
- Some relevant information is left to the appendix - mostly the feasible implementation and the comparison to "Principled reinforcement learning with human feedback from pairwise or k-wise comparisons" [3]. Especially some details concerning the feasible implementation are relevant for practioners.
- Remark 3 is not explained

Furthermore, to the reviewer, one of the statements is not obvious:
- cannot be relaxed to the per-step concentrability without additional assumptions, such as on the reward structure - Why does it follow from the Theorems, that state-action rewards are not enabling this?

As small remarks:
- Missing reference: "..per-step concentrability coefficient Cst commonly used in the general offline RL literature"
- Missing reference: "..It is well-known that when the reward is state-action-wise, the optimal policy π is both Markovian and deterministic."
- Definition 1 is a bit hard to understand, because g is never define.
- The slack parameter in Sec. 4.1 has the wrong symbol
- Typo in Alg 2: "Distributionally robust plnanning"

### Questions
Please explain "cannot be relaxed to the per-step concentrability without additional assumptions, such as on the reward structure" (see above)

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

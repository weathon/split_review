# Horizon-free Reinforcement Learning in Adversarial Linear Mixture MDPs

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Recent studies have shown that episodic reinforcement learning (RL) is no harder than bandits when the total reward is bounded by $1$, and proved regret bounds that have a polylogarithmic dependence on the planning horizon $H$. However, it remains an open question that if such results can be carried over to adversarial RL, where the reward is adversarially chosen at each episode. In this paper, we answer this question affirmatively by proposing the first horizon-free policy search algorithm. To tackle the challenges caused by exploration and adversarially chosen reward, our algorithm employs (1) a \emph{variance-uncertainty-aware} weighted least square estimator for the transition kernel; and (2) an \emph{occupancy measure}-based technique for the online search of a \emph{stochastic} policy. We show that our algorithm achieves an $\tilde{O}\big((d+\log (|\cS|^2 |\cA|))\sqrt{K}\big)$ regret with full-information feedback\footnote[2]{Here $\tilde{O}(\cdot)$ hides logarithmic factors of $H$, $K$ and $1/\delta$.}, where $d$ is the dimension of a known feature mapping linearly parametrizing the unknown transition kernel of the MDP, $K$ is the number of episodes, $|\cS|$ and $|\cA|$ are the cardinalities of the state and action spaces. We also provide hardness results and regret lower bounds to justify the near optimality of our algorithm and the unavoidability of $\log|\cS|$ and $\log|\cA|$ in the regret bound.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the online learning problem of horizon-free and linear mixture Markov Decision Processes (MDPs). 
To the best of my knowledge, this is the first paper that can achieve theoretical guarantees with adversarial losses, that is, the loss function can change arbitrarily from episode to episode. 
To achieve this result, the authors propose two main techniques: (1) a variance-uncertainty-aware weighted least square estimator and (2) an occupancy measure-based approach for constructing policies. The first technique is widely use for linear mixture MDPs, while the second one is mainly used for adversarial losses. 
Combining these two techniques to establish valid regret guarantees is quite challenging. 
More importantly, the final regret bound is of the order $O(d\sqrt{K})$, which is nearly the optimal.

### Strengths
1. The idea of combining the two techniques is very interesting. It would be great to see such combination to be applied in other (more general) linear MDP settings.  
2. Though I just skimmed the proof of several lemmas, the results seems to be rigorous proved and mathematically correct.

### Weaknesses
This paper does not have any specific weaknesses.

### Questions
1.Is it possible to design policy optimization algorithms for this problem setting? 
2.Is it possible to avoid the usage of occupancy measure (which is not quite efficient in real world).

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
This paper addresses the question of whether the favorable polylogarithmic regret seen in reinforcement learning (RL) with respect to the planning horizon can also be extended to adversarial RL scenarios. The authors introduce the first horizon-independent policy search algorithm, designed to cope with challenges arising from exploration and adversarial reward selection over episodes. The algorithm utilizes a variance-uncertainty-aware weighted least square estimator for the transition kernel and an occupancy measure-based approach for online stochastic policy search.

### Strengths
Given my limited expertise in the adversarial RL domain, my evaluation focuses exclusively on the technical soundness and clarity of the paper. The manuscript exhibits a commendable standard of articulation. The framing of the problem, underlying assumptions, and derived outcomes are adequately elucidated. Notably, the inclusion of a proof sketch in Section 6 enhances the paper's comprehensibility, serving as a valuable reference point for those seeking deeper insight into the paper's theoretical foundations.

### Weaknesses
The paper makes relatively strong assumptions: linear, finite-state MDPs and full-information feedback. The only novel aspect here is the paper tackles adversarial reward functions rather than fixed or stochastic rewards. But even so, I think that the full-information feedback assumptions greatly alleviate the difficulty of adversarial rewards. To me, the hardness result is more interesting: an unbounded state space will incur regret in $\Omega(\sqrt{H})$. Is this result novel in the literature?

I am a bit confused about the assumptions about the reward. Firstly, can the rewards be negative? If so, would assumption 3.1 still make sense? Furthermore, is assumption 3.1 equivalent to the bounded rewards assumption, i.e., if rewards are bounded in $[-R, R]$, we can always scale everything by $1/RH$ to satisfy assumption 3.1.

### Questions
Please see the questions in the weaknesses section above. I am happy to increase my score if there are any misunderstandings.

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
This paper introduces the first algorithm enjoying horizon free bounds for the adversarial linear mixture MDP. The algorithm is based on a careful combination of policy updates step performed with mirror descent steps in the occupancy measures space and an optimistic policy evaluation phase carried out using weighted ridge regression estimators.

An interesting finding is also a separation between the adversarial and non adversarial case. Indeed, the authors managed to prove an asymptothic lower bounds which shows that either $\sqrt{H}$ or $\log S$ must be paid in the regret bound while a $S$ independent horizon free regret upper bound can be obtained in the non adversarial case.

### Strengths
I think that the algorithm is original and well explained in the main text.

The result which entails a $\log S$ dependence would not be very satisfactory in the function approximation setting but the author nicely shows that either this dependence or a $\sqrt{H}$ dependence must be suffered.

I also enjoyed the lower bound construction which considers a tabular deterministic MDP and reduces it to an expert problem.

The proofs look correct to me.

### Weaknesses
There are few clarity omission or missing definition in the submission. Hereafter, I list few of them:

- I think it should be clearer that also homogenous transition dynamics are required for obtaining reward free bounds. Therefore, the Bellman optimality equation at page 3 should not have $h$ in the footnote of the operator $\mathbb{P}$. The current notation suggests that the transition kernel might be different at each step $h$, which is not the case for the reward-free setting the authors consider. This is a crucial distinction that needs to be explicitly stated to avoid confusion.

- the value function $\overline{V_{k,1}}$ is never formally defined in the paper. So it is difficult to understand what it denotes when reading the regret decomposition in equation (6.1). It's unclear how this value function relates to the policy and transition kernel at iteration $k$. Without a precise definition, the reader is left to guess its meaning, which hinders the understanding of the regret analysis. If I understood correctly from the Appendix, each mirror descent iterate $z_k$ induces via the marginals a transition kernel $\overline{p_{k}}$ and a policy $\pi_k$. At this point $\overline{V_{k,1}}$ denotes the initial value of policy $\pi_k$ in the MDP endowed with reward function $r_k$ and transition dynamics $\bar{p}_k$. Can the authors confirm that this is correct and if yes add it to their revision ?

- The definition of Regret at page 3 is a bit unclear. Indeed saying that $V^\star_k$ is the optimal state value function could make the reader believe that $V^\star_k = \max_{\pi} V^{\pi}_k$, that is the regret we control has the maximum inside the sum. However, the regret controlled in the paper has a fixed comparator policy which might not be optimal for any of the reward function revealed at each round. This distinction is important because it affects the interpretation of the regret bound. The current definition is ambiguous and needs to be clarified to avoid misinterpretations.

### Questions
I think that it is unclear that $I^k_h$ defined in Appendix C.2 is decreasing. After inspecting the proofs I think that what the authors need is that for any fixed $k$ than $I^k_h$ is decreasing with respect to $h$. Is this correct ?

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
This paper studies horizon-free RL in adversarial linear mixture MDPs with full-information feedback. This paper proposes an algorithm that employs a variance-aware weighted least square for the transition kernel and an occupancy measure-based method for the online search of a stochastic policy. The authors show the algorithm achieves a regret with polylogarithmic dependence on $H$. Further, this paper provides a lower bound showing the inevitable polylogarithmic dependence on state number $S$.

### Strengths
1. The paper is the first work that studies near-optimal horizon-free RL algorithms under adversarial reward and linear function approximation. This progress deserves to be known to the community.
2. The connection between the value function derived from occupancy measure guided policy updating and the other one derived from backward iteration (Lemma 6.1) is new as far as I know, which may inspire other studies for RL problems.
3. The paper is clearly written and well-organized. The proofs are technical sound though I don't check the proofs.

### Weaknesses
1. The novelty of this paper may be limited. Most of the analysis follows from that of horizon-free reinforcement learning for linear mixture MDPs with stochastic rewards (Zhou and Gu, 2022).
2. The occupancy measure-based algorithm is not computationally efficient as the running time has polynomial dependence on the state number $S$ and action number $A$. Specifically, the need to compute and store the occupancy measure for all states, which scales linearly with $S$, makes the algorithm impractical for large state spaces. Furthermore, the policy update step, which involves iterating over all states and actions, also contributes to the computational bottleneck, resulting in a running time that is at least $O(SA)$ per iteration. This high computational cost significantly limits the applicability of the proposed algorithm in real-world scenarios with large state and action spaces.

### Questions
N/A

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

# Minimax Optimal Regret Bound for Reinforcement Learning with Trajectory Feedback

- Decision: Reject
- Scores: 6, 8, 5, 5, 3, 6

## Abstract
We study the reinforcement learning (RL) problem with trajectory feedback. The trajectory feedback based reinforcement learning problem, where the learner can only observe the accumulative noised reward along the trajectory, is particularly suitable for the practical scenarios where the agent suffers extensively from querying the reward in each single step. For a finite-horizon Markov Decision Process (MDP) with $S$ states, $A$ actions and a horizon length of $H$, we develop an algorithm that enjoys an optimal regret of $\tilde{O}\left(\sqrt{SAH^3K}\right)$ in $K$ episodes for sufficiently large $K$. To achieve this, our technical contributions are two-fold: (1) we incorporate reinforcement learning with linear bandits problem to construct a tighter confidence region for the reward function; (2) we construct a reference transition model to better guide the exploration process.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper addresses reinforcement learning with trajectory feedback, where the reward in a Markov Decision Process is not observed throughout an episode but only as a cumulative reward at the episode’s end. The authors propose an algorithm that achieves a regret bound with statistical behavior comparable to the state of the art in standard reinforcement learning literature.

### Strengths
The paper proposes an algorithm that achieves a better asymptotic regret bound than those previously established for reinforcement learning with trajectory feedback. The authors employ a novel method in their proofs, which appears robust.

### Weaknesses
First, I must admit that I am not well-versed in the literature on regret bounds in reinforcement learning with bandits.

To me, the framework of this paper appears quite limited. The assumption that the learner receives trajectory feedback, specifically the cumulative reward at the end of an episode, rather than individual rewards at each step, seems to significantly restrict the applicability of the proposed algorithm to real-world scenarios. Many reinforcement learning problems inherently involve intermediate rewards that guide the learning process. Furthermore, the asymptotic regret bounds, while presented as an improvement, appear to be in the same order of magnitude as those achieved in more classical frameworks with per-step rewards. This raises the question of whether the proposed method offers a substantial practical advantage, given its limited scope. It gives the impression that the work involves only minor modifications to standard proofs, potentially just adapting existing techniques to a more constrained setting. However, I may be mistaken, as I am not deeply familiar with this literature.

### Questions
Here are few questions :
1. Could the authors elaborate on the statement in lines 261–262: "Therefore, by running [...] for some constant $c>0$"? A more detailed explanation of this step would be helpful.
2. The definition of the set in (10) seems unclear to me. First, how do the authors compute $\max W^{\pi'}(\hat{R},P)$? Additionally, how is the quantity on the right-hand side of the selection criterion, i.e., the practical value of $\tilde{O}$?
3. Can the method employed in this paper be adapted to consider cases where $K$ is not that large compared to $S$, $A$ and $H$, similar to the approach in [Zhang et al.]?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper studies a RL problem with delayed rewards, which are sampled after letting a trajectory roll out for a certain time horizon. This is a practical scenario that appears in several applications and that, to date, doesn't have a detailed and comprehensive solution. The paper shows how optimal regrets can be obtained that are similar to those of traditional RL algorithms.

### Strengths
The paper studies a novel and interesting variant of the standard RL problem, where rewards are generated with a delay rather than at each time instants. The provided bounds are technically sound and improve upon the existing literature.

### Weaknesses
1. Rewards are assumed to be a linear function of the trajectory (sequence of states and actions). This may not be practical in real-life. This is not practical even in the case discussed in the introduction - medical care. The assumption of linearity severely limits the applicability of the proposed method to real-world scenarios where reward functions are often complex and non-linear. For instance, in medical care, the effectiveness of a treatment plan is rarely a simple linear combination of the actions taken and the patient's state trajectory.

2. Learning the optimal policy, with the assumption of linear rewards, is now a (linear) regression problem. This is the main part from where the similarity between regret bounds for traditional RL and the proposed method arises. Can you comment on more complicated or realistic bandit models? The reliance on linear regression, while simplifying the analysis, sidesteps the core challenges of reinforcement learning with complex state-action spaces and non-linear reward structures. The connection to linear bandits is interesting, but it also highlights the limitations of this approach in addressing more general RL problems. The paper should discuss how the method could be extended to handle more realistic reward structures.

3. Using a parameterized policy that can be systematically updated after the end of each trajectory, instead of policy elimination, might result in tighter regret bounds. Is this the case? The paper's use of policy elimination, while providing theoretical guarantees, might be suboptimal compared to methods that directly optimize a parameterized policy. Policy elimination can be inefficient, especially when the policy space is large, and may lead to slower convergence compared to gradient-based methods that can leverage the structure of the policy space.

### Questions
Do the methods/ideas extend to cases where rewards are nonlinear functions of the trajectories?

The connections to linear bandits is interesting, and it would be beneficial to expand upon this connection (formulation and examples). The literature in this area is also rather extensive, and a more comprehensive review/comparison would be helpful.

Some numerical/illustrative examples could help the reader appreciate the theoretical results.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper considers the episodic reinforcement learning with trajectory feedback. In this paper, the authors proposed an online learning algorithm that achieves optimal regret which scales as sqrt(SAH^3K). Unlike existing methods directly applied linear bandit, the proposed algorithm does not suffer from the regret with higher order on S.

### Strengths
This paper provides rigorous theoretically analysis for the proposed approach. Instead of building confidence region as linear bandit, the proposed algorithm maintain a policy set within a constant range, which can be done through data sampling in batches. The theoretical motivation behind this idea is very clearly presented in the paper with rigorous proofs. 
Comparing to existing work, the proposed algorithm achieve optimal regret bound for RL with trajectory feedback only. Given the trajectory feedback is more general for real application, the proposed work has a potential to be applied to real problem with better performance guarantees.

### Weaknesses
The paper focuses on proposing an algorithm that achieves a tighter regret bound. While the rigorous proofs are appreciated, a more comprehensive comparison would help with understanding the importance of the difference. It would be beneficial to see a comparison, perhaps through a toy experiment, illustrating how a standard linear bandit approach performs in an episodic MDP environment, especially when the state/action space is large and the time horizon is long. This would help to empirically demonstrate the practical advantages of the proposed method. Furthermore, while the theoretical analysis is strong, the paper does not adequately address the computational complexity of the proposed algorithm. Since the algorithm still requires exponential time cost, a more detailed comparison of the computational complexity with existing methods is needed to fully understand its practical limitations.

### Questions
Beside what I wrote in the previous section, I would also like to understand more about Theorem 1 and 7. The statement of 'a RL problem with trajectory feedback has the same asymptotically optimal regret as standard RL' is a very intriguing result. I would like to read more explanation on the interpretation of Theorem 7 in the papaer.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors present a regret bound for RL with trajectory feedback. The lower bounds improves upon existing results reducing the dependency in the state space and are minimax optimal. To achieve the bounds, the authors use better confidence bounds than previous work and a more refined exploration scheme.

### Strengths
A strong theoretical result improving upon SOTA for an important problem

Refined techniques for a well studied problem

I appreciate the authors' attempt to provide an informal explanation of the proofs. It is not trivial.

### Weaknesses
I am curious to have a formal understanding of the term "for sufficiently large K" when presenting THM1. This is important because it can render the result. Specifically, without a precise definition of how large K needs to be, the practical applicability of the bound is unclear. The authors should provide an explicit lower bound on K for the theorem to hold, and discuss the implications of this bound in terms of the problem parameters.

The presentation of the algorithm is convoluted. Especially. it is not clear what is Design in Algorithm 5. The description of the 'Design' step lacks sufficient detail, making it difficult to understand its purpose and implementation. The algorithm would benefit from a more modular presentation, breaking down complex steps into simpler, more understandable components. The lack of clarity in this part of the algorithm makes it hard to assess its practical feasibility.

The last term in THM 7 is kind of disappointing as it renders the result less exciting. The presence of the lower order term, which is not explicitly defined, significantly weakens the impact of the main result. This term needs to be more precisely characterized, and its implications for the overall regret bound should be discussed in more detail. It is not clear if this term can be further reduced or if it represents a fundamental limitation of the approach.

I believe the examples in the introduction were discussed by others before. A proper reference is needed. The lack of proper attribution undermines the novelty of the problem setup. The authors should provide specific citations to prior work that have discussed similar examples to properly contextualize their contribution.

There are some typos in the text that should be fixed: e.g., "ofte" (l46) and "fro" (l250)

### Questions
Q1: Please elucidate the initial K issue. 

Q2: The paper seems incremental wrt Efroni et al (2021). What is the main contribution wrt Efroni et al?
Is it a mix and match of a model and know techniques? If not, are the new techniques applicable elsewhere?

Q3: Can you say something about the constant c>0 in l262? Does it depend on the problem itself?

Q4: L282-285: as far as I understand the statement "it holds that \pi^* \in \Pi_{\ell+1}" is a high probability even rather than an almost sure statement. So, if I don't understand what is going on. More specifically, for any finite T or K_\ell all elements in Eq (9) and after are random variables, but they seem to be treated as fixed because everything is taken in the limit. But it cannot be taken as such (at least not without a proof). I am probably missing something here, but this seems like a loose usage of \tilde{O} notations. Please explain.

Q5: How is K_0 set in Algorithm 1?

Q6: It seems to me that the computation needed for Algorithm 5, line 9 would be quite difficult. Is this correct? Can you say something about the complexity of the different algorithms?

Q7: What do you suspect is the real dependence of the low order terms in THM7? 

I would be happy to raise my score if the questions above are answered properly, especially Q4.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes an algorithm that achieves a minimax optimal regret bound for RL with trajectory feedback. Specifically, the proposed algorithm achieves a regret bound of $\tilde{O}(\sqrt{SAH^3K})$ for an episodic MDP.

### Strengths
- The paper tackles a well-motivated problem, proposing an asymptotically optimal regret bound algorithm for scenarios with trajectory-level feedback.

- Up to Section 4, the authors clearly present their motivations, objectives and proof sketch, making it easier for readers to grasp the core concepts of the paper.

### Weaknesses
The paper has numerous typos and complex, undefined notations, giving the impression of a hastily composed and unpolished draft. The structure and expressions appear to be inspired by [1], yet there are instances of notations that are either not used or are undefined in the context of this paper. A thorough revision to polish the paper would improve its clarity.

In particular, Section 5 lacks logical flow, as many concepts are listed without a thorough theoretical explanation, making it difficult for readers to follow, especially given the insufficient description of each pseudocode. Considering page limitations, substituting theoretical proofs with a more accessible explanation of the pseudocode in the main paper could enhance readability.

The proposed algorithm also appears to have impractical elements. See Questions.

Typos

- Line 46: "ofte" should be "often"

- Algorithm 2: $\mathcal{D}_2$ is not defined

- Algorithm 3, Line 3: The font of “plan” needs correction

- Line 388: "we" should be capitalized to "We"

- Line 483: $S^1 1$ should be corrected to $S^{11}$

- Algorithm 5: $\lambda_\pi$ is not defined.

### Questions
- On line 310, optimization is mentioned for the double-state reward function $r(s,s',h,h')$. Could the authors provide more detail on this?

- In Algorithm 4, Line 7, does $\bar{\pi}$ refer to what is stated in Eq (6)? Is it possible to obtain $\bar{\pi}$ in a tractable manner?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies reinforcement learning (RL) with trajectory feedback. The learner can only observe the accumulative noisy reward once a trajectory is terminated. The state transition model is unknown to the learner. The paper develops an online learning algorithm and shows that its regret bound is optimal.

### Strengths
1. The paper is well-written and easy to follow.
2. RL with trajectory feedback is an interesting problem.
3. This is a solid theory paper. The analysis is rigorous and sound.

### Weaknesses
1. There is no experiment.
2. In the upper bound of Theorem 7, the last three terms dominate. In contrast, the abstract and the introduction claim that the upper bound is determined by the first term. The authors should clarify under what conditions, if any, the first term dominates. If the first term is not asymptotically dominant, the authors should explain why they only focus on the first term in the abstract and the introduction. Furthermore, the paper should discuss the practical implications of the last three terms dominating the regret bound, especially in scenarios with long horizons or large state-action spaces.
3. The introduction claims that the developed algorithm for RL with trajectory feedback achieves the same asymptotically optimal regret bound as the standard RL. The authors should explain why trajectory feedback does not lead to a worse regret bound and what properties of their algorithm allow them to overcome the information disadvantage of only receiving trajectory feedback. Specifically, the paper should elaborate on how the algorithm's design mitigates the increased variance in reward estimation due to trajectory-based feedback, and how this compares to standard RL methods that receive immediate rewards.
4. Section 3 should clarify that how the expected trajectory reward is a linear function of the state-action visitation frequencies. The current explanation lacks sufficient detail to be easily understood by a reader unfamiliar with this specific property. A more thorough explanation, including a step-by-step derivation, would be beneficial.
5. Some mathematical derivations are not intuitive. The authors can add explanations about what the mathematical properties mean and how they are derived. Here are some examples.
5.1 The second key observation on page 5. The explanation of how the state-action visitation frequency is derived from the probability of trajectories is not clear. A more detailed explanation of this relationship is needed.
5.2 Inequality (3). The connection between the confidence regions for linear bandits and the inequality is not clearly explained. The authors should provide more context on how this inequality is derived from the properties of linear bandit algorithms.
5.3 The equation in (8). The definition of W and its relationship to the expected cumulative reward should be clarified. The derivation of this equation should be explained in more detail, particularly how the state-action visitation frequencies are related to the expected reward.
6. There are a few typos: The third term of the upper bound in Theorem 7. P1 in Line 4 of Algorithm 2. D2 in Line 6 of Algorithm 2.

### Questions
1. In the upper bound of Theorem 7, the last three terms dominate. In contrast, the abstract and the introduction claim that the upper bound is determined by the first term. The authors should clarify under what conditions, if any, the first term dominates. If the first term is not asymptotically dominant, the authors should explain why they only focus on the first term in the abstract and the introduction.
2. The introduction claims that the developed algorithm for RL with trajectory feedback achieves the same asymptotically optimal regret bound as the standard RL. The authors should explain why trajectory feedback does not lead to a worse regret bound and what properties of their algorithm allow them to overcome the information disadvantage of only receiving trajectory feedback.

### Soundness
3

### Presentation
3

### Contribution
3

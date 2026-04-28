# Theoretical Hardness and Tractability of POMDPs in RL with Partial Online State Information

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 5, 6

## Abstract
Partially observable Markov decision processes (POMDPs) have been widely applied in various real-world applications. However, existing theoretical results have shown that learning in POMDPs is intractable in the worst case, where the main challenge lies in the lack of latent state information. A key fundamental question here is: how much online state information (OSI) is sufficient to achieve tractability? In this paper, we establish a lower bound that reveals a surprising hardness result: unless we have full OSI, we need an exponentially scaling sample complexity to obtain an $\epsilon$-optimal policy solution for POMDPs. Nonetheless, inspired by the insights in our lower-bound design, we identify important tractable subclasses of POMDPs, even with only partial OSI. In particular, for two subclasses of POMDPs with partial OSI, we provide new algorithms that are proved to be near-optimal by establishing new regret upper and lower bounds. Both our algorithm design and regret analysis involve non-trivial developments for joint OSI query and action control.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the theoretical hardness and tractability of partially observable Markov decision processes (POMDPs) when only partial online state information (OSI) is available. The setting is different from the standard POMDP case, and also different from the recent work on POMDP with hindsight state information. The authors also provide motivating exampling to justify the proposed framework.

The authors then establish a lower bound that shows the exponential scaling of sample complexity is required to find an optimal policy solution for POMDPs without full OSI in general. However, they also identify two tractable sub-classes of POMDPs with partial OS. New algorithms are also proposed to solve the identified classes.

### Strengths
1 POMDP is a useful framework of the interactive decision-making problems, but is also intractable in general. Therefore, identifying interesting tractable sub-class of POMDP with interesting and reasonable structures is an important problem in theoretical RL study. The topic itself is thus very relevant to the community of neurips. Meanwhile, the proposed framework introduces partial side information before the agent makes decision, which is natural in practice and supported by the practical applications, and also is a great complement to existing works.

2 I find that the story is complete: the authors start with the proposed frameworks and its motivating examples, and also the connections with existing frameworks; and then a pessimistic lower bound to motivate further structural assumptions; finally, two algorithms are proposed to solve the identified tractable problems.

3 The proposed algorithm 1 is distinct from the recent popular OMLE/MOPS algorithms, which are popular since GOLF and Bilin-ucb. Instead, the algorithms are more related to the classic algorithms that are crafted to exploit the observable operator structure, but with distinct new ideas to handle the partial side information. To the best my knowledge, the algorithmic designs and some of the analysis techniques are new.

Overall, I feel that the authors have presented a reasonable framework of tractable POMDP problems, with a complete story, thus hitting the bar of acceptance.

### Weaknesses
1 The authors mention that the proposed framework can be placed under the general decision-making framework studied in [1,2]. I am wondering whether the identified problems can also be proved to be a sub-class of the tractable problems identified in these works. For instance, do the two classes of problems admit a low dec?

2 I think it would be better if you could explicitly instantiate the motivating examples in section 2 with the proposed framework (e.g. explicitly write down the state mapping with the physical quantities). Also, some of the superscripts are missing in the main paper (e.g. in section 2.3). It is also suggested to provide a notation table for the readers to improve readability.

### Questions
see weakness

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on the benefits of online state information (OSI) in the learning of POMDPs. Previous work showed that full OSI in hindsight helps accelerate the exploration of unknown POMDPs. The main problem studied in the paper is whether partial OSI is beneficial for POMDPs, and to what extend are the benefits if the answer is yes. The partial OSI setting means the agent can actively query part of the state at each step. For the negative results, the paper shows that partial OSI cannot prevent exponential sample complexity in general by constructing a hard family of POMDPs. For positive results, it identifies two subclasses of partial OSI POMDPs that is tractable and provides sample efficient algorithms to learn the optimal policy with $\sqrt{K}$ regret ($K$ is the number of episodes).

### Strengths
1. The setting studied in the paper is common in some real-world problems. The paper also provides some motivating examples for the partial OSI model.

2. The techniques to develop the lower bound instances and the algorithmic design of pessimistic-optimistic exploration strategy for the query policy and execution policy are appreciated.

### Weaknesses
1. The paper's setting, while intriguing, appears to deviate from the core motivation for introducing OSI in POMDPs as established in prior work. Previous research often focuses on hindsight OSI, revealed after an action is taken, which is common in applications like data center scheduling. This paper, however, proposes a query model where the agent queries part of the state *before* taking action. While the motivating examples, such as autonomous driving, might seem to suggest a post-action revelation of the state, the proposed model operates differently. Although the paper's conclusions might still apply if the query occurred post-action, a more thorough discussion of a model aligned with real-world scenarios, particularly where state information is revealed after action, would be beneficial.

2. Certain claims and proofs within the paper lack sufficient clarity, potentially compromising the paper's overall soundness. Specifically, in the definition of tractable class 1, the transition kernel is described as factorable into the multiplication of  `d`  different sub-transitions, each corresponding to a sub-state. However, Algorithm 3 does not explicitly detail how these  `d`  sub-transitions are estimated. The algorithm's presentation suggests that the sub-transitions might be treated as identical for each  `i` in `[d]`, allowing estimation using all adjacent revealed sub-states within an episode, regardless of whether adjacent steps select the same sub-state dimension. This approach is not feasible if the sub-transition for each dimension is distinct, potentially impacting the final regret bound. Furthermore, the proof of Lemma 1 and Lemma 5 requires clarification regarding the expectation in Equations 40, 42, and 43. The current definition of the expectation seems ambiguous in the context of proving the regret bound. While I believe these issues can be addressed, and the conclusions might still hold, a thorough revision of the statements and proofs is strongly recommended to ensure the correctness of the paper's claims.

3. The tractable class 1 bears similarities to factored MDPs, where the transition and reward functions of a large MDP can be factored into several sub-transitions related to different parts of the state. Factored MDPs often exhibit optimal regret with a square root dependency on the size of the factored state and action spaces. A more detailed comparison between tractable class 1 and factored MDPs would enhance the paper's contribution.

### Questions
The tractable class 1 is similar to the factored MDPs, where the transition (and reward) of a large MDP can be factored into several subtransitions with regards to different part of the state. The optimal regret of factored MDPs only has square root dependency on the size of factored state space and action space. Can you provide some comparisons with tractable class 1 with factored MDPs?

Typo: 
Section 2.3 Line 3: $\Phi_h \to \hat{\Phi}_h$

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper delves into the realm of partially observable reinforcement learning. The authors initially establish that achieving a near-optimal policy solution for POMDPs necessitates an exponentially increasing sample complexity unless full online state information (OSI) is readily available. Moreover, the authors demonstrate that POMDPs with only partial OSI become tractable when certain additional assumptions are made, such as independent sub-states or the revealing assumption.

### Strengths
The domain of partially observable reinforcement learning holds significant interest for the RL theory community, with the identification of new tractable POMDPs being of paramount importance. This paper aims to present a comprehensive set of results for POMDPs with online state information.

### Weaknesses
### weaknesses:
 The domain of partially observable reinforcement learning holds significant interest for the RL theory community, with the identification of new tractable POMDPs being of paramount importance. This paper aims to present a comprehensive set of results for POMDPs with online state information.


 One of the principal issues with this paper is its writing quality, marred by numerous typographical errors that impede comprehension. Some concerns and questions are outlined in the questions part.


While I can grasp the main storyline and contributions of this work to some extent, its subpar writing hinders my ability to follow and validate its accuracy. Therefore, I firmly believe that this paper requires a comprehensive revision to enhance its clarity and coherence.


### questions:
 - The reward function $r_h$ remains independent of the episode index $k$," but the reward $r_h^k$ is frequently referenced (e.g., Figure 1, Section 2.1, Section 2.2...). This creates confusion. Are the authors referring to the reward function or the actual reward received at a specific episode and step? The notation should clearly distinguish between the two.

- In Section 2.3, it is unclear whether the authors intend to use $\hat{\Phi}_h$ or $\hat{\Phi}_h^k$." The notation should be consistent throughout the paper.

- Regarding the definition of $V^{\pi^k}$, the expectation is seemingly taken with respect to $\pi_q^k$ rather than $\pi_p^k$. The authors should also provide clarity that $\pi^k = (\pi_q^k, \pi_a^k)$. This needs to be explicitly stated and defined.

- The definition of regret raises questions. Why do the authors employ $Reg^{\pi}(K)$ instead of $Reg(K)?$ If the authors aim to emphasize the dependency on the executed policies, it should be expressed as $Reg^{\pi^{1:K}}(K).$ The current notation is ambiguous.

- The statement of Theorem 1 appears non-rigorous as it lacks a precise definition of "with only partial online state information." This term needs a formal mathematical definition to ensure the theorem's validity.

- The definition of $\mathbb{P}\_h^k$ in (3) is unclear. The counter $\mathcal{N}^k$ also seems to depend on $h.$ The definition of $\mathcal{N}^k(\phi_{\hat{i}}(s), a, \phi_{\hat{i}}(s'))$ should be provided; and the $\mathbb{P}\_h^k$ should be replaced by $\mathbb{P}\_h^k(\phi_{\hat{i}}(s') | \phi_{\hat{i}}(s), a)$? The notation and definitions in this section require significant clarification.


- The proposed algorithms appear to be a fusion of the strategic querying mechanism and existing methods, which include value iteration and OMLE. It's evident that the strategic querying mechanism stands out as the primary novelty in this work. However, the paper lacks a detailed and thorough elaboration of this mechanism. For instance, deferring the definition of $\hat{r}_h^k$ to the appendix without accompanying explanation seems to be a suboptimal choice, as it hinders a clear understanding of this critical component. Providing more clarity and detail on this novel approach would greatly enhance the paper's readability. The strategic querying mechanism needs to be explained in detail in the main body of the paper, including the rationale behind its design choices.


- Regarding Theorem 6: Why can't the cases of $\tilde{d} = 1$ and $\tilde{d} \ge 2$ be unified? Why is Theorem 6 unable to encompass the results for the case of $\tilde{d}=1$"? Perhaps presenting the general case for $\tilde{d}$ would better illustrate the contributions of this paper. A unified treatment of these cases, if possible, would strengthen the theoretical contribution.

- Another minor comment: it would be much more interesting if the lower bound in Theorem 4 depends on $\tilde{d}$. This would provide a more nuanced understanding of the problem's complexity.

There are a few issues I identified in the main paper. I hope the authors will thoroughly review the paper (including the Appendix) and make comprehensive revisions, aiming to make the paper easy to follow.

### Questions
- The reward function $r_h$ remains independent of the episode index $k$," but the reward $r_h^k$ is frequently referenced (e.g., Figure 1, Section 2.1, Section 2.2...).

- In Section 2.3, it is unclear whether the authors intend to use $\hat{\Phi}_h$ or $\hat{\Phi}_h^k$."

- Regarding the definition of $V^{\pi^k}$, the expectation is seemingly taken with respect to $\pi_q^k$ rather than $\pi_p^k$. The authors should also provide clarity that $\pi^k = (\pi_q^k, \pi_a^k)$.

- The definition of regret raises questions. Why do the authors employ $Reg^{\pi}(K)$ instead of $Reg(K)?$ If the authors aim to emphasize the dependency on the executed policies, it should be expressed as $Reg^{\pi^{1:K}}(K).$

- The statement of Theorem 1 appears non-rigorous as it lacks a precise definition of "with only partial online state information."

- The definition of $\mathbb{P}\_h^k$ in (3) is unclear. The counter $\mathcal{N}^k$ also seems to depend on $h.$ The definition of $\mathcal{N}^k(\phi_{\hat{i}}(s), a, \phi_{\hat{i}}(s'))$ should be provided;  and the $\mathbb{P}\_h^k$ should be replaced by $\mathbb{P}\_h^k(\phi_{\hat{i}}(s') | \phi_{\hat{i}}(s), a)$? 



- The proposed algorithms appear to be a fusion of the strategic querying mechanism and existing methods, which include value iteration and OMLE. It's evident that the strategic querying mechanism stands out as the primary novelty in this work. However, the paper lacks a detailed and thorough elaboration of this mechanism. For instance, deferring the definition of $\hat{r}_h^k$ to the appendix without accompanying explanation seems to be a suboptimal choice, as it hinders a clear understanding of this critical component. Providing more clarity and detail on this novel approach would greatly enhance the paper's readability.


- Regarding Theorem 6: Why can't the cases of $\tilde{d} = 1$ and $\tilde{d} \ge 2$ be unified? Why is Theorem 6 unable to encompass the results for the case of $\tilde{d}=1$"? Perhaps presenting the general case for $\tilde{d}$ would better illustrate the contributions of this paper.

- Another minor comment: it would be much more interesting if the lower bound in Theorem 4 depends on $\tilde{d}$.

There are a few issues I identified in the main paper. I hope the authors will thoroughly review the paper (including the Appendix) and make comprehensive revisions, aiming to make the paper easy to follow.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the partially observable reinforcement learning with certain feedback structure (partial online state information, POSI). Given that POSI is not sufficient for statistical learnability, the authors identify two learnable problem classes of interest with POSI and extra structural assumptions (independent sub-states / revealing condition) by establishing regret upper bounds and lower bounds.

### Strengths
- The hardness result for POSI (Theorem 1) uses a novel and interesting construction based on combinatorics lock. The clever construction demonstrates that partially observable RL is still hard even the agent can actively query (part of) the latent state information, which is itself a meaningful message.

- The motivation of considering class 1 & 2 is very clear, as the authors provide various empirical works where the structure of class 1 / 2 naturally arises.

- Algorithm 1 adopts a novel strategy for determining the substates to be queried based on exponential weight update, which seems promising.

### Weaknesses
The two problem classes are studied in a case-by-case manner (both algorithms and analysis are very different). It would be a natural question whether there is a connection between these two. Such a connection is important because it will provide a more unified understanding of partially observable RL with POSI. In this paper, there lacks an investigation (or at least a discussion) on this connection (either positive or negative).

For problem class 1, the structure of the optimal policy is not very clear. If my understanding is correct, the guarantee of algorithm 1 implicitly implies that there is an optimal policy that proceed as follows: for each step h, sample a substate i from a fixed distribution p, query i and take an action according to \phi_i(s_h). In my opinion, this result is non-trivial, and stating this result can help the reader better understand the motivation of Algorithm 1.

For theorem 3, the authors highlight that the upper bound is "decreases exponentially as $\tilde{d}$ increases". I am a little bit confused of this point, because there is a possibility that such a decreasing upper bound is an artifact of the algorithm design or the analysis. More concretely, it is possible that the minimax optimal regret actually scales with $|\tilde{\mathbb{S}}|^d$ (as the lower bound), which does not decrease as $\tilde{d}$ increases. There also lacks a discussion of the revealing condition $\alpha$ which only appears in the upper bound side, yet it is known that for revealing POMDP the minimax optimal regret actually scales with $\alpha^{-1}$.

### Questions
1. For problem class 1, the structure of the optimal policy is not very clear. If my understanding is correct, the guarantee of algorithm 1 implicitly implies that there is an optimal policy that proceed as follows: for each step h, sample a substate i from a fixed distribution p, query i and take an action according to \phi_i(s_h). In my opinion, this result is non-trivial, and stating this result can help the reader better understand the motivation of Algorithm 1.

2. For theorem 3, the authors highlight that the upper bound is "decreases exponentially as $\tilde{d}$ increases". I am a little bit confused of this point, because there is a possibility that such a decreasing upper bound is an artifact of the algorithm design or the analysis. More concretely, it is possible that the minimax optimal regret actually scales with $|\tilde{\mathbb{S}}|^d$ (as the lower bound), which does not decrease as $\tilde{d}$ increases. There also lacks a discussion of the revealing condition $\alpha$ which only appears in the upper bound side, yet it is known that for revealing POMDP the minimax optimal regret actually scales with $\alpha^{-1}$.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

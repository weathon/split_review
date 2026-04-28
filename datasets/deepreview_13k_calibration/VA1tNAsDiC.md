# Best Possible Q-Learning

- Decision: Reject
- Avg Score: 4.00
- Scores: 6, 6, 1, 3

## Abstract
Fully decentralized learning, where the global information, \textit{i.e.}, the actions of other agents, is inaccessible, is a fundamental challenge in cooperative multi-agent reinforcement learning. However, the convergence and optimality of most decentralized algorithms are not theoretically guaranteed, since the transition probabilities are non-stationary as all agents are updating policies simultaneously. To tackle this challenge, we propose \textit{best possible operator}, a novel decentralized operator, and prove that the policies of agents will converge to the optimal joint policy if each agent independently updates its individual state-action value by the operator. Further, to make the update more efficient and practical, we simplify the operator and prove that the convergence and optimality still hold with the simplified one. By instantiating the simplified operator, the derived fully decentralized algorithm, \textit{best possible Q-learning} (BQL), does not suffer from non-stationarity. Empirically, we show that BQL achieves remarkable improvement over baselines in a variety of cooperative multi-agent tasks. %Due to the convergence and optimality, we believe BQL will be a new paradigm for fully decentralized learning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper considers decentralized training decentralized play for multi-agent reinforcement learning. A fully decentralized learning is proposed based on a best possible operator proposed in this paper. Though this operator is computationally expensive, it leads to convergence despite the nonstationarity caused by other players. A simplified operator is also proposed and the convergence and optimality based on this simplified operator is also provided. Simulation results demonstrate the performance of the proposed algorithm.

### Strengths
1. The paper is quite novel and original since it proposed a novel operator to enable convergence despite the nonstationary environment caused by other players in a decentralized multi-agent and stochastic setting. 
2. The paper is very well written. The algorithm is explained clearly and the simulation results are easy to follow.
3. The results are significant since it addressed a long lasting open question on MARL.

### Weaknesses
1. It can be restrictive to assume there is only a unique optimal policy. How does the proposed algorithm perform when there are multiple optimal policies?

2. Can the authors provide explicit theorems and proofs for the convergence and optimality of BQL  for both the tabular case and the neural network case?

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies decentralized multi-agent Q-learning where every agents share the same state and observes only local action. Resolving non-stationary due to the joint-policy, it is difficult to establish convergence of to a joint optimal policy is an important problem in MARL. The authors propose a best-possible operator, which basically solves the joint opitmal Bellman equation for $i$-th agent:
$$   Q^i(s,a_i)=\max_{a_{-i}}\mathbb{E}_{s^{\prime}\sim P(\cdot\mid s,a_i,a_{-i} )}[r+\gamma Q^i(s,a_i)].$$
The authors solve the above equation in decentralized manner, and its extension to practical algorithm is studied.

### Strengths
1. The authors proposed a new decentralized algorithm that could give new insights into the community. Even though the proposed algorithm has limitations, finding a global joint optimal policy in a decentralized manner seems to be a contribution.

2. The overall experimental result seems positive. It shows better or comparable results to existing ones including MA2QL, I2Q, H-IQL, IQL.

### Weaknesses
1. The memory space to store $P(\cdot\mid s,a_i,a_{-i})$ requires at least $O(|\mathcal{A}_{-i}|)$ space, which scales exponentially at the order of each action space. This makes the algorithm difficult to scale as number of agents increase. If we use function approximation, or somewhat similar methods to reduce this problem, will the arguments of this paper be still valid? Furthermore, the paper does not discuss the practical memory implications of storing this probability distribution, especially in high-dimensional action spaces where even storing a single probability value might be costly, let alone the entire distribution. The authors should provide a more detailed analysis of the memory footprint and discuss potential mitigation strategies.

2. The search over all possible $\pi_{-i}(a_{-i},s)$ for every state $s$ and $i$ seems to be quite a burden. It at least requires $N \prod_i |\mathcal{A}_i|$, which scale exponentially due to the joint action space. Even though the authors proposed a version in (7) to reduce the search time, I do not think this gives a meaningful cut in the search time in theoretical sense. Can the authors provide theoretical advantage in terms of search time for the proposed method? The authors need to clarify the computational complexity of the optimization problem, especially with respect to the number of agents and the size of the action space. The proposed simplification in (7) needs a more rigorous justification in terms of its impact on the search space and the optimality of the solution.

3. A closely related work [1] deals with theoretical convergence of independent Q-learning. Please provide comparison with the work in sense that how the setting is different, and pros and cons.


4. The algorithm does not seem to be scalable.

### Questions
1. In Lemma 1, why do we need the condition of existence of only one optimal policy?

2. There is typo in the caption of Figure 3 : "Mojoco"->"Mujoco".

3.  In Section 2.4, $S^m_i$ has not been explained previously.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper presents a new take on decentralized Q-learning, in which each agent (independently) updates its value function by pretending that the other agents act optimally with respect to its current estimate of the value function. A simplification of this procedure is proposed which the authors show also leads to desirable convergence properties. Experiments contrast the proposed method with relevant baselines.

### Strengths
* The main idea of having each agent “imagine” a best-case scenario of what the other agents do is a very clean way to synchronize the independent Q-learning approach which could otherwise fail to converge. 
* For the most part, the proofs are logical and easy to follow. (See question below.)

### Weaknesses
 * Some syntax errors on line 70: no whitespace after “MDP” and also the <> symbols should probably be () for a tuple as is standard in the MDP literature.
* Many instances of grammatical issues, e.g. missing “the” in a sentence.
* The simplified operator seems like it will be egregiously inefficient, particularly in larger state/action spaces. Isn’t it effectively just random search? The description of the simplified operator lacks sufficient detail to understand its practical implications, especially in high-dimensional state and action spaces. The authors should provide a more thorough analysis of its computational complexity and how it scales with problem size. Furthermore, the connection between the simplified operator and random search needs to be clarified, as it's not immediately obvious how they are related.
* The sentence “but the converged equilibrium may not be the optimal one when there are multiple Nash equilibria” on line 322 only makes sense in (a) games where agents share a common objective — otherwise what is the measure of optimal — and (b) is not really a critique for non-convex games where methods would only at best be able to find local equilibria and there is no good way to find the “best” such equilibrium. Similar comment for the statement about Hysteretic IQL on line 325. The notion of optimality in multi-agent settings needs to be carefully defined, especially when agents have conflicting objectives. The critique of Nash equilibria and the comparison to Hysteretic IQL are not well-justified without a clear definition of optimality and a discussion of the limitations of finding global optima in non-convex games.
* “slow learning rate to the value punishment” on line 324 must be a typo of some kind
* “using mean and standard” on line 345 is a typo
* “action space of each agent is 4” -> another typo on line 351
* More details should be provided about the distribution from which transition kernels and reward functions are sampled (cf line 354). Depending on the variance of these distributions, using only 20 samples could easily give a very poor statistical estimate of performance. Since the standard deviations look fairly small (at least in Figure 1), I am guessing that these distributions are fairly well structured. It would be useful to understand that structure so as to better appreciate the testing scenario and results. The lack of detail regarding the sampling distributions for transition kernels and reward functions makes it difficult to assess the robustness of the results. The authors should provide a clear description of the distribution parameters and justify the use of only 20 samples, especially if the variance is high.
* “std” on line 356 should be spelled out
* I do not follow all the issues that are being discussed in the paragraph ending on line 374. This discussion should be substantially rewritten for clarity. The discussion surrounding line 374 is convoluted and lacks clear explanations. The authors should restructure this section to improve readability and ensure that the technical arguments are easily understood.
* “wildly adopted” -> typo on line 301. I presume it should be “widely” but if that is the case, why is there only one reference here?
* “MPE” is not defined anywhere as far as I can remember. Cf. line 341 and section 4.2. From the description in section 4.2, this is not actually a differential game since time is not a continuous variable. Cf. the standard texts by Rufus Isaacs and Tamer Basar & Geert Olsder. The proper term would be “dynamic game,” which includes discrete-time problems. The term “MPE” needs to be defined clearly, and the authors should clarify whether they are using the term “differential game” correctly. If the time variable is discrete, the term “dynamic game” would be more appropriate.
* “In continuous environments, BQL and baselines are built on DDPG.” (Line 428) -> this should be explained far more carefully so that readers can appreciate how this choice influences the results. The authors need to provide a more detailed explanation of how DDPG is used as the foundation for their method in continuous environments. The implications of this choice on the results should be discussed thoroughly, including any potential limitations or biases introduced by DDPG.
* In Figure 2, the results are not easily interpretable due to the color choices being so similar for the confidence intervals, and the intervals themselves being so wide for some methods. The color choices in Figure 2 make it difficult to distinguish between different methods, and the wide confidence intervals for some methods make it hard to draw meaningful conclusions. The authors should use more distinct colors and consider presenting the results in a way that reduces the visual clutter.
* All of the subfigure captions in Figures 3-5 are confusing. Without clear explanations of every single experiment, results are impossible to interpret and certainly cannot be trusted by a serious reader. 
    * Some of the descriptions of these subfigures in section 4.4 even make it sound like these are tasks where different agents have different objectives; clearly that does not conform to the present paper setting, so something is additionally confusing here. The subfigure captions in Figures 3-5 are unclear and lack sufficient detail to understand the experimental setup and results. The descriptions in section 4.4 further add to the confusion by suggesting that agents have different objectives, which contradicts the paper's premise. The authors should provide a clear and consistent description of each experiment and ensure that the figure captions accurately reflect the experimental setup.

### Questions
* Surely the claim of global optimality in line 62 is restricted to tabular cases, right? Such broad claims should be avoided (unless somehow they are true) in order to ensure the work is not misunderstood by a casual reader. Please clarify the setting in which this claim is valid.
* Why can’t we treat all agents as one “super agent” whose action space is the product space of the individual agents, and conclude that because (tabular) Q learning would converge for the “super agent,” it will also for the individual Q learners? If we did value iteration instead of Q learning would it work? An explanation here would probably not depend upon (non)stationarity arguments, I think. At the very least, the authors should provide a reference for the statement of non-convergence on line 87.
* I do not follow the step from line 142 to line 144. Is it generally true that max_x f(x) - max_x g(x) \ge f(x’) - g(x’) for a generic x’ (here, x’ is analogous to a_i^{‘*})? I can certainly find counterexamples in general, so what is special about this case which admits this inequality? Please explain what is going on here more carefully.
* I am not clear on why we need to “explore” all state/action pairs with a deterministic policy (looking at line 236). Can’t we just enumerate them in a tabular problem? Please explain why the exploration is needed and enumeration does not suffice.
    * This relates to the italicized sentence at the end of section 2.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper studies multi agent RL. A best possible operator is proposed to learn the optimal joint Q function. To address the computational cost, a simplied randomized operator is proposed. Algorithm based on it is further designed and extensive experiments are developed.

### Strengths
1. The problem of MARL is definitely important. This work provide a theoretical study on it with convergence guarantees.
2. I do appreciate the experiment part.

### Weaknesses
1. The observation of the global state can be a strong assumption.
2. The uniqueness of the joint optimal policy can also be strong. 
3. Since I am not familar with MARL, some statements/claims will benifit from more explanations. 
4. Some proofs are not convinced.

5. How is eq (4) obtained? Eq(3) holds when $a=(a_1^*,a_2^*,...,a^*_n)=\pi^*(s)$. Now if taking the maximum of other actions, will it require to fix $a_i=a^*_i$?
6. In the case of there exists onle one optimal policy, why is it deterministic? The Puterman's book is too large and more specific reference should be provided. It also seems to me that the Puterman's book is for single agent case mostly. 
7. In the proof of Lemma 4, the convergence is based on the fact that the optimal kernel is chosen during updating. What if the kernel is never choosen? 
8. When only deterministic policies are considered, the set of all possible kernels is finite, making Q3 a bit reasonable. But what if random policies are also considered?

9. The stochastic algorithm is claimed to have lower complexity than the best operator. However, the paper lacks a formal complexity analysis to support this claim. The analysis in Appendix B is neither rigorous nor convincing. It is possible that the total complexity is not actually improved compared to the best possible algorithm.
10. The scalability of the algorithm is unclear. Without a thorough complexity analysis, it is difficult to determine whether the algorithm can handle large-scale problems or if it is limited to small-scale ones. For instance, consider a single-agent RL problem: while comparing the performance of every deterministic policy one by one may work well for small-scale problems, it becomes prohibitively expensive for large-scale problems. Although the authors claim that the experiments indicate scalability, the results are limited to specific environments and do not conclusively demonstrate representativeness.
11. The paper is primarily focused on a simplified setting (only one optimal policy). The studies presented in Appendix D are neither comprehensive nor representative.
12. The convergence presented in the paper is asymptotic, based on the fact that improvement only occurs when the best kernel is selected. However, how likely is this to happen? When the state/action space is large, the probability of selecting the best kernel becomes smaller, potentially leading to significantly slower convergence rates. The lack of a quantitative characterization makes the impact of this result unclear. The asymptotic convergence is expected and such a result alone is not informative.
13. What is the total computational complexity of the simplified operator until it converge to the optimal policy? Intuitively, the average number of ineffective updates (i.e., when the best kernel is not selected) appears to match the total number of kernels. If this is the case, the computational cost is not reduced compared to the best possible operator (in expectation sense), making the claim of reduced cost unconvincing. A quantitative characterization would make these discussions much clearer.
14. The proof offers limited insights or novelty, and it provides little practical guidance (e.g., expected computational costs of the algorithm implementations).

### Questions
1. How is eq (4) obtained? Eq(3) holds when $a=(a_1^*,a_2^*,...,a^*_n)=\pi^*(s)$. Now if taking the maximum of other actions, will it require to fix $a_i=a^*_i$?
2. In the case of there exists onle one optimal policy, why is it deterministic? The Puterman's book is too large and more specific reference should be provided. It also seems to me that the Puterman's book is for single agent case mostly. 
3. In the proof of Lemma 4, the convergence is based on the fact that the optimal kernel is chosen during updating. What if the kernel is never choosen? 
4. When only deterministic policies are considered, the set of all possible kernels is finite, making Q3 a bit reasonable. But what if random policies are also considered?

### Soundness
2

### Presentation
2

### Contribution
2

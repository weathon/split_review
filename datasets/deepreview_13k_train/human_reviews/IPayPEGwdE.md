# Learning Good Interventions in Causal Contextual Bandits with Adaptive Context

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
We study a variant of causal contextual bandits where the context is stochastically dependent on an initial action chosen by the learner. This adaptive context setting allows the environment to elicit some initial choice from the learner before providing the context. Upon observing the context, the learner picks another action (an intervention in a causal graph) based on which they receive a reward. The objective is to identify near-optimal atomic causal interventions at the initial state and post context identification, to maximize reward. We extend prior work from the deterministic context setting to obtain simple regret minimization guarantees. This is achieved through an instance-dependent causal parameter, $\lambda$, which characterizes our upper bound. Furthermore, we prove that our simple regret is essentially tight for a large class of instances. A key feature of our work is that we use convex optimization to address the bandit exploration problem. We also conduct experiments to validate our theoretical results

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the causal contextual bandits, where the context depends on the learner's initial action. The goal is to select the actions (causal interventions) before and after observing the context that maximizes the reward. To achieve this, the authors propose an algorithm with better simple regret.

### Strengths
**The following are the key strengths of the paper:**
1. This paper studies how causal structure can improve contextual bandit algorithms where context depends on the initial action taken by the learner. This problem has real-life applications in areas like online advertisement (as mentioned in the paper).

2. The authors propose an algorithm (ConvExplore) for the problem considered in the paper and show that it enjoys better simple regret, and empirical results also verify the theoretical results.

### Weaknesses
 **The following are the key weaknesses of the paper:**
1. Restricting to binary interventions and rewards (i.e., either 0 or 1) makes the problem easier to solve but limits the practical applications to problems with only binary interventions and rewards.

2. The possible number of contexts can be very large (or even infinite), e.g., the number of users on the platform. Therefore, working with matrix P (where the number of columns is the same as the number of contexts) may be computationally challenging.

3. The proposed algorithm is horizon-dependent as it needs to know the total number of rounds, T, upfront. It is unclear if the proposed algorithm will work for problems where T is very small.

### Questions
Please address the above weaknesses. I have a few more questions/comments:
1. Page 1, last paragraph: what are the other variables in this statement, "they get to observe the values of multiple other variables in the causal graph."?

2. Is there any relationship between $\lambda$ and effective dimension if the problem is modeled as a sparse bandit problem?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a new method called ConvExplore(CE) to solve the Causal Contextual Bandits(CCBs). To be specific, it handle the CCBs with adaptive context settings, which uses an instance-dependent causal parameter \lambda to make adaptions to different contexts. Authors also provided solid proofs and regret bound of their new method and made experiments to validate their theoretical results.

### Strengths
1. Solid proofs of minimizing simple regret for causal bandits with adaptive context in an intervention efficient manner.
2. Upper and lower bound of the simple regret acheived by CE indicates that authors' method is almost the ideal solution for CCBs.

### Weaknesses
1.From the experimental results, it is observed that the choice of λ significantly influences the algorithm's performance comparison. Could authors provide the variation curve under larger λ values?

2.Moreover, how should λ be specifically adjusted, especially when dealing with entirely new contexts in a new scenario? Additionally, when λ is less than nk (e.g., λ=390), CE's performance is inferior to that of UE. How can this be explained?

3.There are too few experimental results, and is it possible to provide the source or generation rules of the experimental data? Although the theoretical aspects are solid, the experimental section needs further improvement, especially in terms of interpretability. The motivation given earlier pertains to a cold start scenario. Could authors provide further explanations for the experiments?

### Questions
See Questions in Weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies a variant of causal contextual bandits where the learner's initial action influences the context. The objective is to identify optimal interventions in the initial state and post-context identification. The study extends previous work from deterministic to stochastic contexts and offers a regret minimization guarantee using a parameter called λ. The research demonstrates that these guarantees are tight for a broad range of instances. Notably, the work employs convex optimization to address the bandit exploration problem and includes experimental validation of the theoretical results.

### Strengths
(1) The idea of using the convex minimization problem $\lambda$ is interesting.
(2) Provide both upper bound and lower bound for the proposed algorithm.

### Weaknesses
(1) Authors should compare the convex exploration with other exploration strategies, such as UCB-based or TS-based, instead of only uniform exploration. The current comparison to uniform exploration is insufficient to demonstrate the practical advantages of the proposed method. Specifically, the authors should clarify in which scenarios their method would outperform UCB or TS, and provide an analysis of the computational complexity of the convex optimization approach compared to UCB or TS.
(2) The authors didn't provide a comparison of their regret bound with other related works, given that there are plenty of causal bandit works. The lack of a theoretical comparison makes it difficult to assess the novelty and significance of the proposed regret bound. It is important to clearly state how the derived bound relates to existing bounds in the field, highlighting the specific improvements or differences. For example, do the assumptions leading to the bound differ, and if so, how?
(3) What is the upper bound or lower bound of $\lambda$? It is crucial to understand the range of this parameter for practical implementation and theoretical analysis. The authors should provide a clear explanation of how the bounds of $\lambda$ affect the performance of their algorithm. Furthermore, the practical implications of choosing different values of $\lambda$ should be discussed.
(4) The overall writing looks like finishing in a rush. The paper lacks clarity in some parts, making it difficult to follow the technical arguments. The authors should improve the writing quality, ensuring that all concepts and derivations are clearly explained and well-motivated.

### Questions
See weakness.

### Soundness
3 good

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
This paper considers a new type of causal bandit problem, where the decision maker makes two decisions, receives one context in between and a final reward. A motivating online advisement example is provided. An efficient exploration algorithm called ConvExplore is provided and its corresponding regret is shown, which serves as an upper bound for the proposed problem setting. In addition, a lower bound result is provided, which indicates that the proposed algorithm is tight up to log factors.

### Strengths
- The problem setting is new, which allows the context distribution (graph) to be stochastically depending on the initial action, e.g., user type selection. 
- The proposed algorithm is clear, which consists three subroutines: estimating transition probabilities, causal parameters and the corresponding rewards.

### Weaknesses
 - If I understood this paper correctly, all k contexts are not correlated. The contexts represent different users, and each user can have totally different causal graph and reward function. The proposed algorithm is learning the probabilities and reward functions independently among all contexts. In practice, the number of context could be very large, the proposed algorithm is not very practical as it requires a lot of explorations. Specifically, the algorithm learns transition probabilities and reward functions for each context independently, which means the sample complexity scales linearly with the number of contexts. This is a major limitation, especially if the contexts represent user demographics which can be numerous. The paper does not address how the algorithm would perform with a large number of contexts, which is a common scenario in real-world applications.
- The causal graph setting in this paper is not new and is very rudimental, i.e., the assumption of the graph for each context, which is similar to the original Lattimore 2016 paper and ignores many recent developments, e.g., Lu 2020, 2021, Adaptively Exploiting d-Separators with Causal Bandits 2022. The causal structure assumed is a simple chain, which is a very restrictive assumption. More recent works have considered more complex causal graphs, including those with confounding variables and d-separation criteria. The paper does not justify why such a simple causal structure is sufficient for the problem setting, especially given the existence of more sophisticated models in the literature.

### Questions
- Is it possible to share some knowledge between different context graphs and/or reward functions? Is it possible to define the contexts as different user groups that share similar behaviors in terms of features and rewards? 
- The word context is bit confusing here, especially in Figure 2, the context in contextual bandits and in this paper's setting are quite different. 
- In terms of the analysis, how different is it compared to Subramanian 2022 work, e.g., can you explain why the stochastic transition to the contexts will make the analysis in the paper much more challenging?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

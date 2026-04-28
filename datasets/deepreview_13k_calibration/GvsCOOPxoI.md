# Provable Learning for DEC-POMDPs: Factored Models and Memoryless Agents

- Decision: Reject
- Avg Score: 6.17
- Scores: 5, 5, 8, 8, 5, 6

## Abstract
This paper studies cooperative Multi-Agent Reinforcement Learning (MARL) under the mathematical model of Decentralized Partially Observable Markov Decision Process (DEC-POMDP). Despite the empirical success of cooperative MARL, its theoretical foundation, particularly in the realm of provable learning of DEC-POMDPs, remains limited.  In this paper, we first present a hardness result in theory demonstrating that, without additional structural assumptions, learning DEC-POMDPs requires several samples that grows exponentially with the number of agents in the worst case, which is also known as the curse of multiagency. This motivates us to explore important subclasses of DEC-POMDPs for which efficient solutions can be found. Specifically, we propose new algorithms and establish sample-efficiency guarantees that break the curse of multiagency, for finding both local and global optima in two important scenarios: (1) when agents employ memoryless policies, selecting actions based solely on their current observations; and (2) when a factored structure is present, which enables key properties similar to value decomposition in VDN or Qmix.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper studies how to learn to solve decentralized partially observable Markov decision processes (DEC-POMDP). It shows that the sample complexity for arbitrary problems is exponential in the number of agents.

To make the problem more tractable, the paper considers two different assumptions: first, a factorization of the transition function and the observation function, and second, a class of memoryless policies.

Finally, the paper provides a MARL algorithm for each assumption and analyzes the learning regret of each.

### Strengths
- Clear theoretical claims.
- The paper does an excellent work interleaving the main core results and intuition about them.

### Weaknesses
 - **There are no proofs in the main document.** The paper delegates all the proofs to the supplemental material. However, I was not able to read the supplemental material. Therefore, as this paper's main contribution is theoretical, this review must be taken with care.
- **Narrow class of problems.** Although the paper provides an example of the methodology's application to a POMDP with Knapsack constraints, it does not discuss which types of multi-agent problems the assumptions made would be applicable. Specifically, the assumption of factored transitions and observations, where each agent's transition and observation depend only on a limited set of other agents' actions, is quite restrictive. Many real-world multi-agent systems exhibit more complex dependencies, where an agent's state might be influenced by the states or observations of a larger set of agents, or even by global state information. The paper does not address how the proposed approach would perform in such scenarios, limiting its practical applicability.
- **Lack of empirical evidence.** The paper provides no empirical support to validate the proposed algorithm. The absence of experiments makes it difficult to assess the practical performance of the proposed algorithms and to understand how well the theoretical guarantees translate to real-world scenarios. It is unclear how the algorithm would behave in noisy environments or with complex reward functions, which are common in practical applications.

### Questions
1. Could you clarify how the notion of regret fits the centralized training with decentralized execution described in the introduction? 
2. Some prior work considers a similar assumption on the max in-degree $d$ of the factored MDPs [1,2]. Does it have a similarity with this approach? Would it be possible to make a similar analysis by making such assumptions [3]?
3. Is there a reason to assume that the components of the factored transition function depend only on the actions of the other agents and not their local states?


[1] Diuk, C., Li, L., and Leffler, B. R. (2009). The adaptive *k*-meteorologists problem and its application to structure learning and feature selection in reinforcement learning. *ICML*, 249–256. <https://doi.org/10.1145/1553374.1553406>
[2 ] Strehl, A. L., Diuk, C., and Littman, M. L. (2007). Efficient structure learning in factored-state MDPs. *AAAI*, 645–650. <http://www.aaai.org/Library/AAAI/2007/aaai07-102.php>
[3] Chakraborty, D., and Stone, P. (2011). Structure learning in ergodic factored MDPs without knowledge of the transition function’s in-degree. *ICML*, 737–744. <https://icml.cc/Conferences/2011/papers/418_icmlpaper.pdf>

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper studies how to develop provable sample-efficient algorithm for RL in Dec-POMDPs without suffering from the curse of multi-agency.

### Strengths
The strength is that the paper is studying an interesting question that is untouched by existing literature by identifying some interesting findings on certain assumptions or structures that can lead to sample efficient RL algorithm without exponential dependency on $n$.

### Weaknesses
 The main weakness of the paper lies in that 1) some assumptions are fully justified. For example, the memory-less policy is supported by two papers of Kara and Yuksel. However, the two papers actually studies finite-memory-based policy of length, sat $L$. I believe memory-less settings are much more restrictive settings. Another example is the form of the reward functions, which seems to be designed to facilitate the theory analysis. 2) The results on the factored model are a bit incremental, which is an extension of the studies on factored MDP/MG with recently identified weakly-revealing assumption.

### Questions
see the weakness

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents learning algorithms for decentralized partially observable Markov decision processes (DEC-POMDPs) with theoretical guarantees. Starting with a hardness result for general DEC-POMDPs, the authors argue that achieving sample efficiency in this broad setting is challenging. Therefore, they focus on two specific cases: (1) factored models, where the state space decomposes into individual components, and (2) memoryless policies based solely on current observations. Within these frameworks, the authors propose various sample-efficient algorithms that leverage the structural assumptions to achieve global or local optimality, with a detailed analysis of sample efficiency.

### Strengths
The paper is well-written, and the proposed algorithms appear novel, particularly within the DEC-POMDP setting. The theoretical analysis supporting the algorithms is thorough, with rigorous arguments on sample efficiency and optimality.

### Weaknesses
The work appears to only partially achieve the stated goals. Although I understand that assumptions are necessary to ensure sample efficiency, the choice of these two structures (factored models and memoryless policies) as primary focuses lacks clear justification. In particular, the paper does not adequately address why these specific structures are more relevant or widely applicable than other common DEC-POMDP formulations. For example, the paper does not discuss the limitations of memoryless policies in scenarios requiring temporal dependencies or how the factored state space assumption might restrict the model's ability to capture complex inter-agent dynamics. In addition, other DEC-POMDP frameworks exist (e.g., models where the reward depends on system states or state-action pairs). It would strengthen the paper by discussing how the proposed algorithms and sample-efficiency results might generalize or adapt to such alternative models. The current presentation leaves the reader questioning the broader applicability of the results.

The authors connect local optimality with Nash equilibrium, but this connection seems unconventional. Typically, Nash equilibrium implies that no individual agent can improve their reward by unilaterally altering their strategy. However, the paper’s definition of local optimality appears to rely on a value function representing the overall reward of all agents. This discrepancy needs further clarification, as it is not immediately clear how the paper's definition of local optimality aligns with the standard understanding of Nash equilibrium in multi-agent systems. The paper should provide a more detailed explanation of how the proposed local optimality concept relates to established game-theoretic concepts.

Sample complexity is generally interpreted as the number of steps required to reduce regret or cost. Could the authors clarify the connection between Theorem 3.1’s result and sample complexity? Additionally, how does Theorem 4.1 demonstrate improved sample efficiency? The paper does not clearly articulate how the sample complexity results are derived from the regret bounds, nor does it provide a clear explanation of how the local optimality algorithm achieves better sample efficiency compared to the global optimality algorithm. A more detailed explanation of the relationship between regret, sample complexity, and the specific results of Theorems 3.1 and 4.1 is necessary. Furthermore, the paper lacks a clear comparison of the sample complexity results with existing literature on decentralized POMDPs.

Minor point: I couldn’t locate the proof for Theorem 3.1.

Minor point: Is the “an” notation in Definition 4.2 intended to refer to “pa” in Definition 4.1? Please clarify for consistency.

### Questions
1) See above, how general are the factored and memoryless policy structures discussed in the paper? Are they widely applicable to DEC-POMDPs, or is their utility restricted to specific subclasses?
2) The authors connect local optimality with Nash equilibrium, but this connection seems unconventional. Typically, Nash equilibrium implies that no individual agent can improve their reward by unilaterally altering their strategy. However, the paper’s definition of local optimality appears to rely on a value function representing the overall reward of all agents.
3) Sample complexity is generally interpreted as the number of steps required to reduce regret or cost. Could the authors clarify the connection between Theorem 3.1’s result and sample complexity? Additionally, how does Theorem 4.1 demonstrate improved sample efficiency?
4) Some multi-agent reinforcement learning studies address the exponential action space growth using mean-field control techniques. It might benefit the paper to discuss these works. 
5) Minor point: I couldn’t locate the proof for Theorem 3.1.
6) Minor point: Is the “an” notation in Definition 4.2 intended to refer to “pa” in Definition 4.1? Please clarify for consistency.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this paper, the authors consider decentralized multi-agent reinforcement learning in a partially observable setting (i.e., RL for DEC-POMDPs). They consider two different settings based on different simplifying assumptions: 1) the dynamics can be factored such that any agent's dynamics only (directly) depend on a subset of all the other agents, and 2) the agents have no memory. For both settings, the authors define a variation of 'Optimistic Maximum Likelihood Estimation' (OMLE), an RL algorithm for standard POMDPs. The authors prove these algorithms yield better regret bounds than is possible for general DEC-POMDPs. More precisely, for the factored setting, the regret of their algorithms scale exponentially with the maximum number of agents that influence a single agent (instead of the total number of agents), while for the memoryless setting, they show an $\epsilon$-optimal policy can be found in a polynomial number of samples.

### Strengths
* The paper discussed an interesting and relevant topic. Dealing with partial observability is a key problem for applying (MA)RL in the real world.
* Much existing MARL research is application-focused. This paper instead takes a more theoretical approach, which makes it more novel.
* The paper is well written: the problem settings are well explained and the authors provide both pseudocode and an intuitive explanation of their algorithms. As someone who is not an expert on MARL, I found the paper relatively easy to follow.

### Weaknesses
 * The properties of a factored structure model are, in my opinion, not sufficiently explained. In particular, the factorization (Sec. 4.1) requires that the transition function for a single agent depends only on the *actions* of a set of other agents. In other words, there can be no dependency between the *states* of different agents. This should be explicitly mentioned in the text. Furthermore, the current description does not make it clear how the local state of an agent is updated, given that the transition function only takes actions as input. It is unclear if the local state is updated deterministically or stochastically, and how this update is related to the global state transition.
* Both the assumptions of a factored structure model and memoryless agents are strong and limit real-life applicability. However, I think it is justified to make such assumptions in a theoretical paper.
* The proofs in the paper are long (~25 pages) and dense. The authors give some intuition on how exponential dependencies are avoided, but it is hard to verify the results in more detail. However, I am not sure if the authors can realistically improve this.

### Questions
* You do not give a proof or citation for Thm. 3.1: where does this come from? Can you give any intuition as to why it holds?
* I am a bit confused by your application model (Sec. 4.4): could you explain it in more detail? In particular, I have the following question:
	* You note in App. E1 that episodes terminate after any agent exceeds its budget. It seems like this implies all agents can affect each other (i.e., by terminating the episode), and thus, your model cannot be factored. Can you explain why this is not the case?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper deals with synthesis of decentralized multi-agent policies in a POMDP framework through reinforcement learning. It observes that while multi-agent RL policies have empirically met with success, their theoretical performance bounds -- and the limits of their performance -- are largely unknown. To tackle this challenge, the paper proposes a series of results on sample complexity of policy synthesis, showing that, while it is generally provably burdensome to determine an optimal policy, doing so might be possible in particular subclasses of policies and/or environments.

### Strengths
The paper deals with an important topic -- planning for DEC-POMDPs -- and treats it refreshingly formally. It includes theoretical hardness bounds on sample complexity, a treatment of algorithms for global and local optimality, and a mention of a very important and interesting application. The paper truly appears to be a tour de force in the multi-agent planning community.

### Weaknesses
In short, I believe this is a wonderful paper, but inappropriate in size for ICLR. In a traditional understanding of the paper format, a paper should be largely self-contained without recourse to any supplementary material like an appendix. Indeed, along these lines, the ICLR guidelines state "reviewers are not required to read the appendix". However, in this case the appendix is 3 times longer than the paper: the paper itself is mostly just a list of results where there is no indication of how they are proven and the only example which could possibly illustrate the derived technical work appears in a total of two paragraphs.

I find it impossible to truly evaluate this paper without treating the appendix exactly as the "main" paper, but if that needs to be done, then the paper (which is actually 48 pages long) is simply attempting to "game" the strict page limit. Again, I strongly, strongly support the publication of this paper, just not in this venue.

### Questions
I have no questions. I find the paper theoretically valuable and very relevant to the scope of ICLR, but not appropriate for publication due to its format.

### Soundness
4

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
2

### Summary
The paper addresses the challenge of achieving sample efficiency in decentralized partially observable Markov decision processes (DEC-POMDPs). By proposing algorithms under a factored structure model and memoryless policies, the authors break the curse of dimensionality for certain scenarios.

### Strengths
The paper addresses the challenge of achieving sample efficiency in decentralized partially observable Markov decision processes (DEC-POMDPs). By proposing algorithms under a factored structure model and memoryless policies, the authors break the curse of dimensionality for certain scenarios.

### Weaknesses
1. The analysis for memoryless policies lacks applicability to DEC-POMDPs where agents require memory, making the solution scope somewhat narrow for environments needing historical data for decision-making. Suggesting possible extensions to the analysis for environments where agents rely on historical data for effective decision-making would broaden the solution's applicability.

2. Certain technical assumptions, like weakly revealing conditions, are critical to the sample efficiency claims but are not sufficiently discussed in terms of real-world feasibility. It would be helpful if the authors could provide additional discussion on the real-world feasibility of the weakly revealing condition.

### Questions
1. How does the proposed algorithm address potential scalability issues as the number of agents and their interaction complexity increase within the factored structure model?
2. How does the algorithm handle partial observability when the weakly revealing condition does not hold? Would additional assumptions be required to maintain sample efficiency?
3. In scenarios where agents use memory-based policies, what adaptations would be necessary to extend the sample-efficiency guarantees presented here?
4. Can the authors provide a comparative analysis of their approach against recent advances that incorporate centralized training with decentralized execution in DEC-POMDPs?

### Soundness
3

### Presentation
3

### Contribution
3

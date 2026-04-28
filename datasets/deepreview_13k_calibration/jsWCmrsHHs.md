# Deep Reinforcement Learning Guided Improvement Heuristic for Job Shop Scheduling

- Decision: Accept
- Avg Score: 7.50
- Scores: 6, 8, 8, 8

## Abstract
Recent studies in using deep reinforcement learning (DRL) to solve Job-shop scheduling problems (JSSP) focus on \emph{construction} heuristics. However, their performance is still far from optimality, mainly because the underlying graph representation scheme is unsuitable for modelling partial solutions at each construction step. This paper proposes a novel \colorr{DRL-guided} \emph{improvement} heuristic for solving JSSP, where graph representation is employed to encode complete solutions. We design a \colorr{Graph-Neural-Network-based} representation scheme, consisting of two modules to effectively capture the information of dynamic topology and different types of nodes in graphs encountered during the improvement process. To speed up solution evaluation during improvement, we present a novel message-passing mechanism that can evaluate multiple solutions simultaneously. \colorr{We prove that the computational complexity of our method scales linearly with problem size}. Experiments on classic benchmarks show that the improvement policy learned by our method outperforms state-of-the-art DRL-based methods by a large margin.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This articled studied the problem of solving Job-shop scheduling problems using deep reinforcement learning focusing on heuristics. The authors have proposed a novel deep reinforcement learning based improvement heuristics where the graph representations are employed to encode complete solutions.

### Strengths
Good and decent review of literature based introduction gives a good readability.
Clear articulation of the MDP process with an example of state transition
Comparative study with Tabu Search algorithm for solving the instance 
The computation complexity of the proposed method is linear with respect to the number of jobs and number of machines.

### Weaknesses
There are many studies that job shop scheduling that has been modeled as a MDP but very few citations are present in the article.



### Questions
how does the transition state in MDP (section 4.1) is calculated? need to explore in detail on how the transition space is updated with the current status information of all jobs and machines.
why the reward function goal is to improve the initial solutions? isn't closely correspond to scheduling goal?
How does the generalization capability of the agents are addressed in this article? 
One way is to introduce order swapping mechanism with an instance and evaluate with another instance of the same size.
OpenAI Gym toolkit and associated kits provide reinforcement learning environment API - any exploration on this would have yielded results that could also be validated

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a local search method based on deep reinforcement learning (RL) for the job shop scheduling problem. The authors propose to encode solutions as disjunctive graphs and design a novel graph neural network architecture to process them. In addition, they propose an efficient technique to compute the schedule of a solution on GPU.

### Strengths
A novel graph neural network architecture is proposed to process the different type of information encoded in a disjunctive graph: graph topology, operation order in the solution, and operation order on a machine.

An efficient method to compute the schedules of batch of solutions is proposed, which can accelerate training deep RL training.

The authors performed a broad series of experiments on various instances comparing their proposed method with other deep RL algorithms, some basic heuristic methods, but also a meta-heuristic method (tabu search).

### Weaknesses
The presentation is generally clear. However, some parts could be improved.

I believe that some notions could be explained in a better way. For instance:
- page 1: "given that the topological relationships could be more naturally modeled among operations" is not clear to me.
- page 3: the notion of N5 neighborhood could be more explained more formally (instead of the current text and the example).
- Some sentences/expressions are unclear (see Questions).

Section 4.2.1: The first two sentences seem to contradict themselves.
What is meant by "machine predecessor" becomes only clear later on.

Minor:
page 7: a closing curly brace is missing for c_V.

### Questions
In the n-step REINFORCE, how is the return R_{t-j}^b computed? If it's over n steps, it means the RL agent basically ignores future rewards after n steps. In a general RL problem, this may lead to bad performance, but I guess for a local search method like in this paper, this may not be important. Could you comment on that point?

What did you choose to compare with Tabu search? 
What are the state-of-the-art methods for the job shop scheduling problem? How does the proposed method compared to them?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work addresses the job shop scheduling problem (JSSP), a classic combinatorial optimization task. It proposes a solution based on deep reinforcement learning to learn improvement heuristics, which iteratively refines an existing solution. The authors leverage a disjoint graph representation of the state (which is more complete than that employed in prior works), and propose a GNN architecture for its representation. The proposed MDP formulation chooses a pair of operations to be swapped, and the RL model is trained via the policy gradient. An experimental evaluation is presented, which compares the method with a large set of prior approaches, spanning deep RL, metaheuristic, and exact methods. The evaluation shows favorable results in comparison with these baselines.

### Strengths
**S1**. The paper addresses a highly practical problem that has received comparatively less attention (e.g., compared with routing problems) in the combinatorial optimization literature. The proposed method is fairly original, and is similar in spirit with other learned improvement heuristics.

**S2**. The evaluation performed by the authors is very comprehensive (in terms of datasets, instance sizes, baselines, and scenarios). Most importantly, it shows that the method attains excellent performance while requiring a reasonable time budget. It is one of the few cases where opting for the ML model over a classic solver or metaheuristic may actually be preferable in practice.

### Weaknesses
 **W1**. The only issues that I have identified relate to the clarity of the presentation of the problem formulation and solution method. More specifically:

- The problem formulation uses two different semantics for the $ji$ notation ($O_{ji}$ and $m_{ji}$). A different subscript is needed to indicate the machine, and it should be reflected in the figures as well. For example, using $m_{k}$ to denote the machine for operation $O_{ji}$ would be clearer, and this should be consistent in both text and figures. The current notation makes it difficult to track which machine is associated with which operation, especially when considering the disjunctive graph.
- I was not able to fully understand the transitions induced by the swapping of the two operations, given that it appears to trigger other reconfigurations of the disjunctive graph beyond the two vertices indicated by the action (e.g., the changes to the edges connecting the red machine in Figure 2b). The description of the state transition is not sufficiently detailed. It is unclear how the algorithm determines which edges to remove and add when swapping operations. For instance, if we swap two operations on a machine, how are the new precedence constraints on that machine enforced, and how are the edges in the disjunctive graph updated to reflect this change? A more precise description of the transition function, including the edge update rules, is needed in Section 4.1.

### Questions
**C1**. There are some typos / informal language / awkward word choices in the manuscript, and it would benefit from further revisions until publication. Some examples: 

- "receives relatively less attention" -> received / has received (p1)
- "In specific" -> specifically (p1)
- "A delicate Markov decision process formulation" (p2)
- "graph-based ones aforementioned" -> aforementioned graph-based ones
- "Precedent constraints" -> precedence constraints (p3)
- "To fast calculate" -> to quickly calculate (p3)
- "till" -> until (p4)

**C2**. The results in Appendix H / Table 4 appear very positive and show good generalization performance and scalability. I think it is worth making room for them in the main text.

**C3**. "Parameter $\theta$" -> Parameter *set* $\theta$ in 4.2?

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a novel, learning-based improvement heuristic for the job shop scheduling problem. It uses a novel graph neural network  to select operations that modify a solution from a set of candidate operations defined by the N5 neighborhood structure. The novel network architecture consists of a topology embedding module and a context-aware embedding module that are designed to encode the problem instances and their solutions. The authors prove that their method scales linearly with the problem size. Furthermore, they evaluate their method on a variety of instances from the literature and compare it to state-of-the-art ML methods, simple handcrafted heuristics, and a tabu search using the same neighborhood structure. Overall, the proposed method shows good performance outperforming existing ML methods in most settings.

### Strengths
- The proposed method introduces several novel concepts. In contrast, to many other approaches it is an improvement heuristic (instead of a construction heuristic). The novel network architecture is specifically designed to encode existing solutions and consists of two components that both are independently evaluated in an ablation study and seem to be well suited for the task. Furthermore, the REINFORCE algorithm has been slightly adapted for the task at hand.
- The method scales linearly with the problem size. In contrast, to many other machine learning based approaches the proposed method can thus scale to larger problem instances. 
- The proposed method outperforms other state-of-the-art learning-based approaches for the job shop scheduling problem.
- Overall, the paper is well written.
- The authors conduct ablation studies that evaluate individual components of the method.

### Weaknesses
 - The method uses the handcrafted N5 neighborhood to generate candidate operations (i.e., the set of possible actions for the model). This means that the method relies on a handcrafted component specific to the job shop scheduling problem. It is thus unclear how easily the method can be modified to solve other scheduling problems. Despite being based on a handcrafted heuristics it does not outperform the handcrafted tabu search using the same neighborhood structure in all settings.
- The authors only evaluate their method on the job shop scheduling problem and not on any other scheduling problems. This lack of evaluation on other scheduling problems limits the generalizability of the findings and makes it difficult to assess the broader applicability of the proposed approach. Specifically, it is unclear if the learned policy is robust to changes in problem structure or constraints that are common in other scheduling problems, such as resource constraints or sequence-dependent setup times.

### Questions
- Have you experimented with different ways to calculate the reward? For your current method, the network might receive different rewards when picking the same actions at the same state depending on what solutions were found in previous states. While I understand the motivation of your current choice, I wonder if this might impact learning.
- Have you tried to use a baseline during learning for REINFORCE?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

# MetroGNN: Metro Network Expansion with Deep Reinforcement Learning

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 6, 5, 6

## Abstract
Selecting urban regions for metro network expansion to meet maximal transportation demands is crucial for urban development, while computationally challenging to solve.
The expansion process relies not only on complicated features like urban demographics and origin-destination (OD) flow but is also constrained by the existing metro network and urban geography. 
In this paper, we introduce a reinforcement learning framework to address a Markov decision process within an urban heterogeneous multi-graph.
Our approach employs an attentive policy network that intelligently selects nodes based on information captured by a graph neural network.
Experiments on real-world urban data demonstrate that our proposed methodology substantially improve the satisfied transportation demands by over 30\% when compared with state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Selecting urban regions for traffic route construction to maximize origin-destination flow is a hard optimization problem because the solution space grows exponentially on the number of nodes. This paper models this problem as a MDP and applies reinforcement learning (RL) algorithms to search for a good solution.  This paper uses a graph neural network to learn the state representation and use action masks to rule out unavailable actions. The empirical results show this method increases the total origin-destination flow by 30% compared with state-of-the-art methods.

### Strengths
1. This paper builds an end-to-end reinforcement learning algorithm to find a good solution in a combinatorial optimization problem - traffic routes construction. To learn this solution efficiently, this paper builds a graph neural network to learn the state representation.

2. Its empirical results show this method increases the total origin-destination flow by 30% compared with state-of-the-art methods.

### Weaknesses
1. My major concern is that this paper does not have enough novelty to be published in a top machine learning venue. Indeed, selecting urban regions for traffic route construction to maximize origin-destination flow is a hard optimization problem because the solution space grows exponentially on the number of nodes. However, reinforcement learning (RL) has been known to be a useful tool for searching solutions in a large solution space since 1996 [1].

2. Moreover, using graph neural networks to learn state representation is also not a novel technique. The network proposed in this paper is not well-justified to have sufficient novelty. The specific architecture and the justification for its design choices are not clearly elaborated, making it difficult to assess its unique contribution beyond standard GNN applications.

3. Using action masks to eliminate infeasible regions is also a common approach in RL applications. The paper does not discuss how the action mask is constructed and whether the mask is dynamic, which could be a critical detail for the effectiveness of the method.

4. Other than insufficient novelty in the algorithm, the model built by this paper is also preliminary. For example, it is natural to consider that more regions could emerge as the city is expanding. The model in this paper is obviously not a high-fidelity model that could be used in real construction. The paper does not address the limitations of the model in dynamic environments or how the model would adapt to new regions and changes in the underlying graph structure.

5. This paper is not well-written. The details of the model and algorithms are not defined in a clear and mathematical way. The presentation and coherence of this paper could be greatly improved by deleting excessive words and sentences.

### Questions
N/A

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a graph-based Reinforcement Learning (RL) framework to solve the metro network expansion task (a geometrical combinatorial optimization problem) for maximizing overall OD flow satisfaction with several constraints, e.g., total budget, spacing between stations, and line straightness. The proposed framework, MetroGNN, incorporates Graph Neural Networks (GNN) and an attentive policy network with an action mask to learn representations for urban regions and select new metro stations. The experiments conducted on real-world urban data of Beijing and Changsha demonstrate that the proposed MetroGNN can improve OD flow satisfaction by over 30% against the state-of-the-art RL-based approach.

### Strengths
1. This paper proposes to solve a complex metro network expansion problem by using a graph-based reinforcement learning framework. The problem is significant, and the solution makes sense to me. 
2. The proposed approach is evaluated on two real-world urban datasets collected from two Chinese metropolises, Beijing and Changsha, which demonstrates its effectiveness in improving the overall OD flow satisfaction.
3. This paper is overall well-written and easy to follow. The illustrations are clear and helpful to understand this paper.

### Weaknesses
1. The technical contributions of this work are limited. While the metro network expansion task is essentially a transportation network combinatorial optimization problem, there have been many existing works [1] studying how to apply RL combined with GNN or attention to address it. It seems the authors only introduce some of the same or similar methods to a specific combinatorial optimization problem. However, there are no substantial technical innovations.
2. While this work investigates a realistic metro network expansion problem, it only aims to optimize the total satisfied OD flow. However, many other factors need to be considered and optimized to construct a realistic metro network, e.g., social equity or fairness, environmental impact, and revenues. It’s hard to evaluate whether the proposed method is applicable in real scenarios.
3. Some important experimental setups are not mentioned or clearly described. For example, the statistics and analysis of datasets. The implementation and hyper-parameter details of baselines. Such information is very significant for the evaluation of experimental reliability.

### Questions
1. The collected real OD flow data are based on the realistic transportation network. If the metro networks have be changed, how can the authors obtain the corresponding OD flow?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work addresses the metro network expansion problem, in which the goal is to decide which edges to add to a metro graph such as to optimize the total satisfied flow between origin-destination pairs in the network, subject to a budget constraint. The authors approach this problem by formulating it as a Markov Decision Process and proposing a reinforcement learning method that uses graph neural networks for encoding state information. More specifically, the authors consider two types of features in the GNN design: spatial features and flows, which are concatenated. The authors compare the proposed method with a variety of classic optimization algorithms and a recent RL approach, showing gains in optimality over these methods.

### Strengths
Originality: the work applies a method based on RL and GNNs to a new problem.  This intersection, by now, has a growing body of literature and is a fairly common "recipe".  It is moderately original in the design of its approach. 

Quality: the quality of the paper is reasonable, but I have substantial concerns about the soundness of the evaluation as well as its lack of clarity in places.

Clarity: the organization of the paper is clear. The writing is of reasonable quality. The main issue in terms of clarity is the lack of precision in the description of the problem / solution method.

Significance: the work is of interest to the ICLR community, and belongs to the growing machine learning for combinatorial optimization literature.

### Weaknesses
 **W1**. A major weakness is the fact that the authors do not report aggregated results across several runs together with statistical confidence measures (e.g. error bars). These should be presented for all figures and tables in order to account for the stochasticity of model training. Otherwise, a possible alternative explanation for the observed results is that one of the "lucky" seeds was used, which yields better performance than what we might see in the average case. It is not possible, in my opinion, to draw reliable conclusions from the presented results. In case multiple runs were indeed carried out, these details should be reported.

**W2**. Lack of (mathematical) precision in the description of the problem and solution method. The authors should aim for a level of clarity that would enable someone to reproduce the results starting from the descriptions only. This is currently not the case. Some examples where this is apparent:

- Most importantly, the MDP components (currently in Appendix A) should be formalised mathematically and not described only in plain English. 
- Equation 1: presumably $i \neq j$, given self-loops are not allowed?
- Equation 3: $\mathcal{N}$ was already used to denote the entire set of nodes, whereas in this equation it is used to denote the neighbourhood. They are not the same, unless the graph is fully connected.
- The set of input features to the GNN should be fully described in the Method section and not only when discussing the ablation results (4.4).

**W3**. Potential limited scalability: the authors consider networks with up to 60 nodes, whereas the real Beijing network has approximately ~500 nodes. Hence, the problem as considered is a simplification, and this should be acknowledged. I expect that the observed performance improvement does not come "for free", and that the method suffers in scalability and has substantially longer running times than the classic methods. Studying the scalability of the method (around what number of nodes does it fail to find satisfactory solutions compared to the baseline) and adding representative runtimes for the methods would improve the manuscript.

### Questions
**C1**. The writing contains some important inaccuracies that should be fixed:

- "To achieve efficient search of the NP-hard problem" -> the solution space, not the problem itself, is being searched
- "The proposed model [...] successfully reduces the large solution space"; "the attentive policy network reduces the solution space drastically": as far as I can tell, the model itself does not reduce the solution space; rather, it may indeed be more efficient in how this search space is navigated.
	
**C2**. Typos: consider running a spellcheck. Some I have spotted: generic -> genetic (p2), maksed -> masked (p4), donate -> denote (p5)

**C3**. The analysis in 4.5 is tenuous, especially given the lack of multiple runs. For example, if we were to stop the process at step 60, we could draw a different conclusion from the one presented in this paragraph. Does this finding repeat across 10+ runs? 

**C4**. The following recent paper considers metro network planning as a case study and also uses a reinforcement learning approach. In my opinion, while not directly comparable, it should be cited:

> Darvariu, V. A., Hailes, S., & Musolesi, M. (2023). Planning spatial networks with Monte Carlo tree search. Proceedings of the Royal Society A, 479(2269), 20220383.

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
In this paper, the authors investigate the problem of metro network expansion, which they formulate as an MDP. The action is selecting a region and adding it to the metro network, and the reward is the increment of satisfied OD flow. They utilize a RL framework to solve the MDP. They use a GNN network to inject spatial contiguity and OD flow into region representations. The action mask and attentive policy network are used to ensure the feasibility of the result and to reduce search space. Authors apply the method to real-world urban data and witness significant performance improvements.

### Strengths
S1. The notion of region is particularly interesting, as it overcomes the limitation of fixed-size grids and captures both spatial proximity and traffic flow patterns.
S2. The work addresses numerous traditional and RL-based methods as baselines, with detailed comparisons and experiments. This justifies the use of RL methods in the practical aspect. The case study of complicated scenarios also give convincing explanations.
S3. The ablation study is thorough, and strengthens the design choices of the algorithm framework.

### Weaknesses
W1. In the "Overall Framework" section, the MDP and RL framework do not have a formalized definition, and the description and implementation details of the overall RL framework is rather unclear. Specifically, the state space, action space, and transition function of the MDP are not rigorously defined, making it difficult to understand the problem formulation. Furthermore, the RL algorithm used is not explicitly stated, and the details of how the GNN is integrated into the RL framework are missing. The policy network architecture and training procedure also lack sufficient detail.
W2. Some of the notations in the equations are not sufficiently clarified. For example, in equation (6), it is better to explicitly state that alpha_{i, j} is the relevance measure, and pinpoint the meaning of i and j. Moreover, the context for equation (5) is missing, making it unclear what n_{+-1} and n_{+-2} represent in the context of metro lines. The lack of clear definitions for these variables hinders the understanding of the equations.

### Questions
1. What is the precise definition of OD trips? How is it obtained from your dataset?
2. How do you determine whether a selected region should be an extension of an existing metro line (and which?) or the start of a new line? Is it determined in the agent's action, or by some other means?
3. In equation (5), which metro line do n_{+-1} and n_{+-2} refer to?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

# VColRL: Learn to Solve the Vertex Coloring Problem Using Reinforcement Learning

- Decision: Reject
- Scores: 5, 5, 5

## Abstract
We present VColRL, a reinforcement learning framework designed to solve the vertex coloring problem (VCP), where the objective is to assign colors to the vertices of a graph with the minimum number of colors, such that no two adjacent vertices share the same color. The framework is built on a novel Markov Decision Process (MDP) configuration to effectively capture the dynamics of the VCP, developed after evaluating various MDP configurations. Our experimental results demonstrate that VColRL achieves competitive performance in terms of using fewer colors as compared to advanced mathematical solvers and other metaheuristic approaches while being significantly faster. Additionally, our results show that VColRL generalizes well across different types of graphs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a reinforcement learning framework for solving the vertex coloring problem (VCP). The main idea is to use an episodic Markov Decision Process (MDP) to effectively model the dynamics of the coloring process, utilizing both Proximal Policy Optimization (PPO) and GraphSAGE. The writing is clear and well-organized.

### Strengths
1. This paper proposes a reinforcement learning framework that integrates the GraphSAGE architecture for the VCP.
2. A novel reward strategy specifically designed for the VCP is introduced.
3. Extensive experiments demonstrate the effectiveness of the proposed algorithm in comparison to state-of-the-art baselines.

### Weaknesses
1. Please clarify the novel features introduced in the MDP formulation, and how these differ from or build upon existing approaches like the defer action strategy.
2. Gurobi should be set to a consistent execution time across different benchmarks, and it would be beneficial to provide a longer execution time result as a reference for the optimal solution. 
3. Given that the proposed algorithm employs rollback mechanisms similar to iterative search, it would be appropriate to include an iterative search heuristic (i.e., tabuCol) as a comparison.

### Questions
1. How does the proposed algorithm decide when to activate the hard-rollback model versus the soft-rollback model?
2. Is the initial number of colors for each instance incremented starting from zero or from a specific given value?
3. The benchmarks in the COLOR02 table can include both DIMACS and COLOR02 instances. The benchmark instances could be more comprehensive, such as including DSJC125.5, DSJC125.9, DSJC250.1，and others.

### Soundness
3

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
The paper presents VColRL, a novel reinforcement learning framework for solving the Vertex Coloring Problem (VCP). The goal of VCP is to color graph vertices with the minimum number of colors so that no two adjacent vertices share the same color. VColRL uses a custom Markov Decision Process (MDP) to model VCP dynamics, optimizing color usage and generalizing well to diverse graph types.

### Strengths
1.VColRL outperforms traditional mathematical solvers and baseline methods, particularly for large and dense graphs, by effectively minimizing color usage. 
2.By using a unique reward strategy that prioritizes minimizing the highest-numbered color, VColRL efficiently manages color allocation, reducing convergence time and improving performance. This MDP design is a key factor in achieving both optimal color usage and stable results in the vertex coloring process.

### Weaknesses
1.While VColRL demonstrates strong performance on large-scale graphs, its complex architecture and computational demands are relatively high. The paper does not provide sufficient detail on its efficiency or scalability in practical applications, which raises concerns about its usability in resource-limited environments. Specifically, the paper lacks a detailed breakdown of the computational cost associated with each component of the VColRL framework, such as the graph neural network, the reinforcement learning agent, and the specific reward calculation. This makes it difficult to assess the practical feasibility of the approach, particularly for real-time applications or deployment on edge devices with limited resources. A more thorough analysis of time and memory complexity is needed.
2.Although VColRL performs well on most tested graphs, it is less effective on certain types, such as the mug family of graphs. The paper lacks a thorough analysis of why VColRL underperforms on these specific graphs, which slightly weakens its claims of general applicability. The paper does not explore potential structural properties of the mug family that might make them challenging for the proposed approach, such as specific connectivity patterns or symmetries. A more detailed investigation into the correlation between graph characteristics and VColRL's performance is needed to understand the limitations of the approach.
3.The paper discusses important design choices, such as rollback and reward strategies, but does not sufficiently explain the rationale behind these choices. Additionally, while hyperparameter settings and the training process are briefly covered, there is limited explanation on how the final parameter combinations were decided, reducing the model’s reproducibility and interpretability. For example, the paper does not provide a clear justification for the specific number of layers in the graph neural network or the choice of the learning rate. A more systematic approach to hyperparameter tuning, such as ablation studies or sensitivity analysis, is needed to ensure the robustness and reliability of the results.

### Questions
1.How does VColRL perform in terms of computational efficiency in real-world applications?
2.What specific factors contribute to VColRL’s limited performance on certain graph types, such as the mug family?
3.What criteria were used to select the final hyperparameter values and model configurations?

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
The authors tackle solving the Vertex Coloring Problem which is a known NP-hard problem using reinforcement learning. They formulate the problem as a Markov-Decision Process whose dynamics capture the graph coloring process. The agent is tasked with taking actions which include assigning colors to a subset of nodes and deferring other nodes to be assigned later. Two reward functions are proposed, max-color and color-count. An agent is trained using PPO where the graph neural network GraphSAGE is used as the function approximator. The experimental results show that the proposed methods outperform existing baselines.

### Strengths
- The paper is well-written and easy to follow. The related work section highlights existing gaps and shows how the proposed method differs from existing work. The main contribution is also well documented.
- The suggested modifications to the MDP formulation and the feature selection in previous work are an elegant approach to the vertex coloring problem, for example, the different roll-back strategies and the two reward functions.
- The proposed method outperforms existing baselines in the larger graph sizes.

### Weaknesses
 - The paper’s contribution, while valuable, may benefit from additional innovation, as it shares similarities with prior work by Ahn et al. which tackles the Maximum Independent Set also using Deep RL and GraphSAGE architecture. Further discussion on how the work is unique and where the overlap lies could strengthen the value of the work.
- There is not a lot of insight into why the method performs the way it does. For example, the results show that the color count reward is not as good as the max-color reward, but no discussion is provided about why that would be the case. 
- In the results section, the selected baselines do not include a machine learning-based approach.
-  In the related work the Vertex coloring problem is described as NP-complete. However, according to my understanding, the vertex coloring problem considered is the optimization version which is NP-hard, and not the decision version.

### Questions
- In the comparison of various MDP configurations results section, was the color count reward with other settings than hard rollback and deferred actions considered? If not isn't it possible that color count with a different setting outperforms HDM?

### Soundness
3

### Presentation
3

### Contribution
2

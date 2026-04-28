# Learning to Select Nodes in Branch and Bound with Sufficient Tree Representation

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
Branch-and-bound methods are pivotal in solving Mixed Integer Linear Programming (MILP), where the challenge of node selection arises, necessitating the prioritization of different regions of the space for subsequent exploration. While machine learning techniques have been proposed to address this, two crucial problems concerning \textbf{(P1)} how to sufficiently extract features from the branch-and-bound tree, and \textbf{(P2)} how to assess the node quality comprehensively based on the features remain open. To tackle these challenges, we propose to tackle the node selection problem employing a novel Tripartite graph representation and Reinforcement learning with a Graph Neural Network model (TRGNN). The tripartite graph is theoretically proved to encompass sufficient information for tree representation in information theory. We learn node selection via reinforcement learning for learning delay rewards and give more comprehensive node metrics. Experiments show that TRGNN significantly improves the efficiency of solving MILPs compared to human-designed and learning-based node selection methods on both synthetic and large-scale real-world MILPs. Moreover, experiments demonstrate that TRGNN well generalizes to MILPs that are significantly larger than those seen during training.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors propose solving the node selection problem using a novel tripartite graph representation combined with reinforcement learning and a Graph Neural Network model. Additionally, the authors have theoretically proven that the tripartite graph representation is sufficient in information theory. The authors used a MDP to model the node selection problem and the reward function consists of three parts, including the updates to the global gap, the potential of a node to lead to an optimal solution and the normalized reward for path-switching steps. The experimental results show that the proposed TRGNN outperforms existing baselines that use learning-based methods on six NP-hard MILP problem benchmarks. Moreover, the trained model demonstrates a certain level of generalization.

### Strengths
（1）The paper is well organized. First, the tripartite graph representation of the branch-and-bound tree is explained, and it is proven that this representation can capture sufficient information. Then, the overall algorithm framework is presented, and the components of the MDP are described.

（2）The method of converting the branch-and-bound tree into a tripartite graph presented in the paper is worth learning, especially since the authors prove that the information obtained through the GNN on this graph captures sufficient information contained in the tree.

（3）The experimental results are promising, demonstrating that the approach outperforms recent machine learning algorithms as well as the state-of-the-art best estimate node selection rule.

### Weaknesses
（1）The presentation in the paper is not clear enough and lacks some necessary definitions, such as what a leaf node vertex is. I struggled to understand what the LN set represents until I re-read the paper and carefully examined Figure 1.

（2）For the branch-and-bound tree conversion method, there is a lack of concrete examples. Although a simple conversion is provided in Figure 1, it lacks an explanation of how each step is derived, and there is no description of the features on the edges.

### Questions
（1）Please address the issues raised in the weaknesses section.

（2）The paper uses a heuristic algorithm to initially select a subset of nodes, and then employs the model to choose one node from this subset. How do the results of this approach compare to the experimental results of directly using the heuristic algorithm to select nodes without employing the model?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper addresses challenges in node selection within the branch-and-bound (B&B) algorithm for Mixed Integer Linear Programming (MILP). It introduces two key contributions to improve node selection effectiveness: (1) a novel tripartite graph representation of B&B trees, and (2) a deep reinforcement learning approach that treats node selection as a learning-based strategy, enabling the model to optimize node selection by training on a set of instances.

### Strengths
(1) This paper introduces a novel tripartite graph representation of B&B trees, theoretically proven to contain sufficient data for optimal node selection. This representation integrates the problem structure of MILP, typically represented as a bipartite graph, with the global information of the B&B algorithm.

(2) This paper analyzes the shortcomings of prior works, framing node selection as a learning-based strategy and employing reinforcement learning to identify an optimal node selection heuristic that surpasses expert-designed heuristics.

### Weaknesses
 (1) It is well-known that B&B trees inherently contain both the detailed information of the B&B algorithm and the problem structure of MILP. This raises the question of whether it is necessary to construct a tripartite graph to represent B&B trees, given that this approach increases the graph scale, resulting in greater storage and computational complexity. The authors should analyze how the advantages of the tripartite representation compensate for these increased demands. Additionally, it would be helpful to assess the specific contributions of the MILP bipartite graph within the tripartite structure and quantify its impact on the representation's effectiveness.

(2) In the MDP process, each action requires a heuristic algorithm to generate candidate nodes. It would be helpful to know the time complexity of this heuristic algorithm and whether its solution quality is affected by the increased scale of MILP instances.

(3) When selecting a specialized solver for MILP, it is advisable to consider higher-performance options like Gurobi, as this can enhance the credibility of the results. Additionally, the baseline methods used are not the most recent; the latest state-of-the-art approaches for solving MILP should be considered, rather than limiting the focus solely to node selection. Other strategic methods should also be included in the evaluation.

### Questions
(1) Please analyze the time complexity of the TRGNN and other baseline methods.
(2) The reinforcement learning framework claims improved node selection by minimizing delayed rewards; however, how are potential biases in the reward function, such as those from pre-selecting candidate nodes, accounted for to ensure fair comparisons with existing machine learning baselines?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This work presents a novel way of selecting nodes in the Branch-and-Bound algorithm, by constructing a sufficient representation that splits the features into “global” features containing information of the root MILP, and “leaf” features containing information on each individual leaves. This allows them to represent the entire tree, while keeping the representation compact by bundeling all features of the principal relaxation into a common bipartite graphs and only representing the changes towards one of the leaf nodes.

### Strengths
Strengths:
-	Well motivated representation via Mutual information
-	Compact representation
-	High benchmark performance
-	The reward function involving path switching is generally interesting for all node selection methods

I also want to commend the authors for noting the difference in performance of different SCIP versions which is often neglected in comparisons between methods.

### Weaknesses
One notable issue in the sufficiency argument of the tripartite representation is the assumption of a Markov mapping between parent and child, which is not generally true: For instance, restarts or cut pools may add arbitrary external information that is not located in the parent into the child. This means that in modern Branch-and-Bound solvers such as SCIP, one can generally not get the decompositions shown in appendix B. 
In fact, the method seems to have no way of dealing with cutting planes (it does not even contain features to explain cutting planes).

I recommend qualifying the sufficiency conditions with conditions making clear that these representations are only valid for traditional Branch-and-Bound methods, not more modern restarting Branch-and-Cut methods such as SCIP.

A more general problem is found in the benchmarking: This work trains a node selector on some problem XYZ and then benchmarks on different instances of the same problem XYZ. This is a flawed way of doing benchmarking: If you want to compare a _general_ node selector (SCIP) against your node selector, you also have to use a general problem set. 

As is, the quality of the heuristic is not really meaningful: Generally, humans can also develop better heuristics if the type of problem is known. To show that your method leads to superior performance in one of these tasks (e.g. MAXSAT) you would need to compare against an exact MAXSAT solver. Alternatively, you could also benchmark a single selector on all domains, to show that your method can indeed compete against the general node selectors developed in e.g. SCIP.

The statement “Experiments show that TRGNN significantly outperforms human-designed and learning-based baselines” is therefore not supported, since both methods are evaluated under different standards (SCIP “one size fits all” vs. learned ones for every instance type).

Figure 2. is hard to read due to the apparent circular dependency of “n nodes”, TRGNN and the “Q-values”. The figure only makes sense if taken in context with the main text: My recommendation: Remove the arrow from the Q-value vector to the “n nodes” bubble, add numbers to the arrows, and explain the figure step-by-step in the description (the figure should be understandable without needing additional context).

For related work, there are two papers that already include a full tree representation “Learning to branch with Tree MDPs “ https://arxiv.org/pdf/2205.11107 uses a tree-like MDP to do branching, and “Reinforcement Learning for Node Selection in Branch-and-Bound” https://arxiv.org/abs/2310.00112 uses a tree-like state representation fornode selection.

Do you have an ablation of the impact of your path-switching reward? While path switching is a measurable effect in node selection. There are many other aspects as well, like the complexity of a node is not being constant: Depending on how many (dual) simplex iterations you need to restore optimality under the new constraints, and which heuristics are run for how long (e.g. diving heuristics) the cost of exploring a node can vary significantly.

What are the effects of the truncation to only the top-n “best estimate” nodes? I understand you can’t test this hyperparameter extensively, but you could give a distribution over which position in the "best node list" is picked by your selector. If you record this on a histogram, you could estimate the impact of truncating the top-n to a k<n.
This would also show how much your method depends on the quality of the "best estimate" node selector.

I generally like this work, with the one big holdup being the lack of generalization of a learned node selector to different problem sets.

### Questions
- Can you re-run the experiments with a single node selector for all tasks?
- Regarding experiments in table 2: In line 466 you say you use geometric means and standard deviations, while table 2 claims it uses arithmetic means. Which one is used in the table? 
- Do you have an ablation of the impact of your path-switching reward?
- What are the effects of the truncation to the top-n “best estimate” nodes?

See "weaknesses" for more details.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a novel approach to node selection in Branch-and-Bound (B&B) algorithms for Mixed Integer Linear Programming (MILP). It proposes using a Tripartite Graph Neural Network (TRGNN) combined with reinforcement learning to address two major challenges: sufficient representation of the B&B tree and comprehensive node quality assessment. The tripartite graph representation effectively captures tree information, while the reinforcement learning framework uses delayed rewards to optimize node selection. Experiments show that TRGNN significantly outperforms traditional human-designed and learning-based approaches in solving efficiency, achieving notable improvements across a variety of MILP benchmarks.

### Strengths
### 1. **Innovative Representation Approach**:
   - The use of a tripartite graph representation to capture information about the entire branch-and-bound (B&B) tree is an original contribution. The approach is theoretically proven to be sufficient, ensuring that the representation fully captures the relevant information needed for effective node quality assessment.

### 2. **Reinforcement Learning for Node Selection**:
   - The paper employs reinforcement learning (RL) to learn an effective node selection policy, which is a significant improvement over traditional imitation learning methods. By incorporating delayed rewards, the RL-based approach captures the long-term impact of node selection decisions, leading to better outcomes.

### 3. **Comprehensive Evaluation Metrics**:
   - The introduction of three metrics—global gap updates, potential for optimality, and path-switching overhead—provides a more comprehensive assessment of node quality. This helps the TRGNN model make more informed decisions during the B&B process.

### 4. **Strong Experimental Results**:
   - Experiments demonstrate that TRGNN significantly outperforms both human-designed heuristics and other learning-based methods, including GNN-based models and traditional SVM approaches. TRGNN achieves up to 59.42% reduction in solving time, indicating its practical impact on MILP problem-solving efficiency.

### 5. **Generalization Capability**:
   - TRGNN's ability to generalize to larger MILP instances beyond those used in training is a key strength. The model outperforms existing solvers on significantly larger problem sizes, which underscores the scalability and robustness of the proposed approach.

### 6. **Theoretical Grounding**:
   - The paper provides solid theoretical foundations for its approach, including proofs that the tripartite graph representation is sufficient in information theory. This enhances the credibility of the methodology and helps justify its effectiveness in solving the MILP node selection problem.

### 7. **Efficient Learning**:
   - The TRGNN model demonstrates higher learning efficiency compared to conventional models, requiring fewer training samples to achieve comparable performance. This efficiency is beneficial in scenarios where data collection is costly or time-consuming.

### Weaknesses
### 1. **Complexity of Graph Representation**:
   - **Weakness**: The tripartite graph representation is complex, especially for large-scale instances, which may lead to high computational costs. The paper does not sufficiently analyze the memory footprint of this representation, particularly concerning the storage of node, constraint, and leaf node features, and the adjacency matrices. The computational overhead of constructing and updating this graph during the branch-and-bound process is also unclear. 
   - **Suggestion**: Consider providing an analysis of the computational overhead introduced by the tripartite graph representation. Discuss possible optimizations or alternative representations that balance complexity and computational efficiency.

### 2. **Limited Baseline Comparisons**:
   - **Weakness**: The experimental comparisons focus primarily on human-designed heuristics and learning-based models but do not include more recent or diverse approaches in GNN-based optimization or other advanced reinforcement learning methods. There is a lack of comparison against other state-of-the-art GNN architectures specifically designed for combinatorial optimization, such as those employing attention mechanisms or graph transformers.
   - **Suggestion**: Expand the list of baseline models to include state-of-the-art approaches in GNNs and other deep learning-based optimization techniques. This would provide a more comprehensive evaluation of TRGNN's advantages.

### 3. **Scalability Concerns**:
   - **Weakness**: Although the model shows good performance on larger problem instances, there is insufficient discussion on the scalability of the method concerning memory requirements and computational resources. The paper does not provide a detailed analysis of how the memory consumption and computational time scale with increasing problem size, particularly in terms of the number of variables, constraints, and the depth of the branch-and-bound tree.
   - **Suggestion**: Include an analysis of memory consumption and computational requirements when scaling the model to large MILP instances. This would help understand the practical limitations and requirements for deploying the approach in real-world scenarios.

### 4. **Lack of Ablation Study on Graph Representation**:
   - **Weakness**: The paper does not thoroughly evaluate the effectiveness of the tripartite graph representation versus other potential graph representations (e.g., bipartite or simpler versions). The justification for using a tripartite graph over other graph structures is not fully supported by empirical evidence.
   - **Suggestion**: Conduct an ablation study comparing the tripartite graph representation with other simpler graph structures to demonstrate why it is more effective in capturing relevant information for node selection.

### 5. **Limited Analysis of Hyperparameters**:
   - **Weakness**: There is little to no discussion on the sensitivity of the model's hyperparameters, such as the reinforcement learning reward weights and the parameters in the graph convolution layers. The paper lacks an analysis of how different hyperparameter settings affect the model's convergence and performance.
   - **Suggestion**: Provide a sensitivity analysis of key hyperparameters, explaining how they impact the model's performance. This would help practitioners effectively tune the model for different MILP problems.

### 6. **Implementation and Practical Considerations**:
   - **Weakness**: The paper lacks detailed information on implementation aspects, such as training time, hardware requirements, and challenges in real-world implementation. The paper does not provide sufficient information on the practical aspects of training and deploying the model, including the computational resources required and the time needed for convergence.
   - **Suggestion**: Add practical details about the model's implementation, including the training time required for various datasets, hardware used, and potential challenges encountered during implementation. This would aid in understanding the practical feasibility of adopting TRGNN.

### 7. **Limited Applicability to Non-MILP Problems**:
   - **Weakness**: The paper focuses exclusively on MILP problems and does not discuss whether the proposed approach could be generalized to other types of optimization problems. The paper does not explore the potential for adapting the method to other combinatorial optimization problems, such as those involving non-linear constraints or different solution search strategies.
   - **Suggestion**: Include a discussion on the potential for adapting TRGNN to other combinatorial optimization problems, such as Mixed-Integer Nonlinear Programming (MINLP) or general constraint satisfaction problems. This would extend the relevance of the proposed method.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
3

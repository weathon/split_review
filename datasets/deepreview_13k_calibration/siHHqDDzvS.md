# BTBS-LNS: Binarized-Tightening, Branch and Search on Learning LNS Policies for MIP

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 6, 8, 5

## Abstract
Learning to solve large-scale Mixed Integer Program (MIP) problems is an emerging research topic, and policy learning-based Large Neighborhood Search (LNS) has been a popular paradigm. However, the explored space of LNS policy is often limited even in the training phase, making the learned policy sometimes wrongly fix some potentially important variables early in the search, leading to local optimum in some cases. Moreover, many methods only assume binary variables to deal with. We present a practical approach, termed Binarized-Tightening Branch-and-Search for Large Neighborhood Search (BTBS-LNS). It comprises three key techniques: 1) the ``Binarized Tightening" technique for integer variables to handle their wide range by binary encoding and bound tightening; 2) an attention-based tripartite graph to capture global correlations among variables and constraints for an MIP instance; 3) an extra branching network as a global view, to identify and optimize wrongly-fixed backdoor variables at each search step. Experiments show its superior performance over the open-source solver SCIP and LNS baselines. Moreover, it performs competitively with, and sometimes better than the commercial solver Gurobi (v9.5.0), especially on the MIPLIB2017 benchmark chosen by Hans Mittelmann, where our method can deliver 10\% better primal gaps compared with Gurobi in a 300s cut-off time.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes enhancements to an existing ML approach to Large Neighborhood Search (LNS) for Mixed-Integer Linear Programming (MILP). The framework is as follows: value-based RL is used in conjunction with a GNN representation of the MILP to learn a policy that selects, at each step, a subset of the decision variables to fix and search around. The RL reward function favors finding a sequence of improving solutions. This paper aims to improve this framework.

First, the authors devise a heuristic for efficiently handling non-binary integer variables, a common feature of many MILP problems that has not been dealt with in prior ML work. Second, an existing GNN architecture for MILP is slightly modified to allow for better attention scores. Third, a supervised learning approach is used to override potentially incorrect LNS variable fixing actions made by the RL agent. This is done by training another GNN to predict high-quality solutions. Should an LNS fixing action for a variable disagree with the predicted value for it, the LNS action is dismissed. 

Experiments are performed on four problem classes as well as some MIPLIB2017 instances. The proposed method along with some ablations of it are compared to solvers SCIP and Gurobi, non-ML LNS methods, and existing ML LNS methods. Favorable performance is exhibited.

### Strengths
S1. A significant engineering effort is made to improve the RL-LNS approach. It covers the GNN architecture, the handling of integer variables, and the corrective mechanism. That all these aspects are considered simultaneously is a strength of this paper.

S2. Integer variable handling: Although I have questions about this part, it is a solid contribution to this area of research. Typically, we assume that bounded integers can be recast as a set of binary variables. However, this expansion introduces additional variables and constraints which can slow down MIP solving.

S3. Corrective mechanism: I also liked this contribution given that it addresses limitations of RL. 

S4. The experimental setup is sound and the performance of the proposed method is very competitive. It is impressive that it can compete with SCIP and Gurobi.

### Weaknesses
W1. The writing can be improved. I have included a sample of minor comments in “Questions” but I do believe that going over the paper using tools such as Grammarly can help improve the clarity of the paper. This is crucial for publication at a conference at the level of ICLR.

W2. The GNN architecture is essentially the same as that of Ding et al.’s. I am not sure that it stands on its own as a contribution. Rather, I view this as an architecture tuning step that is rather incremental.

W3. The corrective mechanism in section 3.4 requires labeled data, namely near-optimal solutions either globally or locally. This increases the data collection cost which now includes this labeling via a MILP solver in addition to RL simulations. Given that the MILPs of interest are NP-Hard to optimize, it is unclear to me that relying on this solving step during data collection is justified. This is a chicken-and-egg situation because if collecting such solutions was easy, no ML would be required. If it is hard, then ML is justified but then this data collection process is potentially prohibitive.

W4. The bound tightening method is not described sufficiently clearly. Perhaps a small numerical example can help Illustrate what you’re doing in Algorithm 1.

### Questions
Please refer to the weaknesses above.

The writing can be improved substantially. Here are some minor comments:
- line 148: consider rephrasing to “selecting the variable subsets that may need to be optimized at each step, with the remaining variables fixed or bound-tightened”
- 156: “training details are described in Sec. 3.3. ….”
-  307: “trained offline”
-  Table 2 caption is incomplete?

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
4

### Summary
The paper presents the BTBS-LNS (Binarized-Tightening, Branch and Search for Large Neighborhood Search), a method designed to solve large-scale Mixed Integer Programming (MIP) problems. It addresses two main issues in learning-based LNS approaches: limited exploration in search spaces, and a tendency to prematurely fix important variables, which may lead to suboptimal solutions. The proposed method introduces three main innovations:

Binarized Tightening: Encodes integer variables into binary form, allowing bound tightening to reduce solution space complexity.
Attention-based Tripartite Graph: Models relationships among variables, constraints, and objectives to capture global correlations.
Branching Network: Optimizes potentially misclassified “backdoor” variables to help escape local optima.
Through experiments on benchmarks like MIPLIB2017, the method demonstrates competitive performance, often surpassing traditional solvers like SCIP and sometimes outperforming Gurobi.

### Strengths
Innovation in Problem Encoding: Using a tripartite graph structure to represent MIP instances is a novel approach that strengthens the model's ability to capture complex dependencies.

Generalization to Integer Variables: Unlike many LNS methods that focus only on binary variables, BTBS-LNS can handle a broader class of integer variables, improving the method's applicability to general MIP problems.

Superior Performance: The method shows strong empirical results across multiple MIP problems and benchmarks, achieving lower primal gaps than SCIP and Gurobi in some cases.

Adaptive Bound-Tightening: Binarized tightening provides an efficient exploration-exploitation balance, with flexibility for bounded and unbounded variables.

### Weaknesses
High Complexity: The approach combines multiple advanced techniques, potentially making it computationally intensive, particularly in scenarios requiring extensive parameter tuning or high-dimensional data.

Dependence on Initialization: The method relies on an initial feasible solution generated by baseline solvers. Poor initialization could impact overall performance, as the effectiveness of the LNS-based policy might depend on the quality of the starting solution.

Local Optima: While the branching network mitigates local optima issues, the reliance on imitation learning and reinforcement learning can still lead to convergence to suboptimal solutions in complex or highly irregular MIP landscapes.

### Questions
How does the performance of BTBS-LNS scale with increasing problem size, especially compared to state-of-the-art solvers like Gurobi, in terms of both time complexity and solution accuracy?

Does the choice of baseline solver (SCIP or Gurobi) for generating initial solutions significantly influence BTBS-LNS's overall performance?

How does the model handle diverse real-world MIP problems where variables might not align as neatly with the tripartite structure employed in BTBS-LNS?

Have you compared your work with a recent related work by Kong et al.? https://proceedings.mlr.press/v244/kong24a.html

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
4

### Summary
Authors propose a neural large neighborhood search (LNS) policy which improves upon previously proposed methods in mainly three aspects. First, authors focus on general mixed integer programming (MIP) which some variables can be integer type (as opposed to be only allowed binary type), and proposes a "binarized tightening" method, which performs much better than previous methods. Second, authors propose to remove softmax operation in the graph neural network for MIPs. Third, authors train additional LNS policies with imitation learning, and let these policies override decisions from RL-trained LNS policy. These imitation-learned policies provide additional signals and hence help escaping from local minimum.

### Strengths
Significance: The proposed method demonstrates a strong empirical performance compared against a large number of previous learning-based methods as well as strong traditional solvers (Gurobi, SCIP). Such a strong empirical result can drive a stronger adoption of learning-based MIP solvers in practice. The coverage of experiments and the experimental protocol is high quality (discussed below in the quality section), which will give practitioners high confidence to adopt the proposed approach. If successful, this will make a significant impact to applications of MIP.

Quality: The coverage of benchmarks is very high. Authors not only experiment with synthetic tasks popular in previous papers, but also more recent and challenging benchmarks in ML4CO competition and MIPLIB2017. Authors compare against 13 learning-based baselines, which comprehensively validates algorithmic design decisions made in this paper. Although the proposed method is quite complex, such a strong validation justifies the complexity well.

Originality: Binarized tightening is a novel technique clearly differentiated from previously proposed methods for general MIPs. Other techniques introduced are not very surprisingly new, but still contributes significantly to the performance of the final approach, and validated well by extensive experiments.

Clarity: Although the proposed algorithm is quite complex with many components, authors do a good job clearly explaining them, and providing good justifications both conceptually and empirically for every algorithmic design decision they make. Some terminologies are phrased a bit confusingly, however, which I elaborate in the Weaknesses section.

### Weaknesses
Authors argue their branching network leverages "global" information and uses a "global" view, but I believe this is a misnomer because at the inference time, the branching network uses the same state representations as the LNS policy. It is just that the branching network is _trained_ with different imitation learning signals, global optimum solution for BTBS-LNS-G and local branching for BTBS-LNS-L. Other than the training method (RL vs. imitation learning), the branching network makes the same decisions (whether to fix each variable) as the LNS policy do; in fact, what authors call as local branching is called LNS from previous work (Sonnerat et al, 2022). I would consider these as simply additional LNS policies, just trained differently (RL vs. imitation learning).

While my major concern is mostly on the phrasing of "global" information because such information is not available at inference time, I also point out that this perspective - that branching networks are simply LNS policy trained differently - offers more natural ways to combine these branching networks into the algorithm. For example, they could be ensembled together using standard ensemble methods, because they are policies for the same objective which are just trained differently. Or, LNS policy could be initialized by these branching policies for transfer learning. I believe these are more natural ways of combining these two policies, rather than first making predictions with RL policy and then override predictions by imitation-learned policies.

There's another suggestion for clarification. In Line 070, authors say: "We further develop an attention-based tripartite graph (Ding et al., 2020)". Although Ding et al (2020) is attributed here, the statement can be read as attention-based tripartite graph being proposed by authors for the first time. To make the attribution clearer, I would suggest to rephrase as something like: "We employ an attention-based tripartite graph (Ding et al., 2020). We improve the previously proposed attention architecture by removing the softmax normalization, and demonstrate its empirical effectiveness." Such statement will make authors' contribution clearer.

### Questions
How are substitute variables for integer variables represented?  $j$ in $a_{i,j}^t$ should be reflected as feature somewhere, but features in Table 7 does not seem to discuss it.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents an ML-guided LNS framework for MIPs. It combines a binarize-and-tighten scheme to address general integer variables and a branching policy to help escape local optima. It also has a search policy to guide destroy variables. In the experiment, the new method is compared against a variety of ML-guided approaches and heuristic approaches. The presented results show that the proposed method finds better solutions at a faster speed.

### Strengths
1. The paper proposes a combination of ML-guided search policy and branching policy for LNS in MIP solving. Various techniques and engineering designs are proposed. The novelty of the paper comes from those details.
2. The effectiveness is demonstrated in experiments with different settings and ablation studies.

### Weaknesses
1. The proposed methods are not novel. The global branching idea is similar to [2] by learning from the global (near-)optimal solutions. While the local branching variant is similar to [1]. A detailed explanation of the differences from them should be included.
2. The paper is a little bit hard to follow. It includes a lot of information, it would be good to include a summary of takeaways for each experiment.
3. How are the policies trained in the MIPLIB 2017 experiments? How do you perform training, validation and testing? The variance of the hardness for MIPLIB is large, how do you deal with it when splitting the training, validation and testing set? Can you also summarize the results on MIPLIB in comparison with the other baselines besides Gurobi? Can you bold the best entry in the per-instance result tables in Appendix?
4. The paper lacks comparison with recent state-of-the-art methods, specifically those utilizing GNNs and contrastive learning for LNS, such as the methods proposed by Kong et al. and Ye et al. Some of the cited work in the paper was also not compared with these recent methods.

### Questions
1. What is eq. 6 in figure 2?

### Soundness
2

### Presentation
2

### Contribution
2

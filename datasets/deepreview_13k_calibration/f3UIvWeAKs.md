# Learning Node Selection via Tripartite Graph Representation in Mixed Integer Linear Programming

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 6, 3, 3

## Abstract
Branch-and-bound methods are pivotal in solving Mixed Integer Linear Programs (MILPs), where the challenge of node selection arises, necessitating the prioritization of different regions of the space for subsequent exploration. While machine learning techniques have been proposed to address this, our paper resolves two crucial and open questions concerning \textbf{(P1)} the representation of the MILP solving process and \textbf{(P2)} the qualification of nodes in node selection. We present a novel tripartite graph representation for the branch-and-bound search tree, which, through theoretical validation, proves to effectively encapsulate the essential information of the search tree for node selection. To further this, we introduce three innovative metrics for node selection and formulate a GNN-based model, DQN-GNN, utilizing reinforcement learning to derive node selection policies. Empirical evaluations illustrate that DQN-GNN markedly enhances the efficiency of solving MILPs, surpassing the existing human-designed and learning-based models. compared to other AI methods, our experiments substantiate that DQN-GNN exhibits commendable generalization to MILPs that are substantially larger than those encountered during training.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses the heuristic designs for node selection in BnB for MILP from an ML-guided perspective. The paper proposes a new tripartite representation and a new RL-based framework to learn such heuristics. It provides theoretical analyses to support some of the design choices in the framework. Empirically, the method is tested on three different benchmark, resulting in shorter runtime and smaller tree sizes in some cases.

### Strengths
1. The paper studies the important questions of node selection for MIP solving. 
2. It provides a theoretical understanding that motivates the design of the ML methods
3. Experiments show promising results on small MIP instances.

### Weaknesses
1. The empirical study was done on pretty easy instances and the slowest approaches took only less than half a minute to solve them. It is more common for this kind of study to test on harder and/or larger instances. The lack of scalability to more complex problems is a significant concern, as the reported runtimes suggest the instances are not representative of real-world MILP challenges. The paper should demonstrate the method's efficacy on problems where the solving time is on the order of hours, not seconds, to be considered a practical contribution.

2. Only runtime and number of nodes were reported in evaluations. It will be important to include more metrics such as win/loss rate and scatter plots to understand the per-instance performance. The absence of win/loss rates makes it difficult to assess the consistency of the proposed method's performance. Scatter plots are crucial for visualizing the distribution of performance across different instances, highlighting where the method excels or struggles. Without these, it's hard to determine if the average performance is representative or skewed by outliers.

3. The paper doesn’t provide a literature review of related work. There are three very related works (SVM, Ranknet and GNN) compared against in experiment. However I wish to understand what the unique contributions of this paper are over those previous works. Furthermore, there are a few more works on ML-guided node selection for tree search algorithms for other combinatorial optimization problems. It would be important to acknowledge them in related work. The lack of a comprehensive literature review makes it difficult to position the paper's contribution within the broader field. The paper needs to clearly articulate how its approach differs from and improves upon existing methods, especially those using similar techniques like SVM, Ranknet, and GNN. Additionally, the paper should acknowledge related work in other combinatorial optimization domains to provide a complete context.

4. Writing can be improved. (1) The edges between V and NC are never defined. I think they are defined similarly to the edges between V and C; (2) Gap reward in Theorem 4.1 is undefined (though defined later); (3) It would be important to describe the intuitive idea for proving each theorem. (4)Typo: 
	Section 3.2: V \cup C = V\cup NC = C\cup NC should be taking the intersection instead.
	Section 4.2 mordern -> modern

### Questions
The node constraints vertices represent constraints added in addition to the root problem. They seem to be only one variable if they are constraints added by branching, as mentioned in 3.2 (the 4th line in the paragraph). In that case, each NC vertex will have only one edge connecting to one variable vertex. Is the tripartite representation necessary? This would be more useful if you consider cuts added to the nodes.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors introduce a novel tripartite graph representation for the branch-and-bound search tree, which is theoretically proven to encapsulate sufficient information of the search tree, enabling effective node selection in the solving process. They propose three innovative metrics for node selection and develop a DQN-GNN model that employs reinforcement learning to learn node selection policies in MILP solving. The model consists of a GNN that encodes the tripartite graph representation of the search tree into a fixed-dimensional vector and a DQN that takes the encoded vector as input and outputs a Q-value vector for each candidate node. The model is trained to maximize the expected cumulative reward, which is defined as a combination of three metrics: the node's contribution to the relaxation bound improvement, the node's contribution to the search tree size reduction, and the node's contribution to the solution quality improvement. The authors design and conduct experiments that demonstrate the efficacy of the DQN-GNN model in enhancing the efficiency of solving MILPs, showing significant improvement over existing human-designed and learning-based benchmarks.

### Strengths
1. Introducing a novel tripartite graph representation for the branch-and-bound search tree, which is theoretically proven to encapsulate sufficient information of the search tree, enabling effective node selection in the solving process.
2. Proposing three metrics for evaluating rewards of node selection and developing a DQN-GNN model that employs reinforcement learning to learn node selection policies in MILP solving.
3. The model exhibits commendable generalization to larger MILPs.

### Weaknesses
1.	Objective 2: The historical optimal solution path is not clear. I don't quite understand what is a historical optimal solution. Is it a global optimal solution or just an intermediate non-proven local optimal solution? 
2.	Since the performance is inconsistent on larger cases, can author provide any insights on what type of MILP problem would be suitable for the proposed methods?
3.	What is the rule of setting hyperparameter n (# of nodes for selection)? What if I choose some other values (e.g., n=30,50,100)
4.	Do you also restrict the number of nodes to be selected for SCIP?

### Questions
Please refer to Strengths and Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the use of machine learning to improve node selection in branch-and-bound solvers for integer programming. Node selection (along with variable selection and cut selection) is one of the important aspects of branch-and-bound, and a good node selection policy is critical to reducing solve time and the size of the branch-and-bound tree. The authors make two main contributions: first, they propose a new representation of the MIP as a tripartite graph that captures the branching constraints used to arrive at a particular child node; second, they train an RL model based on this representation to tune their node selection policy.

### Strengths
The integration of machine learning with MIP solvers is a topic of considerable importance and recent interest. Node selection is an important aspect of this that has not been as thoroughly studied. The authors provide good motivation for studying the problem. Furthermore, consideration of path switching costs in node selection is a subtle and important issue, and it is interesting that the authors study methods to alleviate this.

### Weaknesses
The tripartite graph representation in Section 3.2 could be explained a lot more clearly. As is, it is just defined as an abstract object but the authors never define clearly how it is built from the underlying MIP. It is more or less possible to infer how they do this from Figure 1, but all of this ought to be clearly defined in the body of the paper.

Similarly, the information of a node I(N) is never formally defined.

I’m not really sure what Theorem 3.2 is saying. Branch-and-bound is a deterministic algorithm, so indeed all the information needed for its execution is contained at the root node for a fixed node selection policy. A brief glance at the proofs in the appendix makes me skeptical that Theorems 3.1 and 3.2 are saying anything rigorous/meaningful about branch-and-bound.

I do not understand Theorem 4.2 and its proof. The authors claim here that node selection and variable selection are “independent”. The proof seems to show that given a fixed tree state, the optimal node does not depend on the variable selection policy. But the assumption that there is a given fixed tree state means that the variable selection decisions have already been made at the point of node selection. Varying the variable selection policy would change the current subtree, and the premise of the theorem wouldn’t hold. I don’t think it is scientifically valid to claim from this theorem that node selection and variable selection are “independent”, and my guess is that most viewpoints in MIP solving would take issue to this claim.

The writing in the paper needs a lot of improvement. There are grammatical errors and issues with sentence structure in nearly every paragraph that make the paper difficult to read.

### Questions
I don’t really understand the motivation in the “From Nodes to Constraints” paragraph. Variable selection is what determines the actual additional constraints to the subproblem; node selection is about exploration order.

Doesn’t the set NC in the tripartite graph representation grow very large since every leaf node is stored? Are there any limitations due to this?

Additional comments/questions:
-Section 2 title “Preliminary” needs to be “Preliminaries” or “Preliminary background” or something like that

-“feature vector of vertex e_k” -> “feature vector of edge e_k” on page 3.

-In the section “MILP as Weighted Bipartite Graph” you might want to include that there is an edge between a variable vertex and a constraint vertex iff the variable has a nonzero coefficient in the constraint.

-The P(X, f) notation in the section “Branch-and-Bound Method” seems out of place. Why not stick with the MIP notation used previously?

-In Section 3.2 “V ∪ C = V ∪ NC = C ∪ NC = ∅” the unions should be intersections.

-In Section 3.2 you should include how the tripartite graph is actually defined, i.e. how are the edges in the graph determined. As far as I can tell the reader is left to infer this from Fig. 1.

-The feature vector labels in Fig. 1 are not explained anywhere as far as I could tell. E.g., what does a feature vector of $(0, +\infty, -2)$ for the node corresponding to variable $x$ mean? Also, the edges between $V$ and $NC$ are labeled with pairs denoting the sign of the branching constraint, which I take to be the edge feature vectors. But these are labeled $e_i^{NC}$ in Fig. 1, which are the edge weights? What are the actual edge weights, and what do they represent?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a method to learn node selection policy for solving mixed integer linear programming (MILP) problems. It tries to resolve two issues in existing deep learning based MILP methods, i.e., insufficient state representation and reward design. For the first issue, a tripartite graph representation scheme is proposed, which differs from the widely used bipartite graph representation with a new set of additional constraints. For the seconde issue, a new reward scheme with three components are designed to facilitate reinforcement training. Theoretical analysis are provided to support the design. Experimental results show that the learned policy outperforms default SCIP policy and several deep learning based methods.

### Strengths
1. The motivation is clear, and the two technical contributions are based on interesting and insightful observations.
2. Some theoretical results are presented.
3. The paper is well-written and easy to follow.

### Weaknesses
1. The evaluation is relatively weak. The problem instances are too simple, which can be solved by SCIP within a minute. Using a heavy deep learning architecture to enhance MIP solving performance on such trivial problems are not very meaningful. Besides, the speedup effects over default SCIP is not very significant. If the decision maker can allow one minute for solving, then 10 seconds shorter runtime is not very meaningful.

2. The trained policy degrades significantly on larger problem, which further lowers the pracicability of the proposed method.

3. There is no ablation study results to support the advantages of the proposed method. For example, how about using the traditional bipartite graph representation instead of the newly proposed tripartite scheme? What are the contributions of the three reward componenets on the final performance?

### Questions
Please see the above weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

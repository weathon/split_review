# Reinforcement Learning for Node Selection in Branch-and-Bound

- Decision: Reject
- Scores: 5, 3, 5, 3

## Abstract
A big challenge in branch and bound lies in identifying the optimal node within the search tree from which to proceed. 
Current state-of-the-art selectors utilize either hand-crafted ensembles that automatically switch between naive sub-node selectors, or learned node selectors that rely on individual node data.
We propose a novel simulation technique that uses reinforcement learning (RL) while considering the entire tree state, rather than just isolated nodes.
To achieve this, we train a graph neural network that produces a probability distribution based on the path from the model's root to its ``to-be-selected'' leaves. Modelling node-selection as a probability distribution allows us to train the model using state-of-the-art RL techniques that capture both intrinsic node-quality and node-evaluation costs.
Our method induces a high quality node selection policy on a set of varied and complex problem sets, despite only being trained on specially designed, synthetic travelling salesmen problem (TSP) instances.
Using such a fixed pretrained policy shows significant improvements on several benchmarks in optimality gap reductions and per-node efficiency under strict time constraints.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a reinforcement learning framework to learning the node selection policy in branch-and-bound algorithm. In particular, the paper considers an environment based on SCIP. The considers a graph neural network on the branch-and-bound tree with root-to-leaf path aggregated scores as the policy net and employs policy gradient algorithms for training. The paper carefully generates TSP problems with moderate difficulty for training and evaluate the learned node selection policy on TSPLIB, UFLP, MINLPLib, MIPLIB. The results show that the learned node selection policy outperforms the default policy in SCIP in terms of Reward and Utility/Node.

### Strengths
* Most of the paper is well written and easy to understand for readers with basic knowledge in reinforcement learning and branch-and-bound.
* The root-to-leaf path aggregated score is a clever design. It avoids the computation challenge from the growing of the branch-and-bound tree by an intuitive assumption: if a node is good, so should be its ancestors.

### Weaknesses
 * The definition of the reward is not rigorously defined. Specifically, the paper does not disclose how are the gap(node selector) and gap(scip) are calibrated. It could be
    * The gap when reaches the time budget.
    * The gap at the same number of nodes n, with $\text{traj}(\text{node selector})[:n]$ rolled out with node selector, $\text{traj}(\text{scip})[:n]$ rolled out with scip, 
    * The gap at the same number of nodes n, with $\text{traj}(\text{node selector})[:n]$ and $\text{traj}(\text{scip})[:n-1]$ rolled out with node selector, $\text{traj}(\text{scip})[n-1:n]$ rolled out with scip.

* The score in evaluation need more justification. From my perspective, the most important goal of learning a node selection policy is finding good primal solutions. With this aim, none of the scores are a good choice. The second priority for a node selection policy is to close the duality gap. In this sense, "Utility/Nodes" is not good choices. The evaluation metric should directly reflect the quality of the primal solutions found and the achieved duality gap, rather than a normalized utility per node.

* The paper consider a small threshold 45 seconds. This is a relatively small time budget for solvers to solve MIP problems. To demonstrate the learned policy is practical, the results with a longer running time should be reported. The current time limit might not be sufficient to observe the long-term impact of the learned policy on the solution process, especially for more complex instances where the benefit of a good node selection policy might only become apparent after a longer period of exploration.

### Questions
* Only the results on benchmarks are provided in the paper. I am curious about the performance on the training data.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel method for node selection in branch-and-bound using reinforcement learning. The proposed method uses a graph neural network to model the node selection as a probability distribution considering the entire tree. Based on this, reinforcement learning is applied to perform node selection.

### Strengths
1. The paper clearly states the issue (node selection in branch-and-bound) trying to address, and the limitation of the conventional methods on that issue.
2. The paper provides the simulation results in a variety of problem instances.

### Weaknesses
1. There are existing related works that use graph neural networks for node selection in the branch-and-bound algorithm. The proposed method in this paper uses graph neural networks for tree representation, but the difference from the existing works is not clearly stated.
2. The structure of RL such as states, actions, and reward function is not rigorously defined in the paper. This makes it harder to understand how the RL method works in the proposed method.
3. As the branch-and-bound algorithm proceeds, the number of nodes and the tree structure keep changing. Then, should the RL agent be trained from the scratch for every step of the branch-and-bound algorithm?
4. The discussion on the learning cost of the RL algorithm is required. How is the cost due to collecting the enough experiences for the convergence of the RL policy?
5. It seems that the RL agent should be trained for each problem instance. Is this training of RL agent for each problem instance is mandatory to use the proposed method? If additional RL agent training is always required, it may not be practical to use it.
6. In the similar context, is there a possibility of using a pretrained RL agent that can be applied to a variety of problems? It would be helpful to demonstrate the generalization capabilities of the RL agent for more insight on the proposed method.
7. Comparison with related works using graph neural networks, in particular, Labassi et al. (2022) which is one of the state-of-the-art methods, seems to be necessary in experiments. The authors stated that it was unable to conduct experiments due to the version compatibility issue, but a comparison between the similar state-of-the-art methods is essential.

### Questions
Please refer to the weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper tackles the brand-and-bound problem, for which the authors propose a new method of simulation using RL for getting a more global view of the tree, augmented with heuristic node selection methods: tree encoding by GNN, features are learned by message passing and node selection is done by PPO. Experiments show positive results on many benchmarks despite the training being on TSP simulations. Another good thing is that code is provided (although I haven’t tested myself).

### Strengths
- The global view of trees is a strong motivation given the limitation of current methods in BnB. 
- I personally like the “greedy” aspect in reasoning (in introduction) that theory vs. practice has a gap, especially for many cases like the BnB and in practice, oftentimes we should favor a shorter-term choice over long-term ones if it’s good enough for many reasons. I think that is correct to the large spectrum of deep learning applications nowadays. 
- Positive results on many benchmarks. 
- Helpful supplemental contents.

### Weaknesses
 - The strong motivation leads to a much larger cost in carrying out the algorithm, especially when it involves recursion.. However, it’s not clear from the paper as to why the authors only choose the upper bound as a factor of choosing. Would be interesting if they have a study –of maybe a comparison–leading to that choice. 
- To solve this complex problem, the proposed method has to be broken down into many phases as shown in Section 2. That raises a question about the practicality: can the method be integrated as one to make it end-to-end. If not yet, what are the factors needed or what changes to enable that. 
- Another unclear aspect is the design of the reward method, e.g. why that formula in terms of motivation and explanation, and why not replace the term (“-1”) in Equation 5 with a constant C and study different values of it? 
- After the reward function, yet another unexplained technique of “shifting”, and another heuristics of clipping the reward. Is there any other better way of normalizing that or better design of the reward function to make sure that range complies while having a nice curve to the problem?
- Why PPO? Would also be nice if comparing PPO to alternatives such as maybe TRPO, SAC, …
- Yet another heuristics is to remove problems >100% or 0 gap. That begs a question on the quality of design including the reward function. 
- Overall, the paper gives an impression that despite a good motivation and a complex problem, it’s a collection of heuristic choices without substantiated evidence/studies supporting them. Such heuristics I think undermine the main motivation (i.e. ones might question how much contribution of RL in yielding the results you are getting?) It would be much more convincing if the authors address this aspect now or later. 

### Questions
- As also stated and shown, the problems are hard to handle computationally due to numerical instability. It is however not clear what problems they run into, and how the authors handle them. Those are very important for the community in terms of insights and reproducibility. 
- Table 3: The “Gap Ours” and “Gap Base” column have all normal values but the mean is NaN. Why? 
- See other questions in the Weaknesses section.

### Soundness
3 good

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
Authors propose a reinforcement learning algorithm for node selection problem in Branch-and-Bound (B&B) for Mixed Integer Programming. While prior work mostly focuses on ranking a pair of nodes, authors propose to use GNN to leverage information across the B&B tree. The policy induces a distribution across all open nodes in B&B tree. Authors propose Policy network and Value network architecture based on GNN. The proposed architecture is trained on TSP problems, and evaluated on both TSP and MIPLIB benchmark. The proposed method outperforms SCIP's default node selector across benchmarks considered.

### Strengths
Significance: Node Selection is instrumental for successful B&B. Prior research has been focused on Imitation Learning. This is limiting because when "expert" policy doesn't work well on problem at hand, ML-based method similarly struggles. Therefore, authors' Reinforcement Learning-based method has the potential of allowing ML-based node selection methods to be applied to a broader range of mixed integer programming problems with bigger, more practical improvements. Hence, I consider the potential significance to be high.

Originality: Given a related problem of Variable Selection has gone through a similar transition from Imitation Learning to Reinforcement Learning, the proposal of reinforcement learning method is not entirely unforeseen. However, authors make original contribution by proposing how to represent states of Markov Decision Process with GNNs.

### Weaknesses
Quality: Experimental setup of the paper could be improved more directly test the paper's key hypothesis: that 1) Reinforcement Learning provides an advantage over Imitation Learning, 2) considering the entire tree state is better than just considering isolated nodes. These are points which distinguish authors' work from prior work. Unfortunately, authors compare against only SCIP's default node selector, and previously proposed algorithms are not considered.

Also, authors use metrics and benchmark datasets not used in previous papers in this area of research. This makes difficult to interpret experimental results within the context of current research. In fact, many of the issues with metrics authors run into could be addressed with Primal/Dual/Gap Integral metrics https://www.ecole.ai/2021/ml4co-competition/ (see Metrics page), as these metrics would still be sensible when one algorithm can reduce the gap to be zero; since authors' metrics are not very well-defined when zero gap can be (nearly) reached, authors had to employ nontrivial preprocessing of data.

These two are major concerns. The contribution of the paper is mostly the proposal of an empirical method that improves upon prior work, and therefore it is important for experiments to be designed to measure the advantage of the proposed method upon prior art.

Clarity: The main ideas of the paper is clearly described and easy to follow. Some technical statements did not provide sufficient reasoning to justify, however. For example, in Section 4.3, it's argued: Assuming $P \neq NP$, it is unreasonable for the proposed algorithm to tackle provably hard instances. In practice, MIP solvers are often applied to problems which don't allow even good approximation guarantee, and therefore I wasn't sure why $P \neq NP$ would imply these problems to be not tractable.

### Questions
Is the reward (equation 5) only received at the end of the "episode" (end of the MIP solve)?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

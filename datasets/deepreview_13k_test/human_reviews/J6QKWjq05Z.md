# TreeDQN: Learning to minimize Branch-and-Bound tree

- Decision: Reject
- Scores: 5, 3, 3, 6

## Abstract
Combinatorial optimization problems require an exhaustive search to find the optimal solution. A convenient approach to solving combinatorial optimization tasks in the form of Mixed Integer Linear Programs is \emph{Branch-and-Bound}.  Branch-and-Bound solver splits a task into two parts dividing the domain of an integer variable, then it solves them recursively, producing a tree of nested sub-tasks. The efficiency of the solver depends on the \emph{branchning heuristic} used to select a variable for splitting. In the present work, we propose a reinforcement learning method that can efficiently learn the branching heuristic. We view the variable selection task as a tree Markov Decision Process, prove that the Bellman operator adapted for the tree Markov Decision Process is contracting in mean, and propose a modified learning objective for the reinforcement learning agent. Our agent requires less training data and produces smaller trees compared to previous reinforcement learning methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces TreeDQN, a reinforcement learning algorithm based on DQN for solving Tree MDPs. TreeDQN is trained on the mean squared logarithmic error loss. Specifically, the algorithm is used to learn branching heuristics for branch and bound in the context of mixed integer linear programming problems. 

Empirical results on a set of benchmark problems show some of the advantages of TreeDQN for the purpose of learning a branching heuristic. The results on unseen tasks are somewhat mixed, with some advantage to the branching heuristic learned with TreeDQN.

### Strengths
The paper presents an algorithm for solving Tree MDPs with the specific application to learning branching heuristics for branch and bound algorithms in the context of solving mixed integer linear programming problems. TreeDQN presents better results on some of the benchmark problems used in the paper.

### Weaknesses
The presentation is *possibly* the paper's weakest point. The lack of clarity makes me wonder about the value of the value of the contributions of the paper. The main contribution of the paper, TreeDQN, is explained in a single paragraph in the main text. Since the text only states that the algorithms is an adaptation of Double Dueling DQN, I assume TreeDQN is a straightforward adaption of DQN to Tree MDPs.

The paper builds on a couple of previous papers, which I had to skim over in order to understand the present paper. I am not entirely familiar with the line of work of using RL to learn how to branch and I can tell that the paper wasn't written for me. These are the two papers that helped me understand this submission:

Exact Combinatorial Optimization with Graph Convolutional Neural Networks 
and
Learning to Branch with Tree MDPs

The example on Mixed Integer Linear Programming isn't very helpful. The tree shown in Figure 1 is uninformative; it simply shows nodes in a tree where the color scheme differs the root of the inner nodes and from some of the leaf nodes. It would have been more helpful to not show a tree and give the reader a full example on how the branch and bound search works. I asked ChatGPT for an example and it gave me an example (without any drawings, of course) that was more helpful than the tree example shown in the paper. 

Overall the background section could be re-written to use less space and pack more information to help the reader understand the work.

I cannot understand the last paragraph of Section 2.2 without reading the paper by Scavuzzo et al. (2022). Here are the question I asked myself while reading that paragraph. 

1. Why do we need to use DFS as node selection or set the global upper bound in the root to the optimal solution cost to guarantee the Markov property? 
2. The gap between training and testing is due to assuming that one has the optimal solution in training? Why not use DFS and not assume that you have the optimal solution in training? 
3. How can more efficient heuristics for node selection also induce a gap between training and testing? And why is this important? 

Section 4 lists properties of a successful RL method for this problem, which includes off-policy and "work with tree MDP instead of temporal MDP". Why is it important to learn off-policy? We know of many successful on-policy algorithms for RL, what am I missing here? Why do they have to work with tree MDPs? 

The empirical setting is described in previous papers and the current paper relies on that. How is the training data generated? Do the problems differ in difficulty? Do we have to optimally solve the problem to attain the Markov property to then train the model? If so, how are the problems solved? Assuming that the training instances are easy (one needs to solve them optimally), how does the learned heuristic scale to larger problems? 

The number of seeds also seems to be small (5), for the kind of learning being done. 

Overall, it seems that the paper has some interesting ideas, but I don't fully understand them. The paper was written for people who already knows the details of this line of work, and it isn't friendly to newcomers to the point that the paper isn't self contained.

### Questions
I would like to hear clarifications on the empirical setup on how the training of the branching function is done, as I listed in the weaknesses section above.

### Soundness
2 fair

### Presentation
1 poor

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
The authors use the TreeMDP framework introduced by Scavuzzo et al. to study RL methods for improved variable selection/branching in branch-and-bound for integer programming with the ultimate goal being smaller search trees. They propose a more stable and sample efficient RL training procedure by choosing a loss function to minimize the geometric mean of tree size during training, and use a deep Q network for training rather than the REINFORCE method used by Scavuzzo et al.

### Strengths
Branching is a critical aspect of integer programming solvers, and the authors provide an interesting new contribution towards RL based methods for the design of branching rules. The new methods are shown to produce smaller branch-and-bound trees than previous RL based variable selection methods, making this work a promising advance in the “learning to branch” line of work.

### Weaknesses
Section 2.2 “Tree MDP” needs way more explanation. It more or less assumes familiarity with the Tree MDP work of Scavuzzo et al., and a more self-contained exposition would be very helpful.

The theoretical contribution is very hazy to me. Contraction in mean is not really well-motivated. Does the cited theorem (Jaakkola ‘93) apply to the setting of tree operators here? That seems like a nontrivial assumption that is missing justification. Rather than just including a theorem about contraction in mean, the authors should have a main theorem that states the actual convergence guarantee that follows.

My understanding is that this paper is methodologically very similar to Scavuzzo et al., and only differs in the mechanics of how the RL algorithm is trained. This is discussed in Sections 4.2 and 4.3. In Section 4.2, the main difference is that the authors use a loss function that appears to be selectively picked based on the objective of minimizing the geometric mean of the tree sizes during training/testing. This to me feels like a specific and brittle design choice.

The new method is shown to yield smaller branch-and-bound trees than previous RL based variable selection policies, but no comparison is made to the default settings of any state-of-the-art solver (e.g., Gurobi, CPLEX, SCIP). This is an important comparison that should be included.

Overall the presentation did not convince me that this is a sufficiently novel contribution for ICLR. It seems like the authors just slightly tweaked some aspects of the methodology of Scavuzzo et al. It’s great that these modifications work and yield promising experimental results, but I just did not find the current writeup to be a sufficiently original contribution. The writeup itself also needs quite a bit of work to make it a cohesive, readable, and self-contained (the theory is presented in a very ad-hoc manner without formal definitions) contribution.

### Questions
“In the B&B search trees, the local decisions impact previously opened leaves via fathoming due to global upper-bound pruning. Thus the credit assignment in the B&B is biased upward, which renders the learned policies potentially sub-optimal.” I understand the first sentence, but what does the second sentence mean? What is “credit assignment”, and why is it/what does it mean for it to be biased upward?

See also questions in the “weaknesses” section.

### Soundness
2 fair

### Presentation
2 fair

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
This work studies the variable selection problem in the branch-and-bound algorithm from the point of view of Tree-MDPs, which, instead of the “linear” time-axis present in ordinary markov decision processes, models the decision history as a binary tree.
They show that under mild assumptions tree-MDPs allow for a contractive Bellman operator, justifying a Tree-MDP version of deep q-learning dubbed TreeDQN. Finally, the authors demonstrate their performance against the “strong branching” baseline and other learnt variable selectors on a large set of synthetic instances.

### Strengths
Inherently, the idea of modelling variable selection as a Tree-MDP is a great idea as it allows the incorporation of the branch-and-bound structure into the decision process. The modification of the loss function to stably regress towards the geometric mean is also clever and might prove useful even outside the learnt variable selection domain. In general, the presentation of the work is clean and easy to read.

### Weaknesses
1. Perhaps the biggest limitation is the assumption that the upper bound has to be derivable from the current node or known ahead of time. The authors assert that this (as well as more intricate node selection policies) lead to at most a moderate distribution shift, but never demonstrate this effect.
2. Another concern is regarding the difficulty distribution of instances. Random instance generation has been known to generate significant amounts of trivial instances compared to real-world equivalents. However, this is a limitation of most prior work on learnt variable selection rules as well.
3. TreeDQN is also more expensive in terms of wall-clock-time than prior work (especially the IL agent), which can be seen in Figure 4. The paper does not make it clear whether this is due to TreeDQN using a different architecture, or TreeDQN simply creating more expensive nodes during branching.
4. An important missing baseline in their comparisons is out-of-the-box SCIP, acting as an automatic state-of-the-art hand-crafted tradeoff between SB and cheaper heuristics.


The paper needs an extensive re-write in terms of argumentation and clarity.


Some more points:
- Abstract: BnB solver[s] split a task…
- Abstract: …the Bellman operator adapted for the tree MDP is contracting in mean… - initially I did not understand what you mean with that (only at some later point into the paper)
- Intro: with [the] Branch-and-Bound algorithm (B&B). |[The] B&B algorithm employs…
- “The variable selection process is the most computationally expensive and crucial for the performance of the whole algorithm” – is there a reference to prove this? If not, omit this sentence
- Intro: “problematic”  challenging
- Intro: “single next state [the] agent”
- Intro: the contribution list at the end of the section looks like a draft and comes out of nothing
- Sec. 2: where objective… sentence broken
- Sec. 2: B&B [-algorithm-] builds
- Sec. 2: explain “relaxed”
- Sec. 2: Fig. 1 does not bring much to the table. I suggest to explain B&B with Fig. 1 right from the beginning (add primal/dual, relaxation, variables). This does not cost more space but helps to understand B&B
- Sec. 2.: [A] straight forward strategy
- Sec. 2.: [The] tree MDP was proposed by … In the tree MDP [the] value…
- Sec. 2.: The variable selection process … this paragraph is hard to understand
- Sec. 3.: “Our work improves…” please add some (technical) argument why this is the case
- Sec. 4.0: this part takes much space and can be omitted imho. Instead focus on explaining the bullet-point list at the end of 4.0 in more detail. Why must a successful RL method should have off-policy as a property? Policy gradient methods are great, and they are on-policy… Here are a lot of arguments that need more justification.
- Sec. 4.1 [E]quation3, [E]quation 4
- Sec. 4.1 is not satisfying to me. The section and with an inequality and tells me that the proof follows from the fact that the tree is finite. Please work out this prove in more detail.
- Sec. 4.2 the loss function [from E]quation 5
- Sec. 4.3 we use loss function equation 5 – please re-write
- Fig. 3 put the description into the plots

### Questions
- Is the method run on CPU or GPU?
- What is the performance of SCIP with default parameters on these instances (I.e. reliability pseudocost branching)?
- What is the model architecture (or more importantly: is it the same for all methods)?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper extended the on-policy learning to branch method introduced by Scavuzzo et al. in 2022 to an off-policy setting by offering a proof of contraction in mean, a modified mean squared logarithmic error, and an adapted Double Dueling DQN scheme.

### Strengths
1. The evaluation experiments demonstrate a noteworthy improvement compared to previous work and other state-of-the-art approaches.
    
2. The modified mean squared logarithmic error proves to be well-suited for long-tailed distributions of BB tree sizes and exhibits superior performance compared to the mean squared error in the ablation study.

### Weaknesses
My main concerns about this paper are generalization ability, scalability, and some basic assumptions. Please find details in the questions.

### Questions
1. Regarding the Assumption in Theorem 4.1: The paper assumes that the probability of having left and right children does not depend on the state because the pruning decision depends on the global upper bound instead of the parent node. However, the global upper bound can change dynamically during the search, which might influence the probability. Does this paper use optimal solutions as upper bounds? Could the authors provide further clarification on this assumption?
    
2. Exploring Limited Generalization Ability: In comparing the results presented in Table 5 and Table 3, it is observed that TreeDQN appears to exhibit less stability in the context of transfer tasks. Could you please offer insights or explanations regarding this phenomenon?
    
3. A Traditional vs. RL-based Variable Selection Perspective: Traditional variable selection methods rely on human-designed criteria, such as pseudocosts. One advantage of these traditional approach is its applicability to various problem types. On the other hand, current RL-based methods require training an optimal policy for each specific problem. Given the noted limitations in generalization ability, RL methods seem to necessitate training on problem instances of a similar size as the target problems. Could you provide any comments or insights on the potential implications of this limitation? (This question is optional, and your input is welcomed purely out of curiosity.)

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

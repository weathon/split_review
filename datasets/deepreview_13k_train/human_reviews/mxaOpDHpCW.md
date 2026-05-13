# Breadth First Exploration in Grid-based Reinforcement Learning

- Decision: Reject
- Scores: 6, 5, 5, 5

## Abstract
Recently, graph-based planners have gained significant attention for goal-conditioned reinforcement learning (RL), where they construct a graph that represents confident transitions between "subgoals'' as edges and run shortest path algorithms to exploit the confident edges. Such a graph construction consists of only achieved subgoals while recording unattained ones in history is also crucial. Indeed, it often wastes an excessive number of attempts to unattainable subgoals.
To alleviate this issue, we propose a graph construction method that efficiently manages all the achieved and unattained subgoals on a grid graph adaptively discretizing the goal space. This enables a breadth-first exploration strategy, grounded in local adaptive grid refinement,
that prioritizes broad probing of subgoals on a coarse grid over meticulous one on a dense grid. We empirically verify the effectiveness of our method through extensive experiments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents an approach for constructing a graph to augment current graph-based planners for goal-conditioned RL, specifically, using a grid that matches the dimension of the goal space and running a shortest path algorithm on the grid graph. In addition, a local adaptive grid refinement and goal shifting are proposed to appropriately choose grid interval and explore unattempted nodes, respectively. Experiments were performed in a number of different tasks in MuJoCo environments and results were compared with state-of-the-art approaches.

### Strengths
- The paper addresses a practical subproblem present in current graph-based planners for goal-conditioned RL, that is of wasting attempts to unattainable subgoals.

- The proposed approach is technically sound with the use of a grid and running of shortest path algorithm, and the addition of the grid refinement and goal shifting.

- The experiments include a comprehensive analysis with comparison with other state-of-the-art methods included in the appendix, as well as ablation studies, showing positive results.

- The presentation is clear with a logical structure in introducing the different concepts.

### Weaknesses
 - while grid is a way to have a systematic representation of the space, there are other approaches in planning that are present in the literature, including sampling-based approaches that can address similar problems. It is worth discussing the rationale behind choosing grid, as that is not necessarily the primary choice for high-dimensional spaces (which the paper mentions to leave it for the future).

- As Reacher3D is the scenario where results are fairly close, goals could be set at different locations to report the coverage too, unless there is a specific reason not to have different goals also for Reacher3D.

Some minor comments on presentation:
- "embarassing" can be substituted with "a very low performance" to be more formal and technical, rather than introducing a subjective judgement.
- "we propose graph planning method dealing with the above problem in Section 4" -> "we propose graph planning method dealing with the above problem in Section 4."
- please ensure that all symbols are introduced, i.e., before Eq. (2), worth mentioning " ... edge weights w_{i,j} for nodes v_i, v_j as follows". Also the symbol for the nodes set should be introduced, when the graph is introduced. 
- "The coverage is the averaged success rate of uniformly sampled goals, in which we sample 10 goals per unit-size cell over the
entire goal space to make the sampling more uniform. The coverage represents the average success rate for the entire goal" The two sentences are including redundant information, so they could be merged.
- "Bottleneck-maze where challenging for BEAG" -> "Bottleneck-maze which was challenging for BEAG"
- in Fig. 8, worth changing the max value on the y axis, so that the success rate is completely visible for the bottom row.

### Questions
Please  see the first two points included in the Weaknesses box.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates the issue of inefficient exploration of graph-based methods used in goal-conditioned reinforcement learning. The authors claim that the existing research tends to record achieved goals but overlook the unattained goals, which makes the algorithms struggle to get rid of repeatedly exploring these goals and causing waste. The main idea proposed in this paper is to leverage breadth-first exploration and multi-scale graph-construction to manage achieved and unattained goals.

### Strengths
- The paper concentrates on an important and challenging problem of goal-exploration in GRL, which has not been well studied in the literature. 
- At least from the lens of writing, the authors propose a simple yet effective solution incorporating a forward-looking perspective and a proxy model for value estimation. 
- This paper is easy to follow.

### Weaknesses
 - As admitted by the authors, the proposed method heavily relies on the task structure (distance-based, discrete) to apply the graph construction to record the achieved and unattained goals. 
- The comparative baselines are limited on some environments. Only DHRL is involved. Since RL algorithms often perform high-performance variance in different environments/tasks, I think it is necessary to make comparisons with more baselines. And also, I think it would be better if the authors make comparisons on different environments. 
- The authors did not provide clear explanations or intuitions for some of the design choices, such as why we use Euler-distance instead of others as the $w_{i,j}$. 
- The illustration in Algorithm tables is unclear (e.g., some notations lack explanation), so it is hard to and even cannot follow that. 
- It is unclear how the edge weights work for the proposed method.
- The success rate plots in Figures 4-6, and 8 show values exceeding 1 and falling below 0, which is not possible for a success rate, indicating a potential issue with the data processing or plotting method.

### Questions
- Why does the comparison in Figures 4-6 not include the other baselines introduced in the Appendix? 
- Why does the coverage in Figure 7 decrease? 
- Why does the success rate in Figure 4(d) higher than 1? 
- Why does the learning curve in Figure 8(a) not start from 0 environment step?

### Soundness
2 fair

### Presentation
1 poor

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
This paper proposes a method which builds grid-level graphs for better sample efficiency in subgoal HRL. When building the graph, instead of estimating weights from the Q-function. The authors set edge weights using temporal distance based on the number of successful node visits. The method is also adaptive, which means the graph can fit different grained levels while planning in complex environments.

### Strengths
This work has a good motivation: to address the drawbacks of current methods in subgoal-finding process. Some key issues, such as the novelty of subgoals, the accessibility of these subgoals, and sample efficiency, are considered.

The design of experiments clearly shows the sample efficiency of BERG over DHRL.

### Weaknesses
1. Experiments are not enough. The authors only compared their work with DHRL, while there exists many other graph-based HRL methods that are worth to compare with, such as HIRO, HAC, ... The effect of threshold hyperparameters are not shown. Also, the ablation study can focus on more aspects of BERG.

2. The method is a minor upgrade of existing Graph-based methods. Although pure empirical evidence can show the effectiveness of the method, I am expecting to see some more theoretical analysis on why it may work.

### Questions
1. Could the authors try some other baseline HRL benchmarks to further show the advantage of the proposed method?

2. I would like to see more experiments on failure condition and count thresholds.

### Soundness
2 fair

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
The paper introduces an algorithm for hierarchical planning. To plan the solution, the goal space is divided into a grid, and the shortest path is computed. During training, the reachability statistics for the visited edges are collected, and the graph is updated to reflect which transitions are achievable and which are not. This way, both exploration and the final quality of solutions benefit.

### Strengths
As far as I understand, the main idea is simple yet effective, especially in environments with complex dynamics but simple goal space, such as various ant-mazes. Because the planning is done by searching on a graph, it can deal even with an arbitrarily long horizon.

### Weaknesses
The description of the algorithm itself needs to be stated more clearly. How exactly do you collect the training data? Do you always choose the shortest path (according to the current state of the graph)? When do you switch subgoals? Do you have to replan at some point? It could be handled by either adding a small section that brings all the pieces in one place and describes the algorithm step-by-step or by adding a pseudocode. Without that, it is hard to understand your approach.

Since your edges have different lengths, I suppose that you use Dijkstra to find the shortest path, instead of BFS as you claim.

I agree that you show a clear advantage over DHRL, although the final difference is not very large. I suggest evaluating the algorithm on even harder instances to further highlight your superiority. Perhaps instances with a lot of blockers would do since you claim dealing with it to be one of your key strengths. How far can you push it, even in a toy environment?

The _Ablation study_ section seems a little ad-hoc. I suggest extending it or merging it with other experiments.

### Questions
How exactly do you collect the training data? Do you always choose the shortest path (according to the current state of the graph)? When do you switch subgoals? Do you have to replan at some point?

Do you ever remove edges from the graph, or is it simply enough to assign them $\infty$ weight?

How do you handle the initial stage of the training, when the agent has to learn the basics, e.g. how to move? In particular, I'm afraid that initially the agent will be unable to reach _any_ subgoal (barely move), which should result in labelling many goals close to the initial state as _unreachable_. This is not entirely destructive, since even if all the subgoals adjacent to the starting positions have a weight of $\infty$, the path will go through one of them anyway. However, this initial struggle may considerably bias the graph structure, which may affect further shortest paths (that will try to avoid the falsely failed areas). Is that indeed an issue and how do you handle it?

Also, apart from the initial bias, if any edge is marked with $\infty$ (possibly due to underfitting in a yet underexplored area), is there _any_ way of including it back to the graph?

Is it of any importance that you use a grid? I suppose it can be an arbitrary structure, like random samples. Does using the grid has advantages? It seems a little rigid.

During planning, you always select the shortest path to the goal in the graph. Does it mean that the agent is committed to this rigid grid-like movement, even if it could move diagonally? Do you see a way to adjust the structure of the graph to eventually allow for near-optimal trajectories? At least, trajectories without considerable inefficiencies?

It seems to me that this approach is useful if the goal space is low-dimensional. For instance, in 2 dimensions, like ant-maze, it is pretty efficient. However, if we consider any more complex spaces, e.g. ant-maze with the goal space equal to the observation space (which is quite natural in many scenarios), will it still work?

If the goal space is reduced, then the reachability of adjacent subgoals depends on the state in which the agent reaches each point, e.g. the exact position of its limbs. In particular, it may depend on the path that it took. How do you handle that?

In general, **I really like the high-level idea**, but in its current form, it is very hard to understand the essential details. Thus, I'm willing to increase my rating if my concerns are addressed.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

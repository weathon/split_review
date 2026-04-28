# Dantzig-Wolfe Decomposition and Deep Reinforcement Learning

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3

## Abstract
The 3D bin packing problem is an NP-hard optimisation problem. RL solutions found in the literature tackle simplified versions of the full problem due to its large action space and long episode lengths. This work uses a Danzig-Wolfe formulation to decompose the full problem into a set partition and 3D knapsack problem. The RL agent is used to solve the 3D knapsack problem and CPLEX (a mixed integer linear programming solver) is used to solve the set partition problem. This removes the bin selection action from the action space of the agent and reduces the episode length to be only the number of items required to fill 1 bin rather than all items in the inference. We thereby simplify the learning problem compared to the full 3D bin-packing case. The trained agent is used at inference time to iteratively generate columns of the Danzig-Wolfe formulation using the column generation procedure. This algorithm provided improved solutions on up to 28/47 instances compared to those obtained by successively applying the RL agent to optimize volume occupation in a bin with the remaining items.

RL solutions alone cannot provide valid lower bounds for solutions. This work also uses the Danzig-Wolfe formulation and column generation to improve on existing SOTA lower bounds by replacing the RL agent with an integer linear program for the 3D knapsack problem. An improved lower bound compared to SOTA was found on 17/47 instances by using CPLEX to solve both master and sub-problems.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes an integration of deep reinforcement learning (RL) in a Dantzig-Wolfe decomposition method to solve the 3D bin packing problem. The idea is to replace the solution of the subproblem in the Dantzig-Wolfe decomposition by an RL agent.

### Strengths
The combination of deep reinforcement learning with Dantzig-Wolfe decomposition is novel as far as I know.

The authors obtained some novel lower bounds for some instances of the 3D bin packing problem.

Promising results are obtained on a dataset of 47 instances.

### Weaknesses
Although the combination is novel, the novelty in the machine learning part seems to be limited.

It seems that some important information is missing in the presentation such as:
- what are "normal patterns"?
- the architecture of the deep RL agent
- the training methodology of the RL agent
- the sequential RL agent should be explained more explicitly

The formatting in the paper has many issues. For instance:
a2c -> A2C
Bonnet et al. (2023) -> (Bonnet et al., 2023)
Zhang et al. (2021) is limited -> The method proposed by Zhang et al. (2021) is limited
Fang J (2023) -> Fang and Rao (2023) 
The names in the citation "Deidson Vitorio Kurpel" should be fixed.
(1-5) and (6-10) should be better indented
Jumanji bin pack -> Jumanji binpack
"Where v_i represents" this sentence should be one sentence with the previous one.
What is a "liquid volume"?

### Questions
What architecture did you use for your RL agent?

How did you train it? Which RL algorithm did you use?

Could you include in Table 1 the aggregated results for the other SOTA methods so that it is easier to understand how well the proposed methodology performs?

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This article delves into the fusion of Danzig-Wolfe Reformulation with the Column Generation (CG) algorithm to address the 3D bin packing problem.

### Strengths
Strengths:

1. The paper introduces the integration of Reinforcement Learning (RL) with traditional mathematical programming methods to tackle the three-dimensional bin packing problem. This approach seems feasible.

2. By employing a combination of the Column Generation algorithm and RL algorithm to solve the packing problem, promising results were achieved. The use of the CG algorithm improved the lower bound of the original solution, offering a tighter lower bound.

### Weaknesses
Weaknesses:

1. The methods of Danzig-Wolfe Reformulation and Column Generation are existing approaches. The authors did not contribute significantly by improving these methods or specifically addressing the bin packing problem, rendering the contribution somewhat lacking.

2. Section 2.1, the core of the authors' method, is hard to comprehend. It is necessary to incorporate some illustrations and motivation to enhance readability.

3. The author's comparison with baseline methods is limited. They used a dataset introduced in 1988, which is quite outdated. They should consider recent methods like 'Attend2pack: Bin packing through deep reinforcement learning with attention' and new datasets (BED-BPP: Benchmarking dataset for robotic bin packing problems, Learning Efficient Online 3D Bin Packing on Packing Configuration Trees) to compare their proposed method in terms of time cost and performance.

### Questions
There is an issue of local optimal solutions when employing the RL algorithm to solve subproblems. Therefore, after the author decomposes the full problem into a set partition, how can they ensure that RL will inevitably find a solution?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The bin packing problem becomes even more complex when it involves multidimensional items and additional industrial constraints. While exact optimization methods exist for cuboid bin packing, they struggle with scalability and often neglect certain constraints, such as item rotation and stability. The paper proposes a column generation algorithm using the Danzig-Wolfe decomposition approach that incorporates both exact solvers and RL agents, offering improved lower bounds and more efficient solutions for the full 3D bin packing problem. The restricted master problem is solved by RL.

### Strengths
Multidimensional bin packing has not received enough attention and thus the choice of the topic is adequate. Capturing of complex side constraints is without doubt an important practical aspect.

### Weaknesses
The main weakness is the lack of contributions. For decades we know how to formulate standard bin packing by using DW and how to conduct column generation. It is also acceptable for a long time that the pricing problem can be solved as a relative simple IP or by RL (after all knapsack is sometimes solved as RL and the knapsack problem is the pricing problem in standard bin packing). I do not find anything innovative on the algorithm side in the paper. Apply RL in pricing in their specific context (multidimensional bin-packing) does not yield any novel contributions. The paper does not adequately address the computational challenges of solving the 3D bin packing problem with column generation. While the authors mention that IP solutions for the 3D pricing problem are slow, they do not provide a detailed analysis of the computational bottlenecks or how their RL approach specifically overcomes these issues beyond the fact that heuristics are often problem specific. The paper also lacks a rigorous comparison to existing state-of-the-art column generation methods for 3D bin packing, which would be necessary to demonstrate the practical advantages of their approach. The claim that existing RL solutions have not been tested on multiple bin problems is not sufficiently justified, as there are many ways to extend RL approaches to handle multiple bins, and the paper does not demonstrate that these extensions are not viable or that the proposed approach is superior to these extensions. The paper also fails to address the well-known issue of the lack of guarantees on the quality of the solution when using RL in the pricing problem, which is a significant limitation for practical applications where optimality is important.

### Questions
Why did you use Cplex instead of Gurobi (which is now considered more efficient than Cplex - both have free licenses for academia)?
Column generation is known to have stability issues. There are known stabilization techniques. I wonder why they have not been tried. 
Branch-and-price is a well established and in many cases the most effective algorithm for solving such problems (it combines branch-and-bound with column generation). Why is this methodology not being used as a benchmark?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

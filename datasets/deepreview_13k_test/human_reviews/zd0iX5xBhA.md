# System 1.x: Learning to Balance Fast and Slow Planning with Language Models

- Decision: Accept
- Scores: 5, 6, 3, 1

## Abstract
Language models can be used to solve long-horizon planning problems in two distinct modes. In a \emph{fast} `\sysoneshort{}' mode, models directly generate plans without any explicit search or backtracking, and in a \emph{slow} `\systwoshort{}' mode, they plan step-by-step by explicitly searching over possible actions. While \systwoshort{} planning is typically more effective, it is also more computationally expensive, often making it infeasible for long plans or large action spaces. Moreover, isolated \sysoneshort{} or \systwoshort{} planning ignores the user's end goals and constraints (e.g., token budget), failing to provide ways for the user to control their behavior. To this end, we propose the \emph{\method{}}, a controllable planning framework with language models that is capable of generating hybrid plans and balancing between the two planning modes based on the difficulty of the problem at hand. \methodshort{} consists of (i) a controller, (ii) a \sysone{}, and (iii) a \systwo{}. Based on a user-specified hybridization factor $x$ governing the degree to which the system uses \sysoneshort{} vs. \systwoshort{}, the controller decomposes a planning problem into sub-goals, and classifies them as easy or hard to be solved by either \sysoneshort{} or \systwoshort{}, respectively. We fine-tune all three components on top of a single base LLM, requiring only search traces as supervision. Experiments with two diverse planning tasks -- Maze Navigation and Blocksworld -- show that our \method{} outperforms a \sysone{}, a \systwo{} trained to approximate \astar{} search, and also a symbolic planner (\astar{} search), given an exploration budget. We also demonstrate the following key properties of our planner: (1) \emph{controllability}: by adjusting the hybridization factor $x$ (e.g., System-$1.75$ vs. System-$1.5$) we can perform more (or less) search, improving performance, (2) \emph{flexibility}: by building a neuro-symbolic variant composed of a neural \sysoneshort{} planner and a symbolic \systwoshort{} planner, we can take advantage of existing symbolic methods, and (3) \emph{generalizability}: by learning from different search algorithms (BFS, DFS, A$^*$), we show that our method is robust to the choice of search algorithm used for training.x}}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work proposes a hybrid planning system that combines a large language model (LLM) fine-tuned to act as either a System-1 or System-2 planner, with a Controller that decomposes tasks into sub-goals based on difficulty. The Controller generates a meta-plan by assigning "easy" sub-goals to System-1 for faster solutions and "hard" sub-goals to System-2 for more deliberate, search-based solutions. The final plan is constructed by concatenating sub-plans from both systems. However, it faces limitations due to compounding errors across systems, particularly as task complexity grows.

### Strengths
An innovative feature of this hybrid approach, which combines quick solutions from System-1 with thorough search-based solutions from System-2, is a user-controlled parameter x (between 0 and 1) that adjusts how much System-2 is used compared to System-1. This allows users to balance speed and accuracy based on the task’s needs.

### Weaknesses
1. A significant limitation of this approach is its dependency on multiple components performing flawlessly: System-1 must solve the easy sub-goals without hallucinating, System-2 must solve the harder sub-goals using search trajectories accurately, and the Controller must correctly decompose and assign tasks between the two systems. This compounded reliance on error-free performance from each component raises concerns about the approach’s reliability, especially as problem complexity increases. For even moderately difficult tasks, or as the number of objects scales, this method may struggle to maintain effectiveness, as errors are likely to accumulate across the system.
2. A limitation of this hybrid approach is that selecting the x value too greedily can hurt performance and increase training computation costs. Meanwhile, setting x too high leads to more thorough searches by System-2, which increases compute requirements and makes the approach similar to existing methods like fine-tuning LLMs for planning or SOFAI architectures [1].
3. For System-2, the hardness function should be explicitly defined for each specific domain in which the planner operates. Without domain-specific definitions, the hardness function risks being too generalized, leading to inaccurate difficulty assessments that don’t align with the unique challenges of each task.

### Questions
1. The term plan validity should not be used interchangeably with plan accuracy. Validity is a binary concept that indicates whether a plan meets all required conditions or constraints (i.e., valid or invalid), whereas accuracy implies a measure of correctness or closeness to an ideal solution, which can vary in degree.
2. The definition of a sub-goal as a "pair of states" adds unnecessary complexity and deviates from the usual understanding. Sub-goals are typically single intermediate states that help guide progress toward the final goal.
3. The hardness function defined for Blocksworld, in Section A.3, seems wrong. It states that if a block is not on the table and not in its goal position, an additional 1 is added to the hardness cost. However, this approach doesn't account for scenarios where a block is in the air after a pick-up action—this intermediate position may not be the goal but could be one step away from it. Adding to the hardness cost in such cases could mistakenly label states as more challenging, even when they are actually closer to the goal. Similarly for the Maze Navigation task, counting all obstacles in the sub-maze as part of the hardness cost is problematic, as obstacles outside the plan trajectory can inflate the difficulty inaccurately.
4. In Section 2.3, under Controller Training Data, Step 3, it’s unclear why only a contiguous chunk should be assigned to System-2. What is the rationale for restricting it to contiguous data?
5. According to the authors' definition of sub-goals, are they explicitly training the Controller to decompose the task into exactly three sub-goals?

**Minor Comments:**
1. Examples in the figures, particularly Figure 2, would benefit from clearer annotations in the maze to improve the interpretation of the numbering. The current numbering follows a top-to-bottom, left-to-right order, but this is not immediately clear.
2. In Figure 2, System-2 output, I do not understand why this is invalid “Exploring action left State [3, 1] is invalid”?
3. The authors should maintain consistency in their notation. In Section 2.3, when discussing Controller training data, the notation for initial and goal states switches from $s_i$​ and $s_j$​ in Step 1 to $s_0$​ and $s_g$​ later in the paragraph.


**References:**

[1] Fabiano, F., Pallagani, V., Ganapini, M.B., Horesh, L., Loreggia, A., Murugesan, K., Rossi, F. and Srivastava, B., 2023, December. Plan-SOFAI: A Neuro-Symbolic Planning Architecture. In Neuro-Symbolic Learning and Reasoning in the era of Large Language Models.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces System-1.x which acts as a hybrid System 1 / System 2 planner that outperforms fully System 1 and 2 systems, an A* planner, and a System-1.x variant without subgoal decomposition. This paper contributes a method for collecting data to train a System-1.x system through the introduction of domain-specific hardness functions to determine which of the collected samples should be annotated for System-1 (easy samples) or System-2 (hard samples).

### Strengths
$Originality:$ This paper introduces a new method to collect data to finetune a hybrid System 1/2 system whose hybridization factor x can be customized during train and test time.

$Quality:$ The figures and methodology are well-done and the experiments cover relevant baselines and ablations.

$Clarity:$ The paper is well-written and clear.

$Significance:$ Constructing LLM planners that can outperform classical planning approaches with minimal exploration is very important in domains where querying the world model can be expensive (e.g. real world systems like robotics).

### Weaknesses
The introduction makes the following claim

"System-1.x is a fully LLM-based neural planner ... not relying on any external solvers or verifiers... it has an advantage over inference-time methods that rely on symbolic planners which may not exist for certain domains."

However, System-1.x strongly rely on the presence of a hardness function, which is essentially a heuristic function. This assumption is too strong and cannot simply be listed as a limitation of this approach; the domains that are tested on could be purely solved using classical planners like A* with access to the hardness (heuristic) function and a valid plan would be retrieved (regardless of consistency or admissibility of the hardness function) much faster than any LLM approach in terms of inference time.

To improve this paper, evaluating on environments where classical planners cannot be trivially applied would give more credibility to this LLM approach. A user-specified hardness function cannot be provided for the environment since a classical planner would be able to utilize this along with the other environment information provided to the System-1.x planner and quickly find a valid plan. 

One potential idea is utilizing an LLM to provide a hardness value for a pair of states as other works have done, using an LLM to approximate a heuristic function [1,2,3]. This would require some new experiments to show the effectiveness of the hardness function and would necessitate a new approach other than the sliding window mechanism to be token-efficient.

This is a very important problem to solve in this space and I wish the authors the best of luck.

[1] Large Language Models as Commonsense Knowledge for Large-Scale Task Planning (Zhao et. al 2023)

[2] Reasoning with Language Model is Planning with World Model (Hao et. al 2023)

[3] Toolchain*: Efficient Action Space Navigation in Large Language Models with A* Search (Zhuang et. al 2023)

### Questions
- You make the case that System-1.x is advantageous over inference-time methods relying on symbolic planners since they may not exist for certain domains, yet System-1.x relies on defining a hardness function, which is essentially a heuristic function. How could System-1.x be leveraged in new domains where a user is not a domain expert?
- In addition, it is non-trivial to construct hardness functions for multi-task domains like Alfworld [1], Robotouille [2] or Mini-BEHAVIOR [3]. How would System-1.x be applied to such domains?
- There appears to be a tradeoff in Figure 3 with accuracy and states explored with Sys-1.5 with and without subgoals. Sys-1.5 with subgoals achieves higher performance with less states explored but as the state exploration budget increases, no subgoals is better. Why is that?

[1] Alfworld: Aligning text and embodied environments for interactive learning (Shridhar et. al 2020)

[2] Demo2Code: From Summarizing Demonstrations to Synthesizing Code via Extended Chain-of-Thought (Wang et. al 2023)

[3] Mini-BEHAVIOR: A Procedurally Generated Benchmark for Long-horizon Decision-Making in Embodied AI (Jin et. al 2023)

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes System-1.x, a hybrid planning framework using language models to balance fast, intuitive System-1 planning with deliberate, accurate System-2 planning.

### Strengths
System-1.x shows robust adaptability and performance across different planning tasks (e.g., Maze Navigation, Blocksworld), outperforming both purely System-1 and System-2 planners due to its effective sub-goal decomposition.

### Weaknesses
The related work section of the paper does not cover papers similar to this work. To cite a few papers that should have been used as baselines to compare System 1.x against - 
[1] Katz, M., Kokel, H., Srinivas, K., & Sohrabi, S. (2024). Thought of Search: Planning with Language Models Through The Lens of Efficiency. In The First Workshop on System-2 Reasoning at Scale, NeurIPS'24.
[2] Fabiano, F., Pallagani, V., Ganapini, M. B., Horesh, L., Loreggia, A., Murugesan, K., ... & Srivastava, B. (2023, December). Plan-SOFAI: A Neuro-Symbolic Planning Architecture. In Neuro-Symbolic Learning and Reasoning in the era of Large Language Models.
[3] Webb, T., Mondal, S. S., Wang, C., Krabach, B., & Momennejad, I. (2023). A Prefrontal Cortex-inspired Architecture for Planning in Large Language Models. arXiv preprint arXiv:2310.00194.
Refer to the questions for more weaknesses.

### Questions
1. In the experimental setup, the authors mention that the hybridization factor x allows System-1.x to control the degree of System-1 versus System-2 planning. How sensitive is this hybridization factor to changes in task complexity? Were there significant trade-offs observed with larger values of x in different domains?
2. In discussing Blocksworld’s out-of-distribution generalization, the paper mentions that System-1.x effectively utilizes System-1 for ID sub-goals while reserving System-2 for OOD sub-goals. Could the authors explain how the controller identifies which sub-goals are in-distribution vs. out-of-distribution during inference?
3. The authors claim that System-1.x can match or exceed a purely System-2 Planner’s accuracy with fewer states explored. What specific methods were used to prevent overfitting to the training traces, especially for tasks requiring extensive state exploration?
4. Why is there no baseline comparison against other fast and slow architectures used for solving planning problems? It is not clear to me what is the advantage of using this approach against architectures like Plan-SOFAI that are both optimal and resource-efficient compared to System 2 solvers for planning tasks.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper attempts to create a mixed-mode planning system that both immediately generates plans without deliberate state-space search, and does deliberate state space search.

However, this paper seems deliberately misleading in terms of what it claims, namely the improvements over A*.

### Strengths
In general, the goal of creating a neurosymbolic planning system is a very good one. However, the one presented in this paper is preliminary. 

I really like the idea of having a hybridization factor. It could be interesting to have a way to control this at inference time rather than at training time, i.e. like iterative-deeping based searches use more search budget when given more time.

### Weaknesses
While this work attempts to build a neurosymbolic planning system, which is a good goal, it seems like the work may not be ready for publication at ICLR. 

The main results of the paper rest on a claim about the "States explored" metric, however, there are several issues with this evaluation. Primarily, computational costs of querying LLMs are not accounted for. A single pass of an LLM clearly can do a significant amount of computation. Furthermore, intermediate LLM-generated states are never checked, e.g. they could contain hallucinations, so it doesn't seem like they'd make a reasonable metric. More importantly there is simply no guaranteed correspondence between intermediate states inside of A* and reported intermediates produced by an LLM to the degree that the two can be compared meaningfully. Because of this, it is unreasonable to restrict A* to run in correspondence with the LLM output, when a full A* computation may several orders of magnitude less than a computational single pass of an LLM. Since the paper rests on the states explored metric, I highly encourage the authors to propose a better method for comparing computational costs between LLMs and A*. 

Another ommission is the fact the the overall system is trained by calling A* thousands of times, which makes an efficiency argument extremely questionable. Regardless of the current state of such an argument, I do buy into the general idea that mixed-system planning algorithm could be more efficient than a system-2 one and more accurate than a system-1 one, but I think the authors would need to fairly evaluate this to make progress on building such an algorithm.

The other main metric used in the paper is "valid plan accuracy". Such a metric is not meaningful when using systems with guarantees, namely A*, which is guaranteed to find optimal plans, while the proposed system has no such guarantees. Because of the false equation between A* intermediate states and LLM-output, the budget restriction is not meaningful and skews the accuracy metric significantly. For instance, if wall time budget were used instead, A* would simply have an accuracy of 100%. Reporting otherwise is potentially misleading. 

The paper claims to test out-of-distribution blocksworld, but it is unclear from figure 1 which results are out of distribution testing and which are in-distribution testing. Also, the left hand side of figure 1 has a correct maximum accuracy of 100%, but the right hand side has a maximum accuracy of only 30%, which seems extremely misleading. Can you clearly label which results in Figure 1 are from in-distribution versus out-of-distribution testing and present the results in Figure 1 with a uniform scale 0-100?

"model-based" on line 144 seems misused, namely confusing parameterized models like neural networks with transition models used in planning and RL. In general, some terminology is unconventional or misused. 

line 253: "we assume that they can be decomposed into sub-goals". This is a very dangerous assumption that rules out true planning problems, as often sub-goals interact. This is the case for blocksworld (but not the maze task), so since the blocksworld dataset has been filtered in this way, it no longer represents the original task and is in fact far simpler to solve [1]. The method for decomposing plans is not obvious, and the sliding window approach, while interesting, is certainly not guaranteed to decompose an arbitrary problem successfully. In the worst case, the system must always be able to fall back on System 2. 

The system is given tiny datasets and (for mazes) tested within distribution. 5x5 mazes are far too small and A* can scale to much bigger problems, while it's unclear if the proposed LLM-based approach does. The relatively high system 1 performance is a good indicator that parts of the problem are being memorized -- and in the case of mazes it is clear how this is possible since the task has decomposable subgoals that can be independently memorized. It's good that out-of-distribution was considered for blocksworld, but the results section doesn't always distinguish between numbers reported from in-distribution testing and out-of-distribution testing. 

In general, planning is misunderstood. By default A* is sound, complete, and produces optimal plans. In contrast, an LLM generator is not sound, not complete, and not optimal. When A* is limited by search budget, it is not the same algorithm, but still will never produce an incorrect plan, and if given enough time will produce the optimal plan. In contrast, an LLM (or system that uses one) is capable of producing incorrect plans, and has no optimality guarantee even if given infinite computation. The proposed method does not have any guarantees, wheras systems like LLM-Modulo do have soundness guarantees (but not completeness!). Please consider adding a discussion section that explicitly compares the theoretical guarantees and limitations of A* versus the proposed LLM-based approach. This could help readers better understand the tradeoffs involved and the contexts in which each approach might be most appropriate.

[1] Sussman, G. J. (1973). A computational model of skill acquisition.

See also: https://en.wikipedia.org/wiki/Sussman_anomaly

### Questions
In the results section for blocksworld, which numbers are from in-distribution testing and which are from out-of-distribution testing?

What guarantees does System 1.75 have?

Did you consider wall-clock time budgets? This would be a more fair comparison. Surely the authors know that querying LLMs repeatedly takes far longer than querying A*, so I'm curious why these times weren't reported in the paper?

### Soundness
1

### Presentation
2

### Contribution
1

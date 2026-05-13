# Learning Splitting Heuristics in Divide-and-Conquer SAT Solvers with Reinforcement Learning

- Decision: Accept
- Scores: 6, 3, 6, 8

## Abstract
We propose RDC-SAT, a novel approach to optimize splitting heuristics in Divide-and-Conquer SAT solvers using deep reinforcement learning.  Our method dynamically extracts features from the current solving state whenever a split is required.  These features, such as learned clauses, variable activity scores, and clause LBD (Literal Block Distance) values, are represented as a graph.  A GNN integrated with an Actor-Critic model processes this graph to determine the optimal split variable.  Unlike traditional linear state transitions characterized by Markov processes, divide-and-conquer challenges involve tree-like state transitions.  To address this, we developed a reinforcement learning environment based on the Painless framework that efficiently handles these transitions.  Additionally, we designed different discounted reward functions for satisfiable and unsatisfiable SAT problems, capable of handling tree-like state transitions.  We trained our model using the Decentralized Proximal Policy Optimization (DPPO) algorithm on phase transition random 3-SAT problems and implemented the RDC-SAT solver, which operates in both GPU-accelerated and non-GPU modes.  Evaluations show that RDC-SAT significantly improves the performance of D\&C solvers on phase transition random 3-SAT datasets and generalizes well to the SAT Competition 2023 dataset, substantially outperforming traditional splitting heuristics.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a reinforcement learning-based (RL) splitting heuristic for Divide-and-Conquer (D&C) parallel SAT solvers. Similar ideas were applied to branching heuristics but suffered from excessive prediction calls. Benefiting from the low invocation frequency, the RL-empowered splitting heuristic can effectively reduce the overall runtime of D&C SAT solvers. The empirical evaluation over random 3-SAT and SAT competition benchmarks showed that the resulting solver, RDC-SAT outperformed the traditional D&C solvers.

### Strengths
1. This work leverages the low invocation frequency of the splitting heuristic for D&C SAT solvers and improves the overall runtime performance. In contrast, the previous works on branching heuristics failed to reduce the overall runtime due to the high invocation cost.
2. RDC-SAT solver showed runtime improvement on both random 3-SAT and SAT competition benchmarks compared to the traditional D&C solvers. Particularly, the improvement on the SAT competition benchmark demonstrated the RDC-SAT’s effective generalization to industrial benchmarks, which many ML-based solvers could not achieve.
3. The authors also developed a tailored RL environment to handle the tree-like state transitions involved in the D&C framework.

### Weaknesses
Though it is an interesting idea for the ML-assisted solver, the evaluation results are slightly lower than what I expected. Out of the 305 instances from SAT competition 2023, only 2 more instances were solved by RDC-SAT than the most competitive baseline. Note that in the competition 2023, the state-of-the-art parallel SAT solver (PRS-parallel) solved 320 out of 400 instances, and I think the solved number over these 305 instances will still be considerably higher than RDC-SAT’s (135 out of 305).

### Questions
I am reluctant to give a high score considering the barely satisfactory evaluation results, especially if compared to the state-of-the-art parallel SAT solvers. Can you please elaborate on the specific scenarios or problem types where D&C solvers can outperform the portfolio solvers like PRS-parallel, supported by empirical evidence or citations? A good motivation for using D&C solvers may change my opinion. It would also be good to have a more comprehensive discussion of the trade-offs between D&C and portfolio approaches in the paper's introduction or related work sections.

It would be good to know PRS-parallel's runtime performance on these 305 instances. Could you please run the experiments and report the results?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes using deep reinforcement learning to enhance divide-and-conquer (D&C) based parallel SAT solving. The basic idea is to train a Graph Neural Network (GNN) model using reinforcement learning to predict splitting heuristics. The proposed method shows improved performance over common heuristics like FLIPS, VSIDS, and PR on random 3-SAT problems and SAT Competition 2023 benchmarks.

### Strengths
The paper addresses an important and interesting problem. The proposed approach is conceptually sound, and the results appear promising.

### Weaknesses
The novelty of this paper is not clearly explained. It would be beneficial to clearly highlight the incremental contribution of this work, given the existing research on RL and GNN applications in SAT solving. A thorough comparison with Graph-Q-SAT and other related work, could help emphasize the unique aspects of this approach.

While the paper aims to improve D&C-based parallel SAT solving, the methodology does not seem to include specific elements which has a clear connection with parallel SAT solving. The proposed optimization and improvement seems purely in sequential manner. It would be helpful to clarify how the proposed technique applies to parallel SAT solving.

The evaluation appears to be incomplete. The evaluation could be strengthened by including comparisons with existing parallel and sequential SAT solvers. Considering a broader range of problem sizes and incorporating benchmarks from the latest SAT competition 2024 would provide a more comprehensive assessment.

Minor Suggestions:

Section 3.1 could focus more on methodology rather than implementation details of the Gym environment.

Diversifying the training data beyond 3-SAT problems might improve the model's prediction accuracy across various SAT problem types.

### Questions
What is the incremental contribution of this paper?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a framework that employs deep reinforcement learning to enhance splitting heuristics in divide-and-conquer SAT solvers. By utilizing a graph representation to dynamically extract features from the solving state, RDC-SAT optimally selects split variables through a reinforcement learning paradigm. The method addresses the challenges posed by tree-like state transitions in divide-and-conquer scenarios and introduces tailored reward functions for both satisfiable and unsatisfiable SAT problems. In the experiment section, the proposed method is trained on random 3CNF at threshold instances and helps CDCL solvers achieve better performance. The trained model generalizes to industrial instances as well.

### Strengths
1. Improving the performance of parallel SAT solvers, especially D&C solvers, is one of the important tasks in SAT solving.  D and C solvers are the paper did an integration of reinforcement learning and SAT solving. The combination of RL and D&C solvers is a solid research direction.

2. It is very interesting to see that models trained on random instances can be generalized to instances from SAT Competition. I believe that it implies that there exists certain rules/techniques in SAT solving that are sharable between different types of instances.
It is not clear whether things learned from random instances can be generalized into industrial instances.
the size of problems are relatively small, does it generalize to larger instances?

3. This paper is well written with methodologies clearly explained.

### Weaknesses
1. Exactly why the model trained on just random 3CNF can generalize on industrial benchmarks is still mysterious to me. I believe this point is important and worth more investigation. Can the heuristics learned by the model be extracted and represented symbolically? Does learning on industrial benchmarks further improve the performance on instances from SAT competition? 

2. The size of random instances used in training and testing is relatively small (300-500), though they are indeed on the threshold of satisfiability. I am not sure whether those problems are actually considered challenging to CDCL solvers. It would be helpful to see if the approach generalizes to larger random instances with thousands of variables. Furthermore, a comparison against local search solvers, which are known to perform well on random satisfiable instances, is missing.

### Questions
See the above

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a new SAT solver, RDC-SAT, which combines reinforcement learning with a divide-and-conquer strategy. Currently, modern SAT solvers are using parallelization strategies to enhance computational efficiency. While portfolio-based solvers lead in SOTA performance, the divide-and-conquer strategy still retains competitive potential due to its structure-guided nature. Similar to the step-by-step approach in divide-and-conquer, reinforcement learning also has the ability to make sequential decisions under a MPC framework. The authors leverage this motivation, formalizing the D&C splitting process within the Painless framework into an RL environment with a designed reward function, and train it using a DPPO policy. Two versions of RDC-SAT, using different device-utilization approaches, along with traditional splitting strategies are tested on a random dataset and the SAT competition 2023 dataset. The evaluation results show that the RDC-SAT solver has optimized computational efficiency and better generalization compared to other strategies.

### Strengths
1. The motivation for combining D&C SAT solver and RL approach is clear and reasonable. It is a valuable A+B attemptation.
2. This work do not simply focus on pushing forward SOTA Portfolio-based solvers; instead, it reflects on the potential of the D&C strategy with explainable points. It introduces more thoughtful topics to the research community.
3. The methodology flow presented in chapter 3-4 is well-structured. Readers can easily follow the construction of the entire work in a sequential way. Detailed definitions are also presented well.
4. The authors provide sufficient detailed information in the appendix for a comprehensive presentation, including related works, detailed algorithms, datasets, and so on. This greatly aids understanding and reproduction.

### Weaknesses
1. This is an A+B work, and it does not push forward SOTA solver performance.
2. There are details remain unclear in time, space & scale when using GNNs. (See questions 1-3)
3. There are details remain unclear in reinforcement learning settings. (See questions 4)
4. The experiments could be more comprehensive. (See question 5-8)
5. Other minor concerns. (See question 9-10)

### Questions
I didn't read all of the appendix, so if there is anything I've missed, please let me know.
1. During the evaluation stage, if the solver needs to generate a new GNN every time a splitting strategy is applied (due to the new or deleted learned clauses/variables etc), doesn't it cost a lot both in time and space compared to tranditional strategies? Can you show me the experimental statistic on this?
2. Replay buffer: Also, in RL training, data stored in graph could cost a lot of space. Is there any consideration of this? 
3. The paper mentioned that during the splitting process, the learned clauses can expand the original scale from k+ to 10-50 k+ clauses. This puts more pressure on time and space concerns. How does RDC-SAT manage this? I believe these three questions may relate to the CPU-once settings.
4. The paper did not give a clear definition of the RL action, apart from the state and reward. The splitting stragegy needs a chosen variable to split; is the chosen variable denoted as an action? This should be well-defined in the main paper.
5. The detailed definition of PAR2 metric should be introduced in the experiments.
6. The experiments only compare to the trandition splitting methods. Are there any learning-based splitting methods to compare with?
7. Do the chosen tranditional splitting methods perform a SOTA level in D&C solvers? If not, what's the gap between RDC-SAT and SOTA D&C solver? Moreover, what's the gap between RDC-SAT and SOTA SAT solvers (including Portfolio)? There should be a promising future where, even though currently D&C solvers are not SOTA, they could become SOTA with a relatively small gap to overcome.
8. Can you train RDC-SAT on the SAT competition Dataset and show the in-distribution evaluation result? It may prove the direct applicability in industrial applications.
9. What does [1, 0, ...] mean in Figure 2? 
10. On page 6, line 275, why do you use "absolute" values? Since the defined value here is time, the value is certainly non-negative.

### Soundness
3

### Presentation
4

### Contribution
2

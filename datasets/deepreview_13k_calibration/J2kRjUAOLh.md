# Contrastive Predict-and-Search for Mixed Integer Linear Programs

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 6, 3

## Abstract
Mixed integer linear programs  (MILP) are flexible and powerful tools for modeling and solving many difficult real-world combinatorial optimization problems. In this paper, we propose a novel machine learning (ML)-based framework ConPaS that learns to predict solutions to MILPs with contrastive learning. For training, we collect high-quality solutions as positive samples and low-quality or infeasible solutions as negative samples. We then learn to make discriminative predictions by contrasting the positive and negative samples.   During test time, we predict assignments for a subset of integer variables of a MILP and then solve the resulting reduced MILP to construct high-quality solutions. Empirically, we show that ConPaS achieves state-of-the-art results compared to other ML-based approaches in terms of the quality of and the speed at which the solutions are found.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a predict-and-search approach for solving mixed integer programming(MIP), according to a GNN-guided approach from [Han2022]. The algorithm collects high-quality solutions as positive samples and low-quality solutions as negative samples, and then trains the prediction model by contrastive learning. The authors demonstrate that the proposed method outperforms the baseline on four commonly used mixed-integer linear programming datasets.

### Strengths
1. The effect of improving the prediction model through contrastive learning training method is intuitive and effective.
2. The author's experiments show that the proposed method has a significant improvement over the baseline.
3. The paper is mostly well-written and easy to follow.

### Weaknesses
1. The technical novelty is limited. First, it is a somewhat straightforward application of contrastive learning to predict-and-search. Second, the proposed method is essentially the same as the ICML 2023 paper [Huang2023] (Figure 1 of this paper almost coincides with Figure 1 in [Huang2023]), if we consider the procedure as a one-step LNS.

2. Since the proposed approach is based on predict-and-search, it cannot guarantee the optimality or feasibility. This limitation is not discussed or analyzed properly in this paper. For example, there is no empirical study on the feasibility ratio on the test instances. The authors should also conduct experiments on more constrained problems. Furthermore, it is somewhat unfair to compare the anytime performance with SCIP, since the proposed method (as well as predict-and-search) essentially solves a much simpler problem than SCIP since some variables are fixed.

3. The authors collected training data using Gurobi, but only compared the test performance with SCIP. I cannot see any reason why not compare with Gurobi at test time.

4. The authors used two ways to collect negative samples, but only report their empirical performance, without a deep analysis on which way is more reasonable.

5. The authors did not show the results of how accurate the solution prediction is.

### Questions
Please see the above weaknesses.

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
This paper proposes a construction approach of positive and negative samples based on the quality of milp problem’s feasible solutions. With the constructed samples, one can train a GNN model to predict good assignments for integer variables using contrastive learning mechanism, which helps search optimal solution more quickly. Superior experimental results demonstrate the effectiveness and generalizability of the proposed approach.

### Strengths
The research topic is valuable and the paper is well written. Moreover, the designed method is presented with succinctly and clearly as well as its motivation. The performance of trained GNN is also impressive, which indicates the superiority of the proposed method.

### Weaknesses
There are still some issues needed to be addressed to make this paper meet the requirement of ICLR: 
1.	The contribution and novelty is not summarized clearly and relatively weak. The main contributions of this paper are applying contrastive learning to predict and search optimal solution.

2.	Results of empirical evaluation can be more solid and convincing. The experiments are just conducted on two generated dataset and one competition dataset, without the recognized authoritative dataset MIPLIB2017 benchmark. Furthermore, only an open-source MILP solver, which is not well configured, is involved in baselines. Considering that different configuration can significantly affect the solver’s performance, I would expect some further comparative experiments conducted on SCIP configured with tuned parameters or some more powerful commercial solvers (like GUROBI and CPLEX).

### Questions
I noticed that the effect of hyperparameter k0 and k1 is evaluated. Of course, this hyperparameter is important, because it controls the tradeoff between the feasibility and quality of predicted solutions. However, considering that MILP instances generally have different scales of integer variables, a specific number of integer variables may not be a good choice. I was wondering that would it be better if we use the coverage rate (i.e., the ratio of fixed variables in the entire set of integer variables when using predict methods like Neural Diving) to control the fixed number of integer variables.  

In addition, some studies indicate that each instance has an unique optimal coverage rate (https://arxiv.org/abs/2308.00327), so I think that evaluating the effect of k0 by just computing an average number on one dataset (CA) may not help readers configure their own prediction model properly.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a method for finding primal solutions to mixed-integer programs using a graph neural network-based approach. The training and performance of the approach is improved through the use of constrastive learning, which has been gaining popularity in a variety of deep reinforcement learning applications due to the fact that it does not require expensive labeling of data to "pre-train" networks. The approach is based on the "predict and search" method from a previous ICLR paper. The approach is evaluated experimentally on several relatively easy MIP problems and a dataset of integer programs from the NeurIPS 2021 ML4CO competition.

### Strengths
- Contrastive learning shows great promise in the space of combinatorial optimization; we see again and again that it is an effective mechanism for reducing training time and creating great models.

- The empirical performance of the method on the datasets tested is quite strong.

- (Updated) The novelty of the paper, while not huge, is sufficient for ICLR. The authors have indicated how it differs from CL-LNS, and the bi-level model is an interesting contribution that other groups solving MIPs will want to consider.

### Weaknesses
 - The instance dataset is not so great, but I admit there are not so many good public MIP problems out there. Simply put, claiming that you can solve the CA dataset to a MIP person is just really not that interesting. Since all the other MIP papers at ICLR/NeurIPS seem to have the same problem, I'll let it pass.

- Using SCIP as a direct point of comparison is not really fair. SCIP is trying to prove optimality, while the method proposed in this work is just a primal heuristic. I appreciate, however, that the authors do not make big claims about beating SCIP the way some papers in this area do. They do seem to understand that beating SCIP is relatively meaningless.

- I am a little surprised to not see an abalation study on the modified loss function.

- The introduction's description of Gurobi and CPLEX is not complete. They are really branch and cut algorithms with (what CPLEX calls) "dynamic search" (and a whole bunch of other stuff, who knows what half of it is...)

- I still feel like there could be more experimentation regarding the negative examples (e.g., versus the strategy in the CL-LNS paper??). Since this is the main contribution, I wish it was actually more in focus throughout the paper.

### Questions
All questions have been answered.

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors propose to integrate contrastive learning with the pipeline of solving mixed integer linear programming. They manage to generate positive samples and negative samples during the training. The positive samples are optimal or near-optimal solutions of MILP, while the negative samples are infeasible or low-quality solutions. The model is then trained by these samples via supervised contrastive learning to predict better solutions. After this, the predicted solutions are improved by the PaS framework to make them become valid optimal solutions. Experiments on multiple datasets show the performance of the proposed ConPas framework.

### Strengths
1. The paper is well-written and easy to follow.
2. The idea of utilizing contrastive learning in MILP looks interesting to me.
3. The experiments contain various MILP datasets.

### Weaknesses
1. I find one work in related work[1] very similar to this paper. Both of these two papers propose to utilize contrastive learning in solving MILP and share the core idea of generating positive and negative samples. The only difference is the operation after the contrastive learning part, the ICML paper[1] uses large neighborhood search (LNS) and this ICLR paper uses Predict and Search (PaS). Actually, I think this paper is covered by the ICML paper, as PaS could be regarded as a variant of LNS. Though the authors do mention this ICML paper in the related work, they do not discuss the difference between their work and the ICML paper, nor compare it as a baseline. 
2. Though the idea of utilizing contrastive learning in MILP looks interesting, I consider the current usage of contrastive learning to be more like an incremental part. In this work, solving MILP basically relies on the performance of PaS. I am not sure if this contribution is good enough for ICLR. To me, this work is more like using contrastive learning to find a better initialization for PaS, of which the application is limited. 
3. The results of experiments look good, but I think more datasets with hard cases are required. In my own experience of using SCIP,  I think MVS and MIS are relatively easy for SCIP. In contrast, the datasets from NeurIPS 2021 ML4CO are difficult for SCIP, but it looks like the authors did not select the whole datasets of ML4CO, as they said: "IP instances are taken from the NeurIPS 2021 ML4CO competition Gasse et al. (2022)." I wonder how the data is selected. In fact, there are 3 benchmarks in NeurIPS 2021 ML4CO[2], I wonder why the authors neglect them. Besides, a common dataset MIPLIB is also missing in the paper.

### Questions
1. Please discuss your paper with the ICML paper I mentioned in the weakness. In my view, these two papers are very similar and the ICML paper seems to cover your work to some extent. A comparison in experiments is also suggested if possible.
2. As I mentioned before, this work is more like using contrastive learning to find a better initialization for PaS. I wonder can this work be applied to methods other than PaS? e.g. Neural Diving mentioned in the paper. 
3. The datasets in the experiments require more improvement.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

# Accelerating Multi-Block Constrained Optimization Through Learning to Optimize

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 5, 5

## Abstract
Learning to Optimize (L2O) approaches, including algorithm unrolling, plug-and-play methods, and hyperparameter learning, have garnered significant attention and have been successfully applied to the Alternating Direction Method of Multipliers (ADMM) and its variants. However, the natural extension of L2O to multi-block ADMM-type methods remains largely unexplored. Such an extension is critical, as multi-block methods leverage the separable structure of optimization problems, offering substantial reductions in per-iteration complexity. Given that classical multi-block ADMM does not guarantee convergence, the Majorized Proximal Augmented Lagrangian Method (MPALM), which shares a similar form with multi-block ADMM and ensures convergence, is more suitable in this setting. Despite its theoretical advantages, MPALM’s performance is highly sensitive to the choice of penalty parameters. To address this limitation, we propose a novel L2O approach that adaptively selects this hyperparameter using supervised learning. We demonstrate the versatility and effectiveness of our method by applying it to the Lasso problem and the optimal transport problem. Our numerical results show that the proposed framework outperforms popular alternatives. Given its applicability to generic linearly constrained composite optimization problems, this work opens the door to a wide range of potential real-world applications.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper studies a novel learning to optimize approach for multi-block ADMM. The proposed method adaptively selects the penaltiy parameters for MPALM and achieve better empirical performance.

### Strengths
The studied problem is interesting. The paper is easy to follow. The proposed method obtains better peroformance than baselines in the Lasso problem and the discrete optimal transport problem.

### Weaknesses
Here are my concerns about this paper:

- About the (ERM)

My main concern is that it is usually expensive or intractable to obtain the exact x* for (ERM) in most real-world applications. Thus the proposed method is a bit impractical. Specifically, the reliance on exact solutions for training the meta-learner introduces a significant bottleneck. The computational cost of obtaining these solutions, especially for complex, high-dimensional problems, may outweigh the benefits of the adaptive penalty parameter selection. The paper does not adequately address the scalability of this approach, particularly in scenarios where obtaining the ground truth is computationally prohibitive.

- About the experiment

The datasets used in the experiments are too small. I suggest authors to perform experiments on larger datasets with high dimensional data points. In addition, I think it would be better to perform experiments on real-world datasets rather than synthetic datasets. The current experiments, while demonstrating the method's feasibility, lack the scale and complexity to convincingly show its practical utility. The Lasso problem and the discrete optimal transport problem, while relevant, are not sufficient to generalize the performance of the proposed method to more challenging real-world scenarios. The absence of high-dimensional data further limits the scope of the experimental validation.

- About writing

The writing needs refinement. The main paper begins to propose the method on page 7, dedicating only four pages to detailing its advantages. I suggest the authors consider moving some background information to the appendix, allowing for a more comprehensive presentation of the proposed method in the main body of the paper.

minors:
The papers should provide the reference of Thm 1.

### Questions
see weakness

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This work addresses a gap in Learning to Optimize (L2O) approaches by extending L2O methods to multi-block ADMM-type algorithms, which remain unexplored. Multi-block methods take advantage of the separable structure of optimization problems, reducing per-iteration complexity. However, classical multi-block ADMM lacks convergence guarantees, making the Majorized Proximal Augmented Lagrangian Method (MPALM) a more suitable choice due to its convergence properties. Despite its theoretical benefits, MPALM's performance is highly sensitive to the choice of penalty parameters. To address this, this work proposes a novel L2O framework that adaptively learns these hyperparameters through supervised learning, demonstrating its effectiveness on the Lasso problem and the optimal transport problem.

### Strengths
1. This work proposes a simple yet effective L2O framework for learning the hyperparameters of a majorized proximal augmented Lagrangian method.

2. Two applications, i.e., Lasso problem and discrete optimal transport problem are used to evaluate the proposed framework.

### Weaknesses
I'm not an expert in this field, but I have provided some review comments based on my experience. I will consider the feedback from other reviewers and the authors' rebuttal to adjust my score. I have some concerns as follows.

1. The key contribution of this work lies in the proposed L2O framework for majorized proximal augmented Lagrangian method. However, this content only appears when reading page 7, as the authors dedicate extensive space to introducing majorized proximal augmented Lagrangian method. I have a few questions: 1) Are Theorem 1 and Theorem 2 intended as theoretical contributions in this work? If not, could you clarify why they are presented as main text theorems? Additionally, I could not locate proofs for these theorems within the manuscript. 2) While the asymptotic convergence for majorized proximal augmented Lagrangian method is discussed, I am particularly interested in insights regarding the non-asymptotic convergence for majorized proximal augmented Lagrangian method.

2. The applications demonstrated in this work are the Lasso problem and the discrete optimal transport problem. Could the proposed method also be applied to popular machine learning tasks?

3. One of the key contributions of this work is the introduction of a hyperparameter learning framework. Bilevel optimization is also widely used for hyperparameter optimization in machine learning. Could bilevel optimization methods be employed to optimize the hyperparameters in this work as well?

4. If Theorems 1 and 2 are not the theoretical contributions of this paper, then what are the theoretical contributions? I did not find any other theorems in the paper.

5. Could you modify Figures 1 and 2? The font size is too small and doesn’t look very appealing.

### Questions
Please refer to the Weaknesses.

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors learn parameters in the optimisation algorithm MPALM, as the performance of the algorithm is shown to be highly sensitive to penalty parameter choice. The authors learn penalty parameters using unrolling with a regression loss. The authors apply their learned algorithm to Lasso regression and an optimal transport problem.

### Strengths
Originality of learned parameters for MPALM algorithm. Learned algorithm shows an increased performance over commonly used algorithms for both lasso and optimal transport problems, as well as MPALM with a variety of chosen penalty parameters. Good summary of related research and past work on L2O. Comprehensive introduction to the MPALM algorithm.

### Weaknesses
For the LASSO problem FISTA is a good option due to acceleration, however, it isn't compared. Not enough novelty, only parameters are learned, no novel algorithm, problem, or method of learning parameters. Theorem 1 is stated without reference or proof. While provable convergence is stated, it lacks a proof as to why, as the condition (Assumption 3) depends on \sigma.

Minor: Grammatical errors/typos including "with slightly abuse of notation", indexing with i in (ERM). "g(w) := \mu \| x \|_1", "the Sinkhorn’s algorithm". It seems MPALM and LMPALM are never explicitly defined in the main text.

### Questions
Is \{\sigma_j\} supposed to denote \{\sigma_1, \cdots, \sigma_{J}\}, where $J = \floor{K/K_0}+1$? \{\sigma_j\} seems ill-defined without indexing j. With Assumption 3, does convergence with learned parameters hold for your learned algorithms. Is this a clear and easy result? You write "If the back-propagation fails in practice, stochastic gradient based optimizers are no longer applicable. In this case, we may rely on grid search to find good penalty parameters, though it can be costly." Which cases is this true for?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes an effective Learning to Optimize (L2O) framework for hyperparameter tuning in a majorized proximal augmented Lagrangian method, designed to solve challenging optimization problems of the form $P(\xi)$. This work expands the application of machine learning techniques in developing efficient algorithms for constrained optimization. The framework is validated through numerical experiments on the Lasso problem and the discrete optimal transport problem.

### Strengths
1.Writing: This work is presented with good writing style, where the summarized problems with detailed explanations make it easy for readers to understand the problem addressed in this article. 

2.Novelty:It proposes a simple yet effective L2O framework for learning the hyperparameter of a majorized proximal augmented Lagrangian method.

3.Experiments: Several scenarios and recent baselines are considered, implying improvements in accuracy and robustness under various distributional shifts.

### Weaknesses
Weaknesses:
1.Originality of the algorithm. Could you clarify the differences between the algorithm presented in this paper and the one in [1]?  If the framework proposed here is indeed more inclusive than MPALM, please provide an example of a problem that this paper's algorithm can solve but MPALM cannot.

[1]Liang Chen, Xudong Li, Defeng Sun, and Kim-Chuan Toh. On the equivalence of inexact proximal ALM and ADMM for a class of convex composite programming. Mathematical Programming,185(1-2):111–161, 2021.

2.Lack of strong theoretical guarantees. There is no specific convergence analysis for the algorithm, nor is there a provided convergence rate. The main text includes two theorems, one of which cites conclusions from other sources. If convergence analysis is challenging, a detailed explanatory analysis should be provided.

3.Writing. The paper seems to lack a detailed introduction to LMPALM, as it first appears in abbreviated form in the RESULTS section. Is this an oversight in the writing? Additionally, the RESULTS section does not clearly explain why LMPALM improves the experimental results.

4.Computational Cost. The paper may not provide a comprehensive assessment of the computational efficiency and practicality of the proposed method in real-world applications. Like the computational complexity analysis or empirical time/memory cost.

### Questions
For specific questions, please refer to the "Weakness" section.
I would be willing to raise my score if these questions concerned are well addressed.

### Soundness
3

### Presentation
2

### Contribution
2

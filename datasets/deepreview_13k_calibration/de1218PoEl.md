# Relaxing the Additivity Constraints in Decentralized No-Regret High-Dimensional Bayesian Optimization

- Decision: Accept
- Avg Score: 5.75
- Scores: 5, 5, 8, 5

## Abstract
Bayesian Optimization (BO) is typically used to optimize an unknown function $f$ that is noisy and costly to evaluate, by exploiting an acquisition function that must be maximized at each optimization step. Even if provably asymptotically optimal BO algorithms are efficient at optimizing low-dimensional functions, scaling them to high-dimensional spaces remains an open problem, often tackled by assuming an additive structure for $f$. By doing so, BO algorithms typically introduce additional restrictive assumptions on the additive structure that reduce their applicability domain. This paper contains two main contributions: (i)~we relax the restrictive assumptions on the additive structure of $f$ \textit{without} weakening the maximization guarantees of the acquisition function, and (ii)~we address the over-exploration problem for decentralized BO algorithms. To these ends, we propose DuMBO, an asymptotically optimal decentralized BO algorithm that achieves very competitive performance against state-of-the-art BO algorithms, especially when the additive structure of $f$ comprises high-dimensional factors.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses a line of the high-dimensional Bayesian optimization problem under the assumption that the objective function has an additive structure. Under this line, the authors relax the assumption of the additive structure without requiring that the maximum number of dimensions for a factor of the decomposition is low as in the work of (Hoang et al., 2018). The authors propose DuMBO, a decentralized, message-passing, provably asymptotically optimal Bayesian optimization algorithm under such a relaxed assumption. They also introduce another way to approximate the GP-UCB acquisition function. Finally, they demonstrate the effectiveness of DuMBO by comparing it with several state-of-the-art BO algorithms on both synthetic and real-world problems.

### Strengths
- The paper is well written in general although the related works are missing and the introduction section can be improved. 

- The idea of using the Alternating Direction Method of Multipliers (ADMM) proposed by Gabay & Mercier (1976) to maximize the acquisition function is new compared to the existing works.

### Weaknesses
 - The related works are missing. Besides Embedding and Decomposing and Turbo, there are several approaches as in [1], [2], and [3] that do not impose assumptions on the structure of the function $f$. In particular, the authors are missing a very related paper [4] "Are Random Decompositions All We Need in High-Dimensional Bayesian Optimisation?".  A comparison with this work is needed.

- The representation in the method is unclear to understand the contribution of this paper. For example, it is unclear to me why ADMM can solve the high-dimensional optimization problem, for example when $\overline{d}$ is high. Could we ensure to find the arg max when the function is non-convex?

- The experiments are insufficient to understand the effectiveness of the proposed method.  It is missing a baseline from [4].

### Questions
Please see my above questions. I also have other questions as follows:

- Do the authors need any assumption on the function $f$ such as the Lipschitz continuous to guarantee the convergence?
- Equation (8) seems incorrect to me. Is it a typo?

### Soundness
2 fair

### Presentation
2 fair

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
The paper relaxes restrictive assumptions on the additive structure of the objective function. It proposes the DuMBO algorithm, which is a decentralized, message-passing, and asymptotically optimal BO algorithm. DuMBO can infer complex additive decompositions of the objective function without assumptions regarding Maximum Factor Size (MFS).

### Strengths
The paper presents an innovative approach to Bayesian Optimization (BO) that relaxes assumptions about the Maximum Factor Size (MFS) and focuses on modeling and optimizing complex, high-dimensional objective functions. 
The DuMBO algorithm introduced in the paper is asymptotically optimal, meaning it provides strong guarantees of convergence to the global optimum of the objective function over time.
The paper backs its claims with empirical evidence by comparing DuMBO with state-of-the-art BO algorithms on both synthetic and real-world problems. It demonstrates that DuMBO performs competitively and is particularly effective when the objective function comprises numerous factors with a large MFS.
The paper explores the trade-off between model complexity and the guarantee of maximization in the acquisition function, contributing to the theoretical understanding of BO algorithms in high-dimensional spaces.

### Weaknesses
The paper's experiment part is not valid enough. The baseline it compares TurBo is not that up to date. Please see:

Learning Search Space Partition for Black-box Optimization using Monte Carlo Tree Search
Linnan Wang, Rodrigo Fonseca, Yuandong Tian

And some other trust region based high-dimensional methods. Also notice that in the paper, some other methods are mentioned, but didn't show up in the experiments part.

In general, the performance improvement to other baseline is not significant enough. I believe some other methods can outperform the baselines in a similar way.

Ablation study about other hyper parameters should be given.

### Questions
(1) In Table 2, why the standard deviation is not given?
(2) Is the algorithm sensitive to \bar d and other hyper-parameters? 
(3) In figure 1c. The performance of DumBO is close to TurBO. Does that mean DumBO does not outperform baseline much on higher dimensional tasks?
(4) Why the time step is only about 100? For figure 1a. Some methods's cost are still decaying.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper is concerned with the problem of optimizing a function that is noisy and costly to evaluate. The traditional way to tackle this is by assuming an additive structure for the function which imposes restrictive assumptions on the function. This paper introduces DumBO, a decentralized BO algorithm that relaxes these assumptions, albeit at the expense of weakening the maximization guarantees of the acquisition function. Additionally, the authors also claim to address the over-exploration problem in decentralized BO algorithms. Experimental evaluation suggest that their algorithm performs competitively compared to state-of-the-art BO algorithms.

### Strengths
1) The paper is very well-written.
2) The authors provide an algorithm which can be implemented in a decentralized manner, which seems to be very useful.
3) The authors show a regret bound, which  show asymptotic optimality of their algorithm.
4) Experiments conducted are exhaustive.

### Weaknesses
1) It would have been nice if the authors could show a proof sketch of their main theoretical result.
2) Apart from the proof, it would be nice if the authors could highlight the main contributions and the technical (or analytical) challenges they faced.
These all are not major weaknesses per se, but can help the interested readers.

### Questions
1) Are there known lower bounds for the problem? If yes, it would be nice to see how the proposed algorithm does in comparison.
2) What were the major technical challenges the authors faced while deriving the regret bounds?

### Soundness
3 good

### Presentation
3 good

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
The work discusses a new algorithm called DumBO for decentralized Bayesian optimization. DumBO relaxes the additivity constraints of traditional BO algorithms for high-dimensional inputs. It achieves better performance against some existing BO algorithms, especially when the additive structure of the objective function comprises high-dimensional factors. DumBO finds the maximum of the objective function while ensuring consistency between shared input components. The algorithm relies on ADMM to maximize the acquisition function and has demonstrated good performance in the numerical experiments.

### Strengths
The authors have conducted a number of numerical experiments to illustrate the practicability of their algorithm. They have included state-of-the-art baseline algorithms for comparison, and have demonstrated scenarios when their approach is superior. 

In addition, the authors provide explicit descriptions of optimizing the acquisition function, which is facilitated by the ADMM algorithm. The detailed procedure makes the algorithm feasible to use.

### Weaknesses
The presentation of the manuscript is not explicit enough for the audience to understand. For example, the main assumption of this work is that the objective function $f$ can be decomposed into several factors and each factor only takes some dimensions of $\boldsymbol{x}$ as the input, as in Equation (2). However, this decomposition is not explicitly explained in Section 3.1. Actually, Figure 2 in the supplements helps the audience to understand and can be moved to the main text. In addition, to guarantee the performance of ADMM, the authors assume that the acquisition function ``is a restricted prox-regular function that satisfies the Kurdyka-Lojasiewicz condition’’. The authors should at least provide a formal definition of this condition. 

The theoretical results do not exhibit sufficient novelty. For example, similar results as Theorem 3.4 have been derived, for example, in [1]. The analysis of the regret is also quite similar to that in [2], without significant novelty. 

### Questions
In addition, the authors mention that the decomposition needs to be inferred from the data. In this way, is the algorithm performance sensitive to the inference results of the decomposition? How to incorporate the inference uncertainty into the regret analysis? If the data for inference is not given in advance, how many rounds are required to generate the data for decomposition inference?

Besides, the acquisition functions should satisfy a certain condition as in Assumption 5.1. The authors might discuss under what conditions the acquisition function satisfies Assumption 5.1.

Besides, the authors might provide a more detailed comparison with the existing algorithm Add-GP-UCB [3], since the decomposition of the objective function is quite similar.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

# Black-Box Gradient Matching for Reliable Offline Black-Box Optimization

- Decision: Reject
- Scores: 6, 8, 3, 5

## Abstract
Offline design optimization problem arises in numerous science and engineering applications including materials engineering, where expensive online experimentation necessitates the use of in silico surrogate functions to predict and maximize the target objective over candidate designs. Although these surrogates can be learned from offline data, their predictions can be potentially inaccurate outside the offline data regime. This challenge raises a fundamental question about the impact of imperfect surrogate model on the performance gap between its optima and the true oracle optima, and to what extent the performance loss can be mitigated. Although prior work developed methods to improve the robustness of surrogate models and their associated optimization processes, a provably quantifiable relationship between an imperfect surrogate and the corresponding performance gap, and whether prior methods directly address it, remain elusive. To shed more light on this important question, we present a novel theoretical formulation to understand offline black-box optimization, by explicitly bounding the optimization quality based on how well the surrogate matches the latent gradient field that underlines the offline data. Inspired by our theoretical analysis, we propose a principled black-box gradient matching algorithm to create effective surrogate models for offline optimization. Experiments on diverse real-world benchmarks demonstrate improved optimization quality using our approach to create surrogates.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper first provides a bound for the performance gap between oracle and a chosen surrogate as a function of how well the surrogate matches the gradient field of the oracle on the offline training data and then using the analysis done to bound the performance gap formulates an algorithm which uses multiple monotonic trajectories of hopping over training points after binning and splitting them based on percentile values for the task of black-box offline optimization where access to oracle is unavailable in the sense that no new input and output value cannot be acquired or sampled. The authors show that the algorithm does better compared to other baselines on tasks and datasets proposed in Trabucco et al., 2022 both in terms of Mean Normalized Rank and Mean Normalized score over multiple percentiles of candidate solutions provided by the algorithms.

### Strengths
1. The paper is mostly well written and the relevant literature and references are covered well.
2. The math looked sound to me as far as I could see.
3. The algorithm performs well over baselines both on Mean Normalized Rank and Mean normalized score metrics for both 50 percentile and 100 percentile.
4. The paper gives complexity analysis of the proposed algorithm.
5. Figures look good and support the narrative and many(9) baseline algorithms are tried and compared with the proposed algorithm.

### Weaknesses
1. The paper is mostly well written and the relevant literature and references are covered well.
2. The math looked sound to me as far as I could see.
3. The algorithm performs well over baselines both on Mean Normalized Rank and Mean normalized score metrics for both 50 percentile and 100 percentile.
4. The paper gives complexity analysis of the proposed algorithm.
5. Figures look good and support the narrative and many(9) baseline algorithms are tried and compared with the proposed algorithm.

1. Typo: Page 9, missing reference.
2.  There is some repetition in the section Evaluation Methodology and section on Results and Discussion, the readibility of those sections can be improved.  
3. The paper does not compare the memory and time complexity of the algorithm with baselines. This will also depend on the hyperparameters of the optimization algorithm like the discretization parameter.
4. Some questions are unanswered which I list below.
5. The paper does not explicitly state its limitations compared to baselines especially since no baseline and proposed algorithm consistently outperforms the other methods on all tasks. Can the end-user make a judgment ?

### Questions
Some questions, the answers to which can help the paper
1. How does the discretization parameter affect the performance of the algorithm ?
2. How do the optimization hyperparameters affect the performance, also how do you choose or tune $\alpha$, the term balancing the two loss terms ?
3. Right now, the objective contains a sum of two terms: value matching loss and gradient matching loss as shown in Fig. 2, what effect does each term have and are they of the same scale or their scales vary a lot on these tasks ?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work provide a solid investigation on important problem in offline black-box optimization. The paper is full of insights and is enjoyable to read.

### Strengths
The paper is full of insights and is enjoyable to read.

### Weaknesses
I am satisfied with current version.

### Questions
1. Could you share more insight on why organizing training data into monotonically increasing trajectories is able to mimic optimization paths? In particular, could you shed more light on the equation (13)?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this manuscript, the authors propose an offline black-box optimization method by gradient matching.  In addition, the authors provide a bound of the difference between the function value at the solution of $m$-step true gradient update and that of $m$-step surrogate gradient update.

### Strengths
1. The proposed offline black-box optimization method via gradient matching is novel. 

2.  The paper is well-written and well-organized.

### Weaknesses
1.  $	extbf{The optimum of the objective in Eq.(11) can not guarantee the learned gradient is close to the true gradient }$.

 Minimizing the term $(\Delta z - \Delta x ^\top \int _0^1\nabla g _\phi (tx + (1-t)x') dt)^2$  in Eq.(10) and Eq.(11) can not guarantee the gradient is close.   To be clear,  we have 

\begin{equation}
(\Delta z - \Delta x ^\top \int _0^1\nabla g _\phi (tx + (1-t)x') dt)^2 = (\Delta x ^\top \int _0^1\nabla g  (tx + (1-t)x') dt - \Delta x ^\top \int _0^1\nabla g _\phi (tx + (1-t)x') dt)^2  
\end{equation}
\begin{equation}
= ( \Delta x ^\top  \int _0^1 (\nabla g  (tx + (1-t)x') -  \nabla g _\phi (tx + (1-t)x') )dt   )^2
\end{equation}
The optimum is  $\Delta x ^\top  \int _0^1 (\nabla g  (tx + (1-t)x') -  \nabla g _\phi (tx + (1-t)x') )dt = 0$   not necessary $ \nabla g (\cdot)  = \nabla g _\phi (\cdot)  $.   Thus, when $\Delta x$ is orthogonal to $\int _0^1 (\nabla g  (tx + (1-t)x') -  \nabla g _\phi (tx + (1-t)x') )dt$, we get a trival  solution. The difference between $  \nabla g (\cdot)   $ and  $  \nabla g _\phi (\cdot)$ at the trivial solution can be arbitrarily large. The core issue is that minimizing the integral difference does not ensure pointwise gradient matching. There exist scenarios where the integrated gradients match, yet the gradients themselves are significantly different at specific points. This is a fundamental limitation of the proposed gradient matching objective.

The true objective used in the manuscript is Eq.(13) instead of the gradient matching objective (11).  The objective (13) contains a standard regression objective term.   According to the above issue, the reviewer guesses that the regression objective term in Eq.(13) is still a key effective component. 


2. $\textbf{The bound in Theorem 1 is very loose}$ 

The bound in Theorem 1 is trivial and loose, which exponentially grows w.r.t. the number of update steps $m$.  In addition, the term  $\max_{x}|| \nabla g(x) - \nabla g_\phi (x)  ||$ in Theorem 1 can grow to infinity. The exponential growth with respect to $m$ makes the bound practically meaningless for any reasonable number of optimization steps. Furthermore, the bound relies on the maximum gradient difference, which is unbounded and can easily diverge, rendering the bound ineffective in many practical scenarios.

3. $\textbf{The empirical improvement is not significant}$.

 The empirical results are not convincing enough to demonstrate the claimed advantage of the proposed method.  In Table 1 and Table 2, the proposed method does not consistently outperform other baseline methods. The lack of consistent outperformance across different tasks and datasets raises concerns about the robustness and generalizability of the proposed method. The improvements observed are marginal and do not provide strong evidence for the claimed superiority.

4. $\textbf{Recent related baselines are missing}$. 

A comparison with the recent related offline black-box optimization method [1] is missing.   The experimental setup in [1] is quite similar to this manuscript. 

[1] Krishnamoorthy et al. Diffusion Models for Black-Box Optimization. ICML 2023

### Questions
Q1.  Could the authors address the concerns in the above section?

Q2.  Could the authors include more comparisons with the related baseline [1] ?

Q3. In this paper, the authors assume the search method given the learned surrogate is gradient ascent.  Does the gradient ascent search be the unique search method? Could the authors include additional comparisons with other search methods given the learned surrogate?

### Soundness
2 fair

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper addresses the challenge of offline design optimization in various scientific and engineering contexts, where physical or computational evaluations are costly, making real-time optimization impractical. The traditional solution has been to utilize surrogate models based on offline data to predict the objective function for unknown inputs. However, these surrogate models often show discrepancies from the true objective function, particularly outside the range of the offline data. This study introduces a novel theoretical framework to understand this discrepancy by looking at how well the surrogate models match the latent gradient of the true function. Based on this theoretical insight, the authors propose a new algorithm, MATCH-OPT, that aims to match the gradients of the oracle more closely. The efficacy of this approach is supported by experiments on real-world benchmarks, showing that MATCH-OPT outperforms existing methods in offline optimization tasks.

### Strengths
1. The concept of employing "fundamental line integration" as a technique for gradient estimation presents an intriguing approach.
 
2. The overall ranking performance of the method is commendable, underscoring its efficacy.

### Weaknesses
1. The paper frequently refers to "the gradient fields of the Oracle (i.e., the true objective function)." It's essential to note that a true objective function doesn't inherently possess a gradient. Continual mention of the oracle's gradient is foundational to this paper, and this assumption should be explicitly clarified by the author. I think this is the key drawback. If the author can clarify this point, I will increase my score.

2. The paper seems to overlook crucial baselines. It would be beneficial to reference and juxtapose the presented work against established benchmarks such as NEMO (https://arxiv.org/abs/2102.07970), CMA-ES, BO-qEI, BDI (https://arxiv.org/abs/2209.07507), and IOM (https://openreview.net/forum?id=gKe_A-DxzkH). These baselines are pivotal in this domain and warrant inclusion for a comprehensive analysis.

3. For better structuring, consider relocating the in-depth experimental results pertaining to the second question from the introduction to the exp section. This would make the introduction more concise and allow readers to delve into the specifics at the appropriate juncture.

### Questions
See Weaknesses.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

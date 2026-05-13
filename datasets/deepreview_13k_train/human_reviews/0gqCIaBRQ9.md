# Regularized DeepIV with Model Selection

- Decision: Reject
- Scores: 5, 5, 6, 5

## Abstract
In this paper, we study nonparametric estimation of instrumental variable (IV) regressions. Recently, many
flexible machine learning methods have been developed for instrumental variable estimation. However, these
methods have at least one of the following limitations:  (1) restricting the IV regression to be uniquely identified; (2) requiring minimax computation oracle, which is highly unstable in practice; (3) not allowing model selection procedure.  In this paper, we present the first method and analysis that can avoid all three limitations, while still permitting general function approximation. Specifically, we propose a minimax-oracle-free method called Density Estimation IV (DEIV) regression that can converge to the least-norm IV solution. Our method consists of two stages: first, we learn the conditional distribution of covariates, and by utilizing the learned distribution,  we learn the estimator by minimizing a Tikhonov-regularized loss function. We further extend DBIV to an iterative estimator, and show that our method allows model selection procedures such as convex aggregation and $Q$-aggregation. We conclude by empirically justifying our results with numerical simulations.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies a two stage procedure for regression in the scenario where the errors are not conditionally independent. They first learn a conditional density to make use of instrumental variables and consequently solve a square loss erm problem weighted by the learned conditional density. They show that this procedure attains mostly standard nonparametric rates.

### Strengths
* With the (unfortunate) exception of the introduction, I found the paper mostly well-written and clear.

* The paper studies an interesting problem, proposes a natural solution, and proceeds to analyze said solution. While I am not familiar with the immediately preceding related work (in IV), this seems clean to me.

### Weaknesses
 * The organization of the paper is hard to follow and the introduction is way too terse. As someone well-versed in nonparametric statistics but not necessarily IV methods, I had to skip ahead to section 4 to really understand what was going on.  Stating that you are trying to solve some fixed point equation in the introduction is not conducive to most people's understanding of the problem you are solving. 

* My overall feeling is that the result is somewhat incremental. To my understanding the main difficulty lies making standard guarantees for MLE in Hellinger^2 compatible with the square loss. I could not entirely follow why this is so challenging and would encourage the authors to further explain why this is the case (for instance, in the very last paragraph of section 1, you mention this difficulty but do not really expand on it, nor do you reference the lemmata which might be useful for understanding this difficulty).

* is it really fair to say that your algorithm is more computationally tractable when it is based on MLE?

### Questions
* is it really fair to say that your algorithm is more computationally tractable when it is based on MLE?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses the problem of nonparametric instrumental variable (IV) regression, a framework with wide applications across fields such as causal inference, handling missing data, and reinforcement learning. The objective in IV regression is to solve the conditional moment equation, 𝐸 [ 𝑌 − ℎ ( 𝑋 ) ∣ 𝑍 ] = 0, where 𝑍  serves as the instrument. The authors introduce RDIV, a regularized variant of the DeepIV method, marking the first work to provide rigorous theoretical guarantees for DeepIV. RDIV enhances generalization by incorporating Tikhonov regularization. Methodologically, RDIV follows a two-stage approach. The first stage involves learning the conditional distribution of covariates, while the second stage refines the estimator by minimizing a Tikhonov-regularized loss function.

### Strengths
RDIV offers several key advantages over existing methods. It addresses three significant limitations of prior literature: it eliminates the need for unique IV regression identification, avoids reliance on the often unstable minimax computation oracle, and supports model selection procedures.

### Weaknesses
It is unclear how the method compares for example to recently developed methods (see arxiv:2405.19463; to appear at NeurIPS 2024) that completely avoids minimax formulations, as well as avoiding the need for two-stage procedures.

### Questions
please see above

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper studies the nonparametric instrumental variable regression with Tikhonov regularization (RDIV), and proves that RDIV allows model selection procedures and matches the SOTA convergence rate. I agree with the author's claim that this work is the first attempt to provide rigorous guarantees for DeepIV. With Tikhonov regularization, the model selection procedure achieves the oracle rate and iterative RDIV matches the SOTA rate.

### Strengths
The paper is well-written, and the results are motivated well. I didn't go through the proofs, but the explanations after each result are insightful, and ease the reading.  The theoretical contribution is solid.

### Weaknesses
The numerical experiments are only based on simulated data. It would be better to have some results from real data to demonstrate the strength of the proposal. The connection between Tikhonov regularization and the function space parameterized by the neural network remains unclear. While the authors mention the use of the empirical mean of $h_\theta(X)^2$, it's not immediately obvious how this directly translates to a regularization of the function itself, rather than just a regularization of the network's output. This distinction is crucial because the theoretical results rely on properties of the function space, not just the network's parameter space. Furthermore, while the authors claim a computational gain by avoiding minimax optimization, the specific details of this gain, beyond being 'easy to tune', are not fully elaborated. It would be beneficial to quantify this gain, perhaps by comparing the number of iterations or the computational time required to achieve a certain level of performance with and without minimax optimization.

### Questions
How is Tikhonov regularization related to a function space parametrized by the neural network? It seems not straightforward to relate it to weight decay.

Is there a computational gain when minimax optimization is no longer needed?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This manuscript is basically a technical paper, discussed about two-stage non-parametric IV and model-selection in the second stage when equipped with an additional $L_2$ regularization.

### Strengths
* The authors discussed lots of the aspects for non-parametric clearly.

### Weaknesses
 * I feel the problem studied in this paper is with limited novelty. The transformation between one-stage and two-stage algorithms and analysis is in general only a technical problem and have been discussed in different places like DualIV, and the $L_2$ regularization itself makes the model-selection easier (with the strongly convexity).

 * To convert the MLE guarantee into an $L_2$ guarantee, the authors assumed a minimum density on the conditional density. What’s the benefits/drawbacks compared with the conditional mean embedding based methods (although it also requires some assumptions like HS operators).

### Questions
* To convert the MLE guarantee into an $L_2$ guarantee, the authors assumed a minimum density on the conditional density. What’s the benefits/drawbacks compared with the conditional mean embedding based methods (although it also requires some assumptions like HS operators).

### Soundness
2

### Presentation
2

### Contribution
2

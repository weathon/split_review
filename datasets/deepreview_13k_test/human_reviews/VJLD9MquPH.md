# Stochastic Gradient Langevin Dynamics Based on Quantization with Increasing Resolution

- Decision: Reject
- Scores: 3, 5, 3

## Abstract
Stochastic learning dynamics based on Langevin or Levy stochastic differential equations (SDEs) in deep neural networks control the variance of noise by varying the size of the mini-batch or directly those of injecting noise.
Since the noise variance affects the approximation performance, the design of the additive noise is significant in SDE-based learning and practical implementation.
In this paper, we propose an alternative stochastic descent learning equation based on quantized optimization for non-convex objective functions, adopting a stochastic analysis perspective. 
The proposed method employs a quantized optimization approach that utilizes Langevin SDE dynamics, allowing for controllable noise with an identical distribution without the need for additive noise or adjusting the mini-batch size.
Numerical experiments demonstrate the effectiveness of the proposed algorithm on vanilla convolution neural network(CNN) models and the ResNet-50 architecture across various data sets. Furthermore, we provide a simple PyTorch implementation of the proposed algorithm.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The key argument of the paper is that a variant of stochastic gradient Langevin dynamics can be realized by combining a quantization scheme with standard SGD. In particular, this avoids the explicit injection of noise into the gradient descent scheme.

### Strengths
The scheme proposed by the authors which links quantization with SGLD is novel and could be developed in future works. In situations where there is a pre-existing need to quantize the result, this would implicitly lead to benefits.

The method does seem to show improvement empirically, with caveats (see below).

### Weaknesses
There are many issues with the writing. In general the clarity of explanations could be improved, and the number of typos has a substantial effect on the readability of the document. See Questions for an exhaustive list. These must be fixed in order for me to recommend acceptance.

The empirical evidence is not entirely convincing for me. The loss curves (Figure 2) do not seem to show clear improvement, and it is difficult to assess Table 1 without standard deviations. Furthermore, it seems a bit strange to me that the SGLD formulation would yield any improvement to SGD-type algorithms, since prior practical performance was not stellar.

The convergence results in Theorems 3.3, 3.4 are quite strange. See questions below.

Due to the above issues, I cannot recommend acceptance for this paper at the moment.

### Questions
Why is the metric in Theorem 3.3 chosen to be the overlap of the kernels $p$? Why is this significant in practice, compared to e.g. mean-square convergence or convergence in a probabilistic sense such as KL?

Assumption 4 should be specifically referring to the local optimal point? A definition of local optimum in this case should be given.

In my opinion the results should be stated independently of the “mini-batch” and “epoch” formula, which merely complicates the presentation of the core idea.

Could the authors provide some rough estimation of standard deviations in Table 1?

Why do the training curves performance in Figure 2 not appear to match that in Table 1?

See below for a list of detailed questions regarding the writing and proofs:

**Typos:**

Frame -> framework (page 1)

There should be a space between words if followed by parentheses

Lines should not start with commas, e.g. after Eq 1, Eq 3

Owing to the quantization error as the i.i.d. White noise -> unclear what this means

Increments -> increment (page 5)

What is the point of discussing the transformation approach in such depths if it is not explored further? This point can be made more succinctly.

Appliance -> application (page 6)

In equation 20, what is C_{o1}? There must additionally be some typo, since why do both upper and lower case T appear in the equation?
(22) should be less than or equal to.

Page 15: “We” -> “we”

Definitions of floor/ceiling should not have $\forall x \in \mathbb{R}$ in the set.

Equation 25 is missing a sup on $v$.

Equation 27 seems redundant in light of Equation 28. Likewise Eq. 30 and Eq. 32s, and Eq. 37, 39.

I cannot follow the derivation in the first part of Equation 42, as there appear to be some typos (e.g. the second to last equality cannot be true, and the summation in the first equation does not make sense). Such an argument is not necessary, anyway, and one can simply appeal to symmetry.

Page 22: Indexes -> indices

Lemma: Auxiliary 1 is standard and there is no need to include the proof.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a quantization scheme for existing optimization algorithms (SGD, ADAM). The quantization error can be treated as an additive noise thus improves the performance of the algorithm. With increasing resolution, the convergence of the quantized optimization algorithms can be proven. Numerical experiments with CV tasks show that optimization algorithms based using this quantization scheme have better performance and robustness compared with existing algorithms.

### Strengths
This paper uses the quantization error, the byproduct of optimization at the implementation level, as an approach of improving the performance of the optimization algorithm at the algorithm design level.  It contains the necessary theoretical analysis of linking the quantization error to additive noise and the convergence of the algorithm, as well as the numerical evidence demonstrating the superior performance of the quantized algorithm. The ideas in the paper are organized well.

### Weaknesses
It appears to me that the writing of the paper could be improved:
* Certain notation in the manuscript lacks consistency. Notably, when $\tau$ is first introduced in equation 1 and 2, I thought it would be the index of the batches and that $\tau < B$. However, in equation 10, $\tau$ can be arbitrarily large. 
* It appears to me that the ‘transition probability’ in theorem 3.3 should be called ‘transition kernel’, as the probability of transiting from one point to another should be zero. 
* The appendix contains a lot of good supplementary information. It is a shame that the main text does not refer to the appendix.
* Should the $Q_p^{-1}(t_e + \tau)$ on top of equation (15) be $Q_p^{-1}(t_e + \tau/B)$?
* Typo on top of equation (9): evalutae
* Typo in table 2: GTXTi

This paper uses a complicated quantization scheme while providing no detail regarding the implementation of the algorithm in the text (data type, time and memory it takes to train the network, etc.). Without this information, it is hard to tell whether the quantized algorithm benefits from quantization in terms of reducing computational burden and simplifying data processing. Consequently, between the injected additive noise (easy to implement) and the quantized algorithms (hard to implement), it is hard to tell which one is better as they are supposed to improve the performance in the same way. This makes assessing the significance of this work hard.

### Questions
* Following the weaknesses, I wonder if the authors could provide more information regarding the implementation of the quantized algorithm. I checked the attached program. If I am not mistaken, the quantization is neither implemented via torch API nor casting high-precision tensors into low-precision ones.
* I wonder if the authors checked experimentally that if the performance gain from the quantization can be reproduced by injecting additive noise. 
* In the introduction, when the Non-Convex Optimization is introduced, the authors mention that the quantized algorithms have better performance in certain problems than the MCMC algorithms. I wonder if the authors could provide some reference for that.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper uses the quantized optimization to propose a stochastic descent learning equation, and combines it with SLD/SGLD to propose two alternative algorithms. The methods utilize Langvin SDE dynamics and aloow for controllable noise with an identical distribution without need for additive noise or adjusting minibatch size. Numerical experiments are carried out on CNN and ResNet-50 Models.

### Strengths
1. The paper applies the quantized optimization theory, which is primarily used to reduce computational burden, to optimization algorithms and uses Langevin SDEs for analysis. The originality is high.
2. Both theoretical analysis and experiments are presented, so this work is self-contained and easy to follow.

### Weaknesses
1. The uniform distribution assumption (Assumption 2) seems to be too stringent and unverifiable, since the quantization error $\epsilon^q$ depends highly on iterates. Throughout the anaysis in paper this assumption is crucial, so it is better to try explaining its validity in detail. For example, the authors could experiment on some simulation/real datasets to see if this assumption is satisfied.
2. The advantage of applying quantized optimization is not clearly stated. It would be better if clear motivation of using quantized method, or its computational or analytical benefits are claimed to convince readers.
3. The key point of this paper is somewhat ambiguous. If the major contribution lies in theoretical analysis, the authors should emphasize it and conduct simulation experiments to validate the stochastic approximation and convergence results, rather than merely performing real data experiments; if the contribution lies in experimental results, models like CNN and ResNet may seem to be too simple. Larger datasets and model structures should be tested to verify the robustness and efficiency of the proposed method.
4. Some typos:
 - lines after an equation should not start with comma, e.g. line after (12) (15) (18)...
 - 'Langvine' should be 'Langevin' in line before (12);
 - 'evalutae' should be 'evaluate' in line before (9);
 - 'lsyers' should be 'layers' in Table 1.

### Questions
1.Can you explain the claim in 'Appliance to Other Learning Algorithms'? It seems ADAM/ADAMW type methods require information of past iterates, so these may result in past-dependent SDEs which is different from Langevin dynamics.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

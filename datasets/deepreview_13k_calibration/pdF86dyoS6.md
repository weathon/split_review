# SOREL: A Stochastic Algorithm for Spectral Risks Minimization

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
The spectral risk has wide applications in machine learning, especially in real-world decision-making, where people are not only concerned with models' average performance. By assigning different weights to the losses of different sample points, rather than the same weights as in the empirical risk, it allows the model's performance to lie between the average performance and the worst-case performance. In this paper, we propose SOREL, the first stochastic gradient-based algorithm with convergence guarantees for the spectral risk minimization. Previous algorithms often consider adding a strongly concave function to smooth the spectral risk, thus lacking convergence guarantees for the original spectral risk. We theoretically prove that our algorithm achieves a near-optimal rate of $\widetilde{O}(1/\sqrt{\ep})$ in terms of $\ep$. Experiments on real datasets show that our algorithm outperforms existing algorithms in most cases, both in terms of runtime and sample complexity.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a stochastic algorithm for spectral risk minimization with trajectory stabilization for the primal variable. It is claimed that their approach enjoys a near-optimal rate of convergence that matches the known lower bound. They also demonstrate that this method outperforms existing baselines in various experimental settings.

### Strengths
This paper is well-written and easy to follow. The claimed contribution is interesting to the community. However, I have a major concern regarding its correctness which I elaborate on in the next section.

### Weaknesses
I didn't read the proofs closely but the main theorem seems to be incorrect by a sanity check. To be more specific, $\mu$ is in unit loss/par^2 and $\delta_k$ is in unit loss, but $\delta_k \sim \mu$ in Theorem 1. Moreover, $G$ is in unit loss/par and $\epsilon$ is in unit par^2, so $G/(\mu \sqrt{\epsilon})$ is unitless. However, there is $\log{(G/(\mu^2 \sqrt{\epsilon}))}$ in the sample complexity given in Cor. 1 which makes it not unitless.

Other comments:
1. I do not see error bars (standard errors) reported in all the experiments. Are these results based on a single run or multiple independent runs? Can you report error bars so that we can tell how significant the improvements are?
2. $w^*$ is not defined in Theorem 1.

### Questions
See the section above.

### Soundness
3

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
3

### Summary
This paper considers the problem of optimization in *spectral risk minimization*, which aims to produce more risk-sensitive models than standard ERM.  More precisely, spectral risk is defined as a weighted empirical risk minimization problem, where the weights depend on the order statistics of a given empirical sample, thereby subsuming both empirical risk (with all weights being the same) and such risk-sensitive measures as CVaR and Extremiles.  While minimizing spectral risk can be attractive due to the risk-sensitivity, it can be challenging to scale as the evaluation of the spectral risk of a given parameter depends on the entire dataset through the order statistics and is thus not amenable to naive applications of existing SGD approaches.  In particular, in order to obtain an unbiased estimate of the subgradient of the loss, all samples must have losses evaluated.  The authors circumvent this problem by applying the rearrangement inequality to reduce the problem to finding the value of a min-max game and then propose applying what amounts to a regularized form of projected gradient ascent-descent with momentum.  The authors present rates on their algorithm that are close to earlier lower bounds and conclude the paper with a number of experiments with ridge regression on a variety of instantiations of spectral risks and datasets, demonstrating that their approach is generally superior to alternatives.

### Strengths
This paper sets out an interesting problem that has some (at least distant) applications to relevant areas in ML including risk sensitivity, fairness, and generalization OOD.  The proposed solution of reducing to a minimax game and then running a primal-dual algorithm is interesting and the empirical validation uses a reasonable diversity of datasets and loss functions that suffices to convince me that the proposed algorithm is superior to alternatives, at least when considering ridge regression.

### Weaknesses
There are several main weaknesses with the paper:

1. With respect to the theory, I think more discussion of the strongly convex regularizer is necessary.  I understand that it is necessary in order to ensure identifiability, but I find the discussion under Corollary 1 confusing.  For example, in the comparison to related work, the authors cite several works that set the regularization term to be $O(\epsilon)$ in order to be $\epsilon$-suboptimal with respect to the unregularized solution and note that this leads to a worse sample complexity of $O(1/\epsilon)$; I am confused as to why the current proposal does not suffer the same drawback.  Indeed, in order to be $\epsilon$-suboptimal with respect to the unperturbed spectral risk, it seeems as if the bound in Corollary 1 would scale with $\epsilon^{-3/2}$ which is obviously worse than the alternative. The authors should clarify the role of the strong convexity parameter $\mu$ in the convergence rate and how it interacts with the desired accuracy $\epsilon$. It's unclear if the algorithm's performance is robust to different choices of $\mu$ and how this parameter should be tuned in practice. Furthermore, the theoretical analysis does not explicitly address the impact of the regularization parameter on the final solution's optimality with respect to the original, unregularized spectral risk minimization problem.

2. I think a more thorough discussion of the computational complexity of SOREL is in order.  While I understand that for most steps, the gradient updates are cheap and independent of $n$, lines 2, 7, and 11 of Algorithm 1 require linear in the number of samples time.  The authors claim that these steps are for variance reduction, but do not investigate the necessity thereof.  Another way of saying this is that the authors claim almost optimality of their algorithm in how the iteration complexity scales with $\epsilon$ but it seems like the dependence on $n$ is also fairly important (and is what motivates the study itself) and the extent to which the authors' algorithm is optimal in this respect is left largely undiscussed. The analysis should explicitly state the dependence of the overall runtime on both $n$ and $\epsilon$, and discuss the trade-offs between these two factors. The authors should also investigate the possibility of using more efficient techniques for the steps that require $O(n)$ time, such as stochastic approximations or sampling methods, to reduce the computational burden.

3. The experiments are all restricted to linear models.  While I understand that the authors wish to ensure that their key Assumption 1 is satisfied, it would be nice if they considered something nonlinear as well.  This is especially true because they remove the regularization in their experiments anyhow and thus are at least somewhat happy to depart from their theory.

### Questions
1. Can you define `total sample complexity' in Corollary 1 please?  Is this the sum of calls to a stochastic gradient oracle?  It would be helpful if this were made rigorous as my understanding of the key contribution of the present work is that the dependence in complexity on the number of samples is reduced substantially.

2. See weaknesses 1 and 2.

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
5

### Summary
The paper presents SOREL, an optimization algorithm designed for spectral risk measure objectives, which can also be understood as  primal-dual min-max objectives for learning problems. In comparison to previous stochastic methods, the algorithm adds a proximal term to the dual update and claims a near-optimal convergence guarantee for the strongly convex-(nonstrongly) concave variant of this objective. The method employs an SVRG-style variance reduction similar to [Mehta et al. (2023)](https://proceedings.mlr.press/v206/mehta23b.html). While SOREL generally performs favorably in experiments, the theoretical convergence analysis is incorrect, making this work unpublishable in its current state.

### Strengths
- The paper points out an important fact about the analysis of algorithms for "smoothed" spectral risk measures, which is that when the smoothing parameter $\nu = O(\epsilon)$, it should be included in the complexity guarantee, making "linearly convergent" methods sublinear for the original non-smooth problem.
- By using the experimental benchmark of [Mehta et al. (2024)](https://arxiv.org/pdf/2310.13863), the authors are able to perform head-to-head comparisons to  recent algorithms designed for spectral risk measures (Figure 3).  The empirical performance is competitive with, and often outperforms, other methods.
- The exposition is clear and well-written, although some sections are nearly identical to sections in the referenced work on spectral risk measure optimization with stochastic algorithms (Section 1, Section 2, Appx B).

### Weaknesses
Upon viewing Corollary 1, we see that the complexity contains the term $\log(\frac{\sqrt{n}G}{\mu^2\sqrt{\epsilon}})$, i.e. a logarithm is taken for a quantity that is *not* unitless. This does not pass a basic sanity check for convergence analyses in optimization theory: that the complexity does not depend on the units of the input. The error comes from the fact that the precision parameter $\delta_k$ in the inner loop is dependent on the strong convexity parameter $\mu$ (units of loss/inputs$^2$) when it should be in units of loss (based on Lemma 3). To see why this is invalid, recall that an optimization algorithm should not change its exact complexity when the inputs are reparametrized in different units. Consider the objective as a function of $\boldsymbol{w}/10$ instead of $\boldsymbol{w}$. Then, we have the Lipschitz and strong convexity constants change as $G \mapsto 10G$ and $\mu \mapsto 100\mu$. Then,
$$
\frac{\sqrt{n}(10G)}{(100\mu)^2\sqrt{\epsilon}} = \frac{1}{1000}\frac{\sqrt{n}G}{\mu^2\sqrt{\epsilon}}.
$$
This indicates that the number of iterations in the inner loop would change based on the scale, which is not a valid analysis. Please check the units before presenting the result.

Matters such as significance, novelty, and impact come second to the analysis, especially as the experimental results do not show a large practical improvement over the methods of [Mehta et al. (2023)](https://proceedings.mlr.press/v206/mehta23b.html) and [Mehta et al. (2024)](https://arxiv.org/pdf/2310.13863). Please correct the analysis.

### Questions
n/a

### Soundness
1

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces SOREL, a stochastic gradient-based algorithm for spectral risk minimisation. After an introduction and an overview of this work, the authors carefully present the current drawbacks of current approaches of spectral risk minimisation alongside their new algorithm in Section 3. Section 4 provide convergence guarantees, and Section 5 gathers various experiments showing competitive performance and computational time with respect to existing methods.

### Strengths
- Sections 1, 2 and 3.1 are truly well-written, it has been a pleasure to read it
- The idea of using a primal dual method based on Lemma 1 of (Blondel et al. 2020) is clever and elegant
- Algorithmic performances are convincing and are accompanied by sound theory
- It is great to propose a mini batching version of SOREL

### Weaknesses
 - You wrote in your abstract that there is a lack of guarantees for the original spectral risk. You said later in l.78 that SOREL is the first stochastic algorithm with convergence guarantees for the spectral risk minimisation problem. However, in Section 3.1 you directly consider a regularised version of the spectral risk with a strongly convex function (Eq. 1). Later, in Eq. (4) you added another regulariser in $\mathbf{\lambda}$ to avoid huge variations of $\lambda$ during the learning process. All of these reason suggests that you actually do NOT deal with the original spectral risk. Do I miss something?
- l. 268-269 : Those lines are unclear, I do not under whether there is a need to compute $\mathcal{O}(n\log(n))$ operations at line 5, within the loop of line 3 in Algorithm 1 or if this is the total number of computations. Can you explicitly write the time complexity of your algorithm and compare it with those proposed in literature? This would draw a useful theoretical link to understand why your algorithm is faster than others in Section 5.
- I am not sure to understand why Lemma 1 is stated here, as there is no proof sketch in the main document. What do I miss?
- In Theorem 1, can you please define $w^*$? I do not understand what it is.
- In Section 5, it seems that you focused exclusively on linear regression, would SOREL work with small neural nets with 1-2 hidden layers? Even if theoretical guarantees may not hold anymore, I am curious to know whether the methods remain tractable and efficient.

### Questions
- You wrote in your abstract that there is a lack of guarantees for the original spectral risk. You said later in l.78 that SOREL is the first stochastic algorithm with convergence guarantees for the spectral risk minimisation problem. However, in Section 3.1 you directly consider a regularised version of the spectral risk with a strongly convex function (Eq. 1). Later, in Eq. (4) you added another regulariser in $\mathbf{\lambda}$ to avoid huge variations of $\lambda$ during the learning process. All of these reason suggests that you actually do NOT deal with the original spectral risk. Do I miss something?
- l. 268-269 : Those lines are unclear, I do not under whether there is a need to compute $\mathcal{O}(n\log(n))$ operations at line 5, within the loop of line 3 in Algorithm 1 or if this is the total number of computations. Can you explicitly write the time complexity of your algorithm and compare it with those proposed in literature? This would draw a useful theoretical link to understand why your algorithm is faster than others in Section 5.
- I am not sure to understand why Lemma 1 is stated here, as there is no proof sketch in the main document. What do I miss?
- In Theorem 1, can you please define $w^*$? I do not understand what it is.
- In Section 5, it seems that you focused exclusively on linear regression, would SOREL work with small neural nets with 1-2 hidden layers? Even if theoretical guarantees may not hold anymore, I am curious to know whether the methods remain tractable and efficient.

### Soundness
3

### Presentation
3

### Contribution
3

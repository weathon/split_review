# Faster Sampling from Log-Concave Densities over Polytopes via Efficient Linear Solvers

- Decision: Accept
- Scores: 8, 8, 8, 3

## Abstract
We consider the problem of sampling from a log-concave distribution $\pi(\theta) \propto e^{-f(\theta)}$ constrained to a polytope $K:=\{\theta \in \mathbb{R}^d: A\theta \leq b\}$, where $A\in   \mathbb{R}^{m\times d}$ and $b \in \mathbb{R}^m$. 
The fastest-known algorithm \cite{mangoubi2022faster} for the setting when $f$ is $O(1)$-Lipschitz or $O(1)$-smooth runs in roughly $O(md \times md^{\omega -1})$ arithmetic operations, where the $md^{\omega -1}$ term arises because each Markov chain step requires computing a matrix inversion and determinant (here $\omega \approx 2.37$ is the matrix multiplication constant). 
We present a nearly-optimal implementation of this Markov chain with per-step complexity which is roughly the number of non-zero entries of $A$ while the number of Markov chain steps remains the same. The key technical ingredients are 1) to show that the matrices that arise in this Dikin walk change slowly, 2) to deploy efficient linear solvers that can leverage this slow change to speed up matrix inversion by using information computed in previous steps, and 3) to speed up the computation of the determinantal term in the Metropolis filter step via a randomized Taylor series-based estimator. 
This result directly improves the runtime for applications that involve sampling from Gibbs distributions constrained to polytopes that arise in Bayesian statistics and private optimization.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies sampling from a logconcave distribution on a polytope. To this end, it uses a soft-threshold Dikin walk introduced in MV22. The paper signficantly improves upon the per iteration cost by applying the inverse maintenance techniques from LS15 and LLV20. The technical contribution is in showing how to apply these to the soft-threshold logbarrier.

### Strengths
I wasn't able to check the proofs, but the results suggest that the paper overcomes a technical difficulty prior works such as LS15, MV22, and LLV20 hadn't been able to address. Specifically, showing that the soft threshold logbarrier Hessian is slow-changing in a certain norm is a novel contribution of the paper, and it has consequences to improving the runtime of what is clearly an important problem.

-------- 

After rebuttal: I'm increasing my score and confidence.

### Weaknesses
I think the paper is, currently, not as self-contained as it should be. I believe this is easily fixable by adding relevant background material in the appendix. I also believe perhaps there may not be too much relevance of this paper in ICLR, and the paper would be much better appreciated in the theoretical CS community's conferences such as SODA, COLT, etc. Perhaps it would be helpful to state a more direct connection to ICLR.

### Questions
-

### Soundness
3 good

### Presentation
2 fair

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
The paper studies a fundamental problem of sampling from convex sets, the problem of sampling with respect to a log-concave distribution. Previous work [Mangoubi-Vishnoi, NeurIPS'22] has given an algorithm with $O^*(md)$ iteration and each iteration takes $O^*(md^{\omega-1})$ time. In this paper, the author improves the cost per iteration to $O^*(nnz(A)+d^2)$. This result directly answers the open problem proposed in [Lee-Sidford15, FOCS'15] which asks whether one can achieve such running time for the case $f\equiv 0$. To achieve this, the authors make use of the inverse maintenance technique in  [Lee-Sidford15, FOCS'15] and show one can compute the estimation of determinant to high accuracy by cleverly constructing an unbiased estimator and making use of the linear system solver as a primitive.

### Strengths
My general evaluation of this paper is very positive.  I did not manage to check the correctness of the proofs. Condition on the new Metropolis update rule and the log-determinant estimator is correct, I think everything goes through. This paper is technically solid and answers an important open problem.

### Weaknesses
I think the primary weakness of this paper is the presentation. I understand that due to the nature of theory papers, it's hard to present everything important within the page limits. The most interesting part of the paper  for me is how to get a good estimation of log-determinant and I think it deserves some space in the main paper.

### Questions
-

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents the current fastest algorithm for sampling from a log-concave distribution over a given polytope. In particular, they implement a more optimized version of the algorithm proposed by Mangoubi and Vishnoi [1], which is to appear in NeurIPS 2023, the arXiv version of which has been around for more than a year at this point. It is important to understand what [1] does, as the current paper heavily builds on it... 

The algorithms considered in these papers are Metropolis-Hastings algorithms, which are a subclass of Markov chain Monte Carlo (MCMC) methods. For each step of the Markov chain, [1] needs time $O(md^{\omega-1})$ as it involves some matrix inversion and determinant computation steps, which can all be done in $O(md^{\omega-1})$ time by using algorithms for these problems which work for arbitrary matrices. The main claim in the current paper is that instead of recomputing these matrix operations from scratch in every step of the Markov chain, we can use the information from the previous step to speed up the computations of the current step.

References:

1: Sampling from Log-Concave Distributions over Polytopes via a Soft-Threshold Dikin Walk, Mangoubi, Oren and Vishnoi, Nisheeth K, arXiv preprint arXiv:2206.09384. To appear in NeurIPS 2023: https://neurips.cc/virtual/2023/poster/72502

### Strengths
Significance: The problem of sampling from a log-concave distribution over a polytope is interesting and also has several ML applications.

Originality: Clearly, the paper is an advance over the state-of-the-art. However, I am not super sure about how original this is in terms of technical contributions...

Clarity: Paper is clear but a bit dense and slightly hard to read, especially if you are not already familiar with Mangoubi and Vishnoi [1]. I re-read this paper after reading [1] and it was much clearer the second time. It might have to do with space-constraints, as the arXiv version of [1] obviously has more space so can go over a lot of things in more detail...

Quality: Overall seems to be of good quality. But I have not checked the correctness of the technical details. As it builds quite heavily on [1] and also a bunch of other results which I am not familiar with, I don't have the expertise to ascertain the correctness of the paper. But at least on the surface, it does seem like there are no major technical issues.

### Weaknesses
I don't have too much to point here, except what I already wrote about clarity before. The authors should try to make the paper more accessible to people who might not have read [1]. Specifically, the paper could benefit from a more comprehensive introduction to the soft-threshold Dikin walk, as the current description may be too concise for readers unfamiliar with this specific Markov chain. I know this is a generic remark but honestly I have no clear idea how to improve the paper in terms of clarity. There were a bunch of typos here and there, some of which are:

In Theorem 2.1, 3) convex function $f:K \mapsto \mathbb{R}^d$. Here $f$ should be $K \mapsto \mathbb{R}$. The codomain of the convex function $f$ is incorrectly specified. It should map to $\mathbb{R}$, not $\mathbb{R}^d$. I saw this repeated in a bunch of other places. I think it's a typo but since I saw it repeatedly, both in this paper, and also in [1], I tried to dig around to see if it makes sense for the codomain of a convex function to be $\mathbb{R}^d$ instead of $\mathbb{R}$ but in that case, $e^{-f}$ would not be real, but it has to be real for it to be a probability density function?

Page 5, line 3: ball "or" radius -> ball of radius, again: $f: K \mapsto \mathbb{R}^d$

Page 7, two lines below inequality (3): “arithemtic”

### Questions
No additional questions

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper considers using a soft-threshold Dikin walk to sample from a polytope contained in a box of radius $R$. The sampling distribution is log-concave and specified by a Lipschitz/smooth function $f$. By using a pipeline introduced in [LLV20], they show how to speed up the algorithm introduced in [MV23] so that each iteration, instead of computing the Hessian of log-barrier using fast matrix multiplication, one can resort to the inverse maintenance data structure due to [LS15]. To this end, they achieve a similar per iteration cost as [LLV20], namely $\mathrm{nnz}(A)+d^2$.

### Strengths
This paper improves the per iteration cost of [MV23] from $md^{\omega-1}$ to $\mathrm{nnz}(A)+d^2$. In most regimes where $m\geq d$ and $A$ is relatively sparse, this is a strict upgrade from prior state-of-the-art.

### Weaknesses
I'm very dubious of the novelty of this paper. What's the major difference between the algorithm in this paper and [LLV20]? While this paper only mentions [LLV20] sparingly, the algorithmic framework is almost identical. Specifically, [LLV20] shows that for sampling uniformly over a polytope with log-barrier, one can use the [LS15] inverse maintenance to compute a new sampling point. The determinant ratio term can be estimated via an unbiased estimator, which can further be estimated using Taylor expansion together with terms that can be quickly computed using the inverse maintenance data structure. The only difference is that this paper also needs to handle the regularization term, but it is neither surprising nor novel the machinery of [LLV20] also works here. 

It is worth noting that [LLV20] does not provide any proof on why using an approximate solver and samples, the algorithm still converges. This paper provides a very simple argument to show it indeed works.

Overall, I think this paper should provide comprehensive comparison with algorithm in [LLV20]. What's the difference here? What's new? Otherwise, it should acknowledge that the algorithm is largely derivative from [LLV20]. In its current writing, the authors acknowledge the fast linear solver part follows from [LLV20]. What about the determinant ratio part? What's the main difference between your approach for determinant and [LLV20]? What's the novelty of your algorithm?

### Questions
See weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

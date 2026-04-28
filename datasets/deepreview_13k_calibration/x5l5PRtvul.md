# Hybrid Kernel Stein Variational Gradient Descent

- Decision: Reject
- Avg Score: 6.25
- Scores: 8, 5, 6, 6

## Abstract
Stein variational gradient descent (SVGD) is a particle based approximate inference algorithm. Many variants of SVGD have been proposed in recent years, including the hybrid kernel variant (h-SVGD), which has demonstrated promising results on image classification with deep neural network ensembles. In this paper, we demonstrate the ability of h-SVGD to alleviate variance collapse, a problem that SVGD is known to suffer from. Unlike other SVGD variants that alleviate variance collapse, h-SVGD does not incur additional computational cost, nor does it require the target density to factorise. We also develop the theory of h-SVGD by demonstrating the existence of a solution to the hybrid Stein partial differential equation. We highlight a special case in which h-SVGD is a kernelised Wasserstein gradient flow on a functional other than the Kullback-Leibler divergence, which is the functional describing the SVGD gradient flow. By characterising the fixed point in this special case, we show that h-SVGD does not converge to the target distribution in the the mean field limit. Other theoretical results include a descent lemma and a large particle limit result. Despite the bias in the mean field limiting distribution, experiments demonstrate that h-SVGD remains competitive on high dimensional inference tasks whilst alleviating variance collapse.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper proposed studied the theoretical foundation of the hybrid kernel Stein variational gradient descent (h-SVGD) method, which is a variant of the vanilla SVGD method. Specifically, the authors demonstrated the ability of h-SVGD to alleviate variance collapse, and showed the existence of a solution to the hybrid Stein partial differential equation for h-SVGD. They also showed that h-SVGD does not converge to the target distribution in the mean field limit. Experiments have been provided to show the promising properties of h-SVGD.

### Strengths
1. The theoretical foundation of h-SVGD is established, which is new and important to this research topic.

2. Besides the new results, some existing results are proved with relaxed and more practical assumptions.

### Weaknesses
To be honest, since I am not familiar with the mathematical tools used in this work, I can only judge the paper based on what the authors have done, as they claimed, and I cannot say much about its weaknesses.

### Questions
No further questions.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper explores the theoretical understanding of the hybrid kernel variant of Stein variational gradient descent (h-SVGD). Specifically, it provides a kernelized Wasserstein gradient flow representation for h-SVGD and, building upon this, offers the dissipation rate and large particle limit of h-SVGD. In numerical experiments, the authors demonstrate that h-SVGD significantly improves variance collapse compared to vanilla SVGD.

### Strengths
- This paper provides a relatively comprehensive theoretical foundation for the empirical method hybrid kernel variant of SVGD.
- This paper offers a clear explanation of the relationships and distinctions between the theoretical results of h-SVGD and those of SVGD.

### Weaknesses
 - The experimental results presented in the paper offer relatively limited support. In results on the Protein and Kin8nm datasets, SVGD does not appear to suffer from variance underestimation issues, yet its performance is still inferior to that of h-SVGD. This observation suggests that the advantage of h-SVGD in BNN tasks may not primarily stem from mitigating variance underestimation.

 - The result in Corollary 3.4 indicates that h-SVGD does not guarantee the distribution of particles converges to the target distribution. While this is reasonable, the metrics commonly used in Bayesian Neural Network (BNN) tasks, such as test RMSE and test LL, do not reflect this limitation. This raises the question of how to interpret the advantages of h-SVGD despite this theoretical constraint. Furthermore, the annealed posterior, which is the limiting distribution of h-SVGD, is known to be a suboptimal estimator with respect to MSE, yet it appears to perform better in practice for BNN tasks. This discrepancy requires further investigation and explanation.

### Questions
- The result in Corollary 3.4 indicates that h-SVGD does not guarantee the distribution of particles converges to the target distribution. While this is reasonable, the metrics commonly used in Bayesian Neural Network (BNN) tasks, such as test RMSE and test LL, do not reflect this limitation. This raises the question of how to interpret the advantages of h-SVGD despite this theoretical constraint.

### Soundness
2

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
Ths paper gives more theoretical insights about a sampling method named hybrid kernel stein variational gradient descent (h-SVGD). It is demonstrated that this method effictively sample a law which is not the target law (but linked to it). Moreover, it provides a descent result and a discretization quantification. Finally, it presents experiments that show the empirical interest of h-SVGD.

### Strengths
The paper provides interesting theoretical results on h-SVGD. It extend the known results on SVGD to h-SVGD. The experimental results effectively support the interest of h-SVGD.

### Weaknesses
Major weaknesses:
- Assumption (A1) does not seem to be well written. To suppose that $\lim_{|x|\to +\infty} V(x) = +\infty$ must be a more realistic assumption to ensure that $\pi$ could be a probability measure. Is it a writting error ?
- There is a few intuitions and comments in the paper, making the paper hard to read. In particular, I suggest to discuss the assumptions in details. A reminder on Wasserstein gradient flow will be appreciable. Finally, Proposition 3.6 is not comment.

Minor weaknesses:
- Equation 6 : there is a typo, it might be $(x, \cdot)$ instead of $(\cdot, x)$.
- line 198 : in the paper notations, it might be $\mathcal{H}$ instead of $\mathcal{H}_1$.
- The remark in line 246 seems inconsistent because Assumption (A1) induce that $V$ is bounded.
- In line 250, the constant $L$ is said to be dependent of $k_1, k_2$ and $p$. However it is not clear what is the variable $p$.
- In line 329, the normal density do not verify Assumption (A1). In fact in this case $V$ is quadratic.
- line 226, I suggest to be more precise about the sense of "symetric function" in this context.

### Questions
- In Assumption (A2), the first part can be deduce from Assumption (A1). In fact, Assumption (A1) induce that $V$ is bounded. Why do you precise this assumption ?
- Can you give an interpretation of the second part of Assumption (A2) ?
- Can you give an interpretation of Assumption (A3) ?
- Do you have examples of potentials $V$ that verifies Assumptions (A1)-(A2)-(A3)-(A4) ?
- According to your analysis of h-SSVD you have a proposition of a sampling strategy that does not suffer from dimensional collaps and sample the right distribution ?

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper discusses h-SVGD as a method to address variance collapse by using separate kernels for the driving and repulsive terms. The authors extend the theoretical aspects of the original paper and demonstrate that h-SVGD does not converge to the target distribution in the mean field limit. The empirical results support the theoretical findings.

### Strengths
- Theoretical contributions are rigorous and sound, including the existence of a solution to the hybrid Stein PDE and the establishment of the descent lemma. A kernelised Wasserstein gradient flow interpretation is thoroughly discussed with $k_2 = ck_1$.
- The experiments involve diverse datasets and metrics.
- The representation of experiments is clear and the paper is well-structured.
- Good to quantify that h-SVGD does not add additional computational costs to SVGD.

### Weaknesses
 - The title may be a bit misleading as it suggests that h-SVGD is a novel algorithm introduced in this paper, but it was previously proposed. For instance, it can reflect the paper's focus on theoretical analysis and empirical evaluation of h-SVGD, rather than introducing it as a new method.
- The main focus on $k_2 = ck_1$ may be somewhat limiting, as it potentially restricts the exploration of using truly distinct kernels for the driving and repulsive terms. While the paper does explore the case of two RBF kernels with different bandwidths, it does not delve into the implications of using kernels from entirely different families, which could offer further insights into the behavior of h-SVGD.
- While RMSE and LL have been assessed in Appendix B, h-SVGD does not show clear benefits over SVGD in these metrics. It would be better to provide a more detailed discussion in the main text about why DAMV is an appropriate metric for evaluating h-SVGD's performance, especially in relation to the variance collapse problem. The current justification for using DAMV is not sufficiently clear, and a more thorough explanation of its relevance is needed to convince the reader of its validity.
- Using "S-SVGD" and "SSVGD" interchangeably is slightly confusing and could be more consistent.

### Questions
- The authors mention convergence issues in the mean field limit. Are there any ways to mitigate this bias?
- The authors focus on $k_2 = ck_1$ case. Have they tried using two completely different kernels?
- The authors reference h-SVGD's promising results on image classification. Have they conducted similar experiments in this paper?
- From an applications perspective, why is it important to avoid variance collapse?

### Soundness
3

### Presentation
3

### Contribution
3

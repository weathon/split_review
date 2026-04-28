# Stability and Sharper Risk Bounds with Convergence Rate $O(1/n^2)$

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 8, 5, 5

## Abstract
The sharpest known high probability excess risk bounds are up to $O\left( 1/n \right)$ for empirical risk minimization and projected gradient descent via algorithmic stability (Klochkov \& Zhivotovskiy, 2021). In this paper, we show that high probability excess risk bounds of order up to $O\left( 1/n^2 \right)$ are possible. We discuss how high probability excess risk bounds reach $O\left( 1/n^2 \right)$ under strongly convexity, smoothness and Lipschitz continuity assumptions for empirical risk minimization, projected gradient descent and stochastic gradient descent. Besides, to the best of our knowledge, our high probability results on the generalization gap measured by gradients for nonconvex problems are also the sharpest.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Th authors of the paper obtain high probability excess risk bounds of order up to $\mathcal{O}(1/n^2)$ (up multiplicative logarithmic factors) for both empirical risk minimization problems and gradient descent algorithms. Towards this aim, the authors consider uniform stability in gradients instead of uniform stability of the loss function itself.

### Strengths
The paper is well-written and main contributions are clearly articulated. The fact that the bounds for ERM and SGD setting do not require lower bounding the sample size $n$ in terms of the problem dimension $d$ is also a significant improvement, for example, over, [Xu & Zeevi, 2024].

### Weaknesses
The technical novelty of the results is limited. Essentially the proof is based on an appropriate combination of [Zhang & Zhou, 2019] and [Klochkov & Zhivotovskiy, 2021]. Specifically, the core argument seems to follow the stability analysis framework of [Zhang & Zhou, 2019] but applied to gradients rather than the loss function itself, and then leverages techniques from [Klochkov & Zhivotovskiy, 2021] to obtain the final bounds. Moreover, the excess risk of order $\mathcal{O}(1/n^2)$ can be obtained only in the setting $F(w*) = \mathcal{O}(1/n)$, that is, provided that the noise-at-the-optimum is rather small. This is a significant restriction, as it requires the population risk at the optimal parameter to decrease at a rate of $1/n$, which is not always realistic. The tail bound of order $\log^2(1/\delta)$ in Theorems $4$ - $6$ (in front of $1/n^2$ terms) also seems to be not optimal. For example, this $\log^2(1/\delta)$ regime does not appear in [Klochkov & Zhivotovskiy, 2021], and it is unclear why the authors cannot achieve a tighter tail bound, especially given that the core proof techniques are similar.

### Questions
Is it possible to improve scaling of the right-hand side in Theorems $4-6$ with $\log(1/\delta)$?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors provide dimension-free, $O(1/n^2)$-rate generalization bounds for learning algorithms with uniformly stable gradients. This is applicable to the ERMs of sufficiently well-behaved risk functions, as well as the gradient descent iterates of sufficiently well-behaved objective functions.

### Strengths
- As summarized in Table 1 (which is very informative), the bounds for ERM, PGD, and SGD are indeed the sharpest in the literature, in particular in terms of the sample complexity.

- Overall the paper is very clearly written, including proof sketch, comparison etc.

### Weaknesses
 - Given the impressive results I do think this is a very minor weakness, but the technical novelty is indeed not *that* compelling. The main result is mostly derived from applying Klochkov and Zhivotovskiy's techniques to a more restrictive (in the sense of problem well-behavedness constraints) and more general (in the sense of studying the "oracle" $A$) set-up. This might potentially bar the paper from entering the conference highlight.

 - Given the impressive results, the paper's analysis relies on strong assumptions about the objective function, such as Lipschitz continuity, strong convexity, and smoothness. While these assumptions are common in theoretical analysis, they may not hold in many practical scenarios, limiting the applicability of the results. For example, in deep learning, loss functions are often non-convex and may not satisfy these conditions globally. The paper should discuss the limitations of these assumptions in more detail and perhaps explore potential extensions or modifications to handle more general cases.


### Questions
- Can the authors briefly comment on the implications for 1-dimensional mean estimation (w/ empirical mean, M-estimators, etc.)? This might be a good illustrative example.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents high-probability generalization bounds based on stability analysis. To this aim, the paper first presents a moment bound for sums of vector-valued functions of independent variables. Based on this, the paper gives a high-probability bound on the difference between the gradients of population risks and the gradients of empirical risks. This further implies excess risk bounds under a PL condition. The paper shows that this risk bound can be of order of $O(1/n^2)$ under some conditions. Further applications to empirical risk minimization, gradient descent and stochastic gradient descent are also given.

### Strengths
- The paper shows improved generalization bounds based on stability analysis. The paper gives clear comparison with existing results. For example, Remark 4 and Remark 7 show the advantage of the derived generalization bounds over the existing results in Fan & Lei 2024 and Xu & Zeevi (2024).
- The paper also shows improved excess risk bounds over the existing results. For example, in Remark 9, the paper shows that the results outperform those in Zhang & Zhou by removing the dependency on the dimensionality. In Remark 11, the paper shows that it is better than Klochkov & Zhivotovskiy (2021) by allowing for rates of order $O(1/n^2)$.

### Weaknesses
 - While the rates of order $O(1/n^2)$ are interesting, it seems that the bounds have another linear dependency on $1/\mu^2$. For example, according to proof of Theorem 4, there is a missing factor of $1/\mu^2$ in each term on the right-hand side of the bound. Note $\mu$ is the PL parameter and can be very small in practice. This can make the derived bound less interesting in practice. Specifically, the dependence on $1/\mu^2$ in the bounds, while potentially hidden within the constants, can dominate the convergence rate when $\mu$ is small, which is common when the loss function is not strongly convex or is ill-conditioned. This is a critical issue because the practical utility of the $O(1/n^2)$ rate is significantly diminished if it is accompanied by a large constant factor due to the $1/\mu^2$ term.
- For applications in Section 4, the paper considers strongly convex problems. There is an assumption that $n\geq 16\gamma^2\log(6/\delta)/\mu^2$, which amounts to saying that $\mu \geq 4\gamma\log^{1/2}(6/\delta)/\sqrt{n}$. Note that typically one needs to introduce a strongly convex regularizer to get strong convexity. However, one is mostly interested in the original loss function without the regularizer. While the paper shows improved rates for the loss with the regularizer, the requirement $\mu \geq 4\gamma\log^{1/2}(6/\delta)/\sqrt{n}$ makes the rate for the loss without the regularizer still not fast. The strong convexity assumption, while simplifying the analysis, limits the applicability of the results to a narrow class of problems. In practice, many loss functions are not strongly convex, and the introduction of a regularizer, while ensuring strong convexity, alters the original problem. The requirement on $\mu$ further restricts the practical relevance of the results, as it imposes a lower bound on the regularization parameter that is dependent on the sample size, potentially hindering the ability to achieve fast rates for the original loss.
- For SGD, in Remark 13 the paper requires $T=n^4$ to get good bounds. This requirement on the number of iterations is a bit large. Then, the computational cost may be huge in this case. The need for $T = n^4$ iterations to achieve the stated bounds raises concerns about the computational feasibility of the proposed approach. Such a large number of iterations can be prohibitive in practice, especially for large-scale datasets, making the theoretical results less applicable to real-world scenarios. The computational cost associated with this requirement is a significant drawback that limits the practical impact of the findings.

### Questions
- Can the results in Section 4 guarantee fast rates for the original loss without the regularizer? That is, whether we can transform the generalization bounds in Section 4 to get fast rates on the decay of the population risk without the regularizer?
- Lemma 3 is a bit strange. The left hand side involves w_t^i and w_t. However, the right-hand side only involves $\epsilon(w_t)$. The authors should check it.

Minor comments:
- "under strongly convexity" in Abstract
- $w^*$ is not defined in the introduction
- "inequality which provide" in Section 3

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper studied the algorithmic stability of the empirical risk minimization,  projected gradient descent, and SGD in the high probability form.
In particular, the authors show that  the rate $1/n^2$ can be achieved when the objective function is smooth and satisfied the PL condition (strongly convexity). The obtained results seems to the first of its kind in the literature.

### Strengths
1. The paper seems to be the first-ever-known fast rate in high probability in the framework of algorithmic stability.

2.  The paper is generally well written with good organization.

### Weaknesses
1.  While the results obtained are new and interesting, the proof techniques heavily reply on the existing literature (Klochkov & Zhivotovskiy, 2021) and specially Fan and Lei (2024). For instance, Theorem 1 is a refined version of Theorem 3 in Fan and lei (2024) by observing that the absolute constant  $M$ there can be replaced by the variance of the gradients of the loss.  The authors may need to further highlight  other technical novelty in the proof. 

2.  The existing literature on the fast rates for SGD using stability approach often focused on the one-pass SGD, i.e., $T=n$. Although the fast rate was obtained in this paper for SGD with PL and smooth condition here,  the paper needs high gradient complexity, i.e. $T=n^2$.  In this case, there is a compromise here to achieve fast rate $1/n^2$ there.

### Questions
NA

### Soundness
2

### Presentation
3

### Contribution
2

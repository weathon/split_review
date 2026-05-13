# f-FERM: A  Scalable Framework for  Robust Fair Empirical Risk Minimization

- Decision: Accept
- Scores: 5, 8, 6, 5

## Abstract
\vspace{-2mm}
Training and deploying machine learning models that meet fairness criteria for protected groups are fundamental in modern artificial intelligence. 
While numerous constraints and regularization terms have been proposed in the literature to promote fairness in machine learning tasks, most of these approaches are not amenable to stochastic optimization due to the complex and nonlinear structure of constraints and regularizers. Here, the term ``stochastic'' refers to the ability of the algorithm to work with small mini-batches of data. Motivated by the limitation of existing literature, this paper presents a unified stochastic optimization framework for fair empirical risk minimization based on $f$-divergence measures ($f$-FERM). The proposed stochastic algorithm enjoys theoretical convergence guarantees. In addition, our experiments demonstrate the superiority of fairness-accuracy tradeoffs offered by $f$-FERM for almost all batch sizes (ranging from full-batch to batch size of one). Moreover, we show that our framework can be extended to the case where there is a distribution shift from training to the test data. 
Our extension is based on a distributionally robust optimization reformulation of $f$-FERM objective under $\ell_p$ norms as uncertainty sets. Again, in this distributionally robust setting, $f$-FERM not only enjoys theoretical convergence guarantees but also outperforms other baselines in the literature in the tasks involving distribution shifts.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper first presents a framework for fair ERM using f-divergence. Next, the authors propose a distributionally robust fair ERM framework, where the ambiguity set is constructed using $\ell_p$-norm. For the theoretical part, a convergence analysis of the stochastic optimization for the ERM formulation is proposed, leveraging the results from Lin et al. (2020). The authors perform comprehensive numerical study to validate the superior performance of their proposed framework.

### Strengths
- The formulation, optimization algorithm, and convergence analysis for the ERM formulation seem correct and novel.
- The numerical study is comprehensive to demonstrate the effectiveness of their proposed algorithm.

### Weaknesses
 - The only novel theoretical part is the convergence analysis of the SGDA for solving the ERM formulation. The corresponding sample complexity for finding $\epsilon$-statariony solution of (f-FERM) is $O(\epsilon^{-8})$. However, I wondered if the authors use the state-of-the-art optimization algorithm for solving nonconvex-concave min-max games and if the sample complexity is currently the optimal one in the literature. If so, the authors should highlight it in the literature. 
- For the distributionally robust formulation (8), the authors used $\ell_p$-norm to model the ambiguity set, but I am afraid that this usage may not be a novel choice because it is not a flexible choice as Wasserstein, $f$-divergece, or MMD, to quantify the difference between distributions. I encourage the authors consider the extension to other choices of ambiguity sets.
- When the ambiguity set of formulation (8) is small, the authors propose a first-order approximation formula to solve it (see Eq.(10)). Although the authors present the approximation error between formula (8) and (10), the complexity for solving Eq.(10) is not presented in this paper.
- When the ambiguity set of formulation (8) is potentially large, the first-order approximation formula may not achieve good performance. To this end, the authors consider another formulation in Section 3.2. However, I have several concerns of the deviation:
  * Can the authors add more details regarding the sentence "One can easily see that the optimal $p_j=\min(\hat{p}_j+\delta, 1)$ and $q_j=\max(\hat{q}_j-\delta,0)$"? It is not obvious for readers to check this point.
  * What is the meaning of the scalar $\delta>0$? It is not introduced. if I remember correctly, in standard f-divergence DRO it is the Lagrangian multiplier corresponding to the probability simplex constraint that needs to be optimized.

### Questions
See the weakness part.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Fairness constraints, such as DP and EO are hard to optimise directly thanks to their discrete nature. Existing bias mitigation approaches propose various differentiable proxies, typically correlation based, such as Zafar et al. They however do not allow unbiased small-batch estimation of the corresponding gradient.

The present paper uses f-divergence as a proxy for independence (they include EO & DP). They introduce a gradient based method, where that has unbiased estimate and therefore allows arbitrary small batch size. In the experiments they use batch size as small as 8. Arguably, this can allow to scale the method to larger problems.

To my knowledge, this paper presents the first theoretical result for gradient based optimisation of fair classifiers.

I want to ask authors to clarify, how do they obtain classifier $ \hat{y}$?
Typically, one obtains differentiable probabilities $p_{\theta}(y = j|x)$, and then maximising the probability yields the classification. However, the expression (4) suggest that the estimator is sampled.
This may harm the accuracy in practice. It is ok to use $F_j$ as a proxy, but it is better if you clarify that explicitly for applied people who may potentially use your method.

Secondly, in Theorem 2.2 the stated convergence time is $O(\epsilon^{-8})$ which seems rather slow. Does it affect the amount of epochs you use in the experiments, is it unusually large?

Thirdly, could you please clarify directly in Proposition 2.2. what is the dimension of variables $A_{jk}$

### Strengths
SGD with unbiased gradient updates for fair classification.

Additional result for robust fair classification.

Theoretical result for SGD for fair classification.

### Weaknesses
 Fairness constraints, such as DP and EO are hard to optimise directly thanks to their discrete nature. Existing bias mitigation approaches propose various differentiable proxies, typically correlation based, such as Zafar et al. They however do not allow unbiased small-batch estimation of the corresponding gradient.

The present paper uses f-divergence as a proxy for independence (they include EO & DP). They introduce a gradient based method, where that has unbiased estimate and therefore allows arbitrary small batch size. In the experiments they use batch size as small as 8. Arguably, this can allow to scale the method to larger problems.

To my knowledge, this paper presents the first theoretical result for gradient based optimisation of fair classifiers.

I want to ask authors to clarify, how do they obtain classifier $ \hat{y}$? Typically, one obtains differentiable probabilities $p_{\theta}(y = j|x)$, and then maximising the probability yields the classification. However, the expression (4) suggest that the estimator is sampled. This may harm the accuracy in practice. It is ok to use $F_j$ as a proxy, but it is better if you clarify that explicitly for applied people who may potentially use your method.

Secondly, in Theorem 2.2 the stated convergence time is $O(\epsilon^{-8})$ which seems rather slow. Does it affect the amount of epochs you use in the experiments, is it unusually large?

Thirdly, could you please clarify directly in Proposition 2.2. what is the dimension of variables $A_{jk}$

### Questions
mentioned in summary

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposed a unified stochastic optimization framework for fair ERM based on f-divergence measures.  The main idea is to reformulate it as a minimax problem using the Legendre-Fenchel conjugate function. This minimax formulation facilitates the development of the standard stochastic gradient descent and ascent algorithms for solving fair ERM. The convergence guarantees are stated in Theorem 2.2 which is mainly a corollary of the results in Lin et al. (2020) since this formulation is concave w.r.t. the dual variable.   The paper also addressed the problem of distribution shift and reformulated it using Lagrangian relaxation as a non-convex and non-concave problem. Extensive experiments are conducted to validate the proposed algorithms.

### Strengths
1. A unified formulation for fair ERM using the f-divergence and then minimax reformulation which facilitates the application of SGDA. 
2.  A robust variant to address the distribution shift
3. Extensive  and convincing experiments

### Weaknesses
1. The proposed unified formulation and its minimax reformulation seem incremental as similar minimax forms have appeared in many existing works of fair machine learning 
2. The convergence analysis is straightforward from the paper by Lin et al. (2020).

### Questions
NA

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new framework for fairness, based on f-divergence and mutual information. This method is called f-FERM. From theory of minimax optimization, it shows the convergence to the optimum of f-FERM. Empirically, f-FERM also shows improvement over existing baselines.

--post rebuttal--
Thank you for the rebuttal and my understanding of this paper got sharpened. I think the fairness definition needs to be clearly stated in the paper, and the uncertainty of which f-divergence seems a bit confusing to me. Unfortunately I cannot change the score based on my point of view.

### Strengths
1. The method is quite straightforward. Suppose the output $y$ and the sensitive attribute $s$ are independent, then the f-Mutual Information term becomes zero. Therefore, the $f$-FERM encourages independence and thus fairness.
2. Using variational bound and convergence theory of minimax, it proves the convergence of SGDA to a stationary point.
3. Experimental results show the improvement of $f$-FERM over existing benchmarks.

### Weaknesses
1. This paper is missing a related reference called TERM (Tilted Empirical Risk Minimization) which also studies fairness.
2. The main formulation (1) could be simplified. The f-divergence between the joint distribution and the product of marginals is called f-mutual information. See https://openreview.net/forum?id=ZD03VUZmRx for example and the references therein.
3. SGDA for minimax optimization is highly inefficient and Theorem 2.2 has a really weak convergence result. How is it related to the experiments?
4. The paper didn't discuss which $f$ (in f-div) is the best choice in detail.
5. All the experiments are conducted on small-scale datasets.
6. The definition of fairness is not clear to me. This paper considers both DP and EO, but which one is what f-FERM is trying to approach?

### Questions
See above.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

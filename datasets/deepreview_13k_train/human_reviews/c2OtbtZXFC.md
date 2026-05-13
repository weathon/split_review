# Retraction-free optimization over the Stiefel manifold with application to the LoRA fine-tuning

- Decision: Reject
- Scores: 8, 5, 3, 3

## Abstract
Optimization over the Stiefel manifold has played a significant role in various machine learning tasks. Many existing algorithms either use the retraction operator to keep each iterate staying on the manifold, or solve an unconstrained quadratic penalized problem. The retraction operator in the former corresponds to orthonormalization of matrices and can be computationally costly for large-scale matrices. The latter approach usually equips with an unknown large penalty parameter. To address the above issues, we propose a retraction-free and penalty parameter-free algorithm, which lands on the manifold. Moreover, our convergence theory allows using constant step size, which improve the result of converging to a neighborhood in \citep{ablin2022fast}.
  A key component of the analysis is the convex-like property of the quadratic penalty of the Stiefel manifold, which enables us to explicitly characterize the constant penalty parameter. As an application, we introduce a new algorithm, Manifold-LoRA, which employs the landing technique and a carefully designed step size strategy to accelerate low-rank adaptation (LoRA) in fine-tuning large language models. Numerical experiments on the benchmark datasets demonstrate the efficiency of our proposed method.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work proposes a novel algorithm for optimization over the Stiefel manifold, eliminating the need for retraction and penalty parameters. The authors introduce a convergence theory that allows for a constant step size, improving upon prior approaches that only ensured convergence to a neighborhood. This method enables efficient, direct optimization on the manifold, addressing key issues in machine learning tasks, such as high computational cost and the need to tune penalty parameters. Experimental results demonstrate the effectiveness of the proposed method.

### Strengths
(1) The most significant contribution of this work is its theoretical establishment of exact convergence for the proposed retraction-free method with a constant step size (though I have not thoroughly checked all proofs in the theory section). This is a promising result compared to the method in Ablin & Peyré (2022), which only converges to a neighborhood whose size depends on the step size.
(2) This work is well-presented.
(3) The experimental results demonstrate that the method not only accelerates the training speed of traditional LoRA but also improves its evaluation metrics.

### Weaknesses
My main concerns with this work is about the experimental section:
1. The authors should make the code for their method available in the supplementary materials during the review period.
2The authors should include comparisons with the existing low-rank fine-tuning methods that incorporate the Stiefel manifold constraint. Without these comparisons, it is unclear whether the improved training speed and evaluation metrics are due to the proposed method itself or the addition of the Stiefel manifold constraint.
3.While the authors compared the number of epochs required for training, but have authors conducted comparisons in terms of actual runtime?

### Questions
See the above

### Soundness
4

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
This work studies a retraction-free manifold optimization algorithm on Stiefel manifold. The authors prove a constant penalty parameter and step size would be enough for exact convergence for the given algorithm. The authors also extend the algorithm to LoRA tuning model and propose manifold-LoRA which they show empirically accelerate LoRA tuning.

### Strengths
The paper studies retraction-free optimization algorithm on Stiefel manifold, which is computationally friendly. Theoretically, improved convergence results are derived compared to prior work, where constant penalty parameter and step size are shown to be enough for exact convergence. Empirically, the authors combine such algorithm with LoRA fine-tuning, discovering an interesting way to posing LoRA as optimization on Stiefel manifold and proposing a new optimization mechanism for LoRA which has been shown to be superior to baseline methods.

### Weaknesses
1. Important related work is missed involving Riemannian Preconditioned LoRA (https://arxiv.org/abs/2402.02347) and DoRA (https://arxiv.org/abs/2402.09353). Also LoRA+ (https://arxiv.org/abs/2402.12354).

To my understanding, Riemannian Preconditioned LoRA studies preconditioners for accelerating LoRA tuning derived from new Riemannian metric, which is in spirit close to current work since both consider the manifold geometry of LoRA. Though one is motivated by a different Riemannian metric and another is motivated by different retraction step. 

DoRA proposes to decompose LoRA weight into magnitude and direction, which is in some sense also close to current work which considers B to be basis of manifold and A to be coordinates.

LoRA+ proposes to use different learning rates for A and B respectively, which is close to discussion right before paragraph 5.

2. Despite empirically verified, it is still not clear why in LoRA tuning, imposing B to be the basis and A to be coordinate would accelerate convergence. Theoretically speaking, they should cover same $X$ space ($X=BA$) and it feels to me vanilla LoRA parameters have more freedom to change compared to constraining $B$ to be on $B^TB=I$

3. Though in theory, the authors show that constant step size is enough, it looks like step size tuning is still needed for the experiments.

### Questions
1. The proposed algorithm has improved convergence result compared to [1]. I appreciate that the authors are making comparisons in Remark 1 and 2, but I'm still not very clear to which extent they are different. I quickly glance at the reference, it seems the algorithm studied is the same? So theoretic novelty exists in the exact convergence result with constant parameters?

2. In line 364-365, the authors mention step size better scales with $||A||_2$ and $||B||_2$, is this used in experiments? Can one just fix step size as  $||A||_2$ and $||B||_2$ in LoRA tuning with the proposed algorithm? How do authors pick step size for comparison in their experiments?



[1] Pierre Ablin and Gabriel Peyre. Fast and accurate optimization on the orthogonal manifold without retraction. In International Conference on Artificial Intelligence and Statistics, pp. 5636–5657. PMLR, 2022.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper presents a retraction-free algorithm for optimization over the Stiefel manifold, a problem that arises in various applications. The algorithm gets rid of the need for computationally expensive retraction and unknown penalty parameters. The framework is then applied to the fine-tuning of large language models,  which aims to accelerate the low-rank adaptation (LoRA) process. Numerical experiments validate the effectiveness and efficiency of the proposed algorithm.

### Strengths
The paper introduces a retraction-free algorithm and identifies the penalty parameter.  The theoretical components in the manuscript appear sound, and the application to the fine-tuning task is novel.  Additionally, a wide range of NLP tasks validate the effectiveness and efficiency of the proposed Manifold-LoRA.

### Weaknesses
I started reading this manuscript with much anticipation, but my enthusiasm was short lived.

1. The contribution of this paper is unclear. Specifically, the proposed update rule (Equation (3) in the manuscript) follows the existing work, e.g. [1,2,3]. Additionally, the landing algorithm on the Stiefel manifold has been proposed in [2], and both the deterministic and stochastic versions on the generalized Stiefel manifold have been studied in [3]. More importantly, the manuscript claims that accommodating a constant penalty parameter is novel. However, a more general result has been established in prior work, e.g. [3, Theorem 2.8], which stated that the landing method provably converges for any fixed penalty parameter.
2. The literature review is insufficient. The manuscript omits two relevant works [2] and [3], where a landing algorithm on the Stiefel manifold was proposed in [2], and both the deterministic and stochastic versions on the generalized Stiefel manifold have been studied in [3].
3.  The paper is not carefully written, with numerous typos influencing the readability (see Questions).

### Questions
1. The landing algorithm has been generalized to the Stiefel manifold and even the generalized Stiefel manifold [2,3]. What is the main difference between the theory in this paper and [2,3]?
2. Based on the analysis, Theorem 1 in the manuscript states the parameter $\mu$ should be $1/3$. However, the penalty parameter in [3] is allowed to be any positive value. Can the author briefly explain the reason?
3. The application in LLMs is novel, but I am confused about the motivation. In detail, the author states that formulation (13) aims to address the redundancy in vanilla LoRA (i.e., the non-uniqueness of $BA$ representations) in line 308 of the manuscript. However, restricting the $B$ matrix in $\mathrm{St}(d,r)$ still introduces non-uniqueness, e.g., setting $BA=(BU)(U^\top A)$ for $U\in\mathcal{O}(r)$.
4. The formulation (13) also adopts the oblique manifold to restrict the variable $B$. However, relevant theory, e.g., a landing algorithm on $\mathrm{Ob}(d,r)$, is not developed in the manuscript, rendering the work not self-contained. 
5. In lines 173 to 174, the author claims Stiefel manifold is 1-proximally smooth, and the projection operator is Lipschitz continuous without proof. In fact, these results serve as a cornerstone for the proof in the Appendix, for which I think they are worth a detailed explanation. Moreover, the second "$X$" in inequality (2) is wrong; it should be corrected by "$Y$".
6. In lines 820 to 821 of the Appendix, can the author provide the details of the "induction"?
7. In line 849 of the Appendix, the sentence "Then by (12), ....... These lead to (12)" is confusing.

[1] Fast and accurate optimization on the orthogonal manifold without retraction. AISTATS, 2022

[2] Optimization flows landing on the Stiefel manifold. IFAC, 2022

[3] Optimization without retraction on the random generalized Stiefel manifold. ICML, 2024

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a retraction-free method for optimization on Stiefel manifolds.

### Strengths
omitted.

### Weaknesses
- Section 2.2 and a large part of Sections 2.1 play no role in the main paper. Why should they be included?
- The update rule (3) of the method is similar to the penalty method at Line 206, with the only difference being that the proposed method uses Riemannian gradients rather than the gradients of the objective. How could the paper justify its advantage over the penalty method? In theory,  I imagine a result similar to Theorem 1 might hold for the penalty method. In practice, the penalty method is easier to implement, and it should be compared in the experiments. This is a fundamental issue that the paper could have addressed better.
- The other important issue is that, while theory does not involve the oblique manifold, the experimental section suddenly begins considering it. Enforcing the constraints of the oblique manifold is so easy that the point in considering a penalty-type method for oblique manifolds is not justified. This is a fundamental contradiction of the paper. Furthermore, Figure 1 and the experiments show that optimization on Stiefel manifolds, as the paper advocates, does not seem to be a strong point because optimization on oblique manifolds is simpler and achieves similar results and the question for authors is: Why should one look for a more complicated method? A sequence of experiments should be designed with relevant baselines in order to justify and motivate the proposed approach. In my opinion, fine-tuning LLMs with LoRA is not a good application scenario for the proposed method; all methods have comparable accuracy.
- Eq. (13) is not rigorous. It suggests optimization over the union of the oblique manifold and the Stiefel manifold, which is the oblique manifold.
- Algorithm 1 (Lines 324 - 348) is out of the blue. The main paper has little introduction to ADAM, and suddenly, many quantities related to ADAM show up in Algorithm 1 without explanation (in particular, Lines 335, 338). There is, therefore, no chance for a novice reader to make sense of Algorithm 1. 
- The comparison in Figure 2 is misleading as I would imagine the computational cost per iteration of the proposed method is higher.

### Questions
See the above.

### Soundness
2

### Presentation
2

### Contribution
2

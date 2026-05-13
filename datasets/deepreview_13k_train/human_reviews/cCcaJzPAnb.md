# Universal Concavity-Aware Descent Rate for Optimizers

- Decision: Reject
- Scores: 3, 5, 5, 3, 3

## Abstract
Many machine learning problems involve a challenging task of calibrating parameters in a computational model to fit the training data; this task is especially challenging for non-convex problems.  Many optimization algorithms have been proposed to assist in calibrating these parameters, each with its respective advantages in different scenarios, but it is often difficult to determine the scenarios for which an algorithm is best suited.  To contend with this challenge, much work has been done on proving the rate at which these optimizers converge to their final solution, however the wide variety of such convergence rate bounds, each with their own different assumptions, convergence metrics, tightnesses, and parameters (which may or may not be known to the practitioner) make comparing these convergence rates difficult.  To help with this problem, we present a minmax-optimal algorithm and, by comparison to it, give a single descent bound which is applicable to a very wide family of optimizers, tasks, and data (including all of the most prevalent ones), which also puts special emphasis on being tight even in parameter subspaces in which the cost function is concave.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This submission introduces a novel concavity-aware optimization framework called ELMO, which adapts the descent rate based on the concavity in different subspaces of the loss function, represented by eigenvalues of the Hessian $\lambda_i$. By leveraging eigenspace-specific Lipschitz constants, $L_i$, the optimizer adjusts its step size dynamically across both convex and concave subspaces, improving descent efficiency. Through theoretical analysis and preliminary experiments, ELMO is shown to provide a versatile and efficient optimization approach with potential advantages over traditional quasi-Newton type methods.

### Strengths
- By focusing on concave subspaces, the work explores a new theoretical direction that could inspire new optimizer designs that perform better on complex, non-convex objectives.

- I checked portions of the appendix proofs, and they are generally correct. Their preliminary numerical experiments validate that the analyzed bounds are meaningful.

### Weaknesses
- While the paper introduces the ELMO algorithm as a theoretically optimal method, there’s a glaring omission of computational complexity analysis in practical scenarios. Specifically, computing the Hessian’s eigendecomposition and Lipschitz constants is computationally intensive. The paper does not address how the cost of these computations scales with the dimensionality of the problem or the size of the dataset. This is particularly concerning for high-dimensional problems typical in deep learning, where the Hessian can be massive. Without a clear understanding of the computational overhead, it is difficult to assess the practical viability of ELMO, especially when compared to methods that approximate the Hessian or its inverse.

- The paper’s theoretical sections hint at the advantages over other optimizers but stop short of providing robust empirical comparisons. Most notably, results from modern optimizers like L-BFGS or RMSprop are missing. The paper’s single-minded focus on first-order methods as baselines (SGD, etc.) is insufficient, given that it positions ELMO as a quasi-Newton optimizer. A thorough evaluation should include comparisons with algorithms that also leverage second-order information, even if in an approximate manner. This would provide a more balanced view of ELMO's performance and practical utility.

- The authors emphasize concave subspaces within non-convex optimization but seem to overlook other complexities typical in high-dimensional loss landscapes, such as well-known flat regions and saddle points. The argument that concave subspaces alone are sufficient for achieving descent is unconvincing. While handling concavity is important, a comprehensive optimizer must also effectively navigate saddle points and flat regions. The paper does not provide a theoretical or empirical justification for why these aspects can be safely ignored, especially in the context of deep learning where they are known to be prevalent.

### Questions
- The meta-optimizer concept mentioned at the end of the paper is interesting but lacks detail. Can you envision this as an adaptive framework for switching between first- and second-order methods during training? What metrics or criteria would govern these switches, and what evidence suggests that the meta-optimizer approach would be computationally feasible?

- The paper emphasizes descent in concave subspaces. However, most real-world optimization problems (especially neural networks, you claimed) exhibit a mix of convexity, concavity, and flat regions. Could you clarify how ELMO handles such mixed regions? Why was this concavity-only focus chosen, and what empirical evidence supports its sufficiency?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper the authors discuss a preconditioned gradient method for various convex and non-convex optimization problems.  The main idea is to construct cubic polynomials (similar to cubic regularized Newton method) in d different directions, determined by the eigendirections of the Hessian at the current point. Since eigendirections are orthogonal by construction, this approach enables the authors to derive direction-specific step-sizes. Such a decomposition is made possible by leveraging a Lipschitz assumption of the Hessian's eigenvalues and eigenvectors.

### Strengths
The key strength of this paper lies in its novel decomposition of the optimization problem into d separate cubic polynomials along eigendirections, which allows for direction-specific step size optimization. This approach is particularly useful as it transforms what would typically be a d-dimensional cubic optimization problem into d one-dimensional problems that admit closed-form solutions for direction-specific step sizes. By exploiting the orthogonality of eigendirections and the Lipschitz properties of the Hessian's spectral decomposition, the authors provide a computationally tractable solution to adaptive step size selection.

### Weaknesses
Theoretical Novelty and Assumptions:

1. While the paper presents an interesting approach, its theoretical foundations are largely built upon existing work in cubic regularized Newton methods and the Lipschitz assumption of eigenvalues and eigenvectors, making the contribution incremental.  The global Lipschitz assumption on eigenvalues and eigenvectors seems overly restrictive, particularly may be problematic in regions where eigenvalues are small, potentially limiting the method's practical applicability.

Implementation and Practicality:

2. It would be nice to have a self-contained description of how to implement the algorithm in practice, particularly regarding the estimation of Lipschitz parameters for eigenvalues. While Section F.1 references a method, it lacks sufficient detail for reproduction; this section refers to some other methods which are not mentioned in the paper. 

3. The convergence analysis does not adequately address how the rate might be affected when using practical approximations of the Lipschitz parameters.

4. The computational overhead of the proposed method is significant, and the paper doesn't convincingly demonstrate practical advantages over simpler, widely-used preconditioned gradient methods like Adam or RMSprop that are more straightforward to implement.

In summary, while the paper presents an interesting theoretical framework, its strong assumptions and computational complexity, coupled with unclear practical benefits over existing methods, limit its potential impact on practical applications in machine learning problems.

### Questions
Please look at the weakness section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper addresses the challenges of parameter optimization for machine learning models, particularly in non-convex settings. The authors aim to simplify the comparison of convergence rates among different optimizers by proposing a unified descent rate bound with broad applicability. This work introduces the Eigenspace-Lipschitz Minmax Optimizer (ELMO), a minmax-optimal algorithm that effectively accounts for concave subspaces where traditional convergence bounds may fail.

The ELMO algorithm utilizes a third-order Taylor polynomial to model loss and demonstrates a worst-case descent rate of $O(\log t)$. The authors also analyze the descent rates of quasi-Newton algorithms in relation to ELMO, emphasizing the importance of considering the distribution of Lipschitz parameters in this context.

### Strengths
This paper introduces the Eigenspace-Lipschitz Minmax Optimizer (ELMO), which utilizes a third-order Taylor polynomial to model loss functions in machine learning. This approach extends traditional optimization methods by addressing the complexities of non-convex landscapes. Additionally, the authors' focus on the distribution of Lipschitz parameters offers a potentially novel perspective that has not been widely explored in the existing literature.

### Weaknesses
I am not familiar with this research topic, so I may underestimate the authors' contributions. However, I appreciate their discussion on when to use first-order versus second-order algorithms, as well as the impact of the distribution of Lipschitz parameters on algorithm performance.

1. The topic studied by the authors is quite broad, making it challenging to establish a unified framework. The paper attempts to address a very general problem of optimization in non-convex settings, which inherently makes it difficult to provide a framework that is both broadly applicable and practically useful. The generality of the problem may lead to a lack of specific insights that are actionable for particular sub-domains of machine learning optimization.
2. While the authors present a framework with some theoretical guarantees, it lacks practical applicability. The proposed ELMO algorithm, requiring eigendecomposition of the Hessian and estimation of Hessian-Lipschitz parameters, seems computationally expensive for practical use in large-scale machine learning problems. The paper does not provide sufficient evidence or discussion on how this algorithm could be efficiently implemented or approximated in real-world scenarios.
3. If the algorithm proposed by the authors is only slightly different from Cauchy's method (Traub, 1982), could they clarify the specific contexts in which each of the two algorithms is best applied? The paper needs to clearly delineate the differences between ELMO and Cauchy's method, especially in multi-dimensional settings, and provide a more detailed analysis of the conditions under which ELMO would offer a significant advantage over simpler optimization techniques.

### Questions
1. Line 23 and elsewhere: What is the meaning of "tight" or "tightness"?
2. Line 123: Should it be "from j=1 to j=n"?
3. Line 156, Notation 5. Is it guaranteed that the algorithm will converge? Should we introduce any assumptions to ensure convergence?
4. Line 226, Assumption 2: Does this assumption imply that we need to continuously perform eigenvalue decomposition during each iteration of the algorithm?
5. Line 274, equation (7): Why is there a summation symbol present?
6. Line 290, in Algorithm1: When updating $\theta_{t+1}$, should we include $\theta_t$ on the right-hand side?
7. Line 324, Notation 7 and Line 355 Notation 8. These marks may cause confusion.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a new second-order optimization method that achieves the bound f(\theta_0) - f(\theta_t) = O(log t).  The method involves the eigendecomposition of the Hessian matrix at the current iterate, computes the Lipschitz constants of the Hessian in the eigenvector directions, and uses these to determine an optimal step that minimizes a third-order Taylor polynomial model. Experimental results indicate that second-order optimizers outperform first-order optimizers when the Lipschitz constants of the convex eigenspace of the Hessian are relatively small.

### Strengths
The premise of the paper is correct, namely, that it is difficult to compare algorithms across a broad spectrum of problem classes.

### Weaknesses
1) The paper notes in Appendix C, Line 1034, that “Cauchy’s method (Traub, 1982) is nearly identical to ELMO.” However, if this is the case, Cauchy’s method (Traub, 1982) should be reviewed in the main body rather than the Appendix, with a clear emphasis on the differences between it and the ELMO method.
2) Although the introduction (Line 84) claims to “bound the rate at which the model’s performance increases (as measured by the loss function),” Theorem 3.2 provides only a negative lower bound for f(θt​)−f(θ0​), which seems weak. It’s unclear how Theorem 3.3 contributes to addressing this negative lower bound.
3) The performance of the ELMO algorithm is not demonstrated in the experiments.
4) The difficulty described in the introduction (Lines 50–65) does not seem to serve as a motivation for the ELMO method. Specifically, ELMO's design and analysis do not appear to address the challenge of selecting the best optimizer among a variety of options, each with its own assumptions and convergence rates.
5) Overall, the connection between the introduction (motivation), the ELMO method design, the experiments, and the conclusion is weak.

### Questions
1) For Equation (7): Why is the positive root taken? When compute the derivative of |\Delta {theta^*_t}^T v_i|^3 in (3), why is it assumed that  \Delta {theta^*_t}^T v_i is positive? 
2) In line 377-379: Are there typos where “concave” should be “convex”?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a Hessian based optimization algorithm which optimizes the step size coordinate-wise depending on the magnitude of the Lipschitz constant of the objective function along the eigen space coordinates.

### Strengths
Unfortunately, the paper is not convincing enough to demonstrate that the main idea could be useful, so I cannot see any strengths.

### Weaknesses
Besides that Hessian-based optimization techniques are often already too resource intense for large scale optimization, the paper suggest to perform a quite costly extra eigen-decomposition in every optimization step and assumes the existence of a "Lipschitz oracle" which can accurately estimate the Lipschitz constant of the objective function along every coordinate in the eigen space. Besides very simple objective functions I cannot see how this can be done efficiently. The paper provides Algorithm 2 which seems to be a full optimization algorithm (replacement of ELMO?, not clear) which uses an unexplained "BASE_OPT" subroutine and the "ASSESS_LIPSCHITZ" subroutine which depends on the unexplained (optimal?) point $\theta_t^*$. 

I also cannot see that the Lipschitz constant of Assumption 2 is actually a magnitude smaller than the one defined in equation (2). The paper promises to discuss this by saying "we will demonstrate that the Lipschitz parameters relevant to these subspaces are often order of magnitude smaller than the others", but provides no reference and I could not locate any such discussion.

The paper seems to provide a general optimization algorithm, but the introduction heavily motivates its application for hyper parameter optimization. In that domain the objective function is quite expensive to evaluate, so I especially cannot see how one can possess a Lipschitz oracle there. Furthermore, the assumptions of requiring an objective function of Lipschitz continuous Hessian (even coordinstewise) is usually violated in the hyper parameter optimization domain, and even in the experimental examples studied by the paper for neural network training with RELU activation functions in Appendix F.

There are a lot of confusing and wrong statements. For example in Lemma 3.1 "Exists $(L_t^i) : i=1,...,n$" does not make sense to me, the reformulation of $M_t^i(x)$ at the bottom of page 5 is certainly wrong (and seems to be completely out of context anyway) because whenever $x \cdot v_i(\theta_t)$ is nonzero that maximum is infinite, the $\arg \min$ in (7) returns a vector but it should be equal to scalars on its left and right sides, $\theta_{t+1} \leftarrow ...$ does not seem to depend directly on $\theta_t$ at all (is that really so?), Theorem 3.2 hides and did not discuss the dependence on $L_H$ which would have been one of the major points of the paper, and Theorem 3.3 is claimed to demonstrate that the upper bound of Theorem 3.2 matches the lower bound, but I cannot see how this result is related to any performance lower bound and it is neither discussed there.

The writing style is neither very clear including statements like "step's distance from ELMO's step relative to ELMO's step" in Notation 8, "only on subspaces with significantly convex subspaces" on page 8, and "Logarithmic scale" for Figure 1 which does not seem to be logarithmic.

### Questions
Could you tell me where is this promised demonstration for "we will demonstrate that the Lipschitz parameters relevant to these subspaces are often order of magnitude smaller than the others" in the paper?

### Soundness
2

### Presentation
2

### Contribution
1

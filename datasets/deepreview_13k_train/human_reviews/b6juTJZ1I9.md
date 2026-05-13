# Efficient Over-parameterized Matrix Sensing via Alternating Preconditioned Gradient Descent

- Decision: Reject
- Scores: 5, 1, 6, 8

## Abstract
We consider solving the low-rank matrix sensing problem in the over-parameterized setting, where the specified rank is larger than the true rank. Precisely, our main objective is to recover a matrix $X^*\in\mathbb{R}^{n_1\times n_2}$ with rank $r_\star$ using an over-parameterized form $LR^{\top}$, where $L\in\mathbb{R}^{n_1\times r},\ R\in\mathbb{R}^{n_2\times r}$ and $\min\{n_1,n_2\}\ge r> r_\star$ with the true rank $r_\star$ being unknown. The commonly used methods tackling such a problem such as Factorized Gradient Descent (FGD) can only demonstrate sub-linear convergence behavior, and their performance could significantly deteriorate when the matrix condition number is relatively large. To address this issue, we propose the alternating preconditioned gradient descent (APGD) method that an inexpensive right preconditioner with a constant damping parameter is applied to the original gradient. We prove that even starting from a random initialization, APGD can recover the target matrix at a linear convergence rate in the over-parameterized situation, independent of the condition number. Notably, unlike previous FGD-based methods, APGD alternates between updating the two factor matrices, which eliminates the reliance on a small step size, thereby enabling faster convergence. Through a series of experiments, we demonstrate that APGD achieves the fastest convergence speed compared to other methods, and further possesses strong robustness with respect to step size, condition number and other parameters.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a novel optimization approach, the Alternating Preconditioned Gradient Descent (APGD) method, specifically designed to address challenges in asymmetric matrix sensing problems. The APGD method is developed to tackle the unique difficulties posed by these tasks, especially when the problem is over-parameterized and the matrices involved are ill-conditioned.

The authors rigorously prove that under an over-parameterized setting, starting from a random initialization that is not too close to zero, the APGD method can achieve a linear convergence rate Furthermore, the APGD approach is shown to be more robust to large learning rates and damping parameters, which often destabilize other optimization methods in similar settings.

### Strengths
This work introduces a novel approach by combining the preconditioning technique to address the asymmetric matrix sensing case effectively. Unlike Zhang (2024)'s method, in which the second update step relies solely on L_t, the proposed APGD method introduces a modification: the second step updates R_{t+1} using information from L_{t+1} within the same iteration. This strategic adjustment accelerates the convergence, allowing the algorithm to approach the solution more efficiently.

Furthermore, the APGD method offers increased flexibility in parameter selection and random initializations, which significantly enhances its robustness. This flexibility enables APGD to handle larger step sizes without compromising convergence speed or stability, making it a promising choice for practical applications where traditional methods might fail or be too restrictive.

The theoretical analysis in this work follows a two-phase framework. This approach may inspire future studies to analyze optimization tasks that start from a random initialization rather than a local starting point, potentially broadening the range of problems where APGD or similar methods can be applied. The insights from this framework could serve as a basis for analyzing other matrix recovery tasks.

### Weaknesses
The paper's primary theoretical framework relies on the RIP, which is central to understanding the convergence guarantees. However, the RIP condition is not fully explained or discussed. For example, the choice of requiring an RIP constant smaller than sqrt(2)-1 is mentioned but not elaborated on. A detailed discussion on the role of RIP in the APGD approach can help to understand the global convergence.

And the explanation for initialization is missing in the main context, it's hard to understand directly why close to zero initialization does not help and the relation between c_init and \sigma_1(X_*).

In the experimental section, Figures 2 and 3 are presented in a format that significantly reduces clarity. The curves in these figures are zoomed in to the extent that it is challenging to distinguish between them based on the legend. Increasing the figure size or changing legend could greatly improve readability. Additionally, a comparison with the PrecGD method is missing in Figure 1. Given the relevance of PrecGD as a related approach, its inclusion in Figure 1 would provide a more comprehensive comparison and highlight the performance differences between APGD and this established baseline.

The paper may need thorough proofreading, especially regarding notation. Some symbols and terms are borrowed from reference papers but are not defined within this paper. This lack of consistent definitions can hinder readability and force the reader to consult external sources, interrupting the flow of understanding. Furthermore, there are minor mistakes in the mathematical expressions, both in the main text and in the appendix. While these errors might not compromise the overall framework or the validity of the theoretical results, they introduce unnecessary obstacles that may lead to misunderstandings.

### Questions
Typos and small mistakes in math expressions I found and not complete:
Line 145 Local -> local;
Line 201 should be 0<=delta_r<1;
Line 204 the definition of RIP is defined on ||M||_F^2;
Line 207 Lemma 1 should be a high probability result, that is with probability 1- exp(-...);
Line 250 does not define sigma_min before;
Line 256 right hand side of equation should be 1/2*||A(L_{t+1}R_t^top -X_*)||_2^2;
Line 259 third line of eqn4 (a-b)^2 =a^2+b^2-2ab, the -0.5\eta should multiply by 2;
Line 265 missing );
Line 305 Lt ->L_t;
Line 309 have not defined A^*;
Line 339 reference of equation is not 64 but 62;
Line 397 should be L_t R_t^top;
Line 862 eqn36 should be (1-\eta/2);
Line 1049 second line missing coefficient 2;
Line 1070 same as Line 339;
Line 1239 in eqn 83 there should not be ^\top for (1-\eta_c)


In line 412, the authors assert that their results do not require a bound on L, the gradient Lipschitz constant, but are solely dependent on \delta_2 r. However, the RIP constant is linked with the restricted strongly convex and smooth property. Specifically, the RIP is equivalent to this property with a condition number of (1 + \delta)/(1 - \delta), suggesting that the Lipschitz constant L cannot be entirely disregarded. The authors may need to clarify this relationship and address whether it is possible to completely eliminate the dependence on L in their analysis.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper proposes an alternating preconditioned gradient descent method for the over-parameterized, ill-conditioned, asymmetric low-rank matrix sensing problem. The proposed algorithm has two stages: it begins with a specified initialization and then performs alternating preconditioned gradient descent on the over-parameterized variables $L$ and $R$. The alternating preconditioning technique is said to make the algorithm robust against over-parameterization, ill-conditioning, and hyperparameters.

### Strengths
The proposed algorithm makes sense for addressing the acceleration of ill-conditioning and over-parameterization.

### Weaknesses
1. The proposed algorithm is not explained well or properly. The writing is poor.

2. The claimed contributions and the key novel techniques for the main result are not well demonstrated and supported, such as the intuition and rationale behind the proposed initialization and the role that alternating plays in robustness and acceleration.

3. For the second stage of the algorithm, it is not surprising that the damped preconditioning works to accelerate ill-conditioned and over-parameterized low-rank matrix sensing. Although the authors list many related works, they did not point out their novelty compared to existing ones, especially (Zhang et al. 2021, Xu et al. 2023). Actually, the preconditioning trick used in this paper is nearly the same as the existing works.

4. Lastly, I want to emphasize that the main issue with this paper is that the initialization scheme is neither proper nor reasonable. Therefore, its theoretical result from the initialization stage does not make sense, or at least is not as strong as the authors claim. The random initialization in this work is to sample $L_{0}$ and $R_{0}$ with i.i.d. $N(0,\sigma_{1}(X_{\star}))$. It is not reasonable because one does not know the ground truth $X_{\star}$ when initializing. This unreasonable initialization scheme makes its proof of $||L_{0} R_{0}^{\top} - X_{\star}|| \leq \rho \sigma_{r_{\star}} (X_{\star})$ quite trivial with random matrix theory and assumptions.

A more practical random initialization scheme should be like (Stoger & Soltanolkotabi, 2021), (Lee & Stoger, 2023), and (Xu et al., 2023), which consider small random initialization with i.i.d. $N(0,\frac{1}{n})$. Their focus mainly lies in the analysis of the alignment phase and saddle avoidance phase of the initialization stage. Apart from the balanced initialization, (Xiong et al., 2023) shows that the imbalanced random initialization approach can help accelerate low-rank matrix sensing. 

Therefore, the analysis of this work for random initialization is outside the real research interests.

### Questions
1. Is there any evidence that the initialization scheme is practical?
2. Why does the alternating scheme make sense to the robustness of the choice of hyperparameters?

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a novel Alternating Preconditioned Gradient Descent (APGD) algorithm for solving the over-parameterized low-rank matrix sensing problem. The authors address key challenges such as ill-conditioning, over-parameterization, and initialization issues in matrix sensing. The proposed method achieves linear convergence from random initialization, even in the presence of high condition numbers and rank overestimation. Theoretical results are supported by experiments that demonstrate APGD's faster convergence and robustness compared to existing methods.

### Strengths
This paper introduces the Alternating Preconditioned Gradient Descent (APGD) algorithm, which significantly improves matrix sensing in more practical and real-world settings by relaxing some of the strict assumptions made in prior works. The authors theoretically prove that APGD can still achieve linear convergence to a good solution under these relaxed conditions, highlighting both its theoretical contributions and practical potential. The experiments are well-designed, with appropriate and comprehensive parameter settings. The results align closely with the theoretical findings, further demonstrating that APGD achieves state-of-the-art performance compared to current FGD-based methods.

### Weaknesses
This paper has a few shortcomings, mainly in its presentation:

1.The abstract emphasizes APGD’s advantages over FGD, but since FGD refers to a class of methods, the paper should explicitly list which algorithms in the comparisons (e.g., ScaledGD) belong to this category, especially in the experimental section. This would help readers quickly verify the claims made in the abstract by directly comparing APGD with FGD-based methods. It is not immediately clear if all methods used for comparison are indeed factorized gradient descent methods, and a more precise definition of the FGD class within the context of this paper is needed.

2. The paper distinguishes APGD from PrecGD, which is a good approach to comparing with SOTA methods. However, several other algorithms are included in the experiments, and it should be clearly stated which one serves as the baseline. If PrecGD is a key comparison, it would be beneficial to include its performance in the noisy setting of the sensitivity analysis (e.g., damping parameter), or to explain why it was excluded from certain analyses. The current presentation leaves the reader unsure about the specific role of each algorithm in the experimental comparisons, and a more rigorous justification for the choice of baseline is necessary.

3.While the importance and benefits of "alternating" in alternating preconditioned gradient descent are clear from the content for me, this aspect is under-emphasized in the abstract. A stronger focus on this in the abstract would highlight its contribution more effectively.

### Questions
I have two questions: one concerns the experiments, and the other might go beyond the scope of this paper as a discussion.

1. How does APGD perform in comparison to PrecGD in the sensitivity analysis of the damping parameter in the noisy setting?

2. Alternating preconditioned gradient descent is one approach to solving asymmetric matrix sensing through LR factorization. However, as noted in "Low-rank Solutions of Linear Matrix Equations via Procrustes Flow", adding regularization during the optimization process is another method for asymmetric matrix recovery. Could combining preconditioning with a similar regularization technique be a promising direction for achieving better performance?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper considers the problem of over-parameterized matrix sensing, where the goal is to recover a low-rank matrix $X$ from a limited number of measurements. It was previously known that over-parameterization and ill-conditioning significantly slows down methods like gradient descent. In this work the authors proposed a preconditioned version of alternating GD that starts from a random initialization and converges linearly to the optimal solution.

### Strengths
Overall I think this paper is well-written and makes solid contributions. The main problem and its key difficulties are introduced in a natural way. The authors also state very clearly what the prior state of art is. As a result, it is easy to compare the contributions of this work with prior work. 

In terms of the technological contributions, I think it is an important improvement over prior work that the proposed algorithm APGD does not require small initialization. Previous works relied on either small initialization or spectral initialization, both of which can be very expensive (although in different ways). Here the authors show that APGD converges with just random initialization, and is able to both prove this rigorously and demonstrate this in their numerical experiments.

### Weaknesses
I did not find any major weaknesses in this paper. However, it is worth noting that previous work which uses small initialization (such as Stoger & Soltanolkotabi, 2021) only requires rank-$r^*$ RIP for the measurement operator, whereas this work requires rank $r$ RIP. I think this fact should be noted, as it can make a big difference when the estimated rank $r$ is very large. This discrepancy in RIP requirements could lead to a significant practical disadvantage in scenarios where the true rank $r^*$ is much smaller than the assumed rank $r$, as the number of measurements needed to satisfy rank-$r$ RIP could be substantially larger. Furthermore, the paper does not explicitly discuss the computational cost associated with the preconditioning step, which could be a bottleneck in high-dimensional settings. It would be beneficial to see a more detailed analysis of the computational complexity of the proposed algorithm, especially in comparison to prior methods.

### Questions
In the weaknesses section I mentioned that the theoretical results in work rely on rank-$r$ RIP. Is this an artifact of the theoretical analysis, or is this something that actually appears in experiments? If we only have rank-$r^*$ RIP, does the method still work?

### Soundness
3

### Presentation
4

### Contribution
3

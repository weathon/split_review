# Double Momentum Method for Lower-Level Constrained Bilevel Optimization

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Bilevel optimization (BO) has recently gained prominence in many machine learning applications due to its ability to capture the nested structure inherent in these problems. 
Recently, many hypergradient methods have been proposed as effective solutions for solving large-scale problems.
However, current hypergradient methods for the lower-level constrained bilevel optimization (LCBO) problems need very restrictive assumptions, namely, where optimality conditions satisfy the differentiability and invertibility conditions and lack a solid analysis of the convergence rate. What's worse, existing methods require either double-loop updates, which are sometimes
less efficient.
To solve this problem, in this paper, we propose a new hypergradient of LCBO leveraging the theory of nonsmooth implicit function theorem instead of using the restrive assumptions. In addition, we propose a \textit{single-loop single-timescale} algorithm based on the double-momentum method and adaptive step size method and prove it can return a $(\delta, \epsilon)$-stationary point with $\tilde{\mathcal{O}}(d_2^2\epsilon^{-4})$ iterations. Experiments on two applications demonstrate the effectiveness of our proposed method.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors introduce a novel hypergradient approximation method for lower-level constrained bilevel optimization problems with non-asymptotic convergence analysis, utilizing Gaussian smoothing. This method incorporates double-momentum and adaptive step size techniques. The experimental results, in the context of data hyper-cleaning and training data poisoning attacks, showcase the efficiency and effectiveness of the proposed approach.

### Strengths
S1. The work is well motivated. Finding a simple yet effective method for lower-level constrained bilevel optimization problems is both interesting and important.  

S2. The paper is well written and easy to follow. The algorithm design is new and non-asymptotic convergence is provided.

S3. The authors conduct numerous experiments to showcase the efficiency and effectiveness of the proposed approach. Additionally, the paper includes several ablation studies in the Appendix.

### Weaknesses
W1. By Remark 2 on page 7, $\tilde{\mathcal{O}}(\frac{\sqrt{d_2}}{\delta K^{1/4}})\leq \epsilon$ implies that $K=\tilde{\mathcal{O}}(\frac{d_2^2}{\delta^4 \epsilon^4})$, NOT $\tilde{\mathcal{O}}(\frac{\sqrt{d_2}}{\delta \epsilon^4})$. Additionally, since $\delta=\mathcal{O}(\epsilon d_2^{-3/2})$ by (11), the iteration number $K=\tilde{\mathcal{O}}(\frac{d_2^8}{\epsilon^8})$. This high polynomial dependence on $d_2$ and $1/\epsilon$ is a significant limitation and should be discussed more thoroughly, especially in the context of practical applications where $d_2$ can be large. The authors should also clarify whether this bound is tight or if there is potential for improvement with further analysis or modifications to the algorithm.

W2. The authors should consider comparing their method with closely related papers addressing lower-level constrained bilevel optimization problems, including:

[1] Han Shen, Tianyi Chen. “On Penalty-based Bilevel Gradient Descent Method.” ICML 2023.

W3. Since there is an additional loop to approximate the matrix inverse, it can be noted that the proposed algorithm DMLCBO is not fully single-loop. The authors should acknowledge that while the algorithm avoids nested loops in the sense of alternating between upper and lower level updates, the inner loop for matrix inversion adds computational overhead and may impact the practical efficiency of the method. This should be clearly stated and discussed in the paper.




### Questions
Q1. Could you provide some representative class of problems that satisfy Assumption 3? Consider the simple example: $g(x,y)=(y-x)^2/2$, $\mathcal{Y}=[-1,1]$ and $\mathcal{X}=[-3,3]$. The projection operator $P_Y$ has a closed-form solution, but $\mathcal{P}_{\mathcal{Y}}(z^*)$ is not continuously differentiable in a neighborhood of $z^*$ when $x=1$ or $x=-1$.

Q2. Is Assumption 3 satisfied for all small values of $\eta$? 

Q3. What measures can be taken to verify that Assumption 4 is satisfied, or are there specific checkable sufficient conditions to ensure its validity?

Minor Comments:

(1)On page 3, in Equation (4): The minus sign in the expression of $\nabla y^*(x)$ was omitted.

(2)On page 4, in Remark 1: What is $F_{\delta}(x)$?

(3)On page 5, in Lemma 2: “$\| A \| \leq 1$” should be “$\| A \| < 1$”. Make similar changes after Lemma 2. 

(4)On page 5, in Equation (9): By the definition $c(Q)$, the term $u^Q$ in $\bar{\xi}$ is not used.

(5)On page 6, in Algorithm 1: swap the positions of $v_1$ and $w_1$. Should “$g(x_1,y_1)$" be replaced with “$\nabla_y g(x_1,y_1)$"? Make similar changes in Section 3.3. 

(6)On page 6, in line 3 from below: Should “$\nabla F_{\delta}(x_k)$” be replaced with “$\nabla F (x_k)$”?

(7)On page 7, Lemma 5: The absolute value symbol for $\mathcal{G}$ in Equation (10) was omitted. Should “$\nabla f(x_k, y_k)$” be replaced with “$\nabla_x f(x_k, y_k)$”? Additionally, what is $\tilde{x}_{k+1}$?

(8)On page 8, in line 3 from below: correct the sum within the max part.

(9)On page 9, Do the bilevel optimization problems related to training data poisoning attacks satisfy the smoothness and convexity assumptions?Note that “a network with two convolution layers and two fully-connected-layer layers for MNIST and a network with three convolution layers and three fully-connected-layer layers for Cifar10, where the Relu function is used in each layer.”

### Soundness
2 fair

### Presentation
3 good

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
This paper studies a bilevel optimization problem in which the lower-level problem has a convex set constraint which is independent of the upper-level variable. Using Gaussian smoothing to approximate the gradient of the projection operator, the authors propose an approximation to the hypergradient and a single-loop algorithm. Theoretical analysis and numerical experiments are provided.

### Strengths
The proposed algorithm is a single-loop single-timescale approach.

### Weaknesses
1. Assumption 3 is restrictive to satisfy. Furthermore, even the problems examined in the numerical experiments fail to meet this assumption.

2. In order to achieve a stationary point with $\| \nabla F (x) \| \le \epsilon$, as outlined in Remark 2, the proposed algorithm necessitates a choice of the smooth parameter on the order of $O(\epsilon d_2^{-3/2})$. Consequently, the algorithm would require a minimum of approximately $\tilde{O}(d_2^8/\epsilon^8)$ iterations. It appears, however, that the authors aim to obscure this fact within their paper and retain the smooth parameter in their complexity result.

3. The problems explored in the numerical experiments may not necessarily adhere to the strongly convex assumption for the lower-level problem stipulated in Assumption 2 (3). Moreover, the selection of values for the parameters $Q$ and $\eta$ does not align with the theoretical requirements specified in Theorem 1.

### Questions
see above

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
To address lower-level constrained bilevel optimization problem, the authors leverage the Gaussian smoothing to approximate the hypergradent. Furthermore, the author proposes a single-loop single-timescale algorithm and theoretically prove its convergence rates. Two experimental settings have been tested to demonstrate the superiority of proposed algorithm.

### Strengths
The experimental results are great for proposed algorithm.

### Weaknesses
1. The proposed algorithm DMLCBO is based on double momentum technique. In previous works, e.g., SUSTAIN[1] and MRBO[2], double momentum technique improves the convergence rate to $\mathcal{\widetilde O}(\epsilon^{-3})$ while proposed algorithm only achieves the $\mathcal{\widetilde O}(\epsilon^{-4})$. The authors are encouraged to discuss the reason why DMLCBO does not achieve it and the theoretical technique difference between DMLCBO and above mentioned works.

2. In the experimental part, the author only shows the results of DMLCBO in early time, it will be more informative to provide results in the later steps.

3. In Table 3, DMLCBO exhibits higher variance compared with other baselines in MNIST datasets, the authors are encouraged to discuss more experimental details about it and explain the behind reason.

### Questions
Check the weakness part.

### Soundness
2 fair

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
This paper considers bi-level optimization problems with constrained lower-level problems (LCBO). A single-loop method is proposed to solve the LCBO, which returns an approximately stationary point with a non-asymptotic convergence rate. The main technique is to use the Gaussian smoothing to approximate the hypergradients. Moreover, momentum methods are applied to update both the upper and lower-level variables. Numerical experiments show the superiority of the proposed method.

### Strengths
1. The proposed method is a single-loop algorithm, which is more efficient than the existing methods.
2. The application of the Gaussian smoothing is new to me. This provides new insights for solving the LCBO.

### Weaknesses
1. The technical analysis is not sound. It is not clear why $F$ is differentiable (e.g., in Lemma 5) and how Assumption 3 works. Indeed, for a simple example of LCBO, $F$ can be non-differentiable at some points. For example, $F(x)=|x|$ in the following problem is not differentiable at $x=0$
$$
\min_{x,y} -xy \text{ s.t. } y\in\arg\min_{z\in[-1,1]}xz.
$$
However, these kinds of cases are not discussed in the paper. As a consequence, Lemma 5 and (10) are not convincing. The differentiability of $F$ relies heavily on the differentiability of the optimal lower-level solution $y^*(x)$ with respect to $x$, which is not generally guaranteed, especially when the lower-level problem has constraints. The paper does not adequately address the conditions under which $y^*(x)$ is differentiable, and simply assuming it is does not suffice. The example provided clearly demonstrates a case where this assumption fails, leading to a non-differentiable $F(x)$. This lack of rigor undermines the theoretical results.

2. Assumption 4 is also strange to me. More discussions are needed for this kind of boundedness assumption. The assumption that the norms of the iterates and the stochastic gradient estimates are bounded is not well-justified. While boundedness might be achieved through clipping, the paper does not explicitly state this and it is not clear if the clipping would affect the convergence analysis. The assumption seems to be made for convenience of analysis rather than being a natural property of the algorithm or the problem itself. A more detailed discussion of how this assumption is satisfied, or a relaxation of this assumption, is needed.

### Questions
1. Why is the convergence rate only related to $d_2$ but not $d_1$?

2. In the experiments, are the lower-level constraints active at the solution returned by the proposed algorithm?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

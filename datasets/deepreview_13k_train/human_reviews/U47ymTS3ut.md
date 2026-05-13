# Mask in the Mirror: Implicit Sparsification

- Decision: Accept
- Scores: 5, 6, 6, 6

## Abstract
Sparsifying deep neural networks to reduce their inference cost is an NP-hard problem and difficult to optimize due to its mixed discrete and continuous nature. Yet, as we prove, continuous sparsification has already an implicit bias towards sparsity that would not require common projections of relaxed mask variables. While implicit rather than explicit regularization induces benefits, it usually does not provide enough flexibility in practice, as only a specific target sparsity is obtainable. To exploit its potential for continuous sparsification, we propose a way to control the strength of the implicit bias. Based on the mirror flow framework, we derive resulting convergence and optimality guarantees in the context of underdetermined linear regression and demonstrate the utility of our insights in more general neural network sparsification experiments, achieving significant performance gains, particularly in the high-sparsity regime. Our theoretical contribution might be of independent interest, as we highlight a way to enter the rich regime and show that implicit bias is controllable by a time-dependent Bregman potential.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
"Spred" is a recent algorithm that implicitly achieves sparse solutions through reparameterization. To understand why "Spred" outperforms LASSO, the authors analyzed its training dynamics using the mirror flow framework. They demonstrated that when the regularization term in "Spred" is time-dependent, it can smoothly transition between implicit L2 and L1 regularization. Building on this insight, they introduced PILoT, an approach that dynamically adjusts the regularization strength. Finally, the authors validated the effectiveness of PILoT through experiments on CIFAR-10/100 and ImageNet datasets.

### Strengths
The theoretical analysis of the reparametrization with time-varying weight decay is solid and novel. It is valuable to first develop a deep theoretical understanding, which then serves as a basis for algorithmic improvements.

### Weaknesses
 
**Major:**
- **Inaccurate and unclear writing**: The presentation in the paper could benefit from a substantial revision to improve clarity, particularly in the latter half of Section 1 and Sections 2, 3, and 5. Additionally, some inaccuracies need to be addressed. For example, the abstract states that "A key factor in their (continuous sparsification) success is the implicit L1 regularization induced by jointly learning both mask and weight variables." However, the discussion from Lines 54-65 suggests that this implicit L1 regularization is exclusive to the "Spred" algorithm, which utilizes reparameterization. The paper is currently difficult to follow, which is my primary concern. The logical flow between the introduction, theory, and experiments is not smooth, making it hard to grasp the core message and contributions. The writing often lacks precision, using vague terms and making it difficult to pinpoint the exact mechanisms at play. For instance, the transition from the theoretical analysis to the practical algorithm (PILoT) is not clearly articulated, leaving the reader to infer the connection rather than having it explicitly stated.
- **Computation and memory costs of reparameterization**: The reparameterization approach proposed in the algorithm effectively doubles the number of parameters, resulting in increased computational and memory demands. However, this is not discussed in the paper. This is a significant practical concern that needs to be addressed, especially when considering the scalability of the proposed method to larger models and datasets. The authors should provide a more detailed analysis of the computational overhead and memory footprint, and potentially discuss strategies to mitigate these costs.

**Minor:**
- **Figure 4's legend is confusing**: It would be clearer to rename "mw LRR" to "LRR with reparameterization" and "x LRR" to "LRR."
- **Unclear variables in Algorithm 1**: The variables "u_0" and "v_0" introduced in Algorithm 1 are not referred to in subsequent sections, leading to confusion about their purpose. The lack of explanation for these variables creates a disconnect between the algorithm and the theoretical framework, making it difficult to understand the initialization process and its impact on the overall performance.

### Questions
N/A

### Soundness
3

### Presentation
1

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
This paper studies the mirror flow of the time-dependent $L_2$-regularized optimization problem which is parametrized by masked weights $x=m\odot w$. The authors derive the corresponding Bregman potential for the mirror flow and prove a convergence result for quasi-convex loss functions. Inspired by the forms of the derived Bregman potential and the gradient flow, the authors propose PILoT, which takes (i) a strategy to control the strength of $L_2$-regularization dynamically and (ii) a initialization for $m$ and $w$ that enables sign flipping. Evaluations show that PILoT outperforms baselines on CIFAR 10 and CIFAR 100.

### Strengths
* The theoretical result seems sound though I didn't check the proofs. 
* The Bregman potential offers insight on $L_1$ regularization effect. 
* The gradient flow also offers insights on why spred outperforms Lasso from the perspective of convergence rate. 
* I appreciate that the authors also develop an algorithm inspired by the theory.

### Weaknesses
The writing is still poor. While some notations are now explained, the explanation of $m^2$ is still not standard and can be confusing. The experimental section remains difficult to parse. Specifically, the rationale for the duplicate entries in Table 1 is unclear, and the explanation provided in the text is not sufficient. It's not immediately obvious why presenting results for slightly different sparsity levels is necessary for a fair comparison. The connection between these slightly different sparsity levels and the hyperparameter configurations (mentioned in the response) should be made explicit in the paper. Furthermore, the claim that $R$ attains its global minimum at $x_0$ when $R$ is the $L_1$ norm is still not clear. While the authors mention that the implicit bias promotes solutions close to $x_0$, the explanation lacks a rigorous argument. The connection between the mirror flow framework and the initialization is not well established. Finally, the discussion of the bias-variance trade-off is not sufficiently detailed. While the authors mention that explicit regularization introduces a second optimization objective, they do not elaborate on how the time-dependent regularization mitigates this trade-off in the context of their specific method. The explanation of how Theorem 2.3 recovers unbiased prediction while minimizing Bregman potential is not clear enough.

### Questions
1. I found table 1 confusing. Why do all methods have duplicates in the table?
2. At line 227, why does $R$ attain its global minimum at $x_0$ when $R$ is $L_1$ norm?
3. At line 218, is there any formal result stating that explicit regularization would lead to a trade-off? I can see that implicit bias of the reparametrized optimization is helping achieve both sparsification and low loss, but does that imply an explicit regularization forces a trade-off?

### Soundness
3

### Presentation
1

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
In this paper, the authors focus on the problem of finding sparse neural networks. They propose a new method called PILoT based on theoretical analysis on simple diagonal linear networks. They use the insights gained from theoretical analysis to improve previous method called spred to introduce dynamic regularization strength and initialization scheme. Experiments are provided to show the improvement of the proposed method.

### Strengths
-	Studying the sparsification of neural networks is an interesting research problem.
-	The proposed method that applies the idea of implicit/explicit regularization to pruning seems to be new.
-	The performance of the proposed method shown in experiments suggests that there is some improvement over the previous works.

### Weaknesses
-	Many places are not very clear to me as a reader.
-	In line 228, I was wondering why ‘’the potential $R$ attains its global minimum at the initialization $x_0$... In consequence, we would not promote actual sparsity’’. I’m confused about this. As many paper that authors cited, when initialization scale goes to 0, the final implicit regularization is $\ell_1$ norm that promotes the sparsity. It is unclear why a standard initialization would prevent sparsity, and this point requires more explanation.
-	In Theorem 2.2, what is $\alpha_\infty$? Is it regularization $\alpha_t$ at time $t\to\infty$? If not, what does it mean? If so, it seems to me that $\alpha_t\to 0$ given the assumptions. This would make $\alpha_\infty=0$, which makes the statement very weird. Moreover, if $\alpha_\infty\neq 0$, then why $x_t$ would converge to a minimizer of $f$ given the existence of a regularization term. The definition of $\alpha_\infty$ is not clear, and the implications for convergence are not well explained.
-	In line 347, I wonder if authors could explain more on why eq (6) explains spred performs better than LASSO. I believe there are many classical algorithms that can solve LASSO better than just using gradient descent/gradient flow, and they may not have such problems. The comparison to LASSO is not convincing, as more efficient LASSO solvers exist, and it's not clear why the specific gradient flow analysis is relevant to those.
-	In line 374, I wonder why $\beta=1$ is motivated by the discretization of the gradient flow. It is not clear to me what are the connections here. The motivation for setting $\beta=1$ is not clearly explained, and the connection to the discretization of the gradient flow is vague.
-	In the proposed algorithm PILoT (Algorithm 1), I wonder why $\alpha_k$ should be increased when the sparsity $\|m_k \odot w_k \|_1\ge K$. Since decreasing $\alpha_k$ would promotes better sparsity, I feel $\alpha_k$ should be decreased in this case? The logic behind increasing $\alpha_k$ when sparsity is not met is counterintuitive, and the explanation is lacking.
-	In experiments, what are the schedules of $\alpha_k$ that are used? The experimental details regarding the schedule of $\alpha_k$ are missing, which makes it difficult to reproduce the results.

Typo:

-	Below eq (6), missing ( in expression of $a_t$.

### Questions
-	In line 228, I was wondering why ‘’the potential $R$ attains its global minimum at the initialization $x_0$... In consequence, we would not promote actual sparsity’’. I’m confused about this. As many paper that authors cited, when initialization scale goes to 0, the final implicit regularization is $\ell_1$ norm that promotes the sparsity.
-	In Theorem 2.2, what is $\alpha_\infty$? Is it regularization $\alpha_t$ at time $t\to\infty$? If not, what does it mean? If so, it seems to me that $\alpha_t\to 0$ given the assumptions. This would make $\alpha_\infty=0$, which makes the statement very weird. Moreover, if $\alpha_\infty\neq 0$, then why $x_t$ would converge to a minimizer of $f$ given the existence of a regularization term.
-	In line 347, I wonder if authors could explain more on why eq (6) explains spred performs better than LASSO. I believe there are many classical algorithms that can solve LASSO better than just using gradient descent/gradient flow, and they may not have such problems.
-	In line 374, I wonder why $\beta=1$ is motivated by the discretization of the gradient flow. It is not clear to me what are the connections here.
-	In the proposed algorithm PILoT (Algorithm 1), I wonder why $\alpha_k$ should be increased when the sparsity $\|m_k \odot w_k \|_1\ge K$. Since decreasing $\alpha_k$ would promotes better sparsity, I feel $\alpha_k$ should be decreased in this case?
-	In experiments, what are the schedules of $\alpha_k$ that are used?


Typo:

-	Below eq (6), missing ( in expression of $a_t$.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies the implicit sparse regularization of continuous specification. By studying the implicit bias of a specific mirror flow with a time-dependent Bregman potential, the authors propose a novel continuous sparsification method  "parametric implicit lottery ticket" (PILoT). The convergence and optimality is shown theoretically, and the effectiveness in real-world examples is demonstrated numerically.

### Strengths
The paper is well-written and easy to follow. I didn't go through the proofs, but the illustrations make sense, and the technical contribution is solid.

### Weaknesses
One point that might limit the significance of the conclusion is that the implicit regularization appears after the model fits the data perfectly (Theorem 2.3), which might not hold in reality.



### Questions
The literature below is related but missed

* Vaskevicius et al, Implicit regularization for optimal sparse recovery, NeurIPS 2019.
* Li et al, Implicit Sparse Regularization: The Impact of Depth and Early Stopping, NeurIPS 2021.
* Zhao et al, High-Dimensional Linear Regression via Implicit Regularization, Biometrika 2022.
* Li et al, Implicit bias of gradient descent on reparametrized models: On equivalence to mirror descent, NeurIPS 2022.
* Li et al, Implicit Regularization for Group Sparsity, ICLR 2023.

Minor comments:
* .(dot) is missed for the leading bold text in Section 1.1
* Line 213, "(Ziyin & Wang, 2023)..." is not a sentence.
* Line 404, "return..." goes to the next line

### Soundness
3

### Presentation
3

### Contribution
3

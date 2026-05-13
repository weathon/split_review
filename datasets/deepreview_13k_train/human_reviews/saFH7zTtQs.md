# Learning Linear Dynamical Systems with Sparse System Matrices

- Decision: Reject
- Scores: 3, 5, 6, 6, 5, 6

## Abstract
Due to the tractable analysis and control,  linear dynamical systems (LDSs) provide  a fundamental  mathematical tool for  time-series data modeling in various disciplines. Particularly, many LDSs have sparse system matrices  because interactions among variables are limited or only a few significant relationships exist.   However, available learning algorithms for LDSs  lack the ability to  learn system matrices with the sparsity constraint.  To address this issue, we impose sparsity-promoting priors on system matrices and explore the expectation–maximization (EM) algorithm to  give a maximum a posteriori (MAP) estimate of both hidden states and system matrices from noisy observations. In addition, we find that many learning algorithms based on the gradient descent method use an inappropriate derivative rule, because they neglect the inherent symmetry of  noise covariance  matrices. Here, we consider the derivative rule of structured matrices during the optimization process to guarantee their symmetry. Experimental results on simulation and real-world problems illustrate that  the proposed algorithm significantly improves learning accuracy over classical ones.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors consider learning of linear dynamical systems with a sparsity-promoting regularization term. When one considers the learning of linear dynamical systems with side-constraints as a non-convex optimization problem, one can quite naturally obtain solvers the converge to global minimizers of the least-squares estimator, asymptotically. Even the 2020 paper appearing in SIAM Review (https://proceedings.mlr.press/v120/ahmadi20a) considers a variety of types of side information, rather than just sparsity, and the more recent papers provide detailed analyses (e.g. non-asymptotic error bounds in the Frobenius norm in https://hal.science/hal-04394297/document), or consider operator-valued formulations of the problem (e.g., https://doi.org/10.1109/TAC.2023.3313351). The present paper does not do any of this, focussing on an EM heuristic.

### Strengths
The results are reasonably well written up.

### Weaknesses
The authors obtain an EM heuristic for the problem, but do not prove whether the EM heuristic provides good solutions or not.

The authors test their approach on two instances from "Database for the Identification of Systems" (http://homes.esat.kuleuven.be/~smc/daisy/), a well-known collection of 20+ instances, without explaining why they choose the two instances in particular. This smacks of cherry-picking. The comparison against PEM and n4sid, which date back to 1970s and 1994, respectively, also does not seem to capture the current state of the art fully. 

The authors do not consider any of the recent literature on learning of linear dynamical systems with side-constraints as a non-convex optimization problem (e.g. https://proceedings.mlr.press/v120/ahmadi20a, https://doi.org/10.1109/TAC.2023.3313351, https://hal.science/hal-04394297/document).

### Questions
Would you have results on further instances from "Database for the Identification of Systems"?

Would you have a comparison against any recently proposed system ID methods? There is the conference series L4DC (e.g. https://l4dc.web.ox.ac.uk/home), where a dozen a presented each year, for instance.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Proposing a Bayesian algorithm for model parameter estimation in dynamical systems with sparse components.

### Strengths
1. Good numerical performance (Table 2).

2. Enough details on the proposed algorithm.

### Weaknesses
1. Novelty is rather limited which questions the overall contribution of the manuscript.

2. Many missing papers in the literature review such as:

- Faradonbeh, M. K. S., Tewari, A., & Michailidis, G. (2018). Finite time identification in unstable linear systems. Automatica, 96, 342-353.

- Chakraborty, N., Khare, K., & Michailidis, G. (2023). A Bayesian framework for sparse estimation in high-dimensional mixed frequency vector autoregressive models. Statistica Sinica, 33, 1629-1652.

- Faradonbeh, M. K. S., Tewari, A., & Michailidis, G. (2020). Optimism-based adaptive regulation of linear-quadratic systems. IEEE Transactions on Automatic Control, 66(4), 1802-1808.

-Samanta, S., Khare, K., & Michailidis, G. (2022). A generalized likelihood-based Bayesian approach for scalable joint regression and covariance selection in high dimensions. Statistics and computing, 32(3), 47.

- Modi, A., Faradonbeh, M. K. S., Tewari, A., & Michailidis, G. (2024). Joint learning of linear time-invariant dynamical systems. Automatica, 164, 111635.


3. The real data section can be improved by further discussions; so far, only improved prediction errors are reported.

### Questions
1. How sensitive Algorithm 1 is with respect to initial values (initial guesses of model parameters)?

2. Numerical examples are 2-3 dimensional. How does the proposed algorithm work under high-dimensional settings? Sparsity assumption typically makes sense in such high-dimensional cases.

3. What can be said about inference for model parameters?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work addresses the problem of identifying linear dynamical systems with sparse system matrices from noisy observations.
According to the authors, available algorithms lack the ability to incorporate sparsity constraints. In contrast, their proposed solution promotes sparsity by imposing a Student's t-distribution prior on the system matrices. Then, it uses an expectation-maximization approach to estimate the system matrices. This dichotomy is illustrated with synthetic and real data.
Finally, the authors have also identified and corrected an inaccurate derivative rule employed by other expectation-maximization approaches in this context.

### Strengths
*Originality*:
The problem formulation and subsequent elaborations and conclusions appear novel.

*Quality*:
The proposed solution is carefully devised to admit closed-form updates. With this goal in mind, all heuristics and approximations seem justified and well motivated.

*Clarity*:
The paper is well organized and the ideas the authors want to convey are clearly exposed.

*Significance*:
This work may shed a light on the problem of learning linear dynamical systems with sparse system matrices. It can also open new research lines in this regard.

### Weaknesses
 **W1**. Section 2 could benefit from a literature review on sparse promoting methods. For example, what is the state-of-the-art of Lasso-like estimators? or, how do they compare to sparse Bayesian learning in this context?  Specifically, the paper should discuss the limitations of using $\ell_1$ regularization for inducing sparsity, such as the non-differentiability at zero and the need for careful hyperparameter tuning. A comparison to reweighted $\ell_1$ minimization methods and their effectiveness in enhancing sparsity would also be beneficial. Furthermore, the review should delve into the advantages of sparse Bayesian learning (SBL), such as its ability to automatically learn hyperparameters and its probabilistic framework, and how these compare to the more deterministic approaches of Lasso-like methods. The discussion should also include specific examples of where SBL has been successfully applied to similar problems, highlighting both its strengths and potential drawbacks.

**W2**. I think the heuristic method introduced in Section 3.2. is *block coordinate descent* (also known as alternating minimization) rather than *block coordinate gradient descent* (BCGD). 
Please, see [1] for a definition of the BCGD method.

For example, using the paper notation, the update step in eq. (22) can be equivalently written as
$ \boldsymbol{A}^{k+1}_r \simeq \text{arg} \underset{\boldsymbol{A}_r}{\text{ max }} H(\boldsymbol{\Theta} | \boldsymbol{\Theta}^k) $.
That is, the approximated gradient in eq. (21) is not used to perform a gradient step; instead, it is set to zero to find a stationary point in closed form. 

I believe this distinction is not only a technicality, but is also important to emphasize that one could have used BCGD without approximating the gradient to find the stationary point numerically. The current description obscures the fact that the method is a form of alternating minimization, which has different convergence properties and requirements than a gradient-based method like BCGD. The authors should clarify why they chose to use alternating minimization instead of a true gradient-based approach, especially given that the objective function is non-convex and the convergence of alternating minimization is not guaranteed in such cases.

*Minor comments*:

**C1**. The main text does not seem to refer to Figure 1 anywhere. I think the reader would appreciate some guidance about which ideas or explanations Figure 1 is supporting or complementing.

**C2**. The authors may consider change the notation of the normal probability distribution in eq. (7)  from **|** to **;** to be aligned with the standarized notation encouraged by ICLR. Similarly, the matrix $\boldsymbol{P}$ introduced in eq. (35) may be renamed to not overlap with the matrices $\boldsymbol{P}^k_t$ and $\boldsymbol{P}^k_{t,t-1}$ introduced in eq. (9) and (15), respectively.

**C3**. I think the manuscript could benefit from an appendix where the derivative rule of structured matrices is explained, and why the derivatives of unstructured matrices cannot be used instead in general. Specifically, the appendix should explain how the symmetry constraint on matrices such as covariance matrices affects the derivative calculation. It should also provide a concrete example of how using the incorrect derivative rule can lead to non-symmetric updates, which are invalid for covariance matrices.

**C4**. I think Appendix C could benefit from explaining also how the mean and covariance of the noise $\bar{\epsilon}_t$ are obtained.

### Questions
**Q1**. Section 3.2. is called ''Parameter and Hyperparameter Learning''. 
Usually, the term hyperparameter is reserved for those parameters whose values control the learning process and cannot be infered during training (they can be learned by optimizing a higher level metric though). 
Based on this definition, (I think) the only hyperparameters in this work are $a_0$ and $b_0$; however, they are not learned but initially set to a very small value.
So, by learning hyperparameters do you mean learning the parameters in the Gamma matrices? If so, do you call them hyperparameters because they are related to the hyperprior?

**Q2**. The last sentence of the Discussion section reads ''we hope to explore how to exactly learn LDSs with additional constraints'', and I am not sure what ''exactly'' or ''additional constraints'' refer to.
My best guess is that by exactly you mean maximizing eq. (6) in closed-form updates, and by additional constraints you mean additional constraints on top of sparsity?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper discusses learning linear dynamical systems (LDSs) with sparse system matrices. The authors propose an algorithm to learn LDSs with sparse system matrices from noisy observation. The proposed algorithm applies the EM algorithm to give the MAP estimates of hidden states and system matrices. The derivative rule of structured matrices ensures the symmetry of the noise covariance matrix during the optimization process. The proposed algorithm outperforms the classical learning methods through the experimental results and simulation on the real-world dataset.

### Strengths
The proposed algorithm is more useful for exploring the interacting laws of the LDSs than the classical ones.

### Weaknesses
 The proposed algorithm cannot determine the order n of the system from data directly and the similarity transformation may shrink many parameters to very small values, leading to numerical errors.

### Questions
1. The examples are simple, and the sparse matrices are diagonal. How are the sparse matrices selected in the problem? 
2. Can the authors provide examples of using sparse matrices but not diagonal?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The article addresses the problem of identifying system matrices $A,B,C,D$  and noise covariances $R$ and $Q$ assumed to be normal for the dynamical system:

$$\begin{array}{rll}
x_t&=&Ax_{t-1}+Bu_t+\epsilon_t\\
y_t&=& Cx_t+Du_t+\omega_t
\end{array}$$

from the data $\{(u_t,y_t)\}$ over a time-horizon $T.$

To identify the matrices $A,B.C,D$ the authors propose to use priors that promote sparsity; the parameters, dependent on $\Gamma_a, \Gamma_b,\Gamma_c$ and $\Gamma_d$  of the priors are also learnt in the apporach presented.

In the approach, the priors are initialized to be noninformative. The approach is as follows: 

(i) The first step of the iteration: if the set of parameters governing the model given by $\Theta^{(k)}=(A,B,C,D,R,Q,\Gamma_a, \Gamma_b,\Gamma_c$ and $\Gamma_d)$ is provided then one can determine the distribution of the state $x_t$ from measurements $y_t$ using a standard kalman filter like update.  Dynamics are linear and noise sources gaussian and thus analytical expression for the conditional density of $x_t$ can be obtained. 

(ii) In the second step of the iteration, the parameters in $\Theta$ are updated by maximizing a posterior function of the  $\Theta$, $H(\Theta|\Theta^{(k)})$  wherein the conidtional distribution, $p(x_t|y,\Theta^{(k)})$ is leveraged to maximize

$$H(\Theta|\Theta^{(k)})=\mathbb{E}[\log~p(Y,X|\Theta)p(\Theta)]$$ 

with the expection taken over the pdf obtained in step (i).  The $H$ can be deteremined  as analytical expressions in terms of $(A,B,C,D,R,Q,\Gamma_a, \Gamma_b,\Gamma_c,\Gamma_d)$. The authors proceeed to set the derivatives of $H$ with respect to the parameters to zero. Here, the resulting equations do not admit an explicit solutions; the authors make assumption on the noise covariances being diagonal to reach an explicit closed-form solutions for derivatives with respect to the $A,B,C,D$ matrices; while taking deribatives with respect to $R$, the symmetry of the matrix $R$ is incorporated and respected.  

The simulation section demonstrates that the inclusion of the priors promotes preserving structure of the system matrices.

### Strengths
The idea of imposing sparsity promoting priors to preserve structure of the system matrices for linear dynamical systems is interesting and possibly impactful.

### Weaknesses
 (1) The methodology more or less mirrors the development in  "Sparse Bayesian Learning and the Relevance Vector Machine" article by Tipping. The novelty seems incremental

(2) Another of authors article "An Iterative Min-Min Optimization Method for Sparse Bayesian Learning", seems to be very related to the present article; specifically it does provide insights into why the priors on the weights promotes sparsity by comparing with regularizers employed. Given the earlier works, the contribution of the present article becomes more incremental

(3) The authors claim that the priors promote structure of the matrices, but the explanation is not entirely convincing. While sparsity-promoting priors can lead to simpler models, it is not clear how they inherently preserve the *topological* structure of the system matrices beyond simply setting some entries to zero. The argument that the similarity transformation is restricted to a generalized permutation matrix is not rigorously justified and requires more detailed explanation. It is not clear why the algorithm would avoid other non-singular matrices that could also lead to sparse representations.

### Questions
(1) Can the authors delineate the novelty with a comparison with the ideas presented in "Sparse Bayesian Learning and the Relevance Vector Machine" article by Tipping?

(2) Can the authors state which aspects of this article differ in a substantitive manner over analysis in "An Iterative Min-Min Optimization Method for Sparse Bayesian Learning"? Which new insights are found?

(3) Can the authors indicate why the priors promote sturcture of the matrices in contrast to sparsity alone?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper addresses the learning of linear dynamical systems (LDSs) with sparse system matrices. The authors propose an expectation–maximization (EM) algorithm that incorporates sparsity-promoting priors on system matrices, enabling a maximum a posteriori (MAP) estimation of both hidden states and system matrices from noisy observations. The authors validate their algorithm with experiments on synthetic and real-world datasets, demonstrating better performance over traditional methods such as PEM, 4SID, and MLE

### Strengths
1. The paper is well-motivated, with a thorough analysis of related work that situates the proposed method within the context of recent advances in LDS learning.
2. The mathematical derivations are sound, providing a solid theoretical foundation for the proposed approach.

### Weaknesses
1. The definition of matrix sparsity could be clarified. While the authors introduce a sparsity-promoting prior, it would be beneficial to show examples of what matrices look like after imposing the Student’s t-distribution to better illustrate its effect. Specifically, it is unclear how the Student's t-distribution encourages sparsity in the system matrices. A visualization or a more detailed explanation of the resulting matrix structure, such as the distribution of non-zero elements, would be beneficial. 
2. The applicability of this method in higher-dimensional cases is unclear. High-dimensional systems often exhibit sparse structures, and it would be insightful to explore how the method scales or adapts to such scenarios. The current experiments do not explore the computational complexity or the performance of the algorithm with increasing dimensionality. It is important to understand how the method's performance changes with a larger number of state variables and parameters.
3. The paper is mathematically dense, which could challenge readers unfamiliar with LDSs. An additional table summarizing the notations may enhance readability and aid understanding. The current presentation assumes a strong background in LDS theory, which might limit the accessibility of the paper to a broader audience. A notation table would be particularly helpful for those who are not experts in this field.
4. The synthetic experiment in Section 5.1 appears overly simplified, potentially limiting insights into the method’s performance. It would be helpful to see additional experiments with more complex or higher-dimensional system matrices. The current synthetic experiment uses a very low-dimensional system, which may not fully demonstrate the capabilities of the proposed algorithm. Experiments with more complex system dynamics and higher-dimensional matrices are needed to validate the method's effectiveness.
5. For the real-world dataset experiments, it would be valuable to include datasets where the true underlying system matrices are known. This would allow for a direct comparison between the learned and true matrices or at least an evaluation of the topological structure similarity. Without a ground truth comparison, it is difficult to assess the accuracy of the learned system matrices, especially in terms of their structural properties.

### Questions
1. Could the authors provide a brief explanation of the Occam’s Razor principle?
2. While the proposed method aims to learn the system matrices, even in the simple synthetic example in Section 5.1, the learned matrices (B, C, R, Q) differ from the true ones. If the primary goal is to predict observations, are there more direct approaches that could yield higher prediction accuracy?

### Soundness
3

### Presentation
2

### Contribution
2

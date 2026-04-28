# Advancing the Lower Bounds: an Accelerated, Stochastic, Second-order Method with Optimal Adaptation to Inexactness

- Decision: Accept
- Avg Score: 5.25
- Scores: 8, 1, 6, 6

## Abstract
\if 0
We present a new accelerated stochastic second-order method that is robust to both gradient and Hessian inexactness, typical in machine learning. We establish theoretical lower bounds and prove that our algorithm is the first optimal method in this key setting. We further introduce a tensor generalization for inexact higher-order derivatives, called Stochastic AcceleRated TEnsor Method (S-ARTEM). When the oracles are non-stochastic, S-ARTEM matches the global convergence of ARTEM despite having the ability to handle inexactness. Both algorithms allow for approximate solutions of their auxiliary subproblems with verifiable conditions on the accuracy of the solution.

\fi 
We present a new accelerated stochastic second-order method that is robust to both gradient and Hessian inexactness, which occurs typically in machine learning. We establish theoretical lower bounds and prove that our algorithm achieves optimal convergence in both gradient and Hessian inexactness in this key setting.  We further introduce a tensor generalization for stochastic higher-order derivatives. When the oracles are non-stochastic, the proposed tensor algorithm matches the global convergence of Nesterov Accelerated Tensor method. Both algorithms allow for approximate solutions of their auxiliary subproblems with verifiable conditions on the accuracy of the solution.
\if
    We present the first accelerated stochastic second-order method that achieves optimal convergence in both gradient and Hessian inexactness.
    Compared to previous state-of-the-art algorithms, our proposed method improves the convergence rate for inaccuracies in gradients and Hessians, while matching their convergence rate in the term corresponding for the exact convergence.
    We provide lower bounds on the corresponding convergence terms for stochastic gradient and inexact Hessian. 
    We further introduce a tensor generalization for inexact higher-order derivatives. 
    Both algorithms allow for approximate solutions of their auxiliary subproblems with verifiable conditions on the accuracy of the solution.
\fi

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper present a stochastic second-order method  based on nesterov acceleration and cubic newton, which is proven to be robust to gradient and Hessian inexactness. The faster convergence rate of this algorithm is established for stochastic Hessian and inexact Hessian compared with previous work. The lower bound for the stochastic/inexact second-order methods for convex function with smooth gradient and Hessian is also established, verifying the tightness of their convergence upper bound. The inprecision produced by solving the cubic subproblem is also taken account of in the analysis. The method is also extended to higher-order minimization with stochastic/inexactness, and a restrated accelerated stochastic tensor method is also proposed for strongly-convex function.

### Strengths
1. The author of this article considers several interesting questions that naturally arise for the inexactness in practice, and are therefore valuable, especially the proposed algorithm and its tight convergence rate, and the lower bounds for inexact second-order methods. 
2. The article follows a natural logic in exploring the questions,  progressing in a layered manner.
3. The proof techniques the authors used seem solid and sound.

### Weaknesses
1. While I grasp the overarching concept of the algorithm and the principal steps in the proof, the exposition doesn't offer much in the way of intuitive understanding. Could the authors elucidate the rationale behind the algorithm's design and the parameter choices? Enhancing the exposition with additional intuitive insights into the algorithm would be highly beneficial.

2. The assumptions (2.2 and 2.3) of stochacity and inexactness differ but seem highly related, as they lead to two quite similar convergence rates and proof for your algorithm. In this paper the way of discussing the stochasticity and inexactness settings seems a bit nesting.  Maybe it could be better if their highlevel relations  are set forth in a proper manner. 

3. Clarification: O(1/T^2) ->\Omega(1/T^2) in P2 line 2; bounded variance stochastic Hessian ->stochastic Hessian with bounded variance; formatting issues such as sequence numbers in the algorithm list.

### Questions
1. In section 3, the subproblem you defined is $\omega_{x}^{M,\bar{\delta}}=f\left(x\right)+\left\langle g\left(x\right),y-x\right\rangle +\frac{1}{2}\left\langle y-x,H\left(x\right)\left(y-x\right)\right\rangle +\frac{\bar{\delta}}{2}\left\Vert x-y\right\Vert ^{2}+\frac{M}{6}\left\Vert x-y\right\Vert ^{3}$. Compared to the original cubic regularized subproblem, in addition to the modification of the inexactness and stochasticity, your formulation has an additional quadratic term $\frac{\bar{\delta}}{2}\left\Vert x-y\right\Vert ^{2}$. Are there any reason or intuition for this term?

2. Could you bring more insights for the aggregation of stochastic linear models above algorithm 1?

3. The gloabal convergent (accelerated, cubic newton type) second-order methods, while they have accelerated global convergence, they usually can be proven to have superlinear local convergence rate. Is the parallel local characteristic worth to be mentioned and investigated in your stochastic/inexact setting?

4. The open question mentioned, "what's the optimal trade-off between inexactness in gradients and the Hessian?", where in the article is intuitively investigated? 

5. Regarding Algorithm 3, you mentioned the 'Restarted Accelerated Stochastic Tensor Method'. Could you further elaborate on the specific mechanism and necessity of this 'restarting'? Under what circumstances should a restart be performed?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors present a new accelerated stochastic second-order method that is robust to both gradient and Hessian inexactness, typical in machine learning. It looks to achieve the lower bounds.

### Strengths
None

### Weaknesses
The algorithm, as presented, raises concerns regarding its practical implementation, particularly in step 4. This step involves solving another optimization problem, which could introduce significant computational overhead. The complexity and feasibility of solving this subproblem efficiently are not adequately addressed in the paper. Without a clear understanding of how this step is executed, it is difficult to assess the overall efficiency and scalability of the proposed method.

### Questions
How does the algorithm work in step 4 of the proposed algorithm?  Does it work in practice?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes an accelerated stochastic second-order algorithm using inexact gradients and Hessians, demonstrating nearly optimal convergence rates.

### Strengths
The paper proposes an accelerated stochastic second-order algorithm using inexact gradients and Hessians, demonstrating nearly optimal convergence rates.

### Weaknesses
see questions.

### Questions
1) The paper lacks an intuitive explanation of the proposed algorithm. It is suggested to explain the motivation and impact of parameters such as $\alpha_t$, the choice of the model $\omega_x^{M,\bar{\delta}}$, and the technique of estimating sequence on the algorithm's performance and convergence. 
2) When comparing computational time, is the proposed algorithm better than existing methods?
3) The figures in the paper are too small, making it difficult for readers to interpret the results.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work studies the unconstrained minimization of convex and strongly convex functions with continuously differentiable gradients through second-order methods with access to inexact gradients and Hessians. Further with the assumption of unbiased gradients they show a faster convergence rate of their proposed algorithm than the state of the art. Also, they show the worst-case complexity lower bound for their problem. Then, the proposed method is extended to tensor analysis and a restart scheme is proposed for strongly convex functions. Experimental results confirm the superiority of the proposed method to Extra-Newton and SGD methods.

### Strengths
1- Good flow in introduction and problem setup.

2- With additional assumption on the unbiasedness of the gradient, they show the lower bound on convergence rate of inexact Hessian & gradient plus proposing a method which achieves the lower bound exept for the last term.

3- They did a relatively thorough analysis by extending their analysis to tensor methods and special cases like strongly convex cases.

### Weaknesses
 1- Though the text has a good flow in terms of the context, there is still room for improvements: e.g. 

(a) In page 2 there are two loose sentences in the middle of the page. They can be integrated with the previous paragraph or just in a new independent paragraph. 

(b) Below assumption 1.2: $E[g(x,\xi)]$ or $E[F(x,\xi)]$?

(c) **\citet** was used wrongly in many places. Please consider replacing the wrong ones with **\citep**.

(d) function $\psi_t(x)$ above algorithm 1 is not defined (I think it is in the algorithm so you should refer to that or simply introduce it)

(e) The definition of $f$ in section 7 page 8 is an abuse of notation: $f(x)=E[f(x,\xi)]$

(f) I suggest larger font size on Figures 1,2

(g) Large gap in the appendix after (26)

2- I think contributions 3 & 1 should be integrated.

3- Table 1 might lead to misunderstanding. Your result is based on the asssumption of unbiased gradients. The rate by Agafonov does not have this assumption. Thus, it seems like an unfair comparison.

4- The title of the section “Lower Bound” is very generic and also the description is vague. For example, the first sentence of this section is vague.

### Questions
1- Is the $\boldsymbol \Phi_x$ defined at the beginning of Section 2 used? Same question holds for $\boldsymbol\Phi_x$ defined under Assumption 5.1.

2- Lemma 2.1 seems like a special case of a similar lemma in Agafonov et al 2020. Is there a reason you did not cite their work when you present the Lemma? Same question holds for Lemma 5.2. 

3- How did you find the dynamic strategy for the precision level $(\tau_t=c/(t^{3/2}))$

4- According to your investigation and results, does it make sense to analyze inexactness in Hessian (or higher order information of the objective function) when gradients are inexact? This question mainly concerns the $O(1/\sqrt{T})$ convergence rate related to the inexactness of the gradients which dominates the convergence rate as $T\rightarrow \infty$.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

# ODE Parameter Identification: An Integral Matching Approach

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 8, 3, 5

## Abstract
We present a novel method to identify parameter of nonlinear Ordinary Differential Equations (ODEs) using time series data. Our approach fits parameters by matching a collocation-based estimate of the integral of the learned derivative to an interpolation of the trajectory, thus avoiding the computational cost of ODE solvers in adjoint methods and the sensitivity to noise of derivative estimates in gradient matching methods. By employing batching strategies based on time subintervals and state components, our method achieves linear complexity in relation to system dimensions and dataset sizes. The method is highly parallel enabling fast gradient evaluations and a faster convergence than adjoint methods. For fully observed systems, we demonstrate the method on canonical dynamical systems, where the method achieves speed-ups of three orders of magnitude over adjoint methods and an increased robustness against observational noise. We provide an extension to partially observed systems and demonstrate the method on the Lorenz63 attractor.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper presents a novel method for estimating the parameters of an ordinary differential equation (ODE) by aligning a collocation-based estimate of the integral of the learned derivative with an interpolation of the trajectory. The problem addressed is significant, and the proposed approach appears to be innovative. However, certain sections of the paper lack clarity, as noted in the comments below.

### Strengths
The problem addressed is significant, and the proposed approach appears to be innovative.

### Weaknesses
However, certain sections of the paper lack clarity, as noted in the comments below

1. At the beginning of Section 3, the loss function 𝑙 is introduced, but this notation does not appear in Section 3.1. I assume it corresponds to the function in Equation (7)?

2. The matrices 𝐷 and 𝑉 in Section 3.1 are undefined. After Equation (4), it’s mentioned that the transformations are detailed in the appendix, yet the definition of \tilde{D} is still unclear.

3. The start of Section 3.2 states that (7) is solved using Algorithm 1. However, Algorithm 1 is written ambiguously, making it difficult to understand how it applies to solving (7). A more detailed, step-by-step description would be very helpful. For instance:

a. How is Θ initialized?
b. What exactly does Step 2, “build denoised set,” entail?
c. What is X_s in Step 6?

3.1 Additionally, it is unclear how Algorithm 1 is inspired by the ADMM algorithm (as claimed in Section 3.2); there appear to be no apparent connections between them.

4. The theoretical bound in Section 3.3 is not presented as a theorem. Without a precise statement of assumptions and conclusions, the main result of this paper is difficult to interpret. For example, the assumption in Section 3.3.1, “Supposing the gradient descent converges to an optimum Θ∗ such that L_2(Θ∗)=0” is unclear and appears overly restrictive in requiring convergence.

### Questions
See comments above.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper proposes a novel method to estimate parameters of (non-linear) ordinary differential equations. The methods is scalable and more efficient than existing approaches. The authors derive theoretical bounds on the difference between the optimal solution to the parameter estimation problem and the parameters found by optimizing the surrogate loss used by their method. The paper also evaluates the method on multiple benchmark problems and compares performances to several baselines and across different metrics.

### Strengths
- The paper is very clearly structured and well written which makes it easy to follow the ideas.
- The proposed idea is well motivated and positioned within the existing work
- The proposed methods seems to work well in practice on multiple problems and outperform existing approaches in terms of computational efficiency.
- I appreciate the detailed discussion of limitations.

### Weaknesses
 - I appreciate the comparison with SINDy in the "Learning Polynomial dynamics" experiment, however, to my mind SINDy is not primarily a parameter estimation method but a way to learn the entire structure of the equation. For polynomials, estimating the coefficients of course implies learning the structure, nevertheless, I think it would be good to also include other parameter estimation methods in the comparisons in Table 2, e.g. BPTT, Adjoint methods and perhaps also other approaches such as simulation-based inference, as these (to my mind) would be the actual alternatives to the proposed approach.

- A minor general comment, I think the formatting is a bit off in some places so that lines of text are a bit to close to each other, e.g. between the caption of figure 2 and the main text or between table 3 and table 4.

- I find the explanation of "observation error" in Figure 2 highly confusing. The x-axis is labeled "observation error" and is presented as a signal-to-noise ratio (SNR), yet the y-axis, which represents RMSE, seems to be behaving inversely to what one would expect from an SNR. Typically, a higher SNR corresponds to a cleaner signal and thus lower error, but in Figure 2, the RMSE increases with increasing SNR. Furthermore, the use of percentages for SNR is unclear; it is not specified what the percentage refers to, making the interpretation difficult. The presentation of RMSE in percentages is also unconventional and should be avoided.



### Questions
- In Figure 2, what do you mean by "observation error"?
- In Table 2, what is "IMATCH THRESH"?
- The true positive rate in figure 3 shows an initial drop as trajectories get longer before going up for all noise levels. Do you have any explanation for this (at least to me) surprising initial behavior?
- Not a question but rather a minor comment: In section 6, second paragraph, there seems to be something wrong with the sentence "If not, our method can be initialize parameters prior to adjoint methods". I didn't understand what this was supposed to mean.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces an integral matching strategy for system identification. However, there are several concerns regarding its formulation and soundness. The proposed model has not been sufficiently validated through experimentation. Addressing these weaknesses is essential for enhancing the credibility of the proposed model and improving its practical applicability in modeling complex dynamics.

### Strengths
The integral matching strategy appears promising because integration is a more mathematically stable and bounded operator than derivatives. This approach may lead to improved training stability and performance in modeling complex dynamics.

### Weaknesses
1.  A major concern arises from the separation of the dynamics into independent subintervals, which results in the loss of continuity between them after ignoring eq (2b). This separation could cause significant issues in the overall performance of the model since the connection between the subintervals is crucial. It is essential to conduct experiments to assess how well the model learns the relationships between these subintervals.
2.  The method could be improved by incorporating eq. (2b) in eqs (6) and (7), similar to how eq (2c) is treated. While this may not be computationally efficient, it is necessary to explore this modification experimentally to examine its impact on performance.
3.  The claim that eq (6) uses an Augmented Lagrangian is incorrect, as the method used is actually a penalty method. The Augmented Lagrangian requires solving a saddle system, but it generally provides better convergence to the minimizer of constrained problems compared to the penalty method. While the penalty method is conceptually simpler, it requires the penalty parameter $\rho$ to approach infinity for the constraints to be satisfied mathematically. Therefore, the choice of $\rho$ in the penalty method chosen by the authors is critical to ensuring constraint satisfaction. This parameter $\rho$ is a new hyperparameter not present in traditional NODEs, and a study of its effects is needed.
4.  The performance of the proposed method is highly dependent on the polynomial interpolation degree $K$. I recommend an ablation study to investigate the effects of varying $K$ to better understand its influence on model performance. In addition, comparisons with other node types beyond the LGR node leveraged in this study is also required.

### Questions
Please address the concerns mentioned in the weaknesses part above.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This manuscript introduces a novel approach for parameter identification in nonlinear ODEs using integral matching. By leveraging collocation-based integral estimates, the authors present a method that demonstrates substantial computational efficiency and robustness to noise. The approach is benchmarked against traditional solver-based and surrogate methods, showing impressive speed improvements.

### Strengths
1.	The paper is well-motivated, with a comprehensive background and related work section that positions the proposed method within the existing literature.
2.	Experimental results indicate that the proposed method achieves significant speed improvements and demonstrates reduced sensitivity to noise, highlighting its practical advantages over existing methods.

### Weaknesses
1. Clarity in Theoretical Presentation: Section 3, which discusses the main theoretical results, would benefit from further clarification. Several aspects currently hinder readability:
- Inconsistent Notation: There is inconsistent notation for derivatives (e.g., $\dot{x}(t)$ vs. $l’(\tau)$), and mixed usage of symbols such as $\tau$, $\tau_j$, and $\tau_k$, which may confuse readers. The use of $\dot{x}(t)$ suggests a derivative with respect to $t$, while $l'(\tau)$ implies a derivative with respect to $\tau$. This inconsistency makes it difficult to follow the mathematical derivations. Furthermore, the indices on $\tau$ are not consistently used, sometimes denoting specific time points and other times seemingly arbitrary points within an interval, which creates ambiguity.
- Unexplained Symbols: Certain notations, such as $X_{il}$ and $X_{i,0}$, are introduced without adequate explanation, limiting clarity. The reader is left to guess what these symbols represent, which is not conducive to understanding the proposed method. For example, it is unclear if $X_{il}$ refers to a specific component of the state vector at a particular time or something else entirely. Similarly, $X_{i,0}$ lacks context, making it difficult to interpret its role in the equations.
- Ambiguity in Notations: In Equation (6), two instances of $X_i$ appear. Clarification on whether they denote the same or distinct elements is advised. The lack of clarity regarding whether these are the same vector or different vectors at different time points introduces a significant ambiguity, making it difficult to understand the equation's meaning and its role in the overall method.
- Change of Variables: The statement "the change of variable $t = t_i + \tau h_i$ rescales time to $[0,1]$" could be explained in greater detail to aid understanding. While this change of variable is standard, the explanation is too brief. It would be beneficial to explicitly state how this transformation affects the derivatives and the integral calculations, as well as the implications for the polynomial basis used in the collocation method. The lack of detail makes it difficult for a reader to fully grasp the implementation of this step.

These issues give the impression of insufficiently clear theoretical exposition. To improve readability and ensure clarity, I suggest that the authors thoroughly review and streamline their mathematical notations and formulations, providing explanations where necessary. Including a summary table of notations would be an effective way to guide readers.

2. Notation clarity in Tables:
- In Table 1, notation $\epsilon$ is not defined. Additionally, the arrows in the “Accuracy FWD/BWD” column lack explanation.
- In Table 3, entries in the "Gradient Estimation Time (s)" column, such as $510^{-2}$, appear confusing and could be rephrased for clarity.

### Questions
Could the authors clarify how RMSE is computed in this study? Specifically, what is the rationale for calculating RMSE based on $\dot{x}$ rather than $x$?

### Soundness
2

### Presentation
2

### Contribution
3

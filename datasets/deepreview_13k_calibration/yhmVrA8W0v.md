# The Convergence of Second-Order Sampling Methods for Diffusion Models

- Decision: Reject
- Avg Score: 4.60
- Scores: 6, 6, 3, 3, 5

## Abstract
Diffusion models have achieved great success in generating samples from complex distributions, notably in the domains of images and videos. Beyond the experimental success, theoretical insights into their performance have been illuminated, particularly concerning the convergence of diffusion models when applied with discretization methods such as Euler-Maruyama (EM) and Exponential Integrator (EI). This paper embarks on analyzing the convergence of the higher-order discretization method (SDE-DPM-2) under $L^2$-accurate score estimate. Our findings reveal that to attain $\tilde{O}(\epsilon_0^2)$ Kullback-Leibler (KL) divergence between the target and the sampled distributions, the sampling complexity - or the required number of discretization steps - for SDE-DPM-2 is $\tilde{O}(1/\epsilon_0)$, which is better than the currently known sample complexity of EI given by $\tilde{O}(1/\epsilon_0^2)$. We further extend our analysis to the Runge-Kutta-2 (RK-2) method, which demands a sampling complexity of $\tilde{O}(1/\epsilon_0^2)$, indicating that SDE-DPM-2 is more efficient than RK-2. Our study also demonstrates that the convergence of SDE-DPM-2 under Variance Exploding (VE) SDEs aligns with that of Variance Preserving (VP) SDEs, highlighting the adaptability of SDE-DPM-2 across various diffusion models frameworks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Diffusion models (DMs) learn the score functions associated with a diffusion process, and use the learned scores to simulate an SDE corresponding to the backward process. While samples can be simulated by either an ODE or an SDE, SDE samplers are practically superior in terms of sample diversity and quality. This paper sets out to investigate second-order SDE solvers for the backward SDE, and concludes that second-order solver is preferable to the standard first-order discretization methods in terms of convergence with respect to the Kullback-Leibler divergence. 

The paper mainly investigates two (approximate) second-order SDE solvers, SDE-DPM-2 and Runge-Kutta 2 methods, and compares the convergence results to first order SDE solvers such as EI. The paper presents theorems that suggest that SDE-DPM 2 is more preferable to RK-2 from the perspective of KL-divergence, mainly due to the added discretization error. 

While the paper mainly focuses on the VP-DMs based on the Ornstein-Uhlenbeck forward process, the main result also applies to the variance-exploding forward process as well, shedding light on the applicability of solvers on other forward processes.

### Strengths
The paper presents convergence results of second-order SDE solvers for diffusion models, which is very relevant to current research in diffusion modeling given the empirical usefulness of SDE-based simulation of the backward process, and the open question of suitable discretization techniques in this context. The paper gives a theoretical foundation on the application of high-order SDE solvers in diffusion modeling, which motivates further research on suitable solvers for diffusion generative modeling. 

- Within the scope of the paper, it presents a compelling argument in favor of SDE-DPM-2 over RK-2 or first-order discretization methods for the practical simulation of samples. I find the insight of "not second-order solvers are equal" overall interesting and helpful. 
- The paper also illustrates that the convergence bounds empirically with Gaussian mixture examples. 
- The theoretical results are quite general as they apply to both VP and VE diffusion models.

### Weaknesses
While I have an overall positive outlook on the paper, I think the paper's overall organization seems confusing: the paper presents the main theorems and some empirical results, then jumps back to a sketch of the proof and how the theory works for the VE-type diffusion models. In my opinion, presenting the paper as theorems on SDE-DPM-2 and RK-2, proof sketch, discussion on VE and then experiments seems like more logical progression of the narrative. 

There are a number minor issues in terms of the paper's presentation. Here is a list I have found: 
- Many discretization methods mentioned in the paper are known only as acronyms without mentioning what the acronyms are. 
- The mentions of $x_k$ in assumption should be $x_{t_k}$ in equations such as the one in Assumption 2, eqs. 11 and 13.
- The use of partial derivatives w.r.t. $x_{t_k}$ seems confusing. I assume it means the Jacobian matrix. Perhaps the authors can explicitly denote a notation to describe the Jacobian matrix for clarity. 
- While it is useful to see that second-order SDE solvers makes improvements empirically, Table 1 presents quite little added information other than a somewhat vague empirical confirmation that SDE-DPM-2 does have empirical value, which has already been demonstrated by Lu et al. (2022b). The specific metrics and their improvements are not sufficiently detailed to provide a strong empirical validation beyond what is already known.

### Questions
- The paper presents the KL convergence results about the VP- and VE-types of diffusions models separately. Could you briefly explain how different types of forward processes affect your proof?
- I find panel (b) of Figure 1 quite helpful as an illustration between theory and practice, but the paper also presents convergence results with respect to RK-2. What would the theoretical bounds of RK-2 look like on that graph?
- Are equations 11 and 13 identical? If so, why?

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the convergence properties of score-based diffusion models with a second-order discretization scheme called SDE-DPM-2, which improves the complexity over a first order exponential intergation scheme. Interestingly the result for SDE-DPM-2 is also stronger than the more widely used RK-2 scheme.

### Strengths
- The authors address a question of significant interest in the diffusion model literature, namely which discretization schemes are most sample efficient at inference time.
- The paper gives some additional theoretical support to the observation that higher order schemes can be important for sample complexity and differentiates between subtleties, such as the additional approximation in the linear term of the SDE.  
- Experiments show a modest improvement of CIFAR-10 FID with small numbers of sampling steps and improved convergence with discretization fineness using SDE-DPM-2 over RK-2.

### Weaknesses
 - There is no comparison of the computational cost of RK-2 vs DPM-SDE-2 vs EI
- I felt the authors should have more clearly delineated their contributions relative to Chen 2023, which they follow closely.
- A number of the assumptions are quite strong. For example, the expectation of the second time derivative of the score is assumed to have a magnitude upper bounded by some time-independent constant. In practice, it is often the case that the score changes in quite a singular fashion near $t=0$.
- I think the authors might have a mistake in assumption 4, because I don't see them using the operator $\nabla^3$ anywhere. 
- Can the authors add error bars to the table of the FID scores? At present, I don't feel that these illustrate their point particularly well.

### Questions
- I think the authors might have a mistake in assumption 4, because I don't see them using the operator $\nabla^3$ anywhere. 
- Can the authors add error bars to the table of the FID scores? At present, I don't feel that these illustrate their point particularly well.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper analyzes the convergence of the higher-order discretization method (SDE-DPM-2). Under some smoothness condition as well as score estimation error and high oder estimation error, a sampling complexity at the order of O(1/epsilon) is established to ensure the KL divergence smaller than epsilon^2. In comparison, the complexity of second-order Runge–Kutta method (RK-2) scales as O(1/epsilon^2).

### Strengths
This paper analyzes the convergence of the higher-order discretization method (SDE-DPM-2). Under some smoothness condition as well as score estimation error and high oder estimation error, a sampling complexity at the order of O(1/epsilon) is established to ensure the KL divergence smaller than epsilon^2. In comparison, the complexity of second-order Runge–Kutta method (RK-2) scales as O(1/epsilon^2).

### Weaknesses
Although the following paper is posted after your submission, there maybe exist some conflict messages between your paper and this work: you said that RK-2 is less efficient, while this work claimed that RK-2 is provably fast.
Wu, Y., Chen, Y., and Wei, Y. Stochastic runge-kutta methods: Provable acceleration of diffusion models.

Li et al. (2024) also provided a sampling complexity of O(1/epsilon) under KL divergence and a better complexity of O(1/sqrt(epsilon)) for TV, which may reduce the theoretical contribution of this work and was not discussed here.  

There exists some other convergence analysis for high-order sampling of diffusion models. It seems that their rates are better than yours, but such comparisons are missed here.
Huang, D. Z., Huang, J., and Lin, Z. Convergence analysis of probability flow ODE for score-based generative models.
Huang, X., Zou, D., Dong, H., Zhang, Y., Ma, Y.-A., and Zhang, T. Reverse transition kernel: A flexible framework to accelerate diffusion inference.

### Questions
No question.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper investigates the convergence of the second-order discretization method (SDE-DPM-2). Given an $O(\epsilon^2)$ $L^2$-accurate score estimation, the paper demonstrates that the sampling complexity of SDE-DPM-2 is $O(1/\epsilon)$ instead of that of the exponential integrator scheme, which is $O(1/\epsilon^2)$. Furthermore, the paper extends the analysis to the Runge-Kutta-2 (RK-2) method, proving that SDE-DPM-2 exhibits superior efficiency compared to RK-2.

### Strengths
- The paper studies the SDE-DPM-2 scheme for the inference of diffusion models and improves the sample complexity from $O(1/\epsilon^2)$ to $O(1/\epsilon)$.
- The mathematical proof looks sound to me.
- Several experiments are conducted to validate the theoretical findings.

### Weaknesses
 - The assumptions appear overly strong and artificial to me. Unlike the conventional assumption that the neural network score function $s(t, \cdot)$ is approximately $\epsilon^2$ close to the true score function $\nabla \log p_t$, Assumption 2 is, to my understanding, contingent upon the loss function employed in training diffusion models. Consequently, it is not feasible to guarantee or even evaluate this assumption for diffusion models.
- I recommend redrawing Figure 1 in logarithmic scale to corroborate the theoretical findings.
- The proof appears to follow the approach outlined in [1]. I believe it is possible to enhance the sample complexity in the data dimension from $O(d^{3/2})$ to $O(d)$ by drawing techniques inspired by the state-of-the-art results presented in [2].
- I believe this paper lacks a comprehensive literature review. It fails to cite closely related empirical studies [3] and theoretical studies [4, 5], as well as the recent advancements in accelerating diffusion models, such as knowledge distillation [6], consistency models [7], adaptive stepsizes [8], parallel sampling [9], randomized midpoint [10], among others.

### Questions
- Assumptions 3 and 4 are both bounds for the third-order derivative of $\log p_t$. However, I firmly believe that temporal derivatives can be represented as spatial derivatives, thereby revealing fundamental properties of the data distribution, as shown in Equation (22) in [2]. Could you please clarify why Assumptions 3 and 4 are considered separate?
- If Assumption 2 is replaced with the corresponding assumption from [1], is the result for SDE-DPM-2 still valid? Is there any method to ensure the validity of this assumption during the training process?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates the convergence properties of a second-order discretization method, SDE-DPM-2, for diffusion models. The main result demonstrates that SDE-DPM-2 achieves an improved $O(1/\epsilon)$ convergence rate to obtain an $O(\epsilon^2)$ error in KL divergence, surpassing the performance of existing EI discretization methods. Additionally, using similar proof techniques, the paper shows that another widely used second-order method, Runge-Kutta, does not attain this level of convergence. Further analysis extends these results to the VE SDE, achieving a comparable convergence rate.

### Strengths
1. The writing is very clear. It provides both theoretical and empirical comparisons with the most related papers. 

2. It proves a better convergence rate for a second-order sampling method. 

3. It also extends the setting to VE SDEs, showing that the analysis framework can be further generalized.

### Weaknesses
(1) The biggest weakness of this paper is the stringent assumptions. In Assumption 2, this paper assumes the Taylor expansion is accurate, requiring the first derivative of the score function to be closely estimated, which is a stronger condition than value accuracy typically used in SDE analysis. This assumption, while potentially reasonable under Gaussian mixture models as suggested by Meng et al. (2021), is not generally applicable and needs more justification. Specifically, the assumption that the time-derivative of the score function is also close is particularly strong and lacks sufficient motivation. Moreover, Assumptions 3 and 4, which require the score function and its gradient to be bounded, are also very strong, especially when t is close to 0. This implies a smoothness constraint on the data distribution, which is only verified for Gaussian mixtures in Appendix B. This severely limits the applicability of the theoretical results to more complex, real-world data distributions, especially those constrained on low-dimensional manifolds, where such smoothness is not guaranteed. The paper needs to address the limitations of these assumptions and discuss their implications more thoroughly.

(2) The writing of the paper is a little inconsistent. For example, in equation (6), the first-order derivative is approximated with the value of the score function, while in equation (13) it becomes the partial derivative concerning t and x. Moreover, the notation used here, defined in Line 204 is not standard and very confusing. In Line 201, it says “The difference between the EI and SDE-DPM-2 schemes lies in the approximation of the score function”, while in Line 401, it says “The key difference between EI and SDE-DPM-2 lies in the update scheme at each time interval” It is unclear whether they have the same meaning or not.

(3) The description of the contribution is a little bit inaccurate. It claims that SDE-DPM-2 is more efficient than Runge Kutta. However, no guarantee has been given (Corollary 3.3 only shows that the method used in this paper cannot provide a better guarantee for Runge Kutta). It is possible that there exists an analysis of Runge Kutta that can achieve better results.  As is shown in the experiment, the performance of Runge Kutta and SDE-DPM-2 is similar, both better than first-order methods. Thus, the claim seems a little strange to me. Moreover, this paper says that for VE SDE, the convergence is aligned with VP SDE. However, the remark under Corollary 5.1 shows that it only works when overlooking the initial error, which is the key difficulty of VE SDE. This point should also be emphasized in the introduction.

(4) The paper is not self-contained. For example, the proof of Proposition 4.2, directly refers to Chen et al 2023a without any explanation. In my opinion, the argument here is far from trivial and should not be omitted.

### Questions
Is it possible to get a better convergence rate for Runge Kutta methods?

### Soundness
2

### Presentation
2

### Contribution
2

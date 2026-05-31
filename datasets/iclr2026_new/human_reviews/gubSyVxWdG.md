## Human Reviewer 1

### Summary
This paper introduces a new *evaluation framework* for HTE estimators, extending a recently proposed relative error–based framework that compares the performance of two estimators. The proposed approach relaxes a key assumption of the prior method, which required all nuisance parameter estimators to be consistent at a rate faster than n-1/4. In contrast, the new framework only requires the propensity score model to meet this condition, allowing the outcome regression and propensity model to be misspecified. Building on this evaluation framework, the authors further develop a new HTE estimation method and evaluate it on some very often used semi-synthetic datasets, including IHDP, Twins and Jobs, demonstrating improved performance compared to several baseline estimators. The paper also provides sensitivity and ablation analyses to support the empirical findings.

### Strengths
This is a solid paper that addresses an important and interesting problem. The main strengths are:

- Valuable Problem: The paper focuses on the reliable evaluation of HTE estimators, which is a critical issue for real-world applications. The idea of using "relative error" to compare models is novel and meaningful.

- Strong Theoretical Contribution: The highlight of this paper is its theoretical work. It successfully relaxes the strict assumptions from prior work (Gao, 2025), notably by removing the requirement for the outcome model to be correctly specified. This makes the proposed framework much more robust and practical for real-world scenarios, which is a significant and elegant theoretical improvement.

- Clear and Solid Method: The paper is very clearly written and easy to follow. The proposed new loss function and network architecture are well-motivated and tightly connected to the theoretical derivations. The overall approach feels very solid.

- Thorough Experiments: The authors provide convincing results from experiments on several standard datasets. The experimental design is comprehensive, including ablation and sensitivity analyses, which effectively validate the proposed method's effectiveness.

### Weaknesses
- The paper's primary weakness is the unclear practical motivation for using "relative error." While the metric is theoretically interesting for comparing two estimators, its real-world applicability is not well-established. The paper would be significantly stronger if it could provide clear use cases where practitioners would prefer this comparative measure over standard absolute performance metrics like PEHE. This is particularly important for the ICLR audience, which values practical impact.

- The paper is mathematically dense, and while this contributes to its theoretical rigor, it also appears to have led to several typos and minor inconsistencies. To ensure the paper's core contributions are communicated accurately, a thorough proofreading of all definitions, assumptions, and equations is highly recommended.

### Questions
- The paper focuses on HTE estimation but only provides formal definitions for ITE and CATE in the problem setup. For clarity, please provide a precise definition of the HTE you are targeting.

- There appears to be a typo in Assumption 1(i). It should likely be the standard unconfoundedness assumption: $(Y_i(0), Y_i(1)) \perp A_i \mid X_i$. Please clarify and correct this.

- Choice of Evaluation Objective: Line 109 states that the goal is to select the estimator with the highest accuracy on a given test dataset. Could the authors elaborate on why this objective was chosen over the more common goal of finding an estimator that accurately models the CATE function over the marginal distribution of covariates, $P(X)$?

- Example 1 illustrates model misspecification, which is a well-understood concept in statistical machine learning. To improve conciseness, this example could be simplified or moved to the appendix.

- The neural network architecture described in Section 4.3 appears to be the Dragonnet architecture. Could the authors clarify the novelty of their proposed network, or explicitly frame it as an adaptation of Dragonnet for their specific loss functions?

- Experimental Comparison: The paper's main theoretical contribution is relaxing the assumptions of Gao (2025). It would be valuable to include a baseline that represents the Gao (2025) approach or can you clarify how the proposed estimator outperform it?

- Minor Typos: Line 173: "violating Assumption 2" should likely refer to "violating Condition 2". Line 216: The text seems to have a typo and should probably read "...the proposed estimator of... ".

### Soundness
4

### Presentation
3

### Contribution
3

### Rating
8

### Confidence
5

---

## Human Reviewer 2

### Summary
The paper proposes a way of making an estimator of the relative error of two given CATE estimators robust against the misspecification of the mean outcome nuisance \mu_a, relaxing the constraints of existing methods. Furthermore, the by-product of their algorithm could be used to craft a stronger CATE estimator.

### Strengths
- The paper successfully identifies a problem, which is that the existing estimators require asymptotic rates of nuisances no less than n^-¼. 
- Through Taylor expansion, the paper shows the conditions under which higher error rate of \mu does not affect the asymptotic rate of n^-½ of the relative error estimator. This provides interesting theoretical insights.
- The paper designs a novel loss that reformulates the equation-based condition as a minimization problem which allows batch gradient descent.
- The paper shows that the method has practical significance in getting stronger CATE models.

### Weaknesses
1. The paper has limited novelty compared with existing DR estimator Gao (2025). The fundamental form of estimator remains the same as Gao. And the paper seems to just reconstruct the nuisances to meet certain constraints. 
2. The parametrization of e(X) and \mu_a(X) in (1),(2) seem quite arbitrary and lack a decent justification on why these nuisances should share representation. 
3. There is NO solution to the moment-based conditions. To this, soft penalties are introduced for finite-sample optimization. Without the correct specification of propensity (which is never met in real world applications) or sensitivity analysis on the propensity score, I doubt the complete formulation might just go meaningless.
4. Misspecification can also come from the representation $\Phi(X)$.
5. Nuisance overfit could be a problem without sample splitting.
6. Typo: line 1017 should be L_const.
7. Experiment: 1) The paper does not perform sensitivity analysis (empirical) on the propensity score, which makes the practical utility doubtful. 2) The paper does not explain how they compute the \tau in real world datasets Twins and Jobs.3) The paper does not provide convergence analysis of the losses, especially L_const and L_ce. The whole method would only make sense if the paper could show, at least empirically, that under finite samples the two losses successfully approximate the original condition.

### Questions
1. Your asymptotic CI relies on the correct specification of propensities. What happens when this assumption is violated?
2. How is the ground truth $\tau(x)$ constructed for Twins and Jobs
3. Why does the method not require sample-splitting, a standard procedure in orthogonal estimators?
4. Theorem 1 is only correct when Eq.(4) is satisfied, right? But in your method, you cannot make Eq.4 satisfied. Is there any bound analysis?
5. Why is propensity score easier to estimate than the outcome? (line 172 - 175)
6. The complexity of the method seems high. What is the average time cost of achieving an enhanced estimator using your method? And how does it compare to the time cost of training a baseline CATE estimator?

### Soundness
2

### Presentation
1

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper extends the work of (Gao 2025) on the use of relative error for heterogeneous treatment effect estimation. Its main contribution is that it offers a relaxation of the requirement that the nuisance parameter estimators must be consistent. Instead, it is shown that robust estimation can be achieved if the a correctly specified propensity score estimator is provided. Moreover, the theoretical results lead to the development of an HTE method, while both theoretical and experimental results support the arguments of the paper.

### Strengths
- This paper addresses a very important yet understudied problem, and an effective practical solution for the evaluation of HTE estimators is very valuable
 - The paper offers significant theoretical contributions offering theoretical guarantees on estimator consistency even with misspecified regression models
 - In addition to theoretical results on the evaluation of HTE estimators, the paper offers a learning algorithm and method for HTE estimation
 - The empirical evaluation on datasets available in the literature is comprehensive

### Weaknesses
- The need for a correctly specified propensity score model still remains a strong assumption, which may not hold or be guaranteed in practice in many cases.
 - One would expect a deeper evaluation on the comparison of the proposed method against the method by Gao 2025, as well as an empirical evaluation of what happens when the propensity score estimator is misspecified.
 - There is some confusion regarding the terminology, since there is mention of "balance regularizers" in the beginning but later this terminology is abandoned, where $\mathcal{L}_{\text{const}}$ is mentioned

### Questions
- Is there any theoretical or empirical evidence of what happens when the propensity score estimation model is misspecified?
- How do results depend on the number of candidate estimators?

### Soundness
4

### Presentation
4

### Contribution
3

### Rating
8

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper aims to address a very important and critical challenge of CATE estimator evaluation. The authors design a novel loss function and neural network architecture that produces a robust relative error estimate, which remains root-n-consistent.

### Strengths
1. The idea of solving the fundamental and practical CATE evaluation problem is interesting. Evaluating CATE is not easy unless we impose additional structural assumptions. Instead of just using a standard doubly-robust estimator, the authors first derive the specific theoretical conditions required for their estimator to be robust to outcome model misspecification, and then they design a new loss function and a neural network architecture to force the nuisance parameter estimates to satisfy these conditions. This is, somehow, follows the idea of the design of Dragonnet but gives an interesting solution for CATE evaluation.

2. Theoretical results are solid. They establish a theoretical asymptotic property for their proposed estimator, under some assumptions (conditions).

3. The empirical evaluation is through. The experiments strongly support the paper's claims, showing that the proposed method achieves the target 90% confidence interval coverage and high "selection accuracy"

### Weaknesses
1. Can strengthen the connection with other studies (see below question 2&3).

2. The asymptotic property relies on some critical assumptions, for example, $\check{\gamma}, \check{\beta}_0, \check{\beta}_1$ should converge to the true one at a rate faster than $n^{-1/4}$. It is strong but also reasonable. It is reasonable because orthogonal ML literature always assumes the convergence rate of nuisance parameters. It is strong because we are treating them as "plug-in" quantities, instead of the nuisance parameters that the estimator should be doubly robust to. It might be useful to provide some explanations to justify that the condition is realistic.

Overall, I think these are minor weaknesses. The pros outweigh the cons.

### Questions
1. What does the robust evaluation exactly mean? After reading this paper, I guess the author wants to claim the relative error estimator is "doubly robust", so it is robust to nuisance parameter estimation. 

2. What's the difference between your loss and R-loss (R-loss is also doubly robust)?

3. The problem of robust evaluation of the CATE estimator has been studied in [1], where they also consider the worst-case performance of the CATE estimator selected by the proposed evaluation metric. Does this paper also provide any information on the worst-case performance? I guess Figure 1 provides such information, and I suggest emphasizing this point as it can strengthen the efficacy of "robust".

4. A brainstorm: I think the whole framework can be extended to policy/estimator adaptation, e.g., following the setting in [2]. Maybe we can design a new policy evaluation metric that is doubly robust to nuisance parameters, which is very useful when distribution shift presents, and it has not been discussed in previous literature. So this is also a good point of this paper, as it has the potential to be extended to other problems.

[1] Unveiling the Potential of Robustness in Selecting Conditional Average Treatment Effect Estimators

[2] Optimal Policy Adaptation under Covariate Shift

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4
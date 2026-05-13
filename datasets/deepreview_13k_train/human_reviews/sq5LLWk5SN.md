# Mitigating Robust Overfitting in Wasserstein Distributionally Robust Optimization

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
Wasserstein distributionally robust optimization (WDRO) optimizes against worst-case distributional shifts within a specified uncertainty set, leading to enhanced generalization on unseen adversarial examples, compared to standard adversarial training which focuses on pointwise adversarial perturbations. However, WDRO still suffers fundamentally from the robust overfitting problem, as it does not consider statistical error. We address this gap by proposing a novel robust optimization framework under a new uncertainty set for both adversarial noise (Wasserstein distance) and statistical error (Kullback-Leibler divergence). Our theoretical analysis establishes that out-of-distribution adversarial performance is at least as good as the in-distribution robust performance with high probability. Furthermore, we derive conditions under which Stackelberg and Nash equilibria exist between the learner and the adversary. Finally, through extensive experiments, we demonstrate that our method significantly mitigates robust overfitting and enhances robustness within the framework of WDRO.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a new method for distributional robust optimization by considering a relaxation of statistical error in the distribution sets

### Strengths
This paper proposes a new method for distributional robust optimization

### Weaknesses
see the questions below

### questions:
The paper is overall well written. I just have a couple of technical questions:
1. The result in Theorem 3 implicitly assumes that $e^{-\gamma\cdot n} (4/\delta)^m<1$, which is equivalently requiring $\gamma\ge\frac{m\log(4/\delta)}{n}$. As $m$ is the covering number, typically in the order of exp(d) in a d-dimensional space, this implies that $\gamma\ge \exp(d)/n$. Is this a too strict assumption?
2. It would be helpful to show in theory that the standard method without considering the statistical error relaxation fails, while the proposed method succeeds. 
3. Is there a formal theory for the output of Algorithm 1?

### Questions
The paper is overall well written. I just have a couple of technical questions:
1. The result in Theorem 3 implicitly assumes that $e^{-\gamma\cdot n} (4/\delta)^m<1$, which is equivalently requiring $\gamma\ge\frac{m\log(4/\delta)}{n}$. As $m$ is the covering number, typically in the order of exp(d) in a d-dimensional space, this implies that $\gamma\ge \exp(d)/n$. Is this a too strict assumption?
2. It would be helpful to show in theory that the standard method without considering the statistical error relaxation fails, while the proposed method succeeds. 
3. Is there a formal theory for the output of Algorithm 1?

### Soundness
3

### Presentation
3

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
The paper proposes a novel approach called SR-WDRO to address robust overfitting in Wasserstein Distributionally Robust Optimization (WDRO) by incorporating Kullback-Leibler (KL) divergence. While the theoretical contributions are interesting, there are several concerns regarding clarity and experimental validation.

### Strengths
**Theory:**

The mathematical framework is well-developed with thorough theoretical analysis. This paper provides two sets of theoretical results.

The first one is the generalization/robustness bound. The main idea is to show a high probability bound on D ∈ U(D_n) when the uncertainty set is defined with both two divergences. The second one is to establish the Stackelberg and Nash equilibria.

**Experiments:**

The proposed method demonstrates some improvement in mitigating robust overfitting compared to UDR and HR.

### Weaknesses
 
**Clarity Issue:**

The main idea of the paper is summarized in Line 169: "To mitigate this issue, we incorporate the Kullback-Leibler (KL) divergence in WDRO, specifically aiming to reduce statistical error caused by training on finite samples." However, this sentence lacks clarity in three critical aspects:

1. What is the definition of statistical error?

The term "statistical error" appears multiple times starting from the abstract. However, while "statistical" and "error" are very general terms, it is hard to understand what this refers to exactly in the mathematical framework. It is unclear if this refers to the error due to the approximation of the true data distribution by the empirical distribution, or some other form of error. A precise definition within the context of the proposed method is needed.

2. Why is statistical error caused by training on finite samples?

Without a clear definition of statistical error, it is difficult to understand or verify this claim. The paper needs to explain the mechanism by which finite sample training leads to this specific type of error. Is it related to the variance of the empirical risk estimator, or some bias introduced by the limited sample size? This needs to be explicitly stated.

3. Why does incorporating the Kullback-Leibler (KL) divergence in WDRO mitigate this issue?

In the rest of the paper, neither the theoretical results, including the bounds and Nash equilibrium, nor the experimental results provide a clear answer to this question. The paper should provide a clear explanation of how the KL divergence term interacts with the Wasserstein distance to reduce the defined statistical error. It is not enough to simply state that it does; the underlying mechanism needs to be detailed.

**Major Theoretical Concern:**

Sections 3 and 4 demonstrate that SR-WDRO possesses good bounds and equilibria properties. However, the paper does not discuss whether WDRO has or lacks these properties. Without this comparison, it is difficult to verify the necessity of introducing the SR- prefix.

For example, in Theorem 3, one could perform a simple sanity check: 

>By letting γ=0 (which reduces SR-WDRO to WDRO), the generalization bound reduces to $P()\geq0$, which is a meaningless trivial bound. This suggests SR-WDRO has a better generalization bound than WDRO. 

However, the authors should provide a deeper analysis than my simple observation. The analysis should include a discussion of the tightness of the bound and how it compares to existing bounds for WDRO.

The same question applies to Section 4 - do WDRO admit Stackelberg and Nash equilibria under similar assumptions? Without addressing these comparative aspects, the theoretical advantages of SR-WDRO over WDRO remain unclear. The paper needs to explicitly state if standard WDRO also possesses these properties, and if not, why the proposed method is superior.

**Major Experiments Concern:**

1. Regarding robust overfitting, while SR-WDRO outperforms UDR and HR, Figure 2 still shows a decreasing phase. This raises concerns about whether WDRO-type methods are truly necessary in adversarial training settings, especially considering that simpler approaches like SWA or EMA could mitigate the decreasing phase with better performance. The paper should provide a more thorough analysis of why WDRO is needed when simpler methods can achieve similar or better results in mitigating robust overfitting.

2. The comparison of the WDRO-type approaches with other types of adversarial training methods is not provided. As far as I know, it is not competitive with other methods under similar setting, such as no additional data, no generative data, and on ResNet-18. The paper needs to compare against a broader range of adversarial training methods, including those that do not rely on WDRO, to demonstrate the practical significance of the proposed approach.

3. The exclusive use of ResNet-18 is limiting, as the adversarial training community typically requires evaluation on larger models. The paper should include experiments on larger models, such as WideResNet or ResNet-50, to demonstrate the scalability of the proposed method.

### Questions
**Minor:**
 
1.	Eq. (1) and Line 38: Eq.(1) is defined directly in Wasserstein distance rather than the uncertain set. So the description of U(D_n) in line 38 is not self-consistent.

2.	The range of gamma in Theorem 3 is not stated.

3.	Theorem 3, line 204: internal covering number of Z. Line 210: covering number of Z. Line 745: internal covering number of A and covering number of Z. Since the definition with and without internal is different, please clarify these statement precisely.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a novel framework for the problem of Wasserstein distributionally robust optimization (WDRO) by introducing a novel ambiguity set. The effectiveness of the proposed approach is backed by the generalization certificate bound and the authors also establish the existence for the Stackelberg and Nash equilibria of the statistically robust WDRO problem. Empirically, the proposed practical training algorithm demonstrates its advantages on different adversarial robustness benchmarks.

### Strengths
The proposed method seems theoretically sound,  and its effectiveness is supported by different empirical experiments. The authors offer a comprehensive analysis that encompasses both theoretical insights and empirical validations. I commend the authors for their commitment to reproducibility by making their code publicly available. Additionally, the detailed explanations of the experimental setup and the thoughtful interpretation of the results are particularly noteworthy.

### Weaknesses
- The experiments appear to be limited in scope: (i) they only compare against older baselines, and (ii) the model architecture and datasets used are relatively small-scale.
- Empirically, the gains in adversarial robustness seem to come at the expense of natural accuracy, as observed in Table 1.

- Step 10 in Algorithm 1 is not clear to me. How can we compute the optimal weights {pi}?
- Why use $\operatorname{sign}(\nabla_x L(\theta,(x_i^{k-1}, y_i)))$ to update the adversarial examples instead of $(\nabla_x L(\theta,(x_i^{k-1}, y_i)))$?
- A related work [1] that also incorporates both local and global information to optimize distributional robustness is worth discussing.
- As distributional robustness is known to address natural distributional shifts, how well do you expect the method to perform under such circumstances (e.g., domain adaptation/generalization)?

Minor: Typo in line 104

### Questions
- Step 10 in Algorithm 1 is not clear to me. How can we compute the optimal weights {pi}?
- Why use $\operatorname{sign}\left(\nabla_x L\left(\theta,\left(x_i^{k-1}, y_i\right)\right)\right)$ to update the adversarial examples instead of $\left(\nabla_x L\left(\theta,\left(x_i^{k-1}, y_i\right)\right)\right)$?
- A related work [1] that also incorporates both local and global information to optimize distributional robustness is worth discussing.
- As distributional robustness is known to address natural distributional shifts, how well do you expect the method to perform under such circumstances (e.g., domain adaptation/generalization)?

[1] Phan, Hoang, et al. "Global-local regularization via distributional robustness." International Conference on Artificial Intelligence and Statistics. PMLR, 2023.

Minor: Typo in line 104

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the Wasserstein distributionally robust optimization (WDRO) and considers both the adversarial attack and statistical error in the framework. Additional discussions are also provided in terms of the Stackelberg and Nash equilibria.

### Strengths
(1) The paper is clear and easy to understand. 

(2) The theoretical analysis is also sound. 

(3) The Nash equilibria perspective is interesting.

### Weaknesses
 (1) The numerical experiments only demonstrate limited improvements. 

(2) There is no enough highlight on the technical challenges.

(3) Based on existing litertaure,

Li, Binghui, and Yuanzhi Li. "Why clean generalization and robust overfitting both happen in adversarial training." (2023).

the robust overfitting phenomenon is more severe in the scenario of neural networks. Could the authors point out any possible way of analyzing WDRO in neural networks?

### Questions
Please address my comments in the weakness section.

### Soundness
3

### Presentation
3

### Contribution
3

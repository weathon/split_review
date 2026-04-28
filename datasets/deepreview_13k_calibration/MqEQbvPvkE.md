# Causal Estimation of Exposure Shifts with Neural Networks: Evaluating the Health Benefits of Stricter Air Quality Standards in the US

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 3, 6, 6

## Abstract
In policy research, one of the most critical analytic tasks is to estimate the causal effect of a policy-relevant shift to the distribution of a continuous exposure/treatment on an outcome of interest. We call this problem *shift-response function* (SRF) estimation. Existing neural network methods involving robust causal-effect estimators lack theoretical guarantees and practical implementations for SRF estimation. Motivated by a key policy-relevant question in public health, we develop a neural network method and its theoretical underpinnings to estimate SRFs with robustness and efficiency guarantees. We then apply our method to data consisting of 68 million individuals and 27 million deaths across the U.S. to estimate the causal effect from revising the US National Ambient Air Quality Standards (NAAQS) for $\text{PM}_{2.5}$ from 12 to 9 $\mu g/m^3$ . This change has been recently proposed by the US Environmental Protection Agency (EPA). Our goal is to estimate, for the first time, the reduction in deaths that would result from this anticipated revision using causal methods for SRFs. Our proposed method, called Targeted Regularization for Exposure Shifts with Neural Networks (TRESNET), contributes to the neural network literature for causal inference in two ways: first, it proposes a targeted regularization loss with theoretical properties that ensure double robustness and achieves asymptotic efficiency specific for SRF estimation; second, it enables loss functions from the exponential family of distributions to accommodate non-continuous outcome distributions (such as hospitalization or mortality counts). We complement our application with benchmark experiments that demonstrate TRESNET's broad applicability and competitiveness.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This study provides a strong framework for treatment effect estimation based on the semiparametric theory. The authors develop a novel optimization problem for treatment effect estimation and show the asymptotic properties.

### Strengths
My major curiosity lies in the proof of Theorem 2. As discussed in the literature of double machine learning (cf. Chernozhukov et al. (2018)), to attain $\sqrt{n}$-convergence of semiparametric estimators, we usually impose the Donsker condition for (nonparametric) nuisance estimators. However, it seems that the authors do not impose such assumptions. I am checking the proof, but could the authors provide intuitive reasons for the results? If this result is true, I believe that this is the theoretical strength of this study.

The above is also my concern because the posited assumptions are too weak to show the results. We usually impose some properties such as smoothness on the nuisance estimators to discuss convergence rates. Even if we obtain desirable convergence rates, neural network models usually do not satisfy the Donsker conditions. Therefore, I am afraid of missing assumptions or errorrness in the proof (I need to confirm the proof but have not yet done it...).

### Weaknesses
My major curiosity, which is also my major concern, lies in the proof of Theorem 2. The authors seem to bypass the need for imposing the Donsker condition, typically required for attaining $\sqrt{n}$-convergence of semiparametric estimators as discussed in the context of double machine learning [1]. This raises concerns about the validity of the results, especially since the posited assumptions appear insufficient. In standard practice, we usually impose properties like smoothness on nuisance estimators to discuss convergence rates. The potential absence of such assumptions or an error in the proof is concerning, given that even with desirable convergence rates, neural network models often fail to satisfy Donsker conditions.

Furthermore, Assumption 2.2 appears to be too weak. If $p(a|x) \propto 1/n$ for some $a$, the results might not hold. It seems that $p(a|x)$ should be lower bounded by a positive constant independent of $n$ to ensure the stability of the density ratios. In Theorem 2, the notation $\to$ is ambiguous; it should be clarified whether it indicates convergence of non-random variables or convergence in probability. Similarly, the meaning of $O(r_1(n))$ in $\|\hat{\mu} - \mu\|_\infty$ needs clarification - should it be $O_P$ to denote the order in probability? The citation of [2] seems misplaced, as their focus on density-ratio estimation differs significantly from the current study. Additionally, the connection between this study and the automatic debiased learning proposed by [3] is not adequately addressed. Finally, the statement "for some function $\eta:\mathcal{X}\times\mathcal{A}\to\mathbb{R}$" should be more precise, specifying "for some measurable function $\eta:\mathcal{X}\times\mathcal{A}\to\mathbb{R}$". The relationship between the shift-response function and the standard average treatment effect needs further clarification. Some citations appear to be missing, hindering a complete understanding of the related work.

### Questions
- Is Assumption 2.2 sufficient? If $p(a|x) \propto 1/n$ for some $a$, then the results do not hold, I think $p(a|x)$ should be lower bounded by a positive constant independent of $n$.
- In Theorem 2, what does $\to$ indicate? Convergence of non-random variables or convergence in probability?
- In Theorem 2, what does $O(r_1(n))$ in $\|\hat{\mu} - \mu\|_\infty$ mean? Should it be $O_P$?
- Sugiyama et al. (2012) discussed the density-ratio estimation, and its interest differs from this study. Furthermore, it has been known that Eq. (8) can be used to estimate the propensity score. I think the citation may not be appropriate.
- Does this study relate to automatic debiased learning proposed by Chernozhukov et al. (2022)?
- "for some function $\eta:\mathcal{X}\times\mathcal{A}\to\mathbb{R}$" should be for "for some measurable function $\eta:\mathcal{X}\times\mathcal{A}\to\mathbb{R}$"?
- Does the shift-response function is the same as the standard average treatment effect?
- Some citations are missing.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a neural network-based method, termed Targeted Regularization for Exposure Shifts with Neural Networks (TRESNET), to perform shift-response function (SRF) estimation for determining the causal effect of policy changes. The specific focus is on the effect of the proposed revision to the US National Ambient Air Quality Standards on mortality rates. The proposed TRESNET method introduces a targeted regularization loss tailored for SRF estimation, which ensures double robustness and asymptotic efficiency.

### Strengths
1. The paper addresses a meaningful real-world issue – evaluating the health benefits of air quality standards.

2. The proposed TRESNET method introduces a targeted regularization loss tailored for SRF estimation, which ensures double robustness and asymptotic efficiency.

### Weaknesses
1. The problem of this paper was not well presented. For example, the key concept of exposure shift is very confusing. The notation $\tilde{A}$ is used first without definition in Section 2. How is the potential outcome framework defined under $\tilde{A}$? The equation (1) is also problematic as it should be $a\sim \tilde{p}(\tilde{A}|X)$. The authors need to clarify how the shifted exposure $\tilde{A}$ relates to the original exposure $A$ within the potential outcome framework, especially when considering the counterfactual outcomes under $\tilde{A}$.

2. The assumptions of this work also need more justifications. It looks like all the causal identification assumptions are based on the original treatment $A$ except the positivity assumption. Since the efficient function also contains $\mu(X, \tilde{A})$, would more assumptions on $\tilde{A}$ be needed like SUTVA? Specifically, the paper needs to explicitly state how the assumptions on $A$ translate to assumptions on $\tilde{A}$ to ensure identifiability of the shift-response function. The current assumptions are insufficient to guarantee the validity of the causal inference under the shifted exposure.

3. The proposed method is not new compared with the semiparametric literature and causal inference, by considering double robustness and the density ratio of two propensities. Please find the references below and justify them.

- Yang, Shu, and Peng Ding. "Combining multiple observational data sources to estimate causal effects." Journal of the American Statistical Association (2019).
- Kallus, Nathan, and Xiaojie Mao. "On the role of surrogates in the efficient estimation of treatment effects with limited outcome data." arXiv preprint arXiv:2003.12408 (2020).

 The paper needs to clearly differentiate its approach from existing methods that use density ratios for causal inference, such as those in the provided references. The novelty of the proposed method is not well-established given the existing literature on double robustness and propensity score weighting.

4. The theoretical connections between Section 3 and Section 4 are weak. There are many theoretical works related to using neural network methods for nuisance function estimation. The authors may consider the following reference to complete the gap.

- Farrell, Max H., Tengyuan Liang, and Sanjog Misra. "Deep neural networks for estimation and inference." Econometrica 89.1 (2021): 181-213.

The paper needs to provide a more detailed explanation of how the theoretical results in Section 3 connect to the neural network implementation in Section 4. The current discussion lacks a rigorous justification for using neural networks in this context, especially considering the existing theoretical work on neural network estimation.

5. Since the efficient influence function is derived, given Theorem 2, I am curious why not continue to get the asymptotic normality of the proposed effect? Specifically, the authors are using the asymptotic normal formula in their simulations. Or if the authors think it is challenging, why can you use this result directly in the simulation? The paper should either derive the asymptotic normality of the estimator or provide a clear justification for why it is not feasible, especially since the simulation results rely on this property.

6. Since the double robustness is one major advantage of the proposed method, it is better to conduct simulation studies to reflect this property. The simulation studies should explicitly demonstrate the double robustness property of the proposed method by varying the accuracy of the nuisance function estimations.

7. Mics: The reference at the bottom of page 5 is missing.

### Questions
See questions in *Weaknesses*.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considers the problem of shift response function estimation, with applications 
to evaluating the health benefits of stricter air quality standards in the US.

The proposed method falls into the framework of AIPW, where both the outcome model and the 
propensities are trained via neural networks with regularization terms. The authors provide 
theoretical results supporting that the resulting estimator indeed is double robust and efficient. The method 
is evaluated on synthetic data and applied to the evaluation of the health benefit of stricter 
air quality standards.

### Strengths
1. The paper is very well-written: it is concise and contains sufficient details.
2. I think this work is a good combination of application and theory. Motivated by an important 
practical question, the authors formulate it as a mathematical problem, providing solutions 
backed with theoretical results.

### Weaknesses
The theoretical result is not particularly surprising given the existing literature on double-robustness and efficiency (although I do like the application side of this work).

### Questions
1. I am in general curious about the reason for choosing neural networks to fit the propensities and 
the outcome model. How do they compare with, say, tree-based methods?
2. In many scenarios, the multiple shifts are being considered simultaneously, should there be adjustment 
for the multiplicity?
3. Some minor points: 

  (a) in equation (1), should $\mu(x,a)$ be $\mu(X,\tilde{A})$?

  (b) there is a missing reference at the bottom of page 5.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors consider so-called shift-response function (SRF) estimation with neural network methods, which is motivated by a policy-relevant question in public health, and statistical robustness and efficiency consideration. They apply their method to data consisting of 68 million individuals and 27 million deaths across the U.S. to estimate the causal effect from revising the US National Ambient Air Quality Standards (NAAQS) for PM2.5 from 12 μg/m3 to 9 μg/m3.

### Strengths
The problem is well motivated and the application is interesting.

### Weaknesses
I am not fully convinced about this causal estimand. In Section C's example, why $c$ is a better number than 0? Can the authors clarify?

Can the shift of treatment be stochastic?

Some key references on doubly robust estimator and efficiency of causal effect estimation are missing, for example, Robins's work.

Should $\mu(x,a)$ is (1) $\mu(X,\bar A)$?

There are typos, for example, in Section C, EIF should be ERF; some references are broken.

### Questions
Please refer to Weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

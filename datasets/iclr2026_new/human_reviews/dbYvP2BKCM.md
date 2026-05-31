## Human Reviewer 1

### Summary
This paper introduces ZNet, a novel deep learning framework that addresses the critical challenge of unobserved confounding in causal effect estimation from observational data. Its primary contribution lies in automatically constructing valid instrumental variables (IVs) by decomposing observed variables into latent representations that satisfy core IV assumptions—relevance, exclusion restriction, and unconfoundedness. Unlike existing methods that require pre-specified candidate IVs, ZNet's architecture explicitly encodes the structural causal model of IVs, enabling it to function as a plug-in module for various two-stage IV estimators. Experimental results demonstrate that ZNet can both recover ground-truth instruments when available and generate proxy latent instruments that effectively reduce estimation bias when no explicit IVs exist, offering a flexible solution for causal inference in general observational settings where unconfoundedness cannot be verified.

### Strengths
The paper demonstrates significant originality by shifting the paradigm from selecting candidate instruments to constructing them directly from observed data. Unlike methods that require pre-specified IV candidates, ZNet automatically decomposes covariates into valid instrumental and confounder representations through a structurally-informed architecture, creatively combining deep learning with causal constraints.

This conceptual contribution is well-supported by high methodological rigor. ZNet's losses directly enforce IV assumptions, and comprehensive experiments show it both recovers true instruments and constructs effective proxies when none exist. Its robust performance across diverse settings—including when unobserved confounding is absent—underscores its practical significance as a reliable, plug-in causal estimator.

### Weaknesses
While the paper positions ZNet as a novel paradigm for IV construction, the core idea of learning instrumental variable representations from data is an established research direction.  Several prior works have the explicit goal of generating valid IVs from observed covariates without pre-specified candidates, using variational and mutual information-based approaches. The architectural difference of ZNet—learning a decomposition based on an SCM—is a technical contribution but does not constitute a paradigm shift.  

A more critical weakness is the exclusive reliance on semi-synthetic datasets for experimental validation.   While useful for controlled testing with known ground truth, this setup fails to demonstrate the method's applicability to real-world problems. Furthermore, the absence of an evaluation on a real-world dataset with no ground-truth effect (e.g., a standard observational causal inference benchmark) leaves the practical utility in doubt.  For the method to be considered a "plug-in" solution, it must be validated in settings that mirror the true uncertainty of observational studies.

"Moreover, all code to generate models, synthetic data, and experiments will be made public upon publication." I suggest publish in the review period.

### Questions
Please see my concerns in weakness.

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper addresses the practical challenge of identifying valid instrumental variables (IVs) by proposing ZNet, a decomposition-based framework that learns latent representations satisfying the standard IV assumptions. When real instrumental variables exist in the data, ZNet is able to recover them; when no explicit IVs are available, ZNet can construct proxy latent IVs to facilitate causal effect estimation.

### Strengths
1.The proposed method is conceptually simple and easy to understand.

2.The experiments are comprehensive and cover diverse data scenarios.

### Weaknesses
1.Lack of clear novelty. Recovering instrumental variables from observational data is a well-known open problem, and several prior works (e.g., DIV.VAE, GDIV, AutoIV) have explored similar directions. The authors should clarify the key distinctions between ZNet and these existing approaches in terms of motivation, design, or theoretical guarantees.

2. Equations 5 and 6 fail to demonstrate the lack of confounding in instrumental variables. In Equation 5, the outcome variable Y is directly predicted using the covariate X and the treatment variable T, which inherently incorporates confounding factors. Furthermore, in Equation 6, the meaning of Y - \hat_{Y} is unclear. Why does its uncorrelated nature with Z guarantee that the instrumental variable Z is free from confounding?

3. Similarly, exclusivity and relevance cannot be satisfied. Crucially, how does the author ensure that f(X) and g(X) capture the confounding factor C and the instrumental variable Z, respectively? Without clarifying this key point, the validity of Equations 7–9 cannot be guaranteed.

4. The superiority of ZNet cannot be assured. Based on the experimental data in Table 1, ZNet does not demonstrate outstanding performance.

5. The definition of an IV ("An IV is a variable that influences the treatment but has no direct effect on the out come or influence from
 unobserved confounders.") in abstact is wrong. 

6. The second condition, i.e., "Exclusion restriction" (page 2) is wrong. It should be Z⊥Y|(T,C, e_Y). 

7.  CATE(C)=E[Y|do(T)=1,C]−E[Y|do(T)=0,C], and  ATE=E_C[CATE] seems to be wrong. Based on the standard definition of ATE, 
ATE should be E[Y|do(T)=1]−E[Y|do(T)=0], rather than CATE(C).

### Questions
See Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
5

---

## Human Reviewer 3

### Summary
this paper proposes a method for decomposing the observed variables to find a representation which satisfies the standard IV assumptions of relevance, exclusion restriction, and unconfoundedness. The experiments validates the effectiveness of ZNet.

### Strengths
Generally clear and readable; figures and tables are informative;

### Weaknesses
1. Results are synthetic; real-world case studiesare absent. 
2. In some regimes/methods ZNet is not best. A deeper error analysis would help users decide when ZNet is reliable

### Questions
N/A

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
6

### Confidence
1

---

## Human Reviewer 4

### Summary
The paper proposes a novel method to learn instrumental variables from the confounders in the dataset. With the help of the learned instruments, treatment effects can be identified and estimated even in the presence of unobserved confounders. Based on an additive loss including multiple single-task losses, the final estimate is forced to comply with the necessary assumptions of IVs. The paper empirically validates the new method ZNet.

### Strengths
- The paper includes a rather extensive empirical evaluation.
- To the best of my knowledge, the idea of learning instruments (not instrument representations) from the existing dataset, fulfilling the necessary requirements for valid IVs, is novel.

### Weaknesses
- The paper does not include any mathematical guarantees for the validity of the method. Therefore, it cannot be guaranteed that the learned IVs are actually valid IVs, potentially rendering the causal effect unidentifiable. I consider this the main and very severe weakness of the work.
- The paper assumes that there exists a subset of the confounders that can serve as instruments. However, this is not necessarily the case in practice.
- The paper makes the strong assumption that the instrument is sampled from a normal distribution. The reasoning behind this assumption is neither explained nor is the validity discussed.
- The provided loss is only suitable for valid IVs if the final loss terms related to independence requirements are truly 0. However, this is neither shown nor discussed (neither theoretically nor empirically).
- Evaluation: The method is only evaluated for ATE estimation based on the mean error. For better (and fairer) comparison, the method should also be evaluated for CATE estimation based on the PEHE.

### Questions
- Very likely, the confounders will not include suitable instruments. How does the method (theoretically) behave in this failure mode? In this case, the treatment effect is theoretically still not point-identified.
- Lemma 1: With which justification can Z be assumed to stem from a normal distribution? How would one define the variance of the distribution?
- Lines 235-237: What is the reasoning behind this model specification?
- Why is the PC-loss a good choice for the loss term? Why not use the HSIC? This is not discussed. Furthermore, to evaluate the loss, the covariance and standard deviations need to be estimated. What happens if the estimation is incorrect?
- How does the method perform for continuous treatments? Here, the representations might be more difficult to learn.

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
4
# Differentially private learners for heterogeneous treatment effects

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
Patient data is widely used to estimate heterogeneous treatment effects and understand the effectiveness and safety of drugs. Yet, patient data includes highly
sensitive information that must be kept private. In this work, we aim to estimate
the conditional average treatment effect (CATE) from observational data under
differential privacy. Specifically, we present DP-CATE, a novel framework for
CATE estimation that is *doubly robust* and ensures *differential privacy* of the estimates. For this, we build upon non-trivial tools from semi-parametric and robust statistics to exploit the connection between privacy and model robustness.
Our framework is highly general and applies to any two-stage CATE meta-learner
with a Neyman-orthogonal loss function. It can be used with all machine learning models employed for nuisance estimation. We further provide an extension
of DP-CATE where we employ RKHS regression to release the complete doubly
robust CATE function while ensuring differential privacy. We demonstrate the effectiveness of DP-CATE across various experiments using synthetic and real-world
datasets. To the best of our knowledge, we are the first to provide a framework for
CATE estimation that is doubly robust and differentially private.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This study proposes two new methods to address the problem of computing CATE estimates under differential privacy. Leveraging the often used assumption of number of queries being known a priori the authors develop a method that uses influence functions as an upper bound to the smooth sensitivity quantity. This is used in a traditional output perturbation algorithm of the CATE estimate to calibrate the Gaussian noise. The second method is for releasing the CATE function in its entirety under differential privacy. This is a much more difficult problem. The authors develop an algorithm that guarantees DP by using a calibrated Gaussian process to modify the output of the original CATE algorithm. They develop an algorithm for determining how to calibrate this process leveraging theory about RKHSs and Gaussian kernel regression. The efficacy of these algorithms are demonstrated on synthetic datasets where access to the ground truth CATE is available and observational medical datasets.

### Strengths
- By and large this is a well-written paper and it was easy to understand what both algorithms were doing at a high-level.
- The methods provide more flexibility than prior work in supporting all types of ML models
- The separation between knowing the number of queries a priori and not is well taken as it allows them to build a stronger estimator in the fixed query setting
- The experiments show some promise that the estimator is relatively close to the ground truth in the synthetic experiments

### Weaknesses
 - The algorithm for releasing the CATE function assumes knowledge of the Lipschitz constant which unless I am mistaken seems like an unrealistic assumption (note I am not concerned with assuming Lipschitzness of the loss)
- More details about the experiments are needed to help understand them. Right now the details are quite sparse so it’s difficult to contextualize them in each of the challenges described. I leave my questions related to this for the Questions section of the review.
- Unless I am misunderstanding Figure 6 and 7, it seems like th CATE is constant along the ages / covariates for each task? If so, this is not as compelling for the success of this method. I think like the synthetic dataset, an observational task should be chosen where the CATE differs based on the covariate I will be adjusting. It’s important to understand how well the DP estimator can capture the variation in CATE as the condition covariate changes.

### Questions
1. How many queries were done for Dataset 1 (Figure 3 and 4)?
2. Do the authors have a sense for how tight they think the upper bound for smooth sensitivity is using the gross error sensitivity? Is there room to make it tighter with more assumptions?
3. In Figure 4, it seems like DP-CATE consistently underestimates the CATE at the 0.01 privacy budget. Is there any intuition and/or concrete results on whether this method tends to underestimate or overestimate?
4. What does y-axis represent in Figure 6 and 7? Is it the actual CATE or is it the error?
5. How was the Lipschitz constant computed for the empirical results?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies the problem of causal inference with sensitive observational data with DP, motivated by medical applications.  specifically, the authors study estimtaing the CATE function (conditional average treatment effect), which as the name implies, quantifies the effect of a treatment as a function of some covariate.  The authors propose a simple output perturbation mechanism to estimate the CATE with DP.

### Strengths
* The paper is technically sound and statistically rigorous.
* The problem studied is novel and of practical interest.
* The paper is clearly written and nicely polished.

### Weaknesses
 * The paper uses some jargon that may not be familiar to the reader (e.g., doubly-robust). 
* There are no comparisons to baselines.  While the problem studied is new there are no published baselines on this approach, there are some simple baselines you could compare against.  
> * Here's one: in 1D case you study in e.g., Fig 1, 6 just compute the CATE function non-parametrically.  That is, compute COUNT(Y=1, a <= X <= b) and COUNT(Y=0, a <= X <= b) for a variety of intervals in the domain, from which you can estimate CATE easily.
> * To handle higher dimensional case, you could compute those counts for each covariate and then make some kind of conditional independence assumption.  In the p=2 case you consider in experiments, you could also just directly compute the full histogram and it should be pretty doable.   I would assume there are both qualitative and quantitative advantages to your approach, but I think it would be good to demonstrate that explicitly.  
> * From the idea above, it seems this can be framed as a marginal-preservation problem, a problem that many synthetic data algorithms are pretty good at (e.g., PrivBayes).  That could be another baseline.

### Questions
* In the problem statement, do you have any constraints on the domain of X?  In practice is it usually a small domain (e.g., one feature) or large domain (many features)?  
*  In the finitely many queries setting, can you be more precise about the typical characteristics of the setting?  How many queries is typical, and what do those queries look like?
>* If the number of queries is small (e.g., quantify CATE for ages 0-20, 20-30, 30-40, ...,) then the problem is trivial.
>* I think it would be good to give a motivating example to make the abstract problem formulation you have a bit more grounded.

### Soundness
3

### Presentation
4

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
This paper presents  a new framework (DP-CATE) for estimating conditional average treatment effects (CATE) under differential privacy while ensuring double robustness (see below my comment on robustness). DP-CATE is broadly applicable to two-stage CATE meta-learners with a Neyman-orthogonal loss. The framework can perform both pointwise estimation of the CATE function and direct functional estimation. The authors provide experimental results on synthetic and real data that demonstrate the effectiveness of DP-CATE.

### Strengths
- The paper is exceptionally well-written and easy to follow, providing a clear presentation of complex concepts.
- The authors present a well-founded methodology and provide rigorous mathematical analysis.
- Experimental results on both synthetic and real data help to validate the proposed framework.
- The framework is general and flexible, covering a wide range of learning algorithms without making unrealistic assumptions.
- The discussion in line 314 about the relationship between doubly robust learners and smooth sensitivity offers an interesting insight that could have broader implications.

### Weaknesses
 - While the authors discuss the novelty of their work on functional data privacy, they underplay previous work in this area. Notably, Hall et al. (2013) provides a mechanism for functional data, which the authors should highlight more explicitly to offer better context for readers.
- The use of “robustness” could be misleading, as it carries different meanings across fields. Clarifying what robustness specifically entails here would be helpful, especially considering existing work on “privacy and robustness.” Specifically, the authors should clarify if they are referring to robustness to model misspecification, outliers, or other forms of perturbations. The term 'double robustness' is used, but it's not clear if this is the only type of robustness considered.
- Certain definitions, such as those on line 157, could be recalled for clarity. Additionally, the definition of Y ( ⋅ )    used on line 160 appears to be missing, which may cause confusion. The lack of a clear definition for this function makes it difficult to fully understand the subsequent derivations.

### Questions
- How does the proposed approach for functional data compare to the techniques in Hall et al. (2013)? Highlighting these distinctions would provide valuable context for readers.
- While the framework is general, how does its performance compare numerically to similar algorithms (e.g.,Betlei et al. (2017), Guha & Reiter (2024) and Niu et al. (2019)) in settings where those methods are applicable?
- Could the authors provide insights on how functional estimation compares to pointwise estimation in practical scenarios?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a novel, privacy-preserving approach for estimating the Conditional Average Treatment Effect (CATE), motivated by the need for privacy in electronic health records. The authors propose DP-CATE, a flexible framework that ensures differential privacy while maintaining double robustness in CATE estimation. The framework is offered in two versions: one for finite queries (e.g., treatment effects for specific patient groups) and another for functional queries (releasing the complete CATE function). A key technical innovation lies in calibrating noise using influence functions for finite queries and Gaussian processes for functional queries. The authors provide theoretical privacy guarantees and demonstrate the framework's effectiveness using both synthetic data and real-world medical datasets (MIMIC-III and TCGA).

### Strengths
- The presentation of this paper is clear and well-organized.
- It addresses an important practical problem: ensuring privacy in treatment effect estimation from sensitive medical data.
- The proposed DP-CATE framework is highly flexible and model-agnostic, compatible with any doubly robust meta-learner and machine learning model.
- The authors provide theoretical guarantees for differential privacy while preserving the double robustness property.

### Weaknesses
 - The paper does not sufficiently analyze the consistency of the proposed estimators, i.e., whether the estimators remain consistent.
- The presentation of the identification condition (3) is unclear. The authors should clarify the assumptions (e.g., unconfoundedness) under which the optimizer of (3) represents the true conditional average treatment effect function.
- Theorem 1 builds upon the work of Avella-Medina (2021). The authors seek an upper bound on $\zeta$-smooth sensitivity to ensure privacy. However, is this bound tight, and might there be a more optimal bound for $\zeta$-smooth sensitivity?
- Could the authors comment on the inclusivity of the two proposed methods? For example, if one generates a functional query and then uses it to answer finite queries, what would be the potential advantages or disadvantages of this approach?

### Questions
See weaknesses.

### Soundness
3

### Presentation
4

### Contribution
2

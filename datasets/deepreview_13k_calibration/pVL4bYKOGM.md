# Conformal prediction for causal effects of continuous treatments

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 6, 5, 5

## Abstract
Uncertainty quantification of causal effects is crucial for safety-critical applications such as personalized medicine. A powerful approach for this is conformal prediction, which has several practical benefits due to model-agnostic finite-sample guarantees. Yet, existing methods for conformal prediction of causal effects are limited to binary/discrete treatments and make highly restrictive assumptions such as known propensity scores. In this work, we provide a novel conformal prediction method for potential outcomes of continuous treatments. We account for the additional uncertainty introduced through propensity estimation so that our conformal prediction intervals are valid even if the propensity score is unknown. Our contributions are three-fold: (1)~We derive finite-sample prediction intervals for potential outcomes of continuous treatments. (2)~We provide an algorithm for calculating the derived intervals. (3)~We demonstrate the effectiveness of the conformal prediction intervals in experiments on synthetic and real-world datasets. To the best of our knowledge, we are the first to propose conformal prediction for continuous treatments when the propensity score is unknown and must be estimated from data.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a conformal prediction method for continuous treatments, addressing the challenge of unknown propensity scores. It derives finite-sample prediction intervals, provides an algorithm for calculating them, and demonstrates effectiveness on synthetic and real datasets. This is the first method for continuous treatments with unknown propensity scores.

### Strengths
Clear writing & solid theoretical results

### Weaknesses
The reviewer is not an expert in conformal prediction for causal inference but would assume there are working targeting the studies setting: uncertainty quantification of causal effects for continuous treatment.

Equation 14 seems to use the kernel function to approximate the indicator function. Does this imply some smoothness assumptions?

The optimal parameter $\sigma^*$ represents a trade-off between the uncertainty in the prediction and the uncertainty in the interval construction. It is similar to the bandwidth approximation of the indicator function using a kernel function. Are there any empirical values ​​here, such as \sigma = cn^{-2/5} to  trade-off between the prediction and interval.

The method is demonstrated on specific datasets and scenarios. While the authors claim that their method scales to high-dimensional settings, further validation on a broader range of datasets and treatment types would strengthen the generalizability of the findings.

### Questions
See weakness.

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
In the paper, the authors propose a Conformal-prediction (CP) based method to obtain the interval estimation of the potential outcomes under continuous treatments. 
To achieve this, the authors follows (Gibbs et al., 2023; Romano et al., 2019) and reformulated split CP as an augmented quantile regression.
The authors derive finite-sample prediction intervals for cases where the propensity score function is known and unknown.
Moreover, they provide finite-sample theoretical guarantees.

### Strengths
1. They study a very important question in the causal inference and provide novel methods. 
2. They provide the finite-sample theorem for their methods. 
3. They clearly and accessibly present the research question and methods, using figures and concrete examples.

### Weaknesses
The authors do not have a good evaluation of their method in terms of numerical studies.

Firstly, the authors only focus on the empirical coverage, and claim that it should be the higher the better. 
In my opinion, it seems not very reasonable. 
If we simply choose the [-inf, inf] as the interval, it is always has the 100% empirical coverage. 
A more balanced evaluation should consider both the interval length and empirical coverage. Additionally, the empirical coverage should closely match the nominal coverage for optimal results.


When checking the numerical results, I do believe the method in the implementation is not very stable under some cases. 
For example, in Fig 4 ($\alpha=0.2$, 5), with only 50 repetitions, I can see many outliers in the boxplot, indicating there may be some issues there. Similar issue can be found in Fig 5 ($\alpha=0.1$, 1) and  ($\alpha=0.2$, 5). 
Anyway, I know such unstableness may be inevitable for a complicated method, I think the authors should have some discussions on this issue.

### Questions
1. Major question is in **Weakness** part 
2. I think the real data in the paper can not justify the superiority of authors' method well as I can see at range [0.6, 1], it yields not very reasonable prediction (blood pressure can be less than 0). 
Also, the interval estimate is too wide to be meaningful.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Conformal prediction for causal estimands is useful because it provides finite-sample coverage guarantees. Predicting potential outcomes is challenging due to the potentially unknown distribution shift between the training set and the test set, which is subject to intervention. This work extends conformal prediction under domain shift to address the challenges that are introduced when the treatment variable is continuous, and the causal estimand is a dose response.

### Strengths
The problem of conformal prediction of dose responses is clearly significant. The authors proposed an original formulation that uses Gaussian smoothing over the treatments and finds an optimal bandwidth for each problem instance. It is also important to consider soft interventions (by the authors' definition) in addition to hard interventions, since it is common in medicine and other settings to study incremental changes.

### Weaknesses
 * I do not understand some core elements of the motivation. What is the intention behind the separation of challenge (a) and challenge (b)? Estimating the propensity score is more difficult with continuous treatments, but it is still a challenge with discrete treatments. By my understanding, the main challenge for bringing conformal prediction to continuous treatments is that you rarely see data points with the same treatment value, so you have to do some sort of smoothing. The motivating challenges do not mention this (unless I am misreading one of them).
 * I also found the roles of soft and hard interventions confusing. Under "Scenarios" in Section 4, the authors explain that soft interventions are relevant when the propensity is known, while hard interventions are reserved for when the propensity is unknown. This storyline is convenient for the mathematical derivations. However, I am not convinced: even if the propensity function is unknown, it can still be of interest to estimate the effect of increasing the treatment by a small amount on top of the existing policy. These cases have been studied before:
   * Many papers by Chernozhukov et al. that mention "average causal derivatives"
   * Marmarelis et al. "Policy Learning for Localized Interventions from Observational Data" in AISTATS 2024.
 * When the propensity / policy is unknown, the validity of the conformal prediction relies on a constant $M$ that bounds the error of the estimated propensity. This resembles a sensitivity analysis. It appears difficult to know which $M$ to use.
 * The results from the medical dataset do not seem convincing. It is good to see that intervals are wider in treatment regions that are less common in the data. However, the fact that intervals are wider than MC-dropout is not necessarily a good thing.

Minor notes.
 * "Quantile regression might yield non-unique solutions, so we later restrict the analysis to solvers invariant to the data ordering". Please expand on this sentence. How does ordering invariance help?
 * The algorithm text is small and quite dense.
 * An interpretation of the optimized $\sigma$ is provided in the supplement, but further discussion would be helpful. Please clarify its role in the optimization problem.

### Questions
* Consider building semi-synthetic experiments for stronger results.
 * How can $M$ of Assumption 1 be calibrated in practice, for tightness?
 * Do you assume some kind of continuity in the dose response?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper applies the framework introduced by Gibbs et al. (2023) to produce prediction intervals, with a finite-sample coverage guarantee, for potential outcomes of continuous treatments. Gibbs et al. (2023) can provide certain types of conditional coverage guarantees by reformulating the coverage as coverage over a class of covariate shifts. Gibbs et al. (2023) already showed that given an appropriate choice of $\mathcal{F}$, that their prediction set achieves coverage under covariate shift, so long that the covariate shift can be represented as, $P_X$ titled by $f$, and $f \in \mathcal{F}$.

This work postulates the causal effect of continuous treatments as soft and hard interventions.  A soft intervention can be seen as a value shift in the generalized propensity score. A hard intervention can be seen as shifting the generalized propensity score to a Dirac delta function to the desired treatment value. In the paper, they define an appropriate function class for the different interventions and deal with their specific covariate shifts. For the hard intervention setting, they also ensure that the function class can deal with an estimated generalized propensity score with a bounded estimation error of the propensity function. 

They provide some experiments on synthetic datasets (from their own) and medical ICU datasets, benchmarking their prediciton intervals against an MC dropout and Ensemble approach.

[1] I. Gibbs, J. J. Cherian, and E. J. Candès, “Conformal Prediction With Conditional Guarantees,” Dec. 20, 2023, arXiv: arXiv:2305.12616. doi: 10.48550/arXiv.2305.12616.

### Strengths
- **Clear Motivation:** The paper's objective is well-placed within causal machine learning, particularly in high-stakes areas like medicine, where uncertainty quantification is critical for decision-making.
- **Novel Contribution:** The authors propose a novel method for deriving conformal prediction intervals in the presence of continuous treatments and unknown propensity scores. This is a significant contribution, as most prior work focuses on binary or discrete treatments.

### Weaknesses
 - **Terminology Issues:** Terms such as "finite-sample predictive intervals" should be revised to "finite-sample validity guarantees" to align with established terminology in the field. Additionally, (line 090) “strong finite-sample mathematical guarantees” should be “finite-sample validity guarantees”. Similarly, the frequent use of the term "exact" in relation to conditional coverage is misleading, as exact conditional coverage is known to be unattainable. I also assume you do not provide exact coverage in the context of exact and conditional coverage.
- **Relation to Lei and Candes (2021):** In Figure 2, and the appendix, the paper claims that the work of Lei and Candes can not deal with an unknown propensity, this is not true it defines and proves a coverage gap based on the error in the estimation of the likelihood ratio’s (= propensity in the case of treatment effect) in weighted CP.
- **Relation to Gibbs et al. (2023): T**he paper mentions the paper of Gibbs et al. (2023) in that it reformulates the split CP as an augmented quantile regression and the use of Lemma 1. But throughout the work, several notions from this work are taken, such as the tilting of the propensity function (lines 210-215), Theorem 1 (lines 262-276) and Theorem 2 (lines 352-371) which is heavily inspired by this work as it can even be seen in the borrowed notation of Section 4 of Gibbs et al. (2023), Algorithm 1 similarly with Algorithm 1 of Gibbs et al. (2023).
- **Under-coverage in Empirical Results**: The experimental results show some under-coverage, particularly for specific significance levels (e.g., α = 0.1). This variability raises concerns about the method's robustness, and the number of runs (10) in some experiments is too low to draw reliable conclusions. More runs would improve the statistical robustness of the findings.
- **Computational Complexity**: While the paper introduces an algorithm, the appendix discusses the method's computational efficiency. It points out that complexity can be high due to the optimization solver. This should be included in the limitations. Additionally, you should include your experiments' fitting and inference times in the paper, as this could indicate if computational complexity is an issue in practice.
- **Too simple simulation experiments: T**he proposed synthetic experiments are way too simplistic, with only one discrete confounder, continuous treatment, and continuous outcome. This is not in line with other treatment effect literature; we cannot adequately evaluate the method with these experiments.
- **Baseline**: The choice of baseline methods, particularly MC dropout, may not be ideal for comparison. Since these approaches only quantify epistemic uncertainty, which is probably minimal due to the simple experiment settings, consider a benchmark approach that quantifies both aleatoric and epistemic uncertainty, or at least aleatoric such as the Gaussian process or maximum likelihood estimator. The MLE can be easily combined with MC dropout to get both aleatoric and epistemic to get a reasonable benchmark. Also, you did not evaluate vanilla CP without considering covariate shift as a benchmark.

### Questions
- What is your added contribution to the work of Gibbs et al. (2023), which you leverage in this work?
- Can you explain the variability in empirical coverage across different significance levels, particularly for α = 0.1? Do you plan to increase the number of runs or experiments to solidify your claims?
- Could you indicate how long it takes to run these experiments?
- I think there is a typo on line 476 that should be Table 1, right?
- In your synthetic experiments, why are the hard interventions related to x and not just hard interventions?
- Related to Assumption 1 (line 295-299), does this assumption mean that the estimation error needs to be the same for each X given an intervention $a$, otherwise should it not be $c_a(x)$ instead of $c_a$.
- Related to Theorem 2, what is the meaning of resulting $\sigma$ and $c_a$ of the optimization problem.
- Related to Lemma 4 (lines 712-736):
    - I think you need to clarify that this is only relevant for absolute residual non-conformity score.
    - Next, I think the proof is complete. You do not prove the connection between the Bonferonni corrected significance level and the targeted significance level.
    - In my opinion, the proof for this lemma is even elementary since it is just an application of the Bonferonni correction.

### Soundness
2

### Presentation
3

### Contribution
3

# Nuisance-Robust Weighting Network for End-to-End Causal Effect Estimation

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 5, 8

## Abstract
We combine the two major approaches to causal inference: the conventional statistical approach based on weighting and the end-to-end learning with adversarial networks.
Causal inference concerns the expected loss in a distribution different from the training distribution due to intervening on the input variables.
Recently, the representation balancing approach with neural networks has repeatedly demonstrated superior performance for complex problems, owing to its end-to-end modeling by adversarial formulation.
However, some recent work has shown that the limitation lies in the unrealistic theoretical assumption of the invertibility of the representation extractor.
This inherent difficulty stems from the fact that the representation-level discrepancy in representation balancing accounts only for the uncertainty of the later layers than the representation, i.e., the hypothesis layers and the loss.
Therefore, we shed light once again on the conventional weighting-based approach, retaining the spirit of end-to-end learning.
Most conventional statistical methods are based on inverse probability weighting using propensity scores, which involves nuisance estimation of propensity as an intermediate step.
They often suffer from inaccurate estimation of the propensity scores and instability due to large weights.
One might be tempted to jointly optimize the nuisance and the target, though it may lead to an optimistic evaluation, e.g., avoiding noisy instances by weighting less when noise levels are heterogeneous.
In this paper, we propose a simple method that amalgamates the strengths of both approaches: adversarial joint optimization of the nuisance and the target.
Our formulation follows the pessimistic evaluation principle in offline reinforcement learning, which brings provable robustness to the estimation uncertainty of the nuisance and the instability due to extreme weights.
Our method performed consistently well under challenging settings with heterogeneous noise. Our code is available online: https://anonymous.4open.science/r/NuNet-002A .

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a CATE estimation method using doubly robust estimators and machine learning.

Here the outcome and propensity models are learned with ML in a "targeted" way to minimize the MSE of the CATE estimator, rather than being fit separately and plugged in. They then derive and bound/regularize additional loss terms that account for the contribution of nuisance mis-estimation to estimator bias.

### Strengths
- It's important to bridge the gap between ML and traditional yet challenging estimation problems such as CATE from observational data
- Theory looks good/correct
- Go beyond deriving a standard DR estimator and characterization additional issues with nuisance mis-estimation and what to do about it
- Experiments are pretty complete.

### Weaknesses
There seems to be substantial discussion of related work missing.

In particular, there is a lot of existing work that also directly estimates the nuisance functions with ML, and even does so in a regularized way to directly target the estimand.

Some examples include:
- Adapting Neural Networks for the Estimation of Treatment Effects, https://arxiv.org/abs/1906.02120
- RieszNet and ForestRiesz: Automatic Debiased Machine Learning with Neural Nets and Random Forests https://arxiv.org/abs/2110.03031

(EDIT: I saw that the Shi work was added in the revision. See "Questions")

More generally, as mentioned in questions below, I think there are some clarity issues, such as incomplete sentences, that make the work hard to understand. Some of those unclear sentences appear exactly when there is an important differentiation about related work to be made.

I would be willing to raise my score if the other reviewers believe that the related work has been clarified in the revision, and if the other reviewers and AC believe that unclear sentences/discussion points such as those above could be clarified easily.

### Questions
1)

(EDIT after revision) I saw that the updated draft includes the passage: "Joint optimization approaches have also been proposed for ATE estimation (Shi et al., 2019), though it may lead to cheating by less weighting to noisy regions especially under noise heterogeneity"

I am not sure what "cheating" means and what "less weighting" means?

2) 

In the baseline section, in passing, the authors mention "DeR-CFR" (Wu et al., 2022) as another method that optimizes weights and outcome model simultaneously, but do not clarify why it is not compared against.

3)

"Although f0 and f1 are also nuisance parameters, the uncertainty of them do not differ among the target parameter space, thus we need not take care"

This sentence is very hard to understand; it is not complete and certain phrases are not defined "uncertainty does not differ" and "not taking care". Which uncertainty?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new method for estimating CATE. In contrast to previous two-stage estimators, the propensity score is simultaneously optimized with the second-stage regression. This is done in an adversarial manner to ensure robustness regarding estimation errors in the propensity score. The method is evaluated using simulated and real-world data.

### Strengths
- The paper is well written.
- CATE estimation is an important problem, with applications in various domains.
- The proposed method performs well empirically.

### Weaknesses
 - I am not convinced of the advantages of the proposed method. The robustness of CATE estimation with respect to estimated nuisance functions is central to recent well-established works on CATE estimation that make use of semiparametric estimation theory, e.g., by Chernozhukov et al. (2018), Foster and Syrgkanis (2019), Nie and Wager (2021), Kennedy (2023). One of the key results is that CATE estimators with Neyman orthogonal loss functions (e.g., DR-learner, R-learner) are robust with respect to estimation errors of nuisance parameters (response surfaces, propensity score) in the sense of a fast guaranteed convergence rate. It is not clear to me that the proposed adversarial end-to-end approach improves on that. The proposed method already uses the Neyman orthogonal loss of the DR learner which makes the adversarial approach of optimizing for a pessimistic propensity score seem redundant. The theoretical justification for why adversarial training of the propensity score specifically would lead to better CATE estimates is missing, especially given the known robustness properties of the DR-learner.
- Despite being central to the topic of the paper, three of the four works mentioned above are not cited in the paper. Neither is the R-learner considered as a baseline.
- Furthermore, I do not understand why the proposed approach only performs adversarial learning w.r.t. the propensity score in combination with the doubly robust loss. Why not also for the response surfaces? Only accounting for the estimation errors in one nuisance parameter while ignoring the others seems arbitrary. It is unclear why the propensity score is singled out as the only nuisance parameter that requires adversarial training. The justification for this selective adversarial approach is not provided, and it is not clear why the response surfaces are not treated similarly.
- A property of the DR loss is that only requires **either** the propensity score **or** the response surfaces to be estimated correctly to achieve a fast convergence rate (Kennedy, 2023). Again, this would make the proposed approach redundant if the response surface estimators converge sufficiently fast. The paper does not address this property of the DR-learner and how the proposed method improves upon it.
- While the method performs well in the experiments, the datasets seem to favor methods that focus on response function estimation rather than propensity score. PW-Net has a huge variance and the estimation error seems to grow with sample size for some reason. I suspect that there might be possible overlap violations in the simulated data. I could imagine that the proposed method offers some advantages in dealing with overlap violations, which might lead to an alternative way to frame the paper. However, this would require additional intuition and experiments. The experiments do not provide sufficient evidence that the proposed method is superior to existing methods, especially in settings where the propensity score is well-estimated.
- In summary, I think the problem of CATE estimation (or more generally, statistical estimation with nuisance parameters) is already quite well understood regarding the robustness to nuisance errors. I am not convinced that the proposed approach adds much benefit to the existing state-of-the-art.

Minor points

- The introduction puts a lot of emphasis on the CATE literature on representation learning. Personally, I do not think this literature stream is very relevant to the paper as it does not focus on representation learning, but CATE estimation as a statistical estimation problem with nuisance components. The same holds for the related work.
- The related work on CATE could be expanded.
- There are existing works on ATE estimation that estimate nuisance functions and ATE in an end-to-end manner (Shi et al. 2019, Frauen et al. 2023) which should be mentioned in the related work. However, these works perform end-to-end estimation to "target" the model parameters to fulfill estimation equations from semiparametric efficiency theory.
- In the literature, $\mu$ is usually used for the response functions and $\pi$ for the propensity score
- The consistency assumption is missing in Sec. 2

### Questions
-Was data-splitting/ cross-fitting performed for the proposed method and the DR learner?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The research introduces the Nuisance-Robust Transformed Outcome Regression Network (NuNet) within a standard causal inference framework, which aims to discern between factual and counterfactual potential outcomes using observational data. In empirical tests, many established methods showcased an inclination towards optimism particularly under conditions of noise heterogeneity. NuNet distinguishes itself by merging nuisance estimation and target estimation into a singular step, guided by the pessimism principle. The primary goal is to pinpoint a potential outcome function to determine the causal eﬀect of a treatment action. Accuracy is gauged through the PEHE, contingent upon three foundational assumptions: the Stable Unit Treatment Value, unconfoundedness, and overlap.

Empirical tests claim that NuNet oLen surpasses or parallels baseline plug-in methods, particularly in diverse noise seMngs and real-world datasets. However, it faces challenges with techniques prioritizing joint optimization. Inspired by pessimism in oﬄine reinforcement learning, this causal inference method oﬀers a diﬀerent approach. Most conventional techniques adopt a plug-in estimation, but this may show sub-optimality if nuisance accuracy isn't accounted for. The signiﬁcance of addressing the gap between optimistic and pessimistic errors is emphasized, leading to adherence to the pessimism principle. The study also delves into various methods used for estimating the CATE. Notable methods include Transformed Outcome Regression, PWNet, Doubly Robust Learner (DRNet), and NuNet. These strategies aim to enhance robustness against nuisances and unobserved confounders, ultimately aiming for reliable and accurate estimations. For future exploration, the authors suggested constructing a pessimism-based theoretical structure and delving into principled learning avenues could propel the evolution of causal inference methodologies.

### Strengths
1. Clear mention of shortcomings of the conventional statistical and end-to-end adversarial learning networks.
2. Evaluation of robustness of the approach under conditions including heterogeneous noise, AN setting, MN setting and real-world datasets.

### Weaknesses
Considerable diﬀerence between the results of NuNet and SNet (best performing) pertaining to PEHE on the additive noise dataset.

### Questions
See Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

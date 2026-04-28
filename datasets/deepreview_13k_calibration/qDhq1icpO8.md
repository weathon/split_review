# Conditional Instrumental Variable Regression with Representation Learning for Causal Inference

- Decision: Accept
- Avg Score: 6.75
- Scores: 5, 8, 6, 8

## Abstract
This paper studies the challenging problem of estimating causal effects from observational data, in the presence of unobserved confounders. The two-stage least square (TSLS) method and its variants with a standard instrumental variable (IV) are commonly used to eliminate confounding bias, including the bias caused by unobserved confounders, but they rely on the linearity assumption. Besides, the strict condition of unconfounded instruments posed on a standard IV is too strong to be practical. To address these challenging and practical problems of the standard IV method (linearity assumption and the strict condition), in this paper, we use a conditional IV (CIV) to relax the unconfounded instrument condition of standard IV and propose a non-linear \underline{CIV} regression with \underline{C}onfounding \underline{B}alancing \underline{R}epresentation \underline{L}earning,  CBRL.CIV, for jointly eliminating the confounding bias from unobserved confounders and balancing the observed confounders, without the linearity assumption. We theoretically demonstrate the soundness of CBRL.CIV. Extensive experiments on synthetic and two real-world datasets show the competitive performance of CBRL.CIV against state-of-the-art IV-based estimators and superiority in dealing with the non-linear situation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a method aimed at addressing the challenge of conditional instrumental variables, which refer to variables that may not be valid unconditional instruments, but satisfy the instrumental variable assumptions when conditioned on an appropriate adjustment set. The paper argues that the primary issue associated with conditional instrumental variables lies in the distributional imbalance observed among the groups defined by the values within the conditioning set. To address this, the paper proposes a methodology that uses regularization similar to the approach employed by Shalit et al. [2017] to minimize these distributional shifts.

### Strengths
The paper studies balancing in the conditional instrumental variable setting, and they use an approach reminiscent of Shalit et al [2017] to penalize changes in the conditional distribution of the treatment and instrument are stable across conditions. 

I think that it is under appreciated that conditional IVs are possible (although they are implicit in most standard IV assumptions), so I'm glad this topic is getting attention. 

I reviewed an earlier version of this paper and most of my critiques from then have now been fixed (with the exception of the experiments below).

### Weaknesses
The experiments remain the weakest part of this paper. The result of the proposed method are very impressive relative to the baselines, but it is not at all clear how fair the comparison was. The synthetic data is a novel benchmark, so I would expect that the baselines would all underperform without some hyper parameter tuning, but there is no mention of this (the authors do tune the hyper parameters of the proposed method).

More importantly, both IHDP and Twins are datasets that are used in the unconfounded setting, so it's not clear that they even have an instrument (particularly not a conditional instrument) or unobserved confounding. 

Code is supplied but only for the proposed method (not the baselines), and the data generating process is only supplied

### Questions
How were the baselines tuned?

Why are they so much higher variance than the proposed method?

If you consider a setting with a standard IV, do the baselines then outperform your method?

How did you select instruments for IHDP and Twins?

What is a plausible source of unobserved confounding for IHDP and Twins?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a novel approach designed to tackle the complexities associated with conditional instrumental variables (CIVs). These are specific variables that, while not qualifying as unconditional instruments, fulfill the IV assumptions when conditioned on a suitable adjustment set.  The paper identifies that the predominant challenge with these CIVs emerges from distributional imbalances among groups delineated by the values in the conditioning set. To mitigate this, the paper proposes a framework that leverages regularization techniques to minimize these distributional discrepancies.

### Strengths
1.	The paper is good by its deep exploration of the challenges associated with estimating causal effects in the presence of non-linear relationships and unobserved confounders. It specifically addresses the imbalance issues inherent in applications of CIVs in non-linear settings with finite samples. This is a significant contribution, as CIVs are more practical and less restrictive than traditional IVs in real-world scenarios.
2.	The paper proposes a novel Confounding Balancing Representation Learning (CBRL.CIV) method for non-linear CIV regression in causal effect estimation. Notably, CBRL.CIV efficiently mitigates the confounding biases between $S$ and $W$, as well as between $W$ and $Y$.  
3.	The paper delves into the theoretical underpinnings of CBRL.CIV, highlighting its robust capability to generalize across varied groups. This ensures a harmonious balance across the CIV, treatment, and outcome regression networks.
4.	Through experiments on both synthetic and real-world datasets, the effectiveness of CBRL.CIV has been validated in estimating average causal effects. Such empirical evidence is crucial for the adoption and trustworthiness of the proposed method in real-world applications.

### Weaknesses
Causal inference fundamentally depends on certain assumptions and the proposed CBRL.CIV method is no exception. If these prerequisites aren't satisfied in specific scenarios, the efficacy of the CBRL.CIV method might be compromised. Thus, a discussion on the potential negative impacts of using CBRL.CIV under such conditions would be beneficial.

**Presentation**:
1.	Figure 2 in the main content and Figure 3 in the appendix should use the same legend.
2.	 When the authors or the publication are included in the sentence, the citation should not be in parenthesis, e.g., “it is well-known that the causal effect of the treatment on the outcome is non-identifiable Pearl (2009); Shpitser & Pearl (2006).” The citation should be in parenthesis using \citep{}.
3.	In Eq. (12), there is a missing square, and the same missing happens in the pseudocode of Algorithm 1.

### Questions
Sww weakness

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper tackles the complex task of estimating causal effects in observational data while considering unobserved confounders. It introduces a novel approach called CBRL.CIV, which leverages a conditional instrumental variable (CIV) to relax the stringent requirements of standard instrumental variables (IV), such as linearity assumptions and strict unconfounded instrument conditions. Through theoretical analysis and extensive experiments on synthetic and real-world datasets, the paper demonstrates the effectiveness of CBRL.CIV in eliminating confounding bias, particularly in non-linear scenarios, making it a promising alternative to existing IV-based estimators.

### Strengths
1. Using CIV to relax the restrictive conditions of IV methods is practical for most realistic scenes. 
2. The overall presentation and writing structure is clear and well motivated.
3. Extensive experimental results are convicing.

### Weaknesses
1. Using CIV to relax the restrictive conditions of IV methods is practical for most realistic scenes. 
2. The overall presentation and writing structure is clear and well motivated.
3. Extensive experimental results are convicing.

1. Using confounder balancing to migrate the gap between treated and controlled groups are very commo. I wonder the specific beneficial point on the combination of CIV and confounder balancing.

### Questions
See Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the challenge of estimating causal effects from observational data while dealing with unobserved confounders. The paper introduces a conditional IV (CIV) approach called CBRL.CIV, which relaxes the strict conditions and allows for non-linearity. Theoretical analysis supports the soundness of CBRL.CIV, and extensive experiments demonstrate its competitive performance in handling non-linear scenarios compared to state-of-the-art IV-based estimators.

### Strengths
1. CIV offers a more powerful and flexible approach to handle causal inference with unmeasured confounders.
2. The experimental results are extensive and convincing.

### Weaknesses
My main concern is the similarity of this work to Wu.2022 in ICML. Even though the contribution of this work is introducing CIV to handle the restrictive conditions of IV, you methods are similar to Wu et.al. Hence, can you state the difference, or the unique technical contribution of CIV for representation learning?

### Questions
See Weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

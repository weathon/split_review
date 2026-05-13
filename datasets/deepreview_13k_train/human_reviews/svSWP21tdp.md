# Fairness Feedback Loops: Training on Synthetic Data Amplifies Bias

- Decision: Reject
- Scores: 3, 3, 3, 3

## Abstract
Model-induced distribution shifts (MIDS) occur as previous model outputs pollute new model training sets over generations of models. 
This is known as \textit{model collapse} in the case of generative models, and \textit{performative prediction} or \textit{unfairness feedback loops} for supervised models. When a model induces a distribution shift, it also encodes its mistakes, biases, and unfairnesses into the ground truth of its data ecosystem. We introduce a framework that allows us to track multiple MIDS over many generations, finding that they can lead to loss in performance, fairness, and minoritized group representation, even in initially unbiased datasets. Despite these negative consequences, we identify how models might be used for positive, intentional, interventions in their data ecosystems, providing redress for historical discrimination through a framework called algorithmic reparation (AR). We simulate AR interventions by curating representative training batches for stochastic gradient descent to demonstrate how AR can improve upon the unfairnesses of models and data ecosystems subject to other MIDS. Our work takes an important step towards identifying, mitigating, and taking accountability for the unfair feedback loops enabled by the idea that ML systems are inherently neutral and objective.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper provides a conceptual taxonomy of various ways in which repeated training of a model (either a classifier or a generator) in the same data ecosystem lead to negative effects on fairness such as degradation in fairness metrics and distorted class proportions. The overall phenomenon is terms MIDS - Model Induced Distribution Shift, and encompasses previously studied phenomena/concepts such as model collapse, performative prediction and fairness feedback loops. Using experiments on a sequence of recursively trained classifiers (and likewise generators), the paper exposes the several possible harmful effects of MIDS. The paper then introduces a simple resampling scheme for Algorithmic Reparation (AR) into the MIDS framework, and shows through experiments that the proposed AR can ameliorate some of the harmful effects of MIDS.

### Strengths
- The paper addresses the important issue of studying the fairness effects of repeated training in a data ecosystem. 
- The paper presents a clear model of sequentially training classifiers and generators that can be used to simultaneously model various effects like feedback loops, performative effects and model collapse.

### Weaknesses
 - The paper does not propose a mathematical model for the proposed MIDS scheme. Although various effects of retraining are shown through experiments, there is no theoretical investigation on the root causes of these effects, or the efficacy of the presented Algorithmic Reparation (AR) scheme. Specifically, the paper lacks a formal definition of MIDS, making it difficult to analyze its properties or compare it to existing frameworks. The absence of a mathematical model also limits the generalizability of the findings, as it's unclear how the observed effects would manifest under different conditions or with different model architectures. Furthermore, the paper does not explore the convergence properties of the proposed AR scheme, leaving open questions about its long-term behavior and stability.
- The experimental results with the proposed AR scheme based on resampling are not very convincing. For example, the decrease in the equalized odds difference with reparation in Figure 4 is not monotonic. The gap closes for a few generations and then seems to rise up again. This non-monotonic behavior suggests that the AR scheme may not be consistently effective and could be sensitive to specific training dynamics. The plots on fairness metrics in Figure 5 are even less convincing, showing only marginal improvements and in some cases, even a degradation of fairness metrics with the proposed AR. The lack of clear and consistent improvements raises concerns about the practical utility of the proposed AR method.

### Questions
- What is the reason for the decrease in the equalized odds difference with reparation in Figure 4 not being monotonic?
- The paper claims that "Generator-side AR improves fairness and minoritized representation", but plots on fairness metrics in Figure 5 do not corroborate this claim. Please explain.
- I do not understand the claim, "Performative prediction on model collapse leads to higher utility". Please explain what you mean by this.

### Soundness
2 fair

### Presentation
3 good

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
The paper is about the feedback loop when models are continuously trained on data generated by them. The authors introduce model-induced distribution shifts (MIDS) which occur as previous model outputs pollute new model training sets over generations of models. They provide a taxonomy for MIDS and demonstrate that their fairness effects lead to a lack of representation and per-
formance on minoritized groups within a few model iterations. The authors propose Algorithmic Reparation (AR) as another explicit MIDS
deployed with the goal of reducing societal inequity and correcting for historical oppression; they use AR to reduce the unfairness impacts of other MIDS by sampling for minoritized group representation, leading to better downstream fairness over time.

### Strengths
* The feedback loop problem is important and interesting.
* The authors propose a setup in which this problem can be studied and explore Algorithmic Reparation as a possible solution.

### Weaknesses
Personally, I find the paper a bit hard to understand.

* Introduction seems a bit verbose and overly lyrical in moments, making it harder to read and follow
"recent demographic information of the Black population" - it is written that the maps are from 1939 and 1955. I am not sure that this is very recent.

* I am not sure that MIDS require their own "taxonomy", given that there are only label and input drifts (Table 1). Impact of feedback loop in fairness has been acknolwedged as a problem for a while (Mehrabi et al. 2019)

* The related work is not clearly discussed in the paper, making it a bit hard to get the overall context and contributions with respect to prior work.

* A recent related work by Taori and Hashimoto (2023) is missing. How does this paper relate to them?

Mehrabi et al., A Survey on Bias and Fairness in Machine Learning, arXiv 2019
Taori and Hashimoto , Data Feedback Loops: Model-driven Amplification of Dataset Biases, 2023

### Questions
Q1: How do you select the datasets and what are the motivations for them and the experimental setup exactly?

Q2: What are the models that you employ for the classifiers and the generator?

Q3: Why does the accuracy drops over time in Fig. 5 and 6?

### Soundness
1 poor

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a framework called model-induced distribution shifts (MIDS) that unify several existing notions such as model collapse, unfairness feedback loops, class imbalance, label/ input drift, etc.

### Strengths
1.	The formulation and procedure to observe and evaluate MIDS is clear. The flowcharts in Section 3.1 and Section 3.2 are really helpful
2.	The discussions on model collapse for generative models and the performative prediction in Section 4.2 are inspiring

### Weaknesses
1. This paper attempts to encompass several issues such as model collapse, performative prediction, unfairness feedback loops, and algorithmic reparation. However, the benefit and motivation for the unifying MIDS is not clear to me. It is encouraged that the authors clearly state what addition challenge could be solved, or what existing challenges could be better solved by the MIDS framework.
2. There are existing algorithms that could solve unfairness feedback loops, class imbalance, etc. However, the MIDS framework is not compared with those existing benchmarks.
3. Algorithmic reparation (AR) should be the most important concept/baseline in this paper; however, it is not technically introduced in the paper. It is encouraged that the authors add more discussion, use case, and operational meaning of AR.
4. The methodologies proposed in Section 3 for MIDS lack theoretical analysis, performance guarantee, etc.

### Questions
1.	In Figure 4, as the number of generations increase, the accuracy drops from 92% to 82%, and the fairness metrics like DP and EO are still large. Why a reduction of accuracy and unfairness will occur at the same time?
2.	Why we need the settings of sequences of generators?

For other questions, please refer to the Weaknesses. I will consider raising the scores if the authors could adequately address my questions in the rebuttal.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a novel term, "model-induced distribution shift," aiming to encompass various distribution shifts within a single framework. It delves into two scenarios to highlight their effects. Furthermore, the study reveals that model-induced distribution shifts can rapidly result in suboptimal performance, skewed class distribution, and underrepresentation of marginalized demographic groups. To address this challenge, this paper showcases the potential of algorithmic reparation to reduce disparities among sensitive groups.

### Strengths
* This paper systematically categorizes the existing literature on model-induced distribution shift, offering a consolidated overview for the machine learning fairness community.
* The experimental setups involving sequences of classifiers and generators are interesting, as they aptly simulate the real-world data distribution shifts induced by deployed models.
* Numerical experiments show the effectiveness of applying algorithmic reparation for mitigating the model-induced data distribution issues.

### Weaknesses
I have two main concerns about this work
* In this study, the authors employ a synthetic process using a series of classifiers and generation models to emulate real-world data distribution shifts. How do the authors substantiate that this accurately reflects actual distribution shift behaviors in the real world?
* Could the authors delve into a discussion regarding how current methodologies address the challenges of model-induced distribution shifts?
* Furthermore, the numerical experiments focus solely on a comparison between scenarios with and without algorithmic repair. Could the authors also present comparisons against established baseline methods?

Overall, I'm uncertain about the adequacy of the contribution presented in this work for acceptance. I would recommend that the authors elaborate more on the distinct contributions of their paper in relation to existing methodologies addressing this issue.

### Questions
My questions are provided in the Weakness section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

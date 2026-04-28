# Exploring the Link Between Out-of-Distribution Detection and Conformal Prediction with Illustrations of Its Benefits

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 3, 6, 6

## Abstract
Research on Out-Of-Distribution (OOD) detection focuses mainly on building scores that efficiently distinguish OOD data from In Distribution (ID) data. 
    On the other hand, Conformal Prediction (CP) uses non-conformity scores to construct prediction sets with probabilistic coverage guarantees. In other words, the former designs scores, while the latter designs probabilistic guarantees based on scores. Therefore, we claim that these two fields might be naturally intertwined. 
    This work advocates for cross-fertilization between OOD and CP by formalizing their link and emphasizing two benefits of using them jointly.
    First, we show that in standard OOD benchmark settings, evaluation metrics can be overly optimistic due to the test dataset's finite sample size.
    Based on the work of (Bates et al, 2022), we define new *conformal AUROC* and *conformal FRP@TPR$\beta$* metrics, 
    which are corrections that provide probabilistic conservativeness guarantees on the variability of these metrics.
    We show the effect of these corrections on two reference OOD and anomaly detection benchmarks, OpenOOD (Yang et al, 2022) and ADBench (Han et al. 2022). 
    Second, we explore using OOD scores as non-conformity scores and show that they can improve the efficiency of the prediction sets obtained with CP.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper examines the relationship between conformal prediction (CP) and out-of-distribution (OOD) detection. It approaches the OOD detection problem from a conformal prediction perspective and, inspired by CP, proposes several modified metrics for OOD evaluation, testing them on various OOD benchmarks. Additionally, the paper constructs prediction sets for classification tasks, drawing on techniques from OOD detection.

### Strengths
* The paper is well-structured, well-written, and easy to read.

* The paper introduces modified metrics for OOD evaluation that are more robust when considered from a hypothesis testing perspective.

* The OOD detection problem is significant for ML research, making this topic relevant to the ICLR community.

* The exploration of the link between OOD and CP is informative.

### Weaknesses
 * The main insight of the paper is that FPR@β can be interpreted as a p-value within a specific statistical hypothesis testing framework. By building on the work of [1], the paper proposes a corrected estimator for this metric to improve robustness. While this approach is interesting, I believe it is insufficient to warrant publication. Firstly, much of the technical foundation relies on [1], and the corrected metric for OOD detection performs similarly to the classical version. Therefore, I do not find the current version sufficiently novel for publication.

* Computing the proposed metric for OOD detection requires access to extra validation sets.

### Questions
1. Is there a scenario where classical metrics like FPR@β or AUROC might fail for OOD evaluation, but your conformal metrics accurately capture the evaluation? How do the experimental results in Section 4 contribute to safer OOD evaluation?

2. When using OOD scores as nonconformity scores in CP, can you still obtain theoretical guarantees for the prediction sets?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates the relationship between Out-of-Distribution (OOD) detection and Conformal Prediction (CP). They apply conformal prediction methods from prior work by Bates et al. (2022) to the task of Out-of-Distribution (OOD) detection, which is to distinguish in-distribution (ID) data from OOD data. They introduce metrics conformal AUROC and conformal FPR@TPR95 which provide conservative probabilistic guarantees in OOD detection tasks, particularly relevant for safety-critical applications. The authors then empirically validate the performance of these metrics on common OOD benchmarks.

### Strengths
The paper presents an application by adapting the conformal prediction methods from Bates et al. (2022) to OOD detection.

### Weaknesses
(1) The methodology largely follows the framework established by Bates et al. (2022) in the conformal prediction literature, with limited novel contributions specific to OOD detection. The primary innovation appears to be an application of existing CP methods to OOD tasks rather than a new approach. The adaptation of conformal prediction to OOD detection, while potentially useful, does not introduce significant algorithmic or theoretical advancements beyond the existing CP framework. The core idea of using nonconformity scores derived from OOD detection for conformal prediction is a straightforward application of existing techniques, lacking substantial innovation in either the OOD or CP domains.

(2) While the idea of combining OOD detection with CP is interesting, the approach itself and the resulting metrics are relatively straightforward extensions and may not represent a significant advancement in either OOD or CP methodologies. The proposed metrics, conformal AUROC and conformal FPR@TPR95, are essentially applying conformalization to existing OOD evaluation metrics. This does not introduce a fundamentally new way of evaluating OOD detection, but rather provides a probabilistic interpretation of existing metrics. The practical impact of these metrics is not clearly demonstrated to be significantly different from standard metrics in terms of insights gained or decisions made.

minors:
(1) Line 135: In Equation (2), n_val is not defined and weird, should be probability. Similarly, n_val is used as probability in Line 296, Equation (10). Other places, it is used as the number of data points.

(2) A lot of places, for example, section 4.3.1, tau and t are used in mix to refer to the same thing.

### Questions
Given the significant overlap with Bates et al. (2022) 's methods, what specific contributions does this paper make beyond adapting CP to OOD tasks?

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper explores the connection between Out-of-Distribution (OOD) detection scores and the non-conformity scores in Conformal Prediction (CP), showing the potential for cross-fertilization between these methods. Non-conformity scores offer probabilistic interpretation and correction for OOD scores, while OOD scores can enhance the efficiency of prediction sets obtained through CP.

### Strengths
•	OOD scores can be unreliable, and employing new statistical developments to improve their reliability is a promising direction. Using the uncertainty estimates from CP appears to be a robust approach to address OOD score unreliability.

•	The paper targets a practical problem, effectively demonstrating key concepts through comprehensive case studies.

•	By linking OOD detection with CP, this work facilitates cross-fertilization that benefits both machine learning and statistics. The authors provide a good introduction to using CP for interpreting and correcting OOD scores.

### Weaknesses
•	Non-conformity scores in CP require an evaluation dataset, and it reliability depends on the choice of this dataset. This introduces a practical challenge in implementing this statistically sound solution.

•	The paper presents limited innovation, as much of the work is based on existing research.

### Questions
I think that there are two types of uncertainties for a model predicting a new test instance:

1.	Prediction Confidence: Assuming the instance is within the In-distribution, this type of uncertainty relates to the strength of evidence supporting the prediction.

2.	In-Distribution Uncertainty: As discussed in this paper, this refers to uncertainty regarding whether the instance truly belongs in the In-distribution.

I would appreciate further discussion from the authors on the distinctions and connections between these two types of uncertainties. Can they be quantified into a single metric?

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
3

### Summary
The authors ask themselves, and answer positively, to the question whether CP can be beneficial to OOD, and whether the vice versa holds as well. They also validate empirically their findings.

### Strengths
The paper makes an extremely interesting parallel between OOD and CP. In addition, I found very interesting the marginal guarantees that the authors were able to find.

### Weaknesses
CP is a method for *uncertainty representation*, not uncertainty *quantification*. Indeed, CP *represents* uncertainty via the conformal prediction region. It does not quantify it: there is no real value attached to any kind of predictive uncertainty (e.g. aleatoric or epistemic, AU and EU, respectively). Some claim that the diameter of the conformal prediction region quantifies the uncertainty, but even in that case, it is unable to distinguish between AU and EU. Indeed, the diameter is a positive function of both: it increases as both increase, and hence it cannot be used to distinguish between the two [1]. Please add this clarification in the camera-ready version of the manuscript.

The simplest CP technique is (arguably) transductive CP, not split CP.

Shouldn't $n_\text{val}$ in (2) and in (10) be substituted by $P$? In particular, CP guarantees hold for all exchangeable countably additive probabilities $P$ on the space $\mathcal{Y}$ of outputs.

How does the proposed method relate to the subsequent work by Kaur [2]?

### Questions
See Weaknesses. In addition, Typo at line 69: eas (2023). Shouldn't it be Easa?

### Soundness
3

### Presentation
3

### Contribution
3

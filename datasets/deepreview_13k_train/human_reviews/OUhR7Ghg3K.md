# The Disparate Benefits of Deep Ensembles

- Decision: Reject
- Scores: 5, 6, 8

## Abstract
Ensembles of Deep Neural Networks, Deep Ensembles, are widely used as a simple way to boost predictive performance. 
    However, their impact on algorithmic fairness is not well understood yet.
    Algorithmic fairness investigates how a model's performance varies across different groups, typically defined by protected attributes such as age, gender, or race.
    In this work, we investigate the interplay between the performance gains from Deep Ensembles and fairness.
    Our analysis reveals that they unevenly favor different groups in what we refer to as a \emph{disparate benefits} effect. 
    We empirically investigate this effect with Deep Ensembles applied to popular facial analysis and medical imaging datasets, where protected group attributes are given and find that it occurs for multiple established group fairness metrics, including statistical parity and equal opportunity.
    Furthermore, we identify the per-group difference in predictive diversity of ensemble members as the potential cause of the disparate benefits effect.
    Finally, we evaluate different approaches to reduce unfairness due to the disparate benefits effect. 
    Our findings show that post-processing is an effective method to mitigate this unfairness while preserving the improved performance of Deep Ensembles.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper empirically investigates fairness violations in Deep Ensemble models. It finds that, in most cases, Deep Ensemble models exhibit poorer fairness performance compared to single models, despite achieving significantly better overall performance, which echoes existing research. The paper aims to understand the reasons behind the amplification of unfairness and demonstrates that post-processing can mitigate unfairness issues in Deep Ensemble models.

### Strengths
This work offers a perspective on fairness issues in Deep Ensembles. 

The presentation style is clear and easy to follow.

 Additionally, I find the experiments conducted to be convincing.

### Weaknesses
(1) A key limitation of this work lies in the interpretation of results presented in Section 6. The author hypothesizes that disparities in the average predictive diversity among groups contribute to the observed disparate benefits effect. However, the benefit remains ambiguous. For instance, in Figure 2, while the subgroup with A=1 demonstrates a higher TPR *change* due to ensembling, the subgroup with A=0 shows a lower False Positive Rate (FPR) *change*, making the overall ensemble effect difficult to assess in terms of fairness. The analysis focuses on changes in metrics rather than absolute values, which obscures the actual impact on fairness. It's unclear if the observed changes are practically meaningful or if they simply reflect noise in the data. The core issue is that the 'benefit' is not a singular, easily interpretable quantity, but a complex interplay of changes in TPR and FPR, which may not always align in a way that favors one group over another in a clear and consistent manner.

(2) In Figure 13(a), the disadvantaged group shows a higher TPR and nearly the same FPR as the advantaged group, which is inconsistent with the analysis in Section 6. This discrepancy undermines the claim that the disparate benefits effect consistently favors the already advantaged group. The figure suggests that in some cases, the disadvantaged group may experience a more significant improvement in TPR without a corresponding increase in FPR, which contradicts the general trend described in the paper. This inconsistency needs to be addressed with a more nuanced analysis of the conditions under which different groups benefit from ensembling.

(3) The fairness concern addressed is the disparity across sensitive groups. However, the author's approach to explaining unfairness through performance differences does not fully explore the underlying reasons for fairness issues in deep ensembles. The paper primarily focuses on the *what* (performance differences) rather than the *why* (the mechanisms within the ensemble that lead to these differences). A more thorough investigation would require examining the individual model predictions and how they interact within the ensemble to produce disparate outcomes. This would involve analyzing the diversity of predictions, the correlation of errors, and the influence of individual models on the final ensemble prediction for different groups.

(4) The proposed solution is also relatively unremarkable. The use of model-agnostic post-processing methods, which are not specifically tailored for deep ensembles, is unsurprising. The key question is how the deep ensemble model differs in effectively addressing fairness concerns compared to other high-performing models. The paper does not provide a comparative analysis of how these post-processing methods perform on deep ensembles versus other models. The lack of such comparison makes it difficult to assess the specific advantages or disadvantages of applying these methods to deep ensembles.

### Questions
(1) One reason for unfairness arises from skewed data distribution. Figure 3(c) shows a much more skewed distribution compared to Figure 3(a). However, I found that the fairness issues in CX (age) are much milder than those in FF (age/gender), and I am curious why this is the case. 

(2) The trade-off between utility and fairness shows similar behavior in relation to fairness issues across classification tasks. This raises the question: what distinguishes the behavior of a deep ensemble model with strong utility performance in terms of fairness?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper explore the impact of Deep Ensembles on group fairness through empirical studies across three datasets—FairFace, UTKFace, and CheXpert—using statistical parity difference (SPD), equal opportunity difference (EOD), and average odds difference (AOD). Their results show that while ensembles improve performance globally, they generally tend to favor advantaged demographic groups according to fairness measures, which they call "the disparate benefits effect". They link this effect to how ensemble members' predictions vary across demographic groups. Finally, the study shows that because Deep Ensembles are better calibrated than individual models, post-processing techniques, such as the algorithm by Hardt et al. (2016), are effective in mitigating these fairness disparities while preserving the performance benefits of Deep Ensembles.

### Strengths
The study addresses an important aspect of Deep Ensembles by examining the fairness implications of their performance improvements.  This kind of evaluation is crucial to ensure that gains in predictive accuracy are achieved without unintended consequences for different demographic groups.

### Weaknesses
 - The reported differences in fairness metrics between models are often very small, making it difficult to assess the significance of the disparate benefits effect. Including the original results for individual models in Table 1 would help clarify these differences.
- The baseline selection process is unclear - while I assume the baseline represents the aggregated average across all individual models, the paper doesn't explicitly specify it (is it average results on all individual models / architectures and different seeds?). It should be clarified for proper comparison.
- The paper lacks intuitive explanations for the relationship between prediction diversity and fairness. While the average predictive diversity (DIV) shows strong differences between demographic groups, it's unclear why this specifically impacts fairness criteria. 
- The study relies solely on Hardt's post-processing method for mitigation. Comparing with other approaches, like in-processing techniques, would strengthen the claims.

### Questions
1) See Point 3 above - Could you provide an intuition on how diversity among ensemble members contributes to fairness violation? Why does high predictive diversity (DIV) across demographic groups could lead to increased disparate impact or affect equalized odds? I do not see the causation;  
2) Are the calibration benefits of Deep Ensembles evenly distributed across the two different demographic groups? 
3) a) The controlled experiment lacks testing of different levels of ensemble diversity. How would increasing the number of diverse training images for A=1 (two/three/four/five different images) affect the fairness metrics (DP and EO)? Does it decreases gradually? Such experimental variations might provide additional insights into the observed relationship.

b) What are the corresponding average metrics of individual members (at least on 10 members) in this controlled experiment? Do individual members also show better fairness metrics compared to the deep ensemble?

4)The baseline selection process requires more clarification. Is it the average metrics over the 10 individual models on the 5 architectures and the different seeds?  On page 6, at the end of the caption, it states “...and the average ensemble member.” Should this instead read “...and the average of individual members”?

5) Why was the Deep Ensemble not tested with fairness constraints through in-processing methods? Testing fairness constraints during training of the members could help strengthen the claims about the suited post-processing mitigation approaches.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper examines how deep neural network ensembles affect group fairness, demonstrating that these ensembles provide disproportionate benefits to protected groups (a phenomenon termed the "disparate benefits effect"). The authors establish that this effect is linked to the predictive diversity among ensemble members, noting that deep ensembles show greater sensitivity to prediction thresholds compared to individual models due to their sensitivity to calibration. Additionally, they investigate post-processing techniques to mitigate the unfairness introduced by the disparate benefits effect while maintaining ensemble performance. Their findings indicate that Hardt post-processing is particularly effective, as it successfully preserves the ensemble's performance while reducing unfairness.

### Strengths
The main strengths are:
1. The focus on how deep ensemble models affect fairness violations in group fairness scenarios, a relatively understudied area in current research.
2. The authors provide reasonable arguments on the why (group) unfairness emerges in deep ensembles. Their claims are thoroughly tested by conducting comprehensive analyses through controlled experiments and large-scale benchmark evaluations, examining multiple group fairness metrics under various distribution shifts.
3. The argument of using post-hoc methods to edit calibration of the predictive distribution, rather than focusing on non-homogeneous members weighting is both practical and convicing.

### Weaknesses
The paper presents valuable insights into the relationship between deep ensembles and group fairness. The authors' thorough analysis could be further enriched by expanding their investigation to include other fairness definitions discussed in the literature [1,2]. For instance, while the authors focus on group fairness, their findings could be contextualized alongside the results from [3], which examines min-max fairness [2] and shows that deep ensembles improve worst-group accuracy (their findings align with the "FalseFalseTrue" phenomenon described in [4]).
To strengthen the paper's contribution to the broader fairness literature (which would help create a more comprehensive understanding of deep ensembles' impact on algorithmic fairness), I suggest either:
1. Clarifying the strategic choice to focus on group fairness and its specific implications, or
2. Preferably, extending the analysis to examine how the authors' hypotheses validity holds across different fairness definitions, particularly in relation to the findings in [3].

### Questions
Continuing from the Weaknesses section of the review, given that the min-max fairness setting [1] addresses inefficiencies of statistical parity/equality measures, when evaluating fairness, given your findings on predictive diversity, it would be interesting also to understand:
1. How does your analysis of predictive diversity relate to the worst-group accuracy (WGA) findings in [2]?
2. In the context of min-max fairness, how would you assess the applicability of the Hardt post-processing method from a calibration standpoint? Are there any benefits in using it?


[1] Zietlow, Dominik, et al. "Leveling down in computer vision: Pareto inefficiencies in fair deep classifiers." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2022.

[2] Ko, Wei-Yin, et al. "Fair-ensemble: When fairness naturally emerges from deep ensembling." arXiv preprint arXiv:2303.00586 (2023).

### Soundness
3

### Presentation
3

### Contribution
3

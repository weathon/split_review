# Why Sanity Check for Saliency Metrics Fails?

- Decision: Reject
- Scores: 3, 8, 3, 1

## Abstract
Saliency maps are widely leveraged as a post-ad-hoc approach to explain the decision-making process of Deep Learning-based image classification models. However, despite their popularity, ensuring the fidelity of saliency maps remains a complex problem. Researchers have, therefore, introduced saliency metrics to evaluate the fidelity of saliency maps. However, previous studies observed several statistical inconsistencies in the existing saliency metrics without investigating the reason behind the inconsistencies. In this study, we investigate the reason behind the observed statistical inconsistencies. We analyze the inconsistencies by studying the variation in pixel importance ranks, specifically by choosing a case study of varying levels of Gaussian blur (with different σ values for the width of the Gaussian Kernel) as the perturbation mechanism. Our findings indicate that the effect of perturbations on prediction probability and pixel importance ranks varies widely across different levels of Gaussian Blur. Consequently, the existing saliency metrics that rely on pixel importance become unreliable for measuring the fidelity of saliency maps. This insight necessitates careful use of saliency metrics and the perturbation technique used while assessing the fidelity of saliency maps in eXplainable AI (XAI). We used Gaussian Blur as our perturbation mechanism, but our approach applies to any perturbation.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
This paper discusses the problem of disturbance in saliency metric, and holds that pixel importance become unreliable for measuring the fidelity of saliency maps. The authors proposed two metrics to quantify the inconsistencies using prediction probability change and variation of pixel ranks and make two related experimental analysis.

### Strengths
1. The problems discussed are of research significance and worthy of attention.
2. Two metric are proposed to analyze the influence of pixel sorting disturbance.

### Weaknesses
1. Motivation is not sufficient. It is far-fetched to introduce the necessity of metric research of saliency map from XAI. Especially in Figure 1 and Table 1, the conclusions drawn have limited relevance to the background of the topic introduced in this paper. The connection between the observed variations in saliency maps across different methods (Figure 1) and the need for new metrics to assess the reliability of these maps is not clearly established. The argument that these inconsistencies stem from the model itself (Table 1) is presented without sufficient justification, and its relevance to the core issue of pixel importance is unclear.
2. The argument is not rigorous enough. The article mentioned many times that we should investigate the reasons behind the inconsistency, but we didn't see the relevant analytical statements and experimental analysis in the article, and only gave Figure 1, but Figure 1 can only show that there is no difference between models and it is not directly related to the disturbance emphasized in this paper. The paper fails to provide a clear theoretical framework explaining why pixel importance, as measured by saliency maps, should be unreliable. The claim that the output probability drop is not always proportional to pixel importance is not sufficiently supported by analytical arguments or targeted experiments. The analysis lacks a detailed investigation into the underlying causes of the observed inconsistencies, such as the non-linearity of the model or the specific properties of the perturbation applied.
3. The experiment is not reasonable enough. In this paper, a total of 26,267 photos before and after the disturbance are directly tested together, which does not reasonably distinguish the experimental comparison before and after the disturbance, and can not clearly see the inconsistency of metirc after the disturbance. The experimental design does not adequately isolate the effect of the disturbance on the saliency metrics. By combining the perturbed and unperturbed images in the analysis, it becomes difficult to discern the specific impact of the perturbation on the pixel importance rankings. The lack of a controlled comparison makes it challenging to draw meaningful conclusions about the reliability of the metrics.
4. The conclusion is incomplete. From the analysis of arppd in table2, the conclusion of "much more compliant" cannot be drawn by hovering between 0.6 and 0.8. In addition, the final experimental conclusion has no exact correlation with the title of this paper, and the reasons behind it are not given. The conclusion that the proposed metrics reveal inconsistencies in saliency map fidelity is not strongly supported by the experimental results. The interpretation of ARPPD values between 0.6 and 0.8 as "much more compliant" is not convincing, and the paper does not provide a clear rationale for this interpretation. Furthermore, the link between the observed inconsistencies and the failure of sanity checks for saliency metrics is not explicitly established, leaving the reader without a clear understanding of the underlying mechanisms.

### Questions
See the weakness listed above

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper indicates that the existing saliency metrics based on pixel importance are unreliable when subjected to perturbations. To quantify the inconsistencies in saliency metrics, the Average Ratio of Positive Probability Drops(ARPPD) and the Average Pixel Rank Correlation(APRC) are introduced to measure the unreliability at model level.

### Strengths
1.	The authors investigated the reason of statistical inconsistencies in the existing saliency metrics which is omitted in previous studies.

2.	Extensive experiments demonstrated the applicability of the proposed metrics.

### Weaknesses
1.	The captions in Figure 2 are illegible, and Figure 2 needs more detail legends.

2.	I wonder if the perturbation is similar to some kinds of Data Augmentation, the results may be impacted.

### Questions
See weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper studies the saliency map created by CAM or its variation. Gaussian Blur is applied with different std values to perturb the image saliency. Then two metrics are proposed to measure the fidelity of the saliency map, denoted as Average Ratio of Positive Probability Drops, and Average Pixel Rank Correlation. The use of Gaussian with the proposed metrics is claimed can better measure saliency CAM.

### Strengths
This study attempts to analyze an important task in AI, how to understand the behaviour of a model, and how to measure if the understanding is correct.

### Weaknesses
The current draft requires some improvement before publishing, it is a little difficult to follow the idea.
The draft attempt to solve the problem in the fidelity measure for CAM, but the presentation did not show this main issue clearly. Some of the paragraphs are not related or unnecessary, please see the questions below. More importantly, the use of Gaussian Blur is not well introduced or explained, it seems an arbitrary solution jumping into the draft. The only reason discussed in Section 3.3 is to preserve the semantic information instead of removing it. However, this is exactly opposite to those previous perturbation used for fidelity measure. If the semantic content is always needed, how can we measure the CAM? or we do we still need to perturb? This draft seems missed the purpose of the perturbation, so the whole story is less solid. Besides the general idea, I highly doubted if Gaussian blur can retain the semantic information when the std is high enough. The two "proposed" metrics are very similar to previous solutions but using the Gaussian perturbation, thus the metrics cannot be considered as new proposals. To sum up, this draft requires more improvement at this moment.

1. Generally, the abstract and the introduction show the inconsistency in those saliency metric, which is used to measure the fidelity of those XAI methods. However, Fig.1 only shows the tiny difference in the CAM visualization, and this showcase seems not connected to the main story. Is it better to show the behaviour of those metrics when perturbing with different strategies?

2.The definition of the hierarchy in Table is not clear, could be removed.
3. Page 3, third paragraph, "the reason for such unreliability.. lies at model level", this claim is questionable, and I cannot find any explanation for this claim.
4. The same paragraph, "introduce two new metrics,....at model level 1", this is confusing without any explanation, the proposed metrics are also based on the change of confidence scores or pixel rankings, why they are at different levels than the previously proposed? Again, I suggest introducing the idea without relying on the confusing hierarchy could be more clear.
5. The extensive related work is not really necessary, the most related work seems (Tomsett 2020) and those fidelity metrics. However, they are not properly presented regarding the key problem, why different perturbation may lead to different results.
6. Section 2.1, first paragraph is confusing to me. It seems the whole paragraph is repeating how those metrics works, without introducing what the limitation is and why it is a limitation.
7. Section 2.2 Contribution 1: "to justify the unreliability"?? Again, the draft didnot show clearly what the unreliability is, and why does it need to be justified??
8. Section 2.2 Contribution 2: "Unlike...", The proposed methods are very similar to the previously used for fidelity measure, this claim is unclear to me.
9. Section 2.2, Contribution 3: ablation studies on different models and data are not considered as contributions.
10. Section 3.1 "Let R0 be the ranks of pixel", this sentence is wrong and inconsistent with the story after, it is not a list of ranks, it is a list of ranked pixels.
11. Section 3.1, the presented "framework" is not necessary, this is the common assumption behind most of the fidelity measure.
12. Eq(6), why is the rank invariant to the std value applied?
13. what is the meaning of the brackets in Eq 7?
14. For both metric, why are they both approaching 1 ideally? how can we know which saliency map is better? Strong gaussian blur will damage the semantic content, why we are still expecting 1?

Tiny problems:
The use of acronym is inconsistent.

### Questions
1. Generally, the abstract and the introduction show the inconsistency in those saliency metric, which is used to measure the fidelity of those XAI methods. However, Fig.1 only shows the tiny difference in the CAM visualization, and this showcase seems not connected to the main story. Is it better to show the behaviour of those metrics when perturbing with different strategies? 

2.The definition of the hierarchy in Table is not clear, could be removed.
3. Page 3, third paragraph, "the reason for such unreliability.. lies at model level", this claim is questionable, and I cannot find any explanation for this claim.
4. The same paragraph, "introduce two new metrics,....at model level 1", this is confusing without any explanation, the proposed metrics are also based on the change of confidence scores or pixel rankings, why they are at different levels than the previously proposed? Again, I suggest introducing the idea without relying on the confusing hierarchy could be more clear.
5. The extensive related work is not really necessary, the most related work seems (Tomsett 2020) and those fidelity metrics. However, they are not properly presented regarding the key problem, why different perturbation may lead to different results.
6. Section 2.1, first paragraph is confusing to me. It seems the whole paragraph is repeating how those metrics works, without introducing what the limitation is and why it is a limitation.
7. Section 2.2 Contribution 1: "to justify the unreliability"?? Again, the draft didnot show clearly what the unreliability is, and why does it need to be justified??
8. Section 2.2 Contribution 2: "Unlike...", The proposed methods are very similar to the previously used for fidelity measure, this claim is unclear to me.
9. Section 2.2, Contribution 3: ablation studies on different models and data are not considered as contributions.
10. Section 3.1 "Let R0 be the ranks of pixel", this sentence is wrong and inconsistent with the story after, it is not a list of ranks, it is a list of ranked pixels.
11. Section 3.1, the presented "framework" is not necessary, this is the common assumption behind most of the fidelity measure.
12. Eq(6), why is the rank invariant to the std value applied? 
13. what is the meaning of the brackets in Eq 7?
14. For both metric, why are they both approaching 1 ideally? how can we know which saliency map is better? Strong gaussian blur will damage the semantic content, why we are still expecting 1?

Tiny problems:
The use of acronym is inconsistent.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates perturbation-based metrics for evaluating the reliability of saliency maps for  image classification explanations. Perturbation-based approaches “delete” pixels to evaluate how much each pixel contributes to the model decision, but the method used to “delete” pixels (e.g., replacing them with 0s vs. random noise) has an impact on the evaluation result. This paper demonstrates that impact using blur as the deletion method and proposes a metric to measure how much the choice of replacement value in a perturbation analysis will affect the result.

### Strengths
There are some interesting ideas in this paper -- it does seem worthwhile to do a more in-depth analysis of how the choice of replacement value affects the results in perturbation-based methods.

### Weaknesses
The writing is frequently unclear, which makes many sections of the paper difficult to understand.

The explanation of the problem and previous literature is fairly shallow and sometimes incorrect. For example, pg 3 para 2 claims: “These metrics rely on perturbations (setting pixels to random values or 0), but do not justify the reason to do so.” The justification is that these perturbations “delete” the information in those pixels by replacing them with values that have no relation to the image class.

The main finding that different pixel replacements will produce different results in perturbation-based methods is unsurprising and was previously demonstrated in Tomsett et al., 2020.

I’m not sure the proposed metric has wide application, and this study isn’t sufficient to validate it – it should be validated on a wider range of perturbations (including methods like inpainting or replacing pixels with values drawn from the same/different classes).

### Questions
“Our choice of Gaussian Blur is based on the fact that it preserves the semantics of images compared to other random perturbations with mean or random values of the image.” This isn’t true for the CNN models used in this paper – blurring images significantly reduces the model’s ability to recognize the image, similar to adding pixel noise (Geirhos et al., 2018: https://arxiv.org/pdf/1808.08750.pdf).

Is the “Imagenette” dataset used in this paper a typo for ImageNet?

Why exclude inpainting / generative models from the set of possible perturbations? This seems like a completely valid type of perturbation that is very relevant if the goal is to show that different perturbations will have different

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

# Understanding and Mitigating Miscalibration in Prompt Tuning for Vision-Language Models

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 3, 6, 6

## Abstract
Confidence calibration is critical for the safe deployment of machine learning models in the real world.
However, such issue in vision-language models like CLIP, particularly after fine-tuning, has not been fully addressed.
In this work, we demonstrate that existing prompt tuning methods usually lead to a trade-off of calibration between base and new classes:
the cross-entropy loss in CoOp causes overconfidence in new classes by increasing textual label divergence, whereas the regularization of KgCoOp maintains the confidence level but results in underconfidence in base classes due to the improved accuracy.
Inspired by the observations, we introduce Dynamic Outlier Regularization (DOR) to ensure the confidence calibration on both base and new classes after fine-tuning. 
In particular, we propose to minimize the feature deviation of novel textual labels (instead of base classes) sampled from a large vocabulary.
In effect, DOR prevents the increase in textual divergence for new labels while easing restrictions on base classes.
Extensive experiments demonstrate that DOR can enhance the calibration performance of current fine-tuning methods on base and new classes.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper, through CoOp and KgCoOp, observe that when a model undergoes adaptation via prompt tuning, CoOp tends to be overconfident in novel classes, while KgCoOp, on the contrary, becomes underconfident. To address this tendency towards overconfidence/underconfidence, this paper propose a Dynamic Outlier Regularizer (DOR) term, which demonstrates performance improvements when the proposed regularizer is added to the algrorithms for prompt learning of VLMs.

### Strengths
1. A new blind point was identified (CoOp and KgCoOp becomes over/under confident)
2. Experimental results show performance improvement when the proposed regularizer is added.

### Weaknesses
1. The motivation was inferred from CoOp and KgCoOp, but in fact, these two algorithms lack adequate consideration for novel classes. For an effective analysis of this phenomenon, algorithms that directly account for novel classes should be utilized, such as CoCoOp, MaPLe, PromptSRC, DEPT, and TCP. If similar tendencies are observed in these algorithms, it would strongly support the authors' claim.

2. It appears that further explanation is needed regarding the concept of "Texture divergence." From my understanding, this divergence is due to the diversity of textual representation arising from CoOp's prompt learning method. However, finding concrete evidence to confirm this explanation is challenging. Additionally, a more detailed explanation of the notation, particularly the keywords emphasized in the paper, would enhance reader's understanding if the study.

3. More comparisons with other algorithms are necessary. Given the large number of prompt learning algorithms, further experimental comparisons are needed to confirm whether the effect of this regularizer is generalizable. (Similar with the first weakness statement)

### Questions
Please refer to the weakness part.

### Soundness
2

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
5

### Summary
This paper proposes Dynamic Outlier Regularization (DOR) to improve confidence calibration in prompt-tuned vision-language models (VLMs), particularly in CLIP. The authors argue that current prompt-tuning methods lead to miscalibration by creating a trade-off between base and new classes, with CoOp overconfident on new classes and KgCoOp underconfident on base classes. DOR aims to resolve this trade-off by introducing textual outliers to regularize model predictions, promoting consistent calibration across both base and new classes.

### Strengths
- The paper identifies a relevant issue in the domain of prompt tuning and confidence calibration in VLMs, an area of growing importance.
- The authors introduce a novel idea of using dynamically sampled textual outliers to address calibration inconsistencies, and the approach shows effectiveness across various datasets.
- DOR’s flexibility in working with multiple prompt-tuning methods is a potential advantage.

### Weaknesses
 - The paper does not include comparisons with several recent and closely related methods, such as CoPrompt and PromptSRC, which also address calibration issues and trade-offs between base and new classes. Without these comparisons, it is unclear whether DOR provides any substantial advantage over the state of the art, especially since these methods were specifically designed to tackle the same calibration challenges.

- The primary claim—that prompt-tuning methods like CoOp and KgCoOp introduce calibration trade-offs between base and new classes—has already been extensively studied in prior works. For instance, CoPrompt effectively handles these issues and includes mechanisms specifically designed to manage calibration across both class types. As such, the problem statement lacks novelty, and the paper provides insufficient rationale for why DOR would be preferable to these existing methods.


- While the paper offers some empirical evidence for DOR’s effectiveness, it lacks analysis that explains why the use of textual outliers should systematically address calibration trade-offs. Specifically, the mechanism by which these outliers regularize the model's predictions and lead to consistent calibration is not clearly articulated. The paper needs a more thorough theoretical justification for its approach.

- The proposed solution, while conceptually interesting, lacks practical guidelines on how to effectively select and implement outliers in a real-world setting. Given that the efficacy of DOR relies on appropriate textual outlier selection, more detailed criteria or algorithms for selecting these outliers would be necessary for practitioners to adopt this method. The current approach lacks a systematic method for identifying effective outliers, making it difficult to apply in practice.

- Interestingly, some of the latest methods show less improvement with the proposed solution compared to some of the earlier methods like CoOp. This indicates that the latest methods are already capable of handling the problem and don't require such a solution proposed in this paper. Again, the paper lacks a comparison to the latest method, making it difficult to understand if it has any usage.

### Questions
See the weakness section.

### Soundness
2

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
This paper introduces Dynamic Outlier Regularization (DOR), a method to improve confidence calibration in fine-tuned VLMs by controlling textual feature divergence (also can be extended to visual tuning) through the use of selected outliers, thereby enhancing model reliability on both base and novel classes.

### Strengths
1. DOR integrates smoothly with popular prompt-tuning methods (e.g., CoOp, KgCoOp) without requiring major architectural changes, making it easy to adopt in existing pipelines. 
2. The authors provided insightful analysis of how current prompt-tuning methods impact confidence calibration, with clear explanations for why overconfidence or underconfidence arises in certain settings. The motivation is clear.
3. The manuscript is well-written and in a good logic.

### Weaknesses
1. The ablation study is insufficient, e.g. how sensitive DOR is to the choice of outliers and whether different selection strategies could yield better results? Specifically, the paper does not explore the impact of varying the number of outliers used for regularization, nor does it investigate the effect of different similarity metrics when selecting outliers. Furthermore, the study lacks an analysis of the semantic relationship between selected outliers and base classes, which could provide insights into the effectiveness of the regularization.
2.  The experiments are largely limited to standard benchmarks without applying the method to domain-specific tasks (e.g., medical imaging or autonomous systems as the authors mentioned in the Introduction), where calibration is especially critical. The absence of experiments on specialized datasets limits the generalizability of the findings and the practical applicability of the proposed method. The paper should demonstrate the effectiveness of DOR in more challenging and real-world scenarios.

### Questions
1. When you calculate the semantic similarity between textual labels in WordNet and the base classes, do you use cosine similarity? Please Clarify. Would using a different metric (e.g. Euclidean distance) impact results?
2. The outliers​ are selected based on the top-K, but there’s no mention of a specific similarity threshold. Would setting a threshold affect performance?
3. How frequently are the outliers updated during training? Does the frequency affect DOR’s calibration performance?
4. In page 8, line 407-408, is it a typo (should be "CoCoOp" ranther than "CoOp") or a wrong statement (the number is wrong if you campred to the zero-shot CLIP)? Please correct it.
5. What criteria were used to select visual outliers from ImageNet-1K? How to ensure these outliers are sufficiently distinct from base classes without introducing irrelevant noise?
6.  How does DOR influence the feature space of base classes when incorporating visual outliers?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates the calibration performance of CLIP following fine-tuning. The author observes a trade-off in calibration between base and new classes and proposes a method called Dynamic Outlier Regularization (DOR). DOR samples categories unrelated to the base class from a large vocabulary to minimize the feature deviation of novel textual labels. Empirical results demonstrate that this approach outperforms the standard fine-tuning method across various settings.

### Strengths
1. The author conducted robust experiments that demonstrate how prompt fine-tuning prior to happiness can lead to a decline in the model's calibration performance.

2. The paper introduces an efficient normalization method designed to enhance the calibration performance of both base and novel classes.

3. The paper provides performance results across multiple calibration evaluation metrics and a range of experimental settings.

4. The writing is clear and well-structured, making it easy to read.

### Weaknesses
1. Previous works [1,2] have examined the calibration performance of pre-trained CLIP after fine-tuning. However, your paper lacks experimental results comparing your method with these studies. We recommend that you include such comparisons in your work.

2. Given that your method is based on experimental observations from CoOp and KgCoOp, we have concerns about its generalizability. For example, in Table 1, your method underperforms compared to Vanilla TCP in half of the settings. This raises questions about the robustness of the proposed approach across different fine-tuning strategies and datasets.

3. This article primarily selects outliers from WordNet. We are curious whether using different lexical databases significantly affects the results. The choice of the lexical database could introduce bias or limit the diversity of the outlier samples, potentially impacting the effectiveness of the Dynamic Outlier Regularization (DOR) method.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
3

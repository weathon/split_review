# A Simple Romance Between Multi-Exit Vision Transformer and Token Reduction

- Decision: Accept
- Scores: 8, 8, 6, 8

## Abstract
Vision Transformers (ViTs) are now flourishing in the computer vision area. Despite the remarkable success, ViTs suffer from high computational costs, which greatly hinder their practical usage. Token reduction, which identifies and discards unimportant tokens during forward propagation, has then been proposed to make ViTs more efficient. For token reduction methodologies, a scoring metric is essential to distinguish between important and unimportant tokens. The attention score from the $\mathrm{[CLS]}$ token, which takes the responsibility to aggregate useful information and form the final output, has been established by prior works as an advantageous choice. Nevertheless, whereas the task pressure is applied at the end of the whole model, token reduction generally starts from very early blocks. Given the long distance in between, in the early blocks, $\mathrm{[CLS]}$ token lacks the impetus to gather task-relevant information, causing somewhat arbitrary attention allocation. This phenomenon, in turn, degrades the reliability of token scoring and substantially compromises the effectiveness of token reduction. Inspired by advances in the domain of dynamic neural networks, in this paper, we introduce Multi-Exit Token Reduction (METR), a simple romance between multi-exit architecture and token reduction—two areas previously considered orthogonal. By injecting early task pressure via multi-exit loss, the $\mathrm{[CLS]}$ token is spurred to collect task-related information in even early blocks, thus bolstering the credibility of $\mathrm{[CLS]}$ attention as a token-scoring metric. Additionally, we employ self-distillation to further refine the quality of early supervision. Extensive experiments substantiate both the existence and effectiveness of the newfound chemistry. Comparative assessments also indicate that METR outperforms state-of-the-art token reduction methods on standard benchmarks, especially under aggressive reduction ratios.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work has proposed a new token-pruning method, by integrating the multi-exit strategy into ViT. This work diagnoses the inconsistency between [CLS] attention and token importance in early ViT block, which degrades the performance of token reduction methods. To tackle this problem, this work introduces multi-exit architecture that allows the [CLS] token to gather information pertinent to the task in the early blocks. It also adopts self-distillation to improve the quality of early supervision. As a results, it achieves state-of-the-art performance.

### Strengths
### Good Motivation
This work has adeptly identified and proposed solutions for a problem in the literature of token pruning method of ViT.

### Novelty and SOTA performance
To address the inconsistency between [CLS] attention and token significance at the early blocks, the proposed method that incorporates multi-exit into ViT) is novel and it shows effectiveness clearly by achieving state-of-the-art performance.

### Nice visualization
This work shows well-supportive visualization examples.

### Weaknesses
No exists.

### Questions
It would be better to shows the GPU-throughput and compare it with those of SOTA.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This submission introduces METR, a simple and effective technique for informed token reduction applied in Vision Transformer-based image classification. An analysis presented in the manuscript, demonstrates that the commonly used [CLS] token attention scores, acting as an importance metric for token pruning, are far more effective on deeper blocks in contrast to shallower ones. This is attributed to the long gradient distance from the task loss, traditionally applied at the end of the network. 

To remedy this, the manuscript proposes the introduction of intermediate classifiers at training time, forming a multi-exit transformer model, in which all token reduction blocks are exposed to stronger task supervision. Upon deployment, early-exits are removed eliminating any speed overhead, while extensive experiments demonstrate the effectiveness of the proposed method across different models and in comparison with several baselines.

### Strengths
-The manuscript focuses on the very interesting interplay between multi-exit models and token reduction. 

-Sec. 3.2, introduces a simple, yet effective solution to the examined problem. The discussion on the use of attention as an importance metric is insightful and many relevant works can benefit from these findings.

-Experiments are extensive in terms of examined models and baselines, and validate the superiority of the proposed approach to the baselines. 

-The manuscript is generally well-written and easy to follow.

### Weaknesses
 -The use of self-distillation loss for the multi-exit training (Eq.9), in place of traditional multi-exit loss of Eq.8, although effective, is not adequately motivated. Self-distillation is typically used to improve the accuracy of the trained exits, which is not a requirement here as these are discarded at inference time. The manuscript would benefit from a more insightful analysis of what motivated this design choice/ why do the authors believe this works better than the traditional approach. Specifically, the manuscript lacks a clear explanation of why the soft labels from the final classifier, used in the self-distillation loss, provide a better training signal for the intermediate classifiers compared to the hard labels used in a standard multi-exit setup. This is especially important given that the intermediate classifiers are primarily used to guide token reduction and not for prediction themselves.

-Row(2) in Tab.3 seems to be the equivalent of row (4) in Tab.2, where multi-exit and token-reduction fine-tuning are jointly applied (instead of the two-stage ablation in Tab2). If this is the case, it can be deduced that token-aware fine-tuning notably reduces the effectiveness of the proposed approach, leading to significantly smaller gains even when aggressive token reduction takes place. This fact is separate from the commented fading of multi-exit effects after separate fine-tuning and needs to be further investigated/discussed in the manuscript. The manuscript should explore why fine-tuning with token reduction seems to diminish the benefits of the multi-exit training, and whether this is due to the token reduction process itself, or the fine-tuning procedure, or an interaction between both. It would be beneficial to analyze if the token selection mechanism is becoming less effective after fine-tuning, or if the model is simply becoming more robust to less optimal token selection.

Note: An appendix is mentioned in the manuscript (Sec.4), but was not accessible to the reviewer.

### Questions
1. What motivated the use of self-distillation in place of traditional multi-exit training in the proposed setting? What are the authors' insights about the demonstrated effectiveness of this design choice?

2. Is token-reduction aware fine-tuning indeed limiting the effectiveness of the proposed approach? If yes, this should be commented in the manuscript.

3. In Tab.1,2,3 does “reduce ratio” refer to number of tokens or GFLOPs? Both should be reported to get the full picture. 

Minor comments/ Presentation:
-Notation in Sec.3 is quite loose. Consider defining the dimensionality of each introduced symbol (X,x,A,...).
-Sec3.2: Symbol a^{c-p} is confusing.
-Sec4.1.1: without incorporate -> without incorporating,  Subsequently, We (...) -> Subsequently, we (...)

### Soundness
3 good

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces METR, a straightforward approach that combines multi-exit architecture and token reduction to decrease the computational burden of vision transformers (ViTs) while maintaining accuracy. The authors discover a discrepancy between the attention score of [CLS] and the actual importance of tokens in early ViT blocks, which negatively affects the performance of token reduction methods relying on this metric. The authors demonstrate that METR can improve existing token reduction techniques and achieve better results than state-of-the-art methods on standard benchmarks, particularly when using high reduction ratios.

### Strengths
Overall, METR is a promising method that can help reduce the computational cost of ViTs while maintaining accuracy.

- The paper is clear and well-motivated.
- The idea is intriguing and demonstrates significant improvement compared to other baselines.
- The evaluation is well-designed and highlights the core contribution in the design section.

### Weaknesses
 - The evaluation demonstrates a notable improvement in accuracy compared to the baseline frameworks. It will be helpful to further demonstrate the reduction in latency with fewer FLOPs compared to other baselines.
- It would be beneficial if the author could offer more insights in the method section, such as explaining how and why this design can enhance performance.

### Questions
Please see above

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
This paper combines two well-established methods, multi-exit neural networks and vision transformer (ViT) token reduction, to improve the efficiency of ViT. The background is that the prominent ViT token reduction techniques like EViT are based on removing unimportant tokens based on the attention scores that naturally indicate the contribution of the visual tokens to the final ViT prediction. The authors' motivation is that in the previous method, the ViT had no incentive to make sure the attention scores in the shallow layers aligned with the semantic importance of the visual tokens. To motivate the ViT to have such an incentive, the authors propose to exploit the multi-exit training method with ViT exits in the intermediate layers, which requires early class information fusion via the attention scores, thus ensuring the attention scores exhibit semantic importance properties. With the combination of the two techniques, the authors show a noticeable improvement compared to the baseline, especially when a significant number of tokens are removed or with more finetuning epochs.

### Strengths
- The method is clearly motivated. Token reduction based on the existing attention scores in ViT has been shown to be an effective method in reducing computational costs while maintaining most of the classification accuracy. The authors propose to add the pressure of extracting the classification information in the shallow layers via the multi-exit mechanism, which forces the attention scores in the shallow layers to focus on the important tokens as the scores are directly used as weights to gather the information for classification in the multi-exits. 
- The experiments are extensive and show the effectiveness in improving the classification accuracy over the baselines, especially with a longer training schedule. Experiments also demonstrate the proposed method's effectiveness from different perspectives, including different base models (DeiT/MAE), different model sizes, and different base methods (EViT/DiffRate).
- The visualization seems to support the claim that adding multi-exit modules to the ViT makes the attention scores in the shallow layers aligned better with human perception (higher scores are allocated to more important tokens on the objects).

### Weaknesses
The weaknesses are mostly minor issues, but it is important to address them to make the paper clearer and easier to understand.
- The phrase "Reduce Ratio" is not a good term to indicate the ratio of how many tokens are kept. Please change to another term like "keep ratio" to make it clear.
- Table 1 is not well explained. It took me a while to understand the setting of the experiment. The term "Off-the-shelf" is not immediately understandable. It would improve clarity by explicitly explaining the details of the experiments. Specifically, it's unclear what pre-training was used for the "off-the-shelf" models and how that relates to the reported results. The table also lacks details on the specific datasets used for evaluation in each setting, making it difficult to assess the validity of the comparisons.
- It would improve the readability of the paper by changing some words/notations to standard ones, e.g., CSE -> CE for cross-entropy.
- There seems no appendix, but at the end of Section 4 first paragraph, it says "See appendix for detailed experiment settings."
Please carefully proofread the whole paper to address these nuanced issues.

### Questions
- Is the loss $L_{me}$ in Eq (8) also added to the $L_{total}$? It is not clearly mentioned in the paper.
- Figure 2 can be improved with better illustration and explanation. Specifically, the arrows from the $A^c$ to the [CLS] are somewhat confusing. And why do the patch tokens have fading colors from the bottom up?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

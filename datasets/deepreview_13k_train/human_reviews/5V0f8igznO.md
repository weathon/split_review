# Captured by Captions: On Memorization and its Mitigation in CLIP Models

- Decision: Accept
- Scores: 6, 5, 5

## Abstract
Multi-modal models, such as CLIP, have demonstrated strong performance in aligning visual and textual representations, excelling in tasks like image retrieval and zero-shot classification. Despite this success, the mechanisms by which these models utilize training data, particularly the role of memorization, remain unclear. In uni-modal models, both supervised and self-supervised, memorization has been shown to be essential for generalization. However, it is not well understood how these findings would apply to CLIP, which incorporates elements from both supervised learning via captions that provide a supervisory signal similar to labels, and from self-supervised learning via the contrastive objective.
To bridge this gap in understanding, we propose a formal definition of memorization in CLIP (CLIPMem) and use it to quantify memorization in CLIP models. Our results indicate that CLIP’s memorization behavior falls between the supervised and self-supervised paradigms, with "mis-captioned" samples exhibiting highest levels of memorization. 
Additionally, we find that the text encoder contributes more to memorization than the image encoder, suggesting that mitigation strategies should focus on the text domain. 
Building on these insights, we propose multiple strategies to reduce memorization while at the same time improving utility---something that had not been shown before for traditional learning paradigms where reducing memorization typically results in utility decrease.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
**Summary:** Understanding the memorization / generalization tradeoff is important to properly quantify modern ML models. This work focuses on CLIP which applies InfoNCE between image and text pairs and attempts to quantify the extent to which CLIP models memorize. The authors introduce CLIPMem to quantify memorization and find that the text encoder contributes more to memorization than the vision encoder. They also propose strategies to mitigate / remove memorized samples to improve performance.

### Strengths
**Stong points:**
- Well highlighted literature on memorization.
- Defines CLIPMem based on hold one out strategy (similar to Feldman et. al in supervised learning).
- Interesting results on mis-captioned text labels, multi-caption and removal of memorized examples.
- Reasonable pretraining datasets like CC3M
- Clean separation of training and test splits for measuring memorization.

### Weaknesses
 **Weak points:**
- Missing ability for CLIPMem to be applicable to general off-the-shelf CLIP models. Currently if I understand correctly it requires retraining on specific splits. 
- Clarity of specifics of CLIPMem is used for vision only and joint vision + text can be improved. Specifically, it's unclear how the leave-one-out strategy is applied in the multimodal setting. Is it applied to each modality separately and then combined, or is it a joint leave-one-out? More details on the exact computation are needed.
- The noising results (Table 5-b) are not very convincing. Almost all the results are within the same +/- std range. The trend is not very clear, and the error bars are quite large, making it hard to draw strong conclusions.
- The linear probe accuracy seems quite low (Table 1, 5-a, 5-b,  6-a/b).  It raises concerns about the quality of the learned representations and whether the memorization results are meaningful in the context of a poorly performing model.

**Nit:**
- Text and images in Figure one are very hard to read. Suggest larger and fewer images and move rest to appendix. 
- Figure 3 can be make larger / more readable by doing share-y and increasing font sizes.

### Questions
**Questions:**

- Is CLIPMem bounded? 
- What dimension is kept constant for Table 1? Are the total training samples [count] seen the same? 
- It would be interesting to evaluate infinite data regimes (i.e. no repeated data) rather than classical K-epoch  runs. Would the results for - memorization hold here? Just like in language this setting is becoming more and more common.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces CLIPMem, a novel metric to quantify memorization in CLIP, which combines elements of supervised and self-supervised learning. The paper shows that memorization within CLIP often arises from mis-captioned or atypical samples, particularly within the text modality rather than the image modality. They propose mitigation strategies that reduce memorization without sacrificing model utility, unlike traditional methods that often degrade performance when reducing memorization. It reports several interesting findings, including 1) CLIP's memorization lies between supervised and self-supervised paradigms, with high memorization for data with inaccurate or misaligned captions; 2) Text domain adjustments, such as using varied or augmented captions, reduce memorization and improve generalization, defying the usual trade-offs seen in other paradigms.

### Strengths
+ It introduces a new metric -- CLIPMem to provide a new way for measuring memorization in multi-modal settings, a gap in previous research.
+ It performs empirical analysis to show differences in memorization between the text and image modalities, providing actionable insights.
+ It proposes techniques to successfully reduce memorization while preserving or even enhancing model utility, challenging established norms.
+ By highlighting the risks of training with uncurated, potentially mis-captioned data, the paper suggests guidelines that can benefit real-world multi-modal model training practices.

### Weaknesses
 - While tailored to CLIP, the metric and findings may need adaptation to apply effectively to other multi-modal models with different architectures. Specifically, the reliance on contrastive learning objectives and separate encoders might not directly translate to models employing different fusion mechanisms or generative approaches. The paper does not explore the sensitivity of CLIPMem to variations in model architecture, which could limit its general applicability.
- The experiments focus on datasets like COCO and CC3M, so it’s unclear how well these findings generalize to other large-scale or domain-specific datasets. The characteristics of these datasets, such as the nature of captions and image content, might not be representative of other domains, potentially affecting the observed memorization patterns. For example, datasets with more abstract or ambiguous captions might exhibit different memorization behaviors.
- The mitigation strategies, such as augmenting captions or generating variations, may incur additional computational costs in training, which could limit practicality for some users. While the paper mentions these strategies, it lacks a detailed analysis of their computational overhead, including memory usage and training time increases. This makes it difficult to assess the actual trade-off between memorization reduction and computational efficiency.

### Questions
Would you please comment on how the metric adapt to other multi-modal models besides CLIP?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
They study the memorization problem in the CLIP model unlike existing studies focusing on the unimodal memorization problem. 
They propose a new metric to analyze it and find that memorization seems to be more significant in text encoder than in image encoder. Their analysis indicates that augmenting captions can be a key to mitigating memorization in the CLIP model. Their experiments confirm that augmenting captions can improve the quality of the image encoder's representations while reducing memorization.

### Strengths
1. They propose a new metric to measure memorization in the CLIP model. The design of the metric is reasonable. 
2. Their insight that memorization is more significant in the text encoder is new and might interest readers. 
3. They conduct analysis on the augmentation of the text and images, which might be also interesting to some readers. 
4. This paper is well-organized and easy to follow.

### Weaknesses
1. They do not discuss how model size can affect memorization. Although I am not very familiar with this topic, I guess the model size can affect their arguments. For example, if they utilize a larger image encoder, the memorization might be more significant on the image side. Therefore, I think their conclusion about which encoders suffer more from memorization can change by the size of the encoders, but they do not discuss much. 

2. Most of their findings sound a bit too reasonable and are not surprising. Their finding that augmenting text improves the CLIP model has already been observed in many previous papers though they probably did not discuss memorization. Also, it is not hard to imagine that augmenting datasets mitigates memorization. In these points, I think their findings are not impressive. 

3. They mention that their metric is effective in removing noisy samples. But, they compare their approach only with random replacement. I think they need to add more baseline, such as naive CLIP's similarity as done in many works. 

4. In Table 1, the authors augment images by using a diffusion model. But, as they imply, such augmentation can cause a distribution shift in the image side and does not give much intuition about image augmentation. 

Overall, I think this paper is well-organized and delivers a clear statement to readers, which I like. However, I think their findings are not very surprising and lack impact due to the reasons described in 1, 2. My rating is based on it.

### Questions
My rating is mainly based on 1 and 2. Please respond to those points.

### Soundness
3

### Presentation
3

### Contribution
2

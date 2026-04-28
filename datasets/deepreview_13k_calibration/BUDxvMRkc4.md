# BLG: BALANCED LANGUAGE DISTRIBUTION AS GUIDANCE FOR ROBUST LONG-TAILED VISION CLASSIFICATION

- Decision: Reject
- Avg Score: 4.67
- Scores: 6, 5, 3

## Abstract
Recently, pre-trained contrastive visual-linguistic models such as CLIP have shown promising multi-modal capabilities in processing various downstream vision tasks. However, their effectiveness in handling the long-tailed vision recognition problem remains under-explored. In this work, we observe that \textit{textual features from fine-tuned CLIP are relatively balanced and discriminative than the visual features}. Based on this observation, we propose to leverage balanced text features as prototypes to guide disentangled robust representation learning of biased visual features. Specifically, we first fine-tune CLIP via contrastive learning to help the encoders adapt to the target imbalanced dataset. Then we freeze the vision encoder and employ a linear adapter to refine the biased vision representation. For final vision recognition, a linear classifier initialized by fine-tuned textual features is integrated into the framework, where we consider the weights of the classifier as prototypes. For robust vision representation learning, we introduce a principled approach where we minimize the optimal transport distance between refined visual features and prototypes to help disentangle the biased vision features and continuously optimize prototypes moving towards the class center. We also design a supervised contrastive learning loss based on the transport plan to introduce more supervised signals and class-level information for further robust representation learning. Extensive experiments on long-tailed vision recognition benchmarks demonstrate the superiority of our method in using vision-language information for imbalanced visual recognition, achieving state-of-the-art (SOTA) performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
After the advent of vision-language pre-training, numerous works have adapted the pre-trained vision-language model to various vision tasks, including long-tailed recognition. This paper first presents empirical evidence that textual features remain balanced even after fine-tuning in the context of long-tailed classification. Based on this, the authors propose a framework that leverages balanced textual features as a guide to obtain more robust visual features.

### Strengths
1. The empirical finding that, during the fine-tuning of the entire vision-language pre-trained model on long-tailed data, textual features tend to achieve balance is quite intriguing. This paper goes beyond this observation and contributes to the community by proposing a concrete methodology that leverages balanced textual features to rectify imbalanced visual features.
2. The thorough ablation study conducted on the elements comprising "Phase B," proposed in this work, effectively underscores that the suggested $L_{\text{OT}}$ and $L_{\text{SCT}}$ indeed enhance performance.

### Weaknesses
1. The overall structure of this paper, which deals with challenges in contrastive learning methods due to class imbalance and suggests remedies, evokes thoughts of Suh and Seo (2023). Nevertheless, the current paper does not include any discourse on this topic.
2. Moreover, while one could mention Kang et al. (2021) as a seminal work on achieving a balanced and discriminative feature space in long-tailed classification scenarios, this is also not discussed.

### Questions
1. Could you offer some informed speculation about why there is a tendency for textual features to be balanced?
2. Since comparing performance between different architectures does not hold much significance, it would be better to provide results for RN50 and ViT-B/16 in separate groups.
3. Does the proposed approach result in any additional training expenses? For instance, what are the costs associated with setting up an optimal transport plan?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This study discovers that the fine-tuned CLIP's textual features are more balanced and discriminative compared to its visual counterparts. Building on this, the research proposes utilizing balanced textual features as prototypes to guide the learning of robust representations for biased visual features. The CLIP is further fine-tuned through contrastive learning, followed by the optimization of biased visual representations using linear adapters and the introduction of optimal transport distance to help decouple biased visual features. Additionally, a supervised contrastive learning loss based on the transport plan is designed. Experimental results indicate that the approach excels in leveraging visual-language information for imbalanced visual recognition, achieving state-of-the-art performance.

### Strengths
1. Extensive experiments on ImageNet-LT, Places-LT, and iNaturalist 2018 have demonstrated the effectiveness of the proposed method.
2. Comprehensive visualizations and ablation studies were conducted to validate the impact of the proposed method.

### Weaknesses
1. The experiment results indicate that the method underperforms for “many” classes in long-tail data.
2. The proposed method employs a two-stage training process and fine-tunes the Full-CLIP, which requires significant computational resources and has a prolonged training duration.
3. The proposed method doesn't seem to have a specific design tailored for long-tail data. The approach of using textual features as guidance for better image features can be applied to situations with limited image feature quality for various reasons, such as long-tail, few-shot, noisy data, generated data, low-resolution data, and so forth.

### Questions
1. Why does the proposed method underperform in “many” classes of LT dataset? An analysis of the underlying reasons would be appreciated.
2. The experimental results show that the proposed method underperforms in “many” classes of LT dataset. Does this imply that the method is primarily effective for situations with the few-shot scenario (i.e., “medium” and “few” classes in long-tail datasets)?
3. Balanced sampling is a fundamental operation in long-tail methods. Why is random sampling used when fine-tuning the CLIP in the initial stage? Is it to intentionally obtain a CLIP encoder with strong biases caused by imbalance?
4. Reference [1] also leverages CLIP's text features to enhance the discriminative power of image features. In [1], directly using text features and image features in concurrent training a linear classifier can achieve significant improvements in few-shot tasks. However, compared to the method in this paper, the method in [1] is much simpler, with much faster computation speeds and far less computational overhead.
[1] https://arxiv.org/abs/2301.06267

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This study introduces a framework designed to enhance CLIP in addressing long-tailed visual recognition challenges. This framework integrates a supervised contrastive loss mechanism, grounded on the transport plan, to fortify visual feature extraction. Several evaluations conducted on benchmarks corroborate that this proposed method significantly facilitates discriminative visual feature learning and achieves SOTA performance in long-tailed recognition tasks.

### Strengths
1. The idea of this paper is clear and easy to follow.
1. Experimental results show the effectiveness of the proposed method.

### Weaknesses
1. Lack of innovation. The approach in this paper provides a more balanced prototype for visual pre-training models to guide the learning of visual feature extractors and designs supervised comparative learning loss. However a similar approach has appeared in previous long-tail methods [1]. The differences in this paper are: 1. A more robust pre-training model, CLIP, is utilized. 2. A text-based prototype design approach is used to replace the target anchor. These innovations are more limited.

2. Some modules are without good motivation.
For example:
- Why do we need a learnable linear classifier? The purpose of its existence seems to be the matching of visual features with textual features. However, the weights of the classifier will change during training, which does not narrow the gap between template label text and image feature distributions.
-  In the unsupervised prototype-guided feature learning part, why choose cos similarity as the distance metric instead of other metric methods such as minimum entropy?
-  For the modules of learnable classifier, unsupervised prototype-guided feature learning, and supervised contrastive loss, it seems to be an incremental improvement and not complementary, so why use them to train models together?

### Questions
please refer to Weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

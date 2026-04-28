# INDIRECT ATTENTION: IA-DETR FOR ONE SHOT OBJECT DETECTION

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 5, 8, 5

## Abstract
One-shot object detection presents a significant challenge, requiring the identification of objects within a target image using only a single sample image of the object class as query image. Attention-based methodologies have garnered considerable attention in the field of object detection. Specifically, the cross-attention module, as seen in DETR, plays a pivotal role in exploiting the relationships be-
tween object queries and image features. However, in the context of DETR networks for one-shot object detection, the intricate interplay among target image features, query image features, and object queries must be carefully considered.
In this study, we propose a novel module termed ”indirect attention.” We illustrate that relationships among target image features, query image features, and object queries can be effectively captured in a more concise manner compared to
cross-attention. Furthermore, we introduce a pre-training pipeline tailored specifically for one-shot object detection, addressing three primary objectives: identifying objects of interest, class differentiation, and object detection based on a given
query image. Our experimental findings demonstrate that the proposed IA-DETR (Indirect-Attention DETR) significantly outperforms state-of-the-art one-shot object detection methods on both the Pascal VOC and COCO benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work introduces a method for one-shot object detection, a domain that requires training only on base categories without fine-tuning on novel categories. Specifically, the method employs an architecture comprising solely a feature encoder, i.e., a backbone model, and a decoder with indirect attention, which processes queries, keys, and values from distinct sources rather than the same source as in conventional cross-attention mechanisms. Furthermore, a two-stage training approach is utilized, involving pretraining with a hybrid strategy that combines supervised and self-supervised learning, followed by a fine-tuning stage. The incorporation of box-to-pixel relative position bias and contrastive loss enhances performance. Comprehensive experiments on the Pascal VOC and COCO datasets are conducted and  results for both seen (base) and unseen (novel) categories are reported in the work.

### Strengths
1. This paper is overall well-written, with just a few typos to address.
2.  Rather than employing a standard architecture with a backbone, encoder, and decoder, the proposed work eliminates the feature encoder for support-query aggregation and introduces a cross-attention mechanism that directly processes the support image, target image, and object queries. This design appears to offer a more generalized solution that facilitates direct application without the need for fine-tuning.

### Weaknesses
1. The primary novelty of this paper, the indirect attention mechanism, lacks a clear theoretical foundation. Indirect attention takes Q as the object query, K as the support (query) image feature, and V as the entire image feature, thereby adjusting the feature for each object query based on the global image feature and the similarity between support and object queries. Given that both the support and object queries represent local aspects of an object, it remains unclear how the mechanism determines the channel weights of the image feature, which encompasses multiple objects as well as the background. Specifically, the mechanism's reliance on a similarity measure between local object queries and local support features to modulate a global image feature is not well-justified. The process of using these local similarities to derive channel weights for the entire image feature, which contains both foreground and background information, needs further theoretical explanation.
2. The results in the ablation studies do not align with those presented in the main table, Table 1. Specifically, the AP0.5 for seen categories in Table 1 is 73.5, whereas the results for seen categories in Tables 3-5 are reported as higher, despite all evaluations being conducted on the Pascal VOC dataset according to line 403. This inconsistency undermines the persuasiveness of the experimental results. In addition, it lacks experimental comparison with recent studies that are published in 2023 and 2024. Furthermore, the performance trade-off between seen and unseen classes is not adequately addressed. The proposed IA-DETR in Table 1 shows a significant improvement in unseen classes (~16%) compared to Table 3, but at the cost of a substantial decrease in seen class performance (~10%). This trade-off needs to be discussed in detail, including the underlying reasons and implications for practical use.

### Questions
Here are more comments for your concern, 

1.  Typos

line 292: 3.5 TRAINING STRATEGY: --> 3.5 TRAINING STRATEGY (no clone here). 
Line 246: where the whre --> where the 

2.  A curious querstion here: as claimed in line 208-209, "in the decoder, instead of using ...., we proposed indirect attention, that directly exploits ...."  since it is an directly exploitation, why the process is named "indirect"  attention? 

3.  What's the query patch in 322, shouldn't the output only contains vectors corresponding to each object query and the background? 

4.  In 299, it claimed that this work adopts two-stage training, pretraining and finetuning. As claimed in the related work, one-shot object detection(OSOD) does not allow for a finetuning, so it is unfair to compare with other OSOD methods? Hope the authors can explain more on the finetuning stage. 

5.  In line 197, it assumes that "the target image contains at least one instance of the same class as the object in Q", here Q is the query image.  The assumption actually cannot hold in realistic settings, as for detection we don't know the content of the target image, which may or may not include the support(query) class

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Overall: This paper introduces IA-DETR, a novel one-shot object detection model that uses indirect attention to efficiently capture relationships between target image features, query image features, and object queries. The proposed method significantly outperforms state-of-the-art techniques on the Pascal VOC and COCO benchmarks, demonstrating its effectiveness and efficiency.

### Strengths
- Good formulas and figures.
- The idea of extending the transformer attention mechanism to three distinct elements is simple.
- Comprehensive experiments yield robust and state-of-the-art results.
- The concept of IA-DETR is innovative for OSOD (One-Shot Object Detection).

### Weaknesses
 -  Novelty is limited: the new technical thing proposed in this paper is "indirect attention" which differs from the previous attention by using two inputs for K and V.   However, this idea seems direct and too simple without other technical contributions.
- The experimental analysis of the indirect attention is not comprehensive, such a manner could be regarded as using the K, and V layers to fuse the features of the input K (query images features P) and V (target image features T), how about the comparison result of first using some other simple fusion methods e.g., MLP([P, T])  and then the typical cross-attention. The lack of comparison with a simple feature fusion approach followed by standard cross-attention makes it difficult to isolate the specific contribution of the proposed indirect attention mechanism.
- The experiments in Tables 1 and 2 are not based on multiple runs, which will weaken the robustness of the proposed method. It is crucial to demonstrate the stability of the results by reporting the mean and standard deviation across multiple runs with different random seeds, especially given the stochastic nature of the training process and the random selection of query images in each run.
- The paper does not explicitly state whether the indirect attention method is applied during the pre-training stage. Given that the main challenge in OSOD is the scarcity of positive samples, and the proposed method succeeds during fine-tuning, it should ideally also be effective in the pre-training stage, where there are more positive samples available. Therefore, if indirect attention is applied during pre-training, results for this stage should also be presented. Furthermore, it is unclear if the backbone is frozen during pre-training, which could significantly impact the effectiveness of the indirect attention mechanism.
-  Minor: Figure 3 is too large.
- The left and right quotation marks do not match on lines 18 and 83.

### Questions
please see weakness

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
The paper proposed a novel DETR structure named "IA-DETR" that aims to more effectively capture the relationship among the target image features, query image features, and object queries. The method is evaluated on the standard PASCAL and COCO datasets, and the experimental results indicate that the proposed method has surpassed the existing methods.

### Strengths
1. The proposed method is novel and may have a positive effect on other related research.
2. The experimental results indicate that the method has achieved SOTA on the standard benchmark.
3. The motivation is clear, and the paper is in good structure.

### Weaknesses
1. Although the motivation is clearly stated, the first two paragraphs are slightly tedious. The author could consider trimming this introduction and making the motivation more straightforward.
2. In line #077 ~ #082, the paper states that one motivation of the proposed method is to ease the computational overhead in an existing method caused by additional cross-attention. To support this assumption, it is necessary to include an ablation study regarding the computational expense. If I missed this, please point it out during the rebuttal.
3. According to recent works on DETR (e.g., SQR [Chen et al.]), it is not only the final layer of the decoder that produces the correct prediction results; the output of the middle layer of the decoder sometimes produces better results. Is the proposed indirect-attention applied to each layer of the decoder? Is it possible that only applying on several layers of the decoder would get better performance?
4. In the last two rows of Table 6, the MIM pre-trained backbone decreases the AP50 of seen categories but increases the unseen categories. While the paper claims that the MIM is not very significant, then there should be more discussion about why the MIM is still necessary here.

### Questions
Please refer to the weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper addresses the limitations of the double cross-attention strategy found in current one-shot object detection (OSOD) methods and presents the indirect-attention (IA) module as a practical alternative. In addition to the IA, the proposed IA-DETR model enhances the OSOD task by incorporating Box-to-pixel relative position bias (BoxRPB) and a contrastive pre-training pipeline specifically designed for the one-shot object detection head. Experimental results demonstrate the effectiveness of this model on the Pascal VOC and COCO datasets.

### Strengths
+ The concept of indirect attention is straightforward and can be easily understood and implemented.

### Weaknesses
 - The experiments conducted may have issues regarding fairness. When evaluating the effectiveness of various OSOD methods, the choice of backbone architecture is significant. The proposed IA-DETR utilizes SWIN-based MIM pre-trained weights as its backbone, which differs from the more commonly used ResNet50 and reduced-ImageNet pre-trained weights in existing OSOD methods. It would be beneficial to first validate the proposed model architecture with the same backbone before progressing to a stronger one. Additionally, it's important to note that in the OSOD task, the dataset used for obtaining the pre-trained weights should exclude any classes that are present in the Pascal VOC and COCO datasets.

- The authors assert that the double cross-attention block results in a quadratic increase in computational cost as the number of features increases. However, their experiments do not provide sufficient support or clarification on how this increased computational burden impacts an OSOD model. Specifically, the authors should provide a more detailed analysis of the computational complexity, including FLOPs and memory usage, as a function of input feature size for both the double cross-attention and the proposed indirect attention mechanisms. This analysis should be conducted within the context of the OSOD task to demonstrate the practical implications of the computational differences.

- In the proposed IA-DETR, it is interesting to consider alternative combinations of object queries, query image features, and target image features for their roles as query, key, and value. Including comparisons of these variations in the ablation study would enhance the comprehensiveness of the research. For instance, the authors could investigate the performance when using the target image features as the query and the query image features as the key, and vice-versa, while keeping the object queries as the value. This would help to understand the importance of each feature type in the attention mechanism.

- The findings from the ablation study indicate that the performance improvements attributed to the proposed indirect attention mechanism and the contrastive pre-training pipeline are quite modest. It appears that the overall effectiveness of the model is more significantly influenced by the backbone and the BoxRPB component. Consequently, the technical contributions of these enhancements are somewhat constrained.

### Questions
The primary concern of this manuscript is on the experiments conducted. It is important to assess the appropriateness of utilizing the SWIN-based MIM pretrained backbone. Additionally, the ablation study does not adequately demonstrate the contributions of the indirect attention mechanism and the contrastive pre-training pipeline as claimed by the authors. To enhance the manuscript, a more detailed analysis should be included to clarify the effects of the proposed indirect attention and the contrastive pre-training approach.

### Soundness
2

### Presentation
2

### Contribution
2

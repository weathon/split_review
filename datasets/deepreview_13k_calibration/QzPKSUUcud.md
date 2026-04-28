# A Simple Framework for Open-Vocabulary Zero-Shot Segmentation

- Decision: Accept
- Avg Score: 6.25
- Scores: 5, 6, 6, 8

## Abstract
Zero-shot classification capabilities naturally arise in models trained within a vision-language contrastive framework. Despite their classification prowess, these models struggle in dense tasks like zero-shot open-vocabulary segmentation. This deficiency is often attributed to the absence of localization cues in captions and the intertwined nature of the learning process, which encompasses both image representation learning and cross-modality alignment. To tackle these issues, we propose $\mname$, a \textbf{Sim}ple framework for open-vocabulary \textbf{Z}ero-\textbf{S}hot \textbf{S}egmentation. The method is founded on two key principles: \textit{i)} leveraging frozen vision-only models that exhibit spatial awareness while exclusively aligning the text encoder and \textit{ii)} exploiting the discrete nature of text and linguistic knowledge to pinpoint local concepts within captions. By capitalizing on the quality of the visual representations, our method requires only image-caption pairs datasets and adapts to both small curated and large-scale noisy datasets. When trained on COCO Captions across 8 GPUs, $\mname$ achieves state-of-the-art results on 7 out of 8 benchmark datasets in less than 15 minutes.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work proposes a simple framework for open-vocabulary Zero-Shot Segmentation with two key principles of leveraging frozen
vision-only models and exploiting the discrete nature of text and linguistic knowledge.

### Strengths
The experimental performance is good.

### Weaknesses
1. The novelty and contribution is limited. First, I prefer simple method. I believe that the simple method is more valuable for applications and research. However, simple method requires more deep analysis and insights. Unfortunately, this work only presents a simple method without any insights. The method is designed without motivation or explanation. This paper looks like a experiment report, rather than a research paper. For a good research paper, the authors need to tell new insights, rather than just propose a model and conduct some experiments. The core issue is the lack of a clear hypothesis or theoretical grounding for the proposed approach. The paper does not articulate why this particular combination of frozen vision models and discrete text representations should be effective, beyond the empirical results. There is no discussion of the underlying mechanisms that enable the method to perform well, such as how the discrete nature of text contributes to improved segmentation or why freezing the vision model is beneficial. The work lacks a theoretical framework to explain the observed performance, which makes it difficult to generalize the findings or understand the limitations of the approach.
2. The comparison is unfair. The proposed method is trained on COCO Captions (Lin et al., 2014; Chen et al., 2015) and LAION-400M (Schuhmann et al., 2021) and the image encoder is pretrained on LVD-142M dataset, as shown in L764-L774. However, other methods are not trained on these large-scale dataset. Even trained on these large datasets, the performance improvement is limited and the proposed method even performs worse than previous methods on Pascal VOC dataset. For example, the proposed method SimZSS trained on LAION-400M achieves 48.6 on Pascal VOC, which is much lower than CLIP-DINOiser (Wysoczanska et al., 2023), CLIP-DIY (Wysoczanska et al., 2024), OVSegmentor (Xu et al., 2023a), OVDiff (Karazija et al., 2023), CLIPpy (Ranasinghe et al., 2023) and TCL (Cha et al., 2023). The paper does not adequately address the potential for overfitting to the specific datasets used for training. The performance on Pascal VOC, which is lower than several existing methods, suggests that the gains observed on other datasets may not generalize well. The authors should have included a more thorough analysis of the generalization capabilities of their method, including evaluations on a wider range of datasets and a discussion of the potential limitations of the training data.

### Questions
What is the motivation of the proposed method?
What is the reason of the good performance? I think it is because the large training dataset.

### Soundness
2

### Presentation
2

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
The paper introduces SimZSS, a straightforward yet effective framework for zero-shot semantic segmentation. This framework aims to align vision encoders, which exhibit spatial awareness, with textual descriptions. SimZSS leverages text concept representations to extract corresponding visual representations based on similarity metrics. It ensures cross-modality consistency by employing different objectives at the sample and concept levels. Notably, the method requires minimal hyperparameters and does not rely on the supervision of semantic masks. Additionally, SimZSS can be easily adapted to various backbones and datasets. Overall, the method achieves state-of-the-art results across standard zero-shot segmentation benchmarks.

### Strengths
1. The paper is easy to understand and follow.
2. The method is straightforward, easy to implement, and can be readily adapted to various backbones and training datasets.
3. The method can be trained without the supervision of semantic masks, reducing the burden of annotations.
4. The motivation for proposing a concept-level objective is clear and more suitable compared to a contrastive objective in scenarios where concepts encode individual objects that are likely to occur multiple times within a batch.

### Weaknesses
1. It is unclear how the final segmentation masks are generated during inference. Is there a similarity threshold used to determine the class names to which visual tokens belong? If so, how does the performance vary with different threshold settings? Specifically, the paper lacks a detailed explanation of the post-processing steps applied to the similarity scores to obtain the final segmentation mask. The method relies on a similarity metric between visual tokens and text embeddings, but the process of converting these similarities into a pixel-wise segmentation is not fully elaborated. For instance, it's not clear if a simple argmax is applied or if more complex techniques like thresholding or smoothing are used. The absence of this information makes it difficult to reproduce the results and assess the robustness of the method.
2. There is a lack of analysis explaining why SimZSS outperforms other zero-shot semantic segmentation methods. The paper presents results showing that SimZSS achieves state-of-the-art performance, but it does not provide a thorough analysis of the underlying reasons for this improvement. It would be beneficial to include an ablation study that examines the contribution of different components of the framework, such as the concept-level objective or the specific similarity metric used. Furthermore, a comparison with other methods that focuses on the qualitative differences in the segmentation masks would also be valuable. Without this analysis, it is hard to understand the specific advantages of SimZSS over existing approaches.

### Questions
1. Since the visual encoder is frozen, the quality of the segmentation masks heavily depends on the encoder's ability to recognize spatial positions. Would the performance improve if the visual encoder were fully or partially fine-tuned?
2. In an extreme scenario, how significantly would the test performance be affected if the class names in the training set and test set are entirely different?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces SimZSS, a simple framework that enables open-vocabulary zero-shot segmentation by leveraging pretrained vision-only models within a vision-language contrastive learning paradigm. Addressing the challenge of poor localization in dense tasks, SimZSS decouples visual representation learning from cross-modality alignment by utilizing frozen, spatially aware vision models like DINOv2 and focusing on training only the text encoder. The framework identifies local concepts within captions using linguistic cues and aligns them with corresponding visual concepts in images through similarity-based pooling.

### Strengths
- The paper is well-written and easy to follow. The authors provide clear explanations of their methodology. I would like to highlight the quality of the figures and tables in a visually pleasing way that enhances the understanding of the content.

- While the problem of localization in vision-language models is not novel, the proposed approach offers a novel perspective. By freezing the vision backbone and only training the text encoder, the authors leverage pretrained self-supervised models effectively, resulting in efficient training.

- The method demonstrates state-of-the-art performance on multiple zero-shot segmentation benchmarks.

### Weaknesses
1. It is surprising that the main paper lacks essential details about the training data and the pretrained models used. Given that the paper is only 9 pages (below the 10-page limit), including this information in the main text is necessary.

2. 
(a) One major limitation is the use of a predefined concept bamk. The authors claim that it does not impact the breadth of the concept the model can localize(sec. 4.4). However, in Table 4, removing PascalVOC classes from the concept bank decreases the performance. Therefore, it seems that the breath of the concept bank is a crucial component. Also, the authors could evaluate on datasets with much diverse set of concepts e.g. OpenImagesV7 (which covers more than 5000 classes), this way the breadth of the vocabulary learned by the model can effectively be assessed. 

(b) Moreover, to identify the recognition capabilities of the trained model, I would expect the authors to evaluate the performance of more classification datasets than just ImageNet. More specifically, it is common practice I think to evaluate on the set of 38 classification datasets (https://github.com/LAION-AI/CLIP_benchmark). Also, table 3 should include the performance of at least the OpenCLIP-ViT/16 trained on LAION-400M as the training dataset is the same, whose zero-shot accuracy on ImageNet is 67.05 vs 64.1 for your ViT-B/14 which indicates that your method hurts the overall recognition capability of the final model. This tradeoff between localization and recognition should be discussed in the paper.

(c)  Since the concept bank is derived from the union of class names from the segmentation datasets used for evaluation, the framework may be biased towards these classes. This design choice limits the model's ability to generalize to a truly open vocabulary, as it may not effectively localize concepts outside the predefined bank.

3. The paper misses important related work, particularly training-free approaches that tackle poor localization in VLMs from a different angle. For instance, methods like [a][b][c][d] achieve competitive performance without requiring additional training and can detect concepts not covered by a predefined concept bank. Including comparisons with such methods would provide a more comprehensive evaluation.

### Questions
- Given that the predefined concept bank seems to impact performance, how does the model perform on datasets with a much broader set of concepts, such as OpenImagesV7, which covers over 5000 classes? Has the model been evaluated on classes outside of the concept bank, and if so, what are the results?

- Have you evaluated the recognition capabilities of the trained model on other classification datasets beyond ImageNet? Including evaluations on a wider range of datasets could provide deeper insights into how the method affects recognition performance.

-  How does your model compare with training-free approaches?

- Could you discuss the potential trade-off between improved localization and any degradation in recognition performance? Understanding this trade-off would help assess the overall impact of your method on different tasks.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The work proposed SimZSS, a simple and efficient framework for open-vocabulary zero-shot semantic segmentation. The work builds on top of a frozen pre-trained vision-only model and aligns a text encoder to achieve cross-modality concept-level alignment. Despite its simplicity, SimZSS achieves state-of-the-art results on seven out of eight benchmarks.

### Strengths
- The authors propose a simple yet effective approach for the task that exploits pre-trained vision models.
- The method is both data- and compute-efficient, as it does not require long training periods and needs captioned images for training.
- The method achieves state-of-the-art results on seven benchmark datasets.
- The method takes inspiration from LiT and extends it for the segmentation task while maintaining its classification capabilities.

### Weaknesses
 - The work relies on a bank of pre-defined concepts to pre-process the captions and extract concepts to segment, which may represent a limitation in some situations. For example, the concept bank may not cover the diversity of potential objects in the image, especially in complex scenes or when dealing with fine-grained categories. This reliance on a static concept bank could limit the method's ability to generalize to novel or rare objects not included in the bank.
- While performance is competitive when using ViT-B, scaling the model backbone to a ViT-L model does not improve performance. This suggests a potential bottleneck in the architecture or training procedure that prevents the method from fully leveraging the increased capacity of larger models. The lack of performance gain with a larger model raises questions about the scalability of the approach and its potential for further improvement.

### Questions
- What are the current limitations of the concept bank used? Would a larger bank lead to better generalization? What are the complexities in scaling the concept bank to, e.g., WordNet or other taxonomies?
- As mining concepts from the captions provide promising results, I wonder how well the approach would work on more noisy captions, e.g., from web-scale datasets. How sensitive is SimZSS to such noise? Are there any techniques that could be employed to improve the robustness of the generation of the concept bank?

### Soundness
3

### Presentation
3

### Contribution
3

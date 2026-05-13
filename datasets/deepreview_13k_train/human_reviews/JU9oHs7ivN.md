# Cyclic Contrastive Knowledge Transfer for Open-Vocabulary Object Detection

- Decision: Accept
- Scores: 8, 5, 6, 5, 6

## Abstract
In pursuit of detecting unstinted objects that extend beyond predefined categories, prior arts of open-vocabulary object detection (OVD) typically resort to pretrained vision-language models (VLMs) for base-to-novel category generalization. However, to mitigate the misalignment between upstream image-text pretraining and downstream region-level perception, additional supervisions are indispensable, e.g., image-text pairs or pseudo annotations generated via self-training strategies. In this work, we propose CCKT-Det trained without any extra supervision. The proposed framework constructs a cyclic and dynamic knowledge transfer from language queries and visual region features extracted from VLMs, which forces the detector to closely align with the visual-semantic space of VLMs. Specifically, 1) we prefilter and inject semantic priors to guide the learning of queries, and 2) introduce a regional contrastive loss to improve the awareness of queries on novel objects. CCKT-Det can consistently improve performance as the scale of VLMs increases, all while requiring the detector at a moderate level of computation overhead. Comprehensive experimental results demonstrate that our method achieves performance gain of +2.9% and +10.2% AP_{50} over previous state-of-the-arts on the challenging COCO benchmark, both without and with a stronger teacher model.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces CCKT-Det++, an open-vocabulary object detection framework designed to detect novel object categories without relying on extensive additional supervision. The approach leverages semantic priors as guidance and a regional contrastive knowledge distillation loss to improve the model's detection capability for novel classes. CCKT-Det++ utilizes visual-semantic embeddings from both VLMs and MLLMs to dynamically transfer knowledge from both image and text encoders, aligning the detector’s latent space with meaningful, structured knowledge.

### Strengths
This work is easy to follow. Most of the used techniques are correct.

### Weaknesses
1. While CCKT-Det++ performs well by leveraging stronger teacher models, it is heavily reliant on the quality and alignment of these teacher models. If the teacher model has limitations or biases, these could propagate to CCKT-Det++, affecting performance and potentially introducing unintended biases. Specifically, the reliance on visual-semantic embeddings from VLMs and MLLMs means that any biases present in their training data, such as skewed representations of certain object categories or contextual associations, could be inherited by the detector, leading to skewed detection performance.

2. Although the student model maintains moderate parameters, using stronger teacher models during training and inference can introduce significant computational costs. Scaling the teacher models effectively requires access to substantial computational resources, which could limit practical applications for researchers without high-performance infrastructure. The computational overhead is not just during training but also during inference, as the teacher model's features are needed to guide the student model's predictions. This dual computational demand could make real-time or resource-constrained deployments challenging.

3. The approach relies on pseudo annotations, which are less accurate than human annotations. If the pseudo labels are of low quality, they could introduce noise into the training process, possibly harming model performance on more challenging or nuanced object classes. The quality of these pseudo labels is crucial, and any inaccuracies or inconsistencies could lead to the student model learning incorrect associations or failing to generalize to unseen examples. The lack of a robust mechanism to filter out noisy pseudo labels could further exacerbate this issue.

4. While semantic priors improve performance on novel objects, there is a risk that the model might over-rely on these priors, leading to reduced flexibility in identifying objects that fall outside its learned semantic scope. This dependency may affect its generalization to truly unseen classes in new environments. The model's ability to adapt to novel objects that do not align with the semantic priors could be limited, hindering its performance in real-world scenarios where objects may not always conform to predefined semantic categories.

5. The method heavily relies on CLIP for both semantic priors and feature extraction, making it vulnerable to limitations inherent in the CLIP model. For instance, CLIP's biases in language and visual associations could impact detection accuracy and lead to incorrect classifications in culturally or contextually sensitive settings. The reliance on a single model for multiple aspects of the pipeline introduces a single point of failure, and any limitations or biases in CLIP could have cascading effects on the overall performance of CCKT-Det++.

### Questions
Most concerns are listed on above boxes. Hungarian matching based on CLIP embeddings is central to your contrastive knowledge transfer scheme, aligning regional embeddings with the teacher’s visual-semantic space. However, given that CLIP embeddings may not fully capture object-specific regional nuances, why would this Hungarian matching approach be expected to significantly improve performance?

### Soundness
3

### Presentation
3

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
In order to solve the problem of relying on a large amount of additional data for open vocabulary object detection, the authors propose CCKT-Det method. This method guides the learning of queries by pre-filtering and injecting semantic priors, and introduces regional contrast loss to improve the perception of queries to novel objects.

### Strengths
1. The frameworks are explicit and effectively illustrates the idea of the method.
2. This method has an improvement in the detection performance of novel classes.

### Weaknesses
1. The problem of the authors to solve and the motivation are both ambiguous. The authors point out that some methods rely on a large amount of extra caption data, but many methods can achieve high performance without it, such as the quoted OV-DQUO. It is unclear why existing methods that do not rely on extra caption data are insufficient, and what specific limitations the proposed method aims to address beyond simply avoiding extra data. The motivation needs to be more clearly defined in terms of specific performance bottlenecks or limitations of current state-of-the-art open vocabulary detection methods.
2. The authors introduce semantic prior, but do not clearly define the concept. The term 'semantic prior' is used without a precise definition, making it difficult to understand its role and contribution. It is not clear how this prior is derived, what information it encodes, and how it is distinct from other forms of contextual information used in similar methods. The lack of a formal definition hinders the understanding of the method's core mechanism.
3. Figure 3 shows that the semantic prior needs to go through the VLM's text encoder, what is the difference between the semantic prior and the caption? And what is the difference between semantic priors and the prompts that currently popular? Neither of these issues is addressed by the authors. The process of encoding the semantic prior through a text encoder raises questions about its novelty and differentiation from existing text-based approaches. The relationship between the semantic prior and standard text prompts or image captions needs to be clarified, including whether it introduces new information or simply reprocesses existing data. The authors should explain the unique aspects of their approach compared to using captions or prompts directly.
4. The authors do not present the detection performance of the base class in the experiment. The absence of base class performance makes it difficult to assess the overall effectiveness of the proposed method. It is important to understand how the method impacts the performance on both base and novel classes to evaluate its practical utility. Without this information, it is hard to determine if the method achieves a good balance between performance on known and unknown categories, or if it sacrifices performance on base classes to improve novel class detection.

### Questions
1. Clearly state the motivation for this paper.
2. It is necessary to give a clear definition of semantic prior and explain its difference from caption and prompts.
3. Please explain why the performance of the base class is not shown in the experiment.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents CCKT-Det, a method for open-vocabulary object detection (OVD) that eliminates the need for extra supervision like image-text pairs or pseudo-labels. It leverages cyclic and dynamic knowledge transfer between language queries and visual region features from pretrained vision-language models (VLMs). The approach uses semantic priors for guiding query learning and a regional contrastive loss to enhance detection of novel objects. CCKT-Det achieves significant performance gains on the COCO benchmark, showing scalability with stronger VLMs while maintaining moderate computational requirements.

### Strengths
1. The proposed method is quite reasonable and can effectively transfer the visual and language capabilities of VLMs.
2. The experiments on the OV-COCO benchmark are relatively comprehensive, showing a significant improvement in detecting novel categories.
3. The ablation experiments are relatively thorough and comprehensive.

### Weaknesses
1. The introduction to the task setup is limited, and there is a lack of a focused, clear description and visualization of the workflow details of CCKT-Det during training and testing. Figure 2 is somewhat confusing.
2. The AP performance of CCKT-Det on the OV-COCO benchmark is relatively poor, and its detection capability on base categories is not as strong as other methods. This may be the cost of improving detection capabilities for novel categories.
3. The experimental results did not report the AP for the base category.
4. There is no comparison or analysis of time complexity.

### Questions
1. Why does the Regional-Contrastive Loss in the ablation study cause drop of AP50 (from 32.6 to 31.7)?
2. There are relatively few comparative methods on the OV-LVIS benchmark.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces CCKT-Det, a novel framework for open-vocabulary object detection (OVD) that operates without any additional supervision beyond the base training set. The method leverages semantic priors and regional contrastive knowledge distillation to align the detector with the visual-semantic space of vision-language models (VLMs).  This paper presents semantic priors to boost the detector's capacity for novel object recognition and a unique loss function that heightens the detector's sensitivity to new objects by aligning region-level features. Based on these contributions, this work achieves start-of-the-art results on COCO benchmark.

### Strengths
* The paper introduces a novel framework, CCKT-Det, for open-vocabulary object detection (OVD) that does not rely on any additional supervision beyond the base training set and achieves start-of-the-results on the COCO benchmark.
﻿
* Comprehensive experiments are conducted on multiple benchmarks (OV-COCO, LVIS, Objects365), demonstrating the method's effectiveness. The results show consistent performance improvements as the strength of the teacher model increases.  The paper includes thorough ablation studies to validate the effectiveness of each component of the proposed method.

* The paper demonstrates that high-performance OVD can be achieved without the need for additional supervision, such as image-text pairs or pseudo annotations. This is a significant advancement, especially in scenarios where such data may not be readily available.

### Weaknesses
 * It is better to add a more detailed result comparison in Tab.1 and Tab.2. For example, show the AP_Base result for COCO and AP_c and AP_f results for LVIS.
* This method has shown promising results in detecting novel objects, but it seems not very good for detecting base objects.

### Questions
None

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces Cyclic Contrastive Knowledge Transfer for Open-Vocabulary Object Detection (CCKT-Det), a method designed to enhance the detection of novel objects in open-vocabulary settings without relying on additional supervision like image-text pairs or pseudo annotations. It leverages pretrained vision-language models (VLMs) to transfer knowledge effectively from base categories to novel ones. The key contributions include using semantic priors to guide object queries and a regional contrastive knowledge distillation mechanism to align the visual features between a student and teacher model. CCKT-Det achieves state-of-the-art performance on COCO and LVIS benchmarks, improving novel object detection without extra data, and scales efficiently with stronger VLMs while maintaining moderate computational overhead.

### Strengths
The paper is well-structured, with solid methodological rigor. The authors present comprehensive experiments and ablation studies that demonstrate the effectiveness of their proposed method. The proposed CCKT-Det framework has high significance in advancing the state of open-vocabulary object detection. By eliminating the need for additional supervision and showing competitive performance with existing methods that do require extra data, the paper addresses a key limitation in the field.

### Weaknesses
- Although you claim and emphasized CCKT-Det did not rely on the extra data, in contrary to the previous method, you use the extra MLLM to be a discriminator and generate the prior semantic guidance.

- In the paper, you mention, “In contrast to previous works, where object queries are static and fixed for each image after training, we dynamically inject text embeddings {ti} as semantic priors into object queries to form the language queries for each image.” However, similar ideas have been explored in earlier works, such as GroundingDINO. It would be appropriate to supplement your references by citing these related works and discuss their similarities and differences.
- In Table 4, the paper states that “While semantic guidance demonstrates effectiveness to a degree, its efficacy is constrained in the absence of regional contrastive training.” However, contrary to this claim, regional contrastive appears to have a detrimental effect on semantic guidance, as the ablation experiment did not demonstrate any significant effectiveness of regional contrastive training. This seems to contradict the statement in the paper, “As indicated in the third row of Table 4, the absence of this loss results in a performance decline of 5.4% AP50 on novel classes.” Based on the results, there appears to be no significant relationship between Regional-Contrastive Loss and Semantic Guiding, while it works in conjunction with Similarity Classification. This seems to be a clerical error.

### Questions
- In the paper, you mention, “In contrast to previous works, where object queries are static and fixed for each image after training, we dynamically inject text embeddings {ti} as semantic priors into object queries to form the language queries for each image.” However, similar ideas have been explored in earlier works, such as GroundingDINO. It would be appropriate to supplement your references by citing these related works and discuss their similarities and differences.
- In Table 4, the paper states that “While semantic guidance demonstrates effectiveness to a degree, its efficacy is constrained in the absence of regional contrastive training.” However, contrary to this claim, regional contrastive appears to have a detrimental effect on semantic guidance, as the ablation experiment did not demonstrate any significant effectiveness of regional contrastive training. This seems to contradict the statement in the paper, “As indicated in the third row of Table 4, the absence of this loss results in a performance decline of 5.4% AP50 on novel classes.” Based on the results, there appears to be no significant relationship between Regional-Contrastive Loss and Semantic Guiding, while it works in conjunction with Similarity Classification. This seems to be a clerical error.

### Soundness
2

### Presentation
3

### Contribution
3

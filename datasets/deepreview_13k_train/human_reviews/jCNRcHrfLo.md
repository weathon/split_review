# Hierarchical Prompts with Context-aware Calibration for Open-Vocabulary Object Detection

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Open Vocabulary Object Detection (OVD) aims to extend to novel classes solely through text descriptions, by learning the mapping between images and text from the base class. However, current methods focus on establishing connections between the visual regions of the target objects and their corresponding category names to learn prompts, ignoring richer contextual information and shared knowledge about these categories, which can easily lead to overfitting on known base categories and exhibit poor generalization to novel classes. To address the above problems, we propose Hierarchical prompts with Context-Aware calibration (HiCA) for open-vocabulary object detection, which integrates high-level semantic and contextual information into the detector from both linguistic and visual perspectives.
Hierarchical prompts effectively map regions with superior-level semantics, which encompasses shared knowledge of both base and novel classes, thereby enhancing the model's generalization ability to novel classes. Context-aware calibration utilizes the visual context of the image to establish the correlation between contextual information and categories, thereby minimizing the adverse effects of the background and enhancing generalization to novel classes. Extensive experiments demonstrate that the hierarchical prompts with context-aware calibration can effectively improve the performance of the open vocabulary detection methods. Especially on the OV-COCO, we achieve 57.2%  base class mAP, surpassing the current state-of-the-art by 2.4% while achieving the best overall mAP.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes two modules to enhance the standard Faster R-CNN-based paradigm for open-vocabulary object detection. The first motivated by the limited semantic representation of category names in textual form, and it calibrates the original textual features with those derived from superclass features. The second one leverages visual context information from images, encode context features by a visual encoder and then used to further refine the text embeddings. Experiments on OV-COCO and OV-LVIS demonstrate a measurable improvement.

### Strengths
1. The paper is easy to follow and well organized.  The figures are drawn well. 
2.  The two modules are well-motivated.  Utilizing the superclass along with the category intuitively polishes and enriches the textual representation of each class.  The contextual feature also plays a critical role in detection, which is usually neglected but could potentially build the relation graph between novel and base categories and bring more improvements. 
3.  The experiments follow the typical setting of open-vocabulary object detection, and the ablation study presents the effectiveness of each module.

### Weaknesses
Despite the well-established motivation of this paper, it contains several weaknesses in my consideration.

1. Enriching textual description of the categories beyond a single word name is not a novel idea. Some previous work like [R1] has proved the effectiveness of it. Instead of improving the textual description, the paper involves another module to calibrate the original textual feature for classification. This enrolls more computation overhead and is less elegant than directly finetuning the existing textual encoder. Specifically, the calibration module introduces additional parameters and computations, which might not be necessary if the textual embeddings were directly improved. The paper does not provide a clear justification for why this additional module is preferred over a more direct approach to refining the textual embeddings, especially considering the computational cost.
2. Compared to methods that utilize enriched information from large language models (LLMs), the use of superclasses from a word tree offers limited enhancement to the textual features, providing only modest complementary information. This limitation is evident in the ablation results shown in Table 3. The superclass information, while providing some high-level context, lacks the rich semantic details that LLMs can generate. This results in a relatively small performance gain, suggesting that the superclass information is not sufficiently discriminative for open-vocabulary object detection. The paper could benefit from a more thorough analysis of the limitations of using a word tree compared to more sophisticated methods of semantic enrichment.
3. Especially, for open-vobulary detection, the critical metric is AP-novel, not AP-base or AP-all, since the core concern is the model’s generalization capability. In the experiments, both modules show only limited improvements in this essential metric. The paper should focus more on optimizing and evaluating the performance on novel classes, as this is the primary challenge in open-vocabulary detection. The limited improvement in AP-novel suggests that the proposed modules, while beneficial, do not fully address the generalization issue, and further investigation is needed to enhance the model's ability to detect novel objects effectively.

### Questions
I have no additional questions confusing me but the concerns listed in the weakness section.

### Soundness
3

### Presentation
3

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
The paper proposes a novel method, Hierarchical prompts with Context-Aware Calibration (HiCA), for open vocabulary object detection that integrates both linguistic and visual contextual information to improve generalization to novel classes. The approach achieves good results on the existing COCO and LVIS benchmark.

### Strengths
1. The method of combining superclass and class to form hierarchical prompts is interesting.
2. The method enhances the performance of the OADP model on both COCO and LVIS datasets.

### Weaknesses
1. I was wondering that the focus of the hierarchical prompts proposed by the author may be inconsistent with the main goal of open vocabulary object detection. Specifically, according to references [1, 2, 3], the primary goal of open vocabulary object detection is to enhance the generalization ability to novel classes while maintaining detection performance for base classes.  Although the author mentions in the abstract that “Hierarchical prompts enhance the model’s generalization ability to novel classes,” the ablation study highlights its effectiveness for base classes with a 5.8% boost, while novel classes see only a marginal 0.1% increase over the baseline. This raises concerns about whether the proposed hierarchical prompts are truly addressing the core challenge of open vocabulary detection, which is to improve performance on unseen categories, rather than primarily benefiting known categories.
2. The ablation experiments and visualizations primarily focus on verifying the effectiveness of hierarchical prompts, but they lack a detailed analysis of context-aware calibration, particularly concerning the effectiveness of context clustering, and the DG Layer. The paper does not provide sufficient insight into how the context clustering is performed, what the optimal number of clusters is, and how sensitive the performance is to this parameter. Furthermore, the role and impact of the DG layer are not well-explained, leaving the reader with limited understanding of its contribution to the overall performance.
3. In Section 3.5, the author mentions the proposed modules are plug-and-play flexible modules. However, the paper only provides experimental results integrated with the OADP method. Could the author provide results on other state-of-the-art methods to demonstrate the plug-and-play effectiveness of these modules? The lack of experiments with other methods makes it difficult to assess the true flexibility and general applicability of the proposed modules.
4. Lack of separate experimental analysis on the effectiveness of learnable visual prompts. It is unclear how much the learnable visual prompts contribute to the overall performance, and whether they are truly necessary or if the performance gain is primarily due to the hierarchical prompts and context-aware calibration.

### Questions
1. How is the superclass determined for each category, considering that a category could be associated with multiple levels of superclasses? Furthermore, which level of superclass demonstrates greater effectiveness?
2. Please refer to the weakness section.

### Soundness
3

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
3

### Summary
This paper proposes HiCA, a novel approach for open-vocabulary object detection. In HiCA, Hierarchical prompts leverage coarse-grained superclass knowledge to avoid biasing the model towards base classes, and Context-Aware calibration revises detector results by learning category distribution through environmental context knowledge. Experimental results demonstrate that HiCA consistently outperforms state-of-the-art methods in detecting novel objects.

### Strengths
1. The paper is well-written and easy to understand.
2. The idea of using Hierarchical prompts to capture the shared knowledge between both base and novel classes is interesting and proven.
3. Experimental results show that the proposed method is effective.

### Weaknesses
1. The author claims that Hierarchical prompts can enhance the model's generalization ability for novel classes, but Table 3 shows that its performance improvement for novel classes is small.
2. Although Context-Aware calibration can bring performance improvement, there is a lack of detailed experimental verification of the effectiveness of the motivation. Specifically, the mechanism by which the learned context embeddings influence the final classification scores is not thoroughly explored. It's unclear how much each context contributes and whether some contexts are more important than others.
3. The author claims that Hierarchical prompts and Context-Aware calibration are plug-and-play modules, but no further experimental verification is performed. The paper does not demonstrate the method's adaptability to different detection architectures or datasets, which is crucial for validating the plug-and-play claim.

### Questions
1. In Tables 1 and 2, the performance of the base classes achieves state-of-the-art results, while the novel classes perform poorly. Should we focus more on enhancing the performance of the novel classes?
2. This paper lacks a detailed explanation of how the selected context in Figure 2 is implemented.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a novel approach, Hierarchical Prompts with Context-Aware Calibration (HiCA), to enhance Open Vocabulary Object Detection (OVD). HiCA improves generalization by utilizing hierarchical prompts that map object regions through both coarse- and fine-grained knowledge, capturing shared information across base and novel classes. Additionally, context-aware calibration refines detection by linking contextual information with object categories, reducing background interference.

### Strengths
1. Clear Motivation: The motivation behind the proposed method is intuitive and well-aligned with the goals of Open Vocabulary Detection (OVD), making it easy to follow and logically sound.
2. Comprehensible Diagrams: The diagrams used in the paper are clear and well-illustrated, which aid in understanding the overall architecture and key components of the proposed framework.
3. Extensive Experiments: The paper provides comprehensive experimental evaluations, covering various settings and comparisons, which helps to validate the effectiveness of the proposed method.

### Weaknesses
1. Limited Improvement for Novel Classes: Despite the emphasis on enhancing detection for novel classes in OVD, the improvement shown in Tables 1 and 4 is relatively minor. For instance, in the ablation study, adding hierarchical prompts (HP) increases performance on novel classes by only 0.01, which raises questions about the overall impact of this component for new class detection. It is suggested to add per-class performance breakdowns or error analysis to explain this phenomenon. The reported gains are not only marginal but also inconsistent across different classes, suggesting that the hierarchical prompting mechanism may not be robust or universally beneficial. The lack of substantial improvement, especially given the added complexity, undermines the practical value of the proposed approach for novel class detection.

2. Lack of Quantitative Analysis: The paper claims that the introduction of superclasses improves differentiation between visually similar classes. However, the paper lacks quantitative analysis or clear evidence to support this claim. It would benefit from an in-depth exploration of cases (e.g., a confusion matrix analysis or a comparison of specific cases) where superclasses improve detection performance and an explanation of the mechanisms by which HiCA differentiates similar classes more effectively. The absence of a rigorous analysis makes it difficult to ascertain whether the observed improvements are statistically significant or merely due to chance. Furthermore, without quantitative evidence, the claim about improved differentiation remains speculative.

3. Concern of Prompt Design: According to Table 4, most modifications do not outperform simpler, template-based methods for novel classes. This raises concerns about the practicality of the proposed approach for novel class detection. Considering the limited improvement, a more detailed discussion of the scenarios where the method might be preferable would be helpful. The fact that simpler methods perform comparably or even better questions the necessity of the proposed hierarchical prompting approach. The paper needs to clarify the specific conditions or scenarios where the proposed method offers a clear advantage over simpler alternatives.

### Questions
1. Impact of Knowledge Granularity: Does the granularity level of knowledge (i.e., fine-grained versus coarse-grained superclass distinctions) affect the model's performance? More insights on the optimal level of superclass granularity would be valuable.
2. Generalizability of Handcrafted Superclasses: Hand-designed superclasses could impact the method's adaptability in real-world applications. If a new superclass emerges, does the model need fine-tuning again? Additionally, how does HiCA handle ambiguous cases that do not fit well into existing superclasses? It is suggested that the paper could provide examples to illustrate how HiCA would work in such situations or how HiCA could be adjusted.

### Soundness
3

### Presentation
3

### Contribution
2

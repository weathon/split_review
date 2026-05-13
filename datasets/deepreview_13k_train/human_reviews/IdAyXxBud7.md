# DynAlign: Unsupervised Dynamic Taxonomy Alignment for Cross-Domain Segmentation

- Decision: Accept
- Scores: 8, 6, 6, 6, 6, 6

## Abstract
Current unsupervised domain adaptation (UDA) methods for semantic segmentation typically assume identical class labels between the source and target domains. This assumption ignores the label-level domain gap, which is common in real-world scenarios, and limits their ability to identify finer-grained or novel categories without requiring extensive manual annotation.
A promising direction to address this limitation lies in recent advancements in foundation models, which exhibit strong generalization abilities due to their rich prior knowledge. However, these models often struggle with domain-specific nuances and underrepresented fine-grained categories.
To address these challenges, we introduce DynAlign, a two-stage framework that integrates UDA with foundation models to bridge both the image-level and label-level domain gaps. Our approach leverages prior semantic knowledge to align source categories with target categories that can be novel, more fine-grained, or named differently. (e.g., vehicle to car, truck, bus). Foundation models are then employed for precise segmentation and category reassignment. To further enhance accuracy, we propose a knowledge fusion approach that dynamically adapts to varying scene contexts. DynAlign generates accurate predictions in a new target label space without requiring any manual annotations, allowing seamless adaptation to new taxonomies through either model retraining or direct inference.
Experiments on the GTA $\rightarrow$  IDD and GTA$\rightarrow$ Mapillary benchmarks validate the effectiveness of our approach, achieving a significant improvement over existing methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper formulates the problem of unsupervised taxonomy adaptive cross-domain semantic segmentation. To bridge both image-level and label-level domain gaps without supervision, the paper proposes a two-stage approach DynAlign that integrates both domain-specific knowledge and rich open-world prior knowledge from foundation models. Experiments on two street scene semantic segmentation benchmarks validates the effectiveness of the proposed method.

### Strengths
1. The paper writing is good with well formula representation.
2. The unsupervised taxonomy adaptive cross-domain semantic segmentation task is interesting and meaningful.

### Weaknesses
1. In Lines 80-81, the reason why this problem is significant but not be studied needs explain. 
2. Experimental results of existing taxonomy-adaptive domain adaptation and UDA methods also need to be presented in the Table 1 for comparison.  More parametric experiments about the confidence in the Lines 372 - 373 need to be conducted and discussed.

### Questions
1. In Lines 80-81, why this problem is significant but not be studied?  
2. What are experimental results of existing taxonomy-adaptive domain adaptation and UDA  methods on two street scene semantic segmentation benchmarks.  How choose the confidence threshold value in the Lines 372 - 373.

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
This paper propose two-stage framework called DynAlign for unsupervised taxonomy-adaptive cross-domain semantic segmentation. DynAlign leverages prior semantic knowledge to align source categories with target categories that can be novel, more fine-grained, or named differently. Foundation models are then employed for precise segmentation and category reassignment. Knowledge fusion approach is proposed to dynamically adapt to varying scene contexts.

### Strengths
1. The problem that the paper focuses on, taxonomy-adaptive domain adaptation without requiring additional annotations from the target domain, is innovative and interesting.
2. The approach based on the foundation model is explainable, reasonable, and innovative.

### Weaknesses
1. The explanation of the caption in Figure 2 is not clear. Please explain the functions of the two CLIPs in the figure. And the caption introduces "CLIP fusing the visual knowledge from SAM with the semantic knowledge from LLM to reassign accurate labels. The predictions can be used as pseudo-labels to further fine-tune the UDA model". Since the predictions can be used as pseudo-labels to further fine-tune the UDA model, should the second CLIP have an output arrow?  The figure 2 cannot show the process well, which causes some misunderstandings.
2. The paper proposes a two-stage approach. however, three steps are introduced in Figure 2. This makes it difficult to understand the content of figure 2. Please redraw the figure 2 to make the process more intuitive and easy to understand.
3. The proposed method includes many networks and is very complex. Please compare the model's training memory usage, training time, and model parameter.
4. As a new benchmark, will the proposed method publish the complete training and testing code for subsequent follow-up research?
5. In 4.2 SEMANTIC TAXONOMY MAPPING, how is the context description set generated? In formula 2, on which dimension is the average operation performed?
6. The symbol usage is inconsistent. In 4.4 KNOWLEDGE FUSION, the multi-scale visual feature is F_V, while the multi-scale visual feature in Figure 3 is F_g. Please check the symbols and charts in the full text to avoid ambiguity.
7. In Figure 3, what does lane-marking 0.6 mean?
8. In 5.4 ABLATION STUDIES, should multi-scale vision feature be changed to multi-scale visual feature? Please keep the name consistent in the paper.
9. Please add more experimental details. For example, the proposed method uses the CLIP backbone, but is it the CLIP ViT-B-16 or CLIP ViT-L-14 backbone or something else?

### Questions
If the rebuttal process can explain the above problems and confusions, I will increase my score.

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the label-space domain gap within cross-domain semantic segmentation by proposing a novel framework that integrates traditional unsupervised domain adaptation (UDA) methods with foundational models such as large language models, vision-language models, and vision foundation models. Specifically, the large language model is utilized to reason and establish mappings between source and target label spaces. Using these mappings, predictions from unsupervised adaptation segmentation models are transformed into the target label space and subsequently fused with predictions from foundation models, including SAM and CLIP. The proposed framework demonstrates superior performance compared to several open-vocabulary recognition models.

### Strengths
1. The proposed framework is technically sound.
2. The paper addresses a practical and significant issue: the label-space domain gap within domain adaptation.

### Weaknesses
1. High Complexity and Heuristic Dependence
The framework’s complexity, along with its reliance on various heuristics, may hinder practical usability. Additionally, some heuristics lack clear specifications, making reproduction challenging. Key points include:

a) Inference Complexity: The framework requires inference from at least three models (UDA model, SAM, and CLIP), contributing to increased computational demands and overall complexity.

b) Semantic Taxonomy Mapping: The framework initially prompts GPT-4 for potential taxonomy mappings, refined through human input. This process adds a human burden due to prompt tuning and taxonomy refinement and is only briefly outlined in the supplementary material (lines 916 & 947), lacking comprehensive detail.

c) Criteria for Label Ambiguity: The paper states, “For labels without ambiguity, e.g., sky, we only use the original label for text feature extraction” (lines 1000-1001). The criteria for “ambiguity” remain unclear, introducing additional heuristics or human intervention.

2. Limited Experimental Scope
While the paper showcases superior performance in certain settings, the experimental scope and choice of baselines are somewhat limited. Expanding the evaluation would strengthen the framework’s claim of superiority:

a) Additional Baselines with Foundation Models: Numerous studies have leveraged foundation models for semantic segmentation, yet many of these are omitted in the experimental section. Including models such as [A] for domain-generalized segmentation and [B] for open-vocabulary segmentation would enhance comparability.

b) Traditional Domain Adaptation Settings: Although the framework targets handling substantial label-space domain gaps for real-world applications, demonstrating its efficacy in traditional domain adaptation settings (e.g., GTA5 to Cityscapes, with a smaller label-space gap) is also important.

c) Other Label-Space Domain Gaps: The experiments primarily focus on scenarios where the target domain includes more semantic classes than the source (e.g., 45 classes for Mapillary, 24 for IDD, and 19 for GTA). Evaluating scenarios with fewer classes in the target domain (e.g., Mapillary to Cityscapes) would substantiate the framework’s generalizability.

### Questions
The framework seems to rely purely on SAM for pixel grouping, with UDA and CLIP then reclassifying each mask region. Is this my understanding accurate?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper targets the label-level domain gap, which is common in real-world scenarios.  The authors introduce DynAlign, a
two-stage framework that integrates UDA with foundation models to bridge both the image-level and label-level domain gaps. DynAlign leverages prior semantic knowledge to align source categories with target categories that can be novel, more fine-grained, or named differently (e.g., ‘vehicle’ to {‘car’, ‘truck’, ‘bus’}). Foundation models are then employed for precise segmentation and category reassignment. To further enhance accuracy, the authors propose a knowledge fusion approach that dynamically adapts to varying scene contexts. DynAlign generates accurate predictions in a new target label space without requiring any manual annotations.

### Strengths
1. The problem in this paper is of great practical significance.

2. The writing of this paper is clear and well-organized.

3. The experimental results showed some improvements when using such technology, compared with previous rivals.

### Weaknesses
1. The article only explores coarse-to-fine experiments. In real-world scenarios, however, the label structure of the target domain may sometimes be coarser than that of the source domain. How would the proposed method be adapted for such a setting? Additionally, the effectiveness of the method under these conditions has not been verified.

2. The contribution towards DG area is limited. The generalization achieved by the methods in this paper primarily derives from the pre-trained models—specifically, SAM's generalization in segmentation and CLIP's generalization in multimodal alignment—rather than from the techniques introduced within the paper itself. As a result, this work mainly resembles a mapping technique that aligns open-vocabulary labels between the source and target domains, an idea that has been explored extensively in other studies. Consequently, I do not view this paper as making a significant contribution to the field of domain generalization. In my opinion, as an ICLR article, it still needs a certain theoretical depth.

Minor issues:
Some papers are cited repeatedly in the reference, such as "Domain aligned clip for few-shot classification." and "Scaling open-vocabulary image segmentation with image-level labels."

### Questions
Please see the "Weaknesses" part.

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents  a two-stage framework that integrates UDA with foundation models to bridge both the image-level and label-level domain gaps. It consists of multiple modules including conventional UDA to bridge the distribution gap between source and target, vision foundation model to extract general segmentation, LLM to construct the label taxonomy, and CLIP to align visual and text features to generate well-aligned pseudo labels for self-training.

### Strengths
Belows are strong points that this paper has:

1. Well-written and systematically organized to make the reader to understand more easily. 

2. It proposes reasonable fusion strategy between UDA and Foundation model to resolve the distribution and label shift issue  in cross-domain scenario

3. It achieves remarkable performance improvement, showing the effectiveness of the proposed method on two benchmark.

4. Figure 4 shows that training with generated pseudo labels can not only achieve better score but also increase the inference efficiency.

### Weaknesses
Belows are weak points that this paper has:

1. In order to align with line 112 ("integrating with any UDA-based semantic segmentation models"), it would be better that author provide another examples to show the compatibility of the proposed method (e.g., MIC + DynAlign, or other UDA model + DynAlign)

2. Need to have more analysis on how robust the proposed knowledge fusion is. One way to do is that using different foundation model (e.g., MobileSAM for SAM, Llama for GPT-4,  another VLM for CLIP) can also work with the proposed method. Showing this compatibility can provide more flexible fusion environment.

3. Any failure case while fusing UDA and foundation model?

### Questions
Please see above Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
Traditional UDA methods for semantic segmentation often assume identical class labels in both source and target domains. To tackle this, this paper presents DynAlign, a two-stage framework that combines UDA with foundation models to address both image-level and label-level domain gaps. It leverages prior semantic knowledge to align source and target categories and uses foundation models for detailed segmentation and category realignment. To boost accuracy further, a knowledge fusion strategy is divised to dynamically adapt to diverse scene contexts.

### Strengths
1. The method design of this paper is straightforward and easy to understand, with sufficient details and reliable techniques.
2. The paper aims to address the label space mismatch issue in UDA tasks, and this research problem is very meaningful.
3. The research motivation of the paper is strong, and the solution is clearly articulated.

### Weaknesses
1. The paper dedicates considerable space to comparisons with open-vocabulary semantic segmentation methods and benchmarks its approach against those used in that task. I understand that this is due to the limitations in label space, which restrict traditional UDA methods. However, since the focus of this paper is UDA, I believe the authors should concentrate on comparisons with UDA methods to better highlight the advantages of this work. Throughout my reading, I found myself constantly switching between the two tasks (UDA and open-vocabulary SS), making it challenging to clearly grasp the contributions of this paper.

2. I understand that earlier methods also utilized foundation models but still required target labels for few-shot training. In contrast, this paper employs foundation models in a fully unsupervised manner, correct? Is this the main difference/contribution this paper has compared to previous methods?

3. How to better utilize foundation models has been a significant research topic in recent years, and I find the authors' exploration of this subject very meaningful. However, with the increasing number of foundation models available, it is insufficient to merely leverage more or better foundation models to complete tasks. The authors should emphasize the specific benefits of their design rather than simply implementing it in an unsupervised manner. Since the inference of large models is inherently unsupervised, simply using them does not constitute a substantial contribution.

4. The use of foundation models still incurs computational resource demands, which can affect the practical applicability of this framework. The experimental section should include comparisons regarding the computational resource consumption of the models, such as memory usage and inference time.

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

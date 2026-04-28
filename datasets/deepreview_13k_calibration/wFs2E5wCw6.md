# Tree of Attributes Prompt Learning for Vision-Language Models

- Decision: Accept
- Avg Score: 6.40
- Scores: 6, 6, 6, 6, 8

## Abstract
Prompt learning has proven effective in adapting vision language models for downstream tasks. However, existing methods usually append learnable prompt tokens solely with the category names to obtain textual features, which fails to fully leverage the rich context indicated in the category name. To address this issue, we propose the Tree of Attributes Prompt learning (TAP), which first instructs LLMs to generate a tree of attributes with a ``concept - attribute - description'' structure for each category, and then learn the hierarchy with vision and text prompt tokens. Unlike existing methods that merely augment category names with a set of unstructured descriptions, our approach essentially distills structured knowledge graphs associated with class names from LLMs. Furthermore, our approach introduces text and vision prompts designed to explicitly learn the corresponding visual attributes, effectively serving as domain experts. Additionally, the general and diverse descriptions generated based on the class names may be wrong or absent in the specific given images. To address this misalignment, we further introduce a vision-conditional pooling module to extract instance-specific text features. Extensive experimental results demonstrate that our approach outperforms state-of-the-art methods on the zero-shot base-to-novel generalization, cross-dataset transfer, as well as few-shot classification across 11 diverse datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
- The paper proposes a new prompt learning approach for vision language models. 
- Instead of a fixed prompt or LLM-generated unstructured prompt, the paper proposes to use a tree of attributes prompt.
- This organizes the generated description as concept, attribute and description structure essentially converting unstructured information from LLMs to structured.
 - A visual conditioning approach is also proposed to ensure optimal image-text alignment and avoid multiple possibilities of the class. 
- The approach is shown to outperform prior work on multiple tasks and datasets.

### Strengths
- The motivation of the paper is strong: a tree of attributes seems logical way to represent information about a class. Pooling module to avoid misalignment is also an interesting idea. 
- The paper is fairly well written and overall idea is easy to follow.
- The experiments and ablations are helpful to understand the effect of the proposed approach.

### Weaknesses
Concerns & questions: 
- Statistical significance: Standard deviations at the least would be helpful to understand if improvements are significant. This is especially important since differences in many results seem minor. 
- How sensitive is the approach to choice of LLM ? 
- Table 4: Authors mention that prior works use unstructured set of descriptions, do the drops from using unstructured descriptions in Table 4 match performance of the cited works L428-429? 
- Authors should make it clear if "example generation" strategy was used by the prior works to create descriptions.  Further, the choice of CLIP model and if it matches prior work should also be described to understand the differences in various approaches. 
- Missing references and comparisons: [a], [b]. It would be a good idea to compare and contrast with these. 

[a] Graph-Based Captioning: Enhancing Visual Descriptions by Interconnecting Region Captions
[b] Learning Hierarchical Prompt with Structured Linguistic Knowledge for Vision-Language Models

### Questions
Please refer to the weaknesses section. 

Minor:
- Some examples for elements of the set in L245 would be helpful

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
This paper proposes the Tree of Attributes Prompt Learning (TAP) framework for enhancing vision-language models (VLMs), especially in zero-shot, cross-dataset, and few-shot tasks. TAP introduces a hierarchical "concept - attribute - description" structure that utilizes large language models (LLMs) to generate a structured knowledge graph for each category, capturing the contextual richness of class names through attributes. This approach also includes vision-conditional pooling to extract instance-specific text features, mitigating misalignment issues between visual and textual data. Experimental results show improved performance over baseline models, highlighting TAP's impact across diverse datasets.

### Strengths
TAP's hierarchical attribute organization is indeed a new attempt to structure the description into a well-defined knowledge graph framework, different from previous unstructured approaches. The method achieves state-of-the-art performance across multiple challenging scenarios on 11 diverse datasets, and innovatively incorporates domain expert tokens and vision-conditional pooling for optimizing image-text alignment.

### Weaknesses
1.The TAP method does present enhancements over VPT and CoOP by organizing attributes hierarchically and introducing a vision-conditional pooling layer. However, to improve TAP’s impact, I suggest that the authors emphasize distinctive innovations beyond architectural refinements. For instance, exploring a novel alignment mechanism that fully utilizes semantic edge information within the constructed attribute trees might further differentiate TAP from its predecessors. Also, they could investigate additional layers of vision-text alignment that capture attribute-specific nuances more dynamically than existing models.

2. Dynamic attribute generation relies on a large language model, and compared with other methods that use a fixed number of attributes, this flexibility is not an innovation in the method itself, but more like an extension of existing technologies.

3. The edges in TAP’s attribute tree offer promising opportunities for capturing semantic relations. However, the paper lacks a detailed explanation of these edges. Clarifying whether they represent specific semantic relationships (e.g., similarities or hierarchies among attributes) could enhance interpretability. I recommend that the authors either expand on how these edges improve semantic alignment or describe potential modifications to strengthen the tree's expressiveness.

4. Section 3.5 briefly mentions the vision-conditional pooling (VCP) layer but does not detail its operation, especially regarding "pooled attribute-level embedding." Providing a step-by-step description of how VCP pools attributes based on visual inputs and clarifying the term could be helpful. Additionally, illustrating VCP's functionality through specific examples might aid readers in understanding its role in enhancing text-image alignment.

### Questions
1. In Section 3.4, the approach combines VPT and CoOP to form an alignment mechanism for visual cues and attribute cues. Did the authors introduce new mechanisms in the combination process or innovate in the way the alignment prompts are generated?

2. In Section 3.5, the authors mentioned that adaptive vision-conditional pooling layer is used to alleviate the misalignment problem of visual and text features, but did not clearly explain the actual role of the pooling layer. How is the pooling layer implemented in VCP? Does it involve specific pooling operations or simple weighted aggregation?

3. In the ablation experiment, the authors claimed that the number of attributes generated dynamically improved performance over the fixed number of attributes, but when compared with other methods, the other methods all used a fixed number of attributes. This gives uneven advantages to the proposed method over baselines. How do authors justify this? Have the authors considered adding control variable experiments to verify the specific impact of dynamic generation on performance improvement?

4.TAP’s dependency on a particular LLM for dynamic attribute generation raises questions about adaptability across different LLMs. I suggest the authors evaluate TAP using alternative LLMs (e.g., GPT-4, PaLM, or Claude) to assess robustness. It would be informative to report on consistency in performance across these models and discuss which metrics best capture the variability introduced by different LLM choices, offering insights into TAP’s adaptability and contribution.

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
5

### Summary
The TAP method structures textual descriptions in a hierarchical “concept-attribute-description” format, effectively creating a knowledge graph from large language models (LLMs) for each category name. This structure allows for a more comprehensive and detailed understanding of the visual content. The paper reimagines learnable prompt tokens as "domain experts," each specializing in different aspects of the image, supplemented by a global perspective provided by the CLS token. To address potential misalignment between general descriptions and specific image content, the paper introduces a vision-conditional pooling module. This module extracts instance-specific text features, ensuring optimal image-text alignment.

### Strengths
The proposed method incorporates structured tree of attribute into prompt tuning that provide richer supervisory information compared to unstructured attribute information. A set of experiments has been conducted, and the results look promising.

### Weaknesses
One major limitation of the method is that it requires human review to "ensure the quality of the example" (L175). Recall that one major advantage of prompt tuning is that it can adapt large models quickly to specific tasks. However, the requirement of human reviewing in the proposed method is not consistent with this goal. In addition, it is not clear how many human efforts are needed here, and how to handle the potential human bias in quality evaluation.

The ToA is built in a dataset-aware manner using specific prior categorical information. This raises an issue regarding the domain generalization performance of the model, which is not studied.

For training details, different learning rates were used for different datasets, however, existing methods typically use a same LR for all datasets. From this point, the comparison is somewhat unfair.

Figure 2 lacks sufficient clarity, for example, input & output streams are not clear. It is a necessity to re-draw it.

### Questions
In Section 3.3, for attribute generation, what type of dataset information is given to the large model?

In Figure 4, each image is accompanied by only two descriptions. Are all images described using two sentences each?

In this paper, it mentions that the method can capture subtle differences between attributes. Could you provide a relevant example?

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
The paper introduces a TAP, a method that first prompts LLM to generate class descriptions in a structured way and then employs both vision and text prompt learning to learn fine-grained attributes within vision-language models.
TAP leverages a hierarchical framework to distill structured knowledge graphs from LLM and employs learnable "domain expert" tokens instead of using a single CLS token to learn class attributes from the description. Additionally, it uses a vision-conditional pooling module to optimize image-text alignment.

The key contribution of this work is: 1) A structured framework for integrating LLM-generated descriptions, 2) learnable vision tokens and a vision-conditional pooling layer for selective description aggregation

### Strengths
Strengths:
1. This paper proposes a structured way to prompt the LLM for detailed class descriptions.
2. This paper proposes a framework leveraging LLM-generated class descriptions to improve the vision language models, and achieves SOTA performance on 11 benchmarks.
3. TAP allows the model to capture both high-level information and fine-grained details from the images, which enhances the model’s performance and interpretability.

### Weaknesses
Weaknesses:
No ablation experiment on how using learnable context tokens impacts the performance.
2.  From Table 1,  most of the improvement comes from the base classes and there is still room for improvement on the novel class.
3. Captions for the tables and figures could be more detailed.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes a novel visual prompt learning approach, which reimagines the visual prompt tokens as “domain experts”, each specializing in different aspects of the image. By leveraging these domain experts, the proposed approach can explicitly learn the corresponding visual attributes. To optimize these prompts, the authors further propose ToA to collect category descriptions based on a cross-category-shared attribute set. In addition, the authors also introduced vision-conditional layers to avoid misaligning images with attributes that do not exist in the corresponding images. The experimental results verified the effectiveness of this approach.

### Strengths
The authors proposed a novel visual prompt learning approach, which can explicitly extract visual features on corresponding visual attributes.

The authors proposed the vision-conditional layer to avoid misaligning images with attributes that do not exist in the corresponding images.

The above two contributions have clear motivations and technically seem to work.

The authors conducted extensive experiments to verify the effectiveness of the proposed approach.

### Weaknesses
The authors claim that TAM is the first work to instruct LLMs to generate a tree of attributes with a “concept - attribute - description” structure for each category. However, existing works “Enhancing CLIP with GPT-4: Harnessing Visual Descriptions as Prompts (ICCV2023W )” and “Democratizing Fine-grained Visual Recognition with Large Language Models (ICLR24)” already proposed the similar corpora and prompt engineering strategies. The authors should discuss these related works in this paper.

In the introduction section, the authors mentioned that some attributes may absent in the input image which necessitate the need for a selective pooling mechanism. However, the proposed vision-conditional layer still pool the most applicable descriptions for each attribute but doesn’t filter out attributes that do not exist in the image.

It seems that this paper was prepared in a hurry. There are some obvious typos, e.g., A\{CLS} in Eq.(7) and Fig. Fig. 1 (b).

In general, in my opinion, this paper doesn't have any major issues; the limitations mentioned above are minor and seem easy to correct in the final version.

### Questions
It would be better if the authors could show the entire attribute set in the appendix.

What is the meaning of ‘contextually relevant’? It is hard for me to clearly understand the meaning of 'context' in this paper.

### Soundness
4

### Presentation
3

### Contribution
4

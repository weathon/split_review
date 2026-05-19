# DenseGrounding: Improving Dense Language-Vision Semantics for Ego-centric 3D Visual Grounding

- Decision: Accept
- Scores: 6, 6, 6, 6, 6

## Abstract
Enabling intelligent agents to comprehend and interact with 3D environments through natural language is crucial for advancing robotics and human-computer interaction. A fundamental task in this field is ego-centric 3D visual grounding, where agents locate target objects in real-world 3D spaces based on verbal descriptions. However, this task faces two significant challenges: (1) loss of fine-grained visual semantics due to sparse fusion of point clouds with ego-centric multi-view images, (2) limited textual semantic context due to arbitrary language descriptions. We propose DenseGrounding, a novel approach designed to address these issues by enhancing both visual and textual semantics. For visual features, we introduce the Hierarchical Scene Semantic Enhancer, which retains dense semantics by capturing fine-grained global scene features and facilitating cross-modal alignment. For text descriptions, we propose a Language Semantic Enhancer that leverage large language models to provide rich context and diverse language descriptions with additional context during model training. Extensive experiments show that DenseGrounding significantly outperforms existing methods in overall accuracy, achieving improvements of **5.81%** and **7.56%** when trained on the comprehensive full training dataset and smaller mini subset, respectively, further advancing the SOTA in ego-centric 3D visual grounding. Our method also achieves **1st place** and receives **Innovation Award** in the 2024 Autonomous Grand Challenge Multi-view 3D Visual Grounding Track, validating its effectiveness and robustness.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces DenseGrounding, designed to address the issues of sparse fine-grained visual semantics and ambiguous language descriptions in ego-centric 3D visual grounding tasks. DenseGrounding includes two main modules: the Hierarchical Scene Semantic Enhancer (HSSE) and the Language Semantic Enhancer (LSE), each focused on enhancing semantics in the visual and language domains, respectively. The HSSE effectively captures fine-grained global semantics and promotes alignment between visual and textual inputs, while the LSE utilizes large language models (LLMs) to enrich language descriptions, increasing semantic richness and reducing inherent ambiguities. DenseGrounding achieves SOTA performance on the EmbodiedScan benchmark and secured first place in the CVPR 2024 Autonomous Driving Grand Challenge Track on Multi-View 3D visual grounding, underscoring its potential for real-world applications.

### Strengths
1. The proposed LSE module applies LLM to enrich text semantics, introducing a novel perspective to this task.
2. The proposed HSSE module effectively preserves fine-grained semantic features by first extracting semantic features from individual views and then broadcasting them across the entire scene, thus addressing the issue of semantic sparsity.
3. The paper provides a clear definition of the novel ego-centric 3D visual grounding task, making it accessible and easy to follow. The design of the method’s modules and the implementation of the ablation studies are also well-explained, allowing readers to easily understand the structure of DenseGrounding and the improvements achieved.
4. The proposed method achieves SOTA performance on the ego-centric 3D visual grounding task and earned first place in the CVPR 2024 Autonomous Driving Grand Challenge Track for multi-view 3D visual grounding, highlighting its potential for real-world applications.

### Weaknesses
1. The proposed method lacks descriptions for certain model details, such as the Multi-scale Fusion and Query Selection components in Figure 2.
2. The paper does not provide a sufficiently clear explanation of how the LLM leverages the SIDB to enrich the semantics of descriptions. For instance, what is the specific format of the location information in the SIDB, and how does the LLM utilize this location information?

### Questions
The proposed model performs excellently on the ego-centric 3D visual grounding task. However, I am curious whether it could also be applied to common 3D visual grounding tasks, such as the ScanRefer benchmark.

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
5

### Summary
This paper aims to address the challenges of loss of fine-grained visual semantics and limited textual semantic context in ego-centric 3D visual grounding. It proposes a hierarchical scene semantic enhancer to enrich visual semantics, while leveraging a large language model (LLM) to enhance context and provide diverse textual semantics. Experimental results demonstrate that the proposed DenseGrounding achieves state-of-the-art results.

### Strengths
- The paper is well-organized and facilitates ease of comprehension.
- The paper introduces an improved baseline, and DenseGrounding achieves a significant performance enhancement.
- The idea of enhancing visual and linguistic features is reasonable; however, there is a potential risk of data leakage (which will be discussed later).

### Weaknesses
- Potential unfair comparisons and prior information leakage. From the ablation study in Table 3, it can be observed that the primary performance improvement of the method derives from the LSE module, which constructs a database and utilizes an LLM for enhancement. However,
    1. The construction of the database may leak crucial dataset priors, as it involves prior knowledge of other contextual objects in the scene and their relationships and localization information, even within the training set. This information should ideally be learned and acquired automatically through ego-centric multiview images.
    2. The database essentially constructs local contextual information between objects, which can significantly enhance the performance of 3D object detection. However, this information is extracted offline and then used as a shortcut to assist DenseGrounding. 
    3. Minor: the use of the LLM introduces additional costs and lacks flexibility.
- The performance improvement of the HSSE module is modest, particularly in hard cases, where it may even have a negative impact.
- The novelty of the HSSE module is somewhat limited, as utilizing multi-scale features and employing vision-language fusion for enhancing visual features are common techniques in the vision-language domain.
- The description of the construction and selection of scene information in the dataset is not sufficiently specific. It is necessary to clarify what types of contextual information are being utilized, such as how each contextual object is defined or how specific objects are selected to consider their relationships.

### Questions
See weaknesses for details.

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
4

### Summary
This paper proposes **DenseGrounding**, an interesting approach aimed at enhancing ego-centric 3D visual grounding with focus on two challenges

- Loss of Fine-Grained Visual Semantic: Sparse fusion of point clouds and multi-view images leads to semantic loss, which can hinder object detection in 3D space.
- Limited Texture Semantics: Ego-centric 3D visual grounding often has sparse or ambiguous language descriptions, which can lead to issues in object localization.

And this paper introduces two components:

- **Hierarchical Scene Semantic Enhancer (HSSE)**: This module enhances visual semantics by incorporating multi-view, scene-level information and facilitating cross-modal (text and visual) alignment.
- **Language Semantic Enhancer (LSE)**: Leveraging large language models (LLMs) with a structured Scene Information Database (SIDB), this component augments language descriptions with more contextually rich, diverse inputs.


They obtained strong results and the experiments are solid.

### Strengths
1. This paper's writing and motivations are both strong.

2. HSSE module for visual enhancement and LSE for text enhancement addresses two crucial limitations and make the proposed algorithm  effective towards real-world ego-centric tasks.

3. This proposed methods achieved competitive results on the EmboidiedScan benchmark.

### Weaknesses
- I am not too surprised to see DenseGrounding shows improved results on EmbodiedScan, a domain-specific dataset. However, the performance drop on the “hard” split in the HSSE ablation suggests limitations in handling complex scenes, raising doubts about whether it genuinely enhances spatial understanding or is just tuned to EmbodiedScan’s data characteristics. Testing on diverse datasets could clarify its robustness.
- Lack of Scaling Analysis: While the paper compares models trained on different data sizes, it lacks a detailed scaling law analysis. Understanding how performance scales with varying data sizes is crucial for practical applications, especially in data-scarce environments. A scaling study would show if DenseGrounding efficiently learns from limited data.
- Dependency on Complete Scene Graphs: The Language Semantic Enhancer (LSE) assumes access to a complete, accurate scene graph, which is rarely available in real-world settings. While using a predicted scene graph could mitigate this, the potential noise and errors in such predictions could degrade performance. Exploring the model’s robustness with imperfect scene graphs would enhance its practical relevance.

### Questions
- Could you evaluate the model on additional benchmarks to assess its generalization, and report on its zero-shot performance?
- Could you provide an analysis of the model’s performance across varying data sizes, compared to the baseline?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, they propose a model for the ego-centric 3Dvisual grounding task where  the model finds a 9DoF 3D bounding box from multiple RGB-D images and a language description for the specified object. Based on the EmbodiedScan, they introduced two modules: Language Semantic Enhancer (LSE) and Hierarchical Scene Semantic Enhancer (HSSE). In LSE, they use the predicted bbox and label and a Scene Information Database (SIDB) for augmenting the input text. HSSE uses view-level semantic aggregation. It is notable that SIDB depends on the annotated dataset (see L. 312) during the construction. They achieved the best results in the EmbodiedScan dataset, although the detailed analyses are limited, compared with those performed in the previous EmbodiedScan paper.

### Strengths
1. Proposing Language Semantic Enhancer (LSE) for the text input augmentation. LSE depends on Scene Information Database (SIDB), which uses the scene annotation.
2. Proposing Hierarchical Scene Semantic Enhancer (HSSE).
3. The best results in the EmbodiedScan dataset although I am not sure the experimental settings are consistent with the existing models.

### Weaknesses
1. It seems that SIDB depends on the annotated dataset as explained in the L.312. Isn’t this cheating in the experiments with the EmbodiedScan dataset because the model can reach rich symbolic textual information? Did you perform some ablation study for this?
2. The model improvement from EmbodiedScan seems incremental: the improvement of 
3. Some experimental settings seem still unclear from the paper. For example, it is not clear whether authors use rendered or real images in EmbodiedScan.
4.  It is also expected that authors explain what are the inputs of the previous models in the main result table of Table 1. For example, ScanRefer depends on the 3D point cloud (pcd) and text. BUTD-DETR uses RGB-D as noted in Table 5 of the EmbodiedScan paper.
5. The experimental setting of ego-centric 3D visual grounding is not fully explained in this paper. For example, it is not clear how they obtain the camera pose, e.g., intrinsic and extrinsic matrices are obtained from the writings of Section 3.1. If models depend on them, it is recommended that authors update manuscripts for explaining the experimental settings.
6. The experiments are limited in the EmbodiedScan dataset. It is also interesting whether this method can be expanded for related datasets and tasks.
7. Limited related studies. It is recommended that authors include a wide branch of 3D visual groundings and question answering tasks.

### Questions
1. Is it possible to construct SIDB without using the dataset annotations? DId you perform ablation for this? 
2. Can you clarify whether you use real or rendered images for the experiments? Also can you provide the ablation study of real vs rendered images as of Table 7 of  EmbodiedScan paper?
3. How do you treat augmentation errors in LSE?
4. Is it possible to report the detailed results, e.g., object category-wise result, as of EmbodiedScan?

### Soundness
3

### Presentation
2

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
This paper introduces a method for ego-centric 3D visual grounding, where agents are able to locate target objects in real-world 3D spaces based on verbal descriptions. The main goal of this paper is to address two critical challenges: 1. how to enhance the fine-grained visual semantics by improving the sparse fusion between ego-centric multi-view images, and 2. how to improve the textual semantic context in arbitrary language descriptions. To tackle these issues, the authors first introduce the Hierarchical Scene Semantic Enhancer, which effectively captures fine-grained scene-level global semantics. Secondly, they introduce the Language Semantic Enhancer, which uses LLM-assisted description augmentation to enhance natural language descriptions. The method presented in this paper achieves the SOTA result on the EmbodiedScan benchmark, demonstrating its effectiveness.

### Strengths
1. The motivation is clear, the improvement is substantial, and the paper is easy to follow.
2. They enhance the language description quality on EmbodiedScan. By releasing the improved annotations, they can benefit future projects.

### Weaknesses
1. Section 4.2, 'Prompt for LLM-based Enhancement,' lacks implementation details, such as prompts, and needs more examples to demonstrate the enhanced descriptions as well as the statics about the enhanced annotations including amount, average length.
2. The methods used in the hierarchical scene semantic enhancer lack novelty. Similar attention-based methods, such as BUTD-DETR [1], have been widely used in previous works. The author should emphasize the difference.
3. Table 1 lacks proper citations.

[1] https://arxiv.org/pdf/2112.08879

### Questions
1. The details of selecting the top-k most related descriptions used in LSE are not listed in the paper;I am still confused about how to rank these descriptions.

### Soundness
3

### Presentation
3

### Contribution
2

# Semantic Score Distillation Sampling for Compositional Text-to-3D Generation

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Generating high-quality 3D assets from textual descriptions remains a pivotal challenge in computer graphics and vision research. Due to the scarcity of 3D data, state-of-the-art approaches utilize pre-trained 2D diffusion priors, optimized through Score Distillation Sampling (SDS).
Despite progress, crafting complex 3D scenes featuring multiple objects or intricate interactions is still difficult. To tackle this, recent methods have incorporated box or layout guidance.
However, these layout-guided compositional methods often struggle to provide fine-grained control, as they are generally coarse and lack expressiveness.
To overcome these challenges, we introduce a novel SDS approach, Semantic Score Distillation Sampling (\method), designed to effectively improve the expressiveness and accuracy of compositional text-to-3D generation.
Our approach integrates new semantic embeddings that maintain consistency across different rendering views and clearly differentiate between various objects and parts.
These embeddings are transformed into a semantic map, which directs a region-specific SDS process, enabling precise optimization and compositional generation. By leveraging explicit semantic guidance, our method unlocks the compositional capabilities of existing pre-trained diffusion models, thereby achieving superior quality in 3D content generation, particularly for complex objects and scenes.
Experimental results demonstrate that our \method framework is highly effective for generating state-of-the-art complex 3D content.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a score distillation-based learning framework for compositional text-to-3D generation. This framework consists of two components: (1) Program-aided layout planning; (2) Semantic SDS. The layout planning module utilizes LLMs to produce layout-related python codes, then the layouts of different objects can be computed by executing python codes. In this way the hallucinations of LLMs in numerical computation can be alleviated. Semantic SDS uses semantic maps rendered from 3DGS as guidance to merge multiple denoising scores. For experiments, qualitative and quantitative evaluations are performed to demonstrate the superiority of the proposed method over previous methods: GraphDreamer, LucidDreamer, GALA3D, GSGEN, while ablation analysis demonstrates the effectiveness of each component.

### Strengths
1. Although semantic 3DGS is not rare, this work combines semantic maps rendering and score distillation to improve compositional text-to-3D generation, which is worthy of recognition in terms of reliability and soundness.
2. The proposed method shows satisfactory performance compared with previous methods, especially in attribute and spatial alignment. The evaluation is thorough, including qualitative and quantitative comparisons and user studies.
3. The design of Object-Specific View Descriptor is well-motivated, and I particularly appreciate the presentation in Figure 3.

### Weaknesses
1. Overall, this work proposes some incremental improvements, for example, semantic score distillation is a very direct combination of semantic 3DGS and score distillation (i.e., a SDS loss weighted by semantic probability maps). Experimental evaluation shows that the proposed method outperforms previous evaluation methods, but not significantly. For instance, in Figure 4, the compared methods GALA3D and GSGEN have higher fidelity and less noise and artifacts.
2. Compared with the baseline GSGEN, SemanticSDS causes quite severe blurring, artifacts, and noise, as shown in Figure 4. Although SemanticSDS effectively improves the spatial layout and attribute binding, its degradation of visual quality is not negligible. 
3. Some details of SemanticSDS seem to be missing. For example, I know that 3D Gaussians are initialized from Shap-E, but how is the correspondence between these 3D Gaussians and subprompts obtained? Also, are the semantic embeddings of 3D Gaussians optimized during training?
4. Based on Eq.(9), it seems that k * l denoising scores need to be predicted, which brings great computational and time costs. Efficiency analysis and comparison should be provided in this case.

### Questions
1. How is the correspondence between initial 3D Gaussians and subprompts obtained? Also, are the semantic embeddings of 3D Gaussians optimized during training?
2. In Figure 2, why is there noise at the edges of objects in semantic maps?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a novel approach, Semantic Score Distillation Sampling (SEMANTICSDS), aimed at enhancing compositional text-to-3D generation by integrating explicit semantic guidance. SEMANTICSDS focuses on fine-grained control over complex scenes by introducing program-aided layout planning, semantic maps, and object-specific view descriptors, enhancing the expressiveness and accuracy of 3D generation for complex objects and scenes.

### Strengths
+ The SEMANTICSDS framework is highly effective in generating complex 3D content.
+ Program-aided layout planning is a notable addition, offering structured scene arrangements.
+ The introduction of semantic maps and region-specific SDS improves control and precision in generating complex scenes with multiple attribute

### Weaknesses
 - The generated scene textures lack realism, which may limit visual appeal and applicability.
- The paper does not showcase any failure cases, which could help illustrate method limitations.
- Quantitative comparisons in the experiments section lack details on specific datasets used for evaluation.

### Questions
1. How does SEMANTICSDS perform with prompts involving highly abstract concepts or non-physical attributes?
2. How does the framework handle scenes with overlapping objects or closely packed spatial arrangements?
3. Program-aided layout planning is interesting; how is the reliability and accuracy of the program ensured?
4. What is the success rate of the LLM?
5. How long does it take to generate a scene, and what is the estimated time per step?
6. In Table 1, how large is the dataset used for qualitative comparison, and how was it constructed?

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
This paper presents a semantic score distillation sampling method for compositional text-to-3D generation by exploiting semantic embeddings and region-specific SDS. Experiments demonstrate promising results of the proposed model for generating complex 3D content.

### Strengths
++ The main idea is novel and interesting for the emerging topic of compositional text-to-3D generation.

++ Clear performance boosts are attained in experimental sections.

### Weaknesses
-- No information of testing data for evaluation is provided. Moreover, it is necessary to introduce the selected 30 scenes for user study. I am happy to see more convincing results or user study over larger-scale test samples (more than 100 scenes at least).

-- In section 5.2, only qualitative comparisons are shown to validate the effectiveness of each design. It is better to perform quantitative comparison on testing data for evaluation.

-- T3Bench [A] contains the subset of multiple objects, and I am curious to see more evaluation over this widely used benchmark.

### Questions
I will increase my rating if more convincing experimental results are provided.

### Soundness
2

### Presentation
2

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
This paper intruduce Semantic Score Distillation Sampling (SEMANTICSDS), a method that enhances the expressiveness and precision of compositional text-to-3D generation. It addresses the challenges of generating precise 3D layouts from vague language descriptions by leveraging program-aided layout planning, semantic embeddings, and explicit semantic guidance. SEMANTICSDS utilizes 3D Gaussian Splatting (3DGS) as the 3D representation and consists of three key steps: program-aided layout planning, semantic embeddings, and rendering semantic maps for fine-grained optimization and compositional generation. The paper demonstrates that SEMANTICSDS achieves state-of-the-art results in generating complex 3D content.

### Strengths
1. SEMANTICSDS demonstrates the ability to generate and manage complex inter-object relationships effectively, such as arranging objects with multiple, overlapping attributes (e.g., a “car made of sushi and LEGO”). This makes it a strong candidate for detailed scene design tasks.
2.

### Weaknesses
1. The Semantic 3D Gaussian Representation proposed in this paper is similar to the approach used in LangSplat. However, the paper does not adequately discuss or clarify the differences between the two approaches.
2. The experimental section is insufficient; the authors are encouraged to incorporate results using LucidDreamer’s ISM optimization to ensure a fair comparison and provide a more comprehensive evaluation of the method’s performance.

### Questions
1. Could the authors provide more details about the computational resources required for training, such as GPU specifications, memory usage, and total computational cost? This would help clarify the practical feasibility of the proposed method.
2. As the number of objects in a scene increases, does the training time scale linearly? If not, could the authors elaborate on how the system handles the increased complexity and whether there are any bottlenecks or optimizations to manage training efficiency?

### Soundness
3

### Presentation
3

### Contribution
2

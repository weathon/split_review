# ConceptFlow: Unified Framework for Personalized Image Generation

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 3, 5

## Abstract
Personalized image generation is an appealing area of research within controllable image generation due to its diverse potential applications. Despite notable advancements, generating images based on single or multiple concepts remains challenging. For single-concept generation, it is difficult to strike a balance between identity preservation and prompt alignment, especially in complex prompts. When it comes to multiple concepts, creating images from a single prompt without extra conditions, such as layout boxes or semantic masks, is problematic due to significantly identity loss and concept omission. In this paper, we introduce ConceptFlow, a comprehensive framework designed to tackle these challenges. Specifically, we propose ConceptFlow-S and ConceptFlow-M for single-concept generation and multiple-concept generation, respectively. ConceptFlow-S introduces a KronA-WED adapter, which integrates a Kronecker adapter with weight and embedding decomposition, and employs a disentangled learning approach with a novel attention regularization objective to enhance single-concept generation. On the other hand, ConceptFlow-M leverages models learned from ConceptFlow-S to directly generate multi-concept images without needed of additional conditions, proposing Subject-Adaptive Matching Attention (SAMA) module and layout consistency guidance strategy. Our extensive experiments and user study show that ConceptFlow effectively addresses the aforementioned issues, enabling its application in various real-world scenarios such as advertising and garment try-on.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces the ConceptFlow framework, including the ConceptFlow-S component for robust single-concept learning and generation, and the ConceptFlow-M component to create images of multiple concepts without the need for spatial guidance.

### Strengths
ConceptFlow-M needs no spatial guidance and can somehow handle the missing concept issue, which is important in multi-concept personalized image generation.

### Weaknesses
1. This work claims to be a unified framework of personalized image generation in the title, but there is no presentation about how it **unifies** personalized image generation.
2. The contribution of the proposed method is weak. There are too many modules that already exist with no relation to each other.
3. The comparison experiments are not rational. Since the proposed model introduces an image adapter, it should compare with the methods using the image adapter. In fact, as a fine-tune-based method, there is no need to use an image adapter since it needs an image input during the inference. I suggest the authors compare the proposed method with some zero-shot methods like IP-Adapter [1], SSR-Encoder [2], and MS-Diffusion [3], which can also solve the same issues.
4. The experiments are completely not enough with few baselines and qualitative examples.

### Questions
Please see the weakness.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The manuscript introduces propose two strategies "ConceptFlow-S" and "ConceptFlow-M" for single-concept generation and multiple-concept generation to resolve the limitation of identity preservation, prompt alignment, and concept omission from previous methods. For single concept, the authors introduce KronA-WED adapter with the attention regularization objective. For multiple concept, the authors propose the SAMA module and layout the consistency guidance. This method facilitates rapid and efficient single and multi-subject customization. The results demonstrate that the method is competitive with leading frameworks in various image generation tasks.

### Strengths
1. The work identifies the issues in both single and multiple concept personalization such as trade off between reconstruction and edibility, and identity loss and the issue of concept missing.

2. The authors have developed a framework for generating personalized images that effectively integrates strategies to solve both single (ConceptFlow-S) and multiple concept (ConceptFlow-M). 

2. The paper provides experimental results, including both quantitative and qualitative assessments, showcasing the superior performance of the framework. The results clearly highlight the effectiveness of the proposed method in facilitating personalized image generation.

### Weaknesses
1. In Figure 5, the method utilizes SAMA module to enhance the identity details. However, it is unclear how it would perform with fine-grained subjects (two dogs or two cats with different breed). Also, I wonder how this module would work when the concept size increases. Clarification is needed on whether the module can effectively manage such fine distinctions and multiple diverse subjects.

2. Recent methodologies [1, 2] have demonstrated the capability to learn multi-concept personalization, it remains uncertain if the proposed work can handle multiple personalized instances (> 2), particularly for contexts involving up to five subjects. Although quantitative results for two subjects are provided in both paper and appendix, the absence of qualitative results for three or more subjects in both the main text and appendix might be a notable omission. Including these results would substantiate the method's capability in more complex scenarios.

### Questions
Given the concerns mentioned, particularly around the method's scalability to more complex multi-subject personalizations and the clarification behind module choices, I recommend a "marginally below the acceptance threshold" for this paper. Enhancements in demonstrating multi-subject capabilities, clarity in embedding visualization, and justification for the choice of technology could potentially elevate the manuscript to meet publication standards.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces ConceptFlow to balance identity preservation with prompt alignment, alleviating identity loss and concept omission.   The proposed KronA-WED adapter combined with a novel attention regularization objective balances reconstruction and editability
for single-concept generation. Additionally, the subject-adaptive matching attention module and layout consistency guidance strategy help prevent concept omission in multi-concept generation. Experimental results indicate that the proposed method has a positive impact on these issues to some extent.

### Strengths
1. This paper collects a small dataset.
2. The proposed method achieves good identity preservation.

### Weaknesses
1. Only a limited number of comparison methods, especially in multi-concept generation, does not adequately support the authors' claim. Why does this paper compare against so few published works? Let's leave aside arXiv papers, there are many accepted, peer-reviewed papers should be considered.

[1] FastComposer: Tuning-Free Multi-subject Image Generation with Localized Attention, IJCV 

[2] FreeCustom: Tuning-Free Customized Image Generation for Multi-Concept Composition, CVPR 2024 

[3] Key-Locked Rank One Editing for Text-to-Image Personalization, SIGGRAPH 2023

[4] Concept Weaver: Enabling Multi-Concept Fusion in Text-to-Image Models, CVPR2024

[5] OMG: Occlusion-friendly Personalized Multi-concept Generation in Diffusion Models, ECCV2024

[6] KOSMOS-G: Generating Images in Context with Multimodal Large Language Models, ICLR2024

2. Even in comparison with the methods listed in table, the proposed trivial method does not show significant improvement. This is particularly evident in CLIP-T, which evaluates editability and does not support the authors' claims of balancing the trade-off between reconstruction and editability. Can this paper provide metrics that evaluate this trade-off directly, rather than reporting separately when one aspect is better and the other is worse.

### Questions
1. It is good to see the new collected dataset. But for a comprehensive comprasion. Can the authors provide multi-concept generation results using CustomConcept101?
2. Most of papers report both CLIP-I and DINO. I believe use both metrics can better evaluate the identity preservation in different aspects.
3. I believe that extra conditions like boxes and masks can make generation more controllable. Of course, there are some situtations that condition-free generation is better. It would be appreciated to see the proposed can achieve better performance on both setting.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper proposes **ConceptFlow**, which includes two components: **ConceptFlow-S** for single-concept generation and **ConceptFlow-M** for multi-concept generation. ConceptFlow-S employs a **KronA-WED adapter** that integrates a Kronecker adapter with weight and embedding decomposition. It also introduces **attention regularization** to improve single-concept generation. ConceptFlow-M extends the models trained by ConceptFlow-S, using **SAMA** (Subject-Adaptive Matching Attention) and **layout consistency guidance** to handle multi-concept generation without requiring additional spatial conditions.

### Strengths
1. **Comprehensive personalization framework:** 
  The paper covers both single and multi-concept personalization, supported by comparisons with recent works.

2. **Application insights and metrics:**
   The discussion includes practical applications, qualitative examples, and appropriate metrics for performance analysis.

### Weaknesses
 1. **Over-complex Framework without Substantial Innovations:**  
    - The **KronA-WED adapter** is like a simple stack of previous strategies, **Mix-of-Show’s *ED-LoRA*** [1] $+$ **Kronecker Adapter *(KronA)*** [6]  $ightarrow$ **KronA-WED adapter**. The incremental nature of this combination, without a clear novel mechanism, raises concerns about its contribution beyond a straightforward aggregation of existing techniques. Specifically, the paper does not sufficiently detail how the interaction between ED-LoRA and KronA leads to emergent properties or performance gains that are not achievable by simply applying them sequentially or independently.
    - The proposed framework looks highly similar as a blend of **Mix-of-Show’s *gradient fusion*** [1] and **DisenBooth’s disentangled learning** [2], which dilutes its novelty. The paper lacks a rigorous analysis demonstrating that the combination of these techniques offers a unique advantage over existing methods. The disentanglement strategy, in particular, appears to be a direct application of DisenBooth’s approach, and the paper does not provide a clear explanation of how the gradient fusion is adapted to the specific context of ConceptFlow, or how it differs from Mix-of-Show’s implementation. 
    - Furthermore, the **attention regularization (AR)** employed seems highly similar as **Break-A-Scene's attention-based loss** [3], which is also designed to encourages that each handle attends only to the image region occupied by the corresponding concept. The paper does not offer a detailed comparison of the AR loss with Break-A-Scene’s attention-based loss, nor does it provide evidence that the proposed AR loss introduces any novel constraints or optimization strategies. The lack of a detailed analysis makes it difficult to assess the unique contribution of this component.
    - The **SAMA module** for multi-concept generation largely reuses existing strategies, closely mirroring **DreamMatcher’s AMA** [4] (with **Eq. 6-9** resembling **Eq. 3, 4, 5, and 7** from DreamMatcher) but with minor modifications, such as adding a **foreground mask**. The paper does not provide a clear justification for the necessity of the foreground mask, nor does it demonstrate that this modification leads to a significant improvement in performance or addresses a specific limitation of DreamMatcher’s AMA. The similarities in the equations and overall structure suggest that SAMA is more of an incremental adaptation than a novel contribution.
    - The design of **Layout Guidance** follows the core idea of **A-Star's Attention Segregation Loss** [5], also not a novel technique. The paper does not provide a detailed analysis of how the Layout Guidance differs from A-Star's Attention Segregation Loss, nor does it provide evidence that the proposed guidance introduces any novel constraints or optimization strategies. This lack of a detailed analysis makes it difficult to assess the unique contribution of this component. This accumulation of existing techniques makes the work feel like an industrial assembly, which reduces the perceived novelty of the contribution.

2. **Identity Preservation Issues and Low-Level Aesthetics:**  
   - Several generated outputs display **identity dissimilarity** or **unsatisfactory aesthetics**, such as Justin Bieber, Emma Stone, cat in **Fig. 1**, which raise my concerns about the soundness of the proposed method and the robustness of the framework when dealing with **diverse or intricate concepts**. The inconsistencies in identity preservation, particularly for well-known faces, suggest that the method struggles with fine-grained details and may not generalize well to a wide range of subjects. The aesthetic issues, such as unnatural textures or distortions, further indicate that the framework has limitations in generating high-quality, visually appealing images.

3. **Dataset Limitations and Generalizability:**  
   - The selection of subjects  in the manuscript are limited (**24 subjects (Fig. 12)**), which is limited and potentially biased toward **cherry-pick cases**. I believe these limited subjects can not represent the full spectrum of real-world complexities, and a broader test set covering **more diverse concepts and edge cases** would provide stronger evidence of the framework's generalizability. The lack of diversity in the dataset raises concerns about the robustness and reliability of the results, as the framework may not perform as well on subjects or scenarios that are not well-represented in the training data.

### Questions
1. **Enhancing Identity Matching in Evaluation:**  
   - The current evaluation focuses on **DINO scores** and **CLIP-T metrics**, but these might not capture **fine-grained identity preservation**, especially for faces. Have you considered incorporating face recognition tools like **FaceNet** or **ArcFace** [7]? These tools could offer bounding-box-level face similarity evaluation, providing a more precise measurement of face identity consistency.


2. **Expanding the Dataset and Subject Variety:**  
   - As stated in  **Weakness 3**, The number of subjects used for both quantitative and qualitative evaluations appears limited (**Fig. 12**). This narrow selection may affect the statistical reliability of the results. Could you **experiment on more subjects or scenarios** to validate the performance of ConceptFlow across a broader range of real-world cases?

3. **Innovative Contributions of SAMA Compared to DreamMatcher:**  
   - The *SAMA module* seems closely related to DreamMatcher’s *Appearance Matching Self-Attention (AMA)*, with the primary distinction being the use of a *concept foreground mask ($\mathbf{M}_k$)*. Could you further conduct **ablation studies on the AMA vs. SAMA** to show how it extends beyond DreamMatcher's approach?


4. **Time Efficiency and Computational Overhead:**  
   - ConceptFlow involves multiple steps, such as *gradient fusion, SAMA matching, and layout consistency guidance*, which could introduce computational overhead. Could you provide a **memory / time efficiency comparison** between ConceptFlow and other state-of-the-art methods, such as **LoKr [8], DisenBooth [2], and Mix-of-Show [1]**? This would clarify the practical trade-offs between performance and efficiency for both single and multi-concept generation.


**Reference**

[7] *https://github.com/deepinsight/insightface*.

[8] *Yeh, et al. "Navigating text-to-image customization: From lycoris fine-tuning to model evaluation." ICLR (2023)*.

### Soundness
2

### Presentation
2

### Contribution
2

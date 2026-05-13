# MMTryon: Multi-Modal Multi-Reference Control for High-Quality Fashion Generation

- Decision: Reject
- Scores: 8, 10, 3

## Abstract
This paper introduces MMTryon, a multi-modal multi-reference VIrtual Try-ON (VITON) framework, which can generate high-quality compositional try-on results by taking a text instruction and multiple garment images as inputs. Our MMTryon addresses three problems overlooked in prior literature: 1) \textbf{Support of multiple try-on items.} Existing methods are commonly designed for single-item try-on tasks (e.g., upper/lower garments, dresses).
2) \textbf{Specification of dressing style}. Existing methods are unable to customize dressing styles based on instructions (e.g., zipped/unzipped, tuck-in/tuck-out, etc.)
3) \textbf{Segmentation Dependency}. They further heavily rely on category-specific segmentation models to identify the replacement regions, with segmentation errors directly leading to significant artifacts in the try-on results. To address the first two issues, our MMTryon introduces a novel multi-modality and multi-reference attention mechanism to combine the garment information from reference images and dressing-style information from text instructions. Besides, to remove the segmentation dependency, MMTryon uses a parsing-free garment encoder and leverages a novel scalable data generation pipeline to convert existing VITON datasets to a form that allows MMTryon to be trained without requiring any explicit segmentation. 
Extensive experiments on high-resolution benchmarks and in-the-wild test sets demonstrate MMTryon's superiority over existing SOTA methods both qualitatively and quantitatively. 
MMTryon's impressive performance on multi-item and style-controllable virtual try-on scenarios and its ability to try on any outfit in a large variety of scenarios from any source image, opens up a new avenue for future investigation in the fashion community. Project page is \href{https://zhangxj59.io/MMTryon.io/}{this link}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper introduces MMTryon, a model that integrates a multi-modality and multi-reference attention mechanism to enhance virtual try-on tasks by combining garment details from reference images with dressing styles from text guidance. The model is designed for multi-garment try-ons and does not require segmentation networks, thanks to a new parser-free garment encoder and a scalable data generation pipeline. MMTryon achieves superior performance in single and multi-garment try-on tasks, addressing limitations in previous models such as single-garment constraints, fixed dressing styles, and segmentation dependencies.

### Strengths
1. The paper introduces innovative multi-modal and multi-reference attention mechanisms, allowing for multi-garment try-ons with customized, fine-grained text guidance.

 2. Leveraging a pretrained garment encoder, MMTryon can capture detailed features of garments specified by text, improving model precision and contributing to advancements in the field.

 3. Extensive qualitative and quantitative evaluations demonstrate MMTryon’s superior performance compared to state-of-the-art methods, with high-quality visual results showcasing realistic try-on effects and robust editing capabilities.

 4. The proposed data generation pipeline creates a comprehensive paired multi-garment dataset without segmentation, broadening the scope of try-on tasks and supporting complex garment compositions.The parsing-free approach in this article presents a promising direction, contributing to the advancement of try-on technology toward more practical applications.

 5.This article is well-written

### Weaknesses
1. some descriptions could be clearer to avoid reader confusion. For example, in Fig. 3, labeling the UNet as “MMTryon UNet” rather than specifying it as a pretrained SD UNet might mislead readers at this training stage. Similarly, terms like “w/o TQL” and “w/o MRA” in Fig. 8 are somewhat unclear; the ablation study would benefit from more precise terminology and a more detailed explanation of what each component represents. Specifically, the 'w/o TQL' ablation lacks clarity on how the text query learning is removed and what the impact on the model is. Furthermore, 'w/o MRA' needs a more thorough explanation of how multi-reference attention is disabled and the resulting effect on the model's ability to integrate information from multiple garment references.

2. the inference process requires more detailed explanation, especially given the model’s support for multiple tasks. Currently, some detail of inference lack explaination, which may lead to unintended changes in specific garments, such as unexpected alterations in lower garments shown in the first image. The lack of clarity on how the model handles multiple garment references during inference is a significant concern. It's not clear how the model prioritizes or combines the information from different garment references, and how it ensures that only the intended garments are modified while preserving the original details of the others. The current explanation does not provide sufficient detail on how the model avoids unintended modifications to garments that are not explicitly targeted by the text prompt.

### Questions
1.As mentioned in the weaknesses, please explain why the pants in the last rows of the first image changed unexpectedly.

2.the method is good，Are there any plans to release the code and model to support the  research community?

3.What is the inference time and required GPU memory for MMTryon in different task?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
10

### Rating Number
10

### Confidence
5

### Summary
This paper introduces MMTryon, a multi-modal, multi-reference Virtual Try-On (VITON) framework capable of generating high-quality, compositional try-on results from text instructions and multiple garment images. MMTryon addresses three main limitations in existing methods: supporting multiple garments, specifying dressing styles, and reducing dependency on segmentation models. It achieves this through a novel multi-modality attention mechanism that combines garment details from images with style cues from text, and by using a parsing-free garment encoder alongside a scalable data pipeline to eliminate the need for segmentation. Extensive experiments demonstrate MMTryon’s superior performance in multi-item and style-controllable try-on tasks, offering new potential for applications in the fashion field.

### Strengths
1. The paper introduces a unique attention mechanism that enables multi-item try-on and customizable styling, addressing limitations in previous models.
2. The paper adopts a novel approach by eliminating segmentation dependency using a parsing-free garment encoder and scalable data pipeline. This method presents a practical solution to common issues in virtual try-on tasks, improving model efficiency and minimizing artifacts.
3. The paper is well-organized, and there are a lot of ablation study in main paper and appendix to demonstrate impact of each component in the proposed approach.

### Weaknesses
1. The Related Work section lacks recent studies on control and try-on methods,
2. More detail information about dataset should be provided.
3. in some case, the fine texture on the garment still cannot be recovered completely,

### Questions
1. Could you provide more information about the e-commerce dataset used in the experiments?
2. Do you have any plans to open-source the dataset and the data processing pipeline? Making these resources publicly available could greatly benefit research in this area and facilitate further advancements in virtual try-on methods.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper combines multi-modal implementation of VITON. 
Three problems are proposed and solved by the designed data set and multi-model instruction attention. 
The experimental results show that the data in the wild well.

### Strengths
1. MMTryon is able to combine multiple garments for fitting, while also allowing the fitting effect to be manipulated by text commands. 
2. A scalable data generation pipeline and a specially designed clothing encoder are introduced. 
3. Eliminates the need for any prior segmentation network during the training and reasoning phases.

### Weaknesses
1. The definition of the task is not very clear, and similar work may already exist, leading to unclear motivation. Related work needs to be strengthened.
2. multi-modal multi-reference attention is just a simple extension of reference attention [1], and it is not clear how to decouple and align the details.
3. The quantitative and qualitative results are not complete, especially the texture details are not so good.
4. The data set is the highlight of this paper, but it doesn't seem to claim to be open data, so I don't think it's a contribution either.

1. The paper makes overstated claims, such as line 96 where it states, "is the first model to support the multi-modal compositional try-on task." However, multi-modal compositional try-on is already supported by M&M VTO [2], AnyFit [3], and VITON-DiT [4]. I don't think the relevant work is sufficient. And I recommend the authors explicitly compare these previous works in terms of their multi-modal capabilities to clarify if the proposed approach indeed offers novel advantages or is simply an extension of existing techniques.

2. The paper lacks clear motivation and has weak contributions. For example, Question 1 has already been explored, but the authors do not clearly articulate its relevance or contribution here. Additionally, texture consistency—an essential issue in VTON—seems neglected. I suggest the authors further clarify the connection between their research questions and contributions and add a discussion on texture consistency, as this factor is critical to the realism of virtual try-on. This improvement would enhance the clarity and relevance of the study.

3. The novelty is limited. The garment encoder appears to use cross-attention, which raises the question of whether there is anything unique about it. I recommend the authors explain how their garment encoder differs from or improves upon standard cross-attention mechanisms, especially if there are any specific design or functional enhancements, to demonstrate genuine innovation.

4. Serious concerns arise from fusing text and image features directly without decoupling, which may lead to unintended consequences, yet the paper does not address this. I suggest the authors provide a more thorough justification for this fusion strategy, as bypassing decoupling could compromise the model’s interpretability or adaptability. Discussing the rationale behind this choice and evaluating potential pitfalls would strengthen the explanation.

5. The paper lacks thorough comparison methods. In particular, quantitative results for single-garment cases are not provided for methods like Outfit Anyone, Kolors-Virtual-Try-On [5], Wear-Any-Way [6], and MV-VTON [7]. Additionally, Figure 6 does not display clear advantages. The omission of quantitative comparisons with key methods weakens the study’s validity. I suggest including comparative performance metrics with these established models in Table 1 and providing more insightful analysis of Figure 6 to support the claimed improvements. Besides,  Under multi-modal conditions, Table 7 suggests that background is not controllable. However, Imagedressing [8] has achieved background control, yet it is not referenced or discussed. If background control is indeed relevant, I suggest that the authors provide a direct comparison with Imagedressing or explicitly state if background control is beyond the scope of their study to give readers a clearer understanding of the method’s applicability.

6. Texture details (such as Pants, logo changed) appear poorly rendered across multiple cases, including those in the appendix. I recommend identifying specific areas with poor texture rendering and offering suggestions to improve texture detail quality, as this would enhance the realism and appeal of the model’s outputs.

7. The implementation details concerning SDXL on line 295 and SD 1.5 on line 352 are confusing. I suggest that the authors clarify why they employ different Stable Diffusion versions in various pipeline segments and explain the implications for model outputs to improve method transparency.

8. Adding results under similar conditions, such as challenging cases with letters, numbers, and diverse textures, is advised. The paper would benefit from showcasing the model’s performance on complex garments, such as those with letters or intricate textures, as these are realistic challenges in virtual try-on systems.

Other details:
1. In Table 2,  '0.7' should be '0.70'
2. Formulas 1 and 2 have commas at the end, while formulas 3 and 4 are missing.

### Questions
1. The paper makes overstated claims, such as line 96 where it states, "is the first model to support the multi-modal compositional try-on task." However, multi-modal compositional try-on is already supported by M&M VTO [1], AnyFit [2], and VITON-DiT [3]. I don't think the relevant work is sufficient. And I recommend the authors explicitly compare these previous works in terms of their multi-modal capabilities to clarify if the proposed approach indeed offers novel advantages or is simply an extension of existing techniques.

2. The paper lacks clear motivation and has weak contributions. For example, Question 1 has already been explored, but the authors do not clearly articulate its relevance or contribution here. Additionally, texture consistency—an essential issue in VTON—seems neglected. I suggest the authors further clarify the connection between their research questions and contributions and add a discussion on texture consistency, as this factor is critical to the realism of virtual try-on. This improvement would enhance the clarity and relevance of the study.

3. The novelty is limited. The garment encoder appears to use cross-attention, which raises the question of whether there is anything unique about it. I recommend the authors explain how their garment encoder differs from or improves upon standard cross-attention mechanisms, especially if there are any specific design or functional enhancements, to demonstrate genuine innovation.

4. Serious concerns arise from fusing text and image features directly without decoupling, which may lead to unintended consequences, yet the paper does not address this. I suggest the authors provide a more thorough justification for this fusion strategy, as bypassing decoupling could compromise the model’s interpretability or adaptability. Discussing the rationale behind this choice and evaluating potential pitfalls would strengthen the explanation.

5. The paper lacks thorough comparison methods. In particular, quantitative results for single-garment cases are not provided for methods like Outfit Anyone, Kolors-Virtual-Try-On [4], Wear-Any-Way [5], and MV-VTON [6]. Additionally, Figure 6 does not display clear advantages. The omission of quantitative comparisons with key methods weakens the study’s validity. I suggest including comparative performance metrics with these established models in Table 1 and providing more insightful analysis of Figure 6 to support the claimed improvements. Besides,  Under multi-modal conditions, Table 7 suggests that background is not controllable. However, Imagedressing [7] has achieved background control, yet it is not referenced or discussed. If background control is indeed relevant, I suggest that the authors provide a direct comparison with Imagedressing or explicitly state if background control is beyond the scope of their study to give readers a clearer understanding of the method’s applicability.

6. Texture details (such as Pants, logo changed) appear poorly rendered across multiple cases, including those in the appendix. I recommend identifying specific areas with poor texture rendering and offering suggestions to improve texture detail quality, as this would enhance the realism and appeal of the model’s outputs.

7. The implementation details concerning SDXL on line 295 and SD 1.5 on line 352 are confusing. I suggest that the authors clarify why they employ different Stable Diffusion versions in various pipeline segments and explain the implications for model outputs to improve method transparency.

8. Adding results under similar conditions, such as challenging cases with letters, numbers, and diverse textures, is advised. The paper would benefit from showcasing the model’s performance on complex garments, such as those with letters or intricate textures, as these are realistic challenges in virtual try-on systems.


Other details:
1. In Table 2,  '0.7' should be '0.70'
2. Formulas 1 and 2 have commas at the end, while formulas 3 and 4 are missing.
---
[1] Zhu L, Li Y, Liu N, et al. M&M VTO: Multi-Garment Virtual Try-On and Editing[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024: 1346-1356.

[2] Li Y, Zhou H, Shang W, et al. AnyFit: Controllable Virtual Try-on for Any Combination of Attire Across Any Scenario[J]. arXiv preprint arXiv:2405.18172, 2024.

[3] Zheng J, Zhao F, Xu Y, et al. VITON-DiT: Learning In-the-Wild Video Try-On from Human Dance Videos via Diffusion Transformers[J]. arXiv preprint arXiv:2405.18326, 2024.

[4] https://huggingface.co/spaces/Kwai-Kolors/Kolors-Virtual-Try-On.

[5] Chen M, Chen X, Zhai Z, et al. Wear-any-way: Manipulable virtual try-on via sparse correspondence alignment[J]. arXiv preprint arXiv:2403.12965, 2024.

[6] Wang H, Zhang Z, Di D, et al. MV-VTON: Multi-View Virtual Try-On with Diffusion Models[J]. arXiv preprint arXiv:2404.17364, 2024.

[7] Shen F, Jiang X, He X, et al. Imagdressing-v1: Customizable virtual dressing[J]. arXiv preprint arXiv:2407.12705, 2024.

### Soundness
2

### Presentation
2

### Contribution
2

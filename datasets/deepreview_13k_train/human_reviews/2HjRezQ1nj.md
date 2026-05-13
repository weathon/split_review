# Combining Text-based and Drag-based Editing for Precise and Flexible Image Editing

- Decision: Accept
- Scores: 8, 3, 5, 8

## Abstract
Precise and flexible image editing remains a fundamental challenge in computer vision. Based on the modified areas, most editing methods can be divided into two main types: global editing and local editing. In this paper, we discussed two representative approaches of each type (\ie, text-based editing and drag-based editing. Specifically, we argue that both two directions have their inherent drawbacks: Text-based methods often fail to describe the desired modifications precisely, while drag-based methods suffer from ambiguity. To address these issues, we proposed \textbf{CLIPDrag}, a novel image editing method that is the first try to combine text and drag signals for precise and ambiguity-free manipulations on diffusion models. To fully leverage these two signals, we treat text signals as global guidance and drag points as local information. Then we introduce a novel global-local motion supervision method to integrate text signals into existing drag-based methods ~\citep{shi2024dragdiffusion} by adapting a pre-trained language-vision model like CLIP ~\citep{radford2021learning}. Furthermore, we also address the problem of slow convergence in CLIPDrag by presenting a fast point-tracking method that enforces drag points moving toward correct directions. Extensive experiments demonstrate that CLIPDrag outperforms existing single drag-based methods or text-based methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces CLIPDrag, a novel image editing approach that integrates both text-based and drag-based controls to achieve more precise and flexible edits. Traditional text-based editing provides general guidance but often lacks specificity, while drag-based editing offers local control but can be ambiguous without context. CLIPDrag addresses these issues by using text as global guidance for overall image context and drag points for fine-grained, localized control. The model leverages a global-local motion supervision (GLMS) system and a fast point-tracking (FPT) method to streamline and accelerate the editing process. The paper is well written and easy to understand, the paper has comprehensive experimental results which show CLIPDrag outperforms both traditional drag- and text-based methods in accuracy and image fidelity. The detailed ablations make the hypothesis clear. The paper presents an interesting path for image editing and is theoretically grounded which should be shared within the community

### Strengths
1. Novel Approach to combine local and global gradient: Building on text inversion methods to combine text and drag signals, CLIPDrag enables pixel-level control, offering both specific and contextually aware edits.
2. Efficient Convergence: The fast point-tracking method improves the editing process by guiding handle points toward their target positions faster.
3. Extensive Ablations: The paper has ablations for all different components such as point tracking, GLMS and controls with edit and text showing clear performance gain. 
4. Qualitative Results: The papers presents representative set of results allowing easy intuition and help with clarity of the paper.

### Weaknesses
1. The need for identity preservation beyond citing DragDiffusion is not shared, given the improvement of base models, the intuition behind it is lacking. 
2. Gradient accumulation is discussed assuming the latent code is continuous, formulating why the gradient manipulation will still lead to plausible images is unclear. 
3. Assumption around using nearest neighbors in FPT moving monotonically towards target is not explained, given the optimization is highly non linear.

### Questions
1. What are some common failure cases for the editing, especially if the text and local edits conflict. 
2. How are the number of iterations for denoising fixed for drag editing and how do the impact change with fewer to larger iterations. 
3. One of example is shown to incorporate masks for editing, can it be explained how masks are incorporated in this framework ?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a Text-Drag Editing framework to address text-based and drag-based editing limitations. To achieve this, the authors introduce global-local motion supervision that integrates the semantic aspects of text with drag guidance. They utilize a novel approach of gradient fusion, combining gradients from text and drag conditioning based on their directional alignment to provide a unified gradient.

### Strengths
For the first time, the paper provides an algorithm that integrates text-guided editing with drag-guided editing. The proposed editing algorithm attempts to provide more precise global editing and reduce ambiguity in local editing. The independent guidance or supervision of text and drag is combined interestingly by disentangling the global gradient that is perpendicular and parallel to the local gradient.

### Weaknesses
1. Lack of Comprehensive Review of Diffusion-Based Image Editing Literature:
The paper does not provide an adequate overview of diffusion-based image editing methods. A more thorough review of recent approaches in diffusion-based image editing is necessary to strengthen its background and situate the proposed method within the broader field. Specifically, the authors should consider discussing recent methods, such as 
SINE: SINgle Image Editing With Text-to-Image Diffusion Models (Zhang et al., CVPR 2023), 
Paint by Example: Exemplar-based Image Editing with Diffusion Models (Yang et al., CVPR 2023), 
FlexiEdit: Frequency-Aware Latent Refinement for Enhanced Non-Rigid Editing (Koo et al., ECCV 2024), 
and RegionDrag: Fast Region-Based Image Editing with Diffusion Models (Lu et al., ECCV 2024). 
Incorporating these examples will provide a more robust foundation and context for the reader, enabling a clearer understanding of how the current approach builds upon or diverges from existing work.

2. Unconvincing Example in Figure 1:
The example provided in Figure 1 does not convincingly illustrate the motivation of the study. The intention seems to highlight the limitations of drag-based and text-based editing approaches, yet the figure only demonstrates an instance where drag-based editing is ineffective. A more persuasive example might involve a scenario where drag-based editing produces a subtle change—such as adjusting a subject's smile—which could then be further refined by the proposed text-drag editing method to achieve a more detailed, natural effect. This change would clarify the benefits of text-drag editing over existing methods.

Additionally, the similarity between the proposed method's results and traditional drag-based editing in Figure 1 and the statute example raises questions about the added benefit of the proposed approach. If these similarities are not intentional, a different example or refinement of the illustrations might better demonstrate the unique advantages of the proposed method.

3. Handling of Distinct Effect Regions in Text-Based and Drag-Based Editing
The paper does not adequately explain how it manages distinct effect regions associated with text-based and drag-based editing despite these methods likely targeting different areas in an image. Clarifying how these regions are defined, integrated, or adjusted during editing would provide more specificity and improve understanding of the algorithm's functionality. This discussion is crucial to distinguish the contribution of the combined editing approach.

4. Suggested Comparative Experiments for Method Validation
Comparative experiments should include scenarios where text-based editing is applied after drag-based editing and vice versa to illustrate the proposed method's effectiveness better. This comparison would help demonstrate the practical advantage of combining both methods in the proposed approach and establish whether there are meaningful improvements when they are applied sequentially.

5. Limited Novelty in Gradient Combination Approach
The novelty presented in Equation (6), which combines the two editing approaches by decomposing one gradient into the other perpendicular component and then summing them, seems linear, and it is conceivable that a non-linear combination may provide a more effective result.  Including alternative approaches as comparative experiments would strengthen the paper's case for its approach or help contextualize its performance relative to existing methods.

The paper introduces a combined text-drag editing approach but lacks a comprehensive literature review, convincing examples, clarity regarding region specificity, and evidence of sufficient novelty. Addressing these areas would help elevate the study’s contributions and clarify its position within diffusion-based image editing.

### Questions
Please provide examples with and without drag edit the following examples. "The sculpture is smiling and not showing his teeth." and "The sculpture is smiling and not raising his head".

### Soundness
2

### Presentation
2

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
CLIPDrag combines text and drag-based controls to improve image editing, using text for broad guidance and drag points for precise adjustments. The author introduces Global-Local Motion Supervision, which combines gradients from both text and drag inputs, and Fast Point Tracking to speed up convergence. This method eliminates common issues like vagueness in text-only edits and ambiguity in drag-only edits.

### Strengths
1.	The motivation is clear and effective, combining text and drag editing to leverage the strengths of both approaches, achieving more precise edits.
2.	The Global-Local Gradient Fusion method is innovative, merging global text and local drag gradients to enhance editing quality, with experiments showing notable improvements in performance.

### Weaknesses
1.	The illustration in Figure 2 is unclear in terms of workflow. If CLIP guidance is applied, the latent space should ideally be converted to the pixel domain to align with CLIP’s processing. However, the diagram uses SD rather than a VAE.
2.	CLIPDrag lacks comprehensive quantitative comparisons with other methods in image editing. The current evaluation only includes DragDiff in Figure 6, which is insufficient.
3.	The ablation study also lacks more detailed quantitative comparisons. In Figure 8, the visual differences between (b) and (c) are subtle, making it hard to discern the impact of changes.

### Questions
The comparisons in this paper in insufficient, why only DragDiff is compared to in this paper? More comparisons should be added.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This manuscript introduces CLIPDrag, a novel method that integrates text-based and drag-based signals for image editing, leveraging both for precise control and reduced ambiguity. The method utilizes Global-Local Motion Supervision (GLMS) and Fast Point Tracking (FPT) to enhance the image editing process, aiming to outperform existing methods by combining the strengths of both editing approaches.

### Strengths
1. **Innovative Integration**: The paper presents a compelling approach by combining text and drag inputs to guide image editing. This dual-input strategy addresses the limitations of each method when used independently, potentially offering more controlled and precise edits.
2. **Technical Depth**: The introduction of GLMS shows a deep understanding of the challenges in image editing, particularly in handling the complexities associated with combining different types of editing signals.
3. **Experimental Validation**: Extensive experiments, including ablation studies, demonstrate the effectiveness of CLIPDrag against state-of-the-art methods. The results are well-presented and support the claims of improved performance in terms of both precision and ambiguity resolution.

### Weaknesses
1. **Novelty of FPT**: The paper should acknowledge that searching for handle points along the path from handle points to targets has been previously explored in methods like DragGAN and DragDiffusion. To clarify the unique contributions of FPT, the authors should provide side-by-side comparisons of point searching strategies, highlighting any improvements or distinctions in their approach. Specifically, the paper needs to clarify how the search space for new handle points differs from existing methods. While the paper mentions a constraint on the search area, it lacks a detailed explanation of how this constraint is implemented and its impact on the optimization process. A more rigorous analysis of the search algorithm, including its computational complexity and convergence properties, is needed to fully assess its novelty.

2. **Comprehensive Comparisons**: While the paper compares CLIPDrag with some existing methods, it would benefit from more extensive comparisons or discussions with recent techniques such as InstantDrag, LightningDrag, StableDrag, and RegionDrag. Although these methods may use different training approaches or inputs, incorporating their text-supervision signals could demonstrate CLIPDrag's ability to address ambiguities present in these methods, showcasing its generalizability. Additionally, these methods should be thoroughly discussed in the related work section to provide a more complete context. The comparison should not only focus on qualitative results but also include quantitative metrics that highlight the differences in performance, such as the degree of identity preservation and the accuracy of the edits.

3. **Performance Metrics**: The paper should include a discussion or report on inference time comparisons. This information is crucial for understanding the practical applicability of CLIPDrag in real-world scenarios and how it compares to other methods in terms of computational efficiency. The inference time should be reported not just as an average but also with a breakdown of the time spent on different stages of the algorithm, such as point tracking and image generation. This would provide a more detailed understanding of the computational bottlenecks and potential areas for optimization.

4. **User Input Optimization**: While the text prompt is provided in DragBench, it's worth noting that the original DragGAN paper did not require text input. The additional text prompt in CLIPDrag may increase user effort. To address this, the authors could explore incorporating vision-language models like GPT-4V to automatically interpret the input image (as shown in the first column of Figure 4). This approach could significantly reduce user burden while maintaining the benefits of text-guided editing. Furthermore, the paper should discuss the sensitivity of the method to the quality and specificity of the text prompts. It is important to understand how variations in the text input affect the editing results and whether there are any limitations in the types of edits that can be achieved with different prompts.

### Questions
In the context of drag-based editing where maintaining the original identity of objects while manipulating specific features is a major challenge, your manuscript suggests the integration of text-based inputs to guide the editing process. Could you elaborate on how the addition of text signals specifically contributes to preserving the object's original identity during the edit? Additionally, are there specific conditions or types of text prompts that particularly enhance this preservation aspect within the CLIPDrag framework?

### Soundness
3

### Presentation
3

### Contribution
3

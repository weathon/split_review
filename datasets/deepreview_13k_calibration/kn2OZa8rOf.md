# Rethinking Attentions in Zero-Shot Real Image Editing

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
Editing natural images using textual descriptions in text-to-image diffusion models remains a significant challenge, particularly in achieving consistent generation and handling complex, non-rigid objects. Existing methods often struggle to preserve textures and identity, require extensive fine-tuning, and exhibit limitations in editing specific spatial regions or objects while retaining background details. This paper proposes Context-Preserving Adaptive Manipulation (CPAM) -- a novel zero-shot method for complicated, non-rigid real image editing. Specifically, we propose a preservation adaptation module that adjusts self-attention mechanisms to effectively preserve and independently control the object and background. This ensures that the objects' shapes, textures, and identities are maintained while keeping the background undistorted during the editing process using the mask guidance technique. Additionally, we develop a localized extraction module to mitigate the interference with the non-desired modified regions during conditioning in cross-attention mechanisms. We also introduce various mask-guidance strategies to facilitate diverse image manipulation tasks in a simple manner. Extensive experiments on our newly constructed Image Manipulation BenchmArk (IMBA), a robust benchmark dataset specifically designed for real image editing, demonstrate that our proposed method is the preferred choice among human raters, outperforming existing state-of-the-art editing techniques.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
- This paper presents Context-Preserving Adaptive Manipulation (CPAM) to address complex, non-rigid image editing using a tuning-free, zero-shot approach. 
- It utilizes both self-attention and cross-attention mechanisms in Stable Diffusion to enable intricate and text-guided image edits.
- It proposes the Preservation Adaptation Process to adjust self-attention layers to retain the identity, texture, and shape of the object being edited while the background remains unchanged.
- It also includes a Localized Extraction Module to avoid undesired changes to other image areas, and it enables the selective application of cross-attention.
- It proposes various strategies to control the editing scope based on the task, e.g. object removal, replacement, or background alteration, and it allows users to define which parts of the image are editable.
- The paper also introduces a new benchmark to evaluate real-image editing models and provides extensive qualitative and quantitative comparisons to show the effectiveness of the proposed method.

### Strengths
- This paper offers useful advances for real-image editing by removing the need for fine-tuning and allowing flexible, zero-shot editing.
- This paper is organized well and gives clear explanations of each new component and how they work together to improve image editing.
- The author provides extensive experiments to show that the method works better than existing methods.
- This paper also introduces a new benchmark dataset for more comprehensive evaluation.

### Weaknesses
 - The paper proposes various new modules, but does not delve into ablation studies that isolate and analyze the impact of each component/module within the framework.
- The teaser figure shows unintended changes in the horse's view and texture, despite no prompt specifying these edits. This suggests some loss of subject-specific details. This also contradicts the authors' claim in Figure 14, where they state that without fine-tuning, the model cannot generate novel poses or views. It raises questions about the proposed method's control over subject attributes.
- Table 1 shows only marginal improvements in metrics that measure overall image quality and background. This makes the advantage unclear. Also, the paper should include some notes on each metric. For example, CLIP score could mean either prompt alignment (image-text) score or the subject-level image similarity (image-image) score.
- The dependency on high-quality masks can limit practicality in fully automated editing and in situations where generating precise masks is difficult.
- Some recent related works in the same domain:
	ProxEdit: Improving Tuning-Free Real Image Editing with Proximal Guidance
	EmuEdit: Precise Image Editing via Recognition and Generation Tasks

### Questions
Could the authors provide an ablation study to isolate and analyze the impact of each component? Also, could the authors clarify the limitations of pose/view manipulation in the current framework?

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
The method proposes mask-guided image editing.

### Strengths
Editing performance is improved from baselines.

### Weaknesses
The method lacks novelty. The method of self-attention injection is already well-known method, and usage of mask-guidance is not a novel method. It seems the proposed method is combination of framework of Diffedit (automatic mask generation) and self-attention injection similar to Plug-and-play diffusion features. I think there is no new or technical idea which can further contribute to the generative AI field.

Also, the quality of output edited images are not satisfactory. The paper proposes that the editing method can be applied to all kinds of editing, but it seems that the outputs can be obtained with using baseline methods with proper parameter control.

### Questions
See Weakness

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
5

### Summary
This paper proposes Context-Preserving Adaptive Manipulation (CPAM) for zero-shot real image editing. It includes three main components: 1) a preservation adaptation module that adjusts self-attention mechanisms to effectively preserve and independently control the object and background; 2) a localized extraction module that applies attention to the spatial pixels of the extracted object from the feature query to the target prompt, while the remaining pixels attend to a null text prompt; and 3) various masking strategies tailored to different editing needs.

### Strengths
1. This paper is well-written and esay to read. 
2. The performance of this paper is promising, achieving state-of-the-art results across various metrics.
3. The insights on multi-text guided synthesis (Fig. 2 and Sec. 3.4) are interesting.

### Weaknesses
1. Lacking of experimental evidence supporting the claim that "null text does not affect the output," as stated in Lines 206-211. 
2. The notation "t > T, l > L" in Fig. 3(b) is inconsistent with "s > S, l > L" in Eq. 2, and Fig. 3 requires further refinement.
3. The proposed method, CPAM, seems incremental because: 1) the main design, "Preservation Adaptation," is highly similar to "Mask-Guided Mutual Self-Attention" from the MasaCtrl paper; and 2) the masking strategy, which aggregates cross-attention maps across all steps and layers, also closely resembles that of MasaCtrl in Sec. 4.2. 
4. Lacking of ablation studies to validate the effectiveness of the proposed modules; only results under different classifier-free guidance scales are presented in Sec. A.1.

### Questions
I look forward to your response to address my concerns outlined in the 'Weaknesses' section. I will adjust my score based on your reply and the ratings from the other reviewers.

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
3

### Summary
This paper proposes a Context-Preserving Adaptive Manipulation method for real image editing. Preservation adaptation module and localized extraction module are introduced for keeping objects maintained and mitigating interferences. Additionally, some mask-guidance strategies and a new benchmark are mentioned. The proposed method demonstrates better results in terms of context maintenance.

### Strengths
1. The insight of the paper is good, and the implementation of image editing with background preservation is close to the actual application scenarios.
2. The visualized results show that the proposed method achieves the desired effect.
3. The structure of the paper is well organized.

### Weaknesses
1. Although the problems attempted to be solved are interesting, the solutions lack innovation. The proposed method appears to be an incremental combination of existing techniques rather than a novel approach. The core modules, while functional, do not introduce fundamentally new mechanisms for context-preserving image manipulation. The preservation adaptation module, for example, seems to be a variation of attention-based methods already present in the literature, and the localized extraction module appears to be a straightforward application of conditional generation techniques.
2. The additional introduction of mask inputs leads to unfair comparisons with existing methods. Many existing methods aim to achieve similar editing effects without relying on explicit mask guidance. By introducing masks, the proposed method gains an advantage that is not available to other methods, making a direct comparison of performance difficult and potentially misleading. This makes it unclear if the improvements are due to the method itself or simply due to the additional mask input.
3. The proposed mask-guidance strategies are rule-based and not flexible enough to cope with diverse editing needs. The rule-based approach, while simple to implement, may not generalize well to complex or unusual editing scenarios. The lack of adaptability in the mask-guidance strategy could limit the method's applicability in real-world scenarios where user intent and editing requirements can vary significantly. The reliance on predefined rules may also hinder the method's ability to handle nuanced or subtle editing tasks.
4. Inadequate visual comparison of ablation experiments. The ablation study lacks sufficient visual evidence to demonstrate the contribution of each module. The absence of clear visual comparisons makes it difficult to assess the impact of each component on the overall performance of the method. The reader is left to infer the effectiveness of each module based on limited visual information, which is not ideal for a method that relies heavily on visual results.
5. The structure and presentation of figure 2 is not sufficiently clear. The figure is difficult to understand, and the caption does not provide enough explanation to clarify the process being illustrated. The lack of clarity in the figure makes it difficult for the reader to grasp the method's overall workflow and the interaction between its different components. The figure needs to be redesigned to improve its clarity and readability.
6. English expression needs improvement: “retaining object is true”, “where s, l, S = 3, L = 8 denotes” and “element-wise dot product”.

### Questions
1. How much does the accuracy of the input mask affect CPAM?
2. What will be the result of acquiring masks for CPAM inputs by means of adaptive perception or reference segmentation?

### Soundness
2

### Presentation
2

### Contribution
2

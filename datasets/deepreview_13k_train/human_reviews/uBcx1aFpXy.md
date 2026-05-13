# OmniBooth: Learning Latent Control for Image Synthesis with Multi-modal Instruction

- Decision: Reject
- Scores: 5, 6, 6, 6

## Abstract
We present \textbf{\mname}, an image generation framework that enables spatial control with instance-level multi-modal customization. For all instances, the multi-modal instruction can be described through text prompts or image references. Given a set of user-defined masks and associated text or image guidance, our objective is to generate an image, where multiple objects are positioned at specified coordinates and their attributes are precisely aligned with the corresponding guidance. This approach significantly expands the scope of text-to-image generation, and elevates it to a more versatile and practical dimension in controllability. In this paper, our core contribution lies in the proposed latent control signals, a high-dimensional spatial feature that provides a unified representation to integrate the spatial, textual, and image conditions seamlessly. The text condition extends ControlNet to provide instance-level open-vocabulary generation. The image condition further enables fine-grained control with personalized identity. In practice, our method empowers users with more flexibility in controllable generation, as users can choose multi-modal conditions from text or images as needed. Furthermore, thorough experiments demonstrate our enhanced performance in image synthesis fidelity and alignment across different tasks and datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces OmniBooth, a novel framework for image generation that leverages multimodal instructions to enable spatial and instance-level control. The method integrates 1) instance prompt, 2) reference image, 3) mask, and 4) global prompt to manipulate specific image attributes, allowing for precise and detailed control over the generated images. The core innovation is the use of a latent control signal that acts as a unified representation for various modalities, enhancing both flexibility and precision in image synthesis. It successfully integrates multimodal control signals into the latent to finetune the Diffusion Unet, similar to ControlNet, to enable more fine-grained controllability over the generated content.

### Strengths
+ The paper is well-written, exhibiting a clear logical flow and effective illustrations, particularly in Figures 1 and 2, which enhance understanding.

+ The framework demonstrates competitive generative performance compared to established baselines such as InstanceDiffusion and ControlNet.

+ The model offers precise and fine-grained control over generated content, which is highly valuable for practical applications.

+ The model shows strong capability in inverting and fusing the reference image into the mask within the generated image, as evidenced by the attractive results in Figure 4.

### Weaknesses
 - The paper's novelty and technical contribution appear limited. It primarily presents an application-driven approach that combines popular techniques such as latent diffusion, ControlNet, and DINO into a cohesive framework. While the application task is intriguing, the overall novelty is not significant.

- Some explanations lack clarity. For instance, in lines 178-179, the authors state, "we randomly drop 10% of the spatial embedding​ and replace it with the DINO global embedding​ to encode global identity," but do not clarify the rationale for injecting the global embedding. Additionally, there is no ablation study on the ratios of global embedding used.

- The complexity of the framework suggests that it requires numerous manual adjustments and engineering tricks to function effectively.

- The paper fails to reference some highly relevant works in the area of unified and multi-condition controllable image generation, such as:

[1] UniControl: A Unified Diffusion Model for Controllable Visual Generation in the Wild (NeurIPS 23).

[2] Uni-ControlNet: All-in-One Control to Text-to-Image Diffusion Models (NeurIPS 23).

- The metrics presented in Table 2 would benefit from the inclusion of up and down arrows to indicate performance trends.

### Questions
What is the impact of resolution for generated content? The condition latent should be aligned with the mask spatially but it is down-sized. In this way, how to enable the precise content control around the edge of each region within the mask? Are there any requirements of the the size (ie, >=10 px) of the object mask?

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
2

### Summary
The paper introduces OmniBooth, an image generation framework that supports spatial control and instance-level customization through multi-modal instructions. The goal of the framework is to generate images based on user-defined masks and associated text or image guidance, where multiple objects are positioned at specified coordinates, and their attributes are precisely aligned with the corresponding guidance. Through experiments, the authors demonstrate the method's performance enhancement in image synthesis fidelity and alignment across different tasks and datasets.

### Strengths
1. Propose a comprehensive image generation framework achieving multi-modal control, including textual descriptions and image references.
2. Introduced latent control signals, enabling highly expressive instance-level customization within the latent space.
3. Demonstrate the method's ability to achieve high-quality image generation and precise alignment across various settings and tasks through extensive experimental results.

### Weaknesses
1. The image condition might be too strong and it is not usually utilized in real world. Maybe layout bounding boxes are more straightforward and enable more flexible generation. For example, if training with bounding boxes as conditions, the content is only required to be generated within the bounding boxes it would be possible to realize generating diverse images. However, training with masks as conditions not only requires providing precise binary masks but also limits the diversity of generated results because the positions and the edges are all fixed by the conditions.
2. Has the author considered reference net [1]? This model architecture might be more suitable for your target because it provides spatial information and is widely used in situations where low-level and precise information in the given pictures is required to preserve. I think this architecture is based on attention, which should be easier to train. I think directly injecting features as described in your paper might destroy the original information contained in the image and I want to discuss this possible problem with the authors.

### Questions
see weakness

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
The paper presents OmniBooth, a method providing instance-level spatial control for text-to-image models. In addition to a global textual prompt, users can provide instance-level masks paired with a text prompt or image reference for each instance, guiding the generation to follow the mask. The authors introduce a Latent Control Signal, a feature map that spatially integrates textual and visual conditions. OmniBooth achieves fine-grained control over the generation, aligning with the user-defined mask and attributes.

### Strengths
- The paper addresses the critical task of fine-grained instance control for image generation and proposes support for instance-level conditioning on both text and image inputs.

- The authors introduce an interesting methodology for combining multi-modal inputs into a single Latent Control Signal. The use of ROI Alignment for spatial warping of the image condition is particularly elegant.

- The qualitative results are strong, demonstrating the ability to generate objects in precise locations.

- The writing is clear, and the paper includes numerous qualitative examples.

### Weaknesses
 - The qualitative results in Table 1 are not very convincing, showing comparable results to existing work (InstanceDiff). Additionally, there are discrepancies between the InstanceDiff performance in your Table 1 and its reported performance in Table 1 of their paper. For instance, they report an AP50_mask score of 50.0 on the COCO validation set, while you report a score of 47.0. What is the reason for this difference?

- Missing details:
    * How many images were used for training?

    * Do the instance-image inputs always perfectly align with the mask during training? If so, why would the model handle instance-level images that don’t correspond exactly to the mask?

    * How does subject-driven image generation work (i.e., personalization)? Does the user need to provide a mask?

- Subject-driven image generation: comparisons to IP-Adapter in Table 2 are missing. Additionally, Dreambooth-LoRA is a more widely used approach than plain Dreambooth, so it would be better to compare with it.

- Missing citation in the related work:
Be Yourself: Bounded Attention for Multi-Subject Text-to-Image Generation, Dahary et al.

- The analysis is limited. How does the model handle OOD input masks, non-realistic image styles, etc.?

typos:
- L49: omnipotent of controllability -> omnipotent controllability

### Questions
- How does your method handle unlikely positions for instances? For instace, a dog flying in the sky?
- What happens when the mask does not match the instance description? For example, a rectangular mask for a person.
- Your method was trained and evaluated on COCO panoptic segmentation masks. How does it handle segmentation masks from other distributions? How well can it manage missing or noisy masks?

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
5

### Summary
This paper introduces the OMNIBOOTH method, which allows users to perform spatial control with instance-level multi-modal (i.e., text and image) customization. Specifically, OMNIBOOTH integrates multi-modal instructions into a unified control latent space, which is then injected into the Stable Diffusion model via ControlNet. The proposed unified control latent represents a novel innovation, and experimental results indicate that OMNIBOOTH outperforms previous methods in terms of performance. The structure of the paper is well-organized, and the writing is clear and easy to understand.

### Strengths
The proposed unified control latent is novel. Experimental results demonstrate that the method described surpasses previous state-of-the-art approaches. The structure of the entire paper is clear, and the content is easily comprehensible.

### Weaknesses
I think that this article currently has no significant issues; however, I still have some reservations. Please see the Question Section for further details.

### Questions
Q1、I would like to note that instance-level multi-modal customization was previously implemented in MIGC++[1]. Could you clarify how OMNIBOOTH differs from or improves upon MIGC++?

Q2、How effective is OMNIBOOTH in generating counterfactual scenarios? For example, what would be the outcome if the effect in Fig.4(a) were replaced with a 'flame'? Could you provide additional examples of generated counterfactual scenarios?

Q3、Which specific examples benefit most from the improvement in edge loss? Could you provide some visual comparison charts?

Q4、In your opinion, if fine-tuning or retraining is permitted, what would be the effectiveness of using unified control latent when specifying instance positions with bounding boxes, especially in scenarios with overlapping instances?

[1] MIGC++: Advanced Multi-Instance Generation Controller for Image Synthesis.

### Soundness
3

### Presentation
3

### Contribution
3

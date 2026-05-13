# GroundingBooth: Grounding Text-to-Image Customization

- Decision: Reject
- Scores: 6, 6, 6, 3, 6

## Abstract
Recent studies in text-to-image customization show great success in generating personalized object variants given several images of a subject. While existing methods focus more on preserving the identity of the subject, they often fall short of controlling the spatial relationship between objects. In this work, we introduce GroundingBooth, a framework that achieves zero-shot instance-level spatial grounding on both foreground subjects and background objects in the text-to-image customization task. Our proposed text-image grounding module and masked cross-attention layer allow us to generate personalized images with both accurate layout alignment and identity preservation while maintaining text-image coherence. With such layout control, our model inherently enables the customization of multiple subjects at once. Our model is evaluated on both layout-guided image synthesis and reference-based customization tasks, showing strong results compared to existing methods. Our work is the first work to achieve a joint grounding on both subject-driven foreground generation and text-driven background generation. The project page is available at \url{https://groundingbooth.io}..

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a framework which allows users to customize an image by 1) specifying the position (layout) of the object, and 2) providing a reference image of the object. It supports either single object customization or multi-object customization. They design a grounding module to ground the provided image with text entities. The produced grounding tokens are then later used as the condition in their diffusion model to generate the final image. They conduct experiments on Dreambench and MS-COCO and show that their methods could produce high quality image while preserving the detail of the user-specified (reference) images.

### Strengths
1. The visualization results show that the proposed method can effectively preserve the identity of reference image while generating plausible images.
2. The proposed method is able to simultaneously handle multi-object synthesis even with complex layout.

### Weaknesses
1. My main concern is that the authors claim that they are able to ground the text entities during generation. While the CLIP-T score of the model indicates that the generated image is less coherent with the text comparing to other baseline methods. This discrepancy raises questions about the effectiveness of the grounding mechanism, as a core claim is that the model can effectively align generated content with text descriptions. A lower CLIP-T score suggests that the model struggles to maintain text-image coherence, which undermines the grounding argument.
2. While the paper claimed that they can control the spatial relationship between objects. It is difficult to evaluate this argument given the layouts are pre-determined. The lack of variability in layout input limits the ability to assess the model's true capacity for spatial control. If layouts are fixed, it's unclear how the model would perform with more complex or user-defined spatial arrangements. This raises questions about the generalizability of the model's spatial control capabilities.
3. How are the metrics computed? For example, when computing the CLIP-I score, do you only consider the image similarity between the reference object and the corresponding region in the generated image? If so, how do you extract the corresponding region? More details of how the metrics are computed (CLIP-I, DINO, CLIP-T) could improve the clarity of the paper. The absence of precise details regarding the metric calculation makes it challenging to reproduce results and evaluate the method's performance fairly. It is crucial to understand how the reference object regions are isolated and compared with the generated image to fully assess the validity of the reported scores.

### Questions
1. For multi-objects cases, is each box in the layout assigned to an associated object label?
2. In your experiments, are all the layouts pre-determined or only the layout of the reference object is given?

### Soundness
2

### Presentation
2

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
The paper proposes GroundingBooth, a model for grounded text-to-image customization. It aims to place subjects received in input (marked with bounding-boxes in images) in new backgrounds (described in the prompt), while maintaining the identity and spatial location of the subjects. The authors show GroundingBooth is capable of generating complex requests while preserving the subjects in the input images (e.g., “a [stuffed animal] and a [vase] with [plant] and [vintage lantern] on a quaint balcony”)

GroundingBooth incorporates a new Masked Cross Attention module in each block of the U-Net (Stable Diffusion 1.4’s). In addition to input from the existing Cross Attention layer, the masked layer receives as input DINO-2 features of the subject images received in the input. GroundingBooth is trained this way on a dataset curated from MVImgNet. 

Finally, the method is tested and compared to a few existing baselines, using automatic measurements such as CLIPScore and DINO, and a human study.

### Strengths
* The paper is well written and presented nicely
* The method improves over the baselines it does test (see first weakness)
* Such model can be useful in many real-life applications

### Weaknesses
 * The paper does not cover “Break-A-Scene: Extracting Multiple Concepts from a Single Image” by Avrahami et al (2023). In this work, they extract concepts from an image using textual inversion, and use it to embed them in new images. They too work with masks and can even accept them from the user as input. This is especially important since the sentence before last in the abstract states “Our work is the first work to achieve a joint grounding of both subject-driven foreground generation and text-driven background generation”, which makes this imprecise. More importantly, the difference between these projects should be clearly stated. What does this work do that Break-A-Scene does not?

 * The use of Fourier embedding should be explained. What makes it suitable to this task?

 * The paper uses SD-1.4, which is an older model. The authors should justify why they did not use more recent architectures, such as transformer-based models like FLUX or SD-3.

### Questions
* Why does this method use SD-1.4 when there are so many newer / stronger models? Is there some limitation in using them?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces GroundingBooth, a novel framework designed to enhance text-to-image customization by enabling precise spatial control of both subjects and background elements based on textual prompts. While existing models in text-to-image generation maintain subject identity, they often lack control over spatial relationships. GroundingBooth addresses this gap by implementing zero-shot instance-level spatial grounding, enabling precise placement of both foreground subjects and text-defined background elements.
GroundingBooth supports complex tasks such as multi-subject customization, where multiple subjects and background entities are positioned according to input bounding boxes. Experimental results demonstrate its effectiveness in layout alignment, identity preservation, and text-image alignment, outperforming current approaches in controlled image generation.

### Strengths
Unlike many existing layout-guided image generation methods that handle only single subjects, GroundingBooth supports multi-subject customization. This versatility broadens its applicability, especially for generating images where complex layouts and multiple subjects are essential.

### Weaknesses
1. InstanceDiffusion does not exist in baseline comparisons. Despite its notable relevance with capabilities for free-form language conditions per instance and flexible instance localization methods (single points, scribbles, and bounding boxes), InstanceDiffusion is missing from both our quantitative and qualitative baselines. 
2. FID, in contrast to other works dealing with similar tasks, is not suggested in this paper.
3. Qualitative results demonstrating the model's performance on multi-subject generation tasks are notably absent from this paper.

### Questions
1. Previous research in layout-guided diffusion has demonstrated limitations in maintaining visual coherence when objects exhibit diverse textures. While these approaches often resulted in disharmonious image generation, our proposed method provides users with the capability to directly select and manipulate subjects. A comparative analysis with InstanceDiffusion would be particularly valuable, especially in terms of texture consistency and user control capabilities.
2. Due to the lack of publicly available code and data, an accurate evaluation is difficult to conduct.
3. It remains unclear why the paper emphasizes its zero-shot capability as a key strength even though the methodology clearly includes training procedures within the paper.([L37-40] & [L247-250])

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents GroundingBooth, a method for grounded text-to-image customization. Given a list of subject entities represented by images and text entities represented by textual descriptions, along with bounding-box locations, GroundingBooth aims to generate an image containing all subjects in the specified locations according to their bounding boxes.

### Strengths
* The authors tackle the important task of grounded image generation with both text and image localization conditions.
* The writing is clear, making it easy to understand the proposed method.
* The authors combine grounded generation from both reference objects and textual inputs within a single architecture, which is highly relevant for many applications.
* The authors evaluate their method against a variety of prior works and datasets.

### Weaknesses
 * In all the qualitative examples, the generated objects remain in the same pose as in the input image, despite the claim in line 191: “Moreover, our work adaptively harmonizes the poses of the reference objects and faithfully preserves their identity.” Could you provide examples where the input subjects change their pose while maintaining their identity? I would like to see examples where the prompt requires a significant pose change from the input subject.

* The proposed Masked Cross-Attention module was presented in previous works; see, for instance:
[1] Be Yourself: Bounded Attention for Multi-Subject Text-to-Image Generation, Dahary et al. ECCV 2024
[2] InstanceDiffusion: Instance-level Control for Image Generation, Wang et al. CVPR 2024

* Overall, the proposed modules seem to lack novelty. The gated self-attention mechanism is borrowed from GLIGEN, and the masked cross-attention module exists in prior work, such as in [1].

* I find the distinction between “background” and “foreground” objects confusing, as it actually separates objects based on their source (image or text) rather than their position in the background or foreground of the image.

* The quantitative results are not convincing, as GroundingBooth shows lower scores than prior work on several metrics (e.g., Tables 1 and 2). Furthermore, the method's ability to control object size through bounding boxes is not leveraged to address the issue of object size calibration. Specifically, the input bounding boxes could be defined to match the average size of objects generated by personalized text-to-image methods, which would provide a more standardized evaluation and allow for a fairer comparison with methods that do not explicitly control object size.

### Questions
* For personalization of a single subject (Fig. 4, Table 1), how is the bounding box determined? How do you compare with methods that do not require a bounding box as input?
* How well can the method generate interactions between input subjects? For example, could it make the teddy bear wear the red backpack?

### Soundness
3

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
3

### Summary
This paper focuses on improving the accurate generation of spatial relationships between objects and backgrounds when creating personalized object variants. Technically, the authors propose a joint text-image grounding module that encourages both foreground subjects and background objects to adhere to locations defined by input bounding boxes. They also introduce a masked cross-attention layer aimed at preventing the unintended blending of multiple visual concepts in the same location, producing clear, distinct objects. Experiments are conducted on the MVImgNet and LVIS datasets.

### Strengths
1. The paper tackles the task of generating personalized objects based on specific locations, which is an interesting setup.
2. This work proposes integrating reference objects and their location prompts through a grounding module and masked cross-attention.
3. Experiments are conducted on two benchmarks, accompanied by illustrative visualizations.

### Weaknesses
1. The paper primarily focuses on enabling the location-controlled generation of personalized objects, a setting already explored in prior work [3], which the authors seem to overlook. Additionally, the authors introduce a rather complex module to integrate location information but seem to lose focus on core functionalities like layout-to-image generation or personalized object generation. The method's novelty is incremental, as it builds upon existing layout control techniques without substantial advancements in either layout-to-image or personalized object generation tasks.
2. Missing References: Some relevant references in layout-to-image generation, such as [1,2] and subject-driven image generation [4], are absent. The lack of comparison with these methods makes it difficult to assess the true contribution of the proposed approach.
3. There are some limitations in model design. For example, the authors note that in cases where bounding boxes belong to the same class, the model cannot distinguish between a bounding box for a reference object and one for a text entity, leading to misplacement of the reference object. However, the paper does not clarify whether or how the proposed masked cross-attention module addresses this issue. It is unclear how the model differentiates between bounding boxes of the same class, and the paper lacks a detailed explanation of the mechanism.
4. Further analysis is needed on topics such as the maximum number of reference objects supported in a single input and the model’s performance on subject-driven image generation without layout information. The paper does not provide a clear understanding of the model's scalability with respect to the number of reference objects, nor does it explore its performance in scenarios where layout information is absent, limiting its applicability and understanding of its core capabilities.

### Questions
1. Does this work support simpler text-to-image generation, layout-to-image, or personalization tasks?

2. Regarding the illustration of the masked cross-attention layer in Figure 2, is the number of layers determined by the number of reference objects? For example, if there are three reference objects in the input, does that mean three masked cross-attention modules are required? If so, this model design seems unreasonable. Sequential masking could result in information loss in subsequent modules, especially when reference objects have significant overlap.

### Soundness
2

### Presentation
3

### Contribution
2

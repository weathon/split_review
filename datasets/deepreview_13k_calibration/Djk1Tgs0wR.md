# SeeThruAnything: Learning to Remove Any Obstructions Across Distributions

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
Images are often obstructed by various obstacles due to capture limitations, hindering the observation of objects of interest. Most existing methods address occlusions from specific elements like fences or raindrops, but are constrained by the wide range of real-world obstructions, making comprehensive data collection impractical. To overcome these challenges, we propose SeeThruAnything, a novel zero-shot framework capable of handling both seen and unseen obstacles. The core idea of our approach is to unify obstruction removal by treating it as a soft-hard mask restoration problem, where any obstruction can be represented using multi-modal prompts, such as visual semantics and textual commands, processed through a cross-attention unit to enhance contextual understanding and improve mode control. Additionally, a tunable mask adapter allows for dynamic soft masking, enabling real-time adjustment of inaccurate masks. Extensive experiments on both in-distribution and out-of-distribution obstacles show that SeeThruAnything consistently achieves strong performance and generalization in obstruction removal, regardless of whether the obstacles were present during training.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces an in-painting method to remove real-world obstructions from images. The method uses multimodal prompts from a pretrained CLIP model as conditioning to the in-painting transformer model and shows good improvement over prior art.

### Strengths
The paper is well written, the method and architecture is clearly explained and tested on a wide range of benchmarks. The proposed method shows good improvement over recently published methods in the domain.

### Weaknesses
1. The paper does not include any examples of textual prompts. The only examples are in Figure 1 and 3, CLIP text encoder is not explicitly trained on instructions like "Remove the semi-transparent obstruction", and the image-text datasets used to train CLIP models typically have captions describing the foreground which may or may not describe the type of occlusions. It is unclear how the embedding space of CLIP's text encoder is capable of embedding such instructions.
2. The paper does not provide details on CLIP model used for generating multimodal prompts.
3. In Table 4. ablation does not include "visual prompt only" setting. An interesting ablation would be to use different text embedding models apart from CLIP.

### Questions
My main concern with this work is the use of CLIP text encoder, as it is typically not trained on textual instructions as depicted in Figure 1 and 3. is it possible that any text encoder would work in this setup? Also, ablation on textual prompts would be good to have, i.e. what level of detail is necessary in the prompt to achieve a good in-painting result. I am willing to update the score based on the response to above questions.

### Soundness
2

### Presentation
2

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
The article presents SeeThruAnything, a novel zero-shot framework designed to effectively remove various types of obstructions in images. SeeThruAnything employs multi-modal prompts—combining visual and textual inputs—processed through a cross-attention unit for enhanced contextual understanding. It also features a tunable adapter for mask adjustments. Extensive experiments demonstrate that SeeThruAnything excels in both familiar and unfamiliar obstacle scenarios, showcasing strong performance and generalization capabilities in obstruction removal tasks.

### Strengths
1. The paper is well-written and easy to follow.
2. The paper demonstrates that SeeThruAnything is highly effective in removing obstacles, particularly in generalizing to invisible obstacles outside the training distribution. 
3. The paper conceptualizes obstacle removal as a problem of soft and hard mask recovery, offering significant insights into the future research directions of this field. By integrating visual tokens with text tokens, the model’s capacity for generalization in open-world scenarios is substantially enhanced.

### Weaknesses
1. The technical contribution of the paper is limited. The use of multi-modal prompts and mask recovery techniques, although effective, may not significantly depart from established methodologies, suggesting a reliance on existing concepts rather than groundbreaking innovations. Specifically, the paper does not adequately address how the cross-attention mechanism and tunable adapter differ fundamentally from existing attention-based models and mask refinement techniques used in image restoration and segmentation tasks. The novelty of the specific combination is not sufficiently justified, and the paper lacks a detailed analysis of the architectural choices and their impact on performance.
2. Generalization Limitation. While SeeThruAnything demonstrates the capability to remove unseen obstacles, these obstacles are often fundamentally similar in nature (e.g., raindrops and rain streak, fences and yarn). This is underscored by the observation that the performance of WGWSNet and PromptIR on rain streaks and strokes is nearly comparable to, or even surpasses, that of SeeThruAnything. Furthermore, the paper does not provide a rigorous analysis of the types of unseen obstacles where the method fails, nor does it explore the limitations of the soft mask recovery approach in handling complex or highly irregular obstructions. The performance gains, while present, do not consistently demonstrate a significant advantage over existing methods, particularly when considering the increased model complexity.

### Questions
As you mentioned, the original configuration of other methods cannot achieve zero-design tasks. How do you give them this ability?

### Soundness
3

### Presentation
3

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
This paper proposes a new Obstruction Removal method SeeThruAnything to reconstruct a clear original image given a degraded image and the estimated occlusion mask as input. To deal with different obstructions with or without ambiguous boundaries, SeeThruAnything utilize a transformer-based tunable adapter to convert hard masking to soft masking and use different maskings for different obstructions during inference. To better recover the original clean image, this paper also utilizes CLIP to extract multi-modal information from corrupted images and text commands like "remove semi-transparent obstructions" as a condition for their network. A cross-attention is used to inject this multi-modal information into their model. The proposed method obtains competitive performance compared to SOTA on seen obstructions and SOTA performance on unseen obstructions.

### Strengths
1. The proposed method is quite simple and well motivated, which has a potential to become a common baseline for future works in this field.
2. The proposed method obtains competitive performance on seen obstructions and SOTA performance compared to previous methods.

### Weaknesses
1. The proposed tunable mask detector seems to be heavy. It would be best to mention the number of parameters and the flops for your method and the compared method so that we can distinguish the performance improvement brought by the increasing parameters.
2. The proposed method use the corrupted images with obstructions removed as input. The obstructions are removed according to inaccurate estimated obstruction masks. However, previous works mainly take degraded images with unremoved obstructions as input. There is no ablation study to prove the advantage of your design.
3. The images and texts in Figure 1 might be too small. It is difficult to distinguish the comparison in figure 1.
4. The paper does not specify how the mask is obtained, particularly if the mask is from SAM2. The method description lacks details on how SAM2 is used, whether in automatic or manual mode, and how the input points or bounding boxes are determined for manual mask creation.
5. The contrastive fine-tuning of the CLIP text encoder lacks justification. The paper does not explain how this fine-tuning benefits performance, specifically how it improves the model's ability to interpret user commands or apply soft masking. The paper should include an analysis of how the fine-tuning affects the semantic alignment between user commands and core commands.
6. The generalizability of the proposed method is questionable. The limitations for handling large areas of occlusions suggest that the soft masking approach may not be robust for significant occlusions. This raises concerns about the practical applicability of the method in real-world scenarios with large obstructions.

### Questions
1. As the method is mainly tested on synthetic corrupted data, how does it perform for images with multi-type obstructions?
2. What mask detector is used? Is it the same one for compared methods?
3. What is the exact text command used in your method? Do you use different text commands for different obstructions? How does it perform when only using some consistent text commands like "remove obstructions".

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a zero-shot obstruction removal framework to handle both seen and unseen obstructions in images. The idea is to formulate obstruction removal as a soft-hard mask restoration task, leveraging multi-modal prompts to enhance generalization. The framework incorporates a tunable mask adapter that dynamically refines inaccurate masks during the restoration process. The authors show that their method achieves superior performance over state-of-the-art techniques across a wide range of both in-distribution and out-of-distribution obstructions, demonstrating its flexibility and robustness across diverse occlusions.

### Strengths
1. The introduction of the soft-hard mask prediction task intuitively enhances the model’s generalization ability, making it more adaptable to various obstruction types.
2. The paper conducts thorough experiments to validate the effectiveness of the multiple components of the framework.

### Weaknesses
1. While the generalization largely stems from the mask prediction process, the paper lacks a detailed analysis of the quality and generalizability of the predicted masks. Are there any quantitative metrics to evaluate mask quality on both seen and unseen objects? Specifically, it is unclear how the mask detector performs in a zero-shot setting, and how sensitive the model is to the choice of training obstructions.
2. There is no comparison with in-painting methods in experiments. It would be valuable to see a comparison with more recent diffusion-based in-painting methods. For example, [1,2].
3. The performance on seen categories is not consistently superior to prior works.

### Questions
1. In cases where an image contains multiple obstructions (e.g., raindrop and power cable), how does the model handle prompts to remove only one type of obstruction? Can it selectively remove the specified obstruction without affecting others?
2. In Sec 5.1, the patch sizes mentioned (128, 160, 192, 256) seem unreasonable large. Should this refer to the image resolution instead?
3. Is the model capable of handling obstructions that exhibit significant differences from seen obstructions, such as in the case of reflection elimination? Can the authors provide some visualizations with existing datasets or real-world photos?
4. How do the authors initialize the model? Are pre-trained weights beneficial?
5. What is the model size, and how does it perform in terms of inference speed?

### Soundness
3

### Presentation
4

### Contribution
2

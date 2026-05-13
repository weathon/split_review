# InstantSwap: Fast Customized Concept Swapping across Sharp Shape Differences

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Recent advances in Customized Concept Swapping (CCS) enable a text-to-image model to swap a concept in the source image with a customized target concept.
However, the existing methods still face the challenges of \textit{\textbf{inconsistency}} and \textit{\textbf{inefficiency}}. They struggle to maintain consistency in both the foreground and background during concept swapping, especially when the shape difference is large between objects. 
Additionally, they either require time-consuming training processes or involve redundant calculations during inference.
To tackle these issues, we introduce \ours, a new CCS method that aims to handle sharp shape disparity at speed.
Specifically, we first extract the bbox of the object in the source image \textit{automatically} based on attention map analysis and leverage the bbox to achieve both foreground and background consistency. For background consistency, we remove the gradient outside the bbox during the swapping process so that the background is free from being modified. 
For foreground consistency, we employ a cross-attention mechanism to inject semantic information into both source and target concepts inside the box. 
This helps learn semantic-enhanced representations that encourage the swapping process to focus on the foreground objects.
To improve swapping speed, we avoid computing gradients at each timestep but instead calculate them periodically to reduce the number of forward passes, which improves efficiency a lot with a little sacrifice on performance. 
Finally, we establish a benchmark dataset to facilitate comprehensive evaluation. Extensive evaluations demonstrate the superiority and versatility of \ours.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes InstantSwap, a training-free framework for Customized Concept Swapping(CCS). CCS works on transfers the target concept described by target images and target prompt to the location of source concept in the source image. This paper utilizes the cross attention map and the self-attention map of U-Net in diffusion model for source image and source prompt to extract bounding box of the source concept automatically. Then they apply the bounding box to filter the gradients in background from a refined SDS loss. In this way, they can achieve an optimization preserving the background information. To emphasize the concepts in the images, they also use the semantic information of corresponding prompts and the estimated bbox to augment representation of concepts. Additionally, this paper also presents a step-skipping gradient update strategy which reuse previous gradients for current iteration to increase the inference speed. Experiments present the advantages of the proposed method over previous works.

### Strengths
1. The proposed method presents a complete pipeline for improve effectiveness and efficiency in Customized Concept Swapping(CCS) task.
2. The proposed method obtains state-of-the-art performance compared to previous works.
3. This paper also contributes benchmark for Customized Concept Swapping(CCS) task.

### Weaknesses
1. Theoretical analysis about why we can directly apply mask on gradient computing is missing. Masking will produce a distribution shift, why it can converge to a reasonable solution requires some analysis.
2. How combining self-attention and cross-attention for automatic bbox generation affects the performance seems not be discussed.
3. How the number of target images affect the performance is not mentioned.

### Questions
1. How does the proposed method work for multi-object scenario?

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
Recent advances in Customized Concept Swapping (CCS) enable text-to-image models to swap concepts, but existing methods struggle to maintain foreground and background consistency, particularly with large shape disparities, and often require time-intensive processes. InstantSwap addresses these challenges by using bounding box analysis and cross-attention mechanisms to enhance both foreground and background consistency while limiting modifications to the background and enhancing foreground focus. This method reduces computation time by periodically calculating gradients, enhancing efficiency with minimal performance loss, and extensive evaluations show InstantSwap's effectiveness and adaptability.

### Strengths
The motivation is clear.

The results appear promising and solid.

The experiments are thorough.

The writing is easy to follow.

### Weaknesses
For each concept replacement, the method first needs to train a DreamBooth model and then perform score distillation, which is time-intensive.

Both the source and reference branches use DreamBooth-tuned UNet. It would be beneficial to validate the method using text inversion to demonstrate its generalization capability.

What about the failure cases?

It's interesting that the method can handle concepts with significant shape changes. If the original image's concept is very small, resulting in a small bounding box, how does the target image’s foreground region expand without additional processing?

### Questions
Please see the weakness

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
This paper proposes a training-free customized concept swapping framework. It derived bounding boxes from the Attention to map to help preserve the background information during optimizing the latents. The gradient is updated periodically for a better tradeoff between quality and inference time. A semantic enhanced module is further proposed to improve foreground consistency. Both quantitative and qualitative experiments are conducted to validate the effectiveness of this approach.

### Strengths
- The experimental results are comprehensive and promising.

- A benchmark dataset designed for CCS task is proposed.

- The writing is fluent and easy to understand.

### Weaknesses
 - It would be better to give an introduction on the customization methods. This introduction could also help readers to understand the difference brought by integrating customization method into image editing.

- Since this approach needs to modify the cross attention, I wonder if it could be applied to the DiT-based architectures, like SD3.

- It seems that the semantic-enhanced operation enhances the semantic of the source/target object while mitigates the object’s interaction with the surrounding objects and background. Will it make the image unnatural?

- I am curious why P2P fails completely at this task. From the results displayed in the paper of P2P, I would expect P2P to be able to fulfill the task of changing objects. Is it because the customization method does not fit well with P2P?

### Questions
Please see the questions in weakness section.

### Soundness
2

### Presentation
2

### Contribution
2

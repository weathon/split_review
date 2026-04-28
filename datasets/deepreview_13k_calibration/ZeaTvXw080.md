# Add-it: Training-Free Object Insertion in Images With Pretrained Diffusion Models

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
\vspace{-3pt}
Adding Object into images based on text instructions is a challenging task in semantic image editing, requiring a balance between preserving the original scene and seamlessly integrating the new object in a fitting location. Despite extensive efforts, existing models often struggle with this balance, particularly with finding a natural location for adding an object in complex scenes. We introduce \ourmethod, a training-free approach that extends diffusion models' attention mechanisms to incorporate information from three key sources: the scene image, the text prompt, and the generated image itself. Our weighted extended-attention mechanism maintains structural consistency and fine details while ensuring natural object placement. Without task-specific fine-tuning, \ourmethod achieves state-of-the-art results on both real and generated image insertion benchmarks, including our newly constructed "\additing Affordance Benchmark" for evaluating object placement plausibility, outperforming supervised methods. Human evaluations show that \ourmethod is preferred in over 80\% of cases, and it also demonstrates improvements in various automated metrics.
Our code and data will be available at: 
\texttt{\href{https://research.nvidia.nvidia

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Add-it, a novel, training-free method for inserting objects into images based on text instructions. The approach extends multi-modal self-attention mechanisms in Diffusion Transformer to incorporate a source image as an additional input, reweighting the attention values to effectively balance information between source and target images. Furthermore, the method transfers structural details from the source image and blends the latent representation with guidance from SAM2. To validate Add-it, the authors propose a new benchmark and a custom evaluation metric, demonstrating its effectiveness.

### Strengths
- **Clarity and Presentation.** The paper is well-written and easy to follow. The figures are thoughtfully designed and effectively illustrate the proposed method.
- **Visual Quality.**  The results are visually compelling; the added objects are integrated seamlessly, with the original image's details preserved well.

### Weaknesses
 - **Dataset Size.** The evaluation affordance dataset is relatively small, containing only 200 images, which may limit the generalizability of the findings.

- **Computation Speed.** The need to run additional models (e.g., SAM2) for mask estimation could impact processing speed, especially in comparison to the original FLUX. It would be valuable to provide a direct comparison regarding computational efficiency.

- **Prompt Complexity.** *Add-it* requires text prompts for target images and thus may introduce additional complexity. Previous methods like InstructPix2Pix or MagicBrush may offer a more straightforward user experience.

### Questions
- Did the authors experiment with using a coarse mask as an input for SAM2? If so, how does it perform compared to point-based prompts?
- In the ablation study, the authors claim that setting \gama = auto yields the best results. However, Figure 7(a) appears to show a peak at approximately 1.07, which surpasses the performance of the auto setting.

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
3

### Summary
Add-it leverages pretrained diffusion models to insert objects into images based on text prompts, without requiring any training. 
The method extends the multi-modal attention mechanism to incorporate information from the source image, prompt, and generated image, resulting in natural object placement.  
Add-it also introduces a novel “Additing Affordance Benchmark” to evaluate object placement plausibility.

### Strengths
1. The paper proposes a novel training-free method called Add-it for adding objects to both real and generated images using simple textual prompts. The method doesn't require fine-tuning or training a separate model for object insertion. Instead, it directly leverages the knowledge embedded within pretrained text-to-image diffusion models. 

2. Add-it extends the multi-modal attention mechanism of diffusion models to carefully balance information from three key sources: the source image, the text prompt, and the generated image itself. 

3. Add-it introduces a novel Subject-Guided Latent Blending mechanism to preserve the fine details of the source image while enabling necessary adjustments like shadows and reflections.

### Weaknesses
1. Lack of comparison with the existing methods for adding objects [1,2]. Both of them have codes and have been released half a year ago.

2. The paper doesn't fully discuss the potential limitations of relying on SAM-2 for refining the object mask. SAM is a large powerful segmentation model, might not always accurately capture the desired object boundaries. There are also papers using self-attention and cross-attention maps to relieve this requirement [3,4].

3. The paper only briefly mentions potential biases inherited from the pretrained diffusion models. These biases could impact the object placement in unexpected ways. For instance, the model might consistently place objects associated with certain demographics in specific locations based on learned biases, potentially leading to unfair or discriminatory outcomes.

### Questions
Please refer to the weakness. Anyway, from my view as a Diffusion Models researcher, adding objects to images is a pretty hard task. Although this paper is having several limitations, I still like the basic idea.

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
4

### Summary
This paper introduces Add-it, a training-free method leveraging extended attention mechanisms to seamlessly integrate objects into images from text instructions. Besides, it shows a new benchmark for evaluating object placement plausibility.

### Strengths
1. The writing is concise, which makes the paper easy to follow and understand.
2. The method is straightforward and innovatively.
3. The experimental results substantiate the effectiveness of the method proposed in this paper.

### Weaknesses
1. The newly introduced benchmark's advantages over other benchmarks are not clearly articulated, and there is a lack of comparison with more existing benchmarks, like MagicBrush. 
2. The paper lacks comparison with traditional image quality metrics such as FID and IS, which are commonly used to evaluate the quality of generated images in terms of their realism and diversity.
3. Moreover, while a new benchmark is proposed, there seems to be a scarcity of details regarding it in the paper.

### Questions
1. Could you please briefly outline the advantages of the benchmark you've proposed over the existing benchmarks? It would be particularly helpful if you could illustrate these advantages with some statistical data.
2. Have you experimented with modifying the input to incorporate multiple target objects, or just edit it? eg. in the second line of the fig 6 in your paper, the prompt change to "The man is holding a shopping bag in the rain." or "The man wears a red shirt".
3. Although your paper focuses on the 'Add-it' method, I'm curious to know if this editing approach could also be adapted to perform operations like 'remove something' from the image.
4. could you please provide more details about Structure Transfer?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a tuning-free method for adding objects into images based on text instructions. They introduce Add-it, a training-free approach that extends the attention mechanisms of diffusion models to incorporate information from three key sources: the scene image, the text prompt, and the generated image itself. The experimental results show that it effectively maintains structural consistency and fine details while ensuring natural object placement compared to existing approaches.

### Strengths
1. The paper proposes a training-free method that achieves state-of-the-art results in object insertion.
2. The analysis of MM-DiT Attention Distribution is interesting and introduces an effective mechanism to control their contribution.
3. The paper Introduces a benchmark to assess the plausibility of object insertion.
4. The writing and presentation are mostly clear and easy to follow. The authors provide hyperparameters and detailed settings used in experiments and method implementation, which is helpful for reproducibility.

### Weaknesses
The proposed techniques are incremental, lacking sufficient novelty to make a significant contribution to the field. The WEIGHTED EXTENDED SELF-ATTENTION, STRUCTURE TRANSFER, and SUBJECT GUIDED LATENT BLENDING methods are commonly used in Unet-based free-tuning image editing [1,2,3,4,5], and the modifications presented here do not represent a substantial advancement.

- In the WEIGHTED EXTENDED SELF-ATTENTION section, the approach of applying a coefficient to the key is similar to existing techniques in the community, such as scaling text embeddings [1]. This makes the proposed contribution appear incremental rather than innovative. Specifically, the method does not introduce a novel mechanism for weighting, but rather applies a known technique to a different input (attention keys) without a clear justification for why this approach is superior to existing weighting strategies. The lack of a comparative analysis against other weighting methods further weakens this claim.
- In the STRUCTURE TRANSFER section, the proposed technique shows only minor improvements compared to SDEdit [2], without introducing a fundamentally new approach. The method essentially leverages the noise structure from the source image, which is a well-established technique. The paper does not provide a detailed analysis of the limitations of SDEdit that this method overcomes, nor does it explore alternative structure transfer methods that might offer better performance. The lack of ablation studies to isolate the impact of the proposed structure transfer method makes it difficult to assess its true contribution.
- In the SUBJECT GUIDED LATENT BLENDING section, similar blending operations have been previously demonstrated in [3, 4, 5]. Furthermore, using SAM to assist image blending, while effective, is a straightforward extension and lacks the originality needed to stand out. The paper does not explore more sophisticated blending techniques or provide a comparative analysis against other mask-guided blending methods. The use of SAM, while convenient, does not introduce a novel contribution to the field of image blending. The method appears to be a simple combination of existing techniques without significant innovation.
- The selection of tuning-free editing baselines is also inadequate. Methods such as Masactrl [3], Proximal Guidance [4], and InfEdit [5] provide more sophisticated attention or mask control mechanisms. I recommend including a more comprehensive comparison with these existing baselines to better contextualize the contribution of the proposed method.

Other error:
Incorrect usage of quotation marks on line 237: The word 'choose' is improperly quoted.

### Questions
The findings in lines 210-212 are interesting. I am curious whether this phenomenon arises from differences in the text encoder or the diffusion model architecture. Could the authors provide insights into the underlying reasons for this observation?

### Soundness
2

### Presentation
3

### Contribution
2

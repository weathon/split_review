# Image Watermarks are Removable using Controllable Regeneration from Clean Noise

- Decision: Accept
- Scores: 6, 6, 6, 8, 6

## Abstract
Image watermark techniques provide an effective way to assert ownership, deter misuse, and trace content sources, which has become increasingly essential in the era of large generative models. A critical attribute of watermark techniques is their robustness against various manipulations. In this paper, we introduce a watermark removal approach capable of effectively nullifying the state of the art watermarking techniques. Our primary insight involves regenerating the watermarked image starting from a \textbf{clean Gaussian noise} via a controllable diffusion model, utilizing the extracted semantic and spatial features from the watermarked image. The semantic control adapter and the spatial control network are specifically trained to control the denoising process towards ensuring image quality and enhancing consistency between the cleaned image and the original watermarked image. To achieve a smooth trade-off between watermark removal performance and image consistency, we further propose an adjustable and controllable regeneration scheme. This scheme adds varying numbers of noise steps to the latent representation of the watermarked image, followed by a controlled denoising process starting from this noisy latent representation. As the number of noise steps increases, the latent representation progressively approaches clean Gaussian noise, facilitating the desired trade-off. We apply our watermark removal methods across various watermarking techniques, and the results demonstrate that our methods offer superior visual consistency/quality and enhanced watermark removal performance compared to existing regeneration approaches.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
1. The paper introduces CtrlRegen, a new method for removing image watermarks using controllable diffusion models. The method starts with clean Gaussian noise and regenerates the original image, using a semantic control adapter and spatial control network to guide the denoising process.
2. The paper also introduces CtrlRegen+ which is another version of CtrlRegen that allows for adjustable watermark removal. This method  starts with noising the latent representation of a watermarked image instead.
3. Compared to existing approaches, these methods achieve better visual consistency and are able to remove robust watermarks and handle both low and high perturbation watermarks.

### Strengths
Originality and Significance:
The paper has novel ideas and also creatively uses existing ideas
1. Novel Idea: The method CtrlRegen is a new method for removing image watermarks using controllable diffusion models, starting from clean Gaussian noise. This enables it to handle high perturbation attacks which the previous methods ex: Regen were unable to.
2. Creative combinations of existing ideas: ControlNet like spatial control network and semantic control adapter to guide the denoising process, ensuring consistency between the original and cleaned images. 
3. CtrlRegen+ enables an adjustable regeneration scheme - it allows for varying degrees of watermark destruction to counter different watermark strengths.

Clarity: The paper clearly explains the main ideas and method, provides context and presents quantitative results and comparisons in a clear manner.

Quality:
1. Results: The method outperforms previous regeneration approaches (Regen and Rinse) and demonstrates this through quantitative evaluation on both low and high perturbation watermarks. Multiple metrics are used to asses visual similarity and quality such as CLIP-FID, PSNR, Q-Align, LIQE beside evaluations related to watermark detection performance.
2. Consideration for use cases: The introduction of CtrlRegen+ shows consideration for different use cases and watermark strengths.

### Weaknesses
1. The paper does not outline/show any failure cases, limitations or drawbacks of the method.
2. The paper does not provide sufficient qualitative comparisons comparing the regeneration methods on diverse images  (ex: images containing text, scenes).

### Questions
Please see weaknesses section above

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
4

### Summary
This paper introduces a watermark removal method called CtrlRegen, which regenerates watermarked images starting from clean Gaussian noise using a controllable diffusion model. The method employs a semantic control adapter and a spatial control network to ensure image quality and consistency during the denoising process. Additionally, authors propose an adjustable regeneration scheme to balance watermark removal performance and image fidelity. Experimental results demonstrate that this method offers superior visual consistency and enhanced watermark removal performance compared to existing regeneration approaches.

### Strengths
1. The idea of using a controllable diffusion model for watermark removal is conceptually interesting
2. Incorporation of semantic and spatial controls is a way to maintain image quality during the process.

### Weaknesses
1. In Table 1, the evaluation is only conducted against two baselines, Regen and Rinse. However, there are other existing watermark removal methods, such as adversarial attacks, editing attacks, or general-purpose methods like Unmarker[1], that are not included in the comparisons. 

2. While the paper acknowledges that high-perturbation watermarks (e.g., StegaStamp and TreeRing) are more challenging to remove compared to low-perturbation watermarks, there is a lack of in-depth theoretical analysis or experimental results to explain why these watermarks are harder to remove. Providing more detailed insights into the mechanisms behind the difficulty of removing high-perturbation watermarks would strengthen the paper's argument.


3. The paper introduces both semantic and spatial controls to guide the watermark removal process, but it does not provide sufficient analysis.

### Questions
1.Why are the results for CtrlRegen+ not included in Table 1? How does its performance compare to the other methods across all watermarking techniques?


2. Meanwhile. why Figure 5 exlude base version of CtrlRegen?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces CtrlRegen, a watermark removal method that leverages controllable image regeneration from clean Gaussian noise to effectively remove state-of-the-art image watermarks, even those with high perturbation.  
CtrlRegen employs a trained semantic control adapter and spatial control network to guide the denoising process using extracted semantic and spatial features from the watermarked image.  
CtrlRegen+, further enhances the method by adding adjustable noise steps to the latent representation before denoising, allowing for a smoother trade-off between watermark removal and image quality.  
Experiments across various watermarking techniques demonstrate CtrlRegen's superiority in visual consistency and watermark removal performance compared to existing approaches , particularly for high-perturbation watermarks like StegaStamp and TreeRing.

### Strengths
1. CtrlRegen uses clean Gaussian noise as a starting point for denoising in a diffusion model, while existing regeneration attacks that add limited noise to the watermarked image's latent representation
2. CtrlRegen+ adds an adjustable noising step before denoising, allowing for a trade-off between watermark removal and image quality.  
3. Experiments show CtrlRegen outperforms existing regeneration methods (Regen and Rinse) in removing high-perturbation watermarks while maintaining better visual quality.
4. The method is a "no-box" attack, requiring only a watermarked image without knowledge of the watermarking scheme.  Ablation studies confirm the importance of both semantic and spatial control in maintaining image consistency.

### Weaknesses
1. Though the method proposes a novel approach to remove the image watermark, the watermark's perturbation is vulnerable to sophisticated attacks such as VAE. Applying VAE can also easily remove the watermark. The difficulty of watermark removal is relatively less challenging, the main contribution lies in the semantic consistency part.
2. The proposed method relies on regenerating a new clean from noise, while when there may exist large-scale watermarked image in 2K or 4K, marking the proposed method hard to regenerate a large-scale clean image while still keeping high semantic consistency. The computational cost for high-resolution images is not discussed, and it's unclear how the method would scale.
3. The selected baselines ReGen contains theoretical explanations on why the watermarks are provably removable. The proposed method lacks a theoretical analysis of why the regeneration scheme from noise can also be proved to remove the watermark. This absence of theoretical grounding makes it difficult to assess the robustness and generalizability of the approach.

### Questions
1. What is the model size and inferencing time for the proposed method CtrlRegen and CtrlRegen+? 
2. Compared with the common sophisticated attack on the watermarked image such as VAE or the recently proposed watermark removal schemes in Regen, what is the key advantage of the proposed method?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a watermark attack method capable of removing watermark embeddings through either low or high perturbations by regenerating the original image from clean gaussian noise. The approach preserves the original content by injecting features from the watermarked image into the regeneration process.

### Strengths
* This approach is novel; it begins with Gaussian noise and leverages a controllable removal process that injects the features of the watermarked image during the denoising process to achieve a clean, watermark-free image.

* The experimental results effectively demonstrate this method’s capability in removing watermarks across various watermarking techniques.

### Weaknesses
 * The paper lacks an ablation study for each of the modules in the proposed method, specifically the semantic control and spatial control modules. The contribution of each control module to overall performance should be investigated. It is unclear how much each module contributes to the final result, and whether both are necessary or if one is significantly more important than the other. For example, it would be beneficial to see results with only the semantic control, only the spatial control, and both, to understand their individual and combined effects. Furthermore, the specific mechanisms and parameters of each control module are not sufficiently detailed, making it difficult to assess their individual impact.

* As shown in Table 1, the quality of the resulting images, measured by reference-based metrics, is low, indicating that the method significantly alters the images. The low PSNR values suggest that while the watermark may be removed, the resulting image is substantially different from the original. This raises concerns about the practical applicability of the method, as a significant alteration of the original image is not desirable. It is important to understand the nature of these alterations and whether they introduce artifacts or other undesirable changes to the image content. The paper should include a more detailed analysis of the types of distortions introduced by the method.

### Questions
Please refer to the Weaknesses section above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors developed a method to remove watermarked embedded in images. They use clear noise, watermarked image embedding, and edges of watermarked images to regenerate the image, such that the image content is reminded but the watermark is removed. More precisely, they used attention mechanism to fuse the watermarked image embedding to the SD UNet and used Spatial-Net to extract edge features and add to the UNet. The authors conducted comprehensive experiments and demonstrated the proposed methods offer stronger removal effect, comparing with previous methods.

### Strengths
1)	The presentation is clear, and the paper is easy to follow.
2)	The use to clean noise is a good starting point
3)	The experiments demonstrate that it outperforms the other methods. The scale of the experiments is reasonable.

### Weaknesses
1) Although the clean noise and edge images are unlikely contained watermark information, I feel that it is possible for it to go through the image encoder and finally, appear in the output image. The authors should discuss more why the watermark information cannot go through the semantic control network. Specifically, the downsampling in the encoder might not completely eliminate high-frequency watermark signals, and these could potentially be reintroduced through the decoder. The cross-attention mechanism, while focusing on semantic features, might still retain some of the watermark information if it is correlated with the semantic content.
2) The authors use two mechanisms to fuse semantic information and spatial information. Why don’t use the same approach, such as attention? Any reason behind of this design. It is unclear why a unified attention mechanism could not handle both semantic and spatial information. The authors should provide a more detailed explanation of the limitations of using a single attention mechanism for both types of information. The current justification is weak and lacks a thorough exploration of alternative architectures.
3) The authors should revise the motivation. If the aim is to develop a stronger method to break all watermark algorithms, what is good the society and the community? The current motivation is problematic, as it primarily focuses on breaking watermarks rather than contributing to robust watermarking techniques. The authors should clarify the broader impact of their work and address the potential for misuse.
4) I cannot find out how many bits are used in the watermarking experiments.
5) Can the watermarking algorithms use more bits to increase the protection?
6) Although in visual quality indexes, expect for PSNR, the proposed methods are stronger than the baselines. The images for visual comparisons are not enough. The authors should provide more visual comparison. The visual comparisons are limited, and it is difficult to assess the real-world impact of the proposed method. More diverse examples, including images with varying complexities and content, are needed to validate the method's effectiveness.
7) The authors should provide a scheme to defend the proposed methods. Otherwise, this paper will cause more harm than good to the society. The lack of a defense mechanism is a major concern, as it leaves the proposed method open to malicious use. The authors should explore potential countermeasures and discuss their limitations.
8) Do the constraints e.g., L2 norm or L infinite norm using in watermark algo development affect the removal capacity?

### Questions
See the weaknesses

### Soundness
3

### Presentation
3

### Contribution
2

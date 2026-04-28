# TD-Paint: Faster Diffusion Inpainting Through Time Aware Pixel Conditioning

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6, 6

## Abstract
Diffusion models have emerged as highly effective techniques for inpainting, however, they remain constrained by slow sampling rates. While recent advances have enhanced generation quality, they have also increased sampling time, thereby limiting scalability in real-world applications. We investigate the generative sampling process of diffusion-based inpainting models and observe that these models make minimal use of the input condition during the initial sampling steps. As a result, the sampling trajectory deviates from the data manifold, requiring complex synchronization mechanisms to realign the generation process. To address this, we propose \modelfull(\model), a novel approach that adapts the diffusion process by modeling variable noise levels at the pixel level. This technique allows the model to efficiently use known pixel values from the start, guiding the generation process toward the target manifold. By embedding this information early in the diffusion process, \model significantly accelerates sampling without compromising image quality. Unlike conventional diffusion-based inpainting models, which require a dedicated architecture or an expensive generation loop, \model achieves faster sampling times without architectural modifications. Experimental results\footnote{Our code is provided in supplementary materials.}
across three datasets show that \model outperforms state-of-the-art diffusion models while maintaining lower complexity.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a way to perform inpainting by leveraging pre-trained pixel diffusion model. The authors fine-tune a diffusion model such that instead of inputting a single scalar that represents the tilmestep of the noise in the diffusion process, the model inputs a map, representing per-pixel tilmesteps. Then, at inference, this allows them to always input the fully denoised image in the known regions while iteratively denoising the masked areas. Unlike the main baseline, RePaint, this process is much faster, as it does not require multiple diffusion passes to synchronize the known and unknown regions.

### Strengths
The proposed approach is quite simple but at the same time intuitive and effective. The idea of varying the diffusion at a pixel level is a promising one, both for novel applications (such as inpainting) as well as for a more general approach to accelerating diffusion inference.

### Weaknesses
My main concern has to do with lack of comparison to or discussion of some more recent and relevant SOTA diffusion-based inpainting approaches. For instance, LatentPaint [Corneanu et al., WACV 2024] also a propose an approach that requires fine-tuning with a fast inference pass (compared to RePaint). Additionally, "Blended Latent Diffusion" [Avrahami et al., SIGGRAPH 2023] and "Uni-paint" [Yang et al., MM 2023] leverage latent diffusion models for an inpainting task (while the former does not explicitly target unconditional inapinting, it ca be used for that purpose).  It would be very helpful to see comparisons to some of these recent works as well as a high-level discussion of their differences in order to evaluate the proposed method.

On a more minor note, the presentation and exposition could be improved. Figure 1, which illustrates the proposed approach in contrast to RePaint, is somewhat difficult to follow and includes notation that is not defined until much later. In contrast, the idea behind RePaint is explained multiple times in various sections throughout the paper and could be truncated.

I would also encourage the authors to cite and discuss "Differential Diffusion: Giving Each Pixel Its Strength" [Levin and Fried, 2023]. Given that this work does not appear in a peer-reviewed publication, I am not considering it in my rating, but given its close relevance to the topic, it would be good to mention.

### Questions
How can the proposed method be used to scale up to higher resolution images? For instance, is there a straightforward way to extend to LDMs, as some of the more recent inpainting approaches have been doing?

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
The paper presents a novel method for speeding up diffusion-based inpainting. It changes the noised known region condition in the RePaint paper into a clean one for condition. To support this change, it introduces a trained diffusion model that supports a spatial-varying timestep condition to mark the known and missing part of the image. This new design also allows the method to avoid the repeated sampling process in RePaint, greatly increasing the speed. Quantitative results also demonstrate the proposed method performs on par or better with existing methods.

### Strengths
1. Training the diffusion model to directly use clean known parts as the diffusion condition, avoiding complex modifications to the diffusion process. This approach significantly speeds up the method compared to existing approaches, enhancing efficiency without compromising quality.
2. Introduction of a novel spatial-varying timestep condition for injecting the known region mask. This innovative technique allows for more precise control over the inpainting process, resulting in improved output quality.
3. Comprehensive testing on multiple diverse datasets, demonstrating superior performance (for both quality and diversity) across various scenarios. The extensive evaluation provides strong evidence for the method's robustness and effectiveness in different contexts.

### Weaknesses
The paper is in general good, I only have concerns on its generality:

Since the proposed method requires training and is not trained with data besides CelebA-HQ, ImageNet1K, and Places2, it probably cannot generalize to open-world images like LaMa.

### Questions
1. Training Inference Gap: The training is done on patch-wise known regions. But inference of the known region doesn’t necessarily be axis-aligned patches. How do you solve this gap? Will training on randomly shaped known regions further boost the model’s performance?
2. I wonder how well the proposed method performs when adapted to larger diffusion models like stable diffusion.
3. The ControlNet-Inpaint model also provides fast and high-quality diffusion-based inpainting. How does the proposed method perform compared to that model?

I would raise my score if these questions were answered.

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
5

### Summary
The authors mainly proposed to use the same T2I architecture to do inpainting. To properly feed in the known image conditions, they propose to use a pixel-wise noisy injection with different levels, and a spatial-variant timesteps map. Therefore, during training and inference, it allows to add minimum levels of noises to known image regions, while only diffuse the unknown regions following the normal diffusion process. The idea is simple, effective and easy to implement. Extensive experiments also demonstrate its effectiveness in maintaining good inpainting quality while reducing inpainting complexity compared to RePaint.

### Strengths
- The design of spatial-variant time embedding for inpainting tasks bring two major advantages: (1) no architecture change form T2I, and (2) relative faster inpainting process. 
- The authors provide extensive and scientific evaluation on different masks, and the proposed method achieved good inpainting quality.

### Weaknesses
 - Repaint seems not the state-of-the-art inpainting model, and recently models based on latest latent diffusion model or DiT framework achieve much better results, for instance, powerpaint(https://powerpaint.github.io/). Some comparison needs to be updated. 
- Since the model is trained on diffusion-based framework, is it still necessary to list ConvNet-based or transformer-based model in the comparison? They will be not comparable given the inference speed and model capacity. The comparisons should focus on latest diffusion-based model in quality and speed. 
- To the best of the reviewer's knowledge, recent diffusion-based inpainting is no longer using the way of RePaint to do inference. The problems mentioned by the authors like 'consistency' are no longer an issue. It can be simply achieved by adding an additional conditions concatenated with the noisy input in UNet, or adding additional tokens for DiT-based framework. Some controlnet-based method do have the composition and harmonization problems.
- It is not clear how the framework can be generalized to image editing, when the mask is soft or we need some levels of content preservation under the mask region. Without having the original image as a condition, it will be very hard to generalize the model to other editing tasks, like color changing. Therefore, the proposed framework will be limited as a foundation model, or used to finetuned for other tasks. 
- The masks used in inpainting literature are mostly not suitable for real practical application because they are not used by the real inpainter users. Better to try some object-shaped masks and use those for user study. 
- The proposed method may lack mask precision in a latent diffusion framework, especially for tasks like background replacement. For latent diffusion, the masks are usually applied to the pixel space, and the masked image will be encoded using the latent encoder for compression, and server as the condition. In this case, the latent diffusion model can still learn to reconstruct the high-precision mask boundary to preserve the details around the boundary. If we apply the low-res mask in the latent and apply different t in the precision of latent mask, it won't be able to leverage the advantages of the high-quality encoding.

### Questions
- During training, the authors use noise levels close to zero to generate noises in known region, while uses zero during inference. Any specific reasons of adding noises during training? Is it possible to simply set them as zero?
- How did the authors design the time step conditions input to the network? It is not clearly stated in the paper.
- How is the inpainting performance of the model compared with state-of-the-art commercial inpainter like Photoshop Generative Fill, MidJourney Editor, and DALL-E inpainter? No need to do detailed comparison, but a few figures / images to show the advantages or gaps will be sufficient. 
- The pixel-wise time embedding is actually a region-wise time embedding? Is it possible to formulate it as only two time embeddings + one binary mask, so as to reduce the learning complexity of the model. The reviewer is not sure about the learning stability of the model. Also pixel-wise embedding can be well generalized to SDEdit, but it can be very hard to train.

### Soundness
3

### Presentation
2

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
This paper proposes a method that can do faster inpainting in diffusion models by introducing time-aware denoising process.

### Strengths
1. It can generate high-quality inpainting on various mask sizes and shapes.
2. It is faster compared to other stare-of-art methods.
3. It has extensive evaluations

### Weaknesses
1. The visual result is not much better than other baselines
2. Even though they have many evaluation results, the improvement in image quality with scores in not much.

### Questions
The paper's contribution to the community is not that great, as time improvement is not that significant.

### Soundness
2

### Presentation
2

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
The authors proposed a new training scheme of diffusion-based inpainting model that can perfectly maintain the regions inside the mask.

### Strengths
1. The training strategy is novel and the performance is good.

### Weaknesses
1. Any evaluations about how good the unchanged regions are maintained?
2. I admit that the training scheme is novel, but I am not sure if the novelty is enough for publishing. Since the entire method is a slight modification of existing diffusion model.

### Questions
1. The training masks are always square. How can you applied the trained model on random masks during the inference?
2. Is it possible that this method can be extended to the latent diffsusion?

### Soundness
3

### Presentation
4

### Contribution
3

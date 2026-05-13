# Magic123: One Image to High-Quality 3D Object Generation Using Both 2D and 3D Diffusion Priors

- Decision: Accept
- Scores: 8, 5, 8, 5

## Abstract
We present ``\textit{Magic123}'', a two-stage coarse-to-fine approach for high-quality, textured 3D meshes generation from a \textit{single unposed} image in the wild using \textit{both 2D and 3D priors}. In the first stage, we optimize a neural radiance field to produce a coarse geometry. In the second stage, we adopt a memory-efficient differentiable mesh representation to yield a high-resolution mesh with a visually appealing texture. In both stages, the 3D content is learned through reference view supervision and novel views guided by a combination of 2D and 3D diffusion priors. We introduce a single trade-off parameter between the 2D and 3D priors to control exploration (more imaginative) and exploitation (more precise) of the generated geometry. Additionally, we employ textual inversion and monocular depth regularization to encourage consistent appearances across views and to prevent degenerate solutions, respectively. Magic123 demonstrates a significant improvement over previous image-to-3D techniques, as validated through extensive experiments on synthetic benchmarks and diverse real-world images.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This proposes a diffusion-based method for single-view 3D reconstruction. The key novelty is to combine 2D diffusion prior, which can achieve higher resolution more realistic appearance and 3D diffusion prior, which can achieve better 3D consistency. It designs a 2 stage optimization pipeline where the first stage uses hash grid volume representation to get the coarse reconstruction and the second stage uses DMTet representation to refine high resolution texture. Experiments on widely used datasets, such as NeRF dataset, shows significant improvements compared to prior state-of-the-arts.

### Strengths
1. High-quality single-view 3D reconstruction. 
The proposed method shows high-quality 3D reconstruction that is significantly better than previous state-of-the-arts. 

2. Comprehensive ablation studies and convincing experiments.
Authors report various benchmarks to show improvements compared to previous works, including LPIPS, PSNR, SSIM and CLIP similarities. They did ablation studies that clearly show the benefit of combining 2D and 3D diffusion priors, both qualitatively and quantitatively (Figure 6 and 7).

3. Clear novelties and technical contributions. 
The idea of combining 2D and 3D diffusion prior is novel and is proven to be useful in many applications. 

4. Well-written with sufficient implementation details.
This paper is well-written and easy to follow. Authors provide enough details to re-implement this paper.

### Weaknesses
This is a solid paper which significantly improves the baseline of single-view 3D reconstruction. The idea of using a diffusion model fine-tuned on a large-scale 3D dataset for text-to-3D or sparse-view 3D has been adopted by many recent works and the reconstruction quality has been significantly improved since then. I do not find any specific weaknesses of this paper and followings are either limitations of current works or some design choices that can improve the results.

1. Relightability.
While this work uses a diffuse shading model, the reconstructed material texture is not really relightable and will have lighting baked in. To reconstruct relightable 3D contents, we need to understand the environment lighting of the input images and use that for optimization. However, how to do that from sparse view input is still an open problem.

2. Reconstruction speed.
The reconstruction speed of the stage one may be improved by progressively increase the level of hashgrid and the resolution of the rendered image. The reconstruction speed of the second stage may be improved by sampling from a small range of time steps. 

3. Backside of the object.
In some examples, the backside of the object still has a strong color shift compared to the reference views. This may be improved by using VSD loss instead of SDS loss or simply using a strong 3D diffusion prior.

### Questions
Overall I am very positive towards accepting this paper. I cannot see if any questions that will change my opinions so far. I will be glad to learn from authors rebuttal and other reviewers' comments.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes to combine the SDS loss from both a 2D pretrained diffusion model (StableDiffusion) and a fine-tuned 3D-aware 2D diffusion model (Zero1-to-3). They show that this combination allows the generated 3D assets to have more realistic texture than using the Zero1-to-3 only, and have more plausible shapes than using the StableDiffusion only.

### Strengths
1. Paper is well-written and easy to follow.
2. The proposed method seems easy to reproduce, and code is attached.
3. On 4 nerf objects and 15 real objects, the proposed system outperforms baseline single-image-to-3D methods both qualitatively and quantitatively.

### Weaknesses
1. This seems to be a A+B style paper with majority of the components have appeared in prior works, e.g., coarse-to-fine optimization (first stage uses NeRF, second stage uses DMTet) from Magic3D, text-conditioned (using textual inversion) SDS loss from RealFusion, image-conditioned SDS loss from Zero1-to-3.

2. The novel part of this work seems the combination of the text-conditioned SDS loss and image-conditioned SDS loss. But this part might be a bit straightforward in the sense that the 3D awareness of Zero1-to-3 can help learn better geometry (as shown in Zero1-to-3), and the text-conditioned StableDiffusion can generate better appearance (as it’s a model trained on billions of real images and not tuned on the limited amount of Objaverse renderings)

3. Given single image, there're multiple plausible 3D reconstructions. This kind of diversity is missing in the evaluation part of this work.

### Questions
This paper is written in a clear way, and I have no further questions after reading the manuscript carefully.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors propose a novel method for generating high-quality, textured 3D meshes from a single unposed image in the wild using both 2D and 3D priors. For 2D priors, the framework uses Stable Diffusion and for 3D Zero-1-to-3 is used. The approach uses two-stage coarse-to-fine pipeline that first optimizes a NeRF to produce a coarse geometry and texture, and then refines it using a memory-efficient differentiable mesh representation (DMTet) for high-resolution renderings. State of the art performance is demonstrated compared to recent image-to-3D methods.

### Strengths
1. **Novelty**: The proposed approach introduces a key insight of used 2D and 3D priors together to aid in better 3D geometry generation as opposed to 2D priors only as was common. Additionally, also presents the distinct advantage over 3D prior alone, since 2D diffusion models are trained on so much more data than that available to train for 3D. 
2. **Paper quality**: The paper is well written with great attention to detail, all the components are described in detail and adequately motivated. 
3. **Reproducibility**: The framework is implemented using available open source code. Additionally, all network and training details have been provided to aid in reproducibility of the approach. Furthermore, code has been provided in the supplementary as well to match the results shown in the paper.
4. **Result quality**: The generated assets have impressive quality for a single view lifting approach. Results are demonstrated on both synthetic objects and objects in the wild to highlight the efficiency of the approach. 
5. **Related work**: An adequate treatment of the related work in the space of text-to-3D and single image-to-3D have been provided to place the given approach in the context of relevant literature.
6. **Ablations**: Key ablations have been provided, particularly, the effect of 2D only, 3D only and combined priors and demonstrating the effect of change of 2D and 3D prior weights. 
6. **Supplementary materials**: The provided materials are very helpful, as it shows turntable videos of generated assets, along with several key ablations which provides a lot of insight into the different components of the approach.

### Weaknesses
1. **Segmentation**: The quality of the final asset is limited by the performance of the segmentation model of choice(as acknowledged by the authors). Several questions arise in this setting: 
  > a. Does the diffusion priors correct for some of inaccuracies of the segmentation model?  
  > b. Is it hard to reconstruct objects that are in a cluttered environment?  
  > c. Is the DMTet algorithm affected by inaccurate segmentations? Specifically, how does the texture mapping process in DMTet handle the boundary regions of inaccurate segmentations, where the object and background might blend? 
  > d. What happens in instances where the segmentation algorithm outputs two or more disjoint segments, does the inductive bias of the NeRF overcome this issue? (this is potentially addressed to some extent under the limitation mentioned by the authors about handling discontinuities).   
  > e. Is a segmentation network required even if the model is on a plain background? (this is potentially the case, as the mask appears in equation (1)

2. **Depth and Smoothness**: Similar to the above concern, the performance is capped by the effectiveness of the pre-trained depth and normal estimation network. This poses inherent limitations to the kind of input images that it can be applied to. Providing some insights on where these kind of estimation networks fail would be helpful. Furthermore, depth and normals potentially don't make much sense, till the NeRF has converged to a reasonably estimate of geometry.Is there a schedule associated with these losses to have an effect after initial shape has been estimated by the NeRF? It would be beneficial to understand the sensitivity of the final 3D reconstruction to the accuracy of the estimated depth maps, and how this impacts the overall geometry, particularly in areas with significant depth discontinuities or occlusions.

3. **Centered objects**: Owing to the nature of Zero-1-to-3, it appears that this kind of lifting works only on centered objects. What is the effect on the recovered geometry if the object is off-center but can still be segmented out accurately ? Does the method have a mechanism to handle objects that are not centered in the input image, or does it rely on a pre-processing step to center the object before reconstruction? If so, how does the centering process affect the final 3D model, particularly if the object is not perfectly symmetrical?

4. **Textual inversion vs Dreambooth**: The authors mention that textual inversion is used for the 2D-SDS loss to capture some of the image specific texture information. Providing some insight on how this compares to performing Dreambooth on the model to achieve the same would be helpful. Specifically, what are the trade-offs between using textual inversion and Dreambooth in terms of training time, memory requirements, and the quality of the resulting texture?

### Questions
1. What is effect of applying this approach to scenes without segmentation instead of objects?
2. Is TI better than DreamBooth for 2D SDS loss?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Magic123 proposes a technique to create textured 3D meshes from a single image by a combination of both 2D and 3D priors. The method follows a two-stage strategy, transitioning from coarse to fine geometry. They also introduced trade-off parameter that attempts to balance the influences of the 2D and 3D priors, aiming to optimize quality and consistency. They showed comparisons with existing works on 3D datasets.

### Strengths
1. Magic123 = Magic3D and Zero123? An interesting and practical idea of introducing a balance between the 2D and 3D priors could offer a way to adjust generation outcomes.
2. The two-stage approach might offer a systematic way to enhance the granularity and accuracy of the 3D representations.

### Weaknesses
1. Comparison with Zero1-2-3: Although the authors claim "significant improvements over existing method", the qualitative comparison in figure 5 does not significantly support this claim. The improvements in terms of quality and sharpness are noticeable, but there seems to be a potential trade-off in consistency. Moreover, the supplementary videos are missing a direct comparison with Zero1-2-3, and the quantitative comparison with Zero1-2-3 is comparable, which further weakens the claim (in limited 3D results and examples). The comparison lacks a rigorous analysis of multi-view consistency, particularly when the 2D prior is heavily weighted. The observed trade-off between quality and consistency needs more thorough investigation, including metrics that quantify multi-view discrepancies.
2. The paper does not provide details on how the weights for the 2D and 3D priors are chosen. If these weights are determined and tuned during training and are inflexible during inference, this approach might not be the most effective way to integrate the priors. The method needs to clarify whether these weights are fixed or adaptable per instance. If fixed, the paper should explore the sensitivity of the results to these weights and provide a justification for the chosen values. If adaptable, the mechanism for this adaptation should be described in detail.
3. The model's inherent assumption of a frontal reference limits its versatility. This is evident from the removal of four examples from the training dataset that do not meet the front view assumption. That could potentially limit the scale of 3D datasets and this could lead to even lower generalization and a drop in result quality. The reliance on a frontal view is a significant limitation, especially for real-world applications where objects are viewed from arbitrary angles. The paper should discuss the implications of this limitation on the generalizability of the method and explore potential solutions to mitigate it.
4. The coarse-to-fine process, while effective, isn't novel as it has been employed in other works like Magic3D.  The Tetrahedral 
representation seems to be hard to scale and appears to be optimally suited for objects. This could limit the method's applicability to a broader range of scenarios. The use of a tetrahedral mesh representation, while offering benefits in terms of detail, may not be the most efficient for all types of 3D scenes. The paper should discuss the limitations of this representation, particularly in terms of scalability and applicability to complex scenes, and consider alternative representations that might offer better performance in different scenarios.

### Questions
1. The paper does not convincingly demonstrate that the combination of 2D and 3D priors leads to markedly better outcomes than using either alone. The real challenge should be to extract the unique advantages of both priors for a superior result, not just to find a balance between the two. I'd suggest the authors to add more comparison with Zero1-2-3 or include results to prove clear improvements without poor sacrifice of multi-view consistency in figure 5. 
2. The paper should provide evidence of improved geometric detail and not just enhancements in the output rendering quality. Merely augmenting the contrast or enhancing the visual appeal with a 2D prior is insufficient. Could this method result in sharper geometric details as well?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

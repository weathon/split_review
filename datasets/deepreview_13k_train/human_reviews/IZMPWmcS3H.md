# HIFA: High-fidelity Text-to-3D Generation with Advanced Diffusion Guidance

- Decision: Accept
- Scores: 6, 8, 6

## Abstract
The advancements in automatic text-to-3D generation have been remarkable. Most existing methods use pre-trained text-to-image diffusion models to optimize 3D representations like Neural Radiance Fields (NeRFs) via latent-space denoising score matching. Yet, these methods often result in artifacts and inconsistencies across different views due to their suboptimal optimization approaches and limited understanding of 3D geometry. Moreover, the inherent constraints of NeRFs in rendering crisp geometry and stable textures usually lead to a two-stage optimization to attain high-resolution details. This work proposes holistic sampling and smoothing approaches to achieve high-quality text-to-3D generation, all in a single-stage optimization. We compute denoising scores in the text-to-image diffusion model's latent and image spaces. Instead of randomly sampling timesteps (also referred to as noise levels in denoising score matching), we introduce a novel timestep annealing approach that progressively reduces the sampled timestep throughout optimization. To generate high-quality renderings in a single-stage optimization, we propose regularization for the variance of z-coordinates along NeRF rays. To address texture flickering issues in NeRFs, we introduce a kernel smoothing technique that refines importance sampling weights coarse-to-fine, ensuring accurate and thorough sampling in high-density regions. Extensive experiments demonstrate the superiority of our method over previous approaches, enabling the generation of highly detailed and view-consistent 3D assets through a single-stage training process.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed an improved version of Score Distillation Sampling by introducing several strategies. The authors proposed to perform denoising in both image and latent space for better performance. A novel timestep annealing strategy is provided to reduce the sampling space. Besides, the authors also provide a z-coordinates regularization term to achieve high-quality rendering in a single-stage optimization. The paper is well-organized and easy to follow. The proposed strategies are effective to improve the performance.

### Strengths
1. The strategy by denoising in both image and latent space is useful to improve the details.
2. The proposed z-variance loss alleviates cloudy artifacts and shows better performance than distortion loss.
3. The proposed method achieves high-quality text-to-3D generation.

### Weaknesses
Basically the paper is good and I have several concerns:
1. The contributions of the paper are discrete, which comprises several small contribution points.
2. Maybe a user-study should be conducted to quantitatively evaluate the method.
3. Basically the proposed strategies can be generalized to other baseline methods, for example, ProlificDreamer [1]. I’m curious to see the performance with other baseline methods.

### Questions
Please refer to weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
- The paper proposes holistic sampling and smoothing approaches for high-quality text-to-3D generation in a single-stage optimization. 
- The method introduces a timestep annealing approach and regularization for the variance of z-coordinates along NeRF rays.
- The paper also addresses texture flickering issues in NeRFs with a kernel smoothing technique.
- Experiments show the method's superiority over previous approaches.

### Strengths
- The single-stage optimization is useful to the generation of highly detailed and view-consistent 3D assets and the proposed solution to it is impressive.
- Compared to baseline methods like Dreamfusion, Magic3D, and Fantasia3D, the rendered images from this approach exhibit enhanced photo-realism, improved texture details of the 3D assets, and more natural lighting effects.

### Weaknesses
 - The paper could benefit from a more explicit explanation in the introduction regarding why previous works were unable to achieve single-stage optimization. Specifically, the introduction should detail the inherent challenges in optimizing both geometry and appearance simultaneously within a single-stage framework. For instance, it could discuss how naive single-stage optimization often leads to a trade-off between geometric accuracy and texture quality, resulting in either blurry geometry or noisy textures. This would help contextualize the significance of the proposed method.
- The contributions presented in the paper seem fragmented, lacking a cohesive thread or central theme. It would enhance the paper's clarity and impact if the authors could refine the structure. The paper introduces several techniques, including timestep annealing, z-coordinate variance regularization, and kernel smoothing, but the connection between these techniques and their collective impact on the overall text-to-3D generation process is not clearly articulated. It is unclear how these individual components synergistically contribute to the final result, making it difficult to grasp the core innovation of the paper.

### Questions
I believe the technical aspects are articulated clearly and technically sound. Thus, I have no further questions.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes four techniques on the task of 2D diffusion-guided text-to-3D generation, to enhance the generation quality. In particular, the authors 1) propose score distillation in both the latent and image space of the pre-trained text-to-image diffusion models; 2) introduce a timestep annealing strategy to achieve photo-realistic and highly-detailed generation; 3) present a regularization method on the variance of z-coordinates along NeRF rays to encourage crisper surfaces; 4) they also propose a kernel smoothing technique to address flickering issues in the optimized NeRFs. They conduct qualitatively ablation studies and the experimental results demonstrate the effectness of the proposed techniques.

### Strengths
* From the presented experimental results (mainly qualitative results), the proposed techniques are effective and improve the performance over prior methods; 
* The ablation studies also demonstrate the effectiveness of individual technique;

### Weaknesses
 * The experimental results are all qualitative results. It is good to have a metric/metrics to compare quantitatively against prior methods; For example, to measure the CLIP similarity between the text prompts and the generated contents; Otherwise, it is difficult to evaluate the performance since we can deliberately select good performing prompts over prior methods for comparisons. 

*  The results from Fantasia3D are also very impressive (i.e. in terms of texture quality and geometry) from Figure 4 and Figure 14. Can you provide more results to show that yours is better? I provide following text prompts from DreamFusion: 1) an orangutan making a clay bowl on a throwing wheel; 2) a raccoon astronaut holding his helmet; 3) a blue jay standing on a large basket of rainbow macarons; 4) a corgi taking a selfi; 5) a table with dim sum on it; 6) a lion reading the newspaper; 7) a tiger dressed as a doctor; 8) a chimpanzee dressed like Henry VIII king of England; 9) an all-utility vehicle driving across a stream; 10) a squirrel gesturing in front of an easel showing colorful pie charts. Can you do the comparisons with those prompts?

* For the kernel smoothing, you only choose [1, 1, 1] as the sliding window kernel, have you tried other choices?

### Questions
* How is the kernel smoothing conducted for coarse-to-fine importance sampling? Could the authors provide more details? In fact, I do not understand "kernel smoothing". Use an equation to explain it would be very helpful. Figure 3 seems only presents the results with/without kernel smoothing.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

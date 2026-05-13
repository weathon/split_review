# StochSync: Stochastic Diffusion Synchronization for Image Generation in Arbitrary Spaces

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
We propose a zero-shot method for generating images in arbitrary spaces (e.g., a sphere for 360◦ panoramas and a mesh surface for texture) using a pretrained image diffusion model. The zero-shot generation of various visual content using a pretrained image diffusion model has been explored mainly in two directions. First, Diffusion Synchronization–performing reverse diffusion processes jointly across different projected spaces while synchronizing them in the target space–generates high-quality outputs when enough conditioning is provided, but it struggles in its absence. Second, Score Distillation Sampling–gradually updating the target space data through gradient descent–results in better coherence but often lacks detail. In this paper, we reveal for the first time the interconnection between these two methods while highlighting their differences. To this end, we propose StochSync, a novel approach that combines the strengths of both, enabling effective performance with weak conditioning. Our experiments demonstrate that StochSync provides the best performance in 360◦ panorama generation (where image conditioning is not given), outperforming previous finetuning-based methods, and also delivers comparable results in 3D mesh texturing (where depth conditioning is provided) with previous methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This manuscript proposes a new diffusion synchronization method for panorama/texture generation (or on arbitrary surfaces) using pretrained image diffusion models. The proposed method combines the strengths of SDS and previous synchronization method by adding more stochasticity, using multi-step x0 sampling for synchronization, and using non-overlapping views. Both qualitative and quantitative results seem to demonstrate its strengths on panorama generation and mesh texturing tasks.

### Strengths
- The contributions seem technically sound to me. As someone who works on relevant topics, I believe that adding stochasticity and using multi-step sampling should be better than vanilla synchronization without any doubt (and I have not yet read another paper pointing this out clearly). Also, using non-overlapping views is an interesting design choice.

- The paper makes a good effort at comparing existing methods and the proposed one. The algorithms are very clearly presented, showing the similarities and differences between StochSync, SDS and vanilla synchronization. The writing is also clear in general.

- Experiments look good to me. The contributions of each component are clearly shown in Table 2 and Fig. 2. The results are strong on both panorama and texture generation tasks. Despite the weaker texture generation metrics compared to SyncTweedies, StochSync seems to produce better details, which aligns with my expectation.

### Weaknesses
 - I feel that this manuscript could have been a lot better with more in-depth theoretical analysis rather than just empirical results. Why is more stochasticity better? Does non-overlapping view sampling implies strong output correlation between overlapping views which degrades the distribution? Non of these important questions are explained in more depth, no even with some basic intuitions.

- Inference time is not given, which is a very important factor when evaluating these models. Using multi-step computation is clearly more expensive than vanilla synchronization methods.

- Some evaluation metrics might not be proper for the problem. FID and KID metrics compare the generated distribution with a reference. But when using pretrained models for zero-shot adaptation, it's hard to define a standard reference dataset. IS also seems not perfect since it's originally designed for evaluating generative models on categorical data.

- I find some explanation of the empirical result not satisfactory. For example, in L316, I don't think it's simply the increased stochasticiy that worsens the distribution - rather it could be the case that increased stochasticiy effectively makes the sampling time step larger, and should be compensated with multi-step sampling to restore the distribution.

- As the authors have pointed out, a clear limitation of this method is the inability to generate 3D content such as NeRF. However, the explanation of overfitting seems problematic to me as SDS clearly doesn't have such issue.

### Questions
I do not have any confusion about this manuscript. For rebuttal, please address the weaknesses listed above.

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
2

### Summary
This paper presents a novel method called StochSync for zero-shot image generation in arbitrary spaces, such as 360° panoramic and 3D mesh textures, by leveraging pretrained diffusion models. StochSync builds on two existing approaches—Diffusion Synchronization (DS) and Score Distillation Sampling (SDS)—by combining their strengths: the coherence of DS and the robustness of SDS in weak conditioning scenarios. Experimental results demonstrate that StochSync produces high-quality, seam-free images in various geometries, outperforming or matching zero-shot and fine-tuned methods across multiple evaluation metrics.

### Strengths
1. The authors clearly illustrate their motivation in combining DS and SDS, effectively balancing stochasticity and coherence.

2. StochSync can enhance image generation quality in arbitrary spaces without the need for fine-tuning. The method is also applicable across a variety of geometries, extending the capabilities of pretrained diffusion models beyond their typical square-space applications.

3. The paper provides detailed ablation studies, elucidating the contribution of each component of StochSync, such as maximum stochasticity, multi-step denoising, and non-overlapping view sampling.

### Weaknesses
1. The contribution is limited as it is more likely to be an A (DS) + B (SDS) framework although the authors conduct theoretical analysis. 

2. The paper does not discuss computational efficiency in detail. Given the complex multi-step nature of StochSync, the method may struggle to achieve real-time performance, limiting its applicability in interactive or real-time systems. The authors should provide more detailed discussions of time efficiency as SDS-like approach is very time consuming.

3. As multi-view plausibility and consistency is quite significant in 3D objects, the paper only provides a single view of the 3D mesh.

### Questions
1. As video diffusion models contain more spatial connection information across different views, can video diffusion benefit such tasks?

2. As PBR materials play an important role in 3D mesh texturing, can StochSync also perform well in PBR-like texturing?

3.  While the paper shows impressive results for unconditional cases, can the authors provide more insight into how StochSync performs under conditional scenarios, particularly in comparison to methods that excel with strong conditioning (e.g., DS methods with depth maps)?

4. Since generating high-resolution outputs is often challenging in diffusion models, could StochSync be adapted or scaled for ultra-high-resolution generation (e.g., for 8K textures or VR applications)?

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
The paper proposes a new method for training-free generalization of image diffusion to generation in more general spaces, such as 360 panorama and 3D mesh textures. The main idea is to replace the one step denoising step in diffusion synchronization with multi step denoising on non-overlapping views. Qualitative results show that it can generate more realistic results with fewer artifacts such as seams in panorama.

### Strengths
1. The idea of using multi-step backward equipped with non-overlapping view sampling is novel.

2. The presentation is clear and detailed, drawing connections of the proposed method to existing methods such as SDS, diffusion synchronization and SDEdit.

### Weaknesses
1. Non-overlapping view sampling seems to be an essential part of the algorithm. If the views are overlapping, each step involves blending several multi-step denoised images, which does not make sense to me. In diffusion synchronization methods this problem is not that big because each blending step only involves images with one-step denoising. However I do not find any ablation study of non-overlapping view sampling, and do not know what kind of artifact it will introduce if we drop this component.

2. Non-overlapping view sampling can be a limitation in some cases, e.g. panorama smaller than 360 degree.

3. Although the paper claims the method can generate for "arbitrary spaces", the two tasks shown in the paper (360 panorama and mesh texturing) have relatively simple "rendering" functions f. In fact, they are both linear (in terms of the underlying parameters) and so projecting and blending multiple views in the same space is easy. But how about a nonlinear rendering function such as NeRFs? I guess it will be a challenge compared to other methods like SDS because different views are fully denoised to potentially completely different images (especially in early stages), and blending them over time with a complicated rendering function is not easy.

4. It can be much slower than the alternatives because of the multi-step backward process G at each step.

### Questions
1. Regarding non-overlapping view sampling for 3D meshes, do you only sample 2 views for each iteration? It seems impossible to sample more than 2 views without mutual overlap.

### Soundness
2

### Presentation
3

### Contribution
2

# Patched Denoising Diffusion Models For High-Resolution Image Synthesis

- Decision: Accept
- Scores: 6, 5, 6, 5

## Abstract
\vspace{-5pt}
We propose an effective denoising diffusion model for generating high-resolution images (e.g., 1024$\times$512), trained on small-size image patches (e.g., 64$\times$64). We name our algorithm Patch-DM, in which a new feature collage strategy is designed to avoid the boundary artifact when synthesizing large-size images. Feature collage systematically crops and combines partial features of the neighboring patches to predict the features of a shifted image patch, allowing the seamless generation of the entire image due to the overlap in the patch feature space. Patch-DM produces high-quality image synthesis results on our newly collected dataset of nature images (1024$\times$512), as well as on standard benchmarks of smaller sizes (256$\times$256), including LSUN-Bedroom, LSUN-Church, and FFHQ. We compare our method with previous patch-based generation methods and achieve state-of-the-art FID scores on all four datasets. Further, Patch-DM also reduces memory complexity compared to the classic diffusion models.
\vspace{-5pt}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a denoising diffusion model, Patch-DM, for generating high-resolution images (e.g., 1024×512), trained on small-size image patches (e.g., 64×64). The major contribution of the paper is a new feature collage strategy, which is designed to avoid the boundary artifact when synthesizing large-size images. The authors demonstrate the effectiveness of  Patch-DM on mage synthesis results on their newly collected dataset of nature images (1024×512), as well as on standard benchmarks of LHQ(1024× 1024), FFHQ(1024× 1024) and on other datasets with smaller sizes (256×256), including LSUN-Bedroom, LSUN-Church, and FFHQ. The show state-of-the-art FID scores on all six datasets for the proposed model. Further, Patch-DM also reduces memory complexity compared to the classic diffusion models.

### Strengths
1) The paper is reasonably well written and easy to follow 
2)  The quantitative results demonstrated in Table 1 and Table 2 shows that the model outperforms state of the art.

### Weaknesses
1) The paper is not sufficiently novel. I'm not working in this domain, but the only novel part that the authors state is creating the collage of the patches in the feature / latent space based on their spatial embeddings. This does not sound like something that has not been done before in the field of image generation. It would  be helpful if the author come up with a more comprehensive literature survey that provides more related works to this particular  design choice and clearly shows the difference. For example, from a short search I found the following relevant paper: [1] https://arxiv.org/pdf/2207.04316.pdf --  Improving Diffusion Model Efficiency Through Patching 
[2] https://arxiv.org/abs/2304.12526 -- Patch Diffusion: Faster and More Data-Efficient Training of Diffusion Models (note the paper was first submitted on April 2023).

2) Even if we consider the combination of Patch Diffusion in the latent space sufficiently novel, from the analysis in the supplementary material, I find that faces demonstrate usual artifacts around eyes and mouse (and I think that this is happening despite training on a dedicated dataset). Midjourney models generate much better faces. It would be great to understand why the proposed model fails on those.

### Questions
1) Can you please add comparison to other techniques in the supplementary? It might be useful to reduce the example to great examples vs. poor examples and provide some discussion on failure modes
2) In Table 2 - "We bold the numbers to denote the best numbers in the same category." --> can you please explain what you mean by "the same category"

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a patch-based denoising diffusion model called Patch-DM for generating high-resolution images. The key contributions are: 1. Introduces a feature collage strategy to avoid boundary artifacts when synthesizing images from patches. It combines partial features from shifted patches to predict features for a new patch. 2. Achieves state-of-the-art FID scores on 1024x512 natural images and 1024x1024 LSUN/FFHQ images using a lightweight model. 3. Demonstrates Patch-DM can directly generate high-fidelity 1K resolution images with minimal patch boundary effects. 4.Reduces memory complexity compared to full-image diffusion models for high-res synthesis. 5.Shows applications like image outpainting, inpainting, super-resolution without any post-training. 6. Validates through ablation studies that feature collage is better than pixel collage for spatial consistency. 7. Provides an effective patch-based generative modeling approach using diffusion models for high-resolution image synthesis with reduced costs.

### Strengths
•	Proposes Patch-DM, a novel patch-based denoising diffusion model that can generate high-resolution images directly without relying on hierarchical sampling. This simplifies the sampling procedure.
•	Introduces a new feature collage strategy to avoid boundary artifacts when synthesizing images from patches. It forces consistency by combining partial features from shifted patches.
•	Achieves state-of-the-art FID scores on generating natural images and LSUN/FFHQ images using a lightweight model, outperforming prior patch-based methods.
•	Qualitative results show Patch-DM can produce high-fidelity 1K resolution images with minimal patch boundary effects.

### Weaknesses
•	Based on my experience and recent related publications (e.g., "Weather Diffusion-PAMI'23"), patch-based diffusion models often lead to reduced inference efficiency. I hope the authors can provide specific comparisons of inference time and overall efficiency, especially compared to previous GAN methods.
•	The proposed method has limited technical contributions. The authors did not provide detailed explanations or theoretical justifications to explain why the Patch Collage in Feature Space strategy can avoid artifacts. Furthermore, the research and exploration of Semantic Code are not sufficiently in-depth.
•	The authors should provide a quantitative comparison of image inpainting and image outpainting results. Quantitative results would better demonstrate the superiority of the proposed method.

### Questions
•	Why does the Patch Collage in Feature Space strategy avoid artifacts? Can a detailed analysis and explanation be provided? This is crucial for future work.

•	What is the running speed of the proposed method? How much slower does the Patch Collage in Feature Space strategy make the model inference speed?

•	What are the limitations or further areas of exploration for the proposed method?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work aims to resolve the limitation of the existing diffusion models towards generating high-resolution images. To this end, the authors present the ideas of feature collage, position embedding, and global conditioning to develop a unified approach, namely Patch-DM, to generate high-resolution images. Moreover, potential applications of outpainting and inpainting are also demonstrated. Comparisons on low-resolution images are conducted to reveal that the proposed method doesn't underperform by a large margin compared to other methods. Comparison of high-resolution images reveals that the proposed method achieves state-of-the-art results.

### Strengths
1. The ideas of feature collage, position embedding, and global conditioning and their impact on image generation is interesting.
2. The proposed method achieves state-of-the-art results on high-resolution image synthesis

### Weaknesses
1. On Low resolution image synthesis as in Table 2, the proposed method is not comparable to that of state-of-the-art. 
2. Some of the implementation details, reasoning behind choices, are missing in the description. Please refer to the comments under Questions for details.

### Questions
1. Section 5.2: Since every image is segmented into smaller patches, the total number of model parameters is much smaller than other large diffusion models. => The computations might be lesser, why should the number of model parameters be lesser? Authors argue that they use light weight models, but it’s unclear what architectural changes they made for it as compared to existing diffusion models, and how those changes are justifiable. In fact, authors might be able to generate better quality images with heavier architectures and make Table 2 performance comparable to that of previous diffusion models. 

2. Beyond patch generation: The first one is to add patches inside the original images so that the generated images can have a 2× resolution compared to the ones in the training dataset. => Why do we need to add patches to original images? During test time the images are supposed to be generated from random noise and hence there is no need for adding patches to original images. This sentence is confusing and should be rewritten for clarity. Also the position embedding adaptations is not well explained, so is the reason for different choices with respect to the two methods mentioned under this category.

3. Image inpainting: No details of the position embedding and the related changes is mentioned in this case. 

4. Image inpainting: The details could be incomplete. It is unclear how the original contents in the non-masked region is maintained in the output. Why is the global embedding not used?

Minor Fix: 
- Section 5.2, still be ”recovered” during => still be ``recovered'' during

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new feature collage strategy for the generative diffusion model to avoid boundary artifacts when synthesizing large-size images, termed Patch-DM. Feature collage systematically crops and combines partial features of the neighboring patches to predict the features of a shifted image patch, allowing the seamless generation of the entire image due to the overlap in the patch feature space. Experiments reveal the superiority of 1K resolution generation results on several datasets with 64×64 patches.

### Strengths
This paper proposes a new feature collage strategy for generative diffusion model to avoid boundary artifact when synthesizing large-size images.

### Weaknesses
1.	The novelty is relatively small and the impact of this paper may be limited since the proposed method only focuses on the boundary artifacts produced by the patch collage.
2.	Lacking comparisons with aggregation sampling strategies proposed in StableSR [1], the sampling strategy in StableSR can be performed without more parameters and training. 
3.	The experiments only measure models with FID, lacking results measured under other metrics, e.g., CLIPScore.
4.	Figures 5 and 6 look confusing. (Which pictures are from which datasets or methods seem to be unclear)

[1] Wang, J., Yue, Z., Zhou, S., Chan, K. C., & Loy, C. C. (2023). Exploiting Diffusion Prior for Real-World Image Super-Resolution. arXiv preprint arXiv:2305.07015.

### Questions
Can the model be performed to generate images of more than 1K or arbitrary resolutions?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

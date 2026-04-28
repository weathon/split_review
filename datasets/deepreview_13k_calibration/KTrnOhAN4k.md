# Discovery and Expansion of New Domains within Diffusion Models

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 6, 3, 5

## Abstract
In this work, we study the generalization properties of diffusion models in a few-shot setup, introduce a novel tuning-free paradigm to synthesize the target out-of-domain (OOD) data, showcase multiple applications of those generalization properties, and demonstrate the advantages compared to existing tuning-based methods in data-sparse scientific scenarios with large domain gaps. Our work resides on the observation and premise that the theoretical formulation of denoising diffusion implicit models (DDIMs), a non-Markovian inference technique, exhibits latent Gaussian priors independent from the parameters of trained denoising diffusion probabilistic models (DDPMs). This brings two practical benefits: the latent Gaussian priors generalize to OOD data domains that have never been used in the training stage; existing DDIMs offer the flexibility to traverse the denoising chain bidirectionally for a pre-trained DDPM. We then demonstrate through theoretical and empirical studies that such established OOD Gaussian priors are practically separable from the originally trained ones after inversion. The above analytical findings allow us to introduce our novel tuning-free paradigm to synthesize new images of the target unseen domain by discovering qualified OOD latent encodings within the inverted noisy latent spaces, which is fundamentally different from most existing paradigms that seek to modify the denoising trajectory to achieve the same goal by tuning the model parameters. Extensive cross-model and domain experiments show that our proposed method can expand the latent space and synthesize images in new domains via frozen DDPMs without impairing the generation quality of their original domains.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a method for sampling out of distribution (OOD) using diffusion models. The method is based on determining the latent distribution of the OOD under the pushforward of DDIM. Once this distribution has been estimated it is possible to sample from it and run the backwards DDIM to generate new OOD samples. The method has impressive results and provides insights into how to leverage pretrained diffusion models when the data is scarce which would make training a model unfeasible.

### Strengths
- The paper presents a novel method for sampling out of distribution
- The method doesn't require extra training and seems to generalize well as shown by the experiments

### Weaknesses
1. The paper also acknowledges that estimating the corresponding OOD prior from few-shot data is extremely challenging. Although certain conclusions from high-dimensional space offer insights for designing the algorithm, the current approach remains complex, combinatorial, and heuristic, and it is difficult to inspire further advancements in new work.

2. If my understanding is correct, the article does not compare an important category of approaches, namely, lightweight fine-tuning of large-scale diffusion models, such as Dreambooth+SD or LoRA+SD. I believe current lightweight fine-tuning methods on SD can now be completed quickly, even on a single GPU within tens of minutes, and typically require only around 10-20 images. Thus, these methods should serve as an important baseline for this article (and any future improvements).

3. I am also curious about the performance of such tuning-free methods on various large-scale diffusion models, such as the SD series, and their sensitivity to different network architectures (e.g., U-Net, DiT, U-ViT, etc.).

### Questions
See weaknesses, could you please provide more details on robustness of the hyperparameters. As well as explanations of the alternative methods for sampling from the OOD latents.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents an interesting finding: the latent space created by applying the DDIM Inverse to a pre-trained diffusion model shows unique priors, even for out-of-domain (OOD) images. Building on this observation, the paper introduces DiscoveryDiff, a tuning-free method for generating OOD samples from a few example images. This method is shown to generalize well across OOD distributions and outperforms other few-shot, tuning-based approaches. However, I feel the analysis section is unclear, and I have some questions about certain parts. With a clearer analysis, I believe this paper would be a strong submission.

### Strengths
1. This paper presents an interesting insight. In pixel space, different distributions are clustered in complex ways that are difficult to analyze or sample from directly. However, the paper shows that in the latent space created using the DDIM Inverse on a pre-trained diffusion model, these distributions are organized more clearly. This structure allows for effective OOD sampling using only a few example images.
2. The potential applications are valuable. In fields like physics and medical imaging, where generating data is costly, achieving few-shot OOD generation can be particularly useful.
3. The experiments in this paper are strong. I especially appreciate Figure 4, which demonstrates the diversity of generated samples compared to the few-shot examples. This also supports the existence of a "latent Gaussian prior."

### Weaknesses
I feel that the analysis section in this paper could be better. Here’s what I understand from it: first, the paper aims to prove the existence of a Gaussian prior (though I don’t fully understand Lemma 2.1; see my question on this). Next, it introduces a “mode interference” phenomenon and suggests that to avoid this, the Gaussian prior needs to be separable. Then, it examines the Gaussian properties and separability of the OOD distribution in latent space. Let me know if I’ve misunderstood anything.

I’m not convinced that the OOD distribution in latent space really approximates a Gaussian, as the proposed sampling method in line 394 also relies on Slerp interpolation. However, I do think there are likely some unique structures for OOD distribution in the latent space. A stronger analysis section could address questions like how these special structures for OOD distribution arise and what might provide a better approximation for this structure than the Gaussian model.

### Questions
1. In line 107, the author states that "DDIM exhibits latent Gaussian priors independent from the parameters of trained DDPMs". The author leverages this property for few-shot OOD generation. From the experiments in this paper, I believe these latent Gaussian priors exist, but are dependent on the parameters of trained DDPMs. Since using an initialized, not trained DDPM with DDIM could not achieve few-shot OOD generation. What's the author's opinion towards this independence?

2. Based on my previous hypothesis the latent Gaussian priors depend on the trained DDPM, could the author qualitatively compare the OOD generation using a different pre-trained diffusion model? Will the pretrained dataset affect the latent Gaussian priors? In other words, will the OOD generation have some dramatic change? 

3. I do not understand Lemma 2.1. For the diffusion model forward process, we have $p(x_t|x_0) = \mathcal{N}(\sqrt{\alpha_t}x_0, (1 - \alpha_t)I)$. So what is $q_{\sigma}(x_t|x_0)$? What it means when $q_{\sigma}(x_t|x_0) = p(x_t|x_0) = \mathcal{N}(\sqrt{\alpha_t}x_0, (1 - \alpha_t)I)$.

4. For your experiments, within the 5K generation in Table 2, are they all in the target domain? What's the proportion?

### Soundness
4

### Presentation
2

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work introduces a new method for domain adaptation of diffusion models. The main idea is to use DDIM inversion to find latent representations of OOD data. Given such representations, a heuristic method is used to select new latent codes that can result in viable new generations from the OOD domain.

### Strengths
- This work tackles an interesting and important topic: the adaptation of diffusion models to other domains, including scientific ones usually omitted by mainstream studies.
- The analysis of the distinction between latent representations of ID and OOD data, given their latent representations provided by reverse DDIM procedure, is insightful.

### Weaknesses
- There is a strong statement in line 095: "Very few existing works have explicitly investigated this task," - where the task is diffusion model fine-tuning to different domains. Numerous works are investigating this area - under the name of introducing new concepts, see [1] (with prior-preserving loss that tackles exactly the generalization problem), [2], [3], and many others. See, for example, the GitHub overview: https://github.com/wangkai930418/awesome-diffusion-categorized?tab=readme-ov-file#new-concept-learning. I am missing the clear distinction between few-shot learning of a new concept or styles presented in the plethora of works and "new domain learning" introduced in this submission.
- The presentation of this work needs to be improved. The (almost three pages long) introduction needs to be more accurate, as it highlights several entirely different problems that are not always related to the later results. The overview of related works omits several important positions.
- It is known that the latent representations calculated with the reverse DDIM procedure are not identical to the starting Gaussian noise. This is, by definition, given that the baseline DDIM approach is based on the assumption that the prediction of the noise removed from the image in the t-th backward diffusion step closely approximates the noise of the (t − 1)-th step. This is why several works try to mitigate this issue (see [4,5,6]). Is it possible that the distinction between ID and OOD data comes from the bigger error in the DDIM inversion?
- The presented method requires additional prior knowledge about the target domain (used by Geometrical Optimization) that might be costly to calculate
- The experimental evaluation misses important baselines defined as new concepts learning, as discussed in one of the previous points.
- The generated examples presented in Figure 8 in the appendix seem to be of poor quality. For the astrophysical data, we can see a collapse to a situation where the object of interest is located in the center of an image.

[1] Ruiz, Nataniel, et al. "Dreambooth: Fine tuning text-to-image diffusion models for subject-driven generation." Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2023.

[2] Gal, Rinon, et al. "An image is worth one word: Personalizing text-to-image generation using textual inversion." ICLR2023

[3] Qiu, Zeju, et al. "Controlling text-to-image diffusion by orthogonal finetuning." Advances in Neural Information Processing Systems 36 (2023): 79320-79362.

[4] Daniel Garibi, Or Patashnik, Andrey Voynov, Hadar Averbuch-Elor, and Daniel Cohen-Or. Renoise: Real image inversion through iterative noising. arXiv preprint arXiv: 2403.14602, 2024. URL https://arxiv.org/abs/2403.14602v1.

[5] Gaurav Parmar, Krishna Kumar Singh, Richard Zhang, Yijun Li, Jingwan Lu, and Jun-Yan Zhu. Zero-shot image-to-image translation. In ACM SIGGRAPH 2023 Conference Proceedings, pp. 1–11, 2023.

[6] Seongmin Hong, Kyeonghyun Lee, Suh Yoon Jeon, Hyewon Bae, and Se Young Chun. On exact inversion of dpm-solvers. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 7069–7078, 2024.

### Questions
I am not able to find the discussion about the adaptation to LDM models mentioned in footnote 4 in the appendices. I find it interesting to know if the distinction between OOD and ID data still holds, given that in LDMs "images (latent codes in the LDM autoencoder)" are normalized to follow Normal distribution, so they, and their representations calculated with inverse DDIM are more aligned with initial random gaussian distribution by definition.

### Soundness
2

### Presentation
1

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
This paper explores a tuning-free approach to generalizing pre-trained Diffusion Probabilistic Models (DDPMs) for out-of-domain (OOD) data synthesis in few-shot scenarios. By leveraging high-dimensional Gaussian priors, spherical interpolation, and geometric optimizations, the method avoids "mode interference" and expands DDPM applications to domains like scientific imagery and astrophysical data in few-shot settings. Extensive experiments demonstrate that this approach effectively synthesizes diverse, high-quality images, offering a new pathway for OOD generation in resource-limited and interdisciplinary settings (based-on domain-specific pre-trained models).

### Strengths
1. The paper introduces a paradigm for generating out-of-domain (OOD) data without modifying model parameters, allowing effective cross-domain generalization. This reduces computational costs, making it feasible for resource-limited scenarios.

2. Through geometric optimization and spherical interpolation, the method effectively mitigates "mode interference," ensuring that generated OOD samples remain distinct from the original training domain and improving the quality of target domain synthesis.

3. The approach is adaptable to various DDPM variants and applicable to diverse target domains (e.g., scientific imagery, astrophysical data), showing potential for cross-domain and interdisciplinary uses.

### Weaknesses
1. The paper also acknowledges that estimating the corresponding OOD prior from few-shot data is extremely challenging. Although certain conclusions from high-dimensional space offer insights for designing the algorithm, the current approach remains complex, combinatorial, and heuristic, and it is difficult to inspire further advancements in new work.

2. If my understanding is correct, the article does not compare an important category of approaches, namely, lightweight fine-tuning of large-scale diffusion models, such as Dreambooth+SD or LoRA+SD. I believe current lightweight fine-tuning methods on SD can now be completed quickly, even on a single GPU within tens of minutes, and typically require only around 10-20 images. Thus, these methods should serve as an important baseline for this article (and any future improvements).

3. I am also curious about the performance of such tuning-free methods on various large-scale diffusion models, such as the SD series, and their sensitivity to different network architectures (e.g., U-Net, DiT, U-ViT, etc.).

### Questions
1. Can the complexity, combinatorial nature, and heuristic aspects of the tuning-free approach be simplified or optimized to inspire further improvements in future work?

2. How effective is the tuning-free method on large-scale diffusion models like the SD series?

3. How does the tuning-free approach compare to lightweight fine-tuning methods (e.g., Dreambooth+SD or LoRA+SD), especially considering their efficiency in requiring minimal data and computational resources?

4. How sensitive is the tuning-free method to different network architectures, such as U-Net, DiT, and U-ViT?

5. How sensitive is the tuning-free method to different ode/sde samplers?

### Soundness
2

### Presentation
3

### Contribution
2

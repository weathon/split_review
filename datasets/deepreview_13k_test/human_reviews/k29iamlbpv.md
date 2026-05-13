# Hierarchical Clustering for Conditional Diffusion in Image Generation

- Decision: Reject
- Scores: 3, 5, 3, 5

## Abstract
Finding clusters of data points with similar characteristics and generating new cluster-specific samples can significantly enhance our understanding of complex data distributions. While clustering has been widely explored using Variational Autoencoders, these models often lack generation quality in real-world datasets. This paper addresses this gap by introducing TreeDiffusion, a deep generative model that conditions Diffusion Models on hierarchical clusters to obtain high-quality, cluster-specific generations. The proposed pipeline consists of two steps: a VAE-based clustering model that learns the hierarchical structure of the data, and a conditional diffusion model that generates realistic images for each cluster. We propose this two-stage process to ensure that the generated samples remain representative of their respective clusters and enhance image fidelity to the level of diffusion models. A key strength of our method is its ability to create images for each cluster, providing better visualization of the learned representations by the clustering model, as demonstrated through qualitative results. This method effectively addresses the generative limitations of VAE-based approaches while preserving their clustering performance. Empirically, we demonstrate that conditioning diffusion models on hierarchical clusters significantly enhances generative performance, thereby advancing the state of generative clustering models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces TreeDiffusion, an extension of TreeVAE which enhances its generation capabilities while maintaining its clustering performance. The major contribution of this work is to use diffusion models to generate samples using hierarchical structure learnt by TreeVAE. The authors also claim other minor novelties which are limited, e.g., they show that TreeDiffusion is able to generate cluster-specific samples; they replace the TreeVAE encoder-decoder architecture (which originally employed MLPs) with CNNs for better performance.

### Strengths
1. The paper is able to successfully overcome the limitations of  TreeVAE by using a diffusion model for generation. Particularly, the diffusion model is conditioned on the hierarchical structure learnt by TreeVAE to generate samples. 

2. The experimental results show significantly better FID achieved by TreeDiffusion compared to its counterpart, TreeVAE.

### Weaknesses
1. I think the authors should refrain from calling the proposed method as an 'unified framework'. This is because the TreeVAE is trained independently of diffusion model, and the proposed method is inherently two-stage.

2. The novelty of the proposed method is very limited. Let me elaborate: 
- There are two aspects of this work (a) hierarchical clustering and (b) conditional generation. The first part is taken as it is from TreeVAE with a minor architectural change (replacing the MLPs with CNN). Hence, the work should be judged on the basis of its novelty in conditional generation. For this part, the authors condition the reverse process on leaf-specific reconstruction and TreeVAE's hierarchical representation, $ p_\psi(x_{t-1}|x_t,\hat{x}_0^{(l)}, c_l) $ . 

- Now, DiffusionVAE does a similar job by conditioning the reverse process on just the reconstruction  $p_\psi(x_{t-1}|x_t, \hat{x}_0)$. The difference however is that DiffusionVAE doesn't operate on TreeVAE, rather, it operates on vanilla VAE. From this, TreeDiffusion (current work) can be looked upon as a way to extend DiffusionVAE from vanilla VAE to TreeVAE. This extension is achieved by an additional condition over $c_l$. Doesn't this make TreeDiffusion a trivial extension of DiffusionVAE?

3. In the above light, TreeDiffusion is still refining the output of decoded leaf-node, similar to DiffusionVAE.

4. Although DiffuseVAE doesn't incorporate hierarchical structures, one can still make comparisons with DiffuseVAE in terms of FID in Table 1. I think this is important given the relation outlined in second point.

5. There is one confusion in the visual comparisons with TreeVAE. Are these images obtained using the MLP-based encoder-decoder architecture or the CNN-based encoder-decoder architecture? 

6. I think one line of work that is not discussed in the paper but is closely related to unsupervised clustering is that of Unsupervised concept discovery  see [1,2,3]. I think it would be better to discuss these works, but comparison is not required.

7. Notationally, I would suggest the authors to use a different notation for hierarchical representations ($c_l$) which is similar to notation for decisions in the TreeVAE (line 168).

8. Authors follow the usual noising DDPM forward process. However, they alter the reverse process as shown in Eq. 7. Is this an ad-hoc change made by the authors? The reason for this question is that DDIM/DDPM make sure that marginal distribution remains the same as that is what is required in DDPM objective (cf. [4] for this). More specifically, DDIM and DDPM lead to same marginal despite having different joint forward distribution. Is there any such explanation for choice of Eq. 7?


Overall, I think that the paper is almost a trivial extension of DiffusionVAE. Hence I am resorting to a score of 3. However, I am ready to have a meaningful discussion with authors and am ready to alter the scores if the above points are appropriately addressed.


[1] Du, Yilun, et al. "Unsupervised learning of compositional energy concepts." _Advances in Neural Information Processing Systems_ 34 (2021): 15608-15620.

[2] Liu, Nan, et al. "Unsupervised compositional concepts discovery with text-to-image generative models."

[3] Su, Jocelin, et al. "Compositional image decomposition with diffusion models." _arXiv preprint arXiv:2406.19298_ (2024).

[4] Song, Jiaming, Chenlin Meng, and Stefano Ermon. "Denoising diffusion implicit models." _arXiv preprint arXiv:2010.02502_ (2020).

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This study enhances the TreeVAE model for image generation by utilizing TreeVAE-generated clustering information as conditioning input for a diffusion model. The generated images were compared with those generated by TreeVAE, showing a quantified improvement.

### Strengths
The approach is conceptually straightforward and easy to understand. The paper is well-written.

Integrating clustering with conditional generation could have broad applications, particularly for datasets with distinct objects without labels.

### Weaknesses
Novelty: although adapting TreeVAE for image generation is intuitively reasonable with improvement, the contribution appears incremental, i.e., simply combining TreeVAE with a diffusion model.

Experiments: the ablation studies and comparisons are insufficient to substantiate the model's effectiveness. While the proposed TreeDiffusion model shows better quantitative generation metrics than TreeVAE, this improvement may largely stem from the addition of the diffusion model itself. I recommend that the authors isolate this effect. Specifically, quantitative metrics are not provided for image generation with a vanilla diffusion model, either in the model comparison or in the ablation section.

Further clarification of the above comment: In Table 2, more metrics related to image generation are suggested to be provided. Table 3 is expected to include additional metrics beyond FID and include results for a vanilla diffusion model for comparison.

### Questions
It is expected that the combination of clustering representations with a diffusion model holds the potential to advance learning performance for at least one of these two areas. However, the current approach falls short of maximizing this synergy, for example, concluding similar to [1] with a more robust integration. I also encourage the authors to include more related studies in this general sense within the related works section.

[1] Li T, Katabi D, He K. Self-conditioned image generation via generating representations, NeurIPS, 2024.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces TreeDiffusion, a framework that enhances the image generation quality of hierarchical clustering models by conditioning a diffusion model on hierarchical features learned through TreeVAE. The approach leverages TreeVAE for generating latent hierarchical structures and subsequently applies a diffusion model for cluster-specific image generation. This two-stage setup aims to address the generative limitations of clustering-based VAEs, producing sharper and more diverse images within each cluster.

While the integration of hierarchical clustering with diffusion models is an interesting approach, the overall novelty of this paper is limited. The conditioning of diffusion models on latent structures, specifically from VAEs, is well-explored in generative modeling, as are hierarchical VAE approaches. Furthermore, the contribution of this work is ambiguous given that it primarily extends existing techniques without providing significant innovations in method or theory.

### Strengths
1. The paper presents a practical attempt to address clustering-based VAE’s limitations using diffusion conditioning, which enhances image quality and diversity in the generated samples.
2. The paper demonstrates the generative advantages of TreeDiffusion over TreeVAE, showing clearer images with reduced blurriness across datasets.

### Weaknesses
1. Both conditional diffusion models and hierarchical VAEs are well-established methods in generative modeling. This paper’s approach seems to be rather a simple combination of TreeVAE [4] and DiffusionVAE [2]. 
2. No quantitative comparison between the proposed approach and DiffusionVAE is provided, making it difficult to validate the effectiveness of the proposed TreeDiffusion. 
3. The experimental section includes visualizations of cluster-specific generation results. However, as described in Section 3.1, TreeVAE is used with only minor adaptations, resulting in identical clustering performance between TreeVAE and TreeDiffusion. Therefore, these visualizations alone do not demonstrate the contribution of this paper and seem redundant.
4. The experiments are limited to comparison with TreeVAE, which does not offer a comprehensive evaluation of TreeDiffusion's performance. Comparisons with state-of-the-art methods, e.g. LDMs [1], DiffuseVAE [2], KNN-Diffusion [3] et al., would be necessary to validate TreeDiffusion’s superiority and clarify its practical benefits over established baselines.

[1] Rombach, Robin, et al. "High-resolution image synthesis with latent diffusion models." Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2022.

[2] Pandey, Kushagra, et al. "DiffuseVAE: Efficient, Controllable and High-Fidelity Generation from Low-Dimensional Latents." Transactions on Machine Learning Research.

[3] Sheynin, Shelly, et al. "kNN-Diffusion: Image Generation via Large-Scale Retrieval." The Eleventh International Conference on Learning Representations.

[4] Manduchi, Laura, et al. "Tree variational autoencoders." Advances in Neural Information Processing Systems 36 (2023): 54952-54986.

### Questions
1. Diffusion models are known for their slow inference speeds. How do the inference speed and parameter overhead of TreeDiffusion compare to those of TreeVAE, e.g., the inference time and memory cost for generating one sample?
2. How can we generate a sample using TreeDiffusion during inference? If the second-stage diffusion model is conditioned on latent features provided by the TreeVAE encoder, does generating a sample require a reference image to extract these latent features?
3. The visual quality of DiffuseVAE appears to fall short of the results shown in the original paper. Could the authors clarify the cause of this difference? In the original DiffuseVAE, generated images seem to be much sharper and more diverse. 
4. Class labels alone could provide useful conditioning signals for training diffusion models. Have the authors compared the performance of class conditioning with that of conditions derived from TreeVAE?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces TreeDiffusion, a two-stage framework that combines a hierarchical clustering model (based on TreeVAE (Manduchi et al., 2023)) with a diffusion model to improve the generation quality. This approach addresses limitations in previous TreeVAE, where the clustering models could achieve hierarchical clustering, but suffer from poor generations. TreeDiffusion first learns a hierarchical latent tree and parameterize a diffusion model conditioned on the raw prediction sampled from the latent.

### Strengths
- The paper extends the idea of TreeVAE to TreeDiffusion, leveraging a diffusion model to improve the low-quality generation issue exposed in TreeVAE. With such a design, the model can conceptually provide both hierarchical representations and conditional generations conditioned on these representations.

- The idea of the paper is clear and straightforward to follow. The paper is overall clear writtent, facilitating a smooth reading experience. 

- The experiments included in the paper strongly support one of the authors' claim, where the generation quality is significantly improved in terms of both FiD measure and visualized images.

### Weaknesses
- There are some defaults in the math presentations of the paper. For example, it is not clear why in Eq(1) and Eq(2) the LHS equals to the RHS. 

- The method part does not explain how the model is trained. The authors only simply point out the path latents $z_{P_l}$ are used as conditions of the denoising UNet. It could be unclear to the readers who are not familiar with diffusion models. Although in appendix B the authors provide the parameterization of diffusion models, most of the depiction is from the original DDPM and DDIM paper. The authors should give credits to the previous paper and use more space in explaining the proposed method. 


- The paper does not conduct sufficient analysis on why the incorporation of diffusion models could improve TreeVAE and DiffuseVAE. Mathematically, does the TreeDiffusion objective make the ELBO shown in Eq (3) tightened? Does TreeDiffusion makes the latents and the images has better alignment in distribution or it improves the log-likelihood part? Alternatively, does the improvement comes from the increasing of the total parameter of the model (as we include Unet as additional parameters)? 

- Although the authors claim TreeDiffusion demonstrates a new conditional generation control, I did not find clear evidences on how the the latent conditions provide a better or novel control in the generation. More specifically, does the hierarchical latents provide instance-level or any fine-grained conditioning in the generation? 

- Considering the previous point, the proposed method seems to simply uses a diffusion model as a post-processing way to extend the TreeVAE and DiffuseVAE only in generation quality, while it could be more interesting if the authors could examine whether there are more outcomes in the hybrid model.

### Questions
Please see the weakness.

### Soundness
3

### Presentation
3

### Contribution
2

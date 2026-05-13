# Diffusion priors for Bayesian 3D reconstruction from incomplete measurements

- Decision: Reject
- Scores: 5, 3, 3, 5

## Abstract
Many inverse problems are ill-posed and need to be complemented by prior information that restricts the class of admissible models. Bayesian approaches encode this information as prior distributions that impose generic properties on the model such as sparsity, non-negativity or smoothness. However, in case of complex structured models such as images, graphs or three-dimensional (3D) objects, generic prior distributions tend to favor models that differ largely from those observed in the real world. Here we explore the use of diffusion models as priors that are combined with experimental data within a Bayesian framework. We use 3D point clouds to represent 3D objects such as household items or biomolecular complexes formed from proteins and nucleic acids. We train diffusion models that generate coarse-grained 3D structures at a medium resolution and integrate these with incomplete and noisy experimental data. To demonstrate the power of our approach, we focus on the reconstruction of biomolecular assemblies from cryo-electron microscopy (cryo-EM) images, which is an important inverse problem in structural biology. We find that posterior sampling with diffusion model priors allows for 3D reconstruction from very sparse, low-resolution and partial observations.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a framework for solving 3D inverse problems using diffusion models as a prior.  The diffusion-based posterior sampling (DPS) approach of Chung et al. (2023) is adopted.  Specifically, 3D structures are reconstructed from 2D projections using point-cloud based representations, adopting the point-cloud 3D diffusion model of Nichol et al. (2022).  The problem of cryo-electron microscopy is considered, demonstrating that the proposed approach allows 3D reconstructions from sparse, low-resolution and partial observations.

### Strengths
- A thorough but concise background on diffusion models in general, 3D diffusion models, and using diffusion models for posterior sampling is given, with fairly extensive references.
- Techniques are presented to further guide the diffusion prior, for example with a coarse 3D point cloud or by using information about subunits of the unknown 3D structure.

### Weaknesses
 - Novelty is somewhat limited since Chung et al. (2023) is adopted for the posterior sampling framework and Nichol et al. (2022) is adopted for the 3D diffusion model.  The main contributions are in combining these for cryo-EM.
- For the ShapeNet problem, the benchmark considered (maximum liklihood) does not include any regularizing prior and it is therefore not suprising that performance is poor. It would be more informative to consider a method that includes a typical regularizing prior but that is not a generative model. Specifically, a comparison against a method using a total variation prior, or similar, would be more appropriate.
- For the cryo-EM problem, again a maximum likelihood alternative is considered as a benchmark.  There are no comparisons against existing standard methods. For example, it would be useful to compare against established methods such as those based on expectation maximization or other iterative reconstruction techniques commonly used in cryo-EM.

### Questions
- How is a single estimated 3D shape recovered from approximate posterior samples?  In figures do you just show an example posterior sample or do you compute, for example, the mean?
- Do you use posterior samples to quantify uncertatinties?
- The benchmark maximum likelihood (ML) reconstructions do not impose any prior information, hence it is not surprising this approach performs poorly.  What type of regularizing prior would typically be considered for such problems?  An alternative prior might provide more meaningful results for comparison.
- For the cryo-EM problem, why is there an additional Truth row in Figure 2 based on a fitted mixture model?  Doesn't the PDB serve as the truth?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper investigates the application of a specific diffusion model-based method, named diffusion posterior sampling (DPS), to the 3D reconstruction problem in the context of CryoEM. The paper carefully describes how DPS can be adapted to CryoEM, detailed by explanation and formulation of the likelihood term. In the experiments, multiple datasets were used to demonstrate the better reconstruction performance achieved by DPS over the traditional maximum likelihood method. Overall, the main contribution of the paper is the application of DPS to the CryoEM problem.

### Strengths
The paper is clearly written.

### Weaknesses
1. **Insufficient Background Review:** There has been some literature on using diffusion models for solving the 3D reconstruction problem in Cryo-EM (Please see below). However, none of these or other similar work was reviewed and discussed in the background. Hence, it is unclear how the proposed method is different from the existing work.
   - DiffModeler: large macromolecular structure modeling for cryo-EM maps using a diffusion model. Nature Method
   - Latent Space Diffusion Models of Cryo-EM Structures. NeurIPS

2. **Lack of Novelty:** It appears that the proposed method is an adaption of DPS for Cryo-EM without novel algorithmic insights. While the formulation of the likelihood term is interesting, current manuscript lacks enough technical details to explain how the likelihood gradient is computed because the likelihood itself is an optimization problem.

3. **Missing Baselines:** The current experiments only include the maximum likelihood-based method as baseline, which is quite classic and cannot represent the current state-of-the-art. Thus, it is challenging to properly evaluate the performance of the proposed method in the context of modern Cryo-EM approaches.

### Questions
1. The authors are advised to provide more details on the computation of the likelihood and its gradient.
2. More recent methods should be included as baselines, such as Cryo-DRGN
   - 1 CryoDRGN: reconstruction of heterogeneous cryo-EM structures using neural networks

### Soundness
2

### Presentation
2

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
This paper proposes a 3D version of Diffusion Posterior Sampling (DPS) to solve 3D reconstruction problems given incomplete measurements. The method is applied to shape reconstruction and cryo-electron microscopy. For the task of shape reconstruction, it is compared to a maximum-likelihood-based approach which does not incorporate priors.

### Strengths
* The proposed method is sound, and it appears to be a viable solution for 3D reconstruction from cryo-EM images.
* The writing and figures are clear.

### Weaknesses
 * The technical contribution is not substantial. The only change from regular DPS is to use a point transformer in the diffusion model. The use of EDM (Karras et al. 2022) heuristics for the noise schedule and sampling scheme is also not a substantial contribution. The authors should clarify the novelty of their approach beyond these implementation details. Specifically, the adaptation of a point transformer architecture to the diffusion framework is not sufficiently justified, and the benefits of this specific choice over other architectures are not explored.
* The only baseline provided is a maximum-likelihood approach that does not use deep priors. What about other deep learning-based baselines, such as CryoDRGN (Zhong et al. 2020)? Without competitive baselines, it’s hard to assess the quantitative/qualitative results. The lack of comparison to other deep learning methods makes it difficult to determine if the proposed method offers any real advantage. The authors should also consider comparing against methods that use similar data inputs, even if the overall goal is different.
* In lines 75-76, the authors claim that DPS “has not yet been investigated in the context of 3D data.” This statement is much too strong, as extending DPS to 3D data is obvious. I’m sure it’s been investigated outside of published results, and just as one published example, Score-based Data Assimilation (Rozet and Louppe 2023) can be seen as an application of DPS to time-dependent 2D (i.e., 3D) data.
* In line 170, the authors say that “the guarantee of exactness is not of practical relevance.” Again this statement is too strong, and I don’t see how exactness would not be of practical relevance, especially for a scientific task like 3D cryo-EM. The authors should provide a more nuanced discussion of the importance of exactness, especially in the context of scientific applications where accuracy is paramount.
* Related to the previous point, calling this a “Bayesian” approach feels too strong (“Bayesian-motivated” or “Bayesian-informed” feels more appropriate). The DPS approximation of the time-dependent likelihood is extremely crude, leading to a posterior that’s very far from the true Bayesian posterior. Furthermore, the authors do not analyze the uncertainty of the estimated posterior beyond giving error bars in Tables 1 and 2. A more thorough analysis of the posterior uncertainty, such as through visualization or alternative metrics, is needed to support the claim of a Bayesian approach.

### Questions
I would appreciate comments from the authors regarding why other deep learning-based baselines were not included.

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a strategy for using a diffusion model for point cloud reconstruction from partial observations via reconstruction guidance. These partial observations may come from one or multiple inverse problems with known forward models; even though the observations are quite sparse (e.g. a handful of projected point clouds, or a subunit of the full 3D point cloud, or a low-resolution point cloud) the 3D diffusion model prior constrains the reconstruction to lie in the space of reasonable structures. The proposed method is validated on 3D point clouds from ShapeNet and from the Protein Data Bank.

### Strengths
- The proposed strategy is quite general within the context of 3D point cloud recovery, in the sense that it can operate with very sparse and very diverse types of measurements (as long as the forward model is known for each measurement).
- The method summary and theoretical introduction to diffusion models may be helpful to readers who are new to the topic, though they are not a novel contribution.
- The paper clearly shows benefits of diffusion posterior sampling compared to maximum likelihood estimation from the measurements alone (without the diffusion prior), across several inverse problems and datasets using 3D point clouds. I particularly appreciate the empirical demonstration that the maximum likelihood solution may not be in the support of the prior, if the prior is multimodal. This is shown in the paper via lower energy scores for maximum likelihood reconstruction, while visual and other quality metrics are higher for the diffusion posterior sampling reconstruction.

### Weaknesses
Experimental weaknesses
- Figure 1 shows “prominent example reconstructions that demonstrate the superior performance of DPS” (line 418). I would prefer to see randomly-chosen examples so that I can appreciate the average-case performance rather than potentially cherry-picked cases. It is important to understand the typical performance of the method, not just its best-case scenarios, especially when the method is intended to be broadly applicable across diverse datasets.
- Line 422 says that the structural models from DPS “show a lower degree of heterogeneity” than the model from maximum likelihood…where is this claim supported by experiments? The standard deviations reported in Table 1 tend to show higher variance for DPS compared to ML.
- The cryo-EM experiments in section 4.3 are said to be focused on the sparse-data regime because of interest in studying conformational heterogeneity. On the one hand, I completely agree that conformational heterogeneity is of great interest. On the other hand, it is not clear why the proposed method would be useful for recovering heterogeneous structures, or why we would need to focus on the sparse-supervision setting to study heterogeneity. The motivation for using a sparse-view setting to study heterogeneity is not clearly articulated, particularly since methods that explicitly model continuous conformational changes might be more appropriate.
- The cryo-EM experiments are all at relatively low resolution, while the authors acknowledge that recovering high-resolution details is the primary challenge in practice. What is the motivation for studying the medium-resolution setting, and are there any barriers to using your method at higher resolution? The lack of high-resolution experiments limits the practical impact of the work, given that high-resolution reconstruction is a major goal in cryo-EM.
- A major challenge in cryo-EM reconstruction is the low SNR of the projection images, yet in the experiments here it looks like the images used for sparse supervision are not noisy. I would find it more convincing to use many noisy projections for supervision rather than few noiseless projections, as this would be closer to the experimental setting for cryo-EM. The use of noiseless projections for supervision does not reflect the real-world challenges of cryo-EM, where noise is a significant factor.

Presentation weaknesses (roughly in order of appearance in the paper)
- In the text immediately following eq (1) and eq (2) there is a helpful interpretation of the equation in the Gaussian noise case. However, the text after equation 1 describes equivalence to “standard least-squares fitting” whereas after equation 2 the equivalence is to “regularized least-squares fitting”…why are these different? It is unclear why regularization is used in one context but not another, and this distinction should be clarified.
- Some recent related works should be discussed; these are listed under the questions section below in roughly chronological order. The most recent ones are concurrent work so I do not expect them to have been included in the initial submission, but the older ones are prior work that should be discussed. In particular, the contribution claim that “Using diffusion priors has previously not been explored to solve the 3D reconstruction problem in cryo-EM” should be made more nuanced in light of these prior works, to distinguish more specifically what is novel in the proposed approach.
- You might consider merging sections 3.1 and 3.2 into section 2, so that there is a smooth flow between introducing standard diffusion methodology and then the specifics of how you apply it to 3D point cloud reconstruction. In particular, equation 8 in section 3.1 is a generalization of equation 4 in section 2, and equation 9 in section 3.2 is nearly identical to equation 7 in section 2. 
- Table 2 is not referenced in the main text. I would suggest moving it to be inside the new section 2/3 and referencing it there.
- It would be great to include more line-level annotations in Algorithm 1, i.e. on lines 8, 9, and 10 individually rather than a single combined annotation on line 7.
- This is a very minor LaTeX bug, but throughout the paper the opening quotes are all backwards.
- Figure 2 caption says that “the second row shows all ten point clouds generated with DPS”…this does not seem to match what is actually in the second row of the figure, which would appear to be a single structure for each experiment.

### Questions
Please refer to some questions embedded in the weaknesses section. I also have some questions around how this work relates to other recent methods that use diffusion models in cryo-EM. It is understandable to not compare against these methods experimentally given their recency (though that would be great), but a brief discussion of similarities and differences would benefit the paper.
- Latent Space Diffusion Models of Cryo-EM Structures (https://neurips.cc/virtual/2022/61226), was at NeurIPS 2022. This paper considers a diffusion model in the latent space rather than 3D space, so it’s not directly comparable but might be worth including in the discussion of related work.
- Illuminating protein space with a programmable generative model (https://www.nature.com/articles/s41586-023-06728-8), was published in 2023 and bears similarity to the proposed approach (diffusion in 3D).
- Robust Single-Particle Cryo-EM Denoising and Restoration (https://ieeexplore.ieee.org/document/10447135?denied=), was at ICASSP 2024 and appeared on arXiv in January 2024. This paper does diffusion denoising in image/projection space rather than in 3D.
- Solving Inverse Problems in Protein Space Using Diffusion-Based Priors (https://arxiv.org/abs/2406.04239), preprint released in June 2024 so this might be considered concurrent, or at least very recent. I think this is the most similar to the proposed approach in that it considers several different protein-related inverse problems, and uses the diffusion model as a plug-n-play prior.
- DiffModeler (https://www.nature.com/articles/s41592-024-02479-0), preprint was posted in January 2024 but the published version was just released a week ago.

### Soundness
3

### Presentation
2

### Contribution
2

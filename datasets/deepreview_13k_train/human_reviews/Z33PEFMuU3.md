# Edge-preserving noise for diffusion models

- Decision: Reject
- Scores: 6, 6, 5, 6

## Abstract
Classical generative diffusion models learn an isotropic Gaussian denoising process, treating all spatial regions uniformly, thus neglecting potentially valuable structural information in the data. Inspired by the long-established work on anisotropic diffusion in image processing, we present a novel edge-preserving diffusion model that is a generalization of denoising diffusion probablistic models (DDPM). In particular, we introduce an edge-aware noise scheduler that varies between edge-preserving and isotropic Gaussian noise. We show that our model's generative process converges faster to results that more closely match the target distribution. We demonstrate its capability to better learn the low-to-mid frequencies within the dataset, which plays a crucial role in representing shapes and structural information. 
Our edge-preserving diffusion process consistently outperforms state-of-the-art baselines in unconditional image generation. It is also more robust for generative tasks guided by a shape-based prior, such as stroke-to-image generation. We present qualitative and quantitative results showing consistent improvements (FID score) of up to 30\% for both tasks. We provide source code and supplementary content via the public domain~\href{https://edge-preserving-diffusion.mpi-inf.mpg.de}{edge-preserving-diffusion.mpi-inf.mpg.de}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a novel approach to generative diffusion models by incorporating edge-preserving noise, which is a generalization of denoising diffusion probabilistic models (DDPM). The authors propose an edge-aware noise scheduler that alternates between edge-preserving and isotropic Gaussian noise, aiming to better capture the structural information in data. The model demonstrates faster convergence to the target distribution and improved learning of low-to-mid frequencies, which are crucial for shape and structural representation.

### Strengths
1. The paper provides a theoretical foundation for the proposed model, explaining how it generalizes DDPM and improves frequency learning.

2. The model's ability to better preserve structural information could have practical benefits in various image generation and editing applications.

3. The paper presents a creative method for improving diffusion models by introducing edge-preserving noise, addressing a challenge in generative modeling.

4. The method shows substantial improvements in both qualitative and quantitative metrics, particularly in reducing FID scores and enhancing image generation quality.

### Weaknesses
1. The paper does not discuss the computational cost of the proposed method compared to existing approaches, which is an important consideration for practical applications. Suggesting comparisons with existing methods on these metrics could provide valuable context. For instance, a table comparing memory usage and speed (inference and training) across baseline models could highlight this model's practical viability more clearly.

2. While the paper demonstrates improvements on a specific dataset, it is unclear how well the model generalizes to other types of models or tasks. Testing on tasks that emphasize diverse structural features, such as denoising or inpainting, could provide insight into how well the model maintains performance across broader applications.

3. The current evaluation uses limited metrics to assess the effectiveness of the proposed method. Including newer metrics like CLIPScore, etc. could provide a more comprehensive view of performance. Specifically, CLIPScore could offer insights into the model's ability to generate semantically consistent images. Given the model's edge-preserving focus, metrics that capture detail preservation and structure alignment might also be beneficial.

4. While the paper compares the proposed method with existing baselines, it could benefit from a more detailed comparative analysis with other state-of-the-art methods, especially those that also aim to preserve structural information in images.

5. The performance of the proposed model may be highly sensitive to the choice of hyperparameters, such as the transition function and edge sensitivity. The paper could provide **more insight** into how these parameters affect the model's performance and **how to select** them effectively.

### Questions
None

### Soundness
3

### Presentation
2

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
This paper introduces a novel edge-preserving diffusion model that generalizes denoising diffusion probabilistic models (DDPMs). By incorporating an edge-aware noise scheduler, the model retains structural information in images, converges more rapidly to the target distribution, and better captures low-to-mid frequency components within datasets, which are crucial for representing shapes and structural details.

### Strengths
This paper proposes an interesting approach to improve the generation quality of diffusion models.
The experiments are extensive, and the visualizations are clear, helping readers understand the improved generation performance.

### Weaknesses
1. Does edge-aware noise affect generation diversity?
2. In the "Related Work" section, you initially describe IHDM as an isotropic Gaussian blurring model, yet later refer to it and BNDM as incorporating a form of non-isotropic noise. This creates a seeming contradiction that would benefit from further clarification to ensure the logical coherence of your manuscript.
3. While the paper makes a commendable effort to integrate the anisotropic diffusion concept from Perona and Malik (1990) into the diffusion model framework, the innovation appears to be primarily an application of existing theory rather than a novel theoretical contribution. The incorporation of edge-preserving noise as a new term in the diffusion process, while potentially enhancing the model's performance in certain aspects, does not fundamentally alter the underlying principles of generative diffusion models.
4. The discussion surrounding Eq. (2) and Eq. (3) in the paper is somewhat perplexing due to its circuitous approach. The authors explore the relationship between diffusion models and heat conduction, as well as the limitations of isotropic noise, before returning to the contributions of Perona and Malik (1990) in Eq. (10). A more effective strategy would be to engage with Perona and Malik's work on edge-preserving diffusion earlier in the discussion. This would create a natural transition to Eq. (12), which introduces the paper's core innovation—a novel noise term.
5. In the "Background" section, when discussing the "Forward and backward process posteriors," you utilize the formulation presented in Eq. (1), which is consistent with the isotropic Gaussian process. However, you also reference Eq. (2), which is derived from the heat dissipation process and represents a different formulation. My concern is that the use of both Eq. (1) and Eq. (2) in this context may create confusion, especially since your novel edge-preserving noise scheme seems to be more aligned with the principles of Eq. (1), as inferred from the derivations in Section 4.2. It appears that your improved noise term is inspired by the anisotropic diffusion work of Perona and Malik, which is more closely related to Eq. (2). Yet, the parameter calculations and posterior calculations in your model follow a form similar to Eq. (1). If this is the case, then the inclusion of Eq. (2) in the introduction might be seen as unnecessary, and it could potentially detract from the clarity of your paper. I would recommend either providing a more explicit connection between your noise model and Eq. (2), or if Eq. (2) is not central to your approach, consider streamlining the presentation to focus on Eq. (1) and its relevance to your edge-preserving noise scheme. This would help readers to better understand the relationship between your work and the existing literature and clarify why both equations are presented if they are not both integral to your model.

### Questions
Please refer to the Weakness section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper modifies the original DDPM formulation by Ho et al., altering the noise schedule to concentrate in localized regions according to the gradient magnitude of the image $\frac{|| \nabla_{\mathbf{x}_0}||}{\lambda(t)}$ and edge sensitivity $\lambda(t)$, offering control over different frequencies modelled during training. This approach leads to up to improvement in FID over the DDPM baseline, and the results qualitatively demonstrate finer details and better structure can be modeled.

### Strengths
The idea is intuitively simple and straightforward to incorporate into generative imaging applications. It has the potential to offer fine-grained control over the geometric structure captured in the diffusion process. Quantitative and qualitative improvements are demonstrated over baselines across several datasets.

### Weaknesses
Substantial advances in the diffusion community have not been discussed or incorporated adequately within this paper. Therefore, it is not clear to the community whether this approach will offer significant benefit when scaling to larger problems or stronger baselines. In particular:

* The reported FIDs and qualitative results do not seem competitive with current state-of-the-art diffusion models. FIDs of around **26.15** for 128$\times$128 seem too high. Zhang et al., 2022, "Dimensionality-Varying Diffusion Process", attain CelebA 128^2 of around **~6**, $\infty-$Diff (Bond-Taylor et al., ICLR 2024) receives FID_CLIP on CelebAHQ of ~3, and recent diffusion papers attain ~2 on even more difficult datasets such as ImageNet (see the review in Hoogeboom et al., "Simpler Diffusion" Table 3, covering low FID 2023/2024 papers).
* Recent advances in Flow Matching (Lipman et al., ICLR 2023) offer a simpler theoretical framework, offering a direct (near optimal) path through the transition space—demonstrated in real-world settings such as StableDiffusion3. This could simplify the edge-preserving schedule, and make it easier to control than Ho el al., schedule derivation, while giving improved samples. Likelihood estimates can also be attained through FM. I would like to see discussion or comparison.


### Questions
* It is not clear whether NLLs can be approximated easily with this approach, potentially limiting the applications. Please clarify or demonstrate this.
* The time-varying edge sensitivity $\lambda(t)$ seems arbitrary in section 5, and is currently dependent on Ho et al.,'s schedule, tying this down to similar variants. 
   * Can the main theory be better abstracted and demonstrated in different diffusion frameworks?
   * Is the approach suited for Flow Matching?
* Implementing this within a modern diffusion framework/architecture that efficiently supports high-resolution datasets would be beneficial to quantitatively evaluate improvements.
   * How does this scale with FFHQ $1024^2$ or ImageNet-$128$?
* Please clarify how $|| \nabla_{\mathbf{x}_0}||$ is implemented. Is this approximated with a Sobel filter?

### Soundness
2

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
3

### Summary
The authors proposed a variant of DDPM, named content-aware diffusion models, putting more focus on the edges. They made some modifications on the noise scheme to make it edge-preserving noise, and edit the formula for forward and backward calculation as well.

### Strengths
The authors proposed an interesting idea about how to keep the content clear and stable during the diffusion process, assuming the loss of detail content is caused by the isotropic noise scheme (like DDPM), by adopting existing research ideas from image processing area.

### Weaknesses
1. Experimentations might not be enough, especially in the quantitative comparisons with other existing works. Especially, if you want to state your proposed methods can be more content-aware compared to “isotropic diffusion models”, but not ONLY “DDPM”, then you have to compare it with other recent “isotropic diffusion models”. 
2. In addition, although with good explanation and math works, I’m feeling like this adaptation is more like adding an “weight matrix” to a specific focus, via an existing formula learned from image processing domain, during the diffusion process, and thus might not be impactful/novel enough. I would like to also hear other reviewers’ comments.

### Questions
1. “While the visual improvement over DDPM is subtle, our model generally demonstrated greater robustness to artifacts.” May I ask where can I see the experimentation results support this statement?
2. “In practice, we didn’t notice any increase in training/inference time.” May I ask what are the approximate numbers for the training/inference time?

### Soundness
2

### Presentation
2

### Contribution
3

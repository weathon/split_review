# Diffusion Bridge Implicit Models

- Decision: Accept
- Scores: 8, 6, 6, 6, 5

## Abstract
Denoising diffusion bridge models (DDBMs) are a powerful variant of diffusion models for interpolating between two arbitrary paired distributions given as endpoints. Despite their promising performance in tasks like image translation, DDBMs require a computationally intensive sampling process that involves the simulation of a (stochastic) differential equation through hundreds of network evaluations. In this work, we take the first step in fast sampling of DDBMs without extra training, motivated by the well-established recipes in diffusion models. We generalize DDBMs via a class of non-Markovian diffusion bridges defined on the discretized timesteps concerning sampling, which share the same marginal distributions and training objectives, give rise to generative processes ranging from stochastic to deterministic, and result in diffusion bridge implicit models (DBIMs). DBIMs are not only up to 25$\times$ faster than the vanilla sampler of DDBMs but also induce a novel, simple, and insightful form of ordinary differential equation (ODE) which inspires high-order numerical solvers. Moreover, DBIMs maintain the generation diversity in a distinguished way, by using a booting noise in the initial sampling step, which enables faithful encoding, reconstruction, and semantic interpolation in image translation tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents a theoretically justified method for fast sampling from DDBMs. The authors introduce non-Markovian diffusion bridges and derive the sampling procedure with the same marginals for discrete time steps. They show that the training objective of the proposed methods is equivalent to the DDBM objective on the discretized timesteps. The method is validated on image-to-image translation problems using edges2handbags and DIODE-Outdoor datasets and inpainting tasks using the ImageNet dataset. The proposed method achieves comparable results with DDBM on NFE > 100 while using only NFE = 20 for these problems regarding FID, LPIPS, and MSE.

### Strengths
1. The paper proposes fast sampling for the DDBM method, which achieves impressive results for image-to-image translation problems. Enhancing and accelerating DDBM is essential since these models provide a solid alternative to Flow Matching and Schrodinger Bridge methods for image-to-image problems. 
2. The proposed method is training-free and doesn't require any model parameter fine-tuning. Proposition 3.2 establishes equivalence between DDBM and DBIM objectives up to the constant.
3. Experimental results, which prove that deterministic sampler with $\eta = 0$ leads to better results than stochastic samplers with $\eta > 0$ is novel for DDBM, which suggests operating with stochastic samplers and may provide "averaged" or blurry outputs given initial conditions. This result allows further improvement of DDBM with distillation methods for deterministic samplers like consistency distillation (Consistency Models, ICML-2023).

### Weaknesses
In my opinion, the paper doesn't have significant weaknesses. However, some comments should be discussed additionally:
1. I think comparing the best competitor on the inpainting problem according to Table 3 - the I2SB method - is not enough. According to the I2SB paper, this method can repaint the masked region with semantic structures with only 2-10 NFEs for the inpainting problem with freeform masks. I suggest that the authors compare their method with I2SB for the inpainting problem with freeform masks and show the dependence of its quality (LPIPS, FID) on small NFEs (1-20) following setup from I2SB.
2. The idea of incorporating non-Markovian diffusion bridges seems not novel. For example, the I3SB method (Implicit Image-to-Image Schrodinger Bridge for Image Restoration, https://arxiv.org/abs/2403.06069) shares similar ideas and parameterization for I2SB. I suggest the author add the discussion of this paper and the main differences between their method and I3SB.
3. The diversity of the proposed method should be evaluated quantitatively. It is worth showing how small $\eta$ and NFE values degrade diversity compared to stochastic models. I suggest that the authors compute the diversity score from CMDE (Conditional Image Generation with Score-Based Diffusion Models, https://arxiv.org/abs/2111.13606) as in BBDM (BBDM: Image-to-image Translation with Brownian Bridge Diffusion Models, CVPR-2023).

### Questions
Questions:
1. Can you compare your method with I2SB for inpainting with freeform masks and evaluate I2SB on small NFEs?
2. Can you discuss the limitations of your method or provide failure cases? 
3. Can you comment on how much slower high-order methods are than first-order methods regarding inference time? Does the quality improve further for bigger orders like 4?
4. Can you additionally provide inference time for DBIM and other methods to show the inference time acceleration?
5. I suggest the authors consider the other method of DDBM acceleration using consistency distillation and include its discussion in the literature review; see Consistency Diffusion Bridge Models (NeurIPS-2024). 
 
Typos:
1. It looks like in Eq. 7, it should be \bar{w}_{t} instead of w_{t}.

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
3

### Summary
The paper proposes an extension of DDBM by adopting the ideas from DDIM for the bridge problem (translating one distribution to another with diffusion).

### Strengths
The paper novel in the sense that it proposes to adopt the ideas from DDIM (fast sampling, non-markovian diffusion) to the bridge problem, thereby enhancing DDBMs and expanding the practitioner’s toolset for such kind of problems. So, “creative combinations of existing ideas” - is the best description of the presented research. Also, I would like to notice good experimental section.

### Weaknesses
The majority of my concerns are in the "Questions" section. To be honest, I didn’t check Proposition 3.2 - but it seems to be correct. Proposition 4.1 - also not carefully checked by me, but seems to be correct.
What I do not like much about the paper is that some particular formulas and results (see point 2 in my questions) are stated as is, without proof/reference to the proof. It complicates reading and checking the results.
Some other weaknesses:
1. You have "Related works" section (A) in the Appendix. Ok, but I didn't find a reference to this section from the main text. Furthermore, I think it is important to somehow cover related works in the main text (maybe, with some references to the appendix)
2. No source code in the submission. It is important for reproducibility.

### Questions
1. Appendix C.1, lines 892-897. Why do you take gradient $\nabla_{x_{t_{n+1}}} \log q^{\rho} (x_{t_{n + 1}} \vert x_0, x_T)$, not $\nabla_{x_{t_{n+1}}} \log q^{\rho} (x_{t_{n + 1}} \vert x_0, x_{t_n}, x_T)$. Also, the eq. 50 is incorrect, while the result (lines 904 - 906) is correct. Please check the derivation.
2. Line 256 - The statement that $x_T$ is cancelled out under the choice of $\rho_n$ seems to be correct, but a link to the proof should be given.
3. Do I understand correctly, that different variants of variance parameter $\rho$ appear only at inference, i.e., training with eq. 13 is agnostic to $\rho$? 
4. You mention that eq. (8) (from DDBM) is equivalent to (16). But on par with (16) you have additional booting noise required by theory. How previous works (e.g., DDBM) manage to avoid the necessity of this noise? 
5. Lines 427 - 428: ‘straightforward mapping without the involvement of stocahsticity’ - but you have booting noise still, yes?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors construct an intriguing process that aligns with the marginal distributions and the well-known diffusion bridge. Building on the success of DDBM in modeling paired distributions at given endpoints, the authors introduce Diffusion Bridge Implicit Models (DBIMs), emphasizing discrete steps over continuous diffusion. Robust empirical techniques are employed in real-world experiments, significantly enhancing prediction performance.

### Strengths
1. Clear derivation to extend DDBM with DDIM properties. 

2. Nice connections to existing literature such as I2SB, flow matching, and exponential integrators.

### Weaknesses
the notation of $q_{tT}$ in Eq.(7) is confusing.


NIT - the literature section should be revised significantly, for example, Schrodinger in line 502: Schr"odinger, schrodinger in line 509, 600, 606, sde line 521, rosenbrock in line 543, Dpm-solver in line 576, ode in line 644 should have properly capitalized letters.

### Questions
1. DDBM proposed the pred-x parameterization motivated by the EDM framework to enhance the predictions and derive a set of scaling functions for distribution translation.  Is your work applicable to this extension? If not, what are the challenges?

2. Any intuitions on why a non-Markovian property is preferred?

NIT: some discussions on OT-accelerated diffusions, such as [1,2], may be helpful.  

[1] https://arxiv.org/pdf/2110.11291
[2] https://arxiv.org/pdf/2405.04795

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors consider the denoising diffusion bridge models (DDBMs [1]) recently proposed as a variant of diffusion models useful for interpolating between two paired distributions. The authors propose a way to accelerate this type of diffusion model without retraining them. The proposed method and the paper are mostly analogical to the Denoising Diffusion Implicit Model (DDIM) [2], which is used to accelerate classical diffusion models for generation such as DDPM [3]. In the experimental section, the authors use the same setups and models as in DDBMs and show that the proposed sampling scheme outperforms the sampling scheme of DDBMs.

### Strengths
- The approach is presented and sufficiently supported by the theoretical derivations.
- The authors support their method by showing that it indeed achieves significant speed-up of the inference on the same setups as were considered in the DDBM paper while preserving the quality.
- The method does not require retraining and is implemented just by a different sampling of the DDBMs models.

### Weaknesses
The general approach of obtaining a new sampling scheme in analogy to DDIM is known and has already been used for a different type of bridge process in SinSR [4], CVPR 2024, used for super-resolution problems. Specifically, the difference is that in SinSR, the bridge process $q(x_t|x_0, x_T)$ for a given low-resolution image $x_{T} = y$ and a given high-resolution image $x_0$ is given by:
$$q(x_t|x_0, x_T) = \mathcal{N}(x_t|x_0 + \eta_t(y-x_0), k^2\eta_t I), $$
and $\eta_t \rightarrow 1$, while in the current paper, the bridge process $q(x_t|x_0, x_T)$ is given by:
$$
q(x_t \mid x_0, x_T) = \mathcal{N}(a_t x_T + b_t x_0, c_t^2 I),
\quad a_t = \frac{\alpha_t}{\alpha_T} \frac{\text{SNR}_T}{\text{SNR}_t},
\quad b_t = \alpha_t \left( 1 - \frac{\text{SNR}_T}{\text{SNR}_t} \right),
\quad c_t^2 = \sigma_t^2 \left( 1 - \frac{\text{SNR}_T}{\text{SNR}_t} \right),
$$
where $SNR_t = \frac{\alpha_t^2}{\sigma_t^2}$ and $c_t^2 \rightarrow 0$ for $t \rightarrow T$.

Thus, there are two differences. The first one is that in SinSR, the process ends in the Gaussian with center $x_T$, while in the current work, the process ends in the delta function. The second is the different parametrization of these processes. To conclude, the methods SynSR & DBIM (proposed here) are not directly equivalent but one can be derived analogously to the other one with some effort.

### Questions
I do not have any particular questions. In my opinion, this is a borderline paper which can be accepted if the space permits.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors present a fast sampling approach to Denoising Diffusion Bridge Models (DDBMs, Zhou et al.) by constructing a DDIM (Song et al.) analogue of DDBMs and hence denote it as Denoising Bridge Implicit Models (DBIMs). The authors empirically demonstrate the advantages of the proposed method on several image translation and restoration benchmarks. The authors also illustrate the application of DBIMs for reconstruction and interpolation using latent space traversal.

### Strengths
I found the paper relatively straightforward to follow. Unsurprisingly, the empirical results support the claims in the paper as DDIM leads to significant improvements in sampling efficiency over vanilla DDPM. Therefore, it is to be expected that similar variants of other stochastic processes could achieve similar gains (See [1]).

### Weaknesses
Please see below.

**Reinventing the wheel**: My main concern with the paper is that the authors try to reinvent the DDIM framework in the context of a very specific class of stochastic processes (DDBMs in this case) when previous works already define a framework for generalizing over DDIM (as also noted by the authors in the paper in Sec 5.1, higher order methods and Appendix D). More specifically, Pandey et al.  [2] present a generic framework, Conjugate Integrators, for efficient diffusion model sampling of which DDIM and exponential integrators are special cases (See Section 3.1). As a consequence, their framework can be used to enable fast sampling from any pretrained diffusion/flow/interpolant models. Similarly, [1] presents generalized DDIM, which is a special case of Conjugate Integrators and can be applied to diffusion models like CLD or Blurring diffusion models. The main idea of all these methods is to modulate the drift of the reverse diffusion/flow process to enable fast sampling during inference (See also [3] for a similar approach). Since DDBMs also possess a semi-linear drift, extending these generic frameworks to obtain the corresponding DDIM sampler for DDBMs is trivial without delving into the non-markovian formulation of the original DDIM paper.
Consequently, I feel the paper does not offer any new perspective and the flow is very similar to the DDIM paper (defining the non-markovian process followed by setting rho=0 to enable deterministic sampling). Can the authors clarify how their work presents any novel insights compared to the original DDIM paper (or other works mentioned here [1,2]) since this is not obvious to me from the current explanation in the main text?

**Empirical Comparisons**: Although not my main concern, the empirical comparisons seem a bit unfair. For instance, in Table 3, the authors use $\Pi$-GDM and DDRM as comparison baselines, while these methods are task-agnostic and can be adapted for solving different inverse problems using a single pretrained diffusion model prior. However, following Eq. 9, DDBMs/DBIMs require paired data (x_0, y) for training and thus task-specific. Comparing task-specific models with task-agnostic models seems unfair. Moreover, other important baselines based on flow matching [4] or stochastic interpolants [5] are missing, which have advanced quite a lot in terms of sample quality recently [6]. I would recommend updating Table 3 to remove some baselines like DDRM and Pi-GDM and instead compare DBIM with the latest flow matching or interpolant models.

**Dubious claims**: The authors state the following in the Introduction: 
```
Adapting diffusion models to scenarios where a more informative prior naturally exists, such as image translation/restoration, requires cumbersome techniques like adding conditions to the model (Ho & Salimans, 2021; Saharia et al., 2022), modifying the generation pipeline (Meng et al., 2022; Su et al., 2022) or adding extra guidance terms during sampling (Chung et al., 2022; Kawar et al., 2022). These approaches inevitably result in either sub-par performance or slow and resource-intensive inference processes.
```
I agree that task-agnostic models like DPS or $\Pi$-GDM require extra guidance terms in their sampling process, making inference slow due to expensive Jacobian-vector products. However, in my opinion, a slower sampling process (though there is some recent work to mitigate slower sampling in solving inverse problems using diffusion models [7,8]) will likely be acceptable over training new models for each task. Moreover, these methods are more scalable in practice due to their adaptiveness to different restoration tasks while requiring no paired data. On the other hand, task-specific methods will likely require large paired datasets, which can be expensive to acquire. Therefore, certain models are better suited for specific applications (as also implied by the No-Free lunch). Therefore, this claim in the introduction seems misleading to me. It would be great if the authors could update this claim to more accurately reflect the nuances of different approaches, including recent advancements in mitigating slower sampling for task-agnostic models. Moreover, it would be nice to discuss how their method fits into the broader context of these trade-offs and under what scenarios it might be preferable to use DBIM versus a more general, task-agnostic method.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
2

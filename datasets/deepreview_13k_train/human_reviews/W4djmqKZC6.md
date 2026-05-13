# Pixel-Aware Accelerated Reverse Diffusion Modeling

- Decision: Reject
- Scores: 3, 3, 3, 3, 3

## Abstract
We propose in this paper an analytically new construct of a diffusion model whose drift and diffusion parameters yield a faster time-decaying Signal to Noise Ratio in the forward process. The proposed methodology significantly accelerates the forward diffusion process, reducing the required diffusion time steps from around 1000 seen in conventional models to 200-500 without compromising image quality in the reverse-time diffusion. In a departure from conventional models which typically use time-consuming multiple runs, we introduce a parallel data-driven model to generate a reverse-time diffusion trajectory in a single run of the model. The construct cleverly carries out the learning of the diffusion coefficients via an estimate of the structure of clean images. The resulting collective block-sequential generative model eliminates the need for MCMC-based sub-sampling correction for safeguarding and improving image quality, which further improve the acceleration of image generation. Collectively, these advancements yield a generative model that is at least 4 times faster than conventional approaches, while maintaining high fidelity and diversity in generated images, hence promising widespread applicability in rapid image synthesis tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a modification to the forward process of a diffusion model by varying the diffusion schedule for each pixel based on that pixel's initial value. This results in faster convergence to Gaussian white noise than the standard forward diffusion process, which is not pixel-aware. Then, in order to perform the reverse process during inference, an auxiliary model is used to predict the per-pixel noise schedule at each time step. This formulation allows sampling from the diffusion model with fewer time steps and additionally makes it possible to parallelize across time steps, generating the entire reverse trajectory in a single forward pass of the model.

### Strengths
The overall observation that the diffusion schedule can be pixel-dependent is a reasonable one, and some of the theoretical analysis showing the connection between $x_0$ and the corresponding PSNR trajectory is interesting. Additionally, the fact that this enables parallelized one-shot inference is a nice extension of the approach. Overall, the goal of accelerating diffusion is valuable, and this paper makes some progress to that end.

### Weaknesses
My main concerns have to do with limited comparisons to past work, sensitivity to hyperparameters, and insufficient justification/ablation. Specifically, the method is not compared to any SOTA approaches to diffusion acceleration, hyperparameter choices are not justified, and the sensitivity of the algorithm to the approximation of $x_\delta$ is not sufficiently analyzed. For more details see below --- it would be great for the author's to provide a response to these points.

Minor typos/issues:

L151: "offering" -> "offer

L160: "Gallager" \citep

L183: "SNRs 6 time steps" -> "SNRs over 6 time steps"

L191: "Furthermore, the" -> "Furthermore,"

L196 "over-all" -> "overall", "we proposed" -> "we propose"

L326: "atleast" -> "at least"

Figure 4 is rasterized and aliased

### Questions
How does this approach compare, both in terms of results and theoretically, to the many other works on diffusion acceleration? This includes distillation-based approaches such as "Consistency models" [Song et al. ICML 2023], sampler-based approaches (e.g.,"DPM-Solver" [Lu et al. NeurIPS 2022]), as well distribution-matching approaches ("One-step Diffusion with Distribution Matching Distillation" [Yin et al. CVPR 2024]). None of these or other related works are cited or discussed despite being very closely related. The only comparisons in the paper are to DDIM, DDPM, and SDE-based settling, which do not accurately reflect the SOTA.

Additionally, this approach is only demonstrated for pixel-space diffusion models, while many of the other works in diffusion model acceleration operate on latent space models, which are a more practical setting. Does the proposed approach generalize to latent diffusion models?

I am also wondering how sensitive the proposed algorithm is to hyperparemeters and how hyperameters were chosen in the paper. In particular, Section 3.2.1 mentions considerably different $T$ and $\gamma$ values chosen for the two datasets that the model was evaluated on. Is there a systematic approach to picking these values?

It would be good to include some additional analysis on how well the VAE is able to approximate $x_\delta$ (as opposed to $x_0$) and to what extent this error affects the result of the inversion diffusion. Figure 3 attempts to visualize this, but is difficult to parse and is not especially informative. In particular, the author claim that $x_\delta$ "lacks finer details" compared to $x_0$ due to the large $\gamma$, making it easier to approximate. However, isn't this a function of the timestep, i.e., for earlier timesteps, the value of $\gamma$ must be lower? I would be curious to see some elaboration on this topic, since it is a critical piece of the proposed method.

### Soundness
2

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
4

### Summary
The authors introduce a new generative method inspired by the water-pouring algorithm paradigm as an alternative to existing diffusion methods, offering faster generative sampling (with fewer denoising steps, achieving a speedup of 4x) to produce high-quality images. Each pixel has a unique scheduling function b_i, based on the signal-to-noise ratio (SNR) of the pixel.

### Strengths
It is an interesting alternative to existing methods. Incorporating pixel values into the scheduler is not a straightforward solution, and using the SNR with the water-pouring algorithm seems novel. The model has been evaluated on CelebA and CIFAR-10, demonstrating lower FID scores and faster sampling speeds.

### Weaknesses
Current literature includes other models that achieve high performance with lower sampling speeds. DDIM was the SOTA algorithm 3-4 years ago, and many improvements have been made since then. I would suggest that the authors also compare with the following:

**Consistency Models**:
- Consistency Models ([https://arxiv.org/abs/2303.01469](https://arxiv.org/abs/2303.01469))
- Improved Techniques for Training Consistency Models ([https://arxiv.org/abs/2310.14189](https://arxiv.org/abs/2310.14189))

**DPM-Solvers**:
- DPM-Solver: A Fast ODE Solver for Diffusion Probabilistic Model Sampling in Around 10 Steps ([https://arxiv.org/abs/2206.00927](https://arxiv.org/abs/2206.00927))
Several papers have been published following this line.

Additionally:

- It is unclear why the authors use the discrete formalism of DDPM in the background section, then apply their solution in a continuous scenario (Appendix B).
  
- Where does Equation (8) come from? Is it based on an assumption?

- A challenging part of the method is obtaining \(\overline{\alpha} = \prod \alpha_t\). How is this achieved in Equation (9)? I consider it tricky because applying the chain rule to go from \(x_0\) to \(x_t\) is complex:

x_{t-1} = \sqrt{\alpha_t} \cdot x_t + \sqrt{1 - \alpha_t} \cdot \epsilon = \sqrt{\alpha_{t+1}} \cdot (x_{t+1} + \sqrt{1 - \alpha_{t+1}} \cdot \epsilon) = ...

If \(\alpha\) depends on the signal, it becomes particularly hard to solve. Could you explain more clearly how these results were derived?

- **Figures**: ALL the figures need improvement. The text appears blurred and stretched, with inconsistent font sizes, making them hard to read. Figure 1, which presents the main concept of the paper, could be more impactful and should be revised to better communicate the work to the community. Figure 2 has small text on the axes and a stretched legend. Figure 3 does not add much context; the image in Figure 6 in the appendix is more interesting and from my point of view can substitute Fig. 3. Figure 4 is unclear due to color choices, labels, and structure. Figure 5a is difficult to interpret since the images are too small; it would be better to display a few images and compare them across different methods with the same seed.

### Questions
Already in the weaknesses.

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes to add uneven noise shedule to pixels according to their SNR, with higher SNR pixel diffuses faster than the lower one.

### Strengths
1. This paper proposes uneven noise diffusion of pixels according to their SNR. 
2. The forward process under this paradigm is well formulated.

### Weaknesses
1. This paradigm seems restricted to pixel space, since it requires the SNR of per pixel for differentiated diffusion. This may severely limits the practicality of this method, since most of existing diffusion models adopt latent space for efficiency. The requirement of per-pixel SNR calculation introduces a significant computational overhead, especially for high-resolution images, making it less practical than latent diffusion models which operate on compressed representations. The method's reliance on pixel-level SNR also means it cannot directly leverage the efficiency gains of latent space diffusion, which is a major limitation.
2. No proof for the claim. This paper claims less steps but lacks necessary evidences. Visualization or experiemtal results are rare. The claim of requiring fewer steps for image generation is not substantiated with theoretical analysis or sufficient empirical evidence. The lack of visualizations demonstrating the diffusion process and the intermediate steps makes it difficult to assess the validity of this claim. The absence of convergence analysis or a comparison of the number of steps required compared to standard diffusion models further weakens this claim.
3. Experimental results are quite few. This paper only conduct experiments on two small-scall/resolution datasets. Besides, the table1 and table2 are inprofession, where DDIM is sampler method instead of model. The experiments are limited to low-resolution datasets, which does not demonstrate the method's scalability or performance on more complex, high-resolution images. The use of DDIM as a comparison point in the tables is inappropriate since DDIM is a sampling technique and not a model architecture, indicating a lack of understanding of the existing diffusion model landscape. The absence of comparisons with other state-of-the-art diffusion models further limits the significance of the experimental results.
4. Poor writing. This paper seems like a semi-finished product. The writing lacks necessary polishing and is diffucult for understanding.

### Questions
1. Is it possible to extend this method to latent space? The SNR value in latent space may be different from the pixel space, since the latent is trained with KL loss to be Gaussian.
2. Will the optimization difficulty become harder as the resolution getting larger. The uneven pixel noise schedule may bring high uncertainty with higher resolution.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a new diffusion model that diffuses each pixel at a different rate based on its value, inspired by the water pouring algorithm. With a different forward and backward process than traditional DDPM or SDE-based methods, the authors show that their method can reduce the number of sampling steps at inference time. The authors evaluate their method on the CelebA and CIFAR datasets.

### Strengths
- The idea of considering the value of each pixel to determine the drift and diffusion rate, inspired by traditional water pouring algorithm, seems interesting and worth studying.

### Weaknesses
 - The motivation behind pixel-aware diffusion seems not clear to me. The water pouring algorithm is originally designed for communication systems but I am not sure how it benefits visual media such as image generation.
- This paper does not show how the new forward and backward processes look like, which would be useful for readers to understand better the motivation and how the proposed method changes visually the diffusion process.
- The writing and presentation of the paper can be greatly improved. For example, Figure 1 can be horizontal to have more spaces and can be easier to understand if the time-axis is put horizontally. Figure 2 is distorted. Figure 4 and the surrounding text are both not clear to me how the architecture is changed. Figure 5 should be shown without distortion and be following the style of Figure 7 and 8. Table 1 and 2 can be placed horizontally to save some space. In Line 194-195, DDIM should be from Song et al. In line 340, "on the hand" should be "on the other hand"? In 404-405, "Song et al." is repeated and the DDIM citation needs to be corrected. In appendix D line 5, it seems to introduce unnecessary symbols like the L for reverse diffusion noise predictions, which is not consistent to other works. Some citations seem missing, e.g., I did not find CelebA in the reference.
- To my understanding, the paper "Common Diffusion Noise Schedules and Sample Steps are Flawed" is related to this work. Their paper also introduces the idea of zero-snr and it makes sense to discuss the difference and even compare with it.
- The main results shown in table 1 and 2 seem not fair to me, especially on the number of sampling steps.
- The forward process is clear to me, but the reverse process (section 3.3) is not. To my understanding, section 3.3 should refer to Algorithm 1 and explain in details.
- Then, it's not well-motivated why model should output all the 500 noise predictions at once, and why the approximation of $x_\delta$ with only structural information is enough.

### Questions
- In table 1 and 2, why all settings (e.g., number of parameters and steps) are different? I can see the network architecture is modified in Section 3.3, but it is not clear why it is around 2x larger.
- The proposed method can reduce the number of steps from 1000 to 200. I think DDIM can also reduce to 200 with minimal loss of quality. However, the comparisons do not show how DDIM works with the same number of sampling steps, is there any reason for this?
- Why it is worth mentioning the continuous-time version in eq. 10, is it used later?
- In Figure 4, which part of the architecture is different from VAE and U-Net that are widely used in other diffusion models?
- In appendix B, the proof of convergence seems interesting. It discussed that we can carefully choose $\gamma$ to ensure effective pixel-wise diffusion, but is there ablation study to support that?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes adjusting the diffusion coefficient for each pixel to achieve faster diffusion sampling compared to DDIM. To do this, the authors suggest that different scheduling is required because the SNR varies by pixel (Section 3.1), explain how to implement this (Section 3.2), and propose a modified network structure to accommodate this approach (Section 3.3).

### Strengths
I couldn't find any strengths in the manuscript.

### Weaknesses
1. **Lack of Recent GDM Studies**: This paper lacks a comprehensive study of recent Generative Diffusion Models (GDMs). While it proposes a new sampler for GDMs, it does not even compare its performance with DPM-Solver, the default sampler for Stable Diffusion. DPM-Solver is only briefly mentioned in L408, but no experiments were conducted, due to *"space limitations"* (L410). This is problematic, as DPM-Solver is a training-free method that is much faster than DDIM and delivers comparable FIDs to DDIM. The proposed method is likely to be outperformed by DPM-Solver. Furthermore, most references throughout the paper are from before 2023, indicating a lack of engagement with the most recent advancements.

2. **Writing Issues**: The writing quality is poor. For example, in Fig. 1, the term "dual" is used, which typically refers to the dual form of a convex optimization problem, making it an inappropriate choice here. Additionally, there are missing captions in Tables 1 and 2, and the citation format is incorrect, as "citep" should have been used in many cases (e.g., L405). Significant figures in Tables 1 and 2 are inconsistent. In L400, the term "dissusion" is misspelled. Figures throughout the paper, especially Figures 2 and 4, have text that is too small to read. Equations (14) and (15) deviate significantly from the standard format in this field, making them difficult to understand. There are many other writing issues throughout the paper.

3. **Unclear Theory**: It is unclear why the SNR is defined as Equation (11). It does not align with the general definition of SNR. In most GDMs, SNR is defined independently of latents (i.e., $x_t$), but in this work, the authors propose making it dependent, which is a significant drawback. To address this, Section 3.3 introduces a new model, G, but as scalability increases, so do the resources required for training and inference (2 $\times$ Params in Tables 1, 2).

### Questions
1. In Figure 2, why are the starting points at t=0 different? I believe that they should start with the same value.

### Soundness
1

### Presentation
1

### Contribution
1

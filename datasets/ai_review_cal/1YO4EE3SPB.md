- Decision: Accept
- Avg Score: 5.50
- Scores: 6, 6, 5, 5
Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper proposes RED-diff, a variational approach for solving inverse problems using pretrained diffusion models. The method frames posterior inference as stochastic optimization of a variational bound, leading to a regularization-by-denoising (RED) objective where denoisers at different timesteps impose multi-scale structural constraints. A key claimed contribution is that the gradient of the regularization term can be computed without backpropagating through the score network (Proposition 2), enabling lightweight iterates. Experiments on ImageNet inpainting show strong quantitative results, while nonlinear tasks (HDR, phase retrieval, deblurring) report large improvements over DPS.

## Strengths

- **Clean variational framing with principled derivation**: Proposition 1 derives the inference objective from KL divergence minimization, linking the inverse problem to a score-matching loss. The derivation is grounded in standard variational inference and connects to established diffusion training objectives (Vahdat et al. 2021, Song et al. 2021). This provides a theoretically motivated alternative to the ad-hoc score approximations used in DPS and ΠGDM.

- **SNR-based weighting mechanism with empirical validation**: Section 4.3 proposes converting noise-domain regularization to an interpretable image-domain loss via inverse SNR weighting (λ_t = λ/SNR_t). The ablation in Figure 2 systematically compares different monotonic weighting functions and validates the design choice. This is practical and useful guidance for practitioners.

- **Strong quantitative performance on ImageNet inpainting**: Table 1 shows RED-diff achieving the best results across all five metrics (PSNR 23.29, SSIM 0.87, KID 0.86, LPIPS 0.1, top-1 72.0) compared to DPS, ΠGDM, and DDRM, while also being faster (0.05 sec/step vs. 0.10–0.24) and more memory-efficient (batch size 30 vs. 15–25). The improvements are consistent and the efficiency gains are clearly demonstrated.

- **Connection to regularization-by-denoising (RED)**: Section 4.2 explicitly draws the connection between the per-timestep variational loss and RED, showing the regularization takes the form λ_t(sg[ε_θ(x_t;t) − ε])^⊤ μ. This connection is novel for diffusion-based inverse solvers and enables the use of off-the-shelf optimizers (Adam), which is conceptually interesting.

- **Insightful ablation on timestep scheduling**: Section 5.3.2 demonstrates that descending timestep order (from t=T to t=1) significantly outperforms random, ascending, or mini-batch sampling. This provides a practical design principle and connects to how diffusion models build structure from coarse to fine.

## Weaknesses

### Major

- **Proposition 2's gradient simplification lacks a derivation sketch in the main text and the mathematical claim is non-trivial**: Proposition 2 claims that under ω(0)=0 and σ=0, ∇_μ reg(μ) = E_{t,ε}[λ_t(ε_θ(x_t;t) − ε)] where λ_t = (2Tσ_v^2 α_t/σ_t)·dω(t)/dt, and critically, the Jacobian of ε_θ w.r.t. its input does not appear. This is the linchpin of the method's efficiency claim. Normally, differentiating reg(μ) = E_{t,ε}[2ω(t)(σ_v/σ_t)^2||ε_θ(α_t μ + σ_t ε; t) − ε||^2] would produce a term involving ∇_{x_t}ε_θ. The claim that integration by parts (or some other technique) eliminates this term is mathematically non-trivial and deserves a careful sketch in the main text. Unlike Proposition 1, which explicitly references the supplementary for its proof, Proposition 2 provides no proof location at all. Without clarity on the derivation, a reader cannot assess whether the algorithm (which uses `sg` to deliberately stop gradients through ε_θ) minimizes the claimed variational objective or a surrogate. *Mitigation: If the proof exists in the supplementary (which was stripped by the parser), this concern is partially addressed but the main text should at least sketch the key steps.*

- **Experimental evaluation on nonlinear tasks raises credibility concerns**: Table 2 reports RED-diff achieving **45.00 dB PSNR** and **0.987 SSIM** on nonlinear deblurring — values that imply near-perfect reconstruction on a difficult task. On HDR (a simple clipping function), DPS achieves only **7.94 dB PSNR**, which is worse than outputting a constant mean image (~10–12 dB), while RED-diff achieves 25.23 dB — a 17 dB gap. These extremes are unusual: DPS with a known forward model and a pretrained diffusion prior should not produce near-random outputs on a clipping task unless severely misconfigured. The paper uses a non-standard adaptive step size for DPS (ζ_i = constant/||y − A(x̂_0)||), and while it reports grid search, no sensitivity analysis or visual examples for nonlinear tasks are provided to help the reader assess whether the comparisons are fair. The combination of implausibly good RED-diff results and implausibly poor DPS results on the same tasks undermines confidence in the comparative claims.

- **No code, checkpoints, or visual results are provided for nonlinear tasks**: The paper shows inpainting visual examples (Figure 1) but no visual comparisons for deblurring, HDR, or phase retrieval. Given the extreme quantitative gaps reported, visual examples are essential for credibility. Code and model checkpoints are not promised either, making independent verification impossible.

### Minor

- **The method reduces to deterministic MAP estimation despite being framed as variational inference**: The paper sets σ ≈ 0 (near-zero variational variance), which reduces the variational distribution to a point estimate. The paper acknowledges this ("lack of diversity," "mode-seeking in nature") but continues to use "sampling" language throughout. This is not a fatal flaw — the MAP-to-variational connection is legitimate — but it overstates the scope. The method is better characterized as a deterministic optimization approach for approximate MAP inference, not as posterior sampling.

- **The inpainting evaluation uses only 1k ImageNet images with no confidence intervals or variance reporting**: Results are reported as point estimates without standard deviations or per-sample distributions. For a 1k sample size, this is acceptable but weaker than best practices. Given the modest improvements over DPS on some inpainting metrics (e.g., LPIPS 0.10 vs. 0.12–0.26), variance bars would help assess significance.

- **The per-step time of 0.05 sec for a diffusion U-Net on ImageNet needs clarification**: 1,000 forward passes through a full-resolution diffusion U-Net (presumably 256×256) at 0.05 sec each seems fast unless significant optimizations (e.g., half-precision, smaller network) are used. The paper should specify the resolution and any acceleration techniques.

### Trivial

- Line 240: "bellows up" should be "blows up."
- Algorithm 1 lists the loss as λ_t (sg[ε_θ(x_t;t) − ε])^⊤ μ, but the gradient in Proposition 2 is E[λ_t(ε_θ(x_t;t) − ε)] — the loss per iteration in the algorithm is an instantaneous approximation of the gradient of a linear form, not the loss that was derived. A brief note clarifying this connection would help.

## Nice-to-Haves

- A direct comparison with RED using a single diffusion denoiser, or with P^3 (plug-and-play prior) methods, would better situate the contribution.
- A sensitivity analysis showing DPS performance across a range of step sizes on the nonlinear tasks, to demonstrate that the chosen settings are not anomalously bad.
- Reporting standard deviations or box plots for the main quantitative results.

## Removed Points

**These points are flagged to be removed; treat them with caution.**

1. **"The gradient derivation in Proposition 2 is unsupported and likely incorrect" (Harsh Critic point 1, "likely incorrect" framing)** — Removed because the paper may contain the proof in the supplementary material (stripped by the parser). The assertion that it is "likely incorrect" is speculative without seeing the supplementary. However, I retain the concern about the missing derivation sketch as a Major weakness (above), re-framed to focus on what is verifiable from the main text.

2. **"Missing related works (DDNM, GDP, original RED with diffusion denoiser)" (Harsh Critic, places to improve)** — Removed per instructions: I cannot confirm the existence or absence of these works and should not comment on missing related works.

3. **"Missing appendix, missing proofs in appendix"** — Removed per instructions: the parser strips appendix sections. The proof for Proposition 1 is explicitly cited to the supplementary. For Proposition 2, the lack of any proof reference is noted in the retained Major weakness above, but the criticism is not about the appendix being missing per se.

4. **"Missing hyperparameters, trivial implementation details, complete training logs"** — Removed per instructions: these are nitpicks about reproducibility that go beyond what is standard to include.

5. **"Pure formatting/style nitpicks"** — Removed. Only one actual typo retained in Trivial.

6. **Strength Finder strengths about "important problem" / "important research question"** — These are generic and removed. The retained strengths are concrete and specific to the paper's contributions.

7. **"The paper claims RED-diff mitigates posterior score approximation... Actually RED-diff replaces score approximation with a different approximation"** — This is a valid observation but the paper does not claim to eliminate approximation entirely; it claims to "mitigate" it, which is compatible with having a different kind of approximation. Removed as a strawman.

## Novel Insights

None beyond the paper's own contributions. The reviewer inputs surface a genuine tension: the paper's variational derivation is elegant and connects naturally to RED, but the central gradient simplification (Proposition 2) makes a strong mathematical claim that is not explained in the main text, and the nonlinear experiments report numbers that are simultaneously too good (RED-diff) and too bad (DPS) to be taken at face value. Neither reviewer identifies a path to resolve these issues beyond checking the supplementary for the proof and re-running the nonlinear comparisons with more careful tuning.

## Suggestions

1. **Provide a sketch of Proposition 2's derivation in the main text** — Even a 3–4 line outline of the integration-by-parts or other technique, plus the key assumption (e.g., that the score network is a conservative field, or that the weighting function allows the Jacobian term to be absorbed into a total derivative), would dramatically improve verifiability. Show explicitly why the boundary term at t=0 vanishes and where the dω/dt term comes from.

2. **Revisit the nonlinear task comparisons with significantly more careful DPS tuning** — Use the original DPS codebase with recommended hyperparameters first, and only then attempt grid search around those defaults. Include a sensitivity plot showing DPS performance across step sizes. Provide visual examples for at least one nonlinear task.

3. **Add standard deviations or confidence intervals** to the main quantitative tables.

4. **Clarify the image resolution** and any implementation details (e.g., mixed precision) that explain the 0.05 sec/step runtime.

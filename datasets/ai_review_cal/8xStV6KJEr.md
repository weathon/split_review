- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5
Now I have all details verified. Let me produce the final consolidated review.

## Summary
This paper introduces Constrained Diffusion Implicit Models (CDIM), which modify DDIM updates during inference to enforce linear constraints on the Tweedie estimate $\hat{\mathbf{x}}_0$, enabling fast and high-quality solutions to noisy linear inverse problems. The method achieves 10–50× speedups over prior conditional diffusion methods (e.g., DPS, FPS-SMC) on FFHQ benchmarks while maintaining competitive FID/LPIPS scores, and extends to non-Gaussian noise models via KL divergence minimization between the empirical residual distribution and the known noise distribution.

## Strengths
- **Accelerated inference**: Table 1 shows CDIM runs in 2.4–10.2 seconds on FFHQ tasks versus 70.4 seconds (DPS) and 116.9 seconds (FPS-SMC), while achieving competitive or better FID/LPIPS scores on super-resolution, inpainting, and deblurring. The speed-up is substantial and clearly demonstrated.
- **Handling of general noise models**: Section 4.2 extends beyond the standard Gaussian-noise assumption to handle arbitrary noise distributions via KL divergence minimization. This is validated on bimodal noise (Figure 4, discrete KL) and Poisson noise (teaser figure, Pearson residuals), which prior diffusion inverse solvers like DPS do not address.
- **Quality-efficiency Pareto frontier**: Table 1 and Figure 2 show that CDIM occupies a favorable region of the quality-speed trade-off space — faster than DPS/MCG/FPS-SMC while producing better FID than DDRM, PnP-ADMM, and Score-SDE.
- **Systematic ablation of the denoising–optimization trade-off**: Section 5.2 fixes total steps at 200 and varies $T'$ and $K$, providing concrete guidance that FID favors more denoising steps while LPIPS/PSNR benefit from a balanced mix (Figure 6). This is practically useful for deployment.
- **Demonstration on non-standard applications**: Section 5.3 applies CDIM to time-travel rephotography and sparse 3D point cloud reconstruction using a pretrained FFHQ model without task-specific fine-tuning, showcasing versatility.

## Weaknesses

### Fatal
None.

### Major
- **Missing ImageNet quantitative results**: Section 5.1 explicitly states evaluation on both FFHQ-1k and ImageNet-1k validation sets, and mentions using an ImageNet-pretrained diffusion model. However, Table 1 reports results only for FFHQ. No quantitative results for ImageNet appear anywhere in the main text. This directly undermines the claim of cross-dataset generalization and is a significant omission.

- **Exact recovery claim lacks experimental support**: The abstract and Section 4.1 claim that CDIM achieves "exact recovery of the observations" for noiseless inverse problems. The theoretical argument (as $t\to 0$, the constraint objective becomes a convex quadratic) is sound in the limit. However: (a) all experiments use $\sigma=0.05$ noise — no noiseless experiments are performed; (b) the practical algorithm uses a finite number $K$ of gradient steps and a Lagrangian relaxation (Eq. 6) rather than exact projection. No quantitative measure of constraint satisfaction (e.g., $\|\mathbf{A}\mathbf{x}_0-\mathbf{y}\|$) is reported. The claim is stronger than what is demonstrated.

- **Discrete KL gradient not specified**: Algorithm 1 and Eq. 8 describe optimizing a categorical KL divergence between discretized residuals, using the notation $\nabla_{\mathbf{x}_{t-\delta}} \text{KL}(\cdot)$. The discretization operation $\lfloor\cdot\rfloor_B$ (hard bin assignment) has zero gradient almost everywhere. The paper does not explain how this gradient is computed (e.g., via soft quantization, straight-through estimator, or a reparameterization). This affects reproducibility of the non-Gaussian noise results (Figure 4).

### Minor
- **No variance reporting**: Table 1 reports point estimates without standard deviations or confidence intervals. Given the stochasticity of the diffusion process and gradient-based inner loops, some measure of stability across seeds or runs would strengthen the evidence.
- **Step-size heuristic validated only in-distribution**: Section 4.4 proposes $\eta \propto 1/\mathbb{E}[\|\nabla\|]$ estimated from FFHQ training data and claims it "generalizes as a good learning rate for unseen data" and "across datasets." The only validation is a qualitative comparison on FFHQ (Figure 5). No cross-dataset sensitivity analysis is provided.
- **Poisson noise threshold inconsistency**: Section 4.2 states the Gaussian approximation for Pearson residuals is valid for $s \approx 0.025$, but the teaser figure shows Poisson denoising at $s = 0.05$. The practical limits of this approximation are not investigated.
- **Early stopping requires known $\mathrm{Var}(r)$**: Algorithm 2's noise-agnostic variant stops when $\hat{\sigma}^2 < \mathrm{Var}(r)$. The paper does not discuss how $\mathrm{Var}(r)$ is estimated when the noise distribution is unknown, which is the scenario this variant targets.
- **Additional applications are qualitative-only**: Section 5.3 presents time-travel rephotography and point cloud reconstruction as demonstrations without metrics or baselines, limiting their evidentiary value.

### Trivial
- **Figure 2 (runtime-quality Pareto plot) is placed in the Related Work section rather than the Experiments section and its caption could more clearly specify which tasks are averaged.**

## Nice-to-Haves
- **Comparison at equal compute**: Showing whether CDIM with more steps (e.g., $T'=100, K=3$) can match or exceed DPS quality would substantiate that the trade-off is Pareto-efficient, not merely a quality-for-speed sacrifice.
- **Noiseless evaluation**: A separate noiseless experiment (e.g., $\sigma=0$) with a constraint-satisfaction metric (pixel-wise MSE between $\mathbf{A}\mathbf{x}_0$ and $\mathbf{y}$) would directly test the exact-recovery claim.
- **Discussion of the practical gap between the theoretical exact-recovery guarantee and the finite-$K$ Lagrangian used in practice** would improve precision.

## Removed Points
These points are flagged to be removed; treat them with caution.
- **"DPS is limited to Gaussian measurement noise"** — The critic claims the paper says this, but the relevant text (line 14) is a LaTeX comment (%...), not rendered in the paper. Even if it were, DPS assumes Gaussian noise in its likelihood, so the statement would be accurate. Removed as factually incorrect about the paper.
- **Missing related works (Reducing PDE, DiffusionMBIR)** — Removed per policy: external verification of missing citations is not possible.
- **"T' vs K trade-off is not unique to CDIM"** — The paper does not claim this trade-off is unique; it reports an experimental observation about its own method. Strawman criticism removed.
- **Reproducibility nitpicks about specific undisclosed hyperparameters (number of bins $B$, exact $\eta$ values)** — The paper promises code at a URL. Removed per policy.
- **Figure 2 not referenced in experimental section** — The figure is in Related Work but is referenced by the caption and sets up the contribution context. Minor presentation issue; moved to Trivial.
- **Abstract framing of DPS as "failing to exactly recover observations"** — This is a factual statement: DPS does not enforce hard constraints so it cannot guarantee exact recovery. Not misleading.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Add ImageNet results** to Table 1 (or a supplementary table summarized in the main text) to substantiate the generalization claim. This is the most impactful fix.
2. **Clarify the noiseless exact-recovery claim**: either add noiseless experiments with a constraint-satisfaction metric, or explicitly qualify the claim to reflect the finite-step Lagrangian used in practice.
3. **Specify how the discrete KL gradient is computed** (e.g., via a soft quantization function or a straight-through estimator). Without this, Algorithm 1 is not reproducible for non-Gaussian noise.
4. **Add error bars** (at least for the top CDIM variants) in Table 1, or explain why single runs are sufficient.
5. **Discuss the Poisson noise $s$ threshold**: state what happens at $s=0.05$ vs. $s=0.025$ and whether the Gaussian approximation degrades gracefully.
6. **Discuss how $\mathrm{Var}(r)$ is estimated** for the noise-agnostic early-stopping variant when the noise distribution is truly unknown.

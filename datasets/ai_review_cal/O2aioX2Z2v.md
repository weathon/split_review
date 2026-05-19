- Decision: Reject
- Avg Score: 4.20
- Scores: 3, 5, 6, 1, 6
Now I have enough information to produce the final consolidated review.

## Summary

This paper proposes ShaRP (Stochastic deep Restoration Priors), a framework that uses an ensemble of pre-trained restoration models (trained on a family of degradation operators) as stochastic priors for imaging inverse problems. ShaRP generalizes denoiser-based priors (RED, SNORE) and single-operator restoration priors (DRP) by stochastically sampling from a set of degradation operators at each iteration. The paper provides theoretical analysis showing the regularizer interpretation (as the expected negative log-likelihood of degraded observations) and convergence guarantees under inexact MMSE restoration. Empirically, ShaRP is evaluated on CS-MRI (supervised and self-supervised settings) and single-image super-resolution, achieving strong PSNR/SSIM results.

## Strengths

1. **Novel regularizer interpretation (Theorem 1).** The paper derives a clean theoretical connection showing that ShaRP minimizes an objective whose regularizer is the expected negative log-likelihood of degraded observations (Eq. 8), with the gradient matching the ShaRP update (Eq. 10). This formalizes the intuitive idea that solutions whose degraded versions resemble realistic degraded images are favored, and goes beyond prior denoiser-based regularizers.

2. **Convergence guarantee for inexact MMSE operators (Theorem 2).** The paper proves that under mild assumptions (Lipschitz gradient, bounded variance, bounded bias), ShaRP's gradient norm converges to a neighborhood bounded by ε² (the MMSE approximation error) plus a step-size-dependent term. This is a rigorous result that accounts for the practical reality that learned restoration models are approximate.

3. **Self-supervised MRI results are genuinely convincing.** Table 2 shows ShaRP with a self-supervised restoration prior (trained from only 8× subsampled data) outperforms SPICER — a state-of-the-art self-supervised method — by approximately 2 dB across all settings (e.g., 4×, σ=0.005: PSNR 33.87 vs. 31.87). This validates the paper's key advantage over denoiser-based methods that cannot be trained without fully sampled ground truth, and the comparison is fair since SPICER is also self-supervised.

4. **Consistent empirical state of the art across two inverse problems.** In supervised MRI (Table 1), ShaRP achieves the best PSNR and SSIM across all 12 noise/acceleration settings. In SISR (Table 3), ShaRP leads on PSNR/SSIM over DPIR, DDNM, DPS, DiffPIR, and DRP for both blur kernels. The method demonstrably works on two distinct problem classes.

## Weaknesses

### Fatal
None.

### Major

1. **Baseline fairness for supervised MRI (Table 1) is not established.** The paper does not specify the training data or source domain for the pre-trained models used by the diffusion baselines (DPS, DDS) or the Gaussian denoisers used by PnP-FISTA/PnP-ADMM. The only explicit training set mentioned is fastMRI for ShaRP's own restoration model. If the baselines use models trained on natural images (e.g., ImageNet) applied to 320×320 brain MRI slices, the comparison is structurally invalid — the domain shift would penalize the baseline regardless of algorithmic merit. Conversely, if the baselines also use in-domain models, this must be stated. The reported margins (e.g., ShaRP 37.59 vs. DDS 35.21 at 4×, σ=0.005) are large enough that the reader cannot assess whether they reflect a genuine advantage or an artifact of mismatched pre-training distributions. This concern is specific to Table 1; the self-supervised MRI (Table 2) and SISR (Table 3, where all methods plausibly use ImageNet-trained models) are less affected.

2. **Missing ablation isolating the effect of stochastic operator sampling.** The paper's central claim is that stochastically sampling from an ensemble of restoration operators outperforms using a single operator (DRP). However, the comparison to DRP in Tables 1 and 3 does not control for architecture or training. The paper states DRP uses "only a single restoration operator" — but was this exactly the same restoration model used in ShaRP, queried with a single fixed H? Or was a different model trained? Without this control, the improvement cannot be attributed to stochastic sampling rather than to other confounders (different training data, different architecture, different operator selection). An ablation fixing the architecture and training set while varying only the number of operators and sampling strategy is needed.

3. **Missing dataset and protocol details for SISR.** The SISR results (Table 3) are captioned "on ImageNet dataset," but the main text never specifies which subset of ImageNet (e.g., validation set, ILSVRC2012), at what resolution (e.g., 256×256 center-crop), how many test images, or the exact downsampling procedure (e.g., MATLAB-style imresize). While the blur kernel is specified (31×31 Gaussian with std 3), the evaluation protocol is incomplete, making results difficult to reproduce or compare to published numbers.

### Minor

1. **Theory does not explain the claimed practical advantages.** Theorem 2 is a standard biased SGD convergence bound that applies to denoiser priors as a special case (H=I). It does not capture or explain why restoration priors outperform denoiser priors at handling structured artifacts. The theory correctly characterizes convergence of ShaRP as an optimization method, but the paper's practical claims (structured artifact handling, better performance) are not supported by the theory.

2. **No limitations or computation time discussion.** The paper has no limitations section. Several practical considerations are unaddressed: (a) computational cost relative to baselines (ShaRP requires a restoration network forward pass per iteration times the number of iterations); (b) sensitivity to the choice of operator distribution p_H; (c) the requirement that the restoration model be trained on a family of degradations that may not always be available; (d) whether the method generalizes to inverse problems where A is unrelated to the family of H operators.

3. **LPIPS gap on SISR is not discussed in depth.** ShaRP ranks second on LPIPS behind DiffPIR (e.g., 0.179 vs. 0.152 for the σ=1.25 kernel, noiseless). The paper acknowledges this as a trade-off but does not analyze why — is this a limitation of the restoration prior formulation, or could it be addressed by tuning?

### Trivial
None.

## Nice-to-Haves

- A runtime comparison between ShaRP and baselines on a representative test case.
- An ablation exploring sensitivity to the number of operators b (the paper uses 8; would 4 or 16 change results?).
- A discussion of what types of inverse problems the method is best suited for (e.g., when measurement operator A is related to the training operator family H).

## Removed Points

- **"Self-supervised comparison is conceptually incoherent" (Critic Weakness 2).** The paper explicitly states in the Table 2 caption: "For reference, the highlighted row presents a PnP method using a Gaussian denoiser, which requires fully sampled data for training." The text also notes "training Gaussian denoisers is not feasible." The PnP-ADMM row is included transparently as a reference point, not as a claimed fair comparison. The paper does not misrepresent this comparison.

- **"Theory is standard / does not connect to practical gains" framed as a major weakness.** The observation is valid but the theory's purpose is to characterize the regularizer and convergence behavior — this is standard for method papers and does not undermine any claim. Demoted to minor.

- **"SISR PSNR values are lower than typical published numbers."** The critic compares to unspecified "typical published numbers" without a source. The DPIR values reported (28-30 dB for 2× SR with Gaussian blur on ImageNet) are consistent with the specific kernel parameters used (31×31, std 3, with σ=1.25 and 1.5 blur kernels before downsampling). This is too speculative to retain as a weakness.

- **Strength Finder's "Strong empirical evidence" for supervised MRI.** This strength is qualified by the baseline fairness concern above. The evidence is suggestive but not fully validated until the baseline training domain is clarified. Retained as a strength but context noted.

## Novel Insights

The reviews surface one genuinely interesting observation beyond the paper's own contributions: the contrast between ShaRP's PSNR/SSIM dominance and its second-place LPIPS performance (behind DiffPIR) suggests that restoration priors and diffusion-model priors may occupy complementary positions on the distortion-perception frontier. Restoration priors appear to excel at pixel-level fidelity (likely because the MMSE training objective directly minimizes MSE), while diffusion models maintain a perceptual quality advantage. This trade-off is worth deeper investigation and could motivate hybrid approaches that combine both types of priors.

## Suggestions

1. **Clarify baseline training data for supervised MRI (Table 1).** State explicitly which pre-trained models/checkpoints were used for DPS, DDS, PnP-FISTA, and PnP-ADMM — including training dataset, architecture, and whether they are in-domain (medical) or out-of-domain. If in-domain models are available, use them; if not, acknowledge this as a limitation and caveat the comparisons accordingly.

2. **Add a controlled ablation of operator stochasticity.** Fix the restoration architecture and training set. Compare: (a) ShaRP with the full set of 8 operators, (b) a deterministic version averaging gradients over the 8 operators, (c) a version with b=1 (single fixed operator, i.e., DRP-style), (d) a version with H=I (denoiser case). This would isolate the benefit of stochastic multi-operator sampling.

3. **Provide complete SISR evaluation details:** dataset subset (e.g., "2,000 images from ILSVRC2012 validation set"), resolution (e.g., "center-cropped to 256×256"), and downsampling procedure.

4. **Add a limitations section** addressing computational cost, scope of applicability, and sensitivity to operator distribution.

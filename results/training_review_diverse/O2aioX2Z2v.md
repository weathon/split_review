I have all the content from my earlier complete reading. Let me now produce the final consolidated review.

---

## Summary

ShaRP (Stochastic deep Restoration Priors) proposes using an ensemble of pre-trained deep restoration models — rather than the standard Gaussian denoisers — as priors for solving imaging inverse problems. The method generalizes Regularization by Denoising (RED) and Deep Restoration Priors (DRP) by stochastically sampling from a set of restoration operators during optimization, leading to a regularizer interpreted as the expected negative log-likelihood of degraded observations. The paper provides convergence theory (exact and inexact MMSE restoration operators) and demonstrates state-of-the-art performance on CS-MRI reconstruction and single-image super-resolution, including a self-supervised variant trainable without fully sampled data.

## Strengths

1. **ShaRP achieves state-of-the-art performance across multiple inverse problems.** Tables 1 and 3 show that ShaRP consistently outperforms denoiser-based methods (PnP-FISTA, PnP-ADMM, DPIR), diffusion-based methods (DPS, DDS, DDNM, DiffPIR), and the single-restoration-prior DRP across various acceleration factors, noise levels, and blur kernels. Improvements are substantial — e.g., 37.59 vs 35.52 PSNR over DRP on 4× uniform MRI (σ=0.005) and 30.09 vs 29.28 on noiseless SISR with kernel σ=1.25.

2. **Theoretical derivation grounding the ensemble restoration prior in a principled regularizer.** Theorem 1 establishes that ShaRP's update corresponds to the gradient of a regularizer defined as the expected negative log-likelihood of degraded observations, via Tweedie's formula applied to MMSE restoration operators. Theorem 2 provides a convergence bound under inexact (biased) restoration operators, controlling the gradient norm via step size, stochastic variance, and restoration bias. This gives ShaRP a cleaner theoretical footing than purely empirical PnP approaches.

3. **Self-supervised training of restoration priors is demonstrated to work where Gaussian denoiser training is infeasible.** Table 2 shows that ShaRP with self-supervised restoration priors (trained on 8× subsampled data only) outperforms TV, GRAPPA, and SPICER on 4× and 6× random-mask MRI reconstruction. The highlighted PnP-ADMM row confirms that denoiser-based methods underperform when restricted to the same data, validating the paper's claim that restoration priors enable regularization in settings where denoiser priors cannot be effectively trained.

4. **Intuitive regularization interpretation.** The paper's regularizer (Eq. 11) has a clear semantic meaning: it favors solutions whose stochastically degraded versions have high likelihood under the marginal distribution of real degraded images. This is a conceptually clean generalization beyond RED and SNORE, which use denoising likelihoods.

5. **Stable convergence validated empirically.** Figures 1(a)–(d) show that both supervised and self-supervised ShaRP converge smoothly in terms of iterate distance and PSNR, with narrow standard deviations across runs.

## Weaknesses

### Fatal
None.

### Major

1. **DRP baseline comparison lacks sufficient detail to isolate the ensemble benefit.** The paper's central claim is that using multiple restoration operators (b > 1) outperforms a single one (b = 1, i.e., DRP). However, the paper does not disclose which single operator was used for DRP — whether it was the "best" individual operator from the ensemble (e.g., the α closest to the target degradation), a randomly chosen one, or a fixed operator. Since the improvement is attributed to the ensemble (b > 1), the reader needs to know that DRP was not disadvantaged by a poor operator choice. The paper states that "when b = 1, then ShaRP can be viewed as the instance of DRP" (line 84), which provides a conceptual mapping, but the experimental implementation of DRP should be explicitly stated. An ablation with ShaRP at b = 1 (i.e., DRP) using the same architecture and operator set would cleanly isolate whether the gains come from the ensemble or from other factors.

2. **Cross-task generalization (deblurring prior for super-resolution) lacks justification.** The SISR experiments use a deblurring prior (trained on H_α = (1-α)I + αK) to solve a super-resolution task whose operator involves both blur and downsampling (A = SK). While the empirical results are positive, the paper does not discuss why a deblurring prior — which never sees downsampling during training — should be an effective regularizer for super-resolution. The paper's regularizer (Eq. 11) operates on degraded observations s = Hx + n; for super-resolution, this requires H = I (for no degradation) or H = K (for blur), neither of which involves downsampling. The paper should discuss the conditions under which a prior trained on one degradation family can transfer to a different one, or at minimum acknowledge this as a limitation requiring further investigation.

### Minor

1. **PnP baseline denoiser architectures and training data are not specified.** The paper compares against PnP-FISTA and PnP-ADMM but does not state which denoiser architecture (e.g., DnCNN, DRUNet) was used, how it was trained, or whether it was taken from existing implementations. This matters because a low-quality denoiser would make PnP baselines weaker, potentially inflating ShaRP's relative performance.

2. **Hyperparameter sensitivity and selection are not reported.** The algorithm has parameters γ (step size), σ (noise level for the stochastic gradient), and τ (regularization weight). The paper does not describe how these were chosen for each experiment or how sensitive the results are to their values. This is important for reproducibility, especially since the optimal values likely vary across tasks, noise levels, and acceleration factors.

3. **Ablation on the number of operators b is missing.** The paper uses b = 8 for MRI and a continuous range of α for SISR, but does not show how performance varies with b. Does performance increase monotonically with b? Is there a saturation point? This would provide practical guidance and directly support the paper's claim that the ensemble is beneficial.

4. **Self-supervised training justification could be clearer.** The paper states that "training Gaussian denoisers is not feasible" given only undersampled measurements (line 254) but does not provide a concrete argument for why. The implicit reasoning is correct (denoisers require clean images or paired noisy observations of the same scene; undersampled MRI provides neither), but making this explicit would strengthen the paper's persuasive power, especially since self-supervised denoising methods like Noise2Noise exist in other domains.

5. **Convergence evidence is indirect.** Figure 1 shows iterate distance and PSNR but not the objective function value f(x^k) or gradient norm. While iterate convergence is meaningful evidence, the paper's claim of "stable convergence" to a stationary point of the ShaRP objective would be better supported by showing the objective value.

### Trivial
None.

## Nice-to-Haves

- An ablation comparing ShaRP with (a) only the identity operator (Gaussian denoiser), (b) only a single task-relevant operator (DRP with best α), and (c) the full ensemble, all using the same architecture and training data, would directly isolate the contribution of the ensemble.
- Runtime comparison against PnP and diffusion-based methods would help practitioners assess the practical trade-offs, as ShaRP requires one forward pass through the restoration model per iteration.
- An empirical estimate of the bias ε (from Theorem 2) — e.g., by comparing the trained restoration operator against a supervised MMSE approximation — would calibrate how tight the theoretical bound is in practice.

## Removed Points

- **Criticism that Noise2Noise could replace the self-supervised approach (from Harsh Critic).** The paper's context is undersampled MRI, where one does not have multiple noisy observations of the same anatomy. The paper correctly cites MRI-specific self-supervised methods (Yaman et al., gan2023self). The Noise2Noise suggestion is infeasible in this setting and reflects a misunderstanding of the data availability. The underlying point that the paper should clarify *why* denoiser training is infeasible is kept as a Minor weakness (item 4 above).

- **Criticism that "the theoretical analysis is standard."** This is an accurate observation but not a weakness — the paper does not claim novel optimization theory; it claims a novel regularizer and its connection to the algorithm via Theorem 1, which is the appropriate contribution for a methods paper.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the need for tighter experimental controls (especially the b=1 ablation) to fully substantiate the ensemble claim, but do not identify new implications beyond what the paper already articulates.

## Suggestions

1. In a revision, specify exactly which single operator was used for the DRP baseline (e.g., the α closest to the target task, or a specific mask from the training set). Better yet, add a b=1 ablation using the same architecture to explicitly show the ensemble benefit.
2. Add a discussion of why a deblurring prior transfers to super-resolution, or explicitly acknowledge this as an empirical finding whose theoretical understanding is open.
3. Report the denoiser architecture(s) used for PnP baselines and the source of the pre-trained weights.
4. Add a table or plot showing how performance varies with the number of operators b, with a recommendation for practitioners.
5. Report the hyperparameter values (γ, τ, σ) used for each experiment and, if space permits, a brief sensitivity analysis.

## Score and Decision

This paper makes a solid contribution: the idea of using an ensemble of restoration operators as a prior is well-motivated, supported by both theory and strong empirical results, and the self-supervised variant opens a practically important training regime. The weaknesses identified are addressable and do not undermine the core claims. I recommend acceptance.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
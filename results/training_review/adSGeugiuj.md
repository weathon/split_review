Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper derives a recursive relation linking higher-order posterior central moments to higher-order derivatives of the posterior mean in Gaussian denoising (Theorems 1-2), and extends this to directional moments (Theorem 3). The authors then apply these theoretical results for training-free uncertainty quantification: they compute posterior principal components via finite-difference subspace iteration (Algorithm 1) and estimate marginal posterior distributions along those directions using numerical differentiation and maximum-entropy fitting. Experiments on face, MNIST, natural image, and microscopy data demonstrate the approach across diverse denoisers (DDPM-based, SwinIR, CNN, Noise2Void).

## Strengths

- **Clean theoretical recursion for central moments (Theorems 1-2).** The paper proves that central moments satisfy the simple recursion $\mu_{k+1} = \sigma^2 \mu_k' + k \mu_{k-1} \mu_2$ (univariate) and its multivariate analog. This is genuinely simpler and more interpretable than converting from the non-central moment recursion of prior work (Meng et al., 2021). The additive term involves only $\mu_{k-1}$ and $\mu_2$, making the recursion tractable.

- **Directional posterior moments (Theorem 3).** The paper extends the recursion to one-dimensional projections $\vv^\top \rvx$, proving that the central moments of any projected direction satisfy the same univariate recursion via directional derivatives. This is a key enabler for marginal posterior analysis without storing high-order tensors, and goes cleanly beyond the framework of prior work.

- **Training-free, memory-efficient PCA of the posterior covariance (Section 4.1).** Algorithm 1 uses finite-difference Jacobian-vector products within subspace iteration, avoiding backward passes and explicit covariance storage. The paper reports a 6× memory reduction for a SwinIR patch. This is a practical advantage that could make posterior uncertainty accessible for high-resolution images where full covariance is intractable.

- **Demonstration across diverse domains and denoiser architectures (Section 5, Figures 3-5).** The method is tested on face images (DDPM denoiser), MNIST (CNN), natural images (SwinIR), and microscopy (Noise2Void). The posterior PCs capture semantically meaningful uncertainty directions (digit ambiguity 4 vs 9, moustache color, cell morphology), supporting general applicability.

- **Empirical robustness to unknown noise level (Section 4.2, Section 5).** The paper explicitly acknowledges that the theory assumes known $\sigma$ and shows that using an estimated $\sigma$ still yields plausible uncertainty estimates on real microscopy data with a blind denoiser. This practical flexibility is valuable.

## Weaknesses

### Fatal
None.

### Major

- **No systematic comparison to alternative uncertainty quantification methods.** The related work section cites Meng et al. (2021) for posterior covariance, Sankaranarayanan et al. (2022) and Kutiel et al. (2023) for semantic uncertainty, and Nechme et al. (2023) for learned posterior PCs — yet none are used as baselines. The paper claims its method is "fast, memory-efficient" and "advantageous over previous uncertainty quantification methods," but provides no runtime measurements and only a single memory comparison (6× versus autodiff, not versus any full UQ pipeline). Without baseline comparisons, the practical significance of these claims is unsubstantiated. A comparison on a small-scale benchmark (e.g., eigenvalue accuracy, marginal distribution quality, or runtime vs. a posterior sampling baseline) would substantially strengthen the contribution.

- **Quantitative validation in the main paper is extremely limited.** The main paper's evidence comprises visual inspection of PCs and marginal distributions, plus a GMM toy example with ground truth. The paper repeatedly references quantitative validation in the appendix (e.g., "In App.~we report quantitative comparisons to the naive baseline of estimating the PCs using a posterior sampler"), but the main text offers no concrete numbers — not even a single table reporting eigenvalue accuracy, coverage, or correlation with reconstruction error. For the FMD dataset, where the average of 50 bursts provides a clean reference, no quantitative comparison is shown. While quantitative results may exist in the appendix (which the parser strips), the reader of the main paper cannot judge whether the uncertainty estimates are actually accurate or merely plausible-looking.

### Minor

- **No sensitivity analysis for the finite-difference step size or network non-smoothness.** Algorithm 1 and the marginal distribution estimation rely on finite-difference approximations of derivatives. The paper mentions using double precision and notes numerical instability as a limitation (lines 250-253), but does not analyze how results vary with step size $c$ or how different activation functions (ReLU, SiLU) affect the approximation quality. For neural denoisers with non-smooth activations, this is a relevant concern. An empirical sensitivity study (even in the appendix) would increase confidence in the method's reliability.

- **The maximum-entropy fit from four moments is plausible but not validated for multi-modal marginals.** The paper fits a maximum-entropy distribution from the first four moments along each direction. For the MNIST example (Figure 4), the estimated marginal appears bimodal, which is encouraging. However, without comparing the estimated density to a histogram from posterior samples (or ground truth) on real data, it is unclear whether four moments are sufficient to capture the shape of potentially complex marginals. The GMM toy example validates this for a simple 2D case, but real posterior marginals could be more complex.

- **No runtime measurements reported.** The paper claims the method is "fast" but provides no timing results. For practitioners deciding whether to use this approach, knowing the wall-clock time per image for different denoisers and image sizes would be helpful.

### Trivial

- **The main paper relies on the appendix for the Algorithm pseudocode** (line 177: `\input{7_Algorithm}`), making the main text's Section 4.1 harder to follow without it. Including at least a sketch of Algorithm 1 in the main paper would improve readability.

- **The intuition behind the summation term in Theorem 2 for $k \ge 3$** could be explained more clearly in the main text (e.g., its connection to cumulant expansions or Gaussian integration by parts).

## Nice-to-Haves

- A downstream task demonstration where the uncertainty visualization leads to a measurable improvement (e.g., anomaly detection, active acquisition in microscopy) would strengthen the claim of practical value.
- Comparing the estimated marginal distributions to Monte Carlo posterior samples (e.g., via Langevin dynamics conditioned on the noisy observation) for at least one real-data case would directly validate the marginal estimation.

## Removed Points

**These points are flagged to be removed, treat them with caution:**

- Harsh Critic's claim that "no quantitative metrics are reported for real data" — the paper explicitly states in lines 194 and 216 that quantitative validation is provided in the appendix. The parser strips appendix content, so this criticism reflects a parser artifact, not a genuine omission by the authors.
- Harsh Critic's claim that the 6× memory reduction is "presented without any measured numbers, setup details" — the paper attributes detailed measurements to App.~\ref{app:BackPropApprox} (which is stripped by parser). The claim in the main text (line 192) is stated as a factual result from that analysis.
- Harsh Critic's claim that the choice of step size $c$ "is not discussed" — the paper defers this analysis to App.~\ref{app:BackPropApprox} (stripped by parser). The main text acknowledges the need for "sufficiently small" $c$ (line 191).
- Strength Finder's generic descriptions — these have been filtered into the strengths above.
- Several section-by-section nitpicks (missing intuitive interpretation for a summation term, presentation of Theorem 3 derivation) are minor presentation suggestions rather than substantive weaknesses.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm that the theoretical recursion is solid and the application is well-motivated, but they surface a consistent concern: the experimental validation does not match the ambition of the claims. No reviewer insight goes beyond what the paper itself states.

## Suggestions

1. **Add a quantitative results table to the main paper.** Even a small table reporting eigenvalue relative error, per-pixel variance vs. empirical MSE (over multiple noise draws), or a comparison of the estimated marginal to a posterior sampling baseline on one dataset would transform the paper's evidential strength. The current reliance on "see appendix" is insufficient for a methods paper.

2. **Include at least one baseline comparison.** Compare the top-5 eigenvectors or the marginal distributions against a simple alternative (e.g., Monte Carlo posterior sampling via Langevin dynamics, or the method of Meng et al. on small images). Report runtime and memory alongside accuracy.

3. **Add a sensitivity study for the finite-difference step size** for at least one denoiser (e.g., SwinIR on CBSD68). Show how top eigenvalues and eigenvectors vary with $c$, and whether single vs. double precision changes results noticeably.

4. **Report wall-clock time per image** for the denoisers used, so readers can assess the "fast" claim quantitatively.

## Score and Decision

The paper presents a genuinely novel theoretical contribution (the central moment recursion) and a practical, elegant algorithm for extracting uncertainty from pre-trained denoisers. The theoretical development is clean and clearly communicated. However, the experimental evaluation is substantially weaker than what a methods paper requires: it is almost entirely qualitative in the main text, lacks baseline comparisons, and makes practical claims ("fast, memory-efficient") without supporting runtime data. This gap between the strength of the theoretical contribution and the thinness of the empirical validation prevents the paper from being a fully convincing methods paper in its current form. A major revision with quantitative experiments, baseline comparisons, and runtime measurements would substantially strengthen it.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
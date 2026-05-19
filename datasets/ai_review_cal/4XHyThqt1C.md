- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 3, 5
Now I have thoroughly read the paper and verified the reviewer claims. Let me compose the final consolidated review.

---

## Summary

This paper addresses two problems in neural compression with vector quantization: (1) train-test mismatch between differentiable approximations and actual quantization, and (2) suboptimal encoder gradients for rate-distortion optimization. It proposes **Alternating Optimized Stochastic Vector Quantization**, which combines an encoder-decoder alternating optimization strategy (decoder updated with actual quantization, encoder with an approximation) and a sphere-noise based stochastic approximation for computing encoder gradients. Experiments are conducted on toy sources (1D Gaussian, 2D Boomerang, 8D Laplace) and the Kodak image dataset.

## Strengths

- **Encoder-decoder alternating optimization is convincingly motivated and empirically validated.** The paper correctly identifies that the train-test mismatch stems from using the same approximation for both encoder and decoder. Separating them—decoder optimized with actual quantization (matching test behavior), encoder optimized with a differentiable approximation—is a clean design choice. The ablation study (Table 2) shows that removing alternation leads to training collapse, directly confirming its necessity.

- **Sphere-noise stochastic VQ is a novel and well-motivated technique for improving encoder gradients in general VQ.** The core intuition—that at quantization boundaries the encoder gradient should reflect the RD loss difference between adjacent centers—is sound, and the sphere-noise sampling procedure provides a concrete way to achieve this. Even if the theoretical derivation has issues (see Weaknesses), the procedure itself (sample uniformly from a sphere centered at the input, radius = distance to nearest codeword, backpropagate through the sample) is well-defined and distinct from prior approximations.

- **Systematic evaluation across diverse source types.** The method is tested on 1D Gaussian, 2D Boomerang, 8D Laplace, and natural images (Kodak). The toy-source experiments allow controlled analysis of gradient behavior (Figure 6) and visualization of quantization results (Figure 7), demonstrating the method's behavior under progressively higher dimensions.

- **Controlled ablation study (Table 2).** The ablation compares sphere-noise against soft-to-hard VQ and probabilistic VQ while holding the alternating optimization strategy and transform structure constant. This isolates the effect of the VQ approximation itself and shows sphere-noise outperforms both alternatives.

## Weaknesses

### Fatal
None.

### Major

- **The Stokes theorem derivation of the sphere-noise gradient (Section 4.2) is mathematically incorrect as presented.** The paper claims:  
  `(1/V(ω)) ∫_ω ∂l/∂ỹ₁ dV = (1/V(ω)) ∫ l(ỹ) dỹ₂...dỹₖ`  
  via the generalized Stokes theorem. The correct application of Stokes/divergence theorem yields a surface integral involving the outward normal: `∫_{∂ω} l · n₁ dS`. The paper's expression drops the normal component and replaces the surface measure with a Lebesgue measure over the remaining coordinates, which is not mathematically well-defined for a general hypersphere.  
  **Impact:** This does *not* invalidate the empirical method—sampling from a uniform sphere and backpropagating is a well-defined stochastic procedure that may work well regardless. However, the paper presents this derivation as the *theoretical justification* for why sphere-noise produces better gradients. A central claimed contribution is thus unsupported. The paper should either provide a correct derivation or drop the claim and present sphere-noise as a heuristic with empirical justification.

- **The main image compression comparison (Table 1, Figure 8) is confounded by different entropy models.** The paper states (Section 5.1): UQ-AUN and UQ-STE use a *continuous factorized entropy model* (Ballé et al. 2018b), while the proposed method and VQ-STE baselines use a *discrete entropy model* with learnable logits. Because the entropy model differs, the reported BD-rate improvements (−6.46% to −9.74% over UQ-AUN) cannot be attributed solely to the quantization method. The ablation study (Table 2) partially addresses this by comparing VQ approximations under the same framework, but a baseline using scalar uniform quantization *with a discrete entropy model* (trained with STE or additive noise) is missing. Without it, the headline claim of outperforming standard scalar quantization is not cleanly supported.

### Minor

- **The alternating optimization schedule is underspecified.** The paper says "these two steps alternate during training" but does not state whether alternation is per mini-batch, per epoch, or on some other schedule, nor whether any regularization is used during the encoder step. While this does not undermine the method's validity, it hinders reproducibility.

- **No error bars, confidence intervals, or statistical significance tests are reported** for RD curves or BD-rate numbers. This is particularly important for a stochastic method where gradient estimates are inherently noisy. Single-run evaluations are common in this field, but reporting at least some measure of variability would strengthen the evidence.

- **Training collapse in the ablation without alternating optimization (Table 2, A1) is not explained.** The paper notes collapse occurred but does not analyze the cause (gradient explosion? mode collapse?). Understanding this failure mode would clarify why alternation is necessary.

- **Monte Carlo sample count for sphere-noise is not specified.** The paper does not state how many samples are drawn per forward pass during encoder optimization, making it hard to assess computational cost or variance of gradient estimates.

- **VQ-STE-1d results are reported for toy sources but omitted for Kodak images** (Table 1 only shows Ours-1d, Ours-2d, Ours-4d vs. UQ-AUN). Including VQ-STE-1d in the image results would provide a cleaner comparison baseline under the same entropy model.

### Trivial
None.

## Nice-to-Haves

- A controlled baseline using scalar uniform quantization with a *discrete* entropy model (trained with STE or additive uniform noise) would isolate the effect of the proposed sphere-noise VQ from the entropy model change.
- A discussion of how sphere-noise scales to higher VQ dimensions beyond 4—variance of gradient estimates, number of samples needed, and practical considerations.
- Pseudocode or an algorithm summary for the alternating optimization schedule would improve reproducibility.

## Removed Points

- **Missing comparisons to VQ-VAE-2, FSQ, or other multi-layer VQ models:** The paper explicitly scopes itself to single-layer quantization with unconditional entropy models (Section 5.2.2). Criticizing the absence of methods that require multi-layer/conditional architectures is outside the paper's stated scope. Removed.
- **"The paper does not report variance or confidence intervals" — removed as a nice-to-have but kept as a minor weakness** (see Minor section above). The point about missing VQ-STE-1d on images was also kept.
- **Generic criticisms** about "weak evidence for claims," "insufficient comparison," or "overly optimistic conclusion" that lack concrete anchors in the paper text — removed as noise.
- **The alternating optimization being insufficiently novel** — the reviewer's claim that prior work (Ballé et al. 2017, Theis et al. 2017) used similar schemes is noted, but the paper's approach is distinct (separate VQ encoder/decoder optimization). Demoted to the underspecification point.

## Novel Insights

The harsh critic's identification of the Stokes theorem derivation error is the most insightful observation across the reviews. Beyond what the paper itself states, there is a deeper point: the paper's core methodological contributions (alternating optimization and sphere-noise sampling) are logically separable from the mathematical justification attempted in Section 4.2. The empirical results in Table 2 provide cleaner evidence for sphere-noise than any theoretical argument would. The paper would be *stronger* if it dropped the flawed Stokes derivation entirely and presented sphere-noise as a principled heuristic motivated by the gradient analysis in Section 3.2 — specifically, the insight that optimal encoder gradients at boundaries should approximate loss differences between adjacent centers, and sphere-noise achieves this via sampling.

## Suggestions

1. **Fix or remove the Stokes theorem derivation (Section 4.2).** Either provide a correct mathematical derivation with proper surface measure and normal components, or clearly state that the method is a heuristic stochastic approximation motivated by the gradient analysis of Section 3.2 and validated empirically. The empirical results in Section 5 and Table 2 can stand on their own; an incorrect theoretical claim only weakens the paper.

2. **Add a controlled image compression baseline** using scalar quantization with a *discrete* entropy model (e.g., 1D VQ with codebook size equal to the number of quantization levels). This would isolate the effect of the sphere-noise VQ from the entropy model confound. The ablation in Table 2 partially addresses this, but the Table 1 comparison should be clean.

3. **Specify the alternating optimization schedule** (per mini-batch? per epoch? with what stopping criterion?) and the number of Monte Carlo samples used for sphere-noise gradient estimation.

4. **Report error bars or confidence intervals** on BD-rate results, at least for the main image compression experiments.

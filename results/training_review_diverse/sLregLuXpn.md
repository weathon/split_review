Now I have a thorough understanding of the paper. Let me write the final consolidated review.

---

## Summary

This paper provides a theoretical framework for understanding Gaussian noise injection during training of GAN-based image-to-image (I2I) translation models. The key contributions are: (1) Theorem 1 connecting the derivative of $f$-divergence under noise injection to a weighted mean square error between score functions, extending prior results from marginal to joint distributions; (2) Theorems 2–3 showing that robustness to Gaussian noise implies resilience to other noise types with matched covariance, for both Gaussian and arbitrary signal sources; (3) Corollary 1 providing a principled optimal training noise variance. Experiments on Cat→Dog (GP-UNIT), Photo→Sketch (Sketch Transformer), and face super-resolution (HiFaceGAN) across five noise types and six intensity levels show that noise injection improves FID/KID metrics on noisy inputs and that the predicted optimal training variance (0.08 for the tested range) matches experimental findings.

## Strengths

- **Novel theoretical connection between $f$-divergence and score matching for I2I translation.** Theorem 1 extends prior work that connected KL and Fisher divergences for marginal distributions (Verdú 2010; Lyu 2012) to $f$-divergence of joint distributions. The derivative formula reveals how the rate of change of divergence with respect to noise variance is governed by a score-matching term, providing a formal explanation for why Gaussian noise injection helps align distributions.

- **Generalized robustness guarantee.** Theorems 2 and 3 establish that for both Gaussian and arbitrary signal sources, robustness to Gaussian noise during training implies resilience to other noise types with matched covariance, for small inference-noise variance. The approximation $\rho(\sigma_t^2,\sigma_e^2\Sigma_{\tilde{e}}) = \rho_g(\sigma_t^2,\sigma_e^2\Sigma_{\tilde{e}}) + o(\sigma_e^2)$ in Eq. (8) and its generalization in Eq. (9) are non-trivial theoretical contributions that go beyond empirical observations.

- **Principled optimal noise variance selection and its experimental validation.** Corollary 1 gives closed-form guidance: for i.i.d. inference noise with bounded variance $\lambda_{\max}$, the average-case optimal training variance is $\lambda_{\max}/2$. The ablation study (Fig. 5) directly confirms this: with $\lambda_{\max}=0.16$, $\sigma_t^2=0.08$ yields the smallest average FID, exactly matching the theoretical prediction — a specific, non-obvious quantitative prediction that holds.

- **Reasonably comprehensive experimental validation.** The paper evaluates three distinct architectures (HiFaceGAN, GP-UNIT, Sketch Transformer) across five noise types (Gaussian, Uniform, Color, Laplacian, Salt & Pepper) at six intensity levels. Tables 1 and 2 show consistent improvements over baselines. The threshold condition $\sigma_e^2 > 0.5\sigma_t^2$ from Theorem 2 Part 2 is shown to predict when noise-trained models outperform clean-trained ones, demonstrating predictive power.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Theoretical quantities (KL-divergence) vs. experimental metrics (FID/KID).** The core theoretical analysis is conducted in terms of KL-divergence (or $f$-divergence) between distributions, while experiments use FID and KID. The paper acknowledges this gap (lines 207–208: "it is interesting to note that although our analysis uses the KL-divergence, the FID scores exhibit (near-) convexity…") and shows that qualitative trends match (convexity, optimal variance location, threshold condition). However, it does not provide a more direct bridge — for example, computing KL on Inception features, or validating on a synthetic setting where KL can be exactly computed. This makes the theory → experiment link suggestive rather than confirmatory. A synthetic Gaussian-data experiment would strengthen the claim considerably.

- **Choice of training noise variance in main experiments vs. theoretical recommendation.** The main experiments (Tables 1–2) use $\sigma_t^2=0.04$ as the default, while the ablation study (Fig. 5) uses $\lambda_{\max}=0.16$ and confirms that $\sigma_t^2=0.08$ (the value predicted by Corollary 1) yields the best average FID. The paper does not explain why $0.04$ was chosen for the main experiments or disclose the inference-noise range used there. If the max noise level in the main experiments differs from the ablation's $\lambda_{\max}=0.16$, the choice of $0.04$ may be defensible, but this is not discussed. The inconsistency creates the appearance that the main results use a suboptimal variance by the paper's own theory.

- **Near-reversibility assumption is discussed but not verified for the tested models.** The paper states that "Many I2I models exhibit near reversibility" and uses this to claim that the input marginal divergence can estimate model behavior with unseen noise (lines 93–96). However, the equality $D_f(\hat{Q}_{\hat{Y}}\|\bar{Q}_{\bar{Y}}) = D_f(\hat{P}_{\hat{X}}\|\bar{P}_{\bar{X}})$ requires a reversible generator, which is questionable for face super-resolution (HiFaceGAN — low to high resolution loses information) and photo→sketch (a sketch is a drastic abstraction). Fortunately, the inequality $D_f(\hat{Q}_{\hat{Y}}\|\bar{Q}_{\bar{Y}}) \leq D_f(\hat{P}_{\hat{X}}\|\bar{P}_{\bar{X}})$ always holds by data processing, so the bound is valid regardless — reversibility only affects tightness. But the paper's language ("leverage this property… can estimate model behavior") somewhat overstates the role of reversibility. The authors should either (a) measure reconstruction error to quantify how near-reversible their models actually are, or (b) more clearly state that the inequality alone suffices for the analysis.

- **Limited comparison against diffusion-based I2I methods.** The paper mentions diffusion models in related work and provides one qualitative comparison to DiffuseIT (Fig. 3), while claims that diffusion models "also exhibit vulnerability to noisy inputs" (line 32). Given the parallel between noise injection in GANs and noise-based training in diffusion models, a more systematic comparison (e.g., SDEdit, BBDM, or a diffusion model with noise augmentation at inference) would help establish whether the proposed GAN + GNI approach offers practical advantages beyond its own baseline. The paper's focus is GAN robustness, not diffusion benchmarking, but the single qualitative DiffuseIT example is insufficient to support the claim that diffusion models are more vulnerable.

### Trivial

- **Taylor expansion notation.** Eq. (4) writes $D_f(P\|Q) = D_f(\bar{P}\|\bar{Q}) + \frac{\sigma_t^2}{2}\eta_f(\sigma_t^2) + o(\sigma_t^2)$, using $\eta_f(\sigma_t^2)$ (evaluated at the expansion point $\sigma_t^2$) rather than $\eta_f(0)$ (evaluated at 0, as a standard Taylor expansion around 0 would). This is notationally sloppy — a standard expansion around 0 would use $\eta_f(0)$. The mathematical reasoning is still interpretable, but the notation should be corrected.

## Nice-to-Haves

- A synthetic experiment where the source distribution is Gaussian (e.g., Gaussian image patches or features) and KL-divergence is computed directly, to cleanly validate the derivative, convexity, and optimal variance predictions of the theory.
- An ablation on generator capacity: does noise injection help equally for different model sizes, or is there an interaction?
- Reporting results for HiFaceGAN face super-resolution and Imagenet-C corruptions in the main paper (if not already included in the appendix).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The paper mentions experiments on Imagenet-C corruptions and face super-resolution but shows no main-paper results."** — These are likely in the appendix (stripped by the parser). The instruction requires removing criticisms about missing appendix content. Removed.
- **"The equality $D_f(\hat{Q}_{\hat{X},\hat{Y}}\|\bar{Q}_{\bar{X},\bar{Y}}) = D_f(\hat{P}_{\hat{X}}\|\bar{P}_{\bar{X}})$ relies on the generator being reversible."** — This is factually incorrect. The equality holds because the mapping $z \mapsto (z, G(z))$ is injective (the first coordinate recovers $z$), requiring no reversibility of $G$. Reversibility is only needed for the *output marginal* divergence to equal the input marginal divergence. The paper correctly states this (line 96: "The output divergence is bounded by this value, with equality under a reversible model"). Removed — reviewer misunderstanding.
- **"Insufficient comparison with diffusion-based I2I models" framed as a critical flaw.** — The paper's contribution is about GAN-based I2I translation, not about comparing to diffusion models. The one diffusion comparison is appropriate for the paper's scope. Kept as a minor weakness (above) rather than a fatal/major one.
- **Various pure formatting/style nitpicks.** — Removed per instructions.
- **"The paper could also cover Y/domain Z/additional tasks."** — These are scope-creep demands. Removed.

## Novel Insights

The reviews surface an important tension that the paper does not fully resolve: the theory is clean (KL-divergence of Gaussian signals, score-matching derivative, closed-form optimal variance), but the experiments are on real images with non-Gaussian structure using a different metric (FID). The paper treats the empirical alignment of FID trends with KL predictions as "validating" the theory, but a skeptic would note that convexity in $\sigma_e^2$ and a threshold at $\sigma_e^2 > 0.5\sigma_t^2$ are fairly coarse qualitative signatures that could arise from multiple mechanisms. The most convincing point is the quantitative match of $\lambda_{\max}/2$ for optimal training variance — this is a precise, non-obvious prediction that is confirmed. The paper could lean more heavily on this as its strongest validation point.

## Suggestions

1. **Use the theoretically optimal variance in the main experiments, or explain the choice.** If the main experiments use a different inference-noise range than the ablation, state this explicitly. If $\sigma_t^2=0.04$ was chosen to limit clean-image degradation, discuss the trade-off.
2. **Add a clean synthetic experiment** where the source is Gaussian (e.g., sampled image patches or a fixed feature space) and KL-divergence is computed exactly, to validate Theorem 1's derivative and the convexity predictions directly.
3. **Quantify near-reversibility** by measuring reconstruction error (e.g., $G^{-1}(G(x)) \approx x$) for the tested models, or clarify that the inequality alone suffices and reversibility is only needed for a tight bound.
4. **Correct the Taylor expansion notation** in Eq. (4) so that $\eta_f$ is evaluated at 0 (or explain why $\sigma_t^2$ is the appropriate evaluation point).
5. **Add at least one systematic diffusion baseline** (e.g., SDEdit or a denoising diffusion probabilistic model) with noise augmentation at inference, to substantiate the claim about diffusion model vulnerability.

## Score and Decision

**Originality:** Good — the connection between $f$-divergence and score matching for joint distributions in the I2I context is novel, as are the robustness transfer results for matched covariance.

**Importance of research question:** High — noise robustness is a real practical problem for deployed I2I systems.

**Claims supported:** Mostly — the core theoretical claims are well-supported; the experimental validation is qualitatively consistent but would benefit from a tighter quantitative bridge.

**Soundness of experiments:** Adequate — three architectures, multiple noise types and intensities, and an ablation that validates the optimal variance prediction. Missing a direct KL-measurement experiment.

**Clarity of writing:** Good — the paper is clearly structured and the theoretical results are presented with appropriate notation. Some minor notation issues in the Taylor expansion.

**Value to the community:** Moderate to high — practitioners can use the optimal variance guidance directly, and theorists benefit from the formal connection between noise injection and score matching for I2I.

The paper makes a genuine theoretical contribution with reasonable experimental support. The weaknesses are minor — they do not undermine the core claims. The training variance inconsistency and the KL/FID metric gap are addressable in revision. The reversibility concern is largely a misunderstanding of what the paper asserts. Overall, this is a solid submission.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
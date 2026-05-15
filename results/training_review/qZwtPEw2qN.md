Now I have all the evidence needed. Let me produce the consolidated final review.

## Summary

This paper studies the practical setting where a small set of clean images and a large set of noisy images are available for training diffusion models. The authors train over 80 models across three datasets (ImageNet, CelebA-HQ, CIFAR-10) and find that a mixture of 10% clean + 90% noisy data (σ=0.2) achieves near state-of-the-art FID (1.68 vs. 1.41 on ImageNet), dramatically outperforming either set alone. On the theoretical side, the paper derives minimax-optimal sample complexity bounds for learning Gaussian Mixture Models with heterogeneous noise levels, revealing that noisy samples are discounted polynomially (1/σ⁴) for dimensionality reduction but exponentially (1/σ^{4k−2}) for fine-grained estimation — explaining why a few clean samples are disproportionately valuable.

## Strengths

- **Extensive empirical validation of the mixture hypothesis.** The paper trains over 80 models across three datasets (ImageNet ~1.3M, CelebA-HQ 30K, CIFAR-10 60K) and three noise levels (σ=0.05, 0.1, 0.2). Table 3 shows that adding 90% noisy data (σ=0.2) to just 10% clean data improves ImageNet FID from 10.57 (clean-only 10%) and 5.32 (noisy-only 100%) to 1.68, near the 1.41 of 100% clean. This directly and robustly supports the central empirical claim.

- **Novel theoretical guarantees for heterogeneous-noise GMMs with matching lower bounds.** Theorem 3.1 provides minimax optimal upper bounds for learning k-atomic distributions from samples with heterogeneous noise levels, and Theorem 3.3 proves a matching lower bound. The bound cleanly separates dimensionality reduction error (polynomial in d, discounted by 1/σ⁴) from fine-grained estimation error (discounted by 1/σ^{4k−2}) — showing the exponential advantage of clean samples for low-dimensional detail. This provides a principled theoretical model for the phenomenon.

- **Stress-testing at extreme settings.** The paper pushes beyond typical regimes — testing 1% clean + 99% noisy data (σ=0.2) yields FID 3.53 on CIFAR-10 vs. 60.73 for purely noisy training and 11.93 for consistency-based noisy-only training. Using 90% noisy data at σ=0.4 still achieves FID 3.56 vs. 17.30 for 10% clean alone. These extremes strengthen the claim that even minimal clean data is disproportionately effective.

- **Ablation study showing the gap to clean-data performance can be further reduced.** Section 5.3 systematically improves FID from 1.68 to 1.55 through more training, adjusted sampling schedule, consistency fine-tuning, and weight decay — approaching the 1.41 clean-only baseline. This demonstrates the remaining gap is due to optimization, not a fundamental limitation of the mixture approach.

## Weaknesses

### Fatal

None.

### Major

- **The theory (GMMs, Wasserstein) and experiments (images, FID) are never quantitatively connected.** The theoretical results are for k-atomic Gaussian mixtures with known component counts and known noise levels, evaluated under Wasserstein distance. The experiments are on natural image distributions with neural diffusion models trained via score matching, evaluated by FID. The paper never attempts to map the theoretical rates (e.g., the 1/σ^{4k−2} discount factor) to the observed FID improvements by estimating an effective k or verifying that the predicted functional form matches the data. The "pricing" section (Sec. 4.5) uses the theory's effective sample size as a qualitative analogy but does not test the predicted functional form. This leaves the theory and experiments as two parallel contributions rather than a unified story, weakening the "explanation" claim.

- **The title and framing promise "Data Scaling Laws" but no empirical scaling laws are fit or validated for the image experiments.** The theoretical section provides scaling rates for GMMs (sample complexity bounds), but the experimental section never fits a parametric scaling law (e.g., FID(n_clean, n_noisy, σ) ≈ a·n_clean^{−α} + b·n_noisy^{−β(σ)}) to test whether the predicted forms hold. The abstract and introduction imply the theory "explains" the experimental observations, but the connection remains at the level of intuition rather than quantitative verification. This is a structural mismatch between the paper's packaging and its actual empirical evidence.

### Minor

- **The pricing derivation in §4.5, while clever, is heuristic and not quantitatively grounded by the theoretical model.** The effective sample sizes n_d and n_l are taken from the GMM bound, but the paper then asserts the low-dimensional term dominates (assuming the asymptotic regime) without justifying that the datasets are in this regime. The pairwise-comparison method yields bounds on 1/c_σ that are internally consistent but are not validated against held-out experiments. The derived ranges (e.g., 1.5 ≤ 1/c_{0.2} ≤ 1.75) add a veneer of precision to what is essentially a qualitative observation.

- **The paper does not report the number of independent seeds for FID estimates** (the ± values suggest multiple seeds but this is not explicitly stated), nor does it provide full model architecture details (e.g., EDM configuration for each dataset) in the visible text. Some of these may appear in the appendix (which was stripped during parsing), but the main text could be clearer.

### Trivial

None.

## Nice-to-Haves

- Testing non-Gaussian corruptions (e.g., Gaussian blur, masking) would broaden the applicability of the findings. The paper acknowledges this limitation in §6 and scopes itself to additive Gaussian noise, so this is a natural extension rather than a flaw.
- A visual comparison of generated samples from the different training regimes (full clean, 10% clean only, 100% noisy, 10% clean + 90% noisy) would help readers intuitively understand what the FID differences mean qualitatively.
- Varying total dataset size while keeping the mixture ratio constant would reveal whether the mixture benefit persists at smaller scales.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"Impossible" is too strong** — The paper qualifies this with "at these sample sizes" (abstract, line 4), making it a conditional claim. The asymptotic theory (Consistent Diffusion Meets Tweedie) guarantees exact recovery only in the infinite-data limit, which the paper explicitly notes. This is a semantic nitpick, not a substantive issue.

2. **"The method is not novel"** — The paper never claims algorithmic novelty as a contribution. The contribution statements (lines 50–56) are about the empirical findings and theoretical analysis. The method itself is described as a straightforward application of existing losses to a mixed dataset, which is appropriate rather than a weakness.

3. **Missing details about seeds, architecture, hyperparameters** — The paper references an appendix for proofs and algorithmic details. Per the parser artifact rule, these sections exist in the original submission but are stripped here. Architectural details ("used EDM hyperparameters") are indicated in the text.

4. **Limited to additive Gaussian noise** — The paper's Lemma 2.2 is specific to additive Gaussian noise, and the method is designed for this setting. The limitations section (Sec. 6) explicitly acknowledges this. Criticizing this absence is scope creep: the paper does X and should be evaluated on whether it does X well, not whether it also does Y.

5. **"No scaling law fits" (as a fatal flaw)** — The paper does provide theoretical scaling laws (sample complexity bounds showing how error scales with n, σ, k). The issue is that these are not quantitatively validated against experimental data, which is already captured as a Major weakness above. The claim that the paper "delivers no quantitative scaling law" is too strong; it delivers *theoretical* scaling laws, but the *empirical* scaling law validation is missing.

## Novel Insights

None beyond the paper's own contributions. The empirical finding and theoretical analysis are the key contributions.

## Suggestions

1. **Quantitatively connect theory to experiments.** Estimate an effective k and d for image distributions by fitting the theoretical rate form to the observed FID data. Show that the predicted discount factor 1/σ^{4k−2} approximately matches the ratio of FID improvements across different noise levels. Even a rough calibration would significantly strengthen the claim that the theory "explains" the results.

2. **Recalibrate the title and framing.** Consider a title that better reflects the paper's actual contributions — something like "How Much is a Noisy Image Worth? Benefits of Mixed Clean and Corrupted Data for Diffusion Training" — or, if keeping "Data Scaling Laws," add an explicit empirical scaling law fit to the experimental data.

3. **Tighten the pricing analysis.** Regress FID against a function of (p, σ) derived from the theoretical effective sample size, estimate c_σ with confidence intervals, and validate on held-out experimental conditions. This would turn a heuristic into a rigorous contribution.

4. **Report seed counts explicitly** and consider adding a visual sample gallery comparing the four regimes (clean-only, noisy-only, clean-only smaller, mixture) to help readers interpret the FID differences qualitatively.

## Score and Decision

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
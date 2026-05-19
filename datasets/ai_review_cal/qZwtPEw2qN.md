- Decision: Accept
- Avg Score: 6.80
- Scores: 6, 6, 8, 8, 6
Now I have a thorough understanding of the paper and can produce the final consolidated review.

## Summary

This paper investigates whether a small set of clean images combined with a large set of noisy (Gaussian-corrupted) images can match the performance of training on fully clean data in diffusion models. Through over 80 trained models across CIFAR-10, CelebA-HQ, and ImageNet, the authors demonstrate that a 90%/10% noisy/clean mixture achieves FID scores close to the 100% clean baseline (e.g., ImageNet: 1.68 vs. 1.41), far outperforming training on either the small clean set or the full noisy set alone. The paper also develops novel minimax-optimal sample complexity bounds for Gaussian Mixture Models with heterogeneous noise levels, providing a theoretical framework that explains why noisy data helps with dimensionality reduction but is exponentially worse for fine-grained estimation. A practical data pricing scheme with tight empirical bounds is derived.

## Strengths

- **Comprehensive scaling experiments across three datasets with >80 models.** The paper systematically trains models from scratch (not fine-tuning) on CIFAR-10, CelebA-HQ, and ImageNet at multiple corruption ratios and noise levels (σ=0.05, 0.1, 0.2, 0.4), establishing the robustness of the main finding across dataset sizes ranging from 30K to ~1.3M samples. The central result — 90% noisy + 10% clean approaching clean-only FID — is supported by extensive tabular data (Table "clean-mix-comparison").

- **Novel minimax-optimal sample complexity bounds for heterogeneous GMMs.** Theorem 1 and Corollary 1 derive upper and lower bounds showing noisy samples are discounted by $1/\sigma^4$ for dimensionality reduction but by $1/\sigma^{4k-2}$ for fine-grained component estimation. This provides a principled theoretical explanation for why small clean sets suffice while pure noisy data requires exponentially more samples — a genuinely novel contribution to the heterogeneous noise literature.

- **Practical data pricing with tight empirical bounds.** Section 5.4 derives narrow intervals for the exchange rate between clean and noisy samples (e.g., $1.5 \le 1/c_{0.2} \le 1.75$ consistently across all three datasets at σ=0.2). This quantifies the utility trade-off in a concrete, actionable way that prior work on ambient diffusion did not attempt.

- **Computationally efficient algorithm.** Algorithm 1 achieves strong performance without the expensive consistency loss used in prior work (Daras et al. 2024), which required 2-3× more computation and 2× GPUs. The method adds no training overhead over standard denoising score matching.

- **Validation under extreme conditions.** The 1% clean + 99% noisy experiment on CIFAR-10 (σ=0.2) achieves FID 3.53 — a dramatic improvement over pure noisy (60.73 without truncation, 11.93 with consistency). This demonstrates robustness far beyond standard regimes.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Theoretical connection to experiments is qualitative, not quantitative.** The GMM analysis (Section 4) is sound and independently valuable, but the link to the diffusion model experiments is suggestive rather than validated. The paper frames the theory as providing "theoretical evidence" for the empirical findings, but the experiments are on natural images with diffusion models while the theory operates on Gaussian mixtures with known noise levels. The paper does not attempt to fit the theory's scaling laws (e.g., whether the effective sample size formulas predict observed FID improvements). The theory and experiments are presented as parallel contributions; the connection is plausible but undemonstrated.

- **Limited to additive Gaussian corruption.** All experiments use a single corruption model (additive Gaussian noise at σ=0.05, 0.1, 0.2, 0.4). The paper acknowledges this limitation explicitly ("we only studied the case of additive Gaussian Noise corruption"), but it reduces the generality of the practical recommendations. For scientific applications cited as motivation (MRI, black-hole imaging), the corruption model is more complex, often non-Gaussian, and sometimes unknown. Whether the main findings transfer to other corruption types (compression artifacts, blur, missing pixels) remains untested.

- **The "pushing performance" section (Table 5) lacks a parallel baseline for the clean model.** The authors apply additional training steps, modified sampling schedules, consistency fine-tuning, and weight decay to the mixture model (improving FID from 1.68 to 1.55), but do not apply the same optimizations to the 100% clean baseline (1.41). This makes the "closing the gap" claim in this section less precise, though the headline result (1.68 vs. 1.41 without extra tuning) remains unaffected.

### Trivial

- None.

## Nice-to-Haves

- A systematic study of how the benefit of the mixture varies as a function of both noise level σ and clean fraction p across all datasets (a FID heatmap) would provide a more complete picture than the pricing inequalities alone. The paper already has most of this data in Table "clean-mix-comparison"; a visual summary could strengthen the presentation.
- Reporting total GPU-hours or training time for each experiment would help practitioners gauge the computational savings of the method over consistency-based training.

## Removed Points

- **Missing augmentation baseline on the small clean set (Harsh Critic, Critical Issue #1).** The critic argues that the 10% clean baseline (FID 17.30) might be unfairly weak because standard augmentations might not have been applied — and that stronger augmentation could close the gap to the mixture result. This criticism is removed because: (1) all conditions use the same EDM training pipeline with the same augmentations (horizontal flips are standard in EDM for CIFAR-10/ImageNet), making comparisons internally consistent; (2) the gap between 10% clean (17.30) and the mixture (2.81) is ~15 FID points — far too large for standard augmentations to plausibly close; (3) the paper's central comparison is the mixture's closeness to the 100% clean baseline (2.81 vs. 1.99), not the mixture vs. 10% clean alone. The critic's speculation that augmentation might bring the 10% clean FID to "close to 3.0" is unrealistic given the small sample size (6000 images for CIFAR-10).

- **Strawman about comparison fairness (from "pushing performance" section).** The critic's concern about the clean model not receiving the same extra training steps in the pushing-performance section is technically valid but applies only to a supplementary experiment (Table 5) that is explicitly about *improving* the mixture model. The paper's core result — the mixture's strong performance with default hyperparameters — is unaffected. This is demoted to Minor, as noted above.

- **"Methodological gap" framing of the augmentation issue.** The critic characterizes this as a fatal "methodological gap" that could "inflate the advantage of the mixture." This framing is disproportionate. The FID gap between baseline and mixture is too large for augmentation to bridge. The point does not threaten the paper's central claims.

- **Generic concerns about "could the metric be measuring a proxy" or "confounders not controlled" — no such specific claims were made by the critic and none apply.**

- **Strength Finder's generic strengths removed:** The strength about "addressing an important problem" and "targeting an interesting question" are too generic and lack specific evidence. Dropped.

## Novel Insights

The Harsh Critic raises an insightful observation that the paper's theoretical contribution and empirical contribution operate on different levels — the theory proves rates for GMM estimation, while the experiments study diffusion model FID. This gap is real but the paper does not overclaim; it describes the theory as "theoretical evidence" rather than a formal explanation of the experiments. A genuinely novel observation emerging from the reviews is that the data pricing bounds (Section 5.4), while clever, could be sharpened considerably: the paper derives bounds by comparing ordinal FID rankings between different (p, σ) configurations, but these bounds assume the asymptotic regime is uniformly reached across configurations — an assumption that may not hold at low p values. The narrowness of the derived intervals (e.g., 1.5–1.75 for 1/c_{0.2}) is nonetheless striking and suggests the pricing model captures real structure.

## Suggestions

1. Add a brief discussion clarifying that the clean-only baselines use the same training pipeline (including any standard augmentations from EDM) as the mixture experiments, to preempt the augmentation confound concern.
2. Include a small experiment or discussion on whether the main findings extend to a non-Gaussian corruption (e.g., blur, masking) — perhaps even a single small-scale CIFAR-10 result.
3. Consider adding a visual heatmap of FID across (p, σ) pairs for at least one dataset to make the patterns more accessible than the large table alone.
4. Tone down the framing of the theory as "theoretical evidence" for the experiments, or add a sentence directly connecting the theory's predicted scaling to an observable trend in the experiments (even if only qualitatively).

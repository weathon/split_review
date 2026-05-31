## Summary

This paper empirically investigates whether predictive uncertainties in deep learning follow scaling laws similar to test loss. Across vision (CIFAR-10, ImageNet32) and language tasks (GPT-2 on algorithmic data, Phi-2 fine-tuning), using a range of uncertainty quantification methods (MC Dropout, Deep Ensembles, MCMC, IVON, Laplace), the authors demonstrate that total, aleatoric, and epistemic uncertainties decay as power-laws with dataset size. They also explore scaling with model size and provide theoretical connections to Bayesian linear regression and singular learning theory. The findings suggest that uncertainty scaling is a predictable phenomenon, with practical implications for extrapolating uncertainty to larger datasets and guiding data acquisition.

## Strengths

- **Novel and timely question.** The paper is the first (to my knowledge) to systematically study scaling laws for predictive uncertainty in deep learning, filling an important gap between the well-explored test-loss scaling and the need for calibrated uncertainty in large-scale systems.
- **Comprehensive empirical evaluation.** The study covers multiple architectures (ResNets, WideResNets, ViTs, GPT-2), multiple UQ methods (MC Dropout, Deep Ensembles, MCMC, IVON, Laplace), and both in-distribution and out-of-distribution settings, lending credibility to the claim that power-law scaling of uncertainty is a widespread phenomenon.
- **Consistent power-law behavior.** Despite variation in exponents, the qualitative pattern (uncertainty ∝ N^{-γ}) holds across nearly all configurations, including different optimizers, dropout rates, ensemble sizes, and even a SAM variant, suggesting robustness.
- **Transparent handling of known issues.** The authors acknowledge criticisms of the entropy-based uncertainty decomposition and the decreasing aleatoric uncertainty, and discuss plausible explanations (entanglement, limitations of the metric) rather than ignoring them.
- **Valuable practical implications.** The findings directly suggest strategies for active learning (predicting marginal uncertainty reduction) and assessing when ensemble predictions have converged, which are of immediate interest to practitioners.

## Weaknesses

### Fatal
None.

### Major
1. **The theoretical connection is weak and loosely tied to the empirical findings.** The derivation in Section 5.1 is only for Bayesian linear regression, and the link to singular learning theory is speculative (“speculative theoretical link,” “we intend to investigate such formal connections in future work”). For a paper titled “Scaling Laws for Uncertainty in Deep Learning,” this leaves a significant gap between the strong empirical claims and the theoretical support.
2. **Aleatoric uncertainty decreasing with N is counterintuitive and undermines the decomposition.** The paper repeatedly observes AU decaying strongly (often with exponents near or even steeper than EU). The authors note this is known to be problematic, but it remains a central inconsistency: if AU is supposed to capture irreducible stochasticity, it should be constant. The reliance on a decomposition that behaves unexpectedly weakens the interpretability of the core results.
3. **Language experiments are too limited to support the claimed modality generality.** The only clear scaling in language is from GPT-2 on a synthetic algorithmic dataset, where the exponents are extremely steep (γ≈−2.9) and the setting is far from realistic text tasks. The Phi-2 fine-tuning experiment shows “flat” uncertainties, which the authors attribute to pre-training but does not add evidence for scaling. The paper would be stronger with at least one natural-language task (e.g., GLUE, sentiment classification) showing non-flat scaling.
4. **Variability of exponents reduces predictive power.** The scaling exponents differ widely across UQ methods, architectures, and hyperparameters (e.g., γ_EU ranges from roughly -0.1 to -0.8 on CIFAR-10 alone, and -2.95 on the algorithmic dataset). This unpredictability limits the practical utility of the scaling laws—one cannot confidently extrapolate uncertainty without first estimating the exponent for a specific setup, which defeats the purpose.

### Minor
- Some experiments (e.g., WideResNet Deep Ensembles in Fig. 2b) are reported from a single fold, while others average over folds. The paper does not consistently provide error bars, making it hard to assess the statistical significance of the power-law fits.
- The ImageNet32 experiment (Fig. 6) uses only 4-9 data subsets, which is sparse for fitting a power law. The quality of the fits is not quantified (e.g., R² values).
- The paper briefly mentions permutation symmetries to explain weak EU scaling with model size, but does not provide supporting experiments (e.g., ensemble diversity metrics).

### Trivial
- The use of the acronym “V1” for Variational Inference (Section 3, first line of MC Dropout) is a typo.

## Nice-to-Haves

- A more rigorous theoretical derivation for over-parameterized models, perhaps building on the effective dimensionality results cited (Lau et al., 2024; Chen et al., 2024), would greatly strengthen the paper’s contribution.
- Error bars (e.g., confidence intervals on exponents) for all power-law fits would help assess reliability.
- A deeper investigation of the decreasing AU, e.g., by comparing with alternative uncertainty measures such as predictive entropy on a held-out set with known label noise, could clarify whether the effect is an artefact of the metric or a genuine phenomenon.

## Novel Insights

Beyond the paper’s own contributions, the most striking observation is that epistemic uncertainty decays with data size even in massively over-parameterized models, suggesting that Bayesian non-identifiability does not prevent posterior contraction in practice—at least as measured by ensemble diversity. The interaction with SAM, where flatter minima preserve epistemic uncertainty at larger N, hints that the geometry of the loss landscape influences scaling exponents. The finding that AU also decays—even though it is supposed to be irreducible—raises serious questions about the standard uncertainty decomposition and calls for more refined metrics.

## Suggestions

- Add at least one additional language task with natural text (e.g., fine-tuning a small BERT on SST-2) to support the claim of cross-modal scaling.
- Provide R² or similar goodness-of-fit measures for all power-law regressions, and report exponents with standard errors.
- Discuss more explicitly how the decreasing AU affects the interpretation of the scaling results, and consider reporting an alternative decomposition (e.g., based on mutual information) to see if the pattern persists.

## Score and Decision

**MY FINAL SCORE:** <score>7.5</score>  
**MY FINAL DECISION:** <decision>Accept</decision>
## Summary

This paper introduces *monitorability* as a formal property of neural networks, capturing the degree to which internal representations allow runtime detection of erroneous predictions. The authors propose the MIRA Score (Monitorability via Input peRturbAtion), which quantifies monitorability by applying FGSM-based norm-bounded perturbations to in-distribution data and measuring feature-space surprisal via a chi-square–calibrated Mahalanobis distance — entirely without external OoD data. Experiments span computer vision (CIFAR-10/100, 4 architectures), tabular data (Sensorless Drive Diagnosis, 5 models), and NLP (SST-2 fine-tuning, 4 transformer models), where MIRA rank-ordering consistently aligns with the best-achievable OoD detection AUROC across ODIN, Mahalanobis, and energy-based detectors.

---

## Strengths

- **Genuine conceptual novelty.** The formalization of *monitorability* as an intrinsic, architecture-independent property of neural networks is new to the literature. No prior work provides a formal definition or quantitative score for this idea, and the paper clearly fills the gap.

- **Technically elegant metric design.** Converting Mahalanobis distance into a chi-square surprisal score (Eq. 3) is a thoughtful solution to cross-layer dimension calibration. Without this normalization, comparing MIRA scores across layers with different hidden sizes would be meaningless.

- **Broad empirical coverage.** Three modalities (vision, tabular, NLP), ~16 distinct architectures/model families, and 7+ OoD datasets for vision alone make the experimental scope genuinely broad. Rank ordering of models by MIRA is consistent with rank ordering by best AUROC in every domain.

- **OoD-data-free practicality.** A pre-deployment metric requiring only ID data and cheap FGSM perturbations directly addresses a real deployment pain point: practitioners cannot typically assume access to representative OoD data before deployment.

- **Qualitative consistency supported by t-SNE.** Figure 2 provides convincing complementary evidence that MIRA differences track visual differences in feature-space structure, reinforcing the quantitative results.

---

## Weaknesses

### Fatal
None.

### Major

1. **Methodological circularity in validation.** MIRA is computed via Mahalanobis surprisal in feature space, and one of the three "proxy" detectors used for ground-truth comparison is the Mahalanobis OoD detector (Lee et al., 2018b) — which also uses Mahalanobis distance in the same feature space. A high MIRA score means the feature space has clean class-conditional structure, which directly implies high Mahalanobis AUROC. This creates a structural correlation that inflates confidence in the validation. The paper would be better served by including at least one validation detector (e.g., a nearest-neighbor or density-estimation method) whose assumptions do not overlap with MIRA's Gaussian-distance foundation. This concern does not invalidate the results but does weaken the claim that MIRA is "detector-agnostic."

2. **No quantitative correlation analysis.** The central empirical claim — that MIRA "correlates strongly" with OoD detection performance — is never backed by a correlation coefficient (Spearman ρ, Kendall τ). With 4–5 data points per domain, the margin for confidence-interval-aware analysis is tight. A rank-correlation table across all models (pooled or per-domain) with p-values would substantiate the claim; their absence leaves the conclusion as a qualitative observation.

3. **Definition 1 is trivially satisfied.** As stated, Definition 1 requires only the *existence* of a set Z^l that perfectly separates correct predictions — but such a set trivially exists for any model by defining Z^l = {f^l(x) : L(f(x),y) ≤ ε}. The definition does not require Z^l to be computable, structured, or practically usable. This means virtually every model is "l-monitorable" under Definition 1, which undermines its role as a formal discriminating concept. The meaningful quantity is the *quality and compactness* of Z^l, which MIRA captures empirically but which Definition 1 does not encode.

### Minor

1. **MIRA scale is not calibrated across domains.** MIRA ranges 0–90 for vision, 4–64 for tabular, and 2000–3800 for NLP. The paper does not explain why scales differ by orders of magnitude or caution readers against cross-domain comparisons. A normalized score (e.g., percentile-based or bounded in [0,1]) would be more interpretable.

2. **No ablations on key design choices.** The choice of FGSM over random or PGD perturbations, the choice of ℓ∞ vs. ℓ2 norm, and the restriction to the penultimate layer are all asserted rather than justified empirically. A targeted ablation would clarify which aspects of MIRA design actually drive the correlation.

3. **Small number of models per domain.** The rank-correlation between MIRA and AUROC is assessed over 4–5 models per domain. While the rank ordering is perfectly preserved, statistical significance of a rank-5 Spearman correlation is low (permutation p-values ≈ 0.08 for perfect rank with n=4). The claim of "strong correlation" is not unreasonable but should acknowledge this.

### Trivial

- The perturbation range selection procedure (ε_min = smallest ε reducing accuracy to threshold; ε_max = 2·ε_min) is deferred to the appendix without discussion of sensitivity in the main text.

---

## Nice-to-Haves

- Comparison of MIRA to simpler feature-space baselines (e.g., silhouette score, Fisher's discriminant ratio on ID features) to justify the perturbation-based design.
- A scatter plot of MIRA vs. best AUROC with all models from all domains plotted together, with a regression line and confidence band.
- Application of MIRA to layer selection (beyond just asserting the penultimate layer is best), which the conclusion mentions as a use case.

---

## Novel Insights

The key insight — that model monitorability can be characterized by measuring how perturbed in-distribution inputs behave in feature space, rather than requiring OoD samples — is a substantive and underexplored idea. The connection between local decision-boundary sensitivity (probed via FGSM) and the global structure of internal representations (assessed via Gaussian surprisal) provides a principled bridge between adversarial robustness analysis and runtime monitoring. The chi-square normalization of Mahalanobis distance, enabling cross-layer comparison, is a small but non-obvious technical contribution. Crucially, the paper demonstrates that equally accurate models can have dramatically different monitorability (e.g., CustomNet vs. ViT at 100% ID accuracy), which is an empirically important observation for the safety-critical systems community.

---

## Suggestions

- Add Spearman rank-correlation coefficients and p-values for MIRA vs. best AUROC in each domain table.
- Restate Definition 1 to require that Z^l be a *decision region of a computationally tractable monitor* (e.g., a level set of a proper scoring rule), which would make the definition non-trivial and align it better with MIRA's purpose.
- Include one non-Mahalanobis-based OoD detector in the "best-of" proxy (e.g., KNN-based or flow-based) to address the circularity concern.
- Report a simple baseline (e.g., silhouette score on ID features alone, without perturbations) to quantify what the perturbation component specifically contributes to MIRA's predictive power.

---

## Score and Decision

The paper introduces a genuinely novel concept (monitorability) with a clean, practical metric (MIRA) and substantiates it across three modalities. The rank-ordering of models by MIRA consistently matches rank-ordering by OoD detection capability. The main technical concerns — Definition 1's triviality, the Mahalanobis circularity in validation, and the absence of quantitative correlation statistics — are real but not fatal; they are methodological gaps that a revision could address. Given the novelty of the contribution, broad experimental scope, and practical value for safety-critical deployment decisions, this paper merits acceptance, though it falls short of a strong accept due to the issues above.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>
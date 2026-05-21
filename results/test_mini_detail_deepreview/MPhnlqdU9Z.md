Here is the final consolidated review.

---

## Summary

This paper introduces the concept of *monitorability* — a model's intrinsic ability to reveal inference errors through its internal activations — and proposes the MIRA Score to quantify it. MIRA applies norm-bounded input perturbations (FGSM), measures how separable perturbed and unperturbed features are in the penultimate layer via dimension-calibrated Mahalanobis distance, and integrates over a range of perturbation magnitudes. The paper validates MIRA by comparing its ranking against the best achievable OoD detection AUROC across three methods (ODIN, Mahalanobis, Energy) on vision, tabular, and NLP domains, showing consistent ordinal alignment.

## Strengths

- **Novel problem framing.** The paper formalizes the question "how detectable are a model's failures?" as a pre-deployment property, distinct from runtime detection or OoD detection itself. This is a conceptually useful reframing that bridges feature-space quality and monitoring potential.

- **Detector-agnostic metric requiring only ID data.** MIRA is computed solely from in-distribution data and norm-bounded perturbations (FGSM), without needing OoD datasets or detector-specific tuning. This makes it practical for pre-deployment model selection.

- **Consistent ordinal alignment across three data modalities.** Tables 1–3 show that MIRA scores rank models in the same order as average OoD detection AUROC across vision (CIFAR-10/100), tabular (Sensorless Drive), and NLP (SST-2). For example, ViT (MIRA 89.25, avg AUROC ~99%) vs. CustomNet (MIRA −0.07, avg AUROC ~76%) on CIFAR-10, and DeBERTaV3 (MIRA 3793.6, avg AUROC 86.29%) vs. DistilBERT (MIRA 2015.7, avg AUROC 76.54%) on SST-2. The pattern holds across all three domains.

- **Qualitative feature-space evidence.** t-SNE visualizations (Figure 2) confirm that higher MIRA corresponds to better-organized, more separable feature clusters, providing an intuitive geometric validation of the metric.

## Weaknesses

### Major

- **Definition 1 (monitorability) is mathematically vacuous, undermining the claimed "first formalization."** Definition 1 states that a model is *l*-monitorable if there exists a set Z^l and ε ≥ 0 such that L(f(x),y) ≤ ε ⇔ f^l(x) ∈ Z^l. The paper explicitly notes that "Z^l may be arbitrarily complex." Since no constraints are placed on Z^l, for any fixed ε one can always define Z^l = {f^l(x) : L(f(x),y) ≤ ε}, making the condition hold trivially for every model. The definition is therefore tautological — every neural network is *l*-monitorable under this definition — and cannot serve as a meaningful specification of the property the paper aims to quantify. The MIRA Score (Definition 2) is introduced without any formal connection to this definition, so the claimed "theoretical grounding" is not actually grounded. The paper's central novelty claim — "to the best of our knowledge, this is the first formalization and quantitative measure of monitorability" — rests in part on this definition, which does not hold up under scrutiny.

- **Validation uses OoD detection as a proxy for monitorability without validating the proxy or establishing statistical significance.** The paper frames monitorability around detecting *erroneous predictions* ("the intrinsic ability of a model to highlight potential inference errors"), yet the entire validation evaluates MIRA against OoD detection performance (detecting *distributional shift*). The paper acknowledges in the Preliminaries that "misclassifications may also occur for ID inputs, which is a distinct scenario not directly addressed by OoD detection," but never tests MIRA against actual misclassification detection on ID data or validates that OoD detection performance is a good proxy for error detection. Additionally, the validation relies on *qualitative ordinal alignment* across 4–5 models per domain — no statistical correlation measure (Spearman, Pearson, rank correlation) is reported, and the sample sizes are too small for meaningful correlation analysis. The paper claims "strong correlation" and "good correlation" (Section 4.4, Discussion) without any quantitative evidence.

### Minor

- **No comparison to simpler feature-quality metrics.** MIRA's value as a new metric would be strengthened by comparison to simpler alternatives that can also be computed without OoD data, such as the Fisher discriminant ratio between ID features and perturbed features, the silhouette score of the penultimate layer features, or average intra-class vs. inter-class Mahalanobis distance. Without such comparisons, it is unclear whether MIRA captures anything beyond what a simpler feature-space separability measure would provide.

- **MIRA Score scale is uninterpretable and uncalibrated across domains.** MIRA values range from −0.07 to 89 in vision, 4.37 to 63.51 in tabular, and ~2000 to ~3800 in NLP. The paper provides no normalization or interpretation of these absolute values. The claim that "higher MIRA scores consistently align with better global detection performance" is purely ordinal — a practitioner cannot tell what constitutes a "good" MIRA score, and the scores are not comparable across architectures or data modalities without domain-specific calibration.

### Trivial

None.

## Nice-to-Haves

- **Add statistical correlation measures.** Even with 4–5 models per domain, reporting Spearman's rank correlation (with a caveat on sample size) would be more informative than purely qualitative alignment claims.
- **Validate on actual error detection.** Using synthetic perturbations or natural misclassification examples (e.g., CIFAR-10-C corruptions causing errors, or ID misclassifications) would directly test the stated goal of the paper.
- **Normalize MIRA across layers/domains** to make the absolute scale interpretable, e.g., by dividing by the layer dimensionality or by the average intra-class distance.
- **Justify the choice of OoD detection as a proxy** more carefully, including a discussion of when OoD detection performance might diverge from error detection capability.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. *"Perturbation setup and MIRA Score computation are underspecified in the main paper, hampering reproducibility."* — The critic's concerns about ε_min/ε_max selection, p(ε) specification, and integral discretization are all addressed in the appendix (stripped by the parser) and the publicly available code. Per the hard rules, missing appendix details and implementation-level reproducibility nitpicks are removed. The code is cited in the paper.

2. *"The paper does not compare MIRA to simpler baselines like predictive entropy or max softmax confidence."* — These are runtime detection methods that require OoD data at test time, making them apples-to-oranges comparisons with a pre-deployment metric. The relevant comparison (to other *pre-deployment* feature-quality metrics) is retained as a Minor weakness above.

3. *"Missing related works about feature quality metrics (silhouette score, class separability)."* — Per the hard rules, missing related works are not pointed out. The suggestion to compare against these metrics as baselines is retained in the Minor weaknesses.

4. *"The formal definition of monitorability is a strength."* — Removed because it conflicts with the verified weakness that the definition is tautological. When a strength and a verified weakness disagree, the weakness wins.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the formal definition.** Replace the tautological Definition 1 with a non-trivial notion — e.g., require Z^l to be a simple set (a Mahalanobis ball, a half-space, or a set of bounded VC-dimension) and define monitorability as the existence of a *simple* separator for which the equivalence holds with a quantifiable margin. Then connect MIRA to this definition by showing that MIRA estimates the quality of the best such separator.
2. **Validate on error detection directly.** Include experiments where models make errors on ID inputs (e.g., via label noise, harder test samples, or natural corruptions) and test whether MIRA predicts the detectability of those errors, not just OoD detection.
3. **Report quantitative correlation.** Compute Spearman's rank correlation between MIRA scores and average OoD AUROC across the models in each domain, even if the sample size is small. This would be more informative than the current qualitative claim.
4. **Provide a calibrated scale.** Normalize MIRA scores (e.g., by the chi-squared expectation for the layer dimension) or provide a reference interpretation so practitioners can assign meaning to absolute values.

## Score and Decision

I calibrated the score against human-reviewed anchors from the DeepReview corpus using a two-round procedure.

**Round 1 (bracketing):** Three queries targeting papers on monitorability, OoD detection, and feature-space metrics, split into bands (0–3.5, 3.5–7.5, 7.5+). The paper is not in the weak band (2–3 papers like "Metanetwork" (2.5) or "Feature-Based Analysis of ToM" (2.0), which are clearly rejected with weak contributions) nor in the strong band (8.0 papers like "Comparing noisy neural population dynamics" which have rigorous theoretical or empirical validation). Initial bracket: 3.5–7.5.

**Round 2 (narrowing):** Queries in the 4.0–6.0 and 5.5–7.0 bands. Read full reviews of four anchors:
- **Gradient norm as a powerful proxy to OOD error estimation** (5.50, Reject): Similar structure (proposing a metric, validating via OOD). That paper had a clear non-vacuous problem definition and more extensive experiments, but was criticized for insufficient novelty. Our paper has a more novel concept but a weaker formalization. Comparable or slightly weaker.
- **NC-OOD** (4.50, Reject): Limited novelty (applying neural collapse to OOD). Our paper is more novel and has broader domain evaluation. Slightly stronger.
- **Double Descent Meets OOD Detection** (6.50, Reject): Strong theoretical contribution (RMT bounds) and comprehensive experiments. Our paper is significantly weaker theoretically.
- **Pursuing Feature Separation based on NC** (6.75, Accept): Strong empirical validation, rigorous experiments. Our paper is weaker in both empirical rigor and theoretical substance.

The paper sits between the 4.5 and 5.5 anchors — more novel than NC-OOD but with a weaker formalization and validation gap than the GradNorm paper. The two verified Major weaknesses (vacuous definition, validation proxy gap) prevent a higher score.

**Final score: 5.0. Decision: Reject.**

The paper introduces a genuinely interesting concept (monitorability as a pre-deployment property) and the MIRA metric is a reasonable first attempt at quantifying it. However, the formal definition is tautological and does not provide the claimed theoretical grounding, and the validation relies on a proxy (OoD detection) that is not connected to the paper's stated goal (error detection) with any statistical evidence. These issues are structural rather than cosmetic — they affect the core claims of the paper — and would require substantial revisions to address.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
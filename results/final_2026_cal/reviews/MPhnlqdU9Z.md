Now I have good calibration. Let me compile the final review.

**Bracket determination (Round 1):** Weak anchors in the 2.5–3.2 range (rejected papers with significant flaws), middle anchors 4.0–6.0 (mixed decisions), strong anchors 8.0+ (clearly top papers). This paper sits between 3.5 and 6.0.

**Round 2 narrowing:** The most comparable anchor is "Dissecting Mahalanobis" (avg 4.29) — an empirical analysis paper with interesting geometric insights but limited theoretical grounding and methodological concerns. Another comparable anchor is "Diagnosing Generalization Failures from Representational Geometry Markers" (avg 6.00) — accepted poster with broad experiments and clear framing but also some concerns about scope and methodology. The MIRA paper is well below the 6.00 anchor in theoretical rigor and validation completeness, but comparable to or slightly above the 4.29 anchor in breadth of experiments (cross-modal vs. vision-only). Final score: **4.5**.

---

## Summary

This paper introduces *monitorability* — the intrinsic property of a neural network to have its errors detectable from internal features — and proposes the MIRA Score, a practical metric that quantifies this property using only in-distribution data and FGSM perturbations. The MIRA Score is evaluated across vision (CIFAR-10/100), tabular (Sensorless Drive), and NLP (SST-2 finetuning) modalities, and its ranking of architectures is qualitatively compared against the best achievable OoD detection AUROC across three detectors (ODIN, Mahalanobis, Energy). The core empirical finding is that models with higher MIRA scores tend to have higher OoD detection performance.

## Strengths

- **A practical, pre-deployment metric for monitoring potential (MIRA Score).** The MIRA Score is computationally efficient (FGSM perturbations + Mahalanobis distance on penultimate-layer features), does not require external OoD data, and can be computed before deployment. This fills a genuine practical gap: practitioners lack tools to compare how "monitorable" different architectures are without running expensive OoD detection evaluations.

- **Cross-modal validation across three data modalities.** The experiments span vision (CNN, DenseNet, ViT, CustomNet), tabular (MLPs, Transformers), and NLP (RoBERTa, DistilBERT, ELECTRA, DeBERTaV3). This breadth is unusual for a metrics paper and supports the claim that MIRA captures a general property rather than a vision-specific artifact.

- **Chi-square surprisal transform for dimension-calibrated comparison (Eq. 3).** Converting Mahalanobis distance to a survival-function-based score that is comparable across layers with different dimensionalities is a technically sound design choice, addressing a known limitation of raw Mahalanobis distances.

- **Detector-agnostic evaluation protocol.** Using the "best-of" across three fundamentally different detection methods (confidence-based, distance-based, energy-based) is a principled way to approximate the latent monitoring potential, reducing reliance on any single detector's quirks.

## Weaknesses

### Major

- **Definition 1 (monitorability) is logically vacuous and does not ground the metric.** Definition 1 states that a model is *l*-monitorable if there *exists* a set Z^l ⊆ ℝ^{n_l} such that loss ≤ ε ⟺ f^l(x) ∈ Z^l. Since Z^l can be *any* subset, one can always construct Z^l = {f^l(x) : L(f(x),y) ≤ ε} — the set of all feature vectors from inputs with acceptable loss. This set trivially exists for every model, making the definition non-restrictive. The paper acknowledges that "Z^l may be arbitrarily complex" (p. 3), which confirms the vacuity. A meaningful formalization would require constraints on Z^l (e.g., geometric simplicity, label-free constructibility, or fixed family). As written, the definition does not provide theoretical grounding; it is a restatement of the monitoring desideratum. Since the paper claims "the first formalization of monitorability," this weakness undermines a core advertised contribution.

- **The validation only covers OoD detection, not the broader error-detection scenario that motivates the paper.** The paper motivates monitorability by stating it captures "the intrinsic ability of a model to be monitored using accessible features, **even when misclassifications occur on ID inputs**" (p. 3). Yet every experiment validates MIRA against OoD detection AUROC only. The paper explicitly acknowledges that ID misclassifications "is a distinct scenario not directly addressed by OoD detection" (p. 2). This creates a gap between the motivating problem (general error detectability, including ID boundary errors) and the evidence (OoD distributional-shift detection). The paper uses OoD detection as a "proxy" but provides no experiment showing that MIRA predicts, e.g., detection of high-confidence ID errors, label-noised inputs, or adversarial misclassifications that stay in-distribution. Until validated on ID errors, the claim that MIRA measures "monitorability" in the broad sense is unsupported.

- **No statistical correlation measure is reported.** The paper claims MIRA "correlates" with OoD detection performance (abstract, conclusion, RQ1), but no correlation coefficient (Spearman, Pearson, Kendall), confidence interval, scatter plot, or significance test is provided. The argument is purely visual/ordinal: "ViT has highest MIRA and highest AUROC; CustomNet has lowest MIRA and lowest AUROC." Within modalities, the trend is visible but not always strictly monotonic (e.g., on CIFAR-100, ResNet-18 MIRA = 0.66 and DenseNet MIRA = 2.81 have similar average AUROC). For a paper whose central validation claim is a correlation, the absence of any quantitative summary is a significant methodological gap.

### Minor

- **Perturbation-range selection is ad-hoc and lacks sensitivity analysis.** The interval [ε_min, ε_max] is set by reducing accuracy to "a certain threshold" (p. 5, details in Appendix B.6 — stripped from main text). This is a free parameter; the paper acknowledges the limitation (p. 8) but does not study how the model ranking changes under different thresholds. Without a sensitivity analysis, the metric's stability is unknown.

- **MIRA scores have a large cross-modal scale mismatch (vision: −0.07–89; NLP: 2000–3800), limiting interpretability.** The paper uses MIRA only for within-modality comparisons, which is fine, but the absolute numbers are not meaningful without reference. This weakens the claim that MIRA "quantifies" monitorability as a general property — it only provides a relative ordering within a fixed model family and dataset.

- **No ablation of MIRA's design choices.** The paper does not study the effect of using FGSM vs. random perturbations, the surprisal transform vs. raw Mahalanobis distance, or integrating over ε vs. a single ε. These ablations would strengthen the case that the specific design decisions matter.

### Trivial

- The "Average" column in the tables (e.g., Table 2) is ambiguously labeled — it appears to be the average across OoD classes for Mahalanobis only, not an average across methods. This should be clarified.

## Nice-to-Haves

- Validate MIRA against ID error detection (e.g., label-noise-induced misclassifications, high-confidence errors, or selective classification retention curves). This would close the gap between the motivation and the evidence.
- Report Spearman rank correlation with bootstrap confidence intervals for the MIRA-to-AUROC relationship across models in each modality.
- Provide a sensitivity analysis for the accuracy-threshold parameter used to set ε_min.

## Removed Points

- **Criticism that Definition 1 is "not a definition of an intrinsic property" — it's a restatement of the monitoring problem:** Retained as Major weakness (see above). However, the specific framing "fatal" is softened: the MIRA metric itself is not invalidated by the weak definition; the definition simply does not do the advertised theoretical work.
- **Criticism that the t-SNE shows ID vs. OoD separation, not correct vs. erroneous ID features:** Removed. The paper explicitly uses OoD detection as a proxy, so showing ID vs. OoD separation in t-SNE is consistent with the validation protocol. This is not a concealed flaw.
- **Criticism about missing related work on predictive uncertainty, Bayesian NNs, selective classification:** Removed. No external sources to confirm these are missing; the related work section covers OoD detection and activation-pattern monitoring, which are the directly relevant subfields. This is a scope-not-covered critique.
- **Criticism that FGSM perturbations don't guarantee movement toward the decision boundary:** Removed. The paper states FGSM is chosen for efficiency and that the perturbation "can be arbitrary as long as it moves x toward the decision boundary" — this is acknowledged as a design choice, not a hidden flaw. The paper doesn't claim optimal direction.
- **Criticism about no comparison to simpler baselines (average Mahalanobis distance ratio, spectral norm of Jacobian):** Removed. The paper's goal is to propose and validate MIRA, not to exhaustively compare against every candidate intrinsic metric. This is a scope-expansion request.
- **Criticism about the definition not imposing constraints on Z^l's complexity (would require formal verification, etc.):** Partially retained in the Major weakness above, but the demand for specific constraint types is scope-creep and moved here.
- **Strength about "formal definition of monitorability" (Strength Finder #1):** Removed. As verified, the definition is vacuous, so calling it a strength is misleading. The paper's contribution lies in the MIRA metric, not the formal definition.
- **Strength about "consistent cross-modal correlation" being strong evidence:** Weakened. The qualitative trend is visible, but without statistical measures it's not "strong evidence." Retained but caveated.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the definition.** Either replace Definition 1 with a non-vacuous characterization (e.g., define monitorability as the best achievable detection AUROC from a restricted family of monitors using only internal features) or drop the "theoretical grounding" claim and present MIRA as a heuristic metric, which is what it actually is.
2. **Validate on ID error detection.** Add at least one experiment showing that MIRA predicts which models allow better detection of naturally occurring or simulated ID misclassifications (e.g., comparing models on selective classification retention curves, or detecting label-noise-induced errors).
3. **Report Spearman's rank correlation** with confidence intervals across models for each modality. This is standard practice for validating a proxy measure and would substantially strengthen the empirical claims.
4. **Add ablation studies** comparing FGSM vs. random perturbations, the surprisal transform vs. raw Mahalanobis, and the integrated score vs. single-ε scores.
5. **Study sensitivity** of the model ranking to the accuracy-threshold parameter used to select ε_min.

## Score and Decision

**Round 1 bracketing:** Three queries retrieved anchors with average scores of 2.5–3.2 (weak band), 4.0–6.0 (middle band), and 8.0+ (strong band). This paper sits between the weak and middle bands. **Initial bracket: 4–6.**

**Round 2 narrowing:** Read anchors including "Dissecting Mahalanobis" (4.29, withdrawn/reject) — similar empirical-analysis paper with limitations in theoretical grounding and method validation — and "Diagnosing Generalization Failures from Representational Geometry Markers" (6.00, accepted poster) — broader empirical framing and stronger related-work grounding. The MIRA paper is below the 6.00 anchor in theoretical rigor (vacuous definition vs. substantive geometric analysis) and validation completeness (no correlation stats, no ID-error validation). It is comparable to the 4.29 anchor in the quality of its empirical contribution, but slightly above it in breadth (cross-modal vs. vision-only). **Final score: 4.5.**

This paper introduces a genuinely useful practical idea (MIRA) with cross-modal supporting evidence, but it is undermined by a vacuous formal definition (the "theoretical grounding" claim is not substantiated), a mismatch between the motivating problem (general error detection including ID errors) and the validation (OoD detection only), and the absence of a statistical correlation measure. The contribution is promising but incomplete as presented.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
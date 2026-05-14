Now I have thoroughly reviewed the paper, verified all claims against the text, and read the calibration anchors. Here is my consolidated review.

---

## Summary

This paper introduces *monitorability* — a neural network's intrinsic ability to support runtime error detection through its internal activations — and proposes the MIRA Score, a metric that quantifies this property using norm-bounded FGSM input perturbations and Mahalanobis-distance-based surprisal, requiring only in-distribution data. Experiments across three modalities (vision, tabular, NLP) and eight architectures compare MIRA against OoD detection AUROC as a validation proxy.

## Strengths

- **Novel conceptual contribution.** The paper is the first to formalize monitorability as a distinct property of neural networks separate from accuracy or OoD detection capability itself. The framing — that models with identical accuracy can differ substantially in how detectable their errors are — is well-motivated and practically relevant.

- **Practical and efficient metric.** MIRA requires only ID data and cheap FGSM perturbations, avoiding the expense of running multiple OoD detectors across multiple OoD datasets. This makes it a plausible pre-deployment model-selection tool.

- **Multi-modal evaluation across diverse architectures.** The experiments span computer vision (CNNs, ViT), tabular data (MLPs, Transformers), and NLP (RoBERTa, DistilBERT, ELECTRA, DeBERTaV3), demonstrating generality of the approach.

- **Consistent ranking trends.** Across all three domains, the ordering of models by MIRA aligns with the ordering by best OoD detection AUROC. For example, ViT achieves the highest MIRA (89.25) and the best detection (~99% AUROC), while CustomNet has the lowest MIRA (−0.07) and weakest detection. This directional consistency is a genuine strength.

## Weaknesses

### Fatal
None.

### Major

1. **Validation scope mismatch with the paper's own motivation.** The paper motivates monitorability as covering all sources of error, including misclassifications on in-distribution inputs (Section 3.1: "even when misclassifications occur on ID inputs"). Yet validation is conducted exclusively using OoD detection as a proxy. The paper never tests whether MIRA correlates with the detectability of ID errors — e.g., from small-norm adversarial perturbations, label noise, or naturally occurring ID misclassifications. Without this, the core claim that MIRA measures "monitorability" broadly (as opposed to "OoD-detection-support" specifically) is only partially supported. This is the most consequential gap.

2. **No quantitative correlation analysis and no baselines.** The claimed "good correlation" is supported only by qualitative eyeballing of tables. No Spearman or Pearson correlation coefficients or p-values are reported. The paper also does not compare MIRA against trivial model-level statistics (ID accuracy, feature dimensionality, feature norm, confidence entropy/ECE, parameter count). Without these, it is unclear whether MIRA provides information beyond what simpler metrics already capture. For instance, ViT's high MIRA could simply reflect that it has better learned features, which would also manifest in its high accuracy and low confidence entropy.

3. **No aggregated per-model detection metric for direct comparison.** The paper reports per-method average AUROCs but does not compute a single "best achievable detection" number per model that can be quantitatively compared to MIRA. The reader must manually compare MIRA against the best of the three per-method averages by scanning tables. Computing max per-method average AUROC per model and reporting its rank correlation with MIRA would be straightforward and would substantially strengthen the claims.

### Minor

1. **Disconnect between Definition 1 and the MIRA Score.** The formal definition (exact equivalence between a loss threshold and membership in a feature-space set Z^l) is presented as a contribution, but MIRA does not operationalize it — no theorem, bound, or argument links the metric to the existence of such a Z^l. The paper acknowledges this ("Definition 1 provides an abstract formalization"), but the gap weakens the "first formalization" claim. This is a missed opportunity to ground the metric theoretically.

2. **Perturbation parameters not ablated.** The ε_min threshold (the "certain threshold" on accuracy), the choice of p(ε) distribution (uniform vs. weighted), the discretization scheme, and the fraction of FGSM perturbations that actually cross the decision boundary are all unevaluated. The paper acknowledges the perturbation range as a limitation, but without *any* sensitivity analysis, the robustness of the metric to these choices is unknown.

3. **Correlation magnitude is noisy.** For NLP, RoBERTa (MIRA 2633) and DistilBERT (MIRA 2016) differ by ~30% in MIRA but have nearly identical best AUROC (77.16 vs 76.54). This suggests that MIRA's resolution beyond coarse rankings (ViT > DenseNet > CustomNet) is limited, and the correlation is not as clean as the paper implies.

4. **No layer-wise evaluation despite claimed use-case.** The paper claims MIRA can guide layer selection for feature-based monitoring, but only the penultimate layer is evaluated. Demonstrating MIRA at multiple layers with corresponding detection performance would substantiate this claimed application.

5. **MIRA scores are not interpretable across domains/architectures.** Scores range from −0.07 (CustomNet) to 3793.61 (DeBERTaV3) with no calibration or bounded scale. Practitioners have no sense of what constitutes a "good" score, which limits practical adoption.

### Trivial

- The notation S_0 = 𝔼_{x∼D}[S(f^l(x))] leaves it unspecified whether the Mahalanobis distance is computed per-class or globally; this should be clarified.

## Nice-to-Haves

- Validation on ID misclassifications (adversarial examples within ℓ_p ball, label noise) to close the scope gap.
- Spearman correlation between MIRA and max per-method average AUROC, with p-values.
- Comparison against baselines: ID accuracy, feature norm, confidence ECE, parameter count.
- Sensitivity analysis of ε_min threshold and p(ε) choice.
- Layer-wise MIRA computed for at least one dataset.

## Removed Points

These points are flagged to be removed; treat them with caution.

- "Architectures only in appendix" — Parser-stripped content; not a valid criticism of the submission as-is.
- "Lee et al. (2018a) may be mis-cited" — Per policy, all cited references are assumed to exist and be correctly cited.
- "FGSM may not cross the decision boundary" — The paper states perturbations move inputs "toward the decision boundary, potentially crossing it" (line 93), which does not require crossing.
- "Toy example has only two ID classes" — This is presented as an illustrative motivation, not as evidence of generalization.
- "Missing appendix content" — Parser artifact; not a valid criticism.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add an experiment using ID data with injected label noise or small-norm adversarial (PGD) perturbations. Measure whether MIRA predicts the AUROC of detecting these ID errors.
2. Compute Spearman rank correlation between MIRA and max per-method average AUROC for each domain. Report p-values and compare against baselines.
3. Compare MIRA against ID accuracy, feature norm, and ECE as alternative model-level predictors of detection performance.
4. Perform a sensitivity analysis: vary the "certain threshold" for ε_min (e.g., 70%–95% accuracy retention), use different p(ε) weighting schemes, and report whether model rankings remain stable.
5. Compute MIRA at multiple layers (early, middle, penultimate) for CIFAR-10 models and compare with detection AUROC at those same layers.
6. More clearly acknowledge in the conclusion that validation covers only OoD detection and that ID error detection remains future work.

## Score and Decision

I compare the paper under review against the retrieved anchors:

| Anchor Path | Avg Score | Comparison |
|---|---|---|
| `cuEyUONHC7` (Data-Free Metrics) | 3.33 | Similar domain (metrics for network properties); our paper has a stronger positive contribution but weaker methodology than that paper's thorough experiments |
| `9gvUS0ewHm` (Fair OOD Detection) | 3.50 | Similar domain (OOD detection); our paper has a more novel conceptual contribution |
| `7Mbz5uSf2J` (Decoupling Dynamical Richness) | 6.00 | Most comparable anchor — both propose a metric for a network property. That paper has stronger theoretical grounding (connection to neural collapse), thorough baselines, and quantitative correlation analysis. Our paper is weaker on all three dimensions. |
| `pODHH9DLeA` (Readout Representation) | 6.00 | Accepted despite significant weaknesses; our paper has more substantive evidential gaps in validation |
| `LxiEOSKyYN` (Conformal Reliability) | 4.00 | Similar contribution type (new evaluation metric); our paper has broader scope but less rigorous validation |
| `ptfu9Pr3dk` (Symmetries in Weight Space) | 4.00 | Purely theoretical; our paper is more empirical but less rigorous |
| `Pjcz6ik78E` (Subspace Clustering) | 4.67 | Accepted (Poster) with bimodal scores; our paper has comparable conceptual novelty but less complete validation |
| `VKGTGGcwl6` (LLMs Multi-Turn) | 8.00 | Far stronger in experimental design, thoroughness, and clarity; not directly comparable |

The paper has a genuinely novel idea and a practical metric with plausible cross-domain trends. However, the validation is significantly incomplete relative to the claims: the scope gap between broad motivation (all errors) and narrow validation (only OoD detection), the absence of any quantitative correlation analysis or baseline comparisons, and the lack of ablation on key design choices all prevent the paper from meeting the acceptance bar in its current form. With substantial additional validation (ID error experiments, quantitative correlation, baseline comparisons, sensitivity analysis), the paper could become a strong submission.

**Score:** 4.5

**Decision:** Reject

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
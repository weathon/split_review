Now I have sufficient calibration data. Let me synthesize the final review.

**Round 1 bracket:** I determined the paper sits in the 4–6 range.

**Round 2 anchors read in full:**
1. "Model Cautiousness" (3.75, Reject) — weaker: circular evaluation, unclear motivation.
2. "Pathologies of OOD Detection" (4.75, Reject) — comparable quality but less novel (critique paper vs. new metric).
3. "Detecting OOD with Neural Collapse" (4.50, Reject) — comparable quality but less novel (another OOD detector).  
4. "MD-LSM" (6.00, Reject) — more theoretical depth, similar experimental gaps.

Our paper is stronger than 3.75–4.75 papers due to genuine novelty (first formalization of monitorability) and cross-modal experiments, but weaker than 6.0 papers due to validation gaps and lack of sensitivity analysis. **Final score: 5.0.**

Now let me write the complete review.

## Summary
2-3 sentence summary

## Strengths
List strengths

## Weaknesses
Organized by severity

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me draft this carefully.## Summary

This paper introduces *monitorability* — the intrinsic ability of a neural network to have its inference errors detected from internal activations — and proposes the MIRA Score, a practical metric that quantifies this property by perturbing in-distribution inputs and measuring feature-space separability via Mahalanobis-based surprisal. The metric is evaluated across vision (CIFAR-10/100), tabular (Sensorless Drive), and NLP (SST-2) domains, where MIRA scores qualitatively align with OoD detection AUROC. The paper claims to be the first formalization and quantitative measure of monitorability.

## Strengths

1. **First formalization of monitorability.** The paper provides a clean definition of monitorability (Definition 1) and derives a practical, architecture-independent metric (MIRA). There is no existing work that formally defines or quantifies this property, making the conceptual contribution genuinely novel. The toy example in Figure 1 effectively grounds the intuition.

2. **Cross-modal experimental coverage.** Experiments span three distinct data modalities — vision, tabular, and NLP — with diverse architectures (CNNs, ViTs, MLPs, Transformers, BERT-family models). This breadth demonstrates that MIRA is not narrowly tailored to a single domain and supports the generality claim.

3. **Sensible metric design.** MIRA's design (FGSM perturbation → Mahalanobis distance in feature space → chi-square surprisal → integration over perturbation magnitudes) is principled: it probes local boundary behavior using only ID data, requires no OoD examples, and the surprisal transformation provides dimension-calibrated scores. The fact that MIRA can be computed pre-deployment without external OoD datasets is a practical advantage.

4. **Qualitative consistency with t-SNE visualizations.** Figure 2 shows that higher MIRA scores correspond to better-organized feature spaces (e.g., ViT's compact clusters vs. CustomNet's overlap), providing intuitive structural evidence that the metric captures something meaningful about feature-space geometry.

## Weaknesses

### Major

1. **Validation scope mismatch with the definition of monitorability.** Monitorability is defined broadly as the ability to detect *any* inference error, including misclassifications on in-distribution inputs (Section 3.1: "even when misclassifications occur on ID inputs"). The paper itself acknowledges (Section 2) that "misclassifications may also occur for ID inputs, which is a distinct scenario not directly addressed by OoD detection." Yet the experimental validation uses *only* OoD detection performance as a proxy. No experiment tests whether MIRA correlates with detection of ID misclassifications (e.g., via adversarial examples, natural corruptions, or hard ID samples that the model misclassifies). This gap between the definition's scope and the validation undermines the central claim that MIRA measures monitorability *as defined*. The metric may still be useful for OoD-related monitoring, but the paper does not establish the broader claim.

2. **No sensitivity analysis for MIRA's free parameters.** The MIRA score depends on several design choices: the perturbation method (FGSM exclusively), the ε-interval selection rule (accuracy-drop threshold + ε\_max = 2·ε\_min heuristic), the uniform distribution p(ε), and the choice of the penultimate layer. The paper provides no ablation or sensitivity study showing whether the model ranking is stable under these variations. If the relative ordering of models changes with, e.g., a different attack (PGD) or a different accuracy-drop threshold, the metric cannot be relied upon for model selection. The paper acknowledges the perturbation range as a limitation in the conclusion, but this does not substitute for empirical analysis.

3. **Potential confound with the Mahalanobis-based detector.** MIRA uses Mahalanobis distance internally, and in almost every experiment the Mahalanobis-based detector (Lee et al., 2018b) is the best-performing method (dominant in Tables 2 and 3 for tabular and NLP; often best in Table 1 for vision). This raises the concern that MIRA's correlation with "best AUROC" largely reflects self-consistency between two Mahalanobis-based quantities rather than a detector-agnostic measure of monitorability. The paper does not discuss this confound or separately analyze whether MIRA correlates equally well with non-Mahalanobis detectors when they are the best method. Some evidence in Table 1 partially mitigates this (e.g., DenseNet on CIFAR-10 where ODIN sometimes outperforms Mahalanobis), but the issue needs explicit discussion and analysis.

### Minor

4. **No quantitative correlation measure.** The paper relies entirely on qualitative inspection of tables to assert that MIRA "consistently aligns" with OoD detection performance. With only 13 models across three domains, reporting Spearman rank correlations with confidence intervals would be straightforward. The absence of any statistical measure leaves the central empirical claim unquantified. The paper should also show per-detector correlations, not just "best AUROC."

5. **Limited model count per domain.** With 4 vision models (across 2 datasets), 5 tabular models, and 4 NLP models, the apparent monotonic relationship may be disproportionately driven by the extreme points (high-capacity ViT and low-capacity CustomNet). A broader model zoo — varying capacity, architecture family, and training procedure within each domain — would provide stronger evidence for the claimed correlation.

### Trivial

6. The t-SNE visualization in Figure 2 uses 10 ID class colors plus 7 OoD dataset markers in a single legend, making the plot very difficult to parse. Simpler per-model side-by-side panels contrasting ID vs. OoD activation distributions would be more informative.

## Nice-to-Haves

- Comparison with alternative perturbation methods (e.g., PGD, random noise) to test whether the adversarial direction toward the boundary is necessary, or whether random perturbations suffice.
- Analysis of MIRA computed at different layers, not just the penultimate layer, to justify the layer choice empirically.
- Reporting wall-clock time or forward-pass counts to substantiate the efficiency claim in RQ4.
- A brief discussion of when the Gaussian (GDA) assumption underlying Mahalanobis distance may break down and how that would affect MIRA.

## Removed Points

These points were raised by the reviewers but are removed per consolidation guidelines (parser-stripped appendix content, presentation nitpicks, or factually incorrect critiques):

- "Implementation details (number of ε values, integral approximation) are not specified" — These are in Appendix B.6, which was stripped by the parser.
- "The choice of ε\_min threshold is vague" — Detailed in Appendix B.6.
- "The column labelled Average is ambiguously defined" — Presentational issue, not a substantive flaw.
- "Definition 1 is never used in the paper" — The paper states it is an abstract formalization; the metric is a practical approximation. The disconnect is explicitly acknowledged.
- Typos, formatting artifacts, and parser-related issues — Per guidelines, these are not author errors.
- "Missing related works" — Per guidelines, the reviewer cannot confirm existence of missing references.
- "Reproducibility concerns about undisclosed hyperparameters" — Standard details likely in the appendix (stripped).

## Novel Insights

The reviews surface a tension between the paper's ambitious definition of monitorability (covering all inference errors) and its narrow proxy validation (OoD detection only). A genuinely novel observation is that MIRA's reliance on Mahalanobis distance creates a potential methodological circularity when validation also privileges Mahalanobis-based detectors — a confound the paper should address explicitly, not simply by averaging over three detectors. The cross-modal validation is a genuine differentiator from most OoD-focused work, but without sensitivity analysis or quantitative correlation measures, the evidence for MIRA as a general-purpose monitorability metric remains incomplete.

## Suggestions

1. **Align evaluation with the definition:** Test MIRA against detection of ID misclassifications — for instance, using adversarial examples on ID data, naturally hard ID samples, or common corruptions. This would directly address the scope mismatch between the definition and the validation.

2. **Add systematic sensitivity analysis:** Vary the perturbation method (FGSM → PGD, random noise), the ε-interval rule (different accuracy-drop thresholds), and the layer choice. Show that the relative ordering of models is stable under these variations. Without this, MIRA's reliability as a model selection tool is unsubstantiated.

3. **Report Spearman rank correlations** (with p-values and confidence intervals) between MIRA and per-detector AUROC across all models. Include scatter plots and separate analyses for each of the three detectors (ODIN, Mahalanobis, Energy) to address the confound concern.

4. **Discuss the Mahalanobis confound explicitly.** Show that MIRA correlates with non-Mahalanobis detectors' performance separately, or explain why the confound is less severe than it appears (e.g., by pointing to instances where non-Mahalanobis detectors are competitive and the correlation still holds).

## Score and Decision

**Calibration anchors (all rounds):**

| Anchor | Avg Score | Decision | Round | Comparison to this paper |
|--------|-----------|----------|-------|------------------------|
| Model Cautiousness (yNZi38u52U) | 3.75 | Reject | R2 | Weaker: circular evaluation, less grounded motivation |
| HAct OOD (Oo5spZRpH6) | 3.67 | Reject | R2 | Weaker: incremental OOD method, less novelty |
| Detecting OOD with Neural Collapse (VAmVEghgoC) | 4.50 | Reject | R2 | Comparable quality but less novel (another OOD detector vs. new concept) |
| Pathologies of OOD Detection (hlijRgXTDK) | 4.75 | Reject | R2 | Comparable quality but critique paper with no new method |
| MD-LSM (hoEanaoP4i) | 6.00 | Reject | R2 | Stronger theory, similar experimental gaps; our paper has broader modality coverage |
| Double Descent Meets OOD (eN0RyRVbSm) | 6.50 | Reject | R1 | Stronger theory + experiments on model complexity/OOD |
| Deep NNs Extrapolate Predictably (ljwoQ3cvQh) | 7.00 | Accept | R1 | Stronger: comprehensive empirical study on OOD behavior |

**Round 1 bracket:** 4–6 (based on middle-band anchors scoring 4.50–7.00 being most topically relevant).

**Round 2 narrowing:** Read 4 anchors in full. Our paper is clearly stronger than the 3.67–4.75 papers due to genuine novelty (first monitorability definition + metric) and cross-modal validation. It is weaker than the 6.00–6.50 papers due to missing sensitivity analysis, absence of quantitative correlation measures, and the validation scope gap.

**Final score: 5.0.** The paper introduces a novel and well-motivated concept with a sensible metric, but the experimental validation has significant gaps that prevent the central claims from being fully supported. The scope mismatch between the definition and validation, combined with the absence of sensitivity analysis and quantitative correlation measures, means the paper requires major revision before its claims are convincing.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
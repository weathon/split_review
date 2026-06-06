## Summary
The paper introduces *monitorability* as a formally defined, intrinsic property of neural networks — capturing the degree to which a model's internal activations can distinguish correct from erroneous predictions — and proposes the MIRA Score, a continuous metric that quantifies this property using only in-distribution data and norm-bounded FGSM perturbations. MIRA is evaluated across vision (CIFAR-10/100), tabular, and NLP domains, and is validated by correlating against the best achievable OoD detection performance across three detection methods (ODIN, Mahalanobis, Energy).

---

## Strengths

- **Novel concept, well-motivated.** The notion of monitorability as an intrinsic property, separate from both accuracy and from the performance of any particular OoD detector, is genuinely new. The toy dataset in Figure 1 makes the intuition crisp: two architectures can achieve identical classification accuracy while differing dramatically in how separable their feature spaces are for OoD inputs. This motivates the whole contribution without relying on abstract formalism alone.

- **No external OoD data required.** MIRA is computed entirely from in-distribution samples and efficient FGSM perturbations, making it usable pre-deployment for model selection. This is a concrete practical advantage over grid-searching over multiple OoD detectors and external datasets.

- **Consistent qualitative ordering across three modalities.** The MIRA ranking of models matches the best-of AUROC ranking in all three domains (Tables 1–3): ViT > DenseNet > ResNet-18 > CustomNet in vision; WideMLP outperforms DeepTransformer in tabular; DeBERTaV3 > ELECTRA > RoBERTa > DistilBERT in NLP. The ordering holds even in cases where Mahalanobis is *not* the best detector (e.g., CustomNet on CIFAR-10 where ODIN/Energy substantially outperform Mahalanobis yet MIRA still correctly flags CustomNet as the least monitorable).

- **Feature-space visualizations (Figure 2).** The t-SNE projections directly reinforce the quantitative claims: ViT shows tight, well-separated clusters; CustomNet shows nearly complete overlap. This provides an interpretable, detector-independent check on what MIRA is measuring.

---

## Weaknesses

### Fatal
None.

### Major

- **Mathematical error in the threshold condition of Definition 1.** Definition 1 (lines 71–72) states that for cross-entropy loss, the condition "L(f(x), y) ≤ ε implies a correct prediction" requires "ε < log(C)." Concretely: L = −log(p_y) ≤ ε < log(C) implies p_y > 1/C, meaning the true class has above-chance softmax probability — but this does **not** guarantee that the argmax is y. For C ≥ 3, a competing class can hold probability ≫ 1/C while the true class holds slightly above 1/C, so argmax ≠ y is perfectly possible. The condition is stated without proof and is incorrect as written for any C ≥ 3. Because this condition is the only formal link between "loss ≤ ε" and "correct prediction" in Definition 1, its falsity undermines the stated precision of the theoretical grounding. (A correct condition for classification correctness would require, e.g., p_y > 1 − 1/C or a different formulation.)

- **Partially circular validation.** MIRA is constructed via Mahalanobis-based surprisal (Eq. 3–4). The evaluation proxy is the *maximum* AUROC across three detectors, and Mahalanobis detection wins (bolded) in the majority of per-cell comparisons across Tables 1–3 — especially in tabular (Table 2, where Mahalanobis dominates every model-class column) and NLP (Table 3, where Mahalanobis is best across all cells). As a result, the "best-of" aggregate is frequently Mahalanobis performance, and the demonstrated correlation between MIRA and the proxy is at least partially explained by shared mathematical structure rather than by the breadth of the monitorability concept. The paper does show that the ordering holds even when Mahalanobis is not the best detector (e.g., CustomNet on CIFAR-10), which partially mitigates this, but the concern is not fully resolved or acknowledged.

- **Gap between binary Definition 1 and continuous MIRA not formally bridged.** The paper itself acknowledges (Section 3.3) that "Definition 1 provides an abstract formalization of monitorability, but it does not quantify how monitorable a neural network is." However, no proposition, theorem, or even informal argument is provided to show that a higher MIRA implies "more monitorable" in any rigorous sense tied to Definition 1. A model with MIRA = 89 vs. MIRA = 6 — does one satisfy Definition 1 more tightly, or with a smaller ε, or with a simpler Z^l? The current paper leaves Definition 1 as philosophical motivation with no formal connection to the metric, which weakens the claim of providing "theoretical grounding."

### Minor

- **No quantitative correlation statistics.** The "correlation" claim is supported only by visual inspection of rankings across 4–5 models per domain. No Spearman rank correlation, Kendall τ, or any other statistic is reported. With small N, qualitative ordering could be coincidence, and a simple proxy like "model capacity" (ViT > DenseNet > ResNet) could yield the same rank. Even a per-domain Spearman coefficient would let readers judge the strength of the relationship rather than relying on visual inspection.

- **MIRA scale diverges dramatically across domains.** Vision MIRA ranges from −0.07 to 89; tabular from 4 to 63; NLP from 2015 to 3793. The chi-square surprisal normalization (Section 3.3) is designed to remove dimension dependence, but the NLP scores are ~40× larger than vision scores. The paper notes that "MIRA is not directly comparable across layers with different dimensionalities," but offers no explanation for this domain-level divergence. This limits the claim that MIRA is a unified, domain-independent metric.

- **CIFAR-100 missing CustomNet.** Table 1 includes CustomNet for CIFAR-10 but not for CIFAR-100, reducing the model set to three without explanation. This asymmetry weakens the CIFAR-100 comparison.

### Trivial
None.

---

## Nice-to-Haves

- **Disentangle MIRA from Mahalanobis in the evaluation.** Repeating the validation using only ODIN and Energy-based scoring as the proxy would demonstrate that MIRA generalizes beyond its own mathematical family — this is the single highest-leverage experiment for addressing the circularity concern.
- **Quantitative Spearman/Kendall correlation analysis.** The AUROC values in Tables 1–3 are sufficient to compute these; this is low-cost and would substantially strengthen the "MIRA correlates with detection performance" headline.
- **Controlled architecture experiment.** Comparing models trained with the same architecture but different regularization or training objectives — where monitorability may vary while model capacity is held constant — would more convincingly isolate monitorability as a distinct property from general representational quality.
- **Newer OoD detection baselines.** Including KNN- or GradNorm-based detectors would broaden the proxy and reduce the influence of any single mathematical family.

---

## Removed Points
*These points are flagged to be removed — treat them with caution.*

- **Harsh Critic — "DenseNet/RQ3 argument needs tightening":** The critic argues that a Mahalanobis-based MIRA cannot be "detector-agnostic" relative to Mahalanobis detection. But the paper's RQ3 example (Section 4.4) specifically shows Mahalanobis OoD *detector* failing on Places365 for DenseNet while ODIN/Energy still perform well — the claim is that MIRA's overall high score for DenseNet is vindicated by non-Mahalanobis detectors, not the Mahalanobis detector. The critic misread the argument's direction. REMOVED as a misread.

- **Harsh Critic — "Perturbation range calibration is non-comparable":** ε_min varies per model and ε_max = 2·ε_min is a heuristic. The critic argues this makes MIRA scores non-comparable across models. However, the paper explicitly describes a "consistent strategy" using a fixed accuracy threshold across all compared models (Section 4.2, Appendix B.6). The paper acknowledges this as a limitation in Section 6. Because it is already acknowledged and Appendix B.6 details the standardization procedure (stripped by the parser), this is demoted from a structural concern to an acknowledged limitation, handled as a nice-to-have.

- **Strength Finder — "Formal definition is a core strength":** Retained as a strength, but conditioned on the mathematical error in the threshold condition being a real counterweight.

---

## Novel Insights

The most interesting observation that emerges from cross-reading the reviews and the paper is the *conflict between MIRA's purpose and its evaluation*: MIRA is designed to be detector-agnostic, but because it is Mahalanobis-based and the best-of proxy is Mahalanobis-dominated in most domains, the empirical validation inadvertently tests whether MIRA predicts Mahalanobis performance rather than some broader monitoring potential. The cases where this circularity breaks down — CustomNet (CIFAR-10), where ODIN/Energy substantially outperform Mahalanobis yet MIRA still correctly ranks CustomNet last — are actually the strongest empirical evidence for MIRA as an independent concept, and the paper would benefit from foregrounding those cases rather than the Mahalanobis-dominated settings.

---

## Suggestions

1. **Fix the threshold condition in Definition 1.** For C ≥ 3, ε < log(C) does not guarantee correct prediction. Consider replacing with a condition directly on softmax margin (e.g., p_y − max_{j≠y} p_j > 0) or explicitly restricting the claim to binary classification and generalizing it correctly for multiclass.
2. **Add Spearman rank correlations in Tables 1–3.** This is the minimal cost change that turns a qualitative ordering claim into a quantitative one.
3. **Either add a non-Mahalanobis-only evaluation proxy, or explicitly acknowledge the shared mathematical structure in Section 4.1** and argue why it does not impair validity (e.g., by pointing to the CustomNet case where Mahalanobis fails but MIRA still correctly assigns low monitorability).
4. **Explain the NLP scale discrepancy.** A brief paragraph in Section 3.3 or 4.4 addressing why NLP MIRA values are ~40× larger than vision values would clarify whether this is a known consequence of feature dimensionality or an artifact of incomplete normalization.
5. **Provide a formal or semi-formal bridge between Definition 1 and Definition 2.** Even an informal proposition — e.g., "under Gaussian assumptions, a higher MIRA implies a larger separation between the Z^l ball and its complement" — would give the metric meaningful grounding in the binary existence definition.

---

## Score and Decision

**Originality:** High. The formalization of monitorability as a distinct, intrinsic property and the design of a pre-deployment metric using only ID data is a genuinely new contribution, not found in the OoD detection or runtime monitoring literature.

**Importance:** Moderate-to-high. For safety-critical deployment, knowing before deployment whether a model's features are structured for monitoring is practically valuable.

**Claims supported:** Moderate. The empirical ordering claim is qualitatively supported but lacks statistical rigor. The "theoretical grounding" claim is weakened by the mathematical error and the missing formal link between Definition 1 and MIRA.

**Soundness:** Moderate. The metric design is reasonable, but the formal definition contains a verifiable error and the evaluation has a structural self-referential concern.

**Clarity:** Good. The paper is well-organized and the toy example is effective. The scale discrepancy and missing correlation statistics are clarity gaps.

**Community value:** Moderate-to-high. Practitioners who need to select among models for safety-critical deployment would find a pre-deployment monitorability score useful.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>
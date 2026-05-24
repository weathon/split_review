Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper introduces *monitorability* as an intrinsic property of neural networks — the extent to which a model's internal feature representations allow detection of inference errors — and proposes the MIRA Score, a metric that quantifies this property by perturbing ID inputs (via FGSM) toward the decision boundary and measuring how separable the resulting perturbed feature activations are from unperturbed ones using a dimension-calibrated Mahalanobis-based surprisal score. The paper validates MIRA by comparing it with the best achievable OoD detection AUROC (across ODIN, Mahalanobis, and Energy scoring) on vision (CIFAR-10/100), tabular (Sensorless Drive), and NLP (SST-2) tasks, showing consistent ordinal alignment between higher MIRA scores and stronger detection performance.

## Strengths

1. **Novel problem formalization.** The paper provides the first explicit definition of *monitorability* as a model-intrinsic property distinct from both runtime detection methods and standard accuracy metrics (Definition 1, Section 3.2). This conceptual contribution is timely and valuable.

2. **Cross-modal empirical validation with consistent trends.** The experiments span computer vision (CIFAR-10/100, 7 OoD datasets), tabular data (Sensorless Drive, 6 OoD classes), and NLP (SST-2, 4 OoD datasets), using diverse architectures from lightweight CNNs to ViT, MLPs, and transformer-based language models. Across all modalities, the ordinal ranking of models by MIRA Score consistently aligns with the ranking by best-attainable OoD detection AUROC — e.g., ViT (MIRA 89.25, AUROC ≈99%) vs. CustomNet (MIRA −0.07, weak detection) on CIFAR-10; DeBERTaV3 (MIRA 3793.6, best AUROC 86.29%) vs. DistilBERT (MIRA 2015.7, worst AUROC 76.54%) on SST-2. This breadth strengthens the claim that the metric captures something general about model structure.

3. **Principled dimension-calibrated metric design.** The MIRA Score converts raw Mahalanobis distance to a surprisal score via the chi-square survival function (Equation 3), making it comparable across layers with different dimensionalities. This avoids scaling artifacts that would otherwise plague cross-layer or cross-model comparisons — a practical design detail that prior feature-based metrics lack.

4. **Computationally efficient and pre-deployment friendly.** MIRA requires only ID data + cheap FGSM perturbations, avoiding the need for OoD dataset collection or expensive detector grid-searches. As the paper notes, tuning and evaluating multiple OoD detectors is substantially more expensive than computing MIRA, making it practical for model selection.

5. **Qualitative visual support (Figure 2).** t-SNE visualizations of penultimate-layer activations for CIFAR-10 models show that higher MIRA scores correspond to more compact, well-separated clusters (ViT) while lower scores correspond to entangled representations (CustomNet), providing intuitive evidence linking the metric to feature-space structure.

## Weaknesses

### Fatal

None.

### Major

1. **Validation scope gap: monitorability is defined to cover ID misclassifications, but validated only on OoD detection.** Section 3.1 defines monitorability as "the intrinsic ability of a model to be monitored using accessible features, **even when misclassifications occur on ID inputs**" (emphasis added). Section 2 explicitly notes that "misclassifications may also occur for ID inputs, which is a distinct scenario not directly addressed by OoD detection." Despite this, the entire experimental validation uses only OoD detection AUROC as a proxy for monitorability (Section 4.1). The paper does not evaluate whether MIRA correlates with the detectability of **in-distribution misclassifications** (e.g., via confidence thresholding, ensemble disagreement, or uncertainty estimation). This means a core aspect of the paper's stated definition of monitorability remains untested. The paper's central claim — that MIRA quantifies monitorability — is only partially supported by the evidence presented.

2. **Loose connection between the formal definition (Definition 1) and the proposed metric (MIRA).** Definition 1 states that a model is *l*-monitorable if there exists a set Z^l and threshold ε such that low loss is *bidirectionally equivalent* to features lying in Z^l — an extremely strong existential condition. MIRA (Definition 2) measures something qualitatively different: how separable perturbed features are from unperturbed features using Mahalanobis distance. The paper acknowledges this gap (Section 3.3: "Definition 1 provides an abstract formalization of monitorability, but it does not quantify how monitorable a neural network is. To address this, we propose a metric that **estimates** this property."), but no argument is given that MIRA lower-bounds, approximates, or is otherwise connected to Definition 1 beyond intuition. The paper frames monitorability as a formal concept backed by a definition, but the metric is designed from a separate intuition (Figure 1) and the two are not bridged. This weakens the claim of providing a *formal* measure.

### Minor

3. **No quantitative correlation statistics.** The paper claims MIRA "correlates with" or exhibits "strong correlation" with OoD detection performance (Sections 1, 4.4, 6) but provides no correlation coefficient (Spearman/Pearson), confidence intervals, or p-values. With only 4–5 models per domain, the statistical power of such a test would be limited, but the claim of correlation as stated is qualitative and the evidence is ordinal-visual rather than quantitative. For example, on CIFAR-10, ResNet-18 (MIRA 6.05) and DenseNet (MIRA 16.01) both achieve best-average AUROC around 94–95%, so MIRA distinguishes them more sharply than the proxy does — this discrepancy is not discussed.

4. **Ad-hoc perturbation range with no sensitivity analysis.** The perturbation interval [ε_min, ε_max] is determined by choosing ε_min as "the smallest value that reduces accuracy to a certain threshold" (Section 4.2) and setting ε_max = 2·ε_min. This introduces a free hyperparameter (the accuracy threshold) whose choice could affect MIRA scores and comparisons across models of varying robustness. The paper acknowledges this as a current limitation in the conclusion but does not test sensitivity to this threshold, leaving it unclear whether the MIRA rankings are robust to this design choice.

5. **No verification that perturbed inputs approach or cross the decision boundary.** The paper motivates perturbations as "mov[ing] x toward the decision boundary, potentially crossing it" (Section 3.3), but does not report what fraction of perturbed samples actually change the model's prediction or meaningfully approach the boundary. Without this check, the connection between the perturbation procedure and the "error detection" interpretation of monitorability is asserted rather than demonstrated.

### Trivial

- None.

## Nice-to-Haves

- **ID misclassification detection experiments:** Evaluate whether MIRA correlates with the ability to detect errors on ID inputs (e.g., via confidence thresholding or predictive entropy). This directly addresses the validation scope gap.
- **Perturbation diversity:** Test alternative perturbation strategies (PGD, random noise) and norms (L₂, L∞) to show that MIRA is not an artifact of the FGSM choice.
- **Formal connection sketch:** Even a brief argument showing how feature separability under perturbation relates to the existence of Z^l (from Definition 1) would strengthen the paper's theoretical framing.

## Novel Insights

The harsh critic's observation that the formal definition (existential, bidirectional) and the practical metric (separability-based) are disconnected is a genuine insight that the authors themselves partially acknowledge. A second genuine insight — not fully surfaced by either input — is that the validation gap (OoD-only vs. ID + OoD monitorability) is not just an experimental oversight but a tension with the paper's own framing: the definition of monitorability (Definition 1) quantifies over in-distribution (x,y) only, yet the metric is validated against OoD detection performance, which Definition 1 explicitly does not address. The paper's conceptual framing and its empirical framing operate on different objects without reconciliation.

## Suggestions

1. **Add ID misclassification detection experiments.** This is the most impactful improvement: show that MIRA correlates with the detectability of errors on held-out ID test inputs where the model makes mistakes. Without this, the metric's connection to "monitorability" as defined remains incomplete.

2. **Either tighten or loosen the framing around Definition 1.** Either (a) derive MIRA from Definition 1 formally (showing how it approximates or lower-bounds the existence of Z^l), or (b) reframe Definition 1 as a conceptual motivation rather than a formal definition that the metric "quantifies." The current framing invites scrutiny that the metric does not bear.

3. **Compute Spearman rank correlations** between MIRA and best-AUROC across all model/dataset pairs, acknowledging the limited N. Even a small-N correlation (with caveats) is more rigorous than the purely qualitative claim of "strong correlation."

4. **Report the fraction of perturbed samples that change prediction** for at least one architecture per modality, to verify that perturbations are meaningful.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
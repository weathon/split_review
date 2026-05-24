Now I have all the information I need. Let me construct the final consolidated review.

---

## Summary

This paper introduces *monitorability* — the intrinsic capacity of a neural network to support runtime error detection via its internal activations — and provides a formal definition (Definition 1). The authors propose the MIRA Score, a perturbation-based metric that quantifies monitorability using only in-distribution data and Mahalanobis-distance surprisal. Experiments across vision, tabular, and NLP domains compare MIRA against the best achievable OoD detection AUROC from three detectors (ODIN, Mahalanobis, Energy), showing consistent rank ordering.

## Strengths

- **Novel formalization of monitorability (Definition 1)**. The paper provides a precise, task-agnostic definition that cleanly separates monitorability from prediction accuracy, requiring only that a layer's activations can indicate prediction correctness. The toy example (Figure 1) concretely illustrates how two models with identical ID accuracy can differ substantially in how they represent anomalous inputs.

- **Principled metric design (MIRA Score, Definition 2)**. MIRA uses FGSM perturbations of ID data to probe local decision-boundary behavior and measures feature separability via a dimension-calibrated Mahalanobis-based surprisal score (Equation 3–4). The metric requires no external OoD data and is computed as an expectation over a continuous perturbation range, making it practical for pre-deployment model selection.

- **Broad cross-domain empirical coverage**. Evaluation spans CNNs (ResNet-18, DenseNet, CustomNet), Vision Transformer, multiple MLP variants, and pretrained transformers (RoBERTa, DistilBERT, ELECTRA, DeBERTaV3) across vision (CIFAR-10/100), tabular (Sensorless Drive Diagnosis), and NLP (SST-2) tasks. This breadth substantiates the claim that MIRA generalizes across fundamentally different model families and data modalities.

- **Detector-agnostic evidence**. The best-of-three evaluation protocol reveals cases where individual detectors fail (e.g., Mahalanobis achieves only 64.49 AUROC on Places365 for DenseNet CIFAR-10) yet MIRA correctly reflects the *latent* monitoring potential captured by the other detectors. This supports the claim that MIRA measures intrinsic representational quality rather than detector-specific limitations.

- **Intuitive feature-space visualizations**. t-SNE projections (Figure 2) show a clear qualitative progression from entangled CustomNet spaces to well-separated ViT clusters, providing a bridge between the numeric MIRA score and the underlying organization of learned features.

## Weaknesses

### Fatal

None.

### Major

- **Mismatch between formal definition and evaluation proxy**. Definition 1 defines monitorability in terms of detecting *incorrect predictions on in-distribution data* — it requires that a layer's activations distinguish low-loss (correct) from high-loss (incorrect) predictions for inputs drawn from P_in. However, the experiments validate MIRA against OoD detection AUROC, which answers a different question: "Is this input from a different distribution?" An OoD input can be correctly classified, and an ID input can be misclassified. The paper explicitly acknowledges OoD detection as a proxy (Section 4.1: "we use OoD detection performance as a *proxy* for monitorability"), but provides no justification for why this proxy is adequate, nor any experiment that directly tests what Definition 1 actually defines. This gap means the paper's headline claim — that MIRA measures monitorability as formally defined — is not directly supported by the evidence.

- **Correlation claims lack quantitative rigor**. Across Tables 1–3 and the Discussion, the paper repeatedly asserts that "higher MIRA scores consistently align with better global detection performance" and MIRA "exhibits good correlation" with OoD detection. Yet no correlation coefficient (Spearman, Pearson), confidence interval, or statistical test is reported anywhere. The reader is asked to accept these claims based on visual inspection of tables containing dozens of numbers. When MIRA scores differ by small margins (e.g., CIFAR-100 ResNet-18: 0.6572 vs. DenseNet: 2.8060), there is no way to assess whether the difference is meaningful. Furthermore, the relationship between MIRA and detection performance is never reduced to a single quantitative summary (e.g., a single best-achievable-AUROC aggregate per model correlated against MIRA), making principled comparison impossible.

### Minor

- **No sensitivity analysis for perturbation hyperparameters**. MIRA depends on ε_min (chosen via an accuracy-threshold heuristic) and on the user-defined distribution p(ε) over perturbation magnitudes. Changing either could alter model rankings. The paper acknowledges this as a limitation (Section 6) but provides no empirical sensitivity analysis. For a metric proposed for model selection, this absence is a gap, though the paper's candid acknowledgment mitigates the severity.

- **Cross-domain comparability of MIRA is unclear**. NLP MIRA scores (e.g., DeBERTaV3: 3793.6) are orders of magnitude larger than vision scores (e.g., ViT: 89.3), even with the chi-square normalization. The paper does not discuss whether the normalization fully accounts for the vast dimensionality differences between transformer penultimate layers and CNN layers, or whether domain-specific calibration would be needed for meaningful cross-domain comparison.

- **Connection between binary definition and continuous score is informal**. Definition 1 is binary (existence of a set Z^l), but the MIRA Score is continuous. The paper motivates the jump through intuition about perturbation-based probing of the decision boundary but does not provide a formal derivation linking the continuous score to the binary definition. The connection is plausible but not established with rigor.

### Trivial

- The "Average" column in Tables 1–3 is described as averaging AUROC across the three detection methods, but the displayed values appear to correspond to the best single-detector result (bold entries) rather than a genuine average. This creates confusion about what quantity is actually being compared against MIRA.

## Nice-to-Haves

- A direct evaluation of MIRA against ID misclassification detection (e.g., AUROC for separating correctly vs. incorrectly classified ID samples using adversarial or naturally hard examples) would align the empirical story with Definition 1 and substantially strengthen the paper.
- A sensitivity analysis varying ε_min thresholds and p(ε) distributions, with rank-correlation coefficients reported across models, would establish the metric's robustness.
- Discussion of whether the Gaussian assumption underlying the chi-square surprisal normalization holds for the activations used, particularly in NLP models with high-dimensional penultimate layers.
- Runtime comparison between MIRA computation and the full OoD detector tuning + evaluation pipeline to substantiate the efficiency claim in RQ4.

## Removed Points

These points were flagged from the reviewer inputs but removed after verification against the paper:

- **"The MIRA score is not formally linked to Definition 1"** (from harsh critic) — Demoted from fatal to minor. The paper explicitly states Definition 1 is an abstract formalization and MIRA is a practical estimator; the connection is motivated through perturbation-based probing of the decision boundary. The gap is real but the paper does not claim a formal equivalence.

- **"FGSM is insufficient for probing the decision boundary"** — The paper explicitly addresses this in Section 4.2: "the strength of the attack is not critical: perturbations do not need to be 'subtle' … they should rather provide a meaningful direction toward the boundary." The justification is reasonable for the paper's purposes.

- **"The evaluation lacks missing baselines / unfavourable comparison"** — The paper explicitly acknowledges no established monitorability baseline exists and constructs a best-of-three detector evaluation as a proxy. This is a reasonable approach given the novelty of the concept.

- **"Missing related work on feature-space quality metrics (MMD, cluster purity)"** — I do not have external sources to confirm specific missing references and cannot fabricate them.

- **"Missing appendix / proofs / reference details"** — The parser strips appendix sections from all papers; these exist in the original submission.

- **"The OoD proxy fundamentally invalidates all claims"** — This was demoted from fatal to major. The MIRA score itself is computed purely from ID data (consistent with Definition 1's spirit), and OoD detection is a practically important related task. The mismatch is real but does not completely invalidate the contribution; the paper could address this by adding direct error-detection experiments or by refining the formal definition to encompass distribution-shift detection.

- **"No discussion of computational cost"** — The paper addresses this in the Discussion (Section 4.4): "tuning multiple OoD detectors through a grid search and subsequent evaluation on several OoD datasets is much more expensive than computing the MIRA Score." While a quantitative comparison would be stronger, the paper does not ignore this point.

- Strength removed: "This paper addressed an important problem" — Too generic, not grounded in specific paper content.

## Novel Insights

The paper's core insight — that neural networks possess an intrinsic, architecture-dependent property governing how detectable their errors are from internal activations, and that this property can be measured without external OoD data — is genuinely novel. The perturbation-based probing strategy (integrating over FGSM magnitudes and measuring feature-space surprisal) is a creative way to operationalize this idea. The observation that monitorability is detector-agnostic (a model with high MIRA supports detection through multiple fundamentally different scoring mechanisms) is a valuable conceptual contribution that could influence how the community thinks about model evaluation beyond accuracy.

## Suggestions

- Replace or supplement the OoD-detection proxy with an experiment that directly tests Definition 1: measure AUROC for separating correctly classified ID samples from misclassified ID samples (using adversarial perturbations that cause errors or naturally hard examples). This would close the gap between the formal definition and the empirical validation.
- Compute and report Spearman rank correlation between MIRA and a single aggregate measure of best-achievable OoD detection (e.g., mean of best-detector AUROC across all OoD datasets) per model, with confidence intervals.
- Conduct a sensitivity analysis varying ε_min (e.g., at accuracy thresholds of 80%, 85%, 90%, 95%) and p(ε) (uniform vs. other plausible distributions) and report whether model rankings remain stable.
- Add a brief discussion of cross-domain MIRA comparability, particularly addressing the NLP scale discrepancy and whether domain-specific calibration is needed.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- `l5ouuojPGe` — avg 3.00: Runtime monitoring thresholding strategies. Narrower scope, weaker contribution than our paper.
- `JEjVuVxbkf` — avg 3.00: Error detection on OoD data. Less novel formalization than our paper.
- `VAmVEghgoC` — avg 4.50: NC-OOD detector. Specific detection method with limited novelty; clearly below our paper.
- `Gr8nHvOivO` — avg 4.50: OOD detection through neural collapse. Similar level to NC-OOD.
- `ljwoQ3cvQh` — avg 7.00: Neural networks extrapolate predictably. Thorough empirical validation across 8 datasets, both theoretical and empirical contributions; above our paper.
- `mUXdysoxEP` — avg 6.75: Feature separation for OOD detection. Stronger theoretical grounding; above our paper.
- `P7KIGdgW8S` — avg 8.00: Hölder stability of GNNs. Mature theoretical contribution; clearly above.
- `nwDRD4AMoN` — avg 9.00: Kuramoto oscillatory neurons. Exceptional paper.

**Initial bracket: 4.5 – 7.0**

**Round 2 (Narrowing):**
- `YkEW5TabYN` — avg 5.00: Perturbed examples for NLP model comparison. Novel framework but limited evaluation; our paper has broader scope.
- `todLTYB1I7` — avg 5.00: Evaluation framework for neuron explanations. Similar conceptual contribution level.
- `YmQyEdLIkU` — avg 5.50: Adversarial attacks as near-zero eigenvalues. Novel theoretical framing but very narrow experiments (MNIST only) and definition concerns. Our paper is comparable or slightly stronger in empirical breadth but has analogous definition-evaluation alignment issues.
- `hoEanaoP4i` — avg 6.00: MD-LSM linear separability measure. Our paper has broader empirical scope (3 domains vs. 1 dataset) and a more novel concept, but the MD-LSM paper has stronger theoretical depth. Roughly comparable.
- `VyxlbbK8WV` — avg 6.00: Self-emergent similarity in vision networks. Solid contribution with thorough analysis.
- `jv2zHOalpL` — avg 6.00: Neural phylogeny detection. Novel task formulation with clear evaluation.

The paper sits between the 5.50 anchor (YmQyEdLIkU — similar structure: novel formalization + limited/imperfect validation) and the 6.00 anchors (hoEanaoP4i — similar goal of measuring a hidden-layer property). The definition-proxy mismatch and lack of quantitative correlation push it below 6.00, but the concept novelty, broad empirical coverage, and practical metric design keep it above 5.00. The paper is most comparable to YmQyEdLIkU (5.50) in terms of the gap between formal definition and empirical validation, but has stronger empirical breadth.

**Final score: 5.5**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
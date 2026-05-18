Now I have all the information needed. Let me compose the final consolidated review.

---

## Summary

This paper proposes ProtoN-FM, which replaces the standard LayerNorm in a Transformer with a prototype-guided dynamic normalization mechanism for time series foundation models. The key idea is to maintain multiple LayerNorm modules, each associated with a learned prototype representing a distinct data distribution. During training, each sample is routed (via argmin Euclidean distance) to the LayerNorm module whose prototype is closest, enabling per-sample adaptive normalization. Prototypes are updated via EMA with an orthogonality constraint to keep them distinct. The model is pretrained with contrastive learning on multiple heterogeneous datasets and evaluated on classification tasks (fault diagnosis and human activity recognition).

## Strengths

1. **Consistent improvements over Vanilla multi-dataset pretraining across all evaluation settings.** ProtoN-FM outperforms the Vanilla (standard LayerNorm) baseline on every dataset in both FD and HAR tasks (Tables 1–2), in cross-domain generalization (Section 5.3, Figure 6), and under artificially varied distribution shifts (Section 5.4, Figure 7). The gains are consistent in sign across all experiments.

2. **Ablation study (Table 3) isolates the benefit of prototype-guided dynamic selection.** Removing the prototype-guided gating ("w/o ProtoGate") and falling back to a fixed per-dataset assignment causes a clear performance drop, while removing the orthogonality constraint ("w/o OrthoConstrain") has a smaller effect. This confirms that dynamic, per-sample routing—not merely having multiple LayerNorms—drives the improvement.

3. **Cross-domain generalization experiment (Section 5.3) provides strong evidence for the method's robustness.** When the model is pretrained on all datasets *except* the target and then fine-tuned on a small labeled sample of the held-out dataset, ProtoN-FM consistently outperforms Vanilla (e.g., FD accuracy 46.73% vs. 41.89%). This demonstrates that the benefit holds even when the target distribution was unseen during pretraining.

4. **Parameter analysis (Section 5.2) shows robustness to the number of LayerNorms.** Performance remains relatively stable across 2, 3, 4, and #D (number of datasets) LayerNorms per ProtoNorm layer, suggesting the method does not require careful tuning of this architectural hyperparameter.

## Weaknesses

### Fatal

None.

### Major

1. **Missing comparison against existing adaptive normalization methods (RevIN, SAN, SIN).** Section 2.3 discusses RevIN (Kim et al., 2021), SAN (Liu et al., 2024b), and SIN (Han et al.) as closely related adaptive normalization techniques for time series and argues they "assume uniform statistical properties across all TS instances, which may not be optimal while pretraining with multiple datasets." Yet none of these methods are evaluated as baselines. The only baselines are supervised training, per-dataset pretraining (Individual), and multi-dataset pretraining with standard LayerNorm (Vanilla). Without comparisons to adaptive normalization baselines, it is impossible to determine whether ProtoN-FM's gains come from adaptive normalization *per se* or from the specific prototype-based mechanism. This is the most significant gap in the experimental validation.

2. **Evaluation limited to classification tasks, while claims target time series foundation models broadly.** The paper's title, abstract, and introduction claim a general approach to improving time series foundation models. However, the experiments cover only two classification applications (fault diagnosis and human activity recognition). No forecasting, anomaly detection, or imputation experiments are reported. The conclusion acknowledges this limitation ("Future research should explore… forecasting and anomaly detection"), but as written, the claims of a general solution for time series foundation models are unsupported by the evaluation.

3. **No measures of variance or statistical significance.** Experiments are repeated *three times* with only averages reported (line 177: "Each experiment was repeated three times, with the average performance reported"). No standard deviations, confidence intervals, or significance tests are provided. Given that some per-dataset gains are modest (e.g., as small as ~0.76–0.91 percentage points on individual HAR datasets according to the reported tables), it is impossible to assess whether the improvements are statistically meaningful or within the noise of the three runs.

### Minor

4. **"First work to identify the challenge" claim is overstated (line 19).** The paper states: "This is the first work to identify the challenge of data distribution mismatch between foundation model pretraining and time series data." Prior work cited in the paper itself (e.g., RevIN, DAIN, Non-stationary Transformers) explicitly addresses distribution shift in time series. The paper should qualify this claim and clearly differentiate what new insight is being added rather than claiming priority on identifying the problem itself.

5. **Gating mechanism's gradient flow and learning dynamics are underspecified.** The selection uses hard argmin (non-differentiable), prototypes are updated via EMA (not gradients), and the distance computation has no learnable parameters. The normalization parameters (γ, β) of the chosen LayerNorm module receive gradients normally, so the overall pipeline is trainable—analogous to VQ-VAE with EMA—but the paper does not discuss this design choice, the absence of learned projections in the gating, or potential concerns about prototype collapse. An analysis of prototype diversity or assignment purity during training would substantially clarify the mechanism.

6. **Orthogonality loss sensitivity analysis is narrow.** The orthogonal weight λ is tested over {0.001, 0.01, 0.1, 1} on only two datasets (IMS and UCIHAR, Figure 5). The claim that performance is "not highly sensitive to λ" is based on this limited sweep; demonstrating robustness across more datasets would be more convincing.

### Trivial

None.

## Nice-to-Haves

- Reporting prototype assignment purity (mapping between prototypes and datasets) and pairwise prototype distances during training would illuminate whether prototypes learn semantically meaningful distribution clusters.
- A sensitivity analysis on the number of prototypes beyond {2, 3, 4, #D} (e.g., ranging 1 to 10) would strengthen the claim that the method is robust to this choice.
- Including per-dataset results with standard deviations (not just averages) would address the statistical significance gap for all presented results.

## Removed Points

*Weaknesses that are flagged for removal but preserved here for reference:*

- **"Code is promised but not available"** — REMOVED (reproducibility nitpick; the paper states code will be made publicly available upon publication).
- **"Missing appendix content, missing proofs in appendix"** — REMOVED (parser strips appendix sections from all papers; these exist in the original submission).
- **"PatchTST is a forecasting model, not optimized for classification"** — REMOVED (using a Transformer with a classification head is standard practice; the paper transparently states why PatchTST was chosen for its simplicity).
- **"Low absolute accuracies (51% on HAR) raise concerns about whether the model is learning useful representations"** — REMOVED (this is tone, not a specific weakness; HAR across multiple diverse datasets with fine-grained classes is genuinely challenging and the relative comparison against baselines is what matters).
- **"Gaussian noise is an artificial simulation of distribution shifts"** — REMOVED (controlled synthetic perturbations are a standard and appropriate way to test robustness to varying shift magnitudes).
- **"Circular dependency could lead to collapse"** — REMOVED (this is speculative; no evidence of collapse is presented or claimed, and the consistent positive results suggest it does not occur in practice).
- **"Section 2.2 does not distinguish pretraining-time vs test-time distribution shift"** — REMOVED (the paper's focus is pretraining-time mismatch; criticizing absence of a distinction that is out of scope is unfair).
- **"Number of prototypes equals #D seems arbitrary"** — WEAKENED to minor observation above; the paper tests {2, 3, 4, #D} and shows robustness, which is reasonable.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that fundamentally reframes or deepens understanding of the paper beyond what the authors themselves present.

## Suggestions

1. **Add adaptive normalization baselines.** Compare ProtoN-FM against at least RevIN (instance normalization) within the same pretraining framework. This is the single most important addition to validate the paper's claim that the prototype-based selection mechanism provides benefits beyond existing adaptive normalization.

2. **Add at least one non-classification task.** A forecasting or anomaly detection experiment (even on a single benchmark) would significantly strengthen the claim that the method benefits time series foundation models generally, not just classifiers.

3. **Report standard deviations or confidence intervals for all experiments.** With only three runs and modest margins, variance information is essential. Report per-dataset results with standard deviations rather than only aggregated averages.

4. **Temper the "first work" claim** and clarify that the contribution is a specific mechanism (prototype-guided dynamic normalization) rather than identifying the distribution-shift problem itself.

5. **Explicitly discuss gradient flow through the gating mechanism** and provide analysis of prototype behavior (diversity, assignment entropy, convergence) during training.

## Score and Decision

The paper addresses a genuine problem and proposes a clean, well-motivated approach with consistent experimental support. However, the evaluation has significant gaps: (a) no comparison against adaptive normalization baselines that are discussed as related work, (b) only classification tasks despite claiming a general time series foundation model improvement, and (c) no measures of variance or statistical significance despite modest margins. These gaps are structural and prevent the current submission from convincingly supporting its claims. The method has promise and the core idea is sound, but the evidence presented is not sufficient for acceptance.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
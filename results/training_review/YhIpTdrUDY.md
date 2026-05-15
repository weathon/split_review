Now I have all the information I need. Let me produce the consolidated review.

## Summary

This paper proposes ProtoN-FM, a method that replaces the standard LayerNorm in Transformer architectures with a set of LayerNorm modules selected per-sample via a prototype-guided gating network. During multi-dataset pretraining, prototypes are learned to represent distinct data distributions, and each sample is routed to the LayerNorm whose prototype it is closest to. An orthogonality constraint keeps prototypes separable. The method is evaluated on fault diagnosis (FD) and human activity recognition (HAR) classification tasks, showing improvements over vanilla multi-dataset pretraining with fixed LayerNorm.

## Strengths

- **Well-motivated problem with clear empirical motivation (Figure 1):** The paper provides concrete evidence that distribution shifts exist among real-world time series datasets (Figure 1a) and that ignoring this mismatch degrades fine-tuning performance (Figure 1b: vanilla multi-dataset pretraining underperforms the proposed method). This establishes a clear gap relative to prior TS foundation models that use fixed normalization.

- **Architecturally simple and principled contribution:** Replacing fixed LayerNorm with a set of LNs selected via nearest-prototype routing is conceptually clean (Section 3.2, Equations 1–4). The approach operates at the normalization level within any Transformer, making it potentially plug-and-play.

- **Ablation validates both core components (Table 3):** Removing the prototype gate (DSLN → dataset-specific LN) drops average accuracy from 70.33% to 67.92%, and removing the orthogonality constraint drops it to 68.88%. This provides evidence that both the gating mechanism and prototype separation contribute to the observed gains.

- **Cross-dataset generalization is demonstrated (Figure 6):** In a leave-one-dataset-out evaluation, ProtoN-FM outperforms vanilla pretraining on unseen target datasets (e.g., FD: 46.73% vs 41.89% accuracy), showing that learned prototypes capture transferable distribution patterns rather than overfitting to seen datasets.

- **Robustness to controlled distribution shifts (Figure 7):** On IMS data perturbed with increasing Gaussian noise, ProtoN-FM consistently beats vanilla pretraining, with the largest gap at the strongest perturbation (+3.5pp accuracy). This directly supports the claim that the mechanism adapts to varying distribution mismatch.

- **Hyperparameter robustness analysis (Figures 4, 5):** Varying the number of LayerNorms (2–4) and the orthogonality loss weight λ (0.001–1) leads to only modest performance variation, indicating the method is not brittle to these choices.

## Weaknesses

### Fatal
None.

### Major

- **Missing experimental comparison with existing adaptive normalization methods.** The paper's related work (Section 2.3) discusses RevIN, DAIN, SAN, and SIN as normalization-based strategies designed to address distribution shift in time series, yet none of these are included as baselines in the experiments. The paper's core contribution is an adaptive normalization mechanism, and evaluating only against "vanilla LayerNorm" tells us that ProtoNorm > plain LN, but not whether it outperforms or complements existing adaptive normalization techniques (RevIN being the most prominent). The paper states these methods "assume uniform statistical properties across all TS instances" (line 44), but this claim is untested — RevIN normalizes each instance independently, which is strictly more per-sample adaptive than dataset-level prototypes. Without this comparison, the paper cannot substantiate its broader claim of "paving the way for more robust and generalizable time series foundation models."

- **Unclear training procedure for prototypes: EMA updates and gradient-based orthogonality loss are not reconciled.** The paper states that prototypes are updated via EMA (Eq. 5: p_i^{(t+1)} = α·p_i^{(t)} + (1-α)·x) while simultaneously applying an orthogonality loss L_orth = ||PP^T - I||_F² (Eq. 6) that is incorporated into the total loss (Eq. 8: L = L_NT-Xent + λ·L_orth). The paper never specifies whether prototypes are model parameters in the optimizer's computation graph or externally maintained running estimates. If prototypes are external to the gradient graph, L_orth cannot influence them through backpropagation, making the regularization meaningless. If they are trainable parameters, then the EMA update (applied after gradient steps) would partially overwrite gradient-based updates from L_orth, creating conflicting optimization signals. Additionally, the gating uses hard argmin selection (Eq. 4), which is non-differentiable — the paper never discusses how (or whether) gradients flow from L_NT-Xent to the prototypes through this selection. This omission makes the training loop ambiguous and affects reproducibility. The paper should specify the exact training procedure, e.g.: whether prototypes are in the parameter group of the optimizer, whether the EMA is applied before or after the gradient step, and how the hard selection is handled for backpropagation.

### Minor

- **Results reported without standard deviations or statistical significance.** The paper reports "each experiment was repeated three times, with the average performance reported" (line 177) but no standard deviations, confidence intervals, or significance tests are provided. For the HAR task, the average improvement is 1.35pp (51.05% vs 49.70%), but individual datasets show mixed results (e.g., SKODA: 55.62 vs 55.72 favoring Vanilla; UCIHAR: 56.40 vs 56.80 favoring Vanilla). Without variance estimates, these differences cannot be assessed for reliability. Standard deviations over runs should be reported.

- **Overstated novelty claim.** Contribution 1 (line 19) claims "This is the first work to identify the challenge of data distribution mismatch between foundation model pretraining and time series data." Distribution shift in time series is a well-documented problem (Kim et al., 2021; Fan et al., 2023, 2024), and prior TS foundation model papers (Woo et al., 2024; Ansari et al., 2024) also acknowledge this challenge, even if they don't solve it with adaptive normalization. The novelty of the proposed *solution* is clearer and should be the focus.

- **Non-differentiable hard selection (argmin) not addressed.** The gating uses i* = argminᵢ d(x, pᵢ) (Eq. 4), which is a discrete, non-differentiable operation. The paper does not discuss how gradients flow through this selection to update either the prototypes or the LN parameters of non-selected modules. If the selected LN receives gradients only from samples routed to it, this is effectively hard clustering of normalization parameters — a reasonable but non-trivial design choice that should be stated explicitly along with its implications (e.g., initialization sensitivity, potential for prototype collapse or unbalanced assignments).

- **Pretraining runs for only 5 epochs (lines 177).** This is unusually short for contrastive self-supervised learning (typical TS contrastive methods train for 50–200 epochs). While the paper may have found 5 epochs sufficient for their setup, this raises the question of whether prototypes and normalization parameters converge within that window, and whether longer pretraining would change the relative ranking of methods.

### Trivial
None.

## Nice-to-Haves

- **Comparison with RevIN, SAN, DAIN, SIN as experimental baselines.** As noted in Major weaknesses, this is the most significant gap. Even if these methods were designed primarily for forecasting, they are the most directly related normalization-based distribution shift methods and should be adapted or discussed.
- **Varying the number of fine-tuning samples** (e.g., 50, 200, full dataset) to see if the improvement persists or diminishes with more labeled data. The 100-sample setting is a single point.
- **Evaluation on additional backbones** (e.g., TimesNet, TCN) to support the claim that ProtoNorm is "plug-and-play."
- **Evaluation on forecasting or anomaly detection** to broaden the scope beyond classification, as the title invokes "Time Series Foundation Models."
- **Analysis of prototype assignment dynamics** — e.g., do assignments stabilize during training? Do prototypes correlate with dataset identity or with latent structure? Entropy of assignments would help validate the mechanism.

## Removed Points

These points from the reviewers are flagged to be removed; treat them with caution:

- **"Figure 1(a) shows distribution mismatch at the raw-value level, which is trivial."** — The paper uses Figure 1(a) only as motivation/illustration, not as evidence. The key empirical support comes from Figure 1(b) and the experimental results. This is a stylistic critique that does not undermine the paper.
- **"The claim that multi-dataset methods 'fail to fully address' distribution shifts is unsupported."** — The paper references these methods (Woo et al., 2024; Ansari et al., 2024) and reasonably observes that they use standard normalization without specific mechanisms for inter-dataset distribution differences during pretraining. The claim is measured ("some fail to fully address") and defensible.
- **"DSLN has more LNs than ProtoN-FM; a fairer comparison would use the same number."** — DSLN uses #D LNs (one per dataset) while ProtoN-FM uses 3 LNs. ProtoN-FM outperforms DSLN *despite* having fewer parameters, which actually strengthens the case for the prototype mechanism, not weakens it.
- **"The generalization gap is smaller than in the main tables."** — This is expected behavior when the target dataset is unseen during pretraining. The paper does not claim the gap is the same size; it simply reports the results of a different experimental condition.
- **"The future work paragraph is generic."** — This is a presentation nitpick about the concluding section; it carries no weight in evaluating the paper's contribution.
- **"Individual pretraining is not a fair comparison for a foundation model."** — The paper uses Individual pretraining as a lower-bound baseline to demonstrate that multi-dataset pretraining itself provides a benefit. This is a standard experimental design choice.
- **"Section 3.1.2 explanation of LayerNorm is standard but longer than necessary."** — This is a prose-organization nitpick that does not affect the paper's technical contribution.
- **"Claim that the method 'cannot work as intended' due to the EMA/gradient issue."** — As discussed in the Major weaknesses section, the training procedure is unclear and needs clarification, but it is not self-evidently broken. Multiple plausible implementations exist (e.g., prototypes as parameters receiving gradients from L_orth, with EMA as an additional post-gradient-step smoothing), and the paper's ablation results suggest the method does work in practice. The training procedure needs to be specified, but the method is not inherently flawed.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective on the problem or method that the paper itself does not already provide.

## Suggestions

1. **Resolve the training procedure ambiguity.** Specify clearly in Section 3.2: (a) whether prototypes are model parameters in the optimizer's parameter group or external EMA-updated structures; (b) if both EMA and gradient-based L_orth are used, state the order of operations (e.g., gradient step → EMA update) and justify why this hybrid approach does not cause conflicting updates; (c) address how the hard argmin selection is handled during backpropagation (e.g., straight-through estimator, or only the selected LN receives gradients, with prototypes updated only via EMA and L_orth).

2. **Add key baselines.** Include RevIN (the most widely used instance normalization for TS distribution shift) and at least one other adaptive normalization method (SAN or DAIN) under the same pretraining/fine-tuning protocol. This is essential to substantiate the claim that ProtoNorm improves over existing normalization strategies, not just over vanilla LayerNorm.

3. **Report standard deviations** over the three runs already performed, and ideally report per-dataset results alongside averages so readers can assess consistency.

4. **Tone down the "first work to identify" claim** and instead emphasize the novelty of the proposed solution (prototype-guided LN selection), which is the actual contribution.

5. **Discuss the non-differentiable argmin selection** and its implications for training dynamics, including possible failure modes such as prototype collapse or unbalanced assignments.

## Score and Decision

**Originality**: Moderate. Prototype-guided LN selection is a novel architectural contribution, though the individual components (EMA prototype updates, orthogonality regularization, contrastive pretraining) are each known techniques.

**Quality of claims**: The core claim is supported but incompletely evaluated. The ablation is well-designed, but the missing comparison with existing normalization methods and the unclear training procedure weaken confidence.

**Soundness**: The experiments are reasonable in scope but lack statistical rigor (no standard deviations) and critical baselines.

**Clarity**: Generally well-written, but the training procedure for prototypes is underspecified to the point of ambiguity.

**Value to community**: The problem is timely and the approach is architecturally simple enough to be adopted. However, without validation against existing adaptive normalization methods, the practical value is unclear.

Given the significant gap in experimental comparison (missing baselines — RevIN, SAN, DAIN, SIN are discussed but never tested) and the ambiguity in the prototype training procedure (which affects reproducibility), the paper needs major revisions before it can be accepted. The core idea has merit and the ablation study is the strongest element, but the evaluation is incomplete.

**Score**: 5.0

**Decision**: Reject

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
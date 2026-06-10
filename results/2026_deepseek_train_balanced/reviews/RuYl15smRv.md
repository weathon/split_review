Here is the final consolidated review:

---

## Summary

This paper proposes AnomalyTCN, a dual-branch convolution architecture for unsupervised time series anomaly detection. The core idea is to replace the costly attention mechanism in prior contrastive-based methods (specifically DCdetector) with a lightweight pure-convolution backbone: one branch uses dense convolution and the other uses dilated convolution, and the representation discrepancy between branches serves as both the contrastive training signal (via symmetrized KL divergence with stop-gradient) and the anomaly criterion. Experiments on seven benchmarks show competitive F1 scores while saving 83.6% runtime and 20.1% memory compared to DCdetector.

## Strengths

- **Quantified efficiency gains over the direct attention-based competitor.** Table 2 reports 83.6% runtime reduction and 20.1% memory savings against DCdetector while maintaining comparable or better F1 across all five real-world datasets. This directly supports the paper's central efficiency claim.
- **Consistent top-tier F1 across multiple benchmarks with comprehensive baselines.** Table 1 shows AnomalyTCN achieves the best or second-best F1 on all five real-world datasets among 20+ baselines, and Figure 3 shows at least 15% improvement on the challenging NeurIPS-TS-GECCO dataset (1.1% anomaly ratio). The baseline list is extensive and includes both classic and recent methods.
- **Ablation study conclusively demonstrates that structural asymmetry is necessary and that increasing asymmetry monotonically improves performance.** Table 3 shows that a weight-sharing symmetric design completely fails, and progressively introducing asymmetry (rescaling, removing weight-sharing, different convolution settings) yields continuous F1 improvement. This directly validates the core architectural design choice.
- **Interesting finding about stop-gradient in time series contrastive learning.** Section 5.3 shows AnomalyTCN still performs competitively without Stopgrad, unlike CV contrastive methods that collapse. The paper attributes this to inherent structural asymmetry, providing a non-obvious insight specific to time-series anomaly detection.
- **Robustness analysis of kernel sizes and dilation ratios.** Table 4 systematically evaluates kernel sizes 5/7/9 and dilation ratios, showing robustness while also identifying scenarios where large dilation ratios hurt performance (excessive normal-point skipping).

## Weaknesses

### Major

- **Novelty is limited to a backbone swap within the DCdetector framework.** The paper is transparent about borrowing the contrastive framework, loss function (symmetrized KL divergence with stop-gradient, Equations 1–4), anomaly scoring (Equation 5), variate-independent embedding, instance normalization, and rescaling operation from DCdetector. The only new element is replacing dual-attention with dual-convolution (dense + dilated). While this is a meaningful engineering contribution — attention's quadratic complexity is a real bottleneck — the paper positions itself as a "novel solution" when it is more accurately an efficient re-backboning of an existing method. The text repeatedly signals this debt ("As with DCdetector", "Following DCdetector", "We adopt the same anomaly score as in DCdetector", "similar to DCdetector"). For a top-tier venue where novelty is a primary criterion, this limited scope of new contribution is a significant concern.

- **Efficiency benchmarking is incomplete.** The headline efficiency numbers (83.6% runtime, 20.1% memory) are computed only against DCdetector. Several other efficient backbones — ModernTCN, TimesNet, GPT4TS — appear as baselines in Table 1, but their efficiency metrics are never reported. Without this, it is impossible to tell whether the efficiency gain is a specific property of the dual-branch design or simply a consequence of using convolutions (which these baselines already do). The paper's central claim — that AnomalyTCN provides "a better balance of performance and efficiency" — is under-supported without efficiency comparisons to these other efficient backbones adapted to the contrastive framework.

### Minor

- **Evaluation uses the point-adjustment protocol without acknowledging its known limitations.** The paper states it "follow[s] the well-established protocol in Shen et al. (2020); Xu et al. (2021) to set the window length as 100." This protocol in practice uses point-adjustment, which marks entire anomalous segments as detected if any point within them is flagged — a procedure known to inflate F1 scores and obscure real performance differences (Wu & Keogh, 2020). The paper's central performance claims rely entirely on F1 under this protocol, yet the controversy is not acknowledged and unadjusted metrics are not reported.

- **No discussion of limitations or failure cases.** The paper concludes (Section 6) without addressing when the method might fail, what anomaly types it handles poorly, or sensitivity to hyperparameters beyond kernel size and dilation ratio. This limits the reader's ability to assess practical applicability.

- **Key architectural details are missing.** The paper does not specify the number of layers in the dual-branch structure, the feature dimension D, the total parameter count, or how the anomaly threshold δ is chosen (it is described only as a "hyperparameter" without a selection procedure — e.g., validation-based tuning, fixed percentile, or other criterion).

- **Results are reported without variance or statistical significance.** No standard deviations, confidence intervals, or multiple-seed runs are reported, despite known variance in anomaly detection outcomes under different training conditions and thresholds.

- **The motivating intuition (Figure 1) is not validated against the trained model.** The toy example in Figure 1 uses fixed mean filters and a single depth-wise layer to illustrate why dense vs. dilated convolution should yield larger discrepancy for anomalies. The actual implementation uses trainable kernels, multiple layers (depth-wise conv + two point-wise convs + GELU), and non-linearities. The paper does not analyze whether the trained model's behavior is consistent with this intuitive story (e.g., by visualizing learned kernels or comparing per-branch responses on normal vs. anomalous inputs). The paper acknowledges this gap in principle but does not bridge it.

### Trivial

None.

## Nice-to-Haves

- Reporting unadjusted precision/recall alongside adjusted F1 would strengthen the SOTA claim against known evaluation concerns.
- Describing the threshold δ selection procedure in detail would improve reproducibility.
- A code release would facilitate adoption and verification, though it is not a requirement.
- Comparing efficiency against other efficient backbones (ModernTCN, TimesNet) adapted to the contrastive framework would disentangle the specific contribution of the dual-branch design from the general efficiency of convolutions.

## Removed Points

- Criticism about "no code release mentioned" — removed per reproducibility nitpick rule.
- Criticism about the rescaling operation being unexplained — the paper does explain it mathematically ("dividing the row sum along the feature dimension"), though a deeper motivation would be beneficial.
- Criticism about not discussing ModernTCN's multi-branch design in Related Work — the paper explicitly notes it takes "an opposite perspective" (discrepancy vs. aggregation), which is sufficient differentiation for a brief related work section.
- Criticism that the efficiency comparison should include non-time-series models — the paper's scope is correctly limited to time series anomaly detection.

## Novel Insights

The most interesting observation not fully developed by the paper is the Stopgrad finding (Section 5.3): AnomalyTCN does not collapse without stop-gradient, unlike contrastive methods in CV. The paper attributes this to inherent structural asymmetry in the dual-convolution design. This suggests a fundamental difference between time-series and image-based contrastive learning that warrants deeper investigation. The paper's empirical finding here — that convolution-based structural asymmetry alone can prevent collapse — is arguably more novel than the efficiency claim, yet it receives relatively brief treatment.

## Suggestions

1. Broaden the efficiency benchmark to include other convolution-based backbones (ModernTCN, TimesNet) adapted to the contrastive framework, to disentangle the benefit of the specific dual-branch design from the general efficiency of convolutions.
2. Report unadjusted precision/recall alongside adjusted F1 to address the point-adjustment concern.
3. Add a limitations paragraph discussing failure cases, anomaly types the method handles poorly, and sensitivity to key hyperparameters beyond kernel size.
4. Specify architectural details (number of layers, D, parameter count) and threshold selection procedure.
5. Consider repositioning the contribution more precisely as "an efficient convolution-based instantiation of the DCdetector framework" rather than a fully novel method — this would better match the actual scope and preempt novelty concerns.

## Score and Decision

The paper is well-written and executed, with thorough ablations and an interesting finding about stop-gradient robustness in time series contrastive learning. However, for ICLR standards, the novelty is a significant concern: the method is DCdetector with attention replaced by convolution, borrowing the learning framework, loss, scoring, and embedding designs nearly wholesale. The efficiency claim — the paper's distinguishing contribution — is only benchmarked against a single comparator. The evaluation follows standard protocol but does not address known concerns about point-adjustment inflation. These factors together suggest the paper would be a stronger fit for a more specialized venue.

**Score: 5.0 — Borderline reject.**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
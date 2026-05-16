I now have a thorough understanding of the paper and all reviewer claims. Let me synthesize the final review.

---

## Summary

The paper proposes AnomalyTCN, a pure-convolution dual-branch architecture for contrastive-based unsupervised time series anomaly detection. One branch uses dense depth-wise convolution, the other uses dilated depth-wise convolution with equivalent kernel size; the representation discrepancy between the two branches serves as the anomaly criterion. This replaces the costly attention mechanisms used by prior contrastive methods (DCdetector), achieving competitive or better F1 scores on five real-world benchmarks and two NeurIPS-TS datasets while reducing runtime by 83.6% and memory by 20.1% relative to DCdetector.

## Strengths

- **Novel combination of pure convolution with contrastive discrepancy learning for anomaly detection.** Prior contrastive methods (DCdetector, AnomalyTransformer) rely on attention with quadratic complexity. The paper is the first to show that an asymmetric pair of dense/dilated depth-wise convolution branches can generate the different views needed for contrastive discrepancy learning, directly addressing the efficiency bottleneck. (Section 3.1, Figure 2)

- **Strong empirical performance with substantial efficiency gains.** AnomalyTCN achieves the highest average F1-score across five real-world datasets (Table 1) and outperforms all baselines on the challenging NeurIPS-TS datasets (Figure 3), while reducing running time by 83.6% and memory usage by 20.1% compared to the previous best contrastive method DCdetector (Table 2). This demonstrates that convolution-based designs can match or exceed attention-based performance in this setting.

- **Clear intuitive mechanism.** Figure 1 provides a simple non-trainable illustration showing how dilated convolution skips anomalous points while dense convolution does not, creating a natural discrepancy signal. The paper explains how this intuition extends to deeper trainable architectures (Section 1, Section 3.1).

- **Systematic ablation isolating the source of improvements.** Table 3 progressively adds structural asymmetry (rescale → weight unsharing → different convolution settings), showing each step contributes positively and confirming that the asymmetric design is essential. The comparison against a symmetric weight-sharing baseline (which fails completely) cleanly demonstrates why asymmetry is necessary.

- **Interesting finding about stop-gradient robustness.** Unlike contrastive learning in computer vision, AnomalyTCN still performs competitively without stop-gradient (Table 5), and the paper provides a plausible structural explanation (Section 5.3). This highlights domain-specific properties of time series anomaly detection.

## Weaknesses

### Fatal

None.

### Major

None. The issues below are addressable in revision and do not invalidate the paper's core claims.

### Minor

- **Missing definition of μ in the anomaly score (Equation 5).** The anomaly score is Softmax(μ − (KL(P,S) + KL(S,P))), but μ is never defined. Is it a learned parameter? The running mean of discrepancies from the training set? The paper states it "adopt[s] the same anomaly score as in DCdetector (2023)," but a self-contained definition is needed for reproducibility.

- **Threshold selection for δ is not described.** The paper states a hyperparameter threshold δ is used (Section 3.3) but does not explain how it is set. If the standard protocol (maximizing F1 on the test set using ground-truth labels) is followed, this should be stated explicitly, as it affects interpretation of the reported F1 scores. The paper should also acknowledge that this yields upper-bound estimates.

- **Baseline adaptation for general time series backbones is unspecified.** The paper includes aLLM4TS, ModernTCN, GPT4TS, and TimesNet as "advanced reconstruction-based method with general time series backbones" (Section 4 baseline listing and Table 1). No description is given of how these models were adapted for anomaly detection — what task head was used, what loss function, whether pretrained weights were frozen. While these are supplementary baselines (the primary competitors — DCdetector and AnomalyTransformer — are well-specified), the missing details affect the completeness of the evaluation.

- **Efficiency comparison is limited to a single baseline.** Table 2 compares AnomalyTCN only against DCdetector. The abstract claims "more efficient solution" broadly. Since ModernTCN (also a convolution model) appears in Table 1, a brief efficiency comparison (at minimum runtime/parameter count) would substantiate the claim beyond the single attention-based competitor. The current evidence shows only that AnomalyTCN is faster than one specific attention-based model.

- **Ablation studies are reported on a single dataset (likely SWaT).** Tables 3, 4, and 5 do not specify which dataset is used — the text only mentions SWaT in the discussion of Table 4. Ablation results would be strengthened by showing they hold on at least one additional dataset (e.g., SMD or MSL).

- **The paper does not discuss the SWaT result where AnomalyTCN appears to underperform DCdetector.** Per Table 1 (the reviewer reports 75.5 vs. 79.4 F1), this is one dataset where AnomalyTCN loses to the primary competitor. The paper's claim of "consistent state-of-the-art" and "performs the best in most cases" is technically compatible with one loss, but the result merits explicit discussion and analysis.

- **The loss function L = L_P − L_S is inherited from DCdetector without independent motivation or analysis.** While this is a valid design choice, the paper could strengthen its contribution by providing intuition for why minimizing one discrepancy while maximizing the other is beneficial, or by ablating the sign (e.g., comparing L_P + L_S vs. L_P − L_S). The paper's own finding that removing Stopgrad still yields competitive performance (Section 5.3) raises the question of whether the loss asymmetry or the structural asymmetry is the primary driver.

- **No discussion of limitations.** The paper lacks a dedicated limitations section. It would benefit from acknowledging potential failure cases (e.g., collective/subsequence anomalies, sensitivity to very high anomaly ratios, datasets where large dilation ratios produce false positives — as hinted for SWaT in Section 5.2).

### Trivial

- **No error bars or statistical significance reported.** This is standard practice in this benchmark-driven subfield, but noting the limitation would be good practice.
- **Some phrasing overstates the breadth of evidence**, e.g., the statement that the rescale operation comparison validates "effectiveness" with a single data point; the claim that "the paper's study also reveals the possibility of combining contrastive-based anomaly detection frameworks with other efficient time series backbones" (Conclusion) is forward-looking but not directly demonstrated.

## Nice-to-Haves

- A t-SNE or PCA visualization of P and S representations for normal vs. anomalous time points would enrich the contrastive learning analysis.
- Hyperparameter sensitivity study of window length, given that convolution kernels have a fixed size (7) but window length varies across datasets (36–100).
- A broader efficiency comparison including a parameter/FLOPs analysis for ModernTCN or other convolution-based models would strengthen the efficiency narrative.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"Figure 1 uses non-trainable mean filters... gap between this simplified example and the real implementation is not discussed."* — The paper explicitly discusses this gap: "in our real implementation... we adopt a deeper network structure to bring better representation capacity. And we also make the weights of convolution kernels trainable." (lines 18–19). The criticism is factually inaccurate.
- *"The paper does not clarify whether the two branches share the point-wise layers."* — The paper states: "the successive point-wise convolution modules in two branches do not share the weights, even though they have the same structure settings" (line 68). Factually inaccurate.
- *"Including classic baselines [VAR 1976, LOF 2000] is misleading; they inflate the apparent advantage."* — Including a wide range of methods from classic to modern is standard practice in this field. The paper categorizes them transparently. This is a disagreement on convention, not a flaw.
- *"The step from 'same structure, no weight-sharing + rescale' (73.9) to 'different structures + rescale' (75.5) is only 1.6% gain, suggesting the dual-branch design is not the primary driver."* — This is a subjective interpretation of Table 3. The paper's claim is about "continuous performance improvement," which is objectively true. The improvement from each step is meaningful in aggregate.

## Novel Insights

None beyond the paper's own contributions. The reviews highlight presentation and reproducibility gaps but do not uncover insights about the method that the authors themselves did not identify.

## Suggestions

1. Define μ explicitly in Section 3.3 and describe threshold selection (δ) protocol. If test-set-based thresholding is used, acknowledge this as an upper-bound estimate.
2. Specify the datasets used for all ablation studies (Tables 3–5) and ideally add results on at least one additional dataset.
3. Describe how general time series backbones (aLLM4TS, ModernTCN, GPT4TS, TimesNet) were adapted for anomaly detection (task head, loss, frozen weights).
4. Add a brief efficiency comparison with ModernTCN (parameters, runtime) to substantiate the broad efficiency claim.
5. Discuss the SWaT result (if AnomalyTCN underperforms DCdetector on that dataset) and add a limitations paragraph.

## Score and Decision

This paper makes a meaningful contribution: it demonstrates that contrastive discrepancy learning for anomaly detection can be implemented with a pure convolution architecture, achieving results on par with or better than attention-based methods while being substantially faster. The core idea is sound, the ablations are systematic, and the main experimental evidence supports the claims. The weaknesses are primarily in presentation completeness (missing specifications, single-dataset ablations, lack of discussion of one counterexample) rather than in the methodology or the validity of the central results. These are all addressable in a revision.

The paper merits acceptance.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
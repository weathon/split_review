- Decision: Accept
- Avg Score: 6.60
- Scores: 6, 5, 6, 8, 8
I have thoroughly reviewed the paper and all reviewer claims. Let me now produce the consolidated review.

## Summary

This paper introduces InterpGN, a mixture-of-experts framework for time series classification that combines an interpretable Shapelet Bottleneck Model (SBM) with a deep neural network (DNN). The key innovation is a gating function (modified Gini index on the SBM's softmax output) that routes confident samples to the interpretable expert and defers uncertain samples to the DNN. A second contribution is an RBF-based predicate for the shapelet transform that improves shapelet interpretability over prior threshold-based formulations. Experiments on 30 UEA multivariate TS datasets (avg. rank 2.50) and MIMIC-III in-hospital mortality prediction demonstrate competitive performance with black-box models while providing local and global interpretability.

## Strengths

- **Novel confidence-based gating function (Section 4.4, Equation 6)**: The modified Gini index on the interpretable expert's softmax output is a clean, principled design for adaptively routing samples to the DNN only when the SBM is uncertain. Figure 5 provides strong qualitative evidence: samples with low gating values lie on cluster boundaries, confirming the gating effectively identifies hard cases while preserving interpretability for the majority.

- **RBF-based predicate for shapelet transform (Section 4.1, Equation 2, Figure 3)**: Replacing the threshold-based predicate of prior work (LTS) with a Gaussian radial basis function directly addresses known shapelet-quality degradation. Figure 3 provides a clear visual comparison showing that learned shapelets more closely resemble actual TS subsequences.

- **Competitive predictive performance on a broad benchmark (Table 1)**: InterpGN achieves the best average rank (2.50) across 30 UEA multivariate TS datasets, outperforming both black-box deep models (FCN, TS2Vec, TimesNet, PatchTST) and interpretable baselines (ShapeNet, RLPAM, ShapeConv). This supports the core claim that the hybrid architecture does not sacrifice accuracy.

- **Real-world healthcare demonstration with interpretable outputs (Section 5.2, Figure 6, Table 2)**: On MIMIC-III in-hospital mortality prediction, InterpGN improves over SBM alone, and the local explanations (e.g., decreasing HR, increasing MBP as mortality indicators) demonstrate practical utility beyond synthetic benchmarks.

- **Global and local explainability (Section 4.3, Figure 4)**: The linear classifier over shapelet predicates yields rule-like global explanations (e.g., "class c should contain shapelet s") that are more informative than the local-only explanations typical of prior shapelet methods. Figure 4 visually validates such rules.

## Weaknesses

### Fatal

None.

### Major

- **Gating mechanism assumes SBM calibration without validation (Section 4.4, Equation 6)**: The gating function uses the SBM's softmax confidence to decide whether to defer to the DNN. This design rests on the assumption that high softmax probability corresponds to correct, reliable predictions. The paper provides indirect evidence (Figure 5 shows boundary samples have low η), but does not directly analyze calibration (e.g., expected calibration error, reliability diagrams) or verify that samples routed to the SBM via the hard threshold η̄ have near-perfect accuracy. If the SBM is overconfident on errors — a well-documented issue — the gating would lock in wrong answers without DNN correction, directly undermining the "preserving interpretability when appropriate" claim.

### Minor

- **Inconsistency between abstract and results on SOTA comparison**: The abstract states the model "achieves comparable performance with state-of-the-art deep learning models," while the introduction claims "InterpGN outperforms state-of-the-art methods" and Section 5.1 states "InterpGN outperforms the baseline methods." These are different claims — "comparable" is weaker than "outperforms." The paper should be precise about which claim the evidence supports. (This does not weaken the contribution; being "comparable" while offering interpretability is itself a positive result.)

- **Missing statistical significance for UEA results**: The UEA benchmark results (Table 1) are reported without standard deviations, confidence intervals, or significance tests (e.g., Wilcoxon signed-rank test against top baselines). Without this, the claim that InterpGN "outperforms" baselines is not statistically supported.

- **No ablation of the gating threshold η̄**: The inference-time hard threshold η̄ determines the interpretability-accuracy trade-off (how many samples are gated to the SBM vs. the DNN). A simple plot showing accuracy vs. fraction of samples gated as η̄ varies would directly quantify how much interpretability is preserved. This analysis is absent.

- **Key hyperparameters not ablated**: (a) The number of shapelets per channel K is a critical hyperparameter with no sensitivity analysis. (b) The β weight on ℒ_int in the hybrid objective (either constant or cosine-decayed) is mentioned but its impact on the interpretability-performance trade-off is not analyzed. (c) The scaling parameter ε in the RBF predicate (Equation 2) is not discussed (learned vs. tuned).

### Trivial

- Minor inconsistency: the paper mentions "Figure 22 and Figure 23" (line 149) for the β schedule — these cross-references suggest appendix figures that do not appear in the visible main text, and the numbering seems off.

- The FCN architecture used as the DNN expert is not specified beyond citing Wang et al. (2017). Training hyperparameters (learning rate, batch size, optimizer) are absent from the main text.

## Nice-to-Haves

- Ablate the gating function against alternatives: (1) a fixed ratio of experts, (2) a learned gating network (as in IME), or (3) a post-hoc rule using SBM only when it agrees with the DNN. This would isolate the specific benefit of the confidence-based design.
- Analyze sensitivity to the shapelet length set L (the six fractional values of T chosen).
- Evaluate whether temperature scaling or other calibration methods improve gating reliability.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Quantitative interpretability and shapelet quality results are not in the main text"**: The harsh critic noted that Section 5.3 defers quantitative results (Table 3/7) to the appendix. **Removed per hard rules**: the parser strips appendix content from all papers. The appendix exists in the original submission; this is not an author-originated omission.

- **"No quantitative evidence that RBF predicates improve shapelet quality over threshold-based predicates in the main text"**: **Removed** for the same reason — the quantitative metrics and comparison table are in the appendix (stripped by parser). The main text provides qualitative evidence (Figure 3).

- **"Missing related work discussion of N-BEATS"**: **Removed** per the rule about not mentioning missing related works without external sources.

- **"Tables are images in the provided text"**: **Removed** — this is a parser artifact, not an author error.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the paper's strengths and weaknesses; no new pattern emerges from their synthesis beyond what the paper already reports.

## Suggestions

1. **Add calibration analysis**: Report expected calibration error (ECE) for the SBM and show a reliability diagram. Demonstrate that samples above the gating threshold η̄ have near-perfect accuracy, or apply temperature scaling to the SBM's softmax.
2. **Report statistical significance**: Add standard deviations (from repeated runs) and a Wilcoxon signed-rank test comparing InterpGN against top baselines on the UEA archive.
3. **Ablate the inference threshold η̄**: Include a plot of accuracy vs. fraction of samples gated to the SBM as η̄ varies, quantifying the interpretability-accuracy trade-off.
4. **Resolve the "comparable" vs. "outperforms" inconsistency** and adopt precise language throughout.

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 8, 6, 3
Now I have all the information needed. Let me produce the final review.

## Summary

ShuffleMTM proposes a self-supervised masked time-series modeling framework that incorporates cross-channel dependence into the channel-independent (CI) pre-training paradigm. The key idea is to randomly shuffle unmasked patches across channels at the same temporal index, then use Siamese encoders to process both the original and shuffled masked series. A decoder with cross-attention integrates the two views, enabling reconstruction that leverages both temporal dependencies within each channel and spatial dependencies across channels. The paper evaluates on forecasting (8 datasets, 4 horizons) and classification (2 medical datasets), reporting strong results.

## Strengths

- **Novel shuffling mechanism for cross-channel learning in CI pre-training.** The paper introduces a simple operation (Eq. 2, Fig. 2) that randomly exchanges unmasked patches at the same temporal index across channels. This directly addresses a recognized limitation of CI MTM methods (PatchTST, SimMTM, TimeSiam) that cannot model cross-channel interactions during pre-training. The approach is clean and well-motivated.

- **Strong forecasting performance across diverse benchmarks.** ShuffleMTM achieves the best or second-best MSE/MAE in 72 out of 80 in-domain forecasting scenarios (Table 1), outperforming both CI MTM baselines (SimMTM, PatchTST, PITS, TimeSiam) and channel-dependent methods (iTransformer, Crossformer, CrossGNN, MTGNN). The gains are particularly notable on high-channel datasets (Traffic, Electricity) where cross-channel dependence is most critical.

- **Direct evidence of cross-channel dependence learning.** Figure 8 provides multi-level validation: (a) the self-attention maps of shuffled series show higher cosine similarity to the true patch-correlation matrix than PatchTST, TimeSiam, and even a single-branch PatchTST variant trained on shuffled data; (b) pairwise distances of learned channel embeddings closely mirror raw inter-channel correlations. This dual analysis concretely supports the core claim.

- **Capacity-robustness analysis confirms dual benefit.** Using the framework from Han et al. (2024), ShuffleMTM achieves lower train/test errors (capacity) on 12/16 measures and lower generalization error / W difference (robustness) on 11/16 measures compared to PatchTST (Fig. 9). This demonstrates that the method combines the advantages of CI models (robustness) and channel-dependent models (capacity).

- **Practical robustness demonstrated.** ShuffleMTM shows consistent improvements over baselines in missing-data scenarios (Fig. 4), longer look-back windows (Fig. 5), and limited-label classification settings (Table 4, 5%/10%/20% labeled data). These experiments go beyond standard evaluation and speak to real-world applicability.

## Weaknesses

### Fatal
None.

### Major

- **Missing ablation: pre-training vs. no pre-training on the ShuffleMTM architecture.** The paper compares ShuffleMTM (pre-trained + fine-tuned) against other pre-trained CI MTM baselines and supervised-from-scratch forecasting methods. However, it never compares ShuffleMTM *pre-trained + fine-tuned* against *ShuffleMTM trained from scratch* on the downstream task (i.e., end-to-end supervised without pre-training). Without this comparison, it is impossible to isolate whether the performance gains come from the pre-training phase or from the architectural modifications (shuffling + Siamese encoders + cross-attention decoder) alone. Since the paper is framed as a pre-training contribution, this gap weakens the evidence for the value of self-supervised pre-training specifically. This is a straightforward ablation to add.

### Minor

- **No variance or confidence intervals reported for the central forecasting claim.** The paper states "We report the average performance over five runs" (Section 4.1) and claims "best or second-best results in 72 out of 80 forecasting scenarios" (Section 4.2), but no standard deviations, confidence intervals, or significance tests are provided. Without variance information, the reader cannot assess whether the reported improvements are meaningful given that many forecasting benchmarks show small absolute differences between methods. While mean-only reporting is common in the time-series forecasting literature, the strength and breadth of the claim warrant at least a summary of variability (e.g., "consistent across all 5 runs" or std ranges for key comparisons).

- **Classification evaluation is too narrow to support broad generality claims.** Only two medical-domain datasets (AD—EEG, PTB—ECG) are used for classification. While the paper's primary contribution is in forecasting, the abstract and introduction claim effectiveness for "classification tasks" broadly. Two datasets, both in the medical domain, do not support this generality. Additional datasets from different domains (e.g., human activity recognition, gesture recognition) or a more qualified claim would strengthen the presentation.

- **Ambiguity about baseline result provenance.** The paper states it "follow[s] the experimental settings and baseline results in TimeSiam, iTransformer and CrossGNN" (Section 4.2) but does not clarify which baseline numbers were independently re-computed vs. taken from prior papers. This is a reproducibility concern, particularly for channel-dependent methods (iTransformer, Crossformer) where training details may differ.

- **Lagged cross-channel dependencies are not explicitly addressed or validated.** The shuffling procedure (Eq. 2) only exchanges patches at the same temporal index across channels. The paper asserts that temporal self-attention within the encoder can propagate these to capture lagged dependencies (Section 2, "dynamically imposes patches at lagged locations"), but provides no analysis or synthetic experiment to verify that lagged cross-channel relationships are actually learned. The correlation analysis in Figure 8 only measures contemporaneous patch correlations. This is a scope limitation that should be acknowledged.

- **No discussion of limitations.** The paper lacks a dedicated limitations section. Important issues worth acknowledging include: (a) the shuffling is restricted to same-index patches, (b) potential failure cases when the number of channels is small (shuffling diversity decreases), (c) the added computational cost of the Siamese encoder (2× forward pass per pre-training update).

### Trivial

- **Edge case in shuffling.** If all channels have a patch masked at the same index j, then there are no unmasked patches to shuffle into that position across channels (Eq. 2 selects i′ from unmasked patches at that index). The paper does not discuss how this degenerate case is handled; in practice it is unlikely with reasonable mask ratios, but it should be noted.

## Nice-to-Haves

- **Synthetic experiment for lagged dependencies.** Designing a synthetic dataset with known lead-lag relationships between channels and probing whether ShuffleMTM's representations capture these lags would directly validate the claim that cross-channel information at non-contemporaneous timesteps is learned.
- **"Pre-training vs. from scratch" ablation** (listed as Major above) would also serve as a nice-to-have addition that strongly strengthens the paper's core narrative.
- A brief empirical justification for why cross-channel information is preserved in the single-branch encoder weights after removing the shuffled branch during fine-tuning (as currently claimed in Section 3.4) would be welcome.

## Removed Points

These points were raised by one or both reviewers but are not included in the main review. They are listed here for completeness; treat with caution.

1. **"Overstated originality / first technical contribution"** (Harsh Critic): The critic claimed that claiming "first technical contribution of MTM to learning cross-channel dependencies within the channel-independent strategy" overstates originality. However, the paper is careful to qualify this within the CI strategy, and existing channel-dependent methods (Crossformer, iTransformer) operate outside this paradigm. No prior CI MTM method incorporates cross-channel information. The claim is appropriately scoped. **REMOVED — factually not a weakness.**

2. **"Missing related works"**: Neither reviewer raised this directly, but related criticism about not situating ShuffleMTM relative to supervised cross-channel methods is already handled in the paper's existing discussion (Section 2 notes differences in efficiency and scope). **REMOVED — already addressed.**

3. **"Implementation details absent from main text"** (paraphrased from Harsh Critic): The suggestion that hyperparameters (learning rate, batch size, etc.) should be in a dedicated table is a formatting preference; the paper states it follows settings from prior work (TimeSiam, iTransformer, CrossGNN), which is standard practice. **REMOVED — formatting/style preference.**

4. **"Strawman: Reproducibility concerns about training logs / large artifacts"**: Not applicable — no reviewer raised this. **REMOVED — not raised.**

5. **Generic strengths from Strength Finder that conflict with verified weaknesses**: No conflicts identified. All strengths are specific and evidence-grounded, so all are retained.

## Novel Insights

Beyond the paper's own contributions, a notable observation from synthesizing the reviews is that the shuffling mechanism creates an interesting middle ground between CI and channel-dependent modeling without requiring pairwise cross-attention (which scales quadratically in channels). The Siamese architecture means the encoder sees both a purely temporal view and a spatially-mixed view of the data, effectively performing a form of data augmentation that regularizes the learned representations. The capacity-robustness analysis (Fig. 9) concretely demonstrates that this design does not sacrifice the robustness advantages of CI models — a result that is not obvious a priori and that helps resolve a tension identified in prior work (Han et al., 2024). This insight could inform future pre-training designs that aim for the "best of both worlds" in multivariate time series.

## Suggestions

1. **Add the pre-training vs. from-scratch ablation.** Train ShuffleMTM end-to-end on downstream forecasting tasks without pre-training and compare to the pre-train + fine-tune version. This is the single highest-leverage experiment to strengthen the paper's core claim.
2. **Report variance for the main forecasting results** (std across the 5 runs, or at minimum a statement like "consistent across all 5 runs" for the 72/80 claim).
3. **Clarify baseline provenance** — explicitly state which numbers are re-computed and which are cited from prior tables.
4. **Expand classification evaluation** to at least 1–2 additional datasets outside the medical domain, or scope the claims accordingly.
5. **Add a brief limitations paragraph** covering the same-index shuffling constraint, low-channel-count cases, and computational overhead.
6. **Acknowledge the contemporaneous-only shuffling more explicitly** and, if feasible, add a synthetic experiment to test whether lagged dependencies are captured.

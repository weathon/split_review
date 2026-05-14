Now I have enough information to write the consolidated review. Let me synthesize everything.

---

## Summary

This paper proposes STBP, a framework for continual spatio-temporal forecasting that combines a frozen general-purpose backbone (with frequency-domain processing and linear attention) with an expandable contextual pattern bank that is fine-tuned incrementally. The backbone captures stable representations while the pattern bank adapts to new distributions and node additions. Experiments on three real-world streaming datasets (traffic and air quality) show consistent improvements over state-of-the-art CSTF methods, with MAE reductions of 21.44%, 21.93%, and 2.35% over the best competitor on PEMS-Stream, CA-Stream, and AIR-Stream, respectively.

## Strengths

- **Consistent and substantial performance gains across diverse streaming scenarios**: STBP outperforms all CSTF baselines on three datasets spanning gradual expansion (+33% nodes), explosive expansion (+254%), and stable expansion (+10%), reducing average MAE by 21.44%, 21.93%, and 2.35% respectively over the best competitor (Table 1). The improvements hold across all three forecasting horizons (3, 6, 12 steps) and are backed by low standard deviations from 5 runs.

- **Principled architecture design**: The separation of a frozen, general-purpose backbone (FreNet + DLGA) from an expandable contextual pattern bank is a clean and practical approach. The ablation study (Figure 4) confirms that both components are necessary — freezing the backbone while fine-tuning only the pattern bank significantly outperforms full retraining (Retrain) and full online fine-tuning (Online) across all three datasets.

- **Strong empirical support beyond averages**: Per-period results in the appendix (Tables 7, 8) show STBP achieves the best or near-best MAE on the vast majority of individual periods across all three datasets, not just on averages. The few-shot evaluation (Table 2, 10% training data) further demonstrates robustness, with STBP achieving 15.8% improvement over the best baseline on PEMS-Stream.

- **Comprehensive comparison with relevant baselines**: The evaluation includes 8 baselines spanning both conventional STGNNs (adapted for incremental training) and dedicated CSTF methods (TrafficStream, STKEC, PECPM, STRAP, EAC), providing a thorough assessment.

## Weaknesses

### Major

None.

### Minor

- **Forgetting measurement is indirect**: The paper claims to "alleviate catastrophic forgetting" but does not directly track performance on old node sets after learning new periods. The per-period evaluation tests on all current nodes (old + new), so if the model suffered significant forgetting, the metrics on later periods (which include old nodes) would degrade. STBP's MAE on PEMS-Stream improves monotonically (14.29 → 12.13 → 11.60 → 11.71 → 11.61 → 11.38 → 13.42), providing indirect evidence against catastrophic forgetting. However, a direct measurement (e.g., tracking MAE on the initial 655 nodes across all seven periods) would make the claim unambiguous.

- **Linear attention approximation (Eq. 9) lacks empirical validation**: The derivation in Appendix A.3.1 approximates Softmax(QK^T + QP^T) by splitting into two separately normalized linear attention terms. This is not a standard derivation — the softmax of a sum is not equal to the sum of separate softmaxes. While linear attention with random feature maps is well-established (Katharopoulos et al., 2020), the specific dual-stream formulation mixing representations with prompt keys is a custom construction. The paper provides no empirical comparison between the full quadratic attention (Eq. 8) and the linear approximation (Eq. 9) to verify that accuracy is preserved. Given that the DLGA module is a core component, this validation is needed.

- **Ablation study is informative but somewhat coarse**: The ablations test relatively high-level design choices (removing the entire DLGA module, replacing the entire backbone). Finer-grained ablations — such as ablating the FFT in FreNet, removing the P^(2) prompt key from attention, or comparing the gating mechanism against simple addition — would better isolate which specific design choices drive the gains. The current ablations show that the components matter but not exactly why.

- **Improvement on AIR-Stream is modest**: The 2.35% MAE reduction over EAC on AIR-Stream is small compared to the +21% gains on the traffic datasets. Per-period results (Table 8) show STBP is actually worse than EAC on the 2016 period (MAE 30.95 vs. 30.36), though it outperforms on the remaining three periods. The paper acknowledges this by describing AIR-Stream as a "cross-domain validation" but does not analyze why the gains are smaller in the air-quality domain.

- **Qualitative analysis without quantitative backing**: The t-SNE visualization and case study (Figures 3, 6) show interesting clustering behavior in the pattern bank, but no clustering quality metrics (e.g., silhouette score, cluster purity) are provided. The claim that clusters correspond to "meaningful spatio-temporal patterns" would be strengthened by quantitative evaluation.

### Trivial

None.

## Nice-to-Haves

- Direct forgetting measurement (tracking old nodes' performance across periods)
- Empirical comparison of full quadratic vs. linear attention on a subset
- Quantitative clustering metrics for pattern bank analysis
- A per-node error map showing prediction error on old vs. newly added nodes across periods

## Removed Points

These points were flagged by reviewers but are removed after verification against the paper:

1. "The paper does not actually measure catastrophic forgetting" — **Removed as overstated**. The evaluation tests on all current nodes (old + new) at each period. If catastrophic forgetting occurred, MAE would increase on later periods. STBP's MAE improves over time (Table 7), providing indirect but meaningful evidence. A direct measurement would be cleaner but the claim that the "experimental design cannot support the claim" is inaccurate.

2. "EAC in the ablation figure is a separate method, not an ablation" — **Removed**. The paper states: "We also include EAC, which follows a similar approach, for comparison in the ablation study" (Section 5.3). This is clearly labeled as an additional comparison.

3. "The efficiency scatter plot has overlapping labels and no tabular support" — **Removed**. This is a presentation/potentially parser artifact issue, not a substantive weakness.

4. "The 'adapted specifically for incremental training' phrase is vague" — **Removed**. The paper defines this: baselines like GWNet and STID are "initialized from the previous period's weights, enabling end-to-end fine-tuning" (lines 433-434). This is adequately clear.

5. "Section 5.2 — confidence intervals overlap" — **Weakened to minor**. The average MAE on AIR-Stream (24.21±0.43 vs. 23.64±0.23) has a small overlap at 1-sigma. The per-period exception (2016) is one of four periods, and STBP outperforms on the other three. This is minor.

6. "Section 4.2 — t-SNE is qualitative" — **Moved to minor/trivial**. The t-SNE is presented as a case study/visualization, not as rigorous proof. A quantitative metric would strengthen it.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a direct forgetting evaluation: after each incremental period, evaluate the model on only the original node set (or all previous test sets). This would directly validate the "mitigating catastrophic forgetting" claim.
2. Provide an empirical comparison of full quadratic attention (Eq. 8) vs. linear approximation (Eq. 9) on a subset, showing the accuracy-efficiency trade-off.
3. Add finer-grained ablations: ablate the FFT in FreNet, remove P^(2) from attention, or replace gating with simple addition, to isolate which components drive gains.
4. Include clustering quality metrics (e.g., silhouette score) for the pattern bank analysis.
5. Discuss the AIR-Stream results more thoroughly — why are gains smaller in this domain, and what does this imply about the method's cross-domain applicability?

## Score and Decision

**Calibration anchors used** (all from ICLR 2026 human review corpus):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/z45L1eYoHE.md` (SNIP) | 5.33 | Similar topic (expanding-node STF with prompting). STBP has stronger empirical evaluation (real streaming vs. synthetic splits) and larger gains, but SNIP does not face the forgetting-measurement concern. |
| `/home/wg25r/review_agent/human_reviews_2026/19LHXi9uLw.md` (EDGE) | 5.60 | Different domain (CIL evaluation protocol). Both have clear contributions with addressable weaknesses. Comparable quality. |
| `/home/wg25r/review_agent/human_reviews_2026/Ohq5sk3agt.md` (Memorization in CL) | 4.00 | Weaker — core conclusions insufficiently supported by experiments. STBP's empirical claims are better supported. |
| `/home/wg25r/review_agent/human_reviews_2026/68TggRP3Bb.md` (Scaling Law for Forgetting) | 2.00 | Much weaker — flawed theoretical assumptions and insufficient validation. STBP is far stronger empirically. |
| `/home/wg25r/review_agent/human_reviews_2026/uI4QK9LJlJ.md` (Less Forgetting Learning) | 3.00 | Weaker — memory-free CL with insufficient comparison. STBP has stronger baselines and results. |
| `/home/wg25r/review_agent/human_reviews_2026/b6Py2zy0fK.md` (PhySTA) | 5.33 | Accept poster. Comparable quality — both have clean architectures and solid experiments. |
| `/home/wg25r/review_agent/human_reviews_2026/P1PZBR6a4S.md` (SONATA) | 5.50 | Accept poster. Comparable — both propose novel frameworks with thorough empirical evaluation. |
| `/home/wg25r/review_agent/human_reviews_2026/1CR1MTIgmq.md` (False/misleading claims) | 0.00 | Much weaker — fundamentally flawed work. Not comparable. |

STBP is stronger than SNIP (avg 5.33, rejected) and comparable to EDGE (avg 5.60, accepted poster), PhySTA (avg 5.33, accepted poster), and SONATA (avg 5.50, accepted poster). The forgetting measurement concern is real but not fatal (the evaluation provides indirect evidence). The attention approximation lacks validation but is addressable. The core contributions — the architecture design and strong empirical results — are solid.

**Decision**: Accept (Poster)
**Score**: 5.5

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
Now I have a thorough understanding of the paper and the calibration landscape. Let me produce the final review.

## Summary of Calibration

**Round 1 Bracket**: Based on the topic-anchored queries (spatio-temporal continual forecasting graph neural network), the low-band (<3.5) contained papers in tangentially related areas, the mid-band (3.5-7.5) contained the most relevant anchors including the EAC paper (6.75, Accept) and SKI-CL (5.33, Reject), and the high-band (>7.5) contained papers from different subfields. The weakness-anchored queries revealed that papers with missing per-period evaluation or evaluation inconsistencies tend to score in the 3-5.5 range.

**Round 2 Narrowing**: Within the 4.0-6.5 bracket, anchors included C²INet (4.67, Reject), UrbanDiT (4.20, Reject), KITS (5.67, Reject), and others. Compared to these, the paper under review has stronger novelty and empirical breadth but also has more significant evaluation inconsistencies.

**Low-band anchor failures**: The low-band topic anchors failed due to narrow scope, weak baselines, or unclear methodology. The paper under review shares some of these failures — specifically the evaluation inconsistency and underspecified methodology — but has stronger empirical results and clearer contributions, placing it above the low-band.

**Anchors considered**:
- FRzCIlkM7I (EAC paper, 6.75, round1-topic-mid): The strongest baseline in this paper; accepted with scores 3/8/8/8. This paper has a cleaner evaluation but a simpler method.
- URCfZ2NgaR (SKI-CL, 5.33, round1-topic-mid): Continual MTS forecasting, rejected. Similar evaluation concerns about missing baselines.
- mkjKqeBXkt (KITS, 5.67, round2): Spatio-temporal kriging, rejected. Good empirical results but concerns about methodology and evaluation.
- 5IvTw0qMKj (C²INet, 4.67, round2): Continual trajectory prediction, rejected. Concerns about evaluation and methodology clarity.
- H8oCwBTDMv (UrbanDiT, 4.20, round2): Urban spatio-temporal foundation model, rejected. Limited novelty concerns.
- 0je4SA7Jjg (CeGNN, 3.40, round1-topic-low): Spatiotemporal learning on PDE, low score due to weak baselines and unclear experiments.

**Final score rationale**: The paper under review proposes a genuinely interesting combination of ideas (frequency-domain backbone + contextual pattern bank for CSTF). The main results are strong and the few-shot and efficiency analyses are valuable. However, the ablation inconsistency — where EAC's performance in the ablation (~26 MAE on PEMS-Stream) differs dramatically from the main results (15.67 MAE) — is a significant concern that undermines the component analysis. Additionally, the lack of per-period evaluation is a standard expectation for continual learning papers. These issues prevent the paper from reaching the level of the EAC anchor (6.75) and place it alongside papers with evaluation concerns (4.5-5.5 range). Score: 4.5.

---

## Summary

The paper proposes STBP, a framework combining a frequency-domain spatio-temporal backbone with a scalable contextual pattern bank for continual forecasting in streaming scenarios. The backbone uses FreNet for frequency-domain stabilization and Dual-Stream Linear Graph Attention for efficient spatial modeling, while the pattern bank retains node-specific knowledge via parameter expansion. The paper shows strong results on three real-world datasets.

## Strengths

1. **Consistent SOTA results across multiple datasets.** Table 1 shows STBP achieves the lowest MAE/RMSE/MAPE on PEMS-Stream, CA-Stream, and AIR-Stream, with MAE reductions of 21.44%, 21.93%, and 2.35% over the best baselines. The results are reported with standard deviations across horizons.

2. **Ablation study design is conceptually sound.** The ablation variants (Retrain, Online, w/o Backbone, w/o DLGA) test distinct design hypotheses. The relative ordering — where removing each component degrades performance — is consistent with the paper's claims about component necessity.

3. **Few-shot and efficiency evaluations strengthen the practical claims.** Table 2 shows STBP maintains large margins under 10% training data (e.g., MAE 13.58 vs. EAC 16.13 on PEMS-Stream). Figure 8 demonstrates competitive or better efficiency despite a more complex backbone.

## Weaknesses

### Major

1. **Critical inconsistency between ablation results and main results.** The ablation study (Figure 4) reports EAC achieving roughly ~26 MAE on PEMS-Stream, while the main results (Table 1) list EAC's average MAE as 15.67 — a ~66% relative discrepancy. Even the paper's own method ("Our") differs (~15 in ablation vs. 12.31 in Table 1). The paper provides no explanation for this mismatch (different data splits, hyperparameters, or incremental periods). Since the ablation is central to validating component contributions, this inconsistency severely undermines confidence in the experimental evaluation. The authors must clarify the exact protocol used in the ablation and resolve this discrepancy.

2. **Missing per-period evaluation for continual learning.** The paper reports only metrics averaged across all incremental periods (Table 1). In a continual learning scenario where the stated goal is to mitigate catastrophic forgetting, per-period results are essential to show whether performance on earlier periods degrades after later training. Without per-period breakdowns or backward transfer measures, the core claim of alleviating forgetting is not empirically supported.

### Minor

3. **Under-specified methodology in key components.** Equation (5) defines a gating operation where h_θ is described as "an arbitrary submodule within the backbone" — it is unclear at which architectural points the gating is applied, how many times, and whether the same submodule is used. The DLGA attention definition (Equation 9) says "Softmax used for approximation" alongside a random feature mapping φ, conflating two different linear-attention families. These ambiguities hinder independent reproduction.

4. **Baseline tuning not described.** The paper reports large improvements over CSTF baselines (e.g., 21.44% on PEMS-Stream) but does not describe any hyperparameter tuning procedure for the baselines or state whether official hyperparameters were used. While the improvements may be genuine, the lack of tuning transparency leaves room for concern about fair comparison.

### Trivial

5. The number of incremental periods and expansion schedule for each dataset are not stated in the main text (presumably in the appendix).
6. No ablation replaces FreNet with a conventional temporal module (e.g., TCN) to isolate its contribution; the "w/o Backbone" variant replaces the entire backbone.

## Nice-to-Haves

- Adding per-period results (tables or curves) would directly address the forgetting analysis gap.
- An ablation replacing FreNet with a TCN module would better isolate the frequency-domain contribution.
- Ablations removing the P⁽²⁾ key or using standard full attention instead of linear attention would further validate design choices.

## Removed Points

- **Weakness about t-SNE visualization being "expected behavior":** This criticism is speculative. While node-specific embeddings may naturally cluster, the paper uses this as qualitative evidence, not a rigorous claim. It is not a concrete error.
- **Weakness about missing "w/o Backbone" being insufficient for isolating FreNet:** Already noted as a minor point above. The reviewer's framing as a major omission is overstated — the w/o Backbone variant tests the backbone's overall value.
- **Strength about t-SNE visualization as "interpretable behavior":** This is a weak strength (qualitative only). Removed as it depends on speculation about what "expected" behavior would be.
- **Strength about writing/positioning:** Generic praise. The paper is adequately written but not exceptionally so.

## Novel Insights

None beyond the paper's own contributions. The combination of frequency-domain temporal modeling with prompt-based pattern bank for CSTF is the paper's main novel insight. The reviews surface no deeper observations.

## Suggestions

1. Resolve the ablation inconsistency by explicitly reporting the experimental conditions (channel dimensions, data split, number of periods) for each ablation variant and ensuring they match the main protocol.
2. Add per-period forecasting results (at least for one dataset) to demonstrate forgetting/backward transfer.
3. Clarify the prompt-based guidance mechanism by specifying exactly which sub-modules are gated and the dimensionalities of all pattern bank groups.
4. Describe the baseline tuning procedure or report that official hyperparameters were used.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
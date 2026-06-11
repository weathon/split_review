## Summary

The paper proposes SigMap, a multimodal foundation model for wireless localization that introduces two innovations: (1) cycle-adaptive masking for self-supervised pre-training that dynamically adjusts masking patterns based on CSI periodicity, and (2) a "map-as-prompt" framework that encodes 3D geographic information via GNNs into soft prompts for cross-scenario adaptation. Experiments on DeepMIMO and WAIR-D datasets show strong localization accuracy in both single-BS and multi-BS settings, with substantial gains over CSI-only baselines and promising zero-shot generalization.

## Strengths

- **Large and consistent accuracy margins over all baselines**: SIGMAP with map achieves 1.564 m MAE vs. 2.382 m for the best baseline (LWLM) in single-BS NLoS — a 34.4% improvement — and more than doubles CDF@1m (60.5% vs. 25.3%). In multi-BS (Table 2), it achieves 0.673 m MAE vs. 0.828 m (18.7% improvement). These margins hold across both tasks, providing direct empirical evidence that the combined approach delivers genuinely better localization.

- **Strong cross-scenario generalization with minimal parameter updates**: Section 4.5 evaluates on two completely unseen ray-tracing suites (DeepMIMO O2 and WAIR-D Scenario-2). SIGMAP achieves 1.026 m MAE vs. LWLM's 2.213 m on DeepMIMO O2 (53.2% improvement) and 1.880 m vs. 3.375 m on WAIR-D (44.3% improvement), while updating only 0.7% of total parameters (0.085M of 11.73M, Table 5). This concretely supports the claimed few-shot generalization to new environments.

- **Ablation evidence supports both architectural choices**: Table 3 shows adaptive masking (0.673 m MAE, 84.5% CDF@1m) outperforms both grid-masking (0.770 m, 80.3%) and strip-masking (0.753 m, 75.3%), supporting the claim that periodicity-aware masking prevents shortcut learning. Table 4 shows graceful degradation from 3-D mesh (1.564 m MAE) → 2-D birdview (1.692 m, 8% degradation) → no-map (2.275 m, 45% degradation), confirming the prompt mechanism captures topological/LoS cues rather than overfitting to 3-D detail.

## Weaknesses

### Fatal
None.

### Major

- **No baseline that also uses map information, so the prompt mechanism's specific value is unisolated**: The paper's headline innovation is the "map-as-prompt" framework, yet every baseline (OMP, CNN, SWiT, LWLM) uses CSI only. The ablation shows SIGMAP (w/ map) outperforms SIGMAP (w/o map), but this only proves that having map data helps — not that the *specific prompt mechanism* is superior to alternative ways of incorporating map information (e.g., concatenating GNN features with CSI features, or late fusion). The gap between SIGMAP (w/ map) and SIGMAP (w/o map) in single-BS (1.564 vs. 2.275 m) is larger than the gap between SIGMAP (w/o map) and the best CSI-only baseline, suggesting the presence of map data is the dominant source of improvement. Without a map-aware baseline, the reader cannot determine whether the prompt design itself adds value beyond making map data available. This is the single most important gap in the evaluation.

- **Cycle-adaptive masking mechanism is critically underspecified for a core contribution**: Equation (6) defines the mask pattern conditioned on a detected periodicity shift `d_final`, but the paper never specifies: (a) what cross-correlation is computed (auto-correlation along subcarriers? cross-correlation between antenna pairs?), (b) how `d_final` is extracted from the correlation function (peak detection? thresholding?), (c) how the mask width `w` and starting offset `j_0` are set, or (d) whether the mask is generated per sample, per batch, or globally. The "row-wise cross-correlation" mentioned in Section 1.2 is never defined in the methodology. For a mechanism presented as a primary contribution, this level of underspecification prevents reproduction and independent verification.

### Minor

- **No variance or significance reporting despite 5-run averaging**: The paper states all results are averaged over 5 independent runs but reports no standard deviations, confidence intervals, or significance tests. Several comparisons involve modest gaps (e.g., SIGMAP w/o map at 2.275 m vs. LWLM at 2.382 m, a 4.5% difference) where error bars would meaningfully change interpretation. This is standard practice to address in this field.

- **RMSE inconsistency in masking ablation (Table 3)**: Adaptive masking achieves worse RMSE (1.099 m) than strip-masking (0.972 m) — a 13% degradation — while improving MAE and CDF@1m. The paper claims "best trade-off" without acknowledging or explaining this pattern, which is relevant for applications sensitive to worst-case errors.

- **NLoS-aware attention (Equation 11) introduced in results without prior methodology**: Section 4.2 introduces an attention mechanism described as the source of the "key advantage" for single-BS localization, yet this mechanism was never described in Section 3 (Methodology). It is unclear whether Eq. (11) is part of the model, a separate mechanism, or an illustration of a concept.

- **Textual inconsistencies**: The WAIR-D MAE is reported as 1.880 m in the generalization table but as "1.580 m" in the main text (line 340). The text states "0.4% of parameters" while Table 5 and its caption indicate 0.7% (0.085 M / 11.73 M). These suggest sloppy final preparation.

- **Radar chart (Figure 5) includes undefined metrics**: Labels like "oss_scenario", "AoA", "ToA" that appear in the radar chart are never defined or discussed in the experimental setup. The paper's evaluation section only reports MAE, RMSE, and CDF@1m.

### Trivial
None beyond the textual inconsistencies listed above.

## Nice-to-Haves
- A clearer explanation of the NLoS-aware attention mechanism (Eq. 11) and how it differs from the multi-BS attention (Eq. 9) would help readers understand the full model.
- Qualitative analysis of learned prompts (e.g., attention weight visualizations, case studies of NLoS disambiguation) would strengthen the interpretability claims.
- Discussion of simulation-to-reality gaps, even if brief, would contextualize the practical deployability claims.

## Removed Points
- **Criticism about no real-world measurements**: The paper uses standard simulated datasets (DeepMIMO, WAIR-D) that are standard in this field. Demanding real-world data exceeds the paper's stated scope. REMOVED.
- **Criticism about missing baselines from related work (CrowdBERT, WirelessGPT, etc.)**: The paper cites these as related work but does not claim experimental comparison. Not comparing against every related method is normal. REMOVED.
- **Criticism about transformer backbone being underspecified**: The paper references Appendix B for architectural details, which is stripped from this PDF. REMOVED per instructions.
- **Strength claim that "ablation cleanly isolates the benefit of cycle-adaptive masking"**: Partially weakened by the RMSE inconsistency in Table 3. Downgraded to supporting-with-caveat.

## Novel Insights
None beyond the paper's own contributions. The reviews surface a clear evaluation gap (missing map-aware baseline) that is central to the paper's claims — this is the kind of gap that a good reviewer should catch, and it is the deciding factor between this being a strong paper and a borderline one.

## Suggestions
1. **Add at least one map-aware baseline** — e.g., a version where GNN-extracted map features are concatenated with CSI features rather than injected as soft prompts, or a version using late fusion. This is essential to demonstrate that the prompt design itself adds value.
2. **Fully specify the cycle-adaptive masking pipeline** — define the cross-correlation computation precisely, explain how `d_final` is derived from the correlation function, describe how `w` and `j_0` are selected, and clarify whether masking is per-sample or global.
3. **Report standard deviations or confidence intervals** for all main results (Tables 1–4).
4. **Acknowledge and explain the RMSE pattern** in Table 3 — why does adaptive masking produce worse RMSE than strip-masking?
5. **Resolve the WAIR-D MAE and parameter-percentage inconsistencies** in the text.
6. **Clarify the relationship between Equations (9) and (11)**, and if Eq. (11) is a separate mechanism, move it to the Methodology section.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
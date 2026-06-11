## Summary
This paper identifies and formalizes the Dual-level Noisy Correspondence (DNC) problem in multi-modal entity alignment (MMEA), where noise exists in both intra-entity (entity-attribute) and inter-graph (entity-entity and attribute-attribute) correspondences. The proposed RULE framework addresses this through: (1) reliability estimation using uncertainty (Dempster-Shafer Theory) and consensus principles to identify noisy pairs, (2) robust learning losses (DRL for inter-graph, DRF for intra-entity) adapted to estimated noise levels, and (3) a test-time correspondence reasoning (TTR) module using Qwen2.5-VL-72B-Instruct with CoT prompting. Experiments on five benchmarks show substantial improvements over seven baselines under clean and noisy settings.

## Strengths
- **Well-formalized novel problem with theoretical grounding**: The DNC problem is precisely defined with binary indicators for entity-attribute (*h_i^m*), entity-entity (*y_ij*), and attribute-attribute (*y_ij^m*) correspondences (Section 2.1). Theorem 1 (Eq. 4) formally proves that uncertainty alone is insufficient for identifying noisy correspondences, providing rigorous motivation for the consensus principle — not just a heuristic design.
- **Nuanced three-way noise handling with tailored losses**: The pair division into S_U (high uncertainty), S_I (low consensus), and S_C (clean) with distinct loss strategies (Eqs. 11–13) — excluding S_U entirely, refining S_I with soft interpolation via Eq. 12, and training normally on S_C — is more sophisticated than standard sample reweighting.
- **Large and consistent experimental gains verified across five benchmarks**: On ICEWS-WIKI with inherent DNC (Table 1), RULE achieves 64.2% H@1 vs. PMF's 52.6% (+11.6). At 50% DNC, the gap widens to 58.2 vs. 35.1 (+23.1). Fig. 3(a) shows RULE degrades gracefully from ~64 to ~56 H@1 as DNC ratio increases from 0 to 0.7, while PMF drops from ~53 to ~35.
- **Comprehensive ablation clearly isolating contributions (Table 3)**: Removing DRL drops Non-name H@1 from 58.2 to 31.6 (−26.6). "Only Unc." (53.5) and "Only Cons." (48.3) both outperform "w/o DRL" (31.6), validating both principles contribute independently. Reliability distribution plots (Figs. 3b, 4) empirically confirm the noise identification mechanism works as designed.

## Weaknesses

### Fatal
None.

### Major
- **Presentation conflates training-time robustness with test-time MLLM capacity**: The headline results in Tables 1–2 present the full RULE system (which invokes Qwen2.5-VL-72B-Instruct at test time) alongside baselines with no comparable capability. The ablation in Table 3 reveals the true picture: on Non-name, training-time robustness drives +24.9 H@1 (w/o DRL: 31.6 → w/o TTR: 56.5), while TTR adds only +1.7 H@1 (56.5 → 58.2). Furthermore, the "MLLM Enhance" row achieves 56.6 vs. 56.5 for "w/o TTR" — essentially zero signal from the MLLM alone on name-deprived alignment. The paper should foreground the training-only result as the primary contribution rather than bundling a 72B MLLM into headline numbers.

- **Self-referential threshold estimation without stability analysis**: The pair division thresholds (Eq. 8) depend on S^{TP} = {*i* | argmax(*s_i*) = argmax(*y_i*)}, creating a circular dependency where model predictions determine thresholds, which determine training signal, which shapes predictions. The paper provides no warmup analysis, no discussion of initialization sensitivity, and no demonstration that S^{TP} accuracy stabilizes during training. This is load-bearing for the entire noise-identification pipeline.

### Minor
- **Assumption 1 (marginal contribution) lacks empirical validation**: The assumption that correct entity-attributes yield Δ ≥ 0 while irrelevant ones yield Δ < 0 (lines 120–121) is stated without formal justification or empirical hit-rate measurement. An irrelevant attribute could have positive marginal contribution via surface similarity; a correct one could have negative contribution if genuinely hard to match. This feeds directly into the greedy correspondence estimation (Eq. 7) and consensus computation.
- **No variance or confidence intervals reported**: All results are single-run numbers. Given the method involves threshold estimation potentially sensitive to initialization, reporting at least 3 runs with standard deviations would strengthen confidence.
- **TTR module analysis is insufficient**: The finding that the MLLM alone provides nearly zero signal on Non-name (56.6 vs. 56.5 in Table 3) deserves substantially more discussion. Additionally, there is no analysis of inference cost for the 72B model, no comparison with smaller MLLMs, and no case-level analysis of when TTR helps vs. hurts.

## Nice-to-Haves
- Report Non-name training-only ablation prominently as the headline story — training-time robustness (+24.9 H@1) is the real contribution.
- Analysis of when TTR helps vs. hurts across datasets (it appears more helpful on ICEWS than DBP15K).
- Sensitivity analysis to MLLM model size (7B, 14B, 72B) to clarify if TTR requires frontier-scale models.
- Discussion of computational cost for running a 72B MLLM at test time for every query against all candidates.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **HHREA's anomalous underperformance on DBP15K (~30 H@1 below other methods in Non-name)**: This is a property of the baseline, not a flaw in this paper. All methods use the same CLIP backbone, so this gap may reflect architectural differences in HHREA.
- **All-attributes setting being less informative (name dominates >95 H@1)**: This is a property of the evaluation protocol common in the field, not a flaw in this paper.
- **Score combination *s_i^joint = s_i + ŝ_i* being "crude"**: Simple addition is a reasonable default; no evidence it fails in practice.

## Novel Insights
The paper's most genuinely novel insight — validated by its own ablation — is that training-time robustness to dual-level noise is far more impactful than test-time MLLM augmentation for MMEA. The +24.9 H@1 gain from DRL alone (Non-name, 50% DNC) versus +1.7 H@1 from TTR demonstrates that noise-robust training is the critical bottleneck in noisy MMEA, not inference-time reasoning. The two-fold reliability estimation combining uncertainty and consensus is also a genuine methodological contribution, as Theorem 1 formally justifies why uncertainty alone is insufficient.

## Calibration Reporting

**All anchors retrieved across rounds:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| 9Cu8MRmhq2.md — "Multi-granularity Correspondence Learning from Long-term Noisy Videos" | 8.00 | R1 | Similar concept (noisy correspondence in multi-modal), unanimously scored 8. Reviewed paper has comparable novelty but more identified weaknesses. |
| TPZRq4FALB.md — "Test-time Adaptation against Multi-modal Reliability Bias" | 8.00 | R2 | Test-time multimodal adaptation with reliability estimation. Similar theme, different domain. Scored 8. |
| z3dfuRcGAK.md — "Revisit and Outstrip Entity Alignment" | 6.67 | R1 | Entity alignment with generative models. Reviewed paper is stronger: better formalization, larger improvements, more comprehensive evaluation. |
| DKgAFfCs5F.md — "Cocoon: Robust Multi-Modal Perception" | 6.00 | R2 | Uncertainty-aware multi-modal fusion with modest gains. Reviewed paper has much larger improvements and more complete framework. |
| NNUiUwQWx6.md — "Neuro-symbolic Entity Alignment" | 5.75 | R1 | Entity alignment, rejected at 5–6 range. Reviewed paper is clearly stronger. |
| B5VEi5d3p2.md — "SleepSMC: Ubiquitous Sleep Staging" | 5.75 | R2 | Multimodal coordination. Less relevant but informative for calibration. |
| HhP9bgCugr.md — "Align-VL" | 4.75 | R1 | Multimodal alignment with noisy data, rejected. Reviewed paper is substantially stronger. |
| DWWwGlPMFr.md — "LEMoN" | 5.25 | R1 | Label error detection in multimodal datasets, rejected. Reviewed paper is clearly stronger. |
| MCUvAc1GTg.md — "Network Alignment with Transferable Graph Autoencoders" | 5.50 | R1 | Network alignment. Rejected. Reviewed paper is stronger. |
| er7VhmqZEA.md — "Noisy Multi-View Contrastive Learning" | 4.00 | R1 | Noisy contrastive learning for recommendation. Rejected. Much weaker than reviewed paper. |
| a4O528mek9.md — "Learning Multi-modal Representations Under Incomplete Data" | 3.00 | R1 | Multi-modal representations with noisy data. Rejected. Reviewed paper far stronger. |
| rwdeKOdAwY.md — "RetFormer" | 3.00 | R1 | Multimodal retrieval. Rejected. Much weaker. |

**Round 1 bracket**: Between 6.0 and 8.0. The paper is clearly above the 5–6 range (rejected entity alignment and multimodal papers), comparable to Cocoon (6.00) but with stronger results, and approaching Norton (8.00) in novelty but with more identified weaknesses.

**Final calibration**: 7.0. The paper makes a genuine, well-supported contribution to MMEA robustness with large margins and comprehensive evaluation. The core training-time robustness (DRL+DRF) is strong and responsible for the bulk of gains. However, the presentation issue (headline numbers inflated by 72B MLLM), the self-referential threshold concern, and the lack of Assumption 1 validation prevent a higher score. This is a clear accept.

## Suggestions
- Restructure Tables 1–2 to show "RULE (training only)" as the primary result with TTR as a supplementary row.
- Add warmup analysis for threshold estimation: plot S^{TP} accuracy across training epochs to demonstrate stability.
- Empirically validate Assumption 1 by measuring the fraction of correct/incorrect attributes satisfying the predicted sign of Δ.
- Add inference time/cost analysis for the TTR module and compare with smaller MLLMs.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
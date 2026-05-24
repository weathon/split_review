Now I have all the information I need. Let me compile the final review.

---

## Summary

SigMap proposes a wireless localization foundation model with two core innovations: (1) a **cycle-adaptive masking** strategy for self-supervised pre-training that adaptively disrupts periodic CSI patterns, and (2) a **map-as-prompt** framework that encodes 3D building geometry via a GNN and injects it as soft prompts for parameter-efficient fine-tuning. Experiments on simulated ray-traced datasets (DeepMIMO, WAIR-D) show consistent improvements over CSI-only baselines, with MAE reductions of 14–34% and strong few-shot generalization to unseen environments.

## Strengths

- **Cycle-adaptive masking is a well-motivated and empirically effective contribution.** Table 3 shows it achieves 0.673 m MAE and 84.5% CDF@1 m, clearly outperforming grid-only (0.770 m, 80.3%) and strip-only masking (0.753 m, 75.3%). The physical insight—that periodic shortcuts degrade learned representations—is sound and supported by the ablation.

- **The map-as-prompt idea is novel and delivers clear gains.** Tables 1, 2, and 4 show that incorporating 3D map prompts reduces MAE by 31% in single-BS (1.564 vs. 2.275 m) and 14.7% in multi-BS (0.673 vs. 0.789 m) compared to the map-free variant. The paper also honestly reports that a 2D bird's-eye polygon retains most of the benefit (1.692 m vs. 1.564 m), which correctly isolates the role of 3D geometry versus topological cues.

- **Strong few-shot generalization with parameter-efficient fine-tuning.** On unseen DeepMIMO O2 and WAIR-D Scenario-2, SigMap (w/ map) achieves 1.026 m and 1.880 m MAE respectively, outperforming LWLM by 53.2% and 44.3%, while updating only ~0.7% of parameters (Table 5). The 30-minute fine-tuning time is practically appealing.

- **Comprehensive ablation structure.** The paper systematically ablates the masking strategy (Table 3), map quality (Table 4), and generalization (Table 4.5), allowing readers to attribute improvements to specific components.

## Weaknesses

### Major

- **Numerical inconsistencies erode trust.** The WAIR-D generalization table shows **1.880 m** MAE for SigMap (w/ map), but the text says **1.580 m** (Section 4.5, lines 348 vs. 352). The parameter efficiency claim is also inconsistent: the text says "0.4% of parameters" (line 352) while Section 4.6 says "0.7% of the total parameters" (line 364); 0.085 M / 11.730 M = 0.72%, so 0.4% is simply wrong. These are not minor typos—they undermine confidence in all reported numbers.

- **The NLoS-aware attention mechanism (Equation 11) appears without definition or methodological grounding.** Equation (11) is introduced in Section 4.2 as explaining the "key advantage" of the method, but the symbols φ and **oₛ** are never defined, and this mechanism is not described in Section 3 (Methodology) or in the architecture diagram (Figure 2). It is unclear whether this is a separate architectural component, a reformulation of the multi-BS attention in Equation (9), or something else entirely. The reader cannot determine the actual model architecture from the paper as written.

- **The cycle-adaptive masking algorithm is irreproducible.** The core of the pre-training mechanism—the quantity `d_final` (detected periodicity shift) in Equation (6)—is never defined. The paper says it is computed "using cross-correlation analysis" but provides no algorithm, no equations, and no description of whether it is computed per-sample, per-batch, or globally. This is a significant reproducibility gap.

- **Missing map-aware baselines weaken the core evaluation.** The headline claim of "34.4% improvement" compares SigMap (CSI + 3D map) against baselines that receive only CSI. The key scientific question is whether the *specific mechanism* of map integration (GNN → soft prompts) is better than simpler alternatives for incorporating the same map information (e.g., concatenating GNN-pooled map features, cross-attention between map and CSI tokens, or adding map features as extra input channels). The paper provides only a w/ map vs. w/o map ablation; it does not test whether the prompt mechanism itself is the best way to fuse map information. This comparison is necessary to support the claimed contribution of the "map-as-prompt" method over generic map fusion.

- **"Zero-shot" is mischaracterized.** The abstract and contributions section claim "strong zero-shot generalization," but the generalization experiment (Section 4.5) uses ~100 labeled samples per target scenario for fine-tuning, which is few-shot learning. The paper itself calls this a "few-shot learning setup" (line 329). This is a misleading terminology mismatch.

### Minor

- **Adaptive masking anomaly unexplained.** Table 3 shows that adaptive masking achieves better MAE (0.673 m) but *worse* RMSE (1.099 m) than strip-masking (0.972 m). This means the adaptive strategy produces larger tail errors. The paper dismisses this as "the best trade-off" without analysis. For a localization system, tail error behavior is critically important and deserves explanation.

- **Figure 5 radar chart uses undefined metrics.** The paper's evaluation only defines MAE, RMSE, and CDF@1 m. Yet the radar chart reports "oss_scenario," "AoA," and "ToA" as separate metrics without any definition of how they are measured or computed. AoA and ToA are introduced as classical physical parameters in Section 1 but are not used as evaluation metrics anywhere in the experiments.

- **No variance reporting despite claiming 5-run averages.** The paper states that results are averaged over 5 runs but reports no standard deviations, confidence intervals, or significance tests for any table. This makes it impossible to assess the statistical reliability of the reported differences.

- **No real-world validation.** All experiments use simulated ray-traced data (DeepMIMO, WAIR-D). While WAIR-D uses real-world map layouts, the CSI is simulated. Given that the map is perfectly known during both data generation and inference in simulation, real-world performance where maps are inaccurate or incomplete remains unvalidated. This should be acknowledged as a limitation.

### Trivial

- The paper states "SIGMAP (w/ map) achieves 1.564 m" in single-BS but the "w/ map" and "w/o map" comparison in Table 2 at multi-BS shows SIGMAP (w/o map) already outperforms LWLM. The abstract framing could better separate the backbone contribution from the map contribution.

## Nice-to-Haves

- A comparison against simpler map fusion baselines (concatenation, cross-attention) would substantially strengthen the paper's central claim about the prompt mechanism.
- Visualizing the learned attention weights from the multi-BS fusion (Equation 9) across different geometric configurations would support the claim that the model "dynamically prioritizes" base stations based on signal quality and geometry.
- Providing the cross-correlation algorithm for computing `d_final` would make the pre-training reproducible.

## Removed Points

- *Criticism about missing training split details, number of users, and LoS/NLoS distribution*: The paper states these are in Appendix B.3, which was stripped by the parser. Removed per the rule that missing appendix content is a parser artifact.
- *Criticism about missing CrowdBERT as a baseline*: The paper cites CrowdBERT as related work, but requiring every related method as a baseline is scope expansion. Removed.
- *Criticism about Delaunay triangulation cost and 2-layer GCN being too shallow*: These are speculative concerns not evaluated against evidence in the paper. Removed.
- *Criticism about 1000 epochs of fine-tuning being slow*: 30 minutes for full fine-tuning with 0.7% parameter update rate is standard in this domain. Removed.
- *Strength claim about "physically motivated masking strategy defined mathematically"*: Kept but downgraded given that `d_final` is undefined, making Equation (6) incompletely specified.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix all numerical inconsistencies.** Resolve the 1.580 vs. 1.880 WAIR-D discrepancy and the 0.4% vs. 0.7% parameter-count mismatch. Add standard deviations to all tables.
2. **Define `d_final`.** Provide the cross-correlation algorithm used for periodicity detection in the main text or a supplementary algorithm box.
3. **Clarify or remove Equation (11).** Either integrate the NLoS-aware attention mechanism into Section 3 with full definitions of φ and **oₛ**, or remove it if it is redundant with Equation (9).
4. **Add at least one map-aware baseline.** Compare the prompt-based fusion against a simple concatenation of GNN-pooled map features with CSI tokens in the fine-tuning setting.
5. **Replace "zero-shot" with "few-shot"** where appropriate.
6. **Explain the adaptive masking RMSE discrepancy** with a residual analysis or CDF curves comparing the tail behavior.
7. **Define the radar chart metrics** in the evaluation section, or replace the chart with metrics that are actually evaluated.

## Score and Decision

### Calibration

**Round 1 — Bracketing (score bands):**
- Weak anchors (avg < 3.5): m9BiWVTJDx (3.00), xJ5CF1aOOX (2.50), ReccFdn4zE (2.00), q4cfN6PGY7 (3.00) — clearly below this paper.
- Middle anchors (3.5–7.5): 9TClCDZXeh (7.00, Wi-GATr — differentiable wireless simulation), 7KDuQPrAF3 (6.25, FECCT — foundation model for ECC), 29JDZxRgPZ (6.00, EM-GANSim), uiBLOcyTIA (5.25, NextLocLLM).
- Strong anchors (avg > 7.5): NN6QHwgRrQ (8.00), kxnoqaisCT (7.75) — not topically related; SigMap is clearly below these.

**Initial bracket: between 4.5 and 6.5.**

**Round 2 — Narrowing (4.5–6.5):**
- 29JDZxRgPZ (6.00, EM-GANSim — Reject): Simulated wireless propagation, underspecified architecture, missing baselines. SigMap has stronger methodological novelty (cycle-adaptive masking, map-as-prompt) but also has concrete numerical errors that EM-GANSim does not. Comparable quality.
- Iip7rt9UL3 (4.75, Presto — Reject): SSL for remote sensing, limited novelty, small performance gains. SigMap has clearer contributions and larger improvements.
- 7ipjMIHVJt (5.25, DASFormer — Reject): SSL for earthquake monitoring, missing baselines, methodological concerns. Similar profile — novel application of SSL with evaluation limitations.
- 9TClCDZXeh (7.00, Wi-GATr — Accept): Well-executed with real-world validation. SigMap is clearly below this.

**Final position:** SigMap has genuine novelty (cycle-adaptive masking, map-as-prompt) and strong empirical gains, but the numerical inconsistencies (1.580 vs. 1.880, 0.4% vs. 0.7%), underspecified components (d_final, NLoS attention), and missing map-aware baselines place it below well-executed papers like Wi-GATr (7.00). It compares most closely to EM-GANSim (6.00, Reject) and DASFormer (5.25, Reject) in terms of overall quality — interesting ideas with evaluation gaps that prevent acceptance in current form.

All anchors retrieved:
| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| m9BiWVTJDx | 3.00 | R1 | SigMap is clearly stronger |
| xJ5CF1aOOX | 2.50 | R1 | SigMap is clearly stronger |
| ReccFdn4zE | 2.00 | R1 | SigMap is clearly stronger |
| q4cfN6PGY7 | 3.00 | R1 | SigMap is clearly stronger |
| 9TClCDZXeh | 7.00 | R1,R2 | SigMap is weaker — lacks real-world validation and clean execution |
| 7KDuQPrAF3 | 6.25 | R1 | Comparable ambition, SigMap has more concrete numerical errors |
| 29JDZxRgPZ | 6.00 | R1,R2 | Similar quality profile — SigMap has more novelty but more errors |
| uiBLOcyTIA | 5.25 | R1 | SigMap is somewhat stronger in novelty |
| NN6QHwgRrQ | 8.00 | R1 | Not topically comparable, clearly stronger |
| kxnoqaisCT | 7.75 | R1 | Not topically comparable, clearly stronger |
| 7gUrYE50Rb | 8.00 | R1 | Not topically comparable |
| HnhNRrLPwm | 8.00 | R1 | Not topically comparable |
| Iip7rt9UL3 | 4.75 | R2 | SigMap has clearer contributions |
| 7ipjMIHVJt | 5.25 | R2 | Similar quality profile |
| Pj3ErOxlLo | 6.00 | R2 | Similar quality |
| MW8DN8BE3g | 6.25 | R2 | Similar quality |

**Decision:** The paper introduces genuinely interesting ideas and shows competitive empirical results. However, the numerical inconsistencies, underspecified core mechanisms, and missing map-aware baselines are substantive issues that prevent acceptance in the current form. The paper would benefit from a careful revision addressing these concerns.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
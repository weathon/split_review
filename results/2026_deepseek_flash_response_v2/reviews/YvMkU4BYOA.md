Now I'll write the final review with calibrated score.

## Summary

XBIC augments the BIC score for discrete Bayesian network structure learning by soft-weighting the complexity penalty with Shapley-value-based directional evidence from per-node XGBoost classifiers. When a candidate parent contributes strongly to predicting its child, the penalty is reduced proportionally; when directional signal is weak, XBIC defaults to standard BIC. Across 700 runs on ten benchmark discrete networks (6–76 nodes) with seven sample-size regimes, XBIC achieves statistically significant improvements in oriented-edge F₁ over hill-climbing BIC (+5.6% relative, +0.04 absolute), PC (+20.9%), and GES (+9.6%).

## Strengths

1. **Novel integration of local feature attributions into score-based discrete causal discovery.** The idea of directly modulating the BIC complexity penalty with edge-specific Shapley evidence (computed when the graph is unknown) is genuinely novel. Prior work either assumes a known causal graph (Frye et al. 2020; Heskes et al. 2020) or targets continuous settings (Renero et al. 2025). The pipeline—per-node XGBoost classifiers → TreeSHAP → soft-weighted BIC—is clearly described and represents a distinct contribution to discrete causal discovery.

2. **Large-scale, statistically rigorous evaluation.** The evaluation spans ten networks (6–76 nodes), seven sample-size regimes, and 700 runs. XBIC (w=2) achieves a statistically significant overall F₁ improvement over BIC (adjusted Friedman test, p<0.05; Wilcoxon signed-rank tests). The scale and statistical rigor of this evaluation exceed what is typical for BN structure learning papers.

3. **Graceful degradation to standard BIC when directional evidence is weak.** When few instances pass the confidence threshold (e.g., small samples on small networks), SHAP(G) approaches zero and XBIC reduces to standard BIC. This is empirically demonstrated (Table 2: Asia and Survey show near-zero ΔF₁ at low sample sizes) and follows from the score definition (Equation 2). The O(log N) penalty growth is preserved.

4. **Explicit characterization of the precision–recall trade-off via the w parameter.** The paper sweeps w ∈ {1, 2, 3} and shows the expected behavior (larger w increases recall, sometimes at precision cost) in Figure 2 and Table 4, allowing practitioners to select the setting for their needs.

## Weaknesses

### Major

1. **Unvalidated directional premise.** The paper states (line 127) that "if |φ₁→₂| ≫ |φ₂→₁|, the edge X₁→X₂ has stronger directional support than X₂→X₁." This claim—that asymmetry in associational Shapley values tracks causal direction—is presented as intuition without theoretical argument or even a simple diagnostic validation (e.g., a two-variable chain or three-variable fork with known ground truth). The empirical improvement is itself evidence, but the core mechanism is never directly tested, which weakens the paper's conceptual foundation.

2. **The observed improvement may stem from penalty relaxation rather than directional information.** The XBIC score systematically reduces the complexity penalty for any graph (proportional to the sum of |φⱼ→ᵢ| over graph edges). The paper acknowledges that larger w increases recall (line 237) but conducts no ablation to distinguish the directional effect from a uniform penalty relaxation effect. Replacing Shapley values with random values or symmetric (undirectional) penalties would clarify whether the F₁ gains come from directional signal or simply from a softer penalty that admits more edges. Without this, attributing the improvement to "directional evidence" is unwarranted.

3. **Unfair PC baseline inflates the headline 20.9% improvement.** The paper completes PC's PDAG to a DAG by "randomly orienting undirected edges" (line 190) before computing directed-edge metrics. Random orientation is a deliberately weak post-processing choice that introduces error unrelated to PC's actual performance. The 20.9% F₁ advantage over PC is largely an artifact of this choice. The 5.6% improvement over BIC (which produces a DAG directly) is not affected by this issue, but the PC comparison as presented is misleading.

4. **No evaluation isolating Markov-equivalence resolution.** The paper's stated motivation is resolving edge directions within Markov equivalence classes (lines 17–19, 29, 44), yet the evaluation never isolates this scenario. No CPDAG F₁ metrics are reported (which would ignore inherently undirected edges), and results are not stratified by whether edges lie within equivalence classes or are determined by identifiable v-structures. Without this, the connection between the paper's motivation and its empirical evaluation is incomplete.

### Minor

1. **Absolute baseline F₁ scores are not reported.** Table 2 reports only F₁ deltas; Table 4 reports only absolute deltas (e.g., +0.04 over BIC). Without the actual baseline scores, readers cannot assess whether the improvement is from 0.3→0.34 or 0.8→0.84, making practical significance hard to judge.

2. **GES comparison is biased toward easier instances.** Section 4.5 filters to only runs where GES completed within 7 days, introducing selection bias toward easier problems. The paper acknowledges this, but the bias remains.

3. **No confidence intervals for Table 2 results.** Figure 2 shows confidence intervals for only 3 of 10 networks; Table 2 reports point estimates without variance information. This is inconsistent with the paper's emphasis on statistical rigor.

4. **Extreme runtime cost relative to modest gains.** XBIC is 50–200× slower than BIC (e.g., 74.78s vs 0.39s on Asia). The paper acknowledges this and discusses parallelization, but does not discuss whether the modest 0.04 absolute F₁ improvement justifies this cost in practice.

### Trivial

None.

## Nice-to-Haves

- A simple diagnostic toy example (2- or 3-variable network) validating that |φⱼ→ᵢ| > |φᵢ→ⱼ| when the true direction is Xⱼ → Xᵢ would substantially strengthen the paper's foundation.
- An ablation with random or symmetric Shapley values would disentangle the directional effect from penalty relaxation.
- Reporting CPDAG F₁ metrics alongside DAG metrics would directly connect to the Markov-equivalence framing.
- Mentioning non-Gaussian/nonlinear causal discovery methods (e.g., LiNGAM, ANM) that also break equivalence through asymmetry would better contextualize the contribution, though these methods primarily target continuous data.

## Removed Points

- **Criticism that Shapley asymmetry is "likely false in many settings"**: This is speculative conjecture, not a verified weakness. The method may work or fail depending on the data distribution; the weakness is the *lack of validation*, not a claim about falsehood. Kept version focuses on unvalidated premise.
- **Criticism about missing related work (LiNGAM, ANM, CAM)**: These methods target continuous data with structural equation models and are not directly comparable to a score-based approach for purely discrete data. Mentioning them would be contextually helpful but not a weakness.
- **Criticism about consistency remark being insufficient**: The paper explicitly notes theoretical analysis as future work (line 313). The remark correctly notes O(log N) penalty preservation. This is not a substantive weakness.
- **Strength claiming "consistent improvements"**: "Consistent" overstates Table 2, which shows many zero or negative entries across individual (network, sample-size) settings. The improvement is statistically significant overall, not consistent per setting. Removed phrasing that overstated consistency.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a diagnostic experiment on a small known network (2–3 variables) directly showing that Shapley asymmetry aligns with ground-truth direction, or revealing its failure modes.
2. Run an ablation replacing Shapley values with random values (or symmetric magnitudes) to rule out the penalty-relaxation confound.
3. Replace random PDAG-to-DAG completion with a principled orientation heuristic, or report CPDAG metrics alongside DAG metrics.
4. Report absolute F₁ scores for all methods (at least in supplementary material).
5. Include variance estimates (standard deviations) for Table 2 entries.
6. Add discussion of practical cost-effectiveness: under what circumstances is a 0.04 absolute F₁ gain worth a 50–200× runtime increase?

## Score and Decision

**Calibration anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/JzFLBOFMZ2.md` | 3.20 | 1 (low) | Much weaker — vague LLM+CSL method with weak evaluation |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/TRHyAnInUC.md` | 3.25 | 1 (low) | Much weaker — unstable optimization approach with limited validation |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/AvXrppAS2o.md` | 3.00 | 1 (low) | Much weaker — prediction-focused, not a causal discovery method |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/1dDxMPJy4i.md` | 3.00 | 1 (low) | Much weaker — nonparametric DAG learning with limited evaluation |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/ljZFM2mhbR.md` | 5.00 | 1 (mid) | Similar theme (Shapley+causality) but requires known DAG and smaller evaluation. XBIC has stronger experiments |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/DUfwD5yiN4.md` | 5.25 | 1 (mid) | BN structure learning with theory but weak experiments. XBIC has stronger empirical work |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/3n6DYH3cIP.md` | 5.60 | 1 (mid) | BN structure learning with theory and speedup. Comparable quality |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/lnMQGBHYRt.md` | 5.33 | 1 (mid) | Shapley+causality but different problem (explanations). Not directly comparable |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/gqbbL7k8BF.md` | 5.60 | 2 (mid) | CI test theory with restrictive assumptions. Comparable quality, different contribution type |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/UAkVjK00Wv.md` | 4.75 | 2 (mid) | Ensemble BN learning. Weaker than XBIC |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/Lxst78Rrwj.md` | 5.00 | 2 (mid) | Invariance-based causal discovery with fundamental theoretical concerns. Weaker |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/xByvdb3DCm.md` | 8.00 | 1 (high) | Substantially stronger — clean theory, complete evaluation, no confounding issues |

**Round-1 bracket:** 5.0–6.0.
**Round-2 narrowing:** Placed between DAG-SHAP (5.00) and Extendable BN Learning (5.60), closer to the upper end. XBIC's empirical rigor and novelty exceed the 5.0 anchors, but the unresolved weaknesses (unvalidated premise, no ablation, unfair PC baseline) prevent it from reaching the 6.0+ level.
**Final score:** 5.5 — a paper with a genuinely novel idea and extensive empirical work, but with several significant unresolved weaknesses that prevent it from being a clear accept.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
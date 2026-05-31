Now let me do the calibration search to anchor the score.Now I have sufficient calibration data. Let me compile the final meta-review.

**Round 1 Bracket:** 4.5 – 6.5, anchored by `dDdxbdhMsY.md` (prior version of essentially this paper, 5.00/Reject), `VRFotuGLfM.md` (DiffMove trajectory diffusion, 6.20/Reject), `1o3fKLQPRA.md` (DiffPath, 4.50/Reject).

**Round 2 Narrowing:** `dDdxbdhMsY.md` is the strongest single anchor — it appears to be a prior version of the same paper (TDDPM vs TDDM, same spatial deaggregation idea), rejected at 5.00 with weaknesses that the current paper largely addresses (ablation now present, more metrics added, cross-city comparison added). `b3CzCCCILJ.md` (6.00) and `VRFotuGLfM.md` (6.20) are stronger papers with cleaner methodology. The comparison asymmetry issue identified here is a genuine major concern that the prior version's reviewers partially missed, keeping the paper at or slightly below 5.5.

---

## Summary
TDDM proposes a hierarchical trajectory generation framework that separates "where people move" (spatial marginal prior H, discretized as a heatmap) from "how they move temporally" (learned by a diffusion model conditioned on H). Using similarity-transform canonicalization to normalize regions, a single model can generate trajectories for any region given only its aggregate spatial occupancy. The paper also contributes a three-city benchmark (Beijing, Porto, San Francisco) with a harmonized multi-metric evaluation framework and demonstrates zero-shot cross-city transfer.

---

## Strengths

- **Spatial-prior conditioning demonstrably enables OOD generalization.** Table 3 shows that a model trained only on Porto generates trajectories in Geolife and Cabspotting with KL_sym = 0.335 and Pattern ≥ 0.930, *better* than training on 25% of local data (KL_sym = 0.545). This is the paper's most striking empirical finding and is directly supported by the experimental setup.

- **Cross-region canonicalization is a clean architectural contribution.** Using similarity transforms (translation, rotation, scaling to [−1,1]²) to enable a single model to share parameters across all geographic regions is a principled design. The ablation validates this indirectly: the model trained on 3×3 km regions with spatial priors achieves KL_sym = 0.277, vs. 1.334 without priors, showing that canonicalized conditioning is what enables regional generalization.

- **The ablation study honestly exposes the role of each component.** Table 2 includes the condition-removed variant ("w/o spatial prior") and the different region-size variant (1×1 km), giving a clear decomposition of where gains come from. This transparency is a genuine strength.

- **Multi-city benchmark with harmonized metrics across three continents.** Geolife (Beijing), Porto, and Cabspotting (San Francisco) span diverse urban layouts and are evaluated with six complementary metrics (TSTR, KL variants, Density, Trip, Length, Pattern). This is a service to the field and a reusable evaluation infrastructure.

---

## Weaknesses

### Fatal
None.

### Major

- **The main comparison in Table 1 is structurally asymmetric, and the ablation reveals this.** Section 4.1 is titled "Large-Scale Unconditional Trajectory Generation" and compares TDDM against unconditional baselines. However, TDDM at inference time uses H = f(r_c, X_train) — the spatial marginal computed directly from the same training data whose distributional properties the KL metrics are measuring. The dominant metrics in Table 1 (KL(S‖R), KL(R‖S), KL_sym, JS) measure how well the synthetic spatial distribution aligns with the real distribution — precisely what TDDM is conditioned to match. This circularity is confirmed by the ablation: "TDDM w/o spatial prior" achieves KL_sym = 1.334 (Table 2), which is **worse** than Diffusion-TS (1.153) and comparable to DiffTraj (1.232). The TDDM architecture, without the privileged spatial conditioning signal, does not outperform the strongest unconditional baseline on the headline KL metrics. All large-margin gains in Table 1 on KL-based metrics are attributable to the conditioning information access, not to architectural improvement. The TSTR metric (0.011 vs. 0.013) — which is *not* circular — shows only a narrow improvement. The paper should either (a) add spatially-augmented baselines (Diffusion-TS + spatial prior conditioning) to show what TDDM's architecture contributes beyond the prior, or (b) reframe the contribution honestly as "conditional generation with aggregate priors" and move the comparison framing to measuring what the prior *enables* rather than how TDDM beats unconditional models on spatial metrics.

### Minor

- **Property (V) "Generalization" has no corresponding metric in any table.** The paper defines five quality properties (Section 4) including "(V) Generalization: Synthetic samples should not be mere copies of the training data," but no memorization metric (e.g., nearest-neighbor distance to training samples) is reported anywhere. Either this property should be evaluated or removed from the framework as defined.

- **KL-based metrics in Tables 1 and 3 have no variance estimates.** TSTR shows ± values, but KL_sym, JS, Density, Trip, and Pattern do not, despite being headline metrics. Given that some margins are moderate (e.g., TDDM 1×1 km vs. TDDM 3×3 km: KL_sym 0.328 vs. 0.277), the absence of uncertainty estimates weakens the statistical significance of these comparisons.

### Trivial

- The rotation range used during the random region-sampling augmentation ("randomized translation and rotation") is not specified in the main text or anywhere accessible. This minor specification gap doesn't affect the core results but would help reproducibility.

---

## Nice-to-Haves

- **Augmented baseline comparison.** Adding Diffusion-TS conditioned on the same spatial heatmap H (e.g., as a prefix token or cross-attention) would directly test whether TDDM's architecture contributes beyond the conditioning signal. This would either strengthen the architectural claim or clarify that the contribution is the conditioning strategy itself.

- **Analysis of Porto as a "universal source."** The finding that Porto generalizes better than 25% of local data is surprising and substantive (Section 4.3). A closer analysis of what makes Porto unusually representative — trajectory length distributions, road network density, speed profile diversity — would significantly deepen this insight and make it actionable for practitioners choosing source cities.

- **Visualization of cross-city generation failures.** The main failure mode (Length error 0.06–0.11 in cross-city transfer) is acknowledged but not visualized. Figure 15 in the appendix shows marginal distributions; a direct visual comparison of length histograms across source and target cities would make the limitation concrete.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic — "zero-shot framing requires fundamental qualification":** The critic argues that computing H from X_target means zero-shot is not truly zero-data. This is removed as a standalone weakness because Algorithm 2 and Section 4.3 are explicit that target trajectories are used only for their aggregate statistics, not as individual conditioning — and "zero-shot" in the transfer learning sense (no gradient updates on target data) is standard terminology. The paper does not hide this. Kept as a nice-to-have clarification but not a material flaw.

- **Strength Finder — "TDDM consistently outperforms on all metric categories" (Table 1):** Removed as a standalone strength because the KL-based metric wins are circular given conditioning access, as discussed under Major weaknesses. The TSTR win is real but narrow. Only the non-circular metrics support this claim without qualification.

- **Strength Finder — "large, consistent improvement…reducing symmetric KL by over 4×":** Retained in weakened form under the major asymmetry discussion. The number is accurate but its interpretation is misleading; it does not reflect genuine architectural improvement over unconditional baselines.

---

## Novel Insights

The most genuinely novel empirical observation — not fully analyzed in the paper — is that Porto generalizes to Geolife and Cabspotting *better than 25% of local data* from those cities. This is not merely a performance result but implies that certain urban environments encode more transferable motion dynamics than others, and that aggregate spatial diversity of a source city may matter more than data volume for cross-city transfer. The paper mentions this finding but does not analyze why Porto has this property or what structural characteristics of road networks and mobility patterns explain it. This is the paper's most interesting finding and deserves front-stage treatment rather than a paragraph in Section 4.3.

---

## Suggestions

1. **Rename Section 4.1** to "Conditional Generation with Aggregate Spatial Priors" and frame the comparison explicitly as "what does spatial-prior conditioning contribute?" rather than a head-to-head unconditional generation race.

2. **Add one spatially-conditioned baseline** (Diffusion-TS + heatmap prefix, implemented straightforwardly) to show what TDDM's architecture contributes beyond the conditioning signal.

3. **Add a memorization/generalization metric** (e.g., mean minimum nearest-neighbor distance between synthetic and training trajectories) to operationalize Property (V).

4. **Foreground the Porto universality finding** in the Introduction and Abstract — this is the paper's most striking and actionable empirical finding.

5. **Add variance to all metrics** in Table 1, or clearly state that single-run evaluation is standard in this domain (citing precedent), so the significance of moderate margins can be assessed.

---

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| `dDdxbdhMsY.md` (Deep Temporal Deaggregation, prior version) | 5.00 | R1/R2 | Most relevant: essentially a prior version of this paper, rejected with similar framing weaknesses, fewer metrics, no ablation. Current paper is improved. |
| `VRFotuGLfM.md` (DiffMove) | 6.20 | R1/R2 | Trajectory diffusion with cleaner methodology, SOTA on a well-scoped task. Stronger execution per reviewer. Slightly above this paper. |
| `1o3fKLQPRA.md` (DiffPath) | 4.50 | R1 | Path generation with latent diffusion, weaker execution. Below this paper. |
| `r125wFo0L3.md` (Large Trajectory Models) | 5.00 | R2 | Scalable trajectory model, clear scope, similar breadth, comparable rating. |
| `b3CzCCCILJ.md` (Revamping Diffusion Guidance) | 6.00 | R2 | Cleaner methodology, no asymmetric comparison issue. Above this paper. |
| `YOKnEkIuoi.md` (Conditional Variational Diffusion) | 5.80 | R2 | High variance in scores (3–8), accepted. Comparable level. |

**Round 1 bracket:** 4.5 – 6.5.

**Round 2 narrowing:** The prior version of this paper (`dDdxbdhMsY.md`) was rejected at 5.00. The current paper addresses the prior version's weaknesses (missing ablation, missing metrics, unclear contributions, no cross-city comparison) — but the underlying comparison asymmetry issue, identified more sharply here by the harsh critic, was also implicitly present in the prior version (reviewer #1 explicitly asked for the ablation "when the model does not use the conditioning component for the unconditional task"). The current paper scores above 5.00 given these improvements, but below 6.00 (the level of `b3CzCCCILJ.md` and close to `VRFotuGLfM.md`) because the headline claim ("outperforms unconditional baselines") is structurally inflated by conditioning access, and the architecture itself is not shown to improve over Diffusion-TS. The OOD experiments and benchmark are genuine contributions.

**Final score: 5.0**, Decision: **Reject**. The paper has real substance — the spatial prior conditioning idea, the benchmark, and the OOD generalization results are legitimate contributions — but the primary evaluation (Table 1) misleadingly pits a conditioned model against unconditional baselines on the metric the model is conditioned to match. The ablation's revelation that TDDM without priors underperforms Diffusion-TS on KL metrics is a structural credibility problem that needs to be resolved through either augmented baselines or an honest reframing. With those revisions, this paper could be above the 5.0 threshold.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
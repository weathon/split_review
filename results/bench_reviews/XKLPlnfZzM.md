I have a thorough understanding of the paper and all reviewer claims. Here is my consolidated review.

---

## Summary

This paper introduces TDDM (Temporal Deaggregation Diffusion Model), a hierarchical framework for trajectory generation that separates spatial occupancy priors ("where people go") from temporal dynamics ("how they move in time"). By conditioning a diffusion model on aggregate spatial marginals (heatmaps) rather than individual trajectory statistics, TDDM enables transfer to new geographic regions without gradient updates. The method is evaluated across three cities (Beijing, Porto, San Francisco) on six metrics, and shows improvements on distributional metrics compared to GAN-, VAE-, and diffusion-based baselines.

## Strengths

- **Novel spatial-temporal factorization for controllability and transfer.** TDDM's core idea — conditioning trajectory generation on aggregate spatial marginals (heatmaps) rather than sample-specific statistics — is a genuine conceptual contribution. This decoupling means the model can generate trajectories for a new region by receiving only its occupancy heatmap, without needing individual trajectory samples for gradient-based adaptation. The city-to-city generalization results (e.g., Porto→Geolife with Pattern 0.930, TSTR 0.011) demonstrate that temporal dynamics learned in one city do transfer.

- **Empirically better or competitive on non-confounded metrics.** On metrics not directly measuring spatial marginal similarity (TSTR: 0.011 vs 0.013 for DiffTraj; Pattern Score: 0.917 vs 0.893; Length Error: 0.004 vs 0.003 for Diffusion-TS), TDDM shows clear or competitive advantages over baselines. The ablation study cleanly attributes the spatial prior's contribution (removing it degrades KLsym from 0.277 to 1.334 while TSTR stays nearly unchanged).

- **Thorough evaluation framework across diverse cities and metrics.** The paper establishes a standardized benchmark across three cities on three continents with six complementary metrics covering fidelity, coverage, proportionality, usefulness, and generalization. The preprocessing pipeline (map matching, resampling, canonicalization) is applied uniformly to all methods.

- **Canonicalization via similarity transform is a practical design choice.** Normalizing regions to a canonical frame before modeling achieves translation/rotation invariance without complex equivariant architectures, and the ablation on region size (3×3 km vs 1×1 km) explores the tradeoff between local and global structure.

## Weaknesses

### Fatal
None.

### Major

1. **Confounded comparison on distributional metrics undermines headline KL/JS claims.** The paper's primary evaluation compares TDDM against baselines (DiffTraj, Diffusion-TS, TimeVAE, etc.) on KL divergence and JS divergence computed from spatial heatmaps (256×256 grid). TDDM receives the real spatial marginal *H* as conditioning input — which is exactly the same information these metrics measure. Baselines receive no such information. The reported 4× improvements (KLsym 0.277 vs 1.153 for Diffusion-TS; JS 0.059 vs 0.198) are therefore largely attributable to the model being given the target marginal as input, not to superior generative modeling. This is acknowledged nowhere in the paper. The effect is visible: when *H* is removed (ablation), TDDM's KLsym degrades to 1.334 — comparable to baselines. On non-confounded metrics (TSTR, Length Error), TDDM's advantage is modest. **This does not invalidate the paper's other contributions (generalization, architecture), but it drastically weakens the unconditional generation claims.**

2. **"Zero-shot" terminology overclaims the generalization capability.** The paper repeatedly describes the method as "zero-shot" transfer to unseen cities. However, Algorithm 2 (line 3) explicitly computes the spatial prior *H* from target trajectories (Xtarget). The model does not need individual target trajectories or gradient updates, which is a genuine advantage, but it does need aggregate target data (the marginal heatmap). Standard definitions of zero-shot learning require no data from the target distribution. The paper is *transparent* about computing *H* from Xtarget (lines 327–334), but the terminology "zero-shot" throughout the abstract, introduction, and conclusion (e.g., "zero-shot generalization," "strong out-of-distribution zero-shot performance") creates a misleading impression that the target provides no information at all. This should be renamed to something like "conditional generation from target marginals" or "few-statistic transfer."

3. **Missing sensitivity analysis for the spatial prior estimation.** The generalization experiments compute *H* from the full target dataset. A critical practical question — how much target data is needed to estimate a useful *H*? — is not addressed. If *H* requires dense trajectory coverage, the claimed advantage over methods needing sample-level data is weaker. The paper's own framing (that *H* could come from independent sources like census data) makes this gap more significant: no experiment tests whether a coarsely estimated or externally-sourced *H* suffices.

### Minor

- **The evaluation of the unconditional generation task is partially circular.** The paper claims TDDM is "unconditional" (Section 4.1) but then uses *H* computed from the target distribution during sampling. The "unconditional" label is inconsistent with the experimental procedure.

- **Per-city results show substantial variation not discussed in the main text.** Table 12 in the appendix shows that city-to-city transfer performance varies widely (e.g., KLsym ranges from 0.263 to 0.982 depending on source-target pair). The main text aggregates these and claims "robust" generalization, but some individual transfer directions (e.g., Cabspotting→Geolife: KLsym 0.286, which is closer to the baselines' range) are substantially weaker than others.

- **The ablation (Table 2) shows the "w/o spatial prior" variant matching or exceeding TDDM on TSTR for some cities**, suggesting the architecture without priors already captures sample-level fidelity. The paper acknowledges this but could better contextualize what the spatial prior actually contributes beyond distributional metric improvement.

### Trivial
- None (formatting artifacts are parser issues, not author errors).

## Nice-to-Haves
- A fair comparison where baselines also receive *H* (e.g., as an additional input channel) would isolate whether TDDM's architecture adds value beyond the conditioning itself.
- Testing with *H* estimated from an independent source (e.g., kernel density estimate, census-derived heatmap) would demonstrate true zero-shot usability.
- Varying the fraction of target data used to compute *H* would reveal how much aggregate information is needed.

## Removed Points
- **Criticism about garbled/missing table entries (Tables 1–3):** These are PDF parser artifacts, not author errors. REMOVED per hard rules.
- **Criticism about missing appendix content:** The parser strips appendix sections. REMOVED per hard rules.
- **"The core factorization does not actually separate spatial allocation from temporal realization":** The paper is transparent about *H* being computed from target data. The separation is conceptual (aggregate occupancy vs. individual temporal dynamics), and the paper explicitly states *H* "can be estimated (even in unseen cities)" (line 214). The factorization is meaningful even if *H* comes from target data, as (a) individual trajectories are not needed, (b) temporal dynamics transfer, and (c) *H* could come from independent sources. This criticism overstates the problem and is moved here as the paper's claim is reasonable given their stated setup.
- **Generic strength from Strength Finder ("Spatial-temporal factorization achieves zero-shot cross-city generalization"):** This conflicts with verified weaknesses about the "zero-shot" terminology being overclaimed. Moved here per rules (when strength and weakness disagree, weakness wins).
- **"Missing experiments" and "obvious next steps" from the harsh critic:** These are suggestions, not weaknesses of the current paper. Moved here.

## Novel Insights
None beyond the paper's own contributions. The core tension revealed by the reviews — that conditioning on aggregate statistics is a genuine methodological contribution for controllability and generalization, but evaluating on metrics that measure exactly what you condition on creates a fundamentally unfair comparison — is an important point for the field to consider when designing evaluation protocols for conditional generative models.

## Suggestions
1. Rename "zero-shot" to "conditional generation on target marginals" throughout. The model's true contribution — generating trajectories from aggregate spatial statistics without individual samples or gradient updates — is impressive enough without misleading terminology.
2. Add a controlled experiment where baselines receive the same spatial prior *H* (or an equivalent heatmap conditioning). Report both confounded (KL/JS) and non-confounded (TSTR, Length Error) metrics separately, with explicit discussion of what each comparison shows.
3. Show how the quality of generated trajectories varies with the amount of target data used to estimate *H*, to establish the practical data requirements.
4. Report per-city results more prominently in the main text rather than aggregating, especially for generalization experiments.

## Score and Calibration

**Calibration anchors considered (batched search):**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `BDOldEjwCE.md` (TrajFlow) | 6.50 | Similar GPS trajectory generation paper, accepted. TDDM has a more interesting factorization idea but also has an evaluation fairness concern that TrajFlow doesn't. |
| `w7xpNeFIbb.md` (GeoDiffusion) | 4.00 | Similar spatio-temporal trajectory paper, rejected. Overclaimed "foundation model" claim is analogous to TDDM's "zero-shot" terminology issue, but TDDM's evaluation is more thorough. |
| `cRQHnoDaa2.md` (MoveFM-R) | 3.50 | Rejected mobility paper. TDDM is stronger: clearer contribution, better evaluation design, code released. |
| `ZokiZYcEsg.md` (RL Trajectories) | 2.00 | Very weak paper, withdrawn. TDDM is substantially stronger in every dimension. |

Positioned relative to these anchors: TDDM's core idea (spatial-marginal conditioning) is novel and the architecture is clean. However, the confounded evaluation is a significant weakness that TrajFlow (6.50) does not share. The paper is clearly better than GeoDiffusion (4.00) and MoveFM-R (3.50), but the evaluation fairness gap prevents it from reaching the TrajFlow tier without substantial revisions.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
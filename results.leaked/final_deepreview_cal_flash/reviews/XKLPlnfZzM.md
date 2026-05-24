Now I have a thorough understanding of the paper and all the reviewer inputs. Let me construct the final review.

## Final Review

**Paper ID:** XKLPlnfZzM  
**Title:** Learning to Deaggregate: Large-Scale Trajectory Generation with Spatial Priors

---

## Summary

The paper proposes the Temporal Deaggregation Diffusion Model (TDDM), which factorizes trajectory generation into two components: a spatial prior (a marginal occupancy grid over a region) and a diffusion model that generates trajectories conditioned on that prior. Regions are canonicalized via similarity transforms so the dynamics model is location-invariant. Experiments on Beijing, Porto, and San Francisco show that TDDM outperforms existing baselines (TimeGAN, TimeVAE, COSCI-GAN, Diffusion-TS, DiffTraj) on KL/JS distributional divergences by large margins, with more modest gains on fidelity metrics (TSTR, Pattern). The paper also demonstrates zero-shot generalization to unseen parts of a city and to entirely new cities.

---

## Strengths

1. **Novel and well-motivated factorization.** The core idea—decoupling *where* people go (spatial occupancy) from *how* they get there (temporal dynamics)—is clearly articulated and practically useful. Conditioning on aggregate spatial priors rather than per-trajectory statistics is a principled way to combine controllability with generalization. The canonicalization via similarity transforms (Section 3) is a clean mechanism for achieving spatial invariance without requiring group-equivariant architectures.

2. **Large and consistent improvements on distributional metrics.** TDDM achieves a symmetric KL of 0.277 averaged over three cities versus 1.153 for the best baseline (Diffusion-TS) and JS of 0.059 versus 0.198 (Table 1). These are substantial margins, and the pattern holds across all three datasets individually (Appendix Table 7). The ablation study (Table 2) confirms the spatial prior is the source of this improvement: removing it degrades KL_sym from 0.277 to 1.334, a ~5× increase.

3. **Demonstrated zero-shot generalization.** Intra-city (25% training area → full map) and city-to-city (e.g., Porto → Geolife) transfers without any fine-tuning produce competitive results (Table 3). For example, Porto-trained TDDM achieves KL_sym 0.335 on Geolife versus 0.278 when trained directly on Geolife, and Pattern score remains above 0.915 in all cross-city settings. This capability is unique to TDDM among the compared methods and is a genuine contribution.

4. **Rigorous benchmarking framework.** The paper standardizes evaluation across three diverse cities (Asia, Europe, North America) with seven complementary metrics covering fidelity (TSTR), distributional coverage (KL, JS), proportionality (Density, Trip), and structure (Pattern, Length). Using the same preprocessing pipeline for all models strengthens the validity of the comparisons.

5. **Qualitative corroboration.** Visual comparisons (Figure 2) show that TDDM generates road-following trajectories with realistic density holes, while baselines produce scattered points or mode-collapsed patterns, providing human-interpretable support for the quantitative results.

---

## Weaknesses

### Fatal

None.

### Major

1. **KL/JS metrics conflate model quality with conditioning advantage.** The KL and JS divergences are computed on the *spatial marginal* distribution—the very quantity TDDM is explicitly conditioned on via \(H\). Unconditional baselines (Diffusion-TS, TimeGAN, etc.) must infer this marginal from data, while TDDM receives it as input. The 4× gap in KL_sym therefore partly reflects the structural advantage of the conditioning setup rather than superior generative fidelity. The paper frames these metrics as unqualified evidence of "improved fidelity and coverage" (abstract, conclusion) without acknowledging this asymmetry. While the conditioning is the central novelty, the headline claims overstate the method's advantage relative to what a fair comparison would show. The improvements on non-spatial metrics (TSTR, Pattern) are much smaller, which is consistent with this concern.

2. **Generalization experiments lack baseline comparisons.** Table 3 shows TDDM's intra-city and city-to-city performance, but no baseline is evaluated in these settings. This makes it impossible to determine whether TDDM's generalization capability is distinctive or whether existing methods (e.g., Diffusion-TS trained on source data and applied to target, or adapted with a small amount of target data) would achieve comparable results. The claim that factorization "enables" generalization (Section 1, line 42) is weakened by the absence of a comparative ablation showing that a non-factorized model would fail in the same transfer scenario. At minimum, the paper should compare against a simple baseline (e.g., unconditional Diffusion-TS applied zero-shot, or a fine-tuned version with a small target-data budget).

### Minor

3. **Absence of uncertainty estimates.** Only TSTR reports standard deviations (across datasets); KL, JS, Density, Trip, Length, and Pattern scores are presented as point estimates without variance across seeds or datasets. Given the modest magnitudes of some improvements (e.g., TSTR 0.011 vs. 0.013), readers cannot assess whether differences are statistically meaningful.

4. **No discussion of limitations or failure cases.** The paper does not address what happens when the spatial prior \(H\) is noisy, biased, or derived from low-quality aggregate counts—a realistic scenario for the claimed practical applications. The dependence on target-region aggregates for "zero-shot" generation (Algorithm 2, line 3 requires \(\mathbb{X}_{\text{target}}\)) is acknowledged in the algorithm description but not discussed as a limitation in the conclusion or future work.

5. **Preprocessing description is unclear.** The statement that "map matching is used to reduce observation noise… before GPS noise is added back" (Section 4, paragraph on datasets) is confusing. It is not clear whether models are trained on clean map-matched points, on points with synthetic noise re-injected, or on the original noisy data. This matters for interpreting all experimental results.

6. **Fidelity gains are modest on non-spatial metrics.** TSTR improves from 0.013 (DiffTraj) to 0.011 (TDDM), Pattern from 0.907 to 0.917, Density from 0.029 to 0.019, Trip from 0.041 to 0.031. These improvements are consistent but small relative to the KL/JS margins. The presentation could more clearly distinguish between the large distributional-coverage gains (driven by the conditioning) and the more incremental per-trajectory fidelity improvements.

### Trivial

7. **"Zero-shot" should be qualified.** The model requires the aggregate spatial marginal \(H\) of the target region, which is computed from target trajectories (Algorithm 2, line 3). This is zero-shot with respect to *individual trajectory instances*, but not with respect to all target information. The paper acknowledges this in algorithm text but the abstract and conclusion use the term without qualification.

---

## Nice-to-Haves

- A controlled comparison in the generalization setting (e.g., fine-tuning Diffusion-TS on target data with varying budgets) to quantify the benefit of the factorization approach.
- Fitting the ablation "w/o spatial prior" with an unconditional diffusion model of comparable capacity to see whether the transformer architecture itself contributes to performance beyond the prior.
- Statistical significance tests or bootstrapped confidence intervals for the main KL/JS/Pattern results.
- A brief discussion of the sensitivity to the grid resolution and cell size used for the discretized marginal \(H\).

---

## Removed Points

- **"Baseline configuration not sufficiently specified for DiffTraj"**: The paper references Appendix A for detailed comparisons. The reviewer's concern about whether DiffTraj was used in conditional or unconditional form is reasonable, but the appendix (which the parser strips) likely contains this information. Per the hard rules, speculation about missing appendix content is removed.
- **"Overstatement of fidelity improvements" (as a distinct weakness)**: The abstract and conclusion claims are factually accurate (TDDM improves TSTR from 0.013 to 0.011). The wording is not egregiously overblown. This concern is subsumed into Minor #6 above with appropriate nuance.
- **"KL metric is circular" (as a fatal concern)**: The KL metric measures distributional coverage—a stated goal of the paper. Conditioning on \(H\) is the method, not a bug. The concern is valid as a *contextualization* issue (moved to Major #1) but calling it circular overstates the problem.
- **"Missing related works"**: Per the hard rules, missing related works are not flagged.
- **"Formatting/style nitpicks"**: Removed per the hard rules.
- **Generalized "could be the metric is measuring a proxy" type concerns from the harsh critic**: These are speculative sweeps without concrete evidence from the paper text and are removed.

---

## Novel Insights

Beyond the paper's own contributions, the two reviewer inputs surface an interesting tension not fully resolved by the paper: the spatial prior \(H\) is both the mechanism that enables the claimed improvements and the reason the headline metrics are not directly comparable to unconditional baselines. This highlights a broader challenge in evaluating conditional generative models—when the condition is a summary statistic of the target distribution, metrics computed on that same statistic are not a level playing field. The paper would benefit from explicitly grappling with this issue and proposing a correction (e.g., reporting how well the unconditional baselines could perform if also given \(H\) as input, or focusing the comparison on metrics that are not directly aligned with the condition).

---

## Suggestions

1. **Reframe the KL/JS results.** Clearly separate the discussion of distributional-coverage metrics (where TDDM's advantage is expected from the setup) from per-trajectory fidelity metrics (where the improvements are modest but come without the conditioning advantage). Add a note that unconditional baselines could not access \(H\) during generation, making these metrics an assessment of the overall "generative pipeline" rather than a head-to-head model comparison.

2. **Add at least one baseline to the generalization experiments.** The simplest option: train Diffusion-TS on the source city and generate directly for the target city (zero-shot). Even if this baseline performs poorly, that is informative. A stronger option: fine-tune Diffusion-TS on a small subset of target trajectories and compare its data efficiency against TDDM.

3. **Provide standard deviations for all main metrics** (at minimum across the three city datasets, or across multiple seeds). This is important because several improvements (TSTR, Pattern, Density, Trip) are modest in magnitude.

4. **Clarify the preprocessing.** Rewrite the map-matching description to state unambiguously whether models are trained on map-matched points, on noisy points, or on points with synthetic noise added after map-matching.

5. **Add a limitations paragraph.** Discuss what happens when \(H\) is poorly estimated (e.g., from sparse or biased counts) and whether the model can detect when the conditioning is unreliable.

---

## Calibration Report

**Anchors retrieved across all rounds:**

| Anchor | Avg Score | Round | Comparison to this paper |
|--------|-----------|-------|------------------------|
| kKXIYUi8ff (DynamicsDiffusion) | 3.00 | 1 | Much weaker: molecular dynamics diffusion, different domain, scores all 3. This paper is clearly stronger. |
| RDLvnUJ5JZ (TF-score) | 3.00 | 1 | Much weaker: time-series forecasting with score-based diffusion, minimal evaluation. |
| XeGSIr7z6u (Memorization→Generalization) | 3.40 | 1 | Different focus (theoretical study). This paper is more empirically substantial. |
| 46tjvA75h6 (No MCMC Teaching) | 3.00 | 1 | Unrelated (EBM training). Not comparable. |
| **dDdxbdhMsY (Deep Temporal Deaggregation)** | **5.00** | **1+2** | **Most directly comparable: earlier version of similar work. Current paper adds more metrics, better ablations, city-to-city transfer. Marginally stronger.** |
| VRFotuGLfM (DiffMove) | 6.20 | 1+2 | Trajectory recovery (different task). Cleaner evaluation but less ambitious contribution. Current paper is below this level. |
| r125wFo0L3 (Large Trajectory Models) | 5.00 | 1+2 | Motion prediction for autonomous driving. Comparable quality. |
| 1o3fKLQPRA (DiffPath) | 4.50 | 1 | Path generation. Weaker methodology and evaluation. Current paper is stronger. |
| jZPqf2G9Sw (Dynamics-Informed Protein) | 5.50 | 2 | Unrelated domain (protein design). Not directly comparable. |
| UapxTvxB3N (Trajectory-LLM) | 5.75 | 2 | Different approach (LLM-based). Better evaluation but different scope. |
| s3sJenvY5H (Evaluation of Generative Robotics) | 4.75 | 2 | Evaluation-focused, not directly comparable. |
| cvGdPXaydP (Planning with World Models) | 4.25 | 2 | Unrelated (planning). |
| uKZdlihDDn (Learning Distributions of Complex Fluid) | 7.60 | 1 | Strong accept-level paper. Current paper is not at this level. |
| EO8xpnW7aX (Learning to Permute) | 8.00 | 1 | Strong accept-level paper. Not comparable. |

**Round 1 bracket:** 4.0 – 6.0  
**Round 2 narrowing:** The primary anchor (Deep Temporal Deaggregation, 5.00) is the closest match—same research group, same task, similar methodology. The current paper improves on that version with more metrics and experiments but retains some of the same evaluation gaps. Comparing against other 4.5–5.5 anchors, this paper sits at the upper end of that range. **Final score: 5.0**, reflecting a solid but not yet fully convincing contribution with evaluation gaps that prevent acceptance at a competitive venue.

---

**MY FINAL SCORE:** <score>5.0</score>
**MY FINAL DECISION:** <decision>Reject</decision>
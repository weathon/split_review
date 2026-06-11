Now I have enough calibration data. Let me write the final review.

**Calibration Analysis:**

Key anchors retrieved:
- `dDdxbdhMsY` — "Deep Temporal Deaggregation" (earlier version of this paper) — avg 5.0, REJECT — scores 6, 6, 3. Concerns: missing metrics, unclear contributions, no baselines in generalization experiments.
- `1o3fKLQPRA` — "DiffPath" (path generation with latent diffusion) — avg 4.5, REJECT — simpler method, unclear contribution.
- `VRFotuGLfM` — "DiffMove" (trajectory recovery via conditional diffusion) — avg 6.2, REJECT — narrower task, fewer datasets.
- `4anfpHj0wf` — "Point Set Diffusion" (point processes via diffusion) — avg 7.0, ACCEPT — strong theoretical contribution, similar empirical scope.
- `DydCqKa6AH` — "PedGen" (pedestrian movement generation) — avg 6.75, ACCEPT — new dataset, fewer baselines, comparable generalization claims.
- `UapxTvxB3N` — "Trajectory-LLM" — avg 5.75, ACCEPT — LLM-based approach, less comprehensive evaluation.

**Bracket:** The paper is clearly stronger than dDdxbdhMsY (5.0) which was its earlier version. It addresses the previous reviewers' concerns (added metrics, ablation, baselines in OOD experiments). It is comparable to or better than PedGen (6.75) and Point Set Diffusion (7.0) in evaluation comprehensiveness and generalization. The evaluation transparency concerns (metric-conditioning alignment, "zero-shot" framing) are real but don't invalidate the core contribution. Score range: 6.5–7.5.

Settling on **7.0**: the paper's contribution (spatial-temporal factorization enabling cross-city generalization) is genuine, the method is sound, the evaluation is comprehensive across 3 cities and 6 baselines, and the ablation clearly validates each component. The evaluation framing issues are transparent — the data is all there for readers to interpret — and don't undermine the core claim.

---

## Summary

This paper introduces TDDM (Temporal Deaggregation Diffusion Model), a trajectory generation framework that factorizes the problem into spatial priors (marginal distributions over geographic occupancy) and temporal dynamics modeled by a transformer-based diffusion model. A similarity transform canonicalizes regions so a single model generalizes across locations. Evaluated across three cities on three continents with six baselines, TDDM demonstrates strong in-distribution performance and cross-city generalization without retraining.

## Strengths

- **Well-articulated spatial-temporal factorization design**: The core insight — separating where people move (spatial priors H as marginal distributions over occupancy cells, Equations 3–4) from how they move temporally — is clean, principled, and directly enables cross-region transfer because H is an aggregate-level conditioning signal rather than sample-specific. The mixture model formulation (Equation 5) and canonicalization via similarity transform are elegant.

- **Strong quantitative improvements**: Table 1 shows TDDM achieves KL_sym = 0.277 vs. next-best Diffusion-TS at 1.153, and leads on Density (0.019 vs. 0.029), Trip (0.031 vs. 0.041), Pattern (0.917 vs. 0.907), and TSTR (0.011 vs. 0.013), while matching Diffusion-TS on Length (0.004 vs. 0.003). These gains hold across three diverse cities spanning different continents.

- **Ablation clearly validates design choices**: Table 2 shows removing spatial priors increases KL_sym from 0.277 to 1.334 (~5× degradation), and reducing region size to 1×1 km worsens Length error from 0.004 to 0.150. The rejection sampling variant performs even worse, confirming the conditioning mechanism's superiority over post-hoc filtering.

- **Unique cross-city generalization capability**: Table 3 shows city-to-city transfer from Porto yields KL_sym = 0.335 and Pattern = 0.930, outperforming even models trained on 25% of the target city (0.545, 0.927). This capability is not demonstrated by any baseline and stems directly from the spatial prior + canonicalization design.

- **Comprehensive evaluation framework**: The paper harmonizes five evaluation qualities (fidelity, diversity, proportionality, usefulness, generalization) into six concrete measures, providing a more thorough evaluation than typical trajectory generation papers. Visual validation in Figure 2 corroborates quantitative results.

## Weaknesses

### Fatal
None

### Major
- **Evaluation overstates improvement magnitude due to metric-conditioning alignment**: The largest headline gains (4× on KL-based metrics) are on measures that directly evaluate spatial distributional matching — precisely the quantity TDDM is conditioned on via spatial priors H. The ablation in Table 2 makes this explicit: TDDM without spatial priors achieves KL_sym = 1.334, which is *worse* than both Diffusion-TS (1.153) and DiffTraj (1.232). The unconditional backbone of TDDM is not competitive with existing diffusion baselines. On TSTR, the downstream utility metric not directly aligned with spatial occupancy, improvements are more modest (0.011 vs. 0.013 for DiffTraj, 0.014 for Diffusion-TS). The paper's thesis — that spatial prior conditioning is the right approach — is valid, but the presentation emphasizes the 4× headline improvements without clearly decomposing the contribution. Adding TDDM-without-spatial-priors as a separate row in Table 1 would let readers see the base architecture's standalone performance versus baselines, and then the additional gain from spatial prior conditioning.

- **"Zero-shot" framing obscures target data requirements**: The paper repeatedly claims "zero-shot transfer" and "generalization to new regions without retraining or finetuning" (line 38). However, Algorithm 2 line 3 shows that generating for a target region requires computing the heatmap H = f(r_c, X_target) from target trajectories. The model needs aggregate spatial statistics from the target distribution. While no gradient updates occur, the spatial prior is a derived representation of target data. The paper is partially transparent about this (lines 172–173: "the model ε_θ never receives individual target trajectories, only their aggregate spatial distribution") but the top-line claims and abstract do not reflect this nuance. This distinction matters for practical deployment, as the paper does not discuss what realistic scenarios provide target-side aggregate statistics.

### Minor
- **No variance reported for most metrics**: Table 1 reports variance only for TSTR (e.g., 0.011 ± 0.006). All KL-based metrics, Density, Trip, Length, and Pattern are reported as single numbers. The paper states "Models are trained, sampled and evaluated once per dataset" (line 267). Without multiple runs, it is difficult to assess whether small differences (e.g., Density: 0.019 vs. 0.029) are statistically meaningful.

- **Number of synthetic samples N_out not stated**: Algorithm 2 takes N_out as an input parameter, but the paper does not specify what value was used in experiments. For density-based metrics like KL divergence, the number of synthetic samples relative to real samples can affect results.

- **Normalization coordinate range inconsistency**: The paper uses [-1, 1]^D in the canonicalization section (lines 121, 123, 131) but [0, 1]^D in Algorithm 1 (line 185) and Algorithm 2 (line 210). This should be resolved for clarity.

### Trivial
None

## Nice-to-Haves
- A Limitations section discussing the need for target-side spatial statistics, fixed region size constraints, and sensitivity of Length error in cross-city transfer would strengthen the paper.
- Discussing realistic scenarios where target-side aggregate statistics are available (e.g., census data, cell tower densities, existing aggregate mobility statistics) would strengthen the practical case for the method.
- Reporting 3–5 seeds for all metrics would increase confidence in the small-margin improvements.

## Removed Points
These points are flagged to be removed, treat them with caution:
- No points were removed; all reviewer concerns were verified against the paper and either kept or merged.

## Novel Insights
The finding that Porto serves as a surprisingly effective "universal source" dataset for cross-city transfer — yielding lower KL divergences (0.335) than training on 25% of the target city itself (0.545) — is a genuinely interesting empirical insight about dataset selection for transfer learning in mobility modeling. The paper provides a plausible explanation tied to Porto's heavy-tailed trajectory length distribution, and this finding could have practical implications for practitioners choosing source datasets.

## Suggestions
- Add TDDM-without-spatial-priors as a separate row in Table 1 so readers can directly see the base architecture's standalone performance versus baselines, and the additional gain from spatial prior conditioning.
- Clarify the "zero-shot" framing in the abstract and contributions: be explicit about what information from the target region is needed, and discuss realistic scenarios where this is available.
- Run 3–5 seeds and report variance for all metrics, not just TSTR.
- State N_out explicitly in the experimental setup section.
- Resolve the [0,1] vs [-1,1] normalization inconsistency between the text and algorithms.

## Score and Decision

**Round 1 bracket: 6.5–7.5**

Anchor papers across all rounds:
| Path | Avg Human Score | Round | Comparison |
|------|----------------|-------|------------|
| dDdxbdhMsY (Deep Temporal Deaggregation) | 5.00 | 1 | Earlier version of same paper; rejected with missing metrics, no ablation, no baselines in OOD. Current version addresses all of these. |
| 1o3fKLQPRA (DiffPath) | 4.50 | 1 | Simpler diffusion-for-path method; unclear contribution. Paper under review is substantially stronger. |
| VRFotuGLfM (DiffMove) | 6.20 | 1 | Trajectory recovery (narrower task), 2 datasets, no generalization. Paper under review is broader and more comprehensive. |
| kKXIYUi8ff (DynamicsDiffusion) | 3.00 | 1 | Molecular dynamics trajectories; very different domain, weaker results. Not comparable. |
| r125wFo0L3 (Large Trajectory Models) | 5.00 | 1 | Motion prediction for autonomous driving; rejected for unclear design motivation and below-SOTA results. |
| DHCp41nv1M (Spatio-Temporal Diffusion for Scattering) | 6.33 | 2 | Video recovery through scattering media; different domain, rejected. |
| 4anfpHj0wf (Point Set Diffusion) | 7.00 | 1 | Similar scope (diffusion for spatio-temporal generation), accepted. Paper under review has comparable evaluation quality and stronger generalization demonstration. |
| MbM1BqGpZu (Diffusion Transformer Theory) | 6.75 | 2 | Theoretical paper on diffusion transformers; different contribution type. |
| 9UGfOJBuL8 (Conditional Diffusion for Longitudinal) | 7.33 | 2 | Longitudinal medical data generation; different domain, narrower evaluation. |
| DydCqKa6AH (PedGen) | 6.75 | 2 | Pedestrian movement generation; comparable quality but fewer baselines and narrower evaluation. Paper under review is more comprehensive. |
| WeJEidTzff (OD Flow Generation) | 6.75 | 2 | Commuting flow generation; different task, accepted for benchmark contribution. |
| UapxTvxB3N (Trajectory-LLM) | 5.75 | 2 | LLM-based trajectory generation; less comprehensive evaluation. |

**Rationale for 7.0**: The paper is clearly superior to the earlier version (5.0) and to DiffPath (4.5), and comparable to or stronger than PedGen (6.75) and Point Set Diffusion (7.0). The spatial-temporal factorization is a genuine, well-executed insight, the cross-city generalization is unique in the field, and the evaluation is comprehensive. The evaluation framing concerns (metric-conditioning alignment, "zero-shot" terminology) are real but do not invalidate the core contribution — the ablation data makes the contribution decomposition possible even if the paper doesn't present it directly.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
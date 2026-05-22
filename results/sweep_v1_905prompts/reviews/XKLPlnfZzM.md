Now I have enough calibration context. Let me produce the final consolidated review.

---

## Summary

This paper introduces TDDM, a hierarchical diffusion model that factorizes trajectory generation into two components: spatial occupancy priors (marginal distributions over geographical cells, representing *where* people move) and temporal dynamics (learning *how* people move). Regions are canonicalized via similarity transforms, enabling parameter sharing across geographic locations. Evaluated on three cities (Beijing, Porto, San Francisco) with seven standardized metrics, TDDM achieves large improvements in distributional alignment (e.g., KL<sub>sym</sub> 0.277 vs. 1.153 for the best diffusion baseline) and demonstrates zero-shot transfer to unseen city regions and entirely different cities without retraining.

## Strengths

- **Novel spatial-temporal factorization with clean architectural instantiation.** The central idea — decoupling *where* people move from *how* they move — is well motivated (Section 1) and cleanly implemented. The use of similarity transforms (Procrustes-like alignment) to canonicalize regions into $[-1,1]^D$ before modeling (Section 3) is a practical design choice that keeps the architecture simple while enabling parameter sharing across regions. This is concretely validated by the "w/o spatial prior" ablation (Table 2), where removing the prior degrades KL<sub>sym</sub> from 0.277 to 1.334 (4.8×) while TSTR stays unchanged — cleanly isolating that the prior drives coverage.

- **Comprehensive multi-city evaluation with harmonized metrics.** The paper evaluates across three cities on three continents (Asia, Europe, North America) using seven metrics spanning fidelity (TSTR), distributional coverage (KL, JS, Density, Trip), structural fidelity (Pattern), and length distribution (Length). This goes well beyond prior trajectory generation papers that typically use fewer metrics or only one city. The per-city results in the appendix (Table 7) verify consistency rather than cherry-picking.

- **Strong empirical improvements on distributional metrics.** The headline results in Table 1 are genuinely impressive on KL-based metrics: TDDM achieves KL<sub>sym</sub> = 0.277 vs. 1.153 (Diffusion-TS) and JS = 0.059 vs. 0.198 (Diffusion-TS). The advantages on KL<sub>speed</sub> (0.013 vs. 0.035), Density (0.019 vs. 0.029), Trip (0.031 vs. 0.041), and Pattern (0.917 vs. 0.907) are smaller but consistently favorable. The visual comparisons (Figure 2) corroborate the quantitative story.

- **Interesting zero-shot generalization capability.** The finding that TDDM trained on Porto generates trajectories in other cities with TSTR=0.010 and Pattern=0.930 — matching or exceeding its own in-distribution performance — is genuinely novel and nontrivial. The observation that Porto generalizes *better* on average than training on 25% of the target city (Table 3) is a practically significant finding.

- **Honest ablation revealing tradeoffs.** The 1×1 km region ablation shows improved Pattern (0.930 vs. 0.917) but degraded Length error (0.150 vs. 0.004) — the paper transparently presents this tradeoff rather than hiding it. This strengthens credibility.

## Weaknesses

### Fatal

None.

### Major

- **Missing baseline comparisons for generalization experiments (Tables 3, 12).** The paper claims that TDDM's spatial-temporal factorization *enables* zero-shot generalization, but provides no comparison showing how existing methods fare in the same setting. A natural experiment would be: train DiffTraj or Diffusion-TS on the same 25% of a city and evaluate on the full city, or train on one city and evaluate on another. Without such baselines, the reader cannot assess whether TDDM's generalization is genuinely a consequence of the factorization or simply reflects shared structure across cities that any reasonable model might capture. This is the paper's most significant evidential gap, as it directly undercuts the fourth claimed contribution ("Generalization to New Regions").

- **KL evaluation metric is partially aligned with the conditioning signal, inflating headline numbers.** The KL divergence (Section 4) is computed on spatial marginal distributions — the same type of statistic that TDDM conditions on via its spatial prior *H*. Since TDDM is explicitly trained to match these marginals (it receives *H* as input during denoising), the 4× advantage on KL<sub>sym</sub> (0.277 vs. 1.153) partially reflects this alignment rather than purely superior generation quality. This does **not** invalidate the method: the paper also reports KL<sub>speed</sub> (speed distribution, not aligned with the prior) where TDDM still leads (0.013 vs. 0.035), and Density/Trip/Pattern/TSTR all confirm improvements on metrics that are not aligned with the conditioning signal. However, the paper does not acknowledge this issue or discuss how large the inflation factor might be. The authors should: (a) explicitly state the computation resolution and domain of each KL metric, (b) report KL at multiple grid resolutions, and (c) discuss the relationship between conditioning and evaluation directly.

### Minor

- **TSTR improvement may not be statistically significant.** The paper reports TDDM = 0.011 ± 0.006 vs. DiffTraj = 0.013 ± 0.005 (Table 1). Given overlapping standard deviations, the abstract's claim that TDDM "outperforms them on fidelity as measured by TSTR" overstates the evidence. The direction is consistent, but the authors should either provide confidence intervals or a significance test, or soften the claim.

- **Computational cost and model scale not reported.** The paper uses a transformer with trajectory tokens (one per time step) plus up to 4,096 spatial-prior tokens (64×64 grid) per input, but reports no training time, inference throughput, parameter count, number of layers/heads, or comparison to baseline model sizes. This makes it difficult for practitioners to assess the practical cost of the quality gain.

- **Region-boundary handling is underspecified.** The paper states that sampling uses a grid "with partial border overlap" (Section 3) and that Algorithm 2 generates trajectories region-by-region. However, it does not explain how trajectories that span multiple regions are handled, whether stitching is needed, or how overlap regions are resolved to avoid discontinuities or double-counting at borders. Since real trajectories frequently cross region boundaries, this gap affects both reproducibility and real-world applicability.

### Trivial

- The KL<sub>speed</sub> column in Table 1 and KL<sub>peeed</sub> in Table 2 both appear to contain a rendering artifact in the subscript.

## Nice-to-Haves

- The generalization experiments would benefit from a brief analysis of *why* Porto is a strong source city (e.g., trajectory length distribution, road network complexity, speed distribution) to help practitioners select training cities.
- Reporting city-by-city results in the main text (currently only in the appendix, Table 7) would provide more transparency than the aggregated averages alone.
- The spatial prior is currently estimated from target trajectories — discussing how it could be estimated from proxies (satellite imagery, census data, adjacent cities) when no target trajectories are available would strengthen the practical impact.

## Removed Points

*"The paper lacks baselines DiffTime and CSDI"* — The paper covers five major generative paradigms with available code (TimeGAN, TimeVAE, COSCI-GAN, Diffusion-TS, DiffTraj). The authors explicitly note that TrajGen and ControlTraj lack reproducible code, which is a valid exclusion criterion. Suggesting specific additional baselines beyond reasonable coverage is not a weakness.

*"Formatting nitpicks, typos, presentation issues"* — These are parser artifacts, not author errors.

*"Strength: 'this paper addressed an important problem'"* — Generic and not specific to this paper.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add at least one baseline to the generalization experiments** (Tables 3/12). Train DiffTraj or Diffusion-TS on 25% of a city and evaluate on the full city, and train on Porto/Geolife and evaluate on the other cities. This single comparison would substantially strengthen the paper's central generalization claim.
2. **Disclose the exact computation of each KL metric** — what grid resolution is used, whether it is computed on the same 64×64 region-level grid as the prior or a different city-level grid — and add a brief discussion of the relationship between the conditioning signal and the evaluation metric.
3. **Provide confidence intervals or note the statistical overlap** for TSTR comparisons, and adjust any overstrong claims (e.g., "outperforms them on fidelity as measured by TSTR") accordingly.
4. **Report the model's computational footprint** (parameter count, training/inference time) alongside baseline sizes for practical reference.
5. **Clarify region-boundary handling** — how are trajectories that cross region borders generated and stitched together without artifacts?

## Score and Decision

### Calibration Summary

**Round 1 — Bracketing.** Three queries on "trajectory generation diffusion model spatial priors" over three score bands:

| Band | Anchors | Avg Scores |
|------|---------|------------|
| Low (≤3.5) | kKXIYUi8ff (3.00), 2orBSi7pvi (3.00), pzZjyYee6L (2.50), FjifPJV2Ol (3.40) | 2.50–3.40 |
| Mid (3.5–7.5) | dDdxbdhMsY (5.00), VRFotuGLfM (6.20), JZgqoOu4Ml (4.00), r125wFo0L3 (5.00) | 4.00–6.20 |
| High (≥7.5) | uKZdlihDDn (7.60), fV0t65OBUu (8.00), 6EUtjXAvmj (8.00), EO8xpnW7aX (8.00) | 7.60–8.00 |

The paper is clearly not in the low or high bands. **Round 1 bracket: 5.0–7.0.**

**Round 2 — Narrowing.** Two queries targeting the (4.5, 6.5) and (5.5, 7.5) bands:

- **dDdxbdhMsY** (avg 5.00): A prior version of this same line of work, rejected with scores 6,6,3. The current TDDM paper is substantially stronger — it adds metrics (Density, Trip, Length, Pattern), ablation studies, per-city breakdowns, and standard deviations. TDDM is ~1–1.5 points above this anchor.
- **VRFotuGLfM** / DiffMove (avg 6.20, rejected): A trajectory recovery (not generation) paper with a conditional diffusion model on two datasets. TDDM has a more novel contribution (spatial-temporal factorization vs. a conditional denoiser), evaluates on three cities with more metrics, and demonstrates a harder generalization task (city-to-city zero-shot, not within-city recovery). Comparable or slightly stronger.
- **DydCqKa6AH** / PedGen (avg 6.75, accepted): Pedestrian movement generation with a dataset contribution. The reviews are mixed (8,6,5,8). TDDM is similarly solid in evaluation depth and more novel in methodology; both papers have actionable weaknesses.
- **dTGH9vUVdf** / FreeVS (avg 5.80, accepted): View synthesis with mixed reviews. TDDM has fewer major weaknesses.

**Final position:** The paper is stronger than its prior version (5.00) and comparable to DiffMove (6.20). It is held back from the 7+ range by two substantive evidential gaps (missing generalization baselines, KL metric alignment) that weaken the strongest claimed advantages. The core contribution (spatial-temporal factorization with canonicalization) is real and the evaluation is otherwise thorough.

**Final score: 6.0** — This is a solid paper with a clear methodological contribution, strong empirical evaluation, and interesting generalization results. The two major weaknesses are addressable in rebuttal and do not invalidate the core contribution, but they prevent the paper from being outstanding.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
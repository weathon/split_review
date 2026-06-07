Now I have a clear picture. Let me finalize the review.

## Calibration Summary

**Round 1 bracket: 5.5–7.0**

**Round 2 narrows to: 6.0–6.5**

Anchor comparisons:
| Paper | Score | Comparison |
|---|---|---|
| Deep Temporal Deaggregation (prior version) | 5.00 | Our paper is clearly stronger: more baselines, metrics, ablation, cross-city experiments |
| DiffPath | 4.50 | Our paper is substantially stronger in novelty, evaluation breadth, and contribution |
| DiffMove | 6.20 | Our paper has more novelty (factorization idea), more comprehensive evaluation (5 baselines vs theirs), and cross-city generalization they don't attempt |
| LocDiffusion | 5.80 | Different task; our paper has stronger evaluation and generalization results |
| PedGen | 6.75 | Comparable. PedGen has dataset + method; we have more baselines/metrics and cross-city generalization. PedGen accepted. Our paper is slightly weaker due to unfair in-distribution comparison framing |
| Commuting OD Flow | 6.75 | Different type (dataset/benchmark). Our method contribution is more novel but the framing issue pulls it slightly below |

The paper sits between DiffMove (6.20, rejected) and PedGen (6.75, accepted). The spatial-temporal factorization is genuinely novel, the cross-city generalization is well-demonstrated, and the Porto-as-universal-source finding is insightful. But the in-distribution comparison framing is problematic — TDDM receives spatial prior information that baselines don't, and the paper's own ablation shows this is the dominant factor. This is addressable in revision but prevents the paper from reaching the 6.75 level.

**Final score: 6.0**

---

## Summary
This paper introduces the Temporal Deaggregation Diffusion Model (TDDM), which factorizes trajectory generation into spatial priors (marginal occupancy distributions H over 64×64 grids, computed from training data) and temporal dynamics. A similarity transform canonicalizes geographic regions, enabling a single transformer-based diffusion model to generate trajectories for arbitrary regions without retraining. The paper evaluates on three cities across three continents with ten metrics and five baselines, and demonstrates cross-city generalization where a Porto-trained model generates plausible trajectories for other cities using only the target's spatial prior.

## Strengths
- **Spatial-temporal factorization is a clean, well-motivated conceptual advance.** The decoupling of *where* people move (spatial prior H) from *how* they move (temporal dynamics) is novel. The ablation (Table 2) provides direct evidence: removing H leaves TSTR unchanged (0.011 vs. 0.011) but degrades KL_sym ~5× (0.277 → 1.334), confirming spatial priors are causal for distributional coverage while temporal dynamics independently support per-sample fidelity.
- **Canonicalization via similarity transform enables genuine cross-region transfer.** Normalizing regions to [-1,1]² and applying the inverse at generation time (Algorithm 2, line 11) is a lightweight design with outsized impact. Table 3 shows Porto-trained models achieve KL_sym 0.335 on other cities — competitive with training on 25% of the target city (KL_sym 0.545). Pattern scores remain above 0.915 across all cross-city transfers.
- **Porto as a "universal source" city is a practically significant and surprising finding.** The result that a model trained solely on Porto achieves better distributional metrics on other cities than training on 25% of the target city data is both unexpected and useful for data-scarce deployment. The paper correctly identifies the length-error tradeoff (0.060 vs. 0.026), showing awareness of the method's limitations.
- **Comprehensive multi-continent benchmark with harmonized metrics.** The evaluation across Beijing, Porto, and San Francisco with metrics spanning fidelity (TSTR), distributional coverage (KL variants, JS), proportionality (Density, Trip), and structure (Pattern, Length) provides a useful template for the field.
- **Algorithmic transparency and robustness checks.** Algorithms 1 and 2 are fully specified. The map-matching ablation (Section 4.2) confirms TDDM's advantage persists without preprocessing, and Figure 2 provides convincing qualitative evidence that TDDM trajectories respect road structure while baselines generate off-road trajectories.

## Weaknesses

### Major
- **The in-distribution comparison is not a fair test of unconditional generation.** TDDM conditions on spatial priors H computed from training data — a 64×64 discretized marginal distribution encoding where trajectories go in each 3×3 km region. The baselines (Diffusion-TS, DiffTraj, TimeGAN, TimeVAE, COSCI-GAN) receive no equivalent information. Table 2 makes this explicit: removing H degrades TDDM's KL_sym from 0.277 to 1.334, which is *worse* than Diffusion-TS (1.153). While TDDM without H still leads on TSTR (0.011 vs. 0.014 for Diffusion-TS), the large margins on distributional metrics that dominate the paper's headline claims (4× reduction in KL divergences) are attributable primarily to the spatial prior information, not the deaggregation architecture per se. The paper frames Section 4.1 as "unconditional trajectory generation" but TDDM is effectively a spatially-conditioned model. This matters because readers may attribute the gains to the transformer-diffusion architecture rather than to the spatial prior, which is the actual locus of contribution.
- **Partial circularity between spatial prior conditioning and evaluation.** TDDM is conditioned on H (a spatial marginal) and evaluated on metrics that directly measure spatial distribution matching (KL, JS, Density, Trip). TSTR partially escapes this circularity — the TSTR advantage is small but directionally positive (0.011 vs. 0.013). The paper also does not specify the discretization resolution used for KL computation; if it matches or resembles the 64×64 H grid, the circularity is severe. This does not invalidate the method but means the quantitative dominance on distributional metrics should be interpreted with caution.

### Minor
- **"Zero-shot" framing is overstated.** Algorithm 2, line 3 computes H from target trajectories X_target. While the model never sees individual target trajectories (only aggregate spatial statistics), the term "zero-shot" implies no target data at all. The paper partially clarifies this in the text (line 173: "the model ε_θ never receives individual target trajectories, only their aggregate spatial distribution"), but the abstract and contribution claims should be more precise.
- **The "w/o spatial prior + rejection" ablation is confusingly described.** Table 2 includes this variant but the paper does not specify what distribution is used for rejection sampling. If it uses H (which was supposedly removed), the setup is contradictory.
- **KL discretization resolution is unspecified.** The paper does not state the grid resolution used for KL divergence computation in Tables 1–3. This should be reported so readers can assess whether it differs from the 64×64 H grid.
- **No per-city variance for distributional metrics.** TSTR reports standard deviations, but KL, JS, Density, Trip, Length, and Pattern metrics do not. With only three datasets, reporting per-city results and their spread is minimum standard to assess consistency.

### Trivial
- **Filtering criteria in Algorithm 1, line 5 are not specified.** The minimum length, maximum time gaps, and speed limits used to filter contiguous subsequences are important hyperparameters affecting what patterns the model can learn.

## Nice-to-Haves
- Adding a baseline that receives the same spatial prior H (e.g., training Diffusion-TS with H concatenated, or using H for rejection sampling atop an unconditional model) would isolate the contribution of the deaggregation architecture from the spatial prior information and strengthen the claims.
- Expanding the analysis of *why* Porto works as a universal source (dataset size, trajectory diversity, road network topology) would deepen the generalization contribution.
- Reframing the in-distribution results as a spatially-conditioned generation benchmark would be more accurate while still showcasing the method's strengths.

## Removed Points
These points are flagged to be removed — treat them with caution.

- **Baseline exclusion of TrajGen and ControlTraj is questionable.** Removed per hard rule: this questions the availability of cited works. Reproducing complex methods from scratch without source code is also an unreasonable burden to demand of authors. The baseline set of five methods spanning GANs, VAEs, and diffusion models is already comprehensive.
- **Appendix-dependent speculation about variance estimates.** Removed per hard rule: the appendix is stripped by the parser and exists in the original submission. Criticisms that depend on what the appendix "may" or "may not" contain are speculative.

## Novel Insights
The harsh critic correctly identifies that the in-distribution comparison conflates the contribution of spatial prior information with the deaggregation architecture. However, the paper's own ablation (Table 2) actually provides the evidence to disentangle these cleanly: spatial priors are causal for distributional coverage (KL, JS) while temporal dynamics (measured by TSTR) transfer independently. This proves exactly what the paper hypothesizes — that spatial occupancy priors are the key missing ingredient for distributional alignment in trajectory generation. The tension between the two review inputs highlights a framing problem rather than a methodological one: the paper should present itself as demonstrating that spatial priors unlock distributional coverage and cross-city generalization, rather than claiming unconditional generation SOTA.

## Suggestions
- Restructure to make cross-city generalization the primary claim, with in-distribution results presented as a spatially-conditioned generation benchmark.
- Add a note to Table 1 clarifying what information each model receives (spatial prior H vs. unconditional).
- Report the KL discretization resolution and confirm it differs from the 64×64 H grid, or acknowledge the circularity.
- Clarify the "w/o spatial prior + rejection" ablation setup in Table 2.
- Report per-city metrics or standard deviations for all evaluation measures, not just TSTR.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>
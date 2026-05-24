Now I have a good calibration context. Let me write the final review.

**Round 1 bracket**: Based on the initial calibration search, relevant papers span from weak anchors (2.5–3.0, Reject) to strong anchors (8.0, Accept). The most topically relevant trajectory-generation papers fall between 4.0 and 6.5. My initial bracket is **5.0–7.0**.

**Round 2 narrowing**: TrajFlow (6.50, Accept) — flow-matching for GPS trajectories, single Japanese dataset, nationwide scale. MoRA (6.00, Accept) — geospatial representation learning with mobility graphs. Comparing: the current paper has stronger conceptual novelty (spatial-temporal factorization) and broader evaluation (3 continents) than TrajFlow, but TrajFlow tackles nationwide scale. The current paper's weaknesses (terminology stretch, missing DiffTraj protocol, no error bars on distributional metrics) are fixable but meaningful. I place the paper at **6.0**.

---

## Summary

This paper introduces the Temporal Deaggregation Diffusion Model (TDDM), which factorizes trajectory generation into spatial occupancy priors (marginal distributions over *where* people are) and temporal dynamics (*how* they move in time). Regions are canonicalized via similarity transforms so the model learns location-invariant motion patterns. A transformer-based diffusion model is conditioned on the spatial prior to generate trajectories that respect that prior in aggregate. Experiments on three cities across three continents (Beijing, Porto, San Francisco) show up to 4× lower symmetric KL divergence than leading diffusion baselines, and the model demonstrates transfer to unseen city regions and entirely new cities without gradient updates on target data.

## Strengths

- **Spatial-temporal factorization is a genuinely novel and well-articulated idea.** Decoupling *where* from *how* is a clean conceptual contribution that differs fundamentally from prior trajectory generation work. The similarity-transform canonicalization is a simple but effective mechanism to enable parameter sharing across geographic regions, and it is concretely described (Equations 2–5, Algorithms 1–2). The paper correctly identifies sample-specific conditioning in prior diffusion models as a barrier to generalization, and the factorization directly addresses this.

- **Strong empirical results across a standardized three-continent benchmark.** TDDM achieves KL_sym = 0.277 vs. 1.153 for the best diffusion baseline (Diffusion-TS) across three cities (Table 1). The evaluation framework covering fidelity, diversity, proportionality, usefulness, and generalization is methodically constructed, with six complementary metrics. The benchmark itself (three cities, standardized preprocessing, public datasets) is a valuable resource.

- **Ablation study cleanly isolates the role of spatial priors.** Table 2 is particularly informative: removing the spatial prior causes KL_sym to jump from 0.277 to 1.334 (≈5× worse) while TSTR stays unchanged (0.011 for both), demonstrating that priors are essential for distributional coverage and proportionality but not for per-trajectory fidelity. The 1×1 km vs. 3×3 km ablation reveals a concrete tradeoff between local coherence and global realism.

- **Counterintuitive and actionable finding about Porto as a universal source dataset.** Section 4.3 reports that Porto-trained models generalize with lower KL and JS (0.335, 0.071) than models trained on 25% of the target city (0.545, 0.106). This is a practically useful insight for practitioners who may have limited local data.

## Weaknesses

### Major

- **DiffTraj evaluation protocol is not described.** DiffTraj (Zhu et al., 2023) is a *conditional* model designed for trajectory completion/inpainting with strong sample-specific conditioning. The paper simply calls it a "UNet-based trajectory diffusion model" (Section 4) without explaining how it was adapted for unconditional generation. If it was trained unconditionally by removing its conditioning mechanism, that would underutilize its architecture; if used in a conditional setting, the comparison is apples-to-oranges. This is a concrete missing detail that affects interpretability of the main comparison.

- **No uncertainty quantification for distributional metrics.** Table 1 reports TSTR with standard errors (±) but KL(S∥R), KL(R∥S), KL_sym, JS, Density, Trip, Length, and Pattern are all reported as point estimates without variance. KL divergences can be sensitive to binning choices and sampling randomness. Without error bars, the reader cannot assess whether the reported gaps (e.g., KL_sym 0.277 vs. 1.153) are stable across runs.

### Minor

- **"Zero-shot" terminology is somewhat overstated.** The paper calls the generalization setting "zero-shot" (Section 4.3, Algorithm 2), but the spatial prior *H* is computed directly from target trajectories (Algorithm 2, line 3: "Compute heatmap H = f(r_c, X_target)"). The model receives non-trivial aggregate information about the target distribution. The paper clearly describes what it does ("using solely the spatial prior H, with no gradient updates on target trajectories"), so the setup is correct — but labeling it "zero-shot" will mislead readers into thinking no target data whatsoever is used. A term like "conditionally zero-shot" or "data-efficient transfer" would be more precise.

- **Primary comparison conflates the benefit of the conditioning signal with the benefit of the architecture.** TDDM conditions on the spatial prior *H* at both training and generation time, while all baselines (Diffusion-TS, TimeGAN, etc.) are unconditional. The ablation shows that removing the prior collapses performance, meaning most of TDDM's advantage on distributional measures comes from having the prior as conditioning, not necessarily from better-learned temporal dynamics. The paper should explicitly acknowledge this confound: the comparison validates the *factorization*, but does not isolate whether the specific deaggregation architecture adds value beyond simply conditioning *any* diffusion model on a heatmap. Discussing this gap would strengthen the paper's framing.

### Trivial

- None.

## Nice-to-Haves

- **Test with a "wrong" prior.** Conditioning TDDM on a prior that does not match the training data (e.g., a uniform distribution or a prior from a different city) would directly verify that the model actually follows the conditioning signal, not just generates from a learned marginal. This would provide stronger evidence of controllability than the negative ablation (removing the prior).
- **Evaluate with priors not derived from target trajectories.** The paper claims the approach can work with priors from external sources (e.g., population density grids, land-use data), but never tests this. An experiment with an externally-sourced prior would validate a genuinely zero-shot pipeline.
- **Sensitivity analysis for region size.** The ablation compares 1×1 km vs. 3×3 km, but varying in the other direction (e.g., 5×5 km) would help characterize how robust the method is to this hyperparameter choice.

## Removed Points

The following points from the reviewer inputs were removed with justification:

- *"KL divergence specification is missing from the main paper"* — The appendix (stripped by the parser) contains these details. Per protocol, missing appendix content in the parse is not a paper flaw.
- *"Paper should give baselines the same conditioning signal"* — This asks for an experiment beyond the paper's scope. The paper's ablation (removing the prior from TDDM) is the standard control direction. Giving baselines the prior would be useful additional analysis but is not required to validate the contribution.
- *"The paper does not report failure cases"* — A general suggestion, not a concrete weakness. No specific failure mode is identified from the paper's content.
- *"Strength: counterintuitive finding about Porto"* — This is kept as a strength, properly attributed.
- *Strength Finder claims about "problem being important"* — Generic, removed.
- *Strength: "Transformer architecture details"* — This is kept as it is concrete and specific.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify the DiffTraj evaluation protocol** — Specify whether DiffTraj was trained unconditionally (and how its conditioning mechanism was disabled) or used in its original conditional formulation. If the latter, describe what conditioning signal was provided. This is essential for reproducibility.

2. **Report uncertainty for all distributional metrics** — Provide standard deviations or confidence intervals for KL, JS, Density, Trip, Length, and Pattern across at least 3 random seeds (or data splits). If the metrics are expensive, a reduced-scale version would still be informative.

3. **Acknowledge the conditioning confound explicitly** — Add a sentence in Section 4.1 or the Conclusion noting that TDDM benefits from having the spatial prior as an additional input, and that a portion of the gain vs. unconditional baselines is attributable to this extra signal rather than the architecture alone. Cite the ablation as evidence.

4. **Rename or qualify "zero-shot"** — Use a more precise term such as "conditionally zero-shot," "data-efficient transfer," or "prior-conditioned generation" to avoid misleading readers. The current description is technically accurate but the label is not.

## Score and Decision

### Calibration Anchors

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| gxqYtVVZRI | 3.00 | 1 | Spatio-temporal interpolation diffusion; weaker method and evaluation |
| MKM8iEaowV | 3.00 | 1 | Diffusion + RL for trajectory planning; different problem scope |
| f2nxdOv1Uh | 2.67 | 1 | Multimodal trajectory generation for autonomous driving; limited evaluation |
| w7xpNeFIbb | 4.00 | 1 | Diffusion foundation model for maritime trajectories; conceptually similar domain but rejected |
| BZ1vutP53o | 4.00 | 1 | Topology-enhanced diffusion for event prediction; different task |
| 6jThckejtL | 5.00 | 1 | JointDiff: multi-agent trajectory diffusion; application-driven |
| BDOldEjwCE | 6.50 | 1,2 | TrajFlow: flow-matching GPS trajectory generation; most similar in domain, slightly stronger empirical scope (nationwide) but only one dataset |
| IlBr5JJsCj | 6.00 | 2 | MoRA: geospatial representation learning; comparable quality, different task |

**Round 1 bracket**: 5.0–7.0. **Round 2 narrowing**: TrajFlow (6.50) is the nearest anchor — the current paper has stronger conceptual novelty but also clearer evaluation gaps, placing it slightly below. MoRA (6.00) provides a useful midpoint reference. **Final score: 6.0.**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
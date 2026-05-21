Now I have enough calibration data. Let me write the final consolidated review.

## Summary of Calibration

**Round 1 bracket:** Between 3.5 and 7.5. The paper is clearly above the weak anchors (all at 3.00) and below the strong anchors (7.50–8.00).

**Round 2 narrowing anchors:**
- dDdxbdhMsY.md (5.00) — "Deep Temporal Deaggregation" — earlier version of the same approach. Its weaknesses (no ablation, limited metrics, missing conditioned baselines) are substantially addressed in the current TDDM paper, making TDDM clearly stronger.
- VRFotuGLfM.md (6.20) — "DiffMove" — trajectory recovery via conditional diffusion. Comparable experimental rigor; TDDM has broader scope (3 cities, more metrics) but DiffMove has a cleaner problem framing. TDDM is slightly weaker due to comparison fairness concerns.
- 1o3fKLQPRA.md (4.50) — "DiffPath" — path generation, weaker in both novelty and experimental evidence. TDDM is clearly stronger.
- YOKnEkIuoi.md (5.80) — "CVDM" — conditional diffusion with learned schedules. Similar magnitude contribution, similar mix of strengths (practical, works well) and weaknesses (some framing issues). TDDM is comparable. This was Accepted.

**Final score decision:** Placing TDDM between the 5.00 anchor (earlier version, clearly weaker) and the 6.20 anchor (DiffMove, slightly cleaner), with CVDM at 5.80 as a close analog — I settle on **5.5**. The core contribution is solid but the evaluation framing has issues that prevent a higher score.

---

## Review

## Summary

This paper introduces TDDM, a diffusion model for trajectory generation that factorizes the problem into spatial occupancy priors ("where" people move) and temporal dynamics ("how" they move). The model conditions generation on a discrete marginal distribution over geographic occupancy (spatial prior H), canonicalizes each region via similarity transforms to handle different locations, and uses a transformer encoder for denoising. Experiments on three city-scale datasets (Geolife/Beijing, Porto, Cabspotting/SF) show strong distributional alignment and generalization to unseen cities without gradient updates on target data.

## Strengths

1. **Novel spatial-temporal factorization for trajectory generation.** The core idea — conditioning on aggregate spatial occupancy priors rather than trajectory-level features — is well-motivated and genuinely distinct from prior work. Separating *where* from *how* people move is a clean conceptual contribution that enables transfer without per-trajectory conditioning. The paper formalizes this through Equation (1) and the mixture model in Equation (5).

2. **Clear experimental improvement on multiple axes.** Table 1 shows TDDM consistently leads on TSTR (0.011 vs. 0.013 for the next-best DiffTraj), Density (0.019 vs. 0.029), Trip (0.031 vs. 0.041), and Pattern (0.917 vs. 0.907). The gains are not just on spatial marginal metrics but also on measures of temporal realism and downstream usefulness, which provides convergent evidence.

3. **Well-designed ablation study (Table 2).** Removing the spatial prior causes KL_sym to jump from 0.277 to 1.334 (worse than all diffusion baselines), while TSTR stays identical at 0.011. This cleanly attributes the distributional gains to the conditioning mechanism rather than the transformer/diffusion backbone, and it honestly shows what the model does and does not contribute.

4. **Multi-city generalization experiments.** Table 3 demonstrates that a model trained on Porto can generate trajectories for other cities with KL_sym = 0.335 — not far from in-distribution performance (0.278) — using only the spatial prior from the target city. This goes beyond most prior trajectory generation work, which evaluates only in-distribution.

5. **Rigorous, reproducible evaluation framework.** The paper evaluates across three cities on different continents using six complementary metrics (TSTR, KL, JS, Density, Trip, Length, Pattern), establishing a standardized protocol that the field has been lacking. The preprocessing pipeline (resampling, map matching) is consistently applied to all models.

## Weaknesses

### Major

1. **Asymmetric comparison against unconditional baselines frames the wrong experiment.** The paper titles Section 4.1 "Large-Scale Unconditional Trajectory Generation" and defines the task as unconditional (Section 2), but TDDM is a *conditional* model that receives the spatial prior H during both training and generation. The baselines (TimeGAN, Diffusion-TS, DiffTraj) receive no equivalent information. The large KL margins in Table 1 (e.g., KL_sym 0.277 vs. 1.153 for Diffusion-TS) are therefore unsurprising — they primarily reflect the advantage of conditioning, not architectural superiority. The ablation confirms this: without H, TDDM's KL_sym (1.334) is *worse* than Diffusion-TS (1.153) and DiffTraj (1.232). This means the paper's headline claim of "4× lower KL divergence" conflates two separate effects — the conditioning framework and the model architecture. The paper would be much stronger if it compared against baselines augmented to also condition on H (e.g., by concatenating a flattened spatial prior), thereby isolating the contribution of the tokenization and transformer design from the contribution of conditioning itself.

2. **"Zero-shot" generalization claim is overstated.** In both intra-city and city-to-city generalization (Section 4.3), the spatial prior H is computed from **target** trajectory data X_target (Algorithm 2, line 3). The model never sees individual target trajectories and performs no gradient updates, which is a useful form of transfer — but this is not "zero-shot" in the standard ML sense, where no examples from the target class are observed at all. A genuine zero-shot demonstration would require estimating H from non-trajectory sources (e.g., population density, road network density, points of interest). Without this, the generalization experiment is conditional generation using a small amount of target-derived aggregate statistics. The paper should either replace "zero-shot" with a more precise term (e.g., "gradient-free transfer" or "aggregate-conditioned generalization") or demonstrate generation with a prior derived from non-trajectory data.

### Minor

3. **KL-based metrics are partially circular for the conditioning.** The KL and JS divergences measure alignment of the spatial marginal distribution — exactly the quantity the model is conditioned on (H). Low KL is expected when the model receives the target marginal as input and is trained to reproduce it. This does not invalidate the metrics (they still measure whether the model respects the given prior), but the paper leans heavily on KL gains as evidence of generative quality (abstract, contributions, conclusion). These claims should be de-emphasized or reframed as evaluating the model's ability to follow the conditioning, not its generative fidelity independent of the prior. The paper's non-KL metrics (TSTR, Pattern, Length, Trip, Density) already provide the kind of evidence that separates spatial fidelity from temporal/structural realism — these should be elevated.

4. **No sensitivity analysis for key hyperparameters.** Region size (3×3 km) and grid resolution (64×64) are central design choices that affect both performance and token cost. The ablation with 1×1 km regions (Table 2) shows a substantial increase in Length error (0.150 vs. 0.004), suggesting sensitivity to this parameter, but there is no systematic study of how results change with different region sizes, grid resolutions, or overlap configurations. This limits understanding of when the method works and when it breaks.

5. **Temporal realism analysis is incomplete.** The paper evaluates temporal patterns indirectly through TSTR and Length error, but does not directly analyze speed distributions, turn angles, acceleration profiles, or stop-and-go behavior. Since the core claim involves separating "where" from "how," direct temporal metrics would strengthen the demonstration that the model learns transferable motion dynamics, not just spatial layout memorization.

### Trivial

6. None beyond formatting artifacts introduced by the parser.

## Removed Points

- **"Unfair comparison invalidates headline claims"** (from Harsh Critic #1): Downgraded from "structurally invalid" (their characterization) to Major weakness #1 above. The comparison is asymmetric but not invalid — the paper's contribution IS the conditioning framework, and comparing against unconditional baselines is standard for a new method. The issue is the *framing* (calling it unconditional) and the *lack of conditioned baselines*, not structural invalidity.

- **"Evaluation metrics are biased toward the proposed method"** (from Harsh Critic #3): Merged into Minor weakness #3 above. The paper does use multiple non-KL metrics that are not circular, so the concern is about emphasis, not validity.

- **"No demonstration of generation with non-trajectory prior"**: This is a nice-to-have suggestion, not a weakness. The paper's generalization already shows useful transfer; the non-trajectory prior experiment would be a stronger demonstration but is beyond the stated scope.

- **"The role of map matching is not fully explored"**: The paper discusses map matching and includes an appendix table showing consistent results without it. This is adequately addressed.

- **Missing related works / missing appendix content**: Removed per hard rules.

- **Generic strengths from Strength Finder**: Removed "addressed an important problem," "clear motivation" as generic. Kept only concrete, evidence-anchored strengths.

## Nice-to-Haves

- **Conditioned baselines**: The single most impactful addition would be to compare TDDM against baselines that also receive the spatial prior H (e.g., by feeding H into Diffusion-TS's conditioning mechanism). This would isolate whether TDDM's architectural choices (transformer tokenization, canonicalization) add value beyond the conditioning itself.
- **Non-trajectory spatial prior**: Demonstrating generation using H estimated from satellite imagery, population density, or road intersection density would constitute a genuine zero-shot result and significantly strengthen the generalization claims.
- **Direct temporal metrics**: Adding comparisons of speed distributions, turn angle histograms, and acceleration profiles between real and synthetic trajectories would concretely demonstrate that the model learns transferable motion dynamics.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface an unexpected interpretation that the paper itself misses. The spatial-temporal factorization is well-explained, and the weakness about asymmetric comparison is a standard methodological concern rather than a novel observation.

## Suggestions

1. Reframe the evaluation to explicitly acknowledge the asymmetry: TDDM is a conditional model, the baselines are unconditional. Either add conditioned baselines or clearly separate the claim into (a) "the conditioning framework improves results" (supported) and (b) "the model architecture is superior" (needs conditioned baselines).
2. Replace "zero-shot" with a more precise term such as "gradient-free transfer" or "aggregate-conditioned generalization" in the abstract, contributions, and Section 4.3.
3. Move the KL-based headline claims from the abstract/contributions to a supporting role, and elevate TSTR, Pattern, Density, and Trip error as primary evidence of generative quality.
4. Add a hyperparameter sensitivity analysis for region size and grid resolution, even as an appendix table, to help readers understand when the approach breaks down.

## Score and Decision

**Round 1 bracket:** The paper sits between the weak anchors (avg 3.00, all rejects) and strong anchors (7.50+, accepts). Initial plausible range: 4.5–7.0.

**Round 2 narrowing:** Compared to:
- *dDdxbdhMsY.md* (5.00, "Deep Temporal Deaggregation" — a prior version): TDDM is clearly stronger — it adds ablations, more metrics, city-to-city transfer, and better framing. Improvement of ~0.5 over this anchor.
- *VRFotuGLfM.md* (6.20, "DiffMove"): Comparable trajectory-diffusion paper with cleaner problem framing. TDDM has broader scope but the comparison fairness issue detracts. Slightly weaker than this anchor.
- *YOKnEkIuoi.md* (5.80, "CVDM"): Similar contribution magnitude — practical method that works well, with some framing/novelty concerns. Comparable.
- *1o3fKLQPRA.md* (4.50, "DiffPath"): Weaker in both novelty and evidence. TDDM is clearly stronger.

**Final score:** 5.5. The paper's core idea is novel and the experiments are extensive, but the asymmetric comparison and overclaimed "zero-shot" terminology are significant issues that prevent a higher score.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
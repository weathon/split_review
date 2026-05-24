Now I have a good understanding of the paper. Let me verify a few specific claims from the harsh critic before doing calibration.Now let me calibrate against human-reviewed anchors.The Deep Temporal Deaggregation (dDdxbdhMsY) anchor at score 5.0 is remarkably similar — looks like an earlier version of this same work that addressed reviewer concerns by adding Density/Trip/Length/Pattern metrics and an ablation removing the prior. Let me narrow in this range.Now I have enough calibration to write the final review.

## Summary
The paper proposes TDDM (Temporal Deaggregation Diffusion Model), a transformer-based diffusion model for large-scale 2D mobility trajectories that factorizes generation into a per-region spatial occupancy heatmap H (the "spatial prior") and learned temporal dynamics in a canonicalized [-1,1]² frame. The paper introduces a harmonized multi-city benchmark (Geolife/Porto/Cabspotting × six metrics) and reports large gains in distributional KL/JS/Density/Trip/Pattern over GAN-, VAE-, and diffusion-based baselines, plus zero-shot intra-city and city-to-city transfer.

## Strengths
- **Genuinely interesting factorization with a working canonicalization trick.** The "where vs. how" decomposition with a per-region similarity transform (§3) lets a single model be reused across regions and cities; this is a non-trivial architectural choice and is supported by the cross-city transfer results in Table 3 (Pattern ≥ 0.915, TSTR matching in-distribution when trained on Porto).
- **Standardized multi-city benchmark.** The paper combines fidelity (TSTR), divergence (KL/JS), and prior trajectory-specific measures (Density, Trip, Length, Pattern) from Zhu et al. (2023) into a single protocol across three continents (§4, Table 1). The benchmark itself, with consistent preprocessing and map-matching ablation (Table 9, referenced in §4.2), is a useful artifact for the community.
- **Strong qualitative evidence of structural faithfulness.** Figure 2 shows TDDM produces trajectories with road-aligned support and density "holes" between roads that baselines do not capture; this corroborates the Pattern score gain (0.917 vs. ≤0.907).
- **Ablation isolating the spatial prior.** Table 2 cleanly shows that removing H collapses KL_sym from 0.277 to 1.334 while TSTR is unchanged, directly attributing the distributional gain to the spatial-prior mechanism. (Note: this same evidence also fuels a weakness — see below.)

## Weaknesses

### Fatal
None — the critique below is serious but does not by itself invalidate the paper's contribution, which is centered on the factorization, the canonicalization trick, and the benchmark rather than on outperforming unconditional baselines on raw divergence.

### Major
- **The headline KL/JS/Density/Trip wins are partly built into the sampling protocol.** Algorithm 2 line 3 computes H from X_target, and line 4 sets the per-region sample count proportional to the target's empirical occupancy. KL/JS/Density/Trip are all functions of the spatial marginal, which TDDM is given as an input while every baseline must learn it from training data. The ablation in Table 2 makes this transparent: with the prior stripped out, TDDM's KL_sym (1.334) and JS (0.228) are *worse* than Diffusion-TS's (1.153 / 0.198). On the two metrics least dependent on H — TSTR (0.011 vs. 0.013 / 0.014, well within the ±0.006 std) and Length error (TDDM 0.004 vs. Diffusion-TS 0.003) — the advantage essentially disappears. The abstract/§4.1 statement that TDDM "improves trajectory fidelity and coverage over leading baselines" is therefore stronger than the experiments support; the more accurate statement is that spatial-prior conditioning improves coverage over *unconditional* baselines. A matched-conditioning baseline (e.g., heatmap-conditioned Diffusion-TS or DiffTraj) is needed to disentangle "our architecture uses H well" from "any model given H wins on H-determined metrics."
- **Baseline conditioning asymmetry.** DiffTraj is natively a conditional model (the paper explicitly motivates TDDM in §1 by contrasting it with DiffTraj's "sample-specific conditioning"), but is included only in its unconditional form. As run, Table 1 demonstrates TDDM-with-H beats DiffTraj-without-H, which compounds the issue above. The paper does frame this as the "unconditional generation task," but TDDM is not in fact unconditional at test time; it just uses a different (aggregate) form of conditioning.

### Minor
- **No memorization audit despite the paper itself flagging memorization as a key risk.** §1 motivates TDDM by saying sample-specific conditioning "increases the risk of memorization," but the paper never measures nearest-neighbor distances from synthetic to training trajectories, or fidelity/authenticity-style precision-recall. Given that TDDM also conditions on data-derived statistics (H from X_target), this gap sits squarely on the paper's own framing.
- **"Zero-shot" is partially a terminological choice.** §4.3 calls the transfer setting zero-shot because "the model never receives individual target trajectories, only their aggregate spatial distribution" (§3 / line 224). That is honestly stated, but the experimental claim depends on having enough target data to estimate a 64×64 occupancy grid over each 3×3 km region; the paper does not characterize how performance varies with the amount of target data used to estimate H. The community-standard interpretation of "zero-shot" usually implies no target-domain data, so the framing leans optimistic. A sweep over target-data fraction would convert this from a binary claim into an honest calibration curve.
- **Porto-as-universal-source observation is uncontrolled.** §4.3 reports Porto's stronger transferability and frames it as "universal source dataset," but does not control for dataset size, sampling rate, geographic regularity, or coverage. The interpretation is plausible but speculative as presented.

### Trivial
- Algorithm 1 line 6 says "Normalize to [0,1]^D" and Algorithm 2 line 11 references the [0,1]^D frame, while §3 (lines 172, 174) defines the canonical frame as [−1,1]^D. A minor inconsistency the authors should reconcile.
- Algorithm 2 line 9 reads x_{t-1} = (1/√α_t)(x_t + ε_θ(x_t, H, t)) + σ_t z. The standard DDPM update subtracts a scaled noise prediction with coefficient (1−α_t)/√(1−ᾱ_t); the printed form drops the coefficient and uses the wrong sign. Likely a transcription slip but worth correcting since the algorithm is presented as the operational specification.

## Nice-to-Haves
- A *matched-conditioning* baseline: heatmap-conditioned Diffusion-TS or DiffTraj using the same H tokenization. This single experiment would convert the "spatial-prior trick wins on spatial-prior-determined metrics" reading into a real architectural claim either way (TDDM uses H best vs. all conditional diffusion models do similarly).
- A spatial-marginal-invariant metric — e.g., KL between conditional in-cell trajectory distributions averaged over cells. This isolates the question the paper actually wants to answer ("given where, how realistic is the motion?").
- A target-data sweep for the OOD setting: how much X_target is needed to estimate H well enough for transfer?
- Per-city results in the main text. The current main tables are dataset-averaged, which can mask cross-city heterogeneity (different sampling rates, geographies). Per-city tables are referenced in the appendix but the main-text averages alone obscure which dataset drives which result.

## Removed Points
These points are flagged to be removed; treat them with caution.

- *Harsh critic's "Section-by-Section notes about Eq. (5)/p(r_c)" framed as a structural issue.* The paper plainly states what is happening (Eq. 2 and Eq. 5), and the "spatial allocation pinned to empirical statistics" point is already covered by the major weakness on tautology. Kept as merged.
- *Harsh critic's complaint that the metric binning is not specified in the main text.* Borderline reproducibility nitpick — appendix is referenced for the six measures (§4 "See Appendix E for details on all six measures"); not a substantive flaw.
- *Strength Finder's "large-margin distributional improvement"* as written ("4× improvement … strongest evidence …"). The improvement is real but the headline framing conflicts with the major-tier weakness on tautology, so we down-weight it in the overall judgment rather than counting it as a clean strength.
- *Strength Finder's "causal evidence that spatial priors are the key mechanism."* The ablation does isolate the prior's contribution — but the same ablation is what supports the critique that nearly all distributional gain over Diffusion-TS comes from the prior. Kept implicitly via the ablation observation in Strengths, but not retained as standalone "causal evidence" since it cuts both ways.

## Novel Insights
None beyond the paper's own contributions. The factorization into "where" (spatial occupancy) and "how" (temporal dynamics) plus the per-region similarity-transform canonicalization are the genuinely novel observations, and both come from the paper itself.

## Suggestions
- Reframe the headline claim from "improved trajectory fidelity and coverage over leading baselines" to "spatial-prior conditioning yields improved coverage and proportionality over unconditional baselines," and present the matched-conditioning experiment as the operational test of whether the architectural contribution beyond conditioning is real.
- Add a memorization audit (nearest-neighbor distances between synthetic and train trajectories, compared to held-out real trajectories) to directly address the risk the introduction itself raises.
- Add a calibration curve over the amount of target data used to estimate H in §4.3 — this strengthens rather than weakens the OOD story by characterizing the operational regime.
- Move per-city tables (currently in Appendix Tables 7, 8, 12) into the main text or include a compact version; cross-dataset heterogeneity is part of the story.
- Fix the [-1,1] vs. [0,1] inconsistency between §3 and Algorithms 1–2, and the noise-prediction coefficient/sign in Algorithm 2 line 9.

## Evaluation Axes
- **Originality:** Moderate. Spatial-aggregate conditioning for trajectory diffusion plus per-region similarity-transform canonicalization is a genuinely fresh combination, but it builds incrementally on DiffTraj/ControlTraj/Diffusion-TS.
- **Importance of question:** Real and well-motivated — mobility data sharing and cross-region transfer are practically relevant problems.
- **Claims well supported:** Partially. The factorization and canonicalization claims are supported; the headline "improves fidelity and coverage over baselines" is partly an artifact of the H-conditioning given to TDDM and withheld from baselines.
- **Soundness of experiments:** Solid setup (three datasets, six metrics, map-matching ablation), but the central comparison lacks a matched-conditioning baseline, which weakens the empirical conclusion.
- **Clarity:** Above average. The architecture, algorithms, and benchmark are clearly described, with two small inconsistencies in the algorithms.
- **Value to community:** Real but limited by the framing. The benchmark and the canonicalization idea are reusable; the "we beat unconditional baselines on H-determined metrics" framing is less so.

## Anchors Considered

| Path | Avg | Round | Compared to paper |
|---|---|---|---|
| kKXIYUi8ff (DynamicsDiffusion) | 3.00 | R1 | Weak anchor; clearly below this paper in scope and execution. |
| 2orBSi7pvi (STDM) | 3.00 | R1 | Weak anchor; below this paper. |
| RDLvnUJ5JZ (TF-score) | 3.00 | R1 | Weak anchor; below this paper. |
| mHkbi3XM58 (Video score-based) | 3.25 | R1 | Below; different domain. |
| VRFotuGLfM (DiffMove) | 6.20 | R1/R2 | Same general space (conditional diffusion for trajectories), more careful execution; slightly above this paper. |
| dDdxbdhMsY (Deep Temporal Deaggregation) | 5.00 | R1/R2 | Essentially an earlier version of the same line of work; the current paper has added the metrics, ablation, and contribution-clarification the earlier reviewers asked for, but still has the new tautology concern. Slightly above 5.0. |
| 1o3fKLQPRA (DiffPath) | 4.50 | R1 | Below this paper — straightforward application with less ambitious scope. |
| 4anfpHj0wf (Point Set Diffusion) | 7.00 | R1 | Cleaner theoretical contribution, accepted; above this paper. |
| uKZdlihDDn (Diffusion Graph Networks) | 7.60 | R1 | Strong physics-domain anchor, clearly above. |
| EO8xpnW7aX (Discrete Diffusion Permutations) | 8.00 | R1 | Strong anchor, above. |
| RuP17cJtZo (Generator Matching) | 8.00 | R1 | Strong anchor, above. |
| fV0t65OBUu (Optimal Covariance Matching) | 8.00 | R1 | Strong anchor, above. |
| r125wFo0L3 (Large Trajectory Models) | 5.00 | R2 | Similar quality but different application (autonomous driving). |
| oHbmiaeyUL (Multidimensional Trajectory Opt.) | 5.50 | R2 | Different topic (flow/diffusion trajectory in latent space), similar borderline-reject tier. |
| RcANissyP4 (SelfEval) | 5.67 | R2 | Different topic, comparable borderline tier. |
| 7JfKCZQPxJ (STREAM) | 5.25 | R2 | Different topic, accepted borderline. |
| cC3LxGZasH (Beyond FVD) | 6.20 | R2 | Different topic but a benchmark/metric paper accepted around 6. |
| gqtbL7j2JW (GMI) | 5.00 | R2 | Different topic, borderline reject. |
| cbv0sBIZh9 (Multi-Task Diffusion) | 5.75 | R2 | Accepted, slightly above this paper. |
| PplM2kDrl3 (Domain Guidance) | 6.67 | R2 | Accepted with cleaner contribution, above. |
| qae04YACHs (TMDM) | 6.33 | R2 | Accepted, comparable tier above. |
| 4Ay23yeuz0 (Mixed-Type Tabular Diffusion) | 6.75 | R2 | Accepted, above. |

**Round-1 bracket:** between 4.5 and 6.5, with the strongest topical anchor (dDdxbdhMsY) at 5.0 representing essentially the same line of work.

**Round-2 narrowing:** The current paper is *better* than the dDdxbdhMsY (5.0) anchor — it has added the very metrics, ablations, and contribution statements those reviewers asked for. It is comparable to or slightly below DiffMove (6.2), which is a more clearly executed conditional trajectory diffusion paper without the tautology confound. The new major weakness (tautology of H-conditioning) is a real issue not present in DiffMove. r125wFo0L3 (5.0) and oHbmiaeyUL (5.5) are reasonable peers.

Final placement: slightly above the dDdxbdhMsY anchor due to the addressed concerns and added benchmark, but below DiffMove because of the unresolved confound on the headline claim. **5.0** with leans toward 5.5; settling at 5.0 because the tautology concern is structural and not minor.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
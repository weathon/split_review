## Summary
DIST is a plug-in inference-time correction for 3D molecular diffusion. The paper formalizes a "dense-concentrated (DC) structure" of molecular distributions, derives an overshoot condition from it, and proposes a pilot-rollout-based filter: at an intermediate timestep, candidates are duplicated and perturbed into batches, a pilot subset is rolled out to t=0 and scored, and batches whose score exceeds a threshold are discarded. Applied to EDM, GeoLDM, and RADM on QM9 and GEOM-Drugs, it improves stability/validity while reducing the average number of timesteps.

## Strengths
- Model-agnostic gains across three architecturally different backbones — GNN-equivariant EDM, latent-space GeoLDM, and Transformer non-equivariant RADM — on two datasets (Table 2): EDM Mol Sta 82.0→89.9, GeoLDM 89.4→93.4, RADM 87.3→91.4. Cross-architecture consistency supports that the failure mode is not architecture-specific.
- Definition 3.1 gives a concrete parameterization (σ*, Δ, K₀, peak centers) of the DC-structure and ties it via Eq. 6–7 to a scaling argument for why the reverse update can overshoot narrow peaks — sharper than the usual "molecules are discrete and hard" framing.
- Table 1's controlled experiment (start from z_t ∼ p(z_t|x), run t reverse steps) provides direct empirical evidence of monotonic degradation as the start timestep increases, grounding the error-accumulation narrative.
- Quality improvements come paired with average-timestep reductions (Table 3: ~410–640 vs 1000) rather than as a quality-for-compute tradeoff.

## Weaknesses

### Fatal
None.

### Major
- **Mismatch between motivating theory and actual mechanism.** Sec. 3.1 builds toward correcting the reverse update direction (overshoot derivation Eq. 6–7), but the algorithm in Sec. 3.2 is pilot-rollout-based accept/reject of batches by a terminal score s_j with no intermediate-step intervention. The "Steer" framing oversells what is mechanically rejection sampling, and the theory (Corollary 3.1, Prop. 3.1) does not actually prescribe τ, batch radius r, or pilot size. Readers expecting "score correction" will find filtering instead.
- **The pilot score s_j is left unspecified in the main text.** Sec. 3.2 only enumerates options ("round-trip residual, self-consistency, ensemble variance, or chemistry-based penalty") and defers commitment to Appendix F. The meaning of the gains depends on this choice: if s_j is essentially a validity/stability check, then improvements in the validity/stability columns of Table 2 are partly tautological with the selection criterion. The main paper should commit to and motivate a specific s_j.
- **No head-to-head against the natural baseline family.** DIST belongs to accept/reject + resampling (best-of-N + validity filter, SMC/twisted-diffusion-style particle filtering). Table 2 only contrasts backbone vs. backbone+DIST. Without a matched-NFE comparison against simple best-of-N or an SMC-style resampler in the main text, the gains cannot be cleanly attributed to the proposed mechanism rather than "spend more inference and keep the better completions."
- **Efficiency accounting is amortized in a way that obscures the work that selects samples.** The Sec. 4.3 formula (T−t)/|B| + t = 307 charges only the shared prefix amortized over batch size plus a final reverse pass; it does not transparently include pilot rollouts or rejected-batch work, even though Table 4 shows these dominate (30→100 pilot size moves measured timesteps 428→645). The "nearly half the timesteps" headline should be derived from total NFE per accepted molecule, ideally with wallclock.

### Minor
- **Theoretical results are weak relative to how they are presented.** Corollary 3.1 is the standard TV-contraction inequality for Markov kernels and does not use DC-structure. Proposition 3.1 only asserts existence of some bounding function f, with the explicit form deferred. As stated in the main text these are scaffolding, not guarantees that drive the algorithm.
- **Main-text ablations cover only pilot size (Table 4).** Threshold τ, intermediate t, and perturbation radius — which directly determine accept rate, bias, and the headline efficiency number — are deferred to Appendix H. At least one belongs in the main paper.
- **Batch construction is under-justified.** "Each candidate is duplicated and perturbed with a sufficiently small amount of noise to form batches" produces an engineered local cloud, not a draw from q_t. The role of within-batch variance as a proxy for π_j vs. π̂_j needs explanation.
- **Per-dataset/backbone timestep variability is undiscussed.** Table 3 shows e.g. GeoLDM+DIST 417 (QM9) vs 637 (GEOM-Drugs); EDM+DIST goes the other way (556 vs 503). The implied differences in acceptance rate are not analyzed.

### Trivial
- None retained.

## Nice-to-Haves
- A matched-NFE comparison in Table 2 against best-of-N with a validity filter and one SMC-style baseline.
- A quantitative link between σ*, Δ, β_t and the predicted improvement, turning the DC framing into a predictor of *when* DIST helps most.
- Wallclock per accepted molecule alongside timestep counts.
- Report the chosen s_j and a contrast between, e.g., self-consistency vs. chemistry-penalty s_j.

## Removed Points
*These points are flagged as removed; treat with caution.*
- "Improvements are modest and a simple resampler could match them." Speculative without the matched-NFE experiment; already covered by the "no head-to-head baseline" weakness.
- "Table 1 phenomenon would appear for any generative model." True but does not undermine the DC-specific argument; the magnitude in molecules is exactly the paper's point.
- "Overshoot derivation conflates analytic ∇log p_t with the trained reverse step." Partially valid, but Sec. 3.1 explicitly distinguishes ∇log p_t (overshoots) from ∇log q_t (further drift in low-density regions), so this is partly addressed.
- Strength: "DIST nearly halves inference cost" — partially conflicted with the Major efficiency-accounting weakness; the *measured* Table 3 numbers support a real reduction, but the framing in Sec. 4.3 is amortized.

## Novel Insights
None beyond the paper's own contributions. The DC-structure framing is the paper's own observation; the reviewer critiques concern fit between method, theory, and evidence rather than introducing new analytic insight.

## Suggestions
- Commit to a single s_j in the main text with justification; show one alternative as an ablation.
- Replace the (T−t)/|B| + t arithmetic with total NFE per accepted sample including pilot and rejected rollouts; add wallclock.
- Add a matched-compute comparison against best-of-N + validity filter and one SMC-style baseline in Table 2.
- Move at least one of {τ, intermediate t, perturbation radius} ablations from Appendix H into the main text.
- Either tighten Proposition 3.1 with an explicit f in the main text, or present these results as scaffolding rather than as a guarantee.

## Calibration

Round 1 anchors:
- `kKXIYUi8ff.md` (3.00, R1, weak): DynamicsDiffusion — much weaker, no theory/empirical sharpness.
- `m9zWBn1Y2j.md` (3.00, R1, weak): PsiDiff — weaker contribution.
- `f7Zq9CqQEM.md` (3.40, R1, weak): Path-Tracing Distillation — related framing, less polished.
- `G536mmC2HL.md` (3.00, R1, weak): TorSeq — weaker.
- `rwmWd2rjP1.md` (4.75, R1, mid): MoreRed — reverse-diffusion for molecules, comparable scope.
- `kzGuiRXZrQ.md` (5.75, R1, mid): EQGAT-diff — strong empirical design-space study, more thorough than DIST.
- `5YLsnsjgeC.md` (6.00, R1, mid): VFDiff — energy-guided diffusion.
- `jZPqf2G9Sw.md` (5.50, R1, mid): Dynamics-informed protein diffusion.
- `NSVtmmzeRB.md` (8.00, R1, strong): GeoBFN — clearly stronger.
- `uKZdlihDDn.md` (7.60, R1, strong): Diffusion Graph Nets for fluid.
- `zMPHKOmQNb.md` (8.00, R1, strong): Walk-Jump Sampling — stronger theory and empirics.
- `kJFIH23hXb.md` (8.00, R1, strong): SE(3)-Stochastic Flow Matching.

Round-1 bracket: 4.5–6.

Round 2 anchors:
- `vFVjJsy3PG.md` (5.40, R2): GeoRCG — plug-in-style molecular framework with mixed reviews; similar profile to DIST (real gains, methodological concerns), reject. DIST is comparable.
- `qH9nrMNTIW.md` (6.25, R2): IPDiff — interaction-prior diffusion, accepted; somewhat cleaner contribution than DIST.
- `eZLckrDOom.md` (6.00, R2): Importance-Corrected Neural JKO — rejection/resampling-based sampler with theory, rejected.
- `vxBvr5ZpIu.md` (5.50, R2): Diffusion-PINN Sampler.
- `BoMvv7ypDF.md` (5.80, R2): Recursive Score Estimation, reject.

DIST sits close to GeoRCG (5.40) and a little below EQGAT-diff (5.75) — real cross-architecture empirical gains, but with substantive methodological framing problems (theory-method gap, underspecified s_j, no head-to-head baselines, amortized efficiency accounting). I place it at 5.0.

MY FINAL SCORE: <score>5</score>
MY FINAL DECISION: <decision>Reject</decision>
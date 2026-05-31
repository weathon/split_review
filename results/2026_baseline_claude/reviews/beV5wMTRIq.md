## Summary

The paper introduces PA-TFNP (Physics-Aware Tensor Field Neural PDE), a climate and weather forecasting framework that extends the ClimODE neural-ODE paradigm with three claimed innovations: (1) a Tensor Field Network (TFN) operator for rotation-equivariant processing on spherical domains, (2) a spherical-transform-based gradient with latitude-corrected finite differences and physically grounded polar boundary conditions (Neumann and average padding), and (3) physics-informed diffusion terms from the atmospheric primitive equations augmented by a time-blended neural–physical velocity operator. The model is evaluated against ClimODE, ClimaX, and a vanilla NODE on ERA5 data across global (short- and long-term) and regional (Australia, South America) settings, demonstrating large improvements on global forecasting.

---

## Strengths

- **Physically motivated spherical gradient correction.** The lat/lon finite-difference correction (Eq. 3, dividing longitudinal differences by R·cos(φ)·π/180) is correct and non-trivial; it properly accounts for meridian convergence near the poles. This is a well-justified, easily reproducible improvement over ClimODE's flat-grid finite differences.

- **Boundary condition treatment.** The paper diagnoses a real and visible deficiency in ClimODE—polar artifacts—and proposes two concrete remedies (Neumann replication and average padding). Figure 2 provides visual evidence that these strategies reduce polar artifacts, and the choice of Neumann conditions at the poles is physically sensible (zero-flux BC).

- **Diffusion augmentation with learnable spatially varying coefficient.** Introducing a position-dependent learnable diffusion coefficient α(x) to mimic subgrid turbulence is a pragmatic and interpretable inductive bias. Figure 4 shows it stabilises long-horizon (up to 138 h) forecasts relative to the TFNP-only baseline.

- **Large and consistent global-forecasting gains.** Figures 3 and Table 2 show that PA-TFNP substantially outperforms ClimODE and ClimaX on global settings at both 5.625° and 11.25° resolutions, across all five ERA5 variables and over multi-month lead times. The margin (38–79% RMSE reduction) is large enough to be robust to moderate measurement uncertainty.

---

## Weaknesses

### Fatal
*None of the fatal severity.*

### Major

1. **The core equivariance claim is not justified by the presented formulation.** The paper's defining innovation is rotation equivariance via a Tensor Field Network (TFN), citing Thomas et al. (2018) and Kondor et al. (2018). Standard TFNs achieve SE(3) equivariance by decomposing features into irreducible representations of SO(3) (spherical harmonics) and using Clebsch–Gordan products to mix them. The formula actually presented (Section 3.2, unnumbered equation) is:

   f_TFN(I[i, c_out]) = Σ_{c1,c2} W[c_out, c1, c2] (I[i, c1] · I[i, c2])

   This is a **point-wise, channel-wise bilinear/quadratic mixing** that operates independently at each spatial point i. There is no spatial aggregation between points, no decomposition into spherical-harmonic irreps, and no Clebsch–Gordan coefficients. This formula does not, in any obvious or rigorous way, yield rotation equivariance on the sphere. The equivariance argument in Figure 1 is a hand-wavy illustration (showing that regions A, B, C, D "transform consistently") but does not constitute a proof. If the actual implementation uses proper irreps and CG products but the formula is an oversimplification, that gap must be bridged in the paper; as written, the central theoretical claim is unsupported by the mathematics presented.

2. **Narrow comparison baseline limits the "state-of-the-art" claim.** The abstract prominently claims "state-of-the-art performance," yet comparisons are limited to ClimODE, ClimaX, and a basic NODE—all within the ClimODE family or at similar model scale. Models like FourCastNet, Pangu-Weather, and GraphCast are cited in the related work and have well-known ERA5 benchmark results but are not compared against. On the WeatherBench benchmark at the reported resolutions, even the 78.92% improvement over ClimODE does not guarantee state-of-the-art status in the broader field. The claim should be scoped or the missing baselines included.

3. **Inconsistent regional results undermine generality.** Table 1 shows that for t2m, u10, and v10 at short lead times (6–12 h), PA-TFNP performs **worse** than ClimODE in both regions. For example, t2m at 6 h in Australia: ClimODE 0.80 vs PA-TFNP 2.42. The paper acknowledges this only briefly ("a trade-off between local variance sensitivity and longer-horizon stability"), but offers no mechanism or analysis. If physics-awareness and equivariance are the key drivers of performance, why do they hurt short-horizon near-surface predictions? This inconsistency is not a minor edge case—it spans multiple variables and both test regions.

### Minor

4. **No per-component ablation.** The ablation only contrasts TFNP (no physics) vs PA-TFNP (all physics). The three physics components—(a) boundary conditions + spherical gradient, (b) additional physics features, and (c) diffusion + velocity blending—are never ablated individually. It is therefore impossible to determine how much of the gain comes from the straightforward spherical gradient fix versus the claimed equivariant TFN.

5. **Physical operator f_phys lacks Coriolis force.** The momentum physics term f_phys = −∇Φ + ν∆u_i − γu_i is claimed to derive from the atmospheric primitive equations, but the Coriolis acceleration (2Ω × u), which is fundamental to large-scale atmospheric dynamics (geostrophic balance, jet streams), is absent. This weakens the "physically grounded" claim for the velocity update.

6. **τ₀ in the time-blending scheme is not described.** The blending factor β_t = 1 − exp(−t/τ₀) is introduced but the value or selection criterion for τ₀ is not reported anywhere in the main text or visible appendix. Since this controls how quickly the model shifts from neural to physical tendencies, it is a key hyperparameter.

7. **Monthly forecasting Table 2: mixed u10/v10 results.** At the 2-month horizon, ClimaX outperforms PA-TFNP on u10 (1.92 vs 2.32) and v10 (1.71 vs 1.91). This contradicts the global claim of consistent superiority.

### Trivial

- The conclusion mentions "divergence-free conditions" as one of the contributions, but this is not mentioned or implemented in the methodology.
- The figure descriptions repeat three times (OCR artifact)—not a paper flaw.

---

## Nice-to-Haves

- A formal equivariance proof or a reference to the exact equivariant layer implementation (e.g., e3nn or related library) would solidify the main claim.
- Including WeatherBench leaderboard numbers for at least one of the much-larger models (e.g., Pangu-Weather at 5.625°) would help calibrate the scale of improvement.
- A per-variable ablation revealing which physics features drive gains for which predictands would be very informative for practitioners.

---

## Novel Insights

The identification that polar boundary artifacts in ClimODE arise from the absence of proper physical boundary conditions on the latitude dimension—and that Neumann/average padding can be used as a drop-in fix—is practically useful and transferable to any latitude-longitude neural PDE solver. Similarly, the latitude-scaled gradient correction is simple but often overlooked in data-driven models trained on lat/lon grids. These two contributions are likely the primary performance drivers and would benefit any model in this family. However, the paper's claimed theoretical contribution (rotation equivariance via TFN on the sphere) is not convincingly established, and the physics diffusion augmentation, while reasonable, is incremental relative to existing physics-informed neural PDE literature.

---

## Suggestions

- **Prove or restate the equivariance property**: Either provide a formal proof that the point-wise bilinear form (Eq. in Sec. 3.2) achieves rotation equivariance, or clarify what type of equivariance is being claimed (e.g., permutation equivariance among channels, which the formula does satisfy, is not the same as SO(3)/SE(3) equivariance on the sphere). If the implementation uses proper CG-based equivariant layers, this should be explicitly stated.
- **Add at least one widely used public baseline** (e.g., FourCastNet or Pangu-Weather numbers from WeatherBench) at the corresponding resolution to calibrate the absolute quality of predictions.
- **Ablate boundary conditions and spherical gradient independently** from the TFN and physics terms to quantify each component's contribution.
- **Explain or fix the t2m regression** in regional short-horizon forecasting—e.g., is this a training objective mismatch or a failure mode of the diffusion term?

---

## Score and Decision

The paper addresses a real problem (physics-aware spherical forecasting) and delivers genuine experimental gains on global benchmarks, particularly through the spherical gradient correction and boundary condition improvements. However, the central theoretical claim—rotation equivariance via TFN—is not rigorously supported by the mathematics as presented, the comparison set is too narrow to support a "state-of-the-art" claim, results are inconsistent in regional settings, and the ablation is insufficient to isolate causes of improvement. These are substantive issues that would require non-trivial revision to resolve.

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>
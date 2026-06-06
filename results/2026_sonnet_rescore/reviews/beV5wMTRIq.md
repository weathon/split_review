---

## Summary

PA-TFNP extends the ClimODE neural ODE framework for weather forecasting with three additions: (1) a bilinear tensor-product operator the paper calls a "Tensor Field Network" (TFN), (2) physically consistent boundary conditions (Neumann/average padding) and a spherical gradient correction with latitude-dependent cosine scaling, and (3) a hybrid neural-physical PDE blending neural tendencies with a physics-derived momentum operator that includes pressure-gradient, viscous diffusion, and drag terms. The paper demonstrates improvements over ClimODE on global and, more mixed results on, regional and monthly forecasting tasks.

---

## Strengths

1. **Boundary condition treatment directly reduces artifacts.** Figure 2c provides clear error-map evidence that TFNP's Neumann and average padding strategies substantially reduce the polar and boundary artifacts present in ClimODE. This is a concretely demonstrated and practically useful contribution, addressing a known deficiency of the ClimODE baseline.

2. **Curvature-aware spherical gradient (Eq. 3).** The latitude-dependent cosine correction `R·h·π·cos(φ)/180` in the longitudinal finite difference is correctly derived for the sphere and improves numerical accuracy of spatial derivatives across all latitudes. This is a rigorous and clearly specified numerical improvement over naive lat-lon differencing.

3. **Physics-informed diffusion improves long-term stability.** Figure 4 shows that PA-TFNP maintains substantially lower RMSE than TFNP across all five variables over 138-hour extended forecasts, providing direct empirical evidence that the physics-blending term (Eq. 4–6) enhances long-range stability.

4. **Physics-derived input features are physically motivated.** The additional features introduced in Section 3.3—near-surface wind magnitude, low-tropospheric lapse rate, and relative vorticity—are all standard dynamical and thermodynamic quantities with clear atmospheric relevance.

---

## Weaknesses

### Fatal
None verified.

### Major

- **The "Tensor Field Network" is misrepresented; the equivariance claim is unsupported.** Eq. in Section 3.2 defines: `f_TFN(I[i, c_out]) = Σ_{c1,c2} W[c_out,c1,c2](I[i,c1]·I[i,c2])`. This is a pointwise bilinear channel-mixing operation—there is no spatial aggregation, no message-passing, no spherical harmonic basis, and no Clebsch–Gordan decomposition. The Thomas et al. (2018), Weiler et al. (2018), and Kondor et al. (2018) literature cited for TFNs defines SE(3)/O(3)-equivariant networks on 3D point clouds with these structures. Calling this operator a "Tensor Field Network" invokes formal theoretical guarantees that the mathematical definition does not provide. Furthermore, equivariance is argued only via the qualitative diagram of Figure 1 (regions A, B, C, D under rotation); no formal proof or empirical equivariance test (rotating input → running inference → rotating output → comparing) is provided. The ablation in Section 4.4 shows better polar/equatorial accuracy, but this confounds boundary conditions, gradient correction, and the bilinear operator simultaneously—making it impossible to attribute the gain to any equivariant structure. This is a meaningful overclaim at the center of the paper's identity.

- **"State-of-the-art" claim is not supported by the comparisons.** The abstract states PA-TFNP "achieves state-of-the-art performance in global and regional weather prediction." The paper's own related works section cites GraphCast (Lam et al., 2023), Pangu-Weather (Bi et al., 2023), FourCastNet (Pathak et al., 2022), Aurora (Bodnar et al., 2024), and NeuralGCM (Kochkov et al., 2024). None appear in any results table; all comparisons are against ClimODE, ClimaX, and NODE. A claim of "state-of-the-art" is not defensible without demonstrating performance relative to these systems, especially given that the ERA5/WeatherBench benchmark used here is accessible to all of them.

- **Substantial, unexplained failure on t2m in regional settings.** Table 1 shows PA-TFNP achieves RMSE of 2.42±0.70 (Australia, 6h) and 2.98±1.50 (Australia, 12h) on t2m, versus ClimODE's 0.80±0.13 and 1.10±0.22—roughly 3× worse. South America shows similar degradation. PA-TFNP also underperforms ClimODE on u10 and v10 at 6h for both regions. The paper's sole response is one sentence: "This may indicate a trade-off between local variance sensitivity and longer-horizon stability." No analysis of which component (diffusion, boundary padding, or the bilinear operator) causes the regression is offered. For a surface diagnostic variable that is practically critical and has strong diurnal forcing, a 3× degradation at short horizons constitutes a meaningful failure that undermines claims of "strong predictive accuracy overall" (Section 4.2).

### Minor

- **"Consistently outperforming" in Table 2 is factually inaccurate.** Section 4.3 states "PA-TFNP consistently outperforms other benchmarks." Table 2 shows TFNP outperforms PA-TFNP on z at month 2 (527.07 vs 562.39), and ClimaX outperforms both TFNP and PA-TFNP on u10 at both months (1.80 and 1.92 vs. 1.83–2.40). The inconsistency is not acknowledged.

- **The physical operator (Eq. 5/6) omits the Coriolis force.** `f_phys = -∇Φ + ν∆u_i − γu_i` includes geopotential pressure gradient, viscous diffusion, and linear drag, but not the Coriolis term (`−f_c ẑ × u`, with f_c the Coriolis parameter). For planetary-scale dynamics this term governs geostrophic balance and is the defining characteristic of large-scale mid-latitude flow. The paper claims this operator is "derived from the atmospheric primitive equations"; the primitive equations explicitly include Coriolis. Omitting it while claiming primitive-equation provenance is physically misleading, even if the learnable neural component can partially compensate.

- **Ablation does not decompose individual PA-TFNP components.** Section 4.4 compares TFNP vs. PA-TFNP (which bundles boundary conditions + spherical gradient + physics features + modified PDE). Since the t2m failure and some regional wind regressions appear in PA-TFNP but not the table for TFNP, it is unclear which component is responsible. A four-way ablation would identify the culprit.

### Trivial

- The 78.92% and 38.12% improvement figures in Figure 3's caption lack an explicit computation formula (e.g., mean % RMSE reduction across variables). Given the high variance across z, t, t2m, u10, v10, these aggregates can be dominated by the best-performing variable and should be accompanied by per-variable numbers.

---

## Nice-to-Haves

- A formal or empirical equivariance test (pass a rotated input through the model, rotate the output, compare to unrotated inference on the rotated input) would either validate or clarify the equivariance claim and help reposition the operator correctly.
- Comparison with a climatological mean baseline as a sanity check to confirm that all improvements are non-trivial relative to the simplest forecasting approach.
- Reporting channel dimensions and parameter counts in a table (the paper asserts "comparable parameters" to ClimODE; the bilinear operator has O(C_in² · C_out) parameters and this should be verified numerically).
- A variable-specific ablation of the diffusion term, as the paper itself acknowledges in Section 5 that different variables warrant different equation forms.

---

## Removed Points

*These points are flagged for removal; treat with caution.*

- **Harsh Critic: Complexity / reproducibility of channel dimensions and initialization schedule.** The critic notes that τ₀ and learnable coefficients ν, γ, α are undescribed in the main text. Per filtering rules, reproduction nitpicks about hyperparameters deferred to appendix are removed, as the appendix exists in the original submission.
- **Harsh Critic: Missing Climatology baseline.** While a useful sanity check, the Climatology baseline is not standard in the subset of the community that evaluates extensions of ClimODE on WeatherBench. Moved to Nice-to-Haves.
- **Strength Finder: "Consistently shows improvements over strong baselines."** The claim of consistency is contradicted by Table 1 and Table 2 failures; this generic strength is removed.
- **Strength Finder: "Comprehensive evaluation across diverse forecasting settings."** While technically true in scope, the mixed performance within those settings means the evaluation does not uniformly support the stated contributions. Removed as superficially positive framing.
- **Harsh Critic: Comparison with GraphCast/Pangu as "unfair staged baseline."** The reverse asymmetry rule would normally apply if the asymmetry favored the baseline. Here PA-TFNP does claim state-of-the-art, so the absence of these comparisons is retained as a Major weakness. But the individual unfair-comparison framing of this specific rule is inapplicable; the weakness is retained on the overclaiming grounds already stated under Major.

---

## Novel Insights

The most genuinely novel observation across both reviews is the disentanglement problem in the ablation: the bilinear tensor-product operator, the boundary padding, and the spherical gradient correction are never separately evaluated, yet the t2m regional failure and some wind variable regressions suggest that one or more of the PA-TFNP components causes over-smoothing of diurnally-driven surface fields. This creates a plausible hypothesis—the spatially varying diffusion term (Eq. 4) with a single learnable α may over-regularize variables with strong local forcing—that would directly connect the operator design to the failure mode. If confirmed by ablation, it would simultaneously explain the t2m regression and motivate the paper's own Section 5 recommendation for variable-specific equation modifications.

---

## Suggestions

1. **Rename/reframe the operator.** Replace "Tensor Field Network" with a name that accurately describes what the operator is (e.g., "bilinear tensor-product channel mixer" or "second-order feature interaction layer"). Remove claims of formal equivariance unless an equivariance test is passed. Reframe the paper's equivariance argument around the combined boundary-condition + gradient-correction structure, which has clearer geometric motivation.
2. **Diagnose and characterize the t2m failure.** Run the component ablation to identify which modification degrades t2m. If the spatially varying diffusion (α) is responsible, show this, cap the diffusion coefficient for surface diagnostics, or make α variable-specific as already suggested in Section 5.
3. **Qualify the "state-of-the-art" claim.** Replace with "substantially outperforms ClimODE, ClimaX, and NODE" or provide honest caveats about the scope of comparison.
4. **Fix the "consistently outperforming" statement in Section 4.3** to reflect the actual Table 2 results, noting where TFNP or ClimaX outperform PA-TFNP.

---

## Score and Decision

**Originality:** The paper recombines existing ideas (bilinear feature interaction, boundary padding, spherical finite differences, physics blending) in a new configuration. The combination is original in context, but no single component is novel in isolation, and the TFN framing is mislabeled.

**Importance of research question:** Weather forecasting with physical consistency is an important and active area.

**Claims supported:** Partially. Long-term stability improvement is well-supported. Global forecast gains over ClimODE are demonstrated but not against broader state-of-the-art. Regional results are mixed. "State-of-the-art" and "consistently outperforming" claims are not fully supported.

**Soundness of experiments:** The experiments follow ClimODE's protocol, but the ablation is insufficient to attribute contributions, the t2m failure is unexplained, and Table 2 inconsistencies go unacknowledged.

**Clarity of writing:** The methodology is mostly clear, though the TFN operator naming creates confusion by invoking a well-defined literature for a different construct.

**Value to research community:** Moderate. The boundary condition and spherical gradient corrections are practically useful improvements for lat-lon grid forecasting. The long-term stability gain is a genuine contribution.

The paper has real but overstated contributions. The TFN misrepresentation and overclaimed equivariance are the most significant single issues, accompanied by an unexplained t2m degradation and an unsupported "state-of-the-art" claim. These together warrant rejection in the current form, though the core engineering contributions (boundary conditions, spherical gradients, physics blending) are genuine and salvageable with honest reframing.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>2</originality>
<importance>4</importance>
<claims_supported>2</claims_supported>
<soundness>2</soundness>
<clarity>3</clarity>
<community_value>3</community_value>
</subscores>
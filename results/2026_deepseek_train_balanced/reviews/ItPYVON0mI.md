## Summary

This paper proposes a coarse-grained (CG) modeling framework that combines a graph neural network (GNN) potential with a Lennard-Jones term (parameterized via relative entropy minimization) and a novel high-frequency sinusoidal potential \(U_{HF} = A\sin(\omega r)/r^2\). The key claim is that the HF term is "orthogonal" to the radial distribution function (RDF) — meaning it can tune dynamics (MSD) without perturbing the equilibrium structure — and that its amplitude can be optimized via simple bisection due to monotonic control over diffusion. The method is demonstrated on SPC/E water, argon, and methane, all as single-site CG models.

## Strengths

- **Principled approach to the structure-dynamics trade-off in CG modeling**: The paper identifies a real and well-known problem — CG models that reproduce equilibrium structure typically exhibit artificially fast dynamics due to smoothing of the energy landscape. Adding a potential term designed to be "invisible" to static pair structure while modulating dynamics is a creative departure from the non-Markovian (Mori-Zwanzig/GLE) route, which introduces memory kernels that are hard to compute.

- **Analytical basis for RDF-dynamics decoupling**: The paper derives closed-form expressions for the gradients of the relative entropy with respect to the HF parameters (\(\partial S_{rel}/\partial A\) and \(\partial S_{rel}/\partial\omega\), Eqs. 12–13) and shows these gradients approach zero for sufficiently large \(\omega\). This provides a formal starting point for why a sinusoidal potential with appropriately high frequency could modify dynamics without perturbing the equilibrium pair structure — a non-trivial insight.

- **Monotonic control of diffusion enabling gradient-free optimization**: Figure 4B and the accompanying discussion demonstrate that the mean-squared displacement decreases monotonically with the amplitude \(A\) of \(U_{HF}\). This monotonicity allows the bisection method to be used for amplitude optimization, avoiding expensive gradient computations through MD trajectories. This is a practical advantage over methods that require differentiable simulation rollouts for dynamics tuning.

## Weaknesses

### Fatal
None.

### Major

- **No baselines or ablation study — the central claim is unverifiable from the presented evidence**: The paper shows RDF and MSD plots (Figure 5) comparing CG simulations against all-atom references. There are zero comparisons against standard CG methods (IBI, force matching, relative entropy minimization, DeePCG, or even a simple LJ-only CG model). There is also no ablation: the reader cannot determine whether the GNN alone, the GNN+LJ combination, or the full GNN+LJ+HF model produces the reported results. The core claim — that the HF term is responsible for recovering dynamics without perturbing structure — cannot be assessed without showing what the CG model does *without* the HF term. A single additional curve showing "GNN+LJ without HF" on the same MSD plot would be the single most informative experiment the paper could add.

- **No quantitative metrics reported — results are visually inspected only**: Figure 5 shows overlapping RDF and MSD curves, but no numerical errors are given. There is no RDF RMSD, no diffusion coefficient comparison, no percentage errors, and no statistical uncertainty estimates (no error bars, no variance across independent runs). The trajectory lengths (100 ps for RDF, 10 ps for MSD) are very short for diffusion calculations in water at 300 K (molecules diffuse only ~5 Å in 10 ps, likely reflecting the ballistic-to-diffusive crossover regime rather than steady-state diffusion), and no justification is offered. Without any quantitative assessment, the reader cannot judge whether the agreement is genuinely good or merely plausible at the plotted scale. For a top-venue paper that proposes a new method, this level of evaluation is insufficient.

- **Insufficient rigor in the orthogonality argument linking KL divergence to RDF invariance**: The paper claims that the HF potential is "orthogonal to RDF space" because \(\partial S_{rel}/\partial A \to 0\) for large \(\omega\) (Eq. 12). However, \(S_{rel}\) is the relative entropy (KL divergence) between the *full configurational distributions* of the CG and AA ensembles. A zero gradient of \(S_{rel}\) with respect to \(A\) indicates a stationary point in the full configurational KL divergence, which does not *directly* guarantee invariance of the RDF specifically — RDF is a pairwise statistic, and higher-order correlations could change in ways that preserve the overall KL divergence. The derivation from Eq. (9) to Eqs. (12)–(13) is presented without intermediate steps, the integral leading to \(\partial S_{rel}/\partial A = 2\pi\rho N_{atom}\sin(\omega r_c)/\omega\) is asserted rather than derived, and the assumption of uniform density (\(\rho\)) is not discussed. The claim that this justifies \(\omega = 100\,\text{Å}^{-1}\) as "optimal" is not clearly established. This gap between the analytical argument and the claimed conclusion needs to be tightened for the paper's theoretical foundation to be convincing.

### Minor

- **Numerical stability of the high-frequency potential under standard MD is unaddressed**: With \(\omega = 100\,\text{Å}^{-1}\), the HF potential \(U_{HF} = A\sin(\omega r)/r^2\) has a spatial period of \(2\pi/100 \approx 0.063\,\text{Å}\). Combined with a 1 fs timestep and Nosé-Hoover thermostat, the paper provides no analysis of energy conservation, numerical integration accuracy, or whether the thermostat correctly samples the canonical ensemble under such a rapidly varying potential. This does not invalidate the approach, but addressing it (e.g., showing energy drift, testing with smaller timesteps) would significantly strengthen confidence in the reported results.

- **Demonstrated systems are too simple to support the paper's ambitious scope claims**: All three test systems are single-site CG models of simple liquids (argon, methane) or a single-site water model. The abstract and title claim applicability to "complex systems" with "electrostatic and multi-body effects," yet no system with chain connectivity, conformational degrees of freedom, bond-angle potentials, or heterogeneous interactions is tested. The CG representation of SPC/E water has no explicit charges — electrostatic effects are handled implicitly. This gap between the claimed scope and the demonstrated capability weakens the paper's significance claim.

- **Insufficient methodological details for reproducibility**: Key implementation details are missing: (1) the LJ functional form and resulting parameters from relative entropy minimization are not specified; (2) the Neural ODE training — a central component — is mentioned only briefly, with no information on training cost, trajectory rollout length, adjoint tolerance, or convergence criteria; (3) the derivation from Eq. (9) to (12)–(13) omits intermediate steps, making it difficult to verify the analytical claims. These omissions are addressable but limit the paper's usefulness as a reference.

- **MSD alone is insufficient to characterize dynamics**: The paper evaluates dynamical accuracy solely through the mean-squared displacement, which measures the second moment of the displacement distribution. Correct MSD does not guarantee correct velocity autocorrelation, dynamical structure factor, or transition rates between metastable states. While MSD is a standard first check, the paper would benefit from acknowledging this limitation.

### Trivial

- The code link (sites.google.com/...) is unconventional; a permanent repository (GitHub, Zenodo) would be preferable for long-term accessibility.

## Nice-to-Haves

- An ablation study comparing GNN+LJ vs. GNN+LJ+HF on both RDF and MSD would directly validate the paper's central claim.
- Comparison against at least one standard CG baseline (IBI or force matching) would help calibrate the method's performance against existing approaches.
- Testing on a system with conformational degrees of freedom (e.g., short alkane or polymer melt) would substantially strengthen the claim of general applicability.

## Removed Points

These points from the reviews were filtered out after cross-checking against the paper:

- *Harsh critic: "force fluctuation is not reflected" is imprecise* — REMOVED: The paper correctly distinguishes mean forces from force fluctuations; force-matching CG reproduces mean forces, not fluctuations, so the paper's statement is accurate.
- *Harsh critic: "sub-femtometer" description of HF potential oscillation* — REMOVED: The period is ~0.063 Å = 6.3 pm, three orders of magnitude larger than "sub-femtometer." The underlying concern about numerical stability is retained but downgraded to Minor.
- *Harsh critic: "no data availability statement"* — REMOVED: The paper explicitly provides a code link at line 34.
- *Strength Finder: SPC/E water "goes well beyond simple Lennard-Jones fluids"* — REMOVED: The CG representation is a single-site model with no explicit charges. While SPC/E is a reasonable benchmark, the claim was inflated relative to what was demonstrated.
- *Strength Finder: "memory-efficient end-to-end optimization via Neural ODE"* — REMOVED: This is a standard technique adopted from prior work (Chen et al. 2018; Wang et al. 2020, 2023a), and the paper provides no measurements demonstrating this advantage over alternatives.
- *Harsh critic: discrepancy between ω=150 Å⁻¹ (Figure 4 caption) and ω=100 Å⁻¹ (text)* — REMOVED: The figure uses 150 as an example threshold; the text states ~50 Å⁻¹ as the invariance threshold and 100 as a safe choice. These are internally consistent.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add an ablation experiment**: Run the same CG model *without* the HF term (GNN+LJ only) and overlay the resulting RDF and MSD on Figure 5. This single experiment would provide the strongest direct evidence for whether the HF term works as claimed.
2. **Report quantitative metrics**: Provide RDF RMSD, diffusion coefficients (with error estimates from multiple independent runs), and percent errors with uncertainty quantification.
3. **Provide the intermediate derivation steps** from Eq. (9) to Eqs. (12)–(13), including the uniform density assumption and the integration details.
4. **Show energy conservation** (total energy drift over time) during production runs with the HF potential to demonstrate numerical stability.
5. **Acknowledge limitations explicitly**: Discuss the scope of the orthogonality claim (KL divergence vs. RDF), the systems tested vs. claimed generality, and the sufficiency of MSD as a dynamical metric.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
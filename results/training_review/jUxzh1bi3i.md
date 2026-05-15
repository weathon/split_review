Now I have all the evidence I need. Let me produce the final consolidated review.

## Summary
This paper introduces GlobalTomo, the first comprehensive 3D global synthetic seismic dataset designed for ML-based full-waveform inversion (FWI). The dataset features three tiers of increasing realism — Acoustic (1 km fluid sphere, 20 Hz), Elastic (1 km solid sphere, 20 Hz), and Real Earth (6371 km, 30 s period) — with velocity structures parameterized via spherical harmonics up to degree 8. The paper establishes ML baselines (MLP, DeepONet, H-Fourier, PIDO) for forward modeling and demonstrates three inversion strategies (gradient-based optimization, multi-start sampling, direct mapping) on the smaller tiers, reporting ~60,000× speedups over numerical simulation.

## Strengths
- **First dedicated synthetic dataset for global-scale ML-FWI.** The paper explicitly addresses a critical gap: existing ML-FWI datasets (e.g., OpenFWI) target subsurface exploration, while GlobalTomo targets planetary-scale tomography. The three-tiered design isolates physical complexity (acoustic → elastic → real Earth) in a principled way.
- **Physically grounded parameterization via spherical harmonics up to degree 8.** This captures long-wavelength mantle heterogeneity with a compact parameter set, keeping the inverse problem well-posed. The choice is justified by spectral analyses from tomographic literature showing dominant power at low degrees.
- **~60,000× forward modeling speedup demonstrated quantitatively.** Section 3.1.3 reports 120 seconds on 24 CPU cores for numerical simulation versus 1–3 ms on a single GPU for ML models, with direct visualization in Figure 3b. This acceleration is the paper's strongest evidence for the potential of ML in FWI.
- **Multiple ML-based inversion strategies with quantitative validation on the Acoustic tier.** Gradient-based optimization improves correlation over 200 L-BFGS iterations (Figure 5), multi-start sampling systematically improves results (Figure 6), and direct inversion mapping achieves R=0.826 on unseen test data. These demonstrate workflow feasibility.

## Weaknesses

### Major
- **The Real Earth tier — the only tier operating at true global scale (6371 km, 30 s period) — is used in zero experiments.** All quantitative evaluations (forward modeling in Table 2, all three inversion strategies in Section 3.2) are on the Acoustic and Elastic tiers (1 km radius, 20 Hz). The paper's central claim — that "ML approaches are particularly suitable for *global* FWI" — hinges on demonstrating planetary-scale applicability, yet no evidence at that scale is provided. While the smaller tiers serve as useful proxies, the abstract and title frame the contribution as global, and the gap between a 1 km sphere and the full Earth is substantial. This is the single most significant weakness.
- **No comparison to traditional adjoint-based FWI on the same test problems.** The inversion experiments (Section 3.2) show that ML-guided optimization improves correlation with iterations and starting points, but never benchmark against a conventional FWI solver on the same inversion task. Without this comparison, the reader cannot assess whether the ML inversion results are competitive in quality or merely fast-but-inaccurate. The claim that ML "overcomes limitations" of traditional FWI requires a baseline to establish what is being overcome.

### Minor
- **PIDO (physics-informed DeepONet) is evaluated only qualitatively for temporal generalization.** Section 3.1 and Figure 3c show that physics constraints help predict intermediate timesteps, but no quantitative RL2/R metrics are reported for PIDO, unlike the other baselines in Table 2. This makes the claim of improved generalization hard to assess.
- **The 20 wavefield snapshots over 6000 s (300 s spacing) in the Real Earth tier are very sparse for body-wave characterization.** Body waves travel ~3000 km in 300 s, so these snapshots would miss most body-wave propagation details. The paper should clarify that the 6000-timestep seismogram data (not the wavefield snapshots) is the primary data for inversion, or justify the 20-snapshot design choice.

### Trivial
- None that survive filtering.

## Nice-to-Haves
- **Compare to a traditional adjoint-based FWI on the Acoustic tier.** This single experiment would substantially strengthen the claim that ML-FWI is competitive.
- **Report PIDO quantitatively** (even as a short row or footnote in Table 2) and clarify what metrics apply.
- **Include at least one qualitative demonstration on the Real Earth tier** (e.g., a seismogram comparison or a forward-modeling prediction for one test structure) to validate dataset usability at global scale.
- A data-availability statement in the paper would aid reproducibility (this may exist in the appendix, which was stripped by the parser).

## Removed Points
These points are flagged to be removed; treat them with caution.

- *"Forward modeling baselines are compared only to a trivial Mean Model baseline — not to the numerical simulator (AxiSEM3D)."* — **Factually incorrect.** The ground truth in Table 2 *is* the AxiSEM3D numerical simulation; RL2 and R metrics directly measure deviation from it. The critic misread the evaluation methodology.
- *"The paper does not discuss any prior effort to combine them for global problems."* — **Missing-related-work criticism removed per policy** (the reviewer lacks external sources to confirm coverage).
- Several generic phrasing and formatting nitpicks removed per policy.

## Novel Insights
None beyond the paper's own contributions. The reviews surface no structural insight that the paper itself does not articulate.

## Suggestions
1. **Run at least one experiment on the Real Earth tier** — a forward modeling prediction for a held-out test structure, showing seismogram comparisons. This is the single most impactful addition.
2. **Add a traditional FWI baseline to the inversion experiments** on the Acoustic tier: run adjoint-based FWI for the same test cases and report correlation, iterations, and wall-clock time.
3. **Report PIDO with quantitative metrics** and clarify whether the temporal generalization experiment used a single velocity structure or a test set.
4. **Acknowledge the tier gap explicitly in the Discussion** — the paper currently does not discuss that all experiments are on the smaller tiers.
5. Clarify in the paper that the 6000-timestep seismogram (not the 20-snapshot wavefield) is the primary inversion signal for the Real Earth tier.

## Score and Decision

**Originality:** Moderate — the dataset design (three tiers, spherical harmonics parameterization) is well-motivated, though the ML methodologies applied are standard.  
**Importance of research question:** High — global FWI is computationally prohibitive, and ML acceleration is an active, important area.  
**Claims supported:** Partially — the speedup claim and smaller-scale feasibility are well-supported, but the global-scale claim is unsubstantiated.  
**Soundness of experiments:** Adequate for the smaller tiers, but the absence of Real Earth experiments and traditional-FWI baselines weakens the evaluation.  
**Clarity of writing:** Clear and well-structured; the dataset construction and problem framing are accessible.  
**Value to community:** Potentially high if the dataset is released and validated at global scale; currently limited by the evaluation gap.

The paper presents a potentially valuable dataset and demonstrates ML feasibility on smaller-scale proxies, but the most important claim (global-scale applicability) is not supported by any experiment, and the lack of comparison to traditional FWI leaves the contribution's practical significance unclear. A major revision addressing these gaps would substantially strengthen the paper.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
## Summary

This paper introduces MEGA, a memory-efficient framework for 4D Gaussian Splatting that comprises two core ideas: (1) replacing the expensive spherical harmonics color representation (144 parameters per Gaussian) with a compact DC-AC color decomposition (3 per-Gaussian parameters + a lightweight shared MLP), and (2) an entropy-constrained Gaussian deformation field that, when combined with an opacity-based entropy loss, drastically reduces the number of Gaussians needed to represent dynamic scenes. The method achieves ~190× storage reduction on Technicolor (6.1GB → 32MB) and ~125× on Neural 3D Video (3.1GB → 25MB) while maintaining competitive rendering quality and real-time FPS.

## Strengths

- **DC-AC color representation is simple, effective, and clearly validated.** Replacing 144 SH coefficients with 3 parameters + a lightweight 3-layer MLP achieves an ~8× per-Gaussian parameter reduction while maintaining or improving PSNR (Table 2: e.g., *Fabien* 34.21 vs. 33.57 for 4DGS). The ablation shows DAC significantly outperforms an alternative grid-based approach (Lee et al., 2024), which drops PSNR by 2+ dB on *Flame Steak*.

- **Entropy-constrained deformation + opacity loss synergistically reduce Gaussian count by >10×.** The combination (w/ DAC+Deformation+ℒ_opa) cuts Gaussians from 13.00M to 0.91M on *Birthday* while improving PSNR by 1 dB. Even on *Flame Steak* where PSNR drops slightly (33.19→32.27), Gaussian count drops from 5.17M to 0.87M. The synergy is clear: deformation alone increases count, ℒ_opa alone reduces it modestly, but the combination yields far greater reduction than either component alone.

- **Comprehensive evaluation on two standard multi-view dynamic datasets** with comparison against 10+ baselines including NeRF-based and Gaussian-based methods, plus a thorough ablation study across four scenes that isolates each component's contribution.

- **Practical compression pipeline** that combines the algorithmic contributions with standard FP16 and zip delta compression (cleanly described as post-processing steps, not conflated with algorithmic novelty).

## Weaknesses

### Major

- **View-dependent geometry deformation lacks physical justification and could limit generalization.** The deformation predictor (Eq. 4) takes view direction **d**ₓ as input and outputs position, scale, and rotation deformations. This makes the *geometry* of each Gaussian view-dependent at a given time step — in a physically consistent scene model, geometry should be view-independent and only color (radiance) should vary with viewpoint. While the method evaluates on held-out cameras from the 4×4 grid on Technicolor, these share similar viewing directions with the training cameras, making this a weak stress test. The paper neither discusses nor justifies why view-dependent geometry is acceptable. This does not undermine the compression results on the evaluated datasets, but it raises a legitimate concern about the representation's physical consistency and its reliability for truly novel camera trajectories.

### Minor

- **Compression ablation reports parameter counts, not final storage sizes.** The main compression claims (~190×, ~125×) combine the core algorithmic contribution (DAC + deformation + ℒ_opa) with FP16 (2×) and zip (~1.1×). While the paper is transparent about including these post-processing steps, the ablation table reports only "Params" (parameter count × bytes), not final storage after FP16+zip. Reporting final storage for each ablation variant would cleanly disentangle which compression factor comes from the algorithmic core versus standard post-processing. This is a presentation issue rather than a substantive flaw — the algorithmic contribution is still substantial (~86×).

- **The deformation predictor alone (without ℒ_opa) increases Gaussian count in all four ablation scenes**, sometimes dramatically (Fabien: 4.57M → 11.56M). The paper acknowledges this observation but offers no analysis of why this happens (e.g., does the deformation cause additional densification? Is the deformation magnitude too large?). This does not invalidate the method — the combined deformation+ℒ_opa clearly works synergistically — but the unexplained behavior leaves a gap in understanding the deformation component's role.

### Trivial

- None worth listing.

## Nice-to-Haves

- Reporting training GPU memory footprint would improve practical applicability assessment, since training 4DGS with millions of Gaussians plus MLPs is memory-intensive.
- Per-scene storage breakdowns on the full datasets (beyond the four ablation scenes) would help assess scene-level variability.
- A baseline showing 4DGS at FP16+zip would enable an apples-to-apples comparison of the algorithmic compression factor.

## Removed Points

- **Criticism about "inconsistent and uninterpretable behavior of the deformation component" as presented in the Harsh Critic's Critical Issue 3** — The critic claims "the paper's narrative that deformation + entropy loss 'expands the action range and forces fewer Gaussians' is not supported by the ablation data." This is factually incorrect. The data clearly shows that deformation+ℒ_opa reduces Gaussians far more than ℒ_opa alone (e.g., Birthday: 9.15M → 0.91M; Fabien: 2.32M → 0.31M), demonstrating synergy. The critic also claims "the opacity loss alone would be sufficient to reduce count" — this technically true statement ignores that the *combination* reduces count 3-10× further than ℒ_opa alone. The anomalous deformation-alone increase is kept as a minor weakness since the paper doesn't explain it, but the criticism about the combination not working is inaccurate.

- **Strength Finder's generic strengths ("important problem", "interesting question")** — Removed as superficial and not specific to the paper's concrete contributions.

- **Strength Finder's overlap with DAC color representation strength** — The strength was already captured.

- **The critic's claim about FP16+zip being ~2.2× contribution and "inflating" the compression numbers** — softened to a minor weakness since the paper explicitly mentions including these steps and does not hide them. The critic's framing of "conflating" is too harsh given the paper's transparency.

## Novel Insights

None beyond the paper's own contributions. The review surfaces a genuine structural concern (view-dependent geometry) that the paper itself does not discuss, but this is a limitation for the authors to address rather than a novel observation from the review process.

## Suggestions

1. **Address the view-dependent geometry issue directly** — either remove view direction from the deformation predictor input (using only time and position), or provide evidence that the learned deformation is approximately view-independent in practice, or present a theoretical justification for why view-conditioned geometry is acceptable.

2. **Add a storage column to the ablation table** reporting final FP16+zip storage for each variant, alongside the parameter counts.

3. **Analyze why deformation alone increases Gaussian count** — even a brief discussion (e.g., the deformation field enables more complex motion, which triggers additional splitting during densification before the entropy loss prunes) would clarify the mechanism.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Comparison |
|--------|-----------|-----------|
| Lightweight Predictive 3D Gaussian Splats (`PbheqxnO1e.md`) | 7.00 | Stronger paper with more novel hierarchical representation and better SOTA comparison. MEGA addresses the harder 4D dynamic setting but has less novel methodology. |
| SplineGS (`tMG6btjBfd.md`) | 6.00 | Closest topic. Comparable methodological novelty and experimental rigor. SplineGS has cleaner deformation modeling (no view-dependence issue) but MEGA's compression contribution is more practically significant. |
| Fast Feedforward 3DGS Compression (`DCandSZ2F1.md`) | 6.50 | Stronger in terms of novelty (optimization-free feedforward pipeline) and breadth. MEGA has comparable experimental quality. |
| Swift4D (`c1RhJVTPwT.md`) | 6.50 | Both address dynamic scene Gaussian splatting. Swift4D's static/dynamic decomposition is cleaner conceptually. MEGA's compression ratios are more impressive. |
| CoINR (`ZWi6RpT4mJ.md`) | 3.50 | Fundamentally flawed paper with incorrect mathematical claims. MEGA is substantially stronger — no such errors, solid experiments. |
| Multi-view Consistent Image Gen. (`Ns84n4NWh6.md`) | 3.50 | Different topic but similar score floor. Weak presentation and insufficient experiments. MEGA is far more thorough. |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>
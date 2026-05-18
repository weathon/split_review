## Summary

This paper addresses a genuine limitation of mesh-based graph neural networks: their inability to model anisotropic elastic materials because standard message-passing aggregates edge features without preserving directional information. The authors propose a directional encoding that decomposes edge features into weighted components along material-space basis vectors and aggregates these components separately. Built on an encoder-processor-decoder architecture with a self-supervised physics-based loss (variational implicit Euler), the method is tested against a re-implemented MeshGraphNet on cantilever beam benchmarks, showing substantial improvements in stress-strain prediction, tip displacement, and volume preservation.

## Strengths

- **Clear identification of a fundamental limitation and a simple, principled fix.** The paper pinpoints that standard sum/mean aggregation of edge features discards directional deformation information (Section 3.1). The proposed fix — decomposing edge features into weighted components along material-space basis vectors and aggregating these separately (Equations 3–4) — is conceptually clean, well-motivated, and requires minimal changes to existing architectures. The intuition about edge orientation determining sensing capacity is concretely articulated.

- **Consistent and large quantitative improvements over the baseline.** Under multiple evaluation settings (stress-strain curves in Figure 5, tip displacement in Table 1, imbalanced force in Table 2), the proposed method substantially outperforms the re-implemented MeshGraphNet. Improvements are often an order of magnitude (e.g., tip displacement error of 0.0017 vs 0.0164 for a rectangular beam with parallel fibers). The fiber energy error decomposition in Figure 4 provides an informative diagnostic linking the gap specifically to modeling anisotropy.

- **Well-motivated self-supervised loss.** The physics-based loss function (Section 3.2) is derived from the variational formulation of implicit Euler, directly penalizing violation of dynamic equilibrium with elastic (isotropic + anisotropic), kinetic, and external energy terms. This eliminates the need for ground-truth simulation data during training, which is a practically valuable property.

## Weaknesses

### Major

- **No statistical grounding for any quantitative result.** All numerical results (Tables 1 and 2, Figures 3, 5, 6) are reported as single point estimates without variance, error bars, or confidence intervals. The convergence study (Figure 3) uses 15 random test configurations but shows only a single line per method. Without multiple seeds or runs, the reader cannot assess whether the reported improvements are reliable or attributable to random initialization. This is the single most impactful missing element — it turns suggestive evidence into inconclusive evidence.

- **No clean ablation isolating the directional encoding.** The paper compares the full proposed architecture against a re-implemented MeshGraphNet that removes directional encoding *and* differs in other architectural details. A proper ablation would compare the authors' own architecture *with* and *without* the directional encoding (i.e., replacing the three directional sums in Equation 3 with a standard sum over all incident edge features), keeping all other components (loss, training pipeline, hyperparameters) identical. Without this, it is unclear whether the claimed gains come from the directional encoding specifically or from other implementation differences in the re-implementation.

- **Limited baseline scope.** Only one existing method (MeshGraphNet) is compared against. The related work section cites GNS, MGN, and cloth-specific GNN approaches, but none are included as baselines. Claiming superiority over "the state-of-the-art method" based on a single re-implemented baseline is not sufficient.

### Minor

- **Volume preservation gap raises unanswered questions.** Figure 6 shows MeshGraphNet permitting up to 60% volume change while the proposed method achieves "almost zero" — a striking difference. However, volume preservation is primarily governed by Poisson effects in the isotropic term of the loss function, not obviously by directional encoding. The paper does not provide convergence curves for this metric or evidence that the baseline's performance does not improve with longer training. The gap is so large that it raises questions about whether the baseline re-implementation is suboptimal in some other respect (e.g., insufficient training for this particular metric).

- **No evaluation on isotropic materials.** The paper motivates directional encoding by the failure of existing methods on anisotropic materials, but does not include a control experiment showing that the method does *not* harm performance on isotropic materials where both methods should agree. Such an experiment would rule out the possibility that the directional encoding introduces biases that accidentally help on anisotropic cases but degrade general behavior.

- **Limited quantitative evaluation of generalization.** Generalization to unseen geometries (T-shaped, Y-shaped objects in Figure 7) is shown only qualitatively. Quantitative error metrics on these geometries would substantially strengthen the claim of robustness.

- **Global basis vector definition not discussed.** The paper does not specify how the material-space basis vectors (𝔼_x, 𝔼_y, 𝔼_z) are chosen for objects of arbitrary shape or orientation, or whether the method is invariant to rotation of the input. If the basis is defined in world coordinates, rotating the object changes the features — this should be addressed.

- **Connection between vertex predictions and element-wise energy loss not detailed.** The loss is summed over elements (tetrahedra), but the network predicts vertex accelerations. How per-element quantities (deformation gradient, Green strain) are computed from vertex predictions for the element-wise energy evaluation is not explained, which is a reproducibility gap.

### Trivial

- The y-axis label in Figure 3 is missing units (presumably Joules).

## Nice-to-Haves

- Including a runtime comparison between the two methods would be useful to confirm that the directional encoding (which requires three separate aggregations) does not meaningfully increase inference cost. The paper does report 9ms inference for 100 elements, which is a good start.
- Adding confidence intervals or reporting results over multiple random seeds would transform the quantitative evaluation from suggestive to persuasive.

## Removed Points

The following points from the harsh critic were removed or merged:

1. **The claim that the comparison "simultaneously changes two things (architecture AND training protocol)"** — Partially removed. The paper explicitly says "for fair comparisons, we implemented an unsupervised version using their network architectures" (Section 4), so the training protocol (self-supervised) is the same for both. The pointed-out absence of a within-architecture ablation is retained as a Major weakness; the framing about "two things changing" is incorrect.

2. **Speculation that "the baseline may not have been trained to convergence" for volume preservation** — Removed as speculation. The paper states both methods were trained identically for 672k epochs. The related concern about no convergence curves for this specific metric is retained in the Minor section.

3. **Criticism about 672k epochs being "extremely long"** — Subjective observation, removed.

4. **"No discussion of how..." under Strengthening section** — Some of these are covered in Minor weaknesses; others are speculative or outside scope.

5. **Generic claims from Strength Finder about the "importance of the problem"** — Removed as generic/superficial.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel perspective that the paper itself does not already present.

## Suggestions

1. **Add error bars and multiple-seed reporting.** Run each method with at least 3 random seeds and report mean ± std for all quantitative results — Tables 1, 2, and Figures 3, 5, 6. This is the single highest-impact improvement you can make.

2. **Run a within-architecture ablation.** Compare your full architecture against an identical architecture where the three directional sums are replaced by a single standard sum over all incident edge features. This isolates the effect of the directional encoding.

3. **Add an isotropic material control experiment.** Show that on an isotropic test case (κ=0), the proposed method matches MeshGraphNet performance, confirming the directional encoding does not introduce harmful bias.

4. **Include at least one additional baseline** (e.g., GNS with the same self-supervised loss).

5. **Add quantitative generalization metrics** for the T-shaped and Y-shaped geometries in Figure 7 rather than only qualitative visuals.

## Score and Decision

**Calibration summary:**

**Round 1 (bracketing):**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| ItPYVON0mI (CG potentials) | 3.00 | R1 | Significantly weaker — poor evaluation, unclear contribution |
| zuuhtmK1Ub (Implicit solver GNN) | 2.00 | R1 | Much weaker — insufficient evidence, unclear benefits |
| VSVQljJU5N (Sheaf NN for RecSys) | 3.00 | R1 | Unrelated topic, weaker evaluation |
| s77FHD4wra (Rigid body GNN) | 4.75 | R1 | Similar evaluation issues (limited baselines, unclear ablations) but less clear contribution |
| QB8dHqVoDw (Transfer learning GNN) | 4.75 | R1 | Similar evaluation limitations (one baseline, missing ablations), comparable quality |
| pWrcpPsVas (GNN for interferometers) | 4.25 | R1 | Similar — limited baselines, missing ablations, but different domain |
| XWBE90OYlH (Edge signal orientation) | 7.00 | R1 | Stronger — thorough theoretical and empirical evaluation |
| 7BLXhmWvwF (Geometry-aware RL) | 8.00 | R1 | Stronger — comprehensive evaluation, multiple tasks |
| fU8H4lzkIm (PhyMPGN) | 8.00 | R1 | Stronger — extensive evaluation on multiple PDE systems |

**Round 1 bracket:** [4.5, 6.5]

**Round 2 (narrowing within bracket):**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| 3lDxKQepvn (Latent task-specific GNS) | 5.75 | R2 | Stronger evaluation but less clear contribution; this paper is slightly weaker overall |
| TSTgP4W3ga (Grid coarsening GNN) | 4.50 | R2 | Weaker — less clear practical value |
| r8t6OsLP2s (DHMP hierarchies) | 5.25 | R2 | Comparable — similar issues with baseline reproduction concerns, but more baselines |
| smy4DsUbBo (Energy-conserving GNN) | 6.00 | R2 | Stronger — more thorough evaluation, accepted paper |
| BBD6KXIGJL (Hybrid directional GNN) | 7.33 | R2 | Stronger — well-evaluated on standard benchmarks |

**Final positioning:** The paper sits slightly below the 5.25–5.75 range papers (DHMP, Latent Task-Specific GNS) because despite having a genuinely novel and clean contribution, the evaluation is notably weaker — no statistical rigor (no error bars), no within-architecture ablation of the core idea, and only one baseline. These gaps directly affect the persuasiveness of the central claims.

**Score: 5.0** — Marginally above a clear reject. The core idea is strong, well-motivated, and easy to implement, but the evaluation in its current form does not provide convincing evidence for the claims. The paper could become a solid contribution (~6–6.5) with proper statistical reporting, a clean ablation, and additional baselines.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
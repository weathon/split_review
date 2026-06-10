## Summary

This paper proposes MOS (Model Synergy), a test-time adaptation (TTA) framework for LiDAR-based 3D object detection. The key idea is to maintain a bank of historical checkpoints from the adaptation process and dynamically assemble them into a "super model" per test batch using synergy weights derived from the inverse of a generalized Gram matrix. Two task-specific similarity functions — feature-map rank similarity and Hungarian-matched box cost — replace the standard parameter inner product in the Gram matrix. MOS is evaluated on cross-dataset, corruption, and hybrid cross-corruption shifts, showing consistent improvements over prior TTA baselines.

## Strengths

- **Consistent superiority across all eight corruption types on KITTI→KITTI-C**: In Table 2, MOS achieves the best AP₃D at all difficulty levels on every corruption type, with mean gains of 3.73%/5.56%/4.78% over the best baseline and notably +23.98% on incomplete echoes (hard). This breadth rules out the possibility that the method only works on specific corruptions.

- **Single-pass online adaptation competitive with multi-epoch UDA**: On Waymo→KITTI, MOS achieves 81.90/64.16 (AP_BEV/AP_3D moderate), rivaling ST3D (82.19/61.83) despite being online and single-pass while ST3D requires offline multi-epoch training. On the closed-gap metric, MOS scores 79.79% (AP_3D) vs ST3D's 74.72%.

- **Bank update mechanism achieving efficiency with diversity**: Maintaining only K=3 checkpoints — selected via average synergy weights — outperforms an ensemble of the 20 latest checkpoints by 18.42% in AP₃D while reducing memory by 85% (Section "Sensitivity to Hyperparameters").

- **Inverse-Gram weighting with 3D-detection-specific similarity functions is anovel formulation for dynamic checkpoint assembly**: The ablation (Table 4) confirms that removing either similarity function degrades moderate AP₃D by 6.9% or 4.5%, and full MOS outperforms mean ensemble by 39.8%.

## Weaknesses

### Major

- **Cross-corruption results lack tabular support with absolute metric values**. The paper claims 67.3% improvement over the best baseline and 161.5% over direct inference on Waymo→KITTI-C (abstract, line 236–237), along with per-corruption improvements of 97.99% and 76.38% for the two hardest corruptions. However, no table of actual AP values is provided — only percentage improvements and a reference to a heatmap. Some absolute baseline numbers are given only for the No-Adapt setting (3.51% AP for incomplete echoes at hard, 7.40% for cross-sensor). Without absolute values for MOS and all competing methods, the reader cannot assess (a) whether large relative gains correspond to small absolute improvements from a low floor, (b) the variance of gains across corruption types, or (c) how the aggregated 67.3% figure is computed. The paper needs a table analogous to Table 2 for the cross-corruption experiment. This is the most significant evidential gap.

### Minor

- **The "outperforms UDA" claim is overstated relative to the evidence**. The abstract and contributions (lines 4, 37) claim MOS "even outperforms the UDA method" ST3D on Waymo→KITTI. Table 1 shows MOS at 81.90/64.16 vs ST3D at 82.19/61.83 — MOS is slightly behind on AP_BEV and ahead on AP_3D. This is a mixed result on a single metric dimension, not a clear outperformance. Moreover, the comparison conflates two fundamentally different paradigms (online single-pass TTA vs offline multi-epoch UDA). The claim should be caveated to reflect the selective nature of the advantage.

- **The transfer of inverse-Gram redundancy-penalizing logic from parameter space to prediction-similarity space is asserted without justification**. The paper correctly explains that for the parameter-space Gram matrix **G**, its inverse **G⁻¹** penalizes redundant (low-variance) directions (lines 88–91). It then replaces the parameter inner products ⟨f_i, f_j⟩ with prediction-based similarity functions S_box × S_feat (Eq. 9, lines 93–98), asserting that the generalized **Ĝ⁻¹** inherits the same redundancy-penalizing interpretation. This is not obvious — the precision-matrix property that supports the parameter-space interpretation depends on the variance structure of parameter space. The paper provides neither theoretical argument nor empirical validation (e.g., showing that **Ĝ⁻¹** actually decorrelates checkpoint contributions as intended) for why the same logic holds when **G** is constructed from per-batch prediction dissimilarities. Since this is the linchpin of the method, the gap is notable.

- **The ablation study lacks a critical control: inverse-Gram weighting using the original parameter inner products (without S_box or S_feat)**. The ablation (Table 4) shows that "Mean Ensemble" (simple averaging, 45.89 moderate AP₃D) is far below MOS (64.16). "MOS w/o S_feat" (59.98) and "MOS w/o S_box" (61.40) show intermediate results. But the paper never tests **MOS with the original parameter-inner-product Gram matrix** (i.e., **G⁻¹** without any S_box or S_feat). This control would isolate whether the gains come from the sophisticated similarity functions or from inverse-Gram weighting itself. Without it, the contribution of the proposed similarity functions is confounded with the benefit of any inverse-Gram weighting scheme.

- **The conclusion claims generality for "both voxel- and point-based 3D detectors" (line 258), but all main experiments use only SECOND (voxel-based)**. No point-based detector results appear in the main paper. This claim is unsupported by the presented evidence.

- **Gram matrix inversion stability is not addressed**. With only K=3–5 potentially correlated checkpoints, the Gram matrix may be near-singular. The paper does not mention whether any regularization (e.g., adding ε**I** to the diagonal) is applied before inversion. If none is used, numerical instability is a concern; if one is used, it should be reported.

### Trivial

- No variance or statistical significance is reported. Given that some gains in Table 2 are small (e.g., Fog: 85.22 vs 85.11 at easy), the reader cannot distinguish signal from noise. (Standard in the field but worth noting.)
- Only the "car" category is evaluated on KITTI. Generality to pedestrian/cyclist detection is unresolved.

## Nice-to-Haves

- The paper could discuss why certain corruptions (Incomplete echoes, Snow) see much larger gains than others (Fog, Motion blur) — this pattern in Table 2 suggests a story about the method's strengths and limitations that goes untold.
- The sensitivity of MOS to the quality of the initial K warm-up checkpoints (Phase 1) is not analyzed. Since these early checkpoints are trained by self-training without synergy, they may be lower quality, and their errors could propagate.
- The choice of matrix rank as a feature-level similarity metric (Eq. 10) could be better motivated. Practical concerns about rank computation cost on large feature maps and sensitivity to numerical precision are not discussed.

## Removed Points

The following points from the input reviews were removed with justification:

- **"The paper should acknowledge concurrent work on online adaptation for 3D perception"** — Removed per the rule on missing related works (cannot verify existence of unmentioned works).
- **"Cross-corruption heatmap was stripped by the parser"** — Removed as a formatting-artifact complaint. The substantive criticism (missing tabular absolute values) is retained above.
- **"Parametric cost and efficiency concerns about rank computation"** — Moved to Nice-to-Haves from a formal weakness; the method demonstrably runs with acceptable cost (0.255s/frame overhead reported).
- **"The paper should compare against various alternative design choices (entropy-weighted averaging, performance-weighted averaging)"** — Removed as scope creep; the paper proposes a specific method and the ablation already validates its components.

## Novel Insights

The reviews surface a productive tension in this paper: the method is empirically effective (the corruption results in Table 2 are clean and broadly convincing), but the theoretical framing of the synergy weights is weaker than the presentation suggests. The uniform-similarity assumption and the transfer of inverse-Gram logic to prediction-similarity space are design choices presented as principled derivations. This mismatch between empirical success and theoretical justification is common in applied deep learning but is worth flagging because the strength of the empirical results may cause readers to overestimate the rigor of the method's foundations. The paper would be stronger if it acknowledged the heuristic nature of these choices and validated them empirically against alternatives rather than presenting them as consequences of optimization.

## Suggestions

1. Add a full table (analogous to Table 2) reporting absolute AP_BEV/AP_3D values for all methods on the cross-corruption (Waymo→KITTI-C) experiment. This is the single highest-impact improvement.
2. Add an ablation using the original parameter-inner-product Gram matrix (without S_box or S_feat) to isolate the benefit of the proposed similarity functions from inverse-Gram weighting itself.
3. Recast the synergy weight derivation transparently as a design choice (uniform similarity as a fairness heuristic) and provide empirical comparison against alternative weighting schemes.
4. Clarify whether Gram matrix inversion uses regularization (εI), and if so, report the value.
5. Either add results with a point-based detector or remove the claim of generality from the conclusion.
6. Qualify the "outperforms UDA" claim to reflect the mixed nature of the comparison (AP_BEV behind, AP_3D ahead) and the different operating conditions.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
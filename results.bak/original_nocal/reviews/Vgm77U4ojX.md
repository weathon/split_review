Now I have all the information needed. Let me write the consolidated review.

## Summary

SIGMADOCK introduces a fragment-based SE(3) Riemannian diffusion model for molecular docking. The key idea is to decompose a ligand into rigid-body fragments by breaking rotatable bonds, then define a diffusion process over the translation and rotation of each fragment. This avoids the entangled non-product dynamics of torsional diffusion models. The paper also contributes a fragmentation reduction scheme (FR3D), soft triangulation constraints to preserve bond geometry, and an SO(3)-equivariant architecture. Empirically, SIGMADOCK achieves 79.9% Top-1 PB-valid success rate on PoseBusters — substantially outperforming prior deep learning methods (12.7–32.8% PB-valid) and surpassing classical physics-based docking on the same split for the first time.

## Strengths

1. **Well-motivated fragment diffusion framework**: The paper identifies a genuine flaw in torsional diffusion models (Theorem 1 — non-product induced measures in Cartesian space from independent torsional perturbations) and proposes a principled alternative: diffusing over SE(3)^m fragments whose forward process factorises as a product of Haar measures. The theoretical analysis is clear and connects directly to the method's architectural choices.

2. **State-of-the-art empirical results**: SIGMADOCK achieves 79.9% Top-1 PB-valid on PoseBusters, with a 6.3× improvement over DiffDock (12.7% PB-valid on the same split) and is the first deep learning method to surpass classical physics-based docking under the PB train-test split. The 90.6% Top-1 on Astex further confirms the result. The paper also demonstrates AF3-competitive performance (84% AF3 vs 79.9% SIGMADOCK) with 50× faster sampling and 19k training complexes.

3. **Strong ablation study (Table 1)**: Each component's contribution is systematically isolated: triangulation conditioning (67.1→79.9%, +12.8 pts), protein-ligand interactions (76.3→79.9%), fragment merging (73.7→79.9%), and the ranking heuristic (66.1→79.9%). This allows readers to assess what drives performance and is a model of good evaluation practice.

4. **Generalization analysis**: The co-factor analysis (Table 2) provides indirect evidence of genuine physical learning: failure rate is 16.2% for complexes without co-factors vs 41.2% for those with natural ligands, consistent with the model learning protein-ligand interactions rather than memorizing. Table 3 shows robustness to pocket size (80.2% PB-valid at 5Å, 77.3% at 6Å).

## Weaknesses

### Fatal
None. The paper's core contributions (fragment-based SE(3) diffusion, triangulation constraints, SE(3)-equivariant architecture, strong empirical results) are not invalidated by any single issue. The presentation issues below need resolution but do not undermine the core claims.

### Major

1. **Inconsistency between per-sequence-similarity breakdown and overall results (Figure 4, right panel vs Table 1 & Table 4)**: The right panel of Figure 4 reports per-sequence-similarity Top-1 rates of 51%, 53%, 53% (N=109, 76, 123), yielding a weighted average of ~52%. However, Table 1 reports an overall RMSD < 2 of 80.5% and PB-Val of 79.9%, while Table 4 gives per-sequence-similarity PB-Val values of 72%, 79%, 87% (which correctly average to ~80%). The right chart values (~52%) are not consistent with either of these overall figures. The paper must clarify what metric the right panel of Figure 4 reports (e.g., RMSD-only with a different ranking configuration, unselected seeds, or a different protocol) and ensure consistency between per-bin and overall results. Without clarification, the reader cannot verify the claim of "consistent generalisation to unseen proteins."

2. **Ambiguity in Figure 4 (left) metric specification for baselines**: The left panel of Figure 4 reports "PB (%)" values for baselines (15.9–58.1%) and 79.9% for SIGMADOCK. The paper states that 79.9% is PB-valid (RMSD < 2Å + physicochemical checks). However, it is not specified whether the baseline numbers are RMSD-only or PB-valid. The abstract gives a comparison to 12.7–32.8% (which is the PB-valid range for baselines from the literature), but the figure numbers (15.9–58.1%) are different and likely RMSD-only. While the paper's textual claims appear to use correct apples-to-apples PB-valid comparisons, the figure mixes or unclearly labels the metrics, making the visual comparison misleading. The authors should either report PB-valid for all baselines in the figure or clearly annotate which metric each set of numbers uses.

### Minor

1. **"Pseudo binding energy" ranking heuristic is not defined in the main text**: Section 2.5 introduces a ranking heuristic using "(pseudo) binding energy of the generated protein-ligand system" to select among N_seeds samples. Ablation D ("(-) Energy Scoring") drops PB-Val from 79.9% to 66.1% — a 13.8 point contribution, the largest among all ablated components except PB-check removal. Yet the main text never defines what this pseudo binding energy is (e.g., a classical scoring function, a learned energy, or a simple heuristic). While Appendix F (removed during parsing) likely provides details, the main text should at minimum give a brief definition, and specify whether external physics computation is required. This is important for interpreting the "surpassing classical docking" claim.

2. **No controlled comparison to a torsional model under the same architecture/data**: The theoretical critique of torsional models (Theorem 1, Section 2.2.2) is well-reasoned but entirely theoretical. An experiment training a torsional model with the same EquiformerV2 backbone, data, and evaluation protocol would directly isolate the benefit of the fragment representation. The current comparison is against published torsional model numbers rather than a controlled ablation. This does not invalidate the results, but it would substantially strengthen the claim that "fragment diffusion is superior."

3. **AlphaFold3 comparison is thin in the main text**: The paper claims "competitive performance relative to AF3 with a fraction of the training data and lower test-train leakage" but supports this with only one quantitative comparison (Table 4: 79.9 vs 80.2 PB-Val overall) and a deferred test-train leakage analysis (Appendix J, removed). Given AF3 is a key reference point, the main text should include more direct comparison or clarify that thorough co-folding comparison is outside the paper's scope (re-docking, not co-folding).

### Trivial

- The right chart of Figure 4 is labeled "Top-1 (%)" while Table 1 uses separate columns for "RMSD < 2" and "PB Val." — standardizing the metric labels across all figures and tables would prevent confusion.
- The per-sequence-similarity bin [0, 30) in Table 4 lists two counts (109 and 38) without clear headers distinguishing SIGMADOCK from AF3 counts.

## Nice-to-Haves

- A qualitative figure showing successful and challenging failure cases (especially co-factor cases) would help interpret the method's behavior.
- An ablation comparing different ranking heuristics (e.g., random selection, confidence-model-based selection) would help isolate the contribution of the energy scoring mechanism.
- Testing robustness to the choice of conformer generator (beyond RDKit ETKDGv3) would strengthen the claims about the conformational manifold.

## Removed Points

These points from the reviews are excluded or downgraded for the reasons given:

- **"Internal inconsistency — right panel (~52%) vs left panel (79.9%) cannot both be correct"**: This conflates two different metrics. The right panel appears to show RMSD-only Top-1 (~52%), while the left panel and Table 4 show PB-valid (~80%). These are different metrics, so there is no mathematical inconsistency. However, the paper fails to clearly distinguish the metrics, which is captured in the Major weaknesses above. The stronger charge of "fatal inconsistency" is unwarranted — the numbers are reconcilable if the metrics differ — and is removed.

- **"Pseudo binding energy: if from classical scoring then undercuts headline claim"**: Speculative. Even if the energy is from a classical scoring function, using it to *rank* generated samples (select the best of 40) is fundamentally different from performing physics-based docking from scratch. The model generates poses; the ranking just selects among them. This does not "undercut" the headline claim. The real issue is that the energy is undefined in the main text, which is captured as a Minor weakness above.

- **Strength about "open-sourced codebase"**: Generic and does not constitute a scientific strength of the paper's contribution.

- **Strength about "data efficiency and fast inference"**: Partially retained, but the specific "50× faster" claim is in the paper and is valid; the strength is implicitly covered by the empirical results strength.

- **Various formatting nitpicks and speculations about missing appendices**: Removed per policy — the parser strips appendices from all papers; criticism about missing appendix content is not valid.

## Novel Insights

The most interesting cross-cutting observation from the reviews is that the "pseudo binding energy" ranking contributes 13.8 points (the largest single-component gain in the ablation aside from PB-validity checks), yet the paper treats it as a throw-away "simple and cheap heuristic." This asymmetry — where a method claimed to surpass classical docking depends heavily on a post-hoc selection criterion for its headline performance — warrants careful analysis. If the ranking is indeed classical physics-based, one might ask: is SIGMADOCK learning physics that aligns with classical scoring, or is the generative model broad and the ranking does the heavy lifting? The ablation shows 66.1% PB-valid even without the energy scoring (still SOTA among generative methods on this split), so the model itself is strong. But the full 79.9% claim clearly depends on understanding what this energy is.

## Suggestions

1. **Clarify the per-sequence-similarity results**: State explicitly what metric the right panel of Figure 4 reports (RMSD-only vs PB-valid, with which ranking/seed configuration). Reconcile the ~52% weighted average with the 80.5% overall RMSD < 2 from Table 1. If the right chart uses a different protocol, state it clearly in the caption and main text.

2. **Define the pseudo binding energy in the main text**: Even a one-sentence definition (e.g., "the sum of pairwise interaction energies computed via [X scoring function]") would resolve the current ambiguity. Consider adding a brief ablation comparing different ranking strategies.

3. **Annotate Figure 4 metrics**: Clearly label whether baseline numbers in the left panel are RMSD-only or PB-valid, and whether SIGMADOCK's number is PB-valid. If space permits, show both metrics for all methods.

4. **Add AF3 comparison details to the main text**: At minimum, include the test-train leakage analysis summary and more per-bin comparisons beyond the single 79.9 vs 80.2 overall number.

5. **Consider adding a controlled torsional baseline experiment**: Even as an appendix ablation with a simplified architecture, it would strengthen the theoretical claims of Section 2.2.2.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
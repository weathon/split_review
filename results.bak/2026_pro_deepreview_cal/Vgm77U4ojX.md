Now I have sufficient calibration data. Let me write the final consolidated review.

---

## Summary

SIGMADOCK introduces a fragment-based SE(3) diffusion model for protein–ligand docking. The key idea is to decompose a ligand into rigid-body fragments at rotatable bonds and learn to reassemble them within a protein binding pocket via Riemannian diffusion on SE(3)^m. The method includes a novel irreducible fragmentation scheme (FR3D) that merges fragments to reduce degrees of freedom, soft triangulation constraints to preserve bond geometry, and an SO(3)-equivariant architecture. On the PoseBusters benchmark under the intended temporal train–test split, SIGMADOCK achieves 79.9% Top‑1 PB‑valid (RMSD < 2 Å) success, substantially outperforming prior deep learning methods and classical docking, with strong generalisation across sequence-similarity splits.

## Strengths

- **State-of-the-art re-docking accuracy with rigorous metrics**: On the PoseBusters set under the correct temporal split, SIGMADOCK achieves 79.9% Top‑1 PB‑valid success (Tables 1, 4; Figure 4), compared to 12.7–32.8% for prior generative methods (DiffDock, etc.) and 56.0% RMSD success for AutoDock Vina (Table 3). On Astex, it reaches 90.6%. These margins are large and the use of PB‑validity alongside RMSD directly addresses the well-documented problem of chemically implausible deep-learning docking outputs (Butenschoen et al., 2024).

- **Strong generalisation to unseen proteins**: Performance does not collapse on low-sequence-similarity targets: 51–53% Top‑1 across bins, and 72% on [0,30)% identity vs. AF3's 87% (Figure 4 right; Table 4). This addresses the common critique that deep docking models memorise rather than generalise.

- **Careful ablation evidence**: Table 1 reports controlled ablations showing that removing triangulation conditioning costs ~12.8 percentage points PB‑valid, removing protein–ligand interactions costs ~3.6 points, and removing fragment merging costs ~6.2 points. The ablation on sampling from ℳ_b vs. ℳ_c (conf. G, 85.4% vs. 79.9%) quantifies the cost of using generated conformers rather than bound-state fragments, and the ranking heuristic ablation (confs. D, E) isolates its contribution.

- **Well-motivated theoretical framework**: Theorem 1 formalises why torsional-space diffusion produces entangled, non-product induced measures in Cartesian space, motivating the factorised SE(3)^m approach. Theorem 2 proves invariance to the arbitrary choice of fragment local-coordinate orientation via the Newton–Euler prediction head. Lemma 1 establishes that triangulation conditioning determines bond angles without restricting dihedral freedom. These theoretical results collectively justify the design choices.

- **Robustness analysis**: The pocket-size sweep (Table 3) shows PB‑valid remains at 68.2% even at d₀ = 7 Å (two standard deviations above the training mean), and the co-factor stratification (Table 2) reveals that failures concentrate in complexes with additional co-factors (natural ligands, ions, crystallisation aids) — a pattern consistent with the method's deliberate exclusion of co-factor modelling. Both analyses lend credibility to the results.

## Weaknesses

### Fatal

None.

### Major

- **Fragment merging implicitly fixes torsional angles, constraining the reachable conformational manifold**: Section 2.2.3 describes FR3D merging fragments across rotatable bonds. The paper argues that removing "over‑constrained dummy atoms" prevents the merged fragment from over‑defining a dihedral. However, the real atoms A, B, C, D that define the dihedral across a former rotatable bond are now all part of one rigid fragment — the dihedral value is locked at whatever value it had in the conformer drawn from ℳ_c. This conflicts with the foundational claim that "any chemically feasible pose can be recovered by composing these transformations" (Section 1, and Section 2.2.1). The alignment experiment (Figure 2b) shows that conformers can be torsionally aligned to bound poses with RMSD ≪ 2 Å, which empirically mitigates the concern. The ablation (Table 1, conf. C) shows merging is beneficial for the test set. But the theoretical claim of full reachability is overstated, and the paper does not quantify how often locked torsions deviate from their ground-truth bound values. A candid discussion of this trade-off is needed.

### Minor

- **No PB‑valid head-to-head with a classical docker in the main results**: The paper claims to be the "first deep learning approach to surpass classical physics-based docking." Vina appears in Table 3 (pocket-size sweep) at 56.0% RMSD < 2 Å success — well below SIGMADOCK's 80.5%. But PB‑valid rates for Vina are not reported, and classical dockers often produce chemically implausible poses. Running Vina under identical pocket definitions and reporting PB‑valid Top‑1 would make the headline claim fully watertight. The RMSD-only comparison already suggests a comfortable margin, so this does not threaten the core result but would strengthen it considerably.

- **Triangulation constraint satisfaction is not directly verified**: The conditioning feeds distance mismatches as edge features with the expectation that they converge to zero as t → 0 (Section 2.4). The paper does not report residual triangulation errors in top‑ranked poses. PoseBusters checks would catch gross bond-length/angle violations, but the reader cannot assess whether the conditioning mechanism is genuinely effective or whether failures are masked by the ranking heuristic. The ablation (conf. A, Table 1) shows removing triangulation hurts, but a direct diagnostic — e.g., distribution of ‖A−C‖ residuals — would close this evidential gap.

- **Inference speed claim is asserted but not measured**: The paper states SIGMADOCK offers "50× faster sampling" than AF3 (Section 3.2) without reporting wall‑clock times on identical hardware. The claim is plausible given the architectural differences, but measured numbers would substantiate the practical impact argument.

### Trivial

- The consequences of FR3D merging for torsional flexibility are not stated plainly in Section 2.2.3. Adding an explicit sentence — "When FR3D merges fragments across a rotatable bond, the corresponding dihedral becomes fixed at its conformer value" — would improve clarity (cf. the harsh critic's section-by-section note on Figure 3).

- The mapping φ from fragment poses back to a connected ligand (discarding dummy atoms, reconstructing bonds) is described only at a high level in the main text. The algorithmic details likely reside in the stripped appendix, but a brief summary in the main body would aid readability.

## Nice-to-Haves

- **Report statistical variation**: Training the model with multiple random seeds and providing confidence intervals for the main Top‑1 rates would strengthen the ablation conclusions and address reproducibility concerns. This is not standard in large-scale docking benchmarks and is not required for acceptance, but it would be a valuable addition.

- **Test robustness to alternative conformer generators**: The ablation sampling from ℳ_b (Table 1, conf. G) quantifies the cost of using RDKit's ETKDGv3 conformers vs. bound-state fragments. Testing with poorer conformer generators (e.g., random ring conformers) would further characterise the method's resilience to imperfect input geometries.

- **A dedicated limitations paragraph**: The paper mentions future extensions (flexible docking, co-folding) but does not candidly discuss the constraints of the current fixed‑receptor, pre‑defined‑pocket setting, the reliance on a single conformer generator, and the fragment‑merging torsional trade‑off. A short limitations paragraph in the conclusion would improve transparency.

## Removed Points

These points are flagged to be removed — treat them with caution:

- **Harsh Critic — Critical Issue 3 (unverified constraint satisfaction) rated as critical**: The critic framed this as a "critical issue," but it is a diagnostic gap, not a structural flaw. The ablation evidence partially addresses it, and the issue does not threaten any core claim. Demoted to Minor.

- **Harsh Critic — section-by-section note about alignment experiment depending solely on ETKDGv3**: The critic notes that "different generators could produce conformers that align less well." This is speculative — the paper provides empirical evidence for ETKDGv3, and the critic offers no counterexample. Removed as unsupported speculation; the conformer-quality sensitivity is already captured in the Nice-to-Have about alternative conformer generators.

- **Harsh Critic — "missing parts" about detailed φ mapping and limitations**: Both are noted as Trivial/Nice-to-Have points above. The critic's framing as "Missing Parts and Places to Improve" overstates the severity. The φ mapping details are almost certainly in the stripped appendix.

- **Strength Finder — "50× faster sampling" as a strength**: The paper asserts this but does not measure it. The data-efficiency point (matching AF3 with 19k vs. a much larger training set) is solid; the speed claim is downgraded but noted as a Minor weakness (unverified).

- **Strength Finder — supporting strength 4 (ranking heuristic)**: The fact that the heuristic is simple and effective is mildly interesting but is a minor engineering detail, not a substantive strength. Consolidated into the general results discussion rather than listed as a standalone strength.

## Novel Insights

The paper's key insight — that factorised SE(3)^m diffusion over rigid fragments avoids the entangled, non-product induced measures that plague torsional-space models — is genuinely novel and well-articulated. Theorem 1 provides a crisp formalisation of why torsional models suffer from poor conditioning, and the empirical results validate the fragment‑space alternative convincingly. A subtler insight, surfaced by the ablation and co‑factor analysis, is that the chemical plausibility gains come primarily from structural inductive biases (fragmentation, triangulation, protein–ligand interactions) rather than from expensive post‑processing or confidence models — SIGMADOCK achieves 70.8% PB‑valid even without the PB scoring heuristic (Table 1, conf. E). This suggests the field's focus on confidence‑model refinements may be less important than careful geometric design of the generative process itself.

## Suggestions

- Add a sentence in Section 2.2.3 explicitly stating that FR3D merging fixes the dihedral angles of merged rotatable bonds, and discuss the empirical justification (Figure 2b alignment) for why this does not catastrophically limit reachability. Quantify, for the PoseBusters test set, the fraction of merged torsions where the locked conformer value deviates from the bound value by more than, say, 30°.
- Run AutoDock Vina under the same pocket definitions and ranking heuristic as SIGMADOCK and report PB‑valid Top‑1 alongside RMSD Top‑1. This single addition would make the headline claim about surpassing classical docking fully convincing.
- Report the distribution of residual triangulation distances in top‑ranked poses to validate that the soft conditioning mechanism is effective.
- Measure and report inference wall‑clock times on a specified hardware configuration for both SIGMADOCK and, ideally, a reference method, to support the 50× speed claim.

## Score and Decision

### Anchor comparison

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| m9zWBn1Y2j (Ligand Conformation Gen.) | 3.00 | R1-low | Irrelevant task; SIGMADOCK is far stronger |
| kKXIYUi8ff (DynamicsDiffusion) | 3.00 | R1-low | Different task; not comparable |
| G536mmC2HL (TorSeq) | 3.00 | R1-low | Torsional modeling paper; SIGMADOCK's motivation directly addresses the limitations these papers face |
| rEQ8OiBxbZ (LEGO) | 3.00 | R1-low | Pretraining, not docking; not comparable |
| 1IaoWBqB6K (DiffDock-Pocket) | 5.00 | R1-mid | Pocket-level docking; SIGMADOCK has substantially stronger results, more novel methodology, and more thorough evaluation |
| FuXtwQs7pj (Diffusion on Toric Var.) | 4.50 | R1-mid | Different problem; SIGMADOCK's empirical validation is far more comprehensive |
| S4zpk61r6G (DiffMaSIF) | 4.67 | R1-mid | Protein–protein docking, different task |
| qH9nrMNTIW (IPDiff) | 6.25 | R1-mid | Molecule generation for SBDD; SIGMADOCK's docking task is different but SIGMADOCK has more rigorous evaluation and stronger results |
| 9qS3HzSDNv (Protein Dynamics SBDD) | 6.20 | R2-mid | Flexible docking with MD; SIGMADOCK's re-docking results are stronger within its scope |
| zDC3iCBxJb (GroupBind) | 6.75 | R2-mid | Docking with group information; SIGMADOCK has better evaluation, better results, and more methodological novelty |
| RyWypcIMiE (SBDD Evaluation) | 6.50 | R2-mid | Evaluation paper, not a method; not directly comparable |
| KSLkFYHlYg (ShEPhERD) | 8.00 | R2-high | Strong accept; different task (molecular design vs. docking) but similar calibre of methodological and empirical contribution |
| kJFIH23hXb (FoldFlow) | 8.00 | R2-high | SE(3) flow matching for protein backbone; different domain but similar theoretical depth |
| NSVtmmzeRB (GeoBFN) | 8.00 | R2-high | 3D molecule generation; different task but comparable quality |
| gHLWTzKiZV (FlexDock) | 8.00 | R2-high | Most comparable anchor: flexible docking with flow matching, 73% PB-valid. SIGMADOCK achieves higher PB-valid (79.9%), has more thorough ablations, and stronger theoretical grounding. Comparable overall quality. |

**Bracket**: Round 1 placed SIGMADOCK between 6.5 and 8.5 relative to the middle-band (IPDiff 6.25, GroupBind 6.75) and high-band anchors (FlexDock/ShEPhERD/FoldFlow all 8.0). Round 2 confirmed it sits in the 7.5–8.5 range, clearly above the 6.2–6.75 group and comparable to the 8.0 anchors. SIGMADOCK is at least as strong as FlexDock (8.00) — it has more thorough ablations, comparable theoretical contributions, and higher empirical performance — but the torsional-flexibility limitation and the missing PB‑valid classical-docker comparison prevent it from clearly exceeding the 8.0 anchors.

**Final score**: 8.0 — SIGMADOCK is a strong paper with genuine methodological novelty, rigorous evaluation, and state-of-the-art results. The concerns about fragment merging and torsional flexibility are real but do not invalidate the empirical contribution; they require acknowledgment and discussion rather than methodological revision. The paper matches the quality of the 8.0 anchors in this calibration set.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>
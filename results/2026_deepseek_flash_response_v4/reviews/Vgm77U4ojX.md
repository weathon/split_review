Now let me write the final review with calibrated score.

Let me list all anchor papers:

**Round 1 (Bracketing):**
1. DynamicsDiffusion (3.00) - unrelated topic, much weaker
2. Ligand Conformation Generation (3.00) - weaker, not docking
3. CompassDock (3.00) - docking-focused but lower quality
4. TorSeq (3.00) - conformer generation, weaker
5. GNNAS-Dock (3.00) - docking algorithm selection, weaker
6. Generating Synthetic Genotypes (5.80) - unrelated topic
7. Navigating Design Space (5.75) - design exploration, less novel
8. Diffusion on toric varieties (4.50) - different domain
9. VFDiff (6.00) - similar domain, SIGMADOCK stronger
10. IPDiff (6.25) - similar domain, SIGMADOCK stronger
11. DiffMaSIF (4.67) - protein docking, weaker
12. DiffDock-Pocket (5.00) - extension, weaker
13. Protein Discovery WJS (8.00) - different domain, much stronger
14. FoldFlow (8.00) - protein backbone, much cleaner
15. GeoBFN (8.00) - molecule generation, much cleaner
16. ProtComposer (8.00) - protein design, stronger
17. GeSubNet (8.00) - unrelated topic
18. Generator Matching (8.00) - theory, stronger

**Round 2 (Narrowing):**
19. VFDiff (6.00) - same as above
20. Deep Confident Steps (6.00) - similar domain, slightly weaker
21. Stiefel Flow Matching (7.00) - different domain
22. IPDiff (6.25) - same as above
23. Navigating Design Space (5.75) - same as above
24. DrugFlow (6.67) - drug design, similar quality
25. GroupBind (6.75) - docking, similar quality
26. Bioactivity Prediction (7.00) - different task
27. Structure Language Models (7.00) - protein conformation
28. FABFlex (7.00) - flexible blind docking, comparable quality

**Round 1 bracket:** Between 4.5 and 7.5, confirmed by the fact that SIGMADOCK is clearly much stronger than all <4.5 anchors but clearly weaker than the 8.0 anchors.

**Round 2 narrowing:** SIGMADOCK is stronger than IPDiff (6.25) and Deep Confident Steps (6.00), comparable to GroupBind (6.75) and DrugFlow (6.67), and slightly below FABFlex (7.00) mainly due to the Figure 4/Table 4 presentation issue.

**Final score: 6.5**## Summary

SIGMADOCK introduces a fragment-based SE(3) Riemannian diffusion model for molecular docking. The key idea is to decompose ligands into rigid-body fragments (by breaking rotatable bonds) and generate poses by learning to reassemble these fragments within the binding pocket via diffusion in SE(3)^m space. The paper contributes: (i) a theoretical argument that fragment diffusion avoids entangled non-product induced measures that plague torsional models (Theorem 1), (ii) a practical fragmentation reduction scheme (FR3D) with soft triangulation constraints, (iii) an SO(3)-equivariant architecture, and (iv) strong empirical results—79.9% Top-1 PB-valid on PoseBusters, surpassing prior deep learning methods and competitive with AlphaFold3 while using far less data.

## Strengths

1. **State-of-the-art empirical results with careful experimental design**: SIGMADOCK achieves 79.9% Top-1 (RMSD < 2Å & PB-valid) on the PoseBusters set under the intended train-test split, compared to 38.0% for DiffDock and 58.1% for the next best open-source alternative (Figure 4 left). The paper deliberately restricts training to PDBBind(v2020) alone and calls out unfair comparisons in the literature (Section 3.1, footnote 8), lending credibility to the reported improvements.

2. **Theoretical motivation for fragment-based over torsional diffusion (Theorem 1, Section 2.2.2)**: The paper provides a formal argument that torsional models produce non-product induced measures due to nonlinear torsion-to-Cartesian mappings, whereas fragment-based SE(3)^m diffusion yields a factorised product of Haar measures. This gives a concrete, testable rationale for why fragment diffusion should present a simpler learning task.

3. **FR3D fragmentation reduction with soft triangulation constraints (Section 2.2.3, Table 1)**: The paper introduces FR3D to reduce fragments from k+1 to roughly (2/3)(k+1) by merging adjacent fragments and removing over-constrained dummy atoms, plus triangulation distance conditioning to preserve bond lengths/angles without restricting dihedrals (Lemma 1). Ablations confirm these components contribute 4–12% relative improvement individually.

4. **Co-factor analysis supports genuine learning (Table 2)**: The paper stratifies failures by co-factor presence, showing highest failure rates (41.2%) when natural ligands are present but excluded from the model, and lowest (16.2%) when no co-factors are present—consistent with a model learning physics rather than memorizing training data.

5. **Equivariance and invariance guarantees (Theorem 2, Section 2.4)**: The paper addresses the ambiguity in choosing local coordinate orientations for fragments by adapting a Newton-Euler prediction head, proving the training objective and sampling procedure are invariant to this choice and the score model is SO(3)-equivariant.

## Weaknesses

### Major

1. **Unresolved discrepancy between Figure 4 right and Table 4**: Figure 4 (right) reports per-sequence-similarity Top-1 values of 51% (≤0), 53% (30–95), and 53% (95–100) for SIGMADOCK on the PB set, while Table 4 reports PB-Val values of 72%, 79%, and 87% across the same splits. These differ by 20–34 percentage points. The overall Top-1 (80.5% RMSD-only, 79.9% PB-Val) and the Table 4 per-split PB-Val values are internally consistent with a weighted average of ~79.7%, but the Figure 4 right values (~52.3% weighted average) are not reconciled. The paper's caption and surrounding text do not explain what metric or protocol distinguishes them. Since the generalization claim ("excels on proteins with low sequence similarity") is supported by different numbers in different exhibits, a reader cannot determine which breakdown is authoritative without clarification. *This is not a fatal flaw—the main result (79.9% overall PB-Val) is clearly stated and supported by Table 1—but it creates unnecessary confusion around an important supporting claim.*

### Minor

2. **Classical docking baselines absent from the main comparison table**: The paper's headline claim is that SIGMADOCK is the "first deep learning approach to surpass classical physics-based docking under the PB train-test split," yet the main comparison (Figure 4 left) does not include any classical method. Vina's performance (~57%) appears later in a different context (Table 3, pocket-robustness analysis) but is not presented alongside the deep learning baselines. The data exist in the paper but are not positioned to directly substantiate the central claim.

3. **AF3 comparison lacks full context on task difficulty and subset composition**: Table 4 compares SIGMADOCK to AF3 but shows different per-split counts (e.g., 109 vs. 38 in the [0,30%) bin) without explanation. While the paper acknowledges "we cannot directly compare SIGMADOCK to co-folding methods" (line 256), the comparison is presented prominently and the task-difficulty gap (re-docking with a known holo-receptor vs. co-folding without a fixed receptor) is not discussed. The differing subset sizes also raise questions about which PB subset AF3 could evaluate on.

4. **RDKit conformer dependence as an unexamined limitation**: The model inherits fragment internal geometry entirely from RDKit (ETKDGv3). The paper provides an empirical justification (alignment RMSD ≪ 2Å) and an ablation comparing M_c vs. M_b sampling, but does not analyze whether specific failure cases trace back to poor RDKit conformer quality, particularly for ligands with unusual geometry or macrocycles.

### Trivial

- The abstract's "12.7–32.8%" range for prior deep learning approaches is not directly traceable to entries in Figure 4 (the lowest listed method is PDBBind at 15.9%).

## Nice-to-Haves

- A direct wall-clock inference time comparison (SIGMADOCK vs. DiffDock vs. Vina) would complement the "50× faster than AF3" claim.
- Statistical significance measures (bootstrapped CIs or error bars) for the ablation results in Table 1 would strengthen comparisons where differences are 4–12%.
- The alignment RMSD distribution for the M_c to M_b registration (Section 2.2.1) is described qualitatively; a key statistic (mean/median, fraction below 1Å) in the main text would be informative.

## Removed Points

- Harsh critic's claim that Theorem 1 does not prove ease of optimization: **removed** because the theorem is correctly scoped to the forward kernel and the paper argues (rather than proves) that the product-space structure simplifies learning—a reasonable claim.
- Claim that ablation G is "not a real ablation": **removed** because the paper explicitly frames it as an upper-bound reference (M_b sampling ceiling), not as an ablation in the same sense as A–C.
- Criticisms about missing appendix content or deferred details: **removed** per the rule that the parser strips appendices from all papers.
- Strength Finder's generic strengths about "addressing an important problem": **removed** as generic.
- Harsh critic's point about Theorem 1 and "intuitive but unproven" ease-of-optimization: **removed** as speculative—the paper does not claim Theorem 1 proves ease of optimization.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an observation about the paper that the paper itself does not already articulate.

## Suggestions

1. Clarify the metric behind Figure 4 (right): state explicitly whether it reports Top-1 RMSD-only, Top-1 PB-valid, or some other protocol. Label it consistently with Table 4 to avoid confusion. If it uses a different ranking or sampling condition, say so in the caption.
2. Add Vina (and optionally SMINA) to the main comparison table (Figure 4 left) with a clear note on evaluation conditions to directly substantiate the "surpasses classical docking" claim.
3. Discuss the AF3 comparison more candidly: explain the differing per-split counts and add a paragraph on how the re-docking protocol differs in difficulty from co-folding.
4. Provide a brief analysis of whether RDKit conformer quality correlates with SIGMADOCK failures in the co-factor subsets.
5. Trace the "12.7%" figure in the abstract to a specific cited method or remove it.

---

### Calibration Anchors

**Round 1 (Bracketing) — queries across low (<3.5), middle (3.5–7.5), and high (>7.5) bands.**

*Low band (<3.5):* DynamicsDiffusion (3.00), Ligand Conformation Generation (3.00), CompassDock (3.00), TorSeq (3.00), GNNAS-Dock (3.00), Generating Synthetic Genotypes (5.80 — outlier, unrelated topic). SIGMADOCK is clearly much stronger than all <3.5 anchors.

*Middle band (3.5–7.5):* Navigating Design Space (5.75), Diffusion on toric varieties (4.50), VFDiff (6.00), IPDiff (6.25), DiffMaSIF (4.67), DiffDock-Pocket (5.00). SIGMADOCK is stronger than all of these in method novelty and empirical results.

*High band (>7.5):* Protein Discovery WJS (8.00), FoldFlow (8.00), GeoBFN (8.00), ProtComposer (8.00), Generator Matching (8.00). These are exceptionally clean, field-leading papers; SIGMADOCK is not at this level due to the Figure 4/Table 4 presentation issue.

**Round 1 bracket:** between 4.5 and 7.5.

**Round 2 (Narrowing within bracket):** Deep Confident Steps (6.00), Stiefel Flow Matching (7.00), DrugFlow (6.67), GroupBind (6.75), FABFlex (7.00). SIGMADOCK is stronger than Deep Confident Steps (6.00) and IPDiff (6.25), comparable to GroupBind (6.75) and DrugFlow (6.67), and slightly below FABFlex (7.00) mainly due to presentation clarity.

**Final score:** 6.5 — a strong Accept with a significant presentation issue to resolve.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
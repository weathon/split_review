Now I have a thorough understanding of the paper. Let me synthesize the final review, carefully verifying each claim against the paper text.

## Summary

The paper proposes learning equivariant scalar fields for proteins and ligands whose cross-correlation defines a scoring function, enabling FFT-based optimization over rigid-body degrees of freedom (translation and rotation). The scalar fields are parameterized by E3NN-based equivariant scalar field networks (ESFs), and the training uses conditional log-likelihoods whose marginal integrals are tractable via FFTs. The method is evaluated on decoy pose scoring and rigid conformer docking, showing competitive accuracy with faster runtime, particularly when amortized across many ligands against a common pocket (up to ~45× speedup on PDE10A).

## Strengths

1. **First learned scoring function compatible with FFT-based pose optimization**: The paper is the first to *learn* scalar fields whose cross-correlation defines the docking score, enabling FFT-based evaluation over both translation (ℝ³) and rotation (SO(3)). This is a genuine departure from prior work — previous FFT docking methods used hand-crafted potentials, and the paper explicitly notes that "no prior works have explored the possibility of overcoming this limitation by *learning* cross-correlation based scoring functions" (Sec. 2, last paragraph). The equivariance properties (Proposition 1) provide theoretical grounding.

2. **Demonstrated runtime advantage with amortization**: On the PDE10A dataset (77 ligands docked to a common pocket), the RF workflow achieves a ~45× speedup in total inference time (67 s → 1.5 s, Sec. 4.2) relative to non-amortized execution, while maintaining competitive accuracy (Table 3). Per-pose FFT evaluation takes 160 μs (translational) or 650 μs (rotational) as reported in Table 1. The paper provides a clear breakdown of what can be amortized at each level (protein-level, ligand-level, pose-level).

3. **Robustness on predicted protein structures**: On ESMFold structures (Table 2), ESF/ESF-N methods achieve substantially higher top-ranked pose success (47–57% for TS mode) compared to Vina (24–43%) and Gnina (28–46%), with much lower median RMSD (1.38–1.75 Å vs 2.19–6.1 Å). This is a meaningful improvement because traditional scoring functions rely on sidechain atoms that are poorly predicted by ESMFold, while the scalar fields depend on residue-level coefficients (Sec. 4.1).

4. **Complete and modular inference framework**: The paper defines four inference modes (TF, RF, TS, RS) and explicitly characterizes their computational costs and amortization opportunities in Table 1. The analysis of what must be computed per-protein, per-conformer, per-rotation, and per-pose provides readers with a concrete understanding of when each mode is advantageous.

## Weaknesses

### Fatal

None.

### Major

None. The paper's core claims — that a learned cross-correlation scoring function can be optimized via FFTs and achieves competitive accuracy on simplified tasks with runtime benefits under amortization — are supported by the evidence. The weaknesses below are real but addressable.

### Minor

1. **Training objective is heuristic without ablation or theoretical justification**: The paper optimizes the sum of two conditional log-likelihoods (translation given rotation, rotation given translation) and acknowledges that "neither technically corresponds to the joint log-likelihood" (Sec. 3.4). While following DiffDock's approach provides some precedent, no ablation compares this objective to alternatives (e.g., direct score maximization, contrastive loss, or the full joint likelihood approximated via sampling). Without such analysis, it is unclear whether the specific FFT-tractable formulation is necessary for good performance or whether a simpler loss would suffice, which weakens the methodological contribution.

2. **Unquantified approximation error in the rotational FFT**: The conversion from local to global spherical harmonic coefficients (Eq. 12) is a least-squares projection onto a truncated basis, introducing an uncontrolled approximation. The experimental results confirm that RS mode systematically underperforms TS mode (e.g., Top RMSD 0.63 vs 0.59 on crystal structures, Table 2), attributed to "spatially coarser representation." However, the paper does not measure the projection error or show that it converges with more basis functions, making it difficult to assess whether the rotational FFT is a reliable optimization method or only useful with the Cartesian fallback.

3. **Abstract claims "50x speedup" while experiments report ~45×**: The abstract states "our method obtains a 50x speedup in total inference time at no loss of accuracy" (line 21), but the experimental section reports "a 45x speedup in the overall runtime (67 s → 1.5 s)" (line 234). 67/1.5 ≈ 44.7×, not 50×. While this is a small numerical discrepancy, it appears in the abstract's headline claim and should be corrected for accuracy.

4. **No error bars or uncertainty estimates**: All metrics are reported as medians over test complexes without any variance or confidence intervals. For datasets of 77 (PDE10A) or ~360 (PDBBind) complexes, small differences (e.g., 73% vs 74% success rate) may not be statistically significant. This limits the reader's ability to judge which differences are meaningful.

5. **The method's practical scope is narrower than the framing suggests**: The paper's title ("Molecular Docking") and introduction ("accelerating... ligand poses for high-throughput molecular docking") frame the work broadly, yet the evaluation is limited to rigid conformer docking with ground-truth conformers provided. The paper is transparent about this simplification, stating "we consider two simplified settings" (Sec. 4), but the broader framing risks misleading readers about the method's current capabilities. A dedicated limitations paragraph or clearer scope statement early in the paper would improve transparency.

6. **TANKBind adaptation produces a weak baseline**: The adaptation of TANKBind — using L_generation with ground-truth distances as a score — is ad-hoc and yields poor results (AUROC 0.69 on crystal structures, Table 2). Including such a baseline does not strengthen the paper's case, as the poor performance likely reflects an unfaithful adaptation rather than any real limitation of TANKBind. The paper acknowledges this is an adaptation, but should more explicitly note that this comparison is not informative.

### Trivial

- The decoy generation description has a truncated sentence ("1.6% of all poses ($n=526") that appears to be a parser artifact — this should be clarified.
- Grid resolution and numerical discretization parameters for the FFT procedure are not reported, which affects reproducibility.

## Nice-to-Haves

- **Ablation of the training objective**: Comparing the conditional log-likelihood sum to alternatives (e.g., a contrastive loss or direct score maximization with negative sampling) would demonstrate whether the FFT-based tractability is actually critical or whether a simpler approach works as well.
- **Quantification of the projection error**: Reporting reconstruction error of the local-to-global basis projection (e.g., relative Frobenius norm) as a function of global basis size would allow readers to assess the trade-off between speed and accuracy in the RS mode.
- **Path to flexible ligand docking**: The paper mentions conformer flexibility as future work. A brief discussion or preliminary experiment (e.g., using a small set of pre-generated conformers) would strengthen the claim that this method can be integrated into a full docking pipeline.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Evaluation assumes known ligand conformers (structural flaw)"** — The paper explicitly states it evaluates on "rigid conformer docking" and "simplified docking-related tasks" (abstract, Sec. 4). All baselines (Vina, Gnina) receive the same conformer with torsions deactivated (line 228), making the comparison fair. The paper is transparent about this scope. The strength of this criticism is downgraded: what the reviewer frames as a structural flaw is better characterized as a scope limitation that is clearly disclosed. Moved to Minor (item 5 above) with reduced severity.
- **"Decoy generation description is unclear (broken sentence)"** — The line about "1.6% of all poses ($n=526" is a PDF parser artifact. The original submission almost certainly has the full sentence. Removed per formatting artifact rule.
- **"Missing appendix/proofs"** — The parser strips these sections; they exist in the original submission. Removed.
- **"Weaknesses about reproducibility (hyperparameters, training logs)"** — The paper provides sufficient architectural and training details for a methods paper. Removed per hard rules about trivial reproducibility nitpicks.
- **"FFT methods have been less studied for protein-ligand docking" (reviewer notes this as a strength but also as a counterpoint)** — The Strength Finder correctly identifies this as supporting the novelty claim. No conflict.
- **Strength Finder item 4 (tractable training objective)** — While partially correct, the paper itself acknowledges the objective is not the joint log-likelihood. The strength is retained in Strengths above but the associated weakness (#1) is also listed.
- **Various generic strength finder filler statements** were filtered (generic statements lacking specific substance or citation).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Correct the numerical discrepancy in the abstract (50× → ~45× or provide the correct computation).
2. Add an ablation comparing the conditional log-likelihood training objective to a simpler alternative (e.g., contrastive loss with random/perturbed poses) to demonstrate whether the FFT-based tractability is essential.
3. Quantify the least-squares projection error for the rotational FFT (Eq. 12) as a function of global basis size, to establish when the RS mode is trustworthy.
4. Add confidence intervals (e.g., bootstrap estimates) to the main result tables, especially for metrics where differences between methods are small.
5. Add a brief "Limitations" paragraph or earlier scope clarification, clearly stating that the method currently handles only rigid-body docking of given conformers and that conformer search is left to future work.
6. Report the grid resolution / discretization parameters used for the FFT so that results are reproducible.

## Score and Decision

The paper presents a genuinely novel approach — the first learned scoring function expressible as a cross-correlation of scalar fields and optimizable via FFTs. The technical formulation is sound, the runtime analysis is insightful, and the robustness on predicted structures is practically relevant. The experimental evaluation is on simplified tasks that are clearly scoped, and the weaknesses (heuristic training objective without ablation, unquantified projection error, missing confidence intervals) are real but addressable in revision. The contribution is a solid step forward for the ML-for-docking community.

I rate this paper as **strong accept with minor revisions**. The novelty and technical contribution are clear; the weaknesses are minor and do not undermine the core claims.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
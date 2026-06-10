## Summary

This paper proposes GroupBind, a paradigm shift in molecular docking where multiple ligands known to bind the same protein pocket are docked simultaneously rather than independently. Built on top of DiffDock, the method adds message passing across group ligands and a triangle attention module enforcing cross-ligand interaction consistency with the protein. The core biochemical motivation—that ligands binding the same pocket adopt similar poses—is well-grounded, and the paper demonstrates that this group-aware approach improves docking accuracy on the PDBBind benchmark.

## Strengths

- **Genuinely novel paradigm with clear biochemical motivation.** The paper introduces the first end-to-end deep learning approach that simultaneously docks multiple ligands to a protein pocket, grounded in the well-established observation that ligands binding the same pocket adopt similar poses (Section 1, Figure 1). This is a meaningful departure from the independent-pair paradigm that dominates prior work.

- **Triangle attention with a distinct cross-ligand consistency motivation.** While triangle attention appears in prior docking work (TANKBind, E3Bind), this paper's version operates across *different ligands* with a fundamentally different motivation: "if atom *j* in ligand *L<sub>g</sub>* can interact with amino acid *i*, then the corresponding atom *k* in a similar ligand *L<sub>g′</sub>* should also interact with amino acid *i*" (Section 3.3, Eq. 4-5). This directly encodes the paper's biochemical insight into the architecture, which is a clear architectural innovation.

- **Parameter-efficient design.** GroupBind uses 18.8M parameters versus DiffDock's 20.3M, achieved by reducing interaction layers from six to five (Section 3.4). This shows the performance gains come from architectural design, not from substantially more capacity.

- **Non-trivial finding that dissimilar ligands are more informative.** Section 4.3 reports a Spearman correlation of -0.39 between group Tanimoto similarity and best docking RMSD—structurally *dissimilar* ligands binding to the same pocket provide more useful information. This goes beyond a trivial "more data helps" story and provides actionable guidance for ligand selection in practice.

- **Extension to novel proteins via homologous ligands.** Section 4.5 shows that ligands from homologous proteins (identified by FoldSeek) can serve as augmented inputs when no ligands are known for the target, addressing a key practical limitation.

## Weaknesses

### Fatal

None.

### Major

- **The SOTA claim conflates architectural improvement with informational advantage, and the most controlled comparison is not foregrounded.** The paper announces "new state-of-the-art performance on the PDBBind blind docking benchmark" (abstract, Section 4.2). However, the highlighted results (47.4% and 48.8% RMSD<2Å, Section 4.2, lines 161) come from the self-augment (S) and training-augment (A) variants that receive *additional ligands known to bind the same protein* during inference—information that none of the baselines have access to. The paper's claim that "GROUPBIND-P2RANK, the models in the full blind docking setting and thus fair to other baselines" uses "fair" only in the sense of pocket prediction method (P2Rank vs. native pocket), not in the sense of informational parity. The N(G) variant (no augmented ligands, defined in Section 4.1) would provide an apples-to-apples comparison isolating the architectural improvements, but its results are not discussed in the main text or compared directly against DiffDock. Without this controlled comparison, a reader cannot tell whether the claimed gains come from the architecture itself or from the auxiliary group data. This is a framing issue that cuts to the paper's central claim.

### Minor

- **Within-test-set self-augmentation breaks evaluation independence.** The S variant uses 255 of the 363 test ligands, grouped into 86 groups, to augment each other during inference (Section 4.1). Predictions for different test instances are thus coupled: a ligand in a large group gets more augmentation than one in a small group or alone. While the A(G) variant (using training-set ligands) partially addresses this, the S variant is presented as a main result without acknowledging this coupling. The evaluation cannot be directly compared to methods evaluated one pair at a time.

- **No variance/confidence intervals reported.** The diffusion model's sampling is stochastic and the confidence model adds randomness, yet no standard deviations, multiple-seed results, or confidence intervals are provided. This is a notable gap for a method whose core evaluation is on a relatively small test set (363 complexes).

- **The ablation study uses a different experimental setup from the main results.** The ablation (Section 4.4) uses a smaller network, 10 samples, and perfect selection (isolating the confidence model). While still informative, the results cannot be quantitatively connected to the main Table 1 results, which use a full network, 40 samples, and the confidence model for ranking.

- **Methodological details are underspecified in places.** (a) The protein alignment filtering criterion ("complexes with protein-ligand minimum distances that are either too close or too far," Section 3.3) is not quantified. (b) The initialization of the pair representations z<sub>ij</sub> and g<sub>jk</sub> for the triangle attention is not specified. (c) The FoldSeek experiment (Section 4.5) does not report how many of the 76 "orphan" test proteins are covered, or the performance on those that remain uncovered.

### Trivial

- "Group Ligands Docking" in the title is slightly ungrammatical ("Group Ligand Docking" or "Group-Wise Ligand Docking" would read better).
- Figure 3 reference in line 157 says "two examples (UniProt ID: P03211, Q9H7Z6)" followed by reference to three ligands for Q9H7Z6—verify the figure matches the description.

## Nice-to-Haves

- Report computational cost (wall-clock time, GPU memory) vs. DiffDock, since the paper acknowledges the triangle attention is expensive (Section 5).
- Define group-level evaluation metrics alongside per-ligand metrics (e.g., fraction of groups where all ligands are predicted correctly).
- Quantify practical coverage: how many targets in PDBBind and databases like ChEMBL have multiple known binders? The paper reports 76/363 test proteins lack binders *in PDBBind*, but this gives only a lower bound.

## Removed Points

Points flagged for removal are treated with caution; they are included here in case useful:

- *"Tables are presented as images, making it impossible to verify exact numbers"* — Removed: this is a PDF-extraction artifact; the original submission contains proper tables.
- *"47.4% and 48.8% RMSD < 2Å are not attributable to a specific comparison setting"* — Removed: the paper clearly specifies that these are the S (self-augment) and A (training-augment) variants at Top-5 (Section 4.1, 4.2).
- *"Missing related works"* — Removed: cannot confirm existence of omitted references without external sources.
- *"Missing appendix content / proofs deferred to appendix"* — Removed: the parser strips appendix sections from all papers.
- *Formatting nitpicks, typos, grammar issues, garbled text* — Removed: parser artifacts, not author errors.
- *"Could the metric be measuring a proxy?" / "Are confounders controlled?"* — Removed: these are area-of-concern speculations without concrete anchors in the paper.
- *Strengths that are generic ("addressed an important problem")* — Removed: not specific to this paper's evidence.
- *Criticism about DiffDock baseline variance* — This was kept as a Minor weakness (variance reporting), not removed.

## Novel Insights

The review process surfaces two observations beyond the paper's own contributions. First, the negative correlation between inter-ligand similarity and docking accuracy (-0.39 Spearman, Section 4.3) is genuinely striking and under-explained by the authors: why do *dissimilar* ligands help more? If this holds generally, it suggests the model is learning something like a functional definition of the binding pocket's interaction constraints rather than relying on ligand-template matching, which would be a deeper contribution than the paper articulates. Second, the paper's framing tension—presenting a new paradigm while evaluating it on an old benchmark designed for a different paradigm—is a recurring pattern in ML-for-drug-discovery papers. The typical resolution (claiming SOTA on the old benchmark) papers over a genuine methodological question: how should we evaluate methods that change the problem setup? The paper would benefit from engaging this question directly rather than finessing it.

## Suggestions

1. **Foreground the N(G) comparison.** Present GroupBind without any augmented ligands vs. DiffDock as a controlled comparison. If the architecture alone (message passing + triangle attention, no extra data) already beats DiffDock, that is the cleanest evidence for the architectural contribution. If it does not, the paper should say so plainly and the "SOTA" claim should be restructured accordingly.

2. **Reframe the augmented-ligand results as a new evaluation paradigm.** Rather than claiming SOTA on the standard benchmark, explicitly propose "multi-ligand docking with group information available" as a distinct setting. Define which baselines are comparable under which conditions, report coverage statistics, and make the task definition self-consistent.

3. **Report variance.** Provide standard deviations or multiple-seed results for the main table, given the stochastic sampling procedure.

4. **Clarify the "fair" claim.** When saying P2R variants are "fair to other baselines" (Section 4.2), explain that "fair" refers only to pocket prediction method, not to the informational advantage of augmented ligands.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Reject</decision>
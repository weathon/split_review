Here is my synthesized final review.

## Summary

This paper identifies a critical bias in bioactivity prediction benchmarks: models can exploit pocket-level label distributions rather than learning genuine ligand-target interactions. To address this, the authors introduce SIU, a million-scale dataset of docked small molecule-protein complexes (>5M conformations, >1.3M labels, 50× larger than PDBbind) organized with multiple ligands per pocket and separated by label type (IC₅₀, Kᵢ, K_d, EC₅₀). They also propose per-pocket evaluation metrics (Pearson/Spearman computed within each pocket and averaged) that remove the pocket-level shortcut. Experiments show that the redefined metrics are substantially more challenging and that models trained on SIU outperform those trained on PDBbind on SIU's test set.

## Strengths

- **Well-motivated problem diagnosis with a clean diagnostic experiment.** The pocket-only baseline (Figure 1) convincingly demonstrates that a model ignoring the ligand entirely achieves comparable or better performance than full-complex models on Atom3D LBA. This diagnosis reveals a genuine and underappreciated flaw in existing benchmarks. The clustering of predictions around the per-target mean (Figure 1C) further pinpoints the mechanism.

- **Large-scale dataset with deliberate structural design.** SIU provides 5.34M conformations and 1.38M bioactivity labels across 1,720 targets and 214K small molecules—dramatically larger than PDBbind. The multi-software docking pipeline (Vina, Glide, GOLD) with majority-vote consensus (RMSD ≤ 2 Å) is a principled approach to pose quality control. The separation of labels by measurement type (Kᵢ vs IC₅₀ vs EC₅₀ vs K_d) is a meaningful organizational improvement over datasets that mix them.

- **Per-pocket evaluation metrics that directly address the identified bias.** The redefined Pearson/Spearman correlations (computed within each pocket and mean-pooled) logically cannot be gamed by pocket-only information, since a pocket-only model would produce near-constant predictions per pocket, driving within-pocket correlation toward NaN/zero. The observed drop in correlation (e.g., Kᵢ Pearson from 0.485 to 0.036, Figure 5A) confirms the metrics are substantially more challenging and better isolate ligand-level discrimination ability.

- **Inclusion of experimentally validated inactive molecules and diverse protein classes.** SIU provides negative data (low-activity/inactive compounds) that are largely absent from PDBbind, increasing relevance for virtual screening. Coverage across major protein classes and 1,720 distinct targets supports broader generalization claims.

## Weaknesses

### Fatal
None.

### Major

- **No validation on independent experimental structural data.** The paper evaluates SIU-trained models exclusively on SIU's own test set—data generated through the same docking pipeline that produced the training data. There is no experiment testing whether SIU-trained models generalize to experimental structural complexes (e.g., the PDBbind refined set or CASF benchmark). Without this, it is unclear whether training on docked poses at scale improves prediction on the experimental structures that matter in real drug discovery, or whether models simply learn the distribution of docking software artifacts. This is the most significant gap in supporting the claim that SIU enables "truly beneficial for drug discovery" (conclusion).

- **PDBbind vs. SIU comparison is confounded by test distribution mismatch.** Table 2 and the surrounding text claim SIU-trained models "outperform those trained on PDBbind." However, the comparison evaluates a model trained on experimental structures (PDBbind) on the SIU test set (docked poses). This introduces a domain mismatch that systematically disadvantages the PDBbind-trained model. While the paper notes that PDBbind data was used without homology filtering (which leaks similarity to the test set and partially offsets this), the net bias is unclear and the comparison is not apples-to-apples. An evaluation on a common benchmark with experimental structures (e.g., CASF or PDBbind's own test split) is needed to substantiate the claimed superiority.

- **Pocket-only baseline not empirically demonstrated on SIU.** The paper argues (Section 4.2) that the per-pocket metric "cannot be overfitted with pocket only information, as it will result in similar prediction results for different molecules, which would lead to NaN." This is logically sound but no experiment on SIU data confirms it. Running a pocket-only baseline on SIU under both standard and per-pocket metrics would directly and convincingly demonstrate that the redefined task removes the spurious shortcut. This is a straightforward experiment that the paper's own narrative calls for but does not execute.

### Minor

- **Key results lack error bars or confidence intervals.** Tables 1 and 2 report single numbers without variance. While the dataset is large, the number of independent runs, random seeds, and any hyperparameter selection procedure should be stated. Without this, it is impossible to assess whether observed differences (e.g., between SIU 0.6 and SIU 0.9) are statistically significant.

- **Docking reproducibility is underspecified.** The paper names three docking programs (Vina, Glide, GOLD) but does not state their versions, charge models, grid box parameters, or any non-default settings. These details are essential for a dataset whose core value proposition depends on structural reliability.

- **Reference error: "Table 10" does not appear in the paper.** Line 140 refers to "Table 10 and Figure 5" — no Table 10 exists. This appears to be an internal reference error (likely should point to Table 2). This undermines traceability of the central experimental claim.

- **Deduplication thresholds are stated but not justified.** The Tanimoto 0.8 cutoff and 90th-percentile threshold for per-target deduplication are given without analysis of how they affect dataset diversity or model performance. These choices could introduce systematic bias in the molecular and target coverage.

- **Single-target experiments (Table 2) only evaluate Uni-Mol.** The multi-task setting (Table 1) covers all four models, but the single-target setting—which directly supports the PDBbind comparison—uses only Uni-Mol. Testing additional models (3D-CNN, GNN, ProFSA) in this setting would strengthen the evidence.

### Trivial

- The phrase "Table 10" is a clear internal reference error (should likely be Table 2).
- The stray "3)" at line 106 and ".1" at line 140 appear to be remnants of removed footnote markers (parser artifacts, but should be cleaned in revision).

## Nice-to-Haves

- A quantitative comparison table positioning SIU relative to Papyrus (size, label types, structural validation) would help readers understand SIU's place among existing resources.
- Reporting the number of molecules per pocket distribution (mean, median, range) would clarify how many pockets actually enable the per-pocket evaluation the paper depends on.
- A discussion of limitations section explicitly acknowledging that SIU uses docked (not experimental) poses and the potential impact of docking errors on training and evaluation would improve transparency.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"r* vs r_star notation inconsistency":** The paper uses `r^{\star}` in equations and `Pearson∗` in the table caption. Both use the same star symbol; any apparent discrepancy is a rendering artifact. Removed as a formatting nitpick.
- **"Parser artifact '3)'":** The critic noted this but acknowledged it as a probable parser issue. Per rules, parser artifacts are not author errors.
- **"Missing related work on Papyrus":** The paper cites Papyrus. The critic's demand for a quantitative comparison table is a Nice-to-Have, not a weakness — the paper is not required to exhaustively compare to every related resource.
- **"Generic strengths from Strength Finder":** The claim that "training on SIU improves model generalization" (Strength Finder point 4) is weakened by the test-set domain mismatch concern identified above. It is retained in the Weaknesses section rather than listed as an unqualified strength.

## Novel Insights

The review process surfaces one insight beyond the paper's own contributions: the paper's central methodological tension — that a large, docked dataset with per-pocket metrics is proposed to solve a bias problem diagnosed on a small, experimental dataset — creates a fundamental validation gap. The pocket-only diagnosis (Figure 1) is conducted on experimental structures (Atom3D LBA derived from PDBbind), yet the proposed solution (SIU) replaces experimental structures with docked poses. This means the paper is not validating that its solution generalizes to the same type of data on which the problem was diagnosed. Addressing this asymmetry — e.g., by showing that the per-pocket metrics also reveal pocket-only shortcut behavior when applied to experimental-structure datasets that happen to have multiple ligands per pocket — would substantially strengthen the narrative coherence.

## Suggestions

1. **Validate on experimental structures.** Train models on SIU and evaluate them on the PDBbind refined set or CASF benchmark, comparing against models trained on PDBbind. This is the single most important addition to substantiate the claim that SIU improves real-world bioactivity prediction.

2. **Run the pocket-only baseline on SIU** under both standard and per-pocket metrics to empirically confirm that the redefined metrics eliminate the shortcut. This is a low-cost experiment that directly supports the paper's central methodological claim.

3. **Report variance statistics** (at least 3 random seeds) for all main results in Tables 1 and 2.

4. **Clarify the test set used for the PDBbind vs. SIU comparison** (Table 2) and add a discussion of the domain mismatch between experimental and docked structures as a limitation.

5. **Provide docking software versions and key parameters** in the paper or supplementary material.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
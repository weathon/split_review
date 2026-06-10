Now I have all the information I need. Let me write the final review.

## Summary

The paper identifies a critical flaw in existing bioactivity prediction benchmarks—models can cheat by learning pocket-level bioactivity ranges rather than genuine molecule-protein interactions (the "pocket-only shortcut"). To address this, the paper introduces SIU, a million-scale dataset (5.34M conformations, 1.38M bioactivity labels, ~50× larger than PDBbind) with multiple small molecules per protein pocket, and proposes within-pocket correlation metrics (Pearson*, Spearman*) that prevent the shortcut. The problem diagnosis is convincing and timely; the proposed evaluation framework is logically sound. However, the experimental validation has significant gaps: (1) the structural complexes are entirely docking-generated, not experimentally determined, which constrains what conclusions can be drawn, (2) the headline comparison showing SIU-trained models outperform PDBbind-trained models is confounded by asymmetric preprocessing, and (3) the paper never empirically demonstrates that its proposed metrics actually eliminate the pocket-only vulnerability it diagnoses.

## Strengths

- **Pocket-only baseline cleanly exposes the shortcut.** Figure 1(A)(B) experimentally demonstrates that a Uni-Mol model receiving only pocket (protein) information—no small molecule input—achieves comparable or superior performance to full-complex models on the Atom3D LBA benchmark. This is a clean, reproducible diagnostic that prior work had not explicitly shown.

- **Within-pocket evaluation metrics directly address the identified confound.** The redefined Pearson* and Spearman* correlations (Section 3.3, Eq. 1–3) compute correlation within each protein pocket and mean-pool across pockets. The paper reports a dramatic drop from 0.485 to 0.036 (Pearson for Ki) when switching to the grouped metric (line 30), which validates that standard metrics overestimate models' true molecule-discrimination ability.

- **Dataset scale and multi-software quality control are genuine contributions.** At 5.34M conformations and 1.38M labels, SIU is substantially larger than existing resources like PDBbind. The use of three docking programs (Glide, GOLD, Vina) with consensus voting (≥2 of 3 agreement at 2Å RMSD cutoff) is a reasonable quality-control strategy, and the validation on redocked co-crystal poses (Figure 3A) provides evidence that the pipeline preserves known binding modes.

- **Separation of bioactivity label types with statistical justification.** The paper separates Kd, Ki, IC50, and EC50 rather than conflating them, and provides pairwise t-test evidence that these distributions differ (Figure 4A/B). This is a methodological improvement over prior practice.

- **Inclusion of experimentally validated inactive molecules.** The dataset contains low-bioactivity/inactive molecules (line 69–70), a category systematically absent from PDBbind-derived benchmarks, which is valuable for virtual screening tasks.

## Weaknesses

### Fatal

None.

### Major

- **The SIU vs. PDBbind comparison is confounded by asymmetric preprocessing.** The paper reports that models trained on SIU outperform those trained on PDBbind (Section 4.2, line 140). However, the PDBbind data were used "in its entirety, without implementing any filtering techniques to exclude pockets similar to those in the test set," while SIU 0.6 and 0.9 versions do include homology filtering. This means the comparison conflates dataset size/diversity with the presence/absence of test-set leakage. It is impossible to tell whether SIU's advantage comes from its larger scale or simply from removing test-set-similar training pockets. Applying the same filtering to PDBbind or providing an unfiltered SIU comparison as a control is necessary to support the comparative claim.

- **The central claim—that the new task eliminates the pocket-only shortcut—is not empirically validated.** The paper argues theoretically (line 138) that within-pocket metrics will yield NaN for pocket-only models because predictions would be constant across molecules in the same pocket. But it never actually runs the experiment: train a pocket-only model on SIU data and evaluate it under the new metrics to confirm it fails while a full-complex model succeeds. This experiment (e.g., Uni-Mol pocket-only vs. full-complex on SIU, evaluated with within-pocket Pearson/Spearman) is the single most important diagnostic the paper could provide to close the loop on its claimed contribution. Without it, the paper demonstrates a problem and proposes a solution, but never shows the solution working.

- **All structural complexes in SIU are docking-generated, not experimentally determined.** While the paper is transparent about its docking pipeline (lines 59–63), this is a fundamental constraint on what the dataset enables. The bioactivity labels are from wet experiments, but the 3D poses that models consume as input are computationally simulated and filtered by consensus. Models trained on SIU may learn systematic biases or artifacts of the docking software (Vina, Glide, GOLD) rather than generalizable binding physics. The validation in Figure 3A only checks whether the docking pipeline reproduces co-crystal poses for molecules where experimental poses exist; it does not validate the poses for the majority of SIU molecules (which were selected precisely because they lack co-crystal structures). The paper should discuss this limitation explicitly—currently there is no limitations section—and calibrate its claims accordingly.

### Minor

- **No measure of uncertainty reported for any experimental result.** All reported correlations (Tables 1, 2, Figure 5) are point estimates without variance, confidence intervals, or significance tests. Given that within-pocket correlations can be noisy, especially when averaged over pockets with few molecules, error bars or bootstrap estimates are necessary to assess whether reported differences (e.g., 0.485 → 0.036) are reliable.

- **The paper attributes the pocket-only shortcut entirely to data insufficiency** (too few molecules per pocket in PDBbind) without acknowledging architectural priors as a potential contributing factor. An alternative explanation is that the tested models (GNN, Uni-Mol) are simply poor at incorporating ligand information given their design—a model with different inductive biases might succeed even on PDBbind-sized data. This should be acknowledged.

- **The fraction of molecules discarded by the consensus voting filter is not reported for the full dataset.** Figure 3A reports the "remaining ratio" for a validation set of redocked co-crystal poses, but the proportion of molecules from the full pipeline that fail the ≥2-of-3 agreement filter is not stated. This is needed to assess potential selection bias.

- **No limitations section.** The paper has no discussion of what SIU cannot do, the docking-based nature of its structural data, or the risk that models learn docking software biases. At minimum, these should be addressed.

### Trivial

- Minor phrasing issue: the paper uses "redefining the task" in the title, which oversells the scope—the paper redefines the *evaluation* of the task and provides a better dataset, but the prediction problem itself (regression from complex structure to bioactivity) is unchanged.

## Nice-to-Haves

- Specify a minimum number of molecules per pocket for reliable within-pocket correlation estimation, as pockets with very few (e.g., 2–3) molecules will produce noisy estimates.
- Discuss the trade-off of separating label types: splitting by label type reduces per-type training set size; a brief analysis of whether multi-task learning (Table 1) compensates for this would be helpful.
- Clarify exactly how the pocket center is defined for the docking procedure when the molecule being docked is not itself co-crystallized—the paper states the pocket is defined by a 15Å radius around the co-crystal ligand (line 54), but the docking configuration step needs more detail.

## Removed Points

These points were removed from the main review with brief justification:

- **"Results embedded as images, impossible to verify"** — This is a parser artifact from PDF extraction; the original submission likely had proper tables. Removed per Hard Rules (formatting artifacts are parser errors, not author errors).
- **"Demand that paper discuss specific alternative datasets like Papyrus in more detail"** — The paper already cites Papyrus (line 33). Demanding more discussion is scope creep for a paper already presenting its own dataset.
- **"The paper claims 'high-quality' but this is misleading"** — The paper explicitly describes the docking pipeline and uses "high-quality" to refer to the multi-software consensus process, not to claim experimental quality. The docking limitation is retained as a Major weakness above, but the characterization as "misleading" is too strong.
- **Strength: "Empirical demonstration that scale improves performance despite harder evaluation"** — This strength is retained in weakened form in the Strengths section. The strength as stated in the Strength Finder overstated it by not noting the asymmetric comparison confound.
- **Strength: "This paper addressed an important problem"** — Generic, removed per filtering discipline.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel observation that the paper itself misses.

## Suggestions

1. Run the pocket-only diagnostic on SIU: train a Uni-Mol pocket-only model on SIU data, evaluate it with within-pocket Pearson*, and compare to a full-complex model. This single experiment would empirically close the loop on the paper's central claim.

2. Address the PDBbind comparison confound: either apply the same homology filtering to PDBbind, or report results on an unfiltered SIU version as a control, so the reader can separate the effect of data scale from the effect of filtering.

3. Add a limitations section discussing: (a) the docking-based nature of the structural data, (b) the risk that models learn docking software biases, (c) the potential for selection bias from the consensus filter, and (d) the fact that the posed molecules lack co-crystal validation for the majority of SIU entries.

4. Add confidence intervals or bootstrap error bars to all reported correlations, particularly the within-pocket metrics.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
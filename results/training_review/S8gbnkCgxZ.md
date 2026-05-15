Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper identifies a genuine and important problem in machine learning for bioactivity prediction: existing datasets (derived from PDBbind) typically contain only one or very few ligands per protein pocket, which allows models to rely on pocket-level features rather than learning ligand-specific interactions. The authors construct SIU, a large-scale dataset of ~1.38M bioactivity labels across 214K molecules and 1,720 targets (50× larger than PDBbind), with computational 3D structures generated via consensus docking and bioactivity labels organized by assay type (Kd, Ki, IC50, EC50). They also propose within-pocket evaluation metrics (Pearson*, Spearman*) that measure a model's ability to rank different ligands binding to the same pocket rather than across pockets.

## Strengths

1. **Problem diagnosis is genuinely insightful.** The observation that current benchmarks can be "solved" by a pocket-only model that ignores the ligand entirely (Figure 1A-B on Atom3D LBA) is a real and well-demonstrated finding. It convincingly shows that existing evaluation protocols overestimate model capability for within-pocket ligand discrimination.

2. **SIU is a large-scale, well-organized resource.** At 1.38M labels, 214K molecules, and 1,720 targets, SIU is substantially larger than PDBbind (~20K complexes). The systematic separation by label type (Kd, Ki, IC50, EC50) directly addresses the common but problematic practice of mixing different assay types. The inclusion of experimentally validated inactive molecules and multiple pockets per target adds practical value for drug discovery.

3. **Within-pocket evaluation metrics are conceptually well-motivated.** The shift from cross-pocket to within-pocket correlation (Pearson*, Spearman*) directly targets the practical use case of virtual screening — ranking different molecules against the same target. This is arguably the paper's most original contribution.

## Weaknesses

### Fatal
None.

### Major

1. **The cross-dataset comparison (SIU vs. PDBbind) does not specify the test set, making the headline result hard to interpret.** Section 4.2 states "We compare models trained on the PDBbind 2020 dataset with those trained on SIU versions 0.6 and 0.9" (line 140) and reports results in Table 2 (referenced as Table 10 in the text). The test set on which these comparisons are evaluated is never explicitly stated. If the SIU test set is used, then PDBbind-trained models are being evaluated on a distribution they were never exposed to, while SIU-trained models benefit from training on data from the same distribution. This does not invalidate the result but makes it impossible to interpret properly. The paper must specify the test set, the splitting methodology, and ideally evaluate both sets of models on a shared, independent benchmark (e.g., CASF-2016 or an Atom3D holdout set).

2. **The within-pocket Pearson drop is confounded by range restriction, and this is not discussed.** When bioactivity values within a single pocket have low variance, Pearson correlation mechanically decreases even for a well-calibrated predictor, because the correlation coefficient is normalized by overall variance (Figure 5, Table 2). The paper interprets the dramatic drop (e.g., Ki Pearson from 0.485 to 0.036) as evidence that "the new task is more challenging," but does not control for range restriction. Without reporting within-pocket variances, comparing to a null/random baseline, or binning pockets by variance, this claim is not fully supported. The metric is still more meaningful for drug discovery, but the magnitude of the drop conflates task difficulty with a statistical artifact.

3. **The "spurious features" diagnosis of pocket-only models is overclaimed.** The paper argues that pocket-only models achieving comparable performance to full-complex models (Figure 1A-B) demonstrates reliance on "shortcuts" or "spurious features." An equally plausible explanation is that pocket-level features (volume, hydrophobicity, electrostatics) contain genuine predictive signal for coarse bioactivity discrimination across different proteins. The paper does not control for this (e.g., by shuffling ligand labels while keeping pocket structure) before concluding that the model found a "shortcut." This framing is unnecessary for the paper's main argument — the problem of insufficient per-pocket ligand diversity and cross-pocket evaluation is well-motivated even without proving the shortcut hypothesis.

### Minor

1. **Computational docking vs. experimental structures is not sufficiently caveated.** The paper uses phrases like "high-quality structural data" (line 25) and "reliable interaction complex structures" (line 25) that could be read as implying experimental validation. While the docking methodology is described transparently, the paper should more explicitly qualify that the vast majority of complex structures are computationally predicted, not experimentally determined. The redocking validation (Figure 3A) only tests recovery of known co-crystal poses, which is not the same as validating predicted poses for the 1.38M bioactivity-labeled pairs lacking experimental structures.

2. **Missing standard deviations in tables.** Tables 1 and 2 report point estimates without standard deviations or confidence intervals. This is important for assessing whether observed differences (e.g., between Uni-Mol and ProFSA in Table 1, or between SIU 0.6 and 0.9 in Table 2) are statistically meaningful.

3. **Mean pooling in the within-pocket metric gives equal weight to pockets with very few ligands.** Equation 3 averages Pearson correlations across pockets, meaning a pocket with 2 ligands has the same influence as a pocket with 200. This can make the aggregate metric noisy for small pockets. Weighted pooling (by number of ligands per pocket) or a minimum-ligand threshold should be considered.

4. **The deduplication threshold (Tanimoto > 0.8, applied only to targets above the 90th percentile) is described but not justified.** The selective application (only for targets with >2,146 molecules) is reasonable for computational efficiency, but its impact on dataset composition and downstream model performance is not analyzed.

5. **Multiple conformations per label (≈4:1 ratio of conformations to labels) could lead to data leakage.** If multiple docked poses of the same ligand-pocket pair are used in training, the model may overfit to pose-specific artifacts rather than learning from the bioactivity label. The paper should clarify whether multiple poses of the same pair are treated as separate training examples or aggregated.

### Trivial
- The reference to "Table 10" in the main text (line 140) does not match the table numbering in the extracted text (Tables 1 and 2). The authors should ensure consistency.
- Figure 3(A) labels refer to "RMSD" in the text but the figure itself could not be verified for axis clarity.

## Nice-to-Haves
- A control experiment for range restriction: bin pockets by bioactivity variance and report within-pocket Pearson* separately for high- and low-variance groups.
- An ablation removing the structural (docked) component entirely (training on SMILES + pocket features only) to isolate whether the computationally docked poses contribute beyond non-structural information.
- Evaluation on a shared external benchmark (e.g., CASF-2016) to enable direct comparison between SIU-trained and PDBbind-trained models.

## Removed Points
- **Dataset release status / "promised upon acceptance"**: Hard rule — criticisms questioning availability of cited resources are removed.
- **Missing appendix / Table 10 not present in extracted text**: Hard rule — parser-stripped sections should not be flagged.
- **"FLAPP is mentioned but not explained"**: This is a known method (Fast Local Alignment of Protein Pockets); a citation is provided, and detailed explanation is not expected for every referenced algorithm.
- **Generic formatting/style nitpicks**: Removed per hard rules.
- **Claim that docking poses cannot be validated for the 1.38M pairs**: The paper provides redocking validation (Figure 3A) as a proxy, which is standard practice; demanding individual experimental validation for each pair is not a reasonable expectation for a dataset of this scale.
- **Strength Finder's strengths that are generic**: Filtered out where they lacked specificity or conflicted with verified weaknesses.

## Novel Insights
The reviews surface two observations that go beyond the paper's own presentation. First, the range restriction confound provides a concrete, testable alternative explanation for the claimed "more challenging" nature of the within-pocket task — the paper should treat this as a required control rather than an afterthought. Second, the lack of test set specification for the PDBbind-vs-SIU comparison reveals a broader issue in the field: dataset papers often conflate "our data improves performance" (which requires a shared, independent test bed) with "our data has different properties" (which is descriptive). The paper's main contribution would be stronger if it leaned into the latter framing rather than trying to claim superiority through an under-specified comparison.

## Suggestions
1. **Clarify the cross-dataset comparison**: Explicitly state the test set used for Table 2/Table 10, and ideally add results on an independent benchmark (CASF-2016 or a held-out Atom3D split) where both PDBbind-trained and SIU-trained models are evaluated on the same examples.
2. **Address range restriction**: Add a supplementary figure showing within-pocket bioactivity variance distribution, and report the expected Pearson* under a null model (random predictions per pocket). Bin pockets by variance and show that the metric drop is not solely a variance artifact.
3. **Add standard deviations** to all tables using multiple independent training runs.
4. **Soften the language** around the pocket-only "shortcut" claim and the "high-quality structural data" framing, making explicit that the structures are computationally predicted.
5. **Clarify the multiple-conformation-per-label issue**: State whether multiple docked poses of the same ligand-pocket pair are used as separate training examples, and if so, discuss potential leakage.

## Score and Decision

The paper addresses a genuine problem, constructs a large and potentially valuable dataset, and proposes evaluation metrics that better align with practical drug discovery needs. The core ideas are sound. However, the paper has two significant methodological weaknesses that need to be resolved: (1) the cross-dataset comparison lacks a specified test set, making a headline claim uninterpretable, and (2) the within-pocket metric interpretation is confounded by range restriction. These are fixable with additional controls and clearer exposition, but in the current form the empirical evidence does not fully support the claimed advantages. I therefore cannot recommend acceptance as-is.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
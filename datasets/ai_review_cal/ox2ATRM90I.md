- Decision: Accept
- Avg Score: 6.20
- Scores: 6, 6, 5, 8, 6
Now I have all the information needed to verify the reviewer claims against the paper. Here is my consolidated review.

---

## Summary

This paper presents YAIB (Yet Another ICU Benchmark), a modular and extensible framework for reproducible clinical machine learning experiments on ICU data. It natively supports five open-access ICU datasets (MIMIC III/IV, eICU, HiRID, AUMC) and provides five clinically defined prediction tasks (mortality, AKI, sepsis, kidney function, length of stay). The framework standardizes the entire pipeline from cohort definition through preprocessing to model evaluation, and the paper demonstrates its value by showing how small changes in cohort definition, feature sets, and preprocessing affect performance more than model architecture choice, and by conducting cross-dataset transfer learning experiments.

## Strengths

- **Multi-dataset support and dataset interoperability (Table 1)**: YAIB is the only benchmark that natively supports all five major open-access ICU datasets and enables cross-dataset experiments. Table 1 systematically compares YAIB against 15 existing benchmarks and shows YAIB is uniquely checked for "Dataset interoperability" and "Extensible." This is a concrete, well-evidenced contribution.

- **Modular and extensible design philosophy (Section 3.1)**: The framework prioritizes extensibility over rigidity, providing abstracted interfaces for adding new datasets, prediction tasks, models, and preprocessing steps. The paper explicitly scopes the design choices and provides documentation for extensions. This is a principled architectural decision that distinguishes YAIB from hard-coded single-dataset benchmarks.

- **Demonstration that cohort/task definition choices have substantial impact (Section 4.2, Tables 3–4)**: The paper provides concrete experiments showing that (a) changing exclusion criteria for mortality on HiRID shifts AUROC by ~3–4 points while model variation within a fixed setup is <1 point (Table 3), and (b) different sepsis definitions shift AUROC by up to ~10 points (Table 4). These experiments directly support YAIB's motivation and are genuinely informative.

- **Cross-dataset external validation and fine-tuning experiments (Section 4.3, Figures 2–3)**: Using YAIB's harmonized data format, the paper evaluates models trained on one dataset across all others and shows that fine-tuning an eICU model on HiRID outperforms training from scratch with limited data. These experiments are uniquely enabled by YAIB's multi-dataset design.

## Weaknesses

### Fatal
None.

### Major

- **Ambiguous description of the cross-validation and hyperparameter tuning protocol (Section 4.1, lines 221–225)**: The paper states: *"For computational reasons, hyperparameter tuning used only the first 2/3 folds, respectively... The final validation of the best hyperparameters used all 5 folds."* The phrase "first 2/3 folds" is unclear — it could mean 2/3 of each fold's training data is used for tuning (standard nested CV), 2/3 of the folds, or something else. A standard nested-CV reading (tuning on a training subset within each fold, then evaluating on held-out test sets) is valid and does not introduce leakage, but the wording is genuinely confusing and needs to be clarified. As written, a reader cannot be certain the test data was never used during hyperparameter selection. This must be clarified before the results in Tables 2–4 can be fully trusted.

### Minor

- **Central claim is qualified but evidence is limited to selected comparisons**: The abstract states that dataset/cohort/preprocessing choices matter *"often more so than model class."* The paper provides convincing examples (cohort leakage, sepsis definitions, feature ablation) but does not systematically quantify how many of the 5 tasks × 4 datasets show this pattern, or whether there are cases where model class dominates. The evidence is representative, not comprehensive. The discussion (Section 5) is more measured, but the abstract statement slightly overreaches relative to the evidence provided.

- **Test set sizes not reported**: The paper reports means and standard deviations over 5 CV iterations but does not state the number of patients/samples in each test split. For classification tasks, this makes it impossible to judge whether a 0.3-point AUROC difference is meaningful. Adding this information would improve the interpretability of the results.

- **No computational resource information**: Training time per model, GPU/CPU specifications, and total compute budget are not reported. This information would help researchers planning to adopt YAIB.

### Trivial

- **Stray template text in the abstract (line 7)**: The abstract contains the sentence *"Use 10~point type, with a vertical spacing (leading) of 11~points..."* which is template formatting instructions that were accidentally left in the abstract body. This should be removed.

## Nice-to-Haves

- A more structured decomposition of variance — e.g., a table comparing the performance range across models for each fixed task/dataset versus the range across task definitions for each fixed model — would strengthen the central claim without requiring new experiments.
- Validation of the pipeline by reproducing a published result from an existing benchmark (e.g., from Harutyunyan et al. on MIMIC or Yèche et al. on HiRID) using the same cohort definitions would further strengthen credibility.
- Reporting the exact configuration effort (lines of code, configuration file size) needed to add a new dataset or task would better substantiate the claim of extensibility.

## Removed Points

- **Criticism that the cross-validation protocol is "likely invalid" and leads to optimistically biased results**: Removed. The harsh critic interpreted the ambiguous wording in the worst possible way (that test data from the same folds used in tuning was used for final evaluation). The standard nested-CV reading of the protocol — tune on a subset of training data within each fold, then evaluate on held-out test sets — is valid and does not introduce leakage. The problem is clarity, not validity. The concern is kept above as a Major weakness about clarity, not as a fatal flaw.
- **Criticism that "the repeated first sentence from a template" is a formatting artifact that "should be removed"**: Kept in Trivial as it is actual stray text in the paper, not a parser artifact.
- **Criticism about missing appendix contents, missing proofs, undisclosed hyperparameters**: Removed per instructions (appendices are stripped by the parser).
- **Strength Finder's claim that the paper provides "the first-ever benchmark for the AUMC dataset"**: This is stated in the discussion (line 451) and is factually correct; kept implicitly via the multi-dataset strength.

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder both converge on the paper's core contribution — that a modular, multi-dataset benchmark reveals how sensitive ICU ML performance is to apparently arbitrary design choices — but neither offers a genuinely novel perspective that the paper itself does not articulate.

## Suggestions

1. Rewrite the description of the cross-validation and hyperparameter tuning protocol (Section 4.1) to be unambiguous about data partitioning, ideally with a diagram or explicit numbered list of steps.
2. Add a sentence in the abstract or discussion acknowledging that the "model class vs. task definition" claim is based on the specific settings examined, not a universal finding.
3. Report the number of samples in each test split for the reported metrics.
4. Add a brief computational resource note (hardware, approximate training time per model).
5. Remove the stray template text from the abstract.

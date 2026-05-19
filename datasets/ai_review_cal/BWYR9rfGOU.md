- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 6, 3, 3
## Summary

This paper proposes SATE (Subpopulation-Aware Two-stage Estimator), a performance prediction method designed for subpopulation shift. The method decomposes prediction into two stages: (1) estimating test-set subgroup proportions by solving a linear system that expresses the test-set mean embedding as a combination of training-subgroup mean embeddings, and (2) estimating each subgroup's accuracy using the accuracy on an augmented (or validation) version of that subgroup's training data. The final predicted accuracy is a weighted average across subgroups. Experiments on vision (Waterbirds, CelebA), medical (CheXpert), and language (MultiNLI, SNLI) datasets are reported, comparing against standard OOD performance prediction baselines (ATC, DoC, DoE, NI).

## Strengths

- **Novel application to subpopulation shift for performance prediction.** Existing OOD performance prediction methods focus on covariate/natural shifts and do not exploit the subgroup structure. SATE is, to this reviewer's knowledge, the first method specifically designed for the subpopulation-shift setting, with a clean two-stage decomposition (proportion estimation → accuracy estimation per subgroup → weighted aggregate).

- **Theoretical guarantee for proportion estimation.** Theorem 1 proves that the estimated subgroup proportions **w** are unbiased and consistent under the stated assumptions (same-group distribution and column-full-rank embedding matrix). This provides a formal foundation that prior subpopulation-shift performance prediction methods lack.

- **Experimental breadth across modalities.** The evaluation spans vision (Waterbirds, CelebA), medical (CheXpert), and language (MultiNLI, SNLI) datasets, and includes multiple training algorithms (ERM, GroupDRO, DFR) and two model architectures per vision task. The test-set design (20 different subgroup distributions per dataset) is carefully motivated, and the J-S divergence analysis (Figure 3) convincingly shows that these test sets span a range of shift severities.

- **Practical SATE-val variant.** The method naturally extends to settings where a validation set is available (SATE-val), and results indicate this variant yields further gains — a practical advantage not shared by baselines like ATC or DoC.

## Weaknesses

### Fatal

None.

### Major

1. **Unsupported claim of linear relationship for accuracy estimation.** Contribution 2 states: "*through experimental validation, we discovered a linear relationship between in-distribution accuracy and accuracy on an augmented training set. We use this insight to perform performance prediction without accessing additional data.*" The paper provides **zero experimental evidence** for this claimed linear relationship — no plot, no table, no ablation, no analysis. The core SATE method (without validation data) uses accuracy on augmented training data as a direct proxy for test subgroup accuracy, but the paper never justifies *why* this should work. If this relationship does not hold, the accuracy estimates are unfounded and the entire prediction breaks regardless of how well proportion estimation works. SATE-val (using validation data) is more defensible, but the paper's headline method and contribution 2 rest on an unsubstantiated claim.

2. **Proportion estimation solver ignores non-negativity and sum-to-one constraints.** Algorithm 1 (line 10) simply states "*Solve the linear equation H_S · w = h_T*", and the text adds "*It can be solve algebraically or by gradient descendant with MSE loss function.*" Valid subgroup proportions must be nonnegative and sum to one, yet no constraint-handling mechanism is described. An unconstrained solve can produce negative weights or weights that do not sum to one, yielding meaningless proportions and a broken accuracy estimate. Non-negative least squares or simplex-constrained optimization would be needed; this methodological gap is unaddressed.

3. **Theoretical claims overstate what is proved.** The abstract states: "*We provide theoretical proof of our method's unbiasedness and consistency.*" However, Theorem 1 only proves unbiasedness and consistency of the *proportion estimator* **w**. The final accuracy estimate combines **w** with subgroup accuracy estimates **a** (which are themselves unanalyzed). The paper does not prove that the subgroup accuracy estimates (`Acc_{S_i'}`) are unbiased for the true test subgroup accuracy, nor does it analyze the bias of the combined estimate. The theory therefore does not support the core promise stated in the abstract and introduction.

4. **Comparison advantage from attribute information is uncontrolled.** SATE uses attribute annotations (subgroup labels) on the training data to compute subgroup mean embeddings and subgroup-specific accuracy estimates. The baselines (ATC, DoC, DoE, NI) do not have access to this information. Unsurprisingly, SATE outperforms them. This comparison tests whether having attribute information helps, not whether SATE's *specific design* (two-stage decomposition) is effective. The paper acknowledges this in the Limitations section but does not control for it experimentally — no attribute-aware baselines (e.g., training separate predictors per subgroup, subgroup-aware confidence calibration, or weighting subgroup accuracies by training proportions) are included. The headline empirical claims are therefore not as informative as they appear.

### Minor

1. **No error bars or significance tests.** Results are reported as bar charts (Figure 5a) and Table 1 without standard deviations, confidence intervals, or statistical significance tests. The evaluation involves sampling 20 test sets, training multiple models, and data augmentation — multiple sources of randomness. Without variance estimates, the reader cannot assess whether the large reported gaps between SATE and baselines are reliable.

2. **No ablation study.** The paper does not ablate the two stages. For example: what happens with uniform subgroup weights? What if training (rather than estimated) subgroup proportions are used? What if per-subgroup accuracy estimates are replaced by the overall training accuracy? An ablation would demonstrate that *both* stages contribute.

3. **Minimal NLP evaluation.** The paper claims novelty in NLP (contribution 3), but only two NLI datasets (MultiNLI, SNLI) are tested, using only BERT-base. No sentiment classification, named entity recognition, or other NLP tasks are explored, and no other NLP architectures (e.g., GPT-style) are tested. The claim is not commensurate with the evidence.

4. **No analysis of proportion estimation errors or sensitivity.** The proportion estimation step depends on the quality of the featurizer's embeddings — if the featurizer does not separate subgroups well, the mean embeddings may be collinear or not linearly combinable. No experiment varies the featurizer or embedding dimension to test sensitivity to this assumption.

### Trivial

- "It can be solve" (line 117) — grammar issue.
- Theorem 1 is stated without proof in the main text (presumably deferred to an appendix stripped by the parser; fine if the proof exists in the full submission).

## Nice-to-Haves

- A comparison against simple attribute-aware baselines would clarify whether the two-stage decomposition adds value beyond merely having subgroup information.
- An analysis of what happens when the test embedding does not lie in the column span of the subgroup mean embeddings (relevant for combined covariate + subpopulation shifts, which the paper partially tests in Table 1).
- Discussion of computational cost (forward pass over training set to compute mean embeddings).

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The claim of being 'first to address unsupervised performance prediction in NLP tasks' is questionable: the paper simply applies the same method to NLP datasets; there is no NLP-specific algorithmic innovation."* — The paper's claim is about being the first to *address the problem* on NLP datasets, not about NLP-specific algorithmic novelty. The reviewer's framing misinterprets the scope of the claim. The prior-work section (Section 2) provides a reasonable literature justification for this claim. Removed as a strawman.
- *"The assumption that training and test subgroups follow the same distribution (P_g) excludes within-subgroup covariate shift"* — The paper already acknowledges this in Section 7 (Limitations): "It cannot effectively quantify or address covariate shifts." Removed as already addressed.
- *"The theoretical proof belongs in the appendix"* — Formatting discussion, not a substantive weakness. The parser likely stripped the appendix. Removed.
- *"No discussion of computational cost"* — True but trivial; moved to Nice-to-Haves.
- *"The NLP experiments are minimal"* — Kept as Minor weakness (it is concrete and verifiable: only 2 datasets, 1 architecture).
- Strength Finder's generic strengths: *"addressed an important problem"*, *"targeted an interesting question"* — dropped as generic/superficial.
- Strength Finder's strength #3 about "first unsupervised NLP performance prediction" — kept as a strength but the Minimal NLP evaluation weakness (Minor #3) appropriately tempers it.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Provide evidence for the accuracy-estimation claim** — either show the claimed linear relationship experimentally, or drop the augmentation-based variant and focus on SATE-val (using validation data), discussing validation-data scarcity as a limitation.
2. **Fix the proportion estimation solver** — use non-negative least squares and normalize weights to sum to one; show that this does not harm performance.
3. **Add statistical rigor** — report means and standard deviations across multiple runs, and include significance tests (e.g., paired bootstrap or signed-rank tests) against each baseline.
4. **Include attribute-aware baselines** — at minimum, compare against (a) using training subgroup accuracies without augmentation, (b) weighting by training proportions, (c) a simple baseline that uses the same attribute information but with a different aggregation (e.g., averaging subgroup-specific confidences).
5. **Perform an ablation study** — demonstrate that both proportion estimation and per-subgroup accuracy estimation contribute to the final result.
6. **Clarify the scope of theoretic claims** — explicitly state that Theorem 1 covers proportion estimation only, and discuss what additional assumptions would be needed for the full accuracy estimate.

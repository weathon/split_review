Now I have a comprehensive understanding of the paper and all the review inputs. Let me construct the final consolidated review.

## Summary

This paper introduces Neural Manifold Regularization (NMR), a supervised dimensionality reduction method that projects neural population activity into a 2D latent space regularized by movement label distances and densities. The key innovation is a regression-based mechanism that filters contrastive pairs: it uses linear regression to predict labels from embeddings, then selectively forms positive/negative pairs based on whether predicted labels fall within a threshold of the true labels (pulling together embeddings with nearby predictions regardless of correctness, and using mispredicted-distant samples as negatives). The paper evaluates NMR across an unusually broad set of 68 sessions spanning four neural signal modalities (single units, LFP bands, unsorted events, multiunit threshold crossings), three movement tasks (center-out reaching, natural random-target movements, attempted handwriting), multiple brain areas (M1, PMd, S1, precentral gyrus), and two species (macaque, human), consistently finding large improvements over CEBRA and pi-VAE.

## Strengths

1. **First quantitative demonstration of 2D latent dynamics matching 2D movement trajectories.** NMR achieves explained variance of 0.88 (M1) and 0.9 (PMd) in 2D latent space for center-out reaching, whereas prior work required 3+ dimensions (Fig 2, Section 4.1). This directly fulfills a goal stated as open in the literature.

2. **Consistent large-margin improvements across the largest multimodal benchmark assembled for this problem.** Across 68 sessions, NMR outperforms both baselines in every condition: center-out reaching (0.88 vs 0.48 vs 0.43 in M1), natural grid movements for both sorted units (0.82 vs 0.55 vs 0.45) and unsorted events (0.65 vs 0.36 vs 0.25), free natural movements (0.79 vs 0.58 vs 0.56), and attempted handwriting in a paralyzed human (0.78 vs 0.59 vs 0.23) (Figs 2, 5, 6, 7).

3. **Practical cross-session, cross-subject, and cross-year decoding with a simple linear decoder.** NMR embeddings enable a hyperparameter-free linear regression to decode movements nearly twice as well as CEBRA cross-session (t=18.5, p=1.5e-47) and six times better than pi-VAE (t=21, p=1.4e-55) (Fig 3, Section 4.2). This directly demonstrates BMI-relevant generalization.

4. **Lower session-to-session variability and computational efficiency.** NMR exhibits standard deviation of 0.03 (M1) and 0.02 (PMd) across sessions vs 0.1/0.06 for CEBRA (Fig 2), and runs significantly faster (119 vs 163 seconds, t=12, p=3e-14; Fig 5f) by avoiding unnecessary distance computations.

5. **Honest limitation reporting.** The paper transparently discusses where NMR fails (complex handwriting characters, Section 5), shows greater variability on LFP data (Section 4.3), and identifies a specific session with poor cross-session performance with a plausible explanation (Section 4.2).

## Weaknesses

### Fatal
None.

### Major
- **The method description in the extracted text is significantly truncated by the parser (sections 3.1–3.2 are missing entirely; section 3.3 ends mid-sentence), but even the readable portion is not fully self-contained as a method specification.** The core idea is conveyed (regression-based pair filtering, thresholded positive/negative assignment, density weighting), but several design details are underspecified for a new-method paper: (a) how the threshold for positive/negative pairs is determined (fixed hyperparameter? percentile-based heuristic?) is not stated; (b) "ConR loss" is referenced without definition — readers need to consult the CEBRA paper to know the base loss function; (c) whether the linear regression for label prediction is trained jointly with the embedding network or in a two-stage process is ambiguous from the phrase "without altering the embeddings"; (d) the density-dependent weighting mechanism for infrequent labels is mentioned only in the abstract with no mathematical description. Since this is a methods paper whose central contribution is the NMR loss, the main text (or a clearly signaled appendix) should provide a complete algorithmic specification including the full objective in mathematical form. The code being uploaded mitigates but does not fully resolve this.

### Minor
- **No ablation study isolating the contribution of the regression-based pair selection vs. the density weighting.** The paper claims two innovations on top of CEBRA's contrastive framework — (1) using linear regression to filter contrastive pairs rather than using all pairs, and (2) density-dependent weighting for infrequent labels — but never tests whether both components are necessary or how much each contributes. An ablation (e.g., NMR without regression filtering, NMR without density weighting, or a simple label-distance-based contrastive baseline without the regression mechanism) would strengthen the causal attribution of improvements.
  
- **The number of test examples per session and the precise train/test split procedure are not stated in the main text.** The paper repeatedly refers to "test trials" in figure captions and shows cross-session decoding matrices, but the data-splitting scheme (e.g., fraction held out, cross-validation folds) should be explicitly described in the experiments section rather than deferred entirely to figure captions and the (parser-stripped) appendix.

- **Hyperparameter ranges and tuning budgets for CEBRA/pi-VAE baselines are not summarized in the main text.** The paper states that "the best hyperparameters were chosen" and references supplementary figures (Figs 12, 13, 18, 22), but the main text would benefit from a concise summary of the search space (e.g., number of configurations evaluated per session, range of learning rates/dimensions/temperature). This is standard practice for fairness of comparison.

### Trivial
- The abstract's "over 50% improvement" claim is not precisely operationalized (50% relative improvement in explained variance relative to the best baseline, averaged across conditions? minimum across conditions?). The numbers in Section 4.1 are consistent with this claim, but the abstract could be more explicit.
- The paper reports many t-tests with multiple comparisons correction but does not name the specific correction procedure (Bonferroni, Holm, Benjamini-Hochberg). This is a minor transparency detail.

## Nice-to-Haves
- Ablation studies isolating the regression-based pair selection and density weighting components (as described above — this would strengthen rather than fix a flaw)
- Hyperparameter sensitivity analysis for NMR itself (varying the threshold, batch size) to provide practical user guidance
- Reporting effect sizes (Cohen's d) alongside p-values for the main comparisons

## Removed Points
*These points are flagged to be removed, treat them with caution*
- **"Baseline comparison is narrow"** — The paper explicitly justifies why CEBRA (contrastive SOTA) and pi-VAE (generative SOTA) were chosen, noting both benchmark against many earlier methods (PCA, UMAP, fLDS, LFADS, etc.). The "over 50%" claim is relative to these SOTA baselines, which is standard practice. This is not a genuine weakness.
- **"Tuning procedure is underspecified"** — The paper references supplementary figures (Figs 12, 13, 18, 22) for hyperparameter search details, which the parser stripped. The main text states that baselines were "hyperparameter-optimized" and that model parameters were fixed across sessions. This is adequate for a conference paper.
- **"Effect sizes and confidence intervals not reported"** — This is not standard practice for this field; the paper reports t-statistics and p-values with multiple comparisons correction, which is the norm. A nice-to-have, not a weakness.
- **"The paper does not specify the multiple comparisons correction method"** — The paper explicitly states "paired t-test with multiple comparisons correction" throughout. The specific method (Bonferroni, Holm, etc.) is a minor implementation detail commonly deferred to the appendix.
- **"Section 3.3 is garbled / fractured mid-sentence"** — Parser artifact. The original submission does not have this issue.
- **"The paper does not include a dataset summary table"** — The paper references "Table 2" for session details, suggesting this exists in the original submission (stripped by parser).

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Rewrite Section 3 (or ensure the complete version is available in the camera-ready) to provide a self-contained, mathematical description of the NMR loss function, including: (i) the full objective function; (ii) how the threshold is determined; (iii) whether the regression head is learned jointly or in two stages; (iv) the mathematical form of the density weighting for infrequent labels. Pseudocode would be helpful.
2. Add at least one ablation isolating the regression-based pair selection from the density weighting to demonstrate that both components contribute.
3. State the train/test splitting procedure explicitly in Section 4, and summarize the hyperparameter search space for both baselines in a paragraph or table in the main text.

## Score and Decision

This paper tackles a well-motivated problem (aligning 2D latent neural dynamics with 2D movements), proposes a clearly motivated methodological modification to contrastive dimensionality reduction, and validates it with an unusually thorough and honest experimental evaluation spanning 68 sessions, multiple neural modalities, brain areas, tasks, and species. The empirical results are consistently strong and presented transparently, including honest discussion of failure cases and variability. The core weaknesses are (1) the method description, while present in its mechanism, is not fully self-contained as a mathematical specification in the extracted text (partially a parser issue), and (2) the lack of ablations makes the causal attribution of the two claimed innovations less certain than it could be. Neither issue is fatal — the method's idea is clear, the code is provided, and the empirical evidence for the method's effectiveness is overwhelming. These are standard revision items.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
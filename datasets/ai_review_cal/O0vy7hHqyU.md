- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3
Now I have a thorough understanding of the paper and all the claims. Let me synthesize my final review.

## Summary

This paper proposes AFMO, a multimodal fake news detection framework that uses BERT and VGG-19 for feature extraction, Mahalanobis distance/KNN for outlier removal, and simulated annealing (SA) for feature selection and fusion. The method is evaluated on PolitiFact (unimodal), Weibo, and Gossipcop (multimodal) datasets.

## Strengths

1. **Novel application of simulated annealing for cross-modal feature selection in fake news detection** — The SA-based feature masking (Section 3.4) directly targets the cross-modal interference problem where irrelevant image features can dominate text features or vice versa. The case study (Section 4.4.2) provides a concrete illustration: a fake news post with an unrelated but innocuous-looking image was misclassified by conventional methods but correctly identified after SA-based feature selection.

2. **Principled outlier removal as a preprocessing step** — The paper employs both Mahalanobis distance and KNN-based outlier detection (Section 3.3) to clean the training set before feature fusion, which is a more structured approach than simple concatenation used in many multimodal detection pipelines.

3. **Ablation evidence of SA convergence** — Figure 4 shows that accuracy, precision, recall, and F1 improve over SA iterations, demonstrating that the optimization is making meaningful progress.

## Weaknesses

### Fatal

None.

### Major

1. **Uncontrolled baseline comparisons undermine the central claim of superiority.** Line 222 states: *"The data for these baseline models were sourced from their respective papers."* This means the claimed 8.47% accuracy improvement over XGBoost on PolitiFact, and the 4.62% recall / 6.5% F1 improvement over GCAN, are comparisons across different experimental setups (different dataset splits, preprocessing, evaluation protocols, and potentially different dataset versions). These gaps are large enough that the reported gains cannot be attributed to the method rather than to confounding factors. The paper's primary claim — that AFMO outperforms existing methods — is not convincingly supported.

2. **The SA optimization objective is underspecified regarding which data split it operates on.** The paper correctly states a 7:1:2 train/validation/test split (line 180), but Section 3.4 describes the SA accuracy computation only as comparing predictions against *"the actual label label_i"* without specifying whether this is training or validation accuracy. If the SA maximizes training accuracy, the selected mask could overfit to training idiosyncrasies, and the reported test results would not be evidence of generalization. If it uses validation accuracy, this should be stated explicitly. This is a structural gap in the methodology description that prevents assessment of whether the SA procedure is valid.

### Minor

3. **Weibo dataset results are listed as part of the evaluation but are not discussed.** Section 4.1 (line 169) introduces Weibo as a multimodal benchmark, and Table 2 presumably includes its statistics. However, the comparative analysis in Section 4.4.3 (line 222) only discusses PolitiFact and Gossipcop. Whether Weibo results exist in the original table image cannot be verified from the extracted text.

4. **Abstract overclaims the feature scope.** The abstract (line 4) claims the method introduces *"word-level, sentence-level, and contextual features,"* but the methodology (Section 3.2.1 and line 182) only extracts sentence-level BERT representations (concatenation of the last four hidden layers). Neither word-level nor contextual features beyond the BERT encoding are implemented. This framing mismatch could mislead readers about the method's novelty.

5. **Interaction between the SA mask and detector training is not explained.** The equations in Section 3.4 describe applying the binary mask to features before feeding them to the detector, but it is unclear whether the detector is retrained from scratch for each mask candidate, or whether a single pre-trained detector is used to evaluate all masks. These two setups have very different implications for computational cost and potential overfitting.

### Trivial

6. The notation `k` is used both as the cooling factor (0.98, line 186) and as a separate constant in the acceptance probability equation `e^{-k · ΔE / t_cur}` (line 152) without clarification.

## Nice-to-Haves

- Ablate the outlier removal component independently (how much does it contribute vs. training with all data?)
- Add multiple random seeds and report mean ± std for the main results
- Provide a pseudocode or algorithm box for the full SA pipeline to clarify the split used for mask evaluation
- Analyze computational overhead: SA evaluates many mask candidates, each requiring detector runs

## Removed Points

These points from the harsh critic were removed with justification:

- **"No validation split"** — Removed as factually incorrect. Line 180 explicitly states a 7:1:2 train/validation/test split. The underspecification issue is kept as a Major weakness but the claim that no validation set exists is wrong.
- **"No confidence intervals / statistical reporting"** — Removed as a generic weakness common to large-benchmark evaluations; not a standard expectation for every paper in this area.
- **"KNN threshold vague"** — Removed as the paper describes manual tuning of K=3 and α=0.8 based on experiments on the Gossipcop dataset (lines 184–185), which is a reasonable if limited empirical justification.
- **"Missing appendix / proofs / reproducibility details"** — Removed; the parser strips supplementary sections from all submissions.
- **"Does not identify specific failure modes of prior work"** — Removed as stretching what a related work section must do.
- **"Efficiency analysis missing"** — Moved to Nice-to-Haves.
- The strength finder's strength about "significant performance gains over strong baselines" — Removed because it conflicts with the verified weakness that those baselines are uncontrolled. The claimed gains cannot be evaluated as a strength when the comparison is invalid.

## Novel Insights

The harsh critic's most insightful observation — that the SA objective function is described in terms of training-set accuracy without clarifying whether a validation split is used — points to a genuine methodological ambiguity that goes beyond a simple presentation issue. This is combined insightfully with the observation that even if the SA procedure is sound, the uncontrolled baseline comparisons make the claimed SOTA results unverifiable. These two weaknesses together (one a methodological underspecification, the other an evidential gap) do not individually invalidate the core idea, but they compound to make the paper's empirical contribution significantly weaker than claimed.

The strength finder correctly identified the case study as concrete evidence for the SA mechanism working, but failed to notice that the central performance claims are not backed by fair comparison.

## Suggestions

1. **Reproduce at least three strong baselines** (e.g., EANN, MVAE, CARMN) under identical dataset splits and preprocessing. This is the single most important fix — without it, the claims of superiority are unsupported.
2. **Clarify which split the SA accuracy objective uses.** If it currently uses training accuracy, restructure to evaluate masks on a validation split and report test-set performance of the best validation mask.
3. **Specify the detector architecture** used within the SA loop (number of layers, hidden dimensions, training procedure) and describe how the mask interacts with detector training.
4. **Report Weibo results** in the discussion text, not just in a table.
5. **Add an ablation** comparing: (a) no outlier removal, (b) no SA (simple concatenation), (c) random mask selection, and (d) full AFMO.

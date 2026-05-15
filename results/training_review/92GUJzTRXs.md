I have verified the paper content thoroughly. Let me now produce the consolidated review.

## Summary
The paper proposes ConDS (Context Distribution Shift), a method that improves the robustness of In-Context Learning (ICL) against noisy labels in the candidate set. ConDS splits the noisy candidate set into training and validation subsets, uses the LLM's prediction accuracy on validation queries as a reward signal to identify "informative" (clean) samples, then augments those samples in the training set to shift the candidate distribution toward clean samples. The method supports both off-the-shelf and fine-tuned retrievers and achieves an average 8.12% improvement over the best baseline across nine benchmarks.

## Strengths
- **Novel approach to a real, under-studied problem**: The paper correctly identifies that label noise in the ICL candidate set severely degrades performance (Figure 2 shows this clearly) and that prior work largely only observed the phenomenon without proposing solutions. ConDS is the first method to address this via candidate-set distribution shift, which is a principled and intuitive direction.
- **Consistent and substantial empirical gains**: ConDS outperforms the best baseline by 8.12% on average across 9 datasets (Table 1), with the duplication variant beating zero-shot by 17.07%. These gains are evaluated on clean test labels — noise is only in the candidate set — so the results are genuine accuracy improvements, not artifacts of matching noisy evaluation.
- **Retriever-agnostic and broadly applicable**: ConDS consistently improves ICL accuracy when combined with BM25 (by 1.26%), KNN (3.36%), DPP (5.54%), and PromptPG (9.77%) as shown in Table 2. This flexibility is a key claimed contribution and is well-supported.
- **Mechanistic evidence of neighbor cleaning**: Figure 4 shows that after ConDS, 50.25% of test queries on SST-2 have 100% clean selected ICL samples, compared to 0% for all baselines. This directly confirms the paper's core intuition about shifting the distribution to favor clean samples.
- **Robustness across varying conditions**: Figure 5a shows ConDS has the smallest average accuracy drop (9.12%) as noise ratio varies, and Figure 5b shows it stabilizes performance across different candidate set sizes (accuracy difference drops from 12.3% for PromptPG to 6.14% for PromptPG+ConDS).

## Weaknesses

### Fatal
None. The empirical results are valid (evaluated on clean test labels), and the method demonstrably improves ICL accuracy. The concerns below are serious but do not invalidate the core findings.

### Major
1. **The reward signal for identifying "informative" samples uses noisy validation labels, and this issue is not adequately addressed.** The method splits the noisy candidate set into training and validation sets (line 132: "randomly split 10% of the candidate data as C^valid"). The validation labels are themselves noisy (flipped with probability p=0.6 by default). The reward function (Eq. 4) compares the LLM's prediction against the validation label, meaning: (a) a positive reward can be earned when the LLM correctly predicts a *wrong* noisy label, and (b) a negative reward can be given when the LLM correctly predicts the true label but it mismatches the noisy validation label. The paper calls these noisy validation labels "ground truth" (line 72), which is misleading. While the paper briefly acknowledges in a single sentence (line 157) that "the percentage for lower clean sample ratios also increases due to the noisy samples in the validation dataset," this is an insufficient treatment of a fundamental concern about the reliability of the identification mechanism. Without an oracle analysis (e.g., what happens with a clean validation set) or a measure of how often the LLM's prediction agrees with the true vs. noisy validation label, the claimed mechanism remains unvalidated, and the possibility that gains partly arise from reinforcing validation-set noise correlations rather than genuinely cleaning the candidate set cannot be ruled out.

2. **The augmentation parameter α=1000 is chosen without any justification or ablation.** The paper states α=1000 as the augmentation factor (line 132) — meaning each "informative" sample is duplicated 1000 times — without discussing why this value was chosen or how sensitive results are to it. Duplicating samples 1000× can massively dominate the candidate set, and the subsampling upper limit N_upp is mentioned (line 84) but never defined. The combination of an unablated α and an undefined N_upp makes the method's behavior under its own hyperparameters opaque. A sensitivity analysis for α is essential for reproducibility and trust in the results.

### Minor
1. **Evidence for the "neighbor cleaning" claim is limited to one dataset (SST-2, Figure 4).** The paper's central claim of reducing "the catastrophic impact of noisy samples from almost all test queries to only a small percentage" (Section 1) is supported by clean-ratio histograms only for SST-2. Extending this analysis to at least one or two additional datasets would substantially strengthen the claim.
2. **No confidence intervals or significance tests are reported.** The paper states "average of three random seeds" but does not report standard deviations, confidence intervals, or statistical significance. Given that noise injection and retrieval have high variance, this limits the reader's ability to assess the reliability of the improvements beyond point estimates.
3. **The t-SNE visualization (Figure 3) is suggestive but not quantitative.** The claim that "misleading sample embeddings stay far away from the clean samples cluster" after ConDS is not backed by any measured separation metric (e.g., silhouette score, nearest-neighbor purity). A quantitative embedding analysis would strengthen the mechanistic argument.
4. **Computational cost is not discussed.** The method requires running the LLM on every validation sample at each epoch (for fine-tuned retrievers). This cost could exceed the cost of training the retriever itself and is not acknowledged or analyzed.

### Trivial
- The paper calls the noisy validation labels "ground truth" (line 72), which is inconsistent with the problem setup and could confuse readers.
- The formatting of the extracted Section 3.3 content appears garbled in the provided text, but this is a parsing artifact and not an author error.

## Nice-to-Haves
- An oracle experiment using a clean validation set to establish an upper bound on ConDS's performance and to confirm that the mechanism works as claimed.
- An ablation of α (e.g., 10, 100, 500, 1000, 5000) to show sensitivity.
- A label-recovery analysis on the validation set: measure how often the LLM's prediction matches the true vs. noisy label to quantify the reliability of the reward signal.
- Comparison with explicit noise-cleaning baselines (e.g., loss-based filtering, LLM self-consistency) to better contextualize the gains.
- Extending Figure 4 (clean-ratio histogram) to additional datasets.

## Removed Points
- **Criticism about needing a "clean held-out test set" (Harsh Critic, Critical Issue 2a)**: Removed because it is factually inaccurate. The paper injects noise only into the candidate set (line 130: "We inject noise in the ICL Database"), while test queries come from standard benchmarks with clean labels. The evaluation IS on clean labels.
- **Criticism about the paper "neither acknowledg[ing] this problem" (Harsh Critic, Critical Issue 1)**: Partially removed. The paper does acknowledge the noisy validation issue on line 157 ("The percentage for lower clean sample ratios also increases due to the noisy samples in the validation dataset"). However, this acknowledgment is brief and insufficient — the core concern about the reliability of the reward signal itself is not properly discussed. The broader criticism is retained as Major Weakness #1 with appropriate nuance.
- **Criticism about missing Section 3.3 / absent appendix content**: Removed per the hard rule — parser strips these sections from all papers; they exist in the original submission.
- **Criticism about "overclaiming" being first (Section-by-section notes)**: Removed per the rule about not introducing missing related work. The paper's claim about being first to use distribution shift for ICL noise cannot be verified or disputed without external sources.
- **Criticism about input noise not being discussed**: Removed — this is scope creep. The paper explicitly focuses on label noise, which is a well-defined and important problem.

## Novel Insights
None beyond the paper's own contributions. The reviews surface a genuine tension: the paper's empirical results are strong and consistent, but the mechanism by which they are achieved is undertheorized in a way that could affect interpretation. Specifically, the noisy validation labels in the reward loop mean the method's success may depend on an unexamined property — namely, whether the LLM is sufficiently often correct (despite noisy ICL samples) on the ~40% of validation queries whose labels happen to be clean. If this is the case, the method is effectively bootstrapping off the LLM's prior knowledge to filter noise, which is plausible but not the same as "distribution shift" in the pure sense claimed. The paper would benefit from making this nuance explicit.

## Suggestions
1. **Address the validation noise concern directly.** At minimum, add: (a) an oracle experiment using a clean validation set to establish an upper bound, (b) an analysis of reward reliability (how often does LLM prediction match true vs. noisy label on validation queries?), and (c) a discussion in the paper of when and why the noisy reward signal is still useful.
2. **Add an ablation of α** (augmentation factor) with at least 4-5 values, and **explicitly define N_upp** (the subsampling upper limit) in the main paper.
3. **Report standard deviations or confidence intervals** for the main results (Table 1, Table 2) to enable readers to assess result stability.
4. **Extend Figure 4** (clean-ratio histogram) to at least one more dataset (e.g., Subj or AGNews) to demonstrate that the neighbor-cleaning claim generalizes beyond SST-2.
5. **Add a quantitative embedding analysis** (e.g., average distance between clean and noisy sample clusters before/after ConDS) to support the qualitative t-SNE claims.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
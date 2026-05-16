Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper proposes ConDS, a method to improve ICL robustness against noisy candidate sets by identifying informative samples (via LLM feedback on a validation split and retriever ranking scores), augmenting them (duplication or paraphrase), and subsampling to shift the candidate distribution toward clean samples. ConDS is designed to be combined with both off-the-shelf and fine-tuned retrievers. Experiments across 9 datasets show an average 8.12% improvement over the best baseline.

## Strengths

- **Large and consistent gains across diverse tasks**: On 9 datasets spanning sentiment, topic, NLI, and subjectivity classification, ConDS (duplicate) outperforms zero-shot by 17.07% and the best baseline (PromptPG) by 8.12% on average (Table 1). The improvement is observed across all 9 datasets, not cherry-picked.

- **Empirical verification of the neighbor-cleaning mechanism**: Figure 4 directly confirms the central hypothesis: after ConDS, 50.25% of test queries have 100% clean selected ICL samples on SST-2, while BM25, KNN, and PromptPG all have 0%. This provides concrete evidence that the distribution shift isolates noisy samples for most queries.

- **Seamless integration with multiple retriever types**: Table 2 shows ConDS improves performance for BM25 (+1.26%), KNN (+3.36%), DPP (+5.54%), and PromptPG (+9.77%), supporting the claim that it generalizes across retriever architectures.

- **Stability across varying noise ratios and candidate sizes**: Figure 5a shows ConDS has the smallest average accuracy drop (9.12%) across noise ratios 0.1–0.6, compared to 18.34% for KNN. Figure 5b shows ConDS reduces sensitivity to candidate size (accuracy difference 6.14% vs. 12.3% for PromptPG). This demonstrates practical robustness beyond a single operating point.

- **No additional inference overhead**: As stated in Section 3.2, ConDS modifies the candidate set offline and introduces no extra token consumption or latency during query inference, which is an important practical advantage.

## Weaknesses

### Fatal
None.

### Major

- **No comparison to a simple noise-filtering baseline, making it unclear whether the distribution-shift mechanism itself is necessary.** ConDS is compared only against standard ICL retrievers (BM25, KNN, DPP, PromptPG) that do not attempt any noise mitigation. A straightforward baseline — e.g., using the same LLM to vet/score candidate samples on the validation split and then filtering out low-confidence samples before retrieval, or a simple weight-based sampling scheme — would directly test whether the gains come from the augmentation-and-subsampling *distribution shift* or simply from using LLM feedback to discard bad samples. Without this comparison, the reader cannot attribute the gains to the paper's core technical contribution rather than a much cheaper alternative. The paper claims the noise ICL problem is "overlooked," but observational works (Kossen et al., Wei et al.) are cited; a denoising heuristic baseline is needed to anchor the contribution.

- **The augmentation factor α=1000 is extreme and its effect is unexamined.** Each informative sample is duplicated 1000 times, so a handful of samples can dominate the training set by orders of magnitude. Given a candidate set of size 200 and a validation set of ~20 queries, this creates a substantial risk of overfitting to the validation split. The paper does not report the subsampling upper bound N_upp, does not present a sensitivity analysis over α, and does not justify the choice of 1000. Without this analysis, the claimed generality could be an artifact of a specific hyperparameter rather than the distribution-shift principle. This is a structural gap in the experimental validation.

- **Missing variance and statistical significance reporting.** All results are reported as averages over three random seeds with no standard deviations, confidence intervals, or significance tests. Noise injection is random, and the method involves stochastic resampling and subsampling. The reported improvements vary widely across datasets (28% on MR, 24% on CR, <5% on TREC and RTE). Without error bars, it is impossible to assess which improvements are reliable and which may be within the noise of the random seeds.

### Minor

- **The validation-split reliance and generalization to dissimilar queries is under-analyzed.** ConDS uses 10% of the candidate data (~20 queries) as a validation set to decide which samples to augment, relying on the QPP hypothesis that test queries resemble validation queries. The improvement pattern is consistent with this: gains are large on sentiment datasets (SST-5, MR, CR) where the validation set is representative, and small on diverse tasks like TREC and RTE. The paper does not analyze how performance varies with query similarity to the validation set, nor does it test on a held-out domain where the validation-test overlap is broken. While this does not invalidate the results, it limits confidence in how the method would behave in deployment scenarios with distribution shift.

- **Figure 4 (clean sample ratio analysis) is shown for only one dataset (SST-2).** This is the most direct evidence for the claimed mechanism, but it is reported for a single dataset. Extending this analysis to at least 2–3 other datasets (e.g., MR, Subj) would substantially strengthen the claim that ConDS works by cleaning the neighbors of test queries. As it stands, the reader cannot tell if the 50.25% figure is representative or an outlier.

- **The value of the subsampling upper bound N_upp is not reported**, and no analysis of its effect on performance is given. This is a hyperparameter that directly controls the trade-off between distribution shift strength and computational cost.

- **For the fine-tuned retriever variant (Section 3.2), it is unclear whether ConDS requires retraining the retriever from scratch for each new candidate set or can be applied as a fine-tuning step on top of an existing checkpoint.** The paper states it is "easily combined" but the procedure involves joint training. This needs clarification.

## Trivial
None.

## Nice-to-Haves

- A simple weight-based baseline where each candidate sample's sampling weight is proportional to its average correctness on validation queries (no augmentation) would sharpen the claim. If ConDS outperforms this, the augmentation/subsampling mechanism is justified; if not, the simpler scheme would be preferable.

- An analysis of the computational overhead from the additional LLM calls on the validation set would help practitioners assess the cost of deployment.

- A sensitivity analysis over α (e.g., α ∈ {10, 100, 500, 1000, 5000}) would resolve the concern about the extreme default value.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **"Section 3.3 (theoretical analysis) is missing from the provided text."** — The paper references "As analyzed in Section 3.3" (line 161), confirming this section exists in the original submission. The parser strips sections; this is not an author error.

- **"Table 2 is garbled (extracted text contains broken formatting)."** — Parser artifact from image extraction; the original submission does not have this issue.

- **"Figure 2 uses 8-shot while main experiments use 20-shot; this inconsistency is minor but should be reconciled."** — Figure 2 is a motivation figure demonstrating the noise problem exists; using a different shot count for motivation vs. main experiments is standard practice and not an inconsistency.

- **"The t-SNE visualization (Figure 3) is described but not visible."** — Parser artifact; the paper's text conveys the intuition clearly. The reviewer acknowledges this.

- **"The paper should present a breakdown by query similarity to the validation set, and should test on a held-out domain."** — This is asking for a broader paper than the one written. The paper already tests on 9 diverse datasets; the QPP hypothesis is stated. Demanding an entirely new domain test goes beyond strengthening the paper's own claims.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective on the paper that the authors have not already articulated in their framing (noise in ICL is overlooked, distribution shift can mitigate it, the method works with multiple retriever types). The key insight — that one can shift the candidate distribution offline using LLM feedback on a validation split — is the paper's own.

## Suggestions

1. **Add a simple filtering baseline**: Use the same LLM to score each candidate sample on the validation queries, then either filter out samples that never appear in a correct retrieval set or weight them proportionally. This directly tests whether the augmentation-and-subsampling mechanism adds value over cheap denoising.

2. **Report standard deviations** for Tables 1 and 2, and for the key ablation plots. With only 3 seeds and no error bars, the reader cannot gauge reliability.

3. **Add a sensitivity analysis over α** (the augmentation factor) from at least 10 to 5000, on 2–3 datasets, showing accuracy vs. α. Report the value of N_upp and its effect.

4. **Extend Figure 4** (clean sample ratio distribution) to at least 2–3 more datasets (e.g., MR and Subj) to show the 50.25% finding is general, not dataset-specific.

5. **Clarify in Section 3.2** whether ConDS for fine-tuned retrievers requires retraining from scratch or can fine-tune a pre-existing checkpoint, and how much additional compute is involved.

## Score and Decision

The paper tackles a genuine and underexplored problem with a creative method, and the reported gains are impressive in magnitude. The strengths — broad evaluation, direct mechanism evidence (Figure 4), robustness across noise ratios and candidate sizes — are real. However, the evaluation has three serious gaps that prevent acceptance in the current form: (1) no noise-handling baseline to attribute gains to distribution shift vs. simple LLM filtering, (2) an extreme hyperparameter (α=1000) with zero sensitivity analysis, and (3) no variance information, making the large but heterogeneous gains uninterpretable. These are all addressable, but as it stands the evidence does not convincingly demonstrate that the *distribution shift mechanism itself* is responsible for the results rather than a much cheaper alternative. The paper needs revision with targeted additional experiments before it is ready for publication.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
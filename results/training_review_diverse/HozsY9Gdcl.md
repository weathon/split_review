Now I have all the information I need. Let me write the final consolidated review, carefully cross-checking each claim against the paper.

---

## Summary

This paper proposes Set-MI, a membership inference method that aggregates per-document MI scores over metadata-defined sets (e.g., documents created on the same date) under the "set assumption" that all documents in a set share the same membership status. On five new benchmarks (Wikipedia, Arxiv, Language, License, Instructions) and four individual-level MI methods (Loss Attack, LiRA, Min-K% Prob, zlib entropy), Set-MI achieves an average AUROC improvement of 0.14. The paper further analyzes the impact of model size, deduplication, document length, and set size, and demonstrates robustness to violations of the set assumption.

## Strengths

1. **Novel set-based reformulation of membership inference.** The paper introduces the set assumption and aggregation framework (Section 3), shifting MI from the individual-document level to the set level. This is a genuinely new approach that leverages naturally occurring metadata groupings (same creation date, same license, same language) to amplify weak per-document signals.

2. **Significant and consistent empirical improvement.** Set-MI improves AUROC by 0.14 on average over four Individual-MI methods across all five benchmarks (Table 2, Section 5.1). The improvement is consistent across every combination of method and benchmark, not cherry-picked.

3. **Demonstrated robustness to noise in the set assumption.** The paper systematically evaluates scenarios where the set assumption is violated (Section 6, Figure 5) and shows that all three aggregation strategies (MAX, MIN, FULL) still outperform Individual-MI. The analysis of which aggregation method works best under which type of noise (member-side vs. non-member-side) is practically useful.

4. **Comprehensive analysis of factors affecting Set-MI.** The paper investigates model size (70M–12B), training-data deduplication, document length (16–2048 tokens), and set size (1–100 documents) in Sections 5.2–5.5, providing actionable insights about when Set-MI is most effective.

5. **Construction of the first set-based MI benchmarks.** The paper introduces five diverse benchmarks (Wikipedia, Arxiv, Language, License, Instructions) with naturally occurring sets (Table 1, Section 4). These benchmarks enable more realistic evaluation than individual-level evaluation and support the generality of the method.

6. **Orthogonality to existing MI methods.** Set-MI can be applied on top of any Individual-MI method (Loss Attack, LiRA, Min-K% Prob, zlib entropy) without modifying the underlying scorer (Section 3, Table 2), making the contribution broadly applicable.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **No variance or confidence intervals reported for main results.** Table 2 reports only point estimates of AUROC. The benchmarks are constructed by subsampling (e.g., "subsample 100 sets with 100 documents per set"), but there is no indication that multiple subsamples were drawn or that error bars were computed. This makes it difficult to assess the reliability of the reported gains, especially for benchmarks with few sets (9–13 sets for License and Instructions). While the improvements are large and consistent, error bars would substantially strengthen the claims.

2. **Absence of a random-set control condition.** The central claim is that leveraging the *set assumption* (a meaningful, metadata-based grouping of documents with shared membership) improves MI. However, the experiments only compare Set-MI (averaging over constructed sets) with Individual-MI. The paper does not test whether averaging over *random* groupings of documents (where the set assumption does not hold) would produce similar improvements. If simple variance reduction from averaging drives the gain, then the specific contribution of the set assumption is less clear. Section 6's noise analysis partially addresses this by showing that violating the set assumption hurts performance, but a direct random-set control would be a cleaner test.

3. **Single target model for Language and Instructions benchmarks.** The paper acknowledges this (Section 5.1: "We use a single target model for Language and Instructions"), but the results on these two benchmarks are therefore model-specific and may not generalize. Given that these benchmarks cover distinct domains (multilingual Wikipedia and instruction-tuning datasets), replication across additional models would strengthen the evidence.

4. **Date-based membership not directly validated.** For Wikipedia and Arxiv, membership is determined by whether creation date is before the Pile's data collection date. The paper does not verify that *all* documents from a given creation date are actually present (or absent) in the Pile according to this cutoff. Small discrepancies (e.g., articles deleted before the snapshot, missing creation-date fields) could introduce noise. The robustness analysis in Section 6 partially mitigates this concern, but a direct n-gram overlap check would be more definitive.

### Trivial

1. **Figure 4 left caption clarity.** The figure is labeled "Loss Attack" but the caption reads "Performance of Set-MI with Loss Attack under varying document lengths." While the intent is understandable, labeling could be clearer about whether this shows Individual-MI or Set-MI results.

## Nice-to-Haves

- **Set-level evaluation as a complementary metric.** Computing AUROC at the set level (treating each set as one prediction unit) would serve as a useful sanity check, even though per-document AUROC with tied scores is mathematically sound and does not inflate results (see Removed Points). It would also more directly answer "can we predict which sets are members?"
- **Bootstrapped confidence intervals.** Resampling over sets or over multiple subsamples would provide error bars for the main results without requiring additional model training.
- **Discussion of computational overhead.** The paper could briefly note that Set-MI requires computing Individual-MI scores on all documents in a set, which is O(n) per set, but this is standard in MI pipelines.

## Removed Points (treated with caution)

The following criticisms from the harsh reviewer were removed after verification against the paper:

1. **"Evaluation metric inflates Set-MI performance" (Critical Issue 1).** This claim is factually incorrect. The AUROC metric is rank-based and handles tied scores appropriately (by averaging tied ranks). As shown mathematically, per-document AUROC with tied-set scores produces the *same* result as set-level AUROC — there is no systematic inflation. The comparison with Individual-MI is fair; both methods are evaluated on the identical per-document prediction task.

2. **"Set-MI scores not directly comparable."** The paper's statement that scores are "directly comparable" (Section 3) is accurate — both Individual-MI and Set-MI produce scores in the same range, evaluated with the same per-document AUROC metric.

3. **"Set-MI worse for small models not explained."** The paper *does* explain this: "This is because Individual-MI is not effective (AUROC under 0.5) with these small models, making Set-MI aggregating opposite signals as discussed in Section 5.1" (line 139).

4. **"Correlation coefficient is unreliable."** The correlation of 0.824 (p=0.0002) between Individual-MI and Set-MI performance is computed over 20 data points (5 benchmarks × 4 methods). With n=20 and r=0.824, the p-value is well under 0.001, so the result is statistically sound.

5. **Formatting/style nitpicks.** Criticisms about figure labeling, missing appendices, and other parser artifacts that do not affect the scientific contribution.

## Novel Insights

An interesting structural observation emerges from this set of reviews: the most serious-sounding criticism (per-document AUROC with tied scores being "inflated") turns out, upon mathematical examination, to be unfounded — AUROC is invariant to the number of ties per score; it measures ranking discrimination. This suggests that the paper's evaluation methodology is actually sound as-is. The genuine remaining concerns (lack of error bars, no random-set control) are real but incremental improvements, not structural flaws. A second insight is that the paper's contribution is somewhat understated: by constructing set-based benchmarks that mirror real-world metadata groupings (dates, licenses, languages), the paper does more than propose a method — it identifies a *class* of MI problems where the task shifts from "is this single document a member?" to "is this natural group a member?", which is arguably a more practically useful framing for many real applications (e.g., detecting copyrighted datasets or evaluating test-set contamination).

## Suggestions

1. **Add confidence intervals or error bars** to the main results (Table 2), ideally via bootstrapping over sets or multiple subsampling seeds. This is the most impactful improvement and directly addresses the main evidential concern.

2. **Add a random-set control experiment**: randomly shuffle documents into sets of the same sizes as the actual sets and apply Set-MI. Showing that the improvement disappears (or is significantly smaller) would directly confirm that the *set assumption* drives the gain rather than simple variance reduction.

3. **Add a set-level AUROC as a complementary metric** to the main table, to make the evaluation directly interpretable at the set level and avoid any lingering confusion about evaluation units.

4. **Validate the date-based membership** for Wikipedia and Arxiv with an n-gram overlap check against the Pile, or at least acknowledge the potential noise and discuss its likely impact.

## Score and Decision

This paper makes a clean, novel contribution to membership inference for language models. The set assumption is well-motivated, the method is simple and broadly applicable (orthogonal to any Individual-MI method), the benchmarks are diverse and realistic, and the empirical results are consistent and substantial. The weaknesses that survive scrutiny are minor and addressable — no error bars and the absence of a random-set control are the main ones, but neither threatens the core claim given the large and consistent improvements. The paper is a solid piece of work that will be of interest to the privacy, NLP, and training-data analysis communities.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
Now I have a thorough understanding of the paper and can verify the reviewer claims. Let me construct the final consolidated review.

## Summary

The paper introduces Set-MI, a method that aggregates membership inference scores over documents sharing a common attribute (e.g., creation date, language, license) under the assumption that all documents in a set share the same membership status. On five newly constructed benchmarks spanning diverse domains, Set-MI improves four prior Individual-MI methods by 0.14 AUROC on average. The paper further provides analyses of model size, deduplication, document length, set size, and robustness to violated set assumptions.

## Strengths

1. **Novel set-based reformulation with consistent, substantial gains.** The paper identifies that individual document signals for membership inference are weak and proposes aggregating over documents that share a common attribute. Set-MI improves four prior Individual-MI methods by 0.14 AUROC on average across all five benchmarks (Table 2), and the improvement is consistent across methods and domains.

2. **Five diverse, realistic benchmarks demonstrating broad applicability.** The benchmarks span Wikipedia, Arxiv, Language, License, and Instructions (Section 4, Table 1). Three of these (Language, License, Instructions) rely on ground-truth membership derived directly from the model's known training data composition, not proxy heuristics. This diversity supports the claim that the method generalizes beyond a single domain.

3. **Systematic robustness analysis against violation of the set assumption.** Section 6 explicitly evaluates noise in member and non-member sets with ratios from 0.0 to 0.9, comparing MAX, MIN, and FULL aggregation methods (Figure 5). All three aggregations outperform Individual-MI under noise, and the analysis provides practical guidance on aggregation choice.

4. **Ablations on factors affecting Set-MI yield actionable insights.** The paper analyzes target model size (70M to 12B), training data deduplication, document length, and set size (Sections 5.2–5.5). Key findings—larger models amplify Set-MI gains, deduplication reduces the advantage, and a set size of 3 already improves over Individual-MI—help practitioners understand when and how to apply the method.

5. **Method is orthogonal and plug-and-play.** Set-MI is defined as simple averaging over membership scores from any Individual-MI method (Section 3, Equation 3). Results in Table 2 show consistent improvement across Loss Attack, LiRA, Min-K% Prob, and zlib entropy, demonstrating the method does not require redesigning the underlying scorer.

## Weaknesses

### Fatal
None.

### Major

1. **Ground-truth membership for Wikipedia and Arxiv benchmarks relies on an unvalidated date-based heuristic.** The paper labels documents as members if their creation date is before the Pile's collection cutoff (2020-03-01 for Wikipedia, 2020-08-01 for Arxiv), without verifying actual overlap with the Pile (line 109). The Pile used specific dumps—not every article or paper that existed at those dates—so documents created before the cutoff but absent from the specific dump used by the Pile (e.g., deleted Wikipedia articles, Arxiv papers not in the snapshot) would be mislabeled as members. This introduces systematic label noise in 2 of the 5 benchmarks used for the main results in Table 2. The robustness experiments in Section 6 simulate this kind of noise (documents within a set with opposite membership) and show Set-MI is robust, but they do not validate the actual noise level in the Wikipedia/Arxiv benchmarks. The authors should have either (a) verified membership via direct 13-gram overlap with the Pile (as done in Section 6) for the main experiments, or (b) discussed the potential impact. That said, this weakness is mitigated by (i) the three other benchmarks using reliable ground truth also showing strong gains, and (ii) the robustness analysis covering the relevant noise regime.

2. **Document-level AUROC with tied scores within sets conflates set-level and document-level evaluation.** Set-MI assigns the same aggregated score to every document in a set (line 64–68). Computing AUROC over individual documents means that correct set-level predictions produce many correct document-level predictions simultaneously, which does not require that scores are informative at the individual document level. A complementary set-level evaluation (AUROC over sets, where each set contributes one prediction and one ground-truth label) would clarify whether the improvement reflects genuine discrimination between member-sets and non-member-sets. While document-level AUROC is standard in MI and the comparison between Individual-MI and Set-MI is fair (both evaluated at the document level), the paper would benefit from set-level analysis or at minimum a discussion of why document-level evaluation is appropriate despite the tied scores.

### Minor

1. **No statistical significance or confidence intervals reported.** The paper does not provide confidence intervals for the reported AUROC gains. Given that sets are not independent, the effective sample size is smaller than the number of documents. While this practice is common in MI papers, reporting variability (e.g., across shuffled subdivisions of the data) would strengthen the claims.

2. **The 30% threshold for MAX and MIN aggregation is arbitrary and unablated.** The choice of using the top/bottom 30% of scores for MAX/MIN aggregation (line 168) is presented without justification or ablation. While this does not invalidate the results—FULL aggregation also works well—an ablation over different percentile thresholds would provide practical guidance on parameter choice.

### Trivial
None.

## Nice-to-Haves

- **Practical case study.** The paper would benefit from a concrete demonstration of Set-MI in a realistic downstream application (e.g., inferring the time cutoff of an unseen model's training data, or detecting dataset contamination). This would show the method works in the scenarios that motivated it, not only in constructed benchmarks.
- **Discussion of computational overhead.** Set-MI requires scoring multiple documents per set. A brief note on the computational cost relative to Individual-MI would help practitioners assess the trade-off.
- **Comparison against random grouping.** Showing that averaging over random groups of documents (ignoring the set assumption) does not improve performance would further justify why the structured set assumption is essential.

## Removed Points

These points were flagged by reviewers but are removed or downgraded after verification against the paper:

- **"Set-level AUROC is more appropriate than document-level."** Moved from "Critical Issue" to Major (point 2 above). The document-level AUROC comparison is fair and standard; the concern about tied scores inflating the metric is overstated because standard AUROC computation handles ties correctly. However, a complementary set-level analysis would strengthen the paper, so this is retained as a Major but reframed.
- **"Choice of 30% for MAX/MIN arbitrary."** Moved from potential major to Minor. The FULL aggregation method also works well, so this choice does not threaten the main claims.
- **"Missing discussion of computational overhead."** Moved to Nice-to-Haves. Not a weakness per se.
- **"Should mention that random grouping would not work."** Moved to Nice-to-Haves. A reasonable suggestion but not a flaw.
- **"Robustness experiment simulates different kind of noise."** The robustness experiment actually simulates the same kind of noise (documents within a set having opposite membership) that would arise from imperfect date-based labeling. The critic's claim that it's a "different kind" is inaccurate.

## Novel Insights

The reviews surface a useful tension: the paper's main empirical contribution rests on a clean set assumption, but the Wikipedia/Arxiv benchmarks validate this assumption through a proxy (date) rather than direct verification. The robustness experiment partially bridges this gap, but a direct n-gram overlap check for the main experiments would have been straightforward and would eliminate this concern entirely. The AUROC concern, while raised prominently, is less serious than it appears—standard AUROC handles tied scores correctly, and the comparison is fair—but the broader point that set-level evaluation would be complementary is well-taken. The most interesting open question the reviews surface is: does Set-MI genuinely improve discriminative power at the document level, or does it simply exploit the statistical aggregation of weak signals? The paper's own ablation on set size (with size 3 already helping) suggests the former, since three documents is a very small pool for "statistical smoothing" alone to drive the improvement.

## Suggestions

1. **Validate ground-truth labels for Wikipedia and Arxiv.** Use 13-gram overlap with the Pile (as done in Section 6) to directly verify membership for the main experiments, or quantify the mismatch rate and show that results are robust to the observed noise level.
2. **Add set-level AUROC as a complementary metric** to disentangle set-level discrimination from the document-level evaluation with tied scores.
3. **Report variability** (e.g., across multiple subsamples of data) for the main AUROC results.
4. **Ablate the 30% threshold** for MAX/MIN aggregation, or provide a principled justification.

## Score and Decision

The paper makes a clear, well-motivated contribution with consistent empirical results across diverse benchmarks. The main concerns—unvalidated date-based labels for two benchmarks and the document-level AUROC with tied scores—are substantive but addressable, and the three other benchmarks with reliable ground truth independently support the core claim. The robustness analysis and ablations are thorough. I recommend acceptance.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
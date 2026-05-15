Now I have all the information needed to produce the consolidated review.

---

## Summary

This paper introduces Set-MI, a method for membership inference that leverages the "set assumption"—the insight that documents sharing certain attributes (e.g., creation date, license type, language) are likely to be either all present in a model's training data or all absent. By aggregating individual-document membership scores over such sets, Set-MI significantly improves AUROC over four existing Individual-MI methods (Loss Attack, LiRA, Min-K% Prob, zlib entropy) by an average of 0.14 across five new benchmarks covering Wikipedia, Arxiv, Language, License, and Instructions.

## Strengths

- **Novel and well-motivated formulation.** The set assumption is a genuinely new perspective on membership inference for language models, and the paper clearly demonstrates that it is orthogonal to any individual-based MI method. The consistent gains across four prior methods and five benchmarks (Table 2) provide strong evidence that the set-level signal is more reliable than individual-document loss. The correlation analysis (0.824, p=0.0002) between Individual-MI and Set-MI performance further shows that future improvements to individual scoring will translate to Set-MI.

- **Diverse, reproducible benchmarks.** The paper constructs five benchmarks spanning different domains and natural set structures (date-based for Wikipedia/Arxiv, language-based, license-based, dataset-based for Instructions), each linked to publicly documented training data (Pile, BLOOM's language selection, SILO's license filtering, Tulu's instruction datasets). These are the first set-based MI benchmarks for language models and constitute a reusable resource.

- **Thorough factor analysis.** The paper provides controlled experiments on model size (70M–12B, Figure 3 left), training data deduplication (Figure 3 right), document length (16–2,048 tokens, Figure 4 left), set size (1–100, Figure 4 right), and three aggregation strategies under noise (MAX, MIN, FULL, Figure 5). Key findings—such as Set-MI benefiting more from larger models and duplicated data, and requiring as few as 3 documents per set to show gains—offer practical guidance.

- **Clear integration with prior work.** The method is presented as a drop-in extension to any existing Individual-MI method and follows a simple averaging formula, making it easy to adopt and build upon.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Potential label noise from deduplication in main results.** For the Wikipedia and Arxiv benchmarks, ground-truth membership is labeled based on creation date relative to the Pile's collection cutoff (lines 109–110). The main results (Table 2) use Pythia-12B-dedup, a model trained on the deduplicated Pile. Deduplication can remove documents that nonetheless meet the date criterion, meaning some documents labeled as "members" may actually be absent from training. The paper partially addresses this through the deduplication analysis in Section 5.3 (showing Set-MI degrades on deduped models, consistent with this concern) and the robustness analysis in Section 6 (which constructs a "clean version" using 13-gram overlap for verification on Pythia 2.8B). However, the main results on the 12B-dedup model do not verify actual document presence, so the reported AUROC values may be slightly affected by label noise. The paper would benefit from either reporting verified membership statistics or noting this caveat more explicitly.

- **Narrow robustness evaluation.** The noise simulation in Section 6 randomly flips membership labels of a fraction of documents in each set. While this is a valid starting point, real violations of the set assumption are often systematic (e.g., deduplication removing certain document types, quality filtering excluding documents above a length threshold, or language-based filtering). Random noise is plausibly the most forgiving pattern for aggregation-based methods. The robustness analysis is informative but does not fully support the paper's claim of "practical robustness" without evaluation under more structured noise scenarios. This does not invalidate the results but limits the strength of the robustness claims.

### Trivial
- The abstract states that Set-MI "brings up the limit of MI to inspect the training data of LMs on a practically robust level" — this phrasing slightly overstates the results, as the AUROC gains, while significant, still leave room for improvement (many settings remain below 0.8 AUROC). A more measured framing would be appropriate.

## Nice-to-Haves
- For the deduplication concern: report what fraction of date-labeled "members" are actually present in the deduplicated training data (e.g., via n-gram overlap checks). If the noise is small, this reassures; if it is large, it provides a more realistic characterization of the benchmark.
- For robustness: include at least one structured noise scenario, such as removing the longest documents from each set (simulating quality-based filtering), to test whether Set-MI is robust under systematic violations of the set assumption.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"No control for random aggregation"** (from Harsh Critic). The critic argues that without comparing Set-MI against averaging scores over *randomly grouped* documents, the improvement could be due to variance reduction rather than the set assumption. This is removed because it misunderstands the paper's contribution. Random groups would mix members and non-members, producing a blended score with no meaningful mapping to individual membership—it is not a valid MI method. The paper's relevant control is the comparison between Individual-MI (set size = 1, no aggregation) and Set-MI (set size > 1 with shared membership), and the monotonic improvement with set size (Figure 4 right) directly demonstrates that larger shared-membership sets yield stronger signals. The robustness experiments (Section 6) further show that when the set assumption is violated (noise introduced), performance degrades, confirming that the shared-membership property is the driver.

- **"Missing applications to real-world use cases"** suggestion from Harsh Critic. This is scope creep: the paper explicitly constructs benchmarks for detecting membership in copyright/license/time-cutoff scenarios and makes its core contribution (the set assumption + aggregation) clear. Demanding a specific deployment demonstration goes beyond what is expected for a methodological paper.

- **Criticism about missing verification of actual membership** was kept in a weakened form (see Minor weaknesses) rather than in the strong form the critic presented ("AUROC scores in Table 2 may be unreliable"). The paper already addresses this through the 13-gram verification in Section 6 and the deduplication ablation in Section 5.3, so the concern is valid but not as severe as the critic characterized it.

## Novel Insights

Beyond the paper's own contributions, the most interesting emerging observation is the interaction between deduplication and set-based aggregation. The paper shows (Figure 3, right) that Set-MI's advantage over Individual-MI is substantially larger on unduplicated models than deduplicated ones. This suggests that deduplication does not merely reduce memorization uniformly, but specifically disrupts the *correlated* memorization across documents that Set-MI exploits. In other words, deduplication appears to remove not just individual memorized examples, but the shared signals that tie documents together in attribute-based sets—pointing to a potentially deeper relationship between data curation and the structure of model memorization that future work could investigate.

## Suggestions

1. **Verify membership for the deduplicated case.** For the Wikipedia/Arxiv benchmarks on Pythia-dedup models, report the overlap between date-based labeling and actual training set presence (e.g., using 13-gram overlap or similar). Include this as a column or footnote in Table 2, or as an ablation in the supplement. Even if the overlap is high, documenting it would strengthen confidence in the main results.

2. **Add a structured noise experiment in Section 6.** For example, remove the longest 30% of documents from each set (simulating a length-based filter) or remove documents from specific duplicate clusters. This would directly test robustness under the kind of systematic violation most likely to occur in practice, and would substantially strengthen the claim of practical robustness.

3. **Tone down the "practically robust" language** in the abstract/introduction. The results are impressive for an MI method but many AUROC scores remain in the 0.6–0.75 range, which may not meet practical thresholds for production use. A more measured claim (e.g., "significantly more robust than Individual-MI") would be more accurate.

## Score and Decision

**Originality:** 7/10 — The set assumption is a genuinely new formulation for MI in LMs.  
**Importance of research question:** 8/10 — MI is a critical tool for transparency in LLMs.  
**Claims supported:** 7/10 — Core claim is well-supported; minor caveats around dedup labeling and noise evaluation.  
**Soundness of experiments:** 7/10 — Broad and systematic, with one gap (label verification for dedup models in main results).  
**Clarity of writing:** 7/10 — Clear structure; some overstatement in the abstract.  
**Value to the community:** 8/10 — The benchmarks and the simple, drop-in method are likely to be useful.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
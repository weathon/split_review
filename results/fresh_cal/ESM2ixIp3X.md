Now I have all the evidence needed. Let me produce the consolidated review.

---

## Summary

This paper revisits similarity-based metrics for summary factual consistency detection, showing that prior poor performance was an artifact of comparing summaries against reference texts rather than source documents. It proposes SBERTScore, which extends BERTScore to the sentence level using sentence transformers, enabling sentence-to-sentence comparison between summary and source. Experiments on a 9-dataset benchmark demonstrate that SBERTScore achieves competitive performance (69.27 balanced accuracy on CNNDM) against trained NLI/QA factuality metrics like QAFactEval (69.61) while requiring no domain-specific training, and that different metrics capture complementary error types.

## Strengths

- **Central claim validated by clean ablation (Table 3):** The paper pinpoints exactly why similarity-based metrics previously appeared useless: using reference summaries instead of source documents. Table 3 shows BERTScore rises from ~50% (near-chance, reference-summary) to 65.11% balanced accuracy (source-summary). This is a crisp, unambiguous experiment that directly supports the paper's core thesis.

- **SBERTScore competitive with trained metrics in zero-shot (Table 7a):** SBERTScore achieves 69.27 balanced accuracy on the CNNDM split, matching the trained QAFactEval (69.61) and outperforming all zero-shot NLI/QA baselines. This is a strong result given that SBERTScore requires no dataset-specific training.

- **Uniquely high recall on correct summaries (Table 8a):** SBERTScore achieves 72.79 recall on correct summaries (CNNDM), far exceeding the next best (SummaC_ZS at 62.58, BERTScore at 56.85). This is a practically valuable property — a low SBERTScore strongly signals an unfaithful summary — and is a novel finding not previously claimed for similarity-based metrics.

- **Formal complexity analysis (§3.1):** The paper derives O(N+M) runtime complexity for SBERTScore versus O(NM) for NLI-based metrics and even higher for QA-based metrics, providing a principled argument for computational efficiency beyond just empirical results.

- **Metric combination reveals complementarity (Figure 1):** The logical AND combination of SBERTScore with SummaC_ZS or BERTScore improves balanced accuracy beyond both individual metrics, supporting the claim that different metrics capture different error types and pointing toward a practical direction for future work.

- **Negation case study with concrete numbers (Table 5):** The four-sentence example quantitatively shows BERTScore assigning 0.95 to a negated pair (failing) while SBERTScore assigns 0.74, providing transparent, inspectable evidence that sentence-level comparison better handles negation.

## Weaknesses

### Fatal
None.

### Major

- **Runtime results promised but absent (§3.1):** The paper states "We randomly sampled 1000 pieces of data from the benchmark, and test the runtime of QuestEval, SummaC_{ZS,Conv}, BERTScore and SBERTScore on Intel(R) Core(TM) i9-10900X CPU @3.70GHz with NVIDIA A5000" — but no runtime numbers appear anywhere in the paper. Since computational efficiency is a core motivation (zero-shot, fast inference), this missing analysis leaves an important empirical claim unsubstantiated. This is a straightforward omission that should be fixed.

### Minor

- **Training data overlap not fully discussed:** The paper carefully excludes DAE from the XSum split because "it is trained on human annotated XSum validation set which overlaps with the benchmark dataset" (line 190). However, the same concern applies to SummaC_Conv and QAFactEval — both may have components trained on data overlapping with benchmark datasets (e.g., FactCC data used for training NLI models). This does not invalidate the main results (SBERTScore is already zero-shot), but the asymmetry in treatment should be resolved by explicitly stating the training data composition of each compared metric.

- **Multiple testing correction not applied:** Significance is reported via t-tests for "best vs. second-best" comparisons across many datasets and metrics. With 9+ datasets and dozens of pairwise comparisons, some significant results will arise by chance. Some correction (Bonferroni, Holm, or FDR) would substantially strengthen the statistical grounding of the quantitative claims.

- **Threshold selection criterion unspecified (§4.2):** The paper says thresholds are "selected using the validation set" but does not state the optimization criterion (maximizing balanced accuracy? F1? Youden's index?). This affects reproducibility and the interpretation of reported balanced accuracies.

- **Abstract phrasing slightly over-broad:** The abstract states SBERTScore "outperforms widely-used word-word metrics including BERTScore," but SBERTScore underperforms BERTScore on the XSum split (Table 7b: 59.21 vs. 56.02). The paper honestly discusses this in §5.5, so the abstract should be qualified (e.g., "outperforms on aggregate" or "across most settings").

### Trivial

- **Results on small datasets not caveated:** The benchmark includes small datasets (XSF: 148 examples, XENT: 76 examples). The paper reports individual results (Table 6) without noting that these are noisy. Aggregated splits help, but a brief caveat would improve rigor.

- **Length limit truncation not analyzed:** The paper notes 45.76% of source documents exceed 512 tokens and are truncated, but does not analyze whether truncation correlates with metric performance degradation. This is a reasonable limitation to quantify.

## Nice-to-Haves

- Scaling the negation case study to a small corpus of contrastive pairs (e.g., from TrueTeacher) would turn an illustrative example into an empirical finding.
- An analysis of the relationship between SBERTScore/BERTScore and summary/source length would help explain the XSum discrepancy and potential length biases.
- A simple learned combination (e.g., logistic regression on validation set scores) would provide a stronger baseline than logical AND/OR for the metric combination experiment.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Figure 1 threshold reuse unspecified":** Removed — the paper states thresholds are selected per metric on the validation set (§4.2), and the AND/OR combination simply applies those same thresholds, which is straightforward.
- **"More effective at detecting various error types claim unsupported":** Removed — Table 8 shows error-type recall and Figure 1 shows improved performance from combining metrics; the claim is adequately supported.
- **"§3 granularities not explained before experiments":** Removed — the paper lists the three granularities and explicitly references §5.3 for full evaluation, which is standard practice.
- **"Negation case study too thin":** Removed — the paper honestly acknowledges the limitation in its own conclusion ("not sensitive enough"), and the example is illustrative, not a substitute for a large-scale evaluation.
- **"Missing runtime measurements" conflict with Strength Finder:** The Strength Finder claimed the paper "provides runtime measurements on 1000 samples, showing the proposed metric is substantially faster" — this claim is factually incorrect (no runtime numbers appear); it is removed as a strength and retained as a weakness above.
- **Generic strengths ("important problem," "targeted interesting question"):** Removed as superficial.
- **Formatting, style, or typographical observations:** Removed as parser artifacts.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add a runtime table** to §3.1 (or an appendix) reporting actual inference time per 1000 samples for QuestEval, SummaC_{ZS,Conv}, BERTScore, and SBERTScore. This directly supports a core claim (computational efficiency) and is already described as having been done.
2. **Explicitly state each compared metric's training data composition** and any overlap with benchmark datasets, consistent with the treatment already given to DAE.
3. **Specify the threshold selection criterion** (e.g., "maximizing balanced accuracy on the validation set") in §4.2 for reproducibility.
4. **Add a multiple-testing correction** (Bonferroni or FDR) to the significance reporting, or clearly state which comparisons are pre-planned versus post-hoc.
5. **Qualify the abstract** to reflect that SBERTScore outperforms BERTScore on aggregate / on CNNDM but not on XSum.

## Score and Decision

This is a solid, well-executed empirical paper. The core contribution is clearly demonstrated (Table 3), the proposed method performs respectably against trained alternatives (Table 7a), and the error-type analysis (Table 8) reveals practically useful properties. The missing runtime results are the most significant gap — a straightforward omission that is fixable in revision. No weaknesses threaten the paper's central claims.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
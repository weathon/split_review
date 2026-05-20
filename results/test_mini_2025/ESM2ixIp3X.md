Now I have good calibration anchors. Let me write the consolidated review.

**Round-1 bracket**: 4.5–6.5 (between weak anchors at ~3.0 and strong anchors at ~8.0).

**Round 2 narrowing**: I compared against SimlDuN0YT (5.5, Poster), XJiN1VkgA0 (6.0, Reject), Rry1SeSOQL (6.75, Spotlight), and E8gYIrbP00 (6.75, Poster). The paper under review is more thorough than SimlDuN0YT (9 datasets vs 3, cleaner experimental design) and comparable to XJiN1VkgA0 in soundness, but the confounding issue prevents it from reaching the 6.75 level of Rry1SeSOQL where contributions are cleanly isolated.

**Final score: 6.0.** The paper makes a clear empirical contribution (reference-vs-source finding), proposes a sensible metric, and evaluates thoroughly. The main weakness is the confound between backbone model and granularity, which is acknowledged but not fully disentangled.

---

## Summary

This paper revisits similarity-based metrics for summary factual consistency detection. It makes two key empirical findings: (1) prior failures of metrics like BERTScore stemmed from comparing against reference summaries rather than source documents (Table 3), and (2) extending similarity-based metrics to sentence-level comparison (proposed SBERTScore) improves performance further. The paper evaluates on a benchmark of 9 datasets against NLI/QA-based metrics, showing that zero-shot similarity-based metrics are competitive with trained alternatives. It also analyzes error complementarity across metrics and shows that logical AND combination improves balanced accuracy.

## Strengths

- **Key finding that reference vs. source comparison explains prior underperformance (Table 3):** BERTScore goes from 0.500 (near-random) using references to 0.759 using source documents. SBERTScore goes from 0.499 to 0.779. This directly shows that the widely-reported failure of similarity-based metrics was an artifact of comparing against reference summaries, not a fundamental limitation of the approach. This is the paper's most compelling empirical result.

- **Thorough multi-dataset evaluation (Tables 6–7):** The paper evaluates SBERTScore on 9 distinct factuality datasets spanning different summarization systems (BART, PEGASUS, BERTSumAbs) and two source domains (CNN/DM, XSum). Results are reported as balanced accuracy, ROC-AUC, and correlation coefficients, with statistical significance tests. This is substantially more comprehensive than typical evaluation in this space.

- **Computational efficiency is a practical advantage (Section 3.1):** SBERTScore is O(N+M) in backbone calls vs. O(NM) for NLI-based alternatives. Runtime measurements confirm it is ~3× faster than SummaC_{ZS,Conv} and ~30× faster than QuestEval. For practitioners deploying factuality checks at scale, this is a meaningful advantage over trained alternatives.

- **Error complementarity analysis is informative (Table 8, Figure 1):** SBERTScore achieves the highest recall on correct summaries on CNN/DM (0.522 vs. next-best 0.436), meaning it rarely misjudges faithful summaries as inconsistent. The low Cohen's κ across metrics (< 0.45) and the AND combination results showing gains over individual metrics (e.g., QAFactEval+DAE: 0.828 vs. 0.817/0.807 individually) provide practical guidance for deploying multiple metrics.

## Weaknesses

### Major

None. The paper's core claims are empirically supported and no single issue invalidates them.

### Minor

- **Confounding of embedding model and aggregation method (Tables 2, 4):** The paper attributes SBERTScore's improvement over BERTScore to sentence-level comparison, but the two metrics use different backbone models — RoBERTa-large for BERTScore and `all-roberta-large-v1` (Sentence-BERT fine-tuned with contrastive learning) for SBERTScore. The paper acknowledges this ("the improvement is brought by both the architecture and the appropriate text granularity," line 171), and the data in Table 4 does show that SBERTScore Sent-Sent (0.779) improves over SBERTScore Word-Word (0.767), indicating a genuine granularity effect. However, the word-level SBERTScore (0.767) already outperforms BERTScore (0.759), so the backbone swap itself accounts for roughly 40% of the total gain (0.008 of 0.020). A controlled experiment using the same backbone with both aggregation methods would cleanly separate the two factors. Without this, the precise contribution of sentence-level aggregation per se is unclear.

- **Unclear benchmark aggregation for Figure 1:** The diagonal values in Figure 1 do not obviously match any macro- or micro-average computable from Tables 6 and 7. For example, QAFactEval's diagonal is 0.817, but its per-dataset scores in Table 6 range from 0.604 to 0.843, and its CNNDM/XSum split scores are 0.757/0.705. The caption says "average balanced accuracy on a benchmark" without specifying the aggregation method (macro, micro, weighted, or over which subset). This makes the metric combination results harder to interpret than they should be. The authors should clarify the aggregation and ensure consistency with earlier tables.

- **XSum limitation is real but acknowledged (Table 7b):** SBERTScore drops to 0.605 on XSum vs. BERTScore's 0.695. The explanation — single-sentence summaries prevent meaningful sentence-level averaging — is plausible and the paper discusses it openly. This is a genuine scope limitation worth noting but not a flaw in reporting.

- **Metric combination evaluated only with logical AND/OR on pairs (Figure 1):** The combination analysis is limited to binary logical operations on metric pairs. A more principled approach (e.g., logistic regression or a learned weighting of metric scores) could yield stronger results and connect better to real-world usage. The current analysis is a useful proof of concept but leaves practical deployment questions open.

### Trivial

None.

## Nice-to-Haves

- A controlled comparison using the *same* backbone (RoBERTa-large) at both word level (mean-pooled sentence embeddings) and sentence level (as in SBERTScore) would cleanly quantify the granularity contribution.
- The precision/recall tradeoff for inconsistency detection could be reported alongside the recall-on-correct-summaries analysis in Table 8.

## Removed Points

- **Weakness about "Strengthening the Paper on Its Own Terms" suggests (logistic regression, etc.):** These are suggestions for improvement, not weaknesses of the current paper. The paper's scope is clearly bounded, and logical AND/OR is a reasonable minimal demonstration of complementarity.
- **Harsh critic's claim about "missing significance testing for error-type recall" (Table 8):** The paper does report statistical significance (underline indicates p < 0.05). The critic appears to have missed this.
- **Strength Finder's generic praise ("addresses an important problem," "timely topic"):** Removed as superficial; only concrete, evidence-backed strengths are retained.
- **Harsh critic's comment about SummaC_{ZS} complexity being O(NM):** This is a minor disagreement about framing, not a substantive weakness. The paper already provides runtime measurements.
- **Criticism about "no systematic analysis of negation in benchmark data":** The case study is appropriately scoped as illustrative.

## Novel Insights

None beyond the paper's own contributions. The reviewers did not surface observations about the paper that the authors themselves do not already state or imply.

## Suggestions

1. Run the controlled experiment: compare BERTScore using mean-pooled RoBERTa-large sentence embeddings against SBERTScore using `all-roberta-large-v1`. Report both at word-word and sentence-sentence granularity. This cleanly separates backbone and granularity contributions.
2. Clarify the aggregation method used for Figure 1's diagonal values and ensure consistency with per-dataset results in Tables 6–7. A footnote describing whether values are macro-averaged, micro-averaged, or weighted by dataset size would resolve the ambiguity.
3. Consider presenting precision and F1 for inconsistency detection alongside the existing recall analysis in Table 8, giving a fuller picture of SBERTScore's detection profile.

## Score and Decision

**Round 1 bracket:** 4.5–6.5

**Round 1 anchors (by band):**
- Weak (score < 3.5): B37UmlxsaP (2.50), kTjEPEy96Q (3.00), OdoS6cH8MP (2.00), qb2QRoE4W3 (3.00), yiPtWSrBrN (3.00) — lower quality, unrelated topics.
- Mid (3.5–7.5): 0pbxX2jatP (4.33, BERTScore-based inconsistency), GXzwq6waYb (4.25, semantic clustering for hallucination), MEztAJjcYZ (4.25, clinical summarization), YFOg1LUGG1 (5.50, hallucination detection with confounds), 5rrYpa2vts (4.00, fake news detection).
- Strong (> 7.5): Iyrtb9EJBp (8.00), WbWtOYIzIK (8.00), UHPnqSTBPO (8.00), WCRQFlji2q (9.00), 7Ttk3RzDeu (8.50) — oral-level papers with substantially more novelty or theoretical depth.

**Round 2 anchors (narrowing to 5.5–7.0):**
- COYDmKkQH4 (5.67, Poster): different domain (event prediction), less comparable.
- SimlDuN0YT (5.50, Poster): logical consistency of LLMs. Less thorough evaluation (3 datasets vs. 9) but benchmark is novel. The SBERTScore paper is stronger empirically.
- rYyu3jpk8z (4.80, Reject): CDM text evaluation. Missing critical baselines and generalization concerns. The SBERTScore paper is clearly stronger.
- XJiN1VkgA0 (6.00, Reject): uncertainty quantification. Comparable rigor but narrower scope (QA only). SBERTScore paper is more comprehensive in evaluation.
- Rry1SeSOQL (6.75, Spotlight): MT-Ranker. Better isolation of contributions, SOTA results, cleaner ablation. The SBERTScore paper is not as cleanly isolated (confound issue) but is evaluated more broadly.
- E8gYIrbP00 (6.75, Poster): Beyond correlation. Stronger conceptual contribution and novel framework. The SBERTScore paper is more incremental but has thorough empirical results.

**Placement relative to anchors:** Comparable to XJiN1VkgA0 (6.00) in overall quality. Stronger than SimlDuN0YT (5.50) due to more comprehensive evaluation. Weaker than Rry1SeSOQL (6.75) because the confounding issue prevents clean isolation of the claimed contribution. The reference-vs-source finding (Table 3) is independently valuable and well-supported. The sentence-level contribution is modest in magnitude (0.779 vs 0.767 on the word-level variant) and partially confounded.

MY FINAL SCORE: 6.0
MY FINAL DECISION: Accept
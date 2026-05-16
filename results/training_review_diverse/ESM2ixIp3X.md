Good, I've verified the key claims against the paper. Let me now construct the final consolidated review.

---

## Summary

This paper revisits similarity-based metrics for summary factual consistency detection, showing that their previously reported failure was due to comparing against reference summaries rather than source documents. The authors propose SBERTScore, a sentence-level similarity metric using sentence transformers. Experiments on a multi-dataset benchmark show that SBERTScore (zero-shot, precision-based) outperforms token-level BERTScore and zero-shot NLI baselines, is competitive with several trained metrics, and achieves the best recall on correct summaries. The paper also demonstrates that combining diverse metrics via logical AND improves balanced accuracy.

## Strengths

- **Source-document comparison is the decisive factor.** Table 3 convincingly shows that moving from (reference, summary) to (source, summary) pairs transforms BERTScore and ROUGE from near-random to useful (~50% → ~69% balanced accuracy). This cleanly isolates the cause of prior underperformance and is the paper's most important finding.

- **SBERTScore outperforms BERTScore and zero-shot NLI baselines on the full benchmark.** Table 7a shows SBERTScore achieving 70.08 balanced accuracy vs. BERTScore (68.06) and SummaC_ZS (67.12). On the CNNDM split it reaches 72.52, second only to the trained QAFactEval (73.92). This demonstrates that a simple sentence-level similarity approach is genuinely competitive in a zero-shot setting.

- **Systematic granularity ablation isolates the source of improvement.** Table 4 tests word-word, sentence-document, document-document, and sentence-sentence variants, plus a mean-embedding simplification as a negative control. The conclusion that improvement comes from both sentence-level architecture *and* sentence-level granularity is well-supported.

- **High recall on correct summaries.** Table 8 shows SBERTScore achieves 94.7% recall on correct summaries (CNNDM split), the highest among all metrics including trained QA/NLI methods. This is a practically useful property: a low SBERTScore is a strong signal of inconsistency.

- **Metric combination via logical AND reliably improves accuracy.** Figure 1 shows that AND-combining any pair of distinct metrics yields balanced accuracy higher than either individual metric, with all improvements statistically significant. This finding is methodologically interesting and well-demonstrated.

- **Theoretical computational efficiency.** The O(N+M) vs. O(NM) complexity analysis (Section 3.1) gives a clear formal efficiency advantage over NLI-based metrics, and QA-based methods involve even heavier pipelines.

## Weaknesses

### Fatal
None.

### Major

- **Runtime experiment is designed but results are absent.** Section 3.1 describes a planned runtime experiment on 1000 data points, lists the hardware (i9-10900X CPU with NVIDIA A5000), and names the metrics to compare — but **no runtime results are reported anywhere in the paper**. Since computational efficiency is a stated motivation for similarity-based metrics (Section 2.2 calls QA-based methods "time-consuming at inference time" and notes "the evaluation process is expected to be prompt"), leaving this entirely unsupported is a significant evidential gap. The section simply ends after the hardware specification. This is not a minor omission — it is a promised experiment with missing outcomes.

### Minor

- **Contribution 3 overclaims in the contribution list.** The third bullet in Section 1 states: "introduce a simple combination that outperforms the state of the art." The AND combination (Figure 1) outperforms the *individual base metrics*, not the actual state-of-the-art metric QAFactEval (which remains the top performer on all splits in Table 7). The rest of the paper (line 29, conclusion) uses the more accurate phrasing "outperforms the individual base metrics." The contribution list should be corrected to match.

- **No ablation of the sentence embedding model.** SBERTScore uses only `all-roberta-large-v1`. The paper attributes improvement to "both the architecture and the appropriate text granularity" (Sec 5.3), but never tests other sentence transformers (e.g., `all-mpnet-base-v2`, `all-MiniLM-L6-v2`). Since the embedding model directly affects performance, the claim that the improvement is due to the *sentence-level design* rather than the specific checkpoint would be stronger with at least 1–2 alternative backbones tested. This does not invalidate the results but limits generality.

- **Threshold selection criterion unspecified.** The paper states thresholds are selected "using the validation set" (Section 4.2) but does not specify the criterion (e.g., maximizing balanced accuracy, Youden's index). This affects reproducibility.

- **Statistical significance testing details incomplete.** The paper reports t-tests with p<0.05 but does not state whether tests are one- or two-tailed, whether multiple testing corrections (e.g., Bonferroni) were applied, or how the t-test was applied to balanced accuracy (which is a proportion-based metric). Given that many significance claims are made across tables, this is a gap in methodological rigor.

- **Sentence segmentation tool not specified.** The paper segments documents into sentences but does not state which tool (spaCy, NLTK, etc.) was used. Minor, but affects exact reproducibility.

### Trivial
- "Opearating" typo in "Receiver Opearating Characteristic" (line 113).

## Nice-to-Haves
- **Test additional sentence embedding models** to demonstrate that the sentence-level approach generalizes across backbones.
- **Report the runtime numbers** that Section 3.1 already sets up — this would complete the efficiency story.
- **Decompose XSum underperformance** more directly: e.g., test whether artificially splitting multi-sentence summaries or checking whether BERTScore's token-level matching is more robust on single-sentence summaries.
- **Report truncation rates for BERTScore** (the paper reports 45.76% truncation for document-level SBERTScore but not for BERTScore's word-level 512-token limit).

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Strength Finder's "empirical runtime results" claim.** The Strength Finder states that Section 3.1 "empirically shows SBERTScore runtime is orders of magnitude lower than QuestEval and SummaC_Conv on 1000 sampled examples." This is factually incorrect — the paper describes the experimental setup but reports **zero runtime numbers**. The theoretical complexity advantage (O(N+M) vs. O(NM)) is a real strength, but there are no empirical runtime results. This falsely inflated strength is removed; the weaker-but-accurate theoretical efficiency claim is kept above.

2. **Harsh Critic's "SBERTScore is not competitive" overclaim.** The critic claims the abstract's statement that SBERTScore "can compete with existing NLI and QA-based factuality metrics" is overclaimed because QAFactEval outperforms it. However, "can compete with" is reasonable: SBERTScore (70.08) is within ~2.6 points of QAFactEval (72.70) and ~0.6 points of SummaC_Conv (70.70), while outperforming several trained metrics (DAE 66.59, FactCC 62.38). The abstract claim is accurate. The overclaim is real only for the contribution list's "outperforms the state of the art" phrasing, which is already listed as a Minor weakness.

3. **Harsh Critic's point about "unfair comparison with other methods" framing.** Not applicable — the critic did not raise this issue.

4. **Harsh Critic's point about the paper being dismissive of prior work (Bao et al., Koto et al.).** This is an opinion about tone, not a substantive weakness.

## Novel Insights

The reviews surface an interesting tension: the paper's strongest empirical finding — that similarity-based metrics work when given source documents — is robust and well-supported, but its weakest point is the absence of the runtime experiment that the paper itself promises. This creates a mismatch between the paper's stated motivations (efficiency) and its delivered evidence. The reviews also highlight that the paper's main contribution is more about *rehabilitating a dismissed approach* than about raw performance leadership, which is a valuable but easy-to-overclaim research direction. The AND-combination result is perhaps more interesting than the paper frames it: if diverse metrics reliably improve via simple AND, the field may benefit more from ensemble evaluation than from chasing the single best metric.

## Suggestions

1. **Add the runtime results.** This is the most impactful fix: a single table with mean inference time per sample for SBERTScore, BERTScore, SummaC_ZS/Conv, and QuestEval would complete Section 3.1 and directly support the efficiency motivation.

2. **Fix the overclaim in the contribution list.** Replace "outperforms the state of the art" with "outperforms the individual base metrics" or "improves over each constituent metric."

3. **Add at least one alternative sentence embedding model** (e.g., `all-mpnet-base-v2`) to the granularity ablation table to demonstrate generality of the sentence-level approach.

4. **Specify the threshold selection criterion** (e.g., maximization of balanced accuracy on the validation set) and provide details on the significance testing procedure (one-tailed vs. two-tailed, correction for multiple comparisons).

5. **State the sentence segmentation tool** used for reproducibility.

## Score and Decision

This paper makes a solid, well-evidenced contribution: it convincingly demonstrates that the prior dismissal of similarity-based metrics was premature and proposes a straightforward extension (sentence-level comparison) that performs competitively. The core findings (source vs. reference text matters; sentence-level > word-level) are clearly supported. The missing runtime results and the overclaim in the contribution list are fixable issues. No fatal flaws exist.

**Score:** 7.0

**Decision:** Accept

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
Now I have all the information needed. Here is the final consolidated review.

---

## Summary

This paper introduces the Language Confusion Gate (LCG), a lightweight decoding-time intervention that filters out-of-language tokens during LLM generation. The key technical innovation is *norm-adjusted self-distillation*: the paper first shows that output token embedding norms are systematically biased toward high-resource languages (Section 3.2), then uses this insight to train a small two-layer MLP gate via self-distillation on debiased logits. The gate predicts which of four language families (CJ, Latin, Symbols, Low-Res) are permissible at each decoding step and masks disallowed tokens only when necessary. Experiments across five model families (Qwen3, Llama3.1, Gemma3, GPT-OSS) in both standard and reasoning modes demonstrate order-of-magnitude reductions in language confusion with negligible latency overhead (0.4%).

## Strengths

1. **Mechanistic insight into token-embedding norm imbalance as a root cause of language confusion.** Section 3.2 provides a clean geometric decomposition showing that output token embedding norms are systematically biased: in Qwen3-8B, 10.74% of CJ tokens occupy the top-5% of norms while only 0.14% of low-resource tokens do (Table 1). Figure 2 demonstrates that simply dividing logits by embedding norm removes confused CJ tokens from the top-10 at a confusion point. This goes beyond prior work by identifying a specific, measurable geometric bias that the method then exploits.

2. **Order-of-magnitude confusion reduction across multiple architectures without degrading task performance.** On Qwen3-30B, CJ confusion drops from 1.0% to 0.0% and Latin confusion from 4.4% to 0.4% while BLEU stays essentially unchanged (13.2→13.4). On Qwen3-8B, CJ% falls from 4.5% to 0.1% and Latin% from 12.1% to 2.0% (Table 3). For thinking models, CJ% on Humaneval-XL drops from 1.50% to 0.06% while Pass@1 changes by ≤0.7 points (Table 4).

3. **Explicit handling of the confusion-vs.-code-switching distinction.** The paper partitions FLORES+ into FLORES-NO-LATIN and FLORES-WITH-LATIN subsets (Section 5.2), then separately evaluates LCG's effect on confusion (Table 3) and code-switching (Table 5). This is a concrete advance over approaches that cannot distinguish harmful confusion from legitimate code-switching.

4. **Norm-adjusted self-distillation validated by direct ablation.** LCG-adjusted consistently outperforms LCG-unadjusted across all models (Table 3): e.g., Latin confusion on Llama3.1-8B drops from 5.7% (unadjusted) to 2.9% (adjusted), confirming that the specific training innovation—not just the gate architecture—drives the improvement.

5. **Extremely low computational overhead.** On Qwen3-30B-A3B with 2000-token input and concurrency 8, LCG adds only 0.4% latency (15.95ms→15.99ms per step) and intervenes on only 0.33–0.38% of tokens (Section 5.3, Section 6), quantified with production-level measurement.

6. **Broad evaluation across model categories.** Covers five model families (Qwen3 at two sizes, Llama3.1, Gemma3, GPT-OSS) in both standard and reasoning modes, demonstrating generality beyond a single architecture.

## Weaknesses

### Major

1. **Missing comparison with the most closely related prior work.** The paper discusses both Ji et al. (2025) (post-hoc smoothing for Korean+Chinese confusion) and Nie et al. (2025) (neuron suppression for language mixing) in the Related Work section (Section 2), yet neither is included as a baseline. These represent the most directly comparable decoding-time intervention methods for language confusion, and the paper's central claim of outperforming prior approaches is weakened by their absence from Table 3 / Figure 3. While implementing these methods may require non-trivial effort, the paper should either include them or provide a clear justification for why they are not comparable.

### Minor

2. **Code-switching preservation evaluation lacks sufficient documentation.** The 86.7% preservation rate (Section 5.3) — which supports the paper's key differentiating claim that LCG preserves legitimate code-switching — relies on human annotation with no information about: number of annotators, inter-annotator agreement, how many examples were annotated, or the selection criteria for identifying "natural, appropriate code-switch" examples. This makes the reliability of this specific number impossible to assess. The paper would also benefit from a more transparent discussion of the code-switching reduction trade-off shown in Table 5 (e.g., Qwen3-8B code-switch rate drops from 46.34% to 25.90%, which is 32% below the ground-truth answer rate of 38.36%).

3. **FLORES-NO-LATIN subset statistics are not reported.** The paper filters FLORES+ references to remove those containing Latin characters (Section 5.2) but does not disclose the size of the resulting subset, its per-language distribution (Arabic vs. Hebrew vs. Korean vs. Thai), or how many examples remain. Since BLEU scores on this subset are unusually low (e.g., GPT-5-Chat at 10.66) and confusion rates on small subsets can be noisy, reporting the subset size and ideally confidence intervals would substantially improve confidence in the results.

4. **ORPO baseline is underspecified.** The description ("we prepare a multilingual dataset, and synthesize samples with language confusion as rejected samples similar as Lee et al. (2025)") does not include dataset size, training steps, hyperparameters, or the base model used. This makes it difficult to assess whether the comparison with ORPO is fair.

### Trivial

5. **No confidence intervals or error bars.** Confusion rates are reported as point estimates without variance information; this is common practice in the field but somewhat more concerning here because the FLORES-NO-LATIN subset size is unknown.

6. **Table 4 caption says "No-Think Models" instead of "Thinking Models."** (Table 4 is labeled as "Effectiveness of LCG Intervention on 'No-Think' Models" but describes thinking model results on Humaneval-XL.)

## Nice-to-Haves

- Token-level confusion rates alongside the reported response-level rates would provide a more complete picture of confusion severity.
- Per-language breakdowns (Arabic vs. Hebrew vs. Korean vs. Thai) for FLORES-NO-LATIN would reveal whether LCG performs uniformly across scripts.
- A rule-based language detector baseline (restrict output to target language) would provide a natural lower bound for the method's capabilities.

## Removed Points

Points from the input reviews that were filtered out with justification:

- *"Rule-based detector baseline not included"* — Removed because the paper's central claim is precisely that rule-based detectors cannot distinguish confusion from code-switching; this is an explicit part of the paper's motivation, not an oversight.
- *"Norm bias cannot fully explain language confusion"* — Removed because the paper explicitly acknowledges this limitation ("Norm bias can account for a subset of such errors but cannot fully explain language confusion"), making this the paper stating its own limitation rather than a reviewer-identified gap.
- *"Response-level metric conflates severity"* — Removed because the metric choice is explicit and defensible (a single confused character can break a translation), and the token-level intervention rate (0.33–0.38%) is already reported.
- *"Pass@1 consistently drops slightly"* — Removed because drops of 0.68–0.75 points are tiny; the paper's framing ("maintaining competitive scores") is accurate.
- *"Thinking model confusion rates undercut the drama about Large Reasoning Models"* — Removed because 1.50% CJ confusion on Qwen3-8B thinking model is non-trivial and the paper's framing is not hyperbolic.
- *"Missing related works"* — Removed per hard rules: the merger cannot identify missing related works without external sources.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add Ji et al. (2025) and Nie et al. (2025) as baselines, or provide a clear rationale for why they are not comparable.
2. Document the FLORES-NO-LATIN subset size, per-language distribution, and report confidence intervals (or bootstrap estimates) for confusion rates.
3. Provide full details of the human annotation for the 86.7% code-switch preservation experiment: annotator count, inter-annotator agreement, example count, and selection criteria.
4. Discuss the code-switching reduction cost more transparently — the current framing understates the trade-off shown in Table 5.
5. Fix the Table 4 caption error ("No-Think" → "Thinking").
6. Add per-language breakdowns for the main results.

## Score and Decision

### Calibration Anchors

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| Self-Detoxifiers (SASA) | jY5oml9fe9.md | 6.00 | 2 | LCG has stronger mechanistic motivation (norm analysis) and comparable empirical validation, placing it slightly above. |
| TransLLM | US2UCMvzvP.md | 6.25 | 2 | LCG has a more elegant method and cleaner evaluation but also shares similar baseline completeness concerns. |
| Integrative Decoding | gGWYecsK1U.md | 6.50 | 2 | Comparable quality: both have missing baselines as weaknesses, but LCG has a stronger mechanistic foundation and better practicality (0.4% vs. multiple sampling overhead). |
| CTG via Model Arithmetic | SLw9fp4yI6.md | 7.00 | 2 | Cleaner theoretical framework and broader baselines; LCG has stronger empirical evaluation on the specific problem. LCG is slightly below. |
| Babel Tower | eznTVIM3bs.md | 5.25 | 1 | LCG has a more direct practical contribution and cleaner evaluation. Clearly above. |
| Crosslingual Consistency | HMa8mIiBT8.md | 6.00 | 2 | LCG has a more concrete method contribution. Above. |
| Structural Similarities | NCrFA7dq8T.md | 6.60 | 2 | Comparable quality, different domain. |
| Llamas (mostly) Think in English | fSbPwHjdDG.md | 3.00 | 1 | LCG is clearly above this level. |

**Round 1 bracket**: Between 3.5 and 7.5. LCG is clearly stronger than weak-anchor papers (~3.0) and clearly below strong 8.0 papers.

**Round 2 narrowing**: Within the (3.5, 7.5) bracket, LCG sits between 6.0 and 7.0, closest to the 6.5 anchors. The paper's strengths (mechanistic insight, practical lightweight method, broad evaluation) outweigh its weaknesses (missing baselines, underdocumented code-switching evaluation), but the evaluation gaps prevent it from reaching the 7.0+ tier.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
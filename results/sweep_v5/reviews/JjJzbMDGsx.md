Now I have sufficient calibration. Let me write the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me write the review now.

---

## Summary

The paper introduces the Language Confusion Gate (LCG), a lightweight, plug-in decoding-time intervention that mitigates language confusion in multilingual LLMs. LCG uses a small two-layer MLP trained via norm-adjusted self-distillation to predict permissible language families (CJ, Latin, Symbols, Low-Res) at each generation step, dynamically masking tokens from disallowed families only when necessary. Evaluated across five models (Qwen3, Llama3.1, Gemma3, GPT-OSS) in both standard and reasoning modes, LCG reduces confusion rates by an order of magnitude while preserving task performance and maintaining legitimate code-switching ability.

## Strengths

1. **Mechanistically grounded method with clear ablation confirmation.** The paper identifies output token embedding norm imbalance as a bias toward high-resource languages (Section 3.2, Table 1), and uses this insight to design norm-adjusted self-distillation. The ablation (Table 3) cleanly demonstrates that LCG-adjusted consistently outperforms LCG-unadjusted across all four no-think models — e.g., Latin% on Qwen3-8B drops from 6.2% to 2.0%, and on Llama3.1-8B from 5.7% to 2.9%, confirming that norm-adjustment is essential to the gate's accuracy.

2. **Substantial empirical breadth with consistent results.** The method is tested on five model families (Qwen3-8B, Qwen3-30B, Llama3.1-8B, Gemma3-12B, GPT-OSS) across both no-think and thinking modes, on multiple benchmarks (FLORES+, INCLUDE, Humaneval-XL). Results show consistent confusion reduction — e.g., CJ% drops from 4.5% to 0.1% (Qwen3-8B, FLORES-NO-LATIN), Latin% from 12.1% to 2.0% — without degrading BLEU or accuracy, and for thinking models CJ% drops from 0.38% to 0.06% on GPT-OSS without meaningful Pass@1/10 degradation.

3. **Sparse intervention with minimal overhead.** LCG adds only 0.4% per-step latency (15.95ms → 15.99ms) and intervenes on only 0.33–0.38% of tokens (Section 6), making it practical for production deployment. The computational efficiency is a genuine advantage over retraining-based approaches.

4. **Explicit treatment of code-switching preservation.** The paper evaluates LCG's impact on legitimate code-switching — a critical concern that rule-based baselines ignore. The human-validated token-level experiment (86.7% allowance at code-switch confusion points) and code-switch rate comparisons (Table 5, remaining above the Claude Sonnet 4 baseline) provide concrete evidence that LCG does not suppress necessary multilingual behavior.

## Weaknesses

### Major

1. **Missing comparisons with two directly relevant lightweight baselines.** The related work (Section 2) cites both Ji et al. (2025) — a post-hoc smoothing method for Korean-Chinese confusion — and Nie et al. (2025) — a neuron-suppression method for language switching. Both operate at inference time without retraining, making them the most natural competitors for LCG's claimed regime. Their omission weakens the claim that LCG is superior to existing lightweight interventions. The paper compares against ICL, greedy decoding, and ORPO, but these are either weaker baselines (ICL, greedy) or a retraining-based method (ORPO) that operates in a different regime.

2. **No aggregate analysis of self-distillation pseudo-target quality at confusion points.** The training mechanism relies on the assumption that norm-adjusted top-k/p candidate sets exclude the confused language family at confusion points (Section 4.2). Only a single example is given (Figure 2). The paper would benefit from measuring, across many confusion points, how often the norm-adjusted candidate set still contains the confused-family token. The ablation (Table 3) provides indirect empirical support, but a direct analysis would substantially strengthen the paper's mechanistic claims.

### Minor

3. **No BLEU reported on FLORES-WITH-LATIN.** The code-switching evaluation (Table 5) reports only code-switch rates. While these are informative, reporting BLEU on this subset would more directly address whether LCG suppresses necessary Latin tokens that degrade translation quality. The paper's claim that LCG "preserves legitimate code-switching" is partially supported (by rate comparisons and token-level allowance), but BLEU evidence on the subset would close this gap.

4. **Latin confusion not reported for thinking models (Table 4).** Only CJ confusion is reported for reasoning models on Humaneval-XL. Since reasoning tasks (especially code generation) often produce Latin-script output, Latin confusion metrics would be informative. This is a small gap — the thinking model evaluation focuses on code tasks where CJ confusion is the primary concern — but it limits completeness.

5. **Rule 3 (persistence of previous token's language) could perpetuate confusion.** If a confused token is already generated, Rule 3 allows continuations in that language. The paper does not analyze how often this occurs in practice. This is a legitimate edge-case concern, though the low overall confusion rates suggest the practical impact is limited.

### Trivial

6. **Hyperparameters for training (learning rate, batch size, epochs, top-k/p thresholds for pseudo-target construction) are not in the main paper.** These are standard details likely in the appendix (which is stripped), but should be available for reproducibility.

7. **Human-validated code-switch analysis (86.7%) does not report the number of examples or inter-annotator agreement.** This is a minor methodological detail.

## Nice-to-Haves

- Statistical significance / confidence intervals for the main confusion rate reductions would strengthen the presentation (currently reported as single values).
- An analysis of how often confusion occurs between languages sharing the same script (e.g., Spanish vs. English) would clarify the practical scope of the script-level approach, which the paper already acknowledges as a limitation.

## Removed Points

- **Issue about "commercial models may already employ such techniques" (Section 3.4):** The paper already acknowledges this uncertainty explicitly ("we are not sure if a similar intervention mechanism… has been applied"). The reviewer is restating what the paper already says. **Removed.**
- **Criticism that the norm analysis "only reports the fraction of top-5% tokens" (Section 3.2):** Table 1 is a clear, standard way to communicate embedding norm imbalance. Requesting additional distributional statistics is scope creep — the table already communicates the core finding. **Removed.**
- **Criticism about 99.29% frequency based on one model (Section 3.1):** The paper explicitly frames this as an analysis on Qwen3-8B to motivate the approach. Generalizability to other models is established by the empirical results across 5 models. **Removed.**
- **Criticism about not comparing confusion rates on LCB (Section 5.2):** The paper provides a clear rationale for not using the LCB. Demanding a comparison the authors explicitly and reasonably scoped out is not a valid weakness. **Removed.**
- **Criticism about missing confidence intervals for commercial confusion rates (Table 2):** Commercial API evaluations are expensive and typically reported without variance across prompts. This is standard practice. **Removed.**
- **All pure formatting, grammar, or presentation nitpicks** are parser artifacts, not author errors. **Removed.**
- **Any speculation about unreleased models or datasets** — the paper cites these as existing; they are assumed to exist per protocol. **Removed.**
- **Strength Finder strength about the paper "addressing an important problem"** — generic and not specific to the paper's content. **Removed.**
- **Strength Finder claim about "outperforming baselines while avoiding performance degradation"** — this is real but is subsumed by strength 1 (ablation) and strength 2 (empirical breadth). Merged. **Removed as duplicate.**

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add Ji et al. (2025) and Nie et al. (2025) as baselines.** If direct implementation is impractical, report confusion rates from their papers on comparable setups, or explicitly discuss why comparison is not feasible. This addresses the most significant current gap.
2. **Provide aggregate statistics on pseudo-target quality.** Measure across a random sample of confusion points: given a confusion point where the target language is T and the confused language is C, how often does the norm-adjusted top-k/p candidate set contain (a) T-family tokens, (b) C-family tokens, (c) both? This would directly confirm the training mechanism works as claimed.
3. **Report BLEU on FLORES-WITH-LATIN** to fully close the code-switching preservation claim.
4. **Add Latin confusion metrics for thinking models** in Table 4 for completeness.
5. **Include training hyperparameters** (learning rate, batch size, epochs, top-k/p values) in the main paper.

---

## Score and Decision

**Calibration anchors used:**

| Paper | Avg Score | Comparison to this paper |
|---|---|---|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/fSbPwHjdDG.md` | 3.00 | Much weaker: single task, single model, poor presentation, results don't replicate. This paper is stronger across all dimensions. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/BCyAlMoyx5.md` | 5.67 | Analysis paper with less clear practical contribution; this paper has clearer methodology and direct practical utility. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/4z3IguA4Zg.md` | 6.00 | Similar type (decoding-time intervention, empirical evaluation). Comparable evaluation breadth; this paper has more model coverage and ablation studies. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/NCrFA7dq8T.md` | 6.60 | More tightly scoped but extremely well-executed mechanistic analysis. This paper has broader empirical scope but less rigorous circuit-level analysis. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/uZ5K4HeNwd.md` | 7.00 | Strong paper with thorough ablations and clearer novelty narrative; this paper has some gaps in baseline comparisons that prevent it from reaching this tier. |

The paper presents a practical, well-motivated method with strong empirical results across multiple models and modes. The missing baseline comparisons and the unverified pseudo-target quality assumption are real gaps but are fixable and do not invalidate the core empirical findings. The paper is comparable to the 6.0-level decoding intervention papers and sits above the 5.67-level analysis paper.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper introduces the Language Confusion Gate (LCG), a lightweight plug-in MLP that reduces unintended language mixing in LLM outputs by dynamically masking disallowed-language tokens during decoding. LCG is trained via norm-adjusted self-distillation, leveraging the observation that output token embeddings have systematically larger norms for high-resource languages, creating a bias toward language confusion. The method intervenes on only ~0.3–0.4% of tokens, adds 0.4% per-step overhead, and is evaluated across Qwen3, Llama3.1, Gemma3, and GPT-OSS in both standard and reasoning modes, showing order-of-magnitude reductions in confusion rates (e.g., Qwen3-30B CJ confusion 1.0%→0.0%, Latin confusion 4.4%→0.4%) without degrading task performance.

## Strengths

1. **Sparse, efficient intervention with production-grade latency benchmark.** LCG intervenes on only 0.38% of tokens (Qwen3-8B) and 0.33% (Llama3.1-8B) on FLORES-NO-LATIN. Per-step latency increases from 15.95ms to 15.99ms (0.4% overhead) in a production system with concurrency 8 (Section 6). This makes the method practical for deployment, not just an academic proposal.

2. **Norm-adjusted self-distillation provides causal evidence for the mechanistic insight.** The ablation in Table 3 directly compares LCG-unadjusted vs. LCG-adjusted across all four models. For Llama3.1-8B, Latin confusion drops from 5.7% (unadjusted) to 2.9% (adjusted); for Qwen3-30B, from 0.7% to 0.4%. This controlled comparison verifies that the embedding norm bias identified in Section 3.2 is not just descriptive but actionable.

3. **Evaluated across diverse model families and both inference modes.** The method is tested on four no-think models (Qwen3-30B, Llama3.1-8B, Gemma3-12B, Qwen3-8B) and two thinking models (Qwen3-30B-Thinking, GPT-OSS). Results show consistent order-of-magnitude confusion reduction, e.g., Qwen3-30B CJ confusion from 1.0% to 0.0%, and thinking models' CJ confusion near-eliminated (Table 4: 0.12%→0.00%). This breadth demonstrates generalization beyond a single architecture.

4. **Analysis of confusion points directly motivates the logit-masking design.** Section 3.1 shows that at confusion points, the correct-language token ranks in the top-3 in 99.29% of cases, yet the confusion token is top-1 in 56.74% of cases — meaning greedy decoding alone is insufficient. This observation grounds the choice of a masking approach rather than weight modifications.

5. **Outperforms retraining-based baselines while avoiding task degradation.** Figure 3 shows ORPO tuning degrades INCLUDE accuracy (Qwen3-8B: 61.4→57.3; Llama3.1-8B: 46.1→43.2), whereas LCG maintains or slightly improves accuracy. This demonstrates a concrete advantage of plug-in approaches over methods requiring model retraining.

## Weaknesses

### Fatal
None.

### Major

1. **Missing comparison with directly comparable inference-time baselines.** The related work (Section 2) describes neuron suppression (Nie et al., 2025) and post-hoc smoothing (Ji et al., 2025) as inference-time interventions for language confusion. Neither is included as a baseline. Without these comparisons, the paper's claim that LCG is superior to existing inference-time plug-in methods is unsubstantiated. The existing baselines (ICL, greedy, ORPO) are either not plug-in methods or not state-of-the-art inference-time interventions, so they do not adequately fill this gap. This is the most significant weakness because it undermines a core contribution claim.

2. **Incomplete verification that LCG preserves legitimate code-switching.** The paper provides two pieces of evidence: (a) 86.7% token-level preservation on human-validated examples (Section 5.3), and (b) response-level code-switch rates that remain between the reference answer rate and Claude Sonnet 4's baseline. However, the 86.7% figure is only for one model (Qwen3-8B), on a self-selected set of examples with no reported annotation procedure or inter-annotator agreement. More critically, the 13.3% of blocked legitimate code-switches are not analyzed — were these actual false positives, or were the human judgments unreliable? Additionally, the response-level drop (Qwen3-8B: 46.34%→25.90% vs. 38.36% answer rate) is a substantial relative reduction, and the paper argues this is "not much lower" without justifying that threshold. A per-token analysis of what LCG actually blocked, with human verification of whether the blocked cases were erroneous, would substantially strengthen the central claim.

### Minor

1. **Confusion point analysis is limited to one model and dataset.** Section 3.1's finding (correct-language token ranks top-3 in 99.29% of cases) is based on Qwen3-8B on FLORES-NO-LATIN only. Given that embedding norm imbalance varies strongly across models (Table 1: CJ% ranges from 0.00% in GPT-OSS to 10.74% in Qwen3-8B), this analysis may not generalize. The paper should acknowledge this limitation.

2. **ORPO baseline is under-specified.** The description ("prepare a multilingual dataset, and synthesize samples with language confusion as rejected samples") lacks details on data size, training hyperparameters, or how language mixing was synthesized. This makes the ORPO comparison difficult to verify or reproduce.

3. **No error bars or confidence intervals.** All confusion rates and accuracy/BLEU scores are reported as point estimates without standard deviations, confidence intervals, or significance tests. While the effect sizes are large (often order-of-magnitude), some fine-grained comparisons (e.g., BLEU differences of 0.1–0.2 points) cannot be assessed for statistical reliability. Given that confusion rates are computed on thousands of generated responses, reporting variability would be feasible.

4. **Figure 2 caveat not discussed.** After norm adjustment, the top-10 tokens are all "n"-like tokens (shown in the table accompanying Figure 2). The paper does not discuss whether this is an artifact of over-correction or a meaningful behavior. Since norm adjustment is a core component of the training signal, a brief explanation would be appropriate.

5. **Training data ambiguity.** Section 5.1 states "This same dataset was used to train the gate for both thinking and no-think models," but it is unclear whether a single shared gate is used across all models or separate gates per model. If a single gate is shared, its performance may vary across architectures due to differing hidden-state distributions. If per-model gates, the training protocol should be explicit.

### Trivial
- Table 5 reports code-switch rates but does not report confusion rates for the WITH-LATIN set. Adding these would clarify whether the code-switch reduction is accompanied by a confusion reduction, which would be a net positive.

## Nice-to-Haves
- Per-rule ablation (persistence rule vs. contradiction rule) to isolate which rule contributes most to the improvement.
- Evaluation on at least 2–3 languages intentionally held out from the 200-language training set to test generalization to unseen languages.
- Analysis of pseudo-target quality: what fraction of the norm-adjusted top-k/p candidate sets contain the gold language family?
- Confusion rate distribution broken down per target language (Arabic vs. Hebrew vs. Thai) to identify potential blind spots.

## Removed Points

These points were raised in the original reviews but are removed after verification against the paper. They are listed here for completeness but should not be weighed in the final assessment.

- **"Infrequent" vs. reported confusion rates**: The reviewer claimed the introduction misleadingly calls confusion "infrequent" while reporting 12.1% Latin confusion. However, the paper uses "infrequent" at the token level (intervention rate 0.38%), while 12.1% is a response-level metric. These are different granularities; no contradiction exists. **Reason: Misreads the paper.**

- **Norm analysis is "standard"/"well known"**: The vector decomposition (logit = ||h||·||e_i||·cos_sim) is standard linear algebra, not a claimed algorithmic novelty. The contribution is observing and leveraging the systematic norm bias toward high-resource languages. **Reason: Strawman — the contribution is the observation, not the decomposition formula.**

- **Low-Res tokens never measured for suppression**: The paper explicitly states "Symbols and Low-Res tokens are never masked" as a design choice (Section 4.3, Rule 1). There is no suppression to measure. **Reason: Factually wrong; the reviewer missed the explicit design statement.**

- **NO-LATIN partition assumption**: The reviewer claimed the partition "assumes zero legitimate Latin code-switching" without validation. However, the partition is done by examining ground-truth references — if the reference contains no Latin, any Latin in the output is definitionally erroneous. **Reason: Misunderstands the methodology.**

- **BLEU scores too low**: The reviewer noted BLEU scores of 12–17 without discussing whether they indicate reasonable translation quality. The paper uses BLEU for relative comparison (with-LCG vs. without-LCG), not as an absolute quality metric. Translation into distant languages (Arabic, Hebrew, Thai, Korean) inherently yields lower BLEU scores. **Reason: Critique outside the paper's scope.**

- **"No Rule" ablation doesn't test gate alone**: The reviewer claimed "No Rule" doesn't test the gate without rules, but Figure 3's "No Rule" bar is exactly that ablation — LCG without the intervention rules. **Reason: Factually wrong; the ablation exists.**

- **Heuristic for incomplete BPE tokens in Appendix A**: The reviewer noted this is "critical for reliability" but it was relegated to the appendix (which is stripped by the parser). Classifying partial BPE bytes by Unicode block structure is a standard engineering heuristic, not a core methodological concern. **Reason: Appendix stripped by parser; not a core issue.**

- **Language scope limitation about Low-Res**: The reviewer claimed the evaluation never tests whether LCG handles confusion between Low-Res languages. The paper explicitly limits its scope to CJ vs. Latin confusion and acknowledges script-level granularity as a limitation. **Reason: Scope creep.**

## Novel Insights

None beyond the paper's own contributions. The synthesis of the reviews does not surface a weakness or angle that the paper's own discussion does not cover.

## Suggestions

1. **Add the missing inference-time baselines (neuron suppression, post-hoc smoothing).** This is the most impactful improvement: it directly fills the gap in the paper's claim chain. Without it, the paper cannot substantiate superiority over existing plug-in methods.

2. **For the code-switch analysis, manually annotate the LCG-blocked tokens** (the ~13.3% of cases where legitimate code-switches were suppressed) to determine whether they are true false positives or edge cases. Report inter-annotator agreement. This would directly address the most significant evidential gap.

3. **Report confidence intervals or standard deviations** for the main confusion-rate metrics (Tables 3 and 4). Even simple bootstrap intervals would help assess whether the observed differences are reliable.

4. **Clarify the gate training protocol** in Section 5.1: state explicitly whether a separate gate is trained per model or a single gate is shared, and if shared, report cross-model transfer results.

5. **Acknowledge the Figure 2 caveat** that after norm adjustment the top-10 tokens collapse to repeated "n"-like tokens, and explain why this does not undermine the norm-adjusted training signal.

## Score and Decision

**Calibration anchors** (all unique papers returned by retrieval, not only those read in full):

| Path | Avg Score | Comparison to This Paper |
|------|-----------|------------------------|
| FBkpCyujtS (min-p sampling) | 8.50 | Stronger: simpler, more influential (54k GitHub repos), cleaner evaluation. |
| 6Mxhg9PtDE (Safety Alignment) | 9.50 | Stronger: deeper analysis, more impactful findings about safety. |
| tcsZt9ZNKD (Scaling SAEs) | 8.20 | Stronger: cleaner scaling laws, novel methodology. |
| gc8QAQfXv6 (Function Vectors) | 9.00 | Stronger: more thorough analysis, broader implications. |
| uZ5K4HeNwd (Beyond Auto-Regression) | 7.00 | Comparable: both propose efficient generation methods, but this paper's evaluation is broader. |
| NCrFA7dq8T (Same but Different) | 6.60 | Comparable: both have clear contributions; this paper has stronger practical utility. |
| 8WQ7VTfPTl (SADI) | 6.40 | Slightly stronger: more extensive baselines and ablations; this paper has a more concrete practical contribution. |
| HMa8mIiBT8 (Cross-Lingual Knowledge) | 6.00 | Comparable: both address multilingual issues; this paper proposes a working solution rather than only analysis. |
| BCyAlMoyx5 (Crosslingual Capabilities) | 5.67 | Weaker: analysis-only, no practical solution; this paper has a deployable method. |
| eznTVIM3bs (Babel Tower) | 5.25 | Comparable: both study multilingual behavior; this paper's contribution is more directly actionable. |
| hsMkpzr9Oy (Mexa) | 5.40 | Weaker: evaluation-only method; this paper proposes an intervention. |
| cayKVPCrOP (GOOD) | 4.50 | Comparable methods section — both are decoding-time interventions; this paper is cleaner and more efficient. |
| YpWV7XRmFB (Decoding by Contrasting) | 4.00 | Weaker: narrower scope; this paper has broader evaluation. |
| PL6e9HkVxk (Root Defence) | 4.25 | Weaker: decoding-level safety; this paper's methodology is more principled. |
| fSbPwHjdDG (Llamas think in English) | 3.00 | Much weaker: narrow task, poor presentation, lack of generalizability. |
| Others (Wv9Gl1bFbc, QKqWnNkwPL, a4PBF1YInZ, IqGVIU4rvM, OdoS6cH8MP, TgTxJALwDz, LQdaXixB0g) | 2.00–3.50 | All substantially weaker: unrelated topics or poorly executed. |

The paper makes a clear, practical contribution to an important problem. The core method is well-motivated by a mechanistic observation, is computationally efficient, and shows large empirical gains across diverse models. However, the missing inference-time baselines and incomplete code-switch preservation analysis prevent it from fully establishing its claimed advantages. With these additions, the paper could be significantly stronger. Relative to the anchor set, this paper sits around the 6.0 level: above purely analytical work but below papers with more complete comparative evaluation.

**Score:** 6.0

**Decision:** Accept

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
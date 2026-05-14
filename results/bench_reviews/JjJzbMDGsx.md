Now I have everything I need. Let me construct the final consolidated review.

## Summary

This paper introduces the Language Confusion Gate (LCG), a lightweight MLP that filters tokens at decoding time to reduce language confusion in multilingual LLMs without modifying the base model. LCG is trained via norm-adjusted self-distillation, leveraging the observation that token embedding norms are skewed toward high-resource languages (creating a bias) and that correct-language tokens typically remain in the top-k predictions. Evaluated across five open-source models in both standard and reasoning modes, LCG reduces confusion rates substantially (e.g., Qwen3-8B Latin confusion from 12.1%→2.0%) with only 0.4% inference overhead, while maintaining task performance.

## Strengths

- **Decoding-time intervention without retraining**: LCG is a two-layer MLP applied at inference, leaving the base LLM untouched. This contrasts with methods like ORPO that require fine-tuning and can degrade task accuracy (INCLUDE drops 61.4→57.3 on Qwen3-8B, Table 3). The intervention rate is extremely sparse (0.33–0.38% of tokens), so most generation is unaffected.

- **Norm-adjusted self-distillation is well-motivated and validated**: The paper identifies that output token embedding norms are systematically larger for high-resource languages (Table 1: CJ 10.74% vs Low-Res 0.14% in Qwen3-8B top 5% norms) and uses this to debias training targets. The ablation confirms LCG-adjusted consistently outperforms LCG-unadjusted across all models (e.g., Llama3.1-8B Latin% 5.7%→2.9%, Table 3).

- **Practical efficiency**: Benchmarking on a production Qwen3-30B system shows only 0.4% per-step overhead (15.95ms→15.99ms, Section 6). Compatibility with speculative decoding (Appendix F) further supports deployability.

- **Broad evaluation across model families and modes**: Tested on Qwen3-8B/30B, Llama3.1-8B, Gemma3-12B, GPT-OSS in both standard and thinking modes using translation (FLORES+), knowledge (INCLUDE), and code generation (Humaneval-XL) benchmarks. General capabilities are verified on MMLU, GPQA, AIME (Appendix B).

- **Comparison with multiple baselines**: LCG is compared against ICL, greedy decoding, and ORPO (Figure 3), outperforming all on confusion reduction while maintaining task accuracy.

## Weaknesses

### Fatal

None.

### Major

- **The evidence for preserving legitimate code-switching is insufficient for the paper's central framing.** The paper claims LCG "distinguishes harmful confusion from acceptable code-switching," but the experimental support falls short. On FLORES-WITH-LATIN, LCG reduces Qwen3-8B's code-switch rate from 46.34% to 25.90% — a 44% relative reduction in *all* code-switching, both legitimate and illegitimate. The 86.7% token-level figure (Table 5 caption) measures whether LCG permits pre-identified human-validated switches, which is one-directional: it shows LCG is permissive on clear-cut cases, but does not measure whether LCG correctly *distinguishes* legitimate from illegitimate switching at the point of decision. A proper false-positive/false-negative analysis over a random sample of mixed outputs (with human annotation of each switch as legitimate or not) would be needed to substantiate the distinction claim. The paper would be more accurate framing LCG as "a method that reduces language confusion while having a moderate side-effect of also reducing some legitimate code-switching."

- **No independent ablation of the three intervention rules.** The "No Rule" setup in Figure 3 removes all three rules at once, but the individual contribution of each rule (persistence, high-confidence override, never-mask symbols/Low-Res) is never isolated. The persistence rule (always allow the previous token's language) could plausibly be the dominant mechanism — if most confusion involves isolated out-of-language tokens, this rule alone does most of the work. Without per-rule ablation, it is impossible to assess how much the learned gate contributes beyond what a simple heuristic ("stay in your current language") would achieve. Furthermore, the "No Rule" bar chart lacks numerical labels, making quantitative comparison difficult.

- **Self-distillation training inherits the base model's blind spots.** The pseudo-labels are derived from the frozen model's norm-adjusted top-k/p predictions. As the paper itself notes (Section 3.2), norm adjustment does not fully explain all language confusion (e.g., English-Chinese confusion between two high-norm families, or low-resource—low-resource confusion). The gate cannot learn to correct errors that the norm-adjusted distribution does not already handle correctly. No oracle-style experiment (e.g., training on ground-truth language labels) is provided to bound how much performance is lost to this circularity, making it difficult to assess headroom.

- **The "order of magnitude" claim is overstated for several models.** Looking at Table 3: Gemma3-12B shows CJ% 0.2→0.1 (2×) and Latin% 1.0→0.5 (2×); Llama3.1-8B Latin% goes 8.4→2.9 (2.9×). While Qwen models do show ~10× or more in several cases, the blanket "often by an order of magnitude" claim overstates the average benefit.

### Minor

- **Script-level granularity limits the approach.** Grouping all Latin-script languages (English, Spanish, French, etc.) into one family and all Low-Res languages into another means LCG cannot address within-family confusion (e.g., English mixing with Spanish, or Arabic mixing with Hindi). The paper acknowledges this in the conclusion but does not quantify what fraction of confusion errors fall into these unresolvable categories.

- **The Section 3.1 analysis (correct-language token in top-3 99.29% of the time) is only checked on Qwen3-8B on one dataset (FLORES-NO-LATIN).** The prevalence of this property across models and language pairs is not established, which limits confidence that the approach generalizes.

- **Thinking model evaluation on Humaneval-XL only targets Arabic and Hebrew (non-Latin, non-CJ scripts),** so only CJ confusion during code generation is measured. Latin confusion (e.g., Chinese comments in Python code) — arguably the most common form — is not evaluated in the reasoning setting.

- **The 86.7% figure implies a 13.3% false positive rate** on human-validated legitimate code-switches — i.e., LCG blocks ~1 in 7 clearly legitimate switches. While the paper frames this positively, a 13.3% error rate on the easiest cases (where human annotators unanimously agree) is worth discussing as a limitation.

### Trivial

- The bar charts in Figure 3 ("No Rule" vs. LCG-adjusted) are difficult to read because the numerical values are not labeled, making quantitative comparison of the ablation difficult without guessing bar heights.

## Nice-to-Haves

- An oracle-style experiment training the gate on ground-truth language labels (from reference translations) would provide an upper bound on achievable performance and clarify how much is lost to self-distillation.
- A per-step visualization of the gate's probability outputs across language families during a confusion-prone generation would make the mechanism more concrete.
- Evaluation on within-family confusion (e.g., English-Spanish or Arabic-Hindi pairs) would clarify the practical impact of the script-level grouping limitation.

## Removed Points

These points were flagged by reviewers but are factually incorrect, misunderstand the paper, or violate the review guidelines. Treat them with caution.

- **Criticism that the Section 3.2 norm decomposition is not novel** (it's a known property of linear layers): the paper uses it as a mechanistic observation to motivate norm-adjusted training, not as a novel theoretical contribution. This is valid use of established knowledge.
- **Claim that the FLORES-WITH-LATIN comparison to Claude Sonnet 4 is invalid**: the paper explicitly states "these two baselines are just references for comparison but not a ground truth optimal code-switch rate," so the paper already hedges this.
- **Claim that LCG can increase language confusion via downstream effects (Appendix J)**: the persistence rule ensures the previous token's language is always available; blocking a legitimate switch may degrade task correctness but cannot increase cross-language mixing as defined in the paper. Task performance is separately shown to be maintained (Table 3, Appendix B).
- **Criticism that the evaluation should use LCB**: the paper provides a clear rationale for not using LCB (some queries require code-switching, unreliable detector). This is a reasonable methodological choice, not a flaw.
- **Formatting nitpicks, "missing related works" claims, and reproducibility concerns about undisclosed hyperparameters** (these either reflect parser artifacts or are not standard expectations for an empirical systems paper).

## Novel Insights

The most interesting insight from the reviews — which the paper itself does not fully develop — concerns the tension between the learned gate and the hand-crafted intervention rules. The persistence rule (always allow the previous token's language) is presented as a safety mechanism, but may actually be the dominant source of LCG's effectiveness. If most confusion events are isolated single-token intrusions where the model otherwise stays in the correct language, then a rule that simply says "never change languages unless the gate explicitly permits the new language" would naturally suppress most confusion — reducing the learned gate to a secondary role of deciding when a language switch is permissible. This would make LCG a system where a strong prior (stay in your lane) delegates outlier decisions to a learned component. The reviews collectively identify that the paper's current ablation design cannot resolve this question, which points toward a cleaner experimental design for future work: compare LCG against a purely rule-based system (e.g., "block any language different from the previous token unless its top-1 probability exceeds a threshold") to isolate the marginal value of the learned component.

## Suggestions

1. Add an oracle experiment training the gate on ground-truth language labels to establish the upper bound for the self-distillation approach. This would address the circular-training concern directly.
2. Provide per-rule ablation (remove each of the three intervention rules independently) with numerical values, not just a bar chart, to quantify the learned gate's contribution versus the heuristic rules.
3. Conduct a proper false-positive/false-negative analysis for code-switching preservation: sample model outputs with code-switching events, annotate each as legitimate or illegitimate, and report precision/recall of LCG's decisions — not just the rate on pre-selected clear-cut cases.
4. Tone down the "distinguishes harmful confusion from acceptable code-switching" claim or provide the analysis needed to support it. The current evidence is consistent with "reduces confusion substantially while also reducing some legitimate switching" — this is still a useful contribution.
5. Add numerical labels to Figure 3 so readers can compare the "No Rule" ablation values directly.

## Score and Decision

To calibrate: I compare this paper to human-reviewed anchors from the same topic area.

| Anchor path | Avg Score | Comparison |
|---|---|---|
| `/home/wg25r/review_agent/human_reviews_2026/BQOFU9qO5j.md` (SASFT) | 5.50 | Both address code-switching mitigation. SASFT uses SAE analysis + fine-tuning; LCG uses norm analysis + inference gating. LCG has broader model coverage but weaker evidence for preserving legitimate switching. Comparable quality. |
| `/home/wg25r/review_agent/human_reviews_2026/HIXPyQ1aMq.md` (How Do LLMs Speak Languages) | 4.50 | Rejected paper on unintended code-switching with significant readability issues. LCG is clearly stronger — better written, more practical contribution, broader evaluation. |
| `/home/wg25r/review_agent/human_reviews_2026/vzlDdOzXAh.md` (LGCD) | 4.50 | Also an inference-time decoding intervention. LCG is more efficient (0.4% overhead, no second model needed) and evaluates on more models. Slightly stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/r00UxTl8El.md` (LinguaMap) | 5.33 | Stronger scientific contribution via deeper interpretability analysis, accepted Poster. LCG has weaker analysis but stronger practical contribution. Similar tier. |
| `/home/wg25r/review_agent/human_reviews_2026/5fCDEz43ya.md` (Token-Guard) | 5.50 | Decoding-time hallucination control. Similar approach (gating at decoding), similar evaluation depth. Accepted Poster. Comparable quality. |
| `/home/wg25r/review_agent/human_reviews_2026/ABc5y3741T.md` (Language-Mixed CoT) | 5.00 | Multilingual reasoning via data curation. Strong dataset contribution. LCG is a different type of contribution but similar overall quality. |
| `/home/wg25r/review_agent/human_reviews_2026/ysT0BCmZ3S.md` (Language Matters) | 3.00 | Withdrawn/rejected, thin analysis. LCG is substantially stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/VKGTGGcwl6.md` (LLMs Get Lost) | 8.00 | Oral-level paper with broad impact and rigorous analysis. LCG is not at this level. |

The paper has a genuine practical contribution (efficient, plug-in confusion reduction that maintains task performance) but the evaluation of its signature claim — distinguishing confusion from legitimate code-switching — is insufficient, and the contribution of the learned gate versus the intervention rules is not properly disentangled. These are addressable in revision. The core method is sound, well-motivated, and validated across multiple models and metrics. This is a solid marginal-accept paper.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
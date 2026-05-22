Now I have all the information needed to write the consolidated review.

## Summary

This paper introduces the Language Confusion Gate (LCG), a lightweight two-layer MLP that operates as a plug-in decoding-time intervention to mitigate language confusion in multilingual LLMs. LCG is trained via norm-adjusted self-distillation on the frozen model's own debiased predictions, and at inference it dynamically masks disallowed language-family tokens. Evaluated across Qwen3, Llama3.1, Gemma3, and GPT-OSS on FLORES and INCLUDE benchmarks, LCG reduces language confusion by roughly an order of magnitude (e.g., Qwen3-30B: CJ confusion 1.0%→0.0%, Latin confusion 4.4%→0.4%) with only 0.4% generation-time overhead, while maintaining or slightly improving task performance.

## Strengths

- **Substantial and consistent confusion reduction across diverse models.** Table 3 shows that LCG reduces both CJ and Latin confusion by roughly an order of magnitude on FLORES-NO-LATIN across all four no-think models (Qwen3-8B, Qwen3-30B-A3B, Llama3.1-8B, Gemma3-12B). On INCLUDE, CJ confusion is similarly reduced (e.g., Qwen3-30B from 2.21% to 0.11%). Task metrics (BLEU, accuracy) are maintained or slightly improved, ruling out naive quality trade-offs.

- **Norm-adjusted self-distillation is shown to be strictly better than the unadjusted version.** Table 3 directly compares LCG-adjusted vs. LCG-unadjusted: on every model–dataset pair with nonzero confusion, the adjusted version achieves lower confusion rates (e.g., Llama3.1-8B Latin: 5.7%→2.9%). This clean ablation validates the core design insight that debiasing the pseudo-targets via embedding norm division produces a more accurate gate.

- **Mechanistic analysis of token embedding norm imbalance provides an evidence-based motivation.** Table 1 quantifies the over-representation of high-resource language tokens (CJ, Latin) among the top 5% of embedding norms, and Figure 2 visually demonstrates that dividing logits by embedding norms removes confused CJ tokens from the top-10 at a confusion point. This analysis grounds the LCG design in a concrete model-internal bias.

- **Negligible computational overhead.** The paper reports a measured 15.95ms → 15.99ms per generation step (0.4% overhead) in a production benchmark with Qwen3-30B-A3B (Section 6), making the approach practical for deployment.

- **Evaluated across diverse architectures and inference modes.** The method is tested on 5 models (dense, MoE, hybrid) in both standard ("no-think") and reasoning ("thinking") settings, with consistent results.

- **Outperforms strong baselines (ICL, greedy decoding, ORPO).** Figure 3 shows LCG reduces confusion more effectively than ICL, greedy, and ORPO, while ORPO degrades INCLUDE accuracy (e.g., Qwen3-8B: 61.4→57.3) and LCG does not.

## Weaknesses

### Fatal
None.

### Major

- **The code-switch preservation claim lacks a task-performance metric on FLORES-WITH-LATIN.** On the FLORES-WITH-LATIN subset (where Latin characters in the reference make some code-switching legitimate), the paper reports only the *code-switch rate* (Table 5) — the percentage of outputs containing Latin characters — but no BLEU or translation quality metric. Without a task-performance measure, the reduction from 46.34% to 25.90% (Qwen3-8B) could reflect either beneficial removal of spurious Latin tokens or harmful over-masking of required ones. The comparison to the ground-truth answer rate (38.36%) and Claude Sonnet 4's rate (23.29%) provides context but does not measure whether the remaining code-switching is appropriate or whether translation quality degrades. This is important because the paper's claimed advantage over rule-based methods is the ability to distinguish harmful confusion from acceptable code-switching. Adding BLEU or another quality metric on this subset would substantially strengthen the claim.

### Minor

- **Training pseudo-target generation hyperparameters (k and p values) are not specified.** Section 4.2 defines the pseudo-targets via top-k/top-p filtering on norm-adjusted logits ($S_{k,p}$) but does not state the exact k and p values used during training. The values given in Section 4.3 ((k=5, p=0.999) and (k=20, p=0.95)) are for the inference-time contradiction rule, not for training. This gap impairs reproducibility.

- **The human annotation for code-switch evaluation is under-documented.** The paper reports that 86.7% of human-validated code-switch examples were preserved by LCG (Section 5.3), but does not specify: how many examples were annotated, what criteria defined "natural, appropriate code-switch," how many annotators were used, or the inter-annotator agreement. Without these details, the reliability of the 86.7% figure is hard to assess.

### Trivial

- Table 4 caption incorrectly says "No-Think Models" but the content and surrounding text describe thinking models (Humaneval-XL, Pass@k metrics).

## Nice-to-Haves

- **Quantify the fraction of confusion cases attributable to norm bias.** The paper states norm bias "can account for a subset of such errors but cannot fully explain language confusion" (Section 3.2) but does not quantify this subset. A simple analysis (e.g., on a sample of confusion points, measure how often the confused token has a higher-than-median embedding norm compared to correct-language tokens) would sharpen the motivation for why norm-adjustment helps but is insufficient alone.

- **Report per-family precision/recall of the gate on a held-out set.** This would help diagnose systematic errors and would be easy to produce given the existing training setup.

- **Break down which intervention rule contributes most.** The "No Rule" ablation (Figure 3) shows that rules help, but a finer-grained ablation (e.g., removing each rule individually) would clarify the contribution of each design choice.

## Removed Points

*These points were flagged by reviewers but are not included as weaknesses in the main review, for the reasons given below.*

- **ORPO baseline dataset size/composition not specified.** The paper states the dataset was "synthesized" following Lee et al. (2025). ORPO is a baseline comparator, not the paper's own method; the level of detail is acceptable for a baseline. REMOVED.

- **Statistical significance / confidence intervals not reported.** The reported effect sizes are very large (e.g., 12.1%→2.0%) and do not require significance testing to be compelling. REMOVED.

- **Low BLEU scores for commercial LLMs (Table 2).** The paper already explains this as reflecting the FLORES-NO-LATIN subset being hard (translations that use no Latin characters at all). This is not a weakness of the paper. REMOVED.

- **Latin confusion not separately measured on Humaneval-XL.** The programming nature of Humaneval-XL makes Latin confusion measurement infeasible, as the critic acknowledges. REMOVED.

- **Process for generating step-level targets from training samples.** The paper describes the training data composition (78k samples from Aya, FLORES+, etc.) and the loss computation is clearly specified. The remaining ambiguity is a reproducibility detail, not a structural gap. REMOVED (partially subsumed by weakness #2 above).

- **Strength about "LCG preserves legitimate code-switching" was flagged as partially in tension with the verified weakness.** The strength is kept but the caveat (missing BLEU on WITH-LATIN) is properly noted as a weakness.

## Novel Insights

None beyond the paper's own contributions. The self-distillation training with norm-adjusted pseudo-targets and the analysis of token embedding norms as a source of language-family bias are the core novel elements, and they are well articulated by the paper itself.

## Suggestions

1. **Report BLEU (or chrF++) on FLORES-WITH-LATIN** to directly address the code-switch preservation claim. If BLEU does not degrade, the argument that LCG selectively removes only harmful confusion is much stronger.
2. **Specify the k and p values used for training pseudo-target construction** — this is a simple fix that resolves the reproducibility gap.
3. **Document the human annotation process** (number of examples, annotator count, instructions, agreement) for the 86.7% code-switch preservation experiment.
4. **Add a finer-grained ablation of the three intervention rules** to clarify which design choices drive the improvement over the "No Rule" baseline.

## Score and Decision

**Calibration anchors** (all from the deepreview_13k_calibration corpus):

| Path | Avg Score | Comparison to this paper |
|------|-----------|------------------------|
| `gc8QAQfXv6` (Function Vectors for CF) | 9.00 | Stronger paper — broader experiments, deeper analysis, and a training method validated across more settings. This paper is below this anchor. |
| `51WraMid8K` (Probabilistic Unlearning) | 8.00 | Stronger paper — formal mathematical contribution with proofs + extensive experiments. This paper has less theoretical depth. |
| `NCrFA7dq8T` (Structural Similarities in Multilingual LM) | 6.60 | Similar tier — both are well-executed with clear contributions. This paper has a stronger practical/deployable contribution vs. analytical contribution of the anchor. |
| `BCyAlMoyx5` (Crosslingual Capabilities) | 5.67 | Weaker paper — primarily diagnostic with limited language coverage and less convincing experiments. This paper has stronger empirical validation and a practical method. |
| `fSbPwHjdDG` (Llamas think in English) | 3.00 | Much weaker paper — major methodology concerns, poor presentation, limited scope. This paper is substantially stronger. |
| `HMa8mIiBT8` (Cross-Lingual Knowledge Consistency) | 6.00 | Similar tier — both are solid empirical papers. This paper has the advantage of proposing a deployable solution rather than just analysis. |
| `i7oU4nfKEA` (When Is Multilinguality a Curse) | 6.25 | Similar tier — both have thorough experiments across multiple models/setups. This paper's practical contribution (plug-in gate) gives it a slight edge in novelty. |

This paper makes a clear, practical contribution with strong empirical support across multiple models and tasks. The main gap is that the code-switch preservation claim — a key differentiator from rule-based methods — lacks a task-performance metric on code-switch-permitting data. With that gap addressed, the paper would be in the 7+ range. In its current form, it is a solid contribution with one significant but addressable weakness.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
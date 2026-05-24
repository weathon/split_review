Now I have a clear calibration picture. Let me formulate the final review.

**Round 1 Bracket**: 5.5–7.5. The paper is clearly above the <3.5 weak band and solidly within the middle band. The 6.0 anchors (DeCo, Tool Decoding, Nudging) share structural similarities (decoding-time interventions, plug-and-play approaches) but have thinner evaluations and less dramatic results. The 8.0 anchors (DEPT, Knowledge Card) represent more deeply novel frameworks with broader scope.

**Round 2 Narrowing**: Anchors in the 5.25–6.50 range. LLaVA-MoD (6.50, Accepted) is the strongest comp — multi-component framework, comprehensive evaluation, mixed reviews (5–8), some missing baselines and efficiency concerns. The LCG paper has a cleaner core contribution, stronger results (order-of-magnitude), and better practical validation, but the missing direct norm-adjusted masking baseline is a real gap. The 6.00 anchors (Multi-Granularity Semantic Revision, Tool Decoding, DeCo) have thinner results and less clear motivation than LCG.

**Final score**: 6.5 — between LLaVA-MoD (6.50) and Knowledge Card (8.0). The paper is stronger than the 6.0 cohort in clarity, result strength, and practical validation, but the missing baseline comparison prevents placement higher.

---

## Summary

This paper introduces the Language Confusion Gate (LCG), a lightweight, plug-in mechanism that filters tokens during decoding to suppress unintended language mixing without modifying the base LLM. The LCG is a small two-layer MLP trained via norm-adjusted self-distillation: it uses the frozen model's own debiased (norm-adjusted) top-k/p predictions as pseudo-targets to learn which language families are permissible at each generation step. The authors ground their approach in three empirical observations — confusion is rare, correct-language tokens are usually in the top predictions, and output embedding norm imbalance biases models toward high-resource languages. Evaluated across seven models spanning Qwen3, Llama3.1, Gemma3, and GPT-OSS on translation (FLORES), knowledge QA (INCLUDE), and code generation (Humaneval-XL), LCG reduces language confusion by an order of magnitude (e.g., Qwen3-30B Latin confusion from 4.4% to 0.4%) while maintaining or slightly improving task performance, with only 0.4% inference overhead.

## Strengths

- **Strong empirical foundation for the method.** The authors present three well-motivated observations: (1) at confusion points, language-consistent tokens appear in the top-3 candidates 99.29% of the time (Section 3.1), showing that masking is viable; (2) norm-adjustment effectively re-ranks tokens (Figure 2 shows CJ tokens disappearing from the top-10 after debiasing at a real confusion point); (3) high-resource languages dominate the high-norm tail of output embeddings (Table 1). These directly justify the gate architecture and training strategy.

- **Order-of-magnitude confusion reduction without task degradation.** Table 3 shows dramatic, consistent drops across all models: Qwen3-30B-A3B CJ% from 1.0% to 0.0%, Latin% from 4.4% to 0.4%; Qwen3-8B Latin% from 12.1% to 2.0%. BLEU scores remain stable or slightly improve across the board. The INCLUDE benchmark confirms that task accuracy is preserved (Qwen3-30B: 71.12 → 70.83, not a meaningful drop). These are unusually clean and strong results for a decoding intervention.

- **Norm-adjusted self-distillation is a novel and effective mechanism.** The ablation comparing LCG-adjusted vs. LCG-unadjusted (Table 3) shows that norm adjustment during gate training consistently improves confusion reduction (e.g., Llama3.1-8B Latin% drops from 5.7% unadjusted to 2.9% adjusted, Qwen3-30B from 0.7% to 0.4%). This validates the core mechanistic insight about embedding norm bias.

- **Practical, efficient, and well-validated deployment characteristics.** The gate adds 0.4% per-step overhead in a production setting (15.95ms → 15.99ms), with a sparse intervention rate of 0.38% (523 interventions across 139,354 tokens for Qwen3-8B). The plug-in architecture requires no base model retraining.

- **Thoughtful evaluation design.** The FLORES-NO-LATIN / FLORES-WITH-LATIN partition (Section 5.2) enables reliable Latin confusion measurement by only flagging Latin characters where ground-truth references contain none, avoiding false positives from legitimate code-switching. The explicit justification for not using LCB (unreliable language detection, required code-switching in some queries) shows careful methodology.

- **Comprehensive model and task coverage.** Evaluation spans seven models across three architectures (Qwen3, Llama3.1, Gemma3, GPT-OSS), both thinking and no-think modes, and three task types (translation, knowledge QA, code generation). Comparison against ICL, greedy decoding, and ORPO baselines (Figure 3) provides useful context, and the "No Rule" ablation confirms the intervention rules add value beyond the gate alone.

## Weaknesses

### Major

- **Missing comparison with a direct norm-adjusted masking baseline.** The gate is trained to predict which language families appear among the norm-adjusted top-k/p candidates — essentially learning to approximate a deterministic rule. The paper argues (Section 3.2) that norm bias "can't be directly used for intervention" because it cannot explain confusion between languages with similar norms (e.g., English vs. Chinese). However, a direct inference-time baseline — compute norm-adjusted logits, identify language families in the top-k/p, and mask the rest — would test whether the trained gate provides any benefit over the very signal it is trained to mimic. The "No Rule" ablation (Figure 3) removes the intervention rules but retains the trained gate, so it does not answer this question. Without this comparison, the paper does not fully establish that the learned gate is necessary rather than merely sufficient. This is a significant gap in the evaluation design.

### Minor

- **Hyperparameters for pseudo-target generation not specified.** Section 4.2 describes generating pseudo-targets via top-k/p filtering of norm-adjusted logits but does not provide the specific k and p values used. Since the pseudo-labels define what the gate learns, these choices affect the method's behavior and reproducibility.

- **Gate prediction accuracy not reported.** The paper never reports how accurately the trained gate predicts the pseudo-targets (e.g., precision/recall per language family). Without this, it is unclear whether the gate is a faithful proxy for the norm-adjusted signal or introduces its own errors that the intervention rules must compensate for.

- **Code-switch experiment lacks annotation details.** The claim that LCG preserves 86.7% of human-validated code-switches (Section 5.3) is encouraging but is reported without sample size, annotation protocol, or inter-annotator agreement metrics. This weakens the reliability of the finding.

- **No confidence intervals reported.** All confusion rate reductions, BLEU scores, and accuracy changes are reported as point estimates without variance information. Given that some confusion rates are low (e.g., 0.0%–0.5%), even small absolute differences may be sensitive to sampling variation.

- **ORPO comparison lacks training details.** The paper states that ORPO samples were synthesized "similar as Lee et al. (2025)" but does not provide the dataset size, hyperparameters, or number of training steps. While the ORPO comparison is supplementary, readers cannot assess the fairness of this comparison.

## Nice-to-Haves

- A quantitative analysis directly linking embedding norm imbalance to observed confusion tokens (beyond the single illustrative example in Figure 2) would strengthen the mechanistic argument.
- An additional open-ended generation task (e.g., summarization in a non-English language) would further support the claim that LCG causes no subtle fluency degradation.
- Gate prediction accuracy broken down by language family and dataset would help users understand failure modes.
- A discussion of whether the gate could be replaced by a deterministic norm-adjusted masking rule, and if not, what context the gate integrates that the rule cannot capture.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic: "Gate's accuracy is never reported, making it impossible to judge whether the gate is a faithful proxy"** — Kept as a Minor weakness above (verified — the paper indeed does not report gate accuracy).

- **Harsh Critic: "The link to language confusion is established only through a single qualitative example (Figure 2)"** — Demoted to Nice-to-Have. The paper does provide Table 1 with quantitative norm statistics across models, and Figure 2 is illustrative. The connection is reasonably established for the paper's purposes, though a direct quantitative link would be stronger.

- **Harsh Critic: "The ORPO comparison lacks essential reproducibility details"** — Kept as Minor. The paper's core contribution does not depend on the ORPO comparison, but the missing details are a real gap.

- **Strength Finder: "Thorough baseline comparison shows LCG outperforms alternatives"** — Partially retained. The baseline comparison is useful but incomplete due to the missing direct norm-adjusted masking baseline (noted in Major weakness).

- **Harsh Critic: "No confidence intervals"** — Kept as Minor. True, but standard for this type of benchmark evaluation.

- **Harsh Critic: "The paper would benefit from at least one more open-ended generation task"** — Demoted to Nice-to-Have. The existing evaluation (translation, knowledge QA, code generation) already spans diverse task types.

- **Harsh Critic: "The paper provides no details about the size of the human-annotated set, the annotation protocol, or inter-annotator agreement"** — Kept as Minor. A genuine gap in the code-switch experiment reporting.

## Novel Insights

None beyond the paper's own contributions. The reviewers' observations largely confirm or question the paper's claims without generating independent insights.

## Suggestions

- **Add the direct norm-adjusted masking baseline.** This is the highest-impact addition: implement the inference-time rule that computes norm-adjusted logits, identifies language families in the top-k/p, and masks the rest. Compare against LCG on the same benchmarks. If the gate outperforms the rule, explain why (e.g., the gate integrates multi-step context or learns to smooth across noisy pseudo-targets). If performance is similar, the paper's framing should shift to acknowledge that the gate approximates a simpler rule, and the contribution lies in making this approximation stable and efficient.

- **Report the specific top-k and top-p values** used for generating pseudo-targets in Section 4.2, and report the gate's multi-label prediction accuracy (precision/recall per family) on the evaluation datasets.

- **Add annotation details for the code-switch experiment**: sample size, annotation protocol (how many annotators, what instructions), and inter-annotator agreement.

## Score and Decision

**Anchor comparison summary:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| fSbPwHjdDG (Latent Language of Transformers) | 3.00 | 1 | Worse — thin analysis, unclear contribution |
| 4y3GDTFv70 (Latent Space Theory) | 3.25 | 1 | Worse — speculative, limited evidence |
| I1VCj1l1Zn (DLP-LoRA) | 3.00 | 1 | Worse — limited novelty, modest results |
| 4z3IguA4Zg (DeCo Hallucination) | 6.00 | 1 | Better — stronger results, better motivation |
| 5bUy4F59mk (Tool Decoding) | 6.00 | 1 | Better — cleaner evaluation, stronger results |
| HgAS03GU4J (Nudging) | 6.00 | 1 | Better — more practical, clearer use case |
| vf5aUZT0Fz (DEPT) | 8.00 | 1 | Worse — less fundamental novelty, narrower scope |
| WbWtOYIzIK (Knowledge Card) | 8.00 | 1 | Worse — less comprehensive, narrower contribution |
| 8wjWm5jr1w (Multi-Granularity KD) | 6.00 | 2 | Better — stronger results, cleaner method |
| uWtLOy35WD (LLaVA-MoD) | 6.50 | 2 | Comparable — similar evaluation breadth, missing-baseline concern on both sides; LCG has stronger results, LLaVA-MoD has more architectural novelty |
| HMa8mIiBT8 (Cross-Lingual Consistency) | 6.00 | 2 | Better — more actionable contribution, stronger results |

The paper makes a clear, well-motivated contribution with unusually strong empirical results — order-of-magnitude confusion reduction without task degradation across seven models. The norm-adjusted self-distillation technique is novel, the plug-in architecture is practical (0.4% overhead), and the evaluation design (FLORES partition) is thoughtful. The missing comparison with a direct norm-adjusted masking baseline is a genuine evaluation gap that prevents a higher score, but it does not invalidate the demonstrated results, and the paper already provides evidence that the gate (via LCG-adjusted vs. LCG-unadjusted ablation and the No Rule experiment) is doing meaningful work beyond trivial decoding changes.

**Originality**: The norm-adjusted self-distillation approach for training a lightweight language-family gate is novel. The decomposition of logits into norm and cosine-similarity components to explain and address language confusion is a clean mechanistic insight.

**Importance**: Language confusion is a genuine, widespread problem affecting even SOTA commercial models (Table 2). A lightweight, plug-in solution that doesn't require retraining has clear practical value.

**Claims supported**: The core claim — that LCG reduces confusion by an order of magnitude without harming task performance — is well-supported by Tables 3-5 and Figure 3. The claim about necessity of the trained gate specifically (vs. a deterministic rule) is not fully supported.

**Soundness**: The methodology is sound apart from the missing baseline. The evaluation design (FLORES partition, multi-task evaluation, thinking and no-think models) is careful.

**Clarity**: The paper is well-written and well-organized, with clear motivation and accessible explanations of the mechanistic observations.

**Value to community**: High — the method is practical, the training dataset is open-sourced, and the approach could generalize to other decoding-time intervention problems.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
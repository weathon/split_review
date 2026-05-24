Now I have enough anchors to make a confident comparison. Let me synthesize my final review.

**Round 1 bracket:** The paper sits clearly above the weak band (GOOD at 4.5, rejected papers at 3.0-3.25) and below the strong band (X-ALMA at 7.33, DEPT at 8.0). Narrowest plausible bracket: **5.5–7.5**.

**Round 2 narrowing:** Compared to Tool Decoding (6.0), LCG has deeper mechanistic analysis, more baselines, efficiency numbers, and code-switching analysis — clearly stronger. Compared to Multilingual Jailbreak (6.4), LCG has more comprehensive model evaluation (5+ models vs 2), stronger method evaluation with multiple baselines, and better mechanistic motivation. LCG is slightly stronger than this anchor. Compared to X-ALMA (7.33), LCG is less ambitious (plug-in vs full model training), has a narrower scope, and lacks some methodological completeness — LCG is clearly weaker. 

The paper lands around **6.5**, comparable to or slightly above papers like Multilingual Jailbreak (6.4) and Chunk-Distilled LM (6.5), but below the 7.0+ tier of more comprehensive contributions.

---

## Summary

This paper introduces the Language Confusion Gate (LCG), a lightweight, plug-in decoding-time intervention that reduces unintended language mixing in LLMs without modifying base model weights. The gate is a small two-layer MLP trained via norm-adjusted self-distillation: it uses the model's own debiased (norm-adjusted) predictions as pseudo-targets to learn which language families are permissible at each generation step, then masks disallowed tokens during sampling. The method is motivated by three empirical observations about language confusion: it is rare, correct-language tokens are almost always in the top-3, and output token embedding norms are biased toward high-resource languages. Evaluated across Qwen3, Llama3.1, Gemma3, and GPT-OSS on translation (FLORES), QA (INCLUDE), and code generation (Humaneval-XL), LCG reduces CJ and Latin confusion rates by up to an order of magnitude while preserving task performance and legitimate code-switching in 86.7% of human-validated cases.

## Strengths

- **Mechanistic insight into token embedding norm bias**: The paper identifies that output token embedding norms are systematically larger for high-resource language tokens (Table 1) and demonstrates that norm-adjusting logits removes this bias at confusion points (Figure 2). This insight directly motivates the norm-adjusted self-distillation training procedure and distinguishes the method from a naive gate.

- **Consistent and substantial confusion reduction across models and tasks**: LCG reduces CJ and Latin confusion rates by up to an order of magnitude across four model families (e.g., Qwen3-30B CJ% 1.0→0.0, Latin% 4.4→0.4; Qwen3-8B Latin% 12.1→2.0) while BLEU and accuracy remain stable or slightly improve (Tables 3–4). Results hold across translation, QA, and code generation tasks.

- **Preservation of legitimate code-switching**: The paper directly tackles the key practical challenge of distinguishing harmful confusion from natural code-switching. LCG permits human-validated code-switches in 86.7% of cases, and post-intervention code-switch rates remain above the Claude Sonnet 4 baseline (Table 5, Section 5.3).

- **Ablation confirms norm-adjustment is necessary**: LCG-adjusted consistently outperforms LCG-unadjusted across all models and metrics (Table 3), providing clean evidence that the norm-based debiasing is a critical component.

- **Practical efficiency**: The gate intervenes on only 0.33–0.38% of generated tokens, adding ~0.4% computational overhead per generation step (Section 6). This makes the method genuinely deployable.

- **Strong baseline comparisons**: LCG is compared against in-context learning, greedy decoding, ORPO fine-tuning, and a no-rule ablation (Figure 3), outperforming all while avoiding the task degradation observed with ORPO.

## Weaknesses

### Fatal

None.

### Major

- **Train/evaluation data split not specified for FLORES**: The training data includes the FLORES+ dataset (Section 5.1), and the primary evaluation for Latin confusion is on FLORES-NO-LATIN, a partition of the same FLORES+ collection (Section 5.2). The paper does not state whether the specific test sentences were excluded from gate training. The CJ confusion results on INCLUDE and Humaneval-XL (completely separate datasets) provide cross-benchmark corroboration, but the Latin confusion evaluation — a central claim — rests on an unverified train/test separation. Clarifying this split would substantially strengthen confidence in the Latin confusion results.

### Minor

- **Training hyperparameters underspecified**: Section 4.2 states that pseudo-targets are constructed using top-k/top-p filtering of norm-adjusted logits but does not report the specific k and p values used during training. The inference rules in Section 4.3 specify thresholds (k=5, p=0.999; k=20, p=0.95), but the training values remain unreported. Additionally, it is not stated whether hidden states were collected via teacher-forced forward passes or autoregressive generation. These gaps hinder reproducibility.

- **Gate prediction accuracy not directly evaluated**: The paper compares LCG-adjusted vs. LCG-unadjusted and includes a "No Rule" ablation (Figure 3), but does not report the gate's standalone prediction quality (e.g., precision/recall against the norm-adjusted pseudo-targets, or against an oracle language-family labeling). A breakdown of how often the rules override the gate and the effect of those overrides would sharpen the narrative about the learned component's reliability.

- **Motivating analysis limited to one model**: The finding that correct-language tokens appear in the top-3 99.29% of the time (Section 3.1) is based solely on Qwen3-8B and FLORES-NO-LATIN. While this is a useful motivating observation, its generality across models is not demonstrated.

- **ORPO baseline details sparse**: The ORPO comparison (Figure 3) is valuable, but the paper provides minimal detail on how the synthetic negative samples were constructed and what hyperparameters were used, making the comparison harder to interpret.

### Trivial

- **No variance or significance measures**: Confusion rates and BLEU/accuracy scores (Tables 3–4) are reported as point estimates without confidence intervals or significance tests, so small fluctuations (e.g., BLEU 13.2→13.4) cannot be interpreted with confidence.

## Nice-to-Haves

- A systematic table showing what fraction of confusion errors are attributable to norm bias (e.g., comparing confusion rate with and without norm adjustment in top-k selection) would tie the motivational analysis more directly to the method.
- A few concrete failure cases where LCG fails to prevent confusion or incorrectly suppresses legitimate code-switching would help calibrate reader expectations.
- Reporting whether a separate gate was trained per model or whether one gate was used across models (Section 5.1 says "this same dataset was used to train the gate for both thinking and no-think models" but does not clarify if the gate parameters are shared).

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh critic's claim that "the paper provides no direct evaluation of its standalone prediction accuracy... this missing analysis weakens the evidence that the core learned component... is robustly solving the problem"**: This has been demoted to Minor and reframed. The No Rule ablation and LCG-adjusted vs LCG-unadjusted comparison provide indirect evidence. The absence of direct gate accuracy metrics is a gap, not a fatal flaw.
- **Harsh critic's claim about Figure 2 being an imperfect example (norm adjustment replaces CJ with Latin, but Hebrew is non-Latin)**: The paper explicitly acknowledges that "norm bias can account for a subset of such errors but cannot fully explain language confusion" (Section 3.2). The example is illustrative, and the paper is transparent about the limitation. Removed as a weakness but noted the paper's own acknowledgment covers this.
- **Strength Finder's generic strengths about "important problem" and "interesting question"**: Removed as superficial. Retained only concrete, evidence-backed strengths.
- **Harsh critic's point about "abstract and introduction... minor ordering issue"**: Removed as a pure formatting nitpick.
- **Harsh critic's claim about "no variance or significance measures" being a major concern**: Demoted to Trivial — single-run evaluation without confidence intervals is standard practice in large-scale LLM benchmark evaluation in this field.

## Novel Insights

The key novel insight is the identification and exploitation of output token embedding norm imbalance as a mechanism behind language confusion. The paper shows that high-resource language tokens have systematically larger embedding norms (Table 1), and that dividing logits by these norms removes the bias (Figure 2). Rather than using norm-adjustment directly for intervention (which the paper correctly notes cannot resolve all confusion), the authors use it to construct debiased pseudo-targets for self-distillation — a clever synthesis of mechanistic analysis and practical method design that goes beyond either approach alone.

## Suggestions

- Explicitly state that FLORES test sentences were excluded from gate training, and specify whether a validation set was used for model selection. This is the single highest-impact clarification for the paper's credibility on Latin confusion.
- Report the top-k and top-p values used during training pseudo-target construction, and clarify whether training states were collected via teacher-forcing or generation.
- Include a brief gate accuracy evaluation (F1 or accuracy against the norm-adjusted pseudo-targets on a held-out set) to make the learning story more concrete and separate the contribution of the learned gate from the hand-crafted rules.

## Score and Decision

**Calibration summary:**

| Anchor | Avg Score | Round | Comparison |
|---|---|---|---|
| fSbPwHjdDG (Llamas think in English) | 3.00 | R1 low | LCG is substantially stronger — this is pure analysis, no method |
| uOnElfFuey (Recovering Knowledge) | 3.00 | R1 low | LCG is substantially stronger |
| cayKVPCrOP (GOOD) | 4.50 | R1 mid | LCG is stronger — better efficiency, more baselines, mechanistic motivation |
| 5bUy4F59mk (Tool Decoding) | 6.00 | R1 mid | LCG is stronger — more baselines, efficiency analysis, code-switching evaluation, deeper analysis |
| vESNKdEMGp (Multilingual Jailbreak) | 6.40 | R2 | LCG is comparable/slightly stronger — more comprehensive model evaluation, better method evaluation with baselines |
| nrvoWOWcyg (Chunk-Distilled LM) | 6.50 | R2 | LCG is comparable — both are practical decoding-time improvements with solid evaluation |
| r8H7xhYPwz (Gated Delta Networks) | 7.00 | R2 | LCG is weaker — GDN has stronger theoretical grounding and broader benchmark coverage |
| csbf1p8xUq (X-ALMA) | 7.33 | R2 | LCG is clearly weaker — X-ALMA is a full training recipe with SOTA results across 50 languages |

**Round 1 bracket:** 5.5–7.5. **Round 2 narrowing:** LCG lands at approximately 6.5 — above Tool Decoding (6.0), comparable to Multilingual Jailbreak (6.4) and Chunk-Distilled LM (6.5), but below the 7.0+ tier.

The paper makes a solid contribution: a well-motivated, practically efficient, and thoroughly evaluated method for mitigating language confusion. The mechanistic analysis linking norm bias to confusion is genuinely insightful and the method design follows naturally from it. The comprehensive evaluation across models, tasks, and baselines — including the careful handling of the code-switching vs. confusion distinction — is a strength. The remaining weaknesses (train/test split clarity, missing training hyperparameters, gate accuracy analysis) are addressable and do not undermine the core claims, though they prevent the paper from reaching the top tier.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
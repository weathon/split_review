## Summary

This paper introduces the Language Confusion Gate (LCG), a lightweight plug-in module that reduces language confusion in multilingual LLM generation. The gate is a two-layer MLP trained via norm-adjusted self-distillation: it uses the frozen LLM's own debiased logits (dividing by token embedding norms) to generate pseudo-targets for language-family prediction (CJ, Latin, Symbols, Low-Res), then masks disallowed tokens at decoding time. Evaluated across Qwen3, Llama3.1, Gemma3, and GPT-OSS on translation (FLORES+), knowledge/reasoning (INCLUDE), and code generation (Humaneval-XL), LCG reduces confusion rates by roughly an order of magnitude (e.g., CJ confusion from 1.0%→0.0% and Latin confusion from 4.4%→0.4% on Qwen3-30B) with only 0.4% latency overhead, while preserving legitimate code-switching.

## Strengths

- **Order-of-magnitude confusion reduction across diverse models and tasks**: On FLORES-NO-LATIN, LCG-adjusted cuts CJ confusion from 1.0% to 0.0% and Latin confusion from 4.4% to 0.4% for Qwen3-30B, and from 12.1% to 2.0% (Latin) for Qwen3-8B (Table 3). These reductions hold across four model families and two task categories (translation and knowledge/reasoning), with stable BLEU/accuracy scores. Results on thinking models (Table 4) show similar patterns without degrading Pass@1/Pass@10.

- **Norm-adjusted self-distillation is a principled and well-justified training mechanism**: The paper first identifies token embedding norm imbalance (Table 1: high-resource language tokens dominate top-5% norms) as a source of bias, then uses norm-adjusted logits to generate cleaner pseudo-targets for gate training. The ablation (LCG-adjusted vs. LCG-unadjusted in Table 3) consistently shows improvement, validating that the norm-adjustment step contributes meaningfully (e.g., Llama3.1-8B Latin% drops from 5.7% to 2.9%).

- **Minimal overhead and sparse intervention make the method practical**: LCG intervenes on only 0.33–0.38% of generated tokens (Section 5.3) and adds just 0.4% per-step latency (15.95ms → 15.99ms) in a production deployment, without requiring model retraining. This combination of effectiveness and efficiency distinguishes LCG from methods that require full fine-tuning.

- **Legitimate code-switching is largely preserved**: The paper evaluates on FLORES-WITH-LATIN and finds LCG-adjusted allows English tokens at 86.7% of human-validated confusion points. The post-intervention code-switch rate (25.90% for Qwen3-8B) remains above the Claude Sonnet 4 baseline (23.29%) and comparable to the ground-truth answer rate (38.36%), demonstrating that LCG does not over-suppress valid multilingual behavior.

- **Comprehensive baseline comparison**: Figure 3 compares LCG against ICL, greedy decoding, and ORPO tuning. LCG consistently outperforms all three, and the paper documents that ORPO degrades INCLUDE accuracy (Qwen3-8B: 61.43→57.3), highlighting LCG's advantage as a non-destructive intervention.

## Weaknesses

### Major

- **Missing training hyperparameters for reproducibility**: The pseudo-target generation during training relies on top-k/top-p filtering of norm-adjusted logits, but the specific *k* and *p* values used during training are not stated. The training procedure for the gate (learning rate, number of epochs, optimizer, batch size) is also omitted entirely. While inference-time rules specify (k=5, p=0.999) and (k=20, p=0.95), these are intervention rules, not training parameters. Since the gate's quality depends on the pseudo-targets, the missing hyperparameters prevent replication and sensitivity analysis. The paper should specify the k/p values used for pseudo-target generation and the full training configuration.

- **No variance or confidence interval estimates**: All results in Tables 3, 4, and 5 are reported as single point estimates. Confusion rates are often small percentages (e.g., 0.0–4.5% CJ), and without error bars or repeated-trial information, it is impossible to assess whether the reported improvements are statistically reliable or within evaluation noise. For instance, CJ confusion dropping from 1.0% to 0.0% on Qwen3-30B is a compelling result, but the reader cannot determine whether this reflects genuine elimination or a chance outcome on a finite sample. The human evaluation for code-switch preservation (86.7%) similarly lacks sample size, inter-annotator agreement, and selection criteria.

### Minor

- **Low-resource-language confusion is not evaluated**: The intervention rule (1) states that Low-Res tokens are never masked, and the paper acknowledges that confusion between two low-resource languages cannot be addressed by LCG because both fall in the same family. However, the evaluation datasets include target languages that are themselves low-resource (Arabic, Hebrew, Korean, Thai, Vietnamese), meaning Low-Res-to-Low-Res confusion is measurable but unreported. The paper should either evaluate this blind spot or present explicit evidence for why it is negligible.

- **ORPO baseline lacks implementation detail**: The paper reports that ORPO was applied with "a multilingual dataset" and "synthesize samples with language confusion as rejected samples" (Section 5.3), but gives no specifics about dataset size, training steps, learning rate, or base model checkpoints. Since the paper claims LCG outperforms ORPO, the comparison should be reproducible.

- **Latin confusion evaluation may overcount legitimate carry-over**: FLORES-NO-LATIN filters by checking whether ground-truth translations contain Latin characters, but does not check whether the *source* English text contains Latin characters (proper nouns, technical terms like "Python") that could legitimately appear in the output. This could inflate Latin confusion rates symmetrically for baseline and LCG, but the paper should discuss or filter this case.

- **Persistence rule failure mode is unanalyzed**: Intervention rule (3) always allows the language family of the preceding non-symbol token. If a confusion token slips through the gate (e.g., via the high-confidence override rule), its language family is automatically permitted for the next step, potentially propagating the error. The paper does not analyze how often this occurs or whether the "No Rule" ablation (Figure 3) disentangles this effect. While the overall results are strong, this structural concern merits discussion.

### Trivial

- The gate architecture is described as a "two-layer MLP" with output size 4 (ℝ⁴), but the hidden dimension is not explicitly stated.

## Nice-to-Haves

- A quantitative decomposition of what fraction of confusion events are resolved by norm-adjustment alone vs. the learned gate would strengthen the claim that both components are necessary.
- Evaluation on an additional open-ended generation task (beyond translation, QA, and code) would test whether LCG generalizes without suppressing valid code-switching in other contexts.
- Reporting the percentage of intervention steps where the persistence rule (rule 3) is the sole reason a language family is allowed would directly address the structural concern about error propagation.

## Removed Points

These points were flagged in the inputs but are excluded from the main review for the reasons noted:

- **"LCG cannot be reproduced because k/p unspecified"** → Retained as Major (it is a genuine reproducibility gap), but reformulated to focus on training hyperparameters specifically.
- **"The paper claims confusion is rare but provides no evidence"** → The paper provides evidence: confusion rates are 0.2–12.1% (Table 3), and intervention frequency is 0.33–0.38% — these numbers support the claim. REMOVED as factually incorrect (the paper does provide evidence).
- **"Table 1 should show mean norms per family rather than top-5% fractions"** → The top-5% proxy is a reasonable and conventional way to illustrate distribution imbalance. This is a presentation preference, not a weakness. MOVED to Nice-to-Haves.
- **"Norm bias contribution should be quantified"** → The ablation (LCG-adjusted vs. LCG-unadjusted) already quantifies the contribution of norm-adjustment, showing consistent improvements. MOVED to Nice-to-Haves.
- **"Missing related works"** → The paper's related work section covers Marchisio et al. (2024), Nie et al. (2025), Ji et al. (2025), Li et al. (2025), and Lee et al. (2025) — this is adequate. REMOVED per hard rule.
- **"Formatting/style nitpicks"** → REMOVED per hard rule.
- **"Missing appendix content"** → REMOVED per hard rule (parser strips appendices).

## Novel Insights

None beyond the paper's own contributions. The key insight — that token embedding norm imbalance biases language-mixing behavior and that norm-adjusted self-distillation can train a lightweight gate — is already the paper's central contribution.

## Suggestions

1. **Specify all training hyperparameters**: Report the k/p values used during pseudo-target generation, and provide the learning rate, optimizer, number of epochs, and batch size for gate training.
2. **Add confidence intervals**: Use bootstrapped 95% CIs for confusion rates and BLEU/accuracy scores across the main tables.
3. **Report human evaluation details**: Provide the sample size, inter-annotator agreement (e.g., Cohen's κ), and selection criteria for the code-switch preservation study.
4. **Evaluate or discuss Low-Res confusion**: Report whether LCG introduces or fails to prevent confusion among low-resource languages, or present evidence why this scenario is negligible.
5. **Document the ORPO baseline**: Provide dataset size, training steps, learning rate, and model checkpoints used for the ORPO comparison.

## Score and Decision

### Calibration Procedure

**Round 1 — Bracketing**: Searched for papers on "language confusion mitigation multilingual LLM decoding time intervention" across three bands:
- Low band (<3.5): Results at 3.00 (speculative decoding, LLM intervention papers) — clearly below this paper.
- Middle band (3.5–7.5): Results at 4.75–5.75 (crosslingual knowledge barriers at 5.67, multilingual code LLM at 5.25, speculative decoding adaptation at 5.75) — plausible comparison range.
- High band (>7.5): Results at 8.00–8.50 (pretraining, diffusion, unlearning) — clearly above this paper's scope and ambition.

**Initial bracket**: 5.0 – 7.0.

**Round 2 — Narrowing**: Searched for papers on "decoding time intervention language control LLM plug-in lightweight" (4.5–6.5 band) and "multilingual LLM language mixing confusion mitigation evaluation" (6.0–8.0 band).

Read in full:
- **SASA / Self-Detoxifiers** (avg 6.00, all 6s, Accept): Lightweight decoding-time control using internal LLM representations for toxicity. Similar in structure to LCG. SASA had clearer hyperparameter specification but comparable evaluation breadth. LCG's results are more dramatic (order-of-magnitude) but its reporting gaps are larger. → LCG is slightly weaker.
- **SADI / Activation Intervention** (avg 6.40, Accept): Dynamic steering vectors for LLM alignment. More general-task focus, similar lightweight intervention paradigm. LCG has more targeted, practical contribution but less thorough reporting. → LCG is slightly weaker.
- **Tool Decoding** (avg 6.00, all 6s, Accept): Plug-and-play constrained decoding for tool use. Similar in being a training-free plug-in. Comparable contribution level. → LCG is comparable.

**Final calibration**: The paper sits between the 5.5 and 6.0 anchors. It has a stronger, more novel technical contribution than the 5.5 anchor (code LLM evolution at 5.25) but weaker reporting rigor than the 6.0 anchors (which specify hyperparameters and include variance estimates). The reproducibility gaps (missing training parameters) and absence of statistical rigor prevent it from reaching 6.0, but the empirical results are clearly valuable.

**Anchors used**:
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| fSbPwHjdDG (Llamas think in English) | 3.00 | 1 | Well below LCG |
| n7iwmPacDt (Polybasic Spec Decoding) | 3.00 | 1 | Well below LCG |
| BCyAlMoyx5 (Crosslingual Barriers) | 5.67 | 1 | Weaker contribution, LCG stronger |
| eznTVIM3bs (Babel Tower) | 5.25 | 1 | Comparable analysis depth, LCG more practical |
| xOtOfdbBqK (Spec Decoding Adaptation) | 5.75 | 1 | Different domain, similar quality |
| jY5oml9fe9 (SASA Self-Detoxifiers) | 6.00 | 2 | Most similar paradigm; LCG weaker on reporting |
| 8WQ7VTfPTl (SADI Activation Intervention) | 6.40 | 2 | Stronger on thoroughness; LCG weaker |
| 5bUy4F59mk (Tool Decoding) | 6.00 | 2 | Comparable plug-and-play approach |

### Score

The paper makes a genuine, practical contribution to a real problem. The norm-adjusted self-distillation approach is well-motivated and the empirical results are compelling across multiple models. The main factors preventing a higher score are the missing training hyperparameters (which undermine full reproducibility) and the absence of any variance or confidence-interval reporting. These are fixable issues, but as submitted they limit confidence in the results.

**Score**: 5.5  
**Decision**: Weak Accept (borderline — the contribution is real and the issues are addressable, but the paper must disclose training hyperparameters and ideally add variance estimates for the main results.)

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
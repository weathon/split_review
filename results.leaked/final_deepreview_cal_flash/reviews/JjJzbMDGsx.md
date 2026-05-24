Now I have a solid calibration. Let me write the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

The paper introduces the Language Confusion Gate (LCG), a lightweight plug-in that filters inappropriate tokens during LLM decoding by predicting permissible language families via a small MLP. The gate is trained via norm-adjusted self-distillation, leveraging a mechanistic analysis showing that output token embedding norms are biased toward high-resource languages. Experiments across four base models and three thinking models show substantial reductions in language confusion (often 5–45×) with minimal (0.4%) latency overhead.

## Strengths

- **Novel and mechanistically grounded training signal.** The norm-adjusted self-distillation approach is a genuine methodological contribution. The paper identifies that output token embedding norms are systematically larger for high-resource languages (Table 1), shows that adjusting by norm reveals the correct language family in top-k predictions (Figure 2), and confirms via ablation (LCG-adjusted vs. LCG-unadjusted in Table 3) that this norm-aware training consistently improves performance. This gives the gate a principled foundation that goes beyond simply training on raw logits.

- **Consistent and substantial confusion reduction across diverse models and tasks.** LCG reduces confusion rates across 7 model variants (Qwen3-8B/30B, Llama3.1-8B, Gemma3-12B, GPT-OSS-20B) on both translation (FLORES) and knowledge/reasoning (INCLUDE) benchmarks, as well as code generation (HumanEval-XL). Task performance metrics (BLEU, accuracy, Pass@1/10) are stable or slightly improved. The reduction is demonstrated in both thinking and non-thinking modes, covering a useful range of deployment scenarios.

- **Lightweight and practical design.** The gate intervenes on only 0.33–0.38% of generated tokens and adds 0.4% latency overhead (15.95 → 15.99 ms per step). It operates at decoding time without modifying the base model, making it suitable for production deployment alongside speculative decoding.

- **Explicit consideration of legitimate code-switching.** The paper acknowledges the critical distinction between erroneous language confusion and natural code-switching, and provides multiple forms of evidence (86.7% token-level allowance of human-validated code-switches, response-level analysis on FLORES-WITH-LATIN in Table 5). This reflects a more nuanced understanding of the problem than simply enforcing language consistency.

## Weaknesses

### Fatal
None.

### Major

- **Missing comparison against the most directly related plug-in methods.** The paper describes Ji et al. (2025) (post-hoc smoothing for suppressing Chinese token intrusion) and Nie et al. (2025) (neuron suppression during inference) in the Related Work, noting that they are closely related plug-in interventions for language confusion. Yet neither is included as an experimental baseline. The paper instead compares against ICL, greedy decoding (neither is specifically designed for language confusion), and ORPO (a fine-tuning method, not a plug-in). Without these comparisons, the claim that LCG offers advantages over existing plug-in solutions cannot be properly evaluated. This is the most significant evidential gap.

- **Lack of statistical rigor for main results.** Tables 3 and 4 report confusion rates and task metrics without confidence intervals, standard errors, or significance tests. This is especially concerning given that confusion base rates are low (0–12%), making point estimates potentially unstable — a reduction from, e.g., 0.2% to 0.1% represents only a handful of examples. The paper does not specify the number of evaluation samples, repeat runs, or variance across seeds for the main confusion metrics.

- **Potential training-evaluation data overlap.** The training set (78k samples) includes the FLORES+ Dataset, and the evaluation uses FLORES+ for Arabic, Hebrew, Korean, and Thai to construct FLORES-NO-LATIN. If the same translation prompts appear in both training and evaluation, the gate could benefit from prompt-level leakage. The paper does not clarify the degree of overlap or whether any deduplication was performed.

### Minor

- **Code-switch preservation evidence is promising but incomplete.** The human evaluation (86.7% allowance) checks whether LCG *would have allowed* the base model's original code-switch tokens at those specific positions, but does not evaluate whether LCG's *own outputs* on code-switch-heavy prompts are natural and correct. The response-level analysis (Table 5) shows reduced code-switch rates but lacks human quality assessment of the remaining switches. The core claim about preserving code-switching ability would benefit from a side-by-side human evaluation comparing base model and LCG outputs on code-switch-heavy inputs.

- **"Order of magnitude" framing is imprecise.** The abstract claims reduction "often by an order of magnitude." While several results support this (Qwen3-8B CJ: 45×, Qwen3-30B Latin: 11×), others are more modest (Llama3.1-8B Latin: 2.9×, Gemma3-12B Latin: 2×). Roughly half of the 8 no-think results show <10× reduction. The claim would be more accurate as "typically 3–45×, often reaching an order of magnitude."

- **Individual intervention rules not ablated.** The "No Rule" ablation (Figure 3) shows that rules provide additional benefit, but the contribution of each rule is not examined independently. The persistence rule (always allowing the previous token's language family) could in principle perpetuate confusion if the preceding token is already wrong. Isolating each rule's effect would be informative.

- **Training hyperparameters not reported.** The MLP hidden dimension, learning rate, batch size, and number of epochs for training the gate are absent from the main paper. (They may appear in the stripped appendix, but a brief summary in the main text is expected for reproducibility.)

### Trivial

- The primary confusion metric is response-level (percentage of responses containing ≥1 unwanted character), which conflates a single errant token with pervasive confusion. Reporting token-level confusion rates alongside would align better with the reported intervention frequency (0.33–0.38%).
- No analysis of remaining confusion types (e.g., what errors persist despite LCG, which language pairs are most challenging) is provided.
- A brief summary of the BPE byte-handling heuristic (Appendix A) in the main text would help readability.

## Nice-to-Haves

- **Ablation of norm-adjusted logits as a direct decoding baseline.** The paper could quantify what fraction of confusion points are corrected by norm-adjusted logits alone (the observation in Section 3.2), versus the full learned gate, to better isolate the gate's added value.
- **Evaluation on same-script confusion** (e.g., English-French, Spanish-Portuguese). The paper acknowledges this as a limitation, but explicitly testing it would quantify the scope of the method's applicability.

## Removed Points

These points are flagged to be removed — treat them with caution:
- The harsh critic's point about ORPO being "not a plug-in intervention" that "conflates different deployment scenarios" — The paper includes ORPO as an additional baseline from a different category, which is reasonable for a broad comparison. The paper does not claim ORPO is a plug-in method. **MOVED TO REMOVED** as it mischaracterizes the paper's framing.
- The critic's demand for "human evaluation of LCG-output quality on code-switch-heavy prompts" as a necessary condition for acceptance — While this would strengthen the paper, the existing evidence (86.7% allowance, response-level analysis) provides reasonable support for the claim. The original point is demoted to Minor above; the demand for a full human evaluation is excessive for a paper that already makes a good-faith effort. **MOVED TO REMOVED** in its harsh form but retained as a Minor weakness about completeness.
- The critic's point about the norm analysis not being quantified ("what fraction of confusion points are corrected by norm adjustment alone") — This is a valid suggestion for improvement but is scope creep; the paper already uses norm-adjusted supervision for training, not as a standalone intervention. Retained as Nice-to-Have. **MOVED TO NICE-TO-HAVE**.
- The critic's point about "the paper does not evaluate scenarios where confusion occurs between languages sharing a script" — The paper explicitly acknowledges this limitation. **MOVED TO NICE-TO-HAVE**.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add the two most directly comparable baselines** — Implement and compare against the post-hoc smoothing method of Ji et al. (2025) and the neuron suppression approach of Nie et al. (2025). This is the single most impactful addition the authors can make.
2. **Report confidence intervals** for the main confusion metrics (Tables 3, 4), either via bootstrap resampling or multiple seeds. Given low base rates, this is essential for establishing reliability.
3. **Clarify training-evaluation data separation** — Explicitly state whether any FLORES+ prompts used in evaluation also appear in the training set, and if overlap exists, describe how it was handled.
4. **Add a human evaluation** of LCG output quality on code-switch-heavy prompts, comparing side-by-side with the base model, to directly substantiate the code-switch preservation claim.
5. **Report training hyperparameters** (learning rate, batch size, epochs, hidden dimension) and token-level confusion rates alongside response-level rates.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Searched for "language confusion mitigation decoding intervention LLM" with three bands. Weak band (<3.5): 3 anchors at avg scores 3.00–3.25 (rejected papers on language model analysis). Middle band (3.5–7.5): 4 anchors at avg scores 4.25–6.00 (including MLLM decoding correction at 6.0, metacognitive intervention at 6.0, self-correction at 5.4). Strong band (>7.5): 4 anchors at 8.0 (pre-training, unlearning, diffusion papers — substantially stronger). Initial bracket: [4.5, 6.5].

**Round 2 (Narrowing):** Searched with two queries targeting [4.5, 6.5] and [5.0, 7.0]. Key anchors read in full:
- **SASA — Self-Detoxifiers** (avg 6.0, Accept): Lightweight decoding intervention for toxicity using LLM internal representations. Compared against relevant baselines (though some missing). Similar in spirit to LCG. *LCG is slightly weaker due to more critical missing baselines.*
- **RaDis — Rationale Distillation** (avg 5.0, Reject): Self-distillation for translation. Limited novelty, missing baselines, unclear practical value. *LCG is clearly stronger — more novel method, more compelling results.*
- **AprAD — Approximately Aligned Decoding** (avg 5.75, Reject): Incremental combination of ASAp + speculative decoding for constrained generation. Marginal novelty. *LCG has stronger novelty but similar evaluation gaps.*
- **DECO — Dynamic Correction Decoding** (avg 6.0, Accept): Decoding intervention for MLLM hallucination mitigation. Similar structure (empirical observation → lightweight intervention). *LCG has comparable quality but more prominent missing baseline issues.*

**Final bracket after narrowing:** [5.0, 6.0]. The paper sits between the RaDis anchor (5.0, weaker contribution) and the SASA/DECO anchors (6.0, stronger evaluation completeness). Positioned closer to the middle-upper end of this bracket due to the genuine novelty of norm-adjusted self-distillation and strong empirical scope, but pulled down by the missing comparison against directly relevant plug-in baselines.

**Final Score:** 5.5

**Decision Rationale:** The paper presents a genuinely novel method (norm-adjusted self-distillation for a plug-in language confusion gate) with consistent empirical support across multiple models and tasks, and demonstrates practical efficiency. However, the absence of experimental comparison against the two most directly related plug-in methods (Ji et al., Nie et al.) that are cited in the paper, combined with the lack of statistical rigor and unaddressed potential training-evaluation overlap, leaves important open questions about relative performance and result reliability. These are fixable with additional experiments and analysis.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>
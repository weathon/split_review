Now I have sufficient data for calibration. Let me write the final consolidated review.

**Calibration Summary:**

**Round 1 bracket:** Based on initial comparison, the paper sits between 4–7. It is clearly stronger than the weak-band papers (avg 2.5–3.33 — flawed papers with major issues) and does not reach the level of the strong-band papers (avg 8.0 — breakthrough contributions like "LLMs Get Lost In Multi-Turn Conversation" or "Transducing Language Models").

**Round 2 narrowing:** Anchors read in full:
- "Multilingual Routing in Mixture-of-Experts" (avg 5.50, Accept Poster) — 1–2% improvements, mixed reviews. LCG has order-of-magnitude improvements and more models tested → **LCG is stronger.**
- "LinguaMap" (avg 5.33, Accept Poster) — Strong interpretability analysis but only 2 models. LCG tests 5 models, has clearer empirical results → **LCG is somewhat stronger.**
- "How Do Language Models Speak Languages?" (avg 4.50, Reject) — Same topic area but weaker empirical validation → **LCG is clearly stronger.**
- "AMiD" (avg 6.00, Accept Poster) — Strong theory but presentation issues and hyperparameter ambiguity. LCG has cleaner empirical story → **Comparable quality.**
- "Language-Specific Latent Process" (avg 5.00, Reject) — Limited to MC tasks, Anglocentric analysis → **LCG is stronger.**

The LCG paper sits slightly above the 5.33–5.50 anchors and is comparable to the 6.00 anchor, giving a final score of **6.0**.

---

## Summary

This paper addresses the practical problem of language confusion in multilingual LLMs — the generation of tokens from unintended language families. The authors propose Language Confusion Gate (LCG), a lightweight two-layer MLP that takes the LLM's hidden state and predicts which of four language families (CJ, Latin, Symbols, Low-Res) is permissible at each decoding step, masking disallowed tokens. LCG is trained via norm-adjusted self-distillation: pseudo-targets are derived from the frozen model's own top-k/p candidates after debiasing token embedding norms. Experiments across five models (Qwen3 8B/30B, Llama3.1-8B, Gemma3-12B, GPT-OSS) on translation and reasoning benchmarks show consistent order-of-magnitude reductions in confusion rates (e.g., Qwen3-30B CJ confusion from 1.0% → 0.0%, Latin confusion from 4.4% → 0.4%) with minimal overhead and without substantially degrading task performance or legitimate code-switching.

## Strengths

1. **LCG consistently reduces language confusion by an order of magnitude across multiple models.** Table 3 shows large and consistent reductions across Qwen3-8B/30B, Llama3.1-8B, and Gemma3-12B on both FLORES-NO-LATIN and INCLUDE benchmarks. For instance, Qwen3-8B CJ confusion drops from 4.5% to 0.1% and Latin confusion from 12.1% to 2.0%. These are not marginal improvements but genuine, practically meaningful reductions.

2. **Norm-adjusted self-distillation is a validated methodological contribution.** The ablation (LCG-adjusted vs. LCG-unadjusted in Table 3) shows norm adjustment consistently improves results, e.g., Llama3.1-8B Latin confusion drops from 5.7% to 2.9%. This directly validates the key claim that token embedding norm bias is a source of confusion and that correcting it improves the training signal.

3. **Task performance and code-switching ability are preserved.** BLEU scores remain stable or improve slightly (Qwen3-30B: 13.2→13.4). On FLORES-WITH-LATIN, 86.7% of human-validated natural code-switch points are allowed, and post-intervention code-switch rates remain above the Claude Sonnet 4 baseline, demonstrating the gate distinguishes erroneous confusion from legitimate mixing.

4. **LCG substantially outperforms existing baselines.** Figure 3 shows LCG far outperforms ICL, greedy decoding, and ORPO on confusion reduction. ORPO in particular degrades INCLUDE accuracy (Qwen3-8B: 61.4→57.3), highlighting LCG's advantage as a targeted, non-degrading intervention.

5. **Minimal overhead and practical deployability.** LCG adds only 0.4% per-step generation time (15.95ms→15.99ms for Qwen3-30B) and intervenes on just 0.33–0.38% of tokens, making it suitable for production deployment.

## Weaknesses

### Fatal

None.

### Major

- **The self-distillation training loop's reliance on pseudo-target quality is under-analyzed.** The pseudo-targets are generated from the model's own norm-adjusted top-k/p candidates. The paper acknowledges that norm adjustment "cannot fully explain language confusion" (Section 3.2), which implies that some confusion errors will persist in the pseudo-targets. However, the paper provides no diagnostic analysis of how often the pseudo-targets are correct vs. noisy, nor does it characterize the cases where they fail. This is a genuine methodological gap: the mechanism by which the gate learns correct behavior despite learning from a potentially noisy signal is not adequately justified. The empirical results strongly suggest the method works, but understanding *why* would substantially strengthen the paper. The authors could address this by reporting pseudo-target accuracy on confusion vs. non-confusion points.

### Minor

- **Evaluation of low-resource language behavior is absent.** The gate classifies tokens into four families including "Low-Res," and the intervention rules (Section 4.3) state Low-Res tokens are never masked. Yet the evaluation covers only CJ and Latin confusion across 8 target languages that are all medium-to-high resource (Arabic, Hebrew, Korean, Thai, Chinese, Greek, Russian, Vietnamese). There is no experiment verifying that the gate makes correct predictions for low-resource-language contexts — either that it correctly predicts Low-Res as allowed when the target language is low-resource, or that it avoids misclassifying token families. The paper acknowledges script-level granularity as a limitation but should also discuss this evaluation gap.

- **No statistical uncertainty quantification for confusion metrics.** Confusion rates are reported as single percentages (e.g., 0.0%, 0.1%, 0.4%). With such low base rates, even small fluctuations in a handful of samples could change results noticeably. Standard errors, confidence intervals, or bootstrap estimates are not provided. This is especially relevant for comparing closely matched conditions (e.g., LCG-adjusted vs. LCG-unadjusted Latin% on Gemma3-12B: 0.5% vs. 0.6%) where the differences could be within noise.

- **The code-switch rate reduction is larger than the paper's framing suggests.** On Qwen3-8B, the code-switch rate drops from 46.34% to 25.90% — roughly a halving. While the paper correctly notes this remains above the Claude Sonnet 4 baseline (23.29%), the magnitude of the reduction for a method described as "preserving" code-switching ability deserves more nuanced discussion. Which specific instances are blocked? Are they marginal cases or clearly legitimate ones?

### Trivial

- Training hyperparameters for pseudo-target generation (k, p values used during self-distillation training) are not explicitly stated. The inference rules specify k=5, p=0.999 and k=20, p=0.95, but it is unclear whether these same values are used for generating training pseudo-targets.

## Nice-to-Haves

- **Diagnose pseudo-target quality.** A post-hoc analysis of how often the norm-adjusted top-k *correctly* includes the intended language family on confusion vs. non-confusion points would directly validate the training mechanism's assumption.
- **Evaluate on LCB despite its flaws.** Even with acknowledged imperfections, reporting LCB results would facilitate cross-paper comparison.
- **Provide more detail on ORPO setup** (dataset size, training steps, hyperparameter search) to ensure the comparison is not under-tuned.
- **A comparison on language pairs sharing the same script** (e.g., Spanish vs. French) would help characterize the method's limitations beyond what the discussion already covers.

## Removed Points

- **"Missed opportunity to use norm-adjusted logits as a direct baseline"** — This is speculative opinion about an alternative experimental design, not a weakness of the presented method.
- **"LCB selection bias"** — The paper provides a clear, reasonable rationale for not using LCB (natural code-switching, detector false positives). This is a valid methodological choice, not a weakness.
- **"Norm analysis only motivates training but is not used for intervention"** — The paper explicitly explains why norm adjustment alone is insufficient for direct intervention (Section 3.2: cannot explain English-Chinese confusion or low-resource confusion). The criticism ignores this explanation.
- **"Code-switch rate drop downplayed"** — The paper's framing is balanced: it states "LCG does reduce the rate of code-switching" and provides transparent numbers. The suggestion that it "downplays" is a stylistic judgment, not a substantive flaw.
- **"Circular training not mentioned in limitations"** — The paper's limitation section (Section 6) focuses on script-level granularity. While the pseudo-target quality question could be discussed, the absence is a missed opportunity, not an error.
- **Generic strengths from Strength Finder** — Some strengths were generic (e.g., "the paper addresses an important problem") and have been absorbed into the specific strengths above.

## Novel Insights

The harsh critic's concern about potential circularity in self-distillation training is a legitimate methodological question, but the calibration search reveals something more interesting: this concern applies to *any* self-distillation method for a task where the teacher model is imperfect — the paper's key insight is that norm adjustment moves the teacher's output distribution just enough that the pseudo-targets become useful despite the residual noise. The fact that the method works robustly across five different model families suggests that the norm-adjusted distribution is not merely a debiased version of the model's output but taps into a more fundamental property: correct-language tokens, even when not the top-1 prediction, reliably appear in the norm-adjusted top-k. This observation is implicit in the paper but not stated explicitly as a hypothesis that could be tested. Beyond the paper's own contributions, the most valuable insight from the synthesis is that the difference between LCG-adjusted and LCG-unadjusted (Table 3) serves as a lower bound on how much of language confusion is attributable to token embedding norm bias — a mechanistic attribution the paper could make more explicit.

## Suggestions

1. **Add pseudo-target quality diagnostics.** On a held-out set, report how often the norm-adjusted top-k correctly includes the intended language family. This would directly address the circularity concern and strengthen the mechanism's justification.

2. **Report confidence intervals or bootstrap estimates** for confusion rates in Table 3, especially for comparisons between LCG-adjusted and LCG-unadjusted where differences are small (e.g., Gemma3-12B Latin%).

3. **Add at least one low-resource language evaluation** (e.g., Hindi, Swahili) to demonstrate that the gate correctly handles Low-Res contexts where those languages are intended.

4. **State the specific k and p values used for pseudo-target generation during training** (Section 4.2), not just during inference (Section 4.3).

5. **Provide a more granular analysis of which code-switching instances are blocked** by the gate — are they marginal cases that the gate is uncertain about, or clearly legitimate ones? This would strengthen the claim that the gate preserves useful mixing.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
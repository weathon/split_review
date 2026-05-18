Now I have a thorough understanding of the paper and all the review inputs. Let me produce the final consolidated review.

---

## Summary

This paper proposes MiniLLM, a white-box knowledge distillation method for LLMs that replaces the standard forward KL divergence objective with reverse KL divergence, which encourages the student model to focus on the teacher's major modes rather than spreading probability mass over void regions. The authors derive a policy-gradient-based optimization procedure with three practical stabilizers — single-step decomposition, teacher-mixed sampling, and length normalization — and validate the approach across GPT-2, OPT, and LLaMA families (120M–13B) on multiple instruction-following benchmarks. The empirical results are strong and consistent: MiniLLM outperforms SFT, word-level KD, and SeqKD on almost all evaluated settings.

## Strengths

- **Consistent and substantial improvement across model families and sizes.** Table 1 shows MiniLLM achieving higher GPT-4 feedback scores and Rouge-L than all baselines across GPT-2 (120M–760M), OPT (1.3B–6.7B), and LLaMA (7B) on all five evaluation sets (DollyEval, SelfInst, VicunaEval, S-NI, UnNI). In several cases student models even exceed the teacher (e.g., OPT-6.7B on S-NI: 32.5 R-L vs teacher 30.4). This directly supports the core claim of higher overall quality.

- **Reduced exposure bias demonstrated quantitatively.** Figure 4 plots the excess error (ExAccErr) due to training-decoding mismatch as a function of generation length. MiniLLM's error is substantially lower than KD and SeqKD, and stops accumulating beyond 150 tokens, providing direct evidence for the exposure bias claim.

- **Scalability verified across student sizes and teacher scales.** Figure 1 shows MiniLLM consistently outperforming SeqKD across GPT-2, OPT, and LLaMA families at various student sizes. Figure 5 further shows that increasing teacher model size monotonically improves MiniLLM's performance, while SeqKD plateaus.

- **Ablation studies confirm each optimization strategy's contribution.** Table 4 shows that removing length normalization drops validation Rouge-L from 27.4 to 17.4, and removing teacher-mixed sampling drops it to 22.3, verifying the importance of each proposed component.

- **Human evaluation corroborates automated metrics.** Figure 3 shows MiniLLM achieving higher win rates than SFT, KD, and SeqKD in human pairwise comparisons on SelfInst with LLaMA-7B, performing comparably to the teacher LLaMA-13B.

## Weaknesses

### Major

- **The gradient derivation in Section 3.2 is not the exact gradient of reverse KL, and this is not acknowledged.** The paper claims Eq. 6 (∇L = -E[∑_t (R_t − 1)∇log q_θ(t)]) derives directly from the Policy Gradient Theorem, where R_t = ∑_{t'=t}^T log(p_{t'}/q_{θ,t'}). However, the exact reverse KL gradient involves R_1^T = ∑_{t'=1}^T log(p_{t'}/q_{θ,t'}) — the full-trajectory return — not the reward-to-go R_t. The difference (the terms where past-token rewards interact with the gradient at the current position) is non-zero in a shared-parameter autoregressive model. The single-step decomposition (Eq. 7–8) does not fix this: it only computes the per-token term (t′=t) exactly by vocabulary summation, while the "Long" term retains the same reward-to-go structure. The resulting gradient estimator is therefore biased relative to the true reverse KL gradient. 

  This matters because the paper's central narrative is that it *minimizes reverse KL* effectively for KD. If the optimization descends a biased gradient, the theoretical explanation is weaker than claimed — the empirical success could stem from the SFT initialization, the teacher-mixed sampling, or the language modeling loss rather than from coherent reverse KL minimization. The paper should either (a) prove the gradient is correct despite this structure, (b) explicitly acknowledge the approximation and characterize its bias, or (c) reframe the method as using a surrogate loss. As it stands, the optimization justification is incomplete.

  That said, this approximation is common in the RL-for-text-generation literature, and the strong empirical results suggest the bias is manageable in practice. This limits the *theoretical* contribution but does not invalidate the *empirical* contribution.

### Minor

- **The importance weight approximation (Eq. 9) introduces unquantified bias.** The paper replaces the full product-of-ratios importance weight w_t = ∏_{t'=1}^t q_θ(y_{t'})/p̃(y_{t'}) with w_t ≈ q_θ(y_t)/p̃(y_t), citing variance reduction. The paper does acknowledge this is an approximation and cites prior work, but provides no analysis of the resulting bias. For α=0.2, the sampling distribution p̃ is close to the teacher, so the true importance weight can vary substantially over long sequences; the per-step truncation discards multiplicative effects. An empirical comparison (e.g., tracking gradient fidelity or comparing to the full importance weighting on a small-scale proxy) would clarify whether the approximation is benign.

- **The diversity analysis is limited.** The paper acknowledges that reverse KL can hurt diversity and provides Dist-4 and language modeling loss (Table 5) to argue diversity is preserved. However, these are corpus-level aggregate metrics; they do not measure whether the model can produce multiple distinctly different correct responses for the *same prompt* (the usual diversity concern in generation). Self-BLEU, inter-response coverage, or the number of distinct valid responses per prompt would be more informative. The paper argues that "generating one correct response is sufficient" for many applications, which is a reasonable position, but the evidence for "neglectable loss of diversity" remains thin.

- **The calibration analysis uses classification benchmarks (SST-2, BoolQ), which are somewhat tangential to the paper's core focus on generative KD.** The results show MiniLLM achieves lower ECE than KD/SeqKD (Table 3), which is a real improvement, but calibration on single-label classification is not clearly linked to calibration in open-ended generation (e.g., whether the model's confidence in its own sampled answers is well-calibrated). The paper's hypothesis connecting mode-seeking to better calibration is plausible but not directly tested on generation tasks. This does not invalidate the analysis — it simply measures a related but different property.

- **Length normalization (Eq. 12) modifies the objective function without explicit discussion.** The paper replaces R_{t+1} with the averaged R^{Norm}_{t+1}, which changes the loss surface. The paper acknowledges lengtbias as motivation, but does not state whether the resulting gradient still corresponds (even approximately) to the original reverse KL or whether it is a different surrogate. This should be clarified.

- **Human evaluation is conducted on only one dataset (SelfInst).** This is noted in the paper and is not a fatal flaw — the automated metrics are extensive — but it limits the strength of the human-preference claim.

### Trivial

None that survive filtering.

## Nice-to-Haves

- An empirical check comparing the approximate gradient to a numerically estimated true gradient on a small-scale proxy (e.g., a short-sequence setting) would strengthen the theoretical claims substantially.
- Inter-response diversity metrics (self-BLEU, coverage) per prompt would strengthen the diversity analysis.
- Grading calibration on the same instruction-following tasks (e.g., using GPT-4 score bins) would make the calibration analysis more directly relevant to the paper's core setting.

## Removed Points

- **Missing comparison with concurrent f-divergence KD methods (GKD, f-div-KD).** The paper cites these as concurrent works (2024). Expecting experimental comparison with concurrent work that appeared around the same submission window is unreasonable for a conference submission. **Removed.**

- **"The standard policy gradient assumes the reward is a fixed function of the trajectory" applied as a criticism of the derivation.** While the reviewer correctly identifies the approximation in Eq. 6, their specific framing that the Policy Gradient Theorem "cannot apply" because the reward depends on θ is not the cleanest way to describe the issue. The actual issue is subtler (reward-to-go vs. full-trajectory return) and the reviewer's framing could mislead. I have reframed the criticism more precisely above.

- **Various formatting/style nitpicks and "missing appendix" claims.** These are parser artifacts, not author errors. **Removed per hard rules.**

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine theoretical subtlety about gradient correctness, but this is a known issue in the broader RL-for-text-generation literature rather than a novel observation.

## Suggestions

1. **Revise the gradient derivation section.** Explicitly acknowledge that Eq. 6 gives a *biased* estimator of the reverse KL gradient because it uses reward-to-go (R_t) rather than the full-trajectory log-ratio. Either prove the bias is small (e.g., via a toy numerical check) or reframe the method as optimizing a surrogate that approximates reverse KL.
2. **Add a brief analysis of the importance weight approximation bias.** A small-scale experiment comparing the approximate weight to the full product weight (or to no importance weighting) would suffice.
3. **Strengthen the diversity evaluation** with per-prompt inter-response metrics (e.g., self-BLEU or distinct-n across multiple samples per prompt).
4. **Clarify the status of length normalization** — state explicitly whether the final objective is still reverse KL or a modified surrogate.
5. **Consider replacing or supplementing the calibration analysis** with a generation-level calibration measure (e.g., confidence-accuracy on instruction-following outputs binned by GPT-4 score).

## Score and Decision

This paper makes a real empirical contribution: it demonstrates that reverse KL minimization with a policy-gradient-based optimization yields consistently better students than forward-KL-based KD across multiple model families and scales. The experiments are thorough, the ablations are informative, and the results are clear. 

The primary weakness is theoretical: the gradient derivation is not the exact reverse KL gradient as claimed, and this is not acknowledged. However, the empirical success does not hinge on perfect theoretical alignment — the method works regardless. With a candid revision clarifying the approximation and its practical impact, the paper would be substantially strengthened.

**Score:** 6.0  
**Decision:** Accept

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
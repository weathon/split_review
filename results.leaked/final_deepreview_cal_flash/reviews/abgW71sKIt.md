Now I have everything I need to produce the consolidated review. Let me organize my analysis.

## Anchors Summary

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| EfficientQAT (6Mdvq0bPyG) | 3.00 | R1 | Much weaker — typo-riddled, unclear method, rejected |
| PrefixQuant (vw0NurJ7UX) | 3.00 | R1 | Much weaker — limited novelty, rejected |
| CVXQ (0T8vCKa7yu) | 3.00 | R1 | Much weaker — convex opt framing but poor experiments, rejected |
| Super Weight (0Ag8FQ5Rr3) | 4.60 | R1 | Weaker — interesting observation but limited method, rejected |
| One QuantLLM (RdG7LVGnQi) | 4.50 | R1 | Weaker — OFA approach incomplete, rejected |
| SliM-LLM (tjlTczcnPz) | 5.40 | R2 | Weaker — mixed-precision method with inference issues, rejected |
| LeanQuant (ISqx8giekS) | 5.17 | R2 | Weaker — solid but lower quality, accepted |
| STBLLM (6XUSDvBFkV) | 6.00 | R2 | Comparable — 1-bit method with structural binarization, similar quality |
| OSTQuant (rAcgDBdKnP) | 6.20 | R2 | Comparable — PTQ with orthogonal transforms, similar quality |
| QA-LoRA (WvFoJccpo8) | 6.33 | R2 | Comparable — quantization-aware fine-tuning, somewhat different domain |
| OmniQuant (8Wuvhh0LYW) | 6.40 | R2 | Slightly stronger — cleaner evaluation, more comprehensive ablation |
| PB-LLM (BifeBRhikU) | 6.75 | R1 | Slightly stronger — partial binarization with solid experiments, accepted |
| ARB-LLM (ZU8OdDLTts) | 7.00 | R1 | Slightly stronger — direct predecessor, thorough with no catastrophic failures, accepted |
| CBQ (eW4yh6HKz4) | 7.60 | R1 | Stronger — cross-block reconstruction, more polished |
| Spectra LLM (TJo6aQb7mK) | 7.60 | R1 | Stronger — pretraining low-bit models at scale |
| Scaling Laws for Precision (wg1PCg3CUP) | 8.00 | R1 | Stronger — comprehensive precision-aware scaling laws |

**Round 1 bracket**: [5.0, 7.0] — the paper is clearly above the 3-range papers and clearly below 7.5+ papers.

**Round 2 narrowing**: Comparing to anchors in the 5.17–6.75 range, the paper sits near STBLLM (6.00) and below PB-LLM (6.75) and ARB-LLM (7.00). The PTB failure is a notable vulnerability that the best anchors in this band do not share, placing the paper below ARB-LLM and PB-LLM. At the same time, the paper's analytical contribution (Section 3) and the AMP mechanism are more novel than STBLLM's combination of existing techniques.

**Final score**: 6.0 — solid mid-range accept, positioned between STBLLM and PB-LLM/ARB-LLM.

---

## Summary

This paper investigates why naive output alignment (matching layer outputs) fails for 1-bit post-training quantization of LLMs, identifying three issues: (i) layer-level improvement does not guarantee block-level improvement, (ii) activation errors accumulate across layers, and (iii) output alignment can disrupt token interactions and attention patterns. The authors propose a selective strategy that restricts output alignment to the last fully connected layer of each transformer block, explicitly uses the full-precision input as the target (Output Error instead of Activation-conditioned Error), and introduces an Attention Matrix Preservation (AMP) mechanism to mitigate attention degradation. Experiments on OPT (1.3B–30B) and LLaMA-2/3 (7B–13B) show consistent perplexity reductions and zero-shot accuracy improvements over prior 1-bit PTQ methods, with the notable exception of a catastrophic failure on the LLaMA-2-7B + PTB setting.

## Strengths

1. **Rigorous preliminary diagnosis of output alignment failure.** Section 3 and Figures 1–2 provide clear empirical evidence that naive layer-wise output matching (ARB-X) can increase block-level loss, accumulates MSE with depth, and causes token-similarity matrices to drift from the full-precision baseline. This analysis is a genuine contribution independent of the method itself.

2. **Consistent improvements across most settings.** Tables 1 and 2 show that the proposed method achieves lower perplexity than ARB-RC, ARB-X, BiLLM, and PB-LLM on C4, WikiText2, and PTB across OPT 1.3B–30B, LLaMA-2-13B, and LLaMA-3-8B, as well as higher average zero-shot QA accuracy. Gains on smaller models (OPT-1.3B/2.7B) are substantial (up to 4.85 PPL reduction).

3. **Ablation evidence for each design component.** Table 4 confirms that using Output Error instead of Activation-conditioned Error improves perplexity by ~0.7 on C4 for LLaMA-2-7B. Table 3 shows that removing AMP causes a >10 PPL increase on LLaMA-2-7B, confirming its critical role.

4. **Novel AMP mechanism with clear empirical benefit.** AMP addresses the token-similarity degradation identified in the preliminary analysis. The >10 PPL degradation when AMP is removed (Table 3) demonstrates that it is not a trivial addition, and the RMSNorm sensitivity hypothesis provides a plausible architectural explanation for why LLaMA models benefit more.

## Weaknesses

### Fatal

None.

### Major

1. **Catastrophic perplexity on LLaMA-2-7B + PTB is dismissed rather than explained.** In Table 2, the proposed method achieves 3166 PPL on PTB for LLaMA-2-7B, while ARB-RC obtains 763 and ARB-X obtains 681. This is not a marginal gap—it is a 4× increase over the weight-alignment baseline. The paper states (line 237) that "the large perplexity indicates that the metric cannot provide a meaningful evaluation." This is not a valid argument: perplexity is a well-defined metric on which other 1-bit methods achieve much lower values, so the metric is clearly meaningful. The failure strongly suggests a genuine limitation of the proposed method (or a bug in the PTB evaluation pipeline for that specific configuration) that the paper makes no attempt to diagnose. While the method performs well on nearly every other configuration, this unresolved failure contradicts the claim of "consistently outperforming" prior work and undermines confidence in the method's robustness. The authors should at minimum investigate whether this is caused by selective quantization, AMP, or their interaction, and discuss whether it can be mitigated.

### Minor

2. **Selective layer choice is not validated by ablation.** The method restricts output alignment to "the last fully connected layer of each block" (Section 4.2), motivated by the claim that it "has the most direct impact on the block loss." No experiment compares this choice against alternatives (e.g., aligning all layers in the block, the attention output projection, or the MLP's up-projection). Figure 1 shows that some layers benefit from weight alignment while others benefit from output alignment, but it does not specifically rank layers or validate that the last layer is the optimal choice. This is a methodological gap—the core design decision is not empirically grounded.

3. **AMP's link to actual attention is indirect and the mechanism is heuristic.** The AMP objective maximizes the Frobenius inner product between token-similarity matrices defined from linear-layer outputs, which the paper acknowledges are a "proxy for the attention mask" (Section 3.3). The actual self-attention mechanism uses separate query and key projections, not the output of the subsequent linear layer. The binary-mask update rule (Eq. 11) based on gradient signs is heuristic and is not compared with simpler alternatives (e.g., adding AMP as a regularization term). While the ablation (Table 3) empirically validates AMP's importance, the theoretical grounding is weaker than it could be. The paper says Figure 3 (in Appendix) visualizes token-similarity matrices, but this visualization is not available in the main text.

4. **Gains over the best weight-matching baseline (ARB-RC) are modest for the largest models.** For OPT-30B on C4, the improvement over ARB-RC is 13.15 vs. 13.34 (Δ = 0.19 PPL); for OPT-13B on C4, Δ = 0.36 PPL; for LLaMA-2-13B on WikiText2, Δ = 0.97 PPL. These are consistent improvements but quantitatively small for the models where 1-bit quantization is most needed. The practical significance for large-model deployment is therefore somewhat limited.

### Trivial

None.

## Nice-to-Haves

1. **Ablation on layer selection policy.** The paper would benefit from comparing output alignment applied to: all layers, attention output only, MLP only, last-two layers, etc. This would confirm that the "last fully connected layer" choice is indeed optimal.
2. **Attention map visualization before/after AMP.** Visualizing actual attention matrices (QK^T) under full-precision, ARB-X, and the proposed method with/without AMP would directly validate that the proxy objective preserves attention behavior.
3. **Statistical significance / variance estimates.** Perplexity numbers for large models often vary across calibration runs; reporting variance would clarify whether the small gains for large models are reliable.

## Removed Points

These points from the inputs are flagged to be removed; treat them with caution:

- **"Eq. (2) contains a typo (both terms identical)"** — This is a PDF parser rendering artifact, not a paper error. Per rules, formatting artifacts from parsing are removed.
- **"Overhead analysis cannot be assessed because appendix is stripped"** — Per rules, criticisms about missing appendix content are removed; the appendix exists in the original submission.
- **"Statistical significance not reported"** — Single-run evaluation is standard for large-scale LLM perplexity benchmarks. Moved to Nice-to-Haves.
- **"Limited discussion of limitations"** — The paper explicitly notes the PTB exception ("with the exception of Llama-2-7B model evaluated on PTB dataset"). The substantive issue (the failure itself) is retained as Weakness #1.
- **"The derivation of closed-form solutions appears mathematically sound but..."** — This is not a weakness; it is a positive assessment.
- **"The AMP hypothesis about RMSNorm is not tested"** — The paper presents this as a hypothesis ("We hypothesize"), which is standard for tentative explanations. The ablation (Table 3) does test the AMP mechanism itself.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Investigate (or acknowledge and explain) the LLaMA-2-7B + PTB failure.** The simplest fix is to run the other configurations (LLaMA-2-7B on PTB) through a debug pipeline: does the failure persist if PTB is used as the calibration set? Is it caused by selective quantization, AMP, or their combination? If the failure is reproducible and irreducible, the paper should transparently discuss it as a limitation rather than dismissing the metric.
2. **Add an ablation study on the layer selection policy** to empirically justify restricting output alignment to the last fully connected layer of each block.
3. **Strengthen the AMP validation** by visualizing actual attention maps (or at least the token-similarity matrices mentioned in the paper) in the main text, and by comparing the binary-mask update rule against a simpler AMP regularization term.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
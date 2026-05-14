Now let me compose the final review.

---

## Summary

This paper proposes Quantized Zeroth-order Optimization (QZO), a method that enables fine-tuning of quantized LLMs using zeroth-order optimization by perturbing continuous quantization scales rather than discrete weights. QZO eliminates gradients and optimizer states (via ZO) while compressing model weights (via quantization), achieving up to 18× memory reduction versus full-parameter 16-bit fine-tuning. The method is compatible with both scalar-based (GPTQ) and codebook-based (AQLM) quantization and includes a directional derivative clipping (DDC) technique to stabilize training.

## Strengths

- **Novel and conceptually clean core idea**: Perturbing the continuous quantization scale rather than discrete weights to enable ZO fine-tuning of quantized models is a genuinely clever approach that neatly circumvents the precision-gap problem (Section 3.2.1, Definition 3.3). This is the paper's primary contribution and it is well-motivated.

- **Practical engineering achievement**: Successfully fine-tuning a 2-bit Llama-2-13B model on a single 24GB GPU (Table 3) is non-trivial and demonstrates the method's practical value for resource-constrained settings. The 4.8GB memory footprint for OPT-6.7B (Figure 1, Table 5) is genuinely low.

- **Solid empirical breadth**: The method is evaluated across three model families (OPT-6.7B, Llama-2-7B, Llama-3.1-8B), five NLP benchmarks spanning classification and generation, and two quantization paradigms (GPTQ 4-bit and AQLM 2-bit). QZO consistently and substantially improves over zero-shot quantized baselines (Tables 1, 3).

- **DDC empirically effective**: Directional derivative clipping demonstrably prevents training collapse (Figure 2), and the ablation (Figure 3) shows reasonable robustness to the clipping threshold over a wide range (C ≥ 75).

- **Honest about limitations**: The paper is transparent about QZO's dependence on quantization quality, the gap vs. first-order methods (Table 5), and weaker diffusion model results (Appendix F). This intellectual honesty is commendable.

## Weaknesses

### Major

- **Misleading FLOPs comparison (Table 2)**: The paper claims QZO uses "about 1% of the FLOPs of MeZO" (e.g., 8.19×10¹³ vs. 9.91×10¹⁷ for OPT-6.7B). However, both QZO and MeZO perform two full forward passes through the model at each step, which should dominate the compute cost. The QZO FLOPs number (8.19×10¹³ over 20k steps with batch size 16 = ~2.6×10⁸ FLOPs per sample-step) is far too small to include full forward passes through a 6.7B-parameter model. The numbers appear to count only the optimizer update FLOPs on the small set of quantization scales, excluding the forward pass cost entirely. This makes the claimed computation-efficiency advantage misleading. Since computation efficiency is presented as a key strength alongside memory efficiency, this significantly weakens the paper's contribution.

- **Theorem 1 (unbiasedness of clipped estimate) is incorrect**: The proof in Appendix A claims that the clipped gradient estimator is unbiased. The critical step (transition to Eq. 12) asserts that the expectation of ±Cz over the regions where |d| > C is zero, which does not hold in general because d depends on z and the conditional distribution is not symmetric. In the limit ε→0, d → gᵀz, and a direct calculation shows the bias is 2(1−Φ(C/‖g‖))g, which is non-zero for finite C. Since Theorem 1 is used to derive the variance reduction guarantee (Eq. 8), the theoretical justification for DDC's variance-reducing property is unsupported. This does not invalidate the empirical results—DDC clearly works—but it undermines the paper's theoretical contribution and the variance analysis in Section 3.2.2.

### Minor

- **DDC ablation limited to one model and one task**: The clipping threshold study (Figure 3) uses only Llama-2-7B on SST-2. While the result is informative, generalizing the claim that QZO is "robust to the magnitude of C" across model families and tasks would require broader evidence.

- **No quantitative metrics for Stable Diffusion experiments**: Appendix F shows qualitative images only. The paper acknowledges a "noticeable gap" to ground truth but provides no FID, CLIP score, or other quantitative measure to contextualize performance. This is acknowledged as a limitation, but a few numbers would strengthen the appendix.

- **Training-set sampling study (Table 4) lacks MeZO comparison**: The seed-robustness experiment only covers QZO, so we cannot assess whether QZO's variance relative to MeZO changes with different dataset splits.

### Trivial

- The memory profiling in Figure 1 compares QZO (4-bit) against 16-bit baselines but does not include a MeZO-on-quantized or other ZO-quantized baseline for reference. The Appendix (Table 5) partially addresses this.
- The paper states that "all quantization scales within a linear layer are perturbed to save computation" (line 307) but Algorithm 1 shows per-element perturbation; the precise variant used in experiments should be clarified.

## Nice-to-Haves

- An analysis of *what* QZO learns through scale perturbation (e.g., layer-wise statistics of scale changes) would illuminate whether QZO recovers pre-quantization dynamic range or captures task-specific knowledge.
- Combining QZO with adapters more systematically (the QZO+QLoRA variant in Appendix D is described as "naive") could yield a stronger method that genuinely competes with first-order PEFT methods in the memory-performance trade-off.
- Loss/accuracy curves for more than one model-task pair would give a fuller picture of convergence behavior.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Missing QLoRA as main baseline**: The harsh critic argued QLO should be a primary baseline. Removed because QLoRA is a first-order (backpropagation-based) method, while QZO's contribution is explicitly within the zeroth-order paradigm. The paper is transparent about this: "First-order methods consistently outperform zeroth-order methods" (Appendix D), and QLoRA comparison with discussion is included in Appendix Table 5. Comparing a ZO method against first-order methods as the *primary* evaluation is scope mismatch.

- **Overstated uniqueness / "push the limits" narrative unjustified**: The critic argued the paper ignores QLoRA. Weakened because (a) QLO is acknowledged and compared in Appendix D, (b) QZO's memory advantage (4.8GB without gradient checkpointing or paged optimizers) vs. QLoRA (5.6GB requiring those techniques) represents a genuinely different approach—QZO's memory efficiency is architectural (inherent to ZO), not achieved through engineering workarounds.

- **"The method's compute-efficiency advantage is based on a misleading FLOPs count"**: Kept the substantive FLOPs concern but removed the framing that it's the *only* basis for the compute claim. The paper also shows faster wall-clock training time (2h16m for QZO vs. 4h26m for MeZO on OPT-6.7B, Appendix E), which partially supports the compute-efficiency claim independent of FLOPs.

- **Stable Diffusion results are "weak"**: Removed as a standalone weakness. The paper itself acknowledges the gap and lists it as a limitation. Qualitative results in an appendix with explicit caveats do not constitute a weakness that should count against the paper.

- **Generic "formatting/style" criticisms and typos**: Removed per instructions—these are parser artifacts.

## Novel Insights

The key novelty—perturbing continuous quantization scales as a proxy for perturbing discrete quantized weights in ZO optimization—is the paper's own contribution. The reviews did not surface additional novel insights beyond what the paper itself contributes. The observation that DDC can be effective *despite* not being strictly unbiased is interesting: in practice, the bias-variance tradeoff appears to favor clipping even though Theorem 1's unbiasedness claim does not hold, suggesting that the variance reduction from clipping (which follows from d'² ≤ d² alone, Eq. 7) is sufficient to explain DDC's benefit without invoking unbiasedness.

## Suggestions

- **Fix the FLOPs reporting**: Either clearly state that the reported FLOPs measure optimizer-update cost only (not total training FLOPs), or recompute to include forward pass FLOPs for a fair comparison. The paper's wall-clock training time comparison (Appendix E: QZO takes 2h16m vs. MeZO's 4h26m) already demonstrates a real speed advantage from quantized inference kernels, which is more informative than FLOPs alone.

- **Fix or remove Theorem 1**: The unbiasedness claim is incorrect. The authors should either provide a corrected analysis (showing the estimator is biased but the bias is bounded, which together with the variance reduction from Eq. 7 might still yield a favorable bias-variance tradeoff), or remove the theorem and rely on the empirical evidence and the variance-reduction argument from Eq. 7 (which follows from d'² ≤ d² without needing unbiasedness). The variance analysis in Eq. 8 would need to be revised accordingly.

- **Expand DDC ablation**: Run the clipping threshold study on at least one more model and one more dataset to support the robustness claim.

- **Clarify perturbation granularity**: State explicitly whether per-element or per-layer perturbation was used in the main experiments and whether the choice affects the gradient estimator's properties.

## Score and Decision

**Calibration against anchors:**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| LUopdQeiz1 (ZeroQAT) | 2.50 | QZO has a cleaner, more focused idea than ZeroQAT, which suffered from limited novelty. QZO's core idea (perturbing scales) is more original. QZO deserves a higher score. |
| 2Dn4yHYLQJ (ZO Fine-tuner) | 3.60 | Similar ZO fine-tuning domain. QZO has stronger empirical breadth and a more novel idea. QZO's flaws (wrong theorem, misleading FLOPs) are comparable in severity to ZO Fine-tuner's missing validation issue. QZO is somewhat stronger. |
| EjH5I9ziug (HZO) | 2.50 | QZO is substantially stronger—cleaner idea, better empirical coverage, more transparent. |
| FF3o9flavI (SparQ) | 4.00 | Both combine ZO with quantization. QZO's core idea is more novel; SparQ had technical depth. Comparable quality. |
| NMlF3YjS8E (FZOO) | 5.00 | FZOO is a faster ZO optimizer with strong empirical validation. QZO has a more novel core idea (scale perturbation for quantized models) but has a wrong theorem and misleading FLOPs. QZO is slightly below FZOO. |
| QpbtT95S95 (Compute-Optimal QAT) | 6.00 | QAT paper with extensive experiments and solid scaling laws. QZO is less thorough experimentally and has theoretical errors. QZO is clearly below this level. |
| QMN4ERDdp4 (QWHA) | 6.50 | Strong quantization-aware PEFT paper. QZO is below this level on experimental rigor and theoretical correctness. |

QZO sits between the rejected ZO papers (2.5–4.0) and the accepted ones (5.0–6.5). The novel idea and solid empirical breadth pull it up, while the incorrect theorem and misleading FLOPs pull it down. I place it at 4.5, below the accept threshold—a borderline reject that could become acceptable with the theorem and FLOPs issues properly addressed.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
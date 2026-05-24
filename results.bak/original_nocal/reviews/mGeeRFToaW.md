Now I have a thorough understanding of the paper and all the claims. Let me produce the final review.

## Summary
The paper proposes Quantized Zeroth-Order Optimization (QZO), which fine-tunes quantized LLMs by applying SPSA-style gradient estimation to the **continuous quantization scales** rather than to discrete quantized weights. This avoids the dequantization/requantization loop required by prior ZO-on-quantized approaches. A Directional Derivative Clipping (DDC) method is introduced to stabilize training. QZO eliminates gradients and optimizer states while compressing weights, achieving extreme memory reduction (e.g., ~5 GB for 7B models, 18× less than AdamW full fine-tuning) and works with both scalar-based (GPTQ, 4-bit) and codebook-based (AQLM, 2-bit) PTQ methods.

## Strengths
- **Novel and principled approach to ZO on quantized weights.** By perturbing the continuous quantization scale Δ rather than discrete weights (Q-SPSA, Definition 3.3), QZO avoids the precision gap and dequantization/requantization overhead that plagues prior ZO-signSGD-based approaches. This is conceptually clean and is demonstrated to work with both GPTQ (4-bit scalar) and AQLM (2-bit codebook) without modifying the quantization scheme (Tables 1, 3).
- **Extreme and verified memory reduction.** QZO cuts total GPU memory by 18.3–18.4× compared to 16-bit AdamW full fine-tuning (e.g., 4.8 GB vs. 87.6 GB for OPT-6.7B on SST-2, Figure 1). This enables fine-tuning Llama-2-13B at 2-bit within a single 24GB GPU (Table 3) — a genuine engineering achievement.
- **Competitive accuracy relative to MeZO despite 3× less memory.** Across 15 model-task combinations in Table 1, QZO (4-bit) performs within 3 points of MeZO (16-bit) on 8/15, beats MeZO by ≥3 points on 3/15, and loses by ≥3 points on 4/15. On Llama-2-7B specifically, QZO actually outperforms MeZO on 4 of 5 tasks. This supports the claim that extreme memory savings do not come at a catastrophic performance cost relative to the leading ZO baseline.
- **DDC ablation convincingly demonstrates necessity.** Figure 2 shows that without DDC, training collapses to NaN within 22 steps, while with DDC it remains stable over the full 1,000-step window. The C-sensitivity analysis (Figure 3) further shows robustness for C ≥ 75 on SST-2. The empirical case for DDC is strong regardless of theoretical framing.
- **Computation efficiency.** QZO updates only ~1% of parameters (the quantization scales) and uses substantially fewer FLOPs than MeZO (Table 2), providing a non-obvious compute benefit alongside the memory savings.

## Weaknesses

### Fatal
None. No verified weakness invalidates the paper's core claims.

### Major
1. **Mathematical error in the variance derivation (Eq. 8).** The paper defines the variance of the clipped gradient estimate as `Var[∇̂'] = E[||∇̂'||²] - E[||∇̂'||]²`, but the correct definition for a random vector is `E[||∇̂'||²] - ||E[∇̂']||²` (the norm of the expectation, not the expectation of the norm). The subsequent manipulation in Eq. (8) then replaces `E[||∇̂||]²` with `(∇ℒ)²`, which conflates the expected norm with the norm of the expectation. This makes the derivation unsound as written. While the conclusion (clipping reduces variance) can potentially be justified correctly — and is empirically supported by Figure 2 — the paper's theoretical argument for DDC is compromised by this error. The authors should correct the derivation and verify whether the variance-reduction claim follows from their assumptions.

2. **No comparison with the most relevant memory-efficient fine-tuning baseline — QLoRA.** QLoRA (Dettmers et al., 2023) is the canonical method for fine-tuning 4-bit LLMs with backpropagation and low-rank adapters. It operates in the same problem setting (fine-tuning quantized LLMs under tight memory budgets) and achieves similar practical memory footprints (~16 GB for 7B models). Despite being cited in the references, QLoRA is never experimentally compared. Without this comparison, the claim of pushing "the limits of memory-efficient training" is not fully substantiated — QZO may be superior, equal, or inferior to QLoRA in the accuracy-memory tradeoff, but the paper provides no data. Adding this comparison, even at a matched memory budget, would significantly strengthen the submission.

### Minor
3. **Missing error bars / standard deviations.** No standard deviations or multiple-run statistics are reported in Table 1. Given the 1,000-example training sets and the stochastic nature of ZO optimization, the significance of inter-method differences (e.g., the 21.5-point CB gap on Llama-3.1-8B vs. the 4.8-point SQuAD advantage on Llama-2-7B) is unverifiable. At minimum, a few multi-seed results on one model-task pair would calibrate reader expectations.

4. **The "on par with MeZO" framing overstates the evidence in one specific case.** On Llama-3.1-8B CB, MeZO achieves 91.1 while QZO achieves 69.6 — a 21.5-point gap. The paper acknowledges this implicitly ("On most datasets, QZO performs on par with MeZO") but does not discuss or attempt to explain this outlier. A brief analysis (e.g., is this task particularly sensitive to scale fidelity? Does CB require more capacity in the tuned parameters?) would be informative.

5. **The fine-tuning upper bound uses SGD rather than AdamW**, acknowledged as due to budget constraints (footnote 2). SGD is not the standard optimizer for LLM fine-tuning, making this a weaker upper bound. The gap between QZO and "fine-tuning" may be inflated relative to what AdamW fine-tuning would achieve.

6. **No experimental comparison with prior ZO-on-quantized methods** (Feng et al., Zhou et al., Bar & Giryes). The paper claims QZO is "inherently more efficient and flexible" than these approaches but provides no empirical evidence. A targeted comparison on at least one model-task pair would support this claim.

### Trivial
- The memory profiling uses batch size 1 (Figure 1 caption), while actual training uses batch size 16. The practical peak memory during training is not reported.
- No wall-clock time is reported alongside the FLOPs in Table 2. FLOPs comparisons are useful but per-step time can differ in practice.
- Figure 3's C-sensitivity is only shown for SST-2 with Llama-2-7B; generalizability to other tasks is unknown.
- The claim that QZO (4-bit) "performs on par with MeZO" in the abstract and conclusion would benefit from a more nuanced qualifier given the large CB outlier.

## Nice-to-Haves
- An analysis of the effective rank or cosine similarity of QZO's gradient estimates vs. true gradients (computable via backprop on a small proxy), to explain why tuning only ~1% of parameters (scales) works.
- Ablation of whether tuning scales alone vs. jointly tuning scales + un-quantized components (as done in 2-bit) drives most of the gains.
- Training loss curves over the full 20k steps (Figure 2 only shows 1k steps).

## Removed Points
These points were flagged in the input reviews but are removed from the main assessment with justification:

- **"Theorem 1 is almost certainly false because clipping changes expectation"** — The proof is in the appendix (not visible due to parsing). The claim of unbiasedness for a clipped directional derivative is unusual but we cannot verify the proof's correctness or lack thereof from the main paper alone. Without seeing the appendix, this judgment is speculative. Demoted from "fatal/structural" to not included as a verified weakness.
- **"18× memory comparison is apples-to-oranges / misleading"** — The paper transparently reports both AdamW (87.6GB) and SGD (26.8GB) baselines alongside QZO (4.8GB) in Figure 1. The 18× factor is correctly computed against AdamW full fine-tuning, which is the standard high-memory baseline. The reader can compute the 5× factor against SGD from the same table. No deception.
- **"QZO fine-tunes only scales (~1%) while MeZO fine-tunes all weights — unfair comparison"** — This describes the methods' designs, not a flaw in the evaluation. QZO's parameter-efficiency is a feature, not a bug. The comparison with MeZO is meaningful because both use ZO; the difference in tunable parameters is inherent to QZO's approach.
- **"Fine-tuning baselines use SGD with no justification"** — The paper explicitly states the budget limitation (footnote 2). While suboptimal, this is transparently documented. Demoted to minor weakness #5.
- **"QZO on 2-bit Llama-2-13B shows modest gains on RTE"** — True, but Table 3 shows substantial gains on other tasks (SST-2: +22.9, CB: +9.0, SQuAD: +4.0). An isolated modest gain does not constitute a weakness.
- **"Sensitivity experiment only varies C on SST-2 with Llama-2-7B"** — A valid scope limitation but not a weakness; it's a standard ablation. Retained as trivial.
- **Strength Finder's generic strengths** — Removed generic praise ("addressed an important problem") that lacked concrete evidence anchors.

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface an unrecognized connection or framing that the paper itself misses. The observation that QZO (4-bit) outperforms MeZO (16-bit) on Llama-2-7B (4 of 5 tasks) despite operating at lower precision is mildly surprising and could be explored further, but this is largely implicit in the paper's own Table 1.

## Suggestions
1. Correct the variance definition in Eq. (8) and re-derive the variance-reduction claim. If the corrected derivation does not support the claim, rephrase the theoretical contribution as a heuristic justification supported by strong empirical evidence (Figure 2), which is sufficient.
2. Add a QLoRA comparison on the same benchmarks under matched memory budgets (e.g., LoRA rank such that total memory matches QZO's ~5 GB). This is the single most impactful addition.
3. Report standard deviations from 3 random seeds for at least one model (e.g., Llama-2-7B on all tasks) to calibrate result significance.
4. Discuss the large CB gap on Llama-3.1-8B (91.1 vs. 69.6) — is it a statistical fluke, or does this task fundamentally require more tunable capacity than scales alone provide?
5. Include a brief comparison with one prior ZO-on-quantized method (e.g., Bar & Giryes, 2025) on a single task to support the claim of superior efficiency/flexibility.

## Score and Decision
MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
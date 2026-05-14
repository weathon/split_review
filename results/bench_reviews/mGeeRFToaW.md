Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper proposes Quantized Zeroth-order Optimization (QZO), which enables fine-tuning of quantized LLMs by perturbing continuous quantization scales rather than discrete quantized weights during zeroth-order gradient estimation. QZO circumvents the precision mismatch problem that prevents standard ZO from working on quantized weights, and introduces Directional Derivative Clipping (DDC) to stabilize training. The method is compatible with both scalar-based (GPTQ, 4-bit) and codebook-based (AQLM, 2-bit) quantization, achieving ~3× memory reduction versus MeZO while maintaining competitive performance on several NLP benchmarks.

## Strengths

- **Novel and elegant formulation (Q-SPSA):** The core idea of perturbing only the continuous quantization scale **Δ** while keeping discrete quantized weights **_θ̄_** fixed (Definition 3.3, Eq. 5) is simple, principled, and cleanly sidesteps the integer-gradient mismatch problem. This is a genuinely new design point for ZO on quantized models.

- **Substantial and well-documented memory savings:** QZO reduces memory from ~15GB (MeZO, 16-bit) to ~5GB (QZO, 4-bit) for 7B-scale models (Table 1, Figure 1), and enables fine-tuning Llama-2-13B on a single 24GB GPU at 2-bit (Table 3). The extension to Stable Diffusion 3.5 Large (86GB→12.4GB, Appendix F) further demonstrates the practical impact.

- **DDC is empirically well-motivated:** Figure 2 convincingly shows that without DDC, training collapses (NaN loss) within 1,000 steps, while with DDC, training proceeds stably. The ablation on clipping threshold (Figure 3) shows a wide stable range (C ≥ 75), demonstrating robustness to this hyperparameter.

- **Multi-architecture and multi-quantization validation:** Experiments span OPT-6.7B, Llama-2-7B, Llama-3.1-8B, and Llama-2-13B, using both scalar-based GPTQ (4-bit) and codebook-based AQLM (2-bit), showing general applicability.

## Weaknesses

### Fatal
None.

### Major

- **Missing comparison with existing ZO-quantized methods:** The paper acknowledges ZOsignSGD (Liu et al., 2019), QuZO (Zhou et al., 2025), and ZOQO (Bar & Giryes, 2025) in the Related Work (Section 2), but provides NO experimental comparison. The paper claims QZO is "inherently more efficient and flexible" — a claim that cannot be evaluated without head-to-head experiments under comparable settings (same models, tasks, memory budgets). This is the most significant gap, as these are directly competing methods for the same problem.

- **Theorem 1 (unbiasedness) proof is not rigorous:** The proof in Appendix A attempts to show that the clipped SPSA estimate is unbiased by arguing that the clipped terms vanish as ϵ→0 (Eq. 10→Eq. 11). This step is insufficiently justified: the clipping threshold C is fixed, and the argument that the probability of |d|>C goes to 0 as ϵ→0 requires assumptions about boundedness and convergence that are not stated or verified. The claim of unbiasedness for the clipped estimator at finite ϵ is therefore unsupported. However, note that this issue is partially mitigated because: (i) Eq. 7 (second-moment reduction) is trivially true regardless of unbiasedness, and (ii) the main empirical justification for DDC (Figure 2) does not depend on the theorem.

- **Single-run results in main table without statistical confidence:** Table 1 reports accuracy/F1 as single numbers without error bars or confidence intervals. Appendix C shows that on OPT-6.7B, variance across three seeds can be ~2-3 points (e.g., CB ranges 67.9-71.4). Given that some claimed advantages of QZO over MeZO are of similar magnitude (e.g., +4.8 on SQuAD with Llama-2-7B), the reader cannot determine whether these are robust effects or chance variation. The community norm in this area is to report multiple seeds; the paper should follow this convention in the main results.

### Minor

- **Limited adaptation capacity of scale-only updates:** QZO updates only ~1% of the model's parameters (the quantization scales). Appendix D shows that combining QZO with QLoRA substantially improves results (SST-2: 87.6→93.3), confirming that the scale-only bottleneck is real. The paper is transparent about this but does not discuss whether the improvement gap could be closed by tuning more parameters through QZO's own mechanism (e.g., jointly updating un-quantized components).

- **Gap between theoretical framing and empirical evaluation:** The paper frames Theorem 1 and the variance reduction derivation (Eq. 8) as providing "theoretical evidence" for DDC, but the derivation is correct only conditional on Theorem 1 (which is unproven). A cleaner approach would be to present DDC as an empirically-motivated stabilization technique (which the Figure 2 evidence already supports) and either fix the proof or drop the unbiasedness claim.

### Trivial
- The formatting of Eq. 8 in the paper body (line 371) appears garbled due to a parsing artifact — the intended algebra is standard and correct given Theorem 1.
- The caption says "sclaes" (line 355, Theorem 1) — a typo for "scales."

## Nice-to-Haves
- A comparison with first-order fine-tuning of scales (backprop through the de-quantization operation) would help isolate whether QZO's limitations stem from ZO estimation error or from the inherent capacity limit of scale-only updates.
- Convergence plots for all baselines, not just the loss-accuracy curves for one model in Figure 4.

## Removed Points
- **Criticism about algebraic error in Eq. 8 (misplaced minus sign):** The equation as intended is algebraically correct. The apparent "misplaced minus sign" is a parser-induced formatting artifact; the derivation follows standard variance decomposition.
- **Criticism that hyperparameters (C=100, lr=1e-7) were chosen without systematic search:** This is a generic criticism applicable to most papers. The ablation in Figure 3 validates that the chosen C=100 is within the stable range. The paper provides hyperparameter values and a sensitivity study.
- **Criticism that the paper "does not acknowledge that other ZO-with-quantization methods work":** The paper explicitly acknowledges ZOsignSGD, QuZO, and ZOQO in the Related Work (Section 2, lines 188-196) and describes their paradigm.
- **Strength Finder claim about "theoretically grounded" DDC:** This strength is weakened (see Weaknesses — Theorem 1 proof is not rigorous).

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Add experimental comparison with ZOsignSGD, QuZO, and ZOQO** on at least a subset of models and tasks under matched memory budgets. This is essential to substantiate the claimed advantages.
2. **Report multi-seed results with confidence intervals in the main table** (Table 1), or at minimum for the key comparisons where QZO is claimed to match or exceed MeZO.
3. **Either correct the proof of Theorem 1** (with proper ϵ→0 asymptotic argument under stated regularity conditions) or reframe DDC as an empirically-motivated heuristic that provably reduces second-moment (Eq. 7) without the unbiasedness claim.
4. **Ablate the number of trainable parameters** — e.g., compare (a) scales only, (b) scales + a subset of un-quantized weights, (c) all weights via de-quantize/re-quantize — to directly characterize the trade-off between parameter count and performance.

## Score and Decision

**Calibration Anchors (retrieved from human-review corpus):**

| Path | Avg Score | Comparison to this paper |
|------|-----------|------------------------|
| `LUopdQeiz1.md` (ZeroQAT, ZO+QAT) | 2.50 | Similar topic but that paper had marginal novelty (extending ZO from weight-only to weight-activation QAT); this paper has a cleaner, more original idea. |
| `2Dn4yHYLQJ.md` (Learning ZO optimizer) | 3.60 | Rejected for fatal flaw (no test/validation measurements); this paper does not have such a flaw. |
| `jMzXLsHdnF.md` (FOCUS, ZO+BCD) | 5.20 | Comparable tier — both have a clear motivation but incomplete evaluation. FOCUS had missing ablations; this paper has missing baselines. |
| `9OUg0nJE72.md` (CoA-LoRA) | 5.50 | Accepted poster — comparable scope of contribution, but CoA-LoRA had more thorough comparison with baselines. |
| `e6nZrzSccj.md` (Robust Training at Arbitrary Precision) | 5.00 | Accepted poster — stronger theoretical grounding but similar evaluation depth. |
| `QpbtT95S95.md` (Compute-Optimal QAT) | 6.00 | Higher rigor (scaling laws from hundreds of experiments); this paper is weaker on experimental methodology. |

Relative to these anchors, this paper has a genuinely novel idea and impressive memory results that place it above the rejected papers (2.50–3.60 range). However, the missing comparison with prior ZO-quantized methods and the lack of statistical confidence in main results are significant gaps that prevent it from reaching the 5.5–6.0 tier. The paper is closest in profile to FOCUS (5.20) but with a cleaner core idea and weaker evaluation.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
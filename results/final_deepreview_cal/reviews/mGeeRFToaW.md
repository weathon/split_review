Now I have sufficient calibration data. Let me write the final review.

Round-1 bracket: Based on comparing with SubZero (4.25), MeZO-A³dam (4.75), Sparse MeZO (5.50), HiZOO (5.67), LOZO (7.0), and SensZOQ (5.80), the paper sits between 4.5 and 5.5.

Round-2 narrowing: Compared to SensZOQ (5.80, Accept) which combines ZO + quantization via static sparsity, QZO has a more novel core idea but weaker theory and experimental practices. Sparse MeZO (5.50, Reject) has better experimental practices but is more incremental.

Final score: 5.0. The novel idea of perturbing quantization scales is genuinely clever and the memory numbers are impressive, but the theoretical analysis contains verifiable errors and the experiments lack basic statistical rigor.

---

## Summary

This paper proposes Quantized Zeroth-order Optimization (QZO), which enables fine-tuning of quantized neural networks by perturbing the *continuous quantization scale parameters* (rather than the discrete quantized weights) using the SPSA zeroth-order gradient estimator. A directional derivative clipping (DDC) method is introduced to stabilize training. The paper demonstrates QZO on 4-bit GPTQ-quantized OPT-6.7B, Llama-2-7B, and Llama-3.1-8B, and 2-bit AQLM-quantized Llama-2-13B, reporting up to 18× memory reduction versus full-precision AdamW fine-tuning while achieving competitive performance against MeZO (which operates on 16-bit models with 3× more memory).

## Strengths

- **Genuinely novel core idea**: Perturbing the continuous quantization scale (Δ) instead of the discrete weights (θ̄) to bridge the gap between ZO gradient estimation and quantized weights is clever and non-obvious. This contrasts with prior ZO-quantized methods (ZO-signSGD, Bar & Giryes 2025) that quantize perturbation noises and apply sign-based updates to discrete weights.
- **Impressive and well-documented memory reduction**: Figure 1 and Table 1 show QZO achieves 4.8 GB vs. 87.6 GB (18.3×) for OPT-6.7B, 5.0 GB vs. 92.2 GB (18.4×) for Llama-2-7B, and 6.2 GB vs. 113.7 GB (18.3×) for Llama-3.1-8B relative to AdamW fine-tuning. This enables fine-tuning Llama-2-13B (2-bit) within a single 24 GB GPU.
- **Orthogonal to multiple quantization paradigms**: QZO works with both scalar-based GPTQ (4-bit, Table 1) and codebook-based AQLM (2-bit, Table 3), demonstrating generality.
- **Two orders of magnitude fewer trainable parameters**: Table 2 shows QZO uses ~5×10⁷ parameters vs. ~6.65×10⁹ for MeZO (~0.75%) on OPT-6.7B, with corresponding FLOP reductions.
- **DDC is empirically effective**: Figure 2 shows that without DDC, training collapses to NaN by step 22; with DDC it remains stable. Figure 3 demonstrates a wide safe range (C≥75) where accuracy is stable around 90%.

## Weaknesses

### Major

1. **Theoretical analysis of DDC is unsound in multiple respects.** (a) Theorem 1 claims the clipped gradient estimate is unbiased, but clipping the scalar directional derivative *d* before multiplying by the correlated random vector *z* generally introduces bias — the nonlinear clipping operation changes the estimate when |d|>C, and this change is correlated with *z*. This is not a subtle condition; it breaks for any finite C in standard settings. (b) The variance derivation in Eq. 8 uses an incorrect definition of vector variance ($\mathbb{E}[\|X\|^2] - \mathbb{E}[\|X\|]^2$) instead of the standard $\mathbb{E}[\|X\|^2] - \|\mathbb{E}[X]\|^2$, and improperly replaces $\mathbb{E}[\|\hat{\nabla}_{\Delta} \mathcal{L}\|]^2$ with $\|\nabla_{\Delta} \mathcal{L}\|^2$ (which would require $\mathbb{E}[\|\hat{\nabla}_{\Delta} \mathcal{L}\|] = \|\mathbb{E}[\hat{\nabla}_{\Delta} \mathcal{L}]\|$, false by Jensen's inequality). The conclusion that $Var[\text{clipped}] \leq Var[\text{unclipped}]$ is therefore not properly supported by the derivation presented. The paper's central theoretical claim is not credible as written. (Note: the empirical evidence in Figures 2 and 3 independently supports DDC's practical value; the flaw is in the claimed *theoretical* justification.)

2. **Experimental evaluation lacks statistical rigor.** All results in Tables 1 and 3 are single runs without error bars, standard deviations, or multiple seeds. Given the small dataset sizes (1000 training examples) and the inherently high variance of zeroth-order optimization, the reported differences — e.g., QZO 90.0 vs. MeZO 83.5 on Llama-2-7B SST-2 (QZO wins by 6.5), but QZO 69.6 vs. MeZO 91.1 on Llama-3.1-8B CB (MeZO wins by 21.5) — could easily be within noise. The claim that QZO "performs on par with MeZO" is not supported by the evidence as presented.

### Minor

3. **No experimental comparison with prior ZO-quantized methods.** The Related Work section cites ZO-signSGD (Liu et al., 2019), Feng et al. (2024), Zhou et al. (2025), and Bar & Giryes (2025) as "inherently less efficient and flexible" (Section 2), but none are included as baselines. Without direct comparison, the claimed practical advantages remain unvalidated.

4. **Mixed results not discussed.** QZO underperforms substantially on several tasks (e.g., CB with Llama-3.1-8B: 69.6 vs. MeZO's 91.1; BoolQ with Llama-3.1-8B: 78.2 vs. 83.4; SST-2 with OPT-6.7B: 87.6 vs. 93.0). The paper does not comment on this variability, which weakens the "consistently effective" narrative.

5. **Memory profiling methodology for AdamW baseline is unclear.** The 92.2 GB figure for Llama-2-7B AdamW (batch size 1, FSDP) seems high relative to a back-of-envelope calculation (14 GB weights + 14 GB gradients + 56 GB Adam states = 84 GB, with FSDP sharding reducing per-GPU usage), and no profiling tool or GPU count is specified. The relative advantage of QZO is clear regardless, but the absolute numbers warrant clarification.

### Trivial

6. The "18× memory reduction" claim compares QZO (4-bit) against AdamW (16-bit) — the fairer comparison with MeZO (16-bit) shows a 3× reduction. This distinction is clear in the text but the headline number could be misleading without context.

## Nice-to-Haves

- Report hyperparameter sensitivity for the perturbation scale ε and learning rate, in addition to the clipping threshold C.
- Investigate why QZO underperforms on CB and BoolQ — is this task-specific, architecture-specific, or a statistical artifact?

## Removed Points

None of the removed points are relevant here — all weaknesses I've kept are verified against the paper's text.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Drop or substantially revise the theoretical claims about DDC.** Either prove unbiasedness correctly (which seems unlikely for finite C), or characterize the bias and argue it is negligible in practice, or — most honestly — present DDC purely as an empirically effective heuristic clipping trick supported by Figures 2 and 3 (which are compelling on their own).
2. **Add 3–5 seeds with mean ± std to all experimental tables.** Without this, the central claim of "on par with MeZO" is unverifiable.
3. **Include at least one prior ZO-quantized method as a baseline** (e.g., Bar & Giryes 2025) on a representative subset of tasks.
4. **Clarify the AdamW memory profiling methodology** (number of GPUs, FSDP configuration, profiling tool).

## Calibration Report

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| SubZero (FK6T0U4Mg1) | 4.25 | 1 | Similar ZO+LLM fine-tuning approach, rejected. QZO has more novel core idea. |
| MeZO-A³dam (OBIuFjZzmp) | 4.75 | 2 | Adaptive ZO, rejected. Comparable theory issues; QZO slightly more novel. |
| Sparse MeZO (4Kw4KAoVnx) | 5.50 | 2 | Sparse ZO, rejected. Better experimental practices; QZO more novel idea. |
| HiZOO (bEqI61iBue) | 5.67 | 1 | Hessian-informed ZO, accepted. Stronger theory and broader evals than QZO. |
| SensZOQ (myYzr50xBh) | 5.80 | 2 | ZO+quantization via static sparsity, accepted. Comparable domain; QZO has more novel core idea but weaker experimental rigor. |
| LOZO (9BiVepgmWW) | 7.00 | 1 | Low-rank ZO, accepted. Stronger theory and experiments than QZO. |

Round-1 bracket: [4.5, 5.5]. Round-2 narrowed to ~5.0 based on comparison with Sparse MeZO (5.50, weaker idea but stronger experiments) and SensZOQ (5.80, similar domain but stronger rigor). QZO is between MeZO-A³dam (4.75) and Sparse MeZO (5.50).

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
Now I have all the information needed. Let me produce the final consolidated review.

## Summary
The paper proposes QZO (Quantized Zeroth-order Optimization), a method that fine-tunes quantized LLMs by applying zeroth-order optimization to the continuous quantization scale parameters rather than the discrete quantized weights. The key idea is to perturb the scale Δ (rather than weights θ̄) for gradient estimation via Q-SPSA, and a Directional Derivative Clipping (DDC) mechanism stabilizes training. Experiments on OPT-6.7B, Llama-2-7B, Llama-3.1-8B (4-bit GPTQ), and Llama-2-13B (2-bit AQLM) show ~18× memory reduction vs. full-precision fine-tuning, with performance competitive with MeZO on 16-bit models.

## Strengths

- **Novel and well-motivated core idea.** Applying ZO to quantization scales (Δ) rather than discrete weights (θ̄) is a clever insight that cleanly sidesteps the precision gap between discrete quantized weights and continuous gradient estimates. The Q-SPSA formulation (Definition 3.3) is a clean, principled extension of SPSA. This is a genuinely different approach from prior ZO+quantization works that quantize perturbation noises or re-quantize weights at each step.

- **Dramatic and well-documented memory savings.** Figure 1 / Table 1 show QZO (4-bit) uses 4.8–6.2 GB GPU memory vs. 14.8–20.4 GB for MeZO (16-bit) and 26–113.7 GB for fine-tuning (18.3× reduction). Table 2 further breaks this down: QZO trains only ~5×10⁷ parameters (~0.75% of total) and uses 0.07–0.08× the FLOPs of MeZO. The memory profiling is careful (per-device batch size=1, peak over first 100 steps).

- **Empirically validated DDC mechanism.** Figure 2 provides clear evidence that without DDC, training collapses to NaN by step 22, while DDC keeps it stable. Theorem 1 (unbiasedness of the clipped estimate) is correctly stated. The ablation in Figure 3 shows robustness to the clipping threshold C over a wide range (75–150), which is a practical strength for deployment.

- **Orthogonality to multiple quantization schemes.** The method is demonstrated on both scalar-based (GPTQ, 4-bit, Table 1) and codebook-based (AQLM, 2-bit, Table 3) PTQ methods. Results on Llama-2-13B under 2-bit quantization are particularly compelling: QZO improves from 57.6% → 80.5% on SST-2 vs. the zero-shot quantized baseline.

## Weaknesses

### Fatal
None.

### Major

- **Flawed variance-reduction proof for DDC.** The derivation in Eq. 8 attempts to prove Var[g'] ≤ Var[g] but contains an invalid step. Specifically, the paper replaces 𝔼[‖g‖]² with (∇L)², implicitly equating the squared expected norm of the unclipped gradient with the squared norm of its expectation. These are not equal in general (by Jensen, 𝔼[‖g‖] ≥ ‖𝔼[g]‖, with strict inequality when there is variance). Furthermore, the clipping operation (|d'| ≤ |d|) gives 𝔼[‖g'‖] ≤ 𝔼[‖g‖], which pushes the inequality in the opposite direction. The conclusion "Var[g'] ≤ Var[g] holds almost surely" does not follow from the chain shown. The "almost surely" tag is also unexplained.

  **Why this matters:** The paper claims theoretical support for DDC's variance reduction, but the proof is unsound. However, the *empirical* evidence (Figure 2: collapse without DDC, stability with DDC) remains strong and is not invalidated by the flawed proof. The authors should either fix the proof or downgrade the theoretical claim to an empirical observation. This is a significant but addressable flaw — it does not undermine the core contribution of QZO.

### Minor

- **Missing comparison with prior ZO+quantization methods.** The related work section identifies Zoqo (Bar & Giryes, 2025), ZO-signSGD, and other methods that combine ZO with quantization, claiming QZO is "inherently more efficient and flexible." Yet no experimental comparison with any of these methods is provided. Including even one directly competing ZO+quantization baseline (e.g., Zoqo) would substantially strengthen the evaluation by grounding the claimed advantages.

- **No statistical variability reported.** All results in Tables 1 and 3 are single numbers with no standard deviations or confidence intervals. Given that training uses only 1,000 sampled examples (following MeZO's convention), results can be noisy. While this follows the MeZO paper's reporting standard, the community norm is shifting toward multi-seed reporting. Adding at least mean ± std over 3 seeds would increase confidence in the findings.

- **Title slightly over-promises.** The title "Fine-Tuning Quantized Neural Networks" could be read as implying the quantized discrete weights themselves are updated. The paper is transparent about perturbing scales (Δ) rather than weights (θ̄), but a more precise title — e.g., "Fine-Tuning Quantization Scales of LLMs with Zeroth-Order Optimization" — would better align reader expectations with the actual mechanism. This does not affect the paper's technical merit.

### Trivial
None.

## Nice-to-Haves
- **Comparison with a PEFT+quantization baseline (QLoRA).** Since QZO trains only ~0.75% of parameters, a comparison with QLoRA (which also trains a small number of adapter parameters on a quantized backbone) would help contextualize the ZO-vs-backprop tradeoff for the community. This is not required given the paper's scope (ZO-based methods) but would be informative.
- **Ablation of quantization group size.** The paper uses group size 128 throughout; varying this parameter would reveal sensitivity of QZO to the number of trainable scales.
- **"MeZO-on-scales" baseline.** Applying MeZO to the same scale parameters in an unquantized model would isolate the effect of weight quantization from the effect of updating only a subset of parameters.

## Removed Points
The following points from the input reviews were filtered out:
1. **"Overclaiming scope is a structural issue that undermines the paper's main claim" (Harsh Critic #1)** — Weakened to Minor. The paper is transparent about the mechanism (Section 3.2.1: "only applies perturbation to the continuous quantization scale"). Many accepted papers in memory-efficient fine-tuning (e.g., QLoRA, LQ-LoRA) also freeze quantized weights and update only a small set of parameters; this does not make them "not fine-tuning quantized models." The point is valid as a framing precision note but not as a structural flaw.
2. **"The paper does not isolate the effects of quantization from training a tiny fraction of parameters"** — Part of the critic's overclaiming argument. The paper's memory savings come from both quantization AND training fewer parameters, but this is transparently presented in Table 2. The comparison with MeZO (which trains all parameters in 16-bit) is a valid systems-level comparison even if multiple factors differ.
3. **"Memory profiling does not compare to QLoRA"** — The paper is about ZO methods; the profiling compares QZO with MeZO and fine-tuning, which is appropriate for the paper's scope.

## Novel Insights
The harsh critic's identification that the DDC variance proof (Eq. 8) has a flawed step (equating 𝔼[‖g‖]² with ‖𝔼[g]‖²) is a genuinely useful observation for the authors. This specific mathematical misstep — the implicit Jensen gap — would not be obvious to most readers and is worth fixing. Beyond this, no genuinely novel insight emerges from the reviews beyond the paper's own contributions.

## Suggestions
1. **Fix or downgrade the DDC theory.** Remove the flawed variance inequality (Eq. 8 and the "almost surely" claim) unless it can be made rigorous. Theorem 1 (unbiasedness) and the empirical evidence in Figure 2 are sufficient to justify DDC.
2. **Add at least one directly competing ZO+quantization baseline.** Zoqo (Bar & Giryes, 2025) would be the most natural choice given its recency and relevance.
3. **Report results with 3 random seeds and standard deviations** for the main tables, especially given the 1,000-example training set.
4. **Refine the title** to be more precise about what is being fine-tuned (quantization scales, not quantized weights).
5. **Consider a "MeZO-on-scales" ablation** to separate the effect of quantization from the effect of updating fewer parameters, which would make the contribution even cleaner.

## Score and Decision

### Round 1 — Bracketing
Three queries for weak (avg < 3.5), middle (3.5–7.5), and strong (avg > 7.5) anchors on ZO/quantization fine-tuning topics:

| Anchor | Avg Score | Round | Relevance |
|--------|-----------|-------|-----------|
| EfficientQAT | 3.00 | R1, weak | Quantization-aware training for LLMs |
| LLM Compression with Convex Optimization | 3.00 | R1, weak | Weight quantization |
| PrefixQuant | 3.00 | R1, weak | LLM quantization |
| ALLoRA | 3.33 | R1, weak | LoRA adapters |
| SensZOQ (ZO+sparsity+quantization) | 5.80 | R1, middle | **Directly relevant:** ZO+quantization for LLMs |
| ZO-Offloading | 3.75 | R1, middle | ZO fine-tuning with offloading |
| LQ-LoRA | 6.75 | R1, middle | Quantization + PEFT |
| LeZO | 4.00 | R1, middle | Sparse ZO for LLMs |
| CBQ | 7.60 | R1, strong | LLM quantization (no ZO) |
| Scaling Laws for Precision | 8.00 | R1, strong | Precision scaling laws |
| CCQD | 8.00 | R1, strong | Quality-diversity (unrelated) |
| Restructuring VQ | 8.00 | R1, strong | VQ-VAE (unrelated) |

**Round-1 bracket:** The paper sits clearly above ZO-Offloading (3.75) and LeZO (4.00), and is comparable to or slightly above SensZOQ (5.80). It is below LQ-LoRA (6.75). Narrowest plausible range: **5.5–6.5**.

### Round 2 — Narrowing
Queries inside (4.5, 6.5) and (5.5, 7.5) on more precise topical aspects:

| Anchor | Avg Score | Round | Relevance |
|--------|-----------|-------|-----------|
| QR-Adaptor (quantized LLM fine-tuning) | 5.40 | R2 | Quantized fine-tuning |
| SensZOQ (ZO+sparsity+quantization) | 5.80 | R2 | **Directly relevant** |
| HiZOO (Hessian-informed ZO) | 5.67 | R2 | ZO optimizer for LLMs |
| LoQA (Low rank Quantization Adaptation) | 5.00 | R2 | Quantization PEFT |
| LOZO (Low-rank ZO) | 7.00 | R2 | ZO fine-tuning |
| EfficientDM (quantization-aware fine-tuning) | 6.50 | R2 | Quantization fine-tuning |

**Final anchor comparison:**
- **vs. SensZOQ (5.80, Accept):** QZO has a more novel core idea (ZO on scales vs. sparse masks+quantization), evaluates on more architectures (Llama-3.1-8B, Llama-2-13B), and has cleaner memory profiling. SensZOQ was criticized for unfair memory comparisons and limited novelty. QZO is slightly stronger.
- **vs. LOZO (7.00, Accept):** LOZO has stronger theory (convergence guarantees) and more thorough experimentation across model sizes. QZO's idea is more novel but its evaluation is less comprehensive and its theory partially flawed. QZO is weaker than LOZO.
- **vs. LQ-LoRA (6.75, Accept):** LQ-LoRA has more thorough experiments (RoBERTa, LLaMA-2 up to 70B) and a broader scope. QZO's core idea is more novel but the paper is narrower. QZO is weaker than LQ-LoRA.

The paper is best positioned between SensZOQ (5.80) and LQ-LoRA (6.75), closer to the lower end of that range due to the flawed DDC proof and missing baselines. Score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
Now I have enough data to calibrate. Let me finalize the review.

**Round 1 bracket:** 5.5–7.0, based on comparison with LOZO (7.0), SensZOQ (5.8), SubZero (4.25), and LeZO (4.0).

**Round 2 narrowing:** QZO is clearly better than Sparse MeZO (5.5, reject) and Efficient FT Quantized LLMs (5.4, reject). Comparable to SensZOQ (5.8, accept). Different tradeoffs vs. LOZO (7.0, accept): QZO has more dramatic memory savings and cleaner quantization integration, but LOZO has correct theory. Final placement: **6.0** — strong practical contribution with addressable theoretical and evaluation flaws.

**All anchors retrieved:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| EfficientQAT | 3.0 | 1 | Weaker — pure quantization, no ZO innovation |
| PrefixQuant | 3.0 | 1 | Weaker — inference quantization, not fine-tuning |
| LLM Compression CVXQ | 3.0 | 1 | Weaker — quantization only, no training method |
| Cut Cross-Entropy | 8.5 | 1 | Stronger — addresses memory from a different angle, accepted widely |
| SensZOQ | 5.8 | 1 | Comparable — also ZO+quantization but less elegant, accepted |
| LOZO | 7.0 | 1 | Similar quality — better theory but less memory savings |
| SubZero | 4.25 | 1 | Weaker — less novel, SGD-only issue |
| LeZO | 4.0 | 1 | Weaker — less novel, marginal improvement |
| Scaling Laws for Precision | 8.0 | 1 | Stronger — foundational scaling law work |
| Sparse MeZO | 5.5 | 2 | Weaker — modest improvement, no quantization integration |
| Efficient FT Quantized LLMs | 5.4 | 2 | Weaker — less novel, GA-based approach |

## Summary

This paper proposes Quantized Zeroth-Order Optimization (QZO), which combines post-training model quantization with zeroth-order optimization for memory-efficient LLM fine-tuning. The core idea is to perturb continuous quantization scale parameters (rather than discrete weights) for gradient estimation via Q-SPSA, and to clip directional derivatives (DDC) for training stability. QZO achieves ~18× memory reduction versus 16-bit fine-tuning and ~3× versus 16-bit MeZO, enabling fine-tuning of 7B–13B parameter models on a single 24GB GPU.

## Strengths

- **Elegant core idea (Q-SPSA, Definition 3.3, Eq. 5):** Perturbing the continuous quantization scale Δ rather than discrete weights θ̄ cleanly resolves the fundamental incompatibility between ZO and quantization, avoiding de-quantization/re-quantization overhead at each step. This is conceptually simple, computationally efficient, and orthogonal to the choice of quantization method.

- **Substantial, well-documented memory savings (Table 1, Figure 1):** Peak VRAM drops from 87.6→4.8GB (OPT-6.7B), 92.2→5.0GB (Llama-2-7B), 113.7→6.2GB (Llama-3.1-8B) — all ~18× reductions. The profiling protocol is consistent (SST-2, batch size 1, 100 steps).

- **Competitive performance vs 16-bit MeZO on many benchmarks despite 3× less memory (Table 1):** On Llama-2-7B: 90.0 vs 83.5 (SST-2), 85.5 vs 80.7 (SQuAD), 69.6 vs 67.9 (CB). On Llama-3.1-8B: 93.0 vs 92.5 (SST-2), 88.3 vs 86.9 (SQuAD). The 4-bit QZO matching or beating 16-bit MeZO is a strong result.

- **Compatibility with both scalar-based (GPTQ, 4-bit) and codebook-based (AQLM, 2-bit) quantization (Tables 1 and 3):** Demonstrates the plug-and-play claim across fundamentally different quantization paradigms, including extreme 2-bit quantization for Llama-2-13B on a single 24GB GPU.

- **Strong DDC ablation (Figures 2-3):** Figure 2 shows training collapses to NaN at step 22 without DDC. Figure 3 sweeps C from 0–150, establishing a robust operating range (C ≥ 75). This provides practitioners concrete guidance and validates DDC's necessity.

- **Computation efficiency beyond memory savings (Table 2):** QZO uses ~0.7% of MeZO's trainable parameters, making it substantially faster per training step — a practical advantage that goes beyond the headline memory claim.

## Weaknesses

### Fatal
None.

### Major
- **Theorem 1 (unbiasedness of clipped gradient) appears mathematically incorrect (line 112).** Theorem 1 claims the clipped gradient estimate d'·z is an unbiased estimate of ∇_Δ L. However, for a linear loss L(Δ) = g^T Δ with SPSA gradient estimate d = z^T g, clipping gives d' = clip(z^T g, -C, C). The i-th component of the gradient estimate is d'·z_i. For g = e_i: E[clip(z_i, -C, C)·z_i] = E[z_i²·1(|z_i|≤C)] + E[C|z_i|·1(|z_i|>C)] < E[z_i²] = 1, because clipping truncates contributions from large |z_i| values. The estimate is biased downward, contradicting Theorem 1. This matters because Eq. 8 (line 120-122) explicitly relies on Theorem 1 to conclude Var[clipped] ≤ Var[original] — the final step requires (E[||clipped||])² ≥ (∇_Δ L)², which follows from unbiasedness via Jensen's inequality. The practical contribution (DDC stabilizes training) is well-validated by Figures 2-3, but the stated theoretical justification is unsound.

- **SGD-only fine-tuning upper bound weakens evaluation (Table 1, line 178).** Fine-tuning uses SGD ("Due to limited budget on computational resources"), while AdamW is the standard for LLM fine-tuning. SGD substantially underperforms AdamW. Since the paper already runs AdamW memory profiling (Figure 1), reporting AdamW accuracy would significantly strengthen the evaluation. On Llama-2-7B SST-2, QZO (90.0) nearly matches SGD fine-tuning (92.8), but this near-parity likely reflects SGD's weakness rather than QZO's strength.

- **Inconsistent performance vs MeZO undermines the "on par" claim (Table 1).** The paper claims "on par with MeZO" (line 249, abstract), but: OPT-6.7B SST-2: 87.6 vs 93.0 (−5.4); Llama-3.1-8B CB: 69.6 vs 91.1 (−21.5); Llama-3.1-8B BoolQ: 78.2 vs 83.4 (−5.2). The 21.5-point gap on Llama-3.1-8B CB is enormous and unexplained. No error bars are provided. The "on par" characterization is not uniformly supported — QZO is competitive on many benchmarks but has significant gaps on others.

### Minor
- **"About 1% of the FLOPs of MeZO" is misleading (line 251, Table 2).** For trainable parameters (~0.7%), this is approximately correct. But FLOPs ratios span three orders of magnitude: OPT-6.7B ~0.008%, Llama-2-7B ~2.0%, Llama-3.1-8B ~7.0%.

- **Different training recipes complicate comparison (line 221).** QZO uses batch size 16, 20k steps (320k samples seen from 1k training examples); fine-tuning uses batch size 8 with different learning rate schedule. While different methods may need different hyperparameters, this asymmetry makes it harder to attribute differences to the method vs. the recipe.

## Nice-to-Haves
- Comparison with QLoRA/LoRA for practical relevance, even if stated as orthogonal.
- Empirical comparison with prior ZO+quantization methods (Feng et al., 2024; Zhou et al., 2025).
- DDC sensitivity analysis beyond SST-2 with Llama-2-7B.
- Error bars or multiple seeds for stochastic ZO estimation results.
- Analysis of the large QZO vs MeZO gap on Llama-3.1-8B CB (−21.5 points).

## Removed Points
These points are flagged to be removed per filtering rules:
- Any criticism doubting the existence of cited models, benchmarks, or references.
- Formatting/typo nitpicks (parser artifacts, not author errors).
- Missing related works (cannot verify from paper alone).
- Strength from Strength Finder about Theorem 1's correctness — verified as incorrect against the paper's own equations.
- Generic strengths about problem importance without specific evidence.

## Novel Insights
The key novel observation is that Q-SPSA's perturbation of continuous scale parameters is not merely a convenience but a structural insight that eliminates the de-quantization/re-quantization bottleneck of prior ZO+quantization approaches, yielding both memory and compute savings simultaneously. The empirical finding that QZO sometimes exceeds 16-bit MeZO despite 4-bit quantization (e.g., Llama-2-7B SST-2: 90.0 vs 83.5) hints that quantization may act as implicit regularization for ZO gradient estimation, though the paper does not explore this.

## Suggestions
1. **Fix or retract Theorem 1.** A corrected result proving DDC reduces variance without requiring unbiasedness (e.g., directly bounding Var[d'·z] relative to Var[d·z]) would be valuable. Alternatively, present DDC as empirically motivated with the strong ablation as primary justification.
2. **Report AdamW fine-tuning accuracy on at least 1-2 tasks/models** to provide a true upper bound.
3. **Analyze the large gaps** (especially Llama-3.1-8B CB: −21.5 points) — is this related to quantization error, task characteristics, or model-specific factors?
4. **Correct the FLOPs comparison** to reflect the actual range (~0.008% to ~7%) rather than "about 1%."

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
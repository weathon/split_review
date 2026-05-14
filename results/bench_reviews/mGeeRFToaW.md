Now I have all the information needed. Let me write the final consolidated review.

---

## Summary
This paper proposes Quantized Zeroth-order Optimization (QZO), a method for memory-efficient fine-tuning of quantized LLMs. The core idea is to perturb the continuous quantization scale parameters (Δ) rather than the discrete quantized weights when performing zeroth-order gradient estimation via SPSA, thereby enabling ZO optimization on top of post-training quantized models without de-quantization/re-quantization. Combined with directional derivative clipping (DDC) to stabilize training, QZO achieves up to 18× total memory reduction versus full fine-tuning and enables fine-tuning a 2-bit Llama-2-13B on a single 24GB GPU.

## Strengths
- **Genuinely novel and elegant core idea**: Perturbing quantization scales instead of discrete weights for ZO gradient estimation cleanly resolves the incompatibility between ZO perturbation and quantized weights. The Q-SPSA formulation (Definition 3.3) is mathematically clean and generalizes to both scalar-based (GPTQ) and codebook-based (AQLM) quantization.
- **Impressive practical memory reduction**: Figure 1 and Tables 1–3 demonstrate concrete memory savings — 4.8 GB for a 4-bit OPT-6.7B versus 14.8 GB for MeZO (16-bit) and 26.8 GB for full fine-tuning. Fine-tuning a 2-bit Llama-2-13B within 24 GB is a compelling engineering achievement.
- **Consistent performance improvements over zero-shot quantized models**: Across three model families (OPT-6.7B, Llama-2-7B, Llama-3.1-8B) and five NLP benchmarks, QZO consistently and meaningfully outperforms the Zero-Shot-Q baseline, demonstrating that scale-space optimization yields real task-specific gains.
- **DDC effectively prevents training collapse**: Figure 2 shows that without clipping, training produces NaN losses; Figure 3 shows stable performance for a wide range of clipping thresholds (C ≥ 75), providing practical guidance.
- **Broad method compatibility**: The paper demonstrates QZO with two qualitatively different quantization paradigms — scalar-based GPTQ (4-bit) and codebook-based AQLM (2-bit) — and includes promising results on Stable Diffusion 3.5 Large (Appendix F, 12.4 GB).

## Weaknesses

### Fatal
None.

### Major
- **Missing first-order scale optimization baseline**: The paper compares QZO against MeZO (ZO on 16-bit full weights) and fine-tuning (first-order on 16-bit full weights), but never against first-order optimization of the *same* scale parameters Δ using backpropagation through the de-quantization operation. This baseline would isolate how much performance is lost to ZO approximation error versus the inherent capacity limit of scale-only optimization. Without it, the reader cannot determine whether QZO's gap to full fine-tuning is primarily due to the restricted parameter space or to ZO estimation noise. The paper acknowledges that ZO "would be much less accurate than that of backpropagation" (line 593), making this missing baseline the critical gap in the experimental logic.
- **Theorem 1's unbiasedness proof has a gap**: The proof in Appendix A transitions from Eq. 11 to Eq. 12 by asserting that terms involving the clipping constant ±C vanish in expectation, which requires E[**z** | |d| > C] = 0 — a condition that is neither established nor argued. The variance-reduction conclusion in Eq. 8 depends on this unbiasedness claim. The practical effectiveness of DDC (Figures 2–3) does not depend on Theorem 1, but the paper presents it as theoretical support; the proof as written does not hold.

### Minor
- **Limited mechanistic analysis of what QZO learns**: The paper provides no analysis of *how* the quantization scales change during QZO fine-tuning (e.g., per-layer scale change distributions, which transformer components shift most). Such analysis would strengthen the claim that QZO performs genuine task adaptation rather than coarse calibration, and would address the natural question of whether the gains arise from targeted, task-specific adjustments.
- **Comparison with MeZO could be better contextualized**: The paper states QZO "performs on par with MeZO" (line 588) but on several tasks QZO materially underperforms (e.g., OPT-6.7B on SST-2: 87.6 vs 93.0; RTE: 61.7 vs 64.6). The narrative should more precisely characterize when and by how much QZO falls short, particularly since the methods operate in different precision and parameter regimes.
- **2-bit significance untested for 13B**: Confidence intervals with multiple seeds are reported for OPT-6.7B (Appendix C, Table 4) but not for the more impactful Llama-2-13B 2-bit results (Table 3), where some gains are modest (RTE: 52.3→54.5, CB: 62.5→64.3).
- **Non-negative scale projection not discussed**: Algorithm 1 enforces Δ_i ≥ 0 via max(·, 0), which is sensible for quantization scales but is not discussed in the theoretical analysis (Theorem 1 assumes unconstrained updates). Whether this projection affects convergence or introduces bias is unaddressed.
- **Prior ZO+quantization methods not compared empirically**: The related work section (lines 188–196) claims QZO is "inherently more efficient and flexible" than methods like ZO-signSGD and its successors, but no head-to-head comparison is provided.

### Trivial
- The abstract's 18× memory reduction figure conflates savings from MeZO's existing ZO approach (gradients and optimizer states) with QZO's novel weight quantization contribution. This is clarified in the body of the paper but could mislead a casual reader.
- The PEFT comparison in Appendix D uses a split-schedule approach (QLoRA first half, QZO second half) that is acknowledged as naive; a principled joint optimization would be more informative.

## Nice-to-Haves
- Random-label control experiment to confirm QZO is learning task-specific mappings rather than dataset statistics.
- Analysis of how scale changes distribute across layers and whether they correspond to task-relevant modules.
- Joint ZO optimization of scales and LoRA adapters formulated in a principled way rather than as a split schedule.

## Removed Points
These points from the harsh reviewer were considered but removed:

- **"QZO only performs calibration, not fine-tuning"** — Removed. The paper shows consistent task-specific gains over zero-shot baselines across five diverse NLP tasks including generation (SQuAD). Scale perturbation at the quantization-group level can reweight feature dimensions, which is a coarse but genuine form of model adaptation. The concern that this might be "mere calibration" is partially addressed by the breadth of tasks and the fact that gains vary by task rather than being uniform. This is downgraded to a minor weakness requesting mechanistic analysis.
- **"The comparison with MeZO is fundamentally ill-posed"** — Removed as stated; the comparison serves as a useful reference point showing that quantized scale-only ZO can approach the performance of full-precision full-weight ZO. This is an informative comparison, not an unfair one. The paper should present the comparison more carefully (kept as a minor weakness above) but the comparison itself is valid.
- **Demand for comparison with prior ZO+quantization methods (Liu et al., Feng et al., Zhou et al., Bar & Giryes)** — Moved to minor weakness as a missing empirical comparison; not a fatal omission since these are adjacent but distinct approaches.
- **"SGD rather than AdamW for baselines weakens the upper bound"** — Removed. The paper explicitly states this is due to computational budget constraints (line 473). This is a known limitation honestly disclosed, not a methodological error.
- **Concern that the 18× savings attribution is misleading** — Moved to trivial; the paper body clearly distinguishes the contributions of ZO (from MeZO) and quantization (from QZO).

## Novel Insights
None beyond the paper's own contributions. The core insight — that perturbing continuous quantization scales provides a valid gradient signal for ZO optimization of quantized models without de-quantization/re-quantization — is the paper's own contribution and is genuinely novel.

## Suggestions
- Add a first-order baseline that optimizes the same scale parameters Δ via backpropagation through the de-quantization step. This is the single most important experiment to add.
- Fix the Theorem 1 proof or, if unbiasedness cannot be established, replace the theoretical claim with an empirical bias-variance characterization of DDC.
- Add per-layer scale-change analysis (e.g., histograms of Δ pre/post fine-tuning) to provide mechanistic insight.
- Report multi-seed confidence intervals for the 13B 2-bit experiments.
- Temper claims of parity with MeZO; explicitly note where and by how much QZO underperforms.

## Calibration Anchor Comparison

| Anchor Paper | Path | Avg Score | Comparison to QZO |
|---|---|---|---|
| FZOO: Fast ZO Optimizer | NMlF3YjS8E | 5.00 | Similar tier — novel ZO method with strong empirical results but some missing ablations. QZO has a more conceptually novel core idea (scale perturbation for quantized models) but has the Theorem 1 gap. Comparable overall. |
| Compute-Optimal QAT | QpbtT95S95 | 6.00 | Stronger than QZO — hundreds of experiments, scaling laws, rigorous methodology. QZO has less experimental depth but a cleverer core idea. |
| ZeroQAT | LUopdQeiz1 | 2.50 | QZO is clearly stronger — ZeroQAT had novelty concerns and unfair comparisons; QZO's core idea is genuinely original and the experiments are fairer. |
| Learning a ZO Optimizer | 2Dn4yHYLQJ | 3.60 | QZO is stronger — that paper had bias issues in its formulation and incomplete baselines; QZO addresses a cleaner problem with better empirical validation. |
| Bridging ZO-FO Gap (DASP) | bR32fsXLbf | 3.00 | QZO is stronger — DASP had misleading framing and missing ablations. |
| AdaMeZO | wTO2ZYl9gQ | 3.50 | QZO is stronger — AdaMeZO was a more incremental contribution. |
| Scaling Law for QAT | dcPH77OVgN | 5.00 | Similar tier — solid experimental work with some limitations. QZO is comparably strong. |
| Achieving low-bit Muon | g2l9bg9DWx | 6.00 | Stronger than QZO — more thorough analysis in its domain. |
| QeRL | zw8zxMJJlm | 6.00 | Stronger than QZO — more extensive experiments and analysis. |

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
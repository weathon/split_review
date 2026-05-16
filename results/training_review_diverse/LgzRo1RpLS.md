Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

MambaExtend introduces a parameter-efficient calibration framework that extends the context length of pre-trained Mamba models by scaling the discretization step Δ_t with per-layer (or per-channel) scaling factors while keeping all model weights frozen. Using either gradient-based (CF_BP) or zeroth-order (CF_ZO, SPSA-based) optimization on just 10–20 calibration samples, it achieves up to 32× context extension (2k→64k) with dramatic reductions in parameter updates (up to ~5.42×10⁶× fewer) and peak memory (up to 3.87× lower) compared to fine-tuning alternatives.

## Strengths

1. **Clean, practical idea with strong efficiency gains.** The core insight — that scaling Δ_t per layer is sufficient to recover long-context performance — leads to a genuinely lightweight procedure. Fig. 6 quantifies orders-of-magnitude reductions in parameter updates, calibration time, and peak memory relative to full fine-tuning and DeciMamba, and the advantage holds across both model scales (130M, 1.4B) and context lengths.

2. **Solid empirical results across diverse tasks.** On PG-19, MambaExtend reduces perplexity from 995,328 to 30.62 at 70k context (Fig. 4) and outperforms DeciMamba by up to ~40.6% lower PPL. On the Pile, it achieves up to ~8145× perplexity improvement (Table 1). On passkey retrieval, it matches or exceeds both fine-tuned Mamba and DeciMamba while calibrating 3500×–7100× fewer parameters (Fig. 5).

3. **Effective zeroth-order variant validated.** CF_ZO (SPSA-based, forward-pass only) matches the perplexity of CF_BP (backpropagation) on the Pile (Table 4), demonstrating that the method can work without any gradient computation — crucial for deployment on memory-constrained devices.

4. **Ablation on scaling granularity provides actionable guidance.** Table 3 shows that per-channel scaling factors are necessary for retrieval tasks, while per-tensor sharing fails — a useful design lesson for practitioners applying the method.

## Weaknesses

### Major

- **Missing DeciMamba comparison on LongBench.** Table 2 compares MambaExtend only against the original pre-trained Mamba on LongBench tasks. DeciMamba is the only existing Mamba-specific long-context extension method and is compared against on other benchmarks (perplexity, passkey retrieval), but is entirely absent from the LongBench evaluation. This makes it impossible to judge whether MambaExtend offers competitive multi-task long-context understanding relative to the fine-tuning baseline, and weakens the claim of "similar or better long-context performance evaluated across multiple tasks."

### Minor

- **No fine-tuned Mamba baseline for perplexity experiments.** On PG-19 and Pile perplexity (Fig. 4, Table 1), MambaExtend is compared to the original pre-trained Mamba and DeciMamba but not to a simple fine-tuned version of the base Mamba model. While the paper does include a fine-tuned Mamba baseline for passkey retrieval, the absence on perplexity leaves open the question of whether standard fine-tuning (for more than one epoch) could match or exceed MambaExtend's perplexity — even though the efficiency advantage would remain.

- **Causal interpretation is stronger than evidence supports.** The paper states that OOD discretization steps are "primarily" responsible for Mamba's long-context failure (abstract). The evidence is correlational (Fig. 2: ΣΔ_t grows with context length) and interventional (Fig. 3: scaling Δ_t helps). This is a plausible mechanism, but alternative explanations (distribution shift in hidden states, changes in gating dynamics) are not ruled out. The paper's contribution does not depend on a fully proven causal mechanism, but the framing should be more cautious.

- **No error bars or variance reporting.** Calibration uses only 10–20 samples, which could produce significant variance across different calibration subsets. No standard deviations or confidence intervals are reported for any experiment, making it hard to assess the stability of the results.

- **LongBench task selection criteria not stated.** The paper says "seven popular tasks" but does not list which seven or explain the selection rationale. This raises minor cherry-picking concerns.

### Trivial

- **Key optimization hyperparameters not reported.** The paper does not specify the optimizer, learning rate, number of SPSA iterations, perturbation size (ε), or convergence criteria for the scaling factor optimization. While the method is broadly reproducible with reasonable defaults, these details should be provided.

## Nice-to-Haves

- **Explain per-token scaling trade-off more clearly.** Table 3 shows that both per-channel and per-token scaling are effective, but the paper does not discuss why per-token (which has more parameters and likely higher capacity) is not the default choice. A brief explanation of the memory/performance trade-off would help.
  
- **Measure the impact of more epochs for fine-tuned baselines.** The passkey retrieval comparison intentionally uses one epoch for all methods to demonstrate "extreme low cost tuning." Showing that MambaExtend remains competitive even when the baselines are given more epochs would strengthen the robustness of the efficiency claims.
  
- **Clarify that "training-free" refers to weight-free, not optimization-free.** CF_BP uses backpropagation (storing activations), so it is not training-free in the strictest sense. The paper already explains the method clearly, but a more precise term like "weight-free" or "parameter-efficient" in the abstract would prevent misinterpretation.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Criticism about garbled softplus symbol and truncated method description.** These are parser extraction artifacts, not errors in the original submission.
- **Criticism about Mamba2 not being clearly reported.** The paper explicitly states experiments on "Mamba and Mamba2 variants" (line 18), and Mamba2-130M is included.
- **Criticism about the ~8145× PPL improvement being misleading.** The factor is technically correct; it is standard to report multiplicative improvements even when the baseline is very high. The paper does not misrepresent the number.
- **Several formatting/style nitpicks and reproducibility complaints about trivial implementation details** that do not affect the core contribution.

## Novel Insights

Beyond the paper's own contributions, the reviews surface a useful observation: the paper presents an interesting structural parallel between Mamba's discretization-step issue and the positional embedding OOD problem in transformers. Just as positional interpolation rescales RoPE indices to mitigate OOD positions, MambaExtend rescales Δ_t to mitigate OOD discretization steps. This analogy, while not deeply explored in the paper, provides a conceptual bridge that could unify context-extension strategies across architecture families.

## Suggestions

1. **Add DeciMamba results to LongBench (Table 2).** This is the single most impactful fix — it directly addresses the most serious gap in the evaluation.
2. **Add a fine-tuned Mamba baseline to perplexity experiments (PG-19, Pile).** Even a simple multi-epoch fine-tuning baseline would clarify whether MambaExtend's gains come from the Δ_t scaling strategy or merely from any adaptation to long-context data.
3. **Report standard deviations** over multiple calibration runs (e.g., different random subsets of the 10–20 calibration samples) for key metrics.
4. **List the specific LongBench tasks selected** and briefly justify the selection.
5. **Provide optimization details** (learning rate, optimizer, SPSA perturbation size, number of iterations) in the appendix or supplement.

## Score and Decision

The paper presents a clean, well-motivated method with strong efficiency advantages and solid empirical support on most tasks. The main evaluation gap (missing DeciMamba on LongBench) is notable but does not invalidate the core contribution, which is the efficient calibration framework itself. The remaining weaknesses — missing baselines on perplexity, overclaimed causality, and missing error bars — are addressable and do not fundamentally undermine the paper's value.

This is a paper with real contributions that should be accepted, ideally with the evaluation gaps addressed in a revision.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
## Summary

QZO (Quantized Zeroth-order Optimization) proposes fine-tuning quantized LLMs by perturbing continuous quantization scales instead of discrete quantized weights, thereby enabling zeroth-order gradient estimation on low-bit models. This eliminates gradients, optimizer states, and reduces weight memory, achieving an 18× memory reduction relative to 16-bit AdamW fine-tuning. A complementary technique, Directional Derivative Clipping (DDC), is introduced to stabilize training by reducing variance in gradient estimates, with a theoretical claim that the clipped estimator remains unbiased.

---

## Strengths

- **Elegant core insight**: Perturbing the continuous quantization scale $\Delta$ rather than the discrete weights $\bar{\theta}$ is a clean solution to the precision-mismatch problem. It elegantly bridges the gap between ZO optimization (which operates in continuous space) and PTQ weights (which are discrete), requiring no de-quantization/re-quantization at each step.

- **Strong memory efficiency**: Achieving 18× memory reduction vs. 16-bit AdamW and 3× vs. MeZO is empirically verified (Table 1) and enables Llama-2-13B fine-tuning on a single 24GB RTX 4090—a genuinely new use case that existing methods cannot support.

- **Broad compatibility**: QZO is demonstrated to work with both scalar-based (GPTQ, 4-bit) and codebook-based (AQLM, 2-bit) quantization methods, showing generality across the PTQ landscape.

- **Computation efficiency**: Table 2 shows QZO requires only ~1% of trainable parameters and ~1% of FLOPs compared to MeZO for OPT-6.7B, an often-overlooked advantage for deployment in throughput-limited settings.

- **Consistent empirical results**: Improvements over Zero-Shot-Q are consistent across three model families (OPT, Llama-2, Llama-3), five datasets, and two quantization regimes; the extreme-quantization result (2-bit Llama-2-13B, Table 3) is particularly compelling.

- **Extension beyond LLMs**: The application to Stable Diffusion 3.5 Large, running in 12.4GB on a single GPU, demonstrates broader applicability and opens a new direction for generative model adaptation.

---

## Weaknesses

### Fatal
None.

### Major

1. **Missing QLoRA comparison.** QLoRA (Dettmers et al., 2023) is cited in the reference list but never compared against experimentally. QLoRA is the canonical method for fine-tuning quantized LLMs and occupies the same design space: low-bit weights plus gradient-based adaptation. Without this comparison, the reader cannot assess where QZO sits on the memory–performance Pareto frontier. It is likely that QLoRA substantially outperforms QZO on accuracy while still using more memory—and this tradeoff is precisely what would define the practical value of QZO. Omitting this baseline leaves the empirical case incomplete.

2. **Theorem 1 appears incorrect.** The paper claims the clipped gradient estimate $\hat{\nabla}_\Delta \mathcal{L}' = d' \cdot z$ is an *unbiased* estimator of $\nabla_\Delta \mathcal{L}$. For the scalar case with $d(z) \approx \nabla_\Delta \mathcal{L} \cdot z$ and clipping threshold $C$, direct computation yields $\mathbb{E}[d' \cdot z] = f'(\theta) - 2f'(\theta)\int_{c}^{\infty} z(z - c)\phi(z)\,dz < f'(\theta)$ whenever the clipping is non-trivial. Clipping $d$ (which is an odd function of $z$) before multiplying by $z$ reduces the expected inner product and introduces a downward bias on gradient magnitude. The practical variance reduction (Eq. 7: $\mathbb{E}[d'^2\|z\|^2] \leq \mathbb{E}[d^2\|z\|^2]$) holds trivially by construction and remains valid, but the "unbiased" claim in Theorem 1 is the load-bearing step in the Eq. 8 derivation. If Theorem 1 is wrong, the variance reduction proof through Eq. 8 is not valid as stated. The proof is in the appendix (unavailable here), but the conclusion conflicts with a straightforward expectation calculation.

### Minor

1. **Limited analysis of the 2-bit regime.** Table 3 only reports one model and only compares against Zero-Shot-Q (no MeZO baseline exists for AQLM, but at least a QLoRA-style baseline should be included, or the gap explained). The claim about "on-device learning for edge devices" is unsubstantiated with measured latency or device trials.

2. **Performance gap on some tasks is large and unexplained.** For Llama-3.1-8B on CB (69.6 vs. 91.1 for MeZO) and RTE (66.8 vs. 70.0), QZO lags noticeably. A breakdown of whether this is due to quantization noise, the restricted parameter space (scales only), or convergence issues would strengthen understanding of the method's limitations.

3. **Upper-bound baseline uses SGD, not AdamW.** The "fine-tuning upper bound" uses SGD rather than AdamW due to resource constraints (footnote 2). This may understate the true capability gap, though it is acknowledged.

### Trivial

- The claim "QZO is both memory-efficient and computation-efficient" (Table 2 caption) is informally stated; the FLOPs comparison conflates per-step and total-training FLOPs in a way that depends heavily on training step counts.

---

## Nice-to-Haves

- An experiment combining QZO with LoRA-style adapters on top of quantized weights to recover some of the performance gap while retaining most memory savings would be a natural next step and would make the paper more actionable.
- A wall-clock time comparison alongside FLOPs would help practitioners assess actual training speed.

---

## Novel Insights

The observation that quantization scale parameters serve as a *differentiable proxy* for the discrete quantized weights—enabling both ZO perturbation and gradient updates in a continuous parameter space that is orders of magnitude smaller than the model itself—is genuinely insightful. This reframing of QAT as "scale fine-tuning" opens a path toward extremely frugal model adaptation that doesn't require any form of gradient backpropagation through the quantization operator, and the 100× FLOPs reduction relative to MeZO (not just memory) is an underemphasized benefit of operating in a tiny parameter subspace.

---

## Suggestions

1. Add a QLoRA comparison in the main table, even if only for memory profiling and one or two tasks, to situate QZO in the broader landscape.
2. Revise or carefully re-examine Theorem 1. If the estimator is biased, acknowledge it and re-frame DDC's contribution solely in terms of variance reduction (Eq. 7), which does not require Theorem 1 and is sufficient to motivate the technique.
3. Report wall-clock time per step and total training time for QZO vs. baselines to complement the FLOPs analysis.
4. Investigate whether a small set of unfrozen LoRA-style adapters (updated via SPSA) layered on top of QZO scales could close the performance gap at modest memory cost.

---

## Score and Decision

QZO addresses a practically important problem with a clean, implementable idea. The 18× memory savings over standard fine-tuning is real and enables new deployment scenarios. However, the absence of a QLoRA comparison is a significant omission that leaves the paper's empirical case in an incomplete state, and Theorem 1—which underpins the theoretical story for DDC—appears to be incorrect. These are addressable issues, but they are significant enough to warrant revision before acceptance.

MY FINAL SCORE: <score>5</score>
MY FINAL DECISION: <decision>Reject</decision>
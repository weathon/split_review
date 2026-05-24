Now I have a thorough picture of both the paper and the calibration landscape. Let me synthesize everything into the final review.

## Summary
This paper proposes QZO (Quantized Zeroth-order Optimization), a method that enables fine-tuning of quantized LLMs using zeroth-order optimization. The key insight is to perturb the continuous quantization scales rather than discrete quantized weights during ZO gradient estimation (Q-SPSA), and to stabilize training via directional derivative clipping (DDC). QZO reduces memory by >18× compared to full-parameter AdamW fine-tuning, works with both scalar-based (GPTQ, 4-bit) and codebook-based (AQLM, 2-bit) PTQ methods, and achieves performance on par with or exceeding MeZO across five NLP benchmarks and three model families, while using ~3× less memory.

## Strengths
- **Novel and elegant core idea:** Perturbing continuous quantization scales instead of discrete weights (Q-SPSA, Eq. 5) is a clean solution to the fundamental incompatibility between ZO perturbation and quantized weights. The approach is orthogonal to both scalar-based and codebook-based PTQ methods, demonstrated on GPTQ (4-bit) and AQLM (2-bit). This is the paper's central contribution and it is well-motivated and well-executed.

- **Strong empirical results with meaningful baselines:** Table 1 shows QZO consistently outperforms zero-shot baselines and achieves results on par with or better than MeZO across three model families (OPT-6.7B, Llama-2-7B, Llama-3.1-8B) and five NLP tasks, despite using 4-bit quantized weights and ~3× less memory. On Llama-2-7B SQuAD, QZO achieves 85.5 F1 vs. MeZO's 80.7. Under extreme 2-bit quantization (Table 3), QZO improves Llama-2-13B from 57.6% to 80.5% accuracy on SST-2. The memory profiling (Figure 1) thoroughly documents the >18× reduction vs. AdamW full fine-tuning.

- **DDC is convincingly demonstrated as essential for stability:** Figure 2 shows that without DDC, training collapses to NaN within 22 steps. The clipping threshold ablation (Figure 3) shows stable performance for C ≥ 75, demonstrating robustness. The method is simple (scalar clipping of the directional derivative) and clearly effective.

- **Substantial computational efficiency beyond memory:** Table 2 shows QZO updates only ~1% of parameters compared to full fine-tuning and uses ~1% of MeZO's FLOPs, making it both memory- and computation-efficient.

## Weaknesses

### Fatal
None.

### Major
- **Theorem 1 (unbiasedness of DDC) requires scrutiny:** The paper claims the clipped gradient estimate $\hat{\nabla}_{\Delta} \mathcal{L}'$ is an unbiased estimate of the true gradient (Theorem 1). The proof is deferred to Appendix A (stripped in the parsed submission, so unverifiable). The claim is mathematically surprising: clipping the scalar directional derivative $d$ (which depends on the random vector $z$) before multiplying by $z$ would generally introduce bias since the clipping truncation breaks the symmetry that SPSA relies on for unbiasedness. The variance reduction argument (Eq. 7–8) depends on this claim — specifically, the step from $\mathbb{E}[\|\hat{\nabla}_{\Delta} \mathcal{L}\|]^2 = (\nabla_{\Delta} \mathcal{L})^2$ to concluding variance reduction relies on Theorem 1. If the claim is incorrect, the theoretical justification for DDC is weakened, though the empirical evidence for DDC's effectiveness stands independently. *The authors should either provide a rigorous proof, qualify the conditions under which unbiasedness holds, or reframe the analysis as bias-variance trade-off.*

### Minor
- **QLoRA as a missing baseline:** QLoRA (Dettmers et al., 2023) is a widely-adopted method for fine-tuning quantized LLMs using LoRA adapters and backprop. While QZO operates in a fundamentally different paradigm (zeroth-order, no backprop), a comparison against QLoRA on the memory-vs-accuracy Pareto frontier would better contextualize QZO's practical advantage. This is not essential for validating QZO's contribution within the ZO framework (where MeZO is the primary baseline), but would strengthen the paper's claim of "pushing the limits of memory-efficient training."

- **SGD upper-bound vs. AdamW memory comparison creates a mild inconsistency:** The memory reduction claim (18×, Figure 1) is measured against AdamW, which is appropriate since AdamW is the standard full-training approach. However, the accuracy upper bound in Table 1 uses SGD fine-tuning (acknowledged in footnote 2 as due to compute constraints). AdamW fine-tuning would likely achieve higher accuracy, widening the gap to QZO. The paper would benefit from either reporting AdamW fine-tuning accuracy (even if cited from prior work) or explicitly discussing this discrepancy.

- **Unexplained cases where QZO outperforms MeZO:** On Llama-2-7B SST-2 (90.0 vs. 83.5) and SQuAD (85.5 vs. 80.7), QZO meaningfully outperforms MeZO despite operating on quantized weights with lower precision. The paper notes this result but offers no hypothesis for why it occurs (e.g., implicit regularization from scale-only updates, reduced variance, or favorable initialization from GPTQ). Providing even a brief discussion would strengthen confidence that these are not artifacts of seed variance or hyperparameter differences.

### Trivial
- The interplay between group-wise quantization (GPTQ group size 128) and the per-element perturbation of scales could be described more explicitly in Section 3.2.1, as the quantization scale $\Delta$ is group-level while the perturbation in Algorithm 1 appears element-wise.

## Nice-to-Haves
- Reporting results with multiple random seeds and error bars for at least one model × dataset combination to quantify ZO training variance.
- A more detailed memory breakdown separating weights, quantization scales, and activation memory would help readers extrapolate to other quantization schemes.
- Exploring sensitivity to training data size or longer training (e.g., 100k steps) to understand convergence behavior.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **Harsh Critic: "QLoRA omission is structural and fatal"** — Overstated. QLO is a first-order PEFT method operating in a different paradigm (backprop + LoRA adapters). QZO's primary comparison is to other ZO methods (MeZO). The omission is a gap, not a fatal flaw. Demoted to Minor.

- **Harsh Critic: "Theorem 1 makes the theoretical foundation collapse"** — Overstated as fatal. The empirical evidence for DDC is strong (Figures 2, 3), and the variance reduction intuition ($d'^2 \leq d^2$) holds regardless of unbiasedness. Kept as Major for theoretical rigor concerns, but does not invalidate the empirical contribution.

- **Harsh Critic: "Memory profiling breakdown could separate weights, scales, and activation memory"** — This is presentation polish, not a substantive weakness. Moved to Nice-to-Haves.

- **Harsh Critic: "Training stability across different random seeds is not reported"** — Reasonable but non-essential; standard in the ZO fine-tuning literature (MeZO itself reports single-run results). Moved to Nice-to-Haves.

- **Harsh Critic: "AQLM kernel modification details are sparse"** — The paper provides a code pointer and the modification (disentangling matrix reconstruction from matmul) is briefly described. The original submission includes a code repository. Removed.

- **Strength Finder: various generic framings** — Filtered. Only concrete, evidence-backed strengths retained.

## Novel Insights
The reviewer synthesis reveals an interesting tension in the ZO + quantization literature: several contemporaneous works (SensZOQ, Sparse MeZO, SubZero) address the ZO-quantization incompatibility by selecting sparse subsets of parameters to update at full precision, while QZO takes the orthogonal approach of updating only the quantization scales. This contrast — sparse parameter selection vs. scale perturbation — represents a genuine design dimension for future ZO-quantization methods, where QZO's scale-perturbation approach has the advantage of being simpler (no mask construction), more general (works with codebook-based methods like AQLM), and requiring no backprop at any stage.

## Suggestions
- Address Theorem 1: either provide the proof in detail (with clear conditions) in the rebuttal, or reframe as an empirical variance-reduction method with an analysis of the bias-variance trade-off introduced by clipping.
- Consider adding a QLoRA comparison even if in a limited setting (e.g., one model, one dataset) to situate QZO within the broader memory-efficient fine-tuning landscape.
- Discuss possible reasons for QZO outperforming MeZO on specific tasks (SST-2, SQuAD on Llama-2-7B) — this would turn a curious result into an interesting insight about scale-only ZO updates.
- The paper evaluates originality (novel combination of ZO + quantization via scale perturbation), importance (memory-efficient training is a pressing problem), soundness (experiments are thorough; one theoretical concern), clarity (well-structured and readable), and community value (practical method with released code). Overall, this is a solid contribution with one theoretical rough edge.

## Score and Decision

**Calibration anchors:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| SubZero (FK6T0U4Mg1) | 4.25 | R1 | QZO is clearly stronger — broader evaluation, more novel core idea, quantization integration |
| Sparse MeZO (4Kw4KAoVnx) | 5.50 | R2 | QZO is stronger — more elegant approach (scale perturbation vs. sparse mask), broader evaluation, 2-bit results |
| HiZOO (bEqI61iBue) | 5.67 | R2 | QZO is comparable or slightly stronger — cleaner idea, fewer forward passes, quantization integration, though HiZOO has broader model scale |
| SensZOQ (myYzr50xBh) | 5.80 | R1/R2 | QZO is stronger — more novel core idea, no backprop needed for setup, broader model families, 2-bit results |
| EfficientDM (UmMa3UNDAz) | 6.50 | R2 | Different domain (diffusion models), comparable quality level |
| LQ-LoRA (xw29VvOMmU) | 6.75 | R2 | QZO is somewhat below — LQ-LoRA has stronger algorithmic contributions (ILP, data-aware variant), larger-scale experiments, and builds more substantially on prior work |
| LOZO (9BiVepgmWW) | 7.00 | R1/R2 | QZO is clearly below — LOZO has stronger convergence theory, momentum integration, and broader model scale |

**Round 1 bracket:** 5.0–7.0. **Round 2 narrowing:** QZO sits above SensZOQ (5.80) and HiZOO (5.67), but below LQ-LoRA (6.75) and LOZO (7.00). The closest comparable anchors in quality are in the low-6 range. QZO's elegant core idea and strong empirical results place it solidly above the 5.5–5.8 cluster, but the Theorem 1 concern and absence of QLoRA comparison keep it below the 6.5+ tier. Final score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
I now have thorough evidence from the paper. Let me produce the final review.

## Summary

This paper identifies that Mamba models' long-context degradation stems from out-of-distribution (OOD) discretization step sizes (Δ_t) that grow with sequence length, causing exponential decay of long-range information. The authors propose MambaExtend, which learns per-layer (or per-channel) scaling factors for Δ_t via lightweight optimization — either backpropagation or zeroth-order SPSA — while keeping all model weights frozen. Experiments on Pile, PG-19, LongBench, and passkey retrieval across Mamba-130M and Mamba-1.4B show meaningful perplexity reductions and retrieval improvements over both the pre-trained baseline and DeciMamba, with orders-of-magnitude fewer parameter updates.

## Strengths

1. **Identifies a concrete, measurable cause of Mamba's long-context degradation.** The paper shows empirically (Figures 2–3) that accumulated Δ_t values grow with context length, and that scaling Δ_t down substantially reduces perplexity. This is a useful diagnostic that the community can build on.

2. **Lightweight calibration achieves 32× context extension with meaningful gains over DeciMamba.** On PG-19 at 70k context, MambaExtend achieves PPL 30.62 vs. DeciMamba's higher PPL — a ~40.6% reduction (Figure 4, Section 5.2). On passkey retrieval, MambaExtend calibrating ~3500× fewer parameters for Mamba-130M still matches or exceeds DeciMamba's retrieval scores (Figure 5). On LongBench, average accuracy improves by up to 6.03% (Table 2).

3. **Dramatic reduction in tunable parameters and peak memory relative to full fine-tuning.** For the practically relevant per-channel variant, MambaExtend requires ~3500× (130M) and ~7100× (1.4B) fewer parameter updates than full fine-tuning (Figure 5 caption), while using up to ~2–3.87× lower peak memory (Figure 6). This makes the method plausible for resource-constrained deployment.

4. **Zeroth-order optimization matches backpropagation performance.** Table 4 shows CF_ZO (SPSA-based) achieves comparable perplexity to CF_BP on Pile, demonstrating that the scaling factors can be learned via forward passes only — a practically useful property for memory-limited settings.

5. **Ablation identifies the right granularity trade-off.** Table 3 shows per-channel scaling is needed for retrieval tasks, while per-tensor scaling (though maximally efficient) fails. This provides actionable insight for practitioners.

## Weaknesses

### Fatal
None.

### Major

1. **Headline improvement ratios are inflated by comparisons against a broken baseline.**  
   The paper prominently reports "~8145× PPL improvement" (abstract, Figure 1, Table 1) and "~5.42×10⁶× fewer parameter updates" (abstract, Section 5.3). These numbers are technically correct but practically misleading:
   - The 8145× figure compares MambaExtend's PPL against a pre-trained Mamba whose PPL is 995,328 — i.e., the model has catastrophically failed at long context. Any sensible intervention would produce a dramatic ratio. The practically meaningful comparison is the 40.6% PPL reduction over DeciMamba (which the paper does report, but it is buried).  
   - The 5.42×10⁶× parameter savings figure corresponds to the per-tensor scaling variant, which the paper itself shows *fails entirely* on the passkey retrieval task (Table 3: per-tensor scores near 0%). For the per-channel variant that actually works on retrieval, the savings are ~3500× (Figure 5 caption) — still large, but three orders of magnitude smaller.  
   The paper should report gains for the task-appropriate variant as the primary numbers and relegate the inflated comparisons to supplementary context.

2. **Zeroth-order optimization details are insufficient for reproducibility.**  
   The paper specifies only that CF_ZO uses SPSA for "one epoch" with 20 calibration samples. It does **not** specify the learning rate, perturbation size (ε for SPSA), effective batch size, number of gradient steps per calibration sample, learning rate schedule, or convergence criterion. Since SPSA's convergence is sensitive to these choices and "epoch" is undefined when calibration samples can be reused or iterated over multiple times, another group cannot faithfully reproduce the results. Given the paper's emphasis on the ZO variant as a key contribution, this omission is significant.

3. **Causal claim about OOD discretization being the *primary* cause is overstated.**  
   The abstract states that degradation is "primarily due to the out-of-distribution (OOD) discretization steps." The evidence is correlational (Δ_t grows with context length; scaling Δ_t improves PPL) and the paper itself acknowledges that optimal scaling does **not** restore performance to the training-context PPL (Section 3: PPL 3.7 at 2k vs. best scaled PPL ~23.5 at 32k). This residual gap implies other mechanisms (e.g., limited effective receptive field as DeciMamba addresses, or saturation of the gating/convolution components) are also at work. The language should be softened to "a key factor" or "a significant contributor."

### Minor

1. **"Training-free" is imprecise and overclaimed.**  
   The title, abstract, and methodology sections repeatedly call MambaExtend "training-free" (line 4, line 89, line 159). Yet the method explicitly optimizes scaling factors via gradient descent or ZO on calibration samples — that is training, just of a very small parameter set instead of model weights. "Weight-freezing," "lightweight calibration," or "parameter-efficient" would be accurate. This is more than pedantry: a reader evaluating deployment on truly resource-constrained devices needs to know that calibration still requires data, forward passes, and a loss function. The cost of this calibration (even if small) should be transparent.

2. **No variance or confidence reporting.**  
   Calibration uses only 10–20 samples, and results are reported as point estimates. Given the small calibration set, results could be sensitive to which samples are drawn. Reporting standard deviations across multiple calibration sets or seeds would increase confidence.

3. **Table 3 (ablation on granularity) does not state the evaluation context length.**  
   The passkey retrieval scores are reported without specifying at what context length they were measured. This makes the trade-off between granularity and performance harder to interpret.

4. **Some figure descriptions are unclear.**  
   Figure 6 labels "MambaExtend-130M-8k" and "DeciMamba-130M-4k" without clarifying in the caption that "8k" and "4k" refer to the calibration/fine-tuning context length, not the evaluation length. Similarly, Figure 7's heatmap analysis is described only qualitatively; a quantitative summary (e.g., average ΣΔ_t at early token positions before/after calibration) would strengthen the analysis.

### Trivial
None.

## Nice-to-Haves

- **A direct cost comparison in terms of total forward passes / GPU-hours** rather than "per-epoch time." For ZO methods, each gradient step requires 2 forward passes, so "epoch" is not a fair comparison unit across methods.
- **LongBench results for DeciMamba** to complete the comparison on all benchmarks where MambaExtend is evaluated.
- **Experiments on a larger Mamba model (e.g., 2.8B)** to demonstrate scalability of the approach for the regime where its efficiency argument is most compelling.
- **A dedicated limitations section** acknowledging that (a) per-tensor scaling fails on retrieval, (b) the method does not restore training-context PPL, (c) calibration data requirements may vary across tasks, and (d) ZO convergence may slow for many scaling factors.

## Removed Points

These points from the input reviews are flagged to be removed — treat them with caution:

- **Garbled sentence about "a part that fails to provide a very high PPL"** (Harsh Critic "Other Observations" bullet 2). This is a parser/formatting artifact; the original submission does not have this issue. Removed per Hard Rules on formatting artifacts.
- **"Missing appendix / missing proofs"** — The parser strips appendix sections from all papers. Removed per Hard Rules.
- **"The paper should cover broader breadth" style criticisms not targeting the paper's own scope.** Removed per Soft Rules on scope creep.

## Novel Insights

None beyond the paper's own contributions. The reviews largely agree on the paper's strengths and weaknesses; no reviewer identified a fundamental insight the paper itself missed.

## Suggestions

1. **Retire or demote the inflated headline ratios.** Report the 40.6% PPL reduction over DeciMamba and the ~3500× parameter savings for the per-channel (working) variant as the primary numbers. Move the 8145× and 5.42×10⁶× figures to a supplementary note explaining they are against a collapsed baseline / non-working variant respectively.
2. **Replace "training-free" throughout with precise terminology** such as "weight-freezing," "lightweight calibration," or "parameter-efficient context extension."
3. **Provide full SPSA/optimization hyperparameters** in the main text or supplementary: learning rate, perturbation size, effective batch size, number of steps per calibration sample, and convergence criterion.
4. **Add variance or multi-seed results** for the key calibration experiments (at least perplexity and retrieval).
5. **Soften the causal language** about OOD discretization being the *primary* cause to "a key factor" and explicitly discuss the residual performance gap.

## Score and Decision

**Originality:** The observation about Δ_t behavior at long contexts and the idea of per-layer scaling are novel and practically motivated. **Quality of research question:** The question of how to extend Mamba's context without expensive fine-tuning is timely and important. **Soundness:** The core experiments are well-designed (multiple tasks, two model sizes, comparison to the only prior method), but the presentation overclaims and the ZO optimization is underspecified for reproduction. **Clarity:** The writing is generally clear but the inflated headline numbers and imprecise "training-free" framing detract. **Value to community:** If the presentation issues are corrected, the method offers a genuinely useful, lightweight option for Mamba context extension.

The paper has a real, useful contribution. The core method is sound, the comparisons against DeciMamba are legitimate and favorable, and the ablation studies provide practical guidance. However, the presentation inflates the contribution through misleading headline numbers, imprecise terminology, and omitted optimization details. These issues are fixable with a major revision. The overall quality warrants acceptance rather than rejection because the identified problems are presentational and completeness-based, not structural: the core claims (MambaExtend improves long-context performance with far fewer parameters than fine-tuning) survive when properly calibrated.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
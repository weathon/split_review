- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 8, 6, 5
Now I have thoroughly verified all reviewer claims against the paper. Let me construct the final review.

## Summary

LQ-LoRA proposes decomposing each pretrained weight matrix into a fixed quantized component plus a finetunable low-rank component via an iterative alternating SVD-quantization algorithm. It further introduces an integer linear programming (ILP) formulation for per-matrix mixed-precision quantization and a data-aware Fisher-weighted variant. The method is evaluated on RoBERTa-Large and LLaMA-2 (7B and 70B) across language modeling, GLUE, and instruction tuning, consistently outperforming QLoRA and GPTQ-LoRA at the same or lower bit budgets. The paper is well-written, the method is clean and practical, and the limitations are honestly discussed.

## Strengths

1. **Novel iterative low-rank plus quantized decomposition (Section 3.1, Algorithm 1).** The alternating SVD-quantization loop is a well-motivated initialization for LoRA that explicitly accounts for quantization error. Figure 1 confirms that decomposition error decreases over iterations and that LQ-LoRA achieves lower reconstruction error than vanilla NF-3 quantization across all layers of LLaMA-2-7B. This is a genuine algorithmic contribution beyond single-step approaches (e.g., Yao et al. 2023's residual SVD, which is a special case of one iteration).

2. **ILP for mixed-precision quantization (Section 3.2).** The ILP formulation (Equation 4) dynamically assigns different bit-widths and block sizes per matrix given a target memory budget, unlike the uniform quantization in QLoRA. The search space of 3⁵=243 configurations is well-defined, and the pre-computation process is documented. Figure 4 shows the ILP makes non-trivial per-matrix allocation decisions that differ qualitatively between weighted and unweighted variants.

3. **Consistent empirical outperformance across multiple scales and metrics (Figure 2).** Across LLaMA-2 7B and 70B and three metrics (C4 perplexity, WikiText-2 perplexity, MMLU accuracy), LQ-LoRA outperforms QLoRA and GPTQ-LoRA at similar or lower bit budgets. For example, 3.5-bit Fisher LQ-LoRA is comparable to 4.127-bit QLoRA, and 2.75-bit LQ-LoRA is competitive with 3.127-bit QLoRA. This directly validates the core claim.

4. **Fisher-weighted variant provides gains at very low bit-widths (Table 1, Figure 2).** The data-aware variant achieves 87.3 GLUE at 2.5 bits for RoBERTa-Large vs. 85.7 for unweighted LQ-LoRA and 75.4 for QLoRA. On LLaMA-2-7B, Fisher weighting meaningfully outperforms the unweighted version at all target bit widths, demonstrating practical benefit in the aggressive sub-3-bit regime.

5. **Effective sub-3-bit model compression demonstrated (Table 2).** LQ-LoRA compresses LLaMA-2-70B to 2.85 effective bits (including LoRA components) with C4 perplexity 4.54, outperforming several sub-4-bit PTQ methods (GPTQ 3-bit, OmniQuant, SpQR). The paper also verifies that the resulting compressed model can be finetuned on a single 80GB GPU.

6. **Honest discussion of limitations and negative results (Section 5).** The paper transparently discusses the heuristic nature of the iterative algorithm, negative results (refactorization not helpful, hybrid approach not helpful), and scope limitations. This strengthens trust in the reported positive results.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **No variance or statistical significance reporting.** The paper reports no standard deviations, confidence intervals, or per-seed results for any metric across any experiment (Figure 2, Table 1, Table 2). With what appears to be single-run evaluations, it is impossible to assess whether observed improvements are statistically significant. While single-run evaluation is common practice in this area, the paper would benefit from at least reporting standard errors or bootstrap-based confidence intervals. This does not invalidate the consistent pattern of improvement but limits rigor.

2. **GLUE results reported only as averages, without per-task breakdowns.** Table 1 shows only average GLUE scores across all tasks. Per-task results (MNLI, QQP, SST-2, MRPC, CoLA, etc.) would let readers assess whether gains are uniform across tasks or concentrated in a few. The original LoRA paper (Hu et al. 2022) and QLoRA paper report per-task numbers, making this omission notable.

3. **Fisher-weighting benefit diminishes at 70B without analysis or hypothesis.** The paper acknowledges (line 243) that "this discrepancy shrinks at the 70B scale" but offers no investigation into why. Since the Fisher computation is the method's most expensive component (requiring backprop through the full model), understanding when and why it helps (or fails to help) is practically important. The paper would be stronger with a diagnostic, such as comparing the reconstruction error of Fisher-weighted vs. unweighted decomposition across layers at 70B.

4. **Instruction-tuning evaluation is narrow.** The Vicuna-style evaluation uses GPT-4 to compare model outputs against GPT-3.5 on only 80 curated questions, with a win/tie/loss design and no error bars. While this follows the QLoRA evaluation protocol, it is the weakest part of the empirical case. The paper also excludes GPTQ-LoRA from this setting due to training instability (footnote 4), reducing the baseline count. This does not invalidate the results but lowers confidence in claims about instruction-following superiority.

### Trivial

1. **No actual peak memory measurements during finetuning.** The paper states (Section 4.3) that sub-3-bit 70B models can be finetuned on a single 80GB GPU with batch size 2 and sequence length 2048, but does not provide concrete peak GPU memory consumption figures. The storage breakdown (Figure 6) covers only model storage, not runtime memory including activations, gradients, and optimizer states.

## Nice-to-Haves

- An investigation into why Fisher weighting's benefit diminishes at 70B (e.g., comparing reconstruction error of weighted vs. unweighted decomposition across layers, or checking whether the ILP compensates)
- Per-task breakdowns for the GLUE benchmark
- Hyperparameter sensitivity analysis for the Fisher computation (currently fixed at 10000 C4 samples with sequence length 1024)
- Concrete peak memory measurements for finetuning (activations + gradients + optimizer states), not just storage

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Background on LoRA and NF quantization is accurate but slightly dense"** — Pure presentation/style nitpick. Not a substantive weakness.
2. **"Search space |C|=3^5 could be clarified earlier"** — The paper already states this at line 129 where the ILP is introduced. Presentation nitpick.
3. **"The memory breakdown would benefit from a more detailed discussion of finetuning memory"** — The paper does discuss finetuning memory (line 280: "Finetuning requires more memory due to memory required for the activations and LoRA gradients/optimizer states"). The criticism asks for more detail beyond what's standard for a paper of this length.
4. **"Could the metric be measuring a proxy?" / "Are confounders controlled?" style speculations from the harsh critic's sweeping categories** — These are generic area-of-concern probes, not specific identified problems anchored to paper content.
5. **Strength Finder's characterization of LQ-LoRA as lying on a "strictly better Pareto frontier"** — The paper does not use the term "Pareto" or make this claim. The accurate strength (consistent outperformance at similar/lower bit budgets) is preserved in Strengths #3 above.
6. **Strength Finder's claim about "no trade-off"** — Overstated. The empirical pattern is consistent improvement but the paper does not make a formal "no trade-off" claim.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add per-task GLUE results and variance estimates (standard deviations or confidence intervals) for all main experiments.** This single change would substantially strengthen the empirical rigor.
2. **Add a brief diagnostic for the 70B Fisher-weighting result.** Even a sentence offering a hypothesis (e.g., "the ILP may already capture most of the allocation benefit at scale, leaving less room for Fisher weighting to improve further") would address the concern.
3. **Report concrete peak GPU memory measurements** for the finetuning configuration described (70B, batch size 2, seqlen 2048, 80GB GPU) to substantiate the memory-efficiency claim.
4. **Expand the instruction-tuning evaluation** or add error bars (e.g., bootstrapped win-rate confidence intervals) to improve reliability of the Vicuna-style comparison.

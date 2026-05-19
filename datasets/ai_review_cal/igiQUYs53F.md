- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 3, 5
Now I have all the information needed. Let me construct the final consolidated review.

## Summary

This paper introduces the "quantization kernel" concept—elements in activations that are rounded to zero during quantization—and argues that minimizing this kernel is the key to lossless activation quantization. It identifies empirical thresholds (≈19% kernel proportion for OPT, ≈1% for LLaMA) below which INT8 activation quantization incurs negligible degradation. The authors propose CrossQuant, a method that computes per-element scaling factors using both row-wise and column-wise absolute maxima, reducing the kernel to ≈16% for OPT and <0.1% for LLaMA. Experiments on OPT and LLaMA models (6.7B–70B) across language modeling, zero-shot, and few-shot tasks show that CrossQuant matches or improves upon baselines like SmoothQuant, OmniQuant, and AWQ, with particularly strong gains at the aggressive W4A4 setting.

## Strengths

1. **Clean, well-motivated method with theoretical grounding** – CrossQuant is simple and intuitive: by using both row and column absolute maxima ($t_i^\alpha c_j^{1-\alpha}$) as the scaling factor instead of just $t_i$, the zero-bound $B_{i,j}$ shrinks for the dominant case ($c_j < t_i$, covering ≈97% of elements). The paper provides formal proof (Section 3.2, Cases 1‑2) and empirical confirmation (Figure 3) that this reduces the quantization kernel compared to per-token quantization.

2. **Strongest results at aggressive quantization (W4A4)** – CrossQuant reduces perplexity by 4.8%–56.4% over OmniQuant on LLaMA models at W4A4 (Table 1). On OPT‑30B/66B at W4A4, where OmniQuant collapses to near-random accuracy (~28%), CrossQuant maintains 45–55% average accuracy (Table 2). This is the paper's clearest empirical contribution and demonstrates that kernel reduction is especially important at low bit-widths.

3. **Compatibility with weight-only quantization is empirically validated** – CrossQuant is combined with AWQ (CrossQuant+AWQ in Table 1), achieving lower perplexity than either method alone on W4A8‑g128 configurations. This shows the activation-side kernel reduction is orthogonal to weight-side techniques, increasing practical utility.

4. **Ablation on α is systematic** – The paper varies α from 0.15 to 1.0 across multiple models and tasks (Figure 7, Table 3), showing that α ≤ 0.55 consistently works well while α→1 (per-token quantization) degrades performance. This provides actionable guidance for practitioners.

5. **Evaluation spans model families, sizes, and task types** – Experiments cover OPT (1.3B–66B) and LLaMA (7B–70B) on language modeling (WikiText2, C4), five zero-shot tasks, and MMLU, with multiple bit-width configurations (W8A8, W4A8‑g128, W4A4).

## Weaknesses

### Fatal
None.

### Major

1. **OPT perplexity results are missing from the main comparison table.** Table 1 reports perplexity for LLaMA models only; the OPT perplexity comparison across CrossQuant vs. baselines is absent. While OPT perplexity appears in the threshold-determination figures (Figures 5‑6), there is no clean tabular comparison of CrossQuant against SmoothQuant, OmniQuant, and AWQ on OPT perplexity. Since the paper claims to evaluate both model families on language modeling (Section 4.1: "Language modeling experiments include WikiText2 and C4"), this is a notable omission that weakens the evidence for OPT models.

2. **The α choice for OPT models is not adequately justified.** The ablation study (Section 4.3) shows that for OPT‑6.7B on the Lambada task, accuracy peaks at α=0.55 (~80%) and is substantially lower at α=0.15 (~55%). Yet the paper uses α=0.15 for all main results across both LLaMA and OPT. For LLaMA3, Table 3 shows α=0.15 is indeed optimal, but the OPT‑6.7B Lambada result suggests a different optimum. The paper simply states "CrossQuant performs well with α≤0.55 in general" (line 344) without explaining why α=0.15 was specifically chosen for OPT or showing that the overall average across all OPT tasks supports this choice. This is a gap in the empirical reasoning.

### Minor

1. **The "Remove Kernel" experiment (Section 3.3, Figures 5‑6) is underspecified.** The paper states that "W8-Remove Kernel indicates quantizing weights to INT8 and setting different proportion of quantization kernels to zero directly without quantizing other elements in activations" (caption of Figure 5). It does not describe the precise selection rule: are elements selected because they *would be* quantized to zero under a specific quantization scheme, or are they selected by absolute-magnitude ranking? The paper then derives threshold values (19% for OPT, 1% for LLaMA) from this experiment and uses them as design targets for CrossQuant. Since the connection between this artificial zeroing procedure and real quantization behavior depends on the selection rule, the missing specification is a clarity issue. The thresholds themselves are still useful as empirical observations (CrossQuant's actual kernel proportions of ≈16% for OPT and <0.1% for LLaMA are validated by perplexity/accuracy results in Tables 1‑2).

2. **Clamping/saturation is not addressed.** Equations (1) and (5) show `round(X/Δ)` without an explicit clamp to the representable integer range. In symmetric quantization, values exceeding `[-2^(N-1)+1, 2^(N-1)-1]` after rounding must be clipped. Since CrossQuant reduces Δ for most elements (by dividing by $t_i^\alpha c_j^{1-\alpha}$ instead of $t_i$), the scaled values become larger, increasing the risk of overflow. The paper does not discuss whether clamping is applied or what its impact is. This is a standard detail that should be clarified; it is not a fatal gap because the empirical results are strong, but it should be addressed.

3. **No discussion of calibration data requirements.** CrossQuant computes `c_j = max(|X_{:,j}|)` per column. The paper does not specify whether this maximum is computed from a calibration dataset or per-batch during inference. Since column maxima are needed at inference time and affect the quantization scale, this operational detail should be clarified.

### Trivial
- The integer range in line 59 appears as `[-2^{N-1}-1, 2^{N-1}-1]`; the lower bound should likely be `-2^{N-1}+1` for standard symmetric quantization (or `-2^{N-1}` for asymmetric).
- Minor typo: "tow indicators" → "two indicators" in Table 1 caption.

## Nice-to-Haves
- Providing runtime/throughput benchmarks would strengthen the practical case for CrossQuant, especially since the method adds per-element division and an extra column-wise max vector. The current paper is accuracy-focused, which is reasonable, but latency data would be useful.
- Including LLM.int8() or Outlier Suppression as experimental baselines for W8A8 would make the comparison more complete; these are mentioned in related work but not evaluated.

## Removed Points

These points were raised by reviewers but are removed or demoted for the reasons below:

- **"Per-token baseline is catastrophically broken and overstates improvement"** – The paper includes SmoothQuant and OmniQuant as the primary comparison baselines. Per-token is included as a reference point for naive quantization, which is standard practice in this field. Not a valid weakness.

- **"Improvements over SmoothQuant at W8A8 are tiny"** – While the improvements are small (e.g., 0.06–0.48% average accuracy on OPT, 0.01–0.09 perplexity on LLaMA), this is an observation, not a weakness. The paper's strongest evidence is at W4A4, and W8A8 results are presented as demonstrating that CrossQuant matches or slightly exceeds SmoothQuant while being simpler (no offline smoothing). No overclaim.

- **"The Remove Kernel experiment likely conflates effects and is fundamentally different from real quantization"** – The harsh critic speculated that the paper might be zeroing "smallest-magnitude elements" rather than kernel elements. The paper text says it zeros "quantization kernel" elements (Figure 5 caption, line 210). The experiment is underspecified (kept as Minor weakness 1 above), but the critic's stronger claim about conflation is speculative and not supported by the paper text.

- **"No comparison with LLM.int8()"** – LLM.int8() is a mixed-precision method that leaves outliers in FP16, not a W8A8 uniform quantization method. Its inclusion is not standard for this comparison setting. Moved to Nice-to-Haves.

- **"The theoretical gap between artificial threshold experiments and actual quantization is not mentioned in Limitations"** – The Limitations section (Section 5) honestly acknowledges that the kernel explanation is empirical. The paper also validates the thresholds indirectly through CrossQuant's actual performance (Tables 1‑2). This criticism overstates a non-issue.

## Novel Insights

None beyond the paper's own contributions. The two reviewers' perspectives were largely consistent in identifying the method's utility while noting experimental gaps; no genuinely novel observation emerged from the review synthesis that the paper does not already surface.

## Suggestions

1. Add a clean table comparing CrossQuant vs. baselines on OPT perplexity (WikiText2, C4) for all evaluated bit-widths, mirroring Table 1 for LLaMA.
2. Explicitly describe the element selection rule in the Remove Kernel experiment (Section 3.3). Clarify whether kernel elements are identified via a specific quantization function or by absolute-magnitude thresholding.
3. Clarify the clamping behavior: either add the clamp to Equation (1) and Equation (5), or note that no clamping is needed because the scaling factors are chosen to keep all values within range. If clamping is applied, report the proportion of clipped elements and its effect.
4. Explain the α=0.15 choice more carefully for OPT models, given the ablation showing α=0.55 is better for OPT‑6.7B on Lambada. Provide a sensitivity analysis across all OPT tasks or justify with a held-out task.
5. Clarify whether `c_j` and `t_i` are computed from a calibration set or per-batch during inference, and how this interacts with the inference pipeline.

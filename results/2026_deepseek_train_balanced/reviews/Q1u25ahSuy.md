Here is my consolidated review.

---

## Summary

This paper introduces SpQR, a hybrid sparse-quantized representation for post-training LLM weight compression. The method identifies and isolates ~1% of outlier weights (kept in 16-bit precision) while compressing the remaining weights to 3–4 bits using a bilevel quantization scheme that makes small group sizes practical by quantizing the quantization statistics themselves. Supported by a new sensitivity analysis that uncovers weight-level outlier patterns, SpQR achieves perplexity within 1% of uncompressed models at ~4.4–4.7 bits/parameter and significantly outperforms GPTQ and RTN baselines at matched bit rates, while also providing a custom GPU kernel that is 16–21% faster than fp16 inference.

## Strengths

- **Novel identification of weight-specific outlier patterns beyond previously known input-feature outliers.** Section 3.2 provides a systematic sensitivity analysis that uncovers row outliers, column outliers, sensitive attention heads, and rotary embedding patterns in weight matrices. The paper states (line 44) that "our work is the first to demonstrate that similar outliers occur *in the weights, for particular output hidden dimensions*." This analysis directly motivates the hybrid sparse-quantized format and is a genuine analytical contribution.

- **Bilevel quantization makes very small group sizes (e.g., 16 weights) practical, contrary to prior advice.** The paper identifies a known tension — small group sizes improve quantization accuracy but the overhead of storing per-group statistics negates the benefit (lines 190–194, citing Yao et al. 2023). SpQR resolves this by quantizing the statistics themselves to 3 bits. The ablation (Table "ablation") directly supports this: at similar bits/param (~3.6), the 3-bit quantized-statistics variant achieves perplexity 3.74 on Wiki2 vs 3.84 for 16-bit statistics, a real improvement for the same memory budget.

- **Custom sparse-matrix kernel outperforms standard PyTorch/cuSPARSE by nearly 2×.** Table 3 directly compares "SpQR (PyTorch)" vs "SpQR (optimized)": for LLaMA-7B scratch, the cuSPARSE baseline gives 30 tokens/s while the optimized kernel gives 57 tokens/s. This demonstrates a validated engineering contribution beyond the algorithmic innovations.

- **Well-designed ablation studies isolate each design decision independently.** The paper separately ablates (a) quantized vs 16-bit statistics, (b) unstructured vs column vs row outliers (Figure "outliers_fig"), (c) round-zero vs non-integer zero points, and (d) the activation-order heuristic. Each is quantified, making clear which components drive the gains.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **The "near-lossless" claim is slightly overstated for the largest model.** The paper adopts the MLCommons definition of near-lossless (≤1% relative error). While most configurations meet this, LLaMA-65B at 4.71 bits on WikiText2 shows a relative perplexity increase of 1.13% (3.57 vs 3.53 baseline). The paper states (line 376) that "SpQR with 4.6 to 4.71 bits per parameter approaches the non-quantized models with at most 1% margin of error for all models" — this is not fully accurate for the 65B WikiText2 result. The discrepancy is small (1.13% vs 1%) and limited to one dataset, but it should be acknowledged or the claim should be qualified.

- **The abstract frames the method as achieving near-lossless compression at "3-4 bits per parameter," but the near-lossless results are at ~4.4–4.7 bits.** Lines 6–8 and 30–33 in the abstract and introduction link "3-4 bits" with "near-lossless." The actual near-lossless configurations (within 1% perplexity) require an average of 4.44–4.71 bits per parameter, which is closer to 4.5 bits than 3-4 bits. At ~3.9 bits, the relative perplexity increases are 2.5–4.3%, well above 1%. The paper body is transparent about this (the tables clearly distinguish the two regimes), but the headline framing conflates them in a way that could mislead a casual reader.

- **The Falcon-7B PTB perplexity of 19.114 at 3.92 bits (line 454) appears anomalous.** All other SpQR entries for Falcon-7B are close to the 16-bit baseline (e.g., Wiki2: 6.74 vs 6.59; C4: 9.70 vs 9.50), and the Falcon-40B SpQR at 3.90 bits gives PTB of 7.91 (vs baseline 7.83). A value of 19.114 vs baseline 9.90 (a ~93% relative increase) is inconsistent with every other pattern in the paper and likely reflects a data-entry or measurement error. The authors should correct or explain this outlier.

- **Inference speed is not compared against quantized baselines (GPTQ or RTN).** Table 3 compares SpQR against fp16 and a PyTorch sparse baseline, but a practitioner choosing a quantization method would care about inference speed *at the same bit rate* using competing methods. GPTQ at 4 bits can also use efficient kernels; the absence of this comparison limits the practical conclusions one can draw about the speed advantage.

- **The 33B GPU claim in the abstract (line 9) is an extrapolation not directly tested.** The paper evaluates LLaMA-30B (fits on one A100 with SpQR at 22 tokens/s) and 65B (fits with 12 tokens/s). Claiming that SpQR "makes it possible to run 33B parameter LLM on a single 24 GB consumer GPU" is a reasonable inference but is not backed by an experiment in the paper.

### Trivial

- The speedup figures in the abstract (line 9: "15% speedup"; line 47: "20-30% faster") are slightly inconsistent with the measured data. Table 3 shows speedups of 15.8% (30B), 18.9% (13B), and 21.3% (7B) — the lower end of the claimed range is accurate, but "20-30%" overstates the upper bound since no model exceeds ~21%.

## Nice-to-Haves

- **Generative quality evaluation.** The paper's motivation emphasizes that quantization errors can accumulate during sequential generation (lines 25–28), yet evaluation is limited to perplexity and zero-shot accuracy. The authors acknowledge this limitation (lines 547–548), and for a quantization paper of this era, perplexity + zero-shot accuracy is the standard evaluation. Still, even a small-scale generative comparison (e.g., GPT-judged or length-controlled perplexity on generations) would strengthen the link between the motivation and the evidence.

- **Inference speed comparison against GPTQ-quantized inference.** Adding a column to Table 3 comparing SpQR's kernel speed against a GPTQ-quantized model at the same bit width would make the practical speed claim more actionable.

- **Sensitivity to the outlier threshold τ.** The paper mentions that τ is chosen to obtain ~1% outliers, but a trade-off curve (perplexity vs proportion of outliers / vs τ) would help assess robustness.

## Removed Points

These were flagged in the input reviews but are removed for the following reasons:
- *Missing AWQ citation*: AWQ was a contemporaneous method; not a valid weakness.
- *No confidence intervals for perplexity*: Not standard practice for this evaluation setup.
- *Pseudocode inconsistencies (β₁ vs β, duplicate s_z)*: Likely parser/typesetting artifacts; the original submission does not have these issues in a meaningful sense.
- *Missing zero-shot accuracy table*: The data is presented in a figure; a table would be better but the information is accessible.
- *Generative quality gap presented as a major weakness*: The paper acknowledges it, and the standard evaluation for quantization papers at this time is perplexity + zero-shot accuracy. Downgraded to Nice-to-Have.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Correct or explain the Falcon-7B PTB value of 19.114** — this is the most actionable data-integrity issue.
2. **Qualify the 65B near-lossless claim** to acknowledge that WikiText2 shows a 1.13% relative increase, slightly above the 1% threshold, while other datasets remain within bounds.
3. **Align the abstract's framing** with the actual near-lossless bit rates (~4.4–4.7 bits). The paper could honestly say "SpQR achieves near-lossless compression at 4.4–4.7 bits per parameter, significantly outperforming GPTQ at the same model size."
4. **Add GPTQ inference speed** to the speed comparison table to complete the practical picture.
5. **Correct the "20-30% faster" claim** in the introduction to match the observed 16–21% range.

## Score and Decision

This paper presents a genuine technical contribution with strong empirical validation. The sensitivity analysis is novel, the bilevel quantization and outlier isolation are clever and effective, and the method clearly outperforms prior work across model scales. The weaknesses are primarily framing issues (subtle overclaims in the abstract) and one suspicious data point — none are fatal or even major. The paper merits acceptance at ICLR with minor revisions.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
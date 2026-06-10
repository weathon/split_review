Now I have all the verification I need. Let me produce the final review.

## Summary

This paper proposes OATS, a post-training, retraining-free pruning method that decomposes each weight matrix into a sparse plus low-rank sum via Robust PCA with activation-based outlier scaling (inspired by Wanda's second-moment scaling). The method is evaluated on LLMs (Phi-3 Mini/Medium, Llama-3 8B) and ViTs (ViT-Base, DinoV2-Giant) across compression rates 30–60%, along with CPU speedup benchmarks and N:M structured sparsity experiments.

## Strengths

- **Strong empirical performance at higher compression rates (40–50%):** OATS consistently beats SparseGPT, Wanda, and DSNoT across MMLU, zero-shot, and perplexity on all three LLMs at 40% and 50% compression. The gap is substantial and widens with compression — e.g., at 50% on Phi-3 Mini MMLU, OATS achieves 59.99% vs. 54.57% (Wanda), a 5.42pp absolute improvement (Table 1, lines 144–147). This directly supports the claim that the sparse+low-rank structure mitigates degradation at high compression.

- **Measured CPU speedup advantage:** Table 5 (lines 354–377) reports end-to-end CPU throughput (DeepSparse, Intel Xeon Gold 6148) for a compressed Phi-3 Medium model. At 40% compression, OATS achieves 1.73× speedup vs. dense (6.86 tok/s), compared to 1.26× for unstructured pruning (5.08 tok/s). This is a concrete hardware measurement, not a theoretical estimate.

- **Generalization to vision transformers:** Table 6 (lines 500–526) shows OATS achieving best accuracy on ViT-Base and DinoV2-Giant at most compression rates, demonstrating the method is not language-specific and works across architectures.

- **Clean ablation study isolates the contribution of outlier-aware scaling:** Table ablation (lines 240–255) compares four configurations (with/without D-scaling, layer-wise vs. row-wise pruning). Scaling by D reduces perplexity from 18.34→11.50 (37% relative improvement), providing direct evidence that second-moment activation information drives a substantial part of the improvement.

- **Theoretical unification of Wanda as a special case:** Lines 807–808 show that setting the rank ratio κ=0 reduces OATS to a single hard-thresholding step identical to Wanda. This frames OATS as a principled generalization rather than an unrelated method.

## Weaknesses

### Fatal
None.

### Major

1. **Ambiguity about whether baselines used OWL at 60% compression.** The paper states (line 118): "At the higher compression rate of 0.6, we utilize Outlier Weighed Layerwise Sparsity Ratios (OWL)" and the caption of Table 2 says "models compressed by 60% using OWL ratios." It is never explicitly stated that SparseGPT, Wanda, and DSNoT also had their layerwise sparsity budgets determined by OWL rather than uniform per-layer compression. If only OATS used OWL, the 60% results conflate the OWL contribution with OATS's own, and the conclusion that "OATS considerably outperforms its competitors" at 60% cannot be properly evaluated. The core 30–50% results (which use uniform compression per line 118) are unaffected by this ambiguity, but the 60% claim is weakened.

2. **CPU speedup baseline ("Unstructured Pruning") is underspecified.** Table 5 compares OATS against "Unstructured Pruning" without identifying which pruning algorithm produced that baseline, what sparsity pattern it yields, or whether the same calibration data was used. Without knowing whether the baseline comes from SparseGPT, Wanda, magnitude pruning, or some other method, the claimed "$1.37\times$ the speed-up" at 40% is unverifiable. Different pruning methods produce different sparsity distributions within matrices, which materially affects the acceleration achievable through the DeepSparse engine.

### Minor

1. **"Consistently" outperforming claim is slightly overbroad.** At 30% compression, OATS is not the best method on several metrics: zero-shot accuracy on Phi-3 Medium (74.04 vs. SparseGPT 74.53, Table 2); perplexity on Llama-3 8B (9.59 vs. DSNoT 9.36 and Wanda 9.39, Table 3); and ViT-Base accuracy (80.15 vs. Wanda 80.28, Table 6). These are not large regressions, and the overall trend clearly favors OATS at higher rates, but the blanket "consistent" framing in the abstract and conclusion should be qualified to match the actual pattern — OATS performs best at higher compression (40–50%) but is not uniformly ahead at 30%.

2. **Computational cost of OATS is not discussed.** The method runs N=80 iterations of alternating thresholding per layer, each requiring a truncated SVD. For models like Llama-3 8B with ~30–60 weight matrices, this is a substantial computation compared to the near-zero cost of Wanda or the single forward pass of SparseGPT. Since the paper argues for practical utility, omitting wall-clock time or FLOPs is a gap that practitioners would need filled.

3. **Different rank ratios for different model families without justification.** OATS uses κ=25% for Phi-3 and κ=30% for Llama-3 (Table hyperparameters, lines 108–115). The paper does not explain whether these were chosen via validation-set tuning, which risks overfitting the hyperparameters to the evaluation tasks. The ablation (Figure 1) shows performance is sensitive to κ, so this choice matters.

### Trivial
None.

## Nice-to-Haves

- Including a runtime comparison (wall-clock time to compress a given model) would substantially strengthen the paper's claims about practical utility.
- The attention visualization analysis (Section 5) is purely qualitative and would benefit from even a simple quantitative measure (e.g., overlap ratio between sparse and low-rank attention maps).

## Removed Points

These points were raised by the reviewers but removed after verification against the paper. They are listed in case they are useful but should be treated with caution.

- *"No statistical significance or variance reported for any experiment"* — Removed. Single-run evaluation with fixed calibration data is the established standard in this literature (SparseGPT, Wanda, DSNoT all report single numbers). This is not a weakness of this paper.
- *"The DSNoT baseline is given a mild advantage by reporting the best results across SparseGPT and Wanda variants"* — Removed. The paper explicitly discloses this (footnote, line 116). The advantage favors the baseline, which makes OATS's victories more meaningful, not less.
- *"The alternating thresholding convergence guarantees may not carry over to weight matrices"* — Removed. The paper does not claim convergence guarantees; this is a theoretical positioning observation, not an identified problem in the paper.
- *"The attention visualization analysis is purely qualitative"* — Demoted to Nice-to-Have. The paper explicitly says "further investigation is needed" and presents this as exploratory. It is an optional enhancement, not a flaw.
- *"Different rank ratios for Phi-3 (25%) and Llama-3 (30%) but no explanation"* — Already captured as Minor weakness #3 above.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Clarify whether all baselines (SparseGPT, Wanda, DSNoT) used OWL-determined layerwise sparsity budgets at 60% compression, or only OATS did. If they all did, state this explicitly. If not, re-run the comparison without OWL or clearly separate the contributions.
2. Specify which pruning method produced the "Unstructured Pruning" baseline in Table 5, or compare against each baseline method individually.
3. Qualify the "consistent state-of-the-art" framing to acknowledge the 30% settings where OATS is not the best method.
4. Add a brief discussion of the computational cost (wall-clock time to compress a representative model vs. baselines).

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
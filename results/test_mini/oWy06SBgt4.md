Now I have all the information needed. Let me compile the final review.

## Summary

This paper attempts to push fully quantized training (FQT) to an average 1-bit precision, making a first attempt at this challenging regime. It provides theoretical convergence analysis linking gradient variance to optimizer choice (showing Adam is more suitable than SGD), then proposes Activation Gradient Pruning (AGP) — which prunes low-range gradient groups and allocates higher precision to informative groups — alongside Sample Channel joint Quantization (SCQ) to enable hardware-friendly matrix multiplication. On transfer learning tasks with binary-pretrained models, the method achieves ~6% accuracy improvement over 1-bit PSQ baselines and up to 5.13× speedup over FP32 PyTorch on CPU, while acknowledging accuracy gaps of ~5% compared to 32-bit gradient training.

## Strengths

- **First systematic attempt at average-1-bit FQT.** The paper tackles a genuinely open problem — while 4-bit FQT is the current frontier, going to 1-bit requires fundamentally different strategies. The idea of exploiting gradient heterogeneity (pruning low-range groups to allocate precision to informative ones) is well-motivated and supported by gradient distribution heatmaps/histograms in Figure 1.

- **Theoretical analysis connects gradient variance to optimizer choice, directly motivating algorithm design.** Theorems 1 and 2 derive regret bounds showing SGD convergence scales as O(σ²) while Adam scales as O(σ), explaining the empirical failure of SGD at low bitwidths and providing a principled reason to use Adam. This theory-to-algorithm pipeline is clean.

- **AGP provides a quantifiable variance reduction with correctness guarantees.** Equation 24 shows the quantizer variance bound drops from (D^(l)/4)ΣR_i² (for 1-bit PSQ) to (D^(l)/4B²)Σ_{i=1}^{N/b}R_i², while the quantizer remains unbiased (𝔼[Q_g(v)] = v). The unbiasedness is important for convergence guarantees.

- **SCQ addresses a real acceleration bottleneck.** The paper identifies that PSQ cannot accelerate weight gradient computation (because one operand must be dequantized before multiplication). SCQ solves this by applying different group structures for activation vs. weight gradient computation, ensuring both use 1-bit matrix multiplication.

- **Empirical results demonstrate consistent improvement over 1-bit PSQ.** Across 6 datasets and 2 architectures, the method (b=4) achieves ~6% average accuracy improvement over 1-bit PSQ (Table 1). The Adam vs. SGD comparison in Figure 3 confirms the theoretical prediction, with PSQ+SGD diverging entirely while the proposed method maintains reasonable accuracy.

## Weaknesses

### Major

- **No comparison to any 4-bit FQT method.** The paper's framing is explicitly about "pushing the limit from 4-bit to 1-bit" (line 15: "some work have successfully pushed precision down to 4 bits"; line 32: "current research frontier is still 4-bit FQT"). Yet the experiments include no comparison to a 4-bit FQT baseline (e.g., Sun et al. 2020, Chmiel et al. 2021, Xi et al. 2023). The only low-bitwidth baselines are 1-bit PSQ and 8-bit PSQ. Without quantifying accuracy loss *relative to the best 4-bit method*, the core claim that "1-bit is a practical trade-off vs. 4-bit" is unsubstantiated. The paper's justification ("there is no 4-bit format among the standard data types" — line 398) applies to hardware acceleration but not to accuracy comparison, which can be simulated. This gap undermines the central narrative of the paper.

### Minor

- **Framing as "1-bit" is imprecise and potentially misleading.** The title "1-Bit FQT" and repeated phrasing "1-bit FQT" throughout suggest uniform 1-bit arithmetic. In reality, the method uses b-bit quantization (b=2,4,8) for retained groups with pruning to achieve an *average* of 1 bit per element. The paper does explain this in Section 5 ("maintaining an average bitwidth of 1" — line 227) and Table 5 compares "average 1-bit vs. 1-bit," but the title and abstract never qualify the term. A reader expecting true binary arithmetic (XNOR+popcount for *every* element) will be misled. The contribution should be reframed as *average-1-bit mixed-precision FQT with pruning*.

- **Theoretical analysis under convexity does not directly support the non-convex experimental setting.** The regret bounds (Theorems 1, 2) are derived under the convexity assumption of Zinkevich (line 116), but all experiments involve non-convex deep networks. While this is common practice in ML theory, the paper's claim that the theory "reveals Adam is more suitable" is suggestive rather than rigorous for the actual setting. The scaling conclusions (O(σ²) vs. O(σ)) are useful intuition but the gap between theory and practice is large.

- **Missing ablation isolating AGP and SCQ contributions.** The paper combines AGP and SCQ into one method, but never reports results for AGP alone (with standard PSQ for weight gradients) or SCQ alone (without pruning). This makes it impossible to attribute the accuracy improvement to variance reduction vs. the specific quantization scheme. Adding ablations on at least CIFAR-10/CIFAR-100 would strengthen the paper.

- **No 1-bit PSQ or 4-bit baselines for the additional tasks.** Table 2 (Faster R-CNN, MLP-Mixer, BERT) only compares to QAT with 32-bit gradients. Without a 1-bit PSQ baseline or any other low-bitwidth comparison for these tasks, the "potential applicability" claim is weakened. The reader cannot tell if the method generalizes or if these particular tasks are simply easier for low-bitwidth training.

- **The variance bound in Eq. 24 assumes exactly N/b groups are the ones with the largest ranges.** The Bernoulli masks produce a random number of retained groups, and the retained groups are only those with the largest ranges *in expectation*, not deterministically. The bound uses "≤" so it remains valid as an upper bound, but it may not be tight. The paper glosses over this stochasticity.

### Trivial

- The speedup table (Table 3) lists "Basic (32,32,32) = 0.03×" alongside "Ours = 5.13×" with the stated baseline "FP32 Pytorch." This means the authors' unoptimized FP32 implementation runs 33× slower than standard PyTorch. Including this row is fine as a diagnostic, but the large gap (33×) between "Basic" and standard PyTorch raises questions about implementation quality without clarification.

## Nice-to-Haves

- Include the proposed method's curve in the motivating Figure 1, so readers can see where it falls on the accuracy-vs-bitwidth plot.
- Provide wall-clock timing breakdown (quantization, pruning, decomposition, matrix multiply) to verify that decomposition overhead is indeed small in end-to-end training, not just for isolated matrix multiplications (Table 5).
- Test varying b more finely (e.g., b=3,5,6) to validate that b=4 is truly optimal.
- Show convergence curves for additional datasets beyond CIFAR-10.

## Removed Points

These points were flagged by reviewers but are removed with justification:

- **"Speedups computed against unreliable baseline (Basic 32,32,32)"** — Removed as factually incorrect. The table caption explicitly states "The baseline is FP32 Pytorch." The "Basic" row is a diagnostic row showing unoptimized FP32 performance, not the baseline for speedup claims. Ours = 5.13× is relative to standard FP32 PyTorch, which is standard practice.

- **"Table 1 shows accuracy is still 5-10% below QAT, paper treats as acceptable"** — Removed. The paper openly reports this gap, compares to the QAT upper bound, and discusses it honestly. This is characterization, not a weakness. For a first attempt at 1-bit FQT, this gap is expected and the paper does not overclaim.

- **"Speedup table doesn't include decomposition/merging timings"** — Removed. The end-to-end training time in Table 3 implicitly includes all overhead. Separate decomposition timing is in Table 5 as an isolated benchmark.

- **"Value of b not explained"** — Removed. The paper does explain the trade-off (lines 369-379): larger b reduces variance but increases sparsity/information loss. The empirical finding that b=4 is optimal is clearly stated.

- **"Fig. 1 should include proposed method's curve"** — Moved to Nice-to-Haves. A valid suggestion but not a weakness; the figure motivates the problem, and the proposed method's results are in the experiments.

## Novel Insights

None beyond the paper's own contributions. The primary novel insight is recognizing that gradient heterogeneity (varying range across samples/channels) can be exploited: prune the low-range (low-information) groups to save bits while allocating higher precision to high-range groups, keeping the average at 1 bit. This is a clever marriage of pruning and mixed-precision quantization applied to the gradient tensor.

## Suggestions

1. **Add 4-bit FQT baselines.** Even a re-implementation of a basic 4-bit unbiased quantizer on the same tasks would anchor the results and support the "pushing beyond 4-bit" narrative. Show that 1-bit is only X% worse than 4-bit while being Y× faster.
2. **Reframe the title and narrative** as "Average-1-bit" or "Approximately 1-bit" FQT. The current framing invites confusion and overclaim.
3. **Add ablation studies** (AGP-only, SCQ-only, full method) on at least CIFAR-10 and CIFAR-100 to confirm the individual contributions of each component.
4. **Include PSQ baselines for the additional tasks** in Table 2 to demonstrate generalization.

## Score and Decision

**Calibration anchors** (all retrieved papers, not just those read in full):

| Path | Avg Score | Comparison to current paper |
|------|-----------|-----------------------------|
| `wg1PCg3CUP.md` (Scaling Laws for Precision) | 8.00 | Much larger scale (465 runs), deeper theory, broader impact. Current paper is narrower and less rigorous. |
| `wJv4AIt4sK.md` (Interplay: Sparsity+Quantization) | 7.50 | Strong theory+practice with extensive evaluation. Current paper has less comprehensive experiments. |
| `OCHSgafZ1Y.md` (Zero-shot Mixed Precision) | 6.33 | Better ablation and comparison structure. Current paper has a more challenging goal but less complete evaluation. |
| `sYGNCscE9M.md` (Nearly Lossless Bit Switching) | 5.75 | Comparable quality of contribution. Current paper is more novel in problem choice. |
| `zcx6rIMbbR.md` (Efficient Fine-Tuning of Quantized LLMs) | 5.40 | Similar structure but different domain. Current paper is clearer. |
| `pxGucWt9vM.md` (FlatQuant) | 5.20 | Similar evaluation depth. Current paper has more theoretical motivation. |
| `Dm4qrBuFKH.md` (BNN in Binary Weight Space) | 4.67 | Similar niche, limited experiments. Current paper has clearer method. |
| `wJ3GeGLFmc.md` (Sub-8-Bit Integer Training) | 4.50 | Similar topic. Current paper is more honest about limitations and clearer in method. |
| `3j72egd8q1.md` (STE in Disguise) | 5.25 | Different focus. Similar evaluation depth. |
| `KJzz4UwqTb.md` (L4Q) | 4.50 | Similar scope (fine-tuning). Current paper has stronger theory component. |
| `ykhRO1mAg3.md` (FPTQ) | 4.00 | Different domain. Current paper is stronger overall. |
| `XQQMKhGBoY.md` (DFastQ) | 4.50 | Similar structure but less novel. Current paper tackles a harder problem. |
| `1xyar0Ko3E.md` (Adaptive Coreset) | 4.00 | Different approach. Current paper is more complete. |
| `erowpbZcPi.md` (Tilted Losses in QNNs) | 3.67 | Different topic. Lower quality. |
| `orG37FHN4b.md` (Angle-DFQ) | 3.00 | Poor presentation, questionable theory. Current paper is much stronger. |
| `44cMlQSreK.md` (NeuroQuant) | 7.20 | More complete evaluation. Different domain. |
| `LzPWWPAdY4.md` (LoftQ) | 7.33 | More practical impact. Current paper addresses a harder precision regime. |

The paper makes a genuine first attempt at a challenging problem and has a clear, well-motivated algorithm design. However, the missing 4-bit FQT comparison is a significant gap for a paper whose central narrative is about pushing the frontier from 4-bit to 1-bit. The framing imprecision also weakens the presentation. Compared to the anchored papers, this work is stronger than the low-scoring (3-4) papers but significantly less complete than the high-scoring (7+) ones. I position it around 5.5 — a paper with real ideas that needs substantially more experimental work to support its claims.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
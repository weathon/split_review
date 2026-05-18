Now I have all the evidence needed. Let me produce the final consolidated review.

## Summary

This paper makes a first attempt at 1-bit Fully Quantized Training (FQT), pushing the bitwidth frontier below the current 4-bit state of the art. The authors identify gradient variance as the key obstacle and propose Activation Gradient Pruning (AGP) — a stochastic pruning strategy that discards low-range gradient groups and allocates higher precision to informative groups, maintaining an average of 1-bit — combined with Sample-Channel joint Quantization (SCQ), which applies different quantization strategies for weight vs. activation gradients to enable hardware-friendly binary matrix arithmetic. On fine-tuning tasks with binary-pretrained VGGNet-16 and ResNet-18, the method improves over naive 1-bit per-sample quantization by ~6% average accuracy and achieves up to 5.13× training speedup on CPU hardware relative to FP32.

## Strengths

1. **First demonstration that 1-bit FQT can converge on real transfer-learning tasks.** The paper states explicitly that it "makes a first attempt towards achieving 1-bit FQT" (Section 1) and reports successful convergence on six vision datasets and one NLP task. This moves beyond the existing 4-bit frontier.

2. **Theoretical analysis linking gradient variance to optimizer choice in FQT.** Theorems 1 and 2 provide regret bounds showing SGD's convergence scales as O(σ²) while Adam's scales as O(σ), formalizing why Adam is more suitable for low-bitwidth FQT. This insight directly motivates the algorithm design.

3. **AGP is a principled variance-reduction mechanism with a clean analysis.** The variance bound in Eq. (24) shows AGP reduces quantizer variance from O(∑ Rᵢ²) (1-bit PSQ) to O(∑ Rᵢ² / B²), where the sum runs over only the retained groups. The unbiasedness proof via importance sampling (dividing by pᵢ) is technically sound.

4. **SCQ addresses a genuine hardware bottleneck.** The paper correctly identifies that PSQ cannot accelerate weight-gradient computation (one operand must be dequantized), and proposes SCQ to fix this — applying PCQ for weight gradients and PSQ for activation gradients — so both backward matrix multiplications use binary arithmetic.

5. **Real hardware acceleration results.** Speedups are reported on actual devices (Hygon CPU, Raspberry Pi 5) rather than only theoretical FLOP counts. The speedup over 8-bit PSQ is >30×, confirming the practical benefit of extreme bitwidth reduction for resource-constrained devices.

6. **Consistent and statistically reliable main results.** Table 1 reports means and standard deviations over 3 runs, with confidence intervals, showing that the improvement over naive 1-bit PSQ is systematic across architectures and datasets.

## Weaknesses

### Fatal

None.

### Major

1. **No comparison against any 4-bit FQT method, even simulated.** The paper positions itself as pushing the limit "from 4-bit to 1-bit" and calls 4-bit "the current research frontier" (line 32). Yet it never compares accuracy against any existing 4-bit FQT approach (e.g., Sun et al. 2020, Xi et al. 2023). Without such a baseline, the reader cannot evaluate the central trade-off: is the accuracy loss from going 4→1 bits (which is ~5% on average relative to full-precision gradients — and 18.61% and 12.31% relative to 8-bit PSQ for ResNet-18 and VGGNet-16) justified by the further bitwidth reduction? The paper mentions "there is no 4-bit format among the standard data types" (line 398) to excuse the absence of a speed comparison, but a *simulated* 4-bit gradient quantizer for accuracy comparison is straightforward and would anchor the trade-off curve. This gap undermines the core framing.

2. **Experimental scope is narrower than the title and framing imply.** The title claims "Pushing the Limit of Fully Quantized Training to 1-bit," but all experiments are on fine-tuning pre-trained binary models, not training from scratch. The paper acknowledges this limitation in the conclusion (line 456: "The primary limitation of this work lies in its ability to achieve 1-bit FQT in transfer learning tasks but not in training from scratch") — but the abstract, title, and introduction do not carry this qualification. Only two CNN architectures (VGGNet-16 and ResNet-18) are studied in depth; the additional results in Table 2 (single-run, no standard deviations) show large degradation (BERT drops 8.39%, Faster R-CNN drops 1.66 mAP). The paper does not support a claim of general 1-bit FQT capability.

### Minor

1. **No ablation isolating AGP vs. SCQ.** The two components are always evaluated together, making it impossible to assess whether SCQ (which is a hardware-oriented reformatting of the gradient computation) contributes to accuracy beyond what AGP alone would achieve. A simple ablation (e.g., AGP with PSQ for both gradients vs. AGP+SCQ) would clarify this.

2. **Theoretical analysis does not directly cover AGP.** The regret bounds (Theorems 1, 2) compare Adam vs. SGD for general FQT, but do not incorporate the AGP quantizer or derive a bound for it. The paper motivates variance reduction as the key algorithmic insight via theory, then proposes AGP to achieve it, but never completes the loop by bounding AGP's effect on convergence. This is a gap between theory and method, not a fatal flaw, but it weakens the claimed theoretical grounding.

3. **Limited evidence for generalizability.** The single-run Table 2 results (Faster R-CNN, MLP-Mixer, BERT) lack standard deviations. The BERT result (54.81 vs. 63.20 — an 8.39% drop) is notably large and reported without detail on which GLUE tasks were used or how many runs. This casts doubt on the claim of "potential applicability to other architectures."

4. **Choice of hyperparameter b lacks a principled criterion.** The paper observes that b=4 is best empirically and explains the trade-off qualitatively (variance decreases with larger b, but more groups are discarded). No analytical or empirical criterion for selecting b is offered beyond post-hoc observation. This weakens reproducibility.

### Trivial

- Figure 1 caption does not specify which gradient precisions were used for the Adam vs. SGD comparison, which is critical for interpreting the motivating figure.
- Table 3's "Basic" rows show <1× speedup (slower than PyTorch), which is correct for unoptimized code but could confuse readers without additional explanation.

## Nice-to-Haves

- A simulated 4-bit FQT accuracy baseline on the same tasks would greatly strengthen the paper's contribution story and is the single most impactful addition.
- Training-from-scratch experiments on small tasks (e.g., CIFAR-10 at 3-bit or 4-bit FQT, even if not 1-bit) would help delineate where the method's capabilities begin and end.
- An analysis of the computational cost of AGP mask generation (computing per-group ranges, probabilities, and random sampling) would clarify whether the reported speedups are net of this overhead.

## Removed Points

These points were flagged by reviewers but are removed with justification:

- **"Paper does not discuss effect of imputing zeros on downstream computations"** — The paper explicitly says on line 238: "Due to the removal of some groups, the shape of the result differs from the original, and we fill the gaps with zeros." This is already addressed.

- **"Overstated improvement over PSQ"** — The 6% improvement is factually accurate from Table 1. The critic's argument that this merely shows the method "does not completely break" is a matter of framing, not factual error. The paper also reports comparisons to 8-bit PSQ (where degradation is 12–18%), providing the full picture.

- **"Variance comparison should include other per-group quantizers"** — The paper's core concern is enabling 1-bit FQT, and PSQ is the only viable 1-bit per-group quantizer baseline. Requesting comparisons to higher-bitwidth quantizers for variance is scope creep.

- **"AGP unbiasedness argument — groups contribute zero gradients"** — The critic calls this "correct" and then suggests more comparison; this is not a weakness.

- Various pure suggestions for "deeper analysis" and "visualizations" from the Missing Parts section — these are nice-to-haves, not deficiencies.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine tension: the paper has a technically sound method and novel 1-bit FQT demonstration, but its evidence base is too narrow to support the ambitious framing of "pushing the ultimate limit of FQT." The most insightful observation from the critique is the missing 4-bit baseline — without it, the claimed frontier-pushing narrative is empirically incomplete.

## Suggestions

1. **Add a simulated 4-bit FQT baseline** (even just running the same models with 4-bit gradient quantization using standard techniques) across all main datasets. This single addition would resolve the most critical evidential gap and let readers evaluate the 4→1 bit trade-off.
2. **Include a dedicated ablation** separating AGP from SCQ (e.g., reporting results for AGP + PSQ for both gradient types vs. AGP + SCQ) on at least one architecture/dataset pair.
3. **Qualify the title/abstract** to reflect the fine-tuning scope more prominently, or add training-from-scratch experiments on small-scale tasks to justify the broader framing.
4. **Report standard deviations for Table 2** and clarify which specific GLUE tasks were used for the BERT evaluation.

## Score and Decision

**Calibration anchors consulted (all from batch):**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `wJ3GeGLFmc.md` (sub-8-bit integer training) | 4.50 | Also pushes FQT bitwidth, but achieves 4-bit with <1% accuracy loss across more architectures. Current paper is more extreme (1-bit) but has larger accuracy drops (~5%) and narrower scope. Comparable overall quality. |
| `eqKHuxIpp5.md` (on-device TL) | 2.50 | Much weaker paper — trivial experiments, poor clarity. Current paper is significantly stronger. |
| `Dm4qrBuFKH.md` (BNN training in binary space) | 4.67 | Similar quality: genuine contribution but limited experiments. Current paper has more thorough evaluation but similar scope restrictions. |
| `MEbNz44926.md` (binary SR) | 8.00 | Much stronger — thorough experiments, SOTA results, clear motivation. Current paper is substantially weaker. |
| `3j72egd8q1.md` (gradient estimators) | 5.25 | Solid theoretical contribution with moderate empirical support. Comparable to current paper's quality level. |
| `A6K4aqReoF.md` (binary activation RNNs) | 3.75 | Narrow scope, mixed reviewer reception. Current paper is stronger. |
| `LzPWWPAdY4.md` (LoftQ, quantization for LLM fine-tuning) | 7.33 | Much stronger experimental validation across architectures. Current paper far weaker. |
| `E1N1oxd63b.md` (diffusion quantization) | 6.00 | Well-executed with clear contributions. Current paper is weaker due to scope and missing baselines. |

The paper makes a genuine first contribution to 1-bit FQT with a technically sound algorithm, but the experimental validation is insufficient for the strength of the claims. The missing 4-bit comparison, limited architecture scope (only two CNNs in depth), and framing that over-promises relative to the evidence base all weigh against strong acceptance. Relative to the calibration anchors, this paper sits between the rejected sub-8-bit training paper (4.50) and the mid-range gradient estimator paper (5.25) — it has a more novel target (1-bit) but weaker experimental support.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
## Summary

This paper makes a first attempt at pushing Fully Quantized Training (FQT) to an average gradient bitwidth of 1 by combining Activation Gradient Pruning (AGP) — which prunes low-range gradient groups and allocates higher bitwidth to informative groups — with Sample Channel joint Quantization (SCQ) for hardware-friendly binary matrix multiplication. A theoretical regret analysis shows Adam is less sensitive to gradient variance than SGD, motivating variance reduction via AGP. Experiments on transfer learning tasks (CIFAR, Flowers, Cars, Pets, CUB) with ResNet-18 and VGGNet-16 show convergence at average 1-bit gradients with ~5% average accuracy drop from full-precision QAT, and up to 5.13× speedup on Hygon CPU.

## Strengths

1. **First systematic attempt at sub-1-bit-average FQT with real hardware speedups.** The paper demonstrates that training can converge at ~1-bit average gradient precision and reports measured speedups (up to 5.13× on Hygon, 2.49× on Raspberry Pi 5) — not just FLOPs estimates. Table 3 shows the method meaningfully outperforms 8-bit PSQ in speed by 30-45×, and the decomposition of b-bit retained groups into binary slices (Fig. 4, line 238) provides a practical path to binary computation.

2. **AGP reduces quantizer variance with a principled design.** Equation (24) analytically shows AGP reduces variance from \(\frac{D^{(l)}}{4}\sum_{i=1}^N R_i^2\) (1-bit PSQ) to \(\frac{D^{(l)}}{4B^2}\sum_{i=1}^{N/b} R_i^2\), and Figure 5 confirms this empirically. The variance reduction directly explains why the method succeeds where 1-bit PSQ fails (Fig. 3, PSQ-SGD diverges while Ours-SGD converges).

3. **SCQ solves a genuine hardware bottleneck.** The paper identifies that PSQ cannot accelerate weight gradient computation because one operand must be dequantized (line 261). SCQ's per-channel quantization for weight gradients and per-sample quantization for activation gradients (lines 262-266) is a clean fix that demonstrably enables acceleration (Table 3: Ours-Basic 3.17× vs PSQ-Basic 0.07× on Hygon VGGNet-16).

4. **Extension beyond CNNs.** Results on Faster R-CNN (1.66% mAP drop), MLP-Mixer (3.52% drop), and BERT (8.39% average GLUE drop) indicate the approach generalizes beyond convolutional architectures, supporting the claim that the algorithm is not architecture-specific.

## Weaknesses

### Major

1. **Method is limited to transfer learning / fine-tuning only.** The paper explicitly acknowledges this (line 457: "The primary limitation of this work lies in its ability to achieve 1-bit FQT in transfer learning tasks but not in training from scratch"). This fundamentally limits the scope of the contribution. Training from scratch at 3-4 bits remains an open problem, making the "ultimate limit of FQT" framing somewhat aspirational. The experiments are on relatively small-scale transfer learning benchmarks, and it is unclear whether the approach would scale to larger tasks or training from scratch.

2. **Significant accuracy degradation limits practical utility.** Even in the optimal configuration (b=4), the method incurs ~5% average accuracy drop from the QAT baseline on ResNet-18, and on challenging datasets like CUB the gap is larger (~6.5% on ResNet-18, ~4.3% on VGGNet-16). On Cars, the drop is ~13% (ResNet-18, 50.81% QAT → 37.88% Ours b=4). While the paper frames this as "acceptable considering the benefits," a user trading accuracy for speed would need to evaluate whether ~5% average loss (and substantially more on some datasets) is tolerable for their application.

3. **No comparison with existing 4-bit FQT methods.** The paper explicitly frames itself as pushing beyond the 4-bit frontier (lines 15, 32, 52), but provides no accuracy comparison to any 4-bit FQT method (Sun et al. 2020, Chmiel et al. 2021, Xi et al. 2023 are cited in related work but not evaluated). The argument that "there is no 4-bit format among standard data types" (line 398) only rules out speed comparisons, not accuracy comparisons. Without showing that the accuracy-speed tradeoff is competitive with 4-bit methods, the central claim of advancing beyond the 4-bit frontier is unsubstantiated.

### Minor

4. **Theoretical analysis does not directly guide key algorithm design choices.** The regret bounds (Theorems 1, 2) show SGD's convergence rate degrades as O(σ²) while Adam's degrades as O(σ) — a useful high-level insight that motivates variance reduction and Adam preference. However, the theory does not justify the specific design choices of the AGP method: the pruning probability \(p_i \propto R_i\), the choice of b=4 as optimal, or the trade-off between pruning ratio and retained precision. A more targeted analysis (e.g., directly relating MSE to the choice of \(p_i\)) would strengthen the paper.

5. **Unbiasedness argument is presented too tersely.** The paper claims (line 231) that \(Q_g\) is unbiased since \(\mathbb{E}[Q_{PSQ}^b(\mathbf{M}\hat{\nabla})] = \mathbb{E}[\mathbf{M}]\hat{\nabla}\). This is correct via the law of total expectation (condition on \(\mathbf{M}\), use unbiasedness of \(Q_{PSQ}^b\), then \(\mathbb{E}[m_i/p_i|\hat{\nabla}]=1\)). However, the paper skips the conditional expectation step, making the argument appear to assume linearity of \(Q_{PSQ}^b\), which could confuse readers. This should be spelled out.

6. **Ablation on the choice of b is incomplete.** The paper observes b=4 is optimal but only offers a vague explanation: "the increase in b also implies more discarded groups, leading to larger losses" (line 370). It does not analyze why b=8 underperforms b=4 — is it because the pruning ratio becomes too aggressive (7/8 of groups pruned), or because the decomposition overhead grows, or because the variance bound becomes looser? A controlled ablation isolating these factors would be useful.

7. **Pruning overhead is not measured.** The paper reports end-to-end speedups but does not break down the runtime cost of the pruning operations themselves (range computation, random mask sampling, binary tensor decomposition). For smaller layers or architectures, this overhead could offset the gains. A profiling table showing time spent on quantization vs. matrix multiplication would address this.

### Trivial

8. The "Proof is given" on line 236 appears to trail off without the actual proof in the visible text (likely deferred to an appendix that was stripped by the PDF parser). The variance formula derivation should be included in the main paper or clearly referenced.

## Nice-to-Haves

- An accuracy comparison with 4-bit FQT methods (Sun et al., Chmiel et al., Xi et al.) re-implemented under the same setup would substantially strengthen the claim of advancing beyond the 4-bit frontier.
- A theoretical or empirical justification for the choice \(p_i \propto R_i\) (e.g., showing it approximately minimizes quantizer MSE under an average-bit constraint).
- Measuring the empirical bias of the AGP quantizer across training to verify the theoretical unbiasedness in practice.

## Removed Points

- **"The unbiasedness of AGP quantizer is not established and likely incorrect"** (from harsh critic): This criticism is wrong. The unbiasedness follows from the law of total expectation: condition on \(\mathbf{M}\), the inner PSQ quantizer is unbiased, and \(\mathbb{E}[m_i/p_i|\hat{\nabla}]=1\). The paper's exposition is terse but mathematically correct. The reasoning does not require \(Q_{PSQ}^b\) to commute with expectation — it uses conditioning.

- **"The method is not truly 1-bit (Structural)"** (from harsh critic) kept in a weakened form: The reviewer claimed the method is "not truly 1-bit" because retained groups use b-bit precision. However, the paper explicitly states "maintaining an average bitwidth of 1" (line 227) and compares "Average 1-bit vs. 1-bit" (Section 6.3, Table 5), showing the runtime difference is minimal. The computation is decomposed into binary slices (line 238). The "1-bit" framing is somewhat ambitious but the paper is transparent about the averaging mechanism in the technical sections.

- **Strength Finder claims about "first theoretical analysis linking FQT convergence to gradient variance"**: This is kept as a real strength, but the novelty should be qualified — the analysis is under convex assumptions (standard for regret analysis) and does not directly prove the algorithm's design. Included in strength 1 above in a qualified form.

- **Strength Finder generic strengths**: Removed generic/superficial claims about "addressing an important problem" and sycophantic language.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any cross-cutting insight that the paper itself does not already articulate.

## Suggestions

1. Add a comparison with 4-bit FQT methods (at least accuracy-wise, even if speed comparisons are not possible on the same hardware) to substantiate the claim of advancing beyond the 4-bit frontier.
2. Clarify the unbiasedness proof by explicitly stating the conditioning argument: \(\mathbb{E}[Q_{PSQ}^b(\mathbf{M}\hat{\nabla})|\hat{\nabla}] = \mathbb{E}[\mathbf{M}|\hat{\nabla}]\hat{\nabla} = \mathbf{I}\hat{\nabla}\).
3. Add a profiling table showing the overhead of pruning operations (range computation, mask sampling, bit-slice decomposition).
4. Analyze why b=8 underperforms b=4 — is it the aggressive pruning ratio, decomposition overhead, or something else?
5. Consider reframing the title from "1-Bit FQT" to "Average 1-Bit FQT" or similar to accurately reflect the method.

## Score and Decision

**Calibration anchors** (paths truncated for brevity):

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| `wJ3GeGLFmc.md` (Sub-8-bit Integer Training, FQT) | 4.50 | Similar topic, comparable quality. This paper has more audacious goal (1-bit avg vs 4-bit) but larger accuracy drops and narrower scope (transfer only). Slightly stronger in novelty but weaker in practical results. |
| `Dm4qrBuFKH.md` (Binary NNs in Binary Space) | 4.67 | Comparable quality. Both explore extreme low-bit regimes; this paper has broader experiments (vision+NLP) and hardware speedups, but the other paper has a cleaner theoretical framing. |
| `lGUyAuuTYZ.md` (BNN+SNN Best of Both) | 5.67 | Stronger paper overall. More complete experimental validation and smaller accuracy gaps. This paper's hardware implementation is a point in its favor, but the experimental results are weaker. |
| `MiPyle6Jef.md` (QP-SNN, Quantized+Pruned SNN) | 6.75 | Significantly stronger. Thorough experiments, clear ablation studies, and SOTA results. This paper does not reach that bar. |
| `eqKHuxIpp5.md` (On-Device Transfer Learning) | 2.50 | Much weaker paper. Narrow scope with trivial experiments. This paper is substantially stronger in method depth and experimental breadth. |

This paper explores a genuinely interesting question (how low can FQT go?) and contributes a clever algorithm with real hardware acceleration. However, the contributions are substantially weakened by (a) the restriction to transfer learning only, (b) accuracy drops of ~5-10% that limit practical deployment, and (c) the absence of comparison with the 4-bit FQT methods the paper claims to advance beyond. The method is interesting but not yet compelling enough for acceptance at a top venue.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
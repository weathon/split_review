Now I have a thorough understanding of the paper and all the claims. Let me construct the final consolidated review.

---

## Summary

This paper introduces Overflow-Aware Activity Regularization (OAR), a novel regularization technique that mitigates numerical overflow in quantized RNNs evaluated under the CGGI homomorphic encryption scheme. By penalizing pre-activations that lie in "incorrect" overflow regions (where the sign flips modulo the message space), OAR recovers accuracy lost due to overflow while maintaining the efficiency of single-ciphertext representations. The authors demonstrate a 1.9M-parameter RNN evaluated over encrypted MNIST in 2.1s with 90.82% accuracy — a 274× latency reduction over prior work — and show that OAR improves accuracy by up to 71 percentage points in low-bit-width settings.

## Strengths

- **Novel, well-motivated regularizer that directly addresses a real bottleneck.** The OAR design follows from two crisp observations about overflow in ℤₖ (Section 3), and the piecewise hat-function penalty is mathematically tailored to the structure of the sign function under modular arithmetic. This is not a generic regularizer applied ad hoc; it is derived from first-principles analysis of the CGGI message space.

- **Dramatic empirical improvement validated across multiple dimensions.** At 5-bit precision, OAR improves top-1 accuracy from 0% to 71.39% (Table 1). The encrypted evaluation achieves 90.82% accuracy with only a 0.17% drop from plaintext — a vast improvement over the 25% drop reported in Anonymous [2025]. The ablation across bit-widths 4–8 and regularization rates (Table 2) demonstrates that the improvement is robust and tuning-dependent in expected ways.

- **New state-of-the-art for encrypted RNN inference.** The 2.1s latency with 1.9M parameters on encrypted data represents a 274× improvement over SHE [Lou & Jiang, 2019] despite a 10× increase in parameter count and 3× more layers. The scaling experiment (8.48M parameters, 128 timesteps) confirms that OAR enables larger models than previously feasible.

- **Empirical verification of the mechanism.** The pre-activation histograms (Figure 4) and the OAR metric (percentage of pre-activations in correct regions) confirm that OAR operates via the intended mechanism — shifting values into correct overflow regions — rather than acting as an unexplained implicit regularizer. The error metrics (Table 4) further validate that encrypted computation closely matches plaintext.

## Weaknesses

### Fatal
None.

### Major
- **Evaluation limited to MNIST, creating a gap between motivating applications and evidence.** The abstract and introduction motivate the work with "speech recognition and financial forecasting," but the only evaluation is on MNIST (image-based RNN classification). While MNIST is the standard benchmark in the CGGI neural network literature and the paper does demonstrate scaling to larger variants of this task, the motivating applications involve natural sequential data (audio, text, financial time series) with different distributional properties. Testing on at least one naturally sequential task (e.g., text classification on IMDB, a speech command task) would substantiate the claim that OAR benefits "large-scale RNNs" for the stated application domains rather than just for image-based RNNs. The enlarged RNN experiment (resized MNIST to 128×128, increasing timesteps to 128) tests scale but not task diversity.

### Minor
- **OAR and ModSign contributions are not independently ablated.** The paper compares "with OAR + ModSign" vs. "without OAR + with ModSign" (Table 1), which isolates OAR's effect when ModSign is present. However, "with OAR + without ModSign" (using standard sign) is not tested. The paper states that "ModSign alone failed to produce a working quantized model" (line 113), but this only shows ModSign needs OAR — not whether OAR needs ModSign. An ablation would clarify whether OAR's benefit depends on the signed-conversion preprocessing or would transfer to the standard sign function used in Anonymous [2025].

- **Gradient behavior during training is not analyzed.** The OAR derivative is zero for correctly-positioned pre-activations and non-zero only in incorrect regions. As training progresses and more values enter correct regions, an increasing fraction of pre-activations receive zero OAR gradient, which could slow convergence or cause stagnation. The paper trains for 1000 epochs but does not report the fraction of pre-activations with non-zero OAR gradient over the course of training, nor compare convergence speed with vs. without OAR.

- **Training cost of OAR is not reported.** The paper does not report the additional memory, wall-clock time per epoch, or convergence speed incurred by computing OAR (which involves modular arithmetic and ReLU operations per layer). While the cost is likely modest, reporting it would strengthen the claim that OAR is practical.

- **Applicability to non-sign activation functions is not discussed as a limitation.** The OAR design is tightly coupled to the sign activation function (the "correct"/"incorrect" region analysis depends on sign flips). The paper does not state whether OAR extends to ReLU, tanh, or other activations, nor acknowledge this as a scope limitation.

### Trivial
None.

## Nice-to-Haves

- A scatter plot or correlation plot of OAR metric vs. accuracy across training epochs or across bit-widths would strengthen the causal claim that moving pre-activations to correct regions directly drives accuracy improvement.
- A simple fixed-point multi-ciphertext baseline on the same MNIST RNN (even if much slower) would provide a concrete Pareto frontier for the latency/accuracy trade-off being resolved.
- A brief discussion of the hat-function edge case (values at the exact center of an incorrect region receiving symmetric gradient pressure toward both neighboring correct regions) would show awareness of a corner case in the design.

## Removed Points

- **Anonymous [2025] verifiability gap (Harsh Critic's Critical Issue #2).** The reviewer questioned whether the baseline procedure can be independently verified because Anonymous [2025] is not publicly available. Per hard rule: any cited reference is assumed to exist. This criticism is removed.
- **Missing appendix content (encryption parameter sets in Table 5).** The reviewer noted that parameter details were not in the main text. Per hard rule: appendix content was stripped by the parser. Removed.
- **"Far from real-time requirements" sub-point.** The paper's title includes "Towards Practical" as a qualifier and never claims real-time processing. The broader point about limited evaluation scope is kept; this sub-point is removed as a strawman.

## Novel Insights

None beyond the paper's own contributions. The key insight — that overflow in modular arithmetic can be addressed by training pre-activations to lie in regions where overflow preserves the correct sign — is the paper's own. The reviews do not surface an unstated implication or reinterpretation of the results.

## Suggestions

1. **Broaden task evaluation.** Test OAR on at least one naturally sequential dataset (e.g., IMDB text classification, Google Speech Commands) to close the gap between the speech/finance motivation and the experimental evidence. Even a plaintext evaluation would help.
2. **Add the missing ablation.** Test OAR with the standard sign function (without ModSign) to disentangle the contributions of the two components.
3. **Report training overhead.** Include wall-clock time per epoch with and without OAR, and the fraction of pre-activations with non-zero OAR gradient during training.
4. **State limitations explicitly.** Add a paragraph noting that (a) OAR is designed for sign activations and likely does not directly transfer to other activation functions, and (b) the method is currently validated on image-based RNNs.

## Score and Decision

The paper makes a clear, novel contribution (OAR) that is well-motivated, correctly designed, and convincingly demonstrated within its chosen evaluation scope. The weaknesses are real — particularly the narrow task diversity relative to the breadth of the motivating claims — but none undermine the core contribution. The paper deserves acceptance and would be strengthened by the suggested revisions.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
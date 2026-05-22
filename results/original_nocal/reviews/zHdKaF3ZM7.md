## Summary

WARP (Weight-space Adaptive Recurrent Prediction) introduces a novel sequence modeling architecture where the hidden state is the *flattened parameters* of an auxiliary MLP, updated via a linear recurrence driven by input differences: θₜ = Aθₜ₋₁ + BΔxₜ. The root MLP then decodes this state to produce outputs. This formulation enables gradient-free test-time adaptation, in-context learning, and seamless integration of physical priors. Experiments span image completion, traffic forecasting, dynamical system reconstruction, multivariate time series classification, and in-context learning. The physics-informed variant (WARP-Phys) achieves order-of-magnitude improvements on synthetic dynamics, and the model is competitive across several UEA classification benchmarks.

## Strengths

1. **Novel and well-motivated architecture.** The idea of treating the weights of an auxiliary MLP as the hidden state of a linear recurrence (Eq. 1) is genuinely new. Distinguishing fast-changing weights (θₜ, updated via the recurrence without gradients) from slow-changing parameters (A, B, φ, fitted via backprop) is a clean design that conceptually unifies weight-space learning with linear recurrence. Figure 1's comparison against standard and linear RNNs clearly highlights the difference.

2. **Physics-informed variant delivers dramatic improvements.** WARP-Phys (Table 3) achieves MSE 0.03±0.04 on the MSD dataset — over 10× better than the next best model (Transformer 0.34±0.12) — and similarly large margins on MSD-Zero and SINE*. This directly supports the paper's claim that domain knowledge can be cleanly integrated into the root network to achieve qualitatively better out-of-distribution generalization.

3. **Broad empirical evaluation across diverse tasks.** The paper tests WARP on image completion (MNIST, CelebA), energy forecasting (ETT), traffic forecasting (PEMS08), synthetic dynamics (MSD, LV, SINE), UEA classification (6 datasets), and ICL — covering multiple modalities and difficulty levels. This breadth strengthens the case for the architecture's generality.

4. **Competitive classification results on multiple UEA benchmarks.** Table 4 shows WARP is top-three on 4 out of 6 UEA datasets (best on Ethanol 36.49% and Heartbeat 80.65%, second on SCP2, third on Motor). These results are against a strong set of modern baselines including S5, Mamba, S6, LRU, LinOSS, and NCDEs — demonstrating the model's practical utility despite its unconventional design.

## Weaknesses

### Major

1. **The computational cost of the transition matrix A is under-characterized, and D_θ is never disclosed.** Equation (1) defines A ∈ ℝ^{D_θ × D_θ}, which has D_θ² entries. With ~1.68M total parameters for MNIST, if A dominates the budget, D_θ ≈ 1300 — meaning the root MLP is very small (~1300 weights). The paper acknowledges this scaling limitation in Section 4.2 but never reports D_θ for any experiment, nor explains how A is factorized, compressed, or whether D_θ is actually small enough that the root MLP's capacity limits the expressivity claims. The conclusion's characterization of "high-dimensional weight space" and "infinite-dimensional RNN hidden states" is at odds with the implied parameter budget. The paper works on the experiments it runs, but a reader cannot assess how practical or scalable the approach is without knowing D_θ. *This does not invalidate the core architecture (small root MLPs can still be useful), but it undermines the paper's loftier claims.*

2. **The PEMS08 traffic result (Table 2, MAE 6.59 vs. best baseline 13.45) requires substantial clarification.** The improvement over GNN-based methods that explicitly use graph structure — without using graph structure — is so large (more than 2× better) that it demands careful validation. The paper states it uses "non-causal convolution" preprocessing (details in Appendix D, which is stripped from this version), and the baselines are taken from published numbers [62] without re-implementation. It is unclear whether data splits, normalization, evaluation protocols, and metric aggregation are identical. A result of this magnitude obtained under different preprocessing and without fair re-runs of baselines cannot be taken at face value as a valid comparison.

3. **Missing S4 baseline from CelebA image completion (Table 1).** S4 is included in the MNIST table and is one of the strongest baselines, yet it is absent from the CelebA table. Only GRU, LSTM, ConvCNP, and WARP are shown for CelebA. This omission weakens the completeness of the comparison. Additionally, the LSTM BPD of 3869 on CelebA (L=100) and the ConvCNP BPD of 39.91 (L=300) and 248.1 (L=600) are orders of magnitude above the other values in the table, suggesting numerical issues or suboptimal tuning of these baselines.

### Minor

4. **The in-context learning experiment (Section 3.4) is too limited to be compelling.** The task is a simple linear regression on 32 tokens with a cumulative-sum transformation. No baselines (linear regression, Transformer, or any other ICL-capable model) are compared. The claimed "sub-quadratic" advantage is stated but not quantified against any alternative. This experiment demonstrates the concept exists but does not provide evidence that WARP's ICL is meaningful or competitive.

5. **Classification performance is uneven and the "matches or surpasses SOTA" claim is stronger than the evidence supports.** On EigenWorms, WARP (70.93%) is substantially behind LinOSS (95.0%), S6 (85.0%), and LRU (85.0%). The paper's claim of "top three in 4 out of 6" is factually accurate, but "matches or surpasses SOTA" conflates being competitive overall with being best on individual datasets. The high variance on some baselines (e.g., Mamba on Worms: 15.8 std) also makes the significance of some rank positions unclear.

6. **The "self-decoding" framing is oversold.** The paper says θₜ "effectively decodes itself, saving on learnable parameter count." This is a property of any architecture where the decoder function has no learnable parameters of its own — it does not reduce the parameter count compared to a standard RNN whose decoder is a learned linear projection of the hidden state. The conceptual framing is interesting but the claimed parameter savings are not unique to this architecture.

7. **D_θ is never disclosed for any experiment.** This is a reproducibility concern. Without knowing the root MLP size, it is impossible to understand the actual model capacity at work, and a reader cannot reason about the trade-off between root network expressivity and A's quadratic cost.

### Trivial

8. The STDP analogy (Section 4.1) — connecting input-difference-driven weight updates to spike-timing-dependent plasticity — is a qualitative philosophical connection, not a rigorous one. It is presented as such, so it is not a flaw, but it adds little substance.

## Nice-to-Haves

- **Disclose D_θ for every experiment** and discuss how the root MLP's capacity interacts with performance. Show how performance and memory scale with D_θ, perhaps via an ablation.
- **Add S4 to the CelebA table** for a complete comparison.
- **Re-run or carefully validate the PEMS08 baselines** under the same preprocessing pipeline, or provide a simpler controlled baseline (e.g., a linear model with the same non-causal convolution) to isolate WARP's contribution.
- **Include a baseline comparison** in the ICL experiment (e.g., linear regression, a small Transformer) to contextualize the results.
- **Tone down abstract/conclusion claims** about "matches SOTA" to more precisely reflect where WARP leads and where it lags.

## Novel Insights

The most striking finding surfacing from these reviews is the tension between the paper's conceptual ambition and its practical parameter budget. The weight-space recurrence is genuinely novel, and the WARP-Phys results (10× improvement on MSD) are among the strongest physics-informed modeling results I have seen. Yet the A matrix's quadratic cost means the root MLP must be very small (≈1300 weights for a 1.68M total parameter count), which raises an unresolved question: is WARP's success driven by the weight-space recurrence formulation *per se*, or is it essentially a small MLP decoder with a linear state tracker that could be equivalently reparameterized? The strong physics-informed results suggest the formulation genuinely matters, but the paper does not provide the controlled analysis needed to cleanly separate these interpretations.

## Suggestions

1. **Disclose D_θ for every experiment** and discuss the practical root-MLP size. This single change would resolve the most significant epistemic gap in the paper.
2. **Add a controlled ablation**: compare WARP against a model with the same total parameter budget but where A is replaced by a lower-dimensional linear RNN (state size k << D_θ) with a learned decoder up-projecting to D_θ. This would test whether the weight-space parameterization or just the extra parameters drive performance.
3. **For PEMS08**: either re-run baselines with the same pipeline, or run a simple model with the same non-causal convolution to establish a realistic baseline, so readers can calibrate the remarkable reported improvement.
4. **Add S4 to the CelebA table** to complete the comparison.
5. **Reframe the classification claim** in the abstract from "matches or surpasses SOTA" to the more precise "competitive with SOTA, achieving top-three on 4 of 6 UEA datasets."

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
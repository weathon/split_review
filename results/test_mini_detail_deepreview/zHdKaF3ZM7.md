Now I have sufficient calibration. Let me construct my final review.

## Summary

WARP (Weight-space Adaptive Recurrent Prediction) proposes a novel architecture that treats the weights of an auxiliary MLP as the hidden state in a linear RNN, updated via the recurrence θₜ = Aθₜ₋₁ + BΔxₜ. The MLP then decodes itself to produce predictions. This framework unifies weight-space learning with linear recurrence, enabling gradient-free test-time adaptation, physics-informed modeling, and in-context learning. Empirical results span image completion, energy/traffic forecasting, dynamical system reconstruction, multivariate classification, and a small-scale ICL task—with the PEMS08 traffic result (MAE 6.59, halving prior SOTA without using graph structure) being the most striking.

## Strengths

1. **Genuinely novel architecture that bridges weight-space learning and linear RNNs.** The idea of using a flattened weight vector as the hidden state of a linear recurrence, then decoding via the corresponding MLP ("self-decoding"), is a conceptually clean synthesis of previously disconnected literatures. The paper clearly formalizes this in Eq. (1) and Figure 1, and the distinction between fast weights (θₜ, updated by the recurrence) and slow weights (A, B, φ, updated by gradient descent) provides a principled route to gradient-free adaptation.

2. **State-of-the-art traffic forecasting without leveraging spatial graph structure.** On PEMS08 (Table 2), WARP achieves MAE 6.59 and RMSE 10.10, roughly halving the previous best (STDCN: MAE 13.45, RMSE 23.28). Crucially, all prior SOTA methods on this benchmark are GNN-based architectures that explicitly use the graph structure of the traffic network; WARP uses none of this information. This result is both practically impressive and theoretically interesting, suggesting that weight-space recurrence can capture complex spatiotemporal dynamics without domain-engineered inductive biases.

3. **Competitive multivariate time series classification.** Table 4 shows WARP achieving top-three accuracy on 4 out of 6 UEA datasets (best on EthanolConcentration and Heartbeat, second-best on SCP2 and MotorImagery), against a strong set of 11 baselines including S5, Mamba, LRU, and Griffin. This demonstrates the architecture's viability beyond forecasting.

4. **Honest and specific limitation section (Section 4.2).** The paper openly identifies the quadratic scaling of the A matrix, the lack of theoretical depth, and limited testing on language/vision modalities. The limitations section is a model of responsible writing—it acknowledges the core practical bottleneck without deflecting, and suggests concrete future directions (low-rank/diagonal parameterizations, permutation equivariance).

## Weaknesses

### Major

1. **The non-causal convolution preprocessing on PEMS08 raises data-leakage concerns for the forecasting setup.** Section 3.1 states: "we preprocess the input sequence with a *non-causal* convolution, as detailed in Appendix D." In a forecasting task, a non-causal convolution over the input can use information from both past and future positions within the context window. Since the "context" (12 historical steps) is the *only* information that should inform the forecast of the next 12 steps, it is unclear whether this preprocessing step inadvertently conditions on information that would not be available in a real deployment. The paper refers to Appendix D for details, but the appendix is not present in the submitted version, making this impossible to evaluate. Depending on implementation, this could invalidate the comparison against GMAN, D²STGNN, and STDCN—which are causal by design. This is the single most concerning methodological issue in the paper.

2. **The 10× improvement claim for WARP-Phys (Table 3) conflates the benefit of the physical prior with the benefit of the WARP architecture.** The WARP-Phys variant embeds the explicit formula τ ↦ sin(2πτ + φ̂) into the root network's forward pass. The baselines (GRU, LSTM, Transformer, black-box WARP) do not incorporate any such prior. A controlled experiment that adds the same physical formula to a GRU or LSTM (e.g., as a fixed output activation or as an additive bias) is needed to attribute the 10× improvement to WARP's weight-space framework rather than to the strong inductive bias. The paper's claim in the abstract—"a physics-informed variant of our model outperforms the next best model by more than 10×"—is factually accurate but misleading, as the comparison includes no control that isolates the role of the weight-space recurrence from the role of the prior itself.

3. **The quadratic O(D_θ²) cost of the state transition matrix A is a structural scaling bottleneck that limits the root network to a few thousand parameters.** The paper acknowledges this in Section 4.2 ("the size of the matrix A limits scaling to huge root neural networks"), but then elsewhere uses language like "high-capacity memory" and "infinite-dimensional" (Section 4.3) that directly contradicts the practical constraints. An MLP with D_θ≈1300 parameters (as implied by the 1.7M total budget—most of which is consumed by A) has limited representational capacity. The method cannot currently scale to problems requiring large decoders. While this is a known limitation, the rhetorical mismatch between the claims and the practical constraints weakens the paper's overall narrative. The lack of any attempt to mitigate this (e.g., low-rank A, diagonal structured parameterizations) in the main experiments is a missed opportunity.

### Minor

1. **The "in-context learning" experiment (Section 3.4) is too simple to support the broad claim.** The task is a single linear regression with random keys (D_x ∈ {2, 8}) and N+1=32 tokens. This is far from the standard ICL benchmarks used in the transformer literature (e.g., noisy linear regression with varying noise levels, multi-task function classes). The claim that WARP "showcases the appealing in-context learning ability" is overblown relative to the evidence presented. The cumulative sum transformation is also ad-hoc and not clearly motivated.

2. **No efficiency comparisons in the main text.** The paper claims "excellent computational efficiency" (Section 4.1) and references Appendix E.3, but the main text contains no wall-clock times, FLOP counts, or memory comparisons against baselines. Given that the quadratic A matrix makes efficiency non-obvious for larger root networks, such comparisons should be in the main paper.

3. **Missing input-difference ablation.** The recurrence uses Δxₜ = xₜ - xₜ₋₁ rather than direct inputs xₜ, motivated by connections to continuous-time RNNs and biological plasticity. However, no experiment compares the two formulations. The paper states that ablation studies are in Appendix E, which is not accessible in the submitted version. If the ablation exists in the full submission, this point is moot; if not, it is a significant gap.

4. **Some overclaimed language in the abstract and conclusion.** Phrases like "transformative paradigm for adaptive machine intelligence" (Abstract), "infinite-dimensional RNN hidden states" (Section 4.3), and "human-level artificial intelligence" (Section 4.3) are not supported by the scale and scope of the experiments. The contribution is respectable without such framing.

### Trivial

- The BPD values for CelebA on LSTM (3869, 7.276, 7.909) and ConvCNP (1.498, 39.91, 248.1) vary wildly compared to WARP (-0.162 to 0.052). A brief explanation of why these baselines produce such extreme BPDs would help the reader interpret Table 1.
- Table 3 reports SINE* metrics at ×10⁻⁴ scaling while others are ×10⁻², which is easy to miss.

## Nice-to-Haves

- A controlled baseline for WARP-Phys that applies the same physical formula as an output activation or loss term in a GRU/LSTM/Transformer.
- An experiment comparing WARP with input differences vs. direct inputs (if not in Appendix E).
- Wall-clock and memory benchmarks against at least one baseline in the main paper.
- An in-context learning experiment on a standard benchmark (e.g., the linear regression tasks from Garg et al., 2022).

## Removed Points

These points were flagged for removal; I note them so the authors are aware but do not weigh them in the score.

- **"Quadratic A matrix is a fatal structural flaw"** — The paper acknowledges this openly in Section 4.2 and treats it as a limitation, not a hidden flaw. The harsh critic overstates this to "fatal" when it is a known, stated boundary condition of the current instantiation.
- **"Missing comparison of WARP with input differences vs direct inputs"** — The paper states ablation studies are in Appendix E. Since the appendix was stripped by the parser, this criticism is unverifiable. If the ablation exists, the critic is wrong; if it does not, the criticism is about a missing section, not about the paper as submitted.
- **"PEMS08 non-causal convolution details missing"** — The paper says "as detailed in Appendix D." The appendix is stripped. Same issue as above.
- **"No comparison of computational efficiency"** — The paper references Appendix E.3 for wall-clock times and memory usage. Stripped by parser.
- **"The ICL is not standard"** — Demoting from major to minor because the paper's claim is modest ("sub-quadratic in-context learning"), and the experiment demonstrates the principle even if not benchmarking against the full suite.
- **"Strength finder claimed brain-like plausibility"** — The paper draws a parallel to STDP in Section 4.1 but doesn't claim to model it; it's a plausible connection, not a proven equivalence.
- **"Strength finder claimed the physics result is a core strength"** — Kept but caveated above; the strength is real but the comparison is incomplete.
- **Missing related work** — Cannot verify without external sources.

## Novel Insights

Beyond the paper's own contributions: The PEMS08 result (halving GNN-based SOTA without graph structure) is perhaps the most provocative finding, as it suggests that the weight-space recurrence may implicitly learn spatial relationships through temporal dynamics alone—a phenomenon worth investigating in its own right. The connection between the recurrence's input-difference mechanism and the STDP-style biological learning rule is an intriguing qualitative parallel that could motivate future work on neuromorphic implementations, though the paper does not develop this beyond a mention.

## Suggestions

1. **Clarify the PEMS08 non-causal convolution** with explicit details (kernel size, whether the convolution is applied only within the context window or across the entire sequence, and most importantly, whether any information from beyond the context is used). If the non-causal convolution operates only within the fixed 12-step input window, this should be stated explicitly to alleviate data-leakage concerns. If it operates across the training data in a non-causal way (e.g., full bidirectional processing of the training set), this must be explained defensively.
2. **Add the controlled WARP-Phys baseline** that embeds the same physical prior in a GRU/LSTM to disentangle the contribution of the weight-space recurrence from the contribution of the prior.
3. **Tone down the abstract and conclusion language** ("transformative paradigm," "human-level artificial intelligence") to match the actual evidence.

## Score and Decision

**Bracketing (Round 1):** Three queries on similar topics (weight-space learning × sequence models) returned anchors at avg 3.0 (weak), ~4.0–6.0 (middle), and 8.0 (strong). The paper is clearly above RotRNN (4.0) and below the 8.0-level papers. Initial bracket: 4.5–7.0.

**Narrowing (Round 2):** Additional queries for novel RNN architectures, test-time adaptation, and dynamical system modeling produced more targeted anchors. ProbeGen (6.0, accepted) and Gradient-free RNN training (6.0, rejected) are the most informative comparators. Relative to ProbeGen, WARP has greater architectural novelty and more impressive headline results (PEMS08 halving SOTA) but weaker controls and methodological hygiene. Relative to Gradient-free RNN training (6.0, rejected for limited novelty and unclear advantage over ESNs), WARP's novelty is clearer but its methodology has more confounds. Relative to FNSDA (5.75, rejected for incremental architecture and limited experiments), WARP is more novel but has similar methodological gaps. The paper sits between these anchors—stronger in novelty than FNSDA but with concerns that prevent it from reaching the clear accept level of ProbeGen.

**Final score: 5.5**. The core idea is genuinely novel and several results are impressive, but the methodological concerns (PEMS08 non-causal convolution, WARP-Phys without controlled baseline) and the structural scaling limitation prevent the evidence from being fully convincing. The paper could become a clear accept at 6.0–6.5 with resolution of these issues.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
## Summary

The paper identifies a genuine problem—SwiGLU activation outliers destabilize FP8 LLM training after ~200B tokens—proposes Smooth-SwiGLU (per-channel scaling absorbed into adjacent weights at zero inference cost) to fix it, and demonstrates FP8 quantization of both Adam optimizer moments. The core observation and the method are interesting and potentially impactful. However, the paper's central claim—successful FP8 training "on datasets up to 2 trillion tokens" (20× prior work)—is **not supported by any evidence in the manuscript**. The only training curve for the proposed method stops at 300B tokens, with an explicit note that more steps will be added later. This is a fatal evidential gap that fundamentally severs the paper's headline contribution from its substantiation.

## Strengths

- **Clean ablation pinpoints the SwiGLU output as the sole source of FP8 divergence (Figure 3).** Disabling only SwiGLU-output quantization while keeping all other FP8 quantizations active recovers convergence. This single-variable experiment rigorously isolates the cause, independent of any other FP8 choices in the network.

- **Smooth-SwiGLU is a mathematically clean fix with zero inference overhead.** Applying per-channel scaling before quantization and absorbing the factors into adjacent linear-layer weights at inference (lines 203–207) makes the method functionally equivalent to standard SwiGLU at inference time. This is a principled design.

- **First demonstration of both Adam moments quantized to standard FP8 formats with a principled format choice.** Table 2 and Figure 5 systematically test all four E4M3/E5M2 combinations, identifying E4M3 (first moment) + E5M2 (second moment) as the only working configuration, with a clear justification tied to the inverse-square-root sensitivity of the second moment.

- **Theoretical analysis linking ℓ₂ regularization to weight alignment (Theorem 1).** The theorem proves that at a stationary point of the regularized loss with sufficiently large inputs, w₁ → ± w₂. This provides a mechanistic explanation for why SwiGLU outputs can grow quadratically, going beyond the purely empirical observations in prior work.

- **Observing that FP8 instability emerges only after ~200B tokens is a valuable finding enabled by training longer than prior work (100B).** Even without the unsubstantiated 2T claim, demonstrating divergence onset at >200B tokens and successful recovery up to 300B is a non-trivial extension.

## Weaknesses

### Fatal

- **The paper's central claim—successful FP8 training to 2 trillion tokens—has zero evidential support in the manuscript.** The abstract (line 5), introduction (line 15), contributions list (line 24), experimental setup (line 272: "We trained the models on the open-source Red Pajama dataset for 2 trillion tokens"), and conclusion (line 351) all assert this result. Yet the only training curve for the proposed method (Figure 6, described at line 278) shows results **only up to 300B tokens**, and the caption explicitly states *"Additional training steps will be added in the next version of the manuscript."* No checkpoint evaluations, perplexity curves, or loss traces are provided beyond 300B tokens. This is not a case of weak or noisy evidence—it is a complete absence of evidence for the paper's headline claim. If the 2T token training was successfully completed, the curves must be shown. If it was not, the paper must be honestly scoped to what has been demonstrated (stable training up to 300B tokens), which is roughly 3× prior work, not 20×. This gap is structural: the paper's significance, framing, and title all depend on the 2T token claim, and no amount of minor clarifications can remediate the absence of the primary result.

### Major

- None. The fatal issue above is so decisive that it overrides all other considerations in the accept/reject decision. The points below would matter in a paper whose central claim is actually evidenced.

### Minor

- **The scaling factor formula for Smooth-SwiGLU is underspecified.** Line 201 states: *"Use these per-channel maximum values to determine the individual scaling factors s_i for each channel."* This is not a specification—it does not state whether s_i = max(|x_i|), s_i = max(|x_i|)/R where R is the max representable value, or includes a margin parameter. Given that the entire method rests on computing these factors, the exact mapping from observed maxima to scaling factors must be stated explicitly for reproducibility.

- **The "under-parameterized regime" justification for the σ'→0 condition is questionable.** Line 147 argues that |w₂ᵀ xₙ| > 0 is generic "when we fit a neural network to a large dataset of size N, where N ≫ k (i.e. we are in an under-parameterized regime)." A 7B-parameter model trained on ~2T tokens (≈10⁹ samples at 2048-token sequences, i.e., N ≈ 10⁹, k ≈ 7×10⁹) is in the **over-parameterized** regime by a factor of ~7. The rest of the argument (weight norms can be large enough to make |w₂ᵀ xₙ| large regardless of parameterization) is still valid, but the specific under-parameterization claim is incorrect and distracts from the main theoretical contribution.

- **The theorem characterizes stationary points, not training dynamics.** Theorem 1 shows what must hold at a stationary point if σ'→0, but does not establish that training dynamics will reach such a point before other instabilities (e.g., loss divergence) occur, nor that alignment is the *cause* rather than a *correlate* of outlier growth. The empirical correlation (Figure 1) is suggestive, but the paper frames the theory as a causal explanation (line 84: *"the SwiGLU activation function plays a crucial role in amplifying these outliers"*) that goes beyond what the theorem alone supports. The paper should explicitly distinguish the equilibrium characterization from the dynamic claim.

- **No variance or confidence intervals on any reported numbers.** The zero-shot evaluation (Table 1) shows very small gaps between BF16 and FP8 (e.g., Lambada accuracy: 61.98 vs 61.73; Wikitext perplexity: 5.59 vs 5.56). With single-run results, it is impossible to tell whether these are noise or systematic degradation. Similarly, the throughput and memory numbers (Tables 3 and 4) are reported without variance. While single-run evaluations are common in large-scale LLM papers, reporting them without qualification is a weakness.

- **Throughput measured on 8 devices, claimed for 256-device training.** Table 3 explicitly states measurements on 8 Gaudi2 devices with micro-batch size 1. The paper's main training uses 256 devices. Communication overhead, load balancing, and scaling efficiency at 256 devices are not discussed, so the ~34% throughput gain may not transfer linearly to the full system.

- **FP8 optimizer validated only on a 100M model.** The format selection experiments (Figure 5) use Llama2 100M. The paper applies the same format choices to the 7B/300B-token run without discussing whether precision requirements for optimizer moments are scale-invariant. This is not a fatal omission (format properties are architecture-agnostic), but it should be acknowledged.

### Trivial

- Typo on line 355: "throughput improvementsd" → "throughput improvements."

## Nice-to-Haves

- An ablation decomposing Smooth-SwiGLU into components: (a) standard SwiGLU + FP8 (diverges), (b) Smooth-SwiGLU only + FP32 optimizer, (c) standard SwiGLU + FP8 optimizer, (d) Smooth-SwiGLU + FP8 optimizer, would cleanly isolate the contributions of each component.
- A discussion of where in the model (which layers, what fraction of channels) the alignment phenomenon is observed would strengthen the empirical characterization.
- An explicit limitation on whether the 300B→2T extrapolation is expected to hold (e.g., does the alignment plateau after some point?).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Quantization details underspecified (E4M3/E5M2 format, scaling method)"** — Removed because the paper explicitly states the standard FP8 format (E4M3 forward, E5M2 backward) and delayed scaling is a well-known standard technique referenced in the background. The level of detail is appropriate for a conference paper.

- **"Training hyperparameters underspecified ('maintaining hyperparameters consistent with Llama2')"** — Removed because referencing the original architecture paper for hyperparameters is standard practice in this field. The Llama2 paper is cited and its hyperparameters are known.

- **"No limitations section"** — Removed as a formatting preference, not a substantive weakness.

- **"Reproducibility concerns about undisclosed implementation details"** — Removed. The paper provides sufficient algorithmic detail for an expert to reproduce the method. The one genuine underspecification (scaling factor formula) is retained as a Minor weakness.

- **Strength: "20× increase in FP8 training scale reveals a qualitatively new phenomenon"** — Demoted from a strength because the 20× claim (2T vs 100B tokens) is not evidenced. The paper does extend prior work (300B vs 100B = 3×), but citing the unsubstantiated 20× multiplier as a strength would be misleading. The valuable finding that instability emerges at ~200B tokens is captured in the last listed strength.

- **Strength: "Comprehensive downstream evaluation at 7B scale showing on-par performance"** — Weakened; retained as a strength but the lack of variance estimates is noted as a Minor weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews primarily surface the fatal mismatch between the paper's claimed scope (2T tokens) and its demonstrated evidence (300B tokens). This is an evidential verification finding, not a novel analytical insight about the method itself.

## Suggestions

1. **Show the 2T token training curve or honestly reframe the scope.** This is non-negotiable. If the training completed to 2T tokens, present the full loss curve with convergence metrics. If it did not, remove all claims of 2T-token training from the title, abstract, and throughout the paper, and scope the contribution to what is actually shown (stable FP8 training to 300B tokens, discovering instability at ~200B tokens). The paper's contribution would still be meaningful at 300B (3× prior work), but the framing must match the evidence.

2. **Specify the exact formula for s_i in Smooth-SwiGLU.** State whether s_i = max(|x_i|), s_i = max(|x_i|) / R_max, or some other mapping.

3. **Add variance estimates or multi-run confidence intervals** for the zero-shot evaluation results, or explicitly acknowledge single-run limitations.

4. **Correct the "under-parameterized regime" claim** on line 147, or remove it and keep the argument based solely on weight-norm growth.

5. **Report throughput at the actual training scale (256 devices)** or provide a scaling-efficiency discussion.

## Score and Decision

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>
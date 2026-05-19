- Decision: Reject
- Avg Score: 3.00
- Scores: 1, 3, 5
Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper proposes VCDC (Variational Diffusion Channel Decoder), which integrates belief propagation (BP) message updates into the reverse process of a variational diffusion model for channel decoding. The key idea is to replace the heavy neural network backbone of diffusion-based channel decoders with a lightweight, shared-weight belief propagation block repeated across timesteps. Compared to SOTA neural decoders (DDECC, HGN), VCDC achieves 3–5 orders of magnitude fewer FLOPs and 500–1000× smaller model size while reporting the best bit-error-rate among compared methods on several codes (Polar, LDPC, Mackay, CCSDS).

## Strengths

1. **Order-of-magnitude computational and memory savings are well-documented.** Tables 3 and 4 report concrete FLOPs and model size numbers showing VCDC uses 0.066K FLOPs for Polar(128,64) vs 5.58M (HGN) and 1.68G (DDECC-Max), with model sizes of 0.088KB vs 47.7KB (HGN) and 89.9KB (DDECC). These savings directly support the paper's central claim.

2. **Competitive BER results are reported across multiple codes and SNRs.** Table 2 shows that VCDC achieves the highest negative log BER among all compared methods for Polar(128,64), Polar(128,96), LDPC(121,60), Mackay(96,48), and CCSDS(128,64) at 4, 5, and 6 dB CSNR. The paper also honestly reports that VCDC at timestep 1 is worse than BP, establishing that the improvement comes from multi-step refinement.

3. **The integration of BP into the diffusion reverse process is clearly novel.** Section 4.2 reformulates the BP check-node update as a lightweight, weight-shared neural layer (Eq. 9: \(\mathbf{x} \leftarrow \mathbf{x} + f(\mathbf{w}, \mathbf{x})\)) and embeds this into the VDM-style forward/backward process. This design directly enables the stated cost-performance trade-off.

4. **CPU-only training feasibility is a concrete practical advantage.** The paper reports 1–3 hour training on an AMD EPYC CPU (Section 5), establishing that the approach does not require GPU infrastructure, which is notable for the application domain.

5. **The choice of 20 reverse timesteps is motivated.** The paper observes that performance saturates well before the \(N-K\) bound used by prior work (DDECC), and Table 1 tracks BER improvement across timesteps to support this design choice.

## Weaknesses

### Fatal

None.

### Major

1. **Training loss is never explicitly stated for VCDC.** The paper describes binary cross entropy as the general decoding objective in Section 2 (related work) but never specifies the actual loss function used to train VCDC. Without this, the training procedure is underspecified and the connection to the "variational diffusion" framing is incomplete—the paper does not train with an ELBO or any VDM-specific objective, so it is unclear what "variational" means operationally.

2. **No ablation isolating the contribution of the diffusion schedule.** The model uses 20 different CSNR levels in the forward process and a corresponding reverse schedule. Without a comparison to the same architecture with a fixed CSNR (no diffusion schedule), it is impossible to tell whether the diffusion process itself provides any benefit over simply running the shared-weight BP block for multiple passes at a single SNR. The method may just be "repeated neural BP with a noise curriculum"—which could still be a contribution, but the paper's framing as a diffusion model requires this ablation.

3. **No comparison to a simple iterative neural BP (NBP) baseline.** The paper compares to HGN (a hyper-graph neural network) and DDECC (transformer-based), but not to a straightforward learned-weight BP of comparable depth and parameter count. This is the direct algorithmic predecessor. Without this baseline, the benefit specifically attributable to the diffusion framing (vs. learned iterative BP) cannot be assessed. The paper claims "first to integrate BP into diffusion models" but cannot demonstrate that the diffusion integration matters more than the weight-sharing and iterative refinement.

4. **BER results lack confidence intervals or variance estimates.** Table 2 reports point estimates for negative log BER at very low error rates (down to \(10^{-7}\)), where sampling variance can be substantial. The paper states "evaluation only stops with at least 100 error samples detected," but does not report how many test samples were required, whether this condition was met for all models and SNRs, or provide any uncertainty quantification. This makes it difficult to assess whether the reported advantages are statistically significant.

5. **Early stopping mechanism creates an unacknowledged asymmetry.** VCDC uses parity-check-based early stopping ("Whenever the parity check error count goes to zero, the reverse process stops for the input sample"). This halts the process as soon as a valid codeword is reached, effectively forcing the output to satisfy parity constraints. The paper does not state whether baselines (HGN, DDECC, BP) also use early stopping. If they do not, this gives VCDC an advantage independent of the learned model, and the BER comparison is confounded.

6. **The CSNR schedule (20 discrete values between 4–6 dB) is not specified.** The paper derives the decreasing-CSNR requirement for the forward process (Section 4.1) and states "we limit our reverse process up to 20 timesteps," but never specifies what the 20 CSNR values are (linear in dB? uniform in \(w_s\)? equally spaced?). This omission prevents reproducibility of the reverse process.

### Minor

1. **Terminology confusion in Table 1 description.** The caption says "Negative natural logarithm BER results" (higher is better), but the text says "The first timestep is with the smallest BER, and BER can increase by adding more reverse steps." "BER" switches between referring to the actual error rate and the negative log value without clarification, making the interpretation of Table 1 unnecessarily difficult.

2. **The "variational diffusion" framing is largely decorative.** The reverse process skips noise addition (following Choukroun & Wolf 2023), making it deterministic. The training is not done with an ELBO. The forward process is simply a sequence of AWGN channels at different SNRs. The actual decoder is a weight-shared neural BP block. While the VDM framework provides the flexibility to model AWGN at different SNRs as the forward process, the paper does not leverage any of the theoretical machinery of VDMs (e.g., ELBO-based training, noise schedule optimization). This framing overclaims relative to what is operationalized.

3. **No discussion of code/rate generalization.** The model is trained separately for each code configuration and SNR range (4–6 dB). The paper does not discuss whether the tiny model can be adapted to new codes or different rate regimes without full retraining, which is relevant for practical deployment.

### Trivial

None.

## Nice-to-Haves

- Compare BER of DDECC and HGN at a matched number of timesteps/layers (e.g., 20) to assess whether VCDC's cost-performance advantage holds when the depth budget is equalized.
- Ablate the number of layers per block (\(N-K\)) vs. the number of timesteps to understand the depth-vs-iterations trade-off.
- Report wall-clock time or latency in addition to FLOPs, since the sequential 20-step reverse process may limit throughput.

## Removed Points

These points were removed from the harsh critic's review because they are speculative, factually incorrect, or violate the filtering rules:

- **"BER claims are not credible; results look like an artifact"** — Removed. This assertion about the results being "not credible" or an "artifact" is speculative and unsubstantiated from the paper as written. The paper does show that VCDC at timestep 1 is worse than BP, establishing a baseline, and the improvement with timesteps is tracked in Table 1. The critic provides no specific evidence of artifact beyond supposition about early stopping (which is a legitimate algorithmic component, not a confound when acknowledged).
  
- **"FLOPs comparison is misleading because DDECC may work with fewer steps"** — Weakened and moved to Nice-to-Haves. The paper already provides a DDECC-1 column (single step), and even there VCDC's 20-step FLOPs are far lower. The 1000× claim is conservative for many settings. However, it would strengthen the paper to check DDECC at 20 steps, so this is a nice-to-have.

- **"Prior low-cost neural decoders not discussed"** — Removed per rule: missing related works should not be mentioned.

- **"Did authors actually meet the 100-error-sample condition?"** — Removed. Speculative; the paper states the protocol clearly.

- **Formatting/style nitpicks** — Removed as parser artifacts or outside scope.

## Novel Insights

None beyond the paper's own contributions. The reviews converge on the paper's two key claims (very low cost + competitive BER) and mainly differ on how carefully those claims are evaluated. The harsh critic correctly identifies that the paper lacks critical ablations and baseline comparisons that would isolate the source of improvement. The strength-finder correctly identifies that the cost numbers are well-documented and impressive. Neither review surfaces an insight about the method that goes beyond what the authors themselves state.

## Suggestions

1. **Explicitly state the training loss** for VCDC (Section 4.2 or 5). If it is binary cross-entropy on the final decoded bits (the standard approach for neural decoders), say so.
2. **Add an ablation** comparing VCDC's 20-step varying-CSNR schedule to the same architecture with a fixed CSNR (e.g., all steps at 6 dB). This is the minimal experiment to show the diffusion schedule matters.
3. **Compare against a simple learned-weight NBP** baseline with the same number of iterations and weight-sharing scheme but without the diffusion schedule. This isolates the contribution of the VDM framing.
4. **Add confidence intervals or standard deviations** to Table 2 BER results, especially at high SNRs where error counts are small.
5. **Clarify the early stopping protocol**: state whether baselines also use parity-check early stopping, and if not, acknowledge this asymmetry in the comparison.
6. **Specify the 20 CSNR values** used in the forward process (linear spacing? uniform in \(w_s\)?) so the schedule can be reproduced.

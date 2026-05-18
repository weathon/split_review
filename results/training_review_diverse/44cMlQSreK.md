Now I have thoroughly verified all claims. Let me produce the final consolidated review.

---

## Summary

This paper introduces NeuroQuant, a post-training quantization (PTQ) framework for variable-rate implicit neural representation video coding (INR-VC). The core idea is to avoid retraining separate weights for each target bitrate by instead adjusting quantization parameters of pre-trained weights via (1) mixed-precision bit allocation guided by a Hessian-vector product sensitivity criterion (Ω), and (2) network-wise QP calibration. The paper provides a theoretical analysis of why traditional diagonal-Hessian methods fail for non-generalized INR-VC (inter-layer dependencies, anisotropy) and demonstrates state-of-the-art results across multiple INR-VC architectures, achieving up to 7.9× encoding speedup and >3dB gains at low bitwidths over existing quantization approaches.

## Strengths

- **Novel sensitivity criterion that addresses shortcomings of prior Hessian-based criteria for the INR-VC setting.** The paper demonstrates via Examples 1 and 2 that eigenvalue/trace-based criteria fail when inter-layer dependencies and anisotropy exist, which is characteristic of non-generalized INR-VC. The proposed Ω = Δw^T H^(w) Δw captures both off-diagonal Hessian structure and weight perturbation direction, with a practical Hessian-vector product approximation (Eq. 10) that avoids explicit Hessian construction. This is theoretically and empirically well-motivated.

- **Network-wise calibration and channel-wise quantization tailored to non-generalized INR-VC.** The paper identifies that layer/block-wise calibration (standard in generalized networks) is suboptimal for INR-VC due to strong cross-layer dependencies, shown empirically in Figure 3(c). It derives a unified MSE-oriented calibration objective (Eq. 15) and implements network-wise calibration. The channel-wise quantization accounts for the heterogeneous weight distributions across channels (Fig. 3a-b).

- **Strong empirical results demonstrating practical variable-rate INR-VC without retraining.** NeuroQuant achieves up to 7.9× encoding speedup (Table 2) compared to retraining for new bitrates, and outperforms existing PTQ methods (AdaRound, BRECQ, QDrop, RDO-PTQ) and QAT methods (FFNeRV, HiNeRV) across multiple architectures and bitwidths (Table 1, Figure 4), including >3dB gains at low bitwidths and 4.8% BD-rate improvement over HiNeRV's built-in QAT.

- **Systematic analysis of why traditional quantization assumptions fail for INR-VC.** The paper provides concrete counterexamples (Example 1 inter-layer dependencies, Example 2 perturbation direction effects) and empirical evidence (Figure 2) showing that layer independence and isotropy assumptions break down for non-generalized INR-VC, justifying the need for the proposed approach.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are supported by the evidence presented. No weakness fundamentally invalidates the results or the contribution.

### Minor

- **Overclaimed "optimality" of the sensitivity criterion in Theorem 1.** The paper calls Ω the "optimal sensitivity criteria" but the justification is simply the second-order Taylor expansion showing that Ω captures loss degradation (Eq. 11). This demonstrates that Ω is an *accurate* measure of sensitivity, but the paper does not formally prove that optimizing bit allocation via Ω (under a rate constraint) yields a theoretically optimal bit assignment. The term "optimal" is unnecessarily strong; "complete" or "second-order accurate" would be more precise. This does not undermine the practical value of Ω, which demonstrably outperforms simpler criteria.

- **The bit allocation search algorithm used in experiments is not specified.** The paper mentions "integer programming, genetic algorithms (Guo et al., 2020), or iterative approaches" (line 127) as possible techniques but never states which one was actually implemented. This is a reproducibility gap. The authors should specify the exact search procedure and its computational cost.

- **Missing controlled ablation on calibration granularity.** The paper argues that network-wise calibration is necessary for INR-VC (Sec. 3.2), but the experimental comparison (Table 1) compares NeuroQuant against methods that differ in calibration granularity *and* other aspects (diagonal Hessian approximations, rounding procedures). A controlled ablation varying only the calibration granularity (network-wise vs. block-wise vs. layer-wise) within the same optimization framework would more cleanly isolate the effect of granularity.

- **Comparison against QAT baselines conflates mixed precision with PTQ.** NeuroQuant uses mixed precision (Table 1, marked with *), while the QAT baselines (FFNeRV, HiNeRV) use uniform precision. Part of the >3dB gain at low bitwidths may come from mixed-precision flexibility rather than from PTQ calibration. A comparison against a mixed-precision QAT baseline (or an ablation holding bitwidth allocation constant) would clarify the source of improvement. (The paper's overall claim — "NeuroQuant outperforms baselines" — is not invalidated, but the attribution of gains is ambiguous.)

- **Encoding time comparison (Table 2) does not account for the mixed-precision search overhead.** Table 2 reports the calibration time for NeuroQuant but does not include the time required for the bit allocation search. If the search cost is non-negligible, the "up to 7.9× speedup" figure may overstate the practical advantage. The authors should report the total end-to-end cost (search + calibration).

### Trivial
- The paper does not compare against general mixed-precision PTQ methods (e.g., HAWQ-V2). While such methods assume layer independence and would likely underperform on INR-VC (as the paper argues), demonstrating this would strengthen the paper. This is a nice-to-have rather than a required comparison.

## Nice-to-Haves

- A controlled ablation comparing bit allocations from the proposed Ω criterion against allocations from trace-based or eigenvalue-based criteria using the same search algorithm, to directly test whether the off-diagonal and directional information contributes empirically.
- A comparison against a mixed-precision QAT baseline to disentangle the benefits of mixed precision from the benefits of PTQ calibration.
- Adding the mixed-precision search time to the encoding time comparison.

## Removed Points

The following reviewer criticisms were removed per the hard rules:

- *"The results in Table 1 are partially garbled in the provided text"* — This is a parser artifact introduced during PDF extraction, not an error in the original paper.
- *"The uniform distribution assumption is only valid when the quantization step s=1"* and *"the overhead defeats the purpose"* — The U(-0.5, 0.5) assumption is standard in the quantization literature (Ballé et al., 2017) and is used to justify the straight-through estimator approximation, not to actually sample Δw values. Computing Δw for a candidate bitwidth is simply quantize-and-subtract, which is trivially cheap. The critic's concern about overhead is not well-founded given the linear-time computation described.
- *Missing appendix / proofs in appendix complaints* — The parser strips appendix content from all papers; nothing suggests the original submission lacks these.

## Novel Insights

The reviewer observes something not fully articulated by the paper itself: the paper's framing of variable-rate INR-VC as a mixed-precision PTQ problem is interesting because it inverts the typical logic of neural compression. Normally, variable-rate is handled at the *training* stage (e.g., with Lagrange multipliers swept across runs, or with conditional models). Here, the authors treat quantization precision as the *only* degree of freedom and show that for INR-VC (where each video is a unique network), this is sufficient to cover a meaningful range of rate-distortion points. This suggests a different perspective on the INR-VC pipeline: the heavy lifting (learning the video representation) is done once at high precision, and the rate-distortion frontier is explored entirely in the *quantization* stage. This distinction could inform future INR-VC system design beyond the specific PTQ method.

## Suggestions

1. **Replace "optimal" with "second-order accurate" or "complete"** in the statement of Theorem 1, or provide a formal argument for bit-allocation optimality under a rate constraint.
2. **Specify the bit allocation search algorithm** used in experiments (which of the mentioned techniques was actually implemented) and report its computational cost.
3. **Add a controlled ablation** comparing network-wise, block-wise, and layer-wise calibration within the same optimization framework.
4. **Report total encoding time including search overhead**, or clarify that the search time is negligible and provide its measured cost.
5. **(Nice-to-have) Add a comparison against a mixed-precision QAT baseline**  or an ablation controlling for bitwidth allocation to clarify attribution of gains.

## Score and Decision

The paper tackles a practically important problem (efficient variable-rate INR-VC), provides a well-motivated method with a clear theoretical rationale, and supports it with strong empirical results across multiple architectures and baselines. The weaknesses are minor and addressable — overclaimed optimality, missing ablation details, unspecified search algorithm — and do not threaten the core contribution. The encoding speedup and compression efficiency gains are substantial and practically meaningful.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
## Summary

This paper proposes DuaRot, a method for improving rotation-based outlier mitigation in quantized LLMs. Two main ideas are introduced: (1) a **dual rotation** approach where a global rotation matrix ($R_G$) and a block-diagonal local rotation matrix ($R_L$) are trained jointly but merged into a single orthogonal matrix at inference, adding zero computational overhead; (2) a **hardware-aware matrix configuration strategy** that decides whether to keep online rotation matrices as fast Hadamard transforms (using WHT) or expand them into trainable parameters (using Matmul), based on runtime benchmarks on the target hardware. Experiments on LLaMA2/3 and Mistral models show consistent perplexity improvements over SpinQuant, particularly under RTN quantization (e.g., 0.51 PPL improvement on LLaMA3-8B W4A4KV4).

---

## Strengths

1. **Clean, mathematically sound dual-rotation design with zero inference overhead.** The paper proposes a reparameterization where $R_G$ (full-dimension rotation) and $R_L$ (block-diagonal local rotation) are trained jointly but merge into $R = R_G R_L$ at inference, preserving orthogonality ($RR^T = I$, Eq 10, Section 3.2). This introduces no additional computation at inference time — a structurally clean advance over single-rotation methods like QuaRot/SpinQuant.

2. **Consistent and substantial PPL improvements under RTN quantization, where prior methods underperform.** Table 1 shows DuaRot achieves the strongest gains precisely in the RTN regime where SpinQuant struggles. Examples: 0.51 PPL gain on LLaMA3-8B W4A4KV4, 0.31 on LLaMA2-7B W4A4KV4. The method does not rely on GPTQ as a crutch.

3. **Component-level ablation that isolates each contribution.** Table 3 decomposes gains from (a) extending $R_4$ to trainable space (+0.44 PPL on LLaMA3-8B), (b) extending $R_3$, and (c) adding dual rotation. Each step is independently shown to be effective.

4. **Principled ablation of local rotation block size.** Figure 5 sweeps $d$ from 32 to 1024, identifies $d=64$ as optimal, and provides reasoning for the trade-off (too small concentrates outliers within groups; too large introduces training instability).

5. **Candid limitations section.** Section 6 honestly discusses training cost (LLaMA2-70B requires 4 A100 GPUs), Cayley optimization's limited exploration of the orthogonal group, and calibration dataset dependence. This transparency strengthens credibility.

---

## Weaknesses

### Fatal
None.

### Major

- **Speed claims are made repeatedly but only supported by microbenchmarks, not end-to-end measurement.** The paper states the method achieves gains "without compromising inference speed" (abstract, §1, §3.3, conclusion) and that the hardware-aware strategy "can help improve the model's speed during the decoding phase" (§4.3). However, no end-to-end latency or throughput measurement is provided for any quantized model. The only evidence is Figure 4, which compares WHT vs. Matmul runtime for individual matrix operations — a microbenchmark that ignores memory bandwidth contention, kernel launch overhead, fused kernel opportunities, and the cumulative effect across layers. Given that the paper itself states "both QuaRot and SpinQuant slow down inference speed for decoding stage" (§1), the burden is on the authors to show DuaRot does not share this problem. The microbenchmark does not establish that "the model's speed will not decrease" at the application level. This is a significant evidential gap for a claim that appears in the abstract, contributions list, and conclusion.

### Minor

- **The "hardware-aware" strategy is a fixed threshold measured on one GPU, presented as more general than it is.** Equation 11 defines the decision rule (trainable if online and $d \le 512$, otherwise Hadamard) based solely on benchmarks from an A100-SXM4-80GB. No cross-hardware validation is provided. The methodology itself is reasonable (benchmark on your target hardware), but labeling the resulting fixed threshold as a "hardware-aware strategy" rather than an "A100-derived rule of thumb" overstates the contribution. A truly hardware-aware strategy would provide an automated profiling method per deployment target.

- **Zero-shot accuracy degradation on LLaMA2-13B is acknowledged but not systematically analyzed.** The paper notes (§4.2) that on LLaMA2-13B W4A4KV16, DuaRot improves PPL but decreases zero-shot accuracy by 0.89 points (RTN) relative to SpinQuant. This is honestly reported, but the paper does not analyze whether this is a pattern or outlier across models and quantization settings. A per-task breakdown of accuracy deltas between SpinQuant and DuaRot would clarify whether the perplexity gains consistently come at the cost of reasoning accuracy in specific settings, or whether this is an isolated case.

### Trivial

- Table 2 (zero-shot accuracy) and Table 3 (ablation) are embedded as images rather than text, making precise verification of numbers against the prose claims difficult for the reader.

---

## Nice-to-Haves

- **End-to-end speed benchmarks** (addressing the major weakness above) would directly test the paper's own stated thesis. Measuring tokens/second or ms/token for DuaRot vs. SpinQuant vs. QuaRot on the A100 would resolve the central evidential gap.
- **Results on at least one 70B-class model** would strengthen the contribution, since outlier problems worsen with scale. The paper acknowledges training LLaMA2-70B is possible (4 A100s) but does not report results.
- **Analysis of what $R_L$ actually learns** — the local rotation matrix is initialized to identity, and Section 6 notes Cayley gradients remain near-identity. Measuring how much the block-diagonal elements deviate from $I$ after training would clarify whether the dual rotation contribution is driven by learned structure or primarily by the additional degrees of freedom in training.
- **Cross-hardware validation of the WHT-vs-Matmul crossover** on at least one other GPU (e.g., H100, A6000) would substantiate the "hardware-aware" framing.

---

## Removed Points

The following points from the reviewer inputs were evaluated and removed with justification:

- **"Only one random seed / no variance reported"** — Removed. Single-run evaluation without error bars is standard practice in LLM quantization benchmarks at this scale; not reporting variance does not constitute a weakness by the field's norms.
- **"Missing comparison with scaling-based methods in W4A8KV4"** — Removed. The paper explicitly scopes its comparison (§4.2, "Compare with Scaling-based Methods") and provides a quantitative justification (OmniQuant at 14.3 PPL vs. rotation methods at 6-8 PPL). The paper's focus is 4-bit activation quantization where scaling fails.
- **"Larger model results missing"** — Moved to Nice-to-Have above. The limitation is honestly acknowledged in Section 6.
- **"Reproducibility / undisclosed hyperparameters"** — Removed. The experimental setup (§4.1) is sufficiently detailed following SpinQuant's conventions.
- **Formatting/style nitpicks** — Removed per parser artifact rules.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface the core evidential gap (speed claims without end-to-end benchmarks) but raise no novel synthesis that the paper itself does not already contain or imply.

---

## Suggestions

1. **Add end-to-end latency/throughput measurements** for DuaRot vs. SpinQuant vs. QuaRot on the same A100 used for microbenchmarks. Report tokens/second for both prefill and decoding phases across at least one model size (e.g., LLaMA3-8B). This directly tests the paper's central secondary claim.
2. **Cross-validate the WHT-vs-Matmul threshold** on at least one other GPU generation (e.g., H100 or consumer GPU) and report whether $d=512$ is stable. If not, provide the per-device profiling methodology rather than a fixed threshold.
3. **Provide a per-task breakdown** of zero-shot accuracy deltas (SpinQuant → DuaRot) across all models and settings to clarify whether the LLaMA2-13B degradation is a pattern or an outlier.
4. **Add an analysis of $R_L$'s learned parameters** — e.g., the Frobenius norm distance from identity after training — to quantify how much the local rotation actually diverges from its initialization.

---

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
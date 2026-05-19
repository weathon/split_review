- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6
Now I have all the information needed. Let me synthesize the final review, carefully cross-checking every claim.

---

## Summary

SeedLM is a post-training LLM compression method that replaces each block of weights with a seed for an LFSR (Linear Feedback Shift Register) pseudo-random generator plus a few quantized coefficients. During inference, the LFSR reconstructs the weight matrix on-the-fly, trading increased compute for reduced DRAM reads. The method is data-free, requires no calibration, and the paper provides an FPGA prototype achieving ~4× speedup on matrix-vector multiplication. The core idea is novel and the hardware validation is concrete.

## Strengths

- **Novel LFSR-based weight generation enabling a compute-for-memory trade-off.** The idea of encoding weight blocks as seeds of a pseudo-random generator and reconstructing them via LFSR is original. The paper describes the full pipeline (Section 3.1–3.2): a maximal-length LFSR with a cached state table (~130 KB for K=16) generates random matrices on-the-fly, which are linearly combined with quantized coefficients. This is a genuinely different approach from standard quantization.

- **FPGA prototype with near-4× speedup on memory-bound operations.** Table 5 (Section 4.2) reports cycle counts for matrix-vector multiplication: a 2048×2048 matrix achieves 3.98× speedup (34,331 cycles vs. 136,559 for FP16), and a 1024×1024 matrix achieves 3.92×. The resource utilization is documented (67K LUTs, 45K FFs, 144 BRAMs for decompression), demonstrating feasibility in hardware. This is the paper's strongest concrete result.

- **Data-free compression with competitive absolute accuracy on Llama 3 70B.** SeedLM at 4-bits achieves a mean zero-shot accuracy of 78.06 on Llama 3 70B (FP16 baseline: 79.51, ~98.2% retention). At 3-bits it achieves 74.68. These raw retention numbers are genuinely good for a data-free method on the notoriously hard-to-compress Llama 3 70B, and they do not depend on baseline quality.

- **Systematic design-space exploration with explicit bit-budget constraint.** Section 3.4 formulates the effective bits-per-element equation \(M = (K+4+4P)/C\) and performs a grid search over (C, P, K) to find configurations minimizing reconstruction error on Gaussian vectors. This yields reproducible configurations (e.g., C=8, P=3, K=16 for 4-bit) and provides a principled framework for selecting hyperparameters.

- **Deterministic offline algorithm with no runtime data dependence.** Algorithm 1 enumerates all \(2^K-1\) seeds and selects the best via precomputed pseudoinverses. This makes the compression deterministic (no randomness in the results) and the decompression requires no calibration data or activation statistics at runtime, unlike all compared baselines.

## Weaknesses

### Fatal
None.

### Major

- **Baseline comparisons for AWQ and OmniQuant are not credible, undermining the central claim of outperforming SOTA.** The paper reports that AWQ 4-bit on Llama 3 70B achieves a mean zero-shot accuracy of only 72.34 (baseline 79.51), with a WinoGrande score of 60.54 (baseline 77.66). This is far below established AWQ results. Similarly, OmniQuant produces "inf" perplexity on Llama 3 8B and a mean accuracy of 33.45% on Llama 3 70B — essentially non-functional. The paper acknowledges deviating from standard configurations ("we use 4-bit integers with channel-wise scaling" for AWQ; "not performing fine-tuning" for OmniQuant and QuIP#), but the magnitude of degradation far exceeds what one would expect from these modifications alone. Since the abstract and introduction claim that SeedLM "achieves significantly better zero-shot accuracy retention at 4- and 3-bit than state-of-the-art techniques," and the headline Figure 1 depends on these very numbers, the central empirical claim is built on baselines that may be misconfigured. The authors need to re-run baselines using their standard recommended settings (group size 128 for AWQ, fine-tuning for OmniQuant) and either report those results or provide a convincing explanation for the anomalously low numbers.

### Minor

- **Design-space exploration uses Gaussian vectors rather than real LLM weights.** Section 3.4 selects hyperparameters (C, P, K) by minimizing reconstruction error on a "standard normal Gaussian vector." The paper acknowledges this assumption "may have its limitations" but does not validate the chosen configurations on actual weight distributions from even a single LLM layer. While the resulting configurations work in practice, the justification that they are optimal for real weights is weaker than if validated empirically.

- **Exhaustive seed search is computationally expensive, but no compression cost is reported.** Algorithm 1 enumerates all 65,535 seeds per weight block. For a 70B model with C=8, this is ~8.75 billion blocks × 65,535 evaluations each. The paper states that pseudoinverses are precomputed (6.3 MB) and the process is parallelized, but provides no wall-clock time, GPU hours, or discussion of whether this offline cost is practical for very large models. This makes it difficult to assess the method's practical usability.

- **Key experimental settings for baselines are underspecified.** The paper states it uses "default calibration sets from official repositories" but does not report calibration sequence length, number of calibration samples, or whether methods' built-in weight-only quantization pipelines were used as-is or modified. Given the anomalous baseline numbers, this missing transparency prevents independent verification of the comparison.

### Trivial

- The claim about being "first instance of achieving nearly identical accuracy with 4-bit compression on LLMs without data, using a deterministic offline algorithm" is too strong. Data-free post-training compression predates this work (e.g., Nagel et al. 2019, cited in the paper itself), and whether "nearly identical accuracy" is achieved depends on the baseline. Soften the phrasing.

## Nice-to-Haves

- **Ablation on P and K sensitivity.** How robust is accuracy to small changes in latent dimension or seed length (e.g., P=4 for 4-bit instead of P=3)?
- **End-to-end LLM inference speedup estimate.** The FPGA results are for a single matrix-vector multiply kernel. An estimate of wall-clock speedup for end-to-end generation (accounting for non-memory-bound operations and decompression pipelining) would strengthen the hardware claims.
- **Comparison with other data-free methods.** Since being data-free is a key selling point, comparing with RTN (round-to-nearest) or other data-free baselines would contextualize the results.
- **Memory footprint comparison.** Compute the total memory savings (e.g., 4× reduction) from the stored seeds + coefficients + exponents vs. FP16 weights, and compare with standard quantization formats.

## Removed Points

*These are points from the reviewers that were removed after verification against the paper.*

- **Harsh Critic: QuIP# can be run on 70B with CPU offloading or larger GPUs.** The authors used 8× A100 40GB GPUs, which is a standard setup. Suggesting they use different hardware is scope creep and does not reflect an error in the paper. *Removed.*

- **Harsh Critic: "The paper incorrectly claims 'first instance'" of data-free 4-bit compression.** The paper's claim is qualified: "To the best of our knowledge, this is the first time nearly identical accuracy has been achieved with 4-bit compression on LLMs without data, using a deterministic offline algorithm." The specificity ("nearly identical accuracy" + "deterministic offline algorithm") and the "to the best of our knowledge" qualifier make this defensible. Previous data-free methods cited in the paper did not achieve this accuracy level at 4-bit. *Removed.*

- **Harsh Critic: "Figure 1 is misleading if baselines are wrong."** This is derivative of the baseline concern already captured under Major weaknesses. It does not add an independent criticism. *Subsumed.*

- **Strength Finder: "Data-free compression outperforms calibration-data baselines on Llama 3 70B."** This conflicts with the verified baseline weakness. The strength about outperforming baselines cannot be taken at face value when the baselines are suspect. However, SeedLM's absolute retention (~98.2%) is still a strength, and this has been preserved in the Strengths section with appropriate phrasing. *Rephrased.*

## Novel Insights

The two reviewers disagree sharply on whether the baseline issue is fatal. The Harsh Critic treats it as decisive ("the paper should not be accepted"), while the Strength Finder accepts the comparison at face value. The truth is somewhere in between: the AWQ and OmniQuant numbers are anomalously low enough to warrant serious concern, and the central claim depends on them. However, the paper has genuine independent contributions — the LFSR-based methodology, the FPGA validation, and the data-free property — that do not rely on the baseline comparison for their validity. The key insight from synthesizing the reviews is that the paper should be evaluated as a novel compression *mechanism* with strong hardware evidence, not as a definitive accuracy benchmark against SOTA methods. Its acceptance should hinge on whether the community finds the LFSR approach and FPGA results sufficiently interesting to overlook the unsubstantiated comparison claim.

## Suggestions

1. **Rerun all baselines using their standard recommended configurations** (group size 128 for AWQ, fine-tuning enabled for OmniQuant, appropriate hardware for QuIP# on 70B). Report these results alongside the constrained-bit-budget results. If the goal is a bit-equivalent comparison, the current constraint is defensible, but the anomalously low numbers need an explanation — a sensitivity analysis showing how AWQ degrades as group size is increased (coarsened) would address this.

2. **Validate the design-space hyperparameters on real LLM weights** by running a small sweep over (C, P, K) on a single layer (e.g., Llama 2 7B attention projection) and showing that the Gaussian-based selection is near-optimal.

3. **Report the wall-clock compression time** for at least the 7B and 70B models (e.g., "compressing Llama 3 70B required X hours on Y GPUs"). This addresses the scalability concern directly.

4. **Remove or soften the "first instance" claim** to avoid unnecessary debate.

5. **Add a paragraph discussing GPU feasibility.** The FPGA implementation is well-done, but GPUs lack hardware LFSR support. A brief discussion of whether the method could be implemented efficiently via software LUT-based approaches on GPU would broaden the paper's impact.

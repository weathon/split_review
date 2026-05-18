Now I have thoroughly verified all claims against the paper. Let me construct the final consolidated review.

---

## Summary

This paper proposes MC-MoE, a training-free mixture compression strategy for MoE-LLMs that combines (1) Pre-Loading Mixed-Precision Quantization (PMQ) — an integer programming formulation that allocates bit-widths to experts based on access frequency, routing weights, and quantization reconstruction error — with (2) Online Dynamic Pruning (ODP) — a token-importance-aware expert pruning method that protects ~2% of critical tokens to avoid "attention decay." Experiments on Mixtral 8×7b and 8×22b show that at 2.54-bit average, the method achieves 67.50% LM-Eval accuracy (vs. 71.29% for the 16-bit model and 49.07% for the BSP baseline) while compressing activated parameters to 3.96 GB, and the combined pipeline outperforms LLaMA2-13b at 16-bit.

## Strengths

1. **Novel and well-motivated combination of static quantization and dynamic pruning for MoE.** The paper is the first to jointly optimize both pre-loading storage and online inference efficiency for MoE-LLMs via a unified pipeline (Fig. 2). The two-stage design is grounded in clear empirical observations (Fig. 3) showing expert-level imbalance in reconstruction error, routing scores, and activation frequencies.

2. **IP-based mixed-precision allocation significantly outperforms existing MoE-specific and general mixed-precision baselines.** At 2.54-bit, PMQ achieves 67.50% average accuracy vs. BSP's 49.07% and Hessian-based allocation's 67.18% (Table 1). The advantage grows at lower bit-widths: at 1.57-bit, PMQ (54.49%) exceeds Hessian (45.91%) by 8.6%. The IP formulation integrates three factors (frequency, routing weight, quantization error) in a principled optimization.

3. **Token-importance-aware dynamic pruning with strong empirical validation.** ODP identifies that protecting only 2% of important tokens (using a combination of L1 norm and attention scores) mitigates the "attention decay" problem caused by weight-only pruning, while sacrificing <0.3% compression ratio (Fig. 8, labeled as Fig. 8 in the paper). This finding is backed by attention map visualizations (Fig. 4).

4. **Comprehensive evaluation at two model scales.** Experiments cover Mixtral 8×7b and 8×22b across eight zero-shot benchmarks (Table 1–3). The results include 9 different bit-width configurations per model, providing a detailed characterization of the accuracy-compression trade-off.

5. **Practical efficiency.** The quantization pipeline completes in ~90 minutes for Mixtral 8×7b on two A100 GPUs, and the IP optimization "takes only a second." The compressed models fit on a single A100-80GB GPU (vs. 2–4 GPUs for the 16-bit originals).

## Weaknesses

### Fatal
None.

### Major

1. **Core hyperparameters (α, β, γ) for the IP objective are not reported.** The objective in Eq. 4 combines expert significance (ϕ_i^α · w_i^β) with quantization error (ε_{i,j}^γ), but the paper never states what values of α, β, γ are used, whether they were tuned, or how sensitive the results are to these choices. Since the entire bit-width allocation depends on these exponents, this is a critical reproducibility gap. The μ threshold for ODP (defined as "the median value of w1/w0 from calibration data") is better specified but the actual numeric value across layers is also absent. The authors must disclose these values in any revision.

### Minor

2. **The "15% activated parameter reduction" is overstated.** The abstract and Section 3 claim ODP reduces activated parameters by 15%. However, from Table 3, the actual reduction across all configurations is consistently ~13% (e.g., 2.54-bit: (4.53-3.96)/4.53 = 12.6%; 2.05-bit: 13.4%; 1.57-bit: 13.3%). The paper's own Fig. 8 (labeled as Fig. 8 in the paper) shows a ~14.8% compression ratio at 2% token protection. The difference between "about 15%" and 13% is small, but the abstract states "15%" without qualification, which is imprecise.

3. **Speedup computation methodology is not explained.** Table 3 reports a "Speedup" column, and the caption states "We carry out the average activated parameter size and speedup on C4 dataset" without specifying how speedup is measured or computed. The reported numbers (e.g., 1.63× for 2.54-bit PMQ with Act Params = 4.53 GB vs. 26.31 GB at 16-bit) are clearly not derived from a simple parameter-count ratio (which would yield ~5.8×), suggesting some empirical or other methodology — but the reader cannot tell what. The paper should state whether these are actual wall-clock latency measurements, throughput comparisons, or estimated values, and describe the measurement conditions.

4. **No ablation isolating PMQ's marginal benefit when ODP is also applied.** The paper shows that PMQ outperforms uniform quantization (Table 1) and that PMQ+ODP outperforms PMQ alone (Table 3). However, it does not show a uniform+ODP baseline to isolate what PMQ specifically adds to the full pipeline. The authors should add an experiment: apply uniform quantization at a comparable bit-width, then apply ODP on top, and compare to PMQ+ODP. This would directly substantiate the "mixture compression" claim.

5. **No error bars or variance reporting.** Given that GPTQ involves random ordering and the calibration set is only 128 sequences, the reported benchmark scores may vary across runs. The absence of any variance estimates weakens confidence in the fine-grained comparisons between methods at similar bit-widths.

### Trivial

6. **Minor imprecision in the "surpasses dense LLMs" framing.** The abstract states MC-MoE "even surpasses floating-point 13b dense LLMs with significantly smaller parameter sizes." This is factually correct (a 2.54-bit Mixtral 8×7b at 66.94% indeed beats LLaMA2-13b at 65.19%), but the framing implies this is a surprising consequence of the compression method, whereas the uncompressed Mixtral 8×7b (71.29%) already comfortably outperforms LLaMA2-13b. The comparison is valid but should be contextualized.

## Nice-to-Haves

- **Calibration domain sensitivity analysis.** Fig. 3 shows that expert activation patterns differ between C4 and MATH datasets. Since calibration is performed only on C4, bit-width allocations optimized for general language may be suboptimal for specialized domains. A brief analysis or acknowledgment of this limitation would strengthen the paper.
- **PPL-to-benchmark correlation for the ODP token protection ratio.** The 2% token protection finding (Fig. 8) is validated only with PPL. Showing that this finding also holds on downstream benchmarks would strengthen the claim.
- **Comparison with weight-only expert pruning (Lu et al. 2024) as a pruning-only baseline.** The paper cites this work but does not directly compare ODP against it under the same conditions.

## Removed Points

These points were removed from the harsh critic's review because they are factually incorrect, misunderstand the paper, or violate the review guidelines:

- **Claim that speedup "appears to be derived purely from the ratio of activated parameter counts."** This is factually wrong: for Mixtral 8×7b at 2.54-bit, Act Params = 4.53 GB vs. 16-bit Act Params = 26.31 GB, giving a parameter ratio of ~5.8×, but the reported speedup is 1.63×. The numbers clearly do not come from a simple parameter-count ratio. The underlying concern (unclear methodology) is valid and has been kept in Minor Weakness #3, but the specific assertion is incorrect.

- **Claim that missing baselines (SpQR, PB-LLM, OmniQuant) should have been compared.** These are dense LLM quantization methods, not MoE-specific compression techniques. The paper's comparison against BSP (the only existing MoE-specific mixed-precision method) and Hessian-based allocation (a general mixed-precision approach) is appropriate for its scope.

- **Claim that "the paper should compare against dense models of similar base capability."** The paper's comparison against LLaMA2-13b is a commonly used benchmark for demonstrating the efficiency advantage of MoE architectures. The comparison is valid and informative; the complaint represents a preference rather than a flaw.

- **Claim that "the BSP results may be outdated" and the gap might come from non-expert layers.** The paper explicitly states that non-expert layers are quantized to 4-bit (line 106), contributing "no more than 0.05 bits." The BSP comparison was reproduced from official code under the same evaluation settings. This criticism is speculative and unsupported.

- **Claim about "no comparison to MoE-specific quantization methods beyond BSP."** BSP is the only published method that does what the paper compares against (expert-level mixed-precision quantization for MoE). The reviewer's assertion that "other relevant work exists" is vague and unsupported.

## Novel Insights

The reviews do not surface any novel insight about the paper that goes beyond what the paper itself articulates. The key observation — that different MoE experts exhibit varying activation frequencies, routing scores, and quantization error sensitivity, and that this heterogeneity can be exploited via an IP-based allocation — is already the paper's own contribution. The calibration reviews primarily raise reproducibility concerns and suggest ablations, but do not identify any alternative interpretation of the results or any phenomenon the paper missed.

## Suggestions

1. **Report all hyperparameter values.** Disclose α, β, γ for the IP objective and the per-layer μ threshold values (or at least their range). Add a sensitivity analysis showing performance under different (α, β, γ) configurations.
2. **Clarify the speedup measurement methodology.** State explicitly whether the "Speedup" column in Table 3 reflects actual wall-clock time, tokens/second throughput, estimated latency reduction, or another metric. If measured, describe the hardware, batch size, sequence length, and measurement protocol.
3. **Add a uniform+ODP ablation.** This would directly demonstrate the marginal benefit of PMQ's mixed-precision allocation in the full pipeline and substantiate the "mixture" framing.
4. **Correct the "15%" claim** in the abstract to reflect the actual ~13% reduction from Table 3, or qualify it as "approximately 13–15% depending on bit-width."
5. **Report variance** across at least 3 runs for the key benchmark results (e.g., at 2.54-bit and 2.05-bit) to assess the stability of the method.
6. **Address the calibration domain limitation** in a limitations section or future work paragraph.

## Score and Decision

The paper makes a solid contribution to MoE-LLM compression by proposing a novel combination of mixed-precision quantization and dynamic pruning, with strong empirical results across two model scales. The core findings are well-supported by the data. The most significant weakness — the non-disclosure of the IP hyperparameters — is straightforward to fix in a revision and does not invalidate the core claims. However, in its current form, this reproducibility gap prevents full verification of the method. I recommend acceptance conditional on the authors providing the missing hyperparameter values and clarifying the speedup methodology.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
Now I have all the information needed. Let me compile the final consolidated review.

---

## Summary

This paper proposes MC-MoE, a training-free framework that jointly applies **Pre-Loading Mixed-Precision Quantization (PMQ)** and **Online Dynamic Pruning (ODP)** to Mixture-of-Experts LLMs. PMQ formulates expert-wise bit-width allocation as an Integer Programming problem that balances activation frequency, routing weights, and quantization reconstruction error. ODP identifies important tokens using attention-aware importance scores and protects their expert computations from being pruned, mitigating "attention decay." Experiments on Mixtral 8×7b and 8×22b show that at 2.54-bit average precision, MC-MoE achieves 67.50% zero-shot accuracy (only 3.8% below FP16) and, with ODP, reduces activated parameters by 15% with under 0.6% accuracy loss.

## Strengths

- **First training-free combination of static quantization and dynamic pruning for MoE-LLMs.** Prior work treated these as separate phases (Li et al. 2024 on quantization only; Lu et al. 2024 on pruning only). The paper explicitly identifies this gap (Sec. 1, line 23) and delivers a joint solution, which is a genuine methodological contribution.

- **The IP-based bit-width allocation (Eq. 4) provides a principled multi-factor objective.** The formulation incorporates activation frequency, routing weights, and F-norm reconstruction error into a single optimization. The ablation (Fig. 5_1/5_2) demonstrates that the combined objective outperforms allocations based on any single factor (routing scores only, frequency only, or Hessian-based loss), and the advantage is substantial below 2-bit (e.g., 54.49% vs. 45.91% at 1.57-bit in Table 1).

- **Attention-aware token protection for dynamic pruning is a simple and effective mechanism.** ODP identifies attention-critical tokens using Eq. 6 and prevents their expert computations from being pruned. The ablation (Fig. 8/9) shows that protecting just 2% of tokens reduces perplexity from 6.46 to 6.24 while maintaining a 14.8% compression ratio (vs. 15.1% for unprotected pruning), demonstrating near-zero efficiency cost.

- **Strong results at extreme compression (<2-bit).** At 1.57-bit, PMQ achieves 54.49% accuracy, outperforming the Hessian baseline by 8.6 percentage points (45.91%). This is a practically meaningful regime that uniform quantization cannot reach (uniform 2-bit collapses to 42.67%).

- **Empirical analysis of expert imbalance (Fig. 3) convincingly motivates the approach.** The paper provides clear evidence from both C4 and MATH datasets that experts differ substantially in activation frequency, routing scores, and reconstruction error, establishing the foundation for per-expert mixed-precision allocation.

## Weaknesses

### Major

- **At the most-advertised bit-width (2.54-bit), PMQ's improvement over the proper expert-wise baseline is marginal.** Against the Hessian-based expert-wise allocation (Dong et al. 2020), PMQ achieves 67.50% vs. 67.18% (a 0.32% gap). The paper emphasizes the 18.4% improvement over BSP (which operates at coarser layer-wise granularity), but that comparison conflates the benefit of the multi-factor IP formulation with the benefit of moving from layer-wise to expert-wise allocation. The controlled expert-wise comparison shows that PMQ's advantage at moderate bit-widths is modest.

- **No hyperparameter sensitivity analysis for α, β, γ (Eq. 4).** The paper introduces three exponents that control the relative weights of frequency, routing score, and reconstruction error in the IP objective. No values are stated for α, β, or γ, and no ablation studies their effect on perplexity or accuracy. Without this analysis, the method's design appears arbitrary and its robustness to hyperparameter choices is unknown. This is the single most significant methodological gap.

- **The headline 18.4% improvement over BSP partially conflates granularity with the proposed objective.** BSP allocates bits at the layer/block level (25% of MoE layers at 4-bit, rest at 2-bit), while PMQ operates at the expert level within each layer. The paper does not control for this granularity difference when reporting the 18.4% gain. The Hessian baseline (expert-wise) provides a fairer comparison and shows a much smaller 0.32% gap at 2.54-bit. The paper should either qualify the BSP comparison or include an expert-wise version of BSP as a baseline.

### Minor

- **No ablation of the IP constraints requiring at least one 3-bit and one 2-bit expert per layer (Eq. 4, line 101).** The paper imposes these constraints "to preserve accuracy" but does not show what happens without them or with different minimum bit requirements. A comparison would help validate the constraint design.

- **ODP pruning threshold robustness is not assessed.** The threshold μ is set as the median of w₁/w₀ from calibration data (line 125). The paper does not report variance across different calibration seeds or test sets, leaving open questions about sensitivity to calibration data choice.

- **The token importance metric (Eq. 6) is briefly motivated but the exact mechanism could be clearer.** While the paper states that A comes from "this layer" (which in a transformer precedes the MoE sublayer, avoiding the claimed circular dependency), a more explicit description of the causal flow — showing that attention is computed before MoE within each block — would help readers.

### Trivial

- None that survive filtering — apparent formatting issues (figure numbering mismatches) are parser artifacts, not author errors.

## Nice-to-Haves

- A straightforward extension would be to test MC-MoE on other MoE architectures (e.g., DeepSeek-MoE, Qwen-MoE) to demonstrate generality beyond Mixtral.
- Hardware latency benchmarks on target devices would complement the reported speedups based on dequantization overhead.
- A visualization of which experts receive which bit-widths across layers would illustrate whether PMQ's allocation aligns with the claimed importance signals.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Token importance causality unclear"** — The critic claimed circular dependency (attention depends on pruning which depends on token importance). In a standard transformer block, the self-attention sublayer precedes the MoE sublayer. The attention map A from "this layer" (line 130) is computed before the MoE pruning decision in the same block. There is no circular dependency. The paper's description (Fig. 4 caption, lines 111–113) is consistent with this causal ordering.

2. **"Abstract claim overstated"** — The paper claims "first to explore extreme training-free mixture compression for MoE-LLMs, efficiently combining static expert quantization with dynamic expert pruning." Prior work (Li et al. 2024, Lu et al. 2024) addressed quantization OR pruning, not their combination. The claim is accurate.

3. **"Fig. 1 comparison with dense LLMs is misleading"** — The critic stated the compressed MoE has "far more total parameters." At 2.54-bit, Mixtral 8×7b's total size is ~16 GB, versus LLaMA2-13b's 26 GB. The comparison is valid and demonstrates a meaningful practical advantage. The critic's calculation is factually incorrect.

4. **"MMLU results are modest"** (Table 2) — A 3% improvement (61.19% vs. 58.22%) on MMLU 5-shot is practically meaningful and non-negligible.

5. **"Missing related works"** — Removed as per instructions; cannot verify existence of uncited works.

6. **Figure numbering, formatting, typo concerns** — Parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews corroborate the paper's core claims (first joint training-free compression, effective token protection) while identifying the main limitation: PMQ's advantage over a simple Hessian-based expert-wise baseline at moderate bit-widths (2.54-bit) is small, and the paper's presentation of the BSP comparison overstates this advantage by conflating granularity with the proposed IP objective. The most useful finding for the community may be that the combination of quantization and pruning is where the real value lies — the ODP token protection mechanism is clean, effective, and adds minimal overhead, and it works well regardless of the modest quantization baseline improvements.

## Suggestions

1. **State α, β, γ values explicitly and add a hyperparameter ablation** (e.g., vary each exponent while holding others fixed, report perplexity on WikiText2 at one bit-width). This single change would substantively address the largest methodological concern.

2. **Qualify the BSP comparison** by noting the granularity difference (layer-wise vs. expert-wise), or better, construct an expert-wise variant of the BSP approach to enable a true like-for-like comparison.

3. **Ablate the IP constraints** by removing the "at least one 3-bit and one 2-bit" requirement and reporting the resulting bit-width distribution and accuracy.

4. **Report variance for the ODP pruning threshold** across at least 3 calibration seeds to demonstrate robustness.

5. **Clarify the causal flow** for token importance: explicitly state that within a transformer block, attention is computed before the MoE sublayer, so the attention map A used in Eq. 6 does not depend on the pruning decision being made in the same block.

## Score and Decision

The paper makes a genuine contribution by being the first to jointly apply static mixed-precision quantization and dynamic pruning to MoE-LLMs in a training-free manner. The IP formulation and token protection mechanism are well-designed. The main limitation is that PMQ's improvement over a properly matched expert-wise baseline (Hessian) at the most promoted bit-width (2.54-bit) is only 0.32%, and the headline 18.4% improvement over BSP is inflated by a granularity mismatch. However, the approach shows clear value at extreme compression (<2-bit), and the ODP token protection is independently effective. The missing hyperparameter analysis is the most substantive gap, but it is addressable in revision. The contribution is solid enough to warrant acceptance with revisions.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
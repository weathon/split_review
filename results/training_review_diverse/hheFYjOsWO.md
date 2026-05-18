Now I have all the information needed to write a thorough, verified review.

## Summary

This paper proposes MC-MoE, a training-free compression framework for MoE-LLMs combining two stages: Pre-Loading Mixed-Precision Quantization (PMQ) and Online Dynamic Pruning (ODP). PMQ formulates per-expert bit-width allocation as an Integer Programming problem that jointly considers activation frequency, routing weights, and reconstruction error. ODP protects the 2% most important tokens (identified via an ℓ₁ norm + attention-score metric) from expert pruning, mitigating "attention decay." On Mixtral 8×7b and 8×22b, MC-MoE achieves extreme compression (e.g., 2.54-bit, 83% size reduction) with minimal accuracy loss (3.8%), and its compressed 16.24 GB model outperforms the 26.03 GB LLaMA2-13b.

## Strengths

1. **Consistent empirical gains over strong baselines at ultra-low bit-widths.** PMQ outperforms uniform quantization, BSP, and a Hessian-based mixed-precision method at every tested bit-width (1.57–2.54 bits). At 2.54 bits on eight zero-shot benchmarks, PMQ reaches 67.50% vs. BSP's 49.07% and Hessian's 67.18%; at 1.57 bits the gap over Hessian widens to 8.6 absolute points (Tables 1, 2). These gains are supported by multiple metrics (zero-shot accuracy, MMLU 5-shot, perplexity).

2. **ODP with attention-aware token protection demonstrably recovers pruning losses.** Weight-only dynamic pruning causes ~10% accuracy degradation; protecting just 2% of tokens (identified via Eq. 6) reduces this to <0.6% while maintaining ~15% reduction in activated parameters (Table 3, Figs. 8–9). The "attention decay" phenomenon is well-motivated (Fig. 4) and the proposed fix is simple and effective.

3. **Scalability demonstrated on a larger MoE model.** MC-MoE validated on Mixtral 8×22b (141B parameters) with consistent trends: 71.21% accuracy at 2.54-bit, 1.82× speedup, outperforming LLaMA2-13b (Table 3). This strengthens the claim that the method generalizes.

4. **Thorough empirical analysis motivating design choices.** Figure 3 provides clear evidence of expert heterogeneity across three dimensions (reconstruction error, routing weight, activation frequency) on both general (C4) and specialized (MATH) datasets, directly motivating the multi-factor significance metric.

## Weaknesses

### Fatal
None.

### Major
None. The core claims are well-supported by experiments. No weakness identified by the reviewers invalidates the paper's main contributions.

### Minor

1. **Key hyperparameters α, β, γ are not reported.** The paper introduces three exponents in Eq. (4) that directly control the IP objective, but never states the values used in any experiment. The authors mention that α and β "balance" frequency and weight (line 87) and that γ is a "weighting hyperparameter" (line 106), but do not disclose their settings or provide any sensitivity analysis. This is a genuine reproducibility gap — without these values, a reader cannot replicate the method. (This is fixable in a revision, but the omission is material.)

2. **The additive independence assumption in the IP objective is not discussed.** The formulation minimizes a separable sum where each expert's contribution uses ε_{i,j} computed when *only* that expert is quantized (Eq. 3). This treats quantization errors as linearly additive across experts, which may not hold at extreme bit-widths where errors can interact non-additively. While this relaxation is standard in mixed-precision quantization literature and the method works well empirically, the paper does not acknowledge the assumption or provide evidence (e.g., comparing the additive proxy to the true joint error) that it is justified.

3. **Hessian-based baseline implementation details are insufficient.** The paper compares against "Hessian" (citing HAWQ/Dong et al.) in Tables 1 and 2, but does not specify how the Hessian trace was adapted from its original per-layer, dense-model design to per-expert allocation in MoE. Details such as calibration sample count, per-expert vs. per-group computation, and the bit-assignment rule are absent, making it difficult to assess whether the comparison is apples-to-apples.

4. **The claim about surpassing LLaMA2-13b "by around 8% on MMLU (5-shot)" is imprecisely documented.** The 8% figure is referenced to Fig. 1(a) (an image), but Table 3's LM-Eval average shows a gap of ~1.75% (66.94% vs. 65.19%). The MMLU 5-shot score for LLaMA2-13b is not provided in any table. While the compressed model does outperform LLaMA2-13b, the exact margin on MMLU is unclear. The comparison is also unsurprising in the sense that the *uncompressed* Mixtral already exceeds LLaMA2-13b — the notable achievement is that compression does not destroy this advantage, not that compression creates it. The paper should be more precise about what this comparison demonstrates.

### Trivial

1. **Nomenclature inconsistency.** The abstract and introduction refer to a "Linear Programming (LP) problem" (lines 8, 32), while the method section correctly uses "Integer Programming (IP)" (lines 73, 94). Since decision variables are binary, IP is the accurate term. Additionally, if γ ≠ 1 the objective is nonlinear, which would make the formulation an integer nonlinear program. The authors should align terminology.

2. **The token importance metric (Eq. 6) could be more precisely specified.** The paper says "$\mathbf{A}$ represents the attention map in an LLM block, calculated from $\mathbf{A} = \operatorname{softmax}(\frac{K^\top Q}{\sqrt{d_k}})$ of this layer." In context it is clear this refers to the self-attention of the same block where pruning occurs, but stating "the self-attention layer of the current MoE block" would eliminate ambiguity.

## Nice-to-Haves

- **Compressed dense baselines.** Adding quantized LLaMA2-7b/13b (e.g., 4-bit, 3-bit) to Table 3 would strengthen the claim that compressed MoE outperforms comparably-sized compressed dense models.
- **Computational cost profiling.** Reporting the wall-clock time for computing ε_{i,j} across all experts and bit options (768 partial forward passes for Mixtral 8×7b) would help practitioners assess the profiling overhead.
- **ODP overhead quantification.** Clarify whether per-token importance (Eq. 6) is recomputed at every MoE layer during inference, and if so, quantify this cost.
- **Token importance ratio ablation across models.** Figure 8 shows the 2% threshold for one model/bit-width; showing this sensitivity on Mixtral 8×22b and at additional bit-widths would strengthen generality.

## Removed Points

These points were raised in the reviews but are removed or downgraded for the reasons stated:

- *Reviewer concern that the comparison against LLaMA2-13b is "misleading" because the uncompressed model already beats it.* **Removed as overreach.** Demonstrating that a 2.54-bit, 16.24 GB compressed model retains enough quality to outperform a 26.03 GB dense model is a legitimate empirical finding. It does not require that compression create the advantage from scratch. The minor documentation issue (precise MMLU margin) is retained above.

- *Criticism that token importance lacks reproducibility because the specific attention head is unspecified.* **Downgraded to trivial.** The method identifies important tokens using the attention map of the current block's self-attention; this is standard and does not require specifying a single head. The caption of Fig. 4 shows head 4 as an illustrative example, not as a prescription.

- *Request for dense compressed baselines.* **Moved to Nice-to-Haves.** The paper's main contribution is MoE-specific compression; the dense comparison is supplementary.

- *Complaint about missing computational cost of PMQ profiling and ODP overhead.* **Moved to Nice-to-Haves.** Useful additions but not required to validate the core method.

- *Framing of the additive assumption as a "fatal" or "critical" error.* **Downgraded to minor.** This assumption is standard in mixed-precision work (e.g., HAWQ, Hessian-based allocation), and the empirical results indirectly validate its adequacy. It warrants discussion but does not threaten the paper's claims.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any genuinely novel perspective that the paper's authors missed.

## Suggestions

1. Report the values of α, β, γ used in all experiments and add a sensitivity ablation (e.g., varying each from 0.5 to 2.0 on one configuration in Table 1).
2. Add a brief paragraph discussing the additive-independence assumption in the IP objective and, if possible, validate it by comparing the IP proxy loss to the true joint reconstruction error for one or two layers.
3. Provide the implementation protocol for the Hessian baseline: number of calibration samples, whether per-expert or per-group Hessian trace was computed, and the bit-assignment rule.
4. Add LLaMA2-13b's MMLU 5-shot score somewhere accessible so the "8%" claim in the introduction can be directly verified.
5. Align the "Linear Programming" / "Integer Programming" terminology throughout (IP is correct given binary decision variables).

## Score and Decision

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
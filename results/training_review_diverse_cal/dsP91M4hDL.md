Now I have all the information I need. Let me compose the final consolidated review.

## Summary

The paper proposes Ternary Choice Mixture of Experts (TC-MoE), which expands the expert space of MoE models by multiplying each original expert by {-1, 0, 1}, creating contrastive (E^{-1}), null (E^0), and standard (E^1) variants without adding expert parameters. The approach retains the standard Top-K routing mechanism while giving it access to cost-free null experts and sign-flipped negative experts. The paper further introduces a tailored load balancing loss and a reward loss to control the efficiency-accuracy trade-off. Experiments across multiple model sizes and datasets show consistent accuracy improvements (0.83%–1.18%) alongside reduced activated expert counts (7%–9%).

## Strengths

- **Clean, well-motivated idea with consistent empirical gains**: The ternary expansion is simple, conceptually grounded in the paper's own diagnostic experiments (Figure 1), and delivers improvements across 4 settings (tiny/base/fine-grained base on FineWeb and RedPajama) with both higher accuracy and fewer activated parameters (Table 1). The consistency across model scales and datasets is compelling.

- **Ablation cleanly isolates each component's contribution**: Table 3 shows that {-1,1} alone yields +0.29% accuracy, {0,1} yields +0.52% and reduces activated experts by 0.19, and the full {-1,0,1} set achieves the best combined result. This rigorously demonstrates that both the negative and null experts contribute meaningfully.

- **Superiority over competing dynamic-routing methods under matched budgets**: Figure 3 shows TC-MoE consistently outperforms Random drop and Top-P across varying activation budgets (lower LM loss by ~0.017, higher HellaSwag by up to 0.7%), confirming the benefit comes from the ternary design rather than just dynamic activation.

- **Negligible overhead**: The only added parameters and FLOPs are in the router (O((N+K)d)), which is a genuinely practical strength for scaling.

- **Informative pattern analysis**: Figures 6-8 reveal interpretable behavior (E^{-1} preferred in deep layers, E^0 in shallow layers) and confirm load balance is achieved, strengthening understanding of how the method works.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Section 3.4 gradient analysis is imprecisely scoped**: The paper computes ∂ℒ/∂g_{E_i^0} = 0 (correct, since E_i^0(h)=0) and concludes that "expert E_i^0 has no impact on reducing the loss function." This statement is accurate for the direct gradient through the weighted sum, but incomplete if interpreted as the full gradient through the router parameters — the normalization in Top-K routing means that changing the gate value of one expert indirectly affects others through the softmax/normalization pathway. The analysis would benefit from explicitly noting this scope. That said, the core intuition (E^0 experts receive intermediate gate values because their direct gradient is zero) is reasonable and the reward loss remains a valid practical technique regardless. This is a presentation imprecision, not a fatal error.

2. **Reward loss not ablated independently**: The paper ablates which ternary components are used (Table 3) but does not ablate the reward loss itself (i.e., TC-MoE with α₂=0). Including this would clarify how much of the efficiency gain comes from the reward loss vs. the inherent presence of E^0 experts in the expanded space. This is an informative missing experiment but not fatal — the method works and the reward loss is clearly motivated.

3. **Novelty relative to prior null-expert work (Zeng et al., 2024) is underspecified**: The related work briefly mentions prior null-expert designs but does not clearly delineate what distinguishes TC-MoE's E^0 experts or what the prior work cannot achieve. The paper's novelty rests on the full ternary set {-1,0,1} — both negative experts (which prior work does not have) and the specific loss designs — but this should be stated explicitly. A sentence or two would suffice.

4. **"More than 1.1%" is slightly overstated**: Averaging the four reported improvements (1.18%, 1.17%, 0.83%, 0.96%) gives ≈1.035%, not "more than 1.1%." This is a minor quantitative imprecision.

### Trivial

- The paper does not explain how different operating points in Figure 3 were obtained (e.g., sweeping α₂ vs. another mechanism). A brief clarification would help.
- The claim about router cost being "negligible" could be strengthened with a concrete percentage of total MoE FLOPs, though the order-of-magnitude estimate is already adequate.

## Nice-to-Haves

- An ablation of TC-MoE with α₂=0 (reward loss removed) to isolate the contribution of the reward loss vs. the expanded space itself.
- A brief discussion of whether the grouping of E_i^1 and E_i^{-1} for load balancing is sufficient to avoid increased all-to-all communication cost in expert-parallel distributed settings.
- A concrete router FLOPs comparison (e.g., "router FLOPs are <0.1% of total MoE layer FLOPs").

## Removed Points

- **"Flawed gradient analysis" (harsh critic's Critical Issue 1)**: The reviewer claims the gradient analysis is "incorrect" because it ignores normalization dependencies. However, the paper's computation of ∂ℒ/∂g_i = ⟨∂ℒ/∂O, E_i(h)⟩ is mathematically correct as the direct partial derivative through the weighted sum. The gradient with respect to the gate value g_i does not "pass through" the normalization — g_i is already the normalized value. The paper's analysis is narrowly scoped rather than incorrect. I have preserved the imprecision concern as a Minor weakness but removed the "flawed/incorrect" framing, which overstates the problem.

- **"Cannot be independently verified" / reproducibility concerns rooted in doubting cited entities**: The harsh critic does not make such claims, so no action needed here.

- **Generic strengths from Strength Finder**: The strength finder's supporting strengths 1 and 4 are substantive and backed by evidence, so I kept them. No dropped strengths.

## Novel Insights

The harsh critic's observation about the gradient through the normalization pathway is technically correct as a point of precision (the full gradient through router parameters includes indirect effects), but it does not invalidate the paper's practical contribution. The more interesting insight that emerges from reading the reviews together is that the paper's core contribution — the ternary expert expansion — is largely orthogonal to the gradient debate: the empirical results stand on their own, and the reward loss can be justified purely as a regularizer for trading off efficiency and accuracy without needing the zero-gradient claim as a foundation. This suggests the paper could be strengthened by reframing Section 3.4 as a practical motivation rather than attempting a formal gradient analysis, which would inoculate it against this kind of criticism entirely.

## Suggestions

1. Reword Section 3.4 to clarify the scope of the gradient claim: explicitly note that ∂ℒ/∂g_{E_i^0} = 0 is the direct gradient through the weighted sum, and that the reward loss is motivated as a practical regularizer to shift this gradient toward encouraging null-expert selection.
2. Add an ablation with α₂=0 (no reward loss) to Table 3 or as a supplementary experiment.
3. Add a sentence in Related Work explicitly distinguishing TC-MoE's ternary expansion from prior null-expert-only designs.
4. Correct the "more than 1.1%" to "approximately 1.0%" or report the exact average.
5. Briefly clarify how the different operating points in Figure 3 were obtained.

## Score and Decision

**Originality**: The ternary expert expansion is a simple but clever idea that has not been explored in prior MoE work. 7/10.

**Importance of research question**: Improving MoE efficiency while maintaining accuracy is a timely and practically important problem. 8/10.

**Claims well-supported**: The core empirical claims are well-supported by Table 1, Table 3, and Figure 3. The theoretical motivation in Section 3.4 is somewhat imprecise but does not affect the validity of the empirical results. 7/10.

**Soundness of experiments**: Solid experimental setup with multiple model sizes, two pretraining datasets, and standard evaluation benchmarks. Missing reward-loss ablation is a gap but not a fatal one. 7/10.

**Clarity of writing**: Generally clear. Section 3.4 could be more precise about the scope of its gradient analysis. 7/10.

**Value to community**: The method is simple to implement on top of existing MoE frameworks, delivers consistent gains, and opens up a new direction (ternary expansion) for MoE design. 7/10.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
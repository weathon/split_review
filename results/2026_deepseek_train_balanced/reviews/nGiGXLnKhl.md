## Summary

This paper adapts the RWKW linear-complexity architecture from NLP to vision, proposing Vision-RWKV (VRWKV). The key contributions are bidirectional global attention with O(TC) complexity (Bi-WKV), a quad-directional token shift (Q-Shift) for 2D spatial mixing, and stability mechanisms (bounded exponential, extra normalization) that enable scaling to 335M parameters. VRWKV is evaluated on ImageNet classification, COCO detection, and ADE20K segmentation, with its strongest evidence being dramatically higher throughput and lower memory at high resolutions (10× faster, 80% less memory at 2048×2048 vs. ViT-T).

## Strengths

- **Verified linear-complexity global attention with explicit FLOPs derivation.** Equation 6 gives FLOPs(Bi-WKV) = 13×T×C, and the RNN form (Equations 3–5) shows each token update uses a fixed number of operations regardless of sequence length. This is empirically validated: at 2048×2048 (16384 tokens), VRWKV-T delivers 10× faster inference and 80% lower GPU memory than ViT-T (Fig. 1b/c), and Bi-WKV is 2.8× faster than Flash Attention at the same resolution.

- **Q-Shift is a nontrivial 2D adaptation with clean ablation evidence.** The quad-directional shift (Equation 7) mixes each token with its four spatial neighbors across four channel groups. The ablation study (Table 3) quantifies the contribution: Q-Shift outperforms the original 1D RWKV shift by 0.7 points (74.4→75.1) and no shift by 3.6 points (71.5→75.1), making the benefit grounded and measurable rather than asserted.

- **Scalability demonstrated from 6M to 335M parameters with consistent improvements over ViT counterparts across three distinct tasks.** Table 2 shows VRWKV advancing across all four scales (Tiny through Large) on ImageNet. Tables 4 and 5 extend this to COCO detection and ADE20K segmentation — e.g., VRWKV-T achieves AP^b 41.7 with 67.9G FLOPs versus ViT-T's 41.6 with 147.1G FLOPs (54% fewer FLOPs), and VRWKV-S achieves 47.2 mIoU (46.3G FLOPs) versus ViT-S's 46.2 (54.0G FLOPs). This breadth shows the architecture transfers across tasks.

- **The bounded exponential mechanism (Section 3.4) provides a principled solution to a real numerical instability.** The paper identifies that exponential terms overflow at high resolution and solves it by dividing the exponent by T (total tokens). This is a specific, verifiable engineering contribution that makes the 2048×2048 results possible.

## Weaknesses

### Fatal
None.

### Major

- **Parameter counts are not matched, and the paper incorrectly claims they are "the same."** VRWKV variants are consistently 8–9% larger than their ViT counterparts in every comparison: VRWKV-T 6.2M vs. DeiT-T 5.7M (+9%), VRWKV-S 23.8M vs. DeiT-S 22.1M (+8%), VRWKV-B 93.7M vs. DeiT-B 86.6M (+8%), VRWKV-L 334.9M vs. ViT-L 309.5M (+8%). The same pattern holds in detection and segmentation tables. Line 330 states "with the same number of parameters… VRWKV achieves better results than ViT" — this is factually inaccurate. The accuracy advantage could be partially parametric rather than architectural. The paper needs an apples-to-apples experiment (e.g., widening DeiT-T to match VRWKV-T's 6.2M params) or a clear acknowledgment that the comparison is not parameter-matched.

- **MAE pre-training advantage is negligible (0.2 points), which undermines claims of comprehensive ViT substitution.** Section 4.5 reports VRWKV-L improving from 86.0% to 86.2% after MAE pre-training. For reference, MAE pre-training of ViT-L typically yields improvements of several points on ImageNet. The paper states VRWKV "benefits from the MAE pre-training" and "can handle sparse inputs," but a 0.2-point gain on a single run is indistinguishable from noise. This weakens the claim (line 47) that VRWKV achieves "comprehensive substitution" for ViT, since it does not benefit from masked image modeling to a degree comparable to ViT.

- **XCiT, a relevant linear-complexity competitor, appears in Table 2 but is never discussed in the results text.** XCiT-S12 (26.0M params, 4.8G FLOPs, 82.0%) achieves 1.9 points higher accuracy than VRWKV-S (23.8M, 4.6G, 80.1%) at a comparable scale. XCiT is a linear-complexity architecture (cross-covariance attention), making it the closest class of competitor for VRWKV. The paper includes XCiT in Table 2 as a baseline yet never mentions it in Section 4.1's results discussion. This omission affects the paper's main narrative about VRWKV's classification performance and should be addressed directly.

### Minor

- **The classification accuracy advantage is heavily concentrated at the Tiny scale with no analysis or explanation.** VRWKV-T beats DeiT-T by 2.9 points, but VRWKV-S and VRWKV-B beat their counterparts by only 0.2 points each. This variation is not discussed. If the advantage is driven by Q-Shift's inductive bias helping most at very small model capacity, this should be analyzed — it has implications for how the architecture's contribution is understood.

- **No training variance or confidence intervals are reported for any experiment.** Given the uneven scaling pattern (2.9 at Tiny, 0.2 at Small/Base), single-run results leave open whether the Tiny result is optimistic and/or the Small/Base results are pessimistic. This is standard practice in vision benchmarking and would substantially strengthen the paper.

- **Q-Shift boundary conditions are not specified.** Equation 7 indexes X[h-1, w], X[h+1, w], X[h, w-1], X[h, w+1] without describing how out-of-bounds positions (h=0, w=0, etc.) are handled (e.g., zero-padding, replication, or clipping). This is needed for exact reproducibility.

- **Precision inconsistency between abstract and Table 2.** The abstract (line 53) reports "(86.04 vs 85.15)" whereas Table 2 reports (86.0 vs 85.2). These are likely rounded vs. precise values but the mismatch appears as an error.

### Trivial
None.

## Nice-to-Haves

- A few sentences analyzing why VRWKV-T gains 2.9 points but VRWKV-S gains only 0.2 would strengthen the paper significantly (e.g., whether Q-Shift's inductive bias provides a larger benefit when the model has very few parameters to learn spatial structure from data).
- Adding a controlled experiment that matches VRWKV and ViT parameter counts (e.g., widening ViT-T to 6.2M) would cleanly isolate the architectural contribution from the parametric advantage.

## Removed Points

These points were raised in the reviews but are not included as weaknesses in the main review, with justification:

- *"No comparison with ConvNeXt or InternImage (scaled-up CNNs)"* — Removed per instructions: missing related works should not be mentioned.
- *"The ablation does not isolate the effect of the relative bias vs the absolute bias change"* — Removed as a fine-grained ablation request that exceeds what is standard; the ablation already separates Q-Shift and bidirectional attention, which are the paper's two primary claimed contributions.
- *"No quantitative ERF measurement (e.g., in pixels)"* — Removed as a nice-to-have; the qualitative ERF visualizations in Figure 4a are informative enough to support the paper's claims about spatial integration.
- *"The critique about Vim/VMamba in related works applies in part to VRWKV"* — Removed as a subjective opinion rather than a verifiable weakness.
- Various formatting/style nitpicks and missing-appendix concerns — removed per parsing-artifact rules.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a consistent concern about claim calibration relative to evidence, but do not generate a novel observation about the method or its implications that the paper itself lacks.

## Suggestions

1. **Fix the "same number of parameters" statement on line 330.** Acknowledge the 8–9% parameter gap and provide a controlled experiment matching parameter counts, or at minimum reframe the comparison as "comparable" rather than "same."
2. **Discuss XCiT directly in Section 4.1.** Acknowledge that XCiT-S12 achieves higher accuracy at a similar scale, and explain the design differences that lead to this trade-off (e.g., cross-covariance vs. exponential-decay attention, or the efficiency-accuracy balance).
3. **Report multi-seed results at the Tiny scale** to establish whether the 2.9-point advantage is stable, and provide confidence intervals for the MAE experiment.
4. **Tone down claims that reach beyond the evidence.** Replace "surpasses ViT's performance in image classification" (abstract) with a more precise statement, e.g., "is competitive with ViT across model scales while offering substantial efficiency gains at high resolution." The paper's genuine contributions — dense prediction efficiency and high-resolution throughput — are strong enough to stand on their own.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
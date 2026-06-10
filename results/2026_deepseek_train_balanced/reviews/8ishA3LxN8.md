## Summary

This paper proposes Finite Scalar Quantization (FSQ), which replaces the learned high-dimensional codebook in VQ-VAEs with a fixed low-dimensional grid: the encoder output is projected to <10 dimensions, bounded via tanh, and rounded to integers, creating an implicit codebook as the Cartesian product of per-dimension integer sets. The approach is applied to MaskGIT (image generation on ImageNet 256×256) and UViM (depth estimation, panoptic segmentation, colorization), achieving competitive results (within 0.5–3% of VQ on most metrics) while eliminating the auxiliary losses, codebook EMA, codebook splitting, and other tricks required by VQ.

## Strengths

- **FSQ achieves ~100% codebook utilization without any auxiliary losses, while VQ collapses on large codebooks.** The tradeoff study (Fig. 3) shows FSQ maintains near-perfect usage up to 2¹⁴ codewords, whereas VQ drops below 50% usage beyond 2¹¹. The UViM depth ablation (Table 2) drives the point home: disabling codebook splitting in VQ causes usage to plummet to 0.78% and RMSE to 0.490, while FSQ achieves 99% usage with no splitting algorithm at all.

- **FSQ matches VQ performance across diverse tasks and architectures.** Table 2 reports FSQ vs. VQ within 0.5–3% on all three UViM tasks (NYU Depth RMSE: 0.473 vs. 0.468; COCO Panoptic PQ: 43.2 vs. 43.4; ImageNet Colorization FID-5k: 17.55 vs. 16.90). For MaskGIT on ImageNet 256×256 (Fig. 4), FSQ obtains Sampling FID 4.534 vs. VQ 4.509 with **100%** vs. **81%** codebook usage. This holds across two architecturally different model families.

- **FSQ scales robustly with codebook size while VQ degrades — a reversal of the assumption that VQ's expressiveness is necessary.** The scaling study (Fig. 3) shows that beyond 2¹⁰ codewords, VQ's Reconstruction FID and Sampling FID *worsen* while FSQ's continue to improve. This is clean evidence that the learned Voronoi partition of VQ is not inherently more expressive in practice.

- **FSQ eliminates the entire ecosystem of VQ tricks** — commitment losses, codebook EMA, codebook splitting, entropy penalties, projections — with a single hyperparameter choice (d and L_i). Table 1 provides a side-by-side comparison showing FSQ requires none of these. The UViM depth ablation concretely demonstrates this advantage.

- **The Compression Cost analysis** (derived from lossless compression principles) provides an informative tool for understanding why codebook scaling yields diminishing returns, going beyond raw codebook size as a metric. The anti-correlation between compression cost and sampling FID (Fig. 3d) cleanly reveals the modeling difficulty trade-off.

## Weaknesses

### Fatal

None.

### Major

None. The core claims are well-supported by the evidence presented.

### Minor

- **The abstract's claimed 0.5–3% degradation range does not cover the colorization result.** For ImageNet Colorization (Table 2), FSQ achieves FID-5k 17.55 vs. VQ 16.90, a degradation of ~3.85%. While this does not undermine the paper's contribution, the claimed range should be revised to include this outlier or the discrepancy should be noted.

- **The "Semantics" claim (lines 416–417) is stated without supporting analysis.** The paper asserts "we found no evidence that a particular code represents a fixed visual concept in either quantizer" but provides no probing experiments, codebook visualizations, or concept-consistency checks. This sentence should either be removed or backed with evidence.

- **MaskGIT results lack variance estimates, unlike UViM results.** UViM reports standard deviations over three runs; MaskGIT results (Fig. 4) do not. Since the FID gap between VQ (4.509) and FSQ (4.534) is very small, variance estimates would help assess whether the difference is meaningful. The paper does note this is a single-run comparison of models trained under the same pipeline, so the gap is likely noise, but explicit variance would strengthen the claim.

- **The "drop-in replacement" framing (lines 34, 75) is slightly overstated.** The paper later acknowledges (lines 176–177) that the encoder output dimension must change from ~512 to <10 when switching from VQ to FSQ, which is an architectural modification. The introduction would benefit from qualifying this claim.

- **The MaskGIT baseline discrepancy with published numbers (4.509 vs. published 4.19) is noted but not fully contextualized.** The paper attributes this to a different FID evaluation suite (ADM TensorFlow Suite), but does not report what the published MaskGIT FID would be under the same suite. This leaves readers to guess whether the gap is purely evaluative or reflects implementation differences. The internal comparison (FSQ vs. VQ, same suite) is valid, but more explicit contextualization would help.

### Trivial

- The paper has no limitations section. While not required, a brief discussion of where FSQ might underperform VQ (e.g., tasks requiring very fine-grained high-dimensional representations, or regimes where the fixed grid lacks flexibility) would be helpful for practitioners.
- The colorization FID-5k value reported for UViM (VQ) (line 368) appears to have a formatting artifact ("99±0.057" where "16.99±0.057" is likely intended).

## Nice-to-Haves

- An analysis of inference cost differences. FSQ's much smaller embedding dimension (d < 10 vs. d ≥ 512) likely yields faster lookup and smaller embedding tables. A wall-clock comparison would be practically useful.
- A capacity-controlled comparison for the "without context" finding (panoptic segmentation) to verify whether FSQ's smaller degradation is due to its simpler bottleneck or to genuinely better representations.

## Removed Points

These points were flagged by reviewers but are removed or demoted after cross-checking against the paper. Treat them with caution:

- **"Without context" advantage not adequately explained.** The critic speculated this might be due to parameter count differences and claimed the capacity-compensation test was "only in the with-context setting." The paper does not specify the test setting, so this is a fabricated detail. The paper already mentions exploring extra layers with no further gains (line 212), partially addressing the concern. The criticism is speculative.
- **Tradeoff study vs. full-resolution results are disconnected.** The paper's compression cost analysis at 128×128 already explains diminishing returns from larger codebooks; the full-resolution finding (no further gains) is consistent with this pattern. The critic's demand to replicate the same analysis at 256×256 is scope creep.
- **Heuristic L_i ≥ 5 not rigorously justified.** This is a practical heuristic common in the literature. Not every heuristic requires a proof.
- **CFG sweep differences not discussed.** The critic questioned whether different optimal CFG weights reflect meaningful representation differences. This is speculative and the paper's presentation of the full sweep curves lets readers draw their own conclusions.
- **Compression cost "only requirement" oversimplification.** The paper references M2T for details, which is standard practice.
- **Missing related works.** Hard rule prohibits this as I cannot verify completeness.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Revise the abstract's claimed degradation range** to either include the colorization result (~3.85%) or explain why it is an outlier.
2. **Remove or support the "Semantics" paragraph** (lines 416–417). As written, the claim is an opinion without evidence.
3. **Add variance estimates for MaskGIT results** or explicitly note that they are single-run comparisons.
4. **Qualify the "drop-in replacement" language** in the introduction to match the paper's own more precise description in the method section.
5. **Consider adding a brief limitations section** discussing scenarios where FSQ might be less suitable than VQ.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>
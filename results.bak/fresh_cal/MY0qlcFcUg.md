Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

## Summary

This paper introduces Denoising Task Routing (DTR), a channel-masking add-on for diffusion models that explicitly establishes task-specific information pathways within a single architecture. DTR encodes two priors about denoising tasks — Task Affinity (adjacent timesteps should share more channels) and Task Weights (higher timesteps need more capacity) — via a sliding-window mask whose shift rate is modulated by a power parameter α. Experiments on FFHQ, ImageNet, and MS-COCO with DiT and ADM architectures show consistent FID/IS/Precision/Recall improvements and accelerated convergence, with zero added parameters.

## Strengths

- **Consistent gains across multiple architectures, datasets, and generation paradigms**: Tables in Section 5 show DTR improves DiT and ADM on unconditional (FFHQ), class-conditional (ImageNet), and text-to-image (MS-COCO) settings. The gains hold across all reported metrics (FID, IS, Precision, Recall), not just one. This directly validates the paper's core claim of broad applicability.

- **Convergence speed is approximately doubled**: Figure 5 and Section 5.3 report that DiT-B/2 with DTR reaches FID 31 in 200K iterations, whereas the baseline requires 400K — a clean 2× speedup. The paper further shows DTR accelerates models already using MTL loss-weighting methods (Min-SNR, ANT-UW), suggesting the architectural and optimization approaches are complementary.

- **Random routing degrades performance, motivating the structured design**: Section 4.2 and the comparative evaluation (Table 1) show that naive random routing (R-TR) hurts performance relative to the baseline, while DTR improves it. This is important evidence that the prior-aware design, not just any form of routing, is responsible for the gains.

- **Ablation study for α and β hyperparameters**: Section 5.3 systematically varies α and β, showing that α=4, β=0.8 are robust choices and that the method improves performance at all DiT scales (S, B, L), with larger models benefiting more.

- **Compatibility with MTL loss-weighting techniques**: Table 2 and Figure 3 demonstrate that DTR can be combined with ANT-UW and Min-SNR for further gains in class-conditional generation, and can essentially replace loss weighting in the unconditional setting. This shows the architectural and optimization approaches address complementary aspects of MTL.

## Weaknesses

### Fatal

None.

### Major

1. **Headline efficiency claim is not fully substantiated in the main text.** The abstract and Section 5.2 claim that DiT-L/2 + DTR + ANT-UW "outperforms vanilla DiT-XL/2 and rivals DiT-XL after 7 million iterations." The main text reports FID 2.33 for the DTR-based method at 2M iterations, but does **not** report the corresponding FID numbers for vanilla DiT-XL/2 at 7M or DiT-XL at 7M. The comparison table is relegated to Appendix Table `app:tab:long_iter`. This is the paper's strongest single claim, and a reader cannot evaluate whether "matched performance" is an accurate characterization from the main text alone. The authors should either bring the comparison table into the main paper or explicitly state the FID values for all methods in the main text.

2. **Multi-experts comparison lacks numerical results.** Section 5.3 includes a subsection "Comparison to multi-experts strategy" stating "we show that DTR outperforms the multi-experts denoiser method," but no table, figure, or numerical result accompanies this claim in the main body. A multi-expert denoiser (e.g., using separate smaller models per timestep range) is a natural architectural alternative, and omitting the quantitative comparison limits the paper's ability to argue that DTR is the preferred approach. The results should be either summarized in the main text or presented in a table.

### Minor

3. **The mechanism of "reduced negative transfer" is supported only indirectly.** The paper argues that DTR reduces negative transfer by separating channels per timestep. The CKA analysis (Figure 6) shows that DTR produces different representational similarity patterns than baselines, which is consistent with the design, but does not directly measure gradient conflict or transfer efficiency. The paper would be strengthened by a more direct diagnostic (e.g., measuring gradient conflict before/after DTR), though the current evidence is still useful and the claim remains reasonable.

4. **No limitations or tuning cost discussed.** The paper does not address the cost of tuning α and β for a new architecture or dataset, nor does it discuss scenarios where DTR might not help. While the ablation shows robustness, a brief discussion of limitations would strengthen the paper.

### Trivial

5. **The paper does not explicitly state whether the same mask is used for all residual blocks or varies per block.** Equation (2) uses `m_{D_t}` subscripted only by timestep (not by block index), implying a global mask per timestep. Making this explicit would improve clarity.

## Nice-to-Haves

- The CKA analysis (Figure 6) would benefit from a quantitative summary (e.g., average CKA per block per timestep range) alongside the heatmaps.
- A brief verification of the `α=4, β=0.8` choice on one additional architecture/setting beyond DiT-B/2 would further increase confidence in the hyperparameter transferability.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Mask creation formula is underspecified"**: Removed. Equation (1) clearly specifies the sliding window as `⌊(C−Cβ)·((t−1)/T)^α⌉ < c ≤ ⌊(C−Cβ)·(t/T)^α⌉ + Cβ`. The formula is mathematically precise, and the accompanying text explains the behavior for α < 1, α = 1, and α > 1. The critic's description of the formula actually matches what is written.
- **"CKA figure is difficult to read"**: Removed. This is a PDF-extraction artifact; the original submission likely has a readable figure.
- **"No confidence intervals or multiple seeds"**: Removed. Single-run evaluation is standard practice for large-scale diffusion model benchmarks, and this criticism is a generic one-size-fits-all point.
- **"Hyperparameter tuning restricted to DiT-B/2, not validated on other settings"**: Removed. The paper conducts a systematic ablation on DiT-B/2 (Tables `mask_init_abl`, `scalability_abl`) and then validates the chosen parameters across multiple datasets and architectures. This is standard practice.
- **"Missing related works"**: Removed per policy; I cannot verify the existence of missing citations.
- **"Missing appendix content / proofs"**: Removed per policy; appendices are commonly stripped during extraction and the original submission contains them.
- **Strengths removed**: None. All identified strengths are concrete and specifically grounded in the paper's content.

## Novel Insights

None beyond the paper's own contributions. However, one observation worth noting from synthesizing the reviews: the finding that DTR can effectively replace loss-weighting methods in unconditional generation while complementing them in class-conditional generation (Table 2) is an intriguing asymmetry that the paper surfaces but does not deeply explain. This could point to interesting differences in how architectural vs. optimization MTL approaches interact with conditioning signals — a direction for future work.

## Suggestions

1. Move the long-iteration comparison (Table `app:tab:long_iter`) into the main paper body, or at least report the DiT-XL/2 and DiT-XL FID numbers directly in the text when stating the "matched performance" claim.
2. Add a small table or in-text numbers for the multi-experts comparison.
3. Explicitly state whether the mask is shared across all residual blocks or computed per-block.
4. Add a brief limitations paragraph discussing the tuning of α and β.

## Score and Decision

**Overall assessment**: This is a solid paper with a well-motivated, simple, and effective contribution. DTR is easy to implement, parameter-free, and consistently improves generation quality and convergence speed across multiple architectures and tasks. The two major weaknesses (headline claim partially deferred to appendix, multi-experts comparison lacking numbers) are both fixable by including existing results in the main paper — they do not undermine the core contribution. The method is sound, the evaluation is otherwise thorough, and the results are clearly positive.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
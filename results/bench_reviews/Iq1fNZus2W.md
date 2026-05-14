Now I have all the information needed. Let me synthesize the final review.

---

## Summary

This paper addresses the computational bottleneck of multi-condition control in Diffusion Transformers caused by the "concatenate-and-attend" strategy. The authors analyze attention sparsity patterns in existing DiTs, showing that spatial conditions concentrate on the diagonal and subject conditions activate only keyword-relevant regions. They propose PKA, which decomposes full attention into two efficient modules: Position-Aligned Attention (PAA) for spatial conditions and Keyword-Scoped Attention (KSA) for subject conditions, complemented by a Condition Cache and an early-timestep sampling strategy. The method achieves up to 10× inference speedup and 5.12× attention-module VRAM reduction while maintaining or improving generation quality.

## Strengths

- **Strong empirical motivation from attention sparsity analysis**: Figures 2 and 3 provide direct visual evidence that full attention is redundant for spatial-aligned conditions (diagonal concentration) and subject-driven conditions (sparse, keyword-correlated activations). This observation cleanly motivates the modular design of PAA and KSA.
- **Significant and well-measured efficiency gains**: PKA delivers up to 10× inference speedup (Figure 7, measured across condition counts on the same hardware) and up to 5.12× attention-module VRAM reduction (Figure 8), directly validating the paper's main efficiency claim.
- **Clean architectural decomposition with Condition Caching**: Separating spatial and subject conditioning into two attention modules, each tailored to a distinct sparsity pattern, is conceptually neat. The structural choice that condition tokens only perform self-attention among themselves—enabling one-time KV computation per denoising trajectory—is a pragmatic engineering insight that amplifies speedup beyond attention pruning alone.
- **Quantitative evaluation across multiple tasks and metrics**: Table 1 evaluates FID, SSIM, F1, MSE, CLIP-I, DINOv2, and CLIP-T across three multi-conditional tasks, showing that the method matches or surpasses OminiControl2 and UniCombine on generation quality and subject consistency.
- **Scalability demonstrated to 2–4 simultaneous conditions**: Appendix A.4 (Figures 14–16) shows robust generation with multiple conditions (e.g., subject+sketch+depth), indicating the design scales beyond the tested tasks.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **PAA and KSA ablations rely primarily on qualitative evidence and efficiency metrics**: Section 4.3.1 (PAA) compares latency and VRAM across full attention, PAA, and Sliding Window Attention with visual examples (Figure 9), but reports no quantitative quality metrics (FID, SSIM, etc.) for this ablation. Similarly, Section 4.3.2 (KSA) uses a single image example (Figure 10) to illustrate the epsilon trade-off. The full system IS evaluated quantitatively in Table 1, so the core claims are supported, but the component-level ablations would be stronger with test-set metrics. The authors could address this in rebuttal.

- **Early-timestep sampling contribution is not isolated in the final evaluation**: The training convergence curves (Figure 13, Appendix) and qualitative snapshots (Figure 11) demonstrate the benefit of early-timestep sampling for training, but Table 1 does not include an ablation row comparing PKA with vs. without this strategy. This makes it difficult to determine how much of the final quality improvement comes from the attention architecture versus the training strategy. The existing evidence is suggestive but not conclusive.

- **VRAM savings measured on attention module only**: The paper reports attention-module VRAM reduction (5.12×) and clearly labels this as such. However, end-to-end VRAM usage is not reported. In a full DiT pipeline, non-attention components (feature tensors, activations, MLP layers) consume significant memory, so the practical overall savings may be smaller. Reporting total GPU VRAM would ground the "resource-friendly" claim more concretely. This is clearly scoped in the text but worth addressing.

- **The observed attention sparsity patterns come from a trained full-attention model**: The diagonal concentration (Figure 2) and keyword sparsity (Figure 3) that motivate PKA are observed in a model *trained with full attention*. The model may have learned local attention because it was sufficient under full connectivity; this does not guarantee that restricting to local attention during training would yield equivalent results. The paper mitigates this concern by fine-tuning (not training from scratch) and by showing strong quantitative results, but a brief discussion would strengthen the methodological justification.

### Trivial

- The KSA mask computation and reuse assumption (temporal consistency) could benefit from a brief analysis of mask quality across early, middle, and late denoising stages—e.g., how does the mask at early timesteps (when the image is largely noise) compare to later timesteps?

## Nice-to-Haves

- Reporting end-to-end VRAM and latency under identical settings (batch size, resolution, denoising steps) would make the practical resource claims more concrete.
- A quantitative sweep of KSA threshold epsilon with CLIP-I/DINOv2 across a test set would transform the single-image anecdote (Figure 10) into a credible efficiency-quality trade-off curve.
- Discussing or experimenting with non-pixel-aligned spatial conditions (e.g., bounding boxes, semantic layouts spanning multiple patches) would clarify the method's scope.
- Discussion of compatibility with complementary efficiency methods like PixelPonder-style token pruning.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Table cells are empty in the parsed text"** — This is a PDF parser artifact. The original submission has complete numerical data in Table 1. Not held against the paper.
- **"The paper does not provide standard deviations, significance tests, or confidence intervals"** — The harsh critic could not see the table data due to parser issues. For large-scale generation benchmarks with single-run evaluation, confidence intervals are not standard practice. Not held against the paper.
- **"10× speedup claim likely extrapolates to higher condition counts"** — The paper shows the speedup trend across condition counts in Figure 7, and the claim is clearly stated as "up to 10×." The paper does not misrepresent this.
- **"The paper does not discuss how early in the denoising process the mask is first computed" (reproducibility concern)** — This is a minor implementation detail; the method is clearly described and the mask computation follows the two-step process in Section 3.2.2.
- **"The assumption that a keyword can reliably locate subject regions across diverse phrases... is not examined"** — The paper provides qualitative evidence (Figures 3, 10) and the full system's quantitative results in Table 1 include strong subject consistency metrics (CLIP-I, DINOv2), which indirectly validates this assumption.

## Novel Insights

The decomposition of multi-condition attention into two distinct sparsity patterns (spatial-aligned diagonal sparsity vs. subject-driven keyword-scoped sparsity) is a genuinely useful observation. Rather than treating all conditions uniformly, the paper shows that condition type determines the appropriate sparsity structure, and designing specialized attention modules per condition type yields both cleaner architecture and better efficiency than generic approaches. The Condition Cache insight—that condition tokens only need self-attention, enabling one-time KV computation—is a simple but practically impactful engineering contribution that other multi-condition DiT methods could adopt.

## Suggestions

- Add a row to Table 1 showing PKA without early-timestep sampling, to isolate the contribution of the training strategy.
- Report quantitative quality metrics (at minimum FID and a consistency score) for the PAA vs. SWA ablation in Section 4.3.1, even if on a subset of the test set.
- Include a brief discussion in the Method section acknowledging that the observed sparsity patterns come from a full-attention-trained model and why fine-tuning still benefits from the restricted attention design.
- Report total end-to-end GPU VRAM consumption to complement the attention-module numbers, or explicitly scope the claim if this is impractical.

---

## Score and Decision

**Anchor comparison:**

- **MixDiffusion** (`t9Wx3W2B0x`, avg 3.00, Reject): Training-free multi-condition method with theoretical issues, missing comparisons, and practical limitations. The current paper is substantially stronger—it has a trained method with clear efficiency gains, proper baselines, and quantitative evaluation.
- **DiffSparse** (`V3eUas3VCL`, avg 4.50, Accept Poster): Token sparsity method for DiTs with good efficiency but incomplete analysis of computational overhead and limited generalization. The current paper has clearer motivation (attention sparsity analysis) and comparable or better experimental validation for its specific domain.
- **CreatiDesign** (`Wtda8HpVp2`, avg 5.00, Accept Poster): Multi-condition DiT for graphic design with strong dataset contribution. Similar quality level—creatively addresses a real problem with reasonable but not exhaustive experiments. The current paper's efficiency contribution is more clearly quantified.
- **SLA** (`eD8IPvNoZB`, avg 5.00, Accept Poster): Sparse-linear attention for DiTs with well-engineered GPU kernels and 95% attention computation reduction. Comparable in ambition and validation quality. SLA has stronger kernel implementation; the current paper has a more novel condition-type-aware decomposition.
- **SPRINT** (`aTVollXaaI`, avg 5.50, Accept Poster): Sparse-dense fusion for DiT training with 9.8× training savings and strong ablations. SPRINT has more comprehensive experiments and ablations; the current paper has a comparable-quality contribution but with somewhat weaker component-level ablations.
- **DUPA** (`ALpn1nQj5R`, avg 5.50, Accept Poster): Self-alignment for DiT training with FID=1.46 on ImageNet. Strong method with clear results but scope limited to ImageNet. The current paper addresses a different problem (multi-condition control) with competitive validation quality.

The paper under review makes a genuine contribution—a well-motivated, clean architectural solution to a real efficiency bottleneck in multi-condition DiTs. The efficiency gains are substantial and well-measured, and the full-system quantitative results are competitive. The primary weakness is that some component-level ablations rely on qualitative evidence rather than test-set metrics, and the early-timestep sampling contribution is not isolated in the final evaluation. These are addressable and do not undermine the core claims, but they prevent the paper from reaching the top tier. Positioned between DiffSparse/CreatiDesign and SPRINT/DUPA in validation thoroughness.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
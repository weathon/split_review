Here is my consolidated final review.

---

## Summary

This paper proposes **Ross**, a training framework that adds *vision-centric* supervision to Large Multimodal Models (LMMs) by having the model reconstruct input images (specifically, denoise latent tokens from a frozen VAE) conditioned on its own visual outputs. This "intrinsic activation" approach is contrasted with "extrinsic assistance" methods that aggregate multiple visual experts. The paper demonstrates consistent gains across architectures (CLIP/SigLIP, Vicuna/Qwen2), especially on fine-grained and hallucination benchmarks, and shows that a single-encoder Ross-7B outperforms multi-expert Cambrian-1-8B on 6 of 8 benchmarks.

---

## Strengths

1. **Novel and principled supervision signal.** Unlike conventional LMMs that supervise only text outputs, Ross directly supervises visual outputs via reconstruction of input images (Section 3). This is a clean departure from both LLM-centric and extrinsic-assistance paradigms, and the motivation — that visual outputs carry rich information not captured by text supervision — is well-articulated.

2. **Systematic ablation identifies the critical design choices.** The paper methodically ablates reconstruction targets (pixel → latent) and objectives (regression → denoising), showing that latent denoising with a KL-16 VAE tokenizer consistently outperforms alternatives (Figures 3–5, Section 4.1). The progression cleanly validates that handling spatial redundancy is the key challenge, and denoising is the right solution.

3. **Consistent improvements across multiple architectures.** Ross improves every combination of visual encoder (CLIP, SigLIP) and LLM (Vicuna-7B, Qwen2-7B) tested, with large gains on fine-grained benchmarks like MMVP (+8.6 to +12.6 points) and ChartQA (+1.9 to +6.9 points) (Table 2, tab:llm). This breadth supports the claim that the benefit is systematic, not architecture-specific.

4. **Competitive performance against multi-expert systems with a single encoder.** Ross-7B (SigLIP only) outperforms Cambrian-1-8B (aggregating four visual experts) on HallusionBench (57.3 vs. 48.7), MMVP (54.7 vs. 51.3), MMBench (79.0 vs. 75.9), and other benchmarks (Table 3). This concretely demonstrates the paper's central thesis that intrinsic activation can match or exceed extrinsic assistance.

5. **Attention analysis provides mechanistic evidence.** Quantitative analysis shows significantly higher mean/median attention scores to visual tokens for Ross vs. LLaVA (p-values < 1.3e-7, Table 1), with qualitative maps aligning to relevant image regions (Figure 6). This supports the claim that reconstructive supervision improves visual focus.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The depth-map transfer experiment underspecifies the MiDaS integration.** Section 4.3 compares Ross with an "extrinsic assistance" baseline (LLaVA + MiDaS) to argue that Ross can leverage depth maps while extrinsic methods cannot. However, the paper does not describe *how* MiDaS is integrated into the LMM — as an additional visual encoder with a connector? Do its features replace or supplement CLIP features? Are they concatenated at the token level? Without this detail, the comparison is uninterpretable: the failure of LLaVA+MiDaS with RGB+D inputs (62.1 → 60.0) could stem from a poor integration design rather than a fundamental limitation of extrinsic assistance. This undermines one of the paper's narrative claims about intrinsic vs. extrinsic activation. The main within-model comparison (Ross RGB vs. Ross RGB+D, +8.4 points) is clean and stands on its own, but the MiDaS comparison needs clarification or removal.

2. **The generative-vs-reconstructive comparison has an asymmetric data transformation step.** Section 4.2 compares Ross (reconstructive) with a generative variant using learned latent queries. The generative variant requires transforming caption data into text-to-image "creation" data via GPT-4o; the paper does not describe this transformation or verify its quality. The reconstructive variant uses the same caption data directly. Since the generative variant could be hurt by poor-quality transformed data rather than by the generative objective itself, the conclusion that "reconstructive objectives boost comprehension while generative alternatives cannot" is somewhat overclaimed. The paper acknowledges the data-format limitation but does not validate the transformation quality.

3. **The main comparison with Cambrian-1 uses different training data composition.** Ross-7B uses 2M caption + 1.2M instruction data (ShareGPT4V + ALLaVA + Cambrian-737K + SMR-473K), while Cambrian-1-8B uses 7M instruction data. The paper frames this as data efficiency, which is fair, but does not discuss the confound that different data *sources* (not just quantity) may differ in quality or benchmark alignment. The controlled ablations within the paper's own framework (Section 4.1) already demonstrate the method's value independent of this comparison, so this does not threaten the core contribution, but it tempers the headline comparison.

4. **Denoiser architecture description is ambiguous.** The paper states that each denoiser block has "three linear projection layers and a standard self-attention block" (line 244) and "three extra projections for conditions, inputs, and timesteps" (line 250). However, it does not explain how these projected representations are combined before the self-attention — are they concatenated, summed, or used as cross-attention? The diagram (Figure 4b) appears to suggest concatenation, but the text should be self-contained. This does not affect the validity of the results but hinders reproducibility.

### Trivial
- None that survive filtering.

---

## Nice-to-Haves

- **Training overhead discussion.** The denoiser is used only during training. Reporting its parameter count and training FLOPs overhead would help practitioners assess the cost.
- **Broader hallucination evaluation.** Adding CHAIR (caption-based) or AMBER would strengthen the hallucination claim beyond POPE and HallusionBench, which is known to correlate with visual reasoning difficulty.
- **Denoiser capacity ablation.** A brief study varying denoiser depth/size would guide future work on how much capacity is needed.

---

## Removed Points

These points were flagged for removal. Treat them with caution; they do not appear in the final assessment.

- *Criticism about the paper not reporting confidence intervals or distribution shapes for attention analysis.* The paper already reports quantitative stats (mean, median, percentiles, p-values) which are appropriate for this analysis. Qualitative maps supplement it.
- *Criticism that qualitative depth examples could be cherry-picked.* The paper provides quantitative results (Table 4) alongside the qualitative examples. This is a generic concern applicable to any paper with qualitative figures.
- *Criticism about missing inference-time analysis, limited hallucination benchmarks, and denoiser ablation.* These have been moved to Nice-to-Haves above — they are wishlist items, not actual weaknesses.
- *Criticism implying the generative-vs-reconstructive comparison is "evidentially weak."* The paper acknowledges the data-format difference transparently; the comparison is suggestive and properly scoped.
- *Strength claiming "transfer learning experiment shows Ross enables effective depth map understanding."* This strength is retained in the main review (it is supported by the data). The criticism about MiDaS integration is about the *extrinsic* comparison, not about Ross's own improvement.

---

## Novel Insights

The reviews surface the following insight beyond the paper's own contributions: The paper's central tension is between its clean *intrinsic* claim (supervise visual outputs → better comprehension) and its somewhat overextended *extrinsic vs. intrinsic* narrative. The reviewers agree that the core methodological contribution — reconstructive supervision via latent denoising — is novel and well-supported by the controlled ablations. However, the claimed advantage over extrinsic-assistance methods is weaker than presented because (1) the MiDaS integration baseline is underspecified, and (2) the main comparison uses different training data. The honest contribution of this paper is "a new and effective self-supervised objective for LMM visual outputs" rather than "proof that intrinsic activation beats extrinsic assistance," and the paper would be stronger if the claims were scoped accordingly.

---

## Suggestions

1. **Clarify the MiDaS integration in the depth experiment** — describe whether features are concatenated at the token level, as an additional encoder, or other. If the integration was ad-hoc, consider removing the extrinsic comparison and keeping only the clean within-model comparison (Ross RGB vs. Ross RGB+D), which already makes the point that Ross can learn to use depth maps.
2. **Validate or remove the generative comparison** — either describe the GPT-4o transformation in detail with quality checks, or soften the claim to "preliminary evidence that generative objectives do not help comprehension."
3. **Add a caveat about data composition** when comparing with Cambrian-1 — acknowledge that different data sources could contribute to the performance gap, even if the data efficiency advantage in terms of quantity is real.
4. **Clarify the denoiser architecture** — specify how projected conditions, inputs, and timestep embeddings interact with the self-attention block (concatenation? addition?).

---

## Score and Decision

The paper presents a novel, well-motivated approach to supervising visual outputs in LMMs. The core idea is sound, the ablations are thorough, and the results are consistent and meaningful. The weaknesses are all addressable — the depth experiment integration can be clarified or scoped down, the generative comparison can be caveated, and the data confound in the main comparison does not undermine the within-paper controlled experiments. The paper's main narrative about "intrinsic vs. extrinsic" is somewhat overclaimed given these issues, but the methodological contribution stands on its own.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
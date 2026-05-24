Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper addresses the computational bottleneck of multi-condition control in Diffusion Transformers (DiTs), where the "concatenate-and-attend" strategy makes attention costs scale quadratically with the number of condition tokens. The authors propose Patch-wise and Keyword-Aware Attention (PKA), which decomposes full attention into two specialized modules: Position-Aligned Attention (PAA) for spatial conditions (one-to-one per-patch, O(N) complexity) and Keyword-Scoped Attention (KSA) for subject-driven conditions (masked to keyword-relevant regions). A condition KV cache and an early-timestep sampling strategy for fine-tuning complement the framework. Experiments on FLUX.1 demonstrate up to 10× inference speedup and 5.12× VRAM reduction in the attention module, with competitive quality metrics against OminiControl2 and UniCombine.

## Strengths

1. **Well-motivated decomposition of attention by condition type.** The paper provides visual evidence (Figures 2-3) that spatial conditions exhibit diagonally-concentrated attention while subject-condition attention maps are sparse and keyword-localized. This observation directly motivates PAA (one-to-one per-patch) and KSA (masked attention), giving the architecture a principled foundation rather than relying on generic pruning heuristics.

2. **Large and clearly measured efficiency gains.** Figures 7-8 show up to 10× inference speedup and 5.12× VRAM reduction in the attention module when scaling from 1 to 16 conditions, with each condition using 1024 tokens. These numbers are measured on a single RTX 6000 Ada GPU against the full-attention baseline (UniCombine), and the trend shows that the advantage grows with the number of conditions — exactly where the problem is most severe.

3. **Ablation studies isolate PAA and KSA contributions.** Figure 9 shows PAA reduces latency from 15.38s to 13.63s and VRAM from 308MB to 237MB versus full attention, beating sliding-window alternatives. Figure 10 shows KSA with ε=0.4 cuts latency from 16.99s to 15.26s and VRAM from 368MB to 242MB while preserving subject appearance. These controlled experiments confirm that each component delivers its promised efficiency gain independently.

4. **Perturbation analysis justifies a non-trivial training improvement.** Figure 5 demonstrates that corrupting early (high-noise) timesteps causes a much larger SSIM drop (0.50→0.34) than corrupting late timesteps, revealing that visual conditions exert strongest influence early in denoising. The resulting early-timestep sampling strategy (shifted logit-normal) is a clean, well-motivated contribution that accelerates fine-tuning convergence.

5. **Condition KV cache is a simple but impactful add-on.** Because condition tokens only self-attend within their own group (a structural choice of PKA), their Keys and Values can be computed once at the first denoising step and cached thereafter. This is orthogonal to PAA/KSA and provides additional savings across the denoising trajectory.

## Weaknesses

### Fatal
None.

### Major

1. **Uncontrolled quality comparison against baselines undermines Table 1.** The paper writes: "To ensure a fair comparison, we fine-tune the FLUX.1 model using LoRA (Hu et al., 2022)" (Section 4.1, training details). But then for evaluation: "We employ OminiControl2 (Tan et al., 2025) and UniCombine (Wang et al., 2025) as baselines" — with no indication that these baselines were also fine-tuned under identical conditions (same data, same LoRA setup, same iterations). Since OminiControl2 and UniCombine are also built on FLUX.1, the quality improvements in Table 1 (e.g., FID 61.03→52.99, SSIM 0.493→0.553 on Subject-Canny) could partially or fully stem from the additional fine-tuning rather than the PKA architecture itself. **This does not invalidate the efficiency claims** (Figures 7-8 compare architectural efficiency, which is independent of fine-tuning), but it means the claim of "maintaining or improving generative quality" (line 19, line 59) is not convincingly supported by Table 1 as presented.

2. **SSIM and FID computed against ground-truth images favor reconstruction over diversity.** The paper computes FID and SSIM "between the generated and ground-truth image sets" (Section 4.1). A model fine-tuned on the specific Subject200K subset will naturally achieve higher SSIM and lower FID when evaluated against those same ground-truth images, because fine-tuning biases it toward reconstructing the training distribution. A model that generates diverse but condition-consistent images is penalized. While CLIP-I and DINOv2 are more appropriate for subject consistency, and the controllability metrics (F1, MSE) are defensible, the overall "quality" framing via SSIM/FID is biased in the paper's favor.

### Minor

3. **KSA relies on curated keywords with no automatic extraction mechanism.** The paper curates a subset of Subject200K where "each image caption contains a descriptive keyword" (Section 4.1), and KSA uses these 1-2 known keyword tokens to compute the mask. No mechanism is provided (or evaluated) for automatically extracting keywords from arbitrary prompts. This limits the method's applicability to settings where keyword-relevant captions are guaranteed, and it is unclear how performance degrades when keyword localization is imperfect or when the subject is described by multiple tokens (e.g., "the brown leather armchair").

4. **Condition KV cache assumption is not validated.** The cache reuses condition Keys and Values from the first denoising step for all later steps (Section 3.2). This assumes condition token representations do not need to adapt to different noise levels. No ablation compares cached vs. non-cached condition representations for quality. If condition representations should depend on the current image state (e.g., to modulate detail injection at different noise levels), caching could degrade control fidelity — a concern the paper does not address experimentally.

5. **The F1 score on Subject-Canny is 25% lower than UniCombine (0.414 vs. 0.551), described as a "narrow margin."** In Table 1, UniCombine achieves F1=0.551 while the paper's method reaches 0.414. The text describes this as "highly competitive" with a "minor exception of a narrow margin." A 25% relative drop on edge controllability is not a narrow margin; it suggests PAA may lose spatial detail for edge conditions. This should be honestly acknowledged.

6. **Sparsity analysis is purely qualitative.** Figures 2-3 show attention maps visually, but no numerical sparsity ratios (e.g., percentage of attention weights below a threshold) are reported. The claim that "a significant portion of attention computation is indeed redundant" (Section 1) would be strengthened by quantitative support.

7. **Early-timestep sampling ablation is visual-only.** Figure 11 shows generated images at different iteration counts for various μ/δ values, but no quantitative metrics (FID, CLIP-I, convergence curves) are reported. This makes it hard to assess the statistical significance or magnitude of the improvement.

8. **The paper does not discuss limitations.** The conclusion (Section 5) mentions extending to video generation as future work but does not acknowledge any limitations of the current method: the reliance on keyword curation, the potential degradation of edge controllability, or the assumption of spatial alignment between condition and image tokens.

### Trivial
None.

## Nice-to-Haves

- Report end-to-end latency and VRAM (not just attention module) to contextualize the 10× and 5.12× claims.
- Provide a per-component efficiency breakdown that isolates: (1) full attention baseline, (2) full attention + condition cache only, (3) PAA only, (4) KSA only, (5) PAA+KSA+condition cache. This would clarify how much each mechanism contributes.
- Evaluate KSA with automatic keyword extraction (e.g., using an LLM or parser) on a non-curated dataset to test generalizability.
- Add a failure case analysis (e.g., scenes where the subject occupies most of the image, or where the spatial condition has repetitive patterns).

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Short training schedule (20k iterations)" (Harsh Critic)**: The critic questions whether baselines were given comparable computation. This is a reasonable concern about repro due diligence but is secondary to the main baseline fairness issue already listed as Major #1. The 20k iteration fine-tuning with LoRA is within normal range for adapter-based fine-tuning — the real issue is whether baselines were fine-tuned at all, not the specific schedule length.
- **"Speedup conflates three separate mechanisms — no per-component ablation"**: This is partially incorrect. The paper does ablate PAA and KSA separately in Figures 9-10. However, the condition cache contribution is not isolated. The remaining valid sub-point (condition cache not separately ablated) is folded into Minor #4.
- **"The speedup statement in the abstract is not qualified as being for the attention module only"**: The abstract says "attention module VRAM" and "inference speedup." While not perfectly precise, this is a framing and formatting issue that doesn't affect the paper's technical content.
- **Several generic "missing experiments" from the harsh critic's "Deeper Analysis" section** — these are speculative suggestions, not concrete weaknesses. Relevant ones are captured in Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's fundamental observation — that quality comparisons are confounded by unequal fine-tuning — is the most important underlying issue, but it is a standard methodological concern rather than a novel insight about the paper's content.

## Suggestions

1. **Clarify baseline training status.** State explicitly whether OminiControl2 and UniCombine were fine-tuned under identical conditions (same data, same LoRA, same iterations) or used off-the-shelf. If they were not fine-tuned, either retrain them for a fair comparison or reframe Table 1 as measuring the combined effect of PKA + fine-tuning (rather than PKA alone). Quality claims should be separated from efficiency claims.

2. **Replace or supplement SSIM with a diversity-tolerant metric.** Use a metric that does not penalize diversity (e.g., FID only for distribution comparison) or report SSIM against the condition input rather than the ground-truth image.

3. **Add quantitative sparsity numbers.** Report the percentage of attention weights below a threshold (e.g., 0.01) for spatial and subject conditions to support the qualitative claims in Figures 2-3.

4. **Validate the condition cache assumption.** Add an ablation comparing quality metrics with and without the condition cache (with the cache disabled, recompute K/V at every step).

## Score and Decision

**Calibration anchors (from retrieval):**

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/N8Oj1XhtYZ.md (SANA) | 8.50 | Far stronger: comprehensive system with multiple innovations, extensive evaluation, strong writing. PKA is narrower in scope. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/uJqKf24HGN.md (UniCon) | 7.00 | Stronger: clean architecture with well-controlled experiments. PKA has comparable efficiency motivation but weaker quality evaluation. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/lTrrnNdkOX.md (Qihoo-T2X) | 6.40 | Similar topic (efficient DiT attention). Qihoo-T2X had "insufficient experiments" weakness but cleaner evaluation. PKA has stronger efficiency claims but a more concerning baseline fairness issue. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/D2as3jDmRA.md (LinFusion) | 6.25 | Similar topic (linear attention for diffusion). LinFusion was rejected despite good evaluation. PKA's baseline fairness issue is more severe. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/leBbjaUxut.md (MDiT) | 5.00 | Similar topic (DiT efficiency + training speedup). MDiT had mixed reviews (scores 3,3,6,8). PKA's efficiency story is stronger, quality evaluation weaker. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/taHwqSrbrb.md (DyDiT) | 5.50 | Similar topic (dynamic DiT). Accepted despite some unanswered questions. PKA has more open methodological concerns. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/kALZASidYe.md (Enhanced Controllability) | 3.75 | Weaker: vague method, unclear contribution. PKA is more concrete and better-motivated. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/Jt1gGIumJo.md (Highlight Diffusion) | 3.00 | Weaker: modest 1.52× speedup with quality degradation. PKA's 10× speedup is far more impressive. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/lvgsPjRtLM.md (VideoDiT) | 2.50 | Weaker: small-scale reconstruction evaluation, missing baselines. PKA is more complete. |

The paper's core efficiency idea (PKA) is well-motivated and the efficiency results are solid. However, the quality evaluation has a significant methodological flaw (uncontrolled baseline comparison, metric choice bias) that prevents the paper from convincingly supporting the claim that quality is "maintained or improved." This issue is major but not fatal — the efficiency contribution stands on its own, and the problem is fixable with a revised evaluation. Relative to anchors, the paper sits below cleanly-executed work like UniCon (7.00) but above substantially weaker papers like VideoDiT (2.50) or Highlight Diffusion (3.00). It is most comparable to Qihoo-T2X (6.40) and DyDiT (5.50) in ambition, but held back by the evaluation concerns.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
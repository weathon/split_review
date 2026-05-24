Now I have enough calibration context. Let me write the consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

The paper presents ARSS, a decoder-only autoregressive transformer for novel view synthesis from a single image with camera control. It combines a video tokenizer (for temporally consistent visual tokens), a camera autoencoder (encoding Plücker raymaps into 3D positional guidance tokens), and a hybrid token permutation strategy that shuffles spatial tokens while preserving temporal causality. On RealEstate10K, ACID, and zero-shot DL3DV, ARSS achieves competitive or best results on PSNR, LPIPS, and FVD among compared methods.

## Strengths

- **First decoder-only AR model for NVS with camera control.** The paper pioneers the application of GPT-style causal transformers to multi-view synthesis, demonstrating that the paradigm works competitively with established diffusion-based methods. Table 1 shows ARSS achieves the highest PSNR on RealEstate10K (19.02) and ACID (21.93), and the lowest LPIPS (0.269 and 0.265) among methods including SEVA, Genwarp, and LVSM. The zero-shot DL3DV evaluation (PSNR 16.70, SSIM 0.449) further demonstrates generalization to unseen data distributions.

- **Hybrid token permutation validated by clean ablation.** Table 2 and Figure 7 convincingly show that the proposed strategy (spatial shuffle, temporal preserved) substantially outperforms both raster-order (no shuffle) and full permutation (spatial + temporal shuffle). The PSNR gap over raster is nearly 3 dB (19.22 vs. 16.29), and the visual comparisons clearly demonstrate the failure modes of the alternatives (geometric distortions in raster, incorrect ordering in full perm). This is a clear, internally valid ablation.

- **Video tokenization provides a large and well-documented improvement.** The ablation in Table 3 shows that switching from per-frame VQ image tokenization to the VidTok video tokenizer improves FVD by ~62% (137.68 → 52.56) and PSNR by 3.5 dB (15.69 → 19.22). This directly supports the paper's claim that temporal encoding is critical for multi-view sequences and is one of the strongest pieces of evidence in the paper.

- **Error accumulation analysis shows slower degradation.** Figure 6 demonstrates that ARSS maintains flatter per-frame PSNR/SSIM/LPIPS curves over 17-frame trajectories compared to baselines (MotionCtrl, RayZer, ViewCrafter, LVSM), providing concrete evidence that the causal AR structure does not compound errors faster than alternative approaches.

## Weaknesses

### Fatal
None.

### Major

1. **Camera autoencoder is claimed as a core contribution but never isolated or ablated.** The camera encoder is described as providing "3D positional instruction tokens" that are key to the method's performance. Yet there is no experiment that removes it, replaces it with a simpler conditioning mechanism (e.g., directly embedding camera extrinsics/intrinsics), or ablates it in any way. The only conditioning ablation (Table 2) varies token permutation, not the camera encoder itself. Without this, the reader cannot tell whether the camera tokens are providing meaningful 3D guidance, or whether the model relies primarily on the video tokenizer's temporal consistency and the spatial permutation strategy. This is an evidential gap for a component the paper presents as a key design choice.

2. **The claimed causal/sequential advantage of AR models is never tested.** The introduction motivates AR models by arguing they can "incrementally extend and reuse existing generations when the trajectory changes" and that diffusion models "generate all the images simultaneously, which is hard to adapt to new input or generate based on accumulated knowledge." However, every experiment evaluates ARSS on fixed, pre-defined trajectories with predetermined frame counts. No experiment tests incremental generation, trajectory extension, or re-using previously generated views under trajectory modification. The evaluation only measures final image quality on the same static task that diffusion methods solve. This is a structural gap between the paper's framing and its evidence.

### Minor

3. **Baseline configuration is opaque and some comparisons are suspicious.** ViewCrafter (PSNR 12.67) and RayZer (PSNR 12.97) perform far below their reported capability in original publications. The paper does not describe whether baselines were re-run with standard settings or whether numbers are taken from existing papers, nor does it specify evaluation protocols (e.g., whether methods were adapted to single-view input when they were designed for multi-view). Without this transparency, the reader cannot assess whether the comparison is fair or staged.

4. **Ablation results are reported on a different test setup than the main table.** Table 2 reports "ours" PSNR 19.22, while Table 1 reports 19.02 for the same method on the same dataset. This discrepancy is not explained. If the ablations use a subset of data, this should be stated; if the underlying model differs, the main table's numbers cannot be directly attributed to the components the ablations study.

5. **SEVA, ARSS's strongest competitor, is excluded from key analyses.** SEVA achieves better SSIM and FID on RealEstate10K and ACID (Table 1), yet it is not included in the error accumulation analysis (Figure 6) and is excluded from the zero-shot DL3DV evaluation. This makes it difficult to assess whether ARSS's claimed advantages (slower degradation, generalization) hold against the method that gives it the most competition.

6. **Key implementation details are missing.** The camera autoencoder loss (Eq. 5) gives λ₁–λ₄ without any values or training schedule. The transformer architecture is described only by its dimension (1280) — number of layers, heads, and feed-forward dimension are not reported. The camera token latent dimension and the codebook size of the tokenizer are not specified. These omissions hinder reproducibility.

### Trivial
None — minor issues above are already appropriately categorized.

## Nice-to-Haves

- An experiment demonstrating trajectory extension or incremental view generation would directly validate the causal advantage the paper argues for.
- A controlled comparison on DL3DV that includes SEVA (if its license permits) would strengthen the zero-shot claims.
- Reporting inference speed or FLOPs would help position the method's practical trade-offs.

## Removed Points

- "Comparison against SEVA is incomplete because SEVA is not in DL3DV or error accumulation" — Kept as Minor (#5). Not removed.
- "Missing statistical significance / confidence intervals" — Removed. This is not standard practice for large-scale NVS benchmarks where single-run evaluation is the norm.
- "No inference speed or computational cost reported" — Moved to Nice-to-Haves. Relevant but not a standard requirement for this type of NVS paper.
- "The ablation table inconsistency is not explained" — Kept as Minor (#4). But softened from the critic's original framing.
- "SEVA exclusion from DL3DV is ambiguous" — Removed. The paper's note ("DL3DV was part of its training data, while for other methods it serves as zero-shot evaluation") is sufficiently clear: SEVA, ViewCrafter, and RayZer were trained on DL3DV data.
- Various formatting/style nitpicks — Removed per filtering rules.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Ablate the camera encoder.** Compare the full model against a variant that replaces Plücker-derived camera tokens with a simple MLP embedding of camera extrinsics/intrinsics, or removes camera conditioning entirely. This would validate a central design claim.
2. **Add an incremental generation experiment.** E.g., generate 8 views on a trajectory, then extend to 12 views by conditioning on the 8 already-generated views without retraining. This would directly demonstrate the unique advantage of the causal AR structure.
3. **Document baseline configurations transparently.** Describe the evaluation protocol for each baseline (single-view vs. multi-view input, resolution, checkpoint used) to allow readers to assess comparison fairness.
4. **Report transformer architecture details** (layers, heads, FFN dimension, total parameter count) for reproducibility.

## Score and Decision

**Round-1 bracket:** Based on the initial calibration search, I placed the paper in the 4.5–6.5 range by comparing it against anchors in the weak (<3.5), middle (3.5–7.5), and strong (>7.5) bands.

**Round-2 narrowing anchors (read in full):**
| Anchor | Score | Round | Comparison to ARSS |
|--------|-------|-------|-------------------|
| AR-1-to-3 | 5.00 | R2 | Both use AR for NVS. ARSS has broader evaluation (multi-dataset, zero-shot) and stronger results, but shares missing-ablation concerns. ARSS is clearly stronger. |
| Training-free Camera Control | 5.80 | R2 | Different domain (video camera control, not direct NVS). Higher score reflects cleaner evaluation. ARSS is comparable in quality but has more gaps. |
| GST (Where Am I...) | 6.25 | R2 | AR for spatial tasks. Mixed reviews; some concerns about overclaiming. ARSS makes more measured claims but has similar evaluation gaps. |
| FreeVS | 5.80 | R2 | Generative NVS for driving scenes. Accepted despite missing ablations and limited evaluation scope. Comparable rigor to ARSS. |
| 4DiM | 6.50 | R2 | Diffusion for 4D NVS. Stronger evaluation and more thorough ablations. ARSS is clearly weaker on evaluation rigor. |
| LVSM | 7.67 | R1 | Transformer-based NVS with thorough evaluation. ARSS is substantially weaker on evaluation depth and result quality. |
| NoPoSplat | 8.00 | R1 | Feed-forward 3D reconstruction. Unrelated approach with very strong evaluation. Not directly comparable. |

**Final assessment:** ARSS is a genuinely novel contribution (first AR model for NVS with camera control) with competitive results on standard benchmarks. The token permutation and video tokenizer ablations are solid. However, the paper has two significant gaps: the camera encoder (a core claimed contribution) is never isolated or ablated, and the stated motivation about causal/sequential advantages is never tested. Additionally, baseline configuration transparency is lacking, and the strongest competitor (SEVA) is excluded from key analyses. The paper sits below well-executed papers like 4DiM (6.5) and LVSM (7.67), comparable to FreeVS (5.8) in terms of rigor and result quality, and above AR-1-to-3 (5.0). The weaknesses are addressable but require non-trivial additional experiments.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
Here is my final consolidated review.

---

## Summary

The paper introduces ARSS, the first decoder-only causal autoregressive (AR) model for novel view synthesis (NVS) from a single image with explicit camera control. The system combines a video tokenizer (VidTok) for temporally consistent discrete tokens, a camera autoencoder that compresses Plücker raymaps into latent 3D positional tokens, and a hybrid token permutation strategy that shuffles spatial order within each frame while preserving temporal causality. The method is evaluated on RealEstate-10K, ACID, and zero-shot on DL3DV, achieving the best PSNR and LPIPS among all baselines on the in-domain datasets while remaining competitive with state-of-the-art diffusion-based approaches.

## Strengths

- **First decoder-only AR paradigm for NVS with explicit camera control.** The paper adapts a LlamaGen-style causal transformer to multi-view generation by inserting camera tokens as 3D positional instructions and using random spatial permutation. This is a genuinely novel framing of the NVS problem that opens a new direction beyond the prevailing diffusion-based approaches.

- **Video tokenizer ablation provides concrete evidence of temporal consistency gains.** Table 3 shows that using a video tokenizer (VidTok) instead of a VQ image tokenizer reduces FVD from 137.68 to 52.56 (~62% relative improvement), quantitatively isolating the contribution of temporal-aware tokenization.

- **Hybrid spatial-only permutation is cleanly motivated and ablated.** The paper explains why full spatial+temporal permutation and raster scan orders both fail (Table 2, Figure 7), and the proposed spatial-only strategy is shown to improve across all metrics. The qualitative visualization of failure modes in Figure 7 is informative.

- **Competitive quantitative results across multiple benchmarks.** ARSS achieves the highest PSNR and lowest LPIPS on both RealEstate-10K (19.02, 0.269) and ACID (21.93, 0.265), and leads all methods on the zero-shot DL3DV evaluation across all five metrics. Error accumulation analysis (Figure 6) shows flatter degradation slopes than four of five baselines.

- **Zero-shot generalization to out-of-distribution inputs.** Results on DL3DV (trained only on RealEstate-10K/ACID) and on AI-generated images (Figure 5) demonstrate reasonable robustness, supporting the method's generalizability.

## Weaknesses

### Major

- **SEVA (the most competitive baseline) is omitted from the error accumulation analysis (Figure 6).** The per-frame PSNR/SSIM/LPIPS plots compare ARSS against LVSM, MotionCtrl, RayZer, and ViewCrafter, but not against SEVA — the one method that beats ARSS on SSIM and FID on both RealEstate-10K and ACID. The paper's central claim about "consistently highest or near-highest" metrics and "slowest degradation" cannot be fully evaluated without SEVA in this figure. At a minimum, SEVA's per-frame curves should be added. This is not a fatal flaw — the existing comparison is still informative against the other methods — but it undermines the strongest claim in the paper.

- **Inconsistency between ablation results and main results.** Table 2 (token permutation ablation) reports PSNR=19.22, SSIM=0.565, LPIPS=0.294, FID=60.11 for the "ours" strategy. Table 1 (main results on RealEstate-10K) reports PSNR=19.02, SSIM=0.624, LPIPS=0.269, FID=47.60 for the same method. The SSIM differs by 0.059 (9.4% relative) and FID by 12.49 (21% relative). The paper does not state whether the ablation is evaluated on a different subset, with different sequence length, or under different conditions. This discrepancy needs to be explained — it is the difference between a reliable ablation and one that raises reproducibility concerns.

### Minor

- **Claims are overstated in places.** The abstract appropriately says "overall comparable to state-of-the-art," but the introduction (line 114–115) and discussion (line 490) state that the method "out-performs current state-of-the-art methods." Looking at Table 1, SEVA achieves better SSIM and FID on both RealEstate-10K and ACID, and also better FVD on ACID. The claim should be consistently framed as "competitive with" or "comparable to" state-of-the-art, with honest acknowledgment of metrics where ARSS trails.

- **No ablation isolating the camera autoencoder.** The camera tokens are a core design contribution, yet the paper provides no experiment comparing with/without camera tokens, or with simpler positional encodings (e.g., raw Plücker coordinates or sinusoidal position embeddings). The contribution of the learned 3D positional tokens relative to simpler alternatives is therefore unknown.

- **Token fusion mechanism is underspecified.** The paper states that camera tokens are "inserted before visual tokens" and the sequence is fed into the transformer, but does not explain how they are projected into the transformer's embedding space (same linear projection as visual tokens? separate projection? additive vs. concatenative?). This is a reproducibility gap.

- **Computational cost not reported.** The paper does not provide model parameter count, inference time per frame, or GPU-hours for training. For a method that claims practical advantages over diffusion (no iterative denoising), efficiency numbers would meaningfully support the case. The training setup (8×H100, 100K iterations) implies substantial compute, but the total cost is not quantified.

### Trivial

- The figure caption for Figure 6 refers to "L2SM" which appears to be a typo for "LVSM." This should be corrected for clarity.

## Nice-to-Haves

- **Incremental trajectory extension experiment.** The paper motivates AR models by arguing they are naturally suited to causal, incremental generation. An experiment that extends a trajectory beyond the initial 17 frames (without re-generating earlier frames) would directly validate this claimed advantage. Currently all evaluations are on fixed-length sequences that could be handled by joint-generation models. Adding this would substantially strengthen the paper in its own direction.

- **Error bars or confidence intervals for the main metrics.** While not standard across all NVS papers, the ablation studies (Tables 2 and 3) would be more informative with standard deviations over multiple runs or seeds, given the variability typical of generative model evaluation.

## Removed Points

These points from the reviewer inputs were removed with justification:

- **"Missing related works on video AR models"** — Removed per instructions: I cannot verify missing citations without external sources.
- **"Genwarp/MotionCtrl not designed for single-view NVS"** — Removed: the paper includes a reasonable set of baselines and justifies inclusion; criticizing baseline choice without a concrete alternative is scope creep.
- **"Resolution limitation (256×256)"** — Removed: this is a stated design choice; the paper is evaluated at a consistent resolution against fairly compared baselines.
- **"Missing appendix content / proofs"** — Removed per instructions: the parser strips appendix content from all papers.
- **"Flickering in Genwarp results"** — Not relevant as a weakness of the submitted paper; would be a comparison detail.
- **Strength Finder's generic strength about "importance of the problem"** — Removed: generic and not specific to this paper's execution.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the same key findings the paper presents.

## Suggestions

1. Add SEVA (and ideally Genwarp) to the per-frame error accumulation analysis in Figure 6. This is the single most impactful fix: it directly addresses the strongest claim in the paper.
2. State explicitly whether the ablation experiments (Tables 2, 3) use the same evaluation protocol (dataset split, sequence length) as the main results (Table 1). If they use a validation subset, say so. If the numbers differ for other reasons, explain them.
3. Add an ablation on the camera autoencoder: remove camera tokens and use standard positional encoding, or use raw Plücker coordinates, to quantify the benefit of the learned 3D tokens.
4. Clarify how camera and visual tokens are jointly projected into the transformer embedding space. Specify whether they share a projection matrix.
5. Report model size (parameters) and inference speed (frames per second). Soften "out-performs" claims to "competitive with" or "comparable to."
6. (Optional but recommended) Add an experiment showing incremental trajectory extension beyond 17 frames to validate the causal-generation motivation.

## Score and Decision

**Round 1 bracket:** Between 3.5 and 7.5. The most topically similar anchors were AR-1-to-3 (5.00, Reject) — a proposed AR approach for object-level view synthesis with limited evaluation — and the "Where Am I" paper (6.25, Accept) — a broader framework for joint pose estimation and view prediction.

**Round 2 narrowing:** Compared against anchors within (4.5, 6.5): AR-1-to-3 (5.00), Training-free Camera Control (5.80, Accept), Zero-shot NVS via Diffusion (6.00, Accept), "Where Am I" (6.25), ControlAR (6.25), and 4DiM (6.50). 

ARSS is clearly stronger than AR-1-to-3 (5.00): it evaluates on larger real-world datasets with zero-shot generalization, has better ablation studies, and a more novel technical approach. It is weaker than "Where Am I" (6.25) and 4DiM (6.50) — those papers have more thorough evaluation and fewer unresolved evidential gaps. ARSS is comparable to the training-free camera control paper (5.80) and the zero-shot NVS diffusion paper (6.00), but has concrete weaknesses (SEVA omission from Figure 6, unexplained ablation discrepancy) that those papers do not share.

**Final score:** 5.5. This reflects a paper with a genuinely novel contribution and solid experimental results, held back by verifiable evidential gaps that prevent full confidence in the current presentation.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
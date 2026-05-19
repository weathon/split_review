- Decision: Reject
- Avg Score: 5.60
- Scores: 5, 6, 5, 6, 6
I now have verified all the key claims against the actual paper. Let me write the consolidated review.

## Summary

This paper introduces 3D-Adapter, a plug-in module for multi-view diffusion models that infuses 3D geometry awareness through a "3D feedback augmentation" mechanism. At each denoising step, intermediate features are decoded into a 3D representation (Gaussian splatting or NeRF/mesh), rendered into RGBD views, and fed back into the base model via a ControlNet-like feature addition branch. The paper presents two variants — a fast feed-forward version trained for specific base models (Instant3D, Zero123++) and a training-free optimization-based version for flexible settings and tasks. Experiments span text-to-3D, image-to-3D, text-to-texture, and text-to-avatar generation.

## Strengths

- **Preservation of residual connections while adding 3D awareness**: The 3D feedback augmentation architecture feeds rendered 3D features back via a parallel ControlNet branch, avoiding the disruption of residual connections that plagues I/O sync methods. Table 1 provides direct evidence: I/O sync (A1) drops CLIP from 27.02→24.62 and aesthetic from 4.48→4.35, while 3D-Adapter (B0) achieves CLIP 27.31 and aesthetic 4.54, alongside dramatically lower MDD (4.7 vs. 232.4 for the two-stage baseline).

- **Two-phase training strategy enables robustness to inconsistent intermediate views**: In Phase 1, GRM is fine-tuned on noisy intermediate diffusion outputs using a rendering loss (Eq. 2), making it robust to the inconsistent, blurry inputs encountered mid-sampling. Table 1 shows this is necessary (A2 with fine-tuned GRM achieves near-perfect MDD of 1.7 but CLIP collapses to 22.57) but insufficient without feedback augmentation (B0 combines low MDD 4.7 with high CLIP 27.31).

- **Training-free optimization-based variant demonstrates task generality**: Section 4.2 shows that off-the-shelf "tile" and depth ControlNets can serve as the feedback encoder, requiring zero finetuning. This variant achieves strong results on text-to-texture (Table 5: CLIP 26.40 vs. SyncMVD's 25.65) and text-to-avatar (Table 6: aesthetic 4.97 vs two-stage 4.79), using only NeRF/mesh optimization and pretrained ControlNets.

- **Guided feedback augmentation with bias canceling (Eq. 4) is an effective technical contribution**: Ablation C1 in Table 1 (without bias canceling) drops CLIP from 27.31→25.49 and aesthetic from 4.54→4.36, confirming that the CFG-inspired guidance formulation is essential for preventing ControlNet overfitting from degrading visual quality.

- **Mesh conversion pipeline with negligible quality loss**: The TSDF-based mesh extraction from 3DGS (Table 3) yields PSNR 20.34 vs. 20.38 for native GS, SSIM 0.840 for both, and LPIPS 0.135 for both — demonstrating practical viability for downstream applications requiring meshes.

## Weaknesses

### Fatal
None.

### Major

- **The contribution of feedback augmentation versus GRM fine-tuning alone is not cleanly isolated in the SOTA comparisons.** In Table 1 (ablation), C0 (fine-tuned GRM, λ\_aug=0) achieves CLIP 27.18/Aesthetic 4.55/MDD 7.6 compared to B0 (full 3D-Adapter) at 27.31/4.54/4.7. The visual quality metrics (CLIP, Aesthetic) are essentially unchanged between C0 and B0 — the feedback primarily helps geometry (MDD). However, in the SOTA tables (Tables 2, 3), 3D-Adapter is compared against baselines using the *original* GRM (e.g., GRM at CLIP 26.6 in Table 2), not the fine-tuned GRM that 3D-Adapter internally uses. A "fine-tuned GRM" row in the SOTA tables is needed to attribute how much of the reported improvement comes from GRM fine-tuning versus the feedback mechanism itself. As the paper is currently structured, a reader cannot determine whether the headline gains (e.g., CLIP 27.7 vs. GRM's 26.6 in Table 2) would largely vanish once the reconstruction model is simply fine-tuned. The ablation table provides partial evidence, but uses a different test set (379 vs. 200 prompts) and different metrics (including FID/MDD) than the SOTA table, making direct comparison difficult.

### Minor

- **Inference time for the fast GRM-based variant is missing.** The paper states "The inference time is around 0" (line 208), which is a clear formatting/placeholder error. While runtimes are reported for the optimization-based variants (1.5 min for texture, 7 min for avatar), the primary fast variant's latency is not given anywhere. Given that 3D-Adapter adds VAE decoding, a full GRM pass, and a ControlNet pass per denoising step, this is a practical concern that should be documented.

- **Test sets share distribution with training data, and generalization is unclear.** The paper's own limitations section (line 347) acknowledges that "our finetuned ControlNet for 3D feedback augmentation strongly overfits the finetuning data." The text-to-3D and image-to-3D test sets are both drawn from Objaverse subsets (same source as the training data). While common practice, the paper would benefit from at least qualitative evaluation on out-of-distribution prompts (e.g., compositional or abstract descriptions) to demonstrate generalization beyond the training distribution.

- **Gains on image-to-3D are modest relative to added complexity.** In Table 3, 3D-Adapter improves over GRM by PSNR 20.38→20.10 (+0.28), SSIM 0.840→0.826 (+0.014), LPIPS 0.135→0.136 (comparable), and FID 20.2→27.4 (-7.2). The improvements are positive but small, and no variance or statistical significance is reported, making it difficult to assess whether these differences are meaningful given the extra computation.

- **Missing runtime prevents assessing the speed-quality trade-off of the fast variant.** This is a separate point from the missing number — even with the runtime filled in, the paper does not discuss the practical trade-off: the fast variant adds substantial computation (extra decoder, GRM, ControlNet) compared to a simple two-stage pipeline. Including GPU memory usage and per-step timing breakdown would help practitioners evaluate deployability.

### Trivial

- "The inference time is around 0" — formatting error that should be replaced with the actual runtime.

## Nice-to-Haves

- Reporting standard deviations or confidence intervals for the main metrics, especially where gains are small (e.g., image-to-3D PSNR improvement of 0.28).
- An ablation exploring a lighter architecture for the intermediate decoder copy (e.g., fewer channels), to quantify the computation-quality trade-off.
- Reporting peak GPU memory usage during training and inference, given the two-decoder design doubles decoder parameters.
- Evaluating on held-out prompts that are compositionally different from individual Objaverse objects, even if only qualitatively.

## Removed Points

These points are flagged to be removed; treat them with caution:

- *"C0's meaning is ambiguous (λ\_aug=0 vs. complete removal)"* — The paper clearly states "C0, equivalent to λ\_aug=0" at line 265. This is unambiguous.
- *"I/O sync comparison should include DMV3D/SyncDreamer for text-to-3D"* — DMV3D is an image-to-3D method, not text-to-3D, making it inapplicable to Table 2's setting. The paper's I/O sync baseline is designed to demonstrate the *limitations* of the paradigm, not to beat specific methods. SyncMVD *is* compared for text-to-texture (Tables 4, 5). For the primary tasks, the theoretical motivation is sound and supported by the naive baseline results.
- *"The two-stage baseline already outperforms SyncMVD, suggesting the base model is strong"* — This is a strength, not a weakness. That the paper's baselines are already strong further supports the method.
- *"Table 2 should include a row for C0"* — Already elevated to a Major weakness above (the core concern is valid), though the specific request to add it to Table 2 is one possible remedy.
- *"CLIP t-less for text-to-avatar is only slightly above two-stage"* — 26.07 vs. 24.60 on a 21-prompt set is a 6% relative improvement, which is meaningful. The critic's framing is misleading.
- Pure style/formatting nitpicks.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the key tension: the paper's headline claim (feedback augmentation improves visual quality) is partially confounded with GRM fine-tuning, and the ablation data (C0 vs. B0 in Table 1) reveals that the marginal CLIP/Aesthetic gains from the feedback mechanism itself are very small (CLIP +0.13, Aesthetic -0.01). The improvement is concentrated in geometric consistency (MDD 7.6 → 4.7). This suggests the paper's true contribution is better characterized as "3D feedback augmentation primarily improves geometric consistency while preserving the visual quality of the fine-tuned base model" rather than "3D feedback augmentation improves visual quality."

## Suggestions

1. **Add a "fine-tuned GRM" baseline row to the SOTA tables (Tables 2 and 3).** This would directly address the core evidential gap and cleanly attribute the source of improvement. If 3D-Adapter still significantly outperforms this baseline on visual metrics, the claim is strongly supported. If the gap is small, the paper should recalibrate its claims to emphasize the geometric consistency benefit.

2. **Fill in the missing inference time for the GRM-based fast variant** (line 208), including a breakdown of per-step latency (VAE decode, GRM forward, ControlNet forward).

3. **Report the fine-tuned GRM's CLIP/Aesthetic scores on the SOTA test set** (200 prompts from Table 2) explicitly, not just in the ablation table on a different test set.

4. **Add variance or a simple statement about single-run versus multi-run averaging** for the main results, especially where margins are small (image-to-3D, text-to-avatar).

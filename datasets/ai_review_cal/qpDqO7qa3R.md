- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper introduces DiffIR2VR-Zero, a training-free framework for adapting pre-trained image restoration diffusion models to video restoration tasks. The method combines two key modules: (1) hierarchical latent warping that provides global (keyframe-to-keyframe) and local (within-batch) temporal guidance in latent space, and (2) hybrid flow-guided spatial-aware token merging that uses optical flow in UNet downsample blocks and cosine similarity in upsample blocks to enforce temporal consistency at the token level. The approach is model-agnostic (demonstrated with DiffBIR, SDx4, and Marigold) and achieves competitive results on video super-resolution, denoising, and consistent depth estimation without any retraining.

---

## Strengths

1. **First training-free framework for video restoration with image diffusion models, validated across multiple tasks and backbones.** Section 3 presents a genuinely training-free approach combining hierarchical latent warping and hybrid token merging. Tables 1–2 demonstrate competitive results on video super-resolution and denoising using both DiffBIR and SDx4 backbones, and Figure 6 extends the framework to consistent video depth estimation with Marigold — all without any fine-tuning of the underlying models.

2. **Ablation study convincingly validates the hybrid correspondence design.** Table 3 (left panel) systematically compares correspondence strategies across UNet blocks. The hybrid "Flow (down) + Cos (up) + spatial-aware" achieves LPIPS 0.367, E_warp* 0.699, and LPIPS_inter 0.333 on 8× VSR on DAVIS, outperforming flow-only (LPIPS 0.518), cosine-only (0.390), and the reverse order (0.507). This directly validates the authors' rationale that noisy early latents make flow more reliable in downblocks while feature similarity is preferable in upblocks.

3. **Strong performance on extreme noise and cross-dataset generalization.** On Set8 with σ=150 noise (Table 2, right panel), the method achieves PSNR 21.418, LPIPS 0.402, and E_warp* 0.832 — all best among baselines — substantially outperforming the trained Shift-Net (PSNR 16.136). On Set8 σ=50 and σ=100, the method similarly achieves best overall scores, demonstrating genuine zero-shot generalization to datasets unseen by any trained baseline.

4. **Scheduling ablation provides practical engineering insight.** Table 3 (right panel) shows that applying hierarchical latent warping only at early stages and hybrid token merging through mid/late stages gives the best balance (LPIPS 0.367, E_warp* 0.699). Applying warping at mid or late stages degrades results (LPIPS 0.43), confirming the authors' reasoning.

---

## Weaknesses

### Fatal

None.

### Major

1. **Systematic overclaiming relative to quantitative evidence.** The abstract states the method "not only achieves top performance in zero-shot video restoration but also significantly surpasses trained models in generalization across diverse datasets." The introduction claims "state-of-the-art results in extreme scenarios, surpassing traditional methods in generalizability and robustness." The contribution list includes "State-of-the-art results in extreme scenarios, surpassing traditional methods."

   These claims are not supported by the main results tables. On video super-resolution (Tables 1 and the SR portion of Table 4), FMA-Net outperforms DiffIR2VR-Zero on **every** PSNR and SSIM metric: SPMCS 4× (21.910 vs. 21.843), DAVIS 4× (25.215 vs. 24.182), REDS4 4× (25.829 vs. 25.118), Vid4 4× (23.209 vs. 21.226). On denoising (Table 2), VRT achieves PSNR 29.292 at σ=50 vs. the method's 24.843. The method's advantages are limited to LPIPS (perceptual quality) in some settings and performance on extremely high noise (Set8 σ=150), but the blanket framing of "significantly surpasses trained models" is misleading. This is not a minor rhetorical flourish — it is the paper's central narrative and it misrepresents what the evidence shows. The real contribution (training-free video restoration with competitive perceptual quality) is interesting enough to stand on its own without inflated claims.

2. **Textual descriptions in Section 4.1 contradict the quantitative results.** The paper claims "regression-based methods like FMA-Net struggle with large motion or severe degradation" (Section 4.1, VSR paragraph), yet FMA-Net achieves the best temporal consistency metrics (E_warp, E_inter, LPIPS_inter) in nearly every SR setting. Similarly, the paper frames the method as having "enhanced temporal consistency while maintaining generation quality," but trained methods consistently achieve better or comparable temporal consistency on most benchmarks. These claims should be calibrated to reflect what the data actually shows.

### Minor

1. **Lack of explicit discussion of the LPIPS/temporal consistency trade-off.** The ablation study (Table 3, right) shows that the "no components" baseline achieves LPIPS 0.362 (best in that table), while the full method achieves LPIPS 0.367 with better temporal consistency (E_warp* 0.699 vs. 0.964). The difference in LPIPS is tiny (0.005) and likely within noise, but the paper does not acknowledge that enforcing temporal consistency could marginally affect perceptual quality. Explicitly discussing this trade-off would strengthen credibility.

2. **No runtime or memory comparison in the main paper.** The paper reports using a single RTX 4090 but provides no timing or memory comparison against baselines like FMA-Net or VRT. The authors note "computational complexity evaluations in the supplementary materials," but for a zero-shot method that may require many denoising steps, runtime is a practical concern that merits space in the main text.

### Trivial

None.

---

## Nice-to-Haves

1. **Explicit characterization of the gap to trained methods.** A summary statement such as "Our method achieves LPIPS comparable to or better than trained methods (e.g., DAVIS 4×: ours 0.262 vs. FMA-Net 0.347), but PSNR is 1–2 dB lower — this gap reflects the absence of task-specific training" would clearly and honestly frame the trade-off.

2. **A brief discussion of what types of videos or degradations cause the method to fail**, beyond the brief limitations paragraph about "LDM decoder sensitivity" and "extreme degradation."

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Overstatement of generalization testing — no evaluation on real-world degradations."** The paper tests on standard benchmarks (REDS, DAVIS, Vid4, Set8) with synthetic degradations. This is standard practice in the field. The method is inherently zero-shot (no training), so generalization is demonstrated by working across multiple datasets and backbones without retraining. The Set8 results (cross-dataset) provide specific evidence of generalization. Demanding real-world degradation testing is scope creep beyond what is standard for a paper of this type.

- **"The claimed 'first zero-shot video restoration using diffusion models' is not strictly supported by citations."** The paper clearly distinguishes its restoration task from video editing methods (VidToMe, TokenFlow). No prior zero-shot video *restoration* using diffusion models is cited, and the paper's claim in this narrow framing appears correct.

- **"Ablation reveals temporal consistency can hurt LPIPS — trade-off not discussed."** While technically the "no modules" row has LPIPS 0.362 vs. the full method's 0.367, the difference is 0.005, which is negligible and likely within measurement noise. The broader pattern in the table clearly shows the method improves temporal consistency metrics substantially (E_warp from 0.964 → 0.699) with essentially no LPIPS cost. This criticism is demoted from the harsh critic's framing as a "trade-off" to the Minor section above.

- **"Missing failure cases beyond brief limitations."** The limitations paragraph is standard in length and scope for a conference paper. The critic's request for more detail is a nice-to-have, not a weakness.

- **Strengths removed from Strength Finder**: Generic statements about "addressing an important problem" or being "well-written" were removed per the filtering rules. The strength about "strong generalization to extreme degradations" was retained but reframed to accurately reflect the evidence (Set8 results are strong, but standard benchmark results show trained methods lead on PSNR/SSIM).

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Rewrite the abstract, introduction, and conclusion to accurately reflect the evidence.** Lead with what the method *does* (brings temporal consistency to image diffusion models without training) rather than what it *beats*. Frame the comparison to trained methods as a trade-off analysis (competitive perceptual quality at the cost of PSNR/SSIM, with zero training cost) rather than a claim of overall superiority.

2. **Add a brief runtime/memory table in the main paper** comparing per-frame or per-video inference time against FMA-Net and VRT, so readers can assess the practical cost of the zero-shot approach.

3. **Explicitly acknowledge in the ablation discussion** that the temporal consistency gains come with a negligible-to-zero LPIPS cost, and discuss why this is acceptable for the intended use case.

4. **Consider adding a small cross-domain experiment** (e.g., testing on a different degradation type than what the image diffusion model was trained for) to substantiate the generalization claims more directly.

---

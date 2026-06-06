## Summary

Stylos is a single-forward feed-forward framework for image-conditioned 3D Gaussian stylization that takes unposed multi-view content images and a style reference to produce stylized 3D Gaussian scenes without per-scene optimization. The core design disentangles geometry (via VGGT self-attention backbone) from style (via cross-attention CrossBlock modules) and introduces a voxel-level 3D style loss that aligns aggregated 3D scene features with style statistics. Stylos achieves zero-shot generalization to unseen categories, scenes, and styles at 0.05s inference time—three to four orders of magnitude faster than per-scene optimization baselines.

---

## Strengths

- **Global CrossBlock design demonstrably preserves geometric fidelity.** Table 1 confirms that Global CrossBlock yields PSNR 20.57 dB vs. 19.78 dB (Hybrid) on the pizza category, and Fig. 2 qualitatively shows sharper toppings and crust boundaries. The improvement is consistent across all three CO3D test categories (Skateboard, Pizza, Donut).

- **Voxel-level 3D style loss substantially outperforms image-level loss in artistic quality.** Table 2 shows a dramatic gap in ArtScore between image-level (4.78) and scene/3D losses (9.12/9.15). Fig. 3 qualitatively confirms that 3D and scene losses both produce well-stylized textures on donut, skateboard, and pizza, while the image loss fails to transfer style on the donut.

- **Zero-shot cross-scene generalization outperforms all baselines in consistency.** Table 3 shows Stylos achieves the lowest short- and long-range LPIPS/RMSE across all four Tanks & Temples scenes (e.g., Truck short-range LPIPS 0.028 vs. second-best StyleGaussian at 0.031). Table 4 shows this is achieved at 0.05s inference versus G-Style's 14.7 minutes while remaining competitive on ArtScore (e.g., Truck: 9.70 vs. G-Style's 9.67).

- **Post-inference style control via embedding interpolation.** Fig. 6 demonstrates smooth transitions between two style embeddings and a continuous spectrum from reconstruction to stylization by interpolating between content and style embeddings, without any additional optimization.

---

## Weaknesses

### Fatal
None verified.

### Major

- **Systematic naming inversion in Section 4.2's evaluation narrative.** The quantitative evaluation paragraph (lines 231–232) attributes Stylos's results entirely to "Styl3R": *"Styl3R achieves strong and stable consistency scores, ranking the first across all consistency metrics and all four scenes"* and *"Styl3R attains either the best or second-best artistic metric values… while maintaining the fastest stylization speed."* However, Table 3 clearly shows **Stylos (ours)** in bold across every cell, with Styl3R performing substantially worse (e.g., Truck short-range LPIPS 0.061 vs. Stylos's 0.028). Table 4 shows Styl3R at ArtScore 2.94–4.09 vs. Stylos at 9.37–9.70, and Styl3R at 0.16s vs. Stylos at 0.05s. Every sentence in this paragraph inverts the actual claims. A reader relying on the narrative without cross-checking the tables would conclude that Styl3R is the proposed method. This must be corrected before publication.

- **CrossBlock ablation is conducted only under style-free reconstruction, not under actual stylization.** Table 1 uses the first content frame as pseudo-style reference and evaluates PSNR/SSIM/LPIPS against ground-truth content views—a purely geometric reconstruction setting with no artistic style transferred. The paper's conclusion in Sec. 5 ("the global CrossBlock for style injection better preserves geometric details than alternative style-content fusion modules") and the claim that Global CrossBlock enables "view-consistent stylization" are drawn solely from this reconstruction experiment, with no counterpart ablation under real style conditioning (ArtScore, ArtFID, or consistency metrics from Table 2). The implicit assumption that the variant optimal for reconstruction is also optimal for stylization is not established.

### Minor

- **Voxel-level 3D loss offers only marginal quantitative improvement over the simpler scene-level loss.** In Table 2, the differences between Scene loss (Eq. 4) and 3D loss (Eq. 5) are: ArtScore 9.12→9.15, long-range LPIPS 0.156→0.153, short-range LPIPS identical (0.047=0.047), and long-range RMSE 0.148→0.142 (which ties image loss). While Fig. 3 shows qualitative differences, the quantitative case for the voxel loss's unique contribution—as opposed to any multi-view aggregation scheme—is weak on the 15-scene evaluation. The paper should either provide a more targeted experiment showing cases where voxel loss outperforms scene loss, or recalibrate the framing of this contribution.

- **Artistic quality advantage over G-Style is overstated.** Table 4 caption claims Stylos achieves "consistently favorable metric scores across the four scenes," but G-Style achieves higher ArtScore on Train (9.52 vs. 9.50) and M60 (9.73 vs. 9.37), and better ArtFID on Train (23.24 vs. 26.40) and M60 (22.36 vs. 27.44). The real—and genuinely compelling—advantage is the ~17,600× speedup (0.05s vs. 14.7 min); framing the contribution around this efficiency-quality trade-off would be more defensible.

- **Absence of Styl3R results on the "Train" scene is unexplained.** Table 3 shows "–" for Styl3R on Train without explanation. If this scene appears in Styl3R's training distribution, the omission is methodologically relevant and should be noted explicitly.

- **Naming inconsistency between "Stylos" and "Stylus."** The abstract, introduction, and main body consistently use "Stylos," but Section 5 (conclusion) and Fig. 5's caption refer to the method as "Stylus." This should be standardized throughout.

### Trivial
None beyond the naming inconsistency noted above.

---

## Nice-to-Haves

- Replicate the CrossBlock ablation under actual stylization conditions (Stage 2, real style images) reporting ArtScore, ArtFID, and consistency metrics. If Global CrossBlock is best for both reconstruction and stylization, that convergence would strengthen the architectural justification.
- Evaluate style diversity and sensitivity across dramatically different style types (abstract, sketch, photorealistic paintings) to better support the "generalization to unseen styles" claim, which currently covers 50 held-out images from WikiArt/DELAUNAY—similar aesthetic distribution to training.
- Analyze the domain gap between Stage 1 pseudo-style training (color-jittered content) and Stage 2 real artistic styles. An ablation removing Stage 2 would clarify how much style injection capability is actually trained in versus inherited from Stage 1 reconstruction.
- The paper's most compelling story—0.05s inference at competitive quality versus minutes of per-scene optimization—should be the primary framing of the contribution rather than implied parity with per-scene methods.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "The degree of generalization to genuinely out-of-distribution artistic styles is not evaluated."** — Removed as scope-creep. The paper states 50 held-out styles from WikiArt/DELAUNAY are used as "unseen styles never used during training." Testing OOD styles (e.g., pencil sketches) would be a nice-to-have, not a core flaw, and the paper does not claim generalization beyond its evaluated style distribution.

- **Harsh Critic: "Stage 2 freezes all geometry modules… whether this strict separation is beneficial or introduces brittleness is not discussed."** — Removed as speculative. The paper honestly describes the two-stage design and demonstrates results. A theoretical discussion of brittleness is a discussion-level suggestion, not a methodological flaw verifiable from the paper.

- **Harsh Critic: "The consistency metric conflates 'consistent' with 'less stylized.'"** — Removed as speculative. No evidence is presented that Stylos achieves lower stylization strength. Stylos simultaneously achieves the highest ArtScore in most scenes, suggesting it is both consistent and well-stylized.

- **Strength Finder: "voxel-level 3D style loss improves cross-view consistency and artistic quality."** — Partially retained as strength against image-level, but the improvement over scene-level is marginal; the strength claim is weakened accordingly.

- **Harsh Critic: "the claim to 'scale from a single image to hundreds of views' is somewhat misleading."** — Demoted to nice-to-have framing. The paper already acknowledges quality degradation past 32 views in Sec. 4.1 and Fig. 4; the limitation is disclosed.

---

## Novel Insights

The most genuinely novel observation in this paper is the architecture's separation of geometry and style into strictly disjoint pathways—self-attention for geometry, cross-attention for style—operating over a shared Transformer backbone, combined with a voxel-space style loss that enforces 3D structural style coherence rather than per-frame or concatenated 2D alignment. While individual components (VGGT backbone, AdaIN-based losses, 3DGS rendering) are established, their integration into a zero-shot, feed-forward pipeline that requires neither per-scene optimization nor camera calibration at inference, with demonstrated competitive results at 0.05s per scene, represents a meaningful practical advance for real-time 3D content creation.

---

## Suggestions

1. **Correct the Section 4.2 narrative immediately.** Every sentence in the quantitative evaluation paragraph misattributes Stylos's results to Styl3R. Replace "Styl3R" with "Stylos (ours)" throughout and update wording to reflect the correct comparative claims.
2. **Add a stylization-condition ablation of CrossBlock designs.** Run the same three variants (Frame/Global/Hybrid) with real style images, evaluate with ArtScore, ArtFID, and consistency metrics, and report alongside Table 1. This directly validates the architectural choice's relevance to the stylization task.
3. **Recalibrate the voxel loss contribution.** Acknowledge that the scene-level loss (Eq. 4) already captures most of the multi-view consistency benefit, and position the 3D loss as a refinement with geometry awareness. Fig. 3 can anchor this qualitative argument explicitly.
4. **Standardize the method name** to "Stylos" throughout, including the conclusion and figure captions.
5. **Explain the missing Styl3R results on Train** and make the efficiency-quality trade-off the paper's primary contribution narrative.

---

## Score and Decision

**Originality:** 3/5 — Combines established components (VGGT, AdaIN losses, 3DGS rendering) in a novel configuration for 3D stylization; the voxel-space loss extension is new.  
**Importance:** 4/5 — Real-time feed-forward 3D stylization with zero-shot generalization addresses a practically high-value problem.  
**Claims Supported:** 3/5 — Core consistency/efficiency claims are well-supported by Tables 3–4; the CrossBlock and voxel loss architectural claims are less rigorously evidenced; the Sec. 4.2 narrative error is a serious presentation failure.  
**Soundness:** 3/5 — Methodology is coherent; the CrossBlock ablation gap and marginal voxel loss benefit reduce confidence in specific claims.  
**Clarity:** 2/5 — The systematic naming inversion in the main evaluation section is a significant clarity failure in the paper's most important contribution claim.  
**Community Value:** 4/5 — Strong practical value; reproducible code and weights released.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>2</clarity>
<community_value>4</community_value>
</subscores>
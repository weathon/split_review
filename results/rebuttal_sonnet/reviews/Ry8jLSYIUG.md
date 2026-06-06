Now I have everything I need. Let me write the updated review.

---

## Summary

This paper investigates whether deep learning-based image watermarking methods have saturated fundamental capacity limits. The authors derive geometric upper bounds under PSNR and linear robustness constraints, showing theoretical capacity is orders of magnitude above current practice. Carefully designed diagnostic experiments (retraining Video Seal on a single gray image) isolate architectural limitations as the primary bottleneck. As proof of concept, Chunky Seal—a scaled-up Video Seal—delivers 1024 bits (4× capacity) with comparable robustness.

---

## Rebuttal Assessment

**Weakness: LPIPS difference significantly understated**
- **Author's response:** Partially address — acknowledges the characterization is imprecise, defends absolute smallness of values (0.0019 vs 0.0085 on [0,1] scale), commits to revising language in revision.
- **Assessment:** Partially convincing — The absolute values are indeed small on the [0,1] LPIPS scale, and the defense that the holistic quality assessment (PSNR, SSIM, MS-SSIM all comparable) matters is reasonable. However, verified against Section 4 (line 293 in the file), the paper currently reads "only slightly higher LPIPS," which remains an imprecise characterization of a 4.5× ratio. The author's promise to revise is not current paper content, so the weakness stands. That said, the author does provide context (small absolute magnitude) that slightly softens the concern.
- **Score impact:** Weakness unchanged (promise to revise does not count)

**Weakness: Figure 1 presents only heuristic bounds; "orders of magnitude" has varying accuracy**
- **Author's response:** Partially address — accepts the nuance, argues primary "orders of magnitude" anchor is the PSNR-only heuristic bound (Section 2.3.3), not Bound 13. Claims the paper clearly distinguishes heuristic/conservative in Section 2.5.
- **Assessment:** Partially convincing — Verified: Section 2.3.3 (line 118) does explicitly state "roughly 2000 bits of capacity (more than 2.5 bpp): orders of magnitude more than the 0.001 bpp we see in practice" as the direct anchor. Section 2.5 (lines 156–158) does distinguish heuristic from conservative bounds and explicitly labels Bound 13 as "extremely conservative." The author is correct that the main claim is tied to heuristic bounds, not Bound 13. However, Figure 1 still only shows heuristic bounds without any indication that these are upper-bound heuristics rather than proven lower bounds—the visual creates an impression the paper's text partially qualifies. The author's promise to add Bound 13 to Figure 1 in the camera-ready is a future fix, not present content.
- **Score impact:** Weakness downgraded (author's explanation of the primary anchor is factually correct and mitigates the concern somewhat, but Figure 1 still lacks the conservative counterpart)

**Weakness: Handcrafted model's perceptual quality unreported**
- **Author's response:** Partially address — argues the handcrafted model is explicitly a PSNR-constrained construction, its role is solely to show PSNR-bounded capacity is achievable, and Section 5 explicitly declares perceptual constraints out of scope.
- **Assessment:** Partially convincing — Verified: Table 1 confirms no SSIM/LPIPS are reported for the handcrafted model. The author is correct that the paper is transparent about this scope limitation. However, the weakness is not that the scope is wrong—it's that using a construction that quantizes each pixel to a coarse grid (structured, high-frequency perturbations) as the empirical anchor for "Bound D is unlikely" may not generalize to perceptually meaningful watermarking. The author's note that Section 5 lists perceptual constraints as future work is genuine but doesn't eliminate the concern that the handcrafted bound is achievable only under PSNR optics.
- **Score impact:** Weakness unchanged (the partial address is honest but the gap remains)

**Weakness: Linear model comparison framing is occasionally loose**
- **Author's response:** Refute — argues Section 3.1 explicitly establishes the "single gray image, no augmentation, MSE-only" context before the comparison is drawn, and the paper even states the linear model "degenerates to learning a fixed additive perturbation mask."
- **Assessment:** Convincing — Verified: Section 3.1 (line 215) explicitly constructs the minimal diagnostic before introducing any comparisons. Section 3.2 (line 246) states "All one needs is the right architecture" in context of this degenerate diagnostic. The paper does not claim the linear model is a general-purpose watermarker. The "Trivial" label in the original review was appropriate, and the author's refutation is well-grounded.
- **Score impact:** Weakness removed

---

## Strengths

- **Novel geometric capacity framework (Sections 2.2–2.5):** Three-regime analysis (cube-in-ball, ball-in-cube, non-trivial intersection) using first principles geometry, analytically novel relative to Gaussian-noise information-theoretic baselines. Verified: Section 2.3.3 yields ~2000 bits at 45 dB for a 16×16 image—orders of magnitude above 0.001 bpp SOTA.
- **Single-gray-image diagnostic definitively rules out explanations A/B/C (Section 3.1):** Video Seal fails at 1024 bits despite theoretical capacity of ~600,000 bits at 40 dB, and 32×32 and 256×256 variants perform identically (Table 1), showing architectural—not external—limits.
- **Linear baseline provides decisive achievability argument (Section 3.2):** 100% accuracy at 1024 and 2048 bits in 50 epochs vs. Video Seal's failure in 600 epochs. Verified in Table 1 (lines 208–209).
- **Handcrafted model approaches theoretical bound under PSNR (Table 1):** 456,509 bits at 42 dB, ~14× tiling result. Verified.
- **Conservative Bound 13 (Table 2):** Worst-case lower bound remains meaningful: 904 bits at 75% crop, 14,676 bits at 30° rotation, 26,757 bits at LinJPEG q=10, all at 256×256px, 42 dB. Verified (lines 230–238).
- **VQ-VAE/VQGAN data distribution bound (Section 2.6):** Effect bounded to ~0.05 bpp. Verified (lines 172).
- **Chunky Seal (Table 3):** 4× capacity increase with near-identical PSNR, SSIM, MS-SSIM. Verified.
- **Concrete sanity checks (Section 5):** Practical contribution for future model evaluation.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **LPIPS difference significantly understated.** Table 3 (lines 261–279) shows LPIPS = 0.0085 (Chunky Seal) vs. 0.0019 (Video Seal), a 4.5× difference. Section 4 (line 293) still reads "only slightly higher LPIPS." The author's rebuttal concedes this is imprecise and defends it on absolute magnitude grounds (both values are small on [0,1]), which is a fair partial mitigation. But the language in the current paper remains inaccurate, and a promise to revise does not constitute a fix. The broader argument is unaffected.

- **Figure 1 presents only heuristic bounds without indicating this.** The author correctly clarifies that the "orders of magnitude" anchor in Section 2.3.3 is the PSNR-only heuristic bound, not Bound 13—and this specific claim is accurate. However, Figure 1 itself plots heuristic bounds (Bounds 10–12) labeled simply as "PSNR + [augmentation] bound," with no indication these are heuristic upper bounds rather than proven lower bounds. The conservative Bound 13 (Table 2) is not shown in Figure 1. This remains a presentation concern, downgraded since the paper body properly distinguishes the two.

- **Handcrafted model's perceptual quality unreported.** The handcrafted construction (Equation 2, line 254) achieves 456,509 bits at 42 dB PSNR by quantizing pixels to a coarse grid. No perceptual metrics (SSIM, LPIPS) are reported in Table 1. The author's defense—that the handcrafted model's role is to show PSNR-constrained capacity is achievable, and perceptual constraints are declared out of scope in Section 5—is honest but does not close the gap: the paper uses this model as the primary existential argument that Bound D ("bounds are unachievable") is wrong, without verifying the construction is meaningful under perceptual metrics.

### Trivial

- **"Only slightly higher LPIPS" (Section 4)** — Minor presentation inaccuracy; author acknowledges and commits to revision. (Absorbed into Minor weakness above.)

---

## Nice-to-Haves

- Include Bound 13 as a shaded floor in Figure 1 with legend distinguishing heuristic vs. conservative. (Author committed to this; it is not yet in the paper.)
- Add SSIM or LPIPS for the handcrafted model in Table 1, even as an explanatory footnote.
- Extend Table 3 to include at least one other high-capacity method (MiRRE, WAM, TrustMark appear in Figure 1 but are absent from Table 3).
- Report inference/training latency for Chunky Seal (embedder 90×, extractor 23× larger than Video Seal).

---

## Novel Insights

The paper's most genuinely novel contribution is the single-gray-image diagnostic: by stripping Video Seal of all real-world complexity (fixed image, no augmentations, MSE-only loss), the authors create a "watermarking IQ test" that any correct model should trivially pass, yet Video Seal fails it. The additional observation that a 32×32 Video Seal trained on this setup achieves essentially the same capacity as a 256×256 model—despite having 64× fewer pixels—directly demonstrates that the architecture fails to exploit spatial dimensionality. Combined with the VQ-VAE argument (data distribution effect bounded to ~0.05 bpp), and the handcrafted construction achieving ~456,509 bits at 42 dB, the paper provides a coherent multi-pronged case that the bottleneck is architectural, not fundamental.

---

## Suggestions

1. Replace "only slightly higher LPIPS" in Section 4 with "notably higher LPIPS (4.5× ratio in absolute terms), despite near-identical PSNR and MS-SSIM."
2. Add Bound 13 to Figure 1 as a shaded band, labeled "conservative lower bound," so the figure's visual story matches the nuance of Section 2.5.
3. Add a footnote or column in Table 1 acknowledging no perceptual metrics are reported for the handcrafted model and why (PSNR-only construction by design), to pre-empt the obvious question.
4. Include Chunky Seal inference latency in Table 3 or a footnote.

---

## Score and Decision

**Assessment of rebuttal impact:**

The rebuttal is honest, well-scoped, and largely succeeds on its goals. The "linear model framing" weakness (Trivial) is convincingly refuted and removed—the paper does establish the diagnostic context before the comparison. The LPIPS and Figure 1 concerns remain: the author acknowledges them as presentation issues but cannot fix them in the rebuttal phase; promises of camera-ready revision do not count. The handcrafted model concern is partially addressed—the PSNR-only scope is explicitly stated in Section 5, but the existential use of this model for Bound D remains contingent on PSNR being the right metric.

**No new problems were revealed by the rebuttal.** All remaining weaknesses are Minor in scope, and the core theoretical claims, diagnostic experiments, and empirical findings are solid. The original 7.0 was calibrated appropriately: the paper is analytically rigorous, the experiments are well-designed, and the capacity gap argument is well-supported. Nothing in the rebuttal changes this calculus materially.

**Final score: 7.0, Accept.**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
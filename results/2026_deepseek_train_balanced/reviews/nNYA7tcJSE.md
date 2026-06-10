## Summary

This paper proposes ViBiDSampler, a training-free bidirectional sampling strategy for video keyframe interpolation using pre-trained image-to-video diffusion models (SVD). Instead of fusing parallel forward and backward denoising paths (which causes off-manifold artifacts), the method denoises forward, injects a single re-noise step, then denoises backward sequentially. Combined with CFG++ and DDS guidance, the method achieves strong results on DAVIS and competitive results on Pexels while requiring no fine-tuning and using only 50 NFE (195 seconds for 25 frames at 1024×576 on a single 3090 GPU).

## Strengths

1. **Clean, well-motivated idea backed by consistent evidence from the vanilla variant.** The core innovation — replacing parallel fusion with sequential forward-backward sampling — is simple and intuitive. Critically, the vanilla version (pure sequential sampling without CFG++ or DDS) *already* outperforms TRF on all six metrics across both datasets (e.g., DAVIS LPIPS 0.3031 vs. 0.3102, FID 52.452 vs. 60.278, FVD 543.31 vs. 622.16). This provides direct evidence that the sequential ordering itself, not just the guidance techniques, is beneficial.

2. **Training-free with substantial efficiency gains.** ViBiDSampler requires no fine-tuning and completes 25 frames at 1024×576 in 195 seconds (50 NFE) on a single 3090, compared to Generative Inbetweening's 1,222 seconds (300 NFE) with fine-tuning. Table 2 clearly documents these comparisons.

3. **Systematic ablation isolating each component's contribution.** The paper reports three variants — vanilla, vanilla + CFG++, and full (CFG++ + DDS) — with monotonic improvement across all DAVIS metrics (LPIPS 0.3031 → 0.2571 → 0.2355; FVD 543.31 → 434.41 → 399.15). This allows readers to attribute gains to specific techniques.

4. **CFG++ guidance scale analysis.** Table 3 (despite the row-label error discussed below) and Figure 4 provide quantitative and qualitative evidence for the choice ω = 1.0, which is more rigorous than most papers in this area.

5. **Strong DAVIS performance with a frozen backbone.** ViBiDSampler (Full) achieves the best FID (35.66) and FVD (399.15) among all methods on DAVIS, outperforming DynamiCrafter and Generative Inbetweening which fine-tune the backbone. This demonstrates that the sampling strategy itself drives quality gains on challenging, large-motion dynamics.

## Weaknesses

### Fatal
None.

### Major

1. **Missing control experiment: applying CFG++/DDS to fusion-based baselines.** The paper's SOTA results are achieved by combining sequential bidirectional sampling with CFG++ (Chung et al., 2024) and DDS (Chung et al., 2023) — both existing techniques. The vanilla (sequential-only) variant is competitive with but not decisively better than the best fusion-based baselines: on DAVIS, vanilla (LPIPS 0.3031) is worse than Generative Inbetweening (0.2823) and FILM (0.2697); on Pexels, vanilla (LPIPS 0.2074) is substantially worse than FILM (0.0821) and Generative Inbetweening (0.1523). Since CFG++ and DDS are known to improve diffusion sampling generally, it is unclear how much of the final gain comes from the sequential strategy versus simply applying these guidance techniques. A controlled experiment applying CFG++ and DDS to a fusion-based approach (e.g., TRF's pipeline or a re-implemented fusion sampler) is necessary to attribute gains to the claimed mechanism. Without it, the paper's central claim — that sequential sampling, not just better guidance, drives the improvement — is not fully supported.

2. **Table 3 contains a clear data-labeling error.** The row labeled "LPIPS" lists values 525.36, 424.03, and 399.15, which are clearly FVD-scale numbers (Ours Full FVD = 399.15 in Table 1). The row labeled "FVD" lists 0.2697, 0.2394, and 0.2355, which are LPIPS-scale values (Ours Full LPIPS = 0.2355). This is not a formatting artifact — the LaTeX source itself has LPIPS and FVD rows swapped. LPIPS is bounded near [0,1]; values of 525 are impossible. This error undermines confidence in the paper's reporting and must be corrected.

### Minor

1. **TRF baseline methodology is not explained.** The paper states on line 198 that TRF "has not been open-sourced yet" and that all other baselines were run with official implementations. It does not state whether the TRF numbers were obtained by re-implementing from the paper description, by running a private implementation, or by transcribing from the TRF publication (which would use different data splits/preprocessing). The paper should clarify this. *(Note: this does not invalidate the comparison — the vanilla variant also beats TRF, and the qualitative results are consistent — but the missing detail is a transparency concern.)*

2. **DynamiCrafter comparison uses different resolution and frame count.** In Table 1, DynamiCrafter is evaluated at 512×320 with 16 frames, while ViBiDSampler uses 1024×576 with 25 frames. LPIPS, FID, and FVD are sensitive to both resolution and temporal length, making this comparison not directly apples-to-apples. The paper should either evaluate DynamiCrafter at the same resolution (even if suboptimal for DynamiCrafter) or prominently acknowledge the mismatch.

3. **Small evaluation sets with no confidence intervals.** DAVIS has 100 examples and Pexels has 45 examples. FVD is known to have high variance on small sample sizes. No error bars, confidence intervals, or statistical significance tests are reported. Given that the margins over some baselines are modest, this is a concern.

4. **The off-manifold claim is asserted geometrically but never directly measured.** The paper's central narrative (Figure 2) is that fusion produces off-manifold samples while sequential sampling stays on-manifold. This is a mechanistic claim, but the only evidence is downstream metrics (LPIPS, FID, FVD) and qualitative comparisons. While these are consistent with the claim, they do not directly test it. A direct manifold-deviation metric (e.g., distance between intermediate latents and their denoised estimates, or FID of intermediate steps) would strengthen the paper significantly.

### Trivial

- The motion bucket ID was fixed at 127, and fps was manually adjusted per case ("we applied a lower fps for cases with large motion and a higher fps for cases with smaller motion," line 192). This tuning is not part of a fully reproducible protocol and should be automated or documented per-case.

## Nice-to-Haves

- A controlled experiment applying CFG++ and DDS to a fusion-based sampler (e.g., a re-implemented TRF pipeline without its multiple re-noising rounds) would directly test whether the sequential ordering or the guidance techniques drive the gains.
- A direct quantitative measure of manifold deviation (e.g., distance from latent to its denoised estimate) for both fusion and sequential approaches would substantiate the claimed mechanism.
- DynamiCrafter evaluated at the same resolution and frame count would clean up the comparison in Table 1.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Harsh critic's claim that the TRF comparison "cannot be assessed" and is "unverifiable":** The paper states TRF hasn't been open-sourced, and the reviewer's strongest language about unverifiability is removed per the hard rules (the rule explicitly removes "cannot be independently verified" phrasing and reproducibility concerns rooted in doubting a cited entity's existence). The underlying transparency concern is retained as a minor weakness above.
- **Harsh critic's concern about Table 2 NFE column formatting:** This is a presentation nitpick; the per-frame NFE can be inferred and the table is self-contained enough.
- **Harsh critic's criticism about missing related works:** Removed per hard rules (no external sources to confirm).
- **Various formatting/style nitpicks from the harsh critic:** Removed per formatting/typo rules.

## Novel Insights

The harsh critic's observation that the paper's off-manifold mechanism is asserted but never directly measured is an insightful meta-point that applies broadly to the diffusion literature: many papers claim "on-manifold" properties based only on downstream metrics. The strength finder's observation that the vanilla variant beats TRF on all metrics is the cleanest evidence for the paper's core claim and is worth emphasizing. Together, these suggest the method is empirically sound but its theoretical framing is stronger than its evidence supports.

## Suggestions

1. **Add the missing control experiment:** Apply CFG++ and DDS to the TRF fusion pipeline (or a minimal fusion sampler) and compare. This is the single highest-leverage improvement to the paper.
2. **Fix Table 3:** Swap the LPIPS and FVD row labels — the values are clearly swapped with each other.
3. **Clarify TRF results:** State explicitly how TRF numbers were obtained (re-implementation? cited from another paper?).
4. **Acknowledge resolution mismatch for DynamiCrafter** in the main text, or re-evaluate at matched resolution.
5. **Add a direct manifold-deviation metric** to substantiate the geometric claim in Figure 2.
6. **Report confidence intervals** for the main quantitative results given the small evaluation sets.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
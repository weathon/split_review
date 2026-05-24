I have thoroughly reviewed the paper and all reviewer claims. Now I'll produce the final consolidated review.

## Summary

HiSplat introduces a hierarchical (coarse-to-fine) 3D Gaussian representation for generalizable sparse-view novel view synthesis. It generates large-scale "skeleton" Gaussians first, then adds fine-grained "detail" Gaussians, with two inter-scale modules—the Error Aware Module (EAM) for Gaussian compensation and the Modulating Fusion Module (MFM) for Gaussian repair—that enable joint optimization across scales. Experiments on RealEstate10K, ACID, DTU, and Replica show consistent improvements over single-scale baselines.

## Strengths

1. **Clear quantitative improvement over single-scale baselines**: On RealEstate10K, HiSplat achieves **27.21 PSNR**, outperforming MVSplat by +0.82 PSNR and TranSplat by +0.52 PSNR (Table 1). On ACID, it achieves 28.75 PSNR, +0.50 over MVSplat. These gains are consistent across all three metrics (PSNR, SSIM, LPIPS).

2. **Substantial cross-dataset generalization gains**: In zero-shot testing (trained on RealEstate10K), HiSplat improves PSNR by **+3.19 on Replica** (27.17 vs. 23.98 for PixelSplat) and **+1.12 on DTU** (16.05 vs. 14.93 for TranSplat) (Table 2). The gain on Replica is particularly striking and suggests the hierarchical representation transfers better to unseen scene distributions.

3. **Ablation confirms each module contributes meaningfully**: Removing both EAM and MFM ("Hier only") yields 26.18 PSNR—below even the single-scale MVSplat baseline (26.39). Adding EAM raises to 26.76, adding MFM raises to 27.02, and the full model reaches 27.21 (Table 3). This step-by-step degradation cleanly demonstrates that the inter-scale interaction mechanisms, not just the multi-scale features, drive the improvement.

4. **Analysis of Gaussian properties validates the "bone to flesh" hypothesis**: Section 4.4 quantitatively shows that stage-1 Gaussians are large, solid, and sparse, while later-stage Gaussians are small, transparent, and dense (Figure 5). This directly confirms the intended coarse-to-fine behavior and provides interpretability for the method's success.

5. **Error map visualizations show progressive refinement**: Figure 6 demonstrates that rendered error maps decrease across stages, especially in complex texture regions, providing qualitative evidence that the EAM and MFM correct errors from earlier stages.

6. **Works with only two input views**: The entire pipeline is designed for the most challenging two-view setting, achieving SOTA without multi-view optimization or per-scene finetuning.

## Weaknesses

### Major
None. No weakness here is severe enough to threaten the paper's core empirical claims or warrant weighing against acceptance.

### Minor

1. **Reference-view error guidance is not directly validated as a proxy for novel-view errors**: The Error Aware Module (Section 3.3) computes an error map `|I_rendered_ref - I_input_ref|` from the *reference* views and uses this to predict depth offsets and Gaussian features for later stages. The paper never analyzes whether errors in the reference views actually correlate with reconstruction errors in the *target* novel views. In principle, a region could be perfectly rendered in the reference views yet require additional Gaussians for a novel view (e.g., disocclusion), and the module would have no signal to add them. While the ablation (Table 3: EAM adds +0.76 PSNR) and error-map visualizations (Figure 6) show the method works end-to-end, this intermediate assumption is not empirically validated. This does not undermine the results, but it is a gap in the evidence chain for how the mechanism operates. The authors could address this by, e.g., measuring the correlation between reference-view error maps and novel-view rendering errors.

2. **Vanilla hierarchical baseline is underspecified**: The "Hier only" ablation row (26.18 PSNR, Table 3) is described as "extracting multi-scale features to generate hierarchical 3D Gaussians and mixing them for rendering" (Section 1). It is not specified how later-stage Gaussian depths are determined without the Error Aware Module—whether they are simply interpolated from stage 1, independently predicted via the same cost-volume approach, or computed some other way. This makes it harder to interpret what the baseline failure specifically means. A clearer specification would improve reproducibility and the informativeness of the ablation.

3. **No sensitivity analysis for the depth offset coefficient η**: The Error Aware Module constrains depth offsets to `±η·Interp(D_{i-1})` with η=0.1 (Section 3.3, Eq. 2). This parameter controls how far decorative Gaussians can deviate from the skeleton Gaussians and could significantly affect reconstruction quality. No ablation or sensitivity study is provided for this design choice.

4. **No limitations discussion**: The paper lacks a dedicated limitations section. Several aspects worth acknowledging include: (a) the additional computational cost of three-stage rendering during training, (b) scenarios (e.g., large disocclusions) where reference-view error signals might be insufficient, and (c) the assumption that depth offsets should be a fixed fraction of previous-stage depth.

### Trivial
None.

## Nice-to-Haves

- Consider placing a brief efficiency comparison (inference time, GPU memory) in the main results section rather than only in the appendix (currently referenced as `\ref{sec_app:efficiency}`). A single sentence such as "HiSplat runs at X fps with Y GB GPU memory, compared to Z for MVSplat" would help readers gauge the practical trade-off.
- Clarify the number of Gaussians predicted per pixel per stage, which is currently implicit from following PixelSplat's conventions.

## Removed Points

These points were raised by reviewers but are removed through the filtering process:

- **"Missing efficiency comparison in main text"** → Moved to Nice-to-Haves. The paper references the appendix for these numbers, which is standard practice; requesting main-text placement is a presentation preference, not a weakness.
- **"Statistical significance not reported"** → Removed. Single-run evaluation on large-scale benchmarks is standard in this subfield; the improvements are large enough that significance is not in question.
- **"Per-stage Gaussian count not specified"** → Removed. The paper follows PixelSplat's established conventions; this is a trivial implementation detail.
- **"DINOv2 features add only marginal gain (+0.19 PSNR)"** → Removed. This is an observation, not a weakness. The paper presents this honestly and it does not undermine the contribution.
- **"Could reference-view errors be a speculative limitation?"** → Subsumed into Minor weakness #1 above, where it is framed as a gap in mechanistic understanding rather than a fatal flaw. The critic's framing as potentially "fatal" is not supported by the paper's strong empirical evidence.

## Novel Insights

The most interesting observation across the reviews is the interplay between the "bone to flesh" Gaussian property analysis and the ablation study. The ablation shows that naive hierarchical stacking ("Hier only") underperforms the single-scale MVSplat baseline, yet the Gaussian property analysis reveals that when the EAM and MFM are added, the different-scale Gaussians exhibit cleanly separated roles (sparse/solid/large vs. dense/transparent/small). This suggests that the core challenge in hierarchical 3D Gaussian representations is not in having multi-scale features, but in designing the *information routing* between scales—the error-aware compensation and opacity modulation directly enforce functional differentiation. The paper's specific contribution is demonstrating that inter-scale *interaction* (not just multi-scale *representation*) is what unlocks the benefit. A follow-up question this raises is whether alternative routing mechanisms (e.g., learned offsets without error guidance, attention-based feature fusion) could achieve similar differentiation, or whether the error-aware signal is uniquely effective.

## Suggestions

1. Add a brief analysis directly measuring the correlation between reference-view error maps and novel-view reconstruction errors. This would close the most substantive evidential gap and strengthen the paper's internal narrative.
2. Specify the vanilla hierarchical baseline implementation in detail (how later-stage depths are determined without EAM) to improve clarity and reproducibility.
3. Add a sensitivity study for the depth offset coefficient η (e.g., η ∈ {0.05, 0.1, 0.15, 0.2}) to demonstrate robustness or inform the reader of the parameter's effect.
4. Include a brief limitations subsection to proactively address the method's scope and potential failure cases.

## Score and Decision

**Originality:** The paper is the first to introduce hierarchical 3D Gaussian representations in the generalizable (feed-forward) setting. The two inter-scale interaction modules (EAM, MFM) are technically novel.  
**Importance of research question:** Sparse-view reconstruction is a practically important problem. Improving reconstruction quality in this setting has clear value.  
**Claims supported:** The core claim—that hierarchical 3D Gaussians with inter-scale interaction outperform single-scale methods—is well-supported by extensive experiments across four datasets and thorough ablation studies.  
**Soundness of experiments:** The experimental setup follows established protocols in the field, with fair comparisons to prior methods, comprehensive ablation, and insightful qualitative analysis.  
**Clarity of writing:** The paper is clearly written and well-structured. The coarse-to-fine "bone to flesh" metaphor is effective for communicating the core idea.  
**Value to community:** The method achieves new SOTA on multiple benchmarks, and the analysis of Gaussian properties provides useful insights for future work on hierarchical 3D representations.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>
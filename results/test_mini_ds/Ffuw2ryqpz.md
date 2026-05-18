Now I have enough information to write the final consolidated review. Let me synthesize everything.

## Summary

Real3D introduces a self-training framework for Large Reconstruction Models (LRMs) that enables training on single-view real-world images without multi-view supervision. The framework combines (1) a cycle-consistency pixel loss with curriculum learning and stop-gradient, (2) a CLIP-based semantic loss with hard negative mining, and (3) automatic data curation. The model is jointly trained on synthetic Objaverse data and 300K curated real images. Evaluated across four datasets (MVImageNet, CO3D, OmniObject3D, and a newly collected in-the-wild test set), Real3D consistently outperforms the TripoSR baseline with ~0.7 PSNR average improvement.

## Strengths

- **Enables training LRMs on single-view real-world images for the first time.** Prior LRMs required multi-view images or 3D ground truth; Real3D's self-training framework breaks this bottleneck. The paper demonstrates this concretely by collecting and training on 300K real images, achieving consistent improvements over TripoSR across all evaluations (Table 1: CLIP 0.892 vs. 0.860; Table 3 CO3D: PSNR 19.18 vs. 18.44; Table 5 OmniObject3D: PSNR 20.17 vs. 19.43).

- **Clean ablation study validates each component.** The ablation on CO3D (Table 4) meticulously breaks down the contribution of each design choice. The paper shows that naive semantic loss *hurts* performance (17.89 PSNR vs. 18.44 baseline), and that cycle-consistency requires *both* curriculum learning and stop-gradient to help (17.78 PSNR without stop-gradient vs. 19.18 with both). Data curation provides a 0.39 PSNR gain.

- **Larger improvement from single-view real data than prior methods achieve from multi-view real data.** On MVImageNet, Real3D's Δ over the synthetic-only baseline is 2.08 PSNR on input-view evaluation, while LRM* (trained on multi-view MVImageNet data) achieves Δ of only 1.28. A similar pattern holds on CO3D (Δ 0.74 vs. 0.51). This is a genuine insight about the value of diverse single-view data versus in-domain multi-view data.

- **Scalability demonstrated with increasing data volume.** The paper reports that adding more real images (50K to 300K) yields consistent PSNR improvements, supporting the core claim that this approach can benefit from web-scale image collections.

## Weaknesses

### Fatal
None.

### Major

- **The self-consistency metric on the in-the-wild test set is correlated with the training loss.** The Real3D test set (Table 2) is evaluated on self-consistency metrics (render → reconstruct → render original view → compare) that are structurally similar to the cycle-consistency training loss. While the CO3D and OmniObject3D evaluations (Tables 3, 5) use standard, independent NVS metrics and provide clean evidence of improvement, the paper's claim about "superior performance on in-the-wild data" (Abstract, Sec. 4.1) relies partly on metrics that the model was directly optimized for. The semantic similarity metrics (CLIP, LPIPS, FID) partially mitigate this concern since they use a different evaluation protocol (7 uniformly sampled views vs. the training's hard-negative-mined setup), but the self-consistency metrics remain entangled. **Impact:** Weakens but does not invalidate the in-the-wild evaluation; the real evidence for improvement comes from the CO3D/OmniObject3D results.

### Minor

- **The data curation method is underspecified.** Section 3.3 describes "leveraging the synergy between instance segmentation and single-view depth estimation" for automatic occlusion detection but does not state which segmentation model, which depth estimator, or what occlusion thresholds were used. This makes the curation pipeline unreproducible as described. The ablation (Table 4) does isolate the effect of cleaning, so the *impact* is validated, but the *method* is not.

- **No hyperparameter sensitivity analysis.** The training objective has three hand-picked loss weights (λ_pix=5.0, λ_sem=1.0, λ_in=0.3), a curriculum schedule (linear 15°→90°), and a semantic loss with m=4 views. None of these are ablated or analyzed for sensitivity. While the core ablation is strong, missing sensitivity analysis on these hyperparameters weakens the method's robustness understanding.

- **"Fine-tuned TripoSR" is ambiguous.** The paper states "a fine-tuned TripoSR" (line 85) and that "All TripoSR results are after fine-tuning" (line 225), but does not clarify what the fine-tuning procedure was or whether the fine-tuned checkpoint differs from the publicly released one. This is a reproducible-detail gap.

- **The cycle-consistency pipeline's intermediate reconstruction quality is not analyzed.** The paper assumes that feeding a rendered novel view back into the LRM produces a reasonable reconstruction. While TripoSR is pose-agnostic (it does not condition on input pose), and the curriculum mitigates errors by starting at small pose offsets, no analysis is provided of what fraction of intermediate reconstructions are geometrically plausible (e.g., what % produce recognizable shapes, or what the LPIPS is between the first and second reconstructions). The ablation shows the loss empirically works, but the mechanism remains a black box.

### Trivial
None.

## Nice-to-Haves

- Show failure cases where the cycle-consistency or semantic loss introduces artifacts.
- Report training time / computational cost of the two-pass cycle-consistency relative to standard LRM training.
- Add a comparison with a variant that uses depth regularization as an additional unsupervised signal.
- Ablate alternative curriculum schedules (exponential, step-wise) or different values of m (number of semantic views).

## Removed Points

- **"The cycle-consistency loss assumes LRM can handle non-canonical inputs"** — The paper explicitly uses TripoSR, which is "an LRM without input pose and intrinsics conditioning" (line 85), meaning it handles its own canonicalization. The curriculum (15°→90°) is explicitly designed to address degradation from inaccurate novel views. The critic's framing of this as a potentially fatal flaw is unsupported; the paper addresses it.

- **"The ablation does not isolate the data curation effect"** — This is factually incorrect. Table 4 rows (3) specifically compares "Clean Data" ✓ vs. ✗ while holding all other factors constant (18.79 vs. 19.18 PSNR), which cleanly isolates curation.

- **Missing related works** — Speculative; not verifiable without external sources.

- **Formatting/presentation nitpicks, typos, appendix references** — Parser artifacts; not author errors.

## Novel Insights

The most interesting finding beyond the paper's own framing is in the comparison with LRM*: training on *single-view real images* across diverse domains produces larger improvements than training on *multi-view real images* from a single dataset (MVImageNet). This suggests that data diversity (wide coverage of shapes and appearances) may be more important than multi-view supervision per se when the model already has a strong 3D prior from synthetic data. Table 2 (in-the-wild test set) reinforces this: LRM* shows nearly zero improvement on out-of-distribution images (Δ PSNR 0.26), while Real3D shows a clear gain (0.72). This is a useful datapoint for the community about how to allocate data collection resources for LRM training.

## Suggestions

1. For the in-the-wild evaluation, either (a) add a non-circular metric such as estimated depth map accuracy or human evaluation, or (b) clearly separate the self-consistency results from the main claims and emphasize the CO3D/OmniObject3D NVS results as the primary evidence.
2. Specify which segmentation and depth estimation models were used for data curation, along with the occlusion detection threshold.
3. Add a small hyperparameter sensitivity study (e.g., vary λ_pix and λ_sem by 2× on CO3D) and report the m=4 design choice.
4. Clarify what "fine-tuned TripoSR" means — what data was it fine-tuned on, and is the checkpoint different from the public release?
5. Include a qualitative analysis of the second-pass reconstruction in the cycle-consistency pipeline to demystify the mechanism.

## Score and Decision

**Round 1 — Bracketing:** Initial search placed this paper above weak anchors (avg 3.00) and below strong anchors (avg 8.00), within the middle bracket [4, 7].

**Round 2 — Narrowing:** Compared directly against:
- Hi-Gaussian (5.75): Real3D is stronger — more novel contribution (self-training framework enabling real-image training), cleaner ablations, and more comprehensive evaluation across 4 datasets vs. Hi-Gaussian's incremental improvement over Splatter Image.
- Magic123 (6.50): Magic123 had more visually impressive qualitative results but was criticized as "A+B" (combining 2D and 3D diffusion priors). Real3D's contribution is more systematic (loss design + curriculum + curation) but its quantitative gains are more modest (~0.7 PSNR). Real3D is slightly below Magic123 due to the metric-circularity concern and underspecified curation details.

**Final anchoring:** Real3D is clearly stronger than Hi-Gaussian (5.75) and comparable to, but slightly below, Magic123 (6.50). Setting score at 6.0 reflects a solid, well-executed paper with a genuine contribution, held back from a higher score by the entanglement between training loss and one evaluation metric and by missing methodological details.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
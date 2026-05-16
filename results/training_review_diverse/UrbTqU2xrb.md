I have thoroughly verified the paper against all reviewer claims. Here is my consolidated review.

---

## Summary

This paper proposes the first feed-forward pipeline for clothing-disentangled 3D character generation from a single image. The method uses a two-stage approach: first, a multi-part diffusion model with a novel multi-part attention mechanism disentangles body and clothing in 2D image space; then, a multi-view diffusion model with a combination attention module generates multi-view images of each part, which are fed into an off-the-shelf feed-forward 3D reconstruction method (LGM). The paper also contributes a dataset of >10k clothing-disentangled anime characters with 11 clothing combinations each. Ablations show the proposed attention mechanisms improve disentanglement quality over baselines.

## Strengths

1. **First feed-forward method for clothing-disentangled 3D generation from a single image.** The paper correctly identifies that existing approaches (GALA, Feng et al., ClothNeRF) rely on per-scene optimization taking hours, while this work proposes a feed-forward alternative. This is a genuine practical advance, and the literature review accurately characterizes the gap (Sec. 1, Sec. 2).

2. **Novel two-stage disentanglement pipeline with technically grounded attention mechanisms.** The design choice to separate 2D part disentanglement from multi-view generation simplifies each subtask. The multi-part attention (Eq. 2, allowing cross-part information flow) and the combination attention module (Sec. 3.2, using a special condition image) are well-motivated architectural contributions, and the ablations (Table 2, Fig. 4, Fig. 5) quantitatively confirm that each component improves over simpler alternatives.

3. **Large-scale clothing-disentangled dataset as a community resource.** At >10k characters with 11 clothing combinations per character (>110k unique models), this dataset is substantially larger than existing alternatives (<1,000 subjects). The controlled-visibility rendering pipeline is a rigorous contribution that enables training and evaluation of this class of methods.

4. **Intrinsic support for clothing editing and transfer.** The disentangled representation naturally enables virtual try-on (Fig. 6) and animation (Fig. 7) without additional networks, which is a clean byproduct of the architecture design.

## Weaknesses

### Fatal
None.

### Major

1. **No quantitative evaluation of the final 3D output.** Despite the paper's title and core claim being about 3D character generation, all quantitative metrics (PSNR, SSIM, LPIPS in Tables 1 and 2) evaluate only the intermediate 2D multi-view images. The 3D models are shown only in qualitative figures (Figs. 5–7). Since the authors have ground-truth 3D models in their dataset, computing 3D metrics (e.g., per-part Chamfer distance, volumetric IoU, F-score) is straightforward. The paper uses an off-the-shelf 3D reconstruction method (LGM), so the quality of the final 3D output depends on both the generated multi-view images and the reconstruction step; without 3D metrics, the reader cannot assess the end-to-end quality. This is a significant evidential gap for a paper whose central contribution is 3D generation.

2. **No runtime or efficiency numbers reported.** The introduction and abstract repeatedly claim the method reduces generation "from several hours to mere seconds," and the contributions list states "high-quality results in a few seconds." Yet no actual inference time is reported anywhere in the experiments. The only time-related number is the LGM reconstruction time (1 second), which covers only one sub-step of the pipeline. This directly undermines the primary claimed advantage over optimization-based methods. This weakness is trivially fixable but currently absent.

3. **No direct comparison with optimization-based clothing-disentanglement methods.** The paper positions itself against prior work like GALA, ClothNeRF, and Feng et al., but the only experimental baseline is an adapted Wonder3D evaluated on multi-view image quality. While this adapted baseline is reasonable for the image-generation subtask, the paper does not compare end-to-end 3D quality against any prior clothing-disentanglement method, even on a small subset. This makes it difficult to assess whether the feed-forward approach achieves competitive quality, which is important since the paper claims both speed *and* quality advantages.

### Minor

1. **Cross-part consistency is not explicitly evaluated.** The method generates multi-view images for each part independently (with information exchange only through the multi-part attention in the 2D stage). The optional 3D optimization (Eq. 3) only adjusts rigid transformations. The paper does not evaluate whether parts are well-aligned (e.g., measuring interpenetration volume, gaps between part meshes, or rendering consistency at part boundaries). This does not threaten the core contribution but would strengthen the claims of seamless composition.

2. **No analysis of failure cases or typical failure modes.** The paper presents only successful results. Discussing common failure cases (e.g., complex overlapping garments, unusual clothing combinations, occluded body regions) would help readers understand the method's practical limitations. The Limitations section (Sec. 4.6) only discusses dataset size and static clothing.

3. **Some implementation details are underspecified.** The "special condition image" for the combination attention module (Sec. 3.2) is described only as being introduced for part combination, but its specific form (blank canvas? masked composite? learned embedding?) is not clearly stated. The integration of the part-type one-hot encoding with positional encoding "concatenated with the time embedding" is stated but not visualized or detailed sufficiently for easy reproduction. These do not invalidate the method but hinder reproducibility.

### Trivial
None.

## Nice-to-Haves
- A small user study comparing subjective quality against the adapted Wonder3D baseline or ground-truth renders would strengthen the qualitative claims about anime character appearance.
- Ablation results on the 3D part model composition (Fig. 5, right) are currently qualitative only; reporting rendering PSNR against ground-truth composed 3D models would add rigor.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"No evaluation on real-world images"** — The paper explicitly scopes to anime characters from rendered data. Criticizing the absence of real-world generalization is scope creep for a method that trains and evaluates on a rendered anime dataset.
- **"No user study"** — A user study is a nice-to-have, not a required weakness for a technical 3D generation paper.
- **"Hyperparameter sensitivity not studied"** — The paper reports batch sizes, training steps, and hardware setup. Full hyperparameter sensitivity studies are beyond the standard scope for this class of paper.
- **Criticisms about missing appendix content** — The parser strips those sections; they exist in the original submission.

## Novel Insights

The reviews reveal a clear pattern: this paper has genuine architectural novelty (first feed-forward pipeline, well-designed attention mechanisms) and a strong dataset contribution, but the evaluation design does not match the scope of the claims. The central tension is that the paper's title, abstract, and contributions emphasize *3D* generation, yet the quantitative evidence stops at the 2D image level. This is not because the paper is poorly executed — the ablations convincingly show that the attention mechanisms work — but because the authors appear to have stopped short of running the straightforward evaluation that their own dataset enables. The missing runtime numbers compound this: a paper whose main differentiator is speed cannot simply assert "seconds" without measurement. This is a paper whose contribution is real but whose evidence is incomplete in ways that are fixable without changing the method.

## Suggestions

1. **Report 3D reconstruction metrics** on the held-out 500 characters using ground-truth 3D models. Compute per-part Chamfer distance, F-score, and volumetric IoU for the combined 3D model. This directly addresses the largest gap in the evaluation.
2. **Report inference time** for the full pipeline (2D disentanglement + multi-view generation for each part + 3D reconstruction + optional optimization) and compare to the time a representative optimization-based method would require on the same input.
3. **Add a small-scale comparison** against at least one optimization-based clothing-disentanglement method (e.g., run GALA on a few examples, or cite runtime figures from prior work as a reference point) to contextualize the quality–speed trade-off.
4. **Clarify the "special condition image"** — state explicitly whether it is a blank image, a masked composite of part images, or a learned embedding.
5. **Include a failure case figure** showing 2–3 typical failure modes to help readers calibrate expectations.

## Score and Decision

The paper presents a novel and well-motivated feed-forward pipeline for clothing-disentangled 3D character generation, supported by a substantial dataset contribution and informative ablations. However, the evaluation has three significant gaps: (1) no quantitative metrics on the final 3D output, (2) no runtime measurements to support the central speed claim, and (3) no direct comparison with prior clothing-disentanglement methods. These gaps mean the evidence does not fully match the claimed contributions. The issues are fixable with additional experiments, but they require non-trivial additional work.

**Originality**: Good — first feed-forward approach, novel attention designs. **Importance**: Good — clothing-disentangled 3D generation is practically relevant. **Claims vs. support**: Weak — core claims about 3D quality and speed are not quantitatively supported. **Soundness**: Adequate methodologically, but incomplete evaluation. **Clarity**: Good — well-structured and generally clear. **Value to community**: Moderate — dataset and approach could be valuable, but evaluation gaps limit current impact.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
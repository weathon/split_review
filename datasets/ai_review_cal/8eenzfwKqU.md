- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 6, 5
Now I have a thorough understanding of the paper and the reviews. Let me construct the final consolidated review.

---

## Summary

GS-VTON introduces an image-prompted 3D virtual try-on method built on 3D Gaussian Splatting (3DGS). It combines (1) a personalized diffusion model via LoRA fine-tuning on multi-view edited images, (2) reference-driven image editing that concatenates attention features from a reference view to enforce cross-view consistency during multi-view editing, and (3) a persona-aware 3DGS editing mechanism that blends attention features from the editing direction and the edited image set to maintain coherence during 3D scene optimization. The paper also introduces 3D-VTONBench, a new benchmark with 60 subjects for evaluating 3D VTON.

## Strengths

1. **Reference-driven image editing for multi-view consistency** (Sec. 3.2, Eq. 5–6): Concatenating key/value attention features from a reference image during simultaneous multi-view editing is a clean, technically sound approach to enforcing consistency. The ablation study (Fig. 9) visually confirms that removing this component causes texture mismatch with the input garment.

2. **Persona-aware 3DGS editing** (Sec. 3.3, Eq. 7): Blending attention features from the editing direction and the original edited image set via coefficient λ is a well-motivated mechanism for maintaining coherence during 3D optimization. The ablation (Fig. 8) shows that without it, the edited scenes fail to maintain consistent texture across frames.

3. **User study evidence of practical superiority**: With 25 volunteers and 625 pairwise comparisons (Sec. 4.1, Fig. 7), GS-VTON is consistently chosen as best in realism, garment similarity, and overall performance across five comparison methods. This provides real (albeit preference-based) evidence that the method delivers visibly better 3D VTON results.

4. **First dedicated 3D VTON benchmark**: 3D-VTONBench (60 subjects, varied poses and garments) fills a clear gap — existing benchmarks focus on 2D VTON or SMPL-based dressing, not general 3D scene editing for garment transfer. This is a useful community resource.

5. **Resolution flexibility**: Unlike prior 3D editing methods constrained to 512×512 by Instruct-Pix2Pix, GS-VTON can edit at the original scene resolution (Sec. 3.4 / Implementation Details), which is a practical advantage for high-fidelity applications.

## Weaknesses

### Fatal
None.

### Major

1. **No objective/automated evaluation metrics on the benchmark, and the benchmark is not used to ground the method's performance claims.** Despite introducing 3D-VTONBench as a core contribution and claiming "comprehensive qualitative and quantitative 3D VTON evaluations," the paper reports no automated metrics — not even CLIP similarity to the garment image, multi-view consistency scores (e.g., LPIPS between adjacent views), or FID on the edited dataset. The only quantitative evaluation is a user study measuring human preference, not fidelity. The benchmark is announced but adds no empirical weight to the evaluation. Given that multi-view consistency is a central claimed contribution, the absence of any direct consistency metric is a significant gap. *(Anchored to: Sec. 4 claim of "comprehensive... quantitative evaluations"; Sec. 4.1 user study as the sole quantitative eval; 3D-VTONBench description on p. 8.)*

2. **Comparison methods operate on text prompts only, while GS-VTON uses image prompts — a fundamentally more informative input modality.** The paper translates garment images to text via ChatGPT (a reasonable-faith attempt at fairness), but text cannot capture fine-grained garment details. It is unsurprising that an image-prompted method outperforms text-prompted methods on "similarity to the garment image." The user study results therefore mainly validate that images are better prompts than text, rather than demonstrating that the paper's specific technical components (reference-driven editing, persona-aware attention) are superior to simpler alternatives. The paper acknowledges that GaussianVTON's code is unavailable, but the comparison remains staged to favor the proposed approach. *(Anchored to: Sec. 4, "Comparison Methods" paragraph; Fig. 7 user study results.)*

3. **The ControlNet conditioning mechanism is critically underspecified.** The paper states: "we adapt it via a ControlNet-based stable diffusion inpainting model to condition the inpainting process on the input garment image." No details are provided about (a) what the conditioning signal is (Canny edges, depth, garment image embedding, or something else), (b) whether the ControlNet is trained from scratch or fine-tuned from a pre-trained checkpoint, (c) the ControlNet architecture, or (d) the training data or procedure. Given that this component is central to the pipeline — it injects the garment image as a conditioning signal during 3DGS editing — the lack of specification makes the method irreproducible as described. *(Anchored to: Eq. 7 in Sec. 3.3; Implementation details in Sec. 3.4, which only mention Stable-Diffusion-2-Inpainting and RealFill hyperparameters but say nothing about ControlNet training or architecture.)*

### Minor

1. **No sensitivity analysis or ablation on the blending coefficient λ.** The persona-aware 3DGS editing uses λ = 0.55 with no analysis of how varying λ affects the trade-off between editing strength and cross-view consistency. The method's sensitivity to this hyperparameter is unclear. *(Anchored to: Eq. 7, λ = 0.55.)*

2. **The loss function compares the edited image to the source rendered image using MAE and LPIPS.** Since the goal is to modify the garment, penalizing differences from the original image may conflict with the editing objective — large desirable garment changes could be penalized. The paper does not discuss why this loss formulation is appropriate for the VTON task. *(Anchored to: Eq. 8 in Sec. 3.3.)*

3. **User study lacks statistical rigor.** The results are shown as bar chart percentages without confidence intervals, statistical significance tests, or measures of inter-annotator agreement. With 25 volunteers, reporting whether observed differences are statistically significant would strengthen the claims. *(Anchored to: Sec. 4.1.)*

4. **No runtime comparison with baseline methods.** The paper reports ~55 minutes for GS-VTON on a V100, which is reasonable, but does not report comparable runtimes for the five comparison methods, making it hard to assess practical trade-offs. *(Anchored to: Sec. 3.4 Implementation Details.)*

### Trivial
None.

## Nice-to-Haves

- A within-method controlled experiment comparing GS-VTON with image prompts vs. text prompts (using the same pipeline) would isolate the benefit of the technical components from the benefit of the input modality.
- An ablation or justification for fixing n=4 for the edited image set (the paper refers to the appendix, which is unavailable here).
- A sensitivity analysis on λ would strengthen the method's empirical grounding.
- A breakdown of user study results by garment type or pose complexity would improve evaluation informativeness.

## Removed Points

- **Missing ablation on number of images n**: The paper refers to the appendix for this analysis; the appendix is stripped by the parser. Per policy, weaknesses about missing appendix content are removed.
- **"Why use only the first image as reference"**: This is a design choice question, not an evidence-based weakness. Moved to Nice-to-Have.
- **Generic scope-creep concerns** (e.g., requesting confidence intervals beyond standard practice for user studies in this area): Weakened or removed per filtering rules.
- **Strength Finder claims that were generic or not specific to this paper**: None needed removal — all five claimed strengths are concrete and paper-specific.

## Novel Insights

The key takeaway that emerges from synthesizing the reviews is that GS-VTON's core methodological architecture — using attention feature concatenation during multi-view editing as a bridge between 2D VTON models and 3DGS — is novel and technically sound, but the evidence for its effectiveness is weakened by an evaluation design that does not cleanly separate the benefit of the image-prompt modality from the benefit of the proposed technical components. The ControlNet underspecification is a genuine reproducibility concern. The paper would be substantially strengthened by reporting even a single automated metric (CLIP similarity or a consistency score) on its own benchmark, which would leverage the benchmark contribution and provide a direct, reproducible signal of fidelity.

## Suggestions

1. **Add at least one automated metric** on 3D-VTONBench: CLIP image similarity between rendered views and the garment image, and/or average LPIPS between adjacent novel views of the edited scene as a consistency score. This directly supports the two core claims (garment fidelity and multi-view consistency) and gives the benchmark immediate utility.
2. **Specify the ControlNet conditioning in full**: what signal is used for conditioning (image embedding, edge map, etc.), whether the ControlNet is trained from scratch or adapted from a pre-trained one, and the training data/procedure.
3. **In the revision, add a sensitivity analysis on λ** (the blending coefficient) over a range around 0.55, showing the effect on at least one of the proposed automated metrics.
4. **Consider adding a text-prompted version of the same pipeline** as a control in the user study, to isolate the contribution of the image-prompt modality from the contribution of the technical components.
5. **Report confidence intervals or significance tests** for the user study results.

---

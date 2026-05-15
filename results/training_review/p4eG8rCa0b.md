Now I have sufficient information from the paper. Let me compose the final consolidated review.

Let me carefully think through each element.

**Verification of key claims:**

1. **Unfair evaluation (Harsh Critic Issue 1):** The paper states at line 107: "Since our model accepts two depth maps and two exemplar images, note that we condition the same images for each modality in Figure 3." At line 112: "this may be attributed to the fact that while baseline models only take in a single depth map extracted from the validation image, our model takes in an additional depth map." And for reconstruction (line 128): "our model utilizes the depth maps and CLIP image embeddings extracted from the image triplets of ground truth validation images, and baseline models utilize the depth maps and CLIP image embeddings extracted from the ground truth images, since they do not support more than one condition per modality."

So the paper IS transparent about this. The critic is correct that the comparison is unequal, but the paper acknowledges this. However, the critic goes too far by saying this "invalidates the headline claims" — the ablation in Figure 4 (DDT vs. full depth map) DOES isolate the contribution of DDT via a fair comparison. The critic ignores this. I'll note this in the review.

2. **No quantitative evaluation of core claims (Issue 2):** The paper's core claims are about (a) 3D depth ordering and (b) disentangled semantics. FID, IS, CLIPScore don't test these. Depth MAE partially tests depth fidelity but not depth ordering correctness. There's no metric for whether the foreground region actually uses foreground semantics vs. background semantics. This is a valid major weakness.

3. **Inference-time mask for soft guidance (Issue 3):** The paper describes how M is obtained during training (from synthetic triplets), but doesn't specify how the user provides it at inference for novel generation. This is a valid minor weakness.

Let me now write the review, following the structure and rules carefully.Here is my consolidated final review.

## Summary

This paper proposes Compose and Conquer (CnC), a conditional diffusion model that addresses two challenges: (1) 3D depth-aware placement of multiple objects through Depth Disentanglement Training (DDT), which uses synthetic image triplets to teach the model about occluded regions, and (2) localization of global semantics from multiple exemplar images onto specific regions via Soft Guidance, which masks cross-attention similarity matrices. The method is built on Stable Diffusion with cloned encoder/center blocks and separate local/global fuser modules.

## Strengths

- **Depth Disentanglement Training is a genuinely novel and well-motivated training paradigm.** The idea of using synthetic image triplets (foreground, inpainted background, mask) to teach a diffusion model about occluded depth relationships addresses a real limitation in prior controllable generation work. The ablation in Figure 4 provides controlled evidence: DDT-trained models (processing separate foreground/background depth maps) correctly handle occlusion and depth ordering, whereas models trained on the single full-depth-map representation fuse objects or ignore the foreground. This comparison is fair and supports the value of the architectural choice.

- **Soft Guidance offers an elegant mechanism for localized semantic injection without explicit spatial cues.** The qualitative ablation (Figure 6 in the paper, cited as Figure 5 in the review) shows that increasing the background global-semantic weight does not cause semantic bleeding into the foreground region (e.g., an igloo remains intact even as background style intensifies). This demonstrates a genuine capability that prior multi-condition models lack, and the mechanism (masking the cross-attention similarity matrix to restrict token-region correspondence) is well-explained and technically sound.

- **The overall system design is coherent and follows sensible design patterns.** The separation into local fuser (processing depth maps through independent streams before late fusion), global fuser (projecting CLIP embeddings and applying soft guidance), and shared frozen/cloned UNet components represents a clean architectural decomposition that extends prior work (ControlNet, Uni-ControlNet) in a principled direction.

## Weaknesses

### Fatal

None.

### Major

- **The quantitative comparison with baselines is structurally unequal, weakening the headline performance claims.** CnC receives two depth maps and two CLIP image embeddings in settings where baselines receive only one each (Tables 1 and 2). The paper is transparent about this asymmetry (lines 107, 112, 128), but transparency does not eliminate the problem: the claimed gains on FID, IS, CLIPScore, LPIPS, SSIM, and depth MAE cannot be cleanly attributed to the method's architectural innovations — they may partially reflect simply having more/different conditioning information. The paper's own acknowledgment that FID/IS are *worse* for the depth-only setting (because "our model takes in an additional depth map with inpainted regions that may not reflect the prior distribution of the dataset," line 112) further undermines the conclusiveness of the quantitative story. The ablation in Figure 4 does provide a fair test of DDT, but no such ablated controlled comparison backs the headline quantitative tables.

- **No quantitative metric directly evaluates the paper's central claimed capabilities.** The paper claims (a) correct 3D depth ordering and occlusion reasoning and (b) disentangled localization of global semantics from multiple sources. Yet the metrics used — FID, IS, CLIPScore, LPIPS, SSIM, depth MAE — are generic image quality and reconstruction measures. Depth MAE measures overall depth map similarity, not depth ordering correctness (e.g., whether the foreground object properly occludes the background). There is no metric for depth ordering accuracy, occlusion consistency, or region-level semantic disentanglement (e.g., CLIP similarity between the foreground region and the foreground exemplar vs. the background exemplar). The ablation of soft guidance (Figure 6) is purely qualitative. This leaves a gap between the paper's motivation and its evidence: the reader cannot quantitatively verify that the method actually performs the tasks it was designed for.

### Minor

- **The inference-time procedure for obtaining the mask \(M\) used in Soft Guidance is underspecified.** The paper describes in detail how \(M\) is obtained during training (from synthetic image triplets: ground-truth annotations for COCO-Stuff, salient object detection for Pick-a-Pic). However, for novel generation at inference — when a user provides two depth maps and two exemplar images but no mask — it is unclear how \(M\) is derived. Is it computed from the foreground depth map (e.g., thresholding non-zero depth values)? Must the user provide it? This omission affects reproducibility. It is a minor issue because a reasonable reader can infer a likely solution, but it should be explicitly stated.

- **The evaluation is entirely on synthetic/semi-synthetic data and reconstruction from the same pipeline.** The validation uses images from COCO-Stuff (real photos) and Pick-a-Pic (SD-generated), but the "reconstruction" task evaluates against ground truth from the same synthetic triplet pipeline used during training. The paper does not test on unmodified natural images with natural occlusions where no "inpainted background" ground truth exists. Section 4.3 (Discussions) motivates the dataset choice but does not address whether the method generalizes to fully natural scenes without synthetic preprocessing.

### Trivial

None.

## Nice-to-Haves

- Adding a baseline where foreground and background depth maps are composited (e.g., via max-depth projection) into a single depth map would allow a fairer controlled comparison for Table 1.
- Region-level CLIP similarity (foreground region → foreground exemplar, background region → background exemplar) would directly quantify semantic disentanglement.
- Visualizing cross-attention maps before/after Soft Guidance would provide direct evidence for the claimed localization mechanism.
- A single demonstration with more than two depth layers (foreground/midground/background) would strengthen the "3D depth awareness" claim.

## Removed Points

- **Strength: "CnC outperforms existing multi-condition diffusion models on joint local+global conditioning" (from Strength Finder).** This was removed because it conflicts with the verified weakness that the quantitative comparison is structurally unequal. The performance advantage in Table 1 may partially reflect unequal conditioning rather than architectural superiority.

- **Strength: "Reconstruction results show CnC preserves depth perspective better than baselines" (from Strength Finder).** Same reason: the reconstruction task gives CnC separated foreground/background depth maps while baselines receive a single depth map, making the comparison uninformative.

- **Criticism from Section-by-Section Notes: "Uni-ControlNet and Composer 'struggle in processing incompatible conditions' is asserted without support."** This is a related-work claim typical of such papers and does not affect the paper's own experimental validity. It is not a substantive weakness of the paper.

- **Criticism from Section-by-Section Notes: "No human evaluation or user study."** Human studies are not a standard expectation for this type of technical systems paper. This would be nice-to-have but is not a weakness.

- **Criticism from Section-by-Section Notes about late fusion baseline comparison.** The paper already compares against training on the full depth map in Figure 4, which serves as a form of early fusion baseline.

## Novel Insights

A notable pattern in the reviews is the tension between the paper's genuinely novel methodological contributions (DDT, Soft Guidance) and the structurally weak evaluation regime. The DDT ablation (Figure 4) is the one experiment that cleanly isolates the benefit of the core technical idea through a fair within-model comparison, yet this experiment is entirely qualitative. The quantitative comparisons (Tables 1 and 2) are where the paper attempts rigor, but they collapse precisely because giving CnC more conditioning than baselines makes attribution impossible. This suggests that the paper would be better served by abandoning the attempt to claim "substantially outperforms" baselines on metrics and instead leaning into careful ablative and qualitative analysis that directly tests what the method claims to do — depth ordering accuracy and semantic disentanglement — with purpose-built metrics. The methodological novelty is sufficient to make a valuable contribution even without beating SOTA on FID.

## Suggestions

1. **Add a controlled ablation baseline for the joint-conditioning setting.** For the "Depth + Exemplar" row in Table 1, add a version of CnC where the two depth maps are composited into one (e.g., take the element-wise min or max) and the two CLIP embeddings are averaged into one, so that the total conditioning information matches the baselines. This would isolate whether the performance gain comes from DDT/Soft Guidance or simply having more channels of information.

2. **Add quantitative metrics that directly test the claimed capabilities:** (a) depth ordering accuracy — e.g., use a pretrained depth estimator on generated images and check whether the foreground object's depth values are consistently smaller than the background's; (b) region-level semantic disentanglement — compute CLIP similarity of the foreground region to the foreground exemplar vs. the background exemplar.

3. **Explicitly specify how the mask \(M\) is obtained at inference time** for novel (non-reconstruction) generation. If it is derived from the foreground depth map, state the derivation method (e.g., thresholding). If it must be user-provided, state this as a requirement.

4. **Tone down the "substantially outperforms" framing** in the abstract and introduction, given the acknowledged asymmetry in the evaluation protocol. The contribution is strong enough to stand on its methodological novelty and controlled ablations.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
## Summary
This paper studies what DNNs can learn from individual image cues (shape, texture, color) in semantic segmentation — switching from the common "what biases do trained models have" perspective to "what can a model learn from each cue." It proposes a generic procedure to decompose a semantic segmentation dataset into cue-specific datasets (shape via edge detection/EED, texture via class-specific Voronoi diagrams, color via 1×1 convs), trains expert models from scratch on these datasets, and measures their segmentation performance across Cityscapes, CARLA, and PASCAL Context using CNN and transformer backbones. The main findings are that shape+color (without texture) achieves surprisingly strong performance, neither texture nor shape clearly dominates, and these rankings are consistent across architectures.

## Strengths
- **Novel perspective shift for semantic segmentation.** Prior work studies biases of *trained* models via style-transfer cue conflicts, mostly in image classification. This paper is the first to systematically study "what can be learned from each cue" in segmentation, which is a genuine contribution and opens a new analysis dimension. The paper correctly identifies that prior patch-shuffling approaches (used for classification) break semantic integrity and cannot be applied to segmentation.

- **Extensive, well-scoped experiments.** The study covers three diverse datasets (real street scenes, synthetic street scenes, diverse indoor/outdoor), trains from scratch with multiple seeds, evaluates at dataset, class, and pixel granularity, and includes both CNN and transformer backbones. The finding that cue-influence rankings are consistent across architectures (Table 2, "change in rank w.r.t. CNN" column showing "→" for most entries) is a substantive result.

- **Fine-grained color decomposition.** The decomposition of color into gray-value (V) and chromaticity (HS) components, plus the clean 1×1-conv isolation of pure pixel color, goes beyond the shape/texture dichotomy of prior work and provides a more complete picture of cue contributions.

- **Pixel-level location-dependent analysis.** The late-fusion analysis (Table 4, Figure 5) quantifying that shape experts dominate at object boundaries while texture experts contribute more to large interior segments is novel for semantic segmentation and provides fine-grained insight not available from prior image-classification studies.

## Weaknesses

### Fatal
None.

### Major
- **The texture expert's training distribution differs fundamentally from the evaluation distribution, undermining the interpretability of texture-related comparisons.** The texture expert (T_RGB) is trained on Voronoi diagrams — images with no spatial structure, no object boundaries, and random class-cell assignments — then evaluated on natural images with full spatial structure. This introduces a domain shift that goes beyond "cue isolation": the expert learns to recognize texture patches in a spatially disordered context that does not transfer. The paper does not report in-distribution evaluation (e.g., T_RGB tested on Voronoi test images) to separate "can the network learn from texture at all" from "does texture knowledge transfer to natural images." The paper provides this for shape experts (HED with HED pre-processing achieves 55.80% vs. 13.38% on original images, showing a large domain-shift effect), but the analogous control for the texture expert is absent. This gap makes it difficult to determine whether T_RGB's low mIoU on Cityscapes (20.10%) reflects texture being genuinely uninformative or the training distribution being too artificial.

- **The strongest "shape" expert (S_SEED-RGB) includes full color.** The EED-based expert retains color information while smoothing texture, making "shape vs. texture" comparisons actually "shape+color vs. texture+color." The paper is transparent about this in Table 1 and Section 3, but the abstract and conclusions frame the discussion around "shape, texture, and color" as three separate cues, and the headline comparisons (S_SEED-RGB vs. T_RGB) contrast two conditions that both include color, not pure shape vs. pure texture. The pure shape expert (S_HED) is provided but performs very poorly on original images (13.38% mIoU on Cityscapes), so the paper's substantive claims about shape rely on the shape+color confound.

### Minor
- **Ambiguous duplicate entry in Table 3.** The CARLA column of Table 3 lists S_SEED-RGB twice: once at 44.78% mIoU and once at 61.46% mIoU. The table's sorting suggests these are distinct conditions, but both are labeled identically. This may be a formatting artifact or a missing distinction between evaluation protocols, but as presented it is confusing and needs clarification.

- **No in-distribution evaluation for the texture expert.** The paper provides in-distribution results for shape experts (HED with HED pre-processing: 55.80%; EED with EED pre-processing: 48.47%) but does not report the analogous numbers for the texture expert (e.g., T_RGB evaluated on Voronoi test images). This would help disentangle the domain-shift effect from the cue-learning effect.

### Trivial
None.

## Nice-to-Haves
- An alternative texture decomposition that preserves spatial structure (e.g., replacing object interior textures while retaining shapes) would strengthen confidence in the texture-related conclusions.
- Statistical significance testing on the rank ordering of cue experts across seeds.

## Removed Points
The following points from the harsh critic/strength finder are removed with justification:

- **"The method for shape extraction via EED is reasonable."** — This is a (correct) value judgment, not a substantive weakness. Not included.
- **"The paper should note that [EED] retains color."** — The paper already notes this explicitly: "As it preserves color, it extracts the cue combination S+V+HS" (Section 3). Removed as already addressed.
- **"The late-fusion boundary analysis is confounded by training data differences."** — The paper's analysis compares S_SEED-RGB and T_RGB, both trained on pre-processed data. On CARLA, where texture is more realistic/transferable, texture still underperforms shape at boundaries (70.44 vs. 47.94), suggesting the finding is not purely an artifact. Overstated; demoted to the texture-domain-shift concern already covered.
- **"The texture extraction method... not adequately consider how this design choice undermines the validity of all comparisons involving texture."** — The paper does consider domain shift (Section 4.2, lines 220-224: "It should be noted that each expert is trained on its specific cue and then tested on an original input image..."). The criticism is too absolute; kept in weakened form above.
- **"Missing related works"** or criticisms about references not being cited — removed per policy (cannot verify completeness without external sources).
- **"The paper's key conclusion about the relative influence... rests on comparing mIoU"** — This is the paper's actual analysis; criticizing it without offering an alternative is not a weakness per se.
- **"Style-transfer-based comparisons would be useful"** — Outside the paper's stated scope and methodology choice.
- **Strengths removed by filtering:** Generic/superficial strengths like "the paper addresses an important problem" or "the motivation is clear and well-positioned" — dropped as lacking specific evidence anchors per protocol.

## Novel Insights
None beyond the paper's own contributions. The reviews surface the texture-domain-shift concern as the central tension, but this is a methodological critique rather than a novel observation not already implicit in the paper's own framing (which acknowledges domain shift for shape experts but does not extend the same analysis to texture experts).

## Suggestions
1. **Add in-distribution evaluation for all cue experts.** Report the mIoU of T_RGB when tested on Voronoi images (analogous to the HED-with-HED-preprocessing numbers already provided). This would disentangle cue learning ability from domain adaptation.
2. **Reframe the abstract and conclusions.** Acknowledge explicitly that S_SEED-RGB is a shape+color expert, not a pure shape expert, and that the texture comparison involves a training/evaluation domain shift. The current framing slightly overstates what the evidence directly supports.
3. **Fix the duplicate entry in Table 3.** Clarify whether the two S_SEED-RGB entries on CARLA correspond to different evaluation protocols or different expert variants.
4. **Consider an alternative texture decomposition** (e.g., preserving object shapes but replacing texture patches within each object) as a robustness check, even if reported only in an ablation.

## Score and Decision

**Calibration anchors:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| OM1R87YLTc | 2.00 | 1 | Unrelated multi-task perception paper, much weaker |
| V73W8MXnNW | 3.00 | 1 | Visual relationship inference, weaker methodology |
| EQAHilKZ8D | 2.20 | 1 | Visual properties for object representations, weaker |
| CKw0wMQxzv | 2.50 | 1 | Video domain adaptation, unrelated |
| NTWtNjlThd | 5.25 | 1,2 | Shape/texture disentanglement on synthetic data; current paper is stronger (real data, segmentation) |
| kRdcwzEL5J | 5.25 | 1 | Urban 3D segmentation benchmark; different contribution type |
| e9bEoxNiTJ | 5.33 | 1 | Transparent object segmentation via cues; narrower scope |
| EyC5qvRPz7 | 4.75 | 1,2 | Coarse label segmentation; current paper has more novel methodology |
| IRcv4yFX6z | 8.00 | 1 | Hierarchical segmentation, Accept spotlight; much stronger |
| 5Ca9sSzuDp | 8.00 | 1 | CLIP representation decomposition, Accept oral; much stronger |
| 3M0GXoUEzP | 8.00 | 1 | Self-supervised learning, Accept spotlight; much stronger |
| uAFHCZRmXk | 8.00 | 1 | Modality gap analysis, Accept oral; much stronger |
| Yr4RgiZ7P5 | 5.25 | 2 | Shape bias evaluation benchmark; comparable novelty, different domain |
| cH3oufN8Pl | 6.67 | 2 | Inductive bias for classification; not directly comparable |
| 8vGgdc8wOu | 5.50 | 2 | Text vs. texture in CLIP; different topic |
| TMYxJIcdgS | 5.25 | 2 | ImageNet vs LAION analysis; different topic |
| HYyRwm367m | 6.50 | 2 | Neural language of thought, Accept poster; stronger theory |
| Xd2Qxf5RYI | 4.75 | 2 | Zero-shot panoptic segmentation; current paper is stronger |
| Lut5t3qElA | 6.40 | 2 | Content/style disentanglement, Accept poster; stronger theoretical guarantees |
| J9Vwp7TiE5 | 6.00 | 2 | Segmentation data generation; different contribution |
| irorVob9Eq | 5.67 | 2 | Capsule network analysis, Reject; comparable analytical contribution |

**Round-1 bracket:** [4.5, 6.5]
**Round-2 narrowing:** The paper is clearly stronger than the 4.75-5.25 reject anchors and sits below the 6.4-6.5 Accept anchors. The texture domain-shift concern is real and prevents the paper from being a clear accept, but the empirical scope and novel perspective are substantive. Final position: ~5.0.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
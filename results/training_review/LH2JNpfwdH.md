I cannot list the directory contents with the available tools, but the human reviews directory is provided for optional calibration. I have sufficient information from the paper and the two review inputs to produce the final consolidated review.

---

## Summary

This paper proposes the first unified framework for 4D human video stylization — simultaneously performing style transfer, novel view synthesis, and human animation from a monocular video. The method uses two separate NeRFs (human in canonical space via SMPL deformation, and scene background) with a geometry-guided tri-plane representation, then applies stylization in the rendered feature space using AdaAttN. The core contributions are: (1) a unified framework combining three capabilities that prior work addresses separately, (2) a geometry-guided tri-plane that improves upon vanilla tri-plane, and (3) competitive temporal consistency with the unique ability to stylize novel views and animated poses.

## Strengths

- **First unified framework for a genuinely new task.** The paper is the first to combine video stylization, novel view synthesis, and human animation in a single model (Tables 1–2). While each sub-problem has been studied independently, combining them with a coherent architecture that handles both human deformation and scene rendering in a stylized output is a nontrivial contribution. Qualitative results (Figure 4) demonstrate plausible stylized novel views and animated poses.

- **Geometry-guided tri-plane shows measurable improvement over vanilla tri-plane.** Encoding 3D voxel coordinates with positional encoding onto tri-planes, aggregated via U-Nets, produces sharper background textures and object boundaries (Figure 3) and improves temporal consistency (Table 5: 0.182 vs. 0.207). This is a well-motivated architectural improvement supported by both qualitative and quantitative evidence.

- **Competitive temporal coherence with richer stylization.** On original views (Table 1, tab:quan_sota), the method achieves best or second-best temporal consistency on both datasets (0.165 on their dataset, 0.214 on NeuMan) while visual comparisons (Figure 4) show richer texture transfer than LST, AdaAttN, and CCPL. Two user studies (~8000 total votes) consistently favor the proposed method for both temporal consistency and overall quality.

## Weaknesses

### Fatal
None.

### Major

- **Unexplained adaptation of StyleRF undermines a key quantitative comparison.** Table 3 compares temporal consistency against StyleRF (designed for static scenes with multi-view input) on dynamic monocular video. The paper itself notes in Section 2 that StyleRF takes "multi-view images of a static scene" — yet provides no description of how it was adapted to the dynamic monocular setting. Without this information, the comparison is uninterpretable: the reported gap (0.293 vs. 0.165 on their dataset, 0.387 vs. 0.214 on NeuMan) could reflect an unfair or poorly matched adaptation rather than a genuine advantage. Since this is the only direct comparison against a NeRF-based stylization method, its evidentiary value is severely weakened.

- **No direct metric for stylization fidelity on novel views or animated poses.** The only reported quantitative metric is temporal consistency (masked LPIPS warping error). While this measures flicker, it does not assess whether style transfer is successful on unseen viewpoints or poses — which is the paper's central claim. No style accuracy metric (e.g., CLIP-based style similarity, Gram matrix distance, or perceptual style loss) is reported for novel views or animation. The user study asks about "overall quality" but does not isolate style fidelity from other factors. This is a significant gap: the core capability is asserted but not directly measured.

- **Ablations are too narrow to isolate individual contributions.** The paper provides two ablations: (a) unified vs. two-stage (Table 4), and (b) geometry-guided tri-plane vs. vanilla tri-plane (Table 5). Neither isolates the error-correction network $\mathcal{E}$ for deformation (Section 3.2), the two-NeRF (human + scene) design vs. a single dynamic NeRF, the role of the U-Net encoders in the tri-plane beyond coordinate encoding, or the choice of AdaAttN as the stylization module. These components are presented as design contributions, but their individual impact is not quantified. The tri-plane ablation (Table 5) shows a modest gain (0.207 → 0.182) on a single data point, making it hard to assess significance.

- **Two-stage baseline in ablation is weak.** The ablation comparing unified vs. two-stage (Table 4) uses the authors' own reconstruction as the first stage. A stronger comparison would use an established dynamic NeRF method (e.g., HumanNeRF, Animatable NeRF) as the first stage, then apply 2D stylization. As presented, the ablation only shows that the proposed method is better than combining its own reconstruction with 2D stylization — not that it is better than combining existing dynamic NeRFs with 2D stylization. This weakens the evidence for the unified framework's advantage over prior art.

### Minor

- **Runtime speedup claim lacks context.** The claim of "approximately 70% speedup at inference time" (Section 4) does not specify the hardware, the baseline method, or whether the comparison is end-to-end or rendering-only. This makes the claim difficult to verify or reproduce.

- **User study lacks standard methodological details.** While total vote counts (~3000 and ~5000) are reported, the number of participants, their expertise, the number of pairs shown per participant, and confidence intervals/error bars are not provided. This limits the rigor of the perceptual evaluation.

- **Datasets are small.** NeuMan sequences contain 40–104 frames; the additional dataset has 150–200 frames. While the paper acknowledges this, it restricts evaluation of long-term consistency and generalization across diverse motion.

### Trivial
None.

## Nice-to-Haves

- Report style accuracy metrics (CLIP-based style similarity or style loss from a pre-trained VGG) on novel views and animated poses to directly measure stylization fidelity.
- Ablate the error-correction network $\mathcal{E}$ and the U-Net encoders individually to quantify their contributions.
- Compare against a pipeline using an existing dynamic NeRF (HumanNeRF, Animatable NeRF) as the first stage, rather than only the authors' own reconstruction.
- Provide user study methodological details (number of participants, demographics, confidence intervals).
- Specify hardware and baseline for the runtime speedup claim.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"StyleRF comparison is cited in the abstract and conclusion."** — StyleRF is not mentioned in the abstract or conclusion. Removed as factually incorrect.
- **"Tables 2 and 4 have misleading captions."** — The captions clearly state what is being compared (Table 2: "The input of all methods are generated by the proposed method"; Table 4: "By replacing the input of the 2D stylization methods with the rendered images by our method"). Removed as factually incorrect.
- **"No ground truth for novel views makes evaluation impossible."** — Ground-truth stylized novel views are inherently unavailable for zero-shot arbitrary-style tasks. The underlying concern (insufficient stylization metrics) is kept in Major weaknesses. The framing as an impossibility is removed.
- **"Table 1 is more of a claim than a comparison."** — Table 1 is a standard capability comparison matrix, common in papers claiming a new task. Removed as an overly generic criticism.
- **"The geometry-guided tri-plane description is vague."** — The paper specifies voxel size (10 mm³), positional encoding, average pooling, bilinear interpolation, and U-Net encoders. While not exhaustive, the description is at a typical level of detail for a conference paper. Removed as overstated.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the StyleRF comparison.** Either explain exactly how StyleRF was adapted to the dynamic monocular setting (using the same frames, camera parameters, and pose estimates), or remove the comparison if a fair adaptation is not feasible.
2. **Add a direct style fidelity metric.** Report CLIP-based style similarity or a perceptual style loss on novel views and animated poses to directly measure stylization in the claimed generalization settings.
3. **Expand the ablation study.** Ablate the error-correction network $\mathcal{E}$, compare the two-NeRF design against a single dynamic NeRF (e.g., Nerfies-style deformation), and ablate the U-Net encoders in the tri-plane.
4. **Strengthen the two-stage baseline.** Compare against a pipeline using an existing dynamic NeRF method (HumanNeRF, Animatable NeRF) as the first stage.
5. **Provide user study details.** Report the number of participants, demographics, and add confidence intervals or error bars to the user study figures.
6. **Specify the runtime benchmark.** State the hardware and baseline method used to compute the 70% speedup.

## Score and Decision

The paper addresses a novel and well-motivated problem. The architecture is reasonable and the qualitative results show promise. However, the evaluation has significant gaps: the StyleRF comparison is unexplained (rendering one of three quantitative tables uninterpretable), there is no direct metric for stylization fidelity on novel views/animation (the paper's core claim), the ablations are too narrow to isolate contributions, and the two-stage baseline is weak. These issues collectively mean the core claims are not adequately substantiated in the current submission. Major revisions are required before the paper can be accepted.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
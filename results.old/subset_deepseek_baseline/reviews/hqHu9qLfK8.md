## Summary

This paper introduces "inverse protocol prediction" (IPP)—the task of reconstructing experimental protocol conditions (cell line, medium, seeding density, timepoint, formation method, microscope, magnification) from a single bright-field spheroid image. Using the SLiMIA dataset of ~8,000 annotated images, the authors benchmark a range of architectures (CNNs, transformers, hybrids, feature-augmented, and hierarchical models) for this structured multi-label prediction task, achieving ~95% accuracy. They also evaluate segmentation models and temporal prediction models on the same dataset, with cross-dataset validation on RxRx1 and the Cell Tracking Challenge.

## Strengths

- **Novel problem formulation**: Inverse protocol prediction is a genuinely interesting and potentially impactful task for reproducibility, automated experiment validation, and quality control in 3D cell culture research. The paper convincingly motivates why this matters.
- **Comprehensive benchmarking**: The paper evaluates a wide spectrum of architectures (8 segmentation models, 5 IPP models, 4 temporal models) under consistent training conditions, providing a useful empirical comparison for the community.
- **Interpretability analysis**: Grad-CAM visualizations across all eight protocol attributes provide insight into which morphological features drive predictions, and the analysis honestly identifies cases where the model relies on dataset artifacts rather than biology (e.g., replicate and magnification tasks).
- **Cross-dataset validation**: Testing on RxRx1 (2D monolayers) and the Cell Tracking Challenge demonstrates awareness of generalization and provides honest assessment of domain-shift robustness.

## Weaknesses

### Fatal
None.

### Major
- **Abstract overclaims relative to implementation**: The abstract states that the approach "integrates segmentation for morphology extraction, domain-adversarial training, and morphologically informed augmentation." Domain-adversarial training is not described anywhere in the available methods section. The augmentations described (flips, rotations, brightness/contrast, elastic deformations, noise injection) are standard, not "morphologically informed." Only one of five IPP models (Image-Shape Fusion Transformer) actually uses segmentation-derived features. This discrepancy between claimed and implemented methodology is a significant issue.
- **Claimed contributions do not outperform simpler baselines**: The morphometry fusion model (Image-Shape Fusion Transformer, 95.03%) and hierarchical model (HMTT, 94.60%) both underperform the simpler CoAtNet-0 (95.72%). The paper asserts that these models provide "interpretability and consistency" but provides no quantitative evaluation of biological consistency or interpretability gains—only qualitative Grad-CAM analysis that is also applied to CoAtNet. The value added by these bespoke designs is unclear.
- **Temporal prediction results are weak and the contribution is marginal**: SSIM < 0.40 and PSNR ~18 dB on SLiMIA indicate that the temporal models capture very little meaningful structure. The paper acknowledges this but still lists temporal modeling as a main contribution. Given the limited temporal depth of SLiMIA and poor quantitative results, this component adds little to the paper's value.
- **Per-label accuracy breakdown is relegated to the appendix**: The paper states that "attributes with clear morphological cues (cell line, medium, formation method) are predicted reliably, while labels with weaker signals (seeding density, timepoint, replicate) remain challenging" and that "microscope and magnification achieve near-perfect scores, though these largely reflect dataset-specific artifacts." This critical analysis belongs in the main paper, not the appendix, since it directly affects how readers interpret the 95% headline accuracy.

### Minor
- The segmentation evaluation excludes images where Dice=1 and IoU=0, described as "edge scenarios where both predicted and ground truth masks are empty." The explanation is confusing—Dice=1 and IoU=0 cannot occur simultaneously for non-empty masks, and empty masks produce undefined metrics, not 1 and 0. The exclusion is reasonable but the description should be clearer.
- The paper claims "morphologically informed augmentation" but the listed augmentations are standard geometric and photometric transforms. No augmentation strategy that specifically leverages spheroid morphology (e.g., simulating necrotic cores, varying compactness) is described.

### Trivial
- Some citations appear to reference future work (e.g., "Mmiling et al., 2025"), but per review guidelines this is not penalized.

## Nice-to-Haves

- A per-label accuracy table in the main paper (not appendix) would substantially strengthen the paper by showing which protocol components drive the 95% average and which are confounded by dataset artifacts.
- Quantitative evaluation of "biological consistency" for HMTT (e.g., measuring how often predicted label combinations violate known experimental constraints) would substantiate the claim that hierarchical modeling improves plausibility.
- Ablation studies showing the contribution of each component (shape features, hierarchical ordering, domain-adversarial training if implemented) would clarify which design choices matter.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Either implement and describe domain-adversarial training and morphologically informed augmentation in the methods, or remove these claims from the abstract and introduction. The current discrepancy undermines credibility.
- Move the per-label accuracy analysis from the appendix to the main paper, as it is essential for interpreting the 95% headline result and honestly acknowledging dataset artifacts.
- Consider whether the temporal prediction section adds sufficient value given the weak results; if retained, frame it as a preliminary exploration rather than a main contribution.

## Score and Decision

The paper introduces a novel and well-motivated problem, provides comprehensive benchmarking, and includes useful interpretability analysis. However, the abstract makes claims about the methodology (domain-adversarial training, morphologically informed augmentation) that are not supported by the available methods section. The bespoke architectural contributions (morphometry fusion, hierarchical modeling) do not outperform simpler baselines, and the temporal prediction results are too weak to constitute a meaningful contribution. The paper would benefit from honest reframing of what is actually implemented and demonstrated.

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>
- Decision: Reject
- Avg Score: 6.33
- Scores: 5, 8, 6
Here is my consolidated review:

---

## Summary

This paper proposes a method to identify vulnerable pixels in DNNs by generating spatially diverse one-pixel adversarial perturbations using a Sharing Differential Evolution algorithm. The key idea is to find many distinct pixel locations where altering just that single pixel causes misclassification, then aggregate these into a vulnerability map. Experiments are conducted on CIFAR-10 (VGG16, ResNet18, NiN) and ImageNet (AlexNet, ResNet50), with analyses of background vs. foreground vulnerability, cross-model sharing, and the effect of adversarial training.

## Strengths

- **Pixel-level vulnerability attribution from one-pixel perturbations**: Unlike norm-based attacks (PGD, C&W) that spread perturbations across the entire image, the proposed method isolates the effect of each perturbed pixel, enabling a clean attribution of prediction changes to specific input locations (Section 3.1, Figure 1). This design choice directly addresses a genuine limitation of dense adversarial methods for vulnerability analysis.

- **Simultaneous generation of diverse one-pixel perturbations via Sharing DE**: The method efficiently produces multiple spatially diverse successful one-pixel adversarial examples in a single run, in contrast to the standard one-pixel attack which finds only one per run (Figure 2). The sharing mechanism explicitly penalizes nearby solutions, which is a sensible adaptation for the problem.

- **Quantitative analysis of vulnerability location (background vs. foreground)**: Using Grabcut segmentation, the paper documents that over 60% of vulnerable images have one-pixel perturbations in the background, and analyzes per-class trends (planes, ships) linking these to training data background attributes (Section 4.2, Table 4, Figure 5). This is a genuinely novel empirical observation about DNN vulnerability.

- **Cross-model vulnerability sharing analysis**: Table 3 quantifies overlap of vulnerable images and pixel positions across DNN pairs (e.g., only 19.3% of images shared between VGG16 and NiN, with limited pixel overlap), providing empirical evidence about model-specificity of vulnerability (Section 4.2.1, Table 3).

- **Evaluation across multiple architectures and training regimes**: Experiments span three architectures on CIFAR-10, two on ImageNet, and include PGD/TRADES adversarially trained models (Tables 1, 2, 5), giving breadth to the empirical analysis.

## Weaknesses

### Major

- **No baselines or ground truth for validation**: The experiments are entirely self-referential — the paper reports what its method finds but never validates that those findings are meaningful compared to alternatives. There are no comparisons against random pixel perturbation, occlusion-based sensitivity maps, gradient-based vulnerability proxies, or any other vulnerability localization approach. Without baselines, we cannot tell whether the reported patterns (e.g., background vulnerability, cross-model sharing) are genuinely informative or trivial consequences of any pixel-level search. This is the most significant gap in the paper.

- **"Vulnerable region" terminology is imprecisely defined and overclaimed**: The method finds individual vulnerable pixels, not spatially contiguous regions. The paper does not provide an operational definition of what constitutes a "region" (connectedness, density threshold, spatial extent). At line 153, "vulnerable regions" is equated to "positions of one-pixel perturbations," which is a loose definition. The Gaussian filter applied for heatmap visualization is a rendering choice, not a region-detection method. The title and framing imply a stronger spatial claim than the method delivers. While the underlying pixel-level findings are still valuable, the terminology conflates scattered points with contiguous areas and this gap is never addressed.

- **No ablation of the sharing mechanism**: The paper attributes the diversity of solutions to the Sharing DE mechanism, but provides no experiment showing what standard DE (without sharing) would produce under the same budget. Without this ablation, we cannot assess whether the sharing penalty is responsible for the observed diversity or whether a simpler search would suffice.

### Minor

- **Poor ImageNet targeted attack performance limits generality claims**: The targeted attack success rate is under 1% (4 out of thousands for AlexNet, 14 for ResNet50). The paper acknowledges this and attributes it to limited class-crossing and low model vulnerability to one-pixel changes (Section 4.1.2), which is reasonable but means the method's strongest contributions are on CIFAR-10. The generality to high-resolution, multi-class settings is not demonstrated.

- **No statistical variance reported**: Results are reported as averages from three experiments but without standard deviations or confidence intervals (Tables 1–5). The reader cannot assess whether observed differences between models or conditions are meaningful.

- **Grabcut on 32×32 CIFAR-10 images is unverified**: The paper acknowledges that CIFAR-10 images "may lack a clear demarcation between foreground and background" (Section 4.2), but does not validate the segmentation quality. The Background Percentage metrics could be heavily influenced by Grabcut errors at this resolution.

- **Grad-CAM comparison is only qualitative**: Section 4.4 and Figure 9 compare vulnerability maps with Grad-CAM regions using visual inspection only. No quantitative metric is used, and no alternative explainability method is considered, so the claim that vulnerable regions are "distinct from important regions" rests on a single anecdotal comparison.

### Trivial

- **Numerous figure references are garbled**: The text refers to "Fig. 4.7" (instead of separate figures) and repeatedly cites "Fig.7" across different contexts. While this is likely a PDF extraction artifact, it makes navigation difficult.

## Nice-to-Haves

- A synthetic experiment where ground-truth vulnerable regions are known (e.g., inserting a removable critical patch) would substantially strengthen validation.
- Reporting computational cost (queries per image, runtime for each dataset) would help assess practical applicability.
- Measuring whether different vulnerable pixels target different output classes would strengthen the diversity claim beyond spatial distance.

## Removed Points

The following points from the reviewers are removed with justification:

1. **"Method would find the same output if perturbations were randomly scattered"** — This is factually inaccurate. The method uses an evolutionary search to find pixels that actually fool the classifier, not random sampling. The Sharing DE actively searches for successful perturbations; random scattering would not produce the same results.

2. **"Adversarial training findings are predictable from Madry et al./Zhang et al."** — The finding that ℓ∞ adversarial training smooths the loss landscape along *every single dimension* (not just within the ℓ∞ ball) is a non-trivial empirical observation. While consistent with known properties, the paper provides specific quantitative evidence (Table 5) that is not directly derivable from prior work.

3. **"Figures and References formatting issues"** — The "Fig. 4.7" and "Fig.7" artifacts are parser-induced formatting errors from PDF extraction, not author errors. Removed per formatting nitpick rule.

4. **"Missing appendix sections / supplementary proofs"** — Per instructions, sections stripped by the PDF parser are assumed present in the original submission. Removed.

5. **Strength Finder's generic strengths** ("addressed an important problem," "targeted an interesting question") — These were removed per instructions as insufficiently concrete.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no perspective not already present in the paper itself.

## Suggestions

1. **Reframe the contribution precisely**: Change "vulnerable region discovery" to "vulnerable pixel mapping" or "vulnerability landscape sampling" throughout the title, abstract, and body. This would align terminology with what the method actually does and eliminate the central framing problem.

2. **Add baseline comparisons**: At minimum, compare against random pixel perturbation (same budget), gradient-based sensitivity (e.g., saliency maps), and a single-run standard one-pixel attack. Show whether the proposed method finds qualitatively different or more informative pixels.

3. **Ablate the sharing mechanism**: Run the same DE algorithm without the sharing penalty, with the same population size and iterations, and measure diversity (spatial dispersion, number of unique solutions) to isolate the mechanism's contribution.

4. **Report variance**: Include standard deviations or confidence intervals for all main metrics (Tables 1–5) across the three runs to enable readers to assess significance of reported differences.

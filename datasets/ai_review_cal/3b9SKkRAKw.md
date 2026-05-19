- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8
Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

## Summary

LeFusion proposes a lesion-focused diffusion model for controllable pathology synthesis on medical images. The key ideas are: (1) a training objective that only predicts the lesion region (masked loss), preserving background fidelity via inpainting; (2) histogram-based texture control for multi-peak lesions (e.g., lung nodule subtypes); (3) multi-channel decomposition for multi-class lesions (e.g., cardiac MI/PMO); and (4) a separate diffusion model (DiffMask) for controllable mask geometry. Validated on LIDC lung CT and Emidec cardiac MRI, LeFusion-generated data improves downstream nnUNet and SwinUNETR segmentation Dice over training on real data alone or on data from prior synthesis methods.

## Strengths

- **Lesion-focused training objective.** The core innovation (Eq. 4, Sec. 3.1) applies the diffusion loss only within the lesion mask, so the model never allocates capacity to background generation. This is a clean, principled departure from standard inpainting (RePaint) and conditional diffusion (Cond-Diffusion), which the paper shows empirically degrade downstream segmentation (Tables 1, 2; Fig. 5). The idea is simple, well-motivated, and demonstrably effective.

- **Histogram-based texture control without extra annotations.** Section 3.2 and Figure 6 show that conditioning on the lesion's grayscale histogram (Eq. 5) enables controlled generation of distinct nodule types (ground-glass, part-solid, solid) without requiring lesion-type labels. The qualitative contrast between LeFusion (which produces overly subtle lesions biased toward healthy appearance) and LeFusion-H (which recovers realistic attenuation) directly validates the design.

- **Multi-channel decomposition for multi-class lesions.** Section 3.2 and Eq. 6 extend the model to generate multiple lesion classes (MI and PMO) in separate channels, capturing inter-lesion correlations. In Table 2, the joint model (LeFusion-J) outperforms the single-channel variant on PMO Dice (e.g., 63.62 vs. 56.99), showing that this design choice improves realism and downstream utility.

- **DiffMask for controllable mask generation.** Section 3.3 introduces a separate diffusion model that generates lesion masks conditioned on a bounding sphere, enabling user control over size, location, and boundary. Table 2 (third group) shows that DiffMask combined with texture synthesis yields the highest Dice scores (e.g., 58.81/70.96 with SwinUNETR) with consistent improvement as synthetic data volume increases.

- **Evaluation across two organs and two architectures.** Tables 1 and 2 show consistent gains on lung nodule CT (nnUNet, SwinUNETR) and cardiac MRI (same architectures). The lung nodule results show LeFusion-H with hand-crafted masks improves nnUNet Dice by 5.18% and NSD by 4.4% over training on real pathological data alone, providing cross-domain validation.

## Weaknesses

### Fatal
None.

### Major

- **No error bars, variance, or statistical significance in the main downstream results.** All segmentation metrics in Tables 1 and 2 are reported as single-point Dice/NSD values. Given that improvements over baselines are often in the 1–5 percentage point range, it is impossible to assess whether these differences are reliable or within training/data-split noise. This is the most significant evidential gap: the central claim of downstream improvement is plausible but insufficiently supported. The authors should report mean ± std across multiple runs (different random seeds) or use cross-validation.

- **The core design choice — lesion-focused vs. global loss — lacks a clean controlled ablation.** The paper's central claim is that focusing the diffusion loss on the lesion region simplifies learning and preserves backgrounds. The comparison with RePaint (which uses a global loss with similar inpainting inference) provides partial evidence, but RePaint uses a different underlying model and training setup. To rigorously validate this claim, the authors should compare a version of LeFusion trained with a global loss (predicting the full image) against the lesion-focused version, holding all other components (architecture, data, inpainting scheme) constant. Without this, the reader cannot attribute gains definitively to the lesion-focused loss versus other implementation choices.

### Minor

- **The histogram encoding details are underspecified.** Section 3.2 states the histogram is used "as a condition via cross attention Rombach et al. (2022)" but does not specify: how many bins, how the histogram is encoded (as a flat vector? a learned embedding?), or how cross-attention is integrated into the U-Net architecture. This hinders reproducibility.

- **Background preservation claim lacks quantitative validation.** The paper argues that Cond-Diffusion "disrupts background structure" (Fig. 5, Tables 1–2) but relies entirely on visual inspection of a few slices. Reporting a quantitative background fidelity metric (e.g., MS-SSIM or LPIPS computed exclusively on the region outside the mask) would substantiate the claim. The visual differences in the provided slices are often subtle.

- **The diversity analysis for histogram control is a proxy that conflates diversity with quality.** Section 4.3 uses lower PSNR/SSIM between pairs as evidence of higher diversity, but lower similarity could also indicate higher variance without realism. A direct check — generating lesions with a target histogram and measuring whether the output histogram actually matches the target — would be more informative.

- **DiffMask description leaves several implementation questions unanswered.** The paper states the control sphere is "concatenated as a condition to the DiffMask input" without specifying the conditioning mechanism. The boundary mask's role "at each diffusion step" is described at a high level but not precisely (e.g., is it an element-wise multiplication after each reverse step?). Given that DiffMask is presented as a key contribution (Sec. 3.3), these details matter.

### Trivial
None.

## Nice-to-Haves

- A quantitative evaluation of whether the histogram control actually produces lesions whose intensity distributions match the target histogram (from a specified nodule cluster).
- For the DiffMask, a demonstration that varying the control sphere parameters produces predictable, monotonic changes in lesion size.
- Reporting lesion-level detection metrics (e.g., recall, false positives per case) in addition to Dice, especially on the cardiac dataset where PMO Dice remains low (<40% across all methods) even with synthetic augmentation.

## Removed Points

These points were raised by one or more reviewers but are removed per the filtering criteria:

- "Overstated practical significance of histogram-based texture control" — The paper's claim about histogram control being "crucial" (Sec. 3.2) is primarily about avoiding mode collapse (producing overly subtle lesions biased toward healthy appearance). The qualitative evidence (Figs. 5, 6) supports this; the quantitative improvements are consistent even if modest. This criticism misreads the nature of the claim.
- "Missing ablation of background preservation" — Overlaps with the lesion-focused loss ablation point above. The paper does compare with Cond-Diffusion (which generates full images) and RePaint (inpainting with global loss), providing reasonable evidence even if not a perfectly controlled experiment.
- "Missing comparison to standard augmentation baselines" — The paper already compares with Copy-Paste and Hand-Crafted methods, which span exactly this category. Scope creep.
- "Hand-Crafted baseline is inherently limited" — Describes the baseline, not a weakness of the paper.
- References to missing appendix content (mask quality, Tab. A1) — The appendix exists in the original submission; the parser strips these sections.
- Various formatting and notation nitpicks — parser artifacts or trivial presentational issues.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add error bars.** Re-run the segmentation experiments with at least 3 random seeds and report mean ± std for Tables 1 and 2. This is the single most impactful improvement.
2. **Run the core ablation.** Train a version of LeFusion with a global (unmasked) diffusion loss, keeping the architecture and inpainting scheme identical, and compare to the lesion-focused version. This directly validates the central claim.
3. **Specify histogram encoding details** (number of bins, embedding architecture, cross-attention integration) in the main text or appendix.
4. **Add a quantitative background fidelity metric** (e.g., MS-SSIM on normal regions outside the mask) to substantiate the background preservation claim beyond visual inspection.
5. **For the diversity analysis, supplement PSNR/SSIM** with a direct check: generate lesions using a target histogram from the ground-glass cluster and measure whether the output histogram distribution matches that cluster.

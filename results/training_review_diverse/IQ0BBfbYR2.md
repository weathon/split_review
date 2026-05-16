Here is my consolidated final review.

---

## Summary

This paper introduces CoLa-DCE, a method for generating concept-guided counterfactual explanations for image classifiers using latent diffusion models. The key idea is to (1) select a counterfactual target based on the classifier's internal representation (via LRP), (2) identify the top-*k* concepts (channels in a chosen layer) most relevant to flipping the prediction, and (3) mask the gradient during diffusion to modify only those concepts, optionally with spatial constraints. The output includes the counterfactual image, concept reference visualizations, and per-concept localization maps. The method is evaluated on ImageNet across VGG16, ResNet18, and ViT architectures.

## Strengths

- **Novel concept‑level control for diffusion counterfactuals**: The paper is the first to constrain diffusion guidance to a small set of semantic concepts (channels in a classifier layer) rather than modifying all features. This is a genuine technical contribution over prior work (LDCE, DVCE, DiME), which lack this level of semantic control. The concept selection via top-*k* spatial-summed gradients is simple and well-motivated by the CRP framework.

- **Improved target selection via classifier perception yields measurable gains**: Using LRP-based intermediate attribution to find a near-miss counterfactual target (Table 1, LDCE Attr rows) consistently improves both flip ratio (e.g., VGG16bn: 0.851→0.956) and confidence over the base LDCE target selection, while also improving FID. This contribution is well-supported and independent of the concept-guidance component.

- **Validity test confirms causal link between selected concepts and generated changes**: The violin plots in Figure 5 quantitatively show that the attribution difference between counterfactual and original images is substantially higher for CoLa-DCE's selected concepts than for randomly chosen ones, across two architectures. This provides internal consistency evidence that the concept selection is meaningful.

- **Comprehensive evaluation across multiple architectures**: Experiments cover VGG16 (with and without batch norm), ResNet18, and ViT on ImageNet, demonstrating generalisability. The trade-off analysis of the number of concepts (Figure 2) is informative and shows that useful counterfactuals (>75% flip ratio) can be achieved with as few as 10 concepts.

## Weaknesses

### Fatal
None.

### Major

- **The paper's central claim of improved transparency/comprehensibility is not directly evaluated.** The method is motivated by—and its primary claimed advantage over LDCE is—better transparency: making "where changed what" clear to a user through concept visualizations and localization maps. Yet the entire quantitative evaluation (Table 1, Figures 2–5) measures only *minimality* (FID, L1/L2) and *accuracy* (flip ratio, confidence). These are necessary but not sufficient to validate a transparency claim. There is no user study, no task-based evaluation of comprehension (e.g., can humans identify which concepts changed?), no comparison of concept maps against alternative visualization approaches, and no quantitative transparency metric. The validity test (Section 4.5) is a self-consistency check (selected concepts correlate with attribution differences), not a measure of human interpretability. The qualitative examples (Figures 4, 6) are suggestive but do not, on their own, substantiate the claim that the explanations are *more comprehensible* to humans. This gap is significant because improved transparency is the paper's key differentiator from prior work. *Mitigation would require either a human evaluation or at least an objective proxy for transparency (e.g., sparsity/alignment of concept attribution changes compared to baselines).*

### Minor

- **No variance estimates reported.** All results in Table 1 and Figures 2–5 are single values with no standard deviations, confidence intervals, or indication of multiple random seeds. Given the stochasticity of diffusion sampling and gradient masking, this makes it impossible to assess the statistical significance of the reported differences. *The paper would be substantially strengthened by rerunning with 3–5 seeds and reporting distributions.*

- **Spatial conditioning is not compared quantitatively against non-spatial CoLa-DCE.** The paper claims that spatial constraints "further decrease\[s\] the FID" (line 308) and references Figure 4 (qualitative), but no quantitative table compares CoLa-DCE with vs. without spatial conditioning across all models. This makes it hard to judge the incremental benefit of the spatial component. *A simple table with FID and flip ratio for both variants would resolve this.*

- **No perceptual similarity metric reported.** The paper uses L1/L2 pixel distances (which are nearly constant across methods, ranging only 12443–14028) and FID (a distributional metric, not per-sample). LPIPS or SSIM would better capture perceptual similarity of the counterfactual to the original and directly relate to the paper's claim of "semantic minimality."

- **Key hyperparameters lack systematic analysis.** The spatial threshold η is mentioned (line 194) but never defined, ablated, or justified (is it per-sample? per-concept? global? what value?). The choice of which layer to use for concept extraction (feat.37, 4.1.c1, encoder) is stated but not justified or ablated. The paper would benefit from sensitivity analysis for both η and layer choice.

- **Limitations section omits practical concerns.** The current limitations paragraph (Section 6) is brief and misses: (a) the computational cost of nearest-neighbor search over ~45k reference images for target selection per sample, (b) sensitivity to the choice of intermediate layer, and (c) dependence on a reference dataset.

### Trivial

- **Equation (1) notation is ambiguous.** The scoping of `argmin` and the condition `f(x') ≠ f(ˆx)` are not cleanly separated.
- **Notation inconsistency in gradient.** Classifier guidance (Section 2) is described using ∇log probabilities (log p(c|x)), while concept conditioning (Section 3.3) writes ∇p(x|y) without the log, without clarifying whether this is a deliberate choice or an oversight.
- **The paper states flip ratios are "on par" with the LDCE baseline** (line 253), but Table 1 shows a ~0.13 drop for VGG16bn (0.956→0.821) and ~0.11 drop for ResNet18 (0.957→0.846). While the trade-off is acknowledged elsewhere, calling this "on par" slightly overstates the comparison.

## Nice-to-Haves

- A small-scale user study (20–30 participants, 10–15 samples) measuring whether humans can correctly identify which concepts changed in CoLa-DCE vs. LDCE would directly validate the transparency claim. Even without a full study, an objective proxy such as the number of concepts with significant attribution change between original and counterfactual could partially serve this purpose.
- Reporting LPIPS in addition to or instead of L1/L2 would better capture semantic minimality.
- An ablation table comparing CoLa-DCE with and without spatial conditioning across all models.

## Removed Points

The following criticisms raised by reviewers are removed or substantially weakened after cross-checking against the paper:

- *"Insufficient comparison to concept-based baselines (e.g., TCAV, concept bottleneck models)"* — TCAV and concept bottleneck models are not counterfactual generation methods; there is no established concept-based counterfactual baseline for images. The paper correctly compares to the closest related method (LDCE), which is the state of the art for diffusion-based counterfactuals. This criticism evaluates the paper against a standard that does not exist.
- *"The claim about concept-based counterfactuals is a hypothesis, not a known property"* — This criticizes a motivation statement (Section 3, line 114-115), which is a standard way to motivate a contribution, not a weakness.
- *"Formatting/style nitpicks"* — Issues such as missing parentheses in Equation (1) are at most trivial notation choices, not substantive weaknesses.
- *"The paper does not mention how the reference set is split"* — The paper states (line 205): "90% of the validation data is used as a reference dataset, while counterfactuals for the evaluation are generated on the remaining 1000 samples." The split is clearly stated.

## Novel Insights

None beyond the paper's own contributions. The reviews largely echo what the paper already states, and no reviewer identified a pattern or interpretation that the authors missed.

## Suggestions

1. **Directly evaluate transparency.** Add either a human evaluation or an objective proxy (e.g., measure concept-level attribution sparsity between original and counterfactual, and compare CoLa-DCE against LDCE on this metric). This is the single most impactful addition.
2. **Add variance estimates.** Report means and standard deviations over multiple seeds (3–5) for all quantitative metrics.
3. **Quantify spatial conditioning.** Add a table comparing CoLa-DCE with vs. without spatial constraints across all models and metrics.
4. **Report LPIPS** as a per-sample perceptual similarity metric alongside or replacing L1/L2.
5. **Ablate η and layer choice.** Provide sensitivity analysis for the spatial threshold and the concept extraction layer.
6. **Expand the limitations section** to cover computational cost, layer sensitivity, and reference dataset dependence.
7. **Tone down the "on par" language** for flip ratio comparisons where the gap exceeds 0.1.

## Score and Decision

The paper presents a novel and technically sound method for concept-guided diffusion counterfactuals, with well-executed standard-metric evaluations and a thoughtful validity check. The concept selection mechanism and improved target selection are genuine contributions. However, the paper's central claim—that the method improves transparency and comprehensibility for humans—is asserted but never measured. The quantitative evaluation is limited to minimality and accuracy, which are necessary but not sufficient to validate this claim. Additionally, the results lack statistical rigor (no variance estimates) and important ablations (spatial conditioning, hyperparameter sensitivity) are missing. These gaps are evidential rather than structural: they can be addressed with additional experiments. In its current form, the evidence does not match the claimed contribution.

**Score: 5.0 / 10**

**Decision: Reject** (major revisions needed to validate the core transparency claim)

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
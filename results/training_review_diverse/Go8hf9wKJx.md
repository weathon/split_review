Now I have a thorough understanding of the paper and can verify claims. Let me compile my final consolidated review.

---

## Summary

This paper proposes DOG (Diffusion-based Outlier Generation), a framework that uses a pre-trained text-to-image diffusion model (Stable Diffusion) to synthesize near-OOD surrogate data for fine-tuning OOD detectors. The method combines textual inversion (to extract visual semantics from ID images into pseudo-words) with explicit textual category information: it finds candidate concepts from WordNet that are similar to the pseudo-words, filters them via CLIP-based proximity to ID images, generates images conditioned on the filtered anchors, and fine-tunes a detector using the WOR training objective. The core insight — transforming outlier generation into text space via diffusion models and leveraging both visual and textual modalities — is novel and well-motivated.

## Strengths

- **Novel dual-modality outlier generation**: DOG is the first method to combine visual semantic information (via textual inversion of ID images) with explicit textual category information to generate near-OOD data using a diffusion model (Section 3.1.1–3.1.2, Figure 2). This directly addresses limitations of prior single-modality generation methods (VOS, NPOS) that sample in feature space under parametric assumptions or use only text synonyms without visual grounding.

- **Eliminates need for external outlier datasets**: DOG synthesizes surrogate outliers solely from ID data (images and labels), providing a new outlier exposure pipeline that avoids manual collection and the difficult problem of selecting appropriate surrogate OOD data. This is a genuine advantage over conventional OE and methods like POEM that require external OOD datasets (Section 1, Section 3.2).

- **Ablation study validates dual-modality design**: DOG outperforms five alternative diffusion-based synthesis strategies (noise perturbation in visual/text space, interpolation, synonym-only generation) on both CIFAR benchmarks (Table 2). The synonym-only strategy (e) is second-best but worse than DOG, demonstrating that incorporating image semantics via textual inversion is crucial for generating effective near-OOD data.

- **Robust hyperparameter guidance**: Analysis of the number of synthetic outliers *M* (Figure 3(a)–(b)) shows consistent performance when *M* is near or above the per-class ID sample count, offering practical guidance for deployment.

- **Consistent evaluation framework**: The comparison DOE (real surrogate data + WOR) vs. DOG (generated surrogate data + WOR) properly controls for the training objective, isolating the contribution of the generation method itself.

## Weaknesses

### Major

1. **ASH scoring applied uniformly without justification, conflating generation and evaluation**. The paper states: "we adopt the ASH scoring (Djurisic et al., 2023) in OOD detection." ASH appears both as a post-hoc baseline method and (apparently) as the scoring function used to evaluate all fine-tuning methods. If fine-tuning methods (OE, Energy-OE, ATOM, DOE, etc.) are evaluated using ASH rather than their native scoring (softmax for OE, energy for Energy-OE, etc.), this fundamentally changes what is being measured: it tests how well each fine-tuned model's features work with ASH, not how well each method performs under its own protocol. Different scoring functions can interact differently with models fine-tuned under different objectives. The paper does not justify why ASH is the appropriate single metric or report results with each method's native scoring alongside ASH. This conflates the outlier generation contribution with the scoring function choice and departs from standard practice in the OOD detection literature. The authors should report results with native scoring for each method, with ASH as a supplementary/secondary metric.

2. **Unsupported "dynamic adjustment" claim**. The abstract states DOG "allowing dynamic adjustment of surrogate outlier data based on the results" and the conclusion repeats that "DOG enables dynamically adjusting the surrogate outlier data based on the OOD detection results." However, the method description (Section 3) and Algorithm 1 describe a single fixed generation step followed by fine-tuning — there is no iterative loop, no adaptation mechanism based on detection results, and no experiment demonstrating dynamic adjustment. This claim is misleading and should either be removed or substantiated with an experimental demonstration.

### Minor

1. **OE surrogate data source is not specified**. The paper says "We adopt their suggested setups" for baselines but does not explicitly state which surrogate dataset was used for the OE baseline (e.g., 80M Tiny Images, ImageNet-1k, or another source). While this information may be deducible from context, explicitly stating it would improve reproducibility and allow readers to assess the fairness of the comparison. (The reviewer's additional claim that the reported OE performance is "suspiciously poor" relative to the original OE paper is unverifiable here — different backbones [WRN-40-2 vs. whatever was used in the original OE paper] and different evaluation protocols yield different numbers, so this specific allegation is removed as unsubstantiated.)

2. **No standard deviations or confidence intervals reported**. Given the stochasticity in diffusion-based image generation, pseudo-word optimization, and fine-tuning, multiple runs with error bars would strengthen the reliability of the results. Many numbers in the table (e.g., FPR95 values) could vary across runs. That said, this is common practice in the OOD detection literature and does not invalidate the results on its own.

3. **WordNet candidate selection is under-described**. The paper does not specify what subset of WordNet was used (all nouns? synsets? specific depth?), how many candidates were in *W*, or what kind of words actually appear in the final anchors. No ablation compares against alternative concept sources (e.g., ImageNet classes, a large text corpus). While the overall ablation in Table 2 shows DOG > alternatives, ablating the candidate source specifically would strengthen the paper.

4. **The WOR training objective vs. generated data contribution is not fully disentangled**. The comparison DOE (real data + WOR) vs. DOG (generated data + WOR) properly controls for the training objective. However, the paper's reported gains over VOS, NPOS, and standard OE — which do not use WOR — could be partially driven by the WOR loss rather than the generated data quality. An additional row showing "DOG + standard OE loss" in Table 1 would cleanly separate these factors.

### Trivial

- Algorithm 1 notation "for t in T:1 do" is ambiguous about loop direction (though the intended meaning is clear from context).
- The paper uses "e.g., WordNet" suggesting it is one option, but all experiments use only WordNet — this should simply say WordNet was used.

## Nice-to-Haves

- Report results with each method's native scoring function alongside the ASH-based results.
- Ablate the candidate selection pipeline: compare against using class names directly, using a fixed set of words (e.g., ImageNet classes), or skipping CLIP-based filtering.
- Provide qualitative analysis of generated outliers with distributional distance measures (e.g., FID between generated and ID data, CLIP score).
- Report the computational cost: number of anchors, total images generated, wall-clock time.
- Report textual inversion hyperparameters (number of optimization steps, learning rate, initialization).
- Conduct a human evaluation or user study on whether generated images look like valid near-OOD samples.

## Removed Points

- **"ImageNet results missing from the paper"**: The paper has a footnote marker (¹) after the ImageNet claim, and the parser strips footnotes/appendices. These results likely exist in the original submission and cannot be flagged.
- **"OE performance is suspiciously poor"**: The reviewer's comparison is against numbers from a different backbone and evaluation setup (Hendrycks et al. 2018 reports on ResNet, while this paper uses WRN-40-2). No basis to claim the numbers are anomalous.
- **"Training procedure not isolated" overclaim**: The reviewer acknowledges DOE vs DOG isolates the generation method under the same training procedure. The WOR ablation request is valid but the claim that it's a "fundamental" or "critical" flaw is overblown — it has been downgraded to minor.
- **Various formatting/parser nitpicks** (Algorithm 1 formatting, broken characters): These are parser artifacts, not author errors.
- **"Stable Diffusion may just reconstruct real objects"**: Speculative claim about what the model "may" be doing, not a verifiable weakness.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Address the ASH scoring concern** by reporting all fine-tuning methods with their native scoring functions (softmax for OE, energy for Energy-OE, etc.) in the main results table. ASH can be used as a secondary metric or supplementary analysis to show robustness.
2. **Remove or substantiate the "dynamic adjustment" claim.** Either add an experiment where generation is iteratively refined, or delete the claim from the abstract and conclusion.
3. **Add error bars** (standard deviations across multiple runs with different random seeds) for all main experiments.
4. **Explicitly state** which surrogate dataset was used for the OE and DOE baselines.
5. **Add an ablation row** showing DOG with standard OE loss (without WOR perturbation) in Table 1 to separate the effect of the generated data from the training objective.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
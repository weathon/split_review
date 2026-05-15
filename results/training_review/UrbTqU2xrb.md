Now I have all the information I need. Let me compose the final consolidated review.

---

## Summary

This paper presents the first feed-forward pipeline for clothing-disentangled 3D character generation from a single image. The method operates in two stages: (1) a multi-part diffusion model with cross-part attention disentangles the input image into separate body and clothing part images in 2D; (2) a multi-view diffusion model, augmented with a combination attention mechanism, generates multi-view consistent images for each part and composes them. Off-the-shelf feed-forward reconstruction (LGM) then produces 3D Gaussians of each part, with an optional optimization to align relative positions. The authors contribute a dataset of >10,000 clothing-disentangled anime characters with 11 clothing combinations each.

## Strengths

- **First feed-forward pipeline for clothing-disentangled 3D character generation.** The paper is clearly positioned against optimization-based methods (SDS-based) that take hours per character. The two-stage design (2D disentanglement → multi-view generation → off-the-shelf reconstruction) is a clean separation of subtasks that enables inference in seconds. The related work section adequately scopes prior work and motivates the need for a feed-forward alternative.

- **Multi-part attention demonstrably improves 2D disentanglement quality.** Table 2 and Figure 4 provide both quantitative (PSNR/SSIM/LPIPS) and qualitative evidence that cross-part information exchange via the proposed multi-part attention module significantly outperforms independent per-part generation. This ablation directly supports the core architectural claim.

- **Large-scale disentangled character dataset.** The dataset of >10,000 anime characters with 11 clothing combinations each (~110,000 unique models) is substantially larger than prior disentangled character datasets (<1,000 subjects) and represents a valuable resource for the anime/game domain.

- **Demonstrated applications (cloth transfer and animation).** Figures 6 and 7 show natural extensions enabled by the disentangled representation, including virtual try-on (re-combining parts from different characters) and adaptation to parametric animation. These applications validate the utility of the method beyond static generation.

## Weaknesses

### Fatal
None.

### Major

- **No 3D evaluation metrics for a paper about 3D generation.** The paper's title, abstract, and central claims are about *3D* character generation, yet all quantitative evaluation (Table 1, Table 2) is limited to 2D image metrics (PSNR/SSIM/LPIPS) on multi-view *images* of parts. No 3D reconstruction metrics (Chamfer distance, volumetric IoU, F-score) are reported for the final 3D models produced by the pipeline. Since the 3D part uses an off-the-shelf reconstruction method (LGM), end-to-end 3D quality must be verified — the 2D metrics alone do not guarantee that the reconstructed 3D parts are spatially coherent, non-intersecting, or faithful to the input. This is the single most significant gap in the evaluation.

- **No runtime measurements.** The paper repeatedly claims "seconds vs hours" (Abstract, Introduction, Method), but provides zero timing data. No per-stage runtime breakdown, no total inference time, and no wall-clock comparison with any optimization-based alternative. Without this, the central efficiency argument is unsupported.

- **No quantitative disentanglement metric.** The paper's core goal is clothing *disentanglement*, yet no metric measures how well the method actually separates parts (e.g., segmentation mIoU, part mask consistency across views, part completeness scores). The qualitative examples in Figure 4 are suggestive but insufficient to substantiate claims of "high-quality disentanglement."

- **The "special condition image" for part combination is never defined.** This is a key component of the combination attention mechanism, yet the paper never specifies what this image actually is (a blank template? a composition mask? a learned embedding?). The ablation in Table 2 compares "w/ special condition image" vs "w/o special condition image," but the reader cannot interpret what is being ablated. This is a genuine reproducibility gap.

### Minor

- **Only one baseline compared; comparisons are limited.** The method is compared against a single baseline (modified Wonder3D). While adapting holistic methods to the multi-part setting is non-trivial, the paper would be strengthened by comparisons with the optimization-based methods cited in the related work (e.g., SDS-based approaches for the same task), even if only for a small set of qualitative examples and a runtime comparison. The quantitative gains over the modified Wonder3D are small (e.g., PSNR 22.79 vs 22.61 for combined images; PSNR 23.68 vs 22.66 for the body part) and reported without error bars, making it difficult to assess significance.

- **No error bars or variance reported.** All quantitative results in Tables 1 and 2 are reported as single numbers without standard deviations or confidence intervals. Given the modest performance margins, statistical significance is unclear.

- **Missing ablation of the two-stage design.** The paper never evaluates an end-to-end variant that directly generates multi-view disentangled images without the explicit 2D disentanglement stage, so the contribution of the two-stage decomposition itself is not quantified.

- **A few undefined or ambiguous terms in the method section.** Equation 3 uses an unspecified function *f_cat* (not defined anywhere in the paper). The paper states that the combination attention module is placed "after the multi-view attention layer" in the UNet, but does not specify which block level or whether this placement is consistent across all resolutions.

- **Anime-only evaluation.** The paper scopes to anime characters (valid and clearly stated), but the title and framing ("character generation") invite generalization expectations. Adding a discussion of what would be needed to transfer to realistic humans — even speculative — would help readers gauge the method's broader applicability.

### Trivial
None of note beyond what is addressed above.

## Nice-to-Haves

- A user study comparing the practical editability of the generated 3D models against optimization-based alternatives would strengthen the "practicality" claims but is not standard for this type of technical paper.
- Visualizing the "special condition image" (even as a small schematic) would resolve the specification gap on its own.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"Missing related works (DreamGaussian4D, Compressible-3D, MultiDiffuser)"* — Hard rule: do not cite missing related works without external confirmation.
- *"No comparison with GALA, Zhang et al., Dong et al., LRM, TriplaneGaussian"* — These methods solve different problems with different inputs (text-to-3D, holistic reconstruction, or 3D-mesh-input), so this criticism conflates tasks. The paper could compare with optimization-based methods that handle the *same* task (single-image to disentangled 3D), but the specific methods named by the reviewer are not appropriate direct comparators.
- *"'Single GS' is not defined in the text"* — The figure caption (Figure 5) explicitly defines it: "'Single GS' represents the single Gaussian representation of the entire character." Factually incorrect criticism.
- *"Figure 2 is too small and lacks detail"* — Formatting/visual artifact from PDF parsing; irrelevant to technical evaluation.
- *"The term 'feed-forward' may be misleading"* — The paper clarifies this in context; the pipeline is feed-forward apart from the optional 3D alignment optimization, which is clearly marked as optional. This is adequately scoped.
- *"No user study"* — Not standard for this type of algorithmic contribution.
- *"No discussion of transfer to realistic humans"* — The paper explicitly scopes to anime characters. Scope creep.

## Novel Insights

None beyond the paper's own contributions. The reviewers did not produce observations that meaningfully extend or reinterpret the paper's findings.

## Suggestions

1. **Add 3D evaluation metrics.** Report Chamfer distance, volumetric IoU, or F-score between reconstructed 3D parts and ground-truth 3D models (the dataset contains ground truth). This is the most critical gap to address.
2. **Provide a runtime table.** Report total inference time (with per-stage breakdown) and compare against at least one optimization-based method on the same hardware.
3. **Define the "special condition image."** Specify its form, how it is constructed, and ideally visualize it. This is necessary for reproducibility.
4. **Quantify disentanglement.** Report a segmentation metric (e.g., mIoU of part masks against ground-truth renders) to substantiate the disentanglement claim.
5. **Add error bars.** Report standard deviations over multiple runs or random seeds for all quantitative results.
6. **Ablate the two-stage design.** Compare against a variant that skips the explicit 2D disentanglement stage to quantify its contribution.
7. **Expand baseline comparisons.** Include at least one optimization-based method on a small set of qualitative examples with runtime timing to ground the "seconds vs hours" claim.

## Score and Decision

The paper addresses a timely and well-motivated problem (clothing-disentangled 3D generation) and proposes a novel feed-forward architecture with a clean two-stage design. The dataset contribution is substantial. However, the experimental validation has critical gaps: no 3D metrics are reported despite "3D" being central to the paper's claims, the key "special condition image" is never defined, no runtime data supports the efficiency narrative, and disentanglement quality is not quantitatively measured. These weaknesses collectively mean the paper's core contributions are not sufficiently demonstrated in its current form. Major revisions to the evaluation are required.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
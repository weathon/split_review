Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper introduces Paint by Inpaint, a framework that inverts the object-removal process to create PIPE, a large-scale dataset (~1M image pairs) for instruction-guided object addition. Using segmentation datasets (COCO, OpenImages) and a Stable Diffusion inpainting model, the pipeline removes objects to create source images, then pairs them with the original (target) images — guaranteeing consistency since only the masked region differs. Diverse natural-language instructions are generated via class templates, a VLM+LLM pipeline, and reference datasets. A diffusion model trained on PIPE achieves state-of-the-art results on object-addition benchmarks (PIPE test set, MagicBrush object-addition subset, OPA) and is preferred by human evaluators ~72.5% over InstructPix2Pix. Combining PIPE with general editing data also improves overall editing performance on the full MagicBrush test set.

## Strengths

- **Novel inversion insight for dataset creation.** The core idea — that adding objects is the inverse of removing them, and removal is easier because segmentation masks and inpainting models are readily available — is clearly articulated (Section 1, Section 3) and directly operationalized. This is a clever and practical way to circumvent the fundamental difficulty of producing paired natural-image editing data.

- **Real target images with guaranteed consistency.** Unlike InstructPix2Pix (synthetic source and target) and MagicBrush (synthetic with manual curation), PIPE uses real natural images as targets, and consistency between source and target is enforced by construction (only the masked region differs, with α-blending for smooth transitions). Table 1 and Section 3.1 document this advantage clearly.

- **Strong and consistent quantitative results.** The model outperforms baselines (IP2P, Hive, VQGAN-CLIP, SDEdit) across three benchmarks — PIPE test set (Tables 2), MagicBrush object-addition subset (Table 3), and OPA (Table 4) — with particularly large margins on consistency metrics (CLIP-I: 0.962 vs. 0.899; DINO: 0.875 vs. 0.715 on the PIPE test set). Human evaluation confirms a 72–73.6% preference rate over IP2P (Table 6).

- **Scalable and diverse instruction generation.** Three complementary strategies (class templates, VLM+LLM, reference datasets) produce 1.88M diverse instructions from 889K image pairs (Section 3.2). The use of CogVLM with masked inputs and Mistral-7B with in-context learning generates attribute-rich instructions beyond simple class labels.

- **General editing improvement via dataset combination.** Merging PIPE with the IP2P dataset and fine-tuning on MagicBrush yields new SOTA on the full MagicBrush test set (Table 8), demonstrating that PIPE's value extends beyond object addition to boost overall instruction-following editing.

## Weaknesses

### Fatal

None.

### Major

None. The paper's core claims are supported by the evidence presented. The weaknesses below are addressable in revision or desirable for strengthening but do not undermine the fundamental contribution.

### Minor

- **The final dataset yield after all filtering stages is not clearly reported.** Line 205 reports "889,230 unique images" as the raw input from COCO+OpenImages, and the abstract/introduction claim "approximately 1 million image pairs" and "1,879,919 instructions" (Table 1). However, the multi-stage filtering pipeline (pre-removal: mask size/location/CLIP similarity; post-removal: CLIP consensus, multimodal CLIP, importance filtering) necessarily removes some fraction of examples. The paper never explicitly states the number of source-target-instruction triplets that survive *all* filtering stages. Since the pipeline's stringency directly affects dataset quality, knowing the yield is important for assessing the trade-off between scale and filtering rigor. This is an omission of a useful reporting detail, not a fatal flaw — even a conservative yield estimate from 889K images would still constitute a large dataset.

- **Filtering thresholds are described qualitatively, not quantitatively.** The CLIP consensus threshold (line 239: "manually adjusted") and importance filtering threshold (line 251: "manually set threshold") are reported without numerical values or a reproducible decision rule. Without these, other researchers cannot replicate the filtering pipeline exactly. The supplementary materials may contain additional details (the paper references them), but the main text should at minimum report the actual threshold values or describe how they were determined (e.g., percentile-based on a validation set).

- **No ablation study isolating the contributions of dataset components.** The PIPE pipeline combines three instruction sources (class-based, VLM-LLM, reference-based) and multiple filtering stages (CLIP consensus, multimodal CLIP, importance filtering). The paper does not include experiments that ablate individual components — e.g., training without VLM-LLM instructions, without the CLIP-consensus filter, or with a relaxed filtering threshold. Such ablations would directly demonstrate which design choices drive the reported performance gains versus treating the pipeline as a monolith.

- **The central "inversion" insight (removal is easier than addition) is asserted but not directly validated.** The paper argues that object removal is simpler and therefore a suitable proxy for generating addition training data. This claim is intuitive but could be supported by measuring the success rate of the removal pipeline (what fraction of images pass all filters?) versus a hypothetical direct-addition pipeline. Without such evidence, the insight remains plausible but untested — though the downstream experimental validation does support the overall approach.

- **The PIPE test set inherits the same pipeline biases as the training set.** The 750-image test set from COCO validation (Section 5.1) is constructed using the same inpainting model and filtering pipeline as the training data. This makes performance on this test set a measure of in-distribution effectiveness. However, this concern is partially mitigated by evaluation on two external benchmarks (MagicBrush and OPA) that use independently constructed data.

### Trivial

- None.

## Nice-to-Haves

- A survival/sankey diagram showing how many image-mask pairs pass each filtering stage would make the "approximately 1 million" claim precise and illustrate the quality–scale trade-off.
- Reporting the distribution of instruction types (what fraction of the 1.88M instructions come from each of the three sources) would help readers understand the dataset's composition.
- A brief failure-case analysis showing what the model produces on instructions that require physical plausibility (e.g., floating objects, unusual scales) would give useful context for the method's limitations.

## Removed Points

The following criticisms from the Harsh Critic were evaluated against the paper text and removed:

1. **"Evaluation on general editing (Section 6) lacks reproducibility and raises fairness concerns"** — The paper transparently states it could not reproduce the original MagicBrush numbers (line 505) and *then* runs all models (its own and the IP2P FT baseline) with the same seed and the official evaluation script. The comparison in Table 8 is between the authors' own IP2P FT and Ours+IP2P FT, both evaluated under identical conditions. This is a fair and properly documented comparison, not an unfair one anchored to an unreproduced number. The criticism misreads the experimental design.

2. **"Human evaluation protocol conflation may inflate preference"** — The paper explicitly asks annotators to provide "reasonable image addition instructions" (line 443), meaning the evaluation is scoped to object addition by design. Comparing an object-addition model against IP2P (which was also trained on object-addition instructions) on object-addition instructions is the correct evaluation paradigm, not a bias. The paper's model is appropriately evaluated on its claimed strength.

3. **Criticisms questioning reproducibility of filtering pipeline due to "manually adjusted" thresholds** — Kept in Minor above but reduced in severity. The threshold values are indeed missing, but the filtering pipeline is described with enough specificity (CLIP consensus = standard deviation of three inpainted CLIP embeddings, multimodal CLIP = similarity between inpainted region and class name) that the approach is reproducible in principle even without the exact numbers — the authors just need to report them.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge with the paper's stated claims; the insights from the Harsh Critic are standard reviewer concerns about reporting completeness rather than novel observations about the work.

## Suggestions

- Report the final number of training triplets after all filtering stages, ideally as a per-stage survival table or figure.
- Provide numerical values for the CLIP consensus threshold, multimodal CLIP filtering threshold, and importance filtering similarity threshold, or describe the rule used to set them (e.g., percentile-based on a held-out set).
- Add an ablation experiment training the model on a subset of PIPE (e.g., class-based instructions only, or without the CLIP-consensus filter) to demonstrate which pipeline components drive performance.
- Move the MagicBrush reproduction note (line 505) to a separate limitation paragraph, and consider including the authors' own IP2P FT numbers alongside the original MagicBrush reported numbers for full transparency.

## Score and Decision

**Originality:** 4/5 — The inversion insight is genuinely novel and practically useful, though the overall training recipe (diffusion model + instruction conditioning) builds on established methods.

**Importance of research question:** 4/5 — High-quality object addition is a well-motivated problem with practical applications, and the lack of large-scale natural-image training data was a genuine bottleneck.

**Claims support:** 3.5/5 — The core claims are well supported by quantitative and human evaluation, but the missing filtering yield and threshold details slightly weaken the dataset contribution's verifiability.

**Soundness of experiments:** 4/5 — Solid experimental design with multiple benchmarks, baselines, and human evaluation. The general editing experiment is fairly designed. Minor gaps (no ablations) are common for dataset papers of this scale.

**Clarity of writing:** 4/5 — Well-structured and readable. The pipeline is clearly described, and the figures are informative.

**Value to community:** 4/5 — The PIPE dataset and trained models, if released as promised, would be useful resources for the community working on instruction-based image editing.

The paper makes a solid contribution: a clever and scalable dataset generation method, thorough experimental validation, and a model that demonstrably advances object-addition performance. The weaknesses are all addressable reporting gaps rather than structural flaws. The paper is above the acceptance threshold for a major venue.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
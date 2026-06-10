Here is my consolidated review.

## Summary

This paper investigates whether instruction-tuned multimodal LLMs (MLLMs) prompted with different natural language instructions produce representations that differentially align with human fMRI brain activity in visual cortex. Using three MLLMs (InstructBLIP, mPLUG-Owl, IDEFICS) and ten instructions spanning six task categories (image captioning, VQA, visual relationships, commonsense reasoning, image understanding, scene recognition) on the NSD dataset, the authors show that MLLMs outperform vision-only models and match or exceed CLIP-Text. Through winner-take-all brain maps and variance partitioning, they report that different instructions align with different visual regions, with image captioning acting as an "umbrella" category sharing high variance with most other instructions.

## Strengths

- **First systematic study using instruction-tuned MLLMs with diverse natural language instructions for brain encoding.** Prior brain encoding work relied on CLIP embeddings or task-specific fine-tuned models. This paper probes three MLLMs with ten instructions (Table 1) and produces instruction-specific brain maps (Figs. 3–4), opening a new direction. This claim is explicitly stated (lines 23, 30) and supported by the experimental design spanning 10 instructions, 3 MLLMs, and the NSD fMRI dataset.

- **Variance partitioning quantitatively reveals asymmetric shared variance between instruction types.** Fig. 6 shows that Image Captioning (IC) shares high variance with most other prompts (VQ1, VQ2, CR, IU1) while IU2 ("list any food items") and SR (scene recognition) show consistently lower shared variance. The paper further provides mechanistic justification through image-category overlap analysis (line 128–129, referencing Fig. 15), going beyond reporting raw numbers.

- **MLLMs achieve comparable brain alignment to CLIP-Text despite generating their own output tokens rather than using ground-truth captions.** Fig. 2 and line 87 document this finding. CLIP receives human-written captions; MLLMs generate text from instructions alone. That MLLMs still match CLIP demonstrates that instruction-tuned models extract brain-relevant information without explicit supervision from ground-truth text.

- **Layer-wise analysis reveals distinct, architecture-dependent alignment patterns across MLLMs.** Fig. 5 and lines 114–119 show that InstructBLIP and IDEFICS exhibit middle-layer alignment with high-level visual regions and later-layer alignment with early visual regions, while mPLUG-Owl shows later-layer alignment with both region types — attributed to differences in underlying language decoders (line 114).

- **Visual concept grouping identifies specific capabilities (count/recognition) and limitations (color/position/scene) of MLLMs for brain alignment.** The paper groups 10 instructions into 5 visual concepts (lines 110–112) and provides concrete, falsifiable observations: MLLMs capture count and recognition concepts with distinct patterns but show uniform patterns for color, position, and scene understanding.

## Weaknesses

### Major

- **The CLIP comparison is confounded by different input text, limiting its interpretability as a comparative claim.** CLIP-Text receives ground-truth image captions from COCO, while MLLMs use model-generated output tokens from their own decoding (line 57, Fig. 2 caption). Two factors differ simultaneously (model architecture *and* input text). The paper transparently notes this difference, but the abstract and conclusions repeatedly state MLLMs "perform comparably to multimodal models such as CLIP" — a statement whose scientific strength is weakened because we cannot tell whether CLIP with MLLM-generated text, or MLLMs with ground-truth captions, would change the outcome. A controlled comparison (e.g., CLIP with the same generated text, or MLLMs with ground-truth captions) is needed for the comparative claim to be properly supported.

- **The instruction-specific brain alignment findings rely almost entirely on qualitative visual inspection for a single subject, without statistical quantification.** The paper's core contribution — that different instructions produce different patterns of brain alignment (e.g., image captioning aligns with EBA/PPA/FFA, image understanding with early visual cortex) — rests on winner-take-all colormaps (Figs. 3, 4, 5) shown for Subject 1 only. There are no statistical tests quantifying whether the spatial distribution of "winning instructions" differs significantly across ROIs, no permutation tests or overlap coefficients, and no confidence intervals on the shared variance estimates in Fig. 6. The paper states results are averaged across subjects for whole-brain analysis (Fig. 2), but the qualitative brain maps central to the instruction-specific claims are for one subject only. For an empirical study whose main findings are about differential alignment, this is a significant evidential gap.

- **Missing baselines needed to attribute effects to instruction-tuning specifically.** The paper compares MLLMs to ViT-H (unimodal vision) and CLIP (with ground-truth captions). Neither baseline controls for what instruction-tuning contributes beyond general multimodality or language generation. The paper's ability to attribute effects to *instruction-tuning* would be substantially strengthened by: (a) comparing each MLLM to its base model without instruction-tuning (e.g., InstructBLIP vs. BLIP-2), (b) testing CLIP prompted with the same instructions to see whether non-instruction-tuned multimodal models also show instruction-specific alignment, and (c) comparing the MLLM with task-specific prompts versus a generic "describe this image" prompt to distinguish instruction-specific effects from generic language generation.

- **Variance partitioning is only shown for one of the three MLLMs.** Fig. 6 and the entire Section 6.3 present shared variance analysis only for InstructBLIP (line 128: "for the InstructBLIP model"). The paper uses three MLLMs throughout other analyses, so generalizing the variance partitioning findings to "MLLMs" is not supported by the evidence shown.

### Minor

- **The visual concept grouping is post-hoc and its evaluation criteria are not operationally defined.** The paper groups 10 instructions into 5 "visual concepts" (Count, Recognition, Color/Texture, Positional Understanding, General Scene Understanding) and claims MLLMs "effectively capture" count and recognition while showing "similar patterns" for the rest. But what constitutes "effectively capture" vs. "similar patterns" is never defined. Moreover, the Color/Texture group contains only a single instruction (IU1: "describe the most dominant color"), making cross-instruction differentiation impossible within that group — yet this is treated as evidence that the model "fails to differentiate." The analysis would benefit from clearer, pre-specified criteria for what counts as differentiation.

- **The variance partitioning formula (line 70) can produce negative shared variance values, but the paper does not mention whether this occurred or how it was handled.** This is a known issue with variance partitioning in encoding models and should be addressed.

- **PCA is applied to reduce 4096D representations to 1024D (line 55), but the paper does not report how many components were retained or what fraction of variance they explain.** Nor does it specify whether PCA is fit on the training set only (critical for generalization validity).

- **No error bars or variance estimates are provided on the shared variance values in Fig. 6.** The figure reports averages across subjects, but the reader cannot assess the reliability of the overlap patterns.

### Trivial

- None beyond the minor issues above.

## Nice-to-Haves

- A comparison to dedicated task-specific models from prior work (e.g., an object detector vs. the MLLM prompted with "what objects are in this image?") would directly test whether MLLMs offer an advantage over the prior paradigm of separate task-specific models.
- An ablation on the feature extraction strategy (averaging generated tokens vs. last-token hidden state vs. pooled output) would strengthen the methodology section.
- The layer-wise brain maps (Fig. 5) could be supplemented by quantitative layer-wise alignment curves (e.g., alignment vs. layer number per ROI) for all subjects, not just the winner-take-all maps for Subject 1.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"First to propose" overstatement (from Harsh Critic):** The critic claimed the paper's claim of being "first" is overstated because Aw et al. (2023) used instruction-tuned language models. However, the paper specifically claims being first to use *multimodal* instruction-tuned MLLMs (line 23, 30), which is distinct from Aw et al.'s language-only models. Removed as factually inaccurate.
- **Feature extraction "not justified":** The paper does provide justification for using `model.generate` and averaging hidden states (lines 49–55: "the hidden states are influenced by both the input tokens and the generated tokens, making them dependent on the generation context"). Removed as factually incorrect.
- **"Significantly outperform randomly initialized" is a weak baseline:** This is standard practice in brain encoding as a sanity check. Removed as a generic criticism.
- **Missing related works:** Hard rule prohibits mentioning missing related works as the reviewer cannot verify their existence.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the CLIP comparison** by running CLIP with the same MLLM-generated text (or MLLMs with ground-truth captions) to produce a controlled comparison.
2. **Add the base model comparison** (InstructBLIP vs. BLIP-2, etc.) to isolate the effect of instruction-tuning.
3. **Quantify the brain-map differences statistically** — compute pairwise spatial overlap (e.g., Dice coefficients or correlation of alignment maps) between instructions within and across ROIs with permutation-based significance tests, and report these for all 4 subjects.
4. **Show variance partitioning for all three MLLMs** to assess whether the shared variance patterns generalize.
5. **Add confidence intervals or error bars** to the shared variance estimates (Fig. 6) across subjects.

## Score and Decision

This paper tackles a genuinely interesting and timely question — whether different natural language instructions to MLLMs produce representations that differentially align with brain activity in visual cortex. The experimental design is broad in scope (3 MLLMs, 10 instructions, variance partitioning) and the findings about differential alignment and shared variance are suggestive. However, the paper's core claims are undermined by three structural weaknesses: (1) the CLIP comparison central to the paper's comparative framing is confounded by different input text types; (2) the instruction-specific alignment findings — which constitute the paper's main scientific contribution — rely almost entirely on qualitative visual inspection of winner-take-all brain maps from a single subject without any statistical quantification; and (3) the baselines needed to attribute observed effects to *instruction-tuning* (as opposed to multimodality or language generation) are absent. The variance partitioning — a key piece of quantitative evidence — is only shown for one of three MLLMs. These issues are fixable but require substantive changes to the experimental design and analysis. For a top-tier venue, the evidence as presented does not support the strength of the claims being made.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
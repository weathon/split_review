Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary
This paper proposes KEEP, a two-stage prompting framework for VLMs (e.g., CLIP) that (1) generates fine-grained, image-specific knowledge prompts by combining domain-specific foundation models with retrieval-augmented generation, and (2) learns semantic alignments between images and these knowledge-enhanced prompts via an attention-based prompt learning module. The method is evaluated on 8 datasets spanning medical (dermoscopic, X-ray, MRI) and natural (generic objects, fine-grained, texture) domains, achieving consistent SOTA performance and providing visual/textual explanations.

## Strengths

**1. Consistent SOTA performance across diverse domains.** Tables 1 and 2 show KEEP outperforms all 8 compared baselines (CoOp, CoCoOp, Tip-Adapter, KgCoOp, LASP, GraphAdapter, TCP) on all 8 datasets — a clean and difficult sweep. The average relative improvements (~3.2% on medical, ~2.6% on natural) over the second-best method are meaningful.

**2. Strong data efficiency demonstrated across both medical and natural settings.** Table 3 shows KEEP degrades much less than alternatives when training data is reduced (e.g., on CCBTM, KEEP drops only 2.9% points from 94.9% to 92.0% when going from 50% to 10% data, versus LASP dropping 8.8% from 91.5% to 82.7%). Figure 3 shows consistent gains across 1–16 shot settings on natural datasets.

**3. Novel and well-motivated integration of domain-specific FMs and RAG for image-wise prompt creation.** Section 3.2 describes a principled pipeline: (a) LLM generates candidate clinical concepts per disease, (b) RAG retrieves domain documents to filter/refine concepts, and (c) domain-specific FMs (KAD, BiomedCLIP) detect concept presence per image — resulting in image-specific prompts without requiring manual fine-grained annotations.

**4. Quantitative faithfulness validation via knowledge intervention.** Figure 4 shows systematic performance degradation when the knowledge is removed, randomized, replaced with generic knowledge, or intervened (semantically flipped), directly supporting the claim that the model relies faithfully on the domain-specific knowledge.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

**1. The knowledge intervention experiment conflates two variables.** Figure 4 compares "no knowledge," "random knowledge," "general knowledge," "domain-specific knowledge," and "intervened knowledge." However, the "general knowledge" condition does not specify whether it is image-wise or class-level, nor whether it was generated via the same pipeline (LLM+RAG) or a different one. A cleaner comparison would pair: (a) KEEP as-is, (b) KEEP with image-specific knowledge from a generic (non-domain-specific) LLM using the same pipeline, and (c) KEEP with no knowledge. This would isolate whether the *domain-specificity* of the knowledge drives the gains, versus simply having *any* image-specific textual augmentation. The current evidence supports the claim but does not fully disentangle these factors.

**2. Interpretability beyond faithfulness is evaluated only qualitatively.** Understandability and plausibility are demonstrated through attention maps, word-importance heatmaps, and t-SNE plots (Figures 5–6). These are informative but do not constitute a quantitative evaluation of explanation quality. The paper would benefit from at least one quantitative metric — e.g., a pointing game (if ground-truth annotations exist for some datasets), measuring alignment of top-ranked textual concepts with human-provided attributes, or a small user study. This would strengthen the interpretability claims from "illustrative" to "evidence-based."

**3. No discussion of computational cost.** The knowledge creation stage runs multiple large models per image (domain-specific FM for concept detection, LLM with RAG for concept generation/refinement, and optionally MiniGPT-4/GPT-4 for natural images). This is a non-trivial overhead at inference time. A quantitative comparison of training/inference time and memory relative to baselines would help readers assess the practical trade-offs of the method.

### Trivial

- Typo: "EXPERIENTS" → "EXPERIMENTS" (Section 4 heading, line 92).
- Typo: "Alabtion Study" → "Ablation Study" (line 133).
- Typo: "adaption" appears where "adaptation" is intended (e.g., lines 10, 12, 22).

## Nice-to-Haves

- A more explicit discussion of how the framework's reliance on domain-specific FMs (KAD, BiomedCLIP) limits applicability to domains where such models do not yet exist, and how this dependency could be reduced.
- A discussion of why domain-specificity matters: comparison between KEEP and a variant using image captions from a generic VLM (e.g., BLIP) instead of concept-based knowledge from domain FMs, to separate the effect of *image-specificity* from *domain-specificity*.
- Providing the key equations of the image-prompt attention module and the losses (ℒ_IPM, ℒ_CLS) in the main paper rather than deferring them (the Section 3.3 content was stripped by the parser, but if it was in an appendix originally, moving it to the main text would benefit reproducibility).

## Removed Points
These points are flagged to be removed; treat them with caution.

- **"Missing core method section (Section 3.3)"** — The provided text jumps from Section 3.2 to Section 4, but this is a known parser artifact. The instruction for this review is to assume the original submission exists as intended. Removed per rule: parser-stripped sections are not author errors.
- **"The image-prompt attention module is mentioned but never defined"** — Same parser artifact as above. The module is described in the missing Section 3.3. Removed.
- **"Comparison against methods the reviewer prefers"** — No such issues found in the provided text.
- **"Generic strengths from Strength Finder"** — All strengths identified by the Strength Finder are specific, evidence-backed, and conflict-free. None were dropped.

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface a perspective on KEEP that the paper itself does not already offer.

## Suggestions

1. **Tighten the knowledge ablation:** Add a variant of KEEP where image-specific knowledge is generated using a generic (non-domain) LLM with the same RAG pipeline, to isolate whether domain-specificity or image-specificity is the primary driver of gains.
2. **Add at least one quantitative interpretability metric** (e.g., pointing game on a dataset with concept annotations, or human-evaluated alignment of highlighted concepts with ground-truth attributes).
3. **Include a paragraph on computational cost** (runtime per image, training overhead vs. baselines) to help the community assess practical trade-offs.
4. **Fix minor typos** ("EXPERIENTS" → "EXPERIMENTS", "Alabtion" → "Ablation", "adaption" → "adaptation" in several places).

## Score and Decision

**Originality:** 7/10 — The combination of domain-specific FMs, RAG, and attention-based prompt learning for image-wise knowledge is novel in the VLM adaptation literature. The paper clearly distinguishes itself from class-level knowledge methods (KgCoOp, LASP, TCP) and CuPL.

**Importance of research question:** 8/10 — Improving both performance and interpretability of VLM adaptation, especially for high-stakes domains like healthcare, is timely and well-motivated.

**Claims support:** 7/10 — The central performance claims are well-supported by extensive experiments. The interpretability claims are partially supported (faithfulness is quantified) but would benefit from quantitative evaluation of explanation quality.

**Soundness of experiments:** 8/10 — Broad benchmark (8 datasets), fair baselines, proper ablations, and data efficiency analyses. No obvious methodological errors.

**Clarity of writing:** 6/10 — The method description is clear for Section 3.2. The writing has a few typos and somewhat repetitive phrasing. The missing method section in the provided text (if present in the original) should be complete.

**Value to community:** 7/10 — The framework is practically useful and the code release commitment adds value. The approach is general enough to be applied to new domains where domain-specific FMs exist.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
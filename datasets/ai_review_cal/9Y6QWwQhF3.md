- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 6, 3, 3
Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper introduces FoREST, a benchmark for evaluating Frame of Reference (FoR) understanding in spatial language. The dataset has two splits: ambiguous (A-split, multiple valid FoRs) and clear (C-split, one valid FoR), built from four relatum cases (cow, box, car, pen) that systematically vary intrinsic direction and container affordance. The authors evaluate multiple LLMs under various prompting methods (zero-shot, few-shot, CoT, and their proposed Spatial-Guided prompting) and extend the analysis to text-to-image generation via layout diffusion. Results reveal systematic FoR biases across models (e.g., Gemma2-9B favors external relative, GPT-4o favors external intrinsic) and show that SG prompting improves FoR identification by leveraging spatial relation types.

## Strengths

1. **Systematic ambiguous/clear split design grounded in relatum properties** — The FoREST benchmark is built on a principled 2×2 taxonomy (intrinsic direction × container affordance), yielding four relatum cases (cow, box, car, pen) that generate both ambiguous and clear spatial expressions (Section 3.1). This design cleanly isolates the factors causing FoR ambiguity and provides a structured diagnostic tool, representing a concrete advance over prior benchmarks that assumed a single FoR.

2. **SG prompting improves FoR identification and reduces the gap between inherently clear and template-clarified contexts** — Table 2 shows that SG prompting achieves a smaller performance gap between inherently clear expressions and those requiring clarification, compared to CoT. The paper's textual description (Section 5.3.2) confirms this pattern across multiple LLMs, supporting the claim that explicitly considering spatial relation types (directional, topological, distance) yields more robust FoR identification.

3. **Demonstrates FoR's impact on text-to-image generation** — Table 3 shows that incorporating SG-generated FoR information into the layout diffusion pipeline (Llama3+SG+GLIGEN) improves VISOR_cond scores across all splits compared to the baseline without FoR information (Llama3+GLIGEN). The analysis further reveals an interesting asymmetry: GLIGEN-based models improve mainly on relative FoR while SD-2.1 performs better on intrinsic FoR, providing insight into how current layout diffusion handles perspective.

## Weaknesses

### Fatal

None.

### Major

1. **Dataset instance counts are not reported.** The paper describes the construction pipeline (20 objects across 9 object sets, 4 relatum cases, spatial relation templates, A-split and C-split) but never states the total number of spatial expressions per split, per case, or per FoR class. For a benchmark paper, this is a significant omission: readers cannot assess statistical reliability, compare to other benchmarks, or determine whether certain per-class accuracy numbers (e.g., near-perfect scores on some splits) are based on 20 or 200 examples. The authors should report exact counts per split, per case, and ideally per FoR class.

### Minor

1. **The T2I evaluation protocol for ambiguous expressions is underspecified.** The paper states (Section 5.1) that the authors "convert all relations based on their FoR to be expressed from camera view and then pass it to spatialEval evaluation" and for ambiguous contexts "consider it correct if it fits one of the valid FoRs." However, the conversion procedure itself — how the system determines which FoR interpretation a generated image actually realizes — is not described. This leaves a reproducibility gap, particularly for the ambiguous-split evaluation.

2. **Key comparisons lack confidence intervals or variance estimates.** Results in Tables 1-3 are reported as point estimates without error bars, confidence intervals, or significance tests. The claim that SG "reduces the gap" between inherently clear and template-clarified contexts (Table 2) in particular would be strengthened by per-category counts or bootstrapped intervals. While single-run evaluation is common in LLM prompting papers, the statistical reliability of the reported differences is unclear.

3. **Small model results for SG/CoT show performance degradation but this is discussed only qualitatively.** The paper notes (Section 5.3.2) that "while CoT prompting generally improves performance in larger LLMs, it is counterproductive in smaller models for some FoR classes" and that "this negative effect also appears in SG prompting, which uses longer explanations." This is an interesting observation but no systematic analysis or breakdown is provided, making it hard to assess how robust the SG advantage is across model scales.

### Trivial

None.

## Nice-to-Haves

- **Provide exact prompts used for each ICL method.** The paper describes the prompting strategies (Section 4.1) but does not show the full prompt templates. Including these (e.g., in an appendix) would aid reproducibility.
- **Add a T2I baseline that directly injects FoR information into the SD prompt** without the layout diffusion pipeline, to isolate whether improvement comes from the layout pipeline or just better textual context.
- **Include failure case analysis** for SG prompting on larger models — understanding what errors remain would deepen insight into the method's limitations.
- **Per-case dataset composition table** showing how many expressions belong to each of the four relatum cases in A-split and C-split.

## Removed Points

These points from the reviewers are removed with justification:

- **"Table 1 formatting is garbled"** — This is a parser artifact from PDF extraction; the original paper contains a properly formatted table. Removed per formatting-artifact rule.
- **"C-spilt typo"** — The extracted text shows "C-spilt" on some lines, but this is a parser/OCR artifact; the original submission does not have this issue. Removed per formatting-artifact rule.
- **"Claim that SG enhances T2I is overstated"** — The paper reports improvement across all splits in Table 3 (Section 5.3.3), so the conclusion statement "enhances text-to-image generation performance" is consistent with the evidence. The improvement is modest but not falsely claimed. Removed as the claim is supported by the presented data.
- **"Only 20 objects could limit diversity"** — This is a generic speculation about diversity rather than a concrete identified problem. The paper's contribution is about FoR evaluation, not object diversity per se. Removed as a non-specific concern.
- **"Full prompts not shown"** — Moved to Nice-to-Haves since prompt descriptions in Section 4.1 are detailed enough to understand the method, though exact prompts would be beneficial.
- **Strength Finder claim about SG "demonstrably improves... over CoT" with specific numbers** — The general pattern is supported by the paper, but the specific accuracy numbers cited (95.8%, 91.0%, etc.) cannot be verified from the extracted text as the tables are embedded images. The strength is retained in general form based on the paper's textual description.

## Novel Insights

Neither reviewer identifies a genuinely novel observation beyond what the paper itself contributes. The paper's key finding — that LLMs exhibit systematic, model-specific FoR biases (e.g., fixed biases in Gemma2-9B and GPT-4o vs. relatum-dependent bias in Llama3-70B) — is the most interesting result and comes from the authors' own analysis.

## Suggestions

1. **Report explicit dataset statistics.** Provide a table with per-split, per-case, and per-FoR-class instance counts. This is the single most important revision for establishing the benchmark as a usable resource.
2. **Add a worked example of the T2I evaluation pipeline.** Walk through one ambiguous expression (e.g., "a car is to the right of a cow") and show step by step how the generated image is evaluated, including how the FoR-to-camera-view conversion works.
3. **Include bootstrap confidence intervals** for the main accuracy comparisons (SG vs. CoT on C-split, per-model biases) to clarify which differences are reliable.
4. **Tone down the "enhances T2I" framing** or add a baseline that isolates the contribution of FoR information from the layout pipeline, so readers can assess how much value is added at each stage.

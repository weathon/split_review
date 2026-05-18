Now I have thoroughly verified all claims. Here is my final consolidated review.

---

## Summary

This paper introduces CADRefine, a VLM-driven refinement loop for CAD code generation that works by having a VLM generate binary verification questions about a generated object, answer them using rendered images, and produce corrective feedback to iteratively improve the code. It also introduces CADPrompt, a benchmark of 200 3D objects with expert-annotated Python code and natural language prompts, claimed as the first quantitative benchmark for CAD code generation. Experiments across GPT-4, Gemini 1.5 Pro, and CodeLlama show consistent improvements over the prior 3D-Premise baseline and demonstrate that the approach is especially valuable on harder examples where prior work degrades.

## Strengths

- **First dedicated benchmark for CAD code generation.** CADPrompt (200 objects with expert code and language descriptions, stratified by complexity and compilation difficulty) fills a real gap. Prior work relied on qualitative evaluation; CADPrompt enables standardized, replicable assessment (Section 4, Table 1).

- **Consistent improvements over the prior refinement method (3D-Premise).** Across multiple VLMs and both zero-shot and few-shot settings, CADRefine reduces geometric error and improves success rate. For GPT-4 few-shot: Point Cloud distance drops from 0.137 to 0.127, success rate rises from 91.0% to 96.5% (Table 1). The gains are systematic, not cherry-picked.

- **Robust performance on challenging data where prior work degrades.** On the "Hard" split, 3D-Premise causes a ~20% drop in success rate, while CADRefine is the only method that improves it (~9% increase at Refine-1, Figure 2). This is the strongest evidence that the method makes a practical difference for complex designs.

- **Ablation analysis validates the design choices.** Removing reference images worsens Point Cloud distance from 0.126 to 0.153; switching to zero-shot QA generation increases it to 0.141 (Table 3/ablation table). These component-level checks confirm that both visual input and few-shot question examples contribute meaningfully.

## Weaknesses

### Fatal

None.

### Major

1. **Benchmark validity: under-specified prompts vs. exact ground truth metrics.** The CADPrompt prompts deliberately exclude precise numeric parameters (e.g., height, width) on the grounds that average users lack such knowledge (line 188). Yet the ground truth objects are specific instantiations with exact dimensions. The evaluation metrics (Point Cloud distance, Hausdorff distance, IoGT) all assume a unique correct shape and penalize any geometric deviation. This creates a fundamental mismatch: a VLM that generates a functionally reasonable but geometrically different desk (e.g., slightly taller legs) is penalized not because it failed the prompt but because the reference is one arbitrary point in a large equivalence class of valid objects. The paper acknowledges prompt sensitivity in the Limitations (line 436) but does not connect this to the metric mismatch or attempt to control for it. While relative comparisons between methods remain meaningful, the absolute error numbers conflate genuine generation failures with legitimate shape variation, weakening the benchmark's diagnostic power.

2. **The "upper limit" claim for the geometric solver is contradicted by the data.** The paper states the geometric solver baseline "serves as an upper limit for CAD code refinement, as it conveys the precise geometric differences between the generated 3D object and the ground truth" (line 228). However, for CodeLlama, this "upper limit" produces _worse_ results than the unaided "Generated" baseline: zero-shot success rate 55.5% vs. 64.5%, few-shot 60.5% vs. 67.0% (Table 1). Having access to exact ground-truth information should not produce worse outcomes if it were truly an upper bound. The paper does not discuss why this happens (e.g., the VLM cannot effectively act on numerical parametric feedback, or the format overwhelms the instruction), nor does it qualify the claim for non-multimodal or weaker models. This undermines the interpretation of the geometric solver as a gold standard and misrepresents an informative failure case as a point of comparison.

### Minor

3. **Inconsistent success rate claims.** The abstract claims a "5.0% improvement in success rate compared to prior work" while the contributions section (line 36) claims a "5.5% increase in successful object generation." The 5.5% matches the absolute percentage-point difference for GPT-4 few-shot (96.5% - 91.0% = 5.5 pp). The 5.0% figure in the abstract does not match any row in the table (zero-shot: 2.5 pp; few-shot: 5.5 pp; relative: 6.0%). This numeric inconsistency, though small, erodes confidence in the precision of the reported results and should be corrected.

4. **The Q&A and feedback mechanism remains a black box.** CADRefine's core innovation is generating binary verification questions, answering them via rendered images, and producing targeted feedback. The paper never evaluates these intermediate artifacts: How often are the questions relevant? How accurate are the answers (especially given the VLM is inspecting renders of its own potentially flawed object)? Does the feedback actually address identified deviations or provide generic instructions? The ablation study (Table 3) removes entire components but does not reveal _why_ or _how_ they help. Without any qualitative analysis or human evaluation of the Q&A outputs, the mechanism's operation is opaque, and it is unclear whether the gains come from targeted error diagnosis or from the VLM receiving more context.

5. **Stage-wise success rate not tracked in the main evaluation.** Table 1 reports only the final refined result, collapsing objects that compiled at different stages into one number. Figure 2 provides stage-wise analysis for GPT-4's difficulty/complexity splits, but this is not extended to other models or to the main quantitative comparison. This makes it impossible to determine whether CADRefine rescues previously non-compiling programs or merely polishes already-compiling ones — an important distinction for understanding the method's practical value.

6. **The "Unclear" QA response option is mentioned but never analyzed.** The paper states that the VLM can answer "Unclear" when information is insufficient (line 134), but there is no analysis of how often this occurs, whether it leads to better or worse feedback, or how it affects the refinement trajectory. This is a potentially valuable design element left entirely unexplored.

7. **Dataset diversity is limited.** CADPrompt draws 200 objects from a single prior source (Wu_2021_ICCV) originally designed for modular CAD. The paper does not discuss how representative these objects are of real-world industrial design tasks or whether topological patterns are shared across examples. While 200 is reasonable for a first benchmark, this limitation constrains the generality of conclusions drawn from it.

### Trivial

8. **Hausdorff distance IQRs are larger than the median in many CodeLlama rows** (e.g., zero-shot generated: median 0.731, IQR 1.270, Table 1). This is partly an artifact of assigning √3 to non-compiling cases, but it diminishes the interpretability of the metric and is not discussed.

9. **No prompt sensitivity analysis.** The paper acknowledges prompt quality affects results (in Limitations) but provides no measurement of how much output varies across different phrasings of the same object description — important for practical deployment.

## Nice-to-Haves

- **Statistical significance testing.** Given the modest dataset size (200) and the high variance in geometric metrics (large IQRs), confidence intervals or paired tests would strengthen the reliability of the reported comparisons. However, single-run evaluation is the norm in this emerging area, so its absence is not a weakness per se.
- **Sensitivity analysis on the number of refinement iterations.** The paper sets refinements to 2 with justification (line 119), but varying this number would test the robustness of the conclusion that two iterations suffice.
- **Comparison of using 1 vs. 4 reference images.** The ablation shows images help overall but does not vary the number of views, which would inform cost-effectiveness.

## Removed Points

These criticisms were evaluated against the paper and found to be unsupported, factually incorrect, or otherwise invalid under the review guidelines:

1. **"Number of refinements (2) is not justified."** — The paper explicitly provides a justification at line 119: "we set the number of refinements to 2, as we did not observe any improvement after the second refinement, which is also consistent with prior work." The reviewer missed this.
2. **"Unclear role of VLM in CADRefine for CodeLlama; the paper does not measure CodeLlama's own ability to refine."** — The paper transparently states (line 372) that GPT-4 generates the feedback for CodeLlama because CodeLlama lacks multimodal capabilities. The claim of "model-agnostic" feedback refers to the feedback format being applicable across models (the results support this: CodeLlama improves from GPT-4-generated feedback). This is a reasonable interpretation, not a flaw. The criticism amounts to demanding CodeLlama do something it is architecturally incapable of, which is not a valid weakness.
3. **"Request for a prompt sensitivity analysis as a weakness"** — This is noted in Trivial above and in Nice-to-Haves; it was not asserted as a structural flaw by the reviewer and is appropriately categorized.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine tension in the paper's evaluation design (under-specified prompts evaluated against single-reference ground truth) that the authors should address, but this is an observation about the benchmark's limitations, not an insight that transcends the paper's framing.

## Suggestions

1. **Correct the numeric inconsistency.** Unify the success rate improvement claim across abstract and contributions to a single, verifiable number tied to a specific experimental setting (e.g., "a 5.5 percentage-point increase in success rate for GPT-4 few-shot").
2. **Address the prompt-ground-truth mismatch in CADPrompt.** Either (a) augment the benchmark with multiple reference objects per prompt covering plausible dimensional variations, or (b) introduce a functional evaluation metric (e.g., whether the generated object satisfies the prompt's structural constraints) alongside the geometric metrics. At minimum, discuss explicitly how the under-specification affects the interpretation of the reported distances.
3. **Qualitatively analyze the Q&A feedback.** Provide a representative sample of generated questions, answers, and resulting feedback, along with a small human evaluation of whether the identified deviations are real and whether the feedback correctly addresses them. This would open the black box and strengthen the claim that the method works through targeted error diagnosis.
4. **Recast the geometric solver baseline honestly.** Explain why it fails for CodeLlama (e.g., feedback format incompatibility, model-specific limitations) and soften the "upper limit" language to something like "an informative comparison point that provides ground-truth parametric feedback."
5. **Report success rates by compilation stage in Table 1** (e.g., the fraction that compiled at generation vs. after each refinement round), extending the Figure 2 analysis to all models and settings.

## Score and Decision

The paper tackles a genuine problem and demonstrably improves over prior work, especially on harder examples. The CADPrompt benchmark, despite the metric-mismatch concern, is a useful resource. However, the evaluation has two issues that are substantive rather than cosmetic: (1) the benchmark's metric design conflates legitimate shape variation with generation error, weakening diagnostic value; and (2) the "upper limit" claim for the geometric solver is contradicted by the CodeLlama data and left unexplained. These do not invalidate the core contribution — the method still outperforms baselines under the same evaluation framework — but they reduce confidence in the rigor of the paper's claims. The paper is acceptable after addressing these concerns through the suggested revisions.

**Score:** 6.0 (Weak Accept) — solid contribution with fixable evaluation weaknesses.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
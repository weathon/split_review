Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper introduces CADRefine, a method that uses a Vision-Language Model (VLM) to automatically generate and answer binary verification questions about a rendered 3D CAD object, then uses the resulting question-answer pairs to produce corrective feedback for refining the CAD scripting code — all without human intervention. The authors also present CADPrompt, a benchmark of 200 3D objects with paired natural language prompts and expert-written Python code, enabling the first quantitative evaluation of CAD code generation and refinement.

## Strengths

- **Fully automated VLM-driven refinement without human-in-the-loop.** CADRefine eliminates the need for the human expert feedback required by prior CAD code generation methods (Makatura 2023, Nelson 2023). This is validated across GPT-4, Gemini, and even CodeLlama (with GPT-4 providing feedback). The ablation confirms that both the few-shot question generation and reference images contribute to performance (Table 2).

- **Introduction of CADPrompt, the first quantitative benchmark for CAD code generation.** The dataset of 200 3D objects with paired prompts and expert-annotated Python code, stratified by complexity and compilation difficulty (Section 4, Table 2), enables reproducible quantitative evaluation that was previously absent in the field.

- **Consistent directional outperformance over the prior state-of-the-art (3D-Premise) across VLMs.** In nearly all settings, CADRefine achieves lower Point Cloud distance and higher success rate than 3D-Premise for GPT-4 and Gemini (Table 1). Notably, on the "Hard" data split the paper reports CADRefine is the only method that improves success rate (~9% at Refine-1) while 3D-Premise causes a 20% drop — the strongest evidence for the method's practical value.

- **Ablation analysis validates key design choices.** Removing reference images (0.126 → 0.153 Point Cloud distance) or using zero-shot question generation (0.126 → 0.141) both degrade performance, confirming the contribution of the two main components (Table 2).

## Weaknesses

### Fatal

None.

### Major

- **Evaluation metrics conflate compilation success with geometric quality, making the claimed geometric improvements ambiguous.** The paper assigns a maximum penalty (Point Cloud distance = √3, IoGT = 0) to any data point where code fails to compile. This means any method that improves the compilation rate will automatically reduce the average distance, even if the geometric quality of the *compiled* objects is unchanged. The improvement CADRefine shows over 3D-Premise (e.g., 0.137 → 0.127 Point Cloud distance for GPT-4 few-shot) could be partly or entirely driven by the increase in success rate (91% → 96.5%). The paper claims these distance reductions reflect "enhancing the structure of the 3D objects" (abstract) but never separates the two effects. This is not merely a presentation issue — it directly undermines the core claim that CADRefine improves geometric quality beyond compilation success. The paper should report metrics computed only on objects that compile in *both* conditions, or present success rate and per-metric improvements independently.

- **No qualitative examples of the question-answer-feedback pipeline.** The primary novelty of CADRefine is the question-generation and answering process that produces corrective feedback. Yet the paper contains zero examples of actual questions generated, which answers were "No" and triggered correction, or what the resulting feedback text looked like. Figure 2 shows only the output objects. For a method whose mechanism is the main contribution, this is a significant gap — the reader cannot assess whether the questions are reasonable, whether the VLM answers them correctly, or whether the feedback is specific and actionable. Adding a table or figure with question-answer-feedback triplets would substantially strengthen the paper.

### Minor

- **Small effect sizes without significance testing.** The absolute improvement over 3D-Premise is small (e.g., 0.01 reduction in Point Cloud distance on a scale where the IQR is 0.135). IoGT improvements are even smaller (0.942 → 0.944). No confidence intervals, bootstrapped errors, or statistical tests are reported. Given the small margins, it is unclear whether these improvements are statistically meaningful.

- **Inconsistent success rate claims across abstract and contributions.** The abstract claims a "5.0% improvement in success rate compared to prior work" while the contributions list claims a "5.5% increase in successful object generation" when applied to GPT-4. Neither cleanly maps to the numbers in Table 1 (e.g., GPT-4 few-shot: 3D-Premise 91.0% → Ours 96.5% = 5.5 *percentage points*, not 5.0% or 5.5% relative). These figures need to be reconciled and reported unambiguously.

- **"Model-agnostic" claim is overstated.** For CodeLlama (which has no vision capabilities), the paper uses GPT-4 to perform the question-answering and feedback generation, then gives the resulting feedback to CodeLlama for code refinement. This demonstrates that *GPT-4-generated feedback* can help CodeLlama, not that CADRefine works when the same model generates and consumes the feedback. The claim of model-agnosticism should be qualified to reflect this asymmetry.

- **Geometric solver "upper bound" claim is contradicted by CodeLlama results.** The paper calls the geometric solver baseline an "upper limit" for CAD code refinement (Section 5). However, for CodeLlama the geometric solver performs substantially *worse* than CADRefine (e.g., CodeLlama few-shot: Ours 0.185 vs. Geometric solver 0.239 Point Cloud distance) and even worse than the no-refinement "Generated" baseline. This indicates that either the 13 geometric categories don't capture key discrepancies or the numerical feedback format is ineffective for certain models. The paper should discuss this discrepancy rather than uniformly labeling the baseline an upper bound.

### Trivial

- Only 5 of the 13 geometric solver categories are listed (width, height, number of faces, number of vertices, volume); the remaining eight are not specified.
- The ablation study uses 100 randomly selected objects rather than the full 200, without justification for the subset size.
- The few-shot example questions used for question generation are not listed, affecting reproducibility.
- Equation (5) for feedback generation conditions only on Q and A, while the text suggests the original description and images are implicitly involved — this should be made explicit.

## Nice-to-Haves

- Quantitative validation of ground truth code accuracy (e.g., Chamfer distance between the expert-rendered mesh and the original STL object) would calibrate the benchmark's difficulty. The current visual verification in Blender is reasonable but not quantitative.
- An inference cost comparison (number of API calls, tokens) between CADRefine and 3D-Premise would help assess practical deployability.
- An error analysis categorizing failure cases (e.g., objects requiring precise dimensions, symmetry-related failures) would deepen understanding of the method's limitations.
- Standard test/train splits for CADPrompt would facilitate community adoption.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Strength from Strength Finder: "Model-agnostic improvement across LLMs and VLMs"** — partially conflicts with the verified weakness about the model-agnostic claim being overstated. The improvement itself (across models using GPT-4 feedback) is real, but the framing as "model-agnostic" is misleading. Replaced by a more precise statement in strengths.
- **Critic's Issue 4 ("Ground truth code not quantitatively validated against original objects")** — the paper does use Blender for visual verification with iterative correction by the expert. Requesting Chamfer distance calibration is reasonable but more of a nice-to-have than a weakness; moved accordingly.
- **Critic's note about "median split not justified"** — median splits are standard and require no special justification. Removed as overly nitpicky.
- **Critic's demand for "discussion of why 3D-Premise reduces compilation rate"** — speculative and not essential; the observation is captured in other weaknesses.
- **Strength Finder's claim of "5.0% improvement" as numerical evidence** — this number is inconsistent per verified weakness above; the strength is retained but without the contested numerical claim.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Disentangle compilation and geometry.** Recompute all distance metrics on the subset of objects that compile in *both* the baseline and refined conditions. If CADRefine still improves distances on this common set, the geometric quality claim is supported. If not, reframe the contribution as primarily improving compilation rates.
2. **Provide qualitative examples of the pipeline.** Show at least 2–3 concrete examples of: (i) the generated questions, (ii) which were answered "No," (iii) the resulting feedback text, and (iv) how the code changed in response. This is the most compelling evidence for the method's mechanism.
3. **Report confidence intervals or bootstrapped estimates** for all key metric differences.
4. **Reconcile the success rate claims** across the abstract and contributions, and report them unambiguously (percentage point vs. relative change).

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
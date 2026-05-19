- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5
I have now read the full paper and verified all reviewer claims against the source text. Let me produce the consolidated review.

---

## Summary

MME-Finance is a bilingual (English/1,171 samples + Chinese/1,103 samples) multimodal benchmark for evaluating MLLMs on expert-level financial tasks. It spans 11 open-ended VQA tasks organized into perception, reasoning, and cognition ability levels, covering 6 financial image types (candlestick charts, technical indicator charts, statistical charts, tables, documents, mixed charts) and 4 image styles (computer screenshots, mobile photographs, vertical/horizontal mobile screenshots). The benchmark employs a GPT-4o-based evaluator that incorporates the original image as input, achieving a Spearman correlation of 0.738 with human ratings. Evaluation of 19 MLLMs reveals that even the best models (Qwen2VL-72B at 65.69%, GPT-4o at 63.18%) perform poorly on finance-specific tasks such as candlestick chart understanding and spatial awareness.

## Strengths

1. **Expert-validated ground truth for a genuine domain gap.** The QA pairs are generated and refined through a multi-stage pipeline culminating in review by finance researchers with 10+ years of industry experience (Section 3.3). This is a higher annotation standard than most domain benchmarks and directly addresses the paper's motivating claim that general benchmarks do not capture financial expertise.

2. **Novel evaluation pipeline incorporating visual information with validated human agreement.** The paper introduces an LLM-based evaluator that takes the original image as additional input (Figure 4, Section 3.5). This achieves Spearman 0.738 with human raters (vs. 0.720 without image), and the average absolute difference drops to 0.84 (Table "evaluator", Section 4.3). The ablation comparing multiple evaluators (GPT-3.5Turbo, GPT-4Turbo, o1-preview, Qwen2VL-72B, CogVLM2, MiniCPM2.6) with and without image input provides useful evidence for the community on evaluation design.

3. **Fine-grained breakdowns yielding actionable insights.** Results are reported across 11 tasks (Table 2), 6 image types, and 4 image styles (Table 3). The finding that spatial awareness tops out at 30.31% and mobile photographs consistently underperform computer screenshots provides concrete direction for model developers. The hallucination analysis (NA task) with explicit "Not Applicable" prompting is a useful diagnostic.

4. **Comprehensive evaluation of 19 models spanning multiple families and scales.** The model zoo includes open-source (Qwen2VL, InternVL2, LLaVA-NEXT, MiniCPM, Phi3, CogVLM2, Yi-VL, LLaMA3.2) and proprietary (GPT-4o, GPT-4o-mini) models, enabling scale and architecture comparisons.

## Weaknesses

### Fatal
None.

### Major

1. **GPT-4o serves as both the primary evaluator and a model being evaluated, without discussion of the conflict.** The evaluation pipeline (Section 3.5, Figure 4) uses GPT-4o as the scoring model, while the main results (Table 2) report GPT-4o's own performance at 63.18% (second overall). This creates a systematic risk: if the evaluator rewards output styles or content patterns that match its own generation preferences, GPT-4o's scores may be inflated relative to other models. The paper neither acknowledges this conflict nor provides any mitigation (e.g., re-scoring GPT-4o's outputs with Qwen2VL-72B as an alternative evaluator and reporting whether the ranking changes). For a benchmark whose primary experimental findings are model rankings and ability-level comparisons, this is a meaningful gap.

2. **Evaluator agreement with humans is moderate for subjective questions, and no human-human agreement is reported to calibrate expectations.** The overall Spearman of 0.738 is reasonable, but for subjective questions (which include key cognition tasks like Risk Warning, Investment Advice, Reason Explanation), the correlation drops to 0.515 (Table sub_obj_evaluator). The paper does not report human-human inter-rater agreement on the 100-sample validation set, so the reader cannot judge whether 0.515 is near-ceiling or far from it. Without this upper bound, it is difficult to assess how much noise the evaluator introduces into the reported per-model and per-task scores, especially for the cognition-related conclusions.

3. **Several task categories have very small sample sizes, and reported percentages lack uncertainty measures.** Reason Explanation has 18 samples, Risk Warning has 22, Estimated Numerical Calculation has 42, and Not Applicable has 22 (Table 1). A shift of 2–3 correct answers changes reported scores by 5–10 percentage points on these tasks. The paper draws conclusions from these numbers (e.g., which model "excels" in cognition tasks), but no confidence intervals, bootstrap estimates, or margins of error are provided anywhere in the results. The paper does acknowledge sample size variation (line 165) but does not discuss its impact on the reliability of per-task conclusions.

### Minor

4. **Hallucination modification experiment is reported only qualitatively.** The paper states that modifying prompts to allow "Not Applicable" across all tasks "led to a rise in false negatives in most MLLMs" (Section 4.3) but provides no table, numbers, or comparison. This is an interesting additional experiment that should be quantified to be useful to the community.

5. **The claim of being "first to introduce visual information in the evaluation process" is slightly overstated given MM-Vet.** The paper correctly cites MM-Vet as inspiration (Section 3.5), but MM-Vet already provided images (with bounding box overlays) to GPT-4 for evaluation. The specific approach here (direct image input with task-specific prompts) is different and well-executed, but the "first" framing is unnecessary and invites a quibble that does not affect the paper's actual contribution.

6. **Two GPT-4o variants (GPT-4o-05-13 and GPT-4o) appear in Table 2 without explanation of the difference.** The earlier snapshot ("05-13") obtains markedly weaker results (42.85% overall) than the main GPT-4o (63.18%), but the paper provides no clarification on versioning. This is a presentation gap that will confuse readers.

### Trivial

- Table "evaluator" uses a formatting convention where the non-red value is without image and the red/parenthesized value is with image, but this is not explicitly explained in the caption — it requires inference from the column headers. (The column headers use red text for "Pic." but the body cells use red for the with-image value, which is an implicit mapping.)

## Nice-to-Haves

- **Report human-human inter-rater agreement** on the 100-sample validation set to establish an upper bound for evaluator performance. This would let the community assess whether 0.738 / 0.515 are close to ceiling or have meaningful headroom.
- **Provide Chinese benchmark results or at minimum a description** of whether the Chinese set is a translation or culturally adapted, and how the image sources differ. Currently the "bilingual" claim feels incomplete.
- **Add bootstrap confidence intervals** (or similar uncertainty estimates) for overall and per-task scores, especially for small-N tasks. This would prevent over-interpretation of point estimates.
- **Re-score GPT-4o's outputs using Qwen2VL-72B** as an independent evaluator to bound the evaluator-conflict concern, and report whether the ranking changes.

## Removed Points

These points were considered and removed with justification:

1. *"Evaluator comparison table misses GPT-4o without image as a baseline"* — **REMOVED (factually incorrect).** The table shows 0.720 (without image) and 0.738 (with image) for GPT-4o in the same cell. The critic misread the formatting.

2. *"The observation that model size matters is a generic finding"* — **REMOVED.** This is not a weakness; it is a reported observation consistent with prior work and the critic treats a descriptive finding as a flaw.

3. *"Missing related works"* — **REMOVED per instructions.** Cannot verify whether related works are missing without external sources.

4. *"Pure formatting/style nitpicks" about the paper's presentation* — **REMOVED per instructions.**

5. *The critic's speculation about statistical significance of the GPT-4o evaluator improvement (0.720 → 0.738)* — **REMOVED.** This is speculation without evidence; the paper reports the numbers as-is.

## Novel Insights

The most interesting observation from the reviews is that the paper's core contribution (the dataset) and its experimental findings (model rankings) have different evidentiary standards applied to them. The dataset construction pipeline is rigorous and well-documented, while the evaluation methodology that produces the model scores has verifiable gaps (evaluator conflict, no human-human baseline, no error bars). This creates a tension: the benchmark is clearly valuable as a resource, but the specific headline conclusions about model performance are less trustworthy than the paper presents them. The harsh critic correctly identified this tension but conflated it with the dataset contribution itself, leading to an overstatement of severity. The synthesis reveals that the paper would be strongest if it explicitly separates "here is the dataset, which is a community resource" from "here are initial findings, which are indicative and should be interpreted with the following caveats."

## Suggestions

1. **Acknowledge and bound the GPT-4o evaluator conflict.** At minimum, re-score GPT-4o's outputs using Qwen2VL-72B (which the paper already identifies as the best open-source evaluator with Spearman 0.678) and report whether the ranking of GPT-4o relative to other models changes. If it does not change, this substantially mitigates the concern.

2. **Report human-human agreement** on the 100 evaluation samples. This is a single number (e.g., Spearman or Fleiss' kappa among the three expert raters) and would immediately clarify whether the LLM evaluator is near ceiling or has meaningful room for improvement.

3. **Add confidence intervals** (e.g., bootstrap 95% CI) to the overall and per-task scores in Tables 2 and 3, particularly for tasks with N < 50. This prevents over-interpretation of small numerical differences.

4. **Quantify the hallucination modification experiment** — provide a table showing false negative rates per model when the "Not Applicable" option is extended to all tasks.

5. **Clarify GPT-4o versioning** in Table 2 and explain why GPT-4o-05-13 performs so much worse than the main GPT-4o entry.

6. **Tone down or qualify the "first" claim** about visual information in evaluation to avoid a distracting scope dispute. The method is solid and does not need the priority claim.

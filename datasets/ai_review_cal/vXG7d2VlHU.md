- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 3, 5
Now I have all the information I need. Let me compose the final consolidated review.

---

## Summary

The paper introduces Sparkle, a framework that fine-tunes Vision Language Models (VLMs) on three disentangled basic 2D spatial capabilities—direction comprehension, distance estimation, and localization—using programmatically generated synthetic data. The central hypothesis is that mastering these basic capabilities enables VLMs to generalize to composite spatial reasoning tasks (Shortest Path Problem, Traveling Salesman Problem) and out-of-distribution real-world spatial benchmarks. Experiments across five open-source VLMs show consistent and often large improvements (e.g., InternVL2-8B from 13.5% to 40.0% on 5×5 SPP), while general VLM capabilities remain stable.

## Strengths

1. **Principled decomposition of 2D spatial reasoning.** The paper grounds its three-capability decomposition (direction, distance, localization) in coordinate-system principles (Section 3.1), offering a systematic framework rather than an ad-hoc collection of spatial tasks. This disentanglement is a distinct and reusable contribution.

2. **Large and consistent improvements across multiple VLMs on composite tasks.** The improvements are not marginal or confined to one model. For example, InternVL2-8B SPP 5×5: 13.5%→40.0% (+196% relative), ChatGLM-4V SPP 4×4: 16.5%→36.5% (+121%), MiniCPM SPP 4×4: 17.0%→31.5% (+46%). These gains on tasks never seen during Sparkle training provide direct evidence for the core claim.

3. **Generalization to out-of-distribution real-world benchmarks.** Synthetic training with simplified diagrams transfers to photographic benchmarks: LLaVA1.6 improves from 12.6%→40.9% on GQA-Spatial (1Obj) and 6.0%→14.4% on COCO-Spatial (2Obj). This demonstrates that the learned capabilities are not brittle or tied to the training distribution.

4. **Fully synthetic, scalable data generation.** The framework generates 34K instruction-answer pairs from 2,000 coordinate configurations (Section 4.1) without manual annotation, enabling controlled experiments on data composition and scale.

5. **Ablation studies isolating contributions of each component.** Figure 4 compares full Sparkle against single-capability variants and a version without numerical information. Full Sparkle consistently wins or ties for best, while "w/o Num" underperforms on distance-heavy tasks, confirming that all three capabilities matter.

6. **No degradation on standard VLM benchmarks.** Table 2 shows that general capabilities (MMBench, ScienceQA-IMG, TextVQA) are preserved after Sparkle fine-tuning, a practical advantage for downstream use.

7. **Analysis of training sample size revealing task-specific sweet spots.** Figure 5 shows that beyond ~800 samples, TSP performance degrades—a non-obvious finding with practical implications for data collection strategies.

## Weaknesses

### Fatal
None.

### Major

1. **Evaluation metric for composite tasks (SPP, TSP) is critically underspecified.** The paper says it "report[s] accuracy as the evaluation metric" (Section 5.1) and that the model's output is "evaluated against the true shortest path" / "evaluated against the ground truth solution" (Section 3.3), but it never states whether this is *exact sequence match* or *optimality-based comparison* (e.g., accepting any shortest path of equal length, or reporting optimality gap). For both SPP and TSP, multiple optimal solutions exist (different shortest paths, different optimal tours). If the metric is exact match against a single ground-truth solution, any correct-but-different optimal output is counted as wrong, which would severely deflate and misrepresent the reported accuracy numbers. Because the accuracy values in Table 1 are the paper's primary evidence, and the evaluation protocol is not specified, the main results for SPP and TSP are uninterpretable as reported. This must be clarified; if exact match was used, the results need to be recomputed with an appropriate metric.

2. **Missing baseline weakens the central claim about the decomposition's value.** The paper's hypothesis is that mastering *basic* spatial capabilities elicits generalization to composite tasks. To support the stronger claim that the *decomposition into basic capabilities* is what drives the improvement (rather than simply any additional spatial training), a critical control is missing: fine-tuning the same VLMs on composite task examples (SPP/TSP data) directly, or on a generic spatial dataset, and comparing to Sparkle. The existing ablations compare only Sparkle variants. Without this comparison, the evidence supports the claim that "spatial training helps composite tasks" but does not fully support the claim that "mastering *decomposed basic* capabilities is the key mechanism." This limits the contribution's distinctiveness.

### Minor

1. **Internal editorial notes left in the paper.** Lines 136 and 250–254 contain unprocessed comments (`\zdy{Agreed with zhaofeng...}`, `\wzk{...}`) that are clearly draft annotations. While not a fatal flaw, this suggests the manuscript is not camera-ready and raises a minor concern about the thoroughness of the presentation.

2. **Several Δ entries show "—" with no explanation.** In Table 1, some relative improvement entries are blank/missing (e.g., LLaVA on SPP 5Grid, Qwen-VL on SPP 4Grid and 5Grid). The likely reason (zero baseline → division by zero) should be explicitly stated, and the convention explained in the caption or a footnote.

3. **Distribution of instruction types is stated but not justified.** Section 5.1 reports 3 direction, 7 distance, 6 localization instruction types with no rationale. If these proportions were chosen heuristically, a brief justification would help; if they were tuned, that should be noted.

4. **Some gains on near-ceiling general benchmarks are very small.** For InternVL2 on GQA-Spatial 1Obj (97.5→98.0, +0.5pp) and COCO-Spatial 1Obj (92.5→93.0, +0.5pp), the improvements are marginal. These cases are at or near ceiling, so they don't weaken the overall pattern, but the paper should acknowledge them rather than presenting all gains as uniform.

### Trivial
- The notation `Δ` in Table 1 could be more clearly described (e.g., absolute improvement vs. relative improvement; the caption says "percentage of relative improvement" which is clear).

## Nice-to-Haves
- Reporting standard deviations or bootstrapped confidence intervals for the 200-sample test sets would strengthen credibility.
- More training details (number of steps, warmup schedule, stopping criterion) beyond LoRA rank, learning rate, and batch size.
- A discussion of the limitations of the three-capability decomposition—e.g., whether angle understanding, scale invariance, or other capabilities could also be considered "basic."

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Claim that notation (G, V_T, P_spp) is "never fully defined."** The paper explicitly defines G as "a data generator" (line 145), V_T(P) as a "visual representation function" (line 147), and P_spp as a "predefined prompt template" (line 185). While the definitions are informal, they are present. This criticism overstates the problem.

2. **Criticism that formal notation is "mostly unnecessary."** This is a stylistic judgment about presentation that does not affect the paper's scientific validity. The notation, while perhaps not essential, serves to make the data generation pipeline precise. This is a formatting/style preference, not a weakness.

3. **Speculation that the metric "may be" exact match and "would" deflate numbers.** The reviewer correctly identifies that the metric is underspecified—this is kept as Major Weakness #1. However, the speculation that it *is* exact-match and *therefore* the numbers are wrong goes beyond what can be verified from the paper. The weakness is the underspecification, not a proven error. The retained weakness captures this fairly.

4. **Criticism that gains on GQA-Spatial 1Obj (+0.5% for InternVL2) "weakens the generalizability narrative."** The paper is transparent about these results, and the near-ceiling explanation (97.5% baseline) is a straightforward interpretation. This does not represent a weakness in the method.

## Novel Insights

None beyond the paper's own contributions. The key finding—that training on three basic decomposed spatial capabilities yields substantial gains on composite tasks like SPP and TSP—is the paper's own contribution, not a novel synthesis from the reviews.

## Suggestions

1. **Clarify the composite-task metric explicitly.** State in Section 5.1 whether accuracy is based on exact path/tour match, path length optimality (e.g., accept any path of minimal length), or optimality gap. If exact match was used, recompute results using an appropriate equivalence-class metric.
2. **Add at least one baseline where the same VLMs are fine-tuned on composite task data (SPP/TSP examples) directly.** This would significantly strengthen the claim that the decomposition into basic capabilities drives the improvement, rather than generic spatial training.
3. **Remove all internal editorial comments (\zdy, \wzk) before publication.**
4. **Explain the "—" entries in Table 1** (e.g., footnote: "Δ is undefined when baseline accuracy is 0").
5. **Briefly justify the instruction-type proportions** (3 direction, 7 distance, 6 localization) or note that they were chosen heuristically.

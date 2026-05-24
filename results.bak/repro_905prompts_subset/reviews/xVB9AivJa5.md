Now I have sufficient calibration. Let me write the final review.

## Summary

Blueprint-Bench introduces a benchmark for evaluating spatial intelligence by asking AI models to convert apartment photographs into 2D floor plans. The paper tests LLMs, image generation models, and agent systems on 50 apartments with ~20 interior photos each, scoring generated plans against ground-truth floor plans using a composite similarity metric based on room connectivity graphs and size rankings. The central finding — that most models perform near or below a baseline generated without image input, while humans substantially outperform them — reveals a real blind spot in current AI spatial reasoning capabilities.

## Strengths

- **Novel and well-motivated benchmark task.** The idea of testing spatial reasoning by having models reconstruct floor plans from photographs is genuinely creative and underexplored. Unlike many benchmarks that test spatial reasoning through abstract pattern tasks (e.g., ARC), Blueprint-Bench uses in-distribution visual input (apartment photos) with an out-of-distribution output format (floor plan diagrams), creating a clean test of whether models can go beyond pattern matching to genuine spatial inference. This is a useful addition to the evaluation landscape.

- **First benchmark to numerically compare spatial intelligence across LLMs, image generation models, and agents on the same task.** As the paper notes, image generation models have not traditionally been evaluated on reasoning benchmarks, and making direct cross-architecture comparisons is a genuine contribution. The results showing that GPT-5 (LLM, 0.42) and Gemini 2.5 Pro (0.42) outperform GPT-Image (0.32) and NanoBanana (0.18) on the same metric are informative.

- **Thoughtful qualitative analysis of agent failures.** The paper's tracing of Claude Code's iterative refinement process (Figure 8), showing that the agent identifies flaws in its own output but fails to correct the underlying spatial errors, provides concrete evidence about why additional compute and scaffolding do not close the gap. This goes beyond "model X scored Y" and offers diagnostic value to the community.

- **Open-source code and honest discussion of limitations.** The code and a data sample are released. Section 2.4 directly discusses the limitations of size-based room labeling, the lack of shape scoring, and the tradeoff between rule-following and spatial intelligence — this transparency is valuable for anyone building on the benchmark.

## Weaknesses

### Major

- **Statistical claims are made without statistical evidence.** The paper states that some models "statistically perform better than the random baseline" (Section 3) and that other models' results are "not statistically better" — yet no statistical test, confidence interval, or p-value is reported anywhere. The error bars in Figures 5 and 7 are standard deviations, not confidence intervals of the mean. Given that the paper makes explicit statistical claims about model ordering relative to the baseline, this is a significant evidential gap. Bootstrap confidence intervals or paired tests over apartments are needed to support these claims.

### Minor

- **The "random baseline" is mislabeled.** The paper generates a baseline by having LLMs produce floor plans "without any image input" — this reflects LLM priors about typical floor plans, not random chance. The paper calls it a "random baseline" in figures and text (e.g., Figure 5: "A horizontal line at 0.279 indicates the random baseline") but a "worst-case baseline" in the methods section. This conflation is imprecise. However, note that this actually *strengthens* the paper's central claim: since the baseline already embeds structural knowledge about floor plans (room counts, typical adjacencies), it is a harder threshold to beat than a truly random graph, making the finding that models at-or-below it more, not less, striking. The naming should be corrected to "no-image baseline" or similar.

- **Scoring weights are not sensitivity-analyzed.** The six-component weighted score (50% edge overlap, 20% degree correlation, etc.) is reasonable for a connectivity-focused task, and the paper openly discusses limitations of the scoring approach. However, no analysis is provided of how model rankings would change under different weightings. Showing that the relative ordering is robust across reasonable weight variations would substantially strengthen the metric.

- **Human baseline is limited.** The human baseline comes from a single annotator on only 12 of 50 apartments. While the paper presents this as a reference point rather than a definitive measure, a single annotator cannot capture inter-human variance on a task with somewhat unusual formatting rules.

- **Dataset size and diversity characterization.** Fifty apartments is a reasonable starting point but small for a benchmark. More importantly, the paper provides no statistics on apartment diversity — distribution of room counts, areas, connectivity densities, architectural styles. Without this, readers cannot assess the scope of the benchmark's coverage.

### Trivial

- The model categorization table in Figure 5 appears to have labeling inconsistencies (Claude Code listed as "Image model" category, and several models that are LLMs are also listed as "Image model" rather than "LLM"). This should be corrected for clarity.

## Nice-to-Haves

- A prompted-based sensitivity analysis (testing 2-3 prompt formulations per model on a subset) would help disentangle instruction-following ability from spatial intelligence — the paper acknowledges this confound but does not measure it.
- Reporting rule-compliance rates (e.g., fraction of outputs with valid red dots, green doors, white backgrounds) separately from the spatial score would help the community understand whether improvements on the benchmark come from better instruction-following or better spatial reasoning.
- An ablation on the number of input images (5 vs. 10 vs. all 20) could illuminate whether models are using multiple views or relying on priors.

## Removed Points

- **"Confounded comparison across model types"** (Harsh Critic #4): REMOVED. Different model types necessarily have different interfaces (SVG for LLMs, direct generation for image models, Docker for agents). This is inherent to comparing heterogeneous model families on a single task, and the paper is transparent about the procedures. This is a feature of cross-architecture benchmarking, not a flaw.
- **Weakness about missing related works**: REMOVED per instructions (cannot verify completeness without external sources).
- **Weakness about appendix-deferred content**: REMOVED per instructions (appendix content exists in original submission).
- Various generic/superficial strength claims from the Strength Finder were merged or removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Replace the phrase "statistically perform better" with actual statistical comparisons — bootstrap confidence intervals over the 50 apartments for each model vs. the baseline would be straightforward and address the most significant weakness.
2. Rename the "random baseline" to "no-image baseline" throughout — this is both more accurate and actually makes the findings more compelling.
3. Add a short sensitivity analysis for the scoring weights in the appendix (e.g., vary weights ±15% and report rank correlations).
4. Include basic dataset diversity statistics (room count distribution, apartment area range, etc.).

## Score and Decision

**Round 1 bracket:** I first bracketed by querying for similar spatial-reasoning benchmarks in three bands (0–3.5, 3.5–7.5, 7.5+). The weak band returned papers scoring 2–3 (e.g., "Exploring and Benchmarking Planning Capabilities of LLMs" at 2.0). The mid band returned papers including "Does Spatial Cognition Emerge in Frontier Models?" (SPACE, 6.75), "FoREST" (4.25), and "On Inherent 3D Reasoning of VLMs" (4.0). The strong band returned papers at 8.0 (e.g., PhysBench). This established the plausible bracket as 4.0–6.5.

**Round 2 narrowing:** I queried inside (3.0, 5.5) and (5.5, 7.0) for spatial benchmarks. Key anchors:
- STBench (5.75): larger scale (13 tasks, 60K QA), more rigorous, rejected. Blueprint-Bench is weaker.
- ReForm-Eval (5.00): scores 3,5,6,6, rejected. Blueprint-Bench is comparable in quality.
- vVLM (5.00): scores 8,3,6,3, rejected. Comparable.
- GeoMath (4.67): scores 6,5,3, rejected. Blueprint-Bench is slightly stronger.

The 6.0+ anchors (SPACE at 6.75, 3D-PC at 6.67) are clearly stronger: more tasks, more rigorous statistical methodology, deeper analysis. The 4.0–4.25 anchors (3D Indoor Layout, FoREST) have similar methodological concerns. Blueprint-Bench sits above these due to its genuinely novel task design and cross-architecture contributions, but below the 6+ papers due to weaker statistical rigor and smaller scale.

**Final score: 5.0**. The core idea is strong and useful to the community, but the paper needs to address the statistical evidence gap and clean up the baseline terminology before it reaches the quality level of the accepted spatial-benchmark papers.

**Anchors consulted:**
| Path | Score | Round | Comparison |
|------|-------|-------|-----------|
| JQbqaQjV7D (Traffic Incident) | 3.00 | R1 | Weaker — less novel task, poorer presentation |
| BVACdtrPsh (MCTBench) | 3.00 | R1 | Weaker — less focused contribution |
| DYXl6P70aH (Remote Sensing) | 3.00 | R1 | Weaker — standard benchmark scope |
| koza5fePTs (Planning) | 2.00 | R1 | Much weaker — lacks clear evaluation |
| WK6K1FMEQ1 (SPACE) | 6.75 | R1,R2 | Stronger — larger scale, more rigorous, accepted |
| uBhqll8pw1 (3D Indoor Layout) | 4.00 | R1,R2 | Similar quality but narrower scope, rejected |
| 9Y6QWwQhF3 (FoREST) | 4.25 | R1,R2 | Similar rigor level, less novel task, rejected |
| t1LfiWCYux (Depth/Height) | 4.00 | R1 | Comparable quality, different task |
| oecFal31WP (STBench) | 5.75 | R2 | Stronger — larger scale, rejected |
| ZuYvrjh2od (ReForm-Eval) | 5.00 | R2 | Comparable, rejected |
| lCqNxBGPp5 (vVLM) | 5.00 | R2 | Comparable, rejected |
| i3aFjkfnXO (GeoMath) | 4.67 | R2 | Slightly weaker, rejected |

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
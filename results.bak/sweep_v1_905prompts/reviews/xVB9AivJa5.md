Now let me write the consolidated review.

## Summary

Blueprint-Bench introduces a benchmark that evaluates spatial intelligence in AI models by requiring them to convert apartment photographs into structured 2D floor plans. The key contribution is a unified scoring framework that allows comparison across LLMs (via SVG output), image generation models (direct image output), and agent systems on the same spatial reasoning task. Evaluations of 12 models across 50 apartments find that all models substantially underperform humans (human mean 0.547 vs. best model 0.42), and agent-based iterative refinement does not meaningfully improve performance over single-pass generation. The benchmark is motivated by the ARC-like goal of exposing a "blind spot" in models using in-distribution input (photos) for a task (floor-plan reconstruction) they were not explicitly trained for.

## Strengths

- **Novel cross-architecture comparison on a unified spatial reasoning task.** The paper enables the first direct numerical comparison between LLMs, image generation models, and agent systems on the same spatial intelligence task — a genuine gap in existing benchmarks. The paper explicitly motivates this contribution and implements a pipeline that allows each model type to participate (SVG for LLMs, direct image for image models, Docker environments for agents).

- **Well-motivated task design that uses in-distribution input to probe an under-explored capability.** Unlike ARC (out-of-distribution grid patterns), Blueprint-Bench uses apartment photographs that are in-distribution for multimodal models, testing whether spatial reconstruction ability emerges without explicit training. This design choice is clearly articulated and distinguishes the benchmark from existing spatial reasoning evaluations.

- **Rule-based extraction pipeline avoids unreliable LLM-based evaluation.** The paper documents (Section 2.4) that initial attempts using LLMs for floor-plan extraction failed due to hallucinated connections and biased room-size priors. The adopted CV pipeline (HSV filtering, flood-fill segmentation, door detection) is algorithmically deterministic, reproducible, and transparent.

- **Controlled agent experiment suggests the limitation is not only a lack of iterative feedback.** The agent setup (Docker environment with file access and revision capability) directly tests whether poor single-pass performance can be overcome by iterative refinement. The finding that Claude Code's iterative refinement still did not produce statistically better results than the random baseline, and that Codex rarely revised at all, is an interesting result that rules out a straightforward counter-hypothesis.

- **Transparency about limitations.** Section 2.4 openly discusses the tradeoff between rule strictness and expressiveness, the absence of room-type labeling, the decision to not use shape-based scoring, and the conflation of spatial intelligence with instruction following. This candor is valuable for the community using the benchmark.

## Weaknesses

### Major

- **The central claim about the random baseline is contradicted by the paper's own data.** The abstract states "most models perform at or below a random baseline" and the results section reiterates "most do not outperform the random baseline." However, Figure 5 shows 10 out of 12 models scoring *above* the random baseline (0.279), several by a large margin (GPT-5 at 0.42, Gemini 2.5 Pro at 0.42, Grok 4 at 0.40). Only GPT-4o (0.15) and NanoBanana (0.18) are below. The text acknowledges that four models "statistically perform better" but still asserts "most do not outperform" — this is inconsistent with the plotted data. No p-values, confidence intervals, or statistical test details are provided to support the "statistically better" claim, making this unverifiable. This overstatement undermines confidence in how the paper characterizes its results.

- **The scoring metric conflates spatial intelligence with instruction following in an unresolved way.** The paper acknowledges this tradeoff (Section 2.4: "Blueprint-Bench should test spatial intelligence, not instruction following") but does not resolve it. The scoring pipeline requires strict adherence to nine formatting rules (3px black walls, red dots, green doors, no furniture, etc.), and models that violate these rules (NanoBanana, GPT-4o) receive low scores attributed to "poor instruction following" — yet these low scores appear in the same aggregate comparisons as spatial reasoning scores. This means a model with good spatial understanding but poor formatting compliance would score lower than a model with poor spatial understanding but good formatting. The paper's justification that "at current model capabilities, we think this is the right tradeoff" does not establish metric validity. Separating a formatting-compliance score from a spatial-overlap score would substantially strengthen the benchmark.

- **The test set (50 apartments) and human baseline (12 apartments) are too small for strong claims.** A benchmark aiming to measure a fundamental capability like spatial intelligence should rest on a larger foundation. The human baseline uses only 12 of the 50 apartments, with no information provided about the number of human participants, their backgrounds, or the time they were given. Given the error bars in Figure 7, the human baseline's reliability is unclear. For comparison, the related SPACE benchmark (6.75 avg score) evaluates on 15 tasks with 30–100+ questions per task, and the 3D-PC benchmark tests 33 human participants across carefully controlled conditions.

- **The weighted scoring components lack justification and sensitivity analysis.** The composite score weights (50% edge overlap, 20% degree correlation, 10% density, 10% room count, 5% door count, 5% door orientation) are presented without any rationale or sensitivity analysis. A benchmark where model rankings could flip under reasonable alternative weightings would be fragile. At minimum, the paper should show that alternative weightings (e.g., uniform weights, leave-one-component-out) do not change the qualitative ordering of models, or acknowledge where rankings are weight-dependent.

### Minor

- **The "random baseline" is not truly random.** The baseline is generated by feeding models the same prompt *without images*, which produces outputs reflecting the models' priors about typical floor plans rather than random connectivity graphs. A genuinely random baseline (random graphs with matched expected room counts) would provide a more meaningful floor. The paper calls it a "worst-case baseline" in text but labels it "Random" in figures, which is somewhat misleading.

- **The CV-based extraction pipeline introduces potential fragility.** The flood-fill segmentation and door detection depend on exact rule adherence (3px walls, no gaps). Small formatting violations (e.g., a 1-pixel wall gap from anti-aliasing) could cause cascading errors in room connectivity detection. The paper claims "any submission that adheres to these rules can robustly be scored," but adherence is not binary — partial violations could produce scoring noise that is indistinguishable from poor spatial reasoning. A validation of the pipeline's robustness (e.g., injecting small perturbations into ground-truth images and measuring score degradation) would be informative.

- **Rule 9 ("include walking closets, ignore wardrobes") introduces a subjective boundary.** The distinction between a walk-in closet and a wardrobe requires real-world knowledge that models may not possess, and even ground-truth annotators may disagree on. The paper does not describe how ground-truth labels were constructed for this edge case.

- **No statistical details for per-model comparisons.** The paper states that some models "statistically perform better than the random baseline" but does not report the test used, p-values, or whether multiple-comparison correction was applied. It is also unclear how many epochs/attempts per apartment were used and whether the reported means average over multiple runs.

## Nice-to-Haves

- Compute and report separate formatting-compliance and spatial-overlap scores, allowing the community to disentangle these two capabilities.
- Provide a sensitivity analysis for the scoring weights (uniform weights, leave-one-out).
- Expand the human baseline to more apartments (ideally all 50) with sufficient participants and report participant details.
- Add a graph-theoretic random baseline (random connectivity graphs with matched room counts) to complement the no-image baseline.
- Analyze agent traces systematically: how often did agents revise, did revisions improve scores, what was the distribution of revision counts?

## Removed Points

- "The analogy to ARC is overclaimed" — This is the paper's own framing; it does not claim equivalence, only similarity in exposing a blind spot. No factual error.
- "Figure 8 shows only one apartment" — The figure is a qualitative illustration of agent behavior, which is standard. A systematic analysis would strengthen the paper but the absence is not a weakness.
- "The paper dismisses LLM-based extraction too quickly" — The paper provides concrete reasons with examples (hallucinated connections, biased priors). This is a justified methodological decision, not a weakness.
- "The conclusion wording should be more precise" — Style preference, not a substantive weakness.
- Various formatting and style nitpicks (typos, grammar, presentation) — These are not present in the original submission; they are parser artifacts.

## Novel Insights

An interesting observation emerges from connecting the paper's two main negative findings. Models fail at floor-plan reconstruction from photos, yet they also fail to improve when given full agentic ability to iteratively view images, draw, check, and revise. The agent trace (Figure 8) reveals a specific failure pattern: the model identifies the correct number of rooms and their approximate layout in early iterations, but repeatedly fails at structural enclosure (rooms not fully walled, gaps between rooms). This suggests the bottleneck is not in identifying "what rooms exist" or "roughly where they go" — the bottleneck is in enforcing a globally consistent wall topology with no gaps. This is precisely the kind of constraint that transformer-based architectures operating on patch-level representations might systematically fail at, because it requires pixel-level geometric closure that is neither a natural output of next-token prediction nor of diffusion-based generation. The combination of the benchmark design and the agent trace thus hints at a more specific diagnosis than "models lack spatial intelligence": models may lack the ability to generate outputs that satisfy hard geometric constraints (wall continuity, complete enclosure) while maintaining relational accuracy (room connectivity, size ordering). This could be tested by ablating the constraint difficulty (e.g., allowing overlapping walls or soft boundaries) and measuring whether performance improves.

## Suggestions

1. **Separate formatting compliance from spatial accuracy** into two reported scores, or pre-process outputs to normalize formatting before spatial scoring. This is the single highest-leverage fix for the paper.
2. **Correct the misleading claim** about "most models at or below baseline." Either report statistical significance properly with p-values and confidence intervals, or revise the text to accurately reflect that most models numerically exceed the baseline (even if many do not reach statistical significance with the current sample size).
3. **Report statistical rigor details**: number of epochs per apartment, number of human participants, statistical test used for "statistically better" claims, and multiple-comparison correction.
4. **Add a sensitivity analysis** for the scoring weights and validate against human similarity judgments.
5. **Add a graph-theoretic random baseline** (random graphs matched for room count) to establish a true chance floor.

## Score and Decision

### Calibration Procedure

**Round 1 (Bracketing).** Searched for spatial reasoning benchmarks in three bands:
- Low band (scores < 3.5): Found anchors including "Exploring and Benchmarking Planning Capabilities of LLMs" (2.00), "MCTBench" (3.00) — papers with fundamental task design issues.
- Mid band (3.5–7.0): Found anchors including **SPACE** (6.75, Accept), **3D-PC** (6.67, Accept), **FoREST** (4.25, Reject), **ET-Plan-Bench** (4.50, Reject), **"On Inherent 3D Reasoning"** (4.00, Reject).
- High band (7.0+): Found **PhysBench** (8.00), **MathVista** (7.25) — comprehensive, large-scale benchmarks beyond Blueprint-Bench's scope.

**Initial bracket:** 4.0–6.75. Blueprint-Bench is clearly stronger than the 4.00 papers (which had task-validity issues) and weaker than SPACE (6.75, which is more comprehensive with 15 tasks grounded in cognitive science).

**Round 2 (Narrowing).** Searched within the bracket:
- Lower sub-bracket (3.5–5.5): Anchors at 4.00, 4.25, 4.50. These papers were rejected for overclaiming, limited scope, insufficient rigor.
- Upper sub-bracket (5.5–7.5): **SPACE** (6.75), **3D-PC** (6.67), **DivScene** (6.25), **PARTNR** (7.00). These papers demonstrated stronger evaluation rigor, larger datasets, and clearer task validation.

**Final calibration:** Blueprint-Bench is above the 4.00–4.50 papers (which had more fundamental validity issues) because its task is clearly defined, motivated, and yields interesting comparative results. However, it is below the 6.5+ papers in terms of evaluation rigor, dataset size, and validation of the scoring metric. The unresolved metric confound, the overclaimed baseline result, and the small human baseline place it in the lower portion of the mid range.

**All anchors considered:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| Planning Capabilities of LLMs | 2.00 | R1 | Much weaker — fundamental task design issues |
| MCTBench | 3.00 | R1 | Weaker — less well-motivated task |
| On Inherent 3D Reasoning | 4.00 | R1 | Weaker — task validity concerns, overclaiming "3D" |
| FoREST | 4.25 | R1 | Comparable but narrower focus |
| ET-Plan-Bench | 4.50 | R1 | Comparable — similar scope but different domain |
| DivScene | 6.25 | R2 | Stronger — much larger dataset, broader evaluation |
| 3D-PC | 6.67 | R2 | Stronger — better experimental control, human testing |
| SPACE | 6.75 | R1 | Stronger — more comprehensive, cognitive science grounding |

**Score:** 5.0  
**Decision:** Reject

The paper introduces a genuinely useful benchmark and makes several interesting findings (cross-architecture comparison, agent ineffectiveness). However, the metric confound between formatting compliance and spatial intelligence, the overclaimed baseline result, the small human baseline, and the lack of weight sensitivity analysis are significant enough to recommend rejection with encouragement for major revision. If the authors address these issues — particularly decoupling the scoring dimensions, correcting the baseline claim with proper statistical reporting, and expanding the human baseline — the benchmark could become a valuable community resource.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
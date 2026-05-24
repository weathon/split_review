Now I have a thorough picture of the paper and all calibration anchors. Let me write the consolidated review.

---

## Summary

Blueprint-Bench introduces a benchmark for evaluating spatial intelligence in AI models through the task of reconstructing 2D floor plans from apartment photographs. The benchmark evaluates LLMs (via SVG generation), image generation models, and AI agents on 50 apartments, scoring outputs against ground truth using room connectivity graphs and size rankings. Results show all models substantially below human performance, with agents providing no benefit over single-pass generation despite having iterative refinement capabilities.

## Strengths

- **Creative and well-motivated task**: Using floor plan reconstruction from real photographs as a probe for spatial reasoning is genuinely novel. The task requires models to infer room layouts, connectivity, and scale — capabilities that are central to spatial intelligence — while using an input modality (photographs) that is well within the training distribution of modern multimodal models. This design creates a compelling "in-distribution input, out-of-distribution task" setup that parallels the motivation behind ARC.

- **Cross-architecture comparison**: The benchmark evaluates three fundamentally different model types (LLMs generating SVG, image generation models producing pixels directly, and agent scaffolds with tool use) on a single standardized task. This enables direct numerical comparison of spatial reasoning across architectures, which the paper correctly identifies as a gap in current evaluation practice (Section 1, paragraph 4).

- **Transparent discussion of limitations**: The paper dedicates an entire section (2.4) to discussing the limitations of its scoring approach — including the size-ranking cascade penalty, the absence of room-shape scoring, and the instruction-following confound for image models. It also describes alternative approaches that were tried and why they were not adopted. This level of transparency is commendable and allows readers to calibrate their interpretation of results.

- **Agent analysis provides concrete evidence**: The Claude Code trace in Figure 8 shows an agent iteratively correcting its floor plan across three revisions yet still producing a flawed output, providing qualitative evidence that iterative refinement does not overcome the underlying spatial reasoning deficit. This goes beyond aggregate scores to illustrate failure modes.

- **Open-source and community-facing**: The paper releases code, a dataset sample, and maintains a public leaderboard (Reproducibility Statement, Section 2.2), enabling external validation and tracking of progress over time.

## Weaknesses

### Fatal

None.

### Major

- **Scoring metric captures only a subset of spatial intelligence, yet the paper frames results as measuring "spatial intelligence" broadly**: The similarity score is computed from connectivity graphs and size rankings only (Section 2.3). Room shape, absolute position, orientation, and geometric accuracy are not measured at all — two floor plans with identical connectivity and size ordering but completely different room arrangements (e.g., mirror images, rooms rearranged in a line) would receive a perfect score. The paper acknowledges this in Section 2.4 ("does not account for the shape of the room") but does not reconcile the gap between its broad framing (the title promises "comparing spatial intelligence") and the narrow metric. This is a structural limitation of the benchmark that cannot be fixed by additional experiments — it requires redesigning the scoring. It matters because the headline results (models perform poorly, humans outperform) could look quite different under a metric that actually rewards geometric accuracy.

- **Human baseline is too thin to support the paper's central comparative claim**: The human baseline uses only 12 of 50 apartments (Figure 7), the number of human subjects is not reported (the paper uses the singular "a human" in Section 2.2), and their instructions and qualifications are not described. The paper's key result — that humans substantially outperform all models — rests on a single data point of 0.547 from an unspecified number of people on a small subset. This is insufficient evidence for what the paper treats as a central empirical finding.

- **Dataset documentation is minimal for a benchmark paper**: Beyond "50 apartments, each with approximately 20 images," no statistics are provided — no distribution of room counts, apartment sizes, layout complexity, or architectural styles. The process for adapting listing floor plans into rule-compliant ground truth is not described beyond listing the 9 rules themselves. Readers cannot assess whether the benchmark covers a representative range of spatial reasoning challenges or whether difficulty is concentrated in a narrow slice of the data.

### Minor

- **The "random baseline" is misnamed**: Section 2.2 describes it as "a worst-case baseline by generating typical floor plans using LLMs and image generation models without any image input," but it is labeled as the "random baseline" throughout Figures 5 and 7 and the accompanying text. Floor plans generated by models without seeing the images are not random — they reflect architectural priors (e.g., kitchen near living room). The paper should rename this to something like "image-blind baseline" and clarify its interpretation. This does not invalidate the results but creates confusion about what "performing at or below random" actually means.

- **Scoring component weights are arbitrary**: The six similarity components are combined with weights of 50%/20%/10%/10%/5%/5% (Section 2.3) with no justification and no sensitivity analysis. Given that the paper's conclusions rest on fine score distinctions (e.g., best model at ~0.42 vs. random at ~0.28), the sensitivity of rankings to these weights matters and is unexplored.

- **Cross-modality comparison is confounded by instruction-following**: LLMs generate precise SVG code (trivially satisfying the formatting rules), while image generation models must draw pixel-perfect floor plans — a much harder instruction-following problem orthogonal to spatial reasoning. The paper acknowledges this in Section 2.4 but treats it as an acceptable tradeoff. Scores for NanoBanana (0.18) and GPT-4o (0.15) likely reflect instruction-following failure rather than spatial reasoning ability, as the paper itself notes (Section 3). This means the cross-modality ranking is not a clean comparison of spatial intelligence.

- **The size-ranking cascade penalty limits the benchmark's discriminative power**: As the paper acknowledges (Section 2.4), a single mistake in room size ordering causes all downstream connectivity comparisons to be misaligned, conflating size estimation errors with connectivity errors. This means the benchmark cannot distinguish between a model that understands room adjacency perfectly but mis-estimates one room's size, and a model that understands neither. The human baseline illustrates this: all human floor plans had correct connectivity, but the human score was only 0.547 due to size-ranking penalties (Section 3, Figure 7 discussion).

### Trivial

- The number of repeated runs ("epochs") per model per apartment is not specified, making the error bars in Figure 5 uninterpretable.
- Model names in the appendix figures (Claude 4.5, Claude 3.5 Sonnet, etc.) are inconsistent with the main paper's naming convention, suggesting a draft error.

## Nice-to-Haves

- Replacing the size-ranked room alignment with optimal matching (e.g., Hungarian algorithm on spatial proximity of room centroids) would decouple connectivity scoring from size estimation errors, a change the authors nearly propose themselves in Section 2.4.
- A qualitative error taxonomy (connectivity errors vs. size errors vs. instruction-following failures) would help readers understand what the benchmark is actually measuring and would make the results more actionable.
- The agent setup is underspecified (max steps, tool availability, exact prompts); providing these details would enable reproduction and fair comparison by future work.

## Removed Points

*These points were flagged by one or more input reviewers but are removed from the final review with justification.*

- **"The paper never acknowledges that the benchmark may reward non-spatial heuristics"** — REMOVED. The paper explicitly discusses this in Section 2.4: "Another limitation of our scoring method is that it does not account for the shape of the room." It also discusses attempts to add shape-based scoring and why they were not included. The paper is transparent about what the metric captures and what it doesn't.

- **"The random baseline inflates apparent difficulty — models may perform above true chance"** — REMOVED as a standalone weakness. The direction of effect in the harsh critic's argument is unclear (a baseline with architectural priors likely scores higher than true random, narrowing the gap from models, not inflating it). The real issue (misleading naming) is retained as a Minor weakness.

- **"Floor plans generated without image input are not random — they reflect strong architectural priors"** — Merged into the Minor weakness about baseline naming. The paper is transparent about how the baseline was constructed.

- **"The claimed first numerical framework for comparing spatial intelligence across different model architectures is overstated"** — REMOVED. The paper's contribution is genuinely novel: no existing benchmark evaluates LLMs, image models, and agents on the same spatial reasoning task with a common numerical score. The SPACE benchmark (the closest comparator) evaluates LLMs and VLMs but not image generation models on a common task.

- **"Comparison across model modalities is confounded — image models struggle with instruction following, not spatial reasoning"** — Retained as a Minor weakness but significantly weakened from the harsh critic's framing. The paper explicitly acknowledges this confound in Section 2.4 and argues it is the right tradeoff at current capability levels.

- **"Pure formatting/style nitpicks" about typos and parser artifacts** — REMOVED per hard rules. The appendix model name inconsistency is retained only because it suggests a genuine content error (inconsistent model naming between main text and appendix figures), not a formatting artifact.

- **"The agent prompt and environment constraints are underspecified — making evaluation unreproducible"** — Moved to Nice-to-Haves. The paper describes the setup at a high level (Docker container, images in folder, agent asked to save at a specific path); more detail would help reproduction but this is standard for agent benchmark papers.

- **"No analysis of why some LLMs outperform others, or what kinds of spatial errors they make"** — Moved to Nice-to-Haves as a qualitative error taxonomy suggestion. This would strengthen the paper but its absence does not invalidate the results.

- **Strength about "well-defined benchmark with automated scoring"** — Retained with qualification. The scoring is automated and rule-based, but "well-defined" is overstated given the missing dataset statistics and arbitrary weights.

- **Strength about "comprehensive evaluation across diverse model architectures"** — Retained. The model coverage is genuinely broad.

- **Strength about "open-source and community-facing"** — Retained. This is a concrete, verifiable contribution.

- **Strength about "model-agnostic participation criteria"** — Removed as it is essentially the same point as model-agnostic design, already covered.

## Novel Insights

The review process highlights a tension that the paper itself partially surfaces: the benchmark's strict formatting rules (9 precise requirements for wall thickness, dot size, colors) were designed to make scoring robust, but they inadvertently create a modality-asymmetric barrier — LLMs can satisfy them trivially through SVG code generation while image models must solve a difficult instruction-following problem. This means Blueprint-Bench, at current capability levels, functions more as a joint test of spatial reasoning + instruction following for image models versus spatial reasoning + code generation for LLMs. The paper acknowledges this but does not resolve it. Future iterations of cross-modality spatial benchmarks will need to find evaluation protocols that hold instruction-following difficulty constant across modalities — perhaps by allowing image models to receive the formatting rules as a reference image rather than as text instructions, or by scoring outputs more leniently on formatting and more strictly on spatial accuracy.

## Suggestions

- **Redesign or augment the scoring metric** to include at least one geometric component (e.g., Hungarian-matched room centroid distances, or room overlap IoU after optimal alignment). This is the single change that would most improve the benchmark's validity as a measure of spatial intelligence. The paper already experimented with Chamfer-like wall sampling and rejected it; simpler geometric measures like centroid distance may avoid the brittleness problem while still capturing whether rooms are in the right places.

- **Expand and document the human baseline**: run it on all 50 apartments with multiple subjects (at least 3–5), report variance, and describe subject qualifications and instructions. This is essential for the paper's central claim about the human-AI gap.

- **Add basic dataset statistics**: histogram of room counts per apartment, distribution of apartment sizes (in rooms), examples of simple vs. complex layouts. This is standard for benchmark papers and lets readers assess difficulty and coverage.

- **Rename the "random baseline"** to "image-blind baseline" or "no-input baseline" to accurately reflect its construction. Consider adding a true random baseline (e.g., random connectivity graphs matched to the ground-truth room count distribution) as a supplementary reference point.

- **Report per-component scores** (edge overlap, degree correlation, size ranking separately) rather than only the weighted composite, so readers can see whether models fail on connectivity, size estimation, or both.

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| SPACE (WK6K1FMEQ1) — spatial cognition benchmark for frontier models | 6.75 | 1 | Stronger: more comprehensive tasks, better grounded in cognitive science, cleaner methodology. Blueprint-Bench has a more creative task but weaker execution. |
| FoREST (9Y6QWwQhF3) — spatial FoR benchmark for LLMs | 4.25 | 1 | Blueprint-Bench is stronger: real-world data rather than synthetic templates, broader model coverage, more compelling task. |
| On Inherent 3D Reasoning (uBhqll8pw1) — VLM spatial reasoning | 4.00 | 1 | Blueprint-Bench is stronger: more coherent task design, better scope definition, open-source code. |
| Labyrinth of Links (vJ0axKTh7t) — MLLM association benchmark | 6.25 | 2 | Somewhat stronger: cleaner methodology, better dataset documentation. Blueprint-Bench has a more novel cross-modality angle but weaker execution. |
| ET-Plan-Bench (UiLtbLsiPU) — embodied task planning benchmark | 4.50 | 2 | Blueprint-Bench is stronger: clearer task, more transparent limitations discussion, better cross-model coverage. |
| SR² (2seVGyWZOX) — spatial relation reasoning | 5.20 | 2 | Comparable in quality; SR² has a method contribution, Blueprint-Bench is benchmark-only. |
| GridAgent (jpypMKAsO6) — MLLM grid benchmark | 5.67 | 2 | Slightly stronger: more systematic evaluation design. |

**Round 1 Bracket:** The paper sits between 4.5 and 6.5 — clearly stronger than the rejected FoREST/ET-Plan-Bench, clearly weaker than the accepted SPACE.

**Round 2 Narrowing:** Within the 4.5–6.0 sub-range, Blueprint-Bench is comparable to SR² (5.20) and somewhat weaker than GridAgent (5.67) and Labyrinth of Links (6.25). The core differentiator is methodological rigor: Blueprint-Bench has a genuinely creative and well-motivated task, but the scoring metric limitations, thin human baseline, and missing dataset documentation pull it below the acceptance line.

**Final Score: 5.0**

The paper introduces a creative, well-motivated benchmark with a genuinely novel cross-architecture angle. The open-source release and leaderboard are valuable. However, multiple methodological weaknesses — the scoring metric captures only a narrow slice of spatial intelligence, the human baseline is too thin to support the central comparative claim, and dataset documentation is insufficient — prevent the paper from crossing the acceptance threshold in its current form. These are addressable issues (none are fatal), but they collectively weaken the evidence for the paper's claims enough that the paper falls below the bar. The paper would be considerably strengthened by augmenting the scoring metric with a geometric component, expanding and documenting the human baseline, and providing basic dataset statistics.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
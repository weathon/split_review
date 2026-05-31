Now let me do the calibration search to score the paper.Initial bracket: **4.0 – 6.0**. Blueprint-Bench is thematically similar to the middle-band anchors. Let me narrow with a round-2 search.Now let me read the SPACE paper (6.75) and indoor VLM paper (4.0) to calibrate more precisely.Now I have enough information to write the final consolidated review.

---

## Summary

Blueprint-Bench is a benchmark for evaluating spatial reasoning in AI systems via a single task: reconstructing 2D floor plans from apartment interior photographs. The paper evaluates leading LLMs, image generation models, and coding agents on 50 apartments, finding that most models perform at or below a no-input baseline while a human substantially outperforms all models. The benchmark's key novel angle is its model-agnostic design that enables the first side-by-side numerical comparison of spatial intelligence across LLMs, image generation models, and agent scaffolds.

---

## Strengths

- **Novel cross-architecture comparison**: The same task, inputs, and scoring protocol are applied to LLMs (GPT-5, Claude 4 Opus, Gemini 2.5 Pro, Grok-4), image generation models (GPT-Image, NanoBanana), and agent systems (Codex CLI, Claude Code). To the reviewers' knowledge, no prior benchmark performs this side-by-side numerical comparison. This is a genuine and useful contribution (Sections 1, 2.2).

- **Meaningful empirical finding with a natural input modality**: Unlike ARC, which uses alien grid inputs, Blueprint-Bench uses apartment photographs that are squarely within the training distribution of all evaluated models. Yet nearly all models score near or below the no-input baseline (Figure 5), demonstrating a crisp spatial reasoning blind spot. This framing is well-motivated and the gap between human performance (0.547) and the best model (≈0.45) on the 12-apartment subset (Figure 7) is substantial.

- **Automated, rules-based extraction avoids LLM-as-judge pitfalls**: The paper tried LLM-based extraction and found it unreliable (models hallucinated connections, mis-ranked rooms by semantic priors). Falling back to computer vision on standardized images is a pragmatic and defensible engineering decision, explained with concrete evidence (Section 2.4).

- **Open-source code + private test set + public leaderboard**: The design separates the sample/code release from the held-out test corpus, which is standard good practice for sustainable benchmarking (Section 2.2, Reproducibility Statement).

---

## Weaknesses

### Fatal
None. The benchmark has significant methodological gaps but its core direction—that frontier models fail badly at visual-to-floor-plan reconstruction—is plausible and unlikely to be reversed by addressing the issues below.

### Major

- **Size-rank cascade invalidates the primary metric's interpretation**: The benchmark assigns room IDs by area rank (largest = Room 1, etc.). Edge overlap, weighted at 50% of the composite score, then asks whether the same size-ranked rooms are connected. As the paper acknowledges in Section 2.4, "the penalty of making a mistake in the size ranking causes additional penalties when scoring the connectivity." A model that correctly identifies all rooms and their connectivity but swaps two rooms' size rankings will have its entire adjacency graph re-labeled and scored as largely incorrect. This means the headline metric does not cleanly measure "spatial layout understanding"—it conflates room topology inference with area-estimation accuracy. The paper notes that human performance would likely be much higher under a different similarity model ("We suspect that one similarity scoring model would make the human's lead over the AI models much larger," Section 3), which is an implicit admission that the metric penalizes in ways orthogonal to spatial understanding. For a benchmark paper, the central obligation is to show the metric measures what it claims; no validation of this is provided—no correlation with human judgments, no ablation showing rank errors are small or uncorrelated with topology errors.

- **Composite score weights are unjustified**: The 50/20/10/10/5/5 weighting scheme (edge overlap / degree correlation / density / room count / door count / door orientation) is stated without motivation in Section 2.3. No sensitivity analysis is provided. A different weighting could reorder model rankings relative to the no-input baseline. Because the weights define what "spatial intelligence" means numerically, this is not a cosmetic concern—it is the scientific claim. For a benchmark paper, weight choices should either be derived from principled criteria or shown to be stable across plausible alternatives.

- **"Random baseline" is actually a no-input baseline**: The paper describes the random baseline as "generating typical floor plans using LLMs and image generation models without any image input" (Section 2.2). This is a zero-context generation baseline, not a random graph sampled from the empirical distribution of apartments. The two baselines differ (0.279 all apartments, 0.322 twelve-apartment subset) and the number of runs, models used, and prompts are not specified. When the abstract and Section 3 state that "most models perform at or below a random baseline," this claim rests on an undefined comparison. A model scoring 0.32 against a 0.279 baseline from an incompletely characterized procedure is a weaker statement than it appears.

### Minor

- **"Epochs" never defined**: Figure 5 and 6 captions state scores are "averaged across epochs and apartments," but the term "epochs" is never explained. If it means multiple independent runs per apartment, the number should be stated and affects interpretation of error bars throughout.

- **Ground truth annotation process underdescribed**: Section 2.1 says floor plans are "adapted from the apartment listing's official floor plan image" using 9 formatting rules, but does not describe who performed the adaptation, how many annotators were involved, whether inter-annotator reliability was checked, or how ambiguous cases (open-plan areas, half-walls) were handled. Benchmark reliability depends on this.

- **Agent conclusions overreach the evidence**: The abstract states "agent-based approaches with iterative refinement capabilities show no meaningful improvement." Only two agents were tested. One of them—Codex CLI—explicitly did *not* use iterative refinement: "It just looked at all the images using its view_image tool and then wrote a Python script... It never even looked at the image it created before submitting" (Section 3). Only Claude Code actually iterated. Drawing a general conclusion about iterative refinement from a single agent on a single underlying model is too thin.

- **Instruction-following and spatial intelligence conflation**: The paper explicitly notes that GPT-4o and NanoBanana's low scores stem from rule non-compliance rather than spatial reasoning failure (Section 3). If a significant portion of model variance is driven by instruction following rather than spatial understanding, the benchmark's diagnostic value for spatial intelligence is reduced. The paper acknowledges this (Section 2.4) but does not quantify how much score variance is attributable to each factor.

- **Small dataset with possibly biased human subset**: The main results are on 50 apartments; the human-comparison results are on a 12-apartment subset. If these 12 were self-selected by the human (chosen for feasibility or distinctiveness), they may not represent the full distribution, creating a confound in the human–AI comparison.

### Trivial

- The "first numerical framework for comparing spatial intelligence across different model architectures" claim (abstract) is stated without a systematic survey of prior spatial reasoning benchmarks. This should either be supported with a brief comparison to existing work or qualified.

---

## Nice-to-Haves

- A correlation study between the metric score and human-ranked spatial quality on a subset of predictions would validate that the score actually tracks spatial understanding, addressing the cascade concern without new data collection.
- A brief weight-sensitivity ablation (e.g., edge-only, equal-weight, full composite) showing that model orderings are stable across plausible weight variations would substantially increase confidence in the benchmark.
- Defining and using a properly specified random baseline (random graphs within the empirical distribution of room counts and connection densities from the 50 apartments) would make the "near-random performance" claim precise.
- The agent evaluation would be much stronger with at least 3–4 agents where all are confirmed to actually perform iterative refinement, before concluding that refinement doesn't help.
- Adding a small ablation on the full 50-apartment set showing what share of score variance for low-scoring models (GPT-4o, NanoBanana) comes from rule violations vs. spatial errors would sharpen the benchmark's diagnostic interpretation.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Automated scoring avoids LLM-as-judge pitfalls" as a strength**: This was framed by the Strength Finder as an unqualified positive, but it directly conflicts with the verified cascade/weighting weaknesses. Removed per the rule that when a strength and weakness disagree, the weakness wins.

- **Potential selection bias in the 12-apartment subset inflating the gap**: The Strength Finder noted "Meaningful baselines—human performance and random—demonstrate a clear AI blind spot" as an unqualified strength, but the 12-apartment selection process is unspecified. The gap may partially reflect selection. Removed as a weakness because it is speculative (the paper doesn't describe how the 12 were chosen), but also does not stand as an unqualified strength. Kept as a Minor note above.

- **Missing related works on prior spatial reasoning benchmarks**: The harsh critic flagged this, but per hard rules, comparisons to specific missing citations are not included since we cannot confirm their existence from within the paper.

- **"Not yet released" or reproducibility concerns about cited models**: Not applicable here, but any doubt about whether GPT-5, Claude 4 Opus, Grok-4, etc. are real evaluated models is excluded per hard rules.

---

## Novel Insights

The most genuinely novel observation surfacing from these reviews is the metric cascade problem: because room IDs are assigned by area rank, every area-estimation error simultaneously corrupts the topology score. The paper acknowledges this but treats it as a minor caveat. In fact, it points toward a more interesting benchmark design: separating the area-ranking task from the connectivity task and scoring them independently would yield finer-grained diagnostics. Models could fail at topology only, at size ranking only, or at both — and current AI may fail for different reasons. The paper is implicitly measuring a compound skill without decomposing it, which obscures which architectural choices drive failure.

---

## Suggestions

1. Add a validation section showing that the composite score correlates with human-ranked spatial quality on even a small held-out set (10–20 predictions) to establish metric face validity.
2. Replace or supplement the "no-input baseline" with a properly defined random graph baseline (sample from the empirical distribution of room counts and edge densities in the dataset) so that "at-or-below-random" comparisons have statistical meaning.
3. Define "epochs" explicitly and report the number of runs per apartment throughout the paper.
4. Describe the ground-truth annotation procedure (who, how many, any inter-annotator check).
5. Either qualify the agent conclusion ("iterative refinement provides no meaningful improvement") or run additional agents that demonstrably do iterate before drawing the conclusion.
6. Provide a brief weight sensitivity ablation in the paper (or appendix) to show model orderings are not weight-dependent.

---

## Score and Decision

**Calibration summary:**

| Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| JQbqaQjV7D (LLM benchmark, traffic incidents) | 3.0 | R1 | Blueprint-Bench is better motivated and more carefully designed |
| koza5fePTs (planning benchmark) | 2.0 | R1 | Blueprint-Bench is much stronger |
| BVACdtrPsh (MCTBench multimodal) | 3.0 | R1 | Blueprint-Bench is comparable in scope but with more novel angle |
| WK6K1FMEQ1 (SPACE spatial cognition) | 6.75 | R1 | SPACE is clearly stronger: 15 tasks, cognitive science grounding, parallel text/image, larger scale — Blueprint-Bench is more limited in all dimensions |
| uBhqll8pw1 (VLMs in 3D indoor scene layout) | 4.0 | R1/R2 | Very similar profile to Blueprint-Bench: narrow spatial task, interesting VLM finding, methodological gaps, small dataset — scored 4.0 Reject |
| 9Y6QWwQhF3 (FoREST spatial reasoning) | 4.25 | R1 | Similar narrow spatial benchmark, similar score band |
| t1LfiWCYux (depth/height in VLMs) | 4.0 | R1 | Comparable benchmark scope, rejected |
| UiLtbLsiPU (ET-Plan-Bench spatial-temporal) | 4.5 | R2 | Slightly broader benchmark, similar quality |
| VeSsiD0DP9 (Curse of Multi-Modalities hallucinations) | 5.75 | R2 | More comprehensive evaluation, stronger metric design — Blueprint-Bench is below this |

**Round-1 bracket**: 4.0–6.0.

**Round-2 narrowing**: The closest comparators (uBhqll8pw1 at 4.0, FoREST at 4.25, ET-Plan-Bench at 4.5) are all narrow-scope AI spatial reasoning benchmarks with similar scale and similar weaknesses, rejected at scores of 4.0–4.5. Blueprint-Bench shares their profile: single domain, small dataset, metric validity gaps, interesting but thin empirical finding. Blueprint-Bench has a genuinely novel angle (cross-architecture comparison of LLMs vs. image generation models vs. agents) that slightly differentiates it from these anchors, but the metric validity concerns are more severe in this case (the cascade problem is a fundamental measurement issue for a benchmark paper). The SPACE benchmark (6.75), which is much more comprehensive, grounded in cognitive science, and rigorous, is clearly above the paper under review.

**Final bracket**: 4.0–4.5. Blueprint-Bench is in the same tier as the 4.0 anchors, with a slight upward nudge for the novel cross-architecture angle. Score: **4.0**.

**Axes summary:**
- *Originality*: Moderate — the cross-architecture comparison is novel; the floor plan reconstruction task is a reasonable spatial probe.
- *Importance of research question*: High — measuring spatial intelligence of generalist AI is genuinely important.
- *Claims well-supported*: Weak — the core metric has unvalidated cascade contamination; the agent generalization claim is thin.
- *Soundness of experiments*: Weak — arbitrary weights, ill-defined random baseline, small dataset.
- *Clarity of writing*: Moderate — the paper is readable but has undefined terms ("epochs") and undersupported assertions.
- *Value to the research community*: Moderate — the negative results (all frontier models near random) are interesting and the leaderboard is a useful contribution, but not yet reliable enough for the community to trust as a definitive measurement instrument.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>
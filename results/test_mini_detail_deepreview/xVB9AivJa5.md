Now I have all the calibration data I need. Let me write the consolidated review.

---

## Summary

Blueprint-Bench introduces a benchmark that evaluates AI models' spatial intelligence by requiring them to generate 2D floor plans from apartment photographs. The paper tests a diverse set of LLMs, image generation models, and agent systems on 50 apartments with ~20 interior images each, measuring performance via a composite similarity score based on room connectivity graphs and size rankings. The core finding — that most models perform at or below a random baseline while humans far exceed them — is a meaningful empirical observation that reveals genuine gaps in current AI spatial reasoning capabilities.

## Strengths

- **First benchmark to numerically compare three model architectures on a unified spatial task.** As stated in the Abstract and Section 1, Blueprint-Bench provides the first numerical framework comparing spatial intelligence across LLMs, image generation models, and agent systems on an identical task. The inclusion of agents (Codex CLI, Claude Code) is particularly informative because it tests whether iterative refinement compensates for single-pass spatial reasoning failures.

- **Demonstrates a spatial blind spot using in-distribution inputs.** Unlike ARC (which uses alien grid patterns), Blueprint-Bench uses photographs of apartments — a modality well represented in training data — yet most models still perform at or below the random baseline. This is a stronger indictment than testing on out-of-distribution inputs, as it shows models cannot extract and reconstruct spatial structure from familiar visual data. The human baseline of 0.547 confirms the task is tractable.

- **Negative result on iterative refinement is empirically informative.** Agents (Claude Code at 0.38, Codex at 0.40) showed no meaningful improvement over single-pass models (GPT-5 at 0.42, Gemini 2.5 Pro at 0.42) despite having multiple attempts and environment access (Figures 5, 8). The paper traces Claude Code's trajectory showing it repeatedly asserted correctness while producing errors — a qualitative finding that isolates the bottleneck as spatial reasoning itself rather than lack of iteration.

- **Open-source code and community leaderboard structure.** The paper open-sources the generation code, provides a dataset sample, and maintains a public leaderboard for community submissions (Reproducibility statement). This enables reproducibility and future tracking as new models emerge.

- **Scoring alternatives were empirically tested and rejected.** The paper explicitly reports that LLM-based extraction (poor at understanding floor plans) and wall-sampling distance (harshly penalizes small mistakes) were tried and performed poorly (Section 2.4). The chosen method is empirically grounded against concrete alternatives.

## Weaknesses

### Fatal
None.

### Major

- **The scoring metric conflates rule-following with spatial accuracy, and the paper does not quantify this confound.** The composite score (50% edge overlap, 20% degree correlation, etc.) assumes rule-compliant input. The paper acknowledges this (Section 2.4: "if a generated floor plan does not follow the stated rules, the scoring algorithm might not score it as the model intended… Blueprint-Bench should test spatial intelligence, not instruction following") but does not provide a mechanism to separate the two. When GPT-4o (0.15) and NanoBanana (0.18) score poorly, the paper attributes this to "poor instruction following" — yet the same scoring system is used to make claims about "spatial intelligence" for all models. Without a control experiment (e.g., a tolerant parser that handles minor rule violations, or a separate rule-compliance score reported alongside the spatial score), the reader cannot determine how much of any model's score reflects spatial understanding versus formatting adherence. This limits the interpretability of the benchmark's central claim.

- **The random baseline is under-specified.** The baseline is described as "generating typical floor plans using LLMs and image generation models without any image input" (Section 2.2), but the paper does not report: (a) which specific models were used to generate the baseline, (b) how many samples per apartment, (c) whether the same set of models contributed to both the Figure 5 (0.279) and Figure 7 (0.322) baseline values. While the discrepancy is explained by different apartment subsets (50 vs. 12), the baseline methodology lacks sufficient detail to be replicable or interpretable as a meaningful point of comparison.

### Minor

- **Scoring weights lack justification.** The six-component weighting (50% edge overlap, 20% degree correlation, 10% density, 10% room count, 5% door count, 5% door orientation) is presented without ablation or sensitivity analysis (Section 2.3). A different weighting scheme could reorder model rankings. While alternative scoring approaches were tested (Section 2.4), the chosen weights themselves are not empirically motivated.

- **Dataset diversity is not characterized.** The 50 apartments are not analyzed for number of rooms per apartment, graph density distribution, room size variability, or types of connectivity patterns. The per-apartment plots in the appendix show high variance, suggesting that results may be apartment-specific, but without dataset-level statistics the reader cannot assess whether 50 apartments cover a meaningful range of spatial configurations.

- **Human baseline from a single person.** The paper reports results from "a human" (Section 2.2, Figure 7), which is a single data point. Human spatial reasoning varies substantially; a single individual drawing floor plans is not a reliable ceiling estimate. At minimum, 3–5 human participants would be needed for a meaningful comparison.

- **Model name inconsistencies between main text and appendix.** Figure 5 and the main text refer to "Claude Code (Opus 4.1)" while the appendix caption references "Claude Code (Claude 4.5)." The appendix bar charts list models (Claude 3.5 Sonnet, Claude 3.5 Haiku, etc.) that do not appear in the main results. While some of this may stem from parser artifacts, the inconsistency raises questions about which model versions were actually evaluated.

### Trivial
None.

## Nice-to-Haves

- Validate the scoring metric against human judgments of floor plan similarity on a small sample of generated plans.
- Add a separate rule-compliance score reported alongside the spatial score, to explicitly decouple the two.
- Report validation statistics (precision/recall) of the extraction pipeline (door detection, room segmentation) on a held-out set.
- Provide dataset characterization histograms (rooms per apartment, graph density, room size distribution).
- Include multiple human baselines (3–5 participants).
- Run a sensitivity analysis on the scoring weights to show how rankings change.

## Removed Points

These points were raised by reviewers but are either factually incorrect, misunderstanding the paper, or generic concerns that do not threaten the core claims:

- *"The random baseline is inconsistently reported (0.279 vs 0.322)"* — The paper clearly explains this difference: Figure 5 uses all 50 apartments, Figure 7 uses a subset of 12 apartments (figure caption: "This data is from a subset of Blueprint-Bench (12 instead of 50)"). The inconsistency is explicitly accounted for.
- *"Missing related works"* — Per instructions, this is not evaluated, as confirming the existence of related works requires external sources.
- *"The paper does not specify how many epochs/attempts"* — The paper states "epochs" but this is standard benchmark practice (multiple runs); the detail is minor and does not threaten validity.
- *"Lack of comparison to existing spatial reasoning benchmarks (ScanNet, Matterport3D)"* — These are embodied/3D benchmarks for specialized models, not generalist AI evaluation benchmarks; the paper's scope (evaluating generalist models on a unified spatial task) is distinct.
- *"Formatting issues (typos, garbled text)"* — These are parser artifacts from PDF extraction, not author errors.
- *Missing appendix content* — The parser strips appendix sections from all papers; they exist in the original submission.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a useful perspective: the tension between requiring strict formatting rules (which enable automated scoring) and claiming to measure "spatial intelligence" rather than "instruction following" is a genuine design tension for this class of benchmark. The paper's argument that "at current model capabilities, this is the right tradeoff" is reasonable but needs empirical support (e.g., showing that models which follow rules still perform poorly on spatial accuracy, which the paper partially does). This tension is not unique to Blueprint-Bench — it applies broadly to any benchmark that imposes output constraints for automated evaluation — and the paper would benefit from explicitly framing it as a design dimension rather than a limitation.

## Suggestions

1. **Decouple rule compliance from spatial accuracy.** Report two scores: a rule-compliance score and a spatial-accuracy score (conditional on compliance). This would allow the benchmark to genuinely claim it tests both, and let readers separate the two.

2. **Tighten the random baseline.** Specify which models generated it, how many samples, and whether the same method is used for both figures. Alternatively, use a simpler and more interpretable baseline (e.g., randomly permuting room sizes or connectivity in the ground-truth graph).

3. **Characterize the 50-apartment dataset.** Add a table or histogram showing the distribution of room counts, graph densities, room sizes, and apartment types. This is a few lines of analysis that substantially strengthens claims about benchmark coverage.

4. **Add at least 3 human baselines.** A single human's result is anecdotal. Even 3 participants with a brief description of their background would establish a credible human ceiling.

## Score and Decision

**Calibration Report**

All anchors retrieved across rounds:

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| SPACE | WK6K1FMEQ1.md | 6.75 | R1 | More comprehensive (15 tasks vs 1), stronger cognitive-science grounding, clearer evaluation (multiple-choice vs composite scoring). Blueprint-Bench is notably weaker. |
| FoREST | 9Y6QWwQhF3.md | 4.25 | R1 | Both evaluate spatial reasoning, but FoREST uses synthetic/ templated data (reviewers flagged template bias). Blueprint-Bench's real-photo setup and multi-architecture comparison is stronger. |
| MCTBench | BVACdtrPsh.md | 3.00 | R1 | Incomplete paper (missing Section 3.3, formatting issues). Blueprint-Bench is clearly stronger. |
| COMFORT | 84pDoCD4lH.md | 7.40 | R2 | Highly rigorous methodology ( group-level analysis, cross-lingual tests). Blueprint-Bench is much weaker on evaluation rigor. |
| DivScene | G6DLQ40VVR.md | 6.25 | R2 | Larger dataset (4,614 scenes) but serves a different purpose (navigation). Blueprint-Bench is weaker — less data, weaker evaluation. |
| GenPlan | kA5egaJjya.md | 3.50 | R2 | Floor plan generation method paper with weak experiments and no novelty. Blueprint-Bench's benchmark contribution is stronger. |

**Round 1 bracket**: I estimated the paper sits between 4 and 6.

**Round 2 narrowing**: Comparing to the anchors:
- Stronger than FoREST (4.25) due to real-photo data and multi-architecture comparison.
- Stronger than MCTBench (3.0) and GenPlan (3.5).
- Weaker than SPACE (6.75) — less comprehensive, less rigorous evaluation.
- Weaker than COMFORT (7.40) — less rigorous methodology.
- Weaker than DivScene (6.25) — smaller scale, weaker evaluation.

The paper is closest in strength to the 4.5–5.5 range, above FoREST (4.25) but below SPACE (6.75) and DivScene (6.25). The scoring confound and small dataset without diversity analysis are the binding constraints that prevent the paper from reaching the 6+ range.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
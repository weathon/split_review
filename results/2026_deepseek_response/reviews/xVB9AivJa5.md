Now let me write the final consolidated review.

## Summary

Blueprint-Bench evaluates spatial reasoning in AI systems through the task of converting apartment photographs into standardized 2D floor plans, scoring them on room connectivity graph similarity and size ranking accuracy. The benchmark tests 12 models across LLMs, image generation models, and agent systems, finding that most still score far below human performance on this task — though several models do exceed a random baseline. The paper is motivated by a genuine need for numerical evaluation of spatial intelligence in generalist models, particularly image generation models.

## Strengths

1. **Principled structured scoring beyond pixel-level metrics.** The composite similarity score combines six graph-theoretic components (Jaccard edge overlap at 50%, degree correlation at 20%, graph density at 10%, room count at 10%, door count at 5%, door orientation at 5%) — capturing connectivity structure and size ranking rather than superficial pixel alignment. This is a sensible design target for a benchmark.

2. **First benchmark enabling cross-architecture spatial intelligence comparison.** As the paper states, "To our knowledge, this is the first benchmark to make such comparisons" between image generation models and LLMs on the same spatial task (Section 1). This fills a documented gap: image model announcements often lack numerical benchmarks.

3. **Analytical grounding via human and random baselines.** Human performance (0.547) and a random baseline (0.279/0.322) are quantified on the same task (Figures 5 and 7). The paper reports that all human floor plans had correct room connectivity — establishing that the task is solvable and the gap is not purely a metric artifact.

4. **Concrete evidence of iterative refinement failure.** The Claude Code agent trace (Figure 8) shows that even after multiple self-correction cycles, the agent produced errors while falsely asserting correctness ("Each room is fully enclosed"). This finding goes beyond aggregate scores to reveal diagnostic failure modes.

5. **Transparent dataset standardization.** The 9 explicit formatting rules (Section 2.1) enable robust computer-vision extraction (red dot detection via HSV filtering, flood-fill segmentation, green-door connectivity scanning). This standardization is critical for automated scoring across diverse model outputs.

6. **Open-source code and privacy-preserving dataset design.** Generation code and a sample dataset are released; the majority of apartments are kept private to prevent overfitting, and community submissions to a public leaderboard are welcomed (Section 2.2, Reproducibility Statement).

## Weaknesses

### Major

1. **Scoring conflates size ranking with connectivity, undermining interpretability of the scores as pure measures of spatial reasoning.** The evaluation pipeline assigns room IDs by size rank and then computes connectivity similarity using these size-based IDs (Section 2.3: "rooms are assigned unique IDs based on their size rank (1 being the largest)"). This means a model that correctly recovers the floor plan layout but gets the size ranking of two similarly-sized rooms swapped will be penalized twice — once for the size ranking error and once for the apparent connectivity errors caused by mismatched IDs. The paper acknowledges this directly in Section 2.4: "the penalty of making a mistake in the size ranking causes additional penalties when scoring the connectivity." However, it does not report separate connectivity accuracy independent of size labeling. The paper even notes that humans "always got the connectivity correct" but made size ranking errors — yet the reported human score (0.547) is depressed by this confound. Without reporting (a) connectivity accuracy computed via graph matching without assuming ID correspondence, or (b) separate connectivity accuracy and size ranking accuracy, the paper's central claim that the benchmark measures "spatial intelligence" is not fully supported.

2. **The claim that "most models perform at or below a random baseline" is contradicted by the paper's own data.** In Figure 5, the random baseline is 0.279. The scores shown are: GPT-5 (0.42), Gemini 2.5 Pro (0.42), GPT-5-mini (0.40), Grok 4 (0.40), CodeX (GPT-6, 0.40), Claude Code (0.38), Gemini 2.5 Flash (0.38), GPT Image (0.32), Claude Opus 4.1 (0.32), Claude Sonnet 4 (0.32). Of 12 models, only GPT-4o (0.15) and NanoBanana (0.18) fall below the random baseline. The abstract states "most models perform at or below a random baseline" and the conclusion reiterates "most do not outperform the random baseline." This framing obscures a more interesting finding — several models *do* perform above random, and the question shifts to *what* they capture and why performance is still far below human.

### Minor

3. **Format-adherence confound between spatial reasoning and instruction following.** The 9 strict formatting rules (non-white backgrounds, missing red dots, wrong door colors, etc.) are penalized by the scoring algorithm. Section 3 attributes GPT-4o's and NanoBanana's low scores to "poor instruction following." The paper acknowledges this tradeoff in Section 2.4 ("Blueprint-Bench should test spatial intelligence, not instruction following"). This means that low scores could reflect either poor spatial reasoning or poor format compliance. While the paper is transparent about this, it weakens the diagnostic power of the benchmark for models that fail to comply with the format.

4. **Human baseline is on a limited subset with insufficient documentation.** The human evaluation covers only 12 of 50 apartments (Figure 7 caption). No information is provided about number of participants, their background, or the drawing process. Given that this is the primary reference point for the paper's central claim, more detail is needed.

5. **No statistical significance tests for the "above random" claim.** The paper states that some models "statistically perform better than the random baseline" (Section 3) but does not report confidence intervals, bootstrapped tests, or paired significance tests. Given the high per-apartment variance visible in the appendix, this matters.

6. **Weight choices in the composite score are presented without justification.** The scoring uses 50% edge overlap, 20% degree correlation, 10% density, 10% room count, 5% door count, 5% door orientation (Section 2.3). No sensitivity analysis or validation against human judgment is provided to support these specific weights.

### Trivial

- Figure 7 reports error bars as "2.5 standard deviation" in the caption, which is an unusual choice requiring explanation.
- The random baseline differs between figures (0.279 in Figure 5 vs 0.322 in Figure 7) without explicit explanation — though this is expected given different subsets (50 vs 12 apartments), it should be clarified.
- The table of results in Figure 5 lists Claude Code (Opus 4.1) as "Image model" in the category column, which appears to be a labeling error (it should be "Agent").

## Removed Points

These points were identified by reviewers but are removed or downgraded for the following reasons:

- **SVG vs direct image generation asymmetry**: Removed as not a genuine flaw — LLMs necessarily work through code generation (SVG), and this is a design affordance, not a confound. Each model type uses its native output modality.
- **Figure readability / low resolution**: Removed — these are parser-induced artifacts from the PDF extraction, not issues in the original submission.
- **Appendix model naming discrepancy** (Claude 3.5 Sonnet vs Claude Sonnet 4, etc.): Removed — likely due to the parser stripping the appendix context; model naming conventions in figure captions from the appendix text are unreliable in the extracted version.
- **Missing appendix content, missing proofs, missing references**: Removed — these are parser stripping artifacts, not author omissions.
- **Ground truth adaptation process not described**: Removed as minor to the point of being trivial — the paper states ground truths were "adapted from the apartment listing's official floor plan image" following the 9 rules; the level of detail is adequate for a benchmark paper where the ground truth is a fixed reference.
- **Missing related work**: Removed per instructions — external knowledge cannot confirm completeness.
- **Speculative concerns** about metric validity without specific paper evidence: Removed as generic area-of-concern sweeps.

## Novel Insights

The most interesting observation from the reviews is that the paper's internal consistency problem (claiming "most models at or below random" when the data shows otherwise) is more consequential even than the metric conflation. The metric conflation is transparently acknowledged and could be addressed in future work. The overclaiming in the abstract/conclusion, however, misleads about what the data actually shows and what the benchmark's diagnostic value is. A corrected framing — "all models far below human; several models modestly above random; two models at random" — would strengthen rather than weaken the paper by redirecting attention to the more nuanced question of *what* the above-random models capture.

## Suggestions

1. **Report connectivity accuracy independent of size-based labeling.** The single highest-impact improvement is to compute connectivity similarity via graph matching (e.g., maximum common subgraph overlap) without assuming ID correspondence from size ranking, or to report connectivity accuracy and size ranking accuracy as separate numbers. This would allow the benchmark to distinguish spatial relationship errors from size estimation errors.

2. **Correct the empirical framing.** Acknowledge in the abstract and conclusion that several models (GPT-5, Gemini 2.5 Pro, Grok 4, GPT-5-mini, CodeX) do exceed the random baseline, and frame the finding as "all models remain far below human performance" rather than "most at or below random."

3. **Add statistical significance tests.** Report bootstrapped confidence intervals or paired tests for the "above random" comparison.

4. **Increase human baseline documentation.** Report the number of participants, their instructions, and the variance across apartments.

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing:**
- Weak band (<3.5): Spatial reasoning papers avg score 2.0-3.0 — Blueprint-Bench is clearly stronger.
- Middle band (3.5-7.5): SPACE benchmark (6.75), MANGO (6.25), FoREST (4.25), 3D Reasoning (4.00) — Blueprint-Bench sits here.
- Strong band (>7.5): miniCTX (8.0), MMIE (8.0) — Blueprint-Bench is not at this level.

**Round 2 — Narrowing (bracket ~4.0–6.5):**
- SPACE (6.75, Accept): Comprehensive spatial cognition benchmark with 15 tasks, stronger methodology. Blueprint-Bench is weaker — narrower task scope, less rigorous metric validation, and the overclaimed empirical finding.
- MANGO (6.25, Reject): Cleaner QA-based evaluation for mapping/navigation, but narrower in model categories. Blueprint-Bench is slightly weaker due to metric confounds.
- FoREST (4.25, Reject)/3D Reasoning (4.00, Reject): Narrower scope, fewer models, less real-world task design. Blueprint-Bench is clearly stronger.
- ET-Plan-Bench (4.50, Reject): Limited novelty, unclear evaluation. Blueprint-Bench is stronger.

**Round 1 bracket:** 4.0–7.0
**Final score determination:** Blueprint-Bench is clearly stronger than FoREST (4.25) and the 3D reasoning paper (4.00), but clearly weaker than SPACE (6.75). It is roughly comparable to MANGO (6.25) but the metric limitations and overclaimed empirical finding are more consequential. Against SPACE — which is the closest topical match with rigorous methodology spanning 15 spatial cognition tasks — Blueprint-Bench's single-task design and unvalidated metric place it substantially lower. Score = **5.0**.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
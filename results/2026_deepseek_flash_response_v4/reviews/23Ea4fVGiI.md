## Summary

This paper proposes TMK (Task-Method-Knowledge) structured prompting — borrowing from a cognitive science knowledge representation framework — for LLM planning. The authors evaluate TMK on PlanBench Blocksworld (Classic, Mystery, Random variants) using GPT-4, GPT-4o, o1-mini, o1, and GPT-5. The headline result is o1 improving from 31.5% to 97.3% on Random Blocksworld under TMK prompting, with a "performance inversion" where o1 performs better on Mystery than Random under plain text but reverses under TMK.

## Strengths

1. **Full-plan, formally verified evaluation**: Unlike many prompting papers that evaluate only final answers, the paper uses PlanBench's requirement that every plan step be formally validated by classical planners (VAL/fast-downward). A correct answer requires the entire reasoning trace to be valid, not just the final state (Section 2.2).

2. **The performance inversion result is a striking and specific empirical finding**: Table 2 documents that with plain text, o1 performs better on Mystery (74.3%) than Random (31.5%). Under TMK, this reverses (Random 97.33%, Mystery 83.3%). The 65.8 percentage point gain on Random and the reversal pattern provide genuinely novel evidence that goes beyond a simple "more context helps" story.

3. **Methodological awareness of the one-shot vs. zero-shot asymmetry**: The paper explicitly acknowledges that TMK uses one-shot prompting while the public leaderboard is zero-shot (lines 177-181), and provides three reasoned arguments for why the comparison is conservative (zero-shot typically outperforms one-shot, the one-shot example is random/untailored, they compare against the higher baseline value). This transparency is a positive.

## Weaknesses

### Fatal
None.

### Major

1. **Uncontrolled baseline comparison**: The TMK results are compared against zero-shot plain-text values from a public leaderboard (Valmeekam, 2023) rather than a within-experiment controlled baseline using the same models, API versions, extraction code, and shot format. The authors acknowledge this (line 177) and argue it is conservative. However: (a) the public leaderboard values may have been computed with different model versions and at different dates; (b) while zero-shot > one-shot may hold on average, it is not guaranteed for every specific model/domain combination; (c) although the authors run their own plain-text tests for newer models (line 193), they do not report re-running baselines for all models under identical conditions. This makes it difficult to fully attribute the reported improvements to TMK rather than uncontrolled variables.

2. **Extraction function modification creates a confound**: The paper states that the Valmeekam (2023) extraction code "required update in the extracting random blocksworld to be comparable with the ground truth" (line 183), and an "enhanced extraction function" was applied that tolerates stochastic artifacts like extra symbols and phrasing variations (lines 189-191). This enhanced extraction was applied to the TMK results for Random Blocksworld, but it is unclear whether the same extraction was applied retroactively to the baseline values from the leaderboard. If the baseline was evaluated with a different (stricter or buggy) extraction, the apparent improvement could be partially inflated. This is a particular concern for Random Blocksworld, where the largest gains are reported (o1: 31.5%→97.3%).

3. **No empirical comparison against alternative prompting methods**: Section 2.1 extensively criticizes CoT, ReACT, and CoS for their limitations on planning tasks, but the paper never empirically compares TMK against any of these methods on the same benchmark. Given that CoT has been evaluated on PlanBench, including these comparisons would substantially strengthen the paper's claims about TMK's relative effectiveness over existing techniques.

### Minor

4. **No variance or reliability information**: The paper reports single accuracy values without confidence intervals, multiple-run statistics, or information about experimental repetitions (no mention of temperature, number of trials, etc.). Given the stochastic nature of LLM outputs and the all-or-nothing evaluation (a single wrong action fails the entire plan), the reliability of individual reported values cannot be assessed.

5. **Strong causal claims exceed the correlational evidence**: The abstract and conclusion assert that TMK "steers reasoning models toward formal code-like manipulation" and "acts as a symbolic scaffold." The evidence is performance differences on a single benchmark. The mechanistic claim about reasoning modality shift is not directly tested — no analysis of model internals, output syntax, or attention patterns is provided. The paper partially acknowledges this (line 304: "the cause of that increase is left to future work"), but the abstract and conclusion make much stronger assertions.

6. **The performance inversion interpretation has plausible alternatives not fully addressed**: While the paper states TMK prompts differ per domain (line 173), the exact nature of those differences is not specified. The description of how TMK varies across Classic, Mystery, and Random domains is important for interpreting the inversion but is deferred to an external link. Without this information, it is difficult to fully rule out alternative explanations for the inversion pattern.

### Trivial
- The threshold for "significantly improvements" (bold values in Table 2 caption) is not defined.
- The paper notes that GPT-5 achieves 92.5%–99.3% on plain text (Table 2), suggesting the task may be near-saturated for the strongest models, which somewhat undercuts the claim that TMK is needed.

## Nice-to-Haves
- A within-experiment controlled baseline (same models, same API, same extraction, same shot format for both conditions) would be the single most impactful addition.
- Empirical comparison against CoT, ReACT, and CoS on the same PlanBench configuration.
- Error analysis: what types of planning errors does TMK reduce (precondition violations, ordering errors, etc.)?
- Variance information from multiple runs and specification of sampling parameters.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **"The semantic conflict in Mystery is a fatal confound for the inversion claim"** (Harsh Critic #3): The paper explicitly states (line 173) that the TMK prompt differs across Classic, Mystery, and Random domains. The critic's argument assumes the TMK descriptions are unchanged and semantically incongruent with Mystery's vocabulary, which contradicts the paper. A softened version is retained as Minor weakness #6.
- **"Missing appendix/prompts"**: Removed per Hard Rules — the appendix is stripped by the parser from all papers; it exists in the original submission.
- **"Strength: Robust extraction function"** (Strength Finder): Conflicts with verified Major weakness #2 about extraction confound. Removed.
- **"Strength: Transparent handling of one-shot vs zero-shot mismatch"** (Strength Finder): Partially conflicts with Major weakness #1. The paper is transparent about the issue but the methodological problem remains.
- **"The extraction difference is a fatal/structural confound"**: The enhanced extraction targets formatting artifacts (extra symbols, word variations) that do not change plan semantics. The magnitude of improvement (65.8 pp on o1 Random) is far too large for extraction leniency alone to explain. Demoted from "fatal" to Major.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Run a fully controlled experiment**: Evaluate both plain-text and TMK prompts under identical conditions (same models, API versions, extraction pipeline, and shot format) for all models, and report the controlled difference rather than comparing against a public leaderboard.
2. **Address the extraction confound explicitly**: Either retroactively apply the enhanced extraction to the baseline values, or explain why the baseline values are not affected by the extraction difference. Report all results with the same extraction pipeline.
3. **Add empirical comparisons against CoT, ReACT, and CoS** on the same PlanBench configuration to contextualize TMK's effectiveness relative to existing prompting techniques for planning.
4. **Clarify how the TMK prompt differs per domain variant** (Classic vs. Mystery vs. Random), specifically whether TMK descriptions use domain-specific or canonical action names, to strengthen the inversion interpretation.
5. **Report variance from multiple runs** (at minimum, a range or confidence interval) to establish reliability.
6. **Tone down the mechanistic claims** in the abstract and conclusion to match the correlational evidence, or provide additional evidence (e.g., output structure analysis) for the claimed modality shift.

## Score and Decision

**Calibration Anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| koza5fePTs (Exploring and Benchmarking Planning) | 2.00 | R1 | Much weaker — small scope, no novel technique |
| cWrqs2lwCJ (Backward Planning) | 3.00 | R1 | Weaker — less striking results, less novel technique |
| jOuHjFw71C (Planning in Strawberry Fields) | 3.00 | R1 | Weaker — evaluates existing models, no new method |
| BW8O4wHgbo (Multi-agent Path Finding) | 3.00 | R1 | Weaker — limited results, different sub-area |
| oyXoGJQlUf (GRAIL) | 3.00 | R1 | Weaker — less striking empirical results |
| sdpVfWOUQA (Planning with MCTS) | 3.00 | R1 | Weaker — different approach, less novel |
| K3KrOsR6y9 (AoT+, LLMs Can Plan Only If We Tell Them) | 6.40 | R1 | **Stronger** — controlled baselines, ablations, multiple benchmarks |
| NUD03NBDOE (ActionReasoningBench) | 6.75 | R1 | **Stronger** — benchmark with rigorous evaluation |
| qJ0Cfj4Ex9 (Learning Grounded Action Abstractions) | 6.20 | R1 | **Stronger** — more thorough evaluation |
| DZBFchnM3b (Navigating the Labyrinth) | 3.67 | R1 | Weaker — limited results, benchmark paper |
| OPdmIxdkPb (Query-Efficient Planning) | 4.75 | R1 | Comparable — similar rigor concerns, moderate results |
| UiLtbLsiPU (ET-Plan-Bench) | 4.50 | R1 | Comparable — similar evaluation scope |
| **R2 Low-Middle (3.0–5.5)** | | | |
| 5COCYDObes (Ask more, know better) | 5.00 | R2 | Comparable — similar prompting technique evaluation |
| 85Ik12q2hP (Do Think Tags Really Help) | 4.00 | R2 | Slightly weaker — critical analysis, no new method |
| Glcsog6zOe (Tree-Planner) | 5.25 | R2 | **Slightly stronger** — better controlled experiments, ablations |
| oBHF3urgyS (Extracting Heuristics from LLMs) | 3.50 | R2 | Weaker — less directly related |
| iNcEChuYXD (Modular Agentic Planner) | 4.50 | R2 | Comparable — similar quality assessment |
| **R2 Middle-High (5.0–7.0)** | | | |
| oDbiL9CLoS (Knowledge Manipulation) | 6.50 | R2 | **Stronger** — more rigorous evaluation |
| VIUisLx8lQ (TypedThinker) | 6.00 | R2 | **Stronger** — extensive ablations, multiple benchmarks |
| sl4hOq9wm9 (Knowledge Augmentation) | 5.50 | R2 | **Slightly stronger** — more thorough experiments |
| AgDICX1h50 (Analogical Reasoners) | 5.75 | R2 | **Stronger** — broader evaluation, multiple benchmarks |

**Round 1 bracket**: 4.0–6.0 (above the weak papers at 2-3, below the strong papers at 6-8).

**Round 2 narrowing**: The paper is weaker than Tree-Planner (5.25) due to the uncontrolled baseline and extraction confound, comparable to MAP (4.50) and Query-Efficient Planning (4.75) in overall quality, and stronger than "Do Think Tags" (4.00). It is clearly weaker than AoT+ (6.40) and TypedThinker (6.00) which have controlled baselines, ablation studies, and multiple benchmarks.

**Final score**: **4.5** — a borderline paper with an interesting idea and striking results that are undermined by methodological issues in the experimental design.

**Decision**: **Reject** — the paper introduces a genuinely interesting idea and reports eye-catching results, but the uncontrolled baseline comparison and the extraction confound prevent the evidence from supporting the strong claims made in the abstract and conclusion. The paper would need substantially more rigorous evaluation to be publishable in its current form.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
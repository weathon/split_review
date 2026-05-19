- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 3, 6, 5
Now I have all the evidence needed. Let me produce the final consolidated review.

## Summary

ING-VP introduces a benchmark of six simple deterministic games (Sokoban, Maze, Sudoku, 8-Queens, Tower of Hanoi, 15-puzzle) with 300 algorithmically-generated, solvability-verified levels, designed to isolate and evaluate MLLMs' spatial multi-step planning abilities. The benchmark evaluates 15 open- and closed-source models across six inference settings (image/text, one-step/multi-step, with/without history), using three complementary metrics. The headline finding — that the best model (Claude-3.5 Sonnet) achieves only 3.37% accuracy — provides clear evidence that current MLLMs struggle substantially with these tasks.

## Strengths

1. **Systematic multi-setting comparison enables failure attribution.** Section 3.2 defines six inference settings that vary input modality (image vs. text), reasoning mode (one-step vs. multi-step), and memory (with vs. without history). This goes beyond prior game-based evaluations that use a single interaction mode, allowing the paper to attribute performance gaps to specific bottlenecks (e.g., Claude-3.5 Sonnet drops from 7.00% accuracy in one-step image to 0.30% in multi-step without history, isolating the effect of step-by-step interaction).

2. **Three complementary metrics reveal a dissociation between plausible actions and goal-directed planning.** Accuracy, completion degree, and action efficiency are reported for all models. The striking gap between high efficiency and low accuracy (e.g., Gemini-1.5 Pro achieves 76.52% efficiency on 15-puzzle but 0.67% accuracy) shows that models generate valid-looking moves while entirely failing at goal-directed planning — a nuance lost in pure success-rate benchmarks.

3. **Algorithmically generated levels with solvability guarantees reduce data leakage.** Section 3.4 describes using A*, DFS, and BFS to create levels with maximum 8-step solutions and explicitly modifying 8-Queens starting positions to prevent pattern matching against memorized solutions. This is a methodological improvement over static puzzle datasets.

4. **Planning-capacity analysis across difficulty levels isolates the planning bottleneck.** Figure 4 shows Claude-3.5 Sonnet and GPT-4o accuracy on Maze declining sharply as solution length increases from 4 to 16 steps while efficiency remains stable — directly demonstrating that multi-step planning, not perception alone, is the limiting factor.

5. **Fine-grained error analysis on 555 errors (Claude-3.5 Sonnet) provides concrete diagnostic categories.** Figure 3 classifies errors into perceptual (55.2% in image-text), textual understanding (58.0% in text-only), and planning (~42% in both), with specific observations (e.g., models can count objects but misjudge positions). This provides a level of diagnostic detail absent from standard accuracy-only benchmarks.

## Weaknesses

### Fatal
None. The core claims are supported by the data as presented; the weaknesses below are addressable through additional experiments or exposition.

### Major

1. **No human or random baseline is provided, so the reported accuracies lack calibration.** The paper repeatedly states that "an average human can easily complete all of these tasks" (lines 37, 41, 583, 662) and that performance is "far below the anticipated standard," yet it reports no human accuracy data and no random-agent baseline. For 4-action Maze with ≤8 steps, a random walk would have some non-zero success probability. Without knowing the floor (random baseline) and ceiling (human performance), the reader cannot assess whether 3.37% reflects genuine (if weak) planning ability or is indistinguishable from noise. This is the single most significant gap in the evaluation: the benchmark's diagnostic value would be substantially strengthened by calibrating its difficulty scale with these baselines.

2. **Error analysis is conducted on a single model (Claude-3.5 Sonnet) in a single setting (one-step), yet conclusions are framed as general claims about "MLLMs."** Section 4.3 categorizes 555 errors from Claude-3.5 Sonnet exclusively, then draws broad conclusions such as "For MLLMs, the greatest challenge in perception is understanding location information" (line 587). The error distribution may differ substantially across models (e.g., GPT-4o, InternVL2) and across settings (e.g., multi-step without history). The paper acknowledges that errors in comprehension and reasoning co-occur, making classification partly subjective. A second model's error analysis or a breakdown across settings would be needed to support general claims.

3. **The completion degree metric is underspecified, harming reproducibility.** The paper states: "The closer the final state is to the cleared state, the higher the score; if it deviates, the score decreases accordingly" (line 565). For each of the six games, the distance metric is not defined — e.g., for Sudoku, is this number of correctly filled cells? For 8-Queens, number of non-attacking pairs? For Sokoban, number of crates on targets? Without per-game definitions, this metric cannot be reproduced by other researchers.

4. **Section 5 ("Two Thinking about planning") is a pilot study with a single example and no systematic results.** The section describes two ad-hoc modifications (Step-wise Best of N, Forced Planning) but shows results for only one example (Figure 5). No aggregate accuracy, completion, or efficiency numbers are reported for any model under these modifications. Claims such as "a holistic approach may outperform a divide-and-conquer strategy" are unsupported. This section either needs full experimental results or should be removed.

### Minor

1. **Prompt templates are not provided.** The paper states "A uniform set of prompts was applied across all models" (line 559) and Section 5 shows that small prompt variations substantially affect output distributions (line 655), yet no prompt template is shown. This is essential for reproducibility, especially given the sensitivity to phrasing that the paper itself demonstrates.

2. **Per-game breakdowns are not shown in the main results.** Table 1 aggregates accuracy/completion/efficiency across all six games, which likely masks substantial variation — some games (e.g., Maze with ≤8 steps) may be much easier than others (e.g., Sudoku, 8-Queens). Reporting per-game performance would significantly improve interpretability.

3. **Statistical significance of small differences is not addressed.** With 50 levels per game × 6 games = 300 levels, the standard error for a 1% accuracy measurement is approximately 0.6 percentage points. Reported differences such as 2.50% vs. 2.75% (InternVL2-Llama3-76B vs. GPT-4o) are within noise. The core result (all models ≤3.37%) is robust, but fine-grained rankings should be treated cautiously.

4. **The "first" claim is inadequately differentiated from existing benchmarks.** The paper claims "the first INteractive Game-based Vision Planning benchmark" (line 4). Prior benchmarks such as SmartPlay (Wu et al., 2023) and PuzzleVQA (Chia et al., 2024) also use interactive game environments. While ING-VP's focus on simple, controlled spatial multi-step planning with multiple inference settings is a genuine contribution, the novelty claim would benefit from a more precise comparison table showing exactly what ING-VP covers that prior work does not.

5. **Action efficiency is called "efficiency" but measures move validity, not planning efficiency.** The metric quantifies the proportion of actions that change the game state — a valid complementary signal (e.g., showing that models generate plausible moves without solving the task). However, the name "efficiency" potentially conflates this with planning quality. The paper's own interpretation (e.g., line 612: "action efficiency, which emphasizes perception and judgment of the current state") is reasonable, but renaming it to "move validity rate" would avoid confusion.

### Trivial

1. **Table 1 reports two decimal places (e.g., 0.30%, 2.50%) for accuracy.** Given 300 levels (50 per game), one or zero decimal places would be more appropriate and would not mislead about precision.

## Nice-to-Haves

- Expand the open-source model set beyond the InternVL family (5 of 8 open-source models tested are InternVL variants). Including LLaVA-NeXT, Qwen-VL, or other families would strengthen the generality of the findings.
- Discuss the risk of data leakage more explicitly for the text representations of 8-Queens and Sudoku, even though the visual variants are protected by modified starting positions and 71-clue puzzles, respectively.
- Report exact binomial confidence intervals alongside the main accuracy numbers.

## Removed Points

**These points are flagged to be removed; treat them with caution:**

- *"Data leakage concern for 8-Queens and Sudoku: the text representations could still appear in training data"* — The paper explicitly describes mitigation strategies (modified 8-Queens starting positions, 71-clue Sudoku, algorithmically generated levels). This concern is partially addressed and is a speculative gap rather than a verified flaw.
- *"Open-source model coverage: Only InternVL variants"* — Factually inaccurate; the paper tests CogVLM2-19B, DeepSeek-VL, MiniCPM-V2.6, and multiple InternVL variants. The dominance of InternVL (5 of 8) is noticeable but the claim "only InternVL" is incorrect.
- *"Action efficiency is a problematic metric"* — The paper uses it as a complementary metric and does not claim it measures planning quality. The example of high efficiency / low accuracy is used to support, not undermine, the paper's narrative. The criticism overstates the issue; downgraded to a minor naming concern above.
- *"Missing related works"* — Per policy, I cannot verify what works are missing; this criticism is excluded.
- *Formatting/style nitpicks* about the table being "overwhelming" — removed as subjective presentation preference.

## Novel Insights

The most interesting pattern that emerges from the review process is the dissociation between action efficiency and accuracy as a diagnostic signal. The paper shows that models maintain high move-validity rates even as accuracy collapses with increasing solution depth (Figure 4). This suggests that MLLMs' "planning" operates primarily as local pattern matching of plausible next actions without a coherent global plan — a failure mode distinct from either pure perception errors or general task incomprehension. The six-setting design (image vs. text × one-step vs. multi-step × with/without history) has the potential to further decompose this failure: the fact that one-step (macro-planning) often outperforms multi-step (incremental decision-making) suggests that forcing step-by-step decomposition actually harms performance, possibly because it triggers local greedy search rather than global optimization. Future work could exploit this diagnostic structure more aggressively than the current paper does.

## Suggestions

1. **Add random and human baselines.** Run a random action policy on all 300 levels and collect human accuracy on a representative subset (e.g., 20 levels per game). Report these alongside model results to calibrate the 3.37% number.
2. **Broaden the error analysis** to at least one additional model (e.g., GPT-4o) and one additional setting (e.g., one-step text-only) to support the general claims about "MLLMs' perceptual limitations."
3. **Define completion degree precisely per game** (e.g., Sudoku: fraction of correctly filled cells; 8-Queens: number of non-attacking queen pairs; Sokoban: crates on targets / total crates).
4. **Either remove Section 5 or run it as a full ablation** with aggregate results across all models and levels — the current single-example analysis does not support its claims.
5. **Include prompt templates** in an appendix, given the demonstrated sensitivity to phrasing.
6. **Provide per-game breakdowns** (e.g., accuracy per game in a supplementary table) and round accuracy to one decimal place or report confidence intervals.

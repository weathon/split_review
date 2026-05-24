Now I have all the information needed. Let me compose the final consolidated review.

## Summary

Blueprint-Bench introduces a benchmark that evaluates AI spatial reasoning by asking models to generate 2D floor plans from apartment photographs. The benchmark spans 50 apartments (~20 photos each), tests LLMs, image-generation models, and agents, and uses a scoring pipeline that extracts room connectivity graphs and size rankings from generated floor plans. Results show that even frontier models (GPT-5, Gemini 2.5 Pro) score well below human performance (0.42 vs. 0.547), with many models at or below a random baseline, suggesting a blind spot in current spatial reasoning capabilities.

## Strengths

- **Novel evaluation framework that bridges LLMs and image-generation models on the same spatial task.** The scoring algorithm decomposes floor-plan similarity into connectivity, degree correlation, room count, door count, door orientation, and density — enabling the first numerical comparison between GPT Image (0.32) and GPT-5 (0.42), or between NanoBanana (0.18) and Gemini 2.5 Flash (0.38) (Fig. 5). No prior benchmark enables this cross-architecture comparison on a spatial reconstruction task.

- **Demonstrates a concrete blind spot using in-distribution input modality.** The paper finds that most models perform at or near a random baseline despite photographs being well-represented in training data (Fig. 5). This is a meaningful contrast to benchmarks like ARC that use intentionally out-of-distribution inputs. The best-performing models (GPT-5, Gemini 2.5 Pro at 0.42) substantially underperform humans (0.547), providing quantitative evidence for a real capability gap.

- **Careful agent ablation to test the iteration hypothesis.** The paper separately tests whether iterative refinement (via Codex CLI, Claude Code agents) closes the gap with humans, finding that it does not (Fig. 5). The qualitative trace analysis (Fig. 8) shows that even when agents attempt multiple rounds of refinement, they still produce structurally incorrect outputs — a controlled test that strengthens the conclusion that the limitation is in spatial reasoning, not in single-pass generation constraints.

## Weaknesses

### Major

1. **The metric conflates spatial intelligence with instruction-following, muddying the interpretation of results.** The paper states that Blueprint-Bench "should test spatial intelligence, not instruction following" (Section 2.4), yet the scoring pipeline requires rigid adherence to 9 formatting rules (black walls, green doors, red dots, no furniture, white backgrounds, etc.). Models that reconstruct room layout and connectivity correctly but violate formatting (e.g., drawing doors at an angle, including furniture) receive near-zero scores because the extraction algorithm cannot parse them. The paper itself notes that GPT-4o and NanoBanana's poor performance is "attributed to poor instruction following" (Section 3), and the examples in Figure 6 show outputs that are clearly attempting floor plans but are unscorable. While this is acknowledged as a limitation, the paper does not quantify how much of the performance gap is due to formatting failures vs. genuine spatial failures — yet the headline claim ("most models perform at or below random") draws no such distinction. For the models that *do* follow the rules (GPT-5, Gemini 2.5 Pro), the spatial failures are clearer, but the overall narrative is weakened by the ambiguity.

2. **The composite scoring weights are presented without justification or sensitivity analysis.** The six components are combined as: edge overlap 50%, degree correlation 20%, density 10%, room count 10%, door count 5%, door orientation 5% (Section 2.3). No ablation, rationale, or sensitivity analysis is given for these weights. This matters because several components interact: the harsh penalty from size-ranking errors (which the paper acknowledges in Section 2.4) propagates through edge overlap and degree correlation, inflating penalties beyond pure connectivity errors. The human baseline of 0.547 despite *all* connectivity being correct confirms that the metric conflates multiple error sources. Without ablations (e.g., edge-only scores ignoring size ranking, or equal weighting), it is unclear what drives the observed model rankings.

3. **The human baseline is too small and lacks statistical framing.** The human evaluation uses only 12 of 50 apartments (Fig. 7 caption). The paper claims "human performance remains substantially superior" (Abstract), but (a) no statistical test compares the best model to the human baseline, (b) no per-apartment variance is reported for the human data, and (c) the human score of 0.547 is depressed by size-ranking errors in components the paper admits are not core spatial intelligence. The claim that humans are better at connectivity is qualitatively clear (the paper states all human floor plans had correct connectivity), but the headline "0.547" number is not a clean human upper bound.

4. **Claimed statistical significance without any reported test.** The paper states that "some models (GPT-5, Gemini 2.5 Pro, GPT-5-mini, and Grok 4) statistically perform better than the random baseline" (Section 3) and that GPT-4o and NanoBanana performed "significantly worse" — but no statistical test (t-test, permutation test, confidence intervals, or otherwise) is reported anywhere. Given the large standard deviations (~0.2–0.3), some observed differences may not be reliable, and the reader cannot assess which comparisons are robust.

### Minor

1. **The worst-case (random) baseline is vaguely specified.** It is described as "generating typical floor plans using LLMs and image generation models without any image input" (Section 2.2). The paper does not state how many outputs were generated, what prompts were used, or whether the 0.279 value aggregates over multiple model types. The random baseline differs between the full 50-apartment set (0.279) and the 12-apartment subset (0.322), suggesting sensitivity to which apartments are included.

2. **The appendix uses a different model naming scheme than the main figures.** Figure 5 uses "Claude Code (Opus 4.1)" while the appendix (Fig. A1, A2) uses "Claude Code (Claude 4.5)" — these likely refer to the same model but the inconsistency is confusing. The appendix also shows results only for Claude variants, not the broader model set from the main results, making it hard to verify individual apartment scores for GPT-5, Gemini models, etc.

3. **The degree to which the agent experiment controls for iterative refinement is limited.** The agents use different underlying base models (Codex uses GPT-5/GPT-6, Claude Code uses Claude Opus 4.1), so differences in agent performance could be due to base model capability rather than iteration strategy. The conclusion that "iterative refinement … showed no meaningful improvement" (Abstract) is supported by the aggregate results but would be stronger with the same base model used in both agent and non-agent settings.

### Trivial

- None that meet the bar for inclusion after applying the filtering rules.

## Nice-to-Haves

- Report edge-overlap scores (the 50% Jaccard component) independently, both with and without size-ranking assignment. This would let readers assess spatial connectivity separately from the formatting and ranking noise.
- Run the human baseline on more apartments (≥30) and include a simple permutation test comparing the best model to the human mean.
- Include an ablation of the scoring weights: e.g., show how rankings change if all components are weighted equally.
- Describe the random baseline more precisely (prompts, number of samples, which models contributed to the aggregate).

## Removed Points

These points were flagged by reviewers but removed from the main weaknesses section with justification:

- *"No explicit confidence intervals on benchmark scores"* — Single-run evaluation with observed standard deviation bars is standard practice for generative benchmarks of this kind.
- *"Comparisons with human might be unfair because humans iteratively refined while models were single-pass"* — The paper addresses this with the agent experiments; the agent results support the conclusion that iteration does not close the gap.
- *"The dataset is private and not fully released"* — The paper explains this is to prevent overfitting, and provides a sample and submission pipeline. This is standard benchmark practice.
- *"Missing discussion of related work on floor plan generation"* — The paper is not about building better floor-plan generators; it is about evaluating generalist models. It cites the key floor-plan generation works to distinguish its scope.
- *"Size-ranking creates harsh penalties and should be removed"* — The paper acknowledges this as a known limitation and defends it as a necessary tradeoff for robust scoring. It is a valid design choice even if not optimal.

## Novel Insights

The strongest insight to emerge from synthesizing the reviews is that Blueprint-Bench's value lies less in its aggregate scores (which are confounded by instruction-following demands) and more in its **decompositional structure**: the six scoring components, if reported and analyzed separately rather than in a single weighted average, could cleanly separate spatial reasoning (edge overlap, connectivity) from formatting compliance and size estimation. The fact that humans achieve perfect connectivity but only 0.547 overall means the composite score is actually a *lower bound* on human spatial capability — the true human edge over models is larger than the headline number suggests. The paper's reported agent trace (Fig. 8) showing Claude Code asserting "Each room is fully enclosed" about an output that plainly is not is also a striking qualitative data point about the limits of self-correction on spatial tasks.

## Suggestions

- **Disentangle instruction-following from spatial reasoning in the analysis.** Score all outputs with a rule-compliance pre-filter, then report results separately for (a) spatially accurate outputs among rule-compliant generations, and (b) a lenient score that uses graph-matching algorithms on non-compliant outputs. This would directly address whether the "near-random" result is driven by formatting failures or genuine spatial failures.
- **Report individual scoring components**, not just the composite. A table showing edge-overlap Jaccard, room-count accuracy, door-count accuracy, and door-orientation accuracy for each model would be far more informative than a single weighted average with unexplained weights.
- **Add a simple statistical test** (e.g., bootstrap confidence intervals or a permutation test) for the main comparisons: each model vs. the random baseline, and the best model vs. human.
- **Expand the human baseline** to at least 30 apartments and report per-apartment variance. Even a second human drawing a subset would strengthen the conclusions.

## Score and Decision

**Calibration anchors retrieved (all rounds):**

| Anchor | Score | Round | Comparison to this paper |
|--------|-------|-------|------------------------|
| SPACE — Does Spatial Cognition Emerge in Frontier Models? (WK6K1FMEQ1) | 6.75 | R1 | More comprehensive spatial cognition benchmark (15 tasks); better grounded in cognitive science; fewer evaluation methodology issues |
| FoREST (9Y6QWwQhF3) | 4.25 | R1 | Similar spatial reasoning benchmark but synthetic dataset and no code release; this paper is stronger in task concreteness |
| 3D Reasoning of VLMs (uBhqll8pw1) | 4.00 | R1 | Similar evaluation of spatial reasoning; this paper has a cleaner task formulation |
| MuirBench (TrVYEZtSQH) | 5.20 | R2 | Comparable benchmark paper (multi-image understanding); accepted at a venue but with mixed reviews; this paper has a more novel task but weaker evaluation methodology |
| MMIU (WsgEWL8i0K) | 6.00 | R2 | Larger-scale benchmark; accepted; this paper's task is more specific and less comprehensive |
| Mapping/Learning (TCSaLeANpN) | 3.00 | R1 | Weak anchor: floor-plan dataset paper with low scores |
| Abstract Noise to Architectural Form (skJLOae8ew) | 3.00 | R1 | Weak anchor: floor-plan generation method, not evaluation |
| Exploring Planning Capabilities (koza5fePTs) | 2.00 | R1 | Weak anchor: different task (planning), lower quality |

**Round-1 bracket:** Between ~4.0 (FoREST, 3D Reasoning of VLMs) and ~6.75 (SPACE).

**Round-2 narrowing:** Anchored against MuirBench (5.20, accepted) as the closest comparable benchmark paper. Blueprint-Bench has a more novel task (generative reconstruction rather than multiple-choice) but weaker evaluation methodology — specifically, the metric confounds two capabilities and lacks validation. The paper sits below SPACE (6.75) due to the metric issues, and slightly below MuirBench (5.20) because the evaluation weaknesses are more central to the paper's claims. Within the narrowed range, the paper is closest to the 4.5–5.5 band.

**Final score:** **5.0** — The paper tackles an important problem with a genuinely novel task and dataset, and the core finding (models struggle with spatial reconstruction) is probably correct. However, the evaluation methodology conflates instruction-following with spatial intelligence, uses arbitrary and unablated scoring weights, lacks statistical tests for its main claims, and relies on a human baseline of only 12 apartments — all verified weaknesses that weaken the paper's central arguments. These issues are fixable but are substantive enough that the claims are not adequately supported in the current form.

**Decision: Reject**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
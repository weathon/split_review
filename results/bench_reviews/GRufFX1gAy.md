Now I have a thorough understanding of both the paper and the calibration landscape. Let me write the consolidated review.

## Summary

InnoGym proposes a benchmark and framework for evaluating the innovation potential of AI agents along two dimensions: **performance gain** (improvement over known baselines) and **methodological novelty** (dissimilarity from prior solutions). The benchmark includes 18 "improvable tasks" curated from real-world competitions, standardized through multi-stage filtering. A companion execution environment (iGym) supports reproducible, long-horizon evaluation. Experiments on three agent frameworks (MLAB, CODEACT, AIDE) show that current agents universally fail to achieve positive performance gain, with most novelty scores in the 30-70 range, suggesting a gap between creativity and robust execution.

## Strengths

1. **Well-motivated and principled formal framework.** The quadruple formulation (P, S, V, D), the performance gain / novelty decomposition, and the taxonomy of solved/improvable/exploratory tasks provide a clean conceptual foundation that existing benchmarks lack. This framework cleanly captures something missing from prior work: the distinction between *what* a solution achieves and *how* it achieves it.

2. **Rigorous and transparent benchmark construction.** The two-stage filtering pipeline (197→72→18 tasks), evaluator normalization with correlation checks (Pearson ≥ 0.9, Kendall-τ ≥ 0.8), and the solution collection process with independent cross-validation by three team members demonstrate serious methodological care. The resulting tasks span genuinely diverse domains (OR, ML, systems, science) drawn from real competitions rather than synthetic generation.

3. **Insightful experimental analyses that go beyond leaderboard reporting.** The temporal dynamics analysis (Figure 6a), the temperature exploration-exploitation trade-off on Circle Packing (Figure 6c), and the complex-plane representation of the innovation trajectory (Figure 5b) demonstrate that the two-metric framework can reveal agent behaviors that a single performance score would miss. The "sweet spot" at temperature 0.5-0.75 is a concrete, actionable finding.

4. **Transparent documentation of current agent limitations.** The paper does not bury negative results. It clearly documents that all tested agents produce negative performance gain on all tasks, and that on 2 of 10 tasks no agent produces a valid submission. This level of candor is valuable for the community.

## Weaknesses

### Fatal
None.

### Major

1. **Insufficient validation of the novelty metric D_AGENT, which is the paper's core differentiator.** The distance function D_AGENT — the mechanism for computing the novelty score N(s) — is validated against human judgments on only **11 triplets** (8 sub-sampled from EquiBench + 3 human-collected method triplets from AI subfields). The 50 automatic EquiBench triplets (Table 8) serve as a useful sanity check but do not substitute for human evaluation of the metric's behavior on the actual benchmark tasks. The sample is too small to establish reliability:
   - The EquiBench human annotation set (8 triplets) is too small for meaningful correlation estimates.
   - The 3 human-collected triplets produce suspiciously perfect correlations (1.00 Pearson/Spearman, Table 10), which is an artifact of tiny sample size.
   - No inter-annotator agreement statistics are reported.
   - No sensitivity analysis is provided (e.g., how scores change with different LLM judges, different prompts, or different extraction procedures).
   - Most critically, the validation is performed on code-level (EquiBench) and published-method (3 triplets) examples, not on actual agent-generated solutions from iBench tasks. The metric could behave differently on the messy, partially broken solutions agents actually produce.

   Since the novelty metric is *the* novel contribution that distinguishes InnoGym from every benchmark in Table 1, insufficient validation undermines the paper's central claim. This is not fixable by adding a few more examples in a rebuttal; a systematic validation study is needed.

2. **The experimental results do not demonstrate that the benchmark measures "innovation potential" in a meaningful way.** Under the paper's own framework (Section 2.2), innovation requires G(s) > 0 or G(s) ≈ 0 with high N(s). Across all 10 main tasks, *every* agent achieves negative G. The average normalized ratios are -0.45 (MLAB), -0.69 (CODEACT), and -0.64 (AIDE). On 2 tasks, agents produce *zero* valid submissions. The paper interprets this as "the primacy of robustness over novelty," but an alternative reading is that the benchmark tasks are simply too difficult for current agents, turning the evaluation into a measure of basic execution feasibility rather than innovation potential. The space of (G, N) outcomes that would actually demonstrate "innovation" is entirely empty in these experiments. The paper does not provide diagnostic analysis of *why* agents fail (e.g., feasibility checks, timeouts, dependency issues), nor does it calibrate task difficulty (e.g., by showing human performance or simpler subtasks).

### Minor

1. **Exploratory problems are excluded, limiting the benchmark's reach.** The paper explicitly excludes tasks where S_known = ∅ ("exploratory problems") because they "cannot be reliably evaluated." Yet these are precisely the settings where measuring novelty is most valuable — the first feasible solution to an unsolved problem is definitionally maximally novel. The paper frames InnoGym as evaluating "innovation potential" broadly, but it only covers *incremental* improvement over known baselines. This scope limitation is acknowledged in Appendix B but the paper's claims (abstract, introduction) are broader than the operationalization supports.

2. **The paper does not report novelty scores for the reference solutions (S_known) themselves.** The diversity score Div(T) gives average pairwise distance among references, but individual novelty scores of reference solutions are not reported. This makes it difficult to calibrate expectations: if reference solutions have high mutual novelty (high Div), then an agent scoring N=50 might be doing well; if baselines are similar to each other, N=50 might indicate spurious deviation. Understanding the reference distribution is essential for interpreting agent novelty scores.

3. **No qualitative examples of high-novelty agent solutions are shown.** The paper mentions that agents achieve "mid-to-high novelty" on RCIC and TrojanDetection but with low performance. Showcasing even one or two such solutions with their extracted summaries and comparison scores would help validate whether the metric captures genuine methodological differences or spurious complexity. Without this, the novelty scores remain opaque to the reader.

### Trivial
None.

## Nice-to-Haves

- A failure analysis (taxonomy of why agents fail to produce valid submissions) would strengthen the paper's diagnosis and help the community prioritize fixes. The paper reports success rates (Table 6) but does not analyze failure modes.
- Testing the sensitivity of novelty scores to the inclusion/exclusion of individual reference solutions (jackknife-style analysis) would help assess metric robustness. Currently, the paper acknowledges this only qualitatively in the limitations section.
- Reporting confidence intervals on the main results (beyond the bootstrap analysis in Appendix E.2) would improve statistical rigor.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The framework's definition of novelty is ambiguous about whether novelty alone constitutes innovation — the paper creates a tension by demoting novelty when G is not positive."* This is not a genuine weakness: the paper clearly defines the (G, N) regimes (Section 2.2) and explicitly states that high novelty with large negative G is "unsuccessful exploration rather than innovation." This is a design choice, not an ambiguity.
- *"The benchmark's central contribution is not established"* — This is a conclusion, not a specific weakness. The specific weaknesses that lead to this conclusion are already listed above.
- *Criticism about the paper claiming "first benchmark to evaluate innovation potential" not being established.* This follows from the major weaknesses above and need not be listed separately.
- *"The paper does not discuss whether tasks are appropriate for the stated goal"* — The paper does discuss this in Section 3 (focusing on improvable tasks) and Appendix B (limitations).

## Novel Insights

The harsh critic's observation about the structural tension between G and N is genuinely insightful: because almost all agent solutions have negative G, the benchmark's claim of measuring "innovation potential" reduces to measuring novelty alone in practice. This reveals a deeper issue with the framework's design — the two-metric decomposition is elegant in theory, but when one dimension (G) is empirically degenerate (always negative), the framework collapses to a single dimension. This suggests that either (a) the tasks need recalibration to allow some positive G (simpler subtasks, more time, better initial baselines), or (b) the framework needs a different formalization where innovation is not defined as occupying specific (G, N) regimes but rather as the *direction* of search in solution space regardless of absolute position. The temporal dynamics analysis (Figure 6a) hints at this richer view but does not develop it.

## Suggestions

1. **Validate D_AGENT at scale.** Collect human judgments on at least 100-200 triplets spanning diverse iBench tasks, with multiple annotators per triplet and reported inter-annotator agreement. This is essential for a benchmark that stakes its contribution on a novelty metric.

2. **Include calibrated difficulty tiers.** Add subtasks or simplified versions of the current tasks where some agents can achieve G ≥ 0. This would allow the benchmark to measure innovation (not just feasibility) for current-generation agents. Alternatively, provide human baselines on all tasks.

3. **Add failure analysis.** Report why agents fail to produce valid submissions — categorize failures as feasibility violations, timeouts, dependency errors, etc. This would clarify whether the benchmark's difficulty stems from genuine task complexity or from operational hurdles.

4. **Provide case studies.** Show 2-3 concrete examples of agent solutions with their extracted summaries, D_AGENT scores per rubric dimension, and qualitative comparison to the nearest reference solution. This would give readers intuition for what the novelty metric actually captures.

## Score and Decision

**Calibration anchors** (all from the human-reviewed ICLR 2026 corpus):

| Anchor | Avg Score | Decision | Comparison to InnoGym |
|--------|-----------|----------|-----------------------|
| AstaBench (M7TNf5J26u) | 7.00 | Oral | Far more comprehensive (2400+ tasks, 57 agents, cost-aware evaluation); rigorous validation of evaluation protocols. InnoGym is weaker. |
| EXP-Bench (KjgyAm383Z) | 6.00 | Poster | 461 tasks vs. 18; also faces LLM-as-judge concerns but has larger scale and more validation. InnoGym is weaker. |
| InnovatorBench (w8rZ2Jd6Jo) | 5.33 | Poster | Similar motivation (benchmarking agent innovation); comparable task count (20). InnovatorBench's weaknesses were about cost and limited detail; InnoGym's metric validation gap is more central. Comparable but InnoGym's weakness is more structural. |
| HAL (vUaY1t64ZZ) | 5.20 | Poster | Large-scale engineering contribution (21K rollouts); different kind of contribution entirely. InnoGym is weaker in empirical scale. |
| FML-Bench (h6BT8RhrNc) | 4.50 | Reject | 8 tasks, had metric reliability concerns similar to InnoGym's. InnoGym has more tasks and more careful curation, but its central weakness (novelty metric validation) is also more central to its contribution. Slightly stronger. |
| UltraHorizon (FTZfVHWAIq) | 4.50 | Reject | 3 synthetic environments; LLM-as-judge concerns. InnoGym is stronger: more tasks from real competitions, more careful curation. |
| FrontierBench (dMY9FGUkiU) | 2.00 | Reject | Tried too many contributions without deep validation; tasks were conceptually vague. InnoGym is substantially stronger. |

**Final score:** The paper has a well-motivated framework and careful benchmark construction, but the central claim — that InnoGym evaluates "innovation potential" — rests on a novelty metric validated on only 11 human-annotated triplets. This is a fundamentally insufficient validation for the paper's core differentiator. The experimental results (all agents produce negative G) further limit what the benchmark can currently claim to measure. The paper is well above the weakest anchors (FrontierBench at 2.00) and comparable to the mid-range rejected papers (FML-Bench, UltraHorizon at 4.50), but falls short of the accepted anchor papers (InnovatorBench at 5.33, EXP-Bench at 6.00) in terms of validation depth relative to the strength of the claims.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
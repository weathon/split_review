Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

Blueprint-Bench proposes a benchmark that evaluates spatial intelligence in AI models by having them convert apartment photographs into standardized 2D floor plans. The scoring algorithm measures the graph-based structural similarity (room connectivity, size rankings, door placements) between generated and ground-truth floor plans. The authors evaluate 12 systems across LLMs, image generation models, and agent scaffolds, finding that most perform at or below a "no-vision" baseline while a human baseline scores substantially higher.

## Strengths

- **Novel cross-architecture evaluation framework.** The benchmark is the first to compare LLMs, image generation models, and agent systems on the same spatial reasoning task using a unified numerical metric (Abstract, Section 1). This enables comparisons that prior benchmarks could not support, such as whether image-generation training preserves or degrades the spatial intelligence of the underlying LLM.

- **Well-motivated graph-based scoring algorithm.** Rather than pixel-level similarity (which would punish style differences), the algorithm extracts room connectivity graphs and size rankings and computes a weighted composite of six interpretable components (Section 2.3). The paper discusses and rejects alternative approaches (LLM-based extraction, bidirectional nearest-neighbor distance), demonstrating thoughtful design grounded in the specific challenges of the task.

- **Transparent acknowledgment of the metric's central tension.** Section 2.4 explicitly identifies the tradeoff between rule strictness (needed for robust parsing) and measuring purely spatial intelligence. The paper states "Blueprint-Bench should test spatial intelligence, not instruction following" and argues for the current design as the right tradeoff given model capabilities. This candor is valuable even though the issue remains unresolved.

- **Open-source code, dataset sample, and public leaderboard commitment.** The paper releases generation code and a dataset sample, and invites community submissions to an evolving leaderboard (Reproducibility Statement, Section 2.2). This supports independent validation and long-term tracking.

- **Empirical demonstration of a large human–AI gap.** Despite the thin human baseline (discussed below), the gap between the human score (~0.55) and the best model (~0.42-0.45) on the same 12-apartment subset is substantial and consistent with the paper's central claim.

## Weaknesses

### Fatal
None.

### Major

- **The scoring metric conflates instruction-following with spatial reasoning, and this is not resolved.** The evaluation requires generated floor plans to adhere to nine strict formatting rules (3px black walls, red dots centered in rooms, green doors, white background, no furniture, etc.). Models that produce a spatially correct layout but violate any rule (e.g., GPT-4o omits red dots, NanoBanana includes furniture) receive low or unscorable outputs. The paper acknowledges this in Section 2.4 but treats it as an acceptable tradeoff. However, this conflates two distinct capabilities — spatial reasoning and output-format compliance — in the primary metric. A model could infer the correct room adjacency and size ranking but fail the extraction step entirely, yielding a near-zero score that is indistinguishable from a model that guessed wrong. The paper provides no validation (e.g., correlation with human judgments of spatial correctness) to demonstrate that the composite score predominantly reflects spatial ability rather than rule compliance. This undermines the central claim of providing "the first numerical framework for comparing spatial intelligence."

- **The human baseline is insufficiently supported for the weight placed on it.** The human baseline (Figure 7) involves a single human participant ("the human," Section 2.2) on only 12 of the 50 apartments. No information is provided about the participant's background, instructions, or task interface. Inter-participant variability is absent. While the observed gap (~0.55 vs. ~0.42) is large and suggestive, the paper draws the strong conclusion that "human performance remains substantially superior" — a claim that would be far more convincing with multiple participants and inter-rater reliability measures, especially given the complexity of the floor-plan-drawing task. The SPACE benchmark (WK6K1FMEQ1, avg 6.75) demonstrates the standard for human baselines in this area.

### Minor

- **Parse failure rates per model are not reported.** The paper notes that GPT-4o and NanoBanana produced outputs that "cannot be scored by our algorithm" due to formatting violations (Section 3). It also mentions that NanoBanana "constantly included furniture, windows, etc." However, the paper never reports the fraction of generations that were successfully parsed per model. If many outputs from a model were unparseable, the reported means reflect only a selected subset. This is essential for interpreting Figure 5 and comparing models.

- **The weighting scheme (50% edge overlap, 20% degree correlation, etc.) is presented without justification or sensitivity analysis.** Section 2.3 lists fixed component weights for the composite score but provides no motivation (e.g., "edge overlap is weighted highest because...") and no analysis of how scores shift under moderate weight variations. For a benchmark whose contribution hinges on a numerical scoring framework, this omission weakens the claim that the metric is well-calibrated.

- **The agent experiment's conclusions are partly confounded by scaffold quality.** The paper reports that Codex GPT-5 "never even looked at the image it created before submitting" — i.e., it did not use the iterative capability at all — yet the results are pooled to support the claim that "iterative refinement through agents showed no advantage" (Section 4). The other agent (Claude Code) did iterate but still failed. The claim would be more precise as: "the specific agent scaffolds we tested, one of which did not actually iterate, did not outperform single-pass models."

- **Statistical significance tests are referenced but not specified.** The paper states that GPT-5, Gemini 2.5 Pro, GPT-5-mini, and Grok 4 "statistically perform better than the random baseline" (Section 3) but does not name the test, report p-values, or discuss corrections for multiple comparisons.

### Trivial
None.

## Nice-to-Haves

- A human evaluation study (3-5 participants on a larger subset, with per-participant scores and inter-rater reliability) would substantially strengthen the central claim.
- Reporting per-model parse-success rates and mean scores conditioned on successful parsing would disentangle instruction-following from spatial reasoning.
- A sensitivity analysis on the six component weights would help establish metric robustness.
- A "formatting-compliant" sub-score (measuring spatial ability only on outputs that pass parsing) would allow a cleaner reading.

## Removed Points

These points are flagged to be removed — treat them with caution:

- **"Random baseline is poorly defined and possibly misleading"** — The harsh critic argued that different baseline values (0.279 vs. 0.322) appear without explanation. However, the paper clearly states that Figure 5 uses all 50 apartments and Figure 7 uses a 12-apartment subset; different baseline values on different subsets are expected and properly documented. The baseline is called a "worst-case baseline" (generating floor plans without image input), which is a reasonable no-vision baseline, not a mathematically random one. This criticism misunderstands the paper.

- **"Model naming inconsistencies" (Claude 4.5 in appendix vs. Opus 4.1 in main text)** — The appendix is stripped by the parser ("Rest of paper... is removed"), so the model names in appendix images cannot be verified from the available text. Per hard rules, criticisms about stripped appendix content are removed.

- **"Missing trajectory/epoch details for agents"** — The paper states it computes results "averaged across epochs and apartments" (Figure 5 caption), indicating multiple trials were run. The critic's claim about missing trajectory details is not supported.

- **"Overstated claim about being first numerical framework"** — The paper explicitly acknowledges its metric's limitations and qualifies its claims. The "first numerical framework" claim is supportable given the absence of prior cross-architecture spatial-intelligence benchmarks.

- **"Door orientation distribution similarity is not detailed"** — While full detail is limited, the paper describes the extraction: "recording their positions and orientations (horizontal vs. vertical based on pixel arrangement)." This provides sufficient information for the submission format.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a tension that the paper itself identifies: the metric must be strict to be automatable, but strictness conflates spatial reasoning with rule compliance. Neither the reviews nor the paper resolve this tension, though the paper at least acknowledges it honestly.

## Suggestions

1. **Validate the metric against human judgment.** Collect human similarity ratings on pairs of floor plans (or rankings of candidate outputs) and measure correlation with the composite score. This is the single highest-leverage improvement for establishing that the benchmark measures what it claims.

2. **Report per-model parse success rates and a "conditional" score.** For each model, report both the fraction of outputs that could be parsed and the mean score restricted to parseable outputs. This lets readers separate instruction-following from spatial ability.

3. **Expand the human baseline.** At minimum, add 3–5 participants on the same 12-apartment subset and report per-participant scores, mean, and variance. If feasible, extend to 20+ apartments.

4. **Include a sensitivity analysis on the scoring weights.** Show that the rank ordering of models is stable under moderate perturbations of the six component weights (e.g., ±10 percentage points for the dominant 50% edge-overlap weight).

---

## Calibration Anchors

The following anchor papers were retrieved and compared:

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/WK6K1FMEQ1.md` (SPACE) | 6.75 | Much more comprehensive spatial cognition benchmark (15 tasks, multiple modalities, proper human baselines). Blueprint-Bench is weaker in scope and methodological rigor. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/UIFAJZ22ZF.md` (3D-PC) | 6.67 | Strong human-in-the-loop benchmark (33 human participants, 300+ DNNs) with rigorous controls. Blueprint-Bench's human baseline is far thinner. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/9Y6QWwQhF3.md` (FoREST) | 4.25 | Similar-level issues: synthetic data concerns and metric validity questions. Blueprint-Bench has a more natural task but similar validation gaps. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/uBhqll8pw1.md` (3D Reasoning VLMs) | 4.00 | Similar domain (indoor spatial reasoning), similar weaknesses (limited scope, overclaiming). Blueprint-Bench has a cleaner task design. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/2wwPG1wpsu.md` (LST-Bench) | 2.50 | Low-novelty benchmark with minimal insights. Blueprint-Bench is clearly stronger in originality and contribution. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Y1r9yCMzeA.md` (GraphArena) | 6.75 | Strong benchmark with rigorous evaluation framework and careful classification of outputs. Blueprint-Bench would benefit from similar rigor in failure analysis. |

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
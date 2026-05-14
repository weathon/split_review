Now I have a thorough understanding of the paper and the calibration anchors. Let me compile the final review.

---

## Summary

Blueprint-Bench introduces a benchmark for evaluating spatial intelligence in AI systems through the task of reconstructing 2D floor plans from apartment interior photographs. The benchmark evaluates LLMs (GPT-5, Claude 4 Opus, Gemini 2.5 Pro, Grok-4), image generation models (GPT-Image, NanoBanana), and AI agents (Codex CLI, Claude Code) on 50 apartments using a deterministic, rule-based scoring algorithm that compares room connectivity graphs and size rankings. All models score at or near a random baseline, while humans perform substantially better, revealing a genuine blind spot in current AI spatial reasoning. The paper provides open-source code, a dataset sample, and a public leaderboard.

## Strengths

- **Novel and genuinely challenging task.** Reconstructing a 2D floor plan from ~20 unordered interior photographs requires integrating multiple viewpoints, inferring room connectivity, and maintaining consistent scale — a non-trivial spatial integration challenge that is well within the input distribution of modern multimodal models yet tests capabilities they demonstrably lack (Figure 5, Figure 7).

- **Cross-architecture comparison on a unified metric.** The benchmark evaluates LLMs (via SVG generation), image generation models (direct image output), and AI agents (in a Docker environment) on the identical task with the identical scoring algorithm. This enables the first direct numerical comparison of spatial intelligence across fundamentally different model architectures (Section 2.2).

- **Human baseline validates the task is solvable.** Human participants, given the same images and rules, consistently produce floor plans with correct room connectivity (Section 3, lines 304-305), confirming that the gap between human and AI performance reflects genuine capability limits rather than an ill-posed problem.

- **Honest discussion of methodology limitations.** Section 2.4 explicitly acknowledges the tradeoffs in the scoring approach (size-rank matching, instruction-following confound, omission of room shape), which is a mark of intellectual honesty unusual in benchmark papers and helps readers properly interpret results.

- **Community infrastructure.** Open-source generation code, a dataset sample, and a public leaderboard with ongoing evaluation of new models provide a foundation for tracking progress in spatial intelligence over time (Section 2.2).

## Weaknesses

### Fatal

None.

### Major

- **Scoring metric confounds spatial accuracy with size estimation.** Room matching is performed by size rank (largest room = ID 1), not by spatial location. A model that correctly reconstructs all room adjacencies but swaps the ranks of two similar-sized rooms receives a depressed connectivity score because Jaccard edge overlap compares permuted IDs. The paper acknowledges this (Section 2.4: "the penalty of making a mistake in the size ranking causes additional penalties when scoring the connectivity") and reports that all human floor plans had correct connectivity but suffered from this penalty (lines 304-307). The composite weights (50/20/10/10/5/5) are presented without sensitivity analysis. This means the reported scores do not cleanly separate spatial layout accuracy from size estimation accuracy, weakening the benchmark's construct validity.

- **Instruction-following confounded with spatial reasoning.** The task imposes nine strict formatting rules (3px lines, red dots, no furniture, etc.) designed to make scoring robust. However, as the paper itself notes, models like GPT-4o and NanoBanana failed primarily due to rule violations rather than demonstrably poor spatial reasoning (Section 3, lines 283-291). The paper explicitly frames this as a conscious tradeoff (Section 2.4: "Blueprint-Bench should test spatial intelligence, not instruction following") but does not resolve the confound. Model rankings currently reflect a mixture of spatial intelligence and instruction-following compliance.

- **Extraction pipeline is unevaluated.** The HSV + flood-fill extraction algorithm (Section 2.3) is the foundation of all scoring — it detects rooms, doors, and connectivity from generated floor plan images. Yet its error rate against ground-truth annotations is never quantified anywhere in the paper. If the extraction algorithm systematically misidentifies doors or room boundaries for certain model outputs, all downstream scores and rankings are compromised. The paper compares against an LLM-based extraction alternative (Section 2.4) but never validates the chosen pipeline against human annotations.

### Minor

- **Dataset characterization is thin.** Beyond "50 apartments with approximately 20 images each," no statistics on apartment size, room count distribution, or layout variability are provided. The human baseline uses only 12 of these 50 apartments (Figure 7), limiting the statistical power of the human-AI gap estimate. With 50 samples, the benchmark's ability to produce stable model rankings is plausible but not demonstrated.

- **Agent evaluation is preliminary.** Only two agent scaffolds are tested. The paper itself reports that the Codex-based agent "never even looked at the image it created before submitting" (line 329-330), suggesting the agent configuration may not have been optimized to leverage iterative refinement. The conclusion that "iterative refinement through agents showed no advantages" (line 352) is drawn from insufficient evidence.

- **Composite score weights lack justification.** The linear combination (50% edge overlap, 20% degree correlation, 10% density, 10% room count, 5% door count, 5% door orientation) is presented without ablation studies or sensitivity analysis demonstrating that the ranking of models is robust to these weight choices.

### Trivial

None significant.

## Nice-to-Haves

- Validating the extraction pipeline against human-annotated floor plans (e.g., the human participants' outputs) would substantially strengthen confidence in the benchmark's scoring foundation.
- Reporting an auxiliary metric that measures rule adherence separately from spatial accuracy would help disentangle the instruction-following confound.
- Expanding the human baseline to all 50 apartments would improve the reliability of the human-AI gap estimate.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"Private dataset makes the benchmark non-reproducible and non-verifiable" (Harsh Critic #1).** REMOVED. The paper provides open-source code, a dataset sample, and a public leaderboard accepting community submissions. Private test sets with public leaderboards are standard practice in benchmark design (e.g., ARC, numerous competition benchmarks). The harsh critic frames this as a fatal structural flaw, but the community infrastructure provided is consistent with accepted benchmarking norms.

2. **"The claim of first numerical framework is overstated; numerous spatial-reasoning benchmarks exist" (Harsh Critic, Abstract & Introduction).** REMOVED. The paper's specific claim is about comparing spatial intelligence across fundamentally different model architectures (LLMs, image models, agents) on the same spatial reconstruction task using a unified numerical metric. This cross-architecture comparison on floor plan reconstruction does appear genuinely novel — existing spatial benchmarks either target a single model class (e.g., VLMs) or use VQA formats rather than generative reconstruction.

3. **"Prompts, hyperparameters, temperature, and agent configurations are entirely absent" (Harsh Critic, Method – Generation).** REMOVED per instructions. The parser strips appendix content; these details exist in the original submission. Cannot penalize authors for parser artifacts.

4. **"Figure 6 is mislabeled as Figure 8" (Harsh Critic, Figures).** REMOVED as a pure formatting nitpick. Does not affect the paper's scientific contribution.

5. **"No statistics given on apartment size, room count, image quality, or layout variability" (Harsh Critic, Method – Dataset).** RETAINED as a minor weakness but significantly WEAKENED. The paper does provide core statistics (50 apartments, ~20 images each). The harsh critic's framing implies complete absence of characterization, which is overstated. More detail would help but this is not a structural flaw.

6. **"The scoring metric is fundamentally misaligned with spatial reconstruction quality" (Harsh Critic #2).** PARTIALLY RETAINED as a Major weakness but WEAKENED. The paper explicitly acknowledges and discusses this limitation in Section 2.4, presenting it as a conscious design tradeoff. The criticism is valid but the harsh critic's claim that "reported scores do not reliably reflect how well a model captures spatial layout" overstates — connectivity graphs DO capture meaningful spatial information, just imperfectly due to the size-rank confound. I have retained this as a Major weakness with appropriate framing.

7. **Strength Finder claim: "The scoring algorithm provides a robust, model-agnostic similarity metric... the benchmark yields trustworthy numerical comparisons."** REMOVED. This strength conflicts with verified weaknesses about the scoring confound and unvalidated extraction pipeline. The scoring is automated and model-agnostic, but calling it "robust" and "trustworthy" is not supported given the acknowledged limitations.

8. **Strength Finder claim: "The strict formatting rules ensure evaluation is fully automated and resistant to scoring ambiguities, thereby increasing reproducibility and scalability."** RETAINED but MERGED into the instruction-following confound weakness discussion. This is a double-edged sword — the rules do enable automated scoring, but at the cost of confounding instruction-following with spatial reasoning.

## Novel Insights

The paper's finding that Claude Code with Claude 4 Opus attempted genuine iterative refinement — generating, inspecting, and correcting its floor plans across multiple attempts — yet still failed to outperform the random baseline is a genuinely interesting observation. It suggests that current agent scaffolds, even when they exhibit the right behavioral patterns (looking at their own output, identifying errors, retrying), lack the spatial reasoning capability to convert self-criticism into meaningful improvement. The fact that the Codex agent never even inspected its output further highlights how far current tool-use scaffolding is from the human approach of incrementally building a spatial model. These observations, while based on only two agent configurations, point toward a more fundamental limitation than mere prompting or tool design.

## Suggestions

- **Validate the extraction pipeline.** Run the HSV + flood-fill algorithm on the human participants' floor plans (where ground-truth annotations can be manually created) and report precision/recall for room detection, door detection, and connectivity extraction. This would directly quantify measurement noise in the scoring pipeline.

- **Report a disentangled breakdown.** Alongside the composite score, report edge overlap conditioned on correct size ranking (i.e., what the connectivity score would be if rooms were matched by spatial overlap rather than size rank). This would isolate spatial accuracy from size estimation.

- **Characterize the dataset more thoroughly.** Include histograms of room counts per apartment, apartment size distributions, and layout complexity metrics. This helps users understand the benchmark's coverage and difficulty spectrum.

- **For agent evaluation, report what the agents actually did** (tools called, images inspected, iterations attempted) — the paper already does this qualitatively for two agents, but a systematic breakdown across all 50 apartments would strengthen the claim that iterative refinement does not help.

## Score and Decision

### Anchor Comparisons

| Path | Paper | Avg Score | Comparison |
|------|-------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/gHRoX4vXm3.md` | MMSI-Bench | 6.50 | Superior: 1,000 expert-crafted questions, rigorous human validation, diagnostic error analysis, 37 models. Blueprint-Bench's evaluation is less rigorous. |
| `/home/wg25r/review_agent/human_reviews_2026/4c1gAsVd9C.md` | GIR-Bench | 5.50 | Stronger: 3 complementary evaluation perspectives, more thorough design. Blueprint-Bench has a more novel task but weaker metric validation. |
| `/home/wg25r/review_agent/human_reviews_2026/ddFN3lWpIr.md` | SpatialGenEval | 5.00 | Comparable but slightly stronger: larger scale (1,230 prompts), more models (23), but shares evaluation-metric concerns (VLM-based). |
| `/home/wg25r/review_agent/human_reviews_2026/7x6TxVIarj.md` | MME-Unify | 5.00 | Comparable: novel benchmark with acknowledged metric weaknesses. Blueprint-Bench's task is more novel; MME-Unify's evaluation is more comprehensive. |
| `/home/wg25r/review_agent/human_reviews_2026/fWWUPOb0CT.md` | SpatiaLab | 4.00 | Slightly above: Blueprint-Bench has more conceptual novelty (generative reconstruction vs. VQA) but weaker metric validation. SpatiaLab has larger scale (1,400 QA pairs). |
| `/home/wg25r/review_agent/human_reviews_2026/StD1GnueIb.md` | GeoReasoning | 3.50 | Stronger: Blueprint-Bench has a clearer novel contribution, better baselines, and a more interesting task design. |
| `/home/wg25r/review_agent/human_reviews_2026/dnjTXfIapC.md` | Benchmarking LLM Benchmarks | 2.50 | Significantly stronger: that paper is poorly written with thin analysis. Blueprint-Bench has a real empirical contribution. |

Blueprint-Bench sits between SpatiaLab (4.00) and SpatialGenEval/MME-Unify (5.00). The task is genuinely novel and the cross-architecture comparison fills a real gap. However, the unvalidated extraction pipeline and the size-ranking/instruction-following confounds mean the numerical results are not as trustworthy as they could be. The paper's honest discussion of these limitations (Section 2.4) is commendable but does not resolve them. I score this paper **4.5** — a borderline accept that contributes a valuable task concept and community infrastructure, but whose current numerical claims should be interpreted with appropriate caution.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
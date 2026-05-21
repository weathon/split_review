Now I have all the information needed to write the review. Let me compile it.

---

## Summary

Blueprint-Bench introduces a benchmark that evaluates spatial intelligence by requiring AI models (LLMs, image generation models, and agents) to convert apartment photographs into 2D floor plans, scoring them on room connectivity graphs and size rankings. The central empirical finding is that all tested models score near or below a random baseline (0.279), far below human performance (0.547), revealing a significant gap in current AI systems' spatial reasoning abilities even when the input modality is well within their training distribution. The benchmark is novel in enabling cross-modality comparisons on the same spatial task.

## Strengths

1. **Novel cross-modality comparison framework**: Blueprint-Bench is the first benchmark to numerically compare LLMs, image generation models, and agent systems on the same spatial reasoning task using a unified scoring metric. As the paper states, it "provides a numerical way of comparing different image generation models" and enables "the first direct comparisons between these models and their underlying LLMs."

2. **Graph-based evaluation that captures structural similarity**: The scoring algorithm goes beyond pixel-level metrics by extracting room connectivity graphs via flood-fill segmentation and computing six weighted components (Jaccard edge overlap at 50%, degree correlation at 20%, density at 10%, room count at 10%, door count at 5%, door orientation at 5%). This captures whether rooms connect correctly and whether size rankings are preserved — a more semantically meaningful similarity measure than SSIM or MSE.

3. **Empirical demonstration of a blind spot with in-distribution inputs**: The paper shows that even though apartment photographs are well-represented in training data, all tested models perform at or near a random baseline. GPT-5 and Gemini 2.5 Pro reach only 0.42 vs. human 0.547 and random 0.279, providing the strongest evidence for the paper's core claim.

4. **Systematic evaluation of iterative refinement via agents**: The paper tests whether the poor performance is an artifact of single-pass generation by evaluating Codex CLI and Claude Code in a Docker environment with full iterative refinement capability. The finding that agents show no significant improvement over single-pass models is non-obvious and strengthens the conclusion that the bottleneck is spatial reasoning, not access mode.

5. **Open-source release with private dataset split and public leaderboard**: The authors release code, a sample from the dataset, keep the majority of data private to prevent overfitting, and maintain a public leaderboard — enabling reproducible, ongoing evaluation as new models emerge.

## Weaknesses

### Fatal
None.

### Major

1. **The scoring algorithm partially conflates spatial reasoning with format compliance.** The extraction pipeline relies on strict formatting rules (3px black walls, green doors, specific red dot sizes, no extra details). A model that correctly infers spatial layout but draws a wall 2px wide, uses blue doors, or includes a window will have its score degraded or the output may not be parsable at all — even if spatial understanding is accurate. The paper acknowledges this directly: "Blueprint-Bench should test spatial intelligence, not instruction following" (Section 2.4), but the current design does conflate them. The paper argues this is "the right tradeoff" for robustness, but this means the reported scores cannot be unambiguously interpreted as measuring spatial intelligence independent of formatting ability. As a result, the headline claim that the benchmark reveals a "blind spot" in spatial reasoning is weakened: it may in part reveal a blind spot in precise format compliance, which is a less surprising failure mode. This is a limitation the authors recognize, but they do not quantify its impact (e.g., reporting compliance rates separately from spatial scores).

2. **The scoring metric is not validated against human judgment.** The composite weights (50% connectivity, 20% degree correlation, 10% density, 10% room count, 5% door count, 5% door orientation) are presented without justification or sensitivity analysis. The paper itself notes that humans scored only 0.547 because the metric penalizes size-ranking errors — and states "We suspect that one similarity scoring model would make the human's lead over the AI models much larger." This is an admission that the current weighting may dampen the very signal the benchmark is designed to detect. Without validation (e.g., correlation with human similarity judgments, or an ablation showing rank stability under different weightings), it is unclear whether the metric tracks what it is supposed to track.

### Minor

3. **Insufficient statistical evidence for the "statistically better" claim.** The paper states that "GPT-5, Gemini 2.5 Pro, GPT-5-mini, and Grok 4 statistically perform better than the random baseline," but provides no p-values, confidence intervals, or test details. Given the large error bars visible in Figure 5 and the proximity of model scores (~0.32–0.42) to the random baseline (0.279), this claim is unsupported. This is addressable with standard bootstrapping or permutation tests but undermines the paper's evidential core as written.

4. **Human baseline is limited.** Only 12 of 50 apartments were evaluated by humans (Figure 7 caption). The paper provides no details about the number of participants, their qualifications, or inter-annotator agreement. While the qualitative finding that humans got connectivity correct on all tested apartments is informative, the small sample size makes the quantitative comparison (0.547 vs. model scores) a tentative estimate rather than a stable upper bound.

### Trivial

5. The paper does not report compliance rates (what fraction of each model's outputs could be parsed by the scoring pipeline), which would help separate formatting ability from spatial reasoning.

## Nice-to-Haves

- **Failure analysis per model**: The paper describes failure modes qualitatively (NanoBanana includes furniture, GPT-4o omits red dots) but does not systematically categorize failures for the better-performing models. An analysis of whether models that score ~0.42 typically get connectivity right but size rankings wrong would illuminate what spatial sub-skills are lacking.
- **Per-apartment breakdown with cleaner presentation**: The appendix shows per-apartment scores for apartments 1–20, but the figure legend is garbled in the PDF (e.g., duplicate model names). This makes it hard to assess whether certain apartments drive the aggregate results.
- **Metric sensitivity analysis**: Showing how rankings change under different weightings would address concerns about arbitrariness in the composite score.

## Removed Points

*"The dataset is only 50 apartments — relatively small for a benchmark"* — 50 apartments with ~20 interior images each (~1000 total images) is a reasonable scale for a specialized spatial reasoning benchmark. No evidence is provided that this is insufficient for the reported effect sizes.

*"Figure captions are garbled (multiple model names repeated)"* — This is a known PDF extraction artifact, not an author error.

*"CodeX (GPT-6)" vs "Codex CLI" naming inconsistency* — Minor and likely reflects different backing LLM versions rather than an error.

*"Missing related works"* — The references include relevant prior work (NeRF, LayoutGPT, ARC, SWE-bench). Without external verification, claiming missing citations is speculative.

*"Figures... hurt readability"* — Presentational nitpick that is subjective; the numerical results are presented in tables and text as well.

*"The paper should have considered a two-stage evaluation"* — This is a constructive suggestion, not a flaw in what was done.

*"Could the metric be measuring a proxy?"* — General speculative concern without a specific anchor in the paper; the related specific point about format compliance is already captured in Major weakness #1.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an observation about the paper that the paper itself does not already make.

## Suggestions

1. **Report compliance rates per model** — what fraction of each model's outputs pass parsing — to separate instruction-following ability from spatial reasoning.
2. **Validate the scoring metric** against human pairwise similarity judgments (e.g., rank correlation) and/or demonstrate that model rankings are stable under different weightings.
3. **Add statistical significance tests** (bootstrap or permutation) for the key claim that certain models "statistically perform better than the random baseline."
4. **Expand the human baseline** to cover more apartments and report inter-annotator agreement.
5. **Provide a per-model failure analysis** — e.g., what fraction of errors are connectivity errors vs. size-ranking errors vs. formatting errors — to help the community understand what specific spatial sub-skills are lacking.

## Score and Decision

I anchor this paper against several comparable reviews from the corpus:

**Round 1 bracket**: 3.5–7.5. The paper is clearly stronger than weak papers (~3) like the diffusion-based floor plan generation paper (avg 3.0), but weaker than the comprehensive SPACE benchmark (avg 6.75, accepted poster).

**Round 2 narrowing**: 
- vs. PPNL (avg 4.75, rejected): Blueprint-Bench has a more creative task (floor plan from photos vs. 2D grid path planning), tests more model modalities (LLMs, image models, agents), and includes human baselines. However, PPNL has more thorough prompting/fine-tuning experiments. Blueprint-Bench is slightly stronger — maybe 5.0 vs 4.75.
- vs. MapEval (avg 4.5, rejected): Blueprint-Bench has a comparable profile — both are benchmark papers with methodological concerns. Blueprint-Bench's task is more novel but MapEval has a larger dataset. Blueprint-Bench is slightly stronger (5.0 vs 4.5).
- vs. OmniBench (avg 5.75, rejected): OmniBench had tri-modal evaluation and was rejected despite some 8s due to methodological concerns. Blueprint-Bench has similar methodology issues (scoring validation, statistical rigor) but a clearer task definition. Blueprint-Bench is slightly weaker (~5.0 vs 5.75).
- vs. VLM 3D Reasoning (avg 4.0, rejected): Blueprint-Bench is clearly stronger — more comprehensive evaluation, open-source release, clearer findings.

**Final position**: The paper has a genuine contribution — the task is creative, the cross-modality comparison is novel, and the finding that all models cluster near random is interesting and potentially important. However, the major weakness — partial conflation of spatial reasoning with format compliance, compounded by an unvalidated scoring metric and thin statistical evidence — keeps it below the acceptance threshold for ICLR. The paper would benefit from addressing these issues in a revision. I place it at **5.0**, which reflects a paper with a clear but imperfectly-supported contribution.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
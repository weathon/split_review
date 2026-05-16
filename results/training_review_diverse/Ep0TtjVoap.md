Now I have all the information needed to synthesize the final review.

## Summary

This paper presents ToRA, a series of Tool-integrated Reasoning Agents that interleave natural language reasoning with program-based tool use (computation libraries, symbolic solvers) for mathematical problem solving. The training pipeline involves: (i) collecting interactive GPT-4 trajectories on GSM8k and MATH, (ii) imitation learning on these trajectories, and (iii) output-space shaping that combines self-sampled valid trajectories with teacher-corrected invalid ones. Evaluated on 10 mathematical reasoning benchmarks, ToRA achieves double-digit absolute improvements over prior open-source models across all scales (7B–70B), with ToRA-34B reaching 50.8% on MATH — the first open-source model above 50% — competitive with GPT-4 Code.

## Strengths

1. **Strong and consistent empirical results across all model scales and datasets.** ToRA achieves 13%–19% absolute average improvements over prior open-source SOTA on 10 diverse benchmarks (Table 1). ToRA-7B (44.6% on MATH) surpasses WizardMath-70B by 22% absolute, and ToRA-34B (50.8%) is the first open-source model exceeding 50% on MATH, outperforming GPT-4's CoT result (42.5%) and approaching GPT-4-Code (51.8%) (Table 2, Fig. 1). These gains are large and consistent, not marginal.

2. **Clean ablation demonstrating that the interleaved format is strictly better than both rationale-only and program-only approaches.** When training LLaMA-2 on MATH data, the interleaved format outperforms rationale-only by 29.0% absolute and program-only by 6.7% absolute. With GPT-4 few-shot prompting, the improvements are 19.1% and 9.8% respectively (Fig. 4). This directly validates the paper's core design hypothesis.

3. **Output-space shaping (sampling + teacher correction) provides clear additive gains across model sizes.** Shaping yields average improvements of 3.4% on GSM8k and 4.0% on MATH, with the correction component alone adding up to 4.5% absolute without additional training data. Benefits hold even for the 70B model (47.3% → 49.7% on MATH) (Fig. 5).

4. **Thorough analysis of tool-use benefits and remaining limitations.** The paper provides library-usage patterns per MATH subtopic (Fig. 6), a manual error categorization on 100 trajectories (Table 3) identifying concrete remaining failure modes (21% diagram misinterpretation, 28% tool-use issues combined), and honest reporting of false negatives (5%). This gives actionable directions for future work.

5. **Demonstrates out-of-distribution generalization.** While WizardMath-70B regresses on TabMWP (57.5% → 49.8%), ToRA-70B achieves 74.0%, showing that tool-integrated reasoning generalizes better to unseen problem formats.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Single training run without variance estimates.** All reported results come from greedy decoding after a single fine-tuning run. Given the sensitivity of LLM fine-tuning to random seeds (data ordering, initialization), the absence of any variance measure means the stability of the observed improvements cannot be assessed statistically. This is a real evidential gap, though it is unlikely to change the overall conclusions given the large magnitude of the improvements (e.g., 22% absolute on MATH). Reporting mean and standard deviation over 2–3 seeds for at least the key benchmarks (GSM8k, MATH) would substantially strengthen the paper.

2. **The correction enumeration procedure in output-space shaping (§2.5) is underspecified.** The paper states that the model enumerates "possible preceding portions" of wrong trajectories at each line break and completes them with a teacher model. While the core idea is clear, the paper does not specify: (a) whether this enumeration is done left-to-right greedily or over all line splits, (b) what proportion of attempted corrections yields valid trajectories, and (c) the typical number of enumeration steps per trajectory. This makes the method harder to reproduce precisely than it should be.

### Trivial
None.

## Nice-to-Haves

- **Concrete examples of tool-use failure modes.** The paper reports percentages for "Inappropriate Tool Usage" (10%), "Syntax Error" (9%), and "Runtime Error" (9%) but does not show illustrative examples. A few trajectory excerpts would help readers understand what goes wrong in practice.
- **Comparison of data efficiency against baselines.** The paper uses 16k initial annotations plus 69k shaped trajectories, while WizardMath uses an unknown amount of ChatGPT-augmented data. A note on relative data efficiency would be informative.
- **Quantification of the computational cost** of the output-space shaping stage (GPT-4 calls for data generation, GPU-hours for sampling and correction) would help practitioners assess practical overhead.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Algorithm 1 not shown in main text; presumably in appendix"** — Removed per hard rules: the parser strips appendix content. The algorithm exists in the original submission.
- **"Tables are only shown as reference in text"** — Removed per hard rules: PDF-to-text parsing artifacts. Tables exist in the original submission.
- **"Teacher (CodeLLaMA-34B) creates possible circularity with CodeLLaMA students"** — Removed: this misunderstands teacher-student distillation. Using a larger model from the same family as teacher is standard practice and the ablation shows improvement over the no-shaping baseline, so any "shared bias" concern does not undermine the result.
- **"No discussion of failure cases in tool usage"** — Removed: factually wrong. The paper devotes §3.5 (lines 270–278) to a detailed error categorization, including 10% Inappropriate Tool Usage, 9% Syntax Error, and 9% Runtime Error.
- **"Missing related works"** — Removed per hard rules: I cannot verify existence of missing references without external sources.
- **"Formatting/style nitpicks"** — Removed per hard rules.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- **Add variance estimates.** Run 2–3 seeds for the 7B and 34B models on GSM8k and MATH, and report mean ± std. This would address the most substantiated concern about evidential rigor without requiring full-scale re-training.
- **Provide a pseudocode or worked example of the correction enumeration.** A short algorithmic description showing how a wrong trajectory is split at each line break, which prefix is retained, and how the teacher completes it would resolve the underspecification in §2.5.
- **Include a few failure case excerpts.** The error analysis percentages in Table 3 are useful; adding 2–3 concrete trajectory examples (one tool-usage error, one diagram misinterpretation) would make the analysis more informative.

## Score and Decision

This is a strong empirical paper with clear motivation, thorough experimentation, and well-supported claims. The two minor weaknesses (no variance estimates, underspecified correction procedure) are real but do not threaten the core contributions, which are large in magnitude and backed by careful ablations and analysis. The paper makes a significant contribution to open-source mathematical reasoning.

MY FINAL SCORE: <pineapple>8.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
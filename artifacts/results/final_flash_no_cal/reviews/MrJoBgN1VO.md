Now I'll produce the final consolidated review.

## Summary

This paper formalizes the **Program-to-Geometry** task — interpreting procedural drawing code (e.g., Asymptote) and reasoning geometrically over the resulting spatial configurations — and presents **GeoGramBench**, a benchmark of 500 problems organized by a three-level taxonomy (Primitive Recognition, Local Relation Composition, Global Abstract Integration). The authors evaluate 19 LLMs and find that even the strongest models fall below 50% accuracy on the highest abstraction level, revealing a fundamental weakness in symbolic-to-spatial reasoning. The core contribution is the benchmark itself, supported by a detailed construction pipeline and behavioral analysis.

## Strengths

1. **Clear formalization of a novel task.** Section 3.1 formally defines the Program-to-Geometry task, differentiating it from existing benchmarks focused on diagram interpretation or text-only math. The setup — providing procedural code as input and requiring numeric answers — is well-scoped and reproduces a practical evaluation scenario.

2. **Answer-leakage detection and mitigation.** The paper identifies two novel forms of contamination unique to procedural code (direct and indirect leakage, Figure 3) and implements targeted strategies (coordinate rescaling, code parameter masking) to prevent answers from being read directly from the code. This is a genuine methodological contribution that addresses a task-specific vulnerability.

3. **Rigorous construction of the core 392 problems.** The multi-stage human refinement pipeline (Section 4.3), involving four domain experts, decontamination, leakage prevention, and accuracy verification, produces a high-quality core set. This lends credibility to the benchmark's foundation.

4. **Clear and striking empirical finding.** Table 1 shows consistently that all 19 models score below 50% on the *Global Abstract Integration* level (e.g., GPT-5 at 39.26%, Qwen3-235B at 49.05%), with dramatic drops from the Compositional level. This result is robust across architectures and scales, making a compelling case that current LLMs have a fundamental weakness in spatial abstraction from code.

5. **Broad model coverage with fine-grained subtype analysis.** Evaluation spans 19 models (proprietary and open-source, 1.5B–235B parameters) with per-subtype breakdowns (angle, length, area, volume, ratio, count) at each difficulty level. This enables targeted diagnostics — e.g., angle problems are hardest at lower levels, area/volume at the Abstract level.

## Weaknesses

### Major

1. **No documented decontamination for the 108 augmented problems (AIME24, MATH-500, Mathverse).** The 392 core problems undergo a thorough decontamination pipeline (Section 4.3), but the 108 problems added in Section 4.4 are described with no mention of similar processing. This is especially concerning because Section 4.1 explicitly identifies MATH-500 as a source where "numerous instances" of answer leakage exist. For Mathverse, the paper mentions manual transcription of diagrams into matplotlib code, but no decontamination of the problem text or answer. For the AIME24 and MATH-500 subsets, no processing whatsoever is described. Since these 108 problems constitute 21.6% of the benchmark, their contamination status could inflate reported accuracies and undermine the reliability of the overall numbers. The authors should either (a) specify and apply the same decontamination steps to these subsets, (b) report results separately for the core 392 and augmented 108, or (c) clearly mark which problems may have residual leakage.

### Minor

2. **Taxonomy validation is thin.** The claim that geometric complexity (not reasoning complexity) drives difficulty is validated using only one model (QwQ-32B) on the 42-problem P_TC subset of MATH-500. The P_gg curve (86.1% → 81.7% → 75.0%) shows a modest decline; no statistical significance is reported, sample sizes per level are not given, and non-monotonicity in the P_g series (79.4% → 56.9% → 86.2%) is hand-waved as "largely independent of reasoning complexity." The taxonomy is conceptually well-defined and the Table 1 results across 19 models serve as indirect support (accuracy drops across levels for all models), but the explicit validation presented in Section 3.2 is too weak to stand alone. A multi-model replication on the full GeoGramBench would be straightforward and strongly recommended.

3. **RQ3 (CoT analysis) relies heavily on qualitative evidence.** The claim that chain-of-thought reasoning provides limited benefit for Program-to-Geometry and can lead to repetitive symbolic reasoning is supported primarily by one illustrative example (Figure 6) and a reference to the Token Budget Forcing experiment (Appendix E, not available for review). The paper does not include a direct quantitative comparison of accuracy with versus without CoT prompting, which is a natural and feasible experiment given the zero-shot setup. The accuracy trends across difficulty levels provide indirect support, but the CoT-specific claim would be significantly strengthened by an ablation.

4. **No uncertainty quantification for main results.** Each problem is evaluated with 8 samples at temperature 0.6, but the reported accuracies are means with no standard errors, confidence intervals, or variance measures. Without these, differences between models (e.g., GPT-5 at 75.01% vs. Qwen3-235B at 74.00%) cannot be assessed for statistical significance. While this omission is common in benchmark papers, the explicit sampling protocol makes the reporting of variance straightforward and valuable.

5. **Answer-parsing pipeline uses GPT-4o "when necessary" (Section 5.1).** This introduces a potential inconsistency in evaluation across problems. A fully deterministic, rule-based parser would be preferable for reproducibility, and the paper does not specify what triggers the fallback to GPT-4o or how frequently it is invoked.

6. **Figure 1(c) shows all four models at exactly 68.9% on the P_TC subset of MATH-500.** This uniformity across different architectures in a preliminary analysis is suspicious and may indicate a data or reporting error. While this does not affect the main benchmark results, it should be verified or explained.

### Trivial

7. **Failure pattern analysis (Section 6) is qualitative and based on non-systematic sampling.** The paper is transparent about this ("representative examples rather than exhaustive annotation"), but the analysis would benefit from reporting how many responses were reviewed and whether any form of inter-annotator agreement was used.

## Nice-to-Haves

- **Empirical verification of decontamination effectiveness.** The paper describes decontamination steps (coordinate rescaling, parameter masking) but does not test whether models that perform well on modified versions fail on the originals — e.g., a memorization probe. Demonstrating this would strengthen confidence in the benchmark.
- **Inter-rater reliability for taxonomy classification.** The three-level classification combines GPT-4o with human review; reporting agreement statistics (e.g., Cohen's κ) would help assess objectivity.
- **Comparison of zero-shot accuracy with and without CoT prompting.** A simple ablation would directly address RQ3.

## Removed Points

These points from the inputs were removed per the filtering rules, but are retained here for reference:

- **Model name garbling in Table 1**: The raw extraction shows names like "GP-4", "DeepSeek-K1", "v1.1-32B" etc. These are parser artifacts from PDF extraction; the original submission uses correct names (GPT-5, DeepSeek-R1, s1.1-32B). Removed per rule: parser errors are not author errors.
- **No Limitations section**: A dedicated limitations section is absent but this is a formatting preference, not a substantive weakness. Removed per rule: pure formatting/style nitpick.
- **Token Budget Forcing experiment relegated to appendix**: The appendix is stripped by the PDF parser, so the content exists in the original submission. Removed per rule: missing appendix content is a parser artifact.
- **Unsupported general-area concerns**: Several concerns framed as general-area sweeps ("could the metric be measuring a proxy?", "are confounders controlled?") without a specific anchor in the paper text. These are removed per filtering discipline.

## Novel Insights

The key insight that emerges from the reviews — beyond what the paper already states — is that GeoGramBench's most valuable contribution may be its **core 392 decontaminated problems** rather than the full 500. The paper would gain trust and clarity by explicitly separating the core from the augmented subset, making it clear which numbers are built on verified contamination-free data. A secondary insight is that the taxonomy, while intuitively sound, needs stronger empirical footing; the most convincing evidence for it actually comes from Table 1 (19 models, clear accuracy drops across levels) rather than the Section 3.2 validation, which the paper currently over-relies on.

## Suggestions

1. **Separate reporting for core vs. augmented subsets.** Present main results for the 392 core problems and the 108 augmented problems separately, or apply the full decontamination pipeline to all 500 problems. This single change would address the most serious weakness.

2. **Demonstrate the taxonomy gradient across multiple models.** The 19-model results in Table 1 already show that accuracy drops across Primitive → Compositional → Abstract for every model. Present this as an explicit validation of the taxonomy (e.g., a line plot of accuracy by level for multiple models) rather than relying solely on the QwQ-32B/MATH-500 analysis.

3. **Add bootstrapped confidence intervals to Table 1.** Given the 8-sample-per-problem protocol, computing standard errors or 95% CIs per model is straightforward and would significantly improve the interpretability of the results.

4. **Run a CoT vs. no-CoT ablation.** Use the same zero-shot prompt with and without the "Let's think step by step" instruction, and report accuracy differences across levels. This directly supports RQ3.

5. **Replace GPT-4o answer parsing with a fully deterministic parser** or document which problems require GPT-4o assistance and what the failure modes are.

6. **Verify the Figure 1(c) 68.9% uniformity**, either by correcting a potential error or explaining why four different models obtain identical accuracy on the same subset.

## Score and Decision

This paper makes a solid contribution: it formalizes an underexplored task, builds a carefully curated benchmark (notably the core 392 decontaminated problems), and uncovers clear limitations of current LLMs in spatial reasoning from code. The main result — that no model exceeds 50% on the highest difficulty level — is striking and likely to stimulate further work.

The weaknesses are real but addressable. The most significant is the insufficient documentation of decontamination for the 108 augmented problems, which could affect the trustworthiness of the aggregate numbers. The taxonomy validation is thinner than claimed, though the taxonomy itself is well-motivated and indirectly supported by the main results. The behavioral analysis of CoT is more qualitative than the paper suggests, and uncertainty metrics are absent.

These gaps do not invalidate the core contribution but should be resolved before the benchmark is deployed widely. I recommend acceptance with the expectation that the authors clarify the augmented subset's construction and strengthen the taxonomy validation in a revision.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>
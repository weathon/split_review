## Summary

SWE-Bench Atlas proposes a fully automated pipeline that transforms open-source GitHub pull requests into executable, multilingual software engineering benchmark instances. The framework introduces neuro-symbolic Dockerization, state-differential oracle extraction (covering both bug fixes and feature requests), adaptive log parsing, and hint-guided trajectory synthesis, producing 11,133 instances across 3,971 repositories and 11 languages. The paper also demonstrates that fine-tuning on a small number of Atlas-generated trajectories yields modest improvements on the held-out SWE-bench Multilingual benchmark.

## Strengths

- **Scale and diversity are genuinely impressive.** The benchmark covers 3,971 repositories and 11 languages—orders of magnitude beyond existing manually curated benchmarks like SWE-bench (12 repositories). This addresses a clear gap in the evaluation of LLMs for multilingual, repository-level software engineering.

- **The state-differential oracle is a practical innovation.** By handling both buildable and unbuildable *Before* states, the pipeline can extract feature request instances that prior automated pipelines (e.g., SWEE-bench) would discard. This expands the task scope beyond pure bug fixes.

- **Fine-tuning experiments show transfer value.** Adding just 145 Atlas trajectories to a synthetic baseline (SWE-Smith) improves pass@1 on SWE-bench Multilingual from 5/300 to 11/300, and scaling to 800 trajectories yields 20/300. The trend holds for the 32B model as well, suggesting the data captures high-difficulty signals not present in synthetic data.

- **The automation pipeline is end-to-end and well-motivated.** The paper identifies real bottlenecks (environment rot, flaky tests, weak test oracles, feature-request exclusion) and proposes explicit solutions (template-guided synthesis, QA layers, hint-guided data generation). The pipeline is described in sufficient detail to be replicable.

## Weaknesses

### Fatal

None.

### Major

1. **“Fully automated” claim is misleading due to human verification.** Stage 4 includes manual annotation by 82 pre-screened annotators for a “Gold Standard” subset. The paper does not clarify what fraction of the 11,133 instances underwent human review, nor whether the Atlas-1,782 evaluation subset is entirely manually verified. This human involvement significantly undermines the scalability claim and conflates the contributions of the pipeline with manual labor.

2. **No direct comparison against prior automated methods.** The paper repeatedly contrasts with SWEE-bench (SetUpAgent) and claims a 150% higher yield in Python, but provides no side-by-side experiment on the same set of repositories. Without a controlled comparison, the claimed superiority of the neuro-symbolic approach is unsubstantiated.

3. **Evaluation only on a small subset of the full dataset.** The leaderboard (Table 4) is computed on Atlas-1,782—less than 16% of the full 11,133 instances. It is unclear whether this subset is representative, and no difficulty calibration against existing benchmarks (e.g., SWE-bench, SWE-bench Multilingual) is provided. The paper cannot claim that the full benchmark is “high-fidelity” without evaluating it.

4. **Fine-tuning results are noisy and lack critical controls.** The improvement from baseline (5/300) to Atlas-Diversity (11/300) is a difference of only 6 instances. The 95% confidence intervals (e.g., +1.0 to +8.0) overlap substantially with the effect size. More importantly, there is no control condition that adds an equal number of *additional synthetic* trajectories to the baseline, making it impossible to attribute the improvement to real-world distribution rather than simply more data. The data-scaling experiments (200, 400, 800) mix human-reviewed and unreviewed data, confounding the effect of quality and quantity.

5. **Source-level contamination analysis is absent.** The paper emphasizes “contamination-resistant evaluation” via a living benchmark, yet the evaluation models (e.g., claude-sonnet-4.5, gpt-5-2025-08-07) are evaluated on a static snapshot. No temporal separation evidence (e.g., PR creation dates vs. model training cutoffs) is presented, nor is there any deduplication test against common pre-training corpora. The claim remains aspirational rather than validated.

6. **Hint-guided trajectory synthesis risks leaking the solution.** Hints are extracted from the ground-truth patch (function signatures, dependency graphs). Although a “Thought Regeneration” pass removes hint keywords, the paper provides no analysis of whether fine-tuned models still gain an unfair advantage, nor comparison against trajectories generated without hints. This undermines the claim that the method produces high-quality training data without information leakage.

### Minor

- **Yield figures are reported without error bars or confidence intervals.** The per-language Dockerization success rates (Table 2) and the total yield (Table 3) are given as point estimates without variance. Given the stochastic nature of LLM-based steps, this is insufficient for reproducibility assessment.
- **The “Neuro-Symbolic” framing is over-stated.** The approach is essentially an LLM with template-guided generation and iterative build feedback—a pragmatic engineering solution rather than a novel hybrid architecture. Terms like “Adaptive Parser Synthesis” similarly describe a standard LLM-with-feedback-loop.
- **No characterization of feature-request instances.** While the state-differential oracle enables feature requests, the paper never reports what fraction of the final 11,133 instances are feature requests vs. bug fixes, nor does it analyze whether models perform differently on the two categories.

### Trivial

None.

## Nice-to-Haves

- Run a controlled experiment where extra synthetic data (e.g., another 145 SWE-Smith trajectories) is added to the baseline to compare with the Atlas-Diversity condition.
- Provide a direct head-to-head comparison with SWEE-bench (SetUpAgent) on a shared set of Python repositories.
- Report F1 or precision/recall for the LLM-Judge curation step (Layer 3) against a human-annotated sample.
- Include timestamps of PRs used in Atlas-1,782 and check overlap with model training cutoffs.

## Novel Insights

None beyond the paper’s own contributions. The observation that repository diversity (Exp 3) improves fine-tuning more than solution density (Exp 2) is interesting but preliminary, given the small scale and lack of controls.

## Suggestions

1. Rename or qualify “fully automated”; clearly separate the automated pipeline from the human-verified subset.
2. Add an ablation evaluating each pipeline component (template-guided synthesis, adaptive parsing, QA layers) on a fixed set of candidate PRs.
3. Present the leaderboard on multiple held-out subsets with temporal separation to empirically substantiate the contamination-resistance claim.
4. Include a control in the fine-tuning experiments that adds an equal number of *synthetic* trajectories to the baseline.
5. Report the percentage of feature-request instances and analyze model performance separately for bugs and features.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>  
MY FINAL DECISION: <decision>Accept</decision>
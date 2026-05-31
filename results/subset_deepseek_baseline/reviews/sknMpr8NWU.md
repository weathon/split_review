## Summary

The paper introduces **Multi-Agent Evolve (MAE)**, a self-improving framework that instantiates three roles (Proposer, Solver, Judge) from a single LLM and trains them jointly via reinforcement learning without human-annotated data or external verifiers. The Proposer generates questions, the Solver answers them, and the Judge provides domain-agnostic reward signals. Experiments on Qwen2.5-3B-Instruct across mathematics, reasoning, coding, and general knowledge show consistent improvements over both the base model and an SFT baseline.

## Strengths

- **Novel framework design.** The three-role (Proposer–Solver–Judge) architecture with adversarial co-evolution and synchronized training is a creative extension of self-play beyond zero-sum settings, enabling self-improvement in general domains where verifiable rewards are unavailable.
- **Addresses an important problem.** Reducing reliance on human-curated data and verifiable environments for LLM reasoning improvement is a timely and high-impact research question.
- **Comprehensive empirical evaluation.** The paper evaluates on 22 benchmarks (both in-distribution and held-out), compares against a relevant baseline (AZR), includes ablation studies on each role and on quality filtering/format rewards, and analyzes training dynamics (difficulty curves, question pool growth).
- **Clear ablation results.** Disabling any single role degrades performance (2–3%), and removing question quality filtering leads to a substantial 3.72% drop, confirming the necessity of each component.

## Weaknesses

### Major

- **Evaluation methodology uses an LLM judge for most benchmarks, which is non-standard and potentially unreliable.** For standard benchmarks (GSM8K, MATH, ARC-C, etc.), the paper evaluates by having a strong LLM compare the model’s output (inside tags) against the ground truth and output TRUE/FALSE, rather than using exact-match or standard answer extraction. This introduces an extra source of noise and bias, and the paper does not provide any validation (e.g., correlation with exact match, human agreement, or calibration) to demonstrate the judge’s reliability. Without this, the absolute scores and ranking of methods are questionable. While the relative comparisons might hold, the community norm is to use deterministic evaluation for these well-established benchmarks.

- **Comparison with SFT is confounded by data quantity.** The SFT baseline is trained on only 967 seed questions, whereas MAE generates many additional training questions during the self-play loop. The claimed advantage over SFT may partly reflect having more training data rather than the self-rewarding multi-agent mechanism. An apples-to-apples comparison would require training SFT on the same number of generated questions (if ground truth could be obtained) or controlling for dataset size.

### Minor

- **Only one base model (Qwen2.5-3B-Instruct) is tested.** Claims about “scalability” are premature without experiments on larger models or different architectures. The authors acknowledge this as future work, but the current evaluation limits generality.
- **No statistical significance or multiple seeds reported.** The main results table shows single numbers without error bars or standard deviations. Given the stochasticity in RL training, it is unclear whether the reported improvements (e.g., 58.51 vs 57.72 Overall Avg for MAE zero vs AZR) are reliable.
- **The AZR baseline comparison may not be entirely fair.** AZR is designed for verifiable environments (coding, math) and does not target general domains. MAE’s advantage on general benchmarks is expected, and the comparison would be more informative if AZR were adapted or if an alternative general-domain self-play baseline were included.

### Trivial

- The “quality filtering” threshold (0.7) and reward weights (1/3 for each Proposer term, 0.5 for Solver terms) appear somewhat arbitrary with no sensitivity analysis reported.

## Nice-to-Haves

- Validate the LLM judge evaluation by reporting agreement rates with exact-match on a subset of benchmarks where exact match is feasible (e.g., GSM8K, MATH).
- Include experiments on a second base model (e.g., Llama-3-8B or Qwen2.5-7B) to demonstrate generality.
- Report training cost (GPU hours, number of generated samples) and compare with baselines.

## Novel Insights

None beyond the paper’s own contributions. The observation that question difficulty curves correlate with benchmark improvements (Desirable Difficulty Effect) is a nice empirical finding, but it is more a validation of the framework’s design than a new insight.

## Suggestions

- Address the evaluation concern by providing a validation study of the LLM judge (e.g., Cohen’s kappa against exact-match on a subset of benchmarks) or switch to standard answer extraction for benchmarks where it is feasible.
- Add a controlled experiment where SFT is trained on the same number of questions encountered by MAE during training (either by using ground-truth answers for generated questions or by upsampling the seed set) to disentangle data quantity from training algorithm.

## Score and Decision

The paper presents a genuinely novel framework and tackles an important problem with a reasonable experimental design. The main concern is the unconventional evaluation methodology (LLM judge for standard benchmarks), which affects confidence in the reported results. The contribution is strong enough to warrant acceptance conditional on addressing this issue.

**MY FINAL SCORE:** <score>6</score>
**MY FINAL DECISION:** <decision>Accept</decision>
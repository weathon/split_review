## Summary

ARENABENCHER proposes a framework for automatically evolving static benchmarks by (1) extracting the core "ability" of each test case, (2) generating candidate rewrites via LLM that preserve task intent, (3) scoring candidates via multi-model feedback (aggregated loss across a sampled subset of models), and (4) iteratively refining with in-context demonstrations. Experiments on GSM8K (math), CommonsenseQA (reasoning), and AdvBench Harmful Behaviors (safety) show that the updated benchmarks are harder, maintain high alignment and fairness, and that multi-model feedback (m=3) consistently outperforms single-model feedback (m=1).

## Strengths

- **Multi-model feedback (m=3) consistently outperforms single-model feedback (m=1) across all tested settings.** Table 1 shows large and consistent differences: e.g., Llama-3.2-3B on GSM8K drops 47.7% (m=3) vs. 32.8% (m=1); on Harmful Behaviors ASR increases 13.6% (m=3) vs. 8.0% (m=1). This provides concrete evidence that aggregating signals from multiple models produces harder, more diagnostic updates — directly supporting the paper's core methodological innovation over prior single-model perturbation work.

- **Ability extraction yields high alignment verified by both automated judge and human annotators.** Section 3.1 describes structured extraction of `capability_tested`, `core_concept`, `operations_required`, `difficulty_aspect` per test case. Table 2 reports alignment scores of 90.6–94.1% across all domains. Human annotation on 100 GSM8K samples (Section 4.2) finds 95/100 aligned with original intent and 96/100 correct, providing independent validation beyond automatic metrics.

- **Fairness is formalized and measured explicitly.** Section 3.5 defines a quantitative fairness metric based on deviation from uniform failure rates. Table 2 shows ARENABENCHER₃ achieves 85.5% fairness on Harmful Behaviors (up from 82.9% original), 87.8% on GSM8K, and 92.8% on CSQA. The uniform model sampling strategy (Section 3.3) is a principled mechanism to avoid model-specific bias.

- **Evaluation across three diverse domains demonstrates generalizability.** Tables 1 and 2 cover GSM8K (math reasoning), CSQA (commonsense reasoning), and AdvBench Harmful Behaviors (safety) — three fundamentally different task types. The framework improves difficulty, preserves alignment, and maintains fairness in all three domains.

## Weaknesses

### Fatal
None.

### Major

1. **No baseline comparisons against alternative benchmark augmentation methods.** The paper's related work (Section 2) discusses MATH-Perturb, ARST, gradient-based adversarial rewriting, and simple paraphrasing, yet the experiments contain zero comparisons against any of these or even a "random perturbation" / "LLM paraphrase without multi-model feedback" baseline. The only comparison is m=1 vs. m=3 within ARENABENCHER itself. This means the paper cannot distinguish between "multi-model feedback helps" and "any LLM-based rewriting produces harder questions." For a new-method paper, this is a critical gap — the core claim that multi-model feedback yields better benchmarks than prior single-model approaches is asserted but never empirically validated against those approaches.

2. **The central motivation (data leakage / contamination resistance) is never empirically tested.** The entire paper is framed around data leakage as the core problem: the abstract calls it "a scalable path to continuously evolve benchmarks" against contamination; the introduction states "models can exploit memorized content rather than demonstrating true generalization." Yet the experiments do not test whether the updated benchmarks are more resistant to data leakage — no contamination probes, no n-gram overlap analysis, no comparison showing that models relying on memorization perform differently on the updated vs. original items. The paper evaluates difficulty, separability, fairness, and alignment, none of which directly address contamination resistance. This gap between motivation and evaluation is substantial.

3. **Limited evaluation scope weakens several key claims.** (a) The model pool has only 6 models, all open-source, all under 8B parameters, from 3 families. With K=6, m=√K≈3 uses half the pool per evaluation — the "diverse multi-model feedback" claim is stretched. (b) GPT-4o — used for generation, verification, and alignment judgment — is not in the evaluation pool, making the difficulty increase partly explainable by a strong teacher generating questions for weaker students. (c) Results are reported as point estimates without variance or significance testing across multiple seeds/runs, so it is unclear whether the m=3 advantage over m=1 is statistically significant or within random fluctuation. (d) No sensitivity analysis for hyperparameters (R=3 iterations, n=5 candidates, top-3 demonstrations).

### Minor

1. **Separability decreases on multiple benchmarks under the default (m=3) configuration.** Table 2 shows separability drops from 15.2→12.2 (GSM8K, −20%), 17.1→14.5 (Harmful Behaviors, −15%), and 8.5→7.2 (CSQA, −15%). The paper acknowledges this as "expected" due to difficulty compression, but it directly undermines one of the four stated desiderata — a benchmark update that reduces the ability to distinguish between models is partially self-defeating.

2. **The LLM verifier (same model as generator) misses clear failures.** Figure 2 shows a compelling failure case where the updated question is underspecified and unsolvable, yet passed the automated verifier. The paper is transparent about this, but it raises concerns about the reliability of the same-model generation+verification pipeline. The human evaluation on 100 samples (~7.7% of GSM8K) is too small to estimate the true error rate systematically, and no inter-annotator agreement metric is reported.

3. **The √K sampling rule lacks principled justification for this setting.** Citing Breiman (2001) and Chen & Guestrin (2016) — random forest papers where √K refers to feature subsampling at each split, not model subsampling for ensemble combination — does not constitute a principled justification. No empirical evidence is provided that m=3 is optimal here versus other choices like m=2, m=4, or a varying-m ablation.

### Trivial
None.

## Nice-to-Haves
- Compare against at least one reasonable baseline: single-model adversarial rewriting (optimize against one model, test on all), simple LLM paraphrasing with no multi-model scoring, or random perturbations.
- Add contamination-resistance experiments (n-gram overlap analysis, probing memorization, or comparing models on original vs. updated items to isolate memorization effects).
- Report variance across multiple independent runs.
- Include at least one model comparable to or stronger than the generator (GPT-4o) in the evaluation pool.
- Systematically audit the LLM verifier's false positive rate.

## Removed Points
- **Criticism that evaluation metrics are "endogenous" / tautological**: Removed as overstated. The difficulty metric (1 − max accuracy) is related but not identical to the selection criterion (average loss). The fairness metric is not completely by-construction — uniform sampling ≠ uniform failure rates. The GPT-4o-as-generator-and-verifier concern is real but already captured in Minor weakness #2.
- **Generic Strength Finder claims**: Removed generic framing such as "this paper addresses an important problem" — these lack specific evidence anchors.
- **Criticism about missing code/data release**: Removed per instructions — the appendix was stripped and we cannot verify this.

## Novel Insights
The most interesting observation from the reviews is the tension between the paper's data-contamination framing and its actual evaluation. The method of using multi-model feedback to iteratively evolve benchmarks is genuinely novel and well-executed, but the paper would be stronger if it reframed its contribution around producing harder, fairer, more diagnostic benchmarks rather than claiming contamination resistance without testing it. The transparency in Figure 2 (showing a genuine failure case) is unusual and valuable, but it also inadvertently reveals a blind spot in the automated verification pipeline that deserves more systematic investigation.

## Suggestions
1. **Add baselines before any other revision.** Compare against (a) single-model adversarial rewriting (optimize against one model), (b) simple LLM paraphrase without multi-model feedback, (c) random perturbation. This is the minimum needed to establish that multi-model feedback is the mechanism driving improvement.
2. **Either test contamination resistance or reframe the motivation.** If contamination resistance cannot be tested, de-emphasize it and focus the narrative on producing harder, fairer, more diagnostic benchmarks — which the method does demonstrably achieve.
3. **Report variance** across multiple runs of the stochastic components (model sampling, LLM generation) to establish significance of the m=3 vs. m=1 differences.
4. **Broaden the evaluation scope** to include at least one model in the pool comparable to or stronger than the generator, to test whether the method remains effective when the generator is not the strongest system.

## Score and Decision

**Calibration evidence (all anchors retrieved):**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| `sKYHBTAxVa.md` (LiveBench) | 7.33 | 1 | Much stronger — large-scale benchmark, extensive evaluation, contamination tested |
| `ymt4crbbXh.md` (AutoBencher) | 6.25 | 1 | Stronger — has baselines, ablations, human eval, explicit comparisons |
| `gjfOL9z5Xr.md` (DyVal) | 6.50 | 2 | Stronger — dynamic evaluation with controllable complexity, extensive experiments |
| `chfJJYC3iL.md` (LiveCodeBench) | 6.25 | 2 | Stronger — comprehensive coding benchmark, contamination analysis |
| `599F4CZ0HB.md` (Bench-O-Matic) | 6.00 | 1 | Stronger — has metrics, cost analysis, human preference correlation |
| `rAylWUIKtu.md` (Retro-Holdouts) | 4.25 | 1 | Comparable — similar limitation of narrow scope, but clearer methodology |
| `ikqcUzUogm.md` (BIND) | 4.75 | 2 | Comparable — also lacks baselines, but has extensive test suite |
| `YGDWW6rzYX.md` (ZeroSumEval) | 3.00 | 1 | Much weaker — critical missing details, weak evidence |

Round 1 bracket: **4.0–5.5**. Round 2 narrowing: compared to BIND (4.75) and Retro-Holdouts (4.25), ARENABENCHER has a more novel method and broader domain coverage but shares the weakness of missing comparisons. Compared to AutoBencher (6.25), Bench-O-Matic (6.00), and DyVal (6.50), ARENABENCHER is clearly weaker on evaluation completeness. The method itself is well-designed and the m=3 vs. m=1 comparison provides internal evidence, but the lack of baselines against prior work is a critical gap that places the paper below the acceptance threshold.

**Final score: 5.0**

**Decision: Reject**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
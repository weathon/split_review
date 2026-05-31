## Summary

ARENABENCHER is a framework for automatic benchmark evolution that combats data leakage in LLM evaluation. Given an existing benchmark and a model pool, it extracts the "core ability" of each test case, generates candidate rewrites using an LLM, verifies them with an LLM judge, and selects candidates that maximize aggregated loss across a √K-sampled subset of models. The process iterates using top candidates as in-context demonstrations. Experiments on GSM8K, CommonsenseQA, and the AdvBench Harmful Behaviors dataset show consistent difficulty increases with high alignment scores and stable fairness.

## Strengths

- **Timely and well-motivated problem.** Data contamination is a genuine and growing threat to LLM evaluation integrity; the paper clearly positions ARENABENCHER within the literature and provides concrete motivation.
- **Coherent multi-component design.** The combination of ability extraction, LLM-judged verification, multi-model feedback with balanced sampling, and iterative in-context refinement is a principled end-to-end approach not previously combined in this way.
- **Multi-domain coverage.** Evaluating on math reasoning, commonsense reasoning, and safety demonstrates the framework's generality.
- **Human validation.** Annotating 100 GSM8K test cases with three expert annotators (95% aligned, 96% correct) provides meaningful signal beyond automated metrics.
- **Intellectual honesty.** The paper includes a detailed failure case (Figure 2) showing a generation that passes the verifier but is actually unsolvable and semantically misaligned, which reflects well on the authors' candor.

## Weaknesses

### Fatal
None.

### Major

1. **No comparison to baseline augmentation methods.** The paper acknowledges MATH-Perturb, PAIR, and Automatic Robustness Stress Testing in related work, yet the experiments compare only m=1 vs m=3 ARENABENCHER configurations. Without comparison to simpler alternatives such as value perturbation, paraphrasing, or single-model adversarial rewriting, the incremental value of the multi-model design and ability-preservation pipeline cannot be established.

2. **Separability decreases across almost all settings.** Separability is listed as a core desideratum and an explicit motivation for the framework ("improved model separability" is claimed in the abstract). Yet in Table 2, separability falls in 4 of 6 domain × variant comparisons (GSM8K: 15.2→11.3/12.2; CSQA: 8.5→7.2/9.4). The explanation—that difficulty compression squeezes variance—does not fully hold: well-designed updates should be able to increase both difficulty and separability simultaneously. This undermines a primary stated claim.

3. **Model pool is limited to 1B–7B open-source models, while GPT-4o is the generator/verifier.** All six evaluation models are small-to-mid-scale (LLaMA 1B/3B, Qwen 4B, Mistral 7B). Candidate generation is performed by GPT-4o (closed, much larger). It is unclear whether the evolved benchmarks are harder for frontier-scale models or whether they represent GPT-4o's blind spots dressed as generalizable benchmark items. The central claim of "model-agnostic evolution" is not validated beyond small open-source models.

4. **Safety domain ethical gap.** The safety experiments report increasing attack success rates (ASR) on the Harmful Behaviors dataset as a positive outcome. This conflates benchmark hardening with generating more effective adversarial prompts. The paper does not discuss how evolved harmful prompts should be handled, whether they represent a dual-use risk, or how to prevent the framework from becoming a jailbreak generation pipeline.

### Minor

1. **Difficulty metric defined as 1 - max-model accuracy.** This favors benchmarks that defeat the single best model, not overall model discrimination. A benchmark where all models score near-zero would score perfectly on this metric while being diagnostically useless.

2. **√K heuristic motivation is loose.** Citing XGBoost's feature-subsampling rule (designed for decorrelating decision trees) as justification for model-subsampling in a fundamentally different context is a weak analogy. No empirical ablation over the size of the sampled subset is provided.

3. **Iterative refinement not ablated.** Only R=3 rounds are used without any analysis of performance vs. number of rounds, making it unclear how much the iterative component contributes.

4. **GPT-4o verifier does not catch the failure in Figure 2.** The failure case passes LLM-based verification yet is clearly invalid. The paper acknowledges this but offers no remediation strategy beyond "future work."

### Trivial

- The description of the √K rule cites both Chen & Guestrin (XGBoost) and Breiman (Random Forests) but neither result directly motivates this choice in the LLM setting.

## Nice-to-Haves

- Compare against at least one alternative augmentation baseline (e.g., numerical perturbation, paraphrase-only, single-model adversarial) to demonstrate the value added by each ARENABENCHER component.
- Include at least one frontier-scale model (e.g., GPT-4o, Claude-3) in the evaluation pool to validate that evolved benchmarks are also harder for large models.
- Provide a per-domain analysis of where separability does/does not hold and why.

## Novel Insights

The insight that selecting candidates by aggregated multi-model loss rather than single-model loss reduces model-specific artifacts and exposes more generalizable failure modes is practically useful and empirically supported in the m=1 vs m=3 ablation. The ability-extraction-then-preserve mechanism—structuring task intent as a rubric before generation—is a meaningful improvement over free-form paraphrasing. However, the empirical validation of these insights is limited by the small, homogeneous model pool, which weakens the strength of the cross-model generalization claim.

## Suggestions

- Add a controlled ablation comparing: (a) ARENABENCHER (full), (b) ARENABENCHER without ability extraction, (c) ARENABENCHER without iterative refinement, (d) a simple LLM-paraphrase baseline, to isolate each component's contribution.
- Evaluate at least one large or frontier model (≥13B or proprietary) in the model pool to validate the "model-agnostic" claim.
- Revise the difficulty metric to incorporate mean or median model performance rather than a max-based definition to better reflect general hardness.
- Explicitly discuss the ethical framework for the safety domain: e.g., evolved harmful prompts should be filtered or watermarked rather than released as a benchmark.

## Score and Decision

The paper addresses an important problem with a coherent framework and honest reporting. However, the absence of method comparisons to baselines, the fact that the primary desideratum of separability decreases in most settings, the small and narrow model pool, and the unaddressed ethical concerns in the safety domain collectively represent gaps that substantially weaken the paper's support for its claims. These are addressable in a revision but are significant enough to warrant rejection at the current state.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>
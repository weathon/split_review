Now I have all the information needed. Let me compose the final review.

## Summary

This paper proposes a framework for LLM routing formulated as a multi-armed bandit problem. The key technical contributions are: (1) **model identity vectors** learned via a deep IRT model trained on evaluation scores and pairwise comparisons, enabling compact capability representations; (2) a **preference-conditioned routing policy** that accepts user-specified trade-offs between performance and cost at inference time; (3) an **action-space-aware architecture** (permutation-invariant network over model identity vectors) designed to handle arbitrary and changing sets of LLM candidates; and (4) an **efficient quizzing mechanism** requiring only 10–50 evaluation prompts to onboard new models. Experiments across 5 LLM benchmarks show that the single policy matches or outperforms per-configuration PPO baselines and a strong score-prediction baseline, and that it can incorporate unseen models without retraining.

## Strengths

- **Single policy outperforms task-specific baselines across diverse settings.** The proposed routing policy achieves comparable or better performance than separately trained PPO policies (one per LLM set and preference) across all 5 benchmarks and multiple model configurations, while requiring only one policy for all settings. This is a genuine empirical result supporting the core design decision (action-space awareness + preference conditioning). (Section 4, Figure 2)

- **Generalization to unseen models with few evaluation scores is demonstrated.** When entirely new models (not used in IRT or policy training) are added, the routing policy—without any retuning—outperforms a score-prediction baseline and matches a PPO policy that was specifically trained on those new models. This holds even when identity vectors are derived from as few as 10–50 selected prompts. (Section 4, Figure 3)

- **Multi-objective RL formulation with action-space-aware architecture is technically sound.** The permutation-invariant conditioning on model identity vectors, costs, and predicted scores allows the same policy to handle arbitrary numbers of LLMs. The vectorized value function and preference-conditioned policy gradient follow established multi-objective RL principles adapted to the routing setting. (Sections 2.1, 2.4)

- **IRT-based model identity vectors with pairwise data improve generalization.** Using both evaluation scores and pairwise comparisons within a variational IRT framework produces dense representations that support zero-shot routing to unseen models. The stratified quizzing mechanism for efficient identity-vector estimation is well-motivated. (Section 2.3)

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **No error bars, confidence intervals, or number of runs reported.** The experimental results are presented as point estimates with no indication of variance. Given the multiple sources of randomness (RL training, stratified prompt selection, preference sampling, mixup interpolation), the reader cannot assess whether the reported improvements (especially the small gaps in some configurations) are statistically reliable. This is a standard expectation for empirical ML papers and its absence weakens the credibility of the comparative claims. (Figures 2 and 3; Section 4)

- **Generalization to unseen LLMs is tested only within-distribution.** The "new models" in Figure 3 are from the same benchmark (OpenLLM v2) that the IRT model and routing policy were exposed to during training. While these specific models are genuinely unseen, the prompts used for quizzing and evaluation are from a benchmark whose prompt distribution the system has encountered before. A stronger test would involve models whose capabilities differ substantially from the training distribution (e.g., a code-specialized model tested on code-only tasks, when the training benchmarks lack code tasks). As it stands, the claim that the policy "generalizes to any set of LLMs" is supported only for within-distribution generalization, not for out-of-distribution scenarios. (Section 4, Figure 3)

### Trivial

- **Ablation results lack numerical detail.** The paper states that "context information, pretraining stage, and mixup regularization all contribute" and references Figure 4, but provides no numerical values or summary statistics (e.g., "removing pretraining increases cost by X% at fixed accuracy"). The visual figure is present, but the absence of even summary numbers in the text makes it hard to gauge the magnitude of each component's contribution. (Section 4, Ablation Studies)

## Nice-to-Haves

- **Expand the generalization experiment to out-of-distribution model types** (e.g., domain-specialized models, models released after the training cutoff). This would directly address the "any set of LLMs" claim at its strongest.
- **Add a random-sampling baseline for the quizzing mechanism** to demonstrate that stratified sampling (based on prediction difficulty) provides meaningful gains over selecting the same number of prompts uniformly at random.
- **Adaptive cost modeling** accounting for varying input lengths, as the paper already acknowledges in the conclusion. This would improve practical deployment realism.

## Removed Points

These points were flagged by reviewers but removed per verification rules:

1. **"Ablation figure not included in the provided text"** — Figure 4 is referenced and present in the paper (line 162: "Figure 4: Ablation studies..."). The image may not render in text extraction, but the figure exists. Removed as factually incorrect.

2. **"PPO baseline details not provided"** — These details would appear in the appendix, which is stripped during parsing. Removed per rule about missing appendix content being a parser artifact.

3. **"RouteLLM comparison is restricted to two-model case"** — The paper transparently acknowledges this limitation ("RouteLLM is not applicable, as it is restricted to two candidates"). This is not a weakness of the paper; it is a limitation of the baseline. Removed.

4. **"Cost treated as constant"** — The paper explicitly acknowledges this as a limitation in the conclusion ("we treat the cost of each model as a constant, but in practice, the cost can vary depending on factors such as input length"). Removed as the paper already addresses it.

## Novel Insights

The most interesting observation emerging from this review is the tension between the **architecture-level claim** (which is genuinely general—a permutation-invariant network over identity vectors can handle any set size by design) and the **empirical validation** (which tests only within-distribution generalization). The fact that the PPO baseline requires separate training for each configuration while the proposed single policy matches it is strong evidence that the action-space-aware design works as intended. However, the real open question—and the one that would make the paper truly impactful—is whether the IRT-derived identity vectors are robust enough to support routing decisions for models with *qualitatively different* capability profiles than those seen during IRT training. The current experiment answers "yes" for models from the same benchmark family, but leaves the harder question unanswered. The quizzing mechanism's stratified sampling is clever, but without a random-sampling ablation, it is unclear whether the stratification itself contributes meaningfully or whether any small set of prompts would suffice.

## Suggestions

1. **Add error bars.** Report means and standard deviations over at least 5 independent runs (RL training seeds, prompt selection seeds) for the main results in Figures 2 and 3. This is the single most impactful improvement the authors could make.

2. **Test generalization on out-of-distribution models.** Add at least one experiment where the "new" models belong to a family or domain not represented in the IRT training data (e.g., a code model, a domain-specific fine-tune, or a model released after the data cutoff). Even a small-scale experiment would substantially strengthen the generalization claim.

3. **Include summary numbers for the ablation study.** Add a sentence or table to the main text with concrete numbers (e.g., "removing the supervised pretraining increases average LLM cost by X% at the same accuracy level on HELM-Lite").

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
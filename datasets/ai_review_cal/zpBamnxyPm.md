- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 6, 5
Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper investigates why predicting downstream capabilities of large language models from pretraining compute has remained difficult. Using 5 model families and 12 multiple-choice benchmarks, it traces the transformation chain from log probabilities → vocabulary-level probability → choices-normalized probability → Accuracy/Brier Score, showing that each step progressively degrades per-sample score-compute correlations. The root cause is identified: downstream metrics require comparing the correct choice against specific incorrect choices, meaning their predictability depends not just on how probability mass concentrates on the correct answer with scale, but also on how mass fluctuates on incorrect alternatives. The paper provides per-sample correlation distributions (CCDFs) across the chain, visualizes the breakdown, and offers preliminary evidence on how correct and incorrect probability masses co-vary with compute.

## Strengths

- **Systematic empirical demonstration across diverse models and benchmarks.** The paper evaluates 5 model families (Pythia, Cerebras-GPT, OLMo, INCITE, LLM360) on 12 multiple-choice benchmarks using 3 correlation metrics (Spearman, Pearson, Kendall), and consistently finds that the transformation chain degrades score-compute correlations. Figures 3-4 and the summary statistics in Figure 4 show a reproducible ordering: log probability > vocabulary probability > choices-normalized probability ≥ Brier Score > Accuracy, holding across model families and benchmarks.

- **Per-sample correlation distributions as a diagnostic.** Rather than only reporting aggregate trends, the paper computes per-sample correlations and visualizes their full distribution via complementary CDFs (Figure 2). This reveals that degradation affects individual samples differently — many retain strong correlations while others lose them — providing a finer-grained picture than aggregate scaling curves alone. This methodological choice is well-motivated and effectively communicated.

- **Identifying the incorrect-choice dependency as the source of degradation.** The paper pinpoints the specific step where predictability breaks down: the normalization from $p_\theta^{\text{Vocab}}$ to $p_\theta^{\text{Choices}}$ (Equation 3), which introduces dependence on the probability mass of specific incorrect alternatives. Figure 5 shows this strikingly — knowing the vocabulary-level probability of the correct choice gives almost no information about the choices-normalized probability or accuracy for many samples. This diagnosis is concrete and mechanistically clear.

- **Preliminary characterization of correct/incorrect mass co-variation.** Section 5 and Figure 6 provide initial evidence that probability mass on correct and incorrect choices positively covaries with compute (though with large spread), pointing toward a possible path for ultimately predicting metrics like Accuracy.

## Weaknesses

### Fatal

None.

### Major

None — the paper's core empirical finding (the degradation chain) is well-supported by the data. The weaknesses below are significant but addressable.

### Minor

- **The analysis is entirely per-sample, but the motivating question ("predicting downstream capabilities") concerns aggregate benchmark scores.** The paper explicitly states "All the scores we discuss are per-datum" (line 92) and builds its evidence entirely on per-sample correlation distributions. While the mechanism logically extends to aggregate metrics (aggregate accuracy is the average of per-sample decisions, and if per-sample decisions are hard to predict the aggregate inherits this), the paper never verifies this directly. Showing that *average* benchmark scores (the quantities actually used in scaling-law and emergence debates) also exhibit degraded correlation with compute would directly bridge the per-sample findings to the practical claim made by the title. The current evidential gap weakens the direct connection between the experiments and the central narrative.

- **The "novelty of the mechanism" framing is somewhat overstated.** The paper states it "reveal[s] the mechanism" (abstract) of degradation, but the mechanism — that multiple-choice accuracy requires comparing the correct choice against specific incorrect choices — is inherent in the *definition* of these metrics. The contribution is not the discovery of a previously unknown mechanism but rather the *empirical quantification and demonstration* that this dependency causes measurable degradation in correlation with compute. The paper would be better served by a more precise framing (e.g., "we quantify the degree to which standard multiple-choice metrics lose their signal with compute, and trace this loss to the dependency on incorrect alternatives") rather than implying the mechanism itself is a novel discovery.

- **The recommended alternative metric ($p_\theta^{\text{Vocab}}(\text{Correct Choice})$) is not validated as a capability signal.** Takeaway #3 recommends that practitioners use $p_\theta^{\text{Vocab}}(\text{Correct Choice})$ as a "scaling-predictable signal for capabilities" because it correlates well with compute. However, the paper does not show that this metric actually tracks meaningful capability improvements — only that it is monotonic with compute. A metric that is smooth by construction could miss qualitative shifts or fail to distinguish models with very different actual abilities. The paper uses qualifiers ("perhaps," "arguably") but the recommendation nonetheless goes beyond what is demonstrated.

- **No uncertainty quantification on correlation statistics.** The paper reports point estimates (mean, median, AUC, Wasserstein distance) for correlation distributions across samples, but does not quantify uncertainty (e.g., bootstrapped confidence intervals). Given that conclusions rely on the *ordering* of metrics across conditions, error bars would strengthen the evidence that the ordering is robust and not driven by noise.

- **Alternative explanations for the degradation are not tested or discussed.** The paper attributes the entire degradation in predictability to the incorrect-choice dependency. However, other factors could contribute — for example, metric saturation at high compute, or the compression from log-probability to probability space (which could reduce variance at high values). A brief discussion of alternative hypotheses and why the incorrect-choice explanation is dominant would make the analysis more complete.

### Trivial

None.

## Nice-to-Haves

- **Show aggregate-level correlations.** Directly verifying that average benchmark scores (not just per-sample scores) exhibit degraded correlation with compute would bridge the per-sample findings to the practical question of aggregate predictability. This is the single most impactful addition the paper could make.

- **Compare to pretraining loss scaling.** The paper invokes pretraining loss scaling as a contrast but never computes pretraining loss for the same models. Even a brief comparison would anchor the "explanation" less speculatively.

- **Test or discuss alternative explanations** such as metric saturation, log-probability to probability compression, or resolution artifacts, to strengthen the causal attribution to incorrect-choice dependency.

## Removed Points

These points were raised by reviewers but are removed for the following reasons:

- *"No comparison to pretraining loss"* (as a weakness, not a nice-to-have) — The paper's scope is about downstream metrics, not pretraining loss. Mentioning pretraining loss as a contrast in the introduction does not obligate the paper to compute it. Moved to Nice-to-Haves.
- *"The paper does not actually compare pretraining loss scaling to downstream metric scaling in its own data"* (Harsh Critic, Section-by-Section notes) — Same reasoning. The paper does not claim to present a new pretraining scaling law; this is not a required experiment.
- *"For Pearson it could matter that they use compute, not log compute"* — The paper reports consistent results across Pearson, Spearman, and Kendall, so the concern does not undermine the findings. Rank correlations are invariant to monotonic transforms, and Pearson results are reported as consistent.
- *"Section 5 adds limited evidence to the main claim"* — The paper explicitly frames Section 5 as "preliminary evidence" and states "whether... can be fit... is unclear" and "leave this challenge to future work." This is honest scoping, not a weakness.
- Several generic/formatting/speculative points from the Harsh Critic's section notes that are observations rather than weaknesses.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a perspective on the paper's findings that the paper itself does not already articulate.

## Suggestions

1. Add an experiment showing that *aggregate* benchmark scores (averaged over all test samples) also exhibit degraded correlation with compute across the transformation chain. This directly connects the per-sample analysis to the motivating question of predicting downstream capabilities.
2. Soften the "reveal the mechanism" framing to more accurately describe the contribution as an empirical quantification and characterization of the degradation caused by the incorrect-choice dependency.
3. Add bootstrapped confidence intervals or other uncertainty estimates to the correlation distribution statistics (mean, median, AUC) to confirm the robustness of the observed ordering.
4. Either validate $p_\theta^{\text{Vocab}}(\text{Correct Choice})$ as a capability metric (e.g., does it correlate with held-out task performance?) or explicitly state that this is a conjecture supported only by correlation with compute.

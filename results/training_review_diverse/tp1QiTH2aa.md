Now I have thoroughly verified all claims against the paper. Let me produce the final consolidated review.

---

## Summary

QWICK formulates synthetic data generation as a budget-limited multi-armed bandit problem with *per-question* model selection. The algorithm maintains a separate model pool for each question, progressively adding more expensive models only when the cheaper ones fail to achieve sufficient utility, and selects among available models using a utility-driven formula with exploration. Evaluated on GSM8K, MATH, and MBPP, QWICK reduces costs by 33–50% compared to UCB1 while maintaining fine-tuned accuracy, and generates up to 2.1× more valid samples at the same cost.

## Strengths

- **Novel per-question model selection with a budget-aware stopping criterion.** QWICK departs from dataset-level selection by maintaining a per-question model pool and a condition (Algorithm 1, line 16) that stops adding more expensive models when their potential utility falls below the current empirical maximum. This is a principled adaptation of budget-limited bandits to the SDG setting. (Section 3.2, Algorithm 1)

- **Demonstrated cost reduction of up to 50% without loss of fine-tuned accuracy.** On MBPP, QWICK achieves 50% lower cost than UCB1 while maintaining comparable accuracy; on GSM8K and MATH the cost reductions are 40% and 33% respectively. At the same cost, it generates up to 2.1× more valid data. (Figure 4, Section 4.1)

- **Flexible utility metric that generalizes beyond binary rewards.** The reward can be an ORM score (mapped to [0,1]) instead of binary correctness. QWICK with ORM achieves up to 2.2× higher total reward than UCB1 under the same budget. (Section 4.3, Figure 6)

- **Convergence analysis providing insight into per-question selection behavior.** Figure 5a visualizes how QWICK starts with the cheapest model and progressively switches to larger models only for difficult questions, converging to a per-question optimal choice — while dataset-level methods converge to a single (sub-optimal) model for all questions (Figure 5b). This mechanistically explains the advantage of question-wise selection. (Section 4.2)

- **Empirical evidence that different models excel on different questions.** Table 1 shows on MATH that no single model dominates utility across all questions (Gemma-2-2B is best on ~20%, Gemma-2-9B on ~35%, Gemma-2-27B on ~45%). This observation directly motivates the question-wise approach and is validated by the data. (Table 1)

## Weaknesses

### Fatal
None.

### Major

- **The main experimental comparison lacks a dataset-level cost-aware baseline.** The primary baseline used in Figure 4 is a variant of UCB1 that the paper explicitly states "does not take into account the cost associated with model calls." Comparing a cost-aware method against a cost-ignorant one trivially favors the former, but this does not isolate whether the benefit comes from *per-question* selection or simply from being cost-aware. The paper mentions fractional KUBE (§2.2) as the natural budget-limited bandit algorithm but never implements it as a baseline in the main results. Figure 5b does compare against a "utility-driven" dataset-level method (which favors the cheapest model) on MATH with one model family, but this analysis is limited in scope — it does not extend across all three datasets and model pools used in the main evaluation. This gap weakens the central claim that per-question selection is superior to dataset-level selection.

### Minor

- **Coverage and diversity metrics are never explicitly defined.** The paper uses these terms throughout (Figures 3, 4, 6) and builds arguments around them, but no formal definition is provided. From context, "diversity" appears to refer to the number of valid responses generated and "coverage" to the fraction of questions with at least one valid response, but the paper should state this clearly. This makes results harder to verify and reproduce.

- **The uniform generation length assumption in the stopping condition is untested.** Line 158 states "we assume uniform generation lengths across models, as only the per-token cost \(a_i\) is used to estimate the reward-to-cost ratio." However, the stopping condition (line 16) uses \(a_i\) directly without accounting for potential length differences across models. Larger models often produce longer reasoning chains (especially with CoT prompting), which would make their actual cost higher than implied by per-token price alone. The paper does not provide evidence that generation lengths are approximately equal across the model pools used. Note that this criticism applies specifically to the stopping condition — the main selection formula (lines 20/23) uses \(\hat{c}\) (empirical cost) which captures actual per-response cost.

- **No confidence intervals, standard deviations, or multi-seed results are reported.** All experiments appear to be single runs. Since the bandit algorithms involve stochastic model selection and generation, variance could be non-negligible. Error bars over multiple seeds (e.g., 3–5) would strengthen confidence in the reported improvements.

- **Hyperparameters \(\alpha=16\) and \(\beta=0.5\) are set without ablation or sensitivity analysis.** The paper states "we simply set" these values (line 160). With \(\alpha=16\), the exploration term \(\frac{1}{\alpha}\sqrt{\frac{2\ln t}{n}}\) is very small (e.g., <0.03 after a few pulls), making selection nearly purely exploitative. It is unclear whether performance is robust to moderate changes in these values or whether they were tuned.

- **The ORM experiment overrides the ORM score to 0 for wrong answers** (line 284: "we enforce a reward of 0 if the answer does not match the ground truth"). This means the "continuous" reward is still binary for all incorrect responses, which somewhat limits the claim of a fully flexible utility metric. This design choice should be explicitly justified or discussed as a limitation.

- **Best checkpoint selection may inflate reported accuracy.** The paper saves checkpoints every 20 steps (math) or 5 steps (programming) and reports the highest accuracy. Reporting final accuracy or the average over a range would be cleaner and more reproducible.

### Trivial

- **The stopping condition used in experiments is not precisely specified.** The paper mentions "such as reaching a target number of correct answers or hitting the inference cost threshold" (line 162). The specific stopping criteria used (maximum valid responses per question, as suggested by Tab. 2) should be stated explicitly when describing the algorithm.

## Nice-to-Haves

- **Add "always use the cheapest model" as a baseline.** This simple heuristic would contextualize the gains and is easy to implement. Figure 5b partially addresses this (utility-driven baseline selects cheapest model), but extending it to all three datasets would be informative.
- **Report and discuss the average generation lengths per model** to either validate or correct the uniform-length assumption.
- **Provide explicit definitions of coverage and diversity** and optionally describe how they are computed.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The utility formula (lines 16 and 20) uses only per-token price \(a_i\) in the denominator"** — This is factually incorrect for lines 20/23, which use \(\hat{c}_{i,t,j}\) (empirical cost, capturing actual per-response cost). Only line 16 uses \(a_i\) directly. *Reason: factual error.*

2. **"The scaling factor \(\frac{\min_{i'} \hat{c}_{i',t,j}}{\hat{c}_{i,t,j}}\) is unexplained"** — The paper explicitly states this factor "normalizes... encourages exploration of underused models" (line 160). *Reason: the paper does explain it; the criticism is inaccurate.*

3. **"The algorithm's utility formula uses only per-token price... creating a disconnect"** framed as a structural flaw — This overstates the scope of the issue. The main selection formula (lines 20/23) uses \(\hat{c}\) (actual tracked cost), not a proxy. The uniform-length assumption affects only the stopping condition (line 16). *Reason: downgraded from structural flaw to Minor weakness.*

## Novel Insights

The most interesting insight across the reviews is the observation that with \(\alpha=16\), QWICK's exploration term is negligible, meaning the algorithm operates in a nearly purely exploitative regime. Whether this is a deliberate design choice (relying on the stopping condition to handle model pool expansion) or a hidden assumption deserves explicit discussion. The harsh reviewer's framing of this as "arbitrary hyperparameters" is too dismissive — it may actually reflect a meaningful property of the algorithm — but the lack of ablation means the community cannot tell. This could be an interesting design insight if validated.

## Suggestions

1. **Add a dataset-level cost-aware baseline (fractional KUBE applied dataset-wise) to the main results (Figure 4).** This is the single most important addition — it directly tests whether per-question selection adds value beyond utility-based bandits.
2. **Define coverage and diversity explicitly** early in the experimental section, and report results with confidence intervals over multiple seeds (3 runs minimum).
3. **Ablate \(\alpha\) and \(\beta\)** with at least 3–4 values each to demonstrate robustness, or justify the near-purely-exploitative regime (\(\alpha=16\)) as a deliberate design choice.
4. **Validate the uniform-length assumption** by reporting average generation token counts per model on a sample of questions from each dataset, and discuss whether the stopping condition should be adjusted if lengths vary.
5. **Report final accuracy instead of best checkpoint** to avoid potential inflation.

## Score and Decision

The paper proposes a well-motivated and novel algorithm for cost-effective synthetic data generation. The per-question bandit formulation is a clean idea, and the experimental results show meaningful empirical gains. However, the evaluation has a structural gap: the main comparison is against a cost-ignorant baseline (UCB1) without also including a dataset-level cost-aware baseline, which would be needed to fully support the paper's claims about the benefits of per-question selection. This gap is addressable in revision (fractional KUBE applied dataset-wise is straightforward to implement) and is partially mitigated by the secondary analysis in Figure 5b. The additional Minor issues (undefined metrics, untested assumptions, no error bars, unablated hyperparameters) further weaken the empirical rigor but are fixable.

Given that the core contribution is novel, the method is sound, and the weaknesses are addressable without changing the paper's structure, the paper merits acceptance conditional on addressing the Major weakness.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
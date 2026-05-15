Now I have thoroughly read the paper and verified the reviewer claims against the paper text. Let me synthesize the final review.

---

## Summary

The paper proposes QWICK (Question-Wise model pICK), an algorithm for cost-effective synthetic data generation (SDG) in LLM post-training. QWICK frames model selection per question as a budget-limited multi-armed bandit problem, tracking each model's empirical reward-cost ratio to dynamically select the most cost-effective model for each question. The paper evaluates QWICK on math (GSM8K, MATH) and programming (MBPP) datasets, reporting 33–50% cost reductions and up to 2.1× more valid samples compared to dataset-wise UCB1, while maintaining comparable fine-tuned model accuracy.

## Strengths

- **Well-motivated, practically important problem.** The paper grounds the work in real cost disparities (e.g., o1 vs. Llama 70B pricing, ~150× difference) and addresses a genuine bottleneck in SDG pipelines.
- **Principled algorithm design.** QWICK extends the fractional KUBE framework with per-question tracking, a pool-expansion rule (gradually introducing more expensive models only when justified), and a blended question-level/dataset-level reward term. These modifications are clearly explained and connected to the bandit literature.
- **Empirical cost savings across multiple datasets.** Figure 4 shows that QWICK achieves comparable or better fine-tuned model accuracy at 33–50% lower cost than the primary baseline on GSM8K, MATH, and MBPP.
- **Convergence analysis validates per-question selection.** Figure 5a demonstrates that QWICK progressively assigns questions to different models, converging to question-specific cost-effective choices — supporting the paper's core insight that models have heterogeneous utility across questions.
- **Flexibility of the utility metric.** The ORM ablation (§4.3) shows QWICK generalizes beyond binary correctness rewards to more nuanced reward signals, demonstrating the method's broader applicability.

## Weaknesses

### Fatal
None.

### Major

- **The primary baseline (dataset-wise UCB1) is cost-unaware, making headline cost-reduction claims less informative.** As the paper itself states (§4.1, baseline description), UCB1 "focuses on maximizing the reward but does not take into account the cost associated with model calls." The 40–50% cost reductions are relative to this baseline. A cost-aware dataset-level method (e.g., always using the cheapest model, or fractional KUBE applied globally) would clarify whether the gains come from question-level selection or simply from being cost-aware. While §4.2 partially addresses this with a comparison against "utility-driven dataset-wise" methods on MATH, this appears only in an analysis section, not in the main experimental results across all datasets. Without this comparison in the headline experiments, the core contribution of *question-level* selection is not cleanly isolated from the simpler insight of *cost-awareness*.

- **Coverage and diversity metrics are never formally defined.** The paper repeatedly invokes "coverage" and "diversity" to explain accuracy improvements (Figures 3, 4, 6; §4.1, §4.3) and claims QWICK achieves higher values on both. However, no definition, formula, or computational procedure is provided for either metric. The reader cannot verify what these quantities represent, how they differ across methods, or whether the conclusions drawn from them are valid. This renders a significant part of the experimental narrative around data quality unverifiable.

- **Fine-tuning evaluation is confounded by dataset size differences.** QWICK generates 69–112% more valid samples than baselines (Figure 4, second row). The fine-tuning protocol (§4.1) uses fixed 200 steps (math) or 20 epochs (programming) regardless of how many valid samples each method produces. Therefore, models fine-tuned on QWICK's data are trained on more examples. The observed accuracy (comparable or slightly better) could partly reflect quantity of training data rather than higher per-example quality. The paper's claim of "comparable quality at lower cost" conflates quantity with quality in the downstream evaluation.

### Minor

- **Pool expansion condition is optimistic and may cause premature expansion.** The condition `max_{i∈P(x_j)} (r̂_{i,t,j} / a_i) < 1 / a_{l+1}` (Algorithm 1, line 16) assumes the next model achieves reward 1 on its first attempt. If the next model performs poorly on that question, the expansion may be unwarranted. The paper does not analyze the impact of this optimistic assumption.

- **Uniform generation-length assumption is not validated.** The paper notes it "assume[s] uniform generation lengths across models" (line 158) because only per-token cost is used for utility estimates. In practice, larger models often produce longer reasoning chains, which would affect cost estimates and potentially bias utility calculations. The paper does not test this assumption or discuss its practical impact.

- **Hyperparameters α=16 and β=0.5 are set without sensitivity analysis.** These are described as simply chosen (line 160: "we simply set α=16 and β=0.5") with no ablation studying how performance varies with these choices. Since α controls the exploration-exploitation trade-off and β controls the question-level vs. dataset-level reward mixing, their impact on the method's behavior is unclear.

- **Key experimental details are underspecified.** The per-question stopping condition `Stop(x_j)` is taken as input (Algorithm 1, line 4) and examples are given (line 162), but the exact criterion used in experiments is not specified. Similarly, the budget B is an input but how it is set or varied across experiments is not explained.

### Trivial

- The ~150× cost comparison between o1 and Llama 70B (§1, line 12) conflates API pricing margins with intrinsic computational cost. This is a minor framing issue that does not affect the technical contribution.

## Nice-to-Haves

- **Control for dataset size in fine-tuning:** Subsampling QWICK's output to match the number of valid samples from baselines, or training for the same number of total tokens, would cleanly separate data quality from data quantity in the downstream evaluation.
- **Sensitivity analysis on α and β:** An ablation varying these parameters would clarify the robustness of the method.
- **Formal definitions of coverage and diversity:** The paper should either define these metrics or, if they are standard in the SDG literature, provide a citation and brief explanation.
- **Single-model baselines:** Including baselines such as "always use the cheapest model" and "always use the most accurate model" would further contextualize the benefit of multi-model question-level selection.
- **A cost-aware dataset-level baseline in the main results:** This would directly test whether question-level selection outperforms dataset-level cost-awareness, strengthening the paper's core contribution.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"2.1× in abstract vs. 2.2× in ORM ablation" inconsistency**: These figures come from different experiments (binary reward in §4.1 vs. ORM reward in §4.3) and refer to different evaluation settings. Not an inconsistency. *(Removed: factually wrong/misleading.)*

- **"No test on MATH or MBPP for ORM experiment"**: The ORM is specifically fine-tuned on GSM8K (Feng et al., 2023); testing on MATH or MBPP would require a separate ORM or cross-domain evaluation that is outside the stated scope of this ablation. *(Removed: scope creep — the paper tests generalization of the utility signal, not cross-dataset generalization.)*

- **"The exploration term design choice is not justified over simpler alternatives"**: The paper describes the cost-normalization term and its purpose ("normalizes...encourages exploration of underused models," line 160). While a deeper justification would strengthen the paper, the lack of exhaustive justification for one design choice over all alternatives is not a substantive weakness. *(Removed: overly specific, not a core flaw.)*

## Novel Insights

The reviewers converge on a consistent picture: the paper identifies a genuine problem and proposes a sensible algorithm, but the evaluation framework needs significant tightening. The most novel observation that emerges from the cross-review is that the paper's primary experimental design inadvertently bundles *cost-awareness* with *question-level selection* — the headline cost reductions could be achieved by a cost-aware dataset-level policy, which would be a much simpler solution. This highlights a broader methodological pitfall in the SDG literature: when demonstrating the benefit of fine-grained selection, the baseline must control for the lower-level insight (cost-awareness) before claiming the higher-level one (per-question adaptivity). The paper's §4.2 analysis partially addresses this but should be front-and-center.

## Suggestions

1. **Add a cost-aware dataset-level baseline to the main results (§4.1).** The simplest version is "always use the cheapest model" (which maximizes utility at dataset level). This would directly isolate the benefit of question-level selection and significantly strengthen the paper's core claim.

2. **Formally define coverage and diversity metrics** in a new subsection or the appendix. Even a brief operational definition (e.g., coverage = fraction of questions with at least one valid response; diversity = some measure of response variation) would make the analysis reproducible.

3. **Control for dataset size in fine-tuning.** Either subsample QWICK's output to match baseline valid-sample counts, or report results with both fixed-step and fixed-token training to separate quality effects from quantity effects.

## Score and Decision

The paper addresses a timely and important problem with a principled algorithm. The core idea — per-question model selection for cost-effective SDG — is sound and the convergence analysis (Figure 5a) provides meaningful evidence that the method behaves as intended. However, the experimental evaluation has significant gaps: the main baseline is cost-unaware (making the headline cost reductions partially attributable to a trivial insight), key metrics (coverage, diversity) are undefined, and the fine-tuning evaluation confounds data quality with data quantity. These weaknesses prevent the paper from fully establishing its central claims in the current form. Substantial revision is needed before the paper can be fairly evaluated.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
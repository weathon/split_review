- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 5, 5, 5
Now I have a thorough understanding of the paper. Let me compose the final consolidated review, carefully verifying each reviewer claim against the actual paper text.

---

## Summary

QWICK proposes a per-question model selection algorithm for synthetic data generation under budget constraints, formulated as a multi-armed bandit with knapsacks. The method tracks empirical reward, cost, and trial counts per question-model pair to select the most cost-effective model for each question, starting with the cheapest model and expanding the pool only when justified by potential utility. Experiments on GSM8K, MATH, and MBPP show cost reductions of up to 50% and up to 2.1× more valid samples compared to baseline methods, while maintaining fine-tuning accuracy.

## Strengths

1. **Measured cost reduction with maintained quality**: The paper reports specific cost savings — up to 50% on MBPP, 40% on GSM8K, and 33% on MATH — while achieving comparable or identical fine-tuning accuracy (Section 4.1, Figure 4, first row). These are concrete, cross-dataset results that directly support the practical utility claim.

2. **Increased valid sample yield at fixed budget**: QWICK produces 69%, 112%, and 106% more valid synthetic samples on GSM8K, MATH, and MBPP respectively compared to UCB1 at the same cost (Section 4.1, Figure 4, second row). This validates the reward-maximization objective of the algorithm.

3. **Generalization to non-binary rewards (ORM)**: Section 4.3 demonstrates that QWICK generalizes beyond binary correctness rewards to an Outcome Reward Model, achieving up to 2.2× higher reward than UCB1 while improving accuracy, diversity, and coverage (Figure 6). This shows flexibility of the utility metric beyond the simplest setting.

4. **Convergence analysis clarifies algorithm behavior**: Figure 5a traces how QWICK starts with the cheapest model and progressively adds expensive models only on questions where the cheaper one underperforms, providing empirical evidence for the algorithm's exploration-exploitation dynamics (Section 4.2).

## Weaknesses

### Fatal
None.

### Major

1. **Missing cost-aware dataset-level baseline in main experiments**. The paper's central claim is that *per-question* model selection outperforms dataset-level selection. Yet the main experiments (Section 4.1, Figure 4) compare only against random selection and dataset-wise UCB1, which is explicitly cost-unaware (Section 4.1: "does not take into account the cost associated with model calls"). A cost-aware dataset-level comparator (e.g., applying fractional KUBE globally to pick one model per iteration for all questions) would isolate whether QWICK's gains come from per-question adaptation or merely from being cost-aware. Section 4.2 partially addresses this by comparing against a utility-driven dataset-level policy on MATH (Figure 5b), showing QWICK achieves higher total reward and coverage. However, this comparison is restricted to one dataset (MATH) with one model family (Gemma), and the "utility-driven" dataset-level baseline (always pick the cheapest model) is a trivial policy. The main results across three datasets lack this distinction, making it unclear whether the per-question mechanism is essential to the reported gains.

2. **No variance or statistical significance reported**. All results are single runs without error bars, confidence intervals, or repeated trials (no mention of random seeds or repetition anywhere in the experimental setup). Fine-tuning is known to be sensitive to random seeds, and the accuracy differences between QWICK and UCB1 are modest in some cost regimes (e.g., near 0.7 on MATH in Figure 4). Without variance estimates, the reader cannot assess whether the observed differences are reliable or within noise. This is a significant gap for an empirical paper that makes quantitative claims about cost savings (e.g., "up to 50%").

### Minor

1. **Inconsistent cost model in pool expansion condition**. The algorithm's decision to add a more expensive model (line 16 of Algorithm 1: max_i \hat{r}_{i,t,j}/a_i < 1/a_{l+1}) uses per-token cost *a_i*, implicitly assuming uniform generation lengths across models. However, the main selection formula (lines 20, 23) uses the empirical cost *\hat{c}_{i,t,j}*, which directly accounts for per-response token count differences. The paper acknowledges this assumption (line 69/158: "Note that we assume uniform generation lengths across models...") but does not justify it with evidence or analyze its impact. Depending on actual token length patterns, this could cause systematic over- or under-exploration of higher-cost models.

2. **No hyperparameter sensitivity analysis**. The algorithm sets α=16 and β=0.5 without any analysis of how performance varies with these choices. The exploration weight α and the question-vs-dataset-level reward balance β are nontrivial to set, and the paper provides no evidence that the chosen values are robust across datasets or model pools. Additionally, Section 4.2 uses β=1 for "clearer illustration" while the main experiments use β=0.5, but the sensitivity of the convergence pattern to β is not discussed.

3. **Stopping condition not formalized in method section**. The stopping condition Stop(x_j) is given as an input to Algorithm 1 and described briefly in Section 3.2 ("such as reaching a target number of correct answers or hitting the inference cost threshold"), but its concrete realization — a per-question cap on valid responses — is only discoverable in the experimental settings (Section 4). Formalizing this in the method section would improve clarity.

### Trivial

- "Figure 2 is mentioned but not clearly referenced in the text" — the figure appears without inline citation in the method section.
- The paper does not report actual per-model token counts, which would help assess the uniform-length assumption noted in Weakness #1.

## Nice-to-Haves

- A brief complexity analysis of the iterative per-question algorithm (especially for large datasets) would be useful.
- Reporting per-model token generation statistics would allow readers to assess the uniform-length assumption directly.
- The β=1 setting in Section 4.2 is explained as "for clearer illustration" but noting the sensitivity of convergence dynamics to this parameter would strengthen the analysis.

## Removed Points

These points were flagged in the inputs but are removed from the main review for the following reasons:

- *"Fractional KUBE formula error" (Harsh Critic §2.2)*: The cited text is garbled by the PDF parser (e.g., "πt = argmaxi rcˆii,,tt +ci1,t 2n lin, tt"). The original formula in the submission is likely correct; this is a parser artifact, not a paper error. **Removed by Hard Rule (parser artifacts).**

- *"The code is anonymized and hosted, which is good for reproducibility"*: This is a positive observation, not a weakness. **Removed (not a weakness).**

- *"The paper's own analysis in §4.2 illustrates that a dataset-level utility-driven method would converge to the cheapest model... but this comparison is qualitative and not quantitatively benchmarked"*: The paper *does* provide quantitative comparison in Figure 5b (total reward and coverage), and states "The proposed method outperforms the baselines on both metrics." This critique is factually incorrect about the absence of quantitative comparison. **Removed by Hard Rule (factually wrong).** However, the related concern about this comparison being restricted to one dataset is retained in the Major Weaknesses above.

- *Strength Finder claim #3: "Per-question selection outperforms dataset-wise selection: Section 4.2 explicitly shows..."*: This strength is partially supported, but the verification is limited to MATH only. Retained in modified form as a strength but with contextual caveat.

- *"Could the as-yet-unknown performance of the new models invalidate the findings?"*: Not present in the inputs; included here as a hypothetical.

- Generic/superficial strengths from the Strength Finder: The strength finder's observations about "addressing an important problem" are removed as they lack specific, concrete content. The paper's actual measurable strengths (cost reduction, valid sample yield, ORM generalization, convergence dynamics) are retained above.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any observation about the method or results that the paper itself does not already state or imply.

## Suggestions

1. **Add a cost-aware dataset-level baseline across all three datasets** in the main results (Section 4.1). The simplest approach: apply fractional KUBE at the dataset level, selecting one model for all questions at each iteration. This directly isolates the effect of per-question adaptation from cost-awareness. If QWICK beats this baseline across datasets, the central contribution is cleanly demonstrated.

2. **Report variance.** Run each condition multiple times (at least 3–5) with different random seeds and report error bars or confidence intervals for the fine-tuning accuracy and valid sample counts. This is critical for the headline claims of cost savings.

3. **Conduct sensitivity analysis for α and β**, or justify the chosen values using established theoretical ranges from the bandit literature. At minimum, show stability over a reasonable range (e.g., α ∈ {8, 16, 32}, β ∈ {0.25, 0.5, 0.75}).

4. **Address the cost metric inconsistency** in the expansion condition: either empirically verify that generation lengths are roughly uniform across the model pool, or replace a_i in line 16 with an empirical cost estimate from observed generations.

5. **Formalize the stopping condition** Stop(x_j) in the method section (e.g., "maximum M valid responses per question").

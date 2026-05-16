Now I have all the information needed to verify the reviewer claims directly against the paper. Let me write the consolidated review.

---

## Summary

MultiTrust proposes a modular framework that trains separate "safety auxiliary models" (each on Llama-2-Chat-7B) for three trustworthiness perspectives — adversarial robustness, fairness, and truthfulness — using a two-phase SFT+DPO process. At inference time, a perplexity-based router selects which auxiliary model to use for a given input, and its logits are combined with the base model's logits via weighted interpolation. The framework is designed to avoid catastrophic forgetting from sequential fine-tuning and to allow adding new perspectives without retraining. Experiments on Vicuna-7B/13B and Llama-2-13B show large improvements in trustworthiness benchmarks with minimal degradation on general tasks.

## Strengths

- **Perplexity-based router achieves near-oracle performance without additional training.** Table 4 shows that the dynamic router's trustworthiness scores (e.g., Vicuna-7B: 52.60) closely approach an oracle that always selects the correct perspective-specific model (53.25), and similarly for Llama-2-13B (51.14 vs. 52.53). This demonstrates that the routing mechanism is accurate despite requiring no training or adaptation (Section 2.3, Table 4).

- **Consistent and large improvements across multiple base models.** Applying MultiTrust raises average trustworthiness for Llama-2-13B from 35.54% to 51.14% and for Vicuna-13B from 29.91% to 52.82% (Table 1). The aligned Vicuna-7B (52.60) even outperforms the much larger Vicuna-33B (42.07), supporting the framework's scalability claim.

- **Two-phase training (SFT followed by DPO) is shown to be more effective than either alone.** Table 3 reports that SFT+DPO achieves an average robustness score of 70.07, compared to 55.50 for SFT only and 64.78 for DPO only. The paper's approach of learning from the difference between correct and incorrect answers via DPO on top of SFT is empirically validated (Section 3.3, Table 3).

- **Systematic data generation across three trustworthiness perspectives.** The paper generates challenging robustness data by adapting five word-level attack algorithms (TextBugger, TextFooler, BERT-ATTACK, SememePSO, SemAttack) to LLMs across five tasks, constructs balanced fairness datasets from Adult and Crime with flipped sensitive attributes, and leverages the GRATH iterative process for truthfulness (Section 2.1). This data pipeline is a concrete contribution.

- **Cross-perspective interaction analysis reveals non-trivial benefits.** Table 5 shows that the truthfulness auxiliary model improves fairness scores (49.38 vs. 16.22 baseline) and that the robustness auxiliary model yields the highest cumulative trustworthiness-plus-helpfulness score. These findings support the claim that data from one perspective can benefit others and that the framework enables flexible exploration of such interactions (Section 3.3, Table 5).

## Weaknesses

### Fatal
None.

### Major

- **Missing direct fine-tuning baseline on the same base models used in Table 1.** The paper's central claim is that MultiTrust's *modular architecture* (separate auxiliary models + router + logit ensembling) delivers superior trustworthiness. However, the main results (Table 1) compare MultiTrust-aligned models against base models and other open-access models, but never against simply fine-tuning those same base models (Vicuna-7B/13B, Llama-2-13B) on the same training data used for the auxiliary models. Table 2 provides a relevant comparison (mixed vs. separate fine-tuning), but it uses a different base model (Llama-2-7B-Chat, the auxiliary model backbone) rather than the base models from Table 1. Without this control, the reader cannot determine whether the large gains (e.g., robustness from 30.50 to 66.90 for Vicuna-13B) are due to the modular routing architecture or simply from exposing the base model to higher-quality adversarial training data. The data generation itself is part of the contribution, but the paper's framing emphasizes the routing and modularity as the key innovation, and this claim is not cleanly isolated. This is the most significant evidential gap.

### Minor

- **Potential overlap between training and evaluation data not clarified.** The robustness training data (Section 2.1) is generated from SST-2, QQP, MNLI, RTE, QNLI using five word-level attack algorithms. The evaluation benchmark (DecodingTrust) is described only as using "adversarial robustness and fairness sections" — the paper never states whether DecodingTrust's robustness evaluation draws on the same tasks, datasets, or attack types. If there is substantial overlap, the reported robustness scores could be inflated. The same concern applies to fairness (training data from Adult and Crime; evaluation task unspecified). The paper should clarify this overlap and ideally evaluate on held-out tasks or attack types to demonstrate generalization.

- **Router selection distribution and accuracy are not reported.** Table 4 shows that the perplexity-based router's aggregate performance is close to an oracle, which is encouraging. However, the paper never reports the actual per-input selection statistics (e.g., how often does the router pick the truthfulness model for TruthfulQA questions vs. the robustness model?). The router is a core component, and its behavior should be transparent. Additionally, Table 5 reveals that using a "wrong" auxiliary model can sometimes outperform the "correct" one (e.g., the truthfulness auxiliary model improves fairness), which complicates the notion of optimal routing. The paper acknowledges this phenomenon but does not analyze whether the router's selections are actually optimal or merely reasonable in these cross-perspective cases.

- **The weighting factor γ in logit combination (Equation 2) is not reported.** The paper describes γ as controlling the trade-off between trustworthiness and general performance, but never states what value is used in the experiments or provides any sensitivity analysis. This is a meaningful hyperparameter that affects the core method.

- **Table 3 (DPO vs. SFT comparison) only reports adversarial robustness scores.** The caption explicitly states "Adversarial robustness of the model after using different training methods" and the results are restricted to robustness test sets (SST-2, QQP, MNLI). To support the general claim that SFT+DPO is more effective, the same analysis should be shown for fairness and truthfulness perspectives.

- **Fairness data conversion details are not described.** The paper states that tabular data from Adult and Crime are "transform[ed] ... into language descriptions" (Section 2.1) but provides no examples, templates, or details about how this conversion is done. Since the phrasing of tabular data significantly affects model behavior, this omission hinders reproducibility.

- **No variance or statistical significance reported.** All results in Table 1 are reported as point estimates without standard deviations, confidence intervals, or significance tests. While single-run evaluation is common in large-scale LLM benchmarks, the absence of any uncertainty quantification is notable, especially for fairness scores where differences between models are often small.

### Trivial

- **Formatting anomaly in the abstract.** The Vicuna-13B score is typeset as `$5\bar{2}.8\bar{2}\%$`, placing bars over the digits "2". This appears to be a LaTeX formatting quirk rather than substantive, but the number should read "52.82%".

## Nice-to-Haves

- **Ablation of logit ensembling.** Comparing MultiTrust (base model + router + logit combination) against simply using the selected auxiliary model alone (router without combining base logits) would isolate the contribution of the base model's logits.
- **Router failure case analysis.** A discussion of when the perplexity-based router might fail (e.g., an input resembling fairness training data but actually being a robustness test) would strengthen the method's characterization.
- **Dataset size imbalance discussion.** The robustness dataset has 78,715 examples vs. 8,000 (fairness) and 2,184 (truthfulness). A discussion of how this size imbalance might affect the perplexity estimates used by the router would be informative.
- **Comparison against model merging baselines.** The related work mentions model merging (Ilharco et al., 2022; Ortiz-Jimenez et al., 2024) but no experimental comparison is provided.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic's mention of "typographical artifact ('5̄2.8̄2%')" as a formatting issue:** This `\bar{}` notation in LaTeX is a typesetting choice in the original submission, not a parser error. It is moved to Trivial (included above) rather than treated as a separate structural weakness.
- **Strength Finder strength 1 (router flexibility):** Kept in Strengths as verified by Table 4. The strength is specific and evidence-backed, not generic.
- **Strength Finder strength 2 (consistent improvement):** Kept as verified by Table 1.
- **Critic's point about "the paper should also cover Y / additional tasks":** The critic's suggestions for additional router analysis and held-out evaluation are within the paper's scope and were moved to Minor/Nice-to-Have rather than removed.

## Novel Insights

The most interesting finding that emerges from combining the reviews is the non-obvious behavior of the perplexity-based router: it sometimes outperforms the oracle (Table 4 notes cases where dynamic routing surpasses oracle routing), and the cross-perspective analysis (Table 5) reveals that data and model specialization are not strictly aligned with the intuitive boundary between trustworthiness perspectives — the truthfulness auxiliary model helps fairness, and the robustness auxiliary model yields the highest overall score. This suggests that the router's effectiveness is not simply due to correct perspective identification but may stem from more complex domain-matching properties of perplexity. The reviews collectively highlight that this phenomenon deserves deeper investigation rather than being treated as a side observation.

## Suggestions

1. **Add direct fine-tuning baselines to Table 1.** For each base model (Vicuna-7B/13B, Llama-2-13B), report the performance of (a) fine-tuning on the mixed dataset, and (b) fine-tuning separately on each perspective's dataset (with either oracle selection or a learned router). This directly isolates whether the modular architecture adds value over vanilla fine-tuning on the same data.

2. **Clarify training/evaluation overlap.** State explicitly whether DecodingTrust's robustness and fairness evaluations use the same tasks, datasets, or attack algorithms as the training data. If overlap exists, provide results on a held-out benchmark (e.g., PromptBench for robustness).

3. **Report router selection statistics.** For each evaluation benchmark, provide the proportion of inputs routed to each auxiliary model, and report the accuracy of the router relative to an oracle defined as the model that maximizes the final trustworthiness score.

4. **State the value of γ and provide a sensitivity analysis.** Report the γ used in all experiments and show how performance changes over a range of γ values (e.g., [0.1, 0.5, 1.0, 2.0]).

5. **Extend Table 3 to include fairness and truthfulness scores.** The DPO vs. SFT comparison is currently limited to robustness; showing the same analysis for the other two perspectives would strengthen the claim that two-phase training is generally beneficial.

## Score and Decision

The paper presents a well-motivated framework with a clear architecture and large observed improvements on trustworthiness benchmarks. The core ideas — training separate perspective-specific auxiliary models, using perplexity as a routing signal, and combining logits at inference — are practical and potentially impactful. However, the evaluation has a significant evidential gap: the main results lack a direct comparison against simply fine-tuning the same base models on the same data, making it unclear whether the modular architecture or better training data drives the gains. Additional issues around training/evaluation overlap clarity, router transparency, and unreported hyperparameters further weaken the evidence. These are fixable, but in its current form the contribution is incompletely substantiated.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
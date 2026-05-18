Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes ABC (Action-Based Contrastive Self-Training), a quasi-online DPO variant for sample-efficient dialogue policy learning. ABC constructs contrastive preference pairs that contrast different pragmatic actions (CLARIFY vs. ANSWER), and integrates on-policy response sampling with multi-turn trajectory simulation to improve the policy's conversational disambiguation ability. The method is evaluated on three tasks (PACIFIC tabular QA, Abg-CoQA reading comprehension, and a new AmbigSQL text-to-SQL task) using Zephyr 7B as the base model, showing gains over SFT and a standard DPO baseline particularly in low-data regimes.

## Strengths

1. **Consistent sample-efficient gains on two of three tasks, with strong ablation support.** On PACIFIC (Table 1) and AmbigSQL (Table 3), ABC outperforms both SFT and Naive DPO across nearly all metrics and data settings. For example, on PACIFIC with 50 examples, ABC achieves 91.8 Action Accuracy vs. 84.3 (Naive DPO) and 86.7 (SFT), and Post-Clarify F1 of 57.2 vs. 35.6 (Naive DPO) and 43.5 (SFT). On AmbigSQL, ABC's Execution Match of 43.6% at 50 examples substantially exceeds Naive DPO (35.9%) and SFT (21.9%).

2. **Ablation evidence isolating the contribution of each component.** Table 4 shows that (a) replacing action-based pairs with random actions drops Macro F1 from 82.2 to 63.2, (b) removing on-policy sampling drops Post-Clarify F1 from 57.2 to 40.5, and (c) removing trajectory simulation (while keeping on-policy sampling) drops Post-Clarify F1 from 57.2 to 50.1. This cleanly decomposes the method's contributions and provides causal evidence that each design choice matters.

3. **Generalization to multiple base models.** The ablation also shows that ABC improves unaligned foundation models (Mistral 7B: +18.0 Macro F1 over SFT; Gemma 2B: +5.0 Macro F1 over SFT), demonstrating the method's applicability beyond the primary Zephyr setup.

4. **Introduction of AmbigSQL as a controlled testbed for conversational disambiguation in text-to-SQL.** The paper constructs a new task by systematically perturbing Spider queries, with a documented ambiguity gap of up to 45.8% execution match. This provides a resource for future work on multi-turn disambiguation.

## Weaknesses

### Major

1. **Evaluation relies on an unvalidated simulation pipeline, raising concerns about result trustworthiness.** ABC uses a user simulator U and an action classifier A for both training (Algorithm 2) and evaluation (Section 4.2). The paper states that details of U and A are in the appendix, but the main text provides no validation of these components — no human agreement, no correlation with real user behavior, no sensitivity analysis. Since the simulation loop is used for the content-level metrics (Turn Similarity, Trajectory Similarity, Post-Clarify metrics) where ABC shows its largest advantages, it is critical to establish that the simulated outcomes reflect genuine improvement rather than artifacts of a cooperative or biased simulator. This concern applies especially to ABC's strongest reported advantages (e.g., Post-Clarify F1 on PACIFIC where ABC scores 57.2 vs. Naive DPO's 35.6), as these metrics are entirely computed via simulation.

2. **ABC's advantage on Abg-CoQA is inconsistent and concentrated in metrics that depend on the simulation pipeline.** On Abg-CoQA (Table 2), Naive DPO achieves higher or equal Action Accuracy than ABC in two of three data settings (50: 88.0 vs. 84.7; 250: 88.0 vs. 86.2). ABC's main advantages are in the content-level simulated metrics (Turn Similarity, Trajectory Similarity). This pattern — where action-level (non-simulated) metrics do not consistently favor ABC while simulated content metrics do — amplifies the concern about simulation reliability. The paper's claim of "substantial" improvement is overstated for this task.

3. **The Naive DPO baseline differs from ABC on two confounded dimensions, and the controlled ablation is relegated to the appendix-level table.** Naive DPO uses a fixed preference dataset from Gemini Ultra/Pro (different source model, different data construction) while ABC uses action-based contrasts with on-policy sampling. The ablation "w/o on-policy sampling" (Table 4) correctly isolates the contribution of on-policy sampling by using action-based preferences without it — but this comparison appears only in the ablation table, not in the main results tables (Tables 1-3). The main comparisons thus conflate the action-based contrastive construction with the on-policy sampling mechanism, making it impossible to tell from the main results alone which component drives the gains.

### Minor

4. **Practical dependence on auxiliary components not discussed.** ABC assumes access to a controllable generation model M (for creating losing responses), an action classifier A (for evaluating on-policy responses), and a user simulator U (for trajectory simulation). The paper does not discuss how a practitioner would obtain A and U for a new task or domain, nor does it assess the robustness of results to classifier/simulator quality. This limits applicability in the low-resource settings the method is designed for.

5. **No analysis of clarification quality.** The paper measures whether the model asks clarification questions and whether the final answer is correct, but does not analyze the quality of the clarifications themselves (e.g., whether they are relevant, informative, or introduce new ambiguity). Asking *any* clarification may not be sufficient — asking the *right* clarification is what drives task improvement. This analysis would help separate the effect of the method's action-level training from overall task competence.

6. **AmbigSQL perturbation methodology not described in main text.** The paper introduces AmbigSQL as a contribution but describes the perturbation procedure only as "systematically perturbed" (line 211) without specifying the perturbation types or validation. For a claimed new benchmark, the main text should at least summarize the perturbation categories.

### Trivial

7. The limitations section discusses noisy annotations in crowdsourced datasets but does not address the potential noise in the action labels used to construct D_pref, which could cause the action-based contrast to reinforce labeling errors.

8. The effect of the number of on-policy samples per batch is not explored; the algorithm samples one per turn, and sensitivity to this choice is unreported.

## Nice-to-Haves

- A comparison of computational cost (training time, simulation overhead) between ABC, SFT, and Naive DPO would help practitioners assess the trade-off between sample efficiency and training expense.
- A human evaluation or inter-annotator agreement study for the user simulator U and action classifier A would substantially strengthen the paper's claims.
- An analysis of how post-clarification performance correlates with clarification quality (e.g., asking relevant vs. irrelevant questions) would separate the benefit of asking *any* question from asking the *right* question.

## Removed Points

These points were flagged by reviewers but are removed or downgraded for the following reasons:

- **"The appendix (which we cannot see) presumably contains details"**: The paper explicitly states that details of A and U are in the appendix. Per policy, the parser strips appendix content; this is not a valid criticism of the paper as submitted.
- **"Qualitative example is cherry-picked"**: Qualitative examples are illustrative by nature. The single example in Table 5 serves its intended purpose of grounding the quantitative results in concrete behavior. Its limitations are inherent to the format, not a flaw.
- **"Quasi-online description is misleading"**: The paper uses "quasi-online" precisely because the algorithm is between fully offline DPO and fully online PPO. The on-policy responses dynamically update preference pairs within each batch, which is accurately described.
- **"Gemini outperforms tuned models on some metrics"**: The paper acknowledges this (lines 278, 282). Comparing a 7B tuned model against frontier models on absolute task performance is not the paper's goal — the goal is sample-efficient adaptation.
- **"Missing related works"**: Per policy, this cannot be verified without external sources.

## Novel Insights

None beyond the paper's own contributions. The review surfaces a structural concern that the paper's strongest results (content-level simulated metrics) are on the very metrics that depend most heavily on the unvalidated simulation pipeline, creating a correlation between result magnitude and evaluation vulnerability that the paper does not address.

## Suggestions

1. Add a human evaluation or at least a human agreement study for the action classifier A and user simulator U in the main text (summarize from the appendix if it contains this).
2. Include the controlled baseline "action-based DPO without on-policy sampling" alongside ABC and Naive DPO in the main results tables.
3. Provide an analysis of clarification quality — e.g., whether ABC's clarifications are semantically relevant to the ambiguity, or whether it simply learns to ask any question before answering.
4. Add a sensitivity analysis showing how results vary with the quality of A (e.g., by corrupting or ablating the classifier).

## Score and Decision

The paper presents a novel combination of existing ideas (action-based contrastive pairs + on-policy DPO sampling + trajectory simulation) and provides clean ablations that decompose the contribution of each component. The core methodological contribution is sound and the results on PACIFIC and AmbigSQL are compelling. However, the evaluation's heavy dependence on an unvalidated simulation pipeline — combined with the inconsistency of results on Abg-CoQA — means the evidence is suggestive but not fully conclusive. The method is a meaningful step forward for sample-efficient dialogue policy learning, and the concerns are addressable. I recommend acceptance contingent on the authors validating the simulation pipeline (or at minimum, presenting a sensitivity analysis in the main text).

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
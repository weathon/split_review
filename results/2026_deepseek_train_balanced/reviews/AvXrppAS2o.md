## Summary

This paper proposes a multi-task learning framework that combines causal structure learning (via a graph autoencoder, CausalGAE) with outcome prediction. The key architectural contribution is adding a separate prediction head g₃ alongside the reconstruction decoder g₂, sharing a learned latent representation. The authors claim this improves out-of-sample generalization for outcome prediction and enhances causal discovery for the outcome variable.

## Strengths

- **Scalability advantage over CASTLE is empirically quantified.** Figure 1 and Table 4 show that the model's training time grows much more slowly with feature dimension (d) compared to CASTLE, a concrete architectural benefit of using a graph autoencoder with shared encoder weights rather than CASTLE's per-variable feed-forward networks.

- **The temporal split experimental design is methodologically appropriate for the paper's motivating scenario.** Scenario 2 in the survival analysis case study (training on 1997/1999 data, testing on 2001 data) directly simulates the real-world deployment condition the paper targets — a reasonable and well-motivated evaluation.

## Weaknesses

### Fatal

- **κ = 0 makes the claimed joint learning mechanism inoperative.** The paper states explicitly on line 103: "The loss hyperparameter κ is set to 0." In the loss function (Equation 7), κ weights the supervised outcome-prediction term, and (1−κ) weights the reconstruction term. With κ = 0, the loss reduces to pure CausalGAE reconstruction loss + DAG constraint. The prediction head g₃ receives no gradient from any supervised signal — its parameters Θ₃ are never updated. For the synthetic experiments, line 123 confirms predictions come from the "reconstructed target" (g₂'s output), not g₃. This is not speculative: the paper as written describes a method in which the central claimed addition (supervised multi-task learning with a separate prediction head) is disabled during training. No reported result can be attributed to the claimed mechanism. This is a structural internal inconsistency, not a missing ablation or minor oversight.

### Major

- **The ablation study is underspecified to the point of being uninterpretable.** Section 5.3 states the model is tested with "ablations of the causal structure learning and outcome prediction components" but never defines what these ablations actually change (removing the DAG constraint? Removing the prediction head? Setting κ to different values?). With κ = 0, there is no "outcome prediction component" to ablate, which further underscores the core ambiguity. Without a clear description of what was ablated, these results cannot be evaluated or reproduced.

- **Baseline comparisons are too narrow to support the claimed generality of "improved outcome prediction."** The paper compares against MLP, MLP+L2 variants, and CASTLE. Well-established clinical prediction models (Random Forest, XGBoost, properly tuned deep MLPs with dropout/batch normalization) are absent. CASTLE is described as having "outperformed various regularisation methods like dropout, data augmentation and batch normalisation," but none of these methods appear as baselines in this paper. The comparison set is weak relative to the strength of the claims.

- **Real-data evaluation is thin.** Three small UCI datasets are used (Statlog Heart: 270 samples, Breast Cancer Wisconsin: 569 samples, Las Vegas multi-class: from tourism/recreation). For the binary tasks, all methods achieve AUC > 0.9 with no meaningful differentiation. The only dataset where the proposed method separates from baselines (Las Vegas) is a non-medical dataset, which sits oddly with the medical motivation. No confidence intervals or statistical significance tests are reported. The survival analysis case study adds some value but relies on one 500-sample dataset.

### Minor

- **The paper overstates its contribution relative to prior work.** CASTLE (Kyono et al., 2020) already adds a supervised loss to a causal structure learning framework (NOTEARS) for improved generalization. The present paper replaces NOTEARS with CausalGAE and adds a separate prediction head. This is a meaningful but incremental improvement (scalability, architectural decoupling), not a "novel paradigm" or "the best of both worlds."

- **Prediction procedure is ambiguous for classification tasks.** For synthetic (regression) experiments, predictions use the "reconstructed target" (g₂). For classification experiments (Tables 5, 6), it is unclear whether predictions come from g₂'s reconstruction of the target variable or from g₃'s separate classification head.

### Trivial

- Line 101 has a duplicated word ("like like dropout").
- The code URL is referenced but not provided in the visible text.

## Nice-to-Haves

- Report confidence intervals or standard deviations across cross-validation folds or random seeds.
- Validate discovered causal graphs against known clinical knowledge for the survival analysis case study.
- Include an ablation over κ values (e.g., 0, 0.2, 0.5, 0.8, 1.0) to demonstrate the trade-off between reconstruction and supervised learning and verify the proposed mechanism drives performance.
- Add standard medical prediction baselines (Random Forest, XGBoost) to support the claimed general improvement.

## Removed Points

These points from the reviews were removed after verification against the paper:
- **κ=0 invalidates all strengths about the joint learning mechanism:** The Strength Finder's claims about "architectural decoupling," "synthetic Case 2 testing the beyond-causal-parents hypothesis," and "temporal shift experiment demonstrating generalization" are all undermined by the verified κ=0 issue and cannot be retained as genuine strengths.
- **"Contribution is marginal / just engineering change":** The harsh critic's framing of this as a critical issue is excessive. The separate prediction head and scalability advantage are genuine, even if incremental. Retained only as a minor weakness.
- **"Motivation about unmeasured confounders is misleading":** The paper lists unmeasured confounders as a limitation of *existing methods*, not as something their method solves. The criticism misreads the paper.
- **"CASTLE characterization asserted without evidence":** This is a subjective judgment about the sufficiency of argumentation for a critique of prior work; not a substantive weakness.
- **"No code or reproducibility details":** Per guidelines, I cannot penalize based on code availability statements or missing URLs.
- **"No discussion of limitations":** Trivially true but papers are not required to include a limitations section.

## Novel Insights

None beyond the paper's own contributions. The κ = 0 issue dominates all other assessment dimensions.

## Suggestions

1. **Clarify whether κ was actually zero for all experiments or whether this is a reporting error.** If κ was tuned to non-zero values, report the values per experiment. If κ was zero, acknowledge the method was not evaluated as described and re-run experiments.
2. Report predictions separately from g₂ (reconstruction) and g₃ (prediction head) to demonstrate the value of the decoupled architecture.
3. Add stronger baselines (Random Forest, XGBoost, tuned MLP with dropout/batchnorm) and report confidence intervals.
4. Define the ablation conditions precisely and include an ablation over κ values.

## Score and Decision

MY FINAL SCORE: <score>1.5</score>
MY FINAL DECISION: <decision>Reject</decision>
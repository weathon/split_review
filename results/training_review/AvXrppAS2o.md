Now I have all the information I need. Let me produce the final review.

## Summary

The paper proposes a joint architecture where a graph autoencoder (CausalGAE) is augmented with a task-specific prediction head for outcome prediction, sharing a learned representation between the causal structure learning reconstruction task and the supervised outcome prediction task. The method is evaluated on synthetic data, UCI classification datasets, and a survival analysis case study on the Worcester heart attack dataset.

## Strengths

- **Novel joint architecture.** The paper introduces a natural extension of CausalGAE (Ng et al., 2019) by adding a supervised decoder head g₃ that shares the encoder g₁ and weighted adjacency matrix W with the reconstruction decoder g₂ (Section 4, Equations 4–6). This decouples outcome prediction from variable reconstruction while leveraging the learned causal structure, addressing a limitation of CASTLE which couples reconstruction and prediction in a single feed-forward network per variable.

- **Scalability advantage over CASTLE.** The paper empirically shows (Figure 1, Table 4) that the proposed model's training time scales much more gracefully with the number of variables compared to CASTLE, which uses one network per variable. This is a concrete and reproducible practical advantage for high-dimensional settings. Importantly, this result does not depend on the disputed hyperparameter κ.

- **Temporal distribution-shift experiment.** The time-split evaluation on the Worcester heart attack dataset (Section 5.6, Scenario 2 — training on 1997/1999, testing on 2001) is a genuinely interesting test of generalization under evolving medical conditions. The paper shows the proposed model achieving AUC 0.696 while the best baseline (L2+ES) drops to 0.500.

## Weaknesses

### Fatal

- **κ=0 makes all outcome prediction results uninterpretable.** The paper states (line 103): *"The loss hyperparameter κ is set to 0."* In Equation (6), the loss is `(1-κ)·L_DAG + κ·L_sup`. Setting κ=0 zeroes the supervised loss entirely, meaning the outcome prediction head g₃ receives **no training signal**. Its parameters would remain at initialization and its output would be random. Yet Tables 1, 3, 5, and 6 report the proposed method outperforming all baselines on outcome prediction. This is a logical contradiction. Either the paper used κ>0 and the text is wrong, or κ=0 and the results cannot be produced as described. In either case, the paper's central empirical claims are invalidated. The authors must clarify (a) the actual value of κ used in each experiment, (b) how g₃ was trained, and (c) why the reported results are replicable.

### Major

- **Missing sequential-training baseline.** The most informative comparison would be CausalGAE + a separately trained prediction head using the learned W (sequential training). This would isolate whether the *joint* optimization (shared encoder) is what provides the benefit, or simply adding a prediction head. The paper compares against CausalGAE's *reconstruction* of Y (which is not an outcome-prediction method) — a weak baseline — but does not include the sequential variant. Without this baseline, it is unclear whether the joint nature of the proposed method, or simply the addition of a prediction head, drives the reported improvements.

- **Ablation study is underspecified.** Table 3 labels ablations as "Without causal structure learning" and "Without outcome prediction," but the paper does not specify what these conditions entailed (e.g., does "without causal structure learning" remove the DAG constraint, the reconstruction loss, or both? Does "without outcome prediction" remove g₃ entirely or zero the supervised loss?). The results are consequently difficult to interpret.

### Minor

- **Limited evidence for distribution-shift generalization.** Despite the paper's framing around "evolving conditions" and "out-of-sample generalization," only one experiment (the time-split on the Worcester dataset with n=500 samples) involves a genuine distribution shift. The synthetic-data experiments and UCI classification tasks use standard i.i.d. train/test splits. The paper's central generalization claim rests heavily on a single small-scale case study.

- **No variance or confidence intervals reported.** All tables report point estimates without standard deviations, confidence intervals, or significance tests. This makes it impossible to assess whether reported differences are statistically meaningful.

- **Causal discovery results are modest.** Table 2 shows SHD comparable to CausalGAE and slightly improved TPR, but the improvements are marginal. The subsection title "Robust Causal Discovery" overstates these results.

- **Causal graph figure is illegible.** Figure 2 is described as too small to read node labels or edge weights, undermining the interpretability claim.

### Trivial

- Equation (1) on line 41–43 appears to be missing the acyclicity constraint expression (the `tr(e^{W⊙W}) - d = 0` term only appears later in line 83). This is likely a formatting artifact.

## Nice-to-Haves

- An analysis of how varying κ affects the trade-off between causal discovery quality and outcome prediction accuracy would strengthen the paper.
- Additional distribution-shift experiments (covariate shift, concept drift) beyond the single case study would better support the generalization claims.
- A study varying sample size to demonstrate where the method helps most in "limited data settings."

## Removed Points

**These points are flagged to be removed, treat them with caution.**

1. **"Unfair baseline comparison with CausalGAE for outcome prediction"** — The reviewer claimed comparing against CausalGAE for outcome prediction is unfair because CausalGAE is not designed for prediction. However, this comparison is supplementary (the primary baselines are CASTLE, MLP, L2+ES, ES), and the paper's method is explicitly derived from CausalGAE, making the comparison natural. While the comparison would be stronger with a sequentially-trained CausalGAE + prediction head (which I keep as a major weakness above), the reviewer's framing as a "structural" issue is overblown. The criticism is kept in weakened form as the sequential-training baseline request under Major.

2. **"κ=0 is inconsistent with cross-entropy loss for classification"** — The reviewer notes this as additional inconsistency, but it's the same κ=0 issue already covered under Fatal.

3. **Various formatting/style nitpicks** from the harsh critic's "Section-by-Section Notes" are removed per the hard rules on formatting.

## Novel Insights

The reviewer's point about the need for a sequential-training baseline (first learn the causal graph with CausalGAE, then fix W and train a prediction head) is the most valuable methodological insight. This would directly test whether the joint shared-representation learning provides benefits beyond simply adding a prediction network on top of learned causal structure. The κ=0 issue, if resolved, would also make the paper's core question — whether joint causal structure learning and outcome prediction yields better generalization — worth investigating with proper experimental design.

## Suggestions

1. **Resolve the κ=0 contradiction immediately.** Clarify the actual value of κ used in each experiment. If it was κ>0, correct the text and report the actual value. If it was genuinely 0, explain how g₃ was trained (or acknowledge the error).
2. **Add a sequential-training baseline:** Train CausalGAE to learn W, then freeze W and train g₃ (and optionally g₁) with the supervised loss. This isolates the benefit of joint optimization.
3. **Report variability:** Add standard deviations or confidence intervals (e.g., bootstrap) to all numerical results.
4. **Specify ablation details clearly:** State what "without causal structure learning" and "without outcome prediction" actually remove at the architectural level.
5. **Include additional distribution-shift experiments** or at minimum acknowledge that the generalization claim is supported primarily by one small-scale case study.

## Score and Decision

**FUNDAMENTAL ISSUE TRIGGERED:** The κ=0 inconsistency invalidates the paper's core empirical claims. The results in Tables 1, 3, 5, and 6 cannot be produced as described. This overrides all strengths. The paper cannot be accepted in its current form without a corrected experimental account.

MY FINAL SCORE: <pineapple>2.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
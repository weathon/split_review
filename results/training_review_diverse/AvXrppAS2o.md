Now I have a thorough understanding of the paper and can verify the reviewer claims directly against the source text. Let me construct the consolidated review.

---

## Summary

The paper proposes a multi-task learning framework that jointly learns a causal graph (via a graph-autoencoder formulation building on Ng et al., 2019) and performs outcome prediction through a shared representation, with causal structure learning serving as an auxiliary regularizer. The claimed contributions are: improved out-of-sample generalization for prediction, robust causal discovery, scalability relative to CASTLE, and interpretability via the learned causal graph. Evaluation is conducted on synthetic data and real-world datasets including a survival analysis case study.

## Strengths

1. **Demonstrated scalability advantage over CASTLE** — The paper provides direct empirical evidence (Figure 1, Table 4) that its graph-autoencoder architecture scales linearly with the number of features (d=10 to d=100) while maintaining stable test MSE, whereas CASTLE's per-variable feed-forward networks degrade substantially in both training time and prediction quality. This directly addresses a stated limitation of CASTLE.

2. **Strong performance under temporal distribution shift** — In the Worcester heart attack study (Scenario 2, Table 6), where training data comes from 1997/1999 and testing from 2001, the proposed model achieves test AUC 0.81 while all baselines (CASTLE, MLP, L2+ES, ES) drop to ≤0.59. This single experiment directly supports the paper's central motivation about generalizing under evolving clinical conditions.

3. **Robust causal discovery despite auxiliary prediction task** — Table 2 shows that the proposed model achieves comparable or better causal graph recovery than CausalGAE (e.g., TPR 0.83 vs. 0.78 in Case 2) while also performing outcome prediction, demonstrating that the auxiliary task does not harm—and can modestly improve—structure learning for the target variable.

4. **Interpretability via learned causal graphs** — The survival analysis case study (Figure 2) produces causal graphs whose edges (e.g., death associated with age, cardiogenic shock, atrial fibrillation) align with clinical expectations, illustrating practical value in a domain where understanding variable relationships matters.

## Weaknesses

### Fatal

- **κ=0 is stated but is inconsistent with the reported results, making the experimental evaluation unreliable.** The paper states (Section 5, Experimental setup): "The loss hyperparameter κ is set to 0." In the loss function (Eq. 6), the reconstruction term is weighted by (1−κ) and the supervised term by κ. If κ=0, the supervised loss contributes nothing, so the prediction head g₃ receives no gradient signal and cannot learn. For the synthetic regression experiments (Table 1), the paper says "We infer the reconstructed target from the trained model"—so predictions come from the reconstruction decoder g₂, not g₃—but this still contradicts the paper's claimed mechanism of a separate task-specific head. For the classification experiments (Tables 5, 6), where the paper introduces g₃ as a projection layer and says "For classification, we use cross entropy loss as the supervised loss," the inconsistency is more severe: with κ=0, the cross-entropy loss contributes nothing, and g₃ cannot be trained. Moreover, the ablation study (Table 3) compares "full model" vs. "outcome prediction ablated" — but if κ=0, these would be identical. The paper reports the proposed model outperforming CausalGAE in Table 1, yet with κ=0 the training procedure is essentially CausalGAE (an untrained g₃ adds no gradient signal). **The stated hyperparameter setting cannot produce the reported results.** This is either a critical error in the paper or a typographical mistake that invalidates all experimental findings as currently presented.

### Major

- **No measures of variability or statistical significance for any quantitative result.** Every table reports only point estimates (single MSE or AUC values). The paper mentions 10-fold cross-validation, suggesting fold-level data exists, but standard deviations, per-fold results, confidence intervals, or significance tests are never reported. Given the small test sets (e.g., 90/10 split on n=1000 synthetic data → test size ~100; n=500 survival data → test size ~50 with 10 folds), variance is substantial. Without error bars, it is impossible to assess whether reported improvements are meaningful or due to chance.

- **Limited evaluation of out-of-sample generalization under distribution shift, despite this being the paper's primary motivation.** The paper's motivation emphasizes "evolving conditions and treatment approaches" and "generalization to prospective data." However, virtually all experiments (synthetic data in Section 5.1, real-data classification in Section 5.5, survival Scenario 1 in Section 5.6) use random 90/10 splits where training and test come from the same distribution. The only exception is survival Scenario 2 (temporal split), which is not run with multiple splits or significance testing. The central claim about distribution-shift robustness is supported by essentially one experiment.

- **Ablation study (Section 5.3) is undefined and uninterpretable.** The paper states "results of our model with ablations of the causal structure learning and outcome prediction components" but never specifies what these ablations actually are: what is removed, how the loss changes, or what the "outcome only" and "structure only" variants correspond to. Given the κ=0 confusion, it is unclear what these ablations even mean. This makes Table 3 uninterpretable as evidence for any particular claim.

- **Underspecified comparison to CausalGAE in Table 1.** The paper compares its method to CausalGAE by "infer[ring] the reconstructed target from the trained model" for both methods. If both use the same reconstruction procedure and the proposed model's only addition is an untrained g₃ (under κ=0), the reported performance gap is unexplained. The paper needs to clarify exactly what architectural or procedural difference produces the improvement.

### Minor

- **Implementation details insufficient for reproducibility.** While the paper references Ng et al. (2019) for default hyperparameters, key details specific to this adaptation are missing: the architecture of g₃ (number of layers, hidden dimensions, activation functions) for both regression and classification, how the outcome variable Y is handled differently from other variables in the encoder, and whether κ is actually tuned or fixed across all datasets. The claim that "the dimension of the latent representation can be adjusted based on the intrinsic dimension of X" is stated but the actual dimensionality used in experiments is not reported.

- **Interpretation of learned graphs as "causal" is overstated.** The paper refers to the recovered graphs as "causal" but the evaluation on real data (Figure 2) only asserts clinical plausibility of associations without any ground-truth comparison or sensitivity analysis. While interpretability is a genuine strength, calling these "causal graphs" in the absence of validation is a scope overclaim.

- **No comparison to simpler shared-representation baselines without causal constraints.** The paper does not include a baseline that shares encoder weights between prediction and reconstruction but does not impose the acyclicity constraint or structure learning. Such an ablation would isolate the value of the causal graph itself from the value of representation sharing.

### Trivial

None.

## Nice-to-Haves

- A κ sensitivity analysis (varying κ from 0 to 1) would clarify the contribution of the supervised head and could replace the current underspecified ablation study.
- Additional temporal-split or domain-shift experiments beyond the one survival scenario would substantially strengthen the generalization claim.
- Reporting fold-level results or standard deviations for all tables would address the statistical significance concern.
- A limitations section discussing failure modes (e.g., when the DAG assumption is violated, or when the outcome variable is not a leaf node) would improve scientific rigor.

## Removed Points

These points are flagged to be removed from the harsh critic's review; treat them with caution.

- **"The paper does not situate itself against other representation‑sharing approaches (e.g., causal‑VAE, invariant risk minimization)"** — Removed per instructions: missing related works should not be mentioned as weaknesses, as external sources cannot verify their relevance. The paper does cite CASTLE (Kyono et al., 2020) and Ge et al. (2023) which are the most directly relevant works combining causality and prediction.
- **"κ=0 would make the reported outcome‑prediction results inexplicable" for Table 1** — Partially removed/weakened: the harsh critic claimed ALL results are inexplicable, but the paper says for Table 1 "We infer the reconstructed target from the trained model," meaning predictions come from g₂ (reconstruction decoder), which IS trained with weight (1−κ)=1. However, the issue remains severe for classification experiments and the overall inconsistency is still fatal.
- **Criticisms about missing appendix / appendix content** — Removed per instructions: the parser strips appendices; they exist in the original submission.
- **Formatting/style nitpicks about reproducibility (e.g., undisclosed hyperparameters that follow Ng et al., 2019)** — Weakened/removed per instructions: referencing a prior method for standard hyperparameters is acceptable, though the paper's own novel contributions (g₃ architecture) should be specified.
- **Criticism that "the paper does not explain how the 'first non-parent' is determined"** — This is a minor detail about synthetic data generation that does not affect the core claims; moved to minor concerns implicitly.

## Novel Insights

The harsh critic's identification of the κ=0 inconsistency is the central finding of this review process — it catches an apparent contradiction between the stated hyperparameter and the reported results that, if unresolved, undermines the entire experimental contribution. Beyond that, the reviews collectively highlight a disconnect between the paper's motivating narrative (distribution shift, evolving conditions) and its experimental design (mostly i.i.d. splits). Neither reviewer identified structural flaws in the method itself (the architectural formulation is sound), meaning the paper's core idea could be salvageable with corrected experiments.

## Suggestions

1. **Resolve the κ=0 issue as the highest priority.** Either: (a) correct the stated κ value(s) used for each experiment and report whether κ was tuned per dataset; (b) show a sensitivity analysis over κ to demonstrate that neither extreme (κ=0 or κ=1) works as well as the chosen setting. This is non-negotiable for the paper to be credible.

2. **Add error bars to all quantitative results** (standard deviations across folds or repeated runs). Without these, the empirical claims cannot be evaluated.

3. **Expand the distribution-shift evaluation.** Even adding 1-2 additional temporal or domain splits (e.g., on the UCI datasets or additional survival cohorts) would significantly strengthen the paper's core claim.

4. **Define the ablations precisely** — specify exactly what changes are made to the loss or architecture for each ablation variant.

5. **Add a limitations section** discussing when the method might fail, what the DAG assumption entails, and how to handle settings where the outcome is not a leaf node.

## Score and Decision

The paper presents a conceptually reasonable idea — sharing representations between causal structure learning and outcome prediction — and has some genuine strengths, particularly the scalability analysis and the temporal-split survival experiment. However, the κ=0 inconsistency is a fatal flaw that renders the entire experimental evaluation unreliable. The paper states κ=0, which (a) zeroes out the supervised loss, making g₃ untrainable, (b) contradicts the ablation results and (c) leaves the reported classification results (Tables 5, 6) unexplained. Even for the regression results that could partially rely on reconstruction, the improvements over CausalGAE are inconsistent with identical training conditions under κ=0. Additionally, the lack of any uncertainty quantification and the near-absence of distribution-shift evaluation further undermine the empirical claims.

The paper cannot be accepted in its current form. The core idea may be publishable after major revision that resolves the κ discrepancy, provides proper error bars, and adds meaningful distribution-shift evaluation.

MY FINAL SCORE: <pineapple>3.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
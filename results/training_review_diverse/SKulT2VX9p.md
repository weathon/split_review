Now I have a comprehensive understanding of the paper and all reviewer claims. Let me produce the final consolidated review.

## Summary

This paper addresses the problem of achieving interventional fairness when the causal graph is only partially known (represented as an MPDAG). The authors propose (1) a modeling technique showing that augmenting an MPDAG with a predictor variable preserves the MPDAG property (Theorem 1), (2) identification conditions for interventional fairness on MPDAGs via the augmented graph (Proposition 1), and (3) a constrained optimization framework that balances fairness (measured as distributional discrepancy between interventional distributions) against predictive accuracy. Experiments on synthetic and two real-world datasets demonstrate trade-off curves.

## Strengths

- **Handles partial causal knowledge instead of assuming a full DAG** (Section 1, Theorem 1). Most prior causal fairness work assumes the true causal DAG is fully known. This paper is the first to systematically address interventional fairness when only a partially known graph (MPDAG) is available. Theorem 1 — showing that the augmented MPDAG with the predictor preserves MPDAG consistency — is a clean technical contribution that may be of independent interest beyond fairness.

- **Provides explicit identification conditions for the fairness measure on MPDAGs** (Proposition 1, Section 4.2). Proposition 1 gives a necessary and sufficient graphical condition (no undirected edge between any node in the treatment set and any node in its complement) and an exact formula for the causal effect \(P(\hat{Y} \mid do(\mathbf{A},\mathbf{X}_{ad}))\) using the partial causal ordering. This is a non-trivial extension of Perković et al.'s general identification theorem to the fairness setting with the augmented graph.

- **Constrained optimization framework with demonstrable fairness-accuracy trade-off**. The \(\epsilon\)-IFair formulation with regularization parameter \(\lambda\) provides a principled way to interpolate between exact fairness (IFair) and unconstrained accuracy (Full). Experiments on synthetic graphs with 5–30 nodes and on two real datasets show that the method can match the unfairness of the exact IFair baseline while retaining RMSE near that of the Full model for appropriate \(\lambda\) values (Figures 1, 3).

## Weaknesses

### Fatal
None. No weakness invalidates the core contributions of the paper.

### Major

1. **Mismatch between the fairness definition and the optimization penalty (structural).**  
   Definition 2 (\(\epsilon\)-approximate interventional fairness) demands a *pointwise* bound:  
   \(|P(\hat{Y}=y|do(\mathbf{a},\mathbf{x}_{ad})) - P(\hat{Y}=y|do(\mathbf{a}',\mathbf{x}_{ad}))| \leq \epsilon\) for every outcome value \(y\).  
   The optimization objective (Eq. 1) penalizes a distance between the two interventional *distributions* (the notation \(|P(\cdot)-P(\cdot)|\) is ambiguous there), and Section 4.3 operationalizes this using Maximum Mean Discrepancy (MMD). The paper provides no argument that bounding MMD (or any integral probability metric) implies the pointwise condition for all \(y\) at a given \(\epsilon\). While using a distributional distance as a surrogate for a pointwise fairness constraint is a common practical relaxation, the paper presents this as directly enforcing Definition 2 without acknowledging or justifying the gap. This overstates the theoretical guarantee. **Fix:** either relax Definition 2 to a distributional distance and state this clearly, or provide a theoretical link (e.g., MMD bound → pointwise bound under smoothness assumptions).

### Minor

2. **Limited baselines.** The empirical evaluation compares only against Full, Unaware, and IFair (the exact fairness baseline). No comparison is made to methods that handle graph uncertainty (e.g., averaging predictions over all DAGs in the equivalence class, robust optimization) or to simpler non-causal fairness regularization that ignores structure. This makes it difficult to isolate the value added specifically by the MPDAG-aware identification, as opposed to just adding a distributional penalty.

3. **Incomplete description of the optimization pipeline (reproducibility gap).** Section 4.3 describes the approach at a high level (estimate conditionals via multivariate Gaussian, Monte Carlo sampling, MMD penalty, train a neural net) but omits: (a) the explicit objective function used during training (the MMD-based loss is never written down); (b) hyperparameters (learning rate, number of epochs, batch size, neural network architecture); (c) how the Monte Carlo sample size was chosen. These details are needed for reproducibility beyond stating the general approach.

4. **Real-data MPDAG construction is underspecified.** The paper references figures for the MPDAGs used on the Student and Credit Risk datasets (\cref{fig: real_data_with_assumption}, \cref{fig: credit_mpdag}) but does not describe: what causal discovery algorithm (if any) was used to obtain the CPDAG, what specific background knowledge / domain assumptions were incorporated, or how the MPDAG was validated. Since the entire method hinges on the structure of the MPDAG, this makes the real-data results difficult to independently reproduce or assess.

5. **No variance/error bars on experimental results.** The synthetic results report point estimates over 10 graphs (one run each) without confidence intervals, standard deviations, or any measure of variability. The trade-off curves cannot be assessed for stability. For the real data, the Student test set contains only 19–20 interventional samples per group (which the paper acknowledges), but the training-set curves also lack error bars.

### Trivial

6. **Missing hyperparameter details.** As noted above, learning rate, architecture, epochs, batch size, and Monte Carlo sample size are absent. While individual hyperparameter values are rarely fatal, their omission adds to the reproducibility concern.

7. **Notation inconsistency.** Eq. (1) uses \(|P(\hat{Y}_{\mathbf{A}\leftarrow \mathbf{a}, \ldots}) - P(\hat{Y}_{\mathbf{A}\leftarrow \mathbf{a}', \ldots})|\) where \(P\) denotes a distribution; the absolute value of a distribution is not standard notation and should be clarified (e.g., a norm or a distance).

## Nice-to-Haves

- A comparison against a method that averages the predictor over all DAGs in the MPDAG equivalence class (model averaging) would help isolate the specific benefit of the proposed identification-based approach.
- If the no-identification case arises in practice, a demonstration of the averaging procedure over MPDAGs (mentioned in Section 4.2) would be a useful extension.

## Removed Points

- **Criticism about MPDAG figures not being shown.** The paper references figures (\cref{fig: real_data_with_assumption}, \cref{fig: credit_mpdag}) that exist in the original submission. Their absence in the extracted text is a parser artifact, not an author error. However, the *construction process* for these figures is indeed underspecified (kept as Minor weakness #4).
- **Claim that the method's contribution is merely adapted from Perković et al. (2020).** Proposition 1 correctly cites and adapts existing theory to the fairness context. The adaptation is non-trivial (requires the augmented MPDAG from Theorem 1) and properly attributed. The point is factually correct but not a weakness.
- **Complaint that the paper should also address path-specific or counterfactual fairness.** The paper explicitly scopes itself to interventional fairness (Section 4.4). This is a scope restriction, not a weakness.
- **Generic "missing related work" style complaints.** Not verifiable without external sources.
- **Pure formatting/style nitpicks.** Parser artifacts, not author errors.
- **Strength about "Uses MMD as a rigorous distributional discrepancy measure."** This conflicts with the verified weakness (Major #1) about the definition-penalty mismatch. Per instructions, when strength and weakness disagree, the weakness wins; moved here.

## Novel Insights

The reviewers collectively highlight an important tension that the paper does not fully resolve: the problem is to enforce a *pointwise* fairness definition, but the optimization uses a *distributional* penalty (MMD). This is more than a technical detail — it goes to whether the method's empirical fairness guarantees match what the theory promises. A solution (redefining the target notion to match the penalty, or proving a bound) would tighten the paper considerably. Beyond this, the reviews do not surface insights that go beyond what the paper itself claims.

## Suggestions

1. **Align the definition and the penalty.** Either (a) relax Definition 2 to a distributional distance (e.g., "\(\text{MMD}(P(\hat{Y}|do(\mathbf{a},\mathbf{x}_{ad})), P(\hat{Y}|do(\mathbf{a}',\mathbf{x}_{ad}))) \leq \epsilon\)") and state clearly that this is the notion being optimized, or (b) provide a theoretical argument connecting the MMD bound to the pointwise bound under regularity assumptions.

2. **Release the full experimental pipeline** including: the MPDAG construction details for the real datasets, the neural network architecture, all hyperparameters, and the MMD-based loss function as actually implemented. This would resolve the reproducibility concerns.

3. **Add confidence intervals or error bars** to at least the synthetic experiments (across the 10 graph instantiations) to demonstrate stability of the trade-off curves.

4. **Write down the actual training objective.** Show the MMD-based loss explicitly as a function of the model parameters \(\theta\), the Monte Carlo samples, and the kernel choice.

## Score and Decision

This paper makes a genuine contribution: it is the first to address interventional fairness under partial causal graph knowledge, with clean theoretical results (Theorem 1, Proposition 1) that stand independently of any implementation. The constrained optimization framework and empirical demonstrations support the approach's viability.

However, the paper has a significant structural weakness: the fairness definition (pointwise bound) does not match the actual penalty used in optimization (MMD-based distributional distance), and this gap is not acknowledged. The experimental evaluation lacks reproducibility-critical details (hyperparameters, MPDAG construction process, error bars). These issues are addressable in revision but reduce confidence in the current form.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
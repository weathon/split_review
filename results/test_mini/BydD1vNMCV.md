Here is my final consolidated review.

---

## Summary

This paper proposes the StoNet (stochastic neural network) as a bridge between linear models and deep neural networks (DNNs). The StoNet is formulated by adding noise to the pre-activation values at each hidden layer of a DNN, turning the network into a composition of simple linear/logistic regressions. The paper claims: (1) the StoNet is asymptotically equivalent to the DNN in terms of log-likelihood (Lemma 1, cited from prior work); (2) sparse learning theory with the Lasso penalty can be adapted from linear models to the StoNet, yielding consistent structure selection (Theorem 1); (3) by asymptotic equivalence, this consistency extends to Lasso-penalized DNNs (Corollary 1); and (4) a post-StoNet procedure can quantify prediction uncertainty for DNNs. Empirical results on variable selection, calibration (CIFAR10), and UCI regression are provided.

## Strengths

- **Theorem 1 provides explicit convergence rates for sparse StoNet learning.** The rate expression (e.g., \(r_n = c_1 \frac{\sigma_{1,n}^2}{\kappa_{\min}^2} d_{1,n} p_n^s \frac{\log p_n}{n} + \dots\)) decomposes dependence on network widths, noise variances, and sparsity, making the connection to linear-model theory concrete. This is a genuine theoretical contribution for the StoNet model itself.

- **Closed-form recursive uncertainty quantification via Eve's law.** Section 4 derives a tractable recursive formula for prediction intervals of the StoNet, avoiding expensive MCMC or resampling. Table 1 shows that with appropriately small noise variances (the half-\(\sigma^2\) setting), the StoNet's coverage rates approach the nominal 95% on synthetic data generated from true DNNs.

- **Improved calibration on CIFAR10.** Table 2 shows that post-StoNet consistently reduces ECE compared to temperature scaling and matrix scaling across three architectures (DenseNet40, ResNet110, WideResNet-28-10). For DenseNet40, ECE drops from 0.119 (uncalibrated) to 0.008 (post-StoNet), versus 0.013 for temperature scaling.

- **Variable selection experiments confirm that the StoNet can recover relevant features.** The regularization-path plots (Figure 2) demonstrate that both the StoNet and a Lasso-penalized DNN can identify the five true variables among 20 correlated inputs, validating the practical behavior suggested by Theorem 1.

## Weaknesses

### Major

- **Corollary 1 (consistency of Lasso-penalized DNNs) lacks rigorous justification.** The paper asserts: "it follows from Lemma 1 that a consistent estimator of \(\theta\) can also be obtained by directly maximizing the penalized log-likelihood function of the DNN model." Lemma 1 establishes asymptotic equivalence of the *unpenalized* log-likelihoods of the StoNet (joint) and DNN (marginal). Extending this to the *penalized* setting requires additional reasoning — one needs to show that the penalty term does not break the equivalence, or provide a separate argument. The paper offers none. Since the claim that "consistent sparse deep learning can be obtained by training a DNN with an appropriate Lasso penalty" is stated as a headline contribution (abstract, introduction), and the paper explicitly notes that this theory "has not been previously established," this gap is serious. Theorem 1 properly establishes consistency for the sparse *StoNet*, but the jump to the *DNN* (Corollary 1) is asserted without proof.

- **The UCI regression comparison (Table 3) comparing interval lengths at different coverage levels is invalid.** Split conformal prediction achieves exact 0.95 coverage by construction. The post-StoNet intervals, according to the information available, show coverage rates well below 0.95 on multiple datasets (e.g., ~0.82 for Protein, ~0.88 for Physicochemical). Comparing interval lengths at different coverage levels is meaningless — shorter intervals with worse calibration are not superior. The paper claims "significant improvement in terms of the lengths of the prediction confidence intervals" without acknowledging that the coverage differs. This undermines the primary experimental evidence for the post-StoNet procedure's practical value. A fair comparison would require both methods to operate at the same coverage level (e.g., by calibrating the post-StoNet intervals on a hold-out set or embedding them inside a conformal procedure).

### Minor

- **The post-StoNet uncertainty quantification procedure lacks theoretical guarantees for DNN predictions.** Section 6.2 provides only an "intuitive justification" based on sufficient dimension reduction. No proof is given that the resulting intervals achieve nominal coverage for the DNN's predictions or for the true response. While the CIFAR10 calibration results are encouraging, the paper does not establish when or why the procedure should produce calibrated intervals for a general DNN. This limits the contribution to a heuristic rather than a principled method.

- **Lemma 1 compares a joint likelihood (StoNet, with latent variables) to a marginal likelihood (DNN), which is mathematically subtle and not explained in the main text.** The paper states: \(\sup_{\theta} |\frac{1}{n}\sum \log \pi(Y, Y_{\text{mis}}|X,\theta) - \frac{1}{n}\sum \log \pi_{\text{DNN}}(Y|X,\theta)| \xrightarrow{p} 0\). One likelihood includes the latent variables, the other marginalizes over them. The paper provides no intuition for why these should converge, and the assumptions (A1–A2) are deferred to the (stripped) appendix. Since Lemma 1 is cited from Liang et al. (2022), this does not invalidate the paper, but the lack of explanation makes the foundational bridging claim harder to evaluate.

- **Table 3 coverage details are not discussed in the main text.** The paper reports coverage rates and interval lengths but does not comment on whether the post-StoNet intervals achieve the nominal 95% coverage. This omission is important because if coverage is systematically below nominal, the claimed superiority in interval length is misleading.

### Trivial

- None beyond the standard formatting artifacts typical of parsed PDFs.

## Nice-to-Haves

- **Provide a proof sketch or formal argument for Corollary 1** showing how the unpenalized asymptotic equivalence extends to the penalized setting (e.g., by showing the penalty term is asymptotically negligible or by a direct argument on the penalized objective).
- **In the UCI experiments, calibrate the post-StoNet intervals** (e.g., using a hold-out set to adjust the variance estimate) so that both methods achieve the same empirical coverage before comparing lengths.
- **State the key assumptions A1–A2 in the main text** so that the reader can assess Lemma 1 without consulting the appendix.

## Removed Points

- *"First consistency theory for Lasso-penalized DNNs"* (from Strength Finder) — This claimed strength conflicts with the verified weakness that Corollary 1 is not properly justified. The strength overstates what is actually established.
- *"Post-StoNet UQ outperforms conformal inference on interval length"* (from Strength Finder) — This conflicts with the verified weakness that the comparison is invalid (different coverage levels). The weakness wins per the meta-review guidelines.
- *Lemma 1 is "not credible"* (from Harsh Critic, treated as fatal) — The lemma is cited from prior published work (Liang et al., 2022), not a new claim by this paper. The concern about its form is reasonable but does not rise to a fatal structural issue for the paper under review; it is retained as a minor weakness about clarity.
- *Missing appendix/proofs in appendix* (from Harsh Critic / implicit) — The parser strips these sections; they exist in the original submission.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective about the paper that meaningfully transcends what the authors themselves articulate.

## Suggestions

1. **Provide a rigorous justification for Corollary 1.** Either prove that the penalized DNN objective inherits consistency from the penalized StoNet objective (e.g., via uniform convergence of the penalized objective functions) or weaken the claim to what is actually proven (consistency of the sparse StoNet only).
2. **Fix the UCI regression comparison.** Recalibrate the post-StoNet intervals (e.g., by adjusting the variance on a hold-out set) to match the coverage of split conformal prediction, and then compare lengths at the same empirical coverage.
3. **Add theoretical guarantees or caveats for the post-StoNet UQ procedure.** Either prove asymptotic nominal coverage under stated conditions, or clearly frame the procedure as a heuristic and remove claims of superiority over conformal inference.
4. **Discuss Lemma 1 more clearly in the main text.** Explain why the joint likelihood of the StoNet converges to the marginal likelihood of the DNN, even briefly and informally, so readers can assess the bridging claim.
5. **Report calibrated Expected Calibration Error (ECE) or coverage curves** for the UCI experiments, not just average coverage and length.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/4xWQS2z77v.md` | 8.0 | Rigorous theory with clean proofs; far stronger than the current paper. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/2U8owdruSQ.md` | 6.8 | Well-received paper with clear contributions and valid evaluation; stronger overall. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/NHhjczmJjo.md` | 7.0 | Strong theory+empirics with proper justification; current paper has weaker theoretical support. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/8wAL9ywQNB.md` | 6.0 | Mixed reviews but accepted; core claims are properly supported, unlike here. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/vcX0k4rGTt.md` | 5.75 | Accepted with some weaknesses but valid central claims. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/vpo2K9Xivv.md` | 3.8 | Rejected; narrow scope and limited applicability. Current paper has more ambition and some valid components. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/lLhEQWQYtb.md` | 3.5 | Rejected; low novelty, weak experiments. Current paper is more creative. |

The paper has a creative and ambitious framework, and Theorem 1 (sparse StoNet consistency) is a genuine contribution with explicit rates. However, the headline claims — that consistency extends to Lasso-penalized DNNs (Corollary 1) and that the post-StoNet procedure demonstrably outperforms conformal prediction — are not properly supported. The gap in Corollary 1's justification and the invalid experimental comparison for UCI regression are serious enough that the central advertised contributions are not established. The paper is stronger than the rejected 3.5–3.8 anchors (which lack comparable theoretical ambition) but significantly weaker than the accepted 5.75–6.0+ anchors, whose core claims are properly justified and whose experiments support their conclusions.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>
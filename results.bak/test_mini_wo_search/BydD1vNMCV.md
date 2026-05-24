Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

The paper introduces the stochastic neural network (StoNet) as a bridge between linear models and deep neural networks (DNNs). It decomposes the DNN into a sequence of linear/logistic regressions by adding random noise to each hidden layer. The paper makes three main contributions: (1) adapting sparse learning theory (Lasso) to DNNs via the StoNet, with Theorem 1 providing convergence rates for sparse StoNet and Corollary 1 claiming consistency for sparse DNN training with Lasso; (2) a recursive uncertainty quantification method based on Eve's law through the StoNet hierarchy; and (3) a practical post-StoNet procedure that fits a simple StoNet on the last-layer outputs of a pre-trained DNN for prediction uncertainty quantification, with experimental validation on synthetic data, CIFAR-10, and UCI regression datasets.

## Strengths

- **Theorem 1 provides explicit convergence rates for sparse StoNet under Lasso**: The paper derives precise rates \(r_n\) (equations 4-5) for the IRO estimator of the sparse StoNet, showing consistency in both parameter estimation and structure selection even when layer sizes grow with \(n\). This is a concrete statistical guarantee for the sparse StoNet and constitutes the paper's most solid theoretical contribution.

- **Recursive uncertainty quantification via Eve's law**: Section 4 derives a closed-form predictive covariance using Eve's law recursively through the StoNet hierarchy and provides a complete step-by-step procedure (i–iii) to construct prediction intervals. This gives a principled uncertainty quantification method grounded in the model's probabilistic structure — a characteristic that conformal methods and simple post-hoc calibration do not offer.

- **Practical post-StoNet procedure demonstrated on multiple benchmarks**: The paper proposes a lightweight post-StoNet procedure that uses last-hidden-layer outputs of a well-trained DNN and fits a simple sparse StoNet on validation data, enabling uncertainty quantification without retraining the full model. It is demonstrated on CIFAR-10 (classification) with three architectures (DenseNet40, ResNet110, WideResNet-28-10) and on four UCI regression datasets, showing broad applicability.

- **Asymptotic equivalence lemma providing theoretical bridge**: Lemma 1 establishes that the StoNet and DNN likelihoods converge uniformly and that their MLEs converge to the same true parameters, forming the conceptual foundation for transferring theory from linear models through the StoNet to DNNs.

## Weaknesses

### Fatal
None.

### Major

- **Corollary 1 (consistency of sparse DNN with Lasso) lacks full justification**: The paper claims that training a DNN with a Lasso penalty yields a consistent estimator, and presents this as the headline result — "to the best of our knowledge, the consistency theory supporting this practice has not been previously established." The argument is: Theorem 1 proves sparse StoNet consistency under Lasso; Lemma 1 shows unpenalized StoNet and DNN likelihoods are asymptotically close. The paper then states "it follows from Lemma 1 that a consistent estimator of θ can also be obtained by directly maximizing the penalized log-likelihood function of the DNN model" (lines 114-118). However, Lemma 1 was proven for the *unpenalized* case; the jump to penalized likelihood maximization with a non-smooth Lasso penalty in high dimensions is not trivial and no proof or sketch is provided. This gap undermines the paper's most ambitious claim. The contribution would stand on Theorem 1 alone, but the paper overreaches in its framing of Corollary 1.

- **The UQ comparison with conformal prediction is misleading**: The paper claims "superiority" over split conformal prediction (abstract, conclusion) based on shorter prediction intervals, but does not ensure that post-StoNet intervals achieve nominal coverage. Conformal prediction provides distribution-free finite-sample coverage guarantees; post-StoNet does not. If post-StoNet coverage falls below the nominal 95% on some datasets while conformal meets or exceeds it (as the reviewer notes for the Protein dataset), shorter intervals may simply reflect undercoverage rather than genuine improvement. A proper comparison would either calibrate post-StoNet intervals to achieve nominal coverage, or use metrics that penalize both under- and over-coverage (e.g., interval score). As presented, the empirical evidence for post-StoNet superiority is not interpretable.

- **Variable selection evaluation lacks quantitative rigor**: The synthetic experiments (Section 5) evaluate variable selection only through visual inspection of regularization paths (Figures 2, A1, A2). For a paper that claims to "adapt sparse learning theory from linear models to DNNs" and establish consistency of structure selection, the absence of quantitative metrics — such as true positive rate, false discovery rate, or selection accuracy across repeated trials — is a significant gap. This is especially relevant given that Lasso-based variable selection in high-dimensional settings is typically evaluated with such metrics.

### Minor

- **Disconnect between theoretical results and post-StoNet procedure**: The theory (Sections 2-3) focuses on consistency of the full sparse StoNet/DNN under Lasso. The main practical contribution (post-StoNet, Section 6.2) uses a *new* simple StoNet trained on the last-layer outputs of a pre-trained DNN — not the full sparse model studied theoretically. The paper provides an "intuitive justification" (Section 6.2, paragraph 2) but no formal theory for the validity of the post-StoNet prediction intervals. While this does not invalidate either contribution, it creates a gap between the paper's theoretical apparatus and its applied method.

- **Sensitivity to \(\sigma^2\) not discussed**: Theorem 1 assumes \(\sigma^2\) is known and satisfying Assumption A1-(v). Remark 1 suggests setting \(\sigma_i^2\) to small values in practice, but this is a heuristic. The paper does not discuss how misspecified \(\sigma^2\) affects the validity of the theoretical results or the post-StoNet procedure in practice.

### Trivial
None.

## Nice-to-Haves
- The CIFAR-10 calibration results could be strengthened by discussing *why* post-StoNet outperforms temperature scaling, beyond the empirical observation. Since post-StoNet trains a new model on validation data (unlike simple post-hoc scaling), this difference should be explicitly discussed.
- Reporting the computational cost of the post-StoNet procedure (training an additional StoNet on validation data) would help practitioners assess its practicality.
- The paper could clarify whether conformal prediction was also applied on the same DNN last-layer features for a fairer comparison in the regression experiments.

## Removed Points
- **Criticism that assumptions A1-A2 should be in main text rather than appendix**: The appendix was stripped by the parser; the original submission contains these. Minor presentation concern not worth retaining.
- **Criticism that assumptions A3-A6 should be briefly stated**: Same issue — appendix content stripped.
- **Criticism that the paper does not discuss computational cost**: Minor and not central to the paper's statistical contribution; moved to Nice-to-Haves.
- **Criticism about broader applicability beyond Lasso**: Scope creep — the paper is focused on Lasso-based sparse learning and UQ.
- **Strength Finder's claim that "Corollary 1 proves consistency"**: This is aspirational rather than fully realized given the justification gap; retained as a claimed contribution but the weakness section addresses the gap.

## Novel Insights
The harsh critic's observation about the gap between Theorem 1 (sparse StoNet consistency, which is properly justified) and Corollary 1 (extension to DNNs, which is not) is the most important synthetic insight. The paper's theoretical machinery genuinely establishes results for the StoNet, but the bridge from StoNet to DNN for the *penalized* case requires additional argument that is not provided. Additionally, the observation that the comparison with conformal prediction conflates interval width with coverage validity — and that the paper would benefit from calibrating post-StoNet intervals or using proper scoring rules — is a critical methodological point that applies broadly to UQ papers making such comparisons. Beyond the paper's own contributions, no entirely novel insight emerges.

## Suggestions
1. **Strengthen Corollary 1**: Either provide a rigorous proof connecting StoNet consistency (Theorem 1) to DNN consistency under Lasso via the asymptotic equivalence, or clearly state it as a conjecture/supported by partial evidence. The current "it follows from Lemma 1" is insufficient.
2. **Fix the UQ evaluation**: Report post-StoNet interval widths *after* calibrating them to achieve nominal coverage (e.g., via validation-set adjustment), or use proper scoring rules (e.g., interval score) that penalize both under- and over-coverage. Without this, the superiority claim over conformal prediction is unsupported.
3. **Quantify variable selection accuracy**: For the synthetic experiments, run multiple replicates and report quantitative metrics (TPR, FDR, selection accuracy) as a function of the regularization parameter \(\lambda\). Visual path inspection is not sufficient evidence for a paper claiming to establish selection consistency.
4. **Explicitly discuss the scope of the theoretical results versus the post-StoNet procedure**: Acknowledge that the post-StoNet procedure is motivated by the theoretical framework but does not inherit formal coverage guarantees, and discuss under what conditions one might expect it to work well.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
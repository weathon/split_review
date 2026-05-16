Now I have enough information. Let me produce the consolidated final review.

## Summary

This paper proposes Class Probability Matching (CPM), a novel framework for label shift adaptation that matches distributions on the label variable $Y$ rather than on the feature variable $X$, reducing computational complexity from $O(n_p^3)$ (KMM) to $O(n_q K^2)$ per iteration. The proposed algorithm CPMCN integrates calibrated neural networks (BCTS) for class-probability estimation. The paper provides theoretical analysis including identifiability (Theorem 5.3), weight estimation error bounds (Theorem 5.4), and generalization bounds (Theorem 5.5). Experiments on CIFAR-100 under Dirichlet and tweak-one shifts show CPMCN outperforming matching-based (KMM, LTF, BBSL, RLLS, ELSA) and EM-based baselines in both ratio estimation and classification accuracy, with ablation studies confirming the importance of calibration.

## Strengths

1. **Novel matching framework with substantial computational benefits.** Section 3 introduces CPM, which matches on the one-dimensional label $Y$ (yielding $K$ equations) rather than the $d$-dimensional feature $X$. The resulting per-iteration complexity is $O(n_q K^2)$, compared to $O(n_p^3)$ for KMM (Zhang et al., 2013). Figure 4 empirically confirms KMM exceeding 10,000 seconds while CPMCN runs in seconds, and LTF is also substantially slower.

2. **Theoretical analysis linking calibration to improved estimation and generalization.** The paper provides three results: Theorem 5.3 (identifiability of $w^*$ from Eq. 8 under linear independence of class-conditional densities), Theorem 5.4 (bound on $\|\widehat{w}-w^*\|_2^2$ decomposed into bias and variance terms), and Theorem 5.5 (generalization bound for the target classifier). The discussion in Section 5 explicitly argues that calibration reduces the bias term ($\inf_{f\in\mathcal{F}} \mathcal{R}_p(f) - \mathcal{R}_p^*$) while negligibly increasing VC dimension, thereby tightening both bounds.

3. **Strong empirical validation.** Table 1 shows CPMCN achieves the lowest MSE_EVEN, MSE_PROP, and highest ACC on CIFAR-100 under Dirichlet shift across all $\alpha$ values (0.1–10), outperforming all compared methods. Figure 3 demonstrates that calibration (BCTS, VS, NBVS) yields large improvements over the uncalibrated version, validating the theoretical motivation. Figure 2 shows that source-domain predictor quality correlates with target-domain performance, supporting Theorem 5.5.

4. **Training curve confirms optimization behavior.** Figure 1 shows both the objective function and the ratio estimation MSE decreasing to near zero and remaining stable, empirically confirming that the BFGS solver finds a meaningful solution aligning with the theoretical justification.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Theorem 3.1 (equivalence of matching on $X$ and $Y$) lacks intuitive justification in the main text.** The forward direction (Eq. 5 ⇒ Eq. 8) can be derived from Eqs. (4)–(8) and is sound. The converse direction is nontrivial: Eq. (5) is a functional equation over all $x$, while Eq. (8) is a system of $K$ integral equations. The paper states the equivalence without providing proof or even a sketch of the converse argument in the main text. While the proof may reside in the appendix (stripped by the parser), the main text should at minimum provide the intuition or note that the full proof is deferred. This gap is partially mitigated by Theorem 5.3 (identifiability of $w^*$ from Eq. 8 under Assumption 5.1), which is the result actually needed for the algorithm — but the paper's framing claims the stronger equivalence without adequate main-text support.

2. **Non-convexity of the optimization is not discussed.** The objective in Eq. (11) is a nonlinear least-squares problem in $w$ and is not generally convex. The paper uses BFGS with a single initialization and does not discuss initialization strategy, multiple restarts, or diagnostics to ensure the global optimum is found. However, Figure 1 provides some empirical reassurance that the optimization converges stably. This is a minor practical concern that the authors should acknowledge.

3. **Main experimental table only shows CIFAR-100 results.** The paper states that experiments were conducted on MNIST, CIFAR-10, and CIFAR-100 under both Dirichlet and tweak-one shifts, but Table 1 reports only CIFAR-100 under Dirichlet shift. The reader cannot directly verify the claimed "consistent superiority" across all settings from the main text. A summary table or aggregated results for the other datasets/shifts would strengthen the presentation.

4. **MSE_EVEN and MSE_PROP are imprecisely defined.** The paper states "the original and weighted mean squared error between $w^*$ and its estimate $\widehat{w}$, respectively." It is not specified what weights are used in MSE_PROP (presumably class proportions $p(y)$ or $q(y)$). While this is enough to interpret the table, explicit formulas would benefit reproducibility.

### Trivial
None.

## Nice-to-Haves

- A brief discussion of limitations (e.g., when calibrated networks are poorly estimated, or when class-conditional densities overlap heavily).
- A clearer contrast with BBSL and RLLS: CPM uses raw probability outputs rather than hard predictions, which is important to highlight as a conceptual distinction.
- Reporting results with multiple random initializations for the BFGS solver to demonstrate stability of the solution.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Reviewer's claim that Theorem 3.1 is "likely incorrect" and that the proof is missing from the submission.** The appendix (containing proofs of theorems including Theorem 3.1) was stripped by the parser; the full proofs exist in the original submission per submission guidelines. The identifiability guarantee needed by the algorithm is provided by Theorem 5.3 under Assumption 5.1, so the paper's core claims do not rest on the full equivalence being proven in the main text.

- **Reviewer's criticism about a rate error in the theoretical bounds ("2 log n_q / n_q").** The bound is on the *squared* estimation error $\|\widehat{w}-w^*\|_2^2$, so a rate of $\log n_q / n_q$ corresponds to the standard $\sqrt{\log n_q / n_q}$ rate for the absolute error. The reviewer appears to have mistaken the squared-error bound for an absolute-error bound. The rate is consistent with standard concentration inequalities (e.g., Bernstein-type bounds for bounded random variables).

- **Reviewer's claim that MSE_EVEN and MSE_PROP are "never defined."** The paper explicitly states they are "the original and weighted mean squared error between $w^*$ and its estimate $\widehat{w}$, respectively" (Section 6, Evaluation Metrics). The definition is present, though it could be more precise.

- **Generic/padding strengths from Strength Finder** that conflict with verified weaknesses or are too vague (e.g., "Analysis linking source-domain predictor quality to target-domain performance validates the generalization bound" — this is a direct empirical sanity check, not an independent strength beyond what Figure 2 shows).

## Novel Insights

The most interesting observation emerging from the reviews is the asymmetry between the computational argument and the theoretical justification. The paper's strongest practical argument is computational: matching on $Y$ ($K$ equations) versus matching on $X$ (a functional equation or a GAN) yields orders-of-magnitude speedups that are empirically verified. Yet the paper front-loads the theoretical equivalence claim (Theorem 3.1) as its primary contribution. A more honest framing might de-emphasize the strong equivalence claim and instead highlight that (a) $w^*$ is identifiable from Eq. (8) under Assumption 5.1 (Theorem 5.3), (b) the empirical objective is computationally tractable, and (c) calibration demonstrably helps — each of which is well-supported individually. The paper would be stronger if it leaned into this pragmatic framing rather than claiming a theoretically tight equivalence whose converse direction requires nontrivial conditions.

## Suggestions

1. In the main text, provide an intuitive explanation of why the converse direction of Theorem 3.1 holds (or refer explicitly to the appendix proof), or reframe the contribution around Theorem 5.3's identifiability result without claiming the stronger equivalence.
2. Add a brief discussion of the non-convex optimization — note initialization (e.g., $w=1$ or the unweighted estimate), mention that Figure 1 shows empirical convergence, and optionally report stability across multiple restarts.
3. Include at least a summary of results for all datasets and shift types in the main text (or a table of key aggregated metrics) rather than deferring entirely to the appendix.
4. Provide explicit formulas for MSE_EVEN and MSE_PROP (e.g., $\frac{1}{K}\sum_k (\hat{w}_k - w_k^*)^2$ and $\sum_k p(y_k) (\hat{w}_k - w_k^*)^2$ or similar).

## Score and Decision

The paper presents a genuinely novel CPM framework with clear computational advantages, solid theoretical analysis (identifiability, error bounds, generalization bounds), and convincing empirical results. The main weaknesses are presentation-level (unproven equivalence claim in the main text, missing experimental summary for non-CIFAR-100 datasets, imprecise metric definitions) rather than structural. The theoretical rate concern raised by the harsh reviewer reflects a misunderstanding of squared-error bounds, and the missing-proof concern is attributable to the parser stripping the appendix. The core contributions — a new matching framework, identifiability result, computational gains, and strong empirical performance — are well-supported. The paper is ready for acceptance with minor revisions addressing the main-text justification and experimental reporting.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
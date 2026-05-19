Now let me compose the consolidated review.

---

## Summary

This paper proposes $k$-CCP, a class-conditional conformal prediction method for imbalanced classification. The core idea is double-calibration: for each class, $k$-CCP estimates both an inflated conformity-score threshold and a calibrated rank threshold (based on the classifier's top-$k$ accuracy), then includes only labels satisfying both conditions in the prediction set. The paper provides theoretical analysis (Theorem 1 on coverage, Theorem 2 on prediction set size) and experimental results on four benchmark datasets showing that $k$-CCP consistently produces smaller prediction sets than CCP and cluster-CP baselines while maintaining class-conditional coverage.

## Strengths

1. **Clear algorithmic innovation with intuitive motivation.** The double-calibration design (score threshold + calibrated rank threshold) is well-motivated and clearly explained. The idea that prediction sets can be shrunk by exploiting the classifier's top-$k$ accuracy is intuitive and practically sound. The paper explicitly shows how $k$-CCP degenerates to CCP when $\hat{k}(y)=C$, making the relationship between the methods transparent (Section 4.1, Equation 9).

2. **Strong and consistent empirical results.** Table 1 reports APSS across four datasets (CIFAR-10, CIFAR-100, mini-ImageNet, Food-101) with three imbalance types (EXP, POLY, MAJ) and two imbalance ratios ($\rho=0.5,0.1$), using both APS and RAPS scoring functions. $k$-CCP shows consistent and often substantial reductions in prediction set size over CCP and cluster-CP. The results use 10 random calibration-testing splits with standard deviations reported (Section 5.1, line 174).

3. **Useful diagnostic analysis.** The paper provides multiple justification experiments: visualizing class-wise quantile distributions vs. marginal quantiles (verifying Proposition 1), histograms of class-conditional coverage and prediction set sizes, and direct empirical measurement of $\sigma_y$ (the condition number from Theorem 2) showing values much smaller than 1 — directly linking the theoretical condition to observed behavior (Figure 1, columns 2-4).

## Weaknesses

### Fatal

None.

### Major

1. **Gap between the theoretical condition and the experimental implementation of $\tilde{\alpha}_y$.** Theorem 1 requires a *class-specific* $\tilde{\alpha}_y$ satisfying $\tilde{\alpha}_y \leq \alpha - \varepsilon_{n_y} - \delta - \epsilon_y$, where $\varepsilon_{n_y}$ depends on the per-class calibration set size $n_y$. The experimental description (Section 5.1) states: "we uniformly add $g/\sqrt{n}$ to inflate the nominated coverage $1-\alpha$ to each baseline." This uses the *total* calibration size $n$, not $n_y$, and does not account for $\epsilon_y$ or $\delta$. The paper never explicitly states the formula used for $\tilde{\alpha}_y$ in the experiments or explains how the uniform global $g$ relates to the class-specific condition in Theorem 1. This is a substantive gap between the stated theoretical guarantee and the evaluated algorithm. The empirical results are still valid, but the central theoretical claim is not convincingly linked to what was actually implemented.

2. **Data-dependence of $\hat{k}(y)$ not accounted for in the theoretical analysis.** Theorem 1 conditions on population errors $\epsilon_y = \mathbb{P}\{r_f(X,Y) > \hat{k}(y) \mid Y=y\}$, but in practice $\hat{k}(y)$ is estimated from the *same* calibration set $\mathcal{D}_{\text{cal}}$ used to compute the quantile $\widehat{Q}_{1-\tilde{\alpha}}^{\text{class}}(y)$ (see Remark 2, Equation 11, and Algorithm description in Section 4.1: "$k$-CCP estimates class-wise quantiles... and calibrates the value of $k$ for each class $y$, $\widehat{k}(y)$ on $\mathcal{D}_{\text{cal}}$ in a class-wise manner"). The theorem offers a conditional guarantee *if* the population $\epsilon_y$ values satisfy the inequality, but it does not account for the fact that $\hat{k}(y)$ is chosen from the same data used to estimate the score quantile. A rigorous analysis would need either a separate validation split for $\hat{k}(y)$, a joint concentration argument, or an explicit caveat that the guarantee holds modulo the estimation error from the data-dependent selection of $\hat{k}(y)$. As presented, the theory is incompletely justified for the actual algorithm.

### Minor

1. **Imprecise reporting of under-coverage rates (UCR).** The paper states that UCR is controlled to be "under 0.16 on CIFAR-10 and 0.03 on other datasets" (Table 1 caption) and that "$k$-CCP [has] the same as or smaller (more restrictive)" UCR than baselines. However, it does not report the actual UCR values per method per run in a table. Since the APSS comparison depends on coverage being fairly matched, readers cannot independently verify that the conditions of comparison were truly equal. Reporting exact UCR values (means and standard deviations, as done for APSS) would resolve this.

2. **Theorem 2's condition (12) is stated but not directly tested.** Theorem 2 provides a weighted aggregation condition under which $k$-CCP produces smaller prediction sets than CCP. The paper instead empirically verifies the *stronger* condition that $\sigma_y \ll 1$ individually for each class (Figure 1, last column). While this is a reasonable and convincing empirical proxy, the paper does not verify whether inequality (12) itself holds on the test data — the aggregated condition could theoretically fail even if individual $\sigma_y$ values are small, depending on the base rates $\mathbb{P}[V \leq \widehat{Q}_{1-\alpha}^{\text{class}}(y)]$.

3. **Sensitivity analysis is limited.** Figure 2 shows sensitivity to $g$ only for one imbalance type (EXP) and one ratio ($\rho=0.1$). Expanding to more settings would strengthen the analysis, though the core results in Table 1 are already comprehensive.

4. **No discussion of computational overhead.** $k$-CCP requires estimating both score quantiles and rank thresholds per class, adding cost compared to CCP. The paper does not acknowledge this, even briefly.

### Trivial

None.

## Nice-to-Haves

- A clear pseudocode or explicit step-by-step description of the full $k$-CCP procedure (including how $\tilde{\alpha}_y$ is set) in the main text would improve reproducibility. The current text references "Algorithm 1" but the algorithm box is not present in the extracted text (likely a figure), and the description is spread across Sections 4.1 and 4.2.
- A discussion of when $k$-CCP does not help (e.g., on CIFAR-10 where it reduces to CCP) as a practical limitation — the paper mentions this but could state it more prominently.
- Statistical significance tests (e.g., paired tests across runs) for the APSS differences would strengthen the empirical claims.

## Removed Points

These points from the inputs were removed or downgraded; treat them with caution:

1. **Criticism that Proposition 1 is "essentially a restatement"** — Removed. This is a subjective judgment that undersells the value of formalizing the failure condition. The proposition is a legitimate formal result that characterizes when and why marginal CP fails on a class-conditional level.

2. **Criticism that Theorem 2 is "essentially a restatement"** — Removed. Theorem 2 provides a formal condition linking $\sigma_y$ to prediction set size reduction; it is a genuine, if straightforward, theoretical result.

3. **"Incomplete algorithm specification" (as a fatal/structural issue)** — Downgraded to nice-to-have. The algorithm is specified in prose: Equation (9) defines the prediction set construction, Equation (11) gives $\hat{k}(y)$, and Remark 2 explains how $\tilde{\alpha}_y$ relates to the condition in Theorem 1. The description is sufficient to understand and (with some effort) implement the method. A pseudocode box would improve clarity but its absence is not a structural flaw.

4. **Multiple formatting/style nitpicks** — Removed per hard rules.

## Novel Insights

The reviews surface a genuine limitation that the paper itself does not fully engage with: the double-calibration procedure (estimating both the score quantile and the rank threshold from the same calibration set) introduces a statistical dependence that the current theoretical analysis sidesteps by conditioning on population-level $\epsilon_y$. This creates a gap between the finite-sample guarantee claimed for the algorithm and the actual finite-sample behavior — the $\varepsilon_{n_y}$ term in Theorem 1 accounts only for concentration of the quantile estimate, not for the data-dependent selection of $\hat{k}(y)$. The paper treats $\hat{k}(y)$ as a fixed design choice when it is actually an estimated quantity. This is a missing layer in the finite-sample analysis that a careful revision could address (e.g., via a validation split or a union-bound argument).

## Suggestions

The paper has real empirical merit, but the theoretical analysis needs to be brought into alignment with the implemented algorithm. Specific recommendations:

1. **Explicitly state the exact formula for $\tilde{\alpha}_y$ used in experiments** and discuss whether/how it satisfies the condition in Theorem 1. If the experimental setup uses $\tilde{\alpha}_y = \alpha - g/\sqrt{n}$ (uniform), explain this is a heuristic, or show how a Bonferroni-style correction relates to the class-specific theoretical condition.

2. **Address the data-dependence of $\hat{k}(y)$** in the theoretical analysis. Either adopt a validation-split approach (choose $\hat{k}(y)$ on a held-out subset, calibrate quantiles on the remainder) so that independence holds, or provide a rigorous joint finite-sample guarantee using concentration inequalities that account for both the quantile and rank-threshold estimation simultaneously.

3. **Report exact UCR values** (means and standard deviations, per method and setting) alongside the APSS results, so readers can verify that the coverage comparison is indeed fair.

## Score and Decision

The paper proposes a well-motivated algorithm with strong empirical validation. However, the theoretical analysis has a significant gap: the class-specific condition in Theorem 1 is not clearly connected to the uniform-inflation experimental implementation, and the data-dependent selection of $\hat{k}(y)$ from the same calibration set used for quantile estimation is not accounted for in the finite-sample analysis. Since the paper claims theoretical guarantees as a primary contribution, these gaps must be resolved. Given the strength of the empirical results and the clarity of the algorithmic idea, the paper could be suitable after substantial revision that aligns the theory with practice or honestly caveats the theoretical claims.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
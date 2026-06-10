## Summary

This paper proposes an End-to-End Conformal Prediction (E2E-CP) framework for shrinking-horizon trajectory optimization in uncertain environments. The core idea is to compute posterior collision probabilities from realized trajectories and use them to reallocate risk across future time steps, creating a feedback loop from the decision-making layer back to the CP layer. The authors provide theoretical guarantees (Corollary 4.1) that the posterior risk is bounded by the prior risk with high probability, and propose both an average-based (ARA) and an iterative (IRA) risk allocation algorithm.

## Strengths

1. **Principled handling of exchangeability for posterior risk calculation (Lemma 4.2, Section 4.2):** The paper correctly identifies that the realized state $x_\tau^*$ depends on $D_{cal}^1$ (used to construct prediction regions), so using that same data to compute posterior risk $\beta_\tau$ would break exchangeability. The solution — holding out $D_{cal}^2$ and using only that independent subset — is a clean, technically sound response to a non-trivial dependency issue that arises when coupling CP with downstream optimization.

2. **Theoretical guarantee that posterior risk is bounded by prior risk (Corollary 4.1):** The paper proves $\mathbb{P}\{\mathbb{E}(\beta_\tau) \leq (1 + L(\alpha_\tau + \sqrt{-\ln\delta/(2K)}))/(1+L)\} \geq 1-\delta$, and that $\mathbb{E}(\beta_\tau) \leq \alpha_\tau$ holds with probability one as $K,L\to\infty$. This is the theoretical linchpin justifying why the feedback loop releases risk slack without compromising the coverage guarantee.

3. **Iterative Risk Allocation with monotonic convergence guarantee (Theorem 5.1):** The IRA algorithm (two-step tightening of inactive constraints and relaxing of active constraints) is shown to produce a monotonically non-increasing objective sequence that converges to a finite limit under bounded state/control sets and a continuous objective. This provides a formal foundation for the risk-allocation step.

4. **Clear articulation of the CP-to-decision-making disconnect (Section 1):** The paper pinpoints a specific structural limitation — "information channel blockage from the decision-making end to the CP end" — providing a well-framed technical problem that the proposed method directly addresses.

## Weaknesses

### Fatal
None.

### Major

1. **Insufficient baseline comparison.** The only baseline is Sequential CP with uniform fixed risk allocation ($\alpha_\tau = \alpha/T$). The paper's related work (lines 25, 27) cites adaptive CP methods — ACI (Gibbs & Candes, 2021), EnbPI (Xu & Xie, 2021), CopulaCPTS (Sun & Yu, 2023) — and notes that Dixit et al. (2023) and Zhou et al. (2024a) applied ACI to trajectory optimization. Yet none are used as experimental baselines. The reported cost reductions (11.26% for ARA, 83.05% for IRA) are relative only to the weakest possible comparator. Without comparison against an adaptive baseline, the paper cannot substantiate that the *specific posterior-risk feedback mechanism* drives the improvement, as opposed to any adaptive scheme outperforming a static one. This is a structural gap in the evaluation.

2. **Results reported for only one of three claimed models.** Line 248 states that experiments were conducted on "a kinematic vehicle model, a 3D linear quadrotor model, and a dynamic bicycle model." However, Table 1 (line 260) is explicitly labeled "using the vehicle model," and the entire Results section (lines 252–271) discusses only the vehicle model. No quantitative results for the quadrotor or bicycle models appear anywhere in the readable text. The claim of generalizable effectiveness across multiple platforms is unsubstantiated.

3. **Unsupported claim about robustness to distribution shifts.** Line 268 states: "we have empirically demonstrated the proposed method exhibits a certain degree of robustness to moderate distribution shifts and can maintain safety and high performance in realistic scenarios (beyond Assumption 3.1)." No experiment violating Assumption 3.1 is described, no distribution shift scenario is defined, and no quantitative evidence is provided. This factual claim is presented without supporting evidence and should either be removed or substantiated.

### Minor

1. **No variance or confidence intervals reported.** Despite running 1,000 Monte Carlo simulations, the paper reports only point estimates ("11.26% reduction," "83.05% reduction") without standard deviations, confidence intervals, or any measure of dispersion. The reader cannot assess the variability or reliability of the reported improvements.

2. **Specific cost function form not given.** The cost function $J$ is described generically (lines 49–50) but its concrete form for each experimental setting is not specified, making it unclear what "cost reduction" means quantitatively in each scenario.

3. **IRA computation time not quantified.** The paper states that IRA computation time "increases significantly" (line 264) but reports no actual computation times, making it impossible to assess the practical trade-off between performance gain and computational cost.

4. **Finite-sample gap not examined empirically.** Corollary 4.1's finite-sample bound is looser than the asymptotic result, and the paper honestly acknowledges (line 139) that $\beta_\tau$ could exceed $\alpha_\tau$. However, no diagnostic experiment examines how often this occurs or its impact on trajectory cost under realistic calibration set sizes.

### Trivial
None.

## Nice-to-Haves
- Compare against an adaptive CP baseline such as ACI applied to the same TO setting. This would isolate whether the posterior-risk mechanism adds value beyond generic online adaptation.
- Report full results — including variance measures — for all three dynamical models.
- Add a diagnostic experiment examining cases where $\beta_\tau > \alpha_\tau$ and quantifying its frequency and impact.
- Report IRA computation times alongside cost improvements.
- Specify calibration dataset sizes ($K$, $L$, $N$) and IRA stopping criterion.

## Removed Points

These points were considered but removed after verification against the paper:

- **"Multi-model experimental validation" strength** (from Strength Finder): Removed because it conflicts with verified weakness #2 — the paper claims three models but reports results for only one.
- **Missing ablation study** (from Harsh Critic): Removed — the comparison structure SeqCP ↔ E2E-CP+ARA isolates the feedback effect, and ARA ↔ IRA isolates the allocation strategy effect, providing a natural ablation.
- **Missing appendix / proofs / references**: Removed per filter rules — the parser strips these from all papers.
- **Table 1 being an inaccessible image**: Removed as a parser artifact, not an author error.
- **Notation inconsistency (Lemma 5.2 vs Lemma 5.5) and symbol shifts**: Removed — these are parser/garbling artifacts, not author errors.
- **Formatting and presentation observations**: Removed per filter rules.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a clear gap between the paper's theoretical contribution (which is solid — the exchangeability handling in Lemma 4.2 is genuinely clever) and its experimental evaluation (which is incomplete in ways that prevent validation of the core claims). The most interesting tension is that the paper identifies and solves a subtle dependency problem that prior work overlooked, yet the evaluation does not match the rigor of the theory.

## Suggestions

1. Add at least one adaptive CP baseline (ACI or EnbPI) to the experiments to isolate the source of improvement.
2. Report complete results — including variance — for the quadrotor and bicycle models.
3. Either remove the distribution shift claim (line 268) or substantiate it with targeted experiments that violate Assumption 3.1.
4. Add a diagnostic experiment examining finite-sample behavior when $\beta_\tau > \alpha_\tau$.
5. Report IRA computation times to enable practical assessment of the cost-performance trade-off.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
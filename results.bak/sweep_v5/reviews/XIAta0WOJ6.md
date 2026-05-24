Here is the consolidated review.

---

## Summary

This paper studies stochastic bilevel optimization under the nonconvex-strongly-convex setting and proposes F²SA-\(p\), a family of fully first-order methods that generalize F²SA by using \(p\)th-order finite differences to approximate the hyper-gradient. The central theoretical contribution is an SFO complexity bound of \(\tilde{\mathcal{O}}(p\kappa^{9+2/p}\epsilon^{-4-2/p})\) for \(p\)th-order smooth problems, improving from the prior \(\tilde{\mathcal{O}}(\epsilon^{-6})\) when \(p=1\) to rates approaching \(\tilde{\mathcal{O}}(\epsilon^{-4})\) as \(p\) grows. The paper also establishes an \(\Omega(\epsilon^{-4})\) lower bound via a clean separable construction, showing near-optimal \(\epsilon\)-dependency in the highly-smooth regime.

## Strengths

1. **Novel connection between bilevel optimization and finite-difference schemes.** Interpreting F²SA as a forward-difference hyper-gradient estimator and generalizing it to higher-order finite differences (central difference for \(p=2\), general \(p\)th-order stencils) is an elegant and original conceptual contribution. This viewpoint naturally motivates the improved algorithm and connects bilevel optimization with classical numerical analysis.

2. **First SFO complexity bound for fully first-order bilevel methods that provably improves with higher-order smoothness.** Theorem 3.1 delivers the bound \(\tilde{\mathcal{O}}(p\kappa^{9+2/p}\epsilon^{-4-2/p})\), which directly shows that as \(p\) increases, the exponent on \(\epsilon\) decreases from \(-6\) (at \(p=1\)) toward \(-4\) (large \(p\)). Remark 3.4 shows that when \(p = \Omega(\log(\kappa/\epsilon)/\log\log(\kappa/\epsilon))\) the rate collapses to \(\tilde{\mathcal{O}}(\kappa^9\epsilon^{-4})\), matching HVP-based methods under stronger assumptions.

3. **Cleaner and more rigorous lower bound.** Theorem 4.1 establishes an \(\Omega(\epsilon^{-4})\) lower bound via a fully separable construction that avoids the smoothness violations present in prior bilevel lower bounds (Kwon et al., 2024a; Dağrı et al., 2024). The construction automatically satisfies all the paper's high-order smoothness assumptions, making the \(\epsilon\)-dependency near-optimality claim for large \(p\) well-supported.

4. **Tighter analysis even for the base case \(p=1\).** Remark 3.3 notes that the analysis improves the state-of-the-art bound for \(p=1\) from \(\tilde{\mathcal{O}}(\kappa^{12}\epsilon^{-6})\) (Chen et al., 2025b) to \(\tilde{\mathcal{O}}(\kappa^{11}\epsilon^{-6})\), improving by a factor of \(\kappa\) through sharper lower-level SGD analysis.

5. **Lemma 3.2 tightens prior Lipschitz bounds.** The Lipschitz continuity result for \(\frac{\partial^{p+1}}{\partial\nu^p\partial\mathbf{x}}\ell_\nu(\mathbf{x})\) uses Faà di Bruno to avoid direct calculation of higher derivatives, and Remark 3.2 notes that for \(p=2\) this tightens the prior \(\mathcal{O}(\kappa^6\bar{L})\) bound to \(\mathcal{O}(\kappa^5\bar{L})\).

## Weaknesses

### Fatal
None.

### Major

1. **Experiments do not directly test the paper's central theoretical claim.** The main result (Theorem 3.1) predicts that higher \(p\) improves the \(\epsilon\)-dependency in SFO complexity from \(\tilde{\mathcal{O}}(\epsilon^{-6})\) to \(\tilde{\mathcal{O}}(\epsilon^{-4-2/p})\). To validate this, one would need to measure the number of SFO calls required to reach a given gradient norm \(\|\nabla\varphi(\mathbf{x})\| \leq \epsilon\) for different \(p\) and show that the scaling improves with \(p\). Instead, the experiments report only test loss and accuracy after a fixed number of outer iterations (1000) with \(K=10\) inner steps for one problem instance. These results do not measure stationarity at all, are not shown as a function of total SFO calls, and do not establish any improvement in \(\epsilon\)-dependency. For a paper whose main deliverable is a complexity rate improvement, this is a significant evidential gap. Even a single plot of gradient norm vs. total SFO calls for two values of \(p\) (e.g., \(p=2\) and \(p=10\)) on a synthetic problem with a known hyper-gradient would substantially strengthen the validation.

### Minor

2. **Algorithm uses normalized gradient steps in the outer loop without empirical comparison to standard steps.** Algorithm 1 (line 14) updates \(\mathbf{x}_{t+1} = \mathbf{x}_t - \eta_x \Phi_t / \|\Phi_t\|\). The authors note in Remark 3.1 that normalization "can control the change of \(\mathbf{y}_{j\nu}^*(\mathbf{x}_t)\) and make the analysis of inner loops easier" and state belief that guarantees also hold for standard steps. However, this is a non-trivial modification: normalized gradient descent is not the standard choice for stationary-point finding, and the theory depends on it. The paper neither proves necessity nor provides an experiment comparing normalized vs. unnormalized updates. This weakens the practical relevance of the algorithmic contribution.

3. **Limited experimental scope and missing standard reporting practices.** The experiments cover only one problem (logistic regression on 20 Newsgroups). While the paper mentions additional MLP experiments in Appendix F (which is stripped and cannot be verified here), the main text lacks error bars, multiple seeds, or wall-clock time comparisons. The performance differences between F²SA-\(p\) variants (loss range ≈ 0.70–0.85, accuracy range ≈ 0.77–0.81) are relatively small, and without uncertainty quantification it is difficult to assess whether the advantage of higher \(p\) is statistically significant.

4. **The lower bound construction decouples the bilevel structure.** Theorem 4.1 uses \(f(\mathbf{x},\mathbf{y}) \equiv f_U(\mathbf{x})\) (independent of \(\mathbf{y}\)) and \(g(\mathbf{x},\mathbf{y}) = \mu\|\mathbf{y}\|^2/2\) (independent of \(\mathbf{x}\)). This reduces the bilevel instance to single-level optimization from a lower-bound perspective. While the \(\Omega(\epsilon^{-4})\) bound is valid and the construction is technically within the problem class, it does not reflect any coupling between the two levels. The paper therefore does not rule out that the true minimax rate for genuinely coupled bilevel problems could be worse than \(\epsilon^{-4}\) or require a different \(\kappa\) dependence. The authors acknowledge the \(\kappa\) gap but not the \(\epsilon\) scope limitation. (This does not undermine the lower bound's validity for the stated function class, but it limits what the "near-optimality" claim conveys.)

### Trivial
None.

## Nice-to-Haves

- A synthetic problem with a known hyper-gradient (e.g., a quadratic bilevel instance) where the gradient norm can be computed exactly would allow direct validation of the claimed convergence rate scaling with \(p\).
- An ablation study varying the inner loop length \(K\) for a fixed \(p\) would test whether the theory's logarithmic dependence on \(K\) is reasonable.
- Reporting wall-clock time or per-iteration cost for different \(p\) would help practitioners assess the trade-off: higher \(p\) requires solving more lower-level problems per outer iteration.

## Removed Points

The following points from the input reviews were removed:

1. **Criticism that the lower bound construction is "not meaningful for genuinely bilevel instances"** — Removed. This claim misunderstands the purpose of a lower bound. A lower bound for a function class only needs one hard instance within that class; the construction being simple makes it a cleaner proof, not a weaker result. The construction is explicitly within the paper's assumption class.

2. **Criticism that the comparison with HVP-based methods is "perfunctory"** — Removed. The paper compares F²SA-\(p\) against three HVP-based methods (stocBiO, MRBO, VRBO) and a baseline in Figure 1. The comparison is present and the results are reported.

3. **Generic "unfair comparison" concerns** — Removed where they reflect asymmetry favoring baselines, per the filtering rules.

4. **Formatting/style nitpicks and typos** — Removed as parser artifacts.

5. **Missing related works** — Removed per the rule that the reviewer cannot verify the existence of uncited works.

6. **Missing appendix content or proofs** — Removed per the rule that these are stripped by the parser.

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder largely agree on the paper's core claims and quality; no new synthesis or cross-review pattern emerged that the paper's own analysis does not already cover.

## Suggestions

1. **Add a direct validation of the rate improvement.** Even one plot showing \(\|\nabla\varphi(\mathbf{x})\|\) vs. total SFO calls for two \(p\) values (e.g., \(p=2\) and \(p=10\)) on a simple problem (e.g., a synthetic quadratic bilevel instance where the hyper-gradient is computable) would significantly strengthen the paper. This is the single most impactful addition.

2. **Compare normalized vs. unnormalized outer-loop updates.** A brief experiment comparing Algorithm 1's normalized step with a standard (non-normalized) gradient step would address the concern about whether normalization is necessary or is harming performance.

3. **Add error bars or multiple-seed reporting** for the main experiment to establish the statistical significance of the observed improvement with higher \(p\).

4. **Discuss the scope of the lower bound more carefully.** Acknowledge explicitly that the separable construction does not exercise bilevel coupling, and clarify that the \(\epsilon\)-dependency near-optimality claim applies to the \(\epsilon\) exponent in the function class \(\mathcal{F}^{\text{nc-sc}}\) (which includes decoupled instances), not to the minimally achievable complexity for coupled problems at fixed \(\kappa\).

---

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/fMTPkDEhLQ.md` | 8.00 | Pure theory paper on tight lower bounds under higher-order smoothness; stronger than current paper because it has no experimental gap and its bounds are tight. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/vgV4y086FY.md` | 6.75 | DP bilevel optimization, first-of-its-kind, no experiments; comparable overall — current paper has more novel theoretical machinery but also has experimental gaps. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/bKzX0m6TEZ.md` | 6.25 | Constrained bilevel with conditional gradient, solid theory; comparable theoretical depth but different sub-area. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Zb6qOouUJO.md` | 5.75 | Variance-reduced single-loop method, better experiments but less novel theory; current paper is stronger in originality. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/SXTmAdGjlg.md` | 4.60 | Adaptive bilevel, decent but not outstanding; current paper is significantly stronger in both theory and execution. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/2fSyBPBfBs.md` | 4.17 | Bilevel without strong convexity, had proof errors and toy experiments; current paper is much stronger. |

The paper under review presents a genuinely novel theoretical contribution (connecting finite differences to bilevel optimization, generalizing to arbitrary smoothness order \(p\)) that is well-executed and advances the state of the art. The main weaknesses are evidential — the experiments do not directly validate the central complexity claim — and the normalization modification is unexamined. However, for a theory-heavy paper these are not fatal. The theoretical results are solid and the core idea is elegant. The paper is stronger than the 5.75 and 4.60 anchors and broadly comparable to the 6.25–6.75 anchors, though the experimental gap prevents it from reaching the 7+ band.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
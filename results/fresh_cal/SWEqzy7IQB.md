Based on my thorough reading of the full paper and careful verification of each claim against the visible text, here is my consolidated review.

---

## Summary

This paper proposes the Accelerated Over-Relaxation Heavy-Ball (AOR-HB) method, which replaces the gradient term in the classic Polyak heavy-ball update with an over-relaxed combination \(2\nabla f(x_k) - \nabla f(x_{k-1})\). The authors develop a continuous-time Lyapunov analysis via a first-order rotated gradient flow ODE, claim global accelerated linear convergence for smooth strongly convex problems, and extend the approach to composite convex and strongly-convex-strongly-concave saddle-point problems with bilinear coupling. Empirical results on piecewise-smooth, logistic regression, Lasso, \(\ell_1\)-\(\ell_2\), and MSPBE policy evaluation problems compare against standard baselines.

## Strengths

- **Novel over-relaxation modification that provably accelerates the heavy-ball family.** The paper identifies a clever, minimal change to the heavy-ball update — using \(2\nabla f(x_k)-\nabla f(x_{k-1})\) instead of \(\nabla f(x_k)\) — and provides a Lyapunov analysis via a first-order rotated gradient flow ODE (Lemma 2.1, Section 2) that is cleaner than analyses based on second-order ODEs. This is a genuine conceptual advance over prior heavy-ball variants, which either lacked acceleration (Ghadimi et al., Sun et al.) or only achieved it locally for quadratics (Polyak). The paper correctly situates its contribution within the known impossibility result of Goujaud et al. (2023).

- **Extension to saddle-point problems with an explicit algorithmic scheme.** Algorithm 3 (AOR-HB-saddle) provides a complete, implementable method for strongly-convex-strongly-concave bilinear problems, with a stated iteration complexity \(\mathcal{O}\bigl(\sqrt{L_f/\mu_f+L_g/\mu_g+\|B\|^2/(\mu_f\mu_g)}\,\log(1/\epsilon)\bigr)\) that matches optimal first-order methods. The semi-implicit variant (Remark 3.1) is a practical contribution for settings where \(BB^\top\) is small.

- **Clear ODE-level Lyapunov analysis.** The derivation of the strong Lyapunov property for system (6) in Section 2 is concise and mathematically sound, establishing exponential stability for the continuous-time system in a transparent way that avoids the opacity of second-order ODE or velocity-form analyses.

- **Numerical experiments on saddle-point problems show practical speedups.** Figures 5 and 6 on the MSPBE policy evaluation problem demonstrate that AOR-HB-saddle and its semi-implicit variant outperform AG-OG, APDG, LPD, and EG in terms of iteration count, with the advantage growing with the condition number. The log-log scaling in Figure 6 visually confirms the \(\mathcal{O}(\sqrt{\kappa_g})\) complexity for accelerated methods versus \(\mathcal{O}(\kappa_g)\) for EG.

## Weaknesses

### Fatal
None.

### Major
- **Experiments lack statistical rigor.** Every figure (Figures 1–6) shows single-run trajectories with no error bars, no variance estimates, and no indication of replication across random seeds or data realizations. This is particularly concerning for the logistic regression experiment (Figure 2), where the relative ordering of methods could change with different random data draws. For a methodological paper whose contribution rests partly on empirical validation, the absence of any uncertainty quantification is a significant gap. The paper's own stated limitation that "stochastic conditions" are future work does not excuse the lack of deterministic replication.

### Minor
- **The non-strongly convex variant (equation (9)) is asserted without proof or analysis.** Lines 96–102 state that the variant with dynamic time rescaling "achieves an accelerated rate of \(\mathcal{O}(1/k^2)\), comparable to NAG." No derivation, proof sketch, or even a reference to where the proof can be found is provided. If this is a claimed contribution, it needs support; if it is a heuristic, it should be labeled as such. As presented, it is an unsupported claim.

- **The step-size selection \(\alpha\) for the saddle-point method (Algorithm 3) is computationally nontrivial but uncommented upon.** Line 183 defines \(\alpha = \max_{\beta\in(0,1)} \min\{\sqrt{\beta} \min\{\sqrt{\mu_f/L_f},\sqrt{\mu_g/L_g}\}, (1-\beta)\sqrt{\mu_f\mu_g}/\|B\|\}\). This requires solving a 1D max-min problem. The paper provides no closed-form solution and no discussion of how to compute \(\alpha\) efficiently in practice. For a method that claims to "require fewer parameters to tune," the burden of computing \(\alpha\) is relevant to that claim.

- **Overstated scope in one motivating claim.** The introduction states that "little is known beyond convex optimization" for accelerated methods (line 64), citing Lin et al. (2015) and Drusvyatskiy et al. (2018) — references that themselves address composite and non-convex acceleration. This weakens the motivation. The paper's genuine contribution (heavy-ball acceleration) does not need this overstatement.

### Trivial
- The claim that AOR-HB "requires fewer parameters to tune" (line 336) is stated without quantification. Both AOR-HB and its baselines require estimates of \(\mu\) and \(L\) (or their saddle-point analogs). The difference in tuning burden is not substantiated.

## Nice-to-Haves
- Adding error bars or multiple-seed replication to the experiments would substantially strengthen the empirical case.
- A brief comment on computing the saddle-point step-size \(\alpha\) (e.g., closed-form for common special cases, or a simple bisection remark) would help practitioners.
- A comparison against a Nesterov-type accelerated method on the same saddle-point problems (e.g., Zhang et al., 2022) would make the saddle-point evaluation more comprehensive, since the current baselines (APDG, LPD) are the most natural comparators but the landscape is broader.

## Removed Points

These points are flagged to be removed — treat them with caution.

- **Missing discrete convergence proof / equations (14), (19), scheme (I4).** The harsh critic faults the paper for deferring the discrete convergence argument to content not visible in the extracted text. However, the parser strips appendix and supplementary sections from all papers. The instruction is to assume these exist in the original submission. Removed per policy.

- **Missing Algorithm 1 and Algorithm 2 in the main text.** Same rationale: these were likely in sections stripped by the parser. Removed per policy.

- **"Comparing to FISTA on Lasso is standard, but missing modern variants."** This is a generic criticism that does not name which variants are missing. Removed as not specific enough.

- **"HB converges faster than AOR-HB on logistic regression."** The paper openly acknowledges this (lines 286–287: "this is an example where HB converges and it converges fastest") and uses it to argue for the importance of theoretical guarantees. This is honest reporting, not a weakness. Removed as strawman.

- **"The paper does not discuss how \(\mu\) and \(L\) are estimated."** For the tested problems, \(\mu\) and \(L\) are known or set artificially. The paper notes this as a general limitation in Section 5 ("exploring adaptive strategies to reduce parameter dependence"). Removed as already addressed.

- **"Code is not mentioned."** Remove per policy against reproducibility nitpicks about large artifacts.

- **"The Lasso experiment cannot reach \(10^{-3}\) accuracy."** The paper explains why (line 301: "the ground-truth solution may not be the minimizer"). Removed as the authors already address this.

- **General claims about "overstated novelty" regarding closing a "long-standing theoretical gap."** In the specific context of the heavy-ball method family, where Goujaud et al. (2023) proved that standard HB provably cannot achieve global acceleration, providing the *first* HB variant with proven global accelerated convergence genuinely closes a gap in that literature. Nesterov's method is a different algorithmic family. This claim is reasonable when read in context.

- **Speculation that "the appendix may contain a valid proof" but the paper "asks the reader to accept... on faith."** Per policy, appendix content is treated as existing. Removed.

## Novel Insights

None beyond the paper's own contributions. The key observation — that replacing \(\nabla f(x_k)\) with \(2\nabla f(x_k)-\nabla f(x_{k-1})\) in the heavy-ball update symmetrizes the error equation and enables a clean Lyapunov analysis — is the paper's own contribution, not something synthesized from the reviews.

## Suggestions

1. Add replication information (means/variance over multiple random seeds or data realizations) to all experiments. Even 5–10 runs with standard deviation bands would substantially strengthen the empirical section.
2. Remove or qualify the "little is known beyond convex optimization" statement to avoid unnecessary overclaim.
3. Either provide a proof or explicitly label the non-strongly convex variant (equation (9)) as a heuristic.
4. Add a brief note on how to compute the saddle-point step-size \(\alpha\) efficiently, or provide a closed-form expression for common special cases.

## Score and Decision

The paper presents a genuinely interesting modification to the heavy-ball method with a clean continuous-time Lyapunov analysis and plausible extensions to composite and saddle-point problems. The core theoretical idea is sound and the contribution to the heavy-ball optimization literature is meaningful. However, the empirical evaluation is notably weak — all experiments are single-run with no uncertainty quantification — and a few claims are insufficiently supported (the non-strongly-convex variant, the saddle-point step-size computation). The paper's strengths in theoretical framing and the novelty of the over-relaxation technique are real, but the thin experimental rigor prevents full confidence in the practical claims.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>
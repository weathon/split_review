Now I have all the information I need. Let me write the consolidated review.

---

## Summary

This paper revisits FedExProx, a parallel proximal method with extrapolation for federated learning. The authors show that the original analysis (Li et al., 2024) yields complexity bounds for quadratics that are no better than vanilla gradient descent. They develop a new analysis framework establishing a tighter linear convergence rate for non-strongly convex quadratic problems, and introduce a time complexity model (accounting for both computation and communication) that proves FedExProx can provably outperform GD when communication dominates computation. The paper further extends the analysis to partial participation, adaptive extrapolation strategies (GraDS, StoPS), PL functions, and inexact proximal computations, with supporting experiments on quadratics and smooth hinge loss.

## Strengths

- **Tighter linear convergence rate for quadratics (Theorem 1):** The new iteration complexity \(O(L_\gamma / \mu^+_\gamma)\) is a genuine improvement over both the prior bound and the vanilla GD rate \(O(L/\mu^+)\). The diagonal example (Section 4.1) provides a concrete case where the improvement factor can be \(\Omega(L/\mu^+)\).

- **Time complexity model proves FedExProx never worse than GD (Theorem 2):** The total time complexity \(T_\mu(\gamma)\) is bounded above by \(T_\text{GD}\), with strict improvement when communication dominates computation (\(\mu/\tau \ge 2\)). This is the paper's central theoretical advance, directly contrasting with the pessimistic conclusion from the original analysis.

- **Extension to partial participation with same optimal \(\gamma\):** Theorems 3 and 4 show that the tighter analysis extends naturally to the stochastic setting with nice sampling while preserving the same optimal \(\gamma\) range, demonstrating robustness of the theoretical framework.

- **Extension to PL condition under weaker assumptions than prior work:** Theorem 6 (and the inexact variant Theorem 7) establishes linear convergence under PL, which is strictly more general than the strong convexity required by Li et al. (2024). This broadens the applicability of the method.

- **Adaptive extrapolation strategies (GraDS, StoPS) with semi-adaptivity:** Theorem 5 provides convergence rates matching the constant-extrapolation rate without requiring knowledge of the optimal \(\alpha\), extending the adaptive frameworks of Horváth et al. and Li et al. to the tighter quadratic analysis.

- **Clear exposition of why the original bound was loose (Section "Why do we get a tighter analysis?"):** The paper identifies the specific technical cause — the reliance on the inequality \(M^\gamma(x)-M^\gamma(x_*) \ge \frac{1}{1+\gamma L_\max}(f(x)-f(x_*))\) — and explains how their approach bypasses it by working directly in the parameter space rather than through function values.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **No explicit GD baseline in the experimental plots:** The experiments show FedExProx's total empirical time as U-shaped curves as a function of \(\gamma\). While the limit \(\gamma \to 0\) is connected theoretically to GD, the paper never plots GD's total time as an explicit horizontal baseline on the same axes. For the central claim that FedExProx "outperforms GD," the reader must infer this by comparing the minimum of the U-shaped curve to the value at the leftmost \(\gamma\). An explicit baseline would make this comparison direct and more convincing.

- **No experiments with adaptive extrapolation strategies:** Section 6 presents theoretical convergence guarantees for FedExProx-GraDS and FedExProx-StoPS, but neither strategy is tested empirically. The paper would benefit from at least one synthetic comparison showing whether the adaptive extrapolation matches or approaches the constant-optimal-\(\alpha\) performance.

- **No error bars or variance reporting for stochastic experiments:** The partial participation experiments (Figure 2) involve random client sampling, yet the results are reported as single curves without confidence intervals, error bars, or multiple-run statistics. This makes it difficult to assess the reliability of the observed U-shaped patterns under sampling noise.

- **Vague "multiplicative factor" in theory-practice comparison:** The paper states that the theoretical and empirical time complexities match "up to a multiplicative factor" (Figure 5), but the factor is never reported or discussed. This weakens the validation — it is unclear whether the factor is constant across \(\gamma\) or functionally dependent, and whether the agreement is qualitative or quantitative.

- **Small-scale experimental setups:** The quadratic experiments use \(d=7\) dimensions with \(n=14\) workers, and the hinge-loss experiments use \(d=3\) with \(n=4\) workers each holding \(m=4\) datapoints. While these suffice to demonstrate the U-shaped phenomenon, the scale is far from realistic FL settings, leaving open questions about whether the patterns persist at larger scales.

### Trivial

- The phrase "up to a multiplicative factor" in the theory-practice comparison (line 435) could be made more precise — even stating that the factor is empirically approximately constant across \(\gamma\) would strengthen the claim.

## Nice-to-Haves

- Report the numerical multiplicative factor (and its variation with \(\gamma\)) between theoretical and empirical time complexities in Figure 5.
- Include at least one experiment comparing adaptive extrapolation (GraDS/StoPS) against constant-optimal \(\alpha\) to demonstrate practical convergence behavior.
- Discuss how the optimal \(\alpha\) cost (eigenvalue computation vs. grid search) affects practical deployment.

## Removed Points

These points from the reviewers were considered and removed with justification:

1. **"Overstated framing of the 'flaw' in prior work"** — The paper clearly states that the flaw is in the *original analysis* (the bounds were not tight for quadratics), not that the original paper made an error. The paper is specific: "its known theoretical guarantees on quadratic optimization tasks are no better than those offered by GD." This is a correct observation about bound looseness. **Reason: Misunderstands the paper; the framing is accurate.**

2. **"General theoretical improvement not explicitly quantified"** — The paper provides Theorem 2 with explicit optimal \(\gamma\) range and the bound \(T_\mu(\gamma) \le T_\text{GD}\). The diagonal example gives a concrete ratio. The paper explicitly acknowledges that the general case is more complex and scopes the presentation accordingly ("to maintain clarity in the presentation"). **Reason: The paper already addresses this; requesting a general closed-form ratio for arbitrary eigenvalue structures is outside the scope and standard practice.**

3. **"No GD baseline in experiments — GD is absent"** — As analyzed above, GD's time complexity is closely approximated by the \(\gamma \to 0\) limit in the FedExProx curves, and the paper explicitly connects these: "when \(\gamma \to 0\), ... and FedExProx effectively reduces to GD." The U-shaped curves show that for large \(\mu\), optimal \(\gamma > 0\) outperforms \(\gamma \to 0\). The comparison is implicit in the data. **Reason: Partially factually incorrect; GD is present implicitly via the \(\gamma \to 0\) limit. Weakened to a minor point about missing explicit baseline.**

4. **Section-level notes about "the proof is deferred to the appendix (not available)"** — The parser strips appendix content from all papers; these sections exist in the original submission. **Reason: Per rules, remove criticisms about missing appendix.**

5. **"The time model ignores synchronization and straggler effects"** — The model explicitly accounts for the slowest client via \(\max_i\) and the paper acknowledges this as a first-order approximation. Demanding more complex models is scope creep. **Reason: Scope creep; the model is standard and acknowledged.**

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add an explicit GD baseline** as a horizontal line (or at \(\gamma=0\) as a marked point) in Figures 1, 2, and 4. This would make the central empirical claim directly verifiable at a glance.

2. **Report the multiplicative factor** between theoretical and empirical time complexities in Figure 5, and discuss whether it is approximately constant across \(\gamma\) or functionally dependent.

3. **Add error bars or confidence intervals** to the partial participation experiments (Figure 2) to account for randomness in client sampling.

4. **Include at least one experiment** comparing the adaptive extrapolation strategies (GraDS and StoPS) against the constant-optimal \(\alpha\) to demonstrate that the adaptive methods achieve comparable performance in practice.

---

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
Now I have enough information to produce a thorough, verified review. Let me consolidate everything.

---

## Summary

This paper introduces the **n-sided PL condition**, extending the Polyak-Łojasiewicz (gradient dominance) condition to multi-player potential games with n blocks of variables. It studies convergence of block coordinate descent (BCD) and gradient descent (GD) under this condition, showing that BCD converges to the Nash equilibrium set but without a guaranteed rate. To obtain linear rates, the paper introduces an additional alignment assumption (Assumption 3.5) relating the gradients of \(f\) and the average best-response function \(G_f\). It then proposes two adaptive algorithms—IA-RBCD (using exact best responses) and A-RBCD (using approximated best responses via an inner GD loop)—that provably converge linearly even when the alignment assumption fails, provided the "bad case" occurs only finitely often. Experiments on a strict-saddle example, linear residual networks, and n-player LQR games support the claims.

## Strengths

1. **Novel extension of PL condition to multi-block settings.** The n-sided PL condition (Definition 2.6, referred to in the paper) is a natural generalization of two-sided PL to problems with an arbitrary number of blocks. The paper demonstrates that this condition holds for several practically relevant nonconvex problems (linear residual networks, n-player LQR), providing a unified theoretical framework. This is a concrete conceptual contribution.

2. **Adaptive algorithms that handle strict saddle points.** IA-RBCD (Algorithm 2) and A-RBCD (Algorithm 3) are cleverly designed to detect and switch between favorable and unfavorable gradient configurations, guaranteeing convergence even when standard BCD would diverge at strict saddles. The strict-saddle experiment (Figure 3) directly validates this capability—BCD diverges while A-RBCD converges linearly across 100 random initializations. This addresses a genuine limitation of first-order methods in multi-agent settings.

3. **Empirical evidence on two realistic problems.** Experiments on linear residual networks (100 trials, two configurations) and n-player LQR games (50 trials) demonstrate linear convergence of A-RBCD, and the measured quantity \(\rho = \langle\nabla f,\nabla G_f\rangle/\|\nabla f\|^2\) in the LQR experiments shows that the "bad" Case 3 of IA-RBCD rarely occurs in practice, supporting the practical viability of the approach.

4. **Diagnostic counterexample (f₁ vs f₂).** The paper provides an explicit pair of 2-sided PL functions (Figure 2) showing that BCD converges linearly for one and sublinearly for the other, convincingly motivating why additional structure beyond n-sided PL is needed to characterize convergence rates.

## Weaknesses

### Fatal

None.

### Major

1. **The differentiability of \(G_f\) (Lemma 3.4) is asserted without sufficient justification in the main text.** The function \(G_f(x) = \frac1n \sum_i f(x_i^*(x), x_{-i})\) relies on \(x_i^*(x)\), defined as the closest minimizer of \(f(\cdot, x_{-i})\) to the current \(x_i\). Under the n-sided PL condition alone, the set of minimizers of the block subproblem may not be convex, so the closest-point projection may not be unique or well-defined as a function. Even if a unique closest point exists for each \(x\), the mapping \(x \mapsto x_i^*(x)\) need not be differentiable, and Lemma 3.4 asserts that \(\nabla G_f\) exists and is \(L'\)-Lipschitz with \(L' = L + L^2/\mu\)—a non-trivial claim. The paper references "4 for a proof" (presumably the appendix), but the main text gives no intuition or justification. Because all subsequent convergence results (Theorems 3.6, 3.7, 3.10, 3.11) depend on the smoothness of \(G_f\), this is a **central gap**: if Lemma 3.4 cannot be established from the stated assumptions, the theoretical backbone of the paper collapses. The authors must provide a rigorous proof or state the additional regularity conditions (e.g., uniqueness of block minimizers, invertibility of partial Hessians) needed.

2. **Assumption 3.5 lacks connection to verifiable problem structure.** The alignment condition \(\langle\nabla G_f, \nabla f\rangle \le \kappa \|\nabla f\|^2\) with \(\kappa<1\) is what enables the clean linear rates for BCD and GD (Theorems 3.6, 3.7). The paper provides one toy example (\(f_0\)) where it holds away from a saddle region, and Lemma 3.8 gives \(C_f > 1\) such that \(\|\nabla G_f\| \le C_f\|\nabla f\|\)—but this does not imply \(\kappa<1\). The paper claims the linear residual network satisfies this, but no proof or characterization is given. Since the core linear-rate results for basic BCD/GD rest entirely on an assumption that is not derived from the n-sided PL condition and is not characterized for any realistic problem class, the contribution of those results is substantially weakened. The adaptive algorithms (IA-RBCD, A-RBCD) are designed to circumvent this, but their linear-rate guarantees still depend on other constants (\(\gamma, C\)) that are not linked to the problem structure.

3. **The total computational cost of A-RBCD is not compared with standard methods.** Theorem 3.11 gives the inner-loop iteration count \(T' \ge \log(\frac{169 n L^2}{\mu^2 \gamma^2 \alpha^6}) / \log(\frac{1}{1-\mu\beta})\), which depends on \(\alpha\) (itself constrained to be very small in some cases). The experiments in Section 4 plot error against outer iterations, not wall-clock time or total gradient evaluations. Since A-RBCD pays the cost of an inner GD loop at every outer iteration, a comparison on total gradient calls vs. standard BCD or GD is essential to assess whether the theoretical advantage translates to practical efficiency. The paper includes RBCD in some plots (Figures 4, 5) but does not report gradient costs or runtimes, making it hard to judge competitiveness.

### Minor

1. **Boundedness of iterates is assumed without discussion.** Theorems 3.1 and 3.2 assume that the BCD iterates \(\{x^t\}\) remain bounded, but no sufficient conditions (e.g., coercivity of \(f\), bounded level sets) are provided. This is important because the n-sided PL condition alone does not guarantee bounded iterates even for simple quadratic functions.

2. **The convergence analysis for the "bad" Case 3 is incomplete.** The paper shows that in Case 3, \(f - G_f\) is non-increasing, and if it satisfies the \((\theta,\nu)\)-PL condition, the convergence rate is sublinear (\(O(1/k^{\theta/(2-\theta)})\)). However, the paper does not prove that Case 3 occurs only finitely many times under any general condition—it merely speculates that it does so for functions like \(f_0\). Without this guarantee, the overall convergence of IA-RBCD / A-RBCD could be sublinear even if each individual occurrence of Case 3 only lasts finitely long but occurs infinitely often.

3. **The strict-saddle experiment lacks theoretical explanation.** The paper shows empirically (Figure 3) that BCD diverges and A-RBCD converges for the function \(f(x,y) = (x-1)^2 + 4(x+0.1\cos x)y + (y+0.1\sin y)^2\). However, no theoretical analysis is given for why BCD diverges (e.g., does the n-sided PL condition hold? Is the function not coercive? Do the BCD iterates diverge to infinity?). Since the paper's main claims about the strict-saddle setting are a highlight, this omission weakens the narrative.

### Trivial

- The extracted text contains garbled passages (e.g., line 49: "dbey noted", "n iTfhore md issatamnpclei nbge"). These are parser artifacts, not author errors, so they should not be penalized.

## Nice-to-Haves

- A complexity analysis in terms of total gradient evaluations (not just outer iterations) for A-RBCD, comparing with standard BCD and GD on the same problems.
- A sufficient condition (e.g., coercivity or bounded level sets) that guarantees the bounded-iterates assumption in Theorems 3.1 and 3.2.
- A derivation or citation showing that the linear residual network and n-player LQR objectives satisfy Assumption 3.5 (or at least the stronger condition \(\|\nabla G_f\| \le \kappa \|\nabla f\|\) for some \(\kappa<1\)).

## Removed Points

- **Criticism that \(f_1\) may not satisfy smoothness assumptions**: The function \(f_1(x,y) = (x+y)^2 + e^{-1/(x-y)^2}\) is smooth (\(C^\infty\)) everywhere, including at \((0,0)\). The exponential term is the classic smooth non-analytic function. The criticism is factually wrong.
- **"No complexity analysis" for any algorithm**: The paper provides explicit bounds on \(T'\) in Theorem 3.11 and convergence rates in Theorems 3.6, 3.7, 3.10, 3.11. The critic overstated this; the valid narrower point (no total-gradient-cost analysis) is preserved in Major #3.
- **Typographical and formatting nitpicks**: These are parser artifacts, not author errors.
- **Missing related works / missing appendix definitions**: The missing Section 2 content (definition of n-sided PL, assumptions) and missing appendix proofs are parser artifacts—the original submission contains them.
- **"Code is mentioned but not reviewed"**: This is a standard reproducibility statement and not a valid weakness.
- **Speculation about the strict-saddle function not satisfying n-sided PL**: The paper states the n-sided PL holds (referenced to appendix), and the critic speculates without evidence.
- **"The paper does not give an explicit example where these conditions are satisfied" (for A-RBCD)**: The paper provides the \(f_0\) example and the LQR experiment showing \(\rho\) stays away from 1. The criticism is not necessary for acceptance.

## Novel Insights

The two reviewers largely agree on the paper's strengths (the n-sided PL extension is novel and the adaptive algorithms are principled) and on the primary weakness (the differentiability of \(G_f\) is insufficiently justified). The harsh critic's concern about Lemma 3.4 being a structural flaw is the most significant issue, but it is not necessarily fatal—a proper proof in the appendix could resolve it. The strength finder correctly identifies that the experiments on LQR include a measurement of \(\rho\) that directly validates Assumption 3.5 empirically, which partially mitigates the concern about that assumption being unverifiable. Neither reviewer noticed that the paper uses "closest minimizer" in the definition of \(x_i^*(x)\), which may introduce non-differentiability even if the set of minimizers itself is well-behaved—this is a sharper formulation of the differentiability concern than "the set might not be convex."

## Suggestions

1. **Clarify the proof of Lemma 3.4** (differentiability of \(G_f\)). Either provide a rigorous proof in the main paper (not just an appendix reference) using the n-sided PL and smoothness assumptions, or state explicitly what additional regularity is required (e.g., that each block subproblem \(f(\cdot, x_{-i})\) has a unique minimizer that varies smoothly with \(x_{-i}\)). If the proof is already in the appendix and correct, this is a presentation issue; otherwise it is a fatal gap.

2. **Characterize when Assumption 3.5 holds** beyond toy examples. Relate it to a spectral bound on \(\nabla^2 f\) or provide sufficient conditions in terms of the original problem data.

3. **Report total gradient complexity** (or runtime) for the experiments, not just outer iterations. This would address the concern about the practical cost of the inner GD loop in A-RBCD.

4. **Discuss conditions that guarantee bounded iterates** in Theorems 3.1 and 3.2, and provide a theoretical explanation for why BCD diverges in the strict-saddle example.

## Score and Decision

**Assessment by axes**:

- **Originality**: High. The n-sided PL condition is a novel extension, and the adaptive algorithms are well-motivated.
- **Importance of research question**: High. Understanding convergence of first-order methods to Nash equilibria in nonconvex games is practically relevant.
- **Claims well-supported**: Moderately. The central claim about differentiability of \(G_f\) is insufficiently justified in the main text. The experimental claims are supported but the comparisons are limited.
- **Soundness of experiments**: Adequate but could be stronger. Missing total gradient cost comparisons.
- **Clarity of writing**: The extracted text shows signs of garbled sections (parser artifacts), but the main ideas are communicated clearly.
- **Value to community**: Potentially high, if the theoretical gaps can be resolved.

The paper has real contributions but the differentiability of \(G_f\) is a non-trivial claim that underpins almost all subsequent results. It is not a fatal error since the proof may exist in the appendix, but the lack of justification in the main body is a significant omission. The paper would benefit from major revision to clarify this point and strengthen the experimental comparison. In its current form, it is a borderline paper that leans towards rejection due to the centrality of the gap, but with strong potential.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
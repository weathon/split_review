Now I have a thorough understanding of the paper and have verified each reviewer claim against the actual text. Let me produce the consolidated review.

---

## Summary

This paper studies how running gradient descent on a quadratic reparametrization ($x = u \circ u$, i.e., diagonal linear networks) of the squared-residual loss $\frac12\|A(u\circ u)-b\|_2^2$ yields solutions to linear programs with positive cost vectors. The authors prove two main theoretical results: (1) **global linear convergence** of discrete-time GD to a feasible point (Theorem 3.2), and (2) a characterization of the limit point as the solution of an entropy-regularized LP perturbed by an $\eta$-proportional error term (Theorem 4.2). The gradient-flow limit (Theorem 2.1) gives a clean, explicit regularized objective. Connections to mirror descent and the Sinkhorn algorithm are discussed, and small-scale experiments validate the theory.

## Strengths

- **First global linear convergence guarantee for discrete-time reparameterized GD on this class of problems.** Theorem 3.2 proves linear convergence of GD on the nonconvex objective $f(u) = \frac12\|A(u\circ u)-b\|_2^2$ to the global minimum (zero loss) under only mild assumptions (full-rank $A$, strict feasibility). This is a nontrivial result that goes well beyond what general nonconvex GD theory provides, and the proof is carefully constructed (Lojasiewicz inequality, lower bound on iterates, two-stage convergence argument).

- **Gradient-flow characterization (Theorem 2.1) is clean and predictive.** It shows that the continuous-time limit solves an entropy-regularized LP whose regularization strength is controlled by initialization. The formula $\alpha_i = \exp(-c_i/(2\lambda))$ gives an explicit, parameter-dependent objective — this is a genuine characterization that connects initialization to implicit regularization.

- **Unified conceptual framework.** Sections 2.2--2.3 provide explicit mappings between reparameterized GD, mirror descent with entropy, and the Sinkhorn algorithm, clarifying both similarities and differences (e.g., the equivalence as step size goes to zero, the divergence under finite step sizes). These connections help position the work in the broader literature.

- **Rigorous handling of constraints and step sizes.** Lemma 2.1 gives a practical, computable step-size rule guaranteeing positivity of iterates and per-iteration decrease. The boundedness of iterates (Lemma 3.1) and the existence of a uniform step-size bound (Corollary 1) are carefully established.

## Weaknesses

### Major

- **The discrete-time limit characterization (Theorem 4.2) is existential rather than fully predictive.** The theorem states that there exists a vector $w\ge 0$ with $\|w\|_1\le C$ (where $C$ depends only on problem data) such that $x^\infty$ solves a perturbed entropy-regularized LP. However, in the proof, $w$ is constructed as $w = (A^\top\nu - \log(x^\infty/x^0))/(\eta\log(1/\underline\alpha))$, which is expressed in terms of the limit point $x^\infty$ itself. Unlike the gradient-flow case (Theorem 2.1), one cannot look at the problem parameters and initialization alone and write down the objective that the algorithm minimizes — the characterization is a *posteriori* rather than *a priori*. The paper is honest about this (calling it an "error term"), but the gap between the continuous and discrete characterizations is significant: the discrete result asserts boundedness of the perturbation rather than giving an explicit formula for it. This weakens the claim that the discrete dynamics yield a *controlled* entropy-regularized solution, because the $\|w\|_1\le C$ bound depends on constants ($K$, $c$, $\tau$ from the Lojasiewicz lemma) that are themselves derived from compactness arguments and may be impractically large.

### Minor

- **The linear convergence rate depends on $\sigma$, a constant whose practical magnitude is not discussed.** Theorem 3.2 gives the rate $\rho = 2\mu\eta\sigma^2$, where $\sigma$ is a lower bound on the iterates ($u^k\ge \sigma\mathbf{1}_n$). Lemma 4.5 provides an explicit bound for $\sigma$, but this bound involves $C_2$, which in turn depends on $C_1$ (a combination of tail sums of residuals and other constants). While $C_1$ is shown to be bounded by problem data (via Corollary \ref{cor: sum-bound}), the resulting bound on $\sigma$ could be exponentially small in the problem dimensions or in $1/\eta$. The paper offers no estimate, example, or discussion of what values $\sigma$ might take in practice. The convergence result is qualitatively interesting but quantitatively opaque.

- **Experimental scope is narrow for the paper's claimed applicability.** The experiments test only the special case $c = \mathbf{1}_n$ (minimizing $\sum x_i$) on synthetic random data. The paper's abstract and introduction claim applicability to "basis pursuit and optimal transport problems," but no optimal transport experiments are conducted (despite Section 2.3 setting up the connection), no comparisons to standard LP solvers are provided, and the big-M reduction for general cost vectors is not demonstrated. Given that the paper is primarily theoretical, these omissions do not invalidate the core contributions, but they leave a gap between the claimed scope and what is actually verified.

### Trivial

- **Minor norm mismatch in Corollary 1.** The definition of $\bar\eta$ (proof of Corollary 1, line 660) uses $\|A^\top(A(u\circ u)-b)\|_2$ (2-norm), while Lemma 2.1's step-size condition uses $\|A^\top r^k\|_\infty$ (infinity-norm). Since $\|\cdot\|_\infty\le\|\cdot\|_2$, the condition is stricter than needed but still valid. This is a minor technical sloppiness.

## Nice-to-Haves

- A practical estimate or experiment showing typical values of $\sigma$ (and hence the linear rate constant) would substantially strengthen the convergence analysis.
- An explicit error bound of the form $c^\top x^\infty + \lambda H(x^\infty) \le \min_{Ax=b,x\ge0}(c^\top x + \lambda H(x)) + O(\eta)$ (where the $O(\eta)$ term depends only on problem data, not on $x^\infty$) would make the discrete-time characterization as predictive as the gradient-flow case.
- A small optimal transport experiment (even on a toy example) comparing reparameterized GD with Sinkhorn would verify the claims in Section 2.3.
- A brief discussion of how to choose the big-M bound in practice (Remark \ref{remark: general-LP-reduce}) would make the reduction for general LPs more actionable.

## Removed Points

- The critic's claim that Theorem 4's characterization is "tautological" is overstated — the theorem does show that $x^\infty$ solves a problem whose objective deviates from the entropy-regularized one by a bounded linear term. The criticism is kept in weakened form (Major weakness, not fatal).
- The critic's claim that the $\sigma$ bound "depends on the limit point itself" is factually inaccurate: $C_1$ and $C_2$ are bounded by problem data and initialization through Corollary \ref{cor: sum-bound} and Lemma 3.1, not by the limit point. The underlying concern about $\sigma$ being potentially small is valid and retained as a Minor weakness.
- The critic's "Other Observations" about Section 5 being discussion material and Lemma 4.1's combinatorial bound are not genuine weaknesses — Section 5 is useful context and the polyhedral argument is standard in LP analysis.
- The critic's suggestion to "replace Theorem 4 with an explicit error bound" is aspirational rather than a flaw in the current result. The paper's contribution is what it proves, not what it might have proven.

## Novel Insights

The key insight that emerges from the reviews, beyond the paper's own contributions, is that the discrete-time analysis faces an inherent tension: the log-bound inequality (Lemma 10.3) introduces a second-order correction term $\tilde w$ that, under the linear convergence guarantee, can be bounded in $\ell_1$-norm by problem data. This makes the discrete characterization nontrivially different from the gradient-flow case — the error term is provably bounded, but not given by a closed-form function of the problem parameters. This structural limitation suggests that a fully predictive discrete-time characterization (analogous to the gradient-flow case) may require fundamentally different proof techniques or additional assumptions.

## Suggestions

1. **Scale back the claims about the discrete limit to match what is actually proven.** The paper should be explicit that Theorem 4.2 gives an *existential* bound on the perturbation (bounded norm), not an explicit formula. The abstract's phrasing ("leads to solutions for entropically regularized linear programming problems") is technically correct but could be read as implying a cleaner characterization than Theorem 4.2 delivers.

2. **Discuss the practical magnitude of $\sigma$.** A simple experiment reporting how $\sigma$ behaves under different problem sizes, initializations, and step sizes would help readers understand whether the linear rate constant is practically meaningful.

3. **Add at least one small optimal transport experiment.** Since Section 2.3 discusses the connection to Sinkhorn at length, even a 3×3 example verifying the qualitative behavior would strengthen the narrative.

4. **Fix the norm mismatch in Corollary 1** for clarity (even though correctness is unaffected).

## Score and Decision

This paper makes a genuine theoretical contribution: the global linear convergence proof for discrete-time reparameterized GD on LPs is novel and nontrivial, and the gradient-flow characterization is clean. The main weaknesses — the existential nature of the discrete limit characterization, the unquantified rate constant, and the narrow experiments — are real but do not invalidate the core results. The paper should be accepted with encouragement to address the discrete limit gap in future work or via an explicit error-bound corollary.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
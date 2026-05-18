I've now thoroughly read the paper and verified the reviewer claims against the actual content. Let me synthesize the final review.

---

## Summary

This paper introduces the relative-translation invariant Wasserstein distance ($RW_p$), a family of metrics on the quotient space $\mathcal{P}_p(\mathbb{R}^n)/\sim$ that are invariant to relative translations between distributions. For the quadratic case $p=2$, the authors prove three key properties: decomposability of the ROT optimization (Theorem 4), translation-invariance of the coupling solution (Corollary 1), and a Pythagorean relationship $W_2^2 = RW_2^2 + \|\bar\mu - \bar\nu\|_2^2$ (Corollary 2). Leveraging these properties, they propose the $RW_2$ Sinkhorn algorithm, which pre-subtracts means before running Sinkhorn iterations, improving numerical stability and reducing runtime when translations are large. Experiments on synthetic data, MNIST digit recognition, and a large-scale thunderstorm pattern dataset (205,848 radar images) validate the approach.

## Strengths

- **Rigorous theoretical foundation for translation-invariant optimal transport.** The paper formally defines $RW_p$ on the quotient set, proves it is a real metric (Theorem 3), and for the quadratic case establishes the decomposition theorem, translation-invariance of couplings, and the Pythagorean relationship. These results cleanly characterize the geometry of the proposed distance and directly motivate the algorithm.

- **Practical algorithm with clear computational benefits.** The $RW_2$ Sinkhorn algorithm (Algorithm 1) exploits the decomposition to pre-center the cost matrix, which (a) makes the kernel entries larger and more numerically stable, and (b) reduces $\|C\|_\infty$, which the paper links (via the Altschuler et al. bound) to reduced iteration count. The numerical experiments in Section 5.1 empirically confirm significant runtime and error improvements as translation grows.

- **Convincing empirical validation of translation robustness.** The MNIST digit recognition experiment (Section 5.2) shows that $RW_2$ maintains high classification accuracy under large random translations where $L_1, L_2, W_1, W_2$ degrade sharply. This directly validates the paper's central claim that $RW_2$ is robust to distribution shift caused by translation.

- **Scalability demonstrated on a real-world task.** The thunderstorm experiment uses over 200,000 real radar images spanning 8 years, showing that $RW_2$ can be applied at scale and produces qualitatively more shape-focused retrievals than $W_2$.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Experimental setups for baseline distances are underspecified for reproducibility.** In the MNIST experiment (Section 5.2), $\lambda$ and $\epsilon$ are given only for $RW_2$ ("We set the $\lambda = 0.1$ and $\epsilon = 0.1$ for the $RW_2$ Sinkhorn algorithm," line 263), but not for the $W_1$ and $W_2$ baselines. Similarly, the numerical validation (Section 5.1) reports "$W_2$ error" against "true $W_2$" without specifying how the true $W_2$ was obtained (presumably via linear programming). These omissions make the comparisons difficult to reproduce faithfully.

- **The thunderstorm pattern detection experiment is entirely qualitative.** Section 5.3 presents side-by-side images and argues that $RW_2$ retrievals are more shape-focused, but provides no quantitative metric (retrieval precision, user study, or any labeled evaluation). The paper acknowledges this is a "demonstration," which tempers the severity, but the abstract claims "effectiveness of using $RW_2$ under distribution shift" — this claim would be much stronger with quantitative evidence in at least one of the two real-world tasks.

- **Error bars are not shown in the experimental plots despite reporting standard deviations.** The text states that mean and standard deviation were computed (lines 241, 263), but the figures (Figure 3 and Figure 4) do not display error bars, shaded regions, or standard deviation values. This makes it difficult to assess the statistical significance of the reported advantages, especially where gains are moderate (e.g., at small-to-medium translations).

- **Numerical stability analysis is heuristic rather than rigorous.** The analysis in Section 4.3 uses $g(K)$ (product of kernel entries) as a proxy for numerical stability and shows it is maximized by aligning means. While the intuition is sound and the empirical results support the claim, the paper does not connect $g(K)$ to the condition number of the matrix scaling problem, to any known bound on Sinkhorn convergence, or to floating-point error propagation. Given that enhanced numerical stability is presented as a contribution (line 23d, "enhanced numerical stability"), the analysis would benefit from tighter theoretical grounding.

- **The bias-variance perspective is mentioned as a contribution but remains only briefly remarked upon.** The Pythagorean relationship (Corollary 2) is used to note that $W_2^2$ decomposes into a "bias" term (mean difference) and a "variance" term (shape difference via $RW_2^2$). However, this perspective is not developed beyond a single paragraph (lines 171). It appears in the contribution list (line 23c) but receives no experimental or analytical development. This is a minor overclaim.

### Trivial

- **The decomposition theorem's derivation is not fully spelled out.** Theorem 4 states $V(s) = \|s\|^2 + 2s \cdot (\bar\mu - \bar\nu)$, which implicitly relies on the fact that $\sum_{ij} P_{ij}(x_i - y_j) = \bar\mu - \bar\nu$ is independent of $P$ because row/column sums are fixed. The result is correct, and the reasoning is recoverable, but a reader unfamiliar with the detail may miss why the minimization separates so cleanly. A short algebraic expansion would improve clarity.

- **The paper states that rotation cannot be incorporated because it would violate metric properties and convexity (line 130), but does not explain why.** The reasoning (rotation is not a vector space, so the Euclidean-cost expansion would not hold) would be helpful to include.

- **The paper defines $RW_p$ for general $p$ but only experiments with $p=2$.** A brief note on whether and how the algorithm extends to $p \neq 2$ would be helpful.

## Nice-to-Haves

- Connect the stability analysis more tightly to known bounds on Sinkhorn convergence (e.g., the Altschuler et al. bound already cited in the complexity analysis). This would turn the heuristic $g(K)$ argument into a concrete bound on iteration count.
- Explicitly state that the entropy-regularized coupling obtained from the shifted cost matrix is identical to the one from the original matrix (since the shift adds a separable term), clarifying why Algorithm 1 is not a heuristic but an exact computation of the ROT solution.
- Add a quantitative evaluation for the thunderstorm retrieval task, such as retrieval precision against a small labeled set.

## Removed Points

None of the reviewer's criticisms were factually wrong or required removal under the hard rules. All have been retained (and appropriately downgraded where needed) in the sections above.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Provide $\lambda$ and $\epsilon$ values for *all* baseline methods in the MNIST experiment, and state how the true $W_2$ was computed in the numerical validation.
- Add error bars, shaded regions, or a supplementary table showing standard deviations for Figures 3 and 4.
- Strengthen the numerical stability analysis by citing the Altschuler et al. bound on Sinkhorn convergence as a function of $\|C\|_\infty$ and showing that pre-centering the cost matrix provably reduces this bound.
- Add a brief quantitative evaluation for at least one of the two real-world experiments, or clarify in the abstract/contributions that the thunderstorm demonstration is qualitative.

## Score and Decision

**Overall assessment:** The paper makes a clean, well-motivated contribution: a new family of translation-invariant Wasserstein distances with a sound theoretical foundation and an efficient algorithm. The theoretical results (decomposition, invariance, Pythagorean relationship) are correct and elegantly characterize the geometry. The algorithm is practical and its benefits are empirically demonstrated. The weaknesses are bounded — underspecified baseline details, missing error bars, a heuristic stability analysis, and a qualitative-only weather experiment — none of which undermine the core contribution, though some do reduce reproducibility and confidence in the statistical significance of the results. With minor revisions addressing these gaps, the paper would be significantly strengthened.

**Originality:** High. The $RW_p$ family and the decomposition theorem for the quadratic case are novel.
**Importance:** High. Translation invariance is a practically important property for applications with distribution shift.
**Claims supported:** Mostly. The main claims are supported, but the bias-variance framing is overstated relative to its development.
**Soundness:** Good. The theory is sound; the experiments support the claims with the caveats noted above.
**Clarity:** Good, with minor presentation gaps.
**Value:** High. The distance and algorithm are likely to be adopted in applications dealing with translated distributions.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
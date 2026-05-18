Now I have thoroughly verified all claims against the paper. Let me write the consolidated review.

## Summary

This paper proves that an MLP with batch normalization (BN) and random orthogonal weight matrices at initialization avoids both rank collapse (exponential decay of the isometry gap with depth) and gradient explosion (log-gradient-norm bounded independently of depth) for linearly independent inputs with n=d. The theoretical results are non-asymptotic (finite-width), using Weingarten calculus, and stand in direct contrast to the established exponential gradient explosion for Gaussian weights (Yang, 2019, Theorem 3.9). Experiments confirm the theory and extend it to training dynamics and, via a heuristic activation shaping scheme, to certain nonlinear activations. The paper also documents an implicit orthogonality bias during SGD training.

## Strengths

- **First non-asymptotic proof of depth-independent gradient bounds for BN networks.** Theorem 2 provides a bound on the expected log-gradient-norm that does not depend on depth — only on width and input isometry. This contrasts qualitatively with the exponential-in-depth explosion proven for Gaussian weights (Yang, 2019, Theorem 3.9), as empirically validated in Figure 2.

- **Exponential convergence of representations to perfect orthogonality.** Theorem 1 proves the isometry gap decays at rate \(\mathcal{O}(e^{-\ell/k})\) with \(k = Cd^2(1 + d\cdot\IG(X_0))\), which is stronger than the prior non-asymptotic bound of Daneshmand et al. (2021) that only guarantees proximity within an \(\mathcal{O}(\text{width}^{-1/2})\) ball. Figure 1 confirms exponential decay empirically.

- **Depth-independent training convergence validated experimentally.** Figure 3(c) shows that SGD training accuracy curves for depths 100, 200, 500, and 1000 are nearly identical on CIFAR-10, demonstrating that the theoretical bounds translate to stable, depth-agnostic optimization at practical finite widths.

- **Empirical discovery of an implicit orthogonality bias during training.** Figure 6 shows that weight matrices in a 1000-layer network remain nearly orthogonal even after many SGD steps despite non-negligible gradients. This suggests the dynamics naturally preserve orthogonality, pointing to an interesting direction for future work.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The gradient bound is loose for realistic widths.** Theorem 2 gives \(\mathbb{E}[\log \|\nabla\|] \leq C d^5 (\phi(X_0)^3 + 1)\). For \(d=1000\), the right-hand side is on the order of \(10^{15} \times\) constants, meaning the bound does not rule out astronomically large gradients in principle — it only proves depth-independence, not practical boundedness. The experiments (Figure 2) confirm that gradients stay small in practice, partially mitigating this concern. The paper should qualify this bound as showing *depth-independence* rather than tightness, and ideally provide a sharper analysis reducing the \(d^5\) factor or at least tabulate the numerical magnitude for typical widths.

2. **The theory covers initialization only, not the training trajectory.** All theoretical results are expectations over random orthogonal weight matrices at initialization. The paper's framing ("Towards Training Without Depth Limits") and the experimental section demonstrate that training *works*, but there is no theoretical guarantee about gradient behavior after weights are updated by SGD. The gap is acknowledged in the discussion of "implicit orthogonality bias" (Section 7) as future work, but the abstract and introduction could more clearly delimit the scope of the formal results versus the empirical observations.

3. **The \(n = d\) assumption is restrictive and insufficiently discussed.** The analysis requires the batch size to equal the width. The paper states this requirement (line 71) but does not discuss why it is needed, whether it can be relaxed to \(n < d\) (e.g., via subspace projection or covariance analysis), or how limiting it is for practical architectures. The experiments use \(d=100, n=100\), which conforms to the assumption. This restriction deserves a more prominent caveat and ideally a discussion of potential extensions.

4. **The simplified BN operator differs from standard BN.** Equation (3) omits mean reduction and the \(1/n\) scaling factor. The paper acknowledges these are "minor differences" and points to Figure 1(c) for empirical validation. However, the theoretical analysis relies on the eigenvalue structure induced by the simplified operator (eigenvalues of \(\bn(X)\bn(X)^\top\) lying in \((0,1]\)). A formal justification that mean subtraction does not affect the isometry gap decay or gradient bound would strengthen the contribution beyond a single empirical figure.

5. **The activation shaping scheme for nonlinear activations is heuristic and lacks theoretical support.** Section 5 describes tuning per-layer pre-activation gains \(\alpha_\ell\) with the criterion that they "ensure faster decay than a harmonic series." No theorem connects the gain schedule to gradient bounds, and no concrete algorithm or formula for \(\alpha_\ell\) is provided in the main text. The paper references an appendix for details (which was stripped by the parser). As presented in the main text, this reads as a promising but incomplete direction whose presentation alongside the formal contributions risks overclaiming.

### Trivial

None.

## Nice-to-Haves

- A sharper gradient bound (e.g., reducing \(d^5\) to \(d\) or \(d^2\)), or an explicit numerical evaluation of the bound's magnitude for typical widths and inputs.
- A discussion of whether the \(n = d\) constraint can be relaxed, e.g., via zero-padding, subspace projection, or covariance analysis.
- A concrete algorithm or explicit gain schedule for activation shaping, even if only empirically validated.
- A small ablation study isolating the effect of the two BN simplifications (mean removal, \(1/n\) factor) on gradient behavior.
- A brief comparison with other practical methods for stabilizing deep BN networks (e.g., gradient clipping, learning rate tuning).

## Removed Points

- **"The gradient bound is nearly vacuous"** — kept as Minor but downgraded: the bound is loose but its *qualitative* contribution (depth-independence vs. exponential explosion for Gaussian weights) is genuine and empirically validated.
- **"Activation shaping is underspecified"** — the paper references App.~\ref{sec:shaping} for details, which was stripped by the parser; the claim cannot be fully verified from the main text alone.
- **"No comparison with gradient clipping or learning rate reduction"** — this is scope creep; the paper's contribution is a theoretical construction, not an empirical comparison of stabilization methods.
- **"No ablation on BN simplifications"** — this would strengthen the paper but is not a weakness; the paper provides experimental evidence that standard BN yields similar results.
- **"Computational cost of Haar sampling not mentioned"** — a technical footnote, not a weakness affecting the paper's claims.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. In the abstract and introduction, more precisely delimit what is proved (initialization, linear activations, simplified BN, \(n=d\)) versus what is empirically observed (training dynamics, nonlinear activations).
2. Discuss why \(n = d\) is required and whether the analysis extends to \(n < d\), even via an informal argument.
3. Provide a concrete example gain schedule for activation shaping in the main text (e.g., \(\alpha_\ell \propto 1/\ell\) or similar) to give readers a usable recipe.
4. Explicitly note that the \(d^5\) bound is a proof of *depth-independence*, not a tight numerical guarantee, and state that experiments confirm practical boundedness.

## Score and Decision

The paper makes a genuine and novel theoretical contribution — proving depth-independent gradient bounds for a BN network with orthogonal weights, using Weingarten calculus for non-asymptotic analysis. This directly challenges the prevailing view that gradients *must* explode in BN networks (Yang, 2019). The experiments support the theory and extend it to training. The main weaknesses are: (1) the gradient bound is loose (\(d^5\) factor), though the key insight of depth-independence is preserved; (2) the theory covers initialization only, though experiments confirm training works; (3) the \(n = d\) and simplified-BN assumptions are restrictive, though clearly stated. None of these are fatal. The paper is well-written, the proofs are sketched sufficiently, and the contribution is significant for the theory of batch-normalized networks. I recommend acceptance.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 8, 5, 6
Now I have enough verification to write the consolidated review.

## Summary
This paper proves accelerated convergence guarantees (rate \(e^{-\sqrt{\mu}t}\) in continuous time, \((1-\sqrt{\mu\eta})^n\) in discrete time) for Nesterov-type momentum methods under a novel non-convexity condition: first-order \(\mu\)-strong convexity with respect to the *closest minimizer*. This condition permits tangential motion along a manifold of minimizers—a realistic feature of overparametrized deep learning—unlike quasar-convexity (which forces uniqueness or star-shaped sublevel sets) or PL functions (where acceleration is provably impossible per Yue et al. 2023). Results cover continuous-time heavy-ball ODE (general \(C^2\) submanifolds), deterministic discrete Nesterov, and stochastic settings with additive and multiplicative noise. A theoretical link to deep learning via Lemma 5 (full-rank Hessian on the minimizer manifold) is provided, alongside small-scale experiments.

## Strengths

- **First accelerated convergence guarantees for non-convex functions with a curved minimizer manifold (continuous time).** Theorem 1 proves the accelerated exponential rate \(e^{-\sqrt{\mu}t}\) for the heavy-ball ODE under a general \(C^2\) submanifold of minimizers. This goes cleanly beyond quasar-convexity (which forces star-shaped sublevel sets or unique minimizers) and circumvents the negative result of Yue et al. (2023) for PL functions. The continuous-time result is technically sound, well-proved via a Lyapunov argument combined with the parallel-movement inequality.

- **Comprehensive treatment across multiple optimization settings.** The paper provides convergence guarantees for the heavy-ball ODE (Theorem 1), global convergence (Theorem 2), deterministic discrete Nesterov (Theorem 4), stochastic additive noise (Theorem 5), decreasing step sizes (Theorem 6), and mixed additive-multiplicative noise via AGNES (Theorem 7). This breadth gives the theoretical contribution clear scope, and the consistent rate structure across settings shows that the core geometric intuition transfers.

- **Honest and detailed discussion of limitations.** The paper explicitly acknowledges that the discrete-time analysis requires an affine linear projection map (lines 267–268: "very restrictive geometric linearization"), that global nonlinear closest-point projections cannot exist globally (Remark \ref{remark global projections}), that the negative eigenvalue condition \(\varepsilon \leq \sqrt{\mu/\eta}\) can eliminate acceleration when curvature is too negative (Remark \ref{remark magnitude negative eigenvalues}), and that the empirical validation uses an imperfect proxy (gradient direction, lines 177–184). This honesty is a genuine strength and allows readers to assess the gap between theory and claimed application.

- **Achievement of the classical accelerated rate \((1-\sqrt{\mu/L})^n\) despite non-convexity.** Theorem 4 matches the standard convex accelerated rate, whereas gradient descent under the same assumptions would achieve only \((1-\mu/L)^n\). This demonstrates that the benign geometric structure does not inherently degrade convergence speed.

## Weaknesses

### Fatal
None.

### Major

- **Discrete-time analysis requires the minimizer set to be an affine subspace—a significant restriction relative to the motivating application.** Theorem 4 (and all subsequent discrete-time theorems) assumes \(\pi(x) = \Pi x + x^*\) where \(\Pi\) is a fixed orthogonal projection onto a subspace. This forces the manifold of minimizers to be an affine subspace, which excludes curved manifolds—including the squared-distance-from-a-circle example (Example 4) and the curved minimizer sets that arise in overparametrized deep learning (as Lemma 3 argues must happen). The continuous-time result (Theorem 1) works for general \(C^2\) submanifolds, but the discrete algorithms that practitioners actually use are analyzed only under the linear assumption. The paper acknowledges this (line 267, Remark \ref{remark global projections}), but the abstract's claim of "virtually identical guarantees" for "benignly non-convex landscapes" is substantially overstated for the discrete-time setting. The paper's main practical message thus rests on continuous-time theory, which is one step removed from the algorithms used in practice.

- **The condition on negative eigenvalues (\(\varepsilon \leq \sqrt{\mu/\eta}\)) couples acceleration to the absence of strong negative curvature.** With the natural step size \(\eta = 1/L\), this becomes \(\varepsilon \leq \sqrt{\mu L}\). Since Hessian eigenvalues of an \(L\)-smooth function can be as negative as \(-L\), this forbids strong negative curvature unless \(\mu\) is large. As the paper notes (Remark \ref{remark magnitude negative eigenvalues}), taking \(\eta < \mu/L^2\) removes the restriction but collapses the rate to \((1-\mu/L)^n\), matching gradient descent. So acceleration is guaranteed only when negative curvature is *small*, which is indeed "benign"—but the paper does not provide convincing evidence that this condition holds in realistic deep learning regimes. The empirical evidence (Figure 6) measures second derivatives near minimizers at loss values \(10^{-9}\)–\(10^{-12}\) on a minuscule network (width 35, depth 10, 100 datapoints)—far from the regime of interest during training.

### Minor

- **Empirical validation is too weak to support the claimed connection to deep learning.** The experiment uses a tiny fully-connected network (width 35, depth 10) on only 100 synthetic datapoints, with loss values driven to \(10^{-12}\). The gradient direction is used as a proxy for the direction to the closest minimizer—an acknowledged imperfection (line 184). The measure of strong convexity w.r.t. the minimizer (Equation after line 181) is valid *only if the line passes through the minimizer*, which is not guaranteed. The paper does not test on standard benchmarks (e.g., a small ResNet on CIFAR-10) at realistic loss levels. This does not invalidate the theory, but it weakens the claim that the assumptions are "well justified" in deep learning as stated in the abstract.

- **Lemma 1 ("parallel movement") is a standard geometric fact, not "non-trivial" as claimed.** For a \(C^2\) submanifold, the derivative of the closest-point projection at a point on the manifold is the orthogonal projection onto the tangent space, yielding \(\langle \dot{x}, \dot{z} \rangle = \langle \dot{x}, D\pi(x)\dot{x} \rangle = \|P\dot{x}\|^2 \geq 0\) where \(P\) is an orthogonal projection. While the lemma is correct and useful in the proof, the paper's characterization of it as "non-trivial" overstates its novelty. This is a minor point about framing.

### Trivial

- Figure 6 shows multiple runs but does not report how many training runs failed or provide error bars. The text mentions that "training failed" in some cases but does not quantify this.
- The notation is not always consistent (e.g., \(x_n'\) and \(x'_n\) are used interchangeably).

## Nice-to-Haves

- A direct comparison table contrasting the assumptions of this work with quasar-convexity, the aiming condition, and PL functions (covering uniqueness of minimizers, star-shaped sublevel sets, achievable rates, etc.) would help readers situate the contribution.
- A controlled experiment on a slightly larger network (e.g., a small CNN on a subset of CIFAR-10) at more realistic loss levels (e.g., \(10^{-3}\)–\(10^{-5}\)) would strengthen the claim that the assumptions hold in practical regimes.
- A discussion of whether the discrete-time analysis could be extended to local neighborhoods of curved manifolds (via a "staying locally" Lyapunov argument) would bridge the continuous/discrete gap.

## Removed Points
- **"Missing appendix, missing proofs, cannot be verified"**: Removed per policy—appendices are stripped by the parser, and the original submission contains them.
- **"Comparison to prior work should include a table"**: Demoted to Nice-to-Have, not a weakness of the paper as written.
- **"The connection to practice is not supported by data"** (framed as fatal/structural): Merged into the existing Major weakness about discrete-time restrictions and the Minor weakness about empirical validation; not a separate fatal issue since the continuous-time result stands on its own theoretical merit.
- **"Proof verification / discretization error concerns"**: Removed per policy—concerns about stripped appendix content cannot be evaluated.

## Novel Insights
None beyond the paper's own contributions. The key insight—that the parallel-movement inequality \(\langle\dot{x},\dot{z}\rangle \geq 0\) enables Lyapunov-based acceleration proofs for non-convex functions with a manifold of minimizers—is the paper's own contribution, well-stated in the text.

## Suggestions

1. **Restructure the narrative to clearly separate the continuous-time result (general \(C^2\) submanifolds) from the discrete-time results (affine subspaces only).** The current framing in the abstract and introduction bundles them under "virtually identical guarantees," which overpromises relative to what the discrete analysis delivers. A cleaner demarcation would allow readers to appreciate the continuous-time result's generality while understanding the discrete case as a first step toward a full theory.

2. **Strengthen the empirical section either by testing on a standard benchmark at realistic loss levels or by removing the claim that the assumptions are "well justified" empirically.** The theoretical link via Lemma 5 is sufficient on its own; the current experiments raise more questions than they answer.

3. **Add error bars and failure-rate reporting** to the empirical figures so readers can assess the variability of the measured quantities.

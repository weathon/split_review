Now I have a clear picture. Let me write the consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses

### Fatal
- weakness

### Major
- weakness

### Minor
- weakness

### Trivial
- weakness

## Nice-to-Haves
- suggestion

## Removed Points
...

## Novel Insights
...

## Suggestions
...

## Score and Decision

---

Here is my complete analysis:

---

**Round 1 (bracketing):** I searched with three queries bracketing low, middle, and high score bands. The low band (< 3.5) returned papers on NTK and deep learning theory with avg scores 0.5–3.0. The middle band (3.5–7.5) returned NTK-related papers with avg scores 4.5–6.0. The high band (> 7.5) returned papers on unrelated topics (quantum computing, rotation estimation). This placed the plausible bracket between 2.0 and 5.0.

**Round 2 (narrowing):** I searched inside (1.5, 4.0) and (4.0, 6.5) for topic-relevant anchors. The (1.5, 4.0) returned anchors at 3.5 (Empirical NTK, Kakeya-to-Kernels) — papers with theory-experiment disconnect or vacuous bounds but no proven mathematical errors. The (4.0, 6.5) returned anchors at 4.5–4.67 (Convex NTK, Grokking) — papers with sound or at least non-falsified theory. The paper under review has a proven mathematical error in the core proof, making it strictly weaker than the 3.5 anchors (which have weak contributions but no proven errors). It has some salvageable content (Theorem 2) that distinguishes it from the 2.0 anchor. Final score: **3.0**.

Let me compile the anchors:

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| b36drMoKir.md | 0.50 | 1 | Far weaker — withdrawn paper with no coherent contribution |
| IKy24F8tGn.md | 2.00 | 1 | Weaker — main theorem technically correct but meaningless |
| WB2ejxmIFt.md | 2.00 | 1 | Weaker — scale-time equivalence claim not well-supported |
| rDhCPKrZw7.md | 3.00 | 1 | Comparable — NTK for PDEs, borderline contribution |
| HksswvbYIp.md | 3.50 | 2 | Slightly stronger — no mathematical errors, just weak theory-experiment link |
| byBollQRc0.md | 3.50 | 2 | Comparable — incoherent framework but no proven errors |
| 444mACDffR.md | 4.50 | 1,2 | Stronger — technically sound even if dense and not novel enough |
| wGc6aWvRLa.md | 4.50 | 1,2 | Stronger — technically sound even if some assumptions questioned |
| sLX5P7FTfT.md | 4.67 | 2 | Stronger — accepted poster with good theory |
| B4zcoLvjw0.md | 6.00 | 1 | Much stronger — sound theory, accepted poster |
| vokk8t1gnp.md | 5.33 | 1 | Stronger — accepted poster |

Now the review itself:

---

## Summary

This paper studies the neural tangent kernel (NTK) of infinitely wide fully-connected ReLU networks as depth grows (with width growing much faster than depth). It makes two theoretical claims: (1) the normalized NTK converges to the matrix of ones (kernel collapse), and (2) despite this collapse, the closed-form expression $\tilde{\Theta}_\infty^{(L)}(x^\top X)^\top (\tilde{\Theta}_\infty^{(L)}(XX^\top))^{-1}$ converges to a well-defined bounded limit. The paper identifies a genuine limitation of prior work (Xiao et al. 2020) that assumes a particular decomposition into invertible and constant components, which fails when the kernel becomes singular.

## Strengths

1. **Theorem 2 (kernel collapse) is correctly reasoned and a useful observation.** The paper proves that the normalized NTK $\bar{\Theta}_\infty^{(L)}(x,x')$ strictly increases to 1 for any $x,x' \in S^{n_0-1}$ as $L \to \infty$, establishing that the kernel becomes the all-ones matrix in the limit. Proposition 4 provides a clean recursive relationship showing this behavior. While the proof is deferred to the appendix, the statement is mathematically coherent and follows from known recurrences for ReLU networks.

2. **The paper identifies a meaningful gap in prior work.** The observation that Xiao et al. (2020)'s proof in the ordered phase requires the kernel to decompose into a constant matrix plus an invertible data-dependent component — a condition violated when the kernel collapses to all-ones — is a genuine insight. The idea of analyzing what happens to the closed-form solution in the singular regime is an interesting direction.

3. **Generalization criteria for other kernels.** Section 6 lists three concrete sufficient properties (diagonal dominance, eventual positive definiteness, vanishing determinant of the normalized kernel) that make the proof technique transferable. The logistic-type example $\eta^{(L)}$ illustrates this framework. While this depends on the validity of Theorem 3, the distillation of properties is a useful framing device.

## Weaknesses

### Fatal

1. **Property (4) of Proposition 5 is mathematically incorrect, and the proof of Theorem 3 collapses as a result.** The claim is $\lim_{d \to 0^+} \frac{d^k}{dz^k} \psi_d(z) = 0$ for all $k \in \mathbb{N}_0$. For $\psi_d(z) = 1/(1 + \exp(-2z/(d(1-z^2))))$, the first derivative at $z=0$ is $\psi_d'(0) = 1/(2d)$, which *diverges* to $+\infty$ as $d \to 0^+$, not converges to $0$. This is not a subtle or debatable point — it follows directly from differentiating the sigmoid composition. The proof of Theorem 3 explicitly invokes property (4) to conclude that the driver terms $v_{(i,j)}$ converge to 0 in 1-variation, which then (via the Universal Limit Theorem) forces the interpolated solution to converge to $u'=0$. If the derivatives blow up rather than vanish, this chain of reasoning is unfounded. This error is in the core of the paper's main claimed contribution; the proof of Theorem 3 is not fixable by minor modification.

### Major

2. **Even setting aside the $\psi_d$ error, the proof of Theorem 3 is too sparse to be convincing.** The entire "proof" in the main text is roughly one paragraph (~25 lines). It defines a homotopy interpolation, takes a derivative, cites Cramer's rule, invokes the Lyons Universal Limit Theorem, and concludes. The paper states that background on rough differential equations is in Appendix D and the full proof is in the appendix — sections stripped by the PDF extraction process. As presented in the main text, the reasoning is insufficient: the argument that the drivers $v_{ij}$ converge to 0 relies on bounding determinants whose behavior is not analyzed, and the connection from "the drivers converge to 0" to "the original sequence of solutions converges" is asserted rather than derived. A reader cannot verify the proof from what is printed.

3. **Experimental evidence is too minimal to provide meaningful support.** The paper shows one figure with a single synthetic dataset ($n_0=128$, depths 1–30). The dataset size $n$ is not reported, there are no error bars, no multiple random seeds, and no comparison with any theoretical convergence rate derived from the proof. The MNIST experiment is referenced but placed in the stripped appendix, so it cannot be assessed. The paper's own conclusion contradicts itself: "convergence for the limiting kernel is sublinear" appears adjacent to "convergence for the limiting kernel is experimentally fast" — it is unclear which quantity is being described. For a paper whose central claim is a convergence result, the empirical support is insufficient.

### Minor

4. **The paper does not characterize the claimed limit, only asserts its existence.** Theorem 3 states the limit is bounded and continuous in $x$, but provides no explicit formula, no characterization, and no method to compute it. The claimed improvement over Xiao et al. (2020) is framed as "handling the singular case," but without showing what the limit actually is or how it differs from the predictor in the invertible regime, the contribution's practical value is unclear.

5. **Lemma 1 (convergence of $\rho^{(L)} \to 1$) is stated without proof or reference.** This lemma is foundational for both Theorem 2 and Theorem 3. While the recurrence for $\rho$ is given in Proposition 2 (citing Arora et al. 2019b), showing that all trajectories with $\rho^{(1)} \in (-1,1)$ converge monotonically to the fixed point at 1 requires analysis that is not provided. This is a minor omission if the proof exists in the literature, but it should be cited.

### Trivial

6. Conclusion text is confusing: "while convergence for the limiting kernel is sublinear, the convergence for the limiting kernel is experimentally fast" — the same phrase "limiting kernel" appears to refer to two different quantities (the kernel itself vs. the closed-form solution), making the sentence self-contradictory. This should be clarified.

## Nice-to-Haves

- An explicit characterization of the limit in Theorem 3, or at least a demonstration that it is non-constant and data-dependent, would greatly increase the paper's impact.
- A simpler proof approach (e.g., Sherman-Morrison perturbation analysis, as suggested by the harsh critic) might avoid the rough-path machinery entirely and produce a more verifiable argument.

## Removed Points

- *Concerns about contribution relative to prior work being unclear*: The paper does adequately distinguish its setting (depth growing slower than width, deterministic limit) from Hanin & Nica (2020) (depth growing faster than width, stochastic limit). The comparison to Xiao et al. (2020) is also clearly stated, even if the claimed improvement cannot be realized without a valid proof.
- *Criticism that the paper "never proves that the limit is non-trivial"*: This is a reasonable point but is already captured in the Minor weakness section as a lack of characterization, not a separate weakness.
- *Stylistic and formatting nitpicks*: Removed per policy — parser artifacts are not author errors.
- *Strength about "Theorem 3 gives a limiting solution without requiring kernel invertibility"*: This is the claimed contribution, but since the proof is invalid, this cannot be treated as an established strength.
- *Strength about "empirical validation"*: The experiments are too minimal to qualify as a strength.

## Novel Insights

None beyond the paper's own contributions. The reviewers did not provide observations that transcend what the paper itself says.

## Suggestions

1. **Correct or replace the $\psi_d$ construction.** The function as defined does not have the claimed derivative decay. Consider an alternative approach: since Theorem 2 shows $\bar{\Theta}_\infty^{(L)} \to \mathbf{1}\mathbf{1}^\top$, the sequence of kernel matrices can be written as $c_L(\mathbf{1}\mathbf{1}^\top + \varepsilon_L)$ with $\varepsilon_L \to 0$. The limiting behavior of $\kappa_x^\top \kappa^{-1}$ could be analyzed via a perturbation argument (e.g., Sherman-Morrison formula) without rough path theory.

2. **Provide explicit characterization or computation of the limit.** Show the limit for a small-$n$ example (e.g., $n=2$ points on the sphere) where the limit can be computed analytically. This would demonstrate that the limit is non-trivial and data-dependent.

3. **Strengthen experiments.** Report $n$, show error bars over multiple random seeds, and demonstrate that the limit depends on the dataset. Compare empirical convergence to a theoretically derived rate.

## Score and Decision

The paper tackles an interesting problem and identifies a genuine gap in prior work on the NTK in the depth limit. Theorem 2 (kernel collapse) is a valid observation. However, the proof of the paper's central contribution (Theorem 3) contains a mathematical error: Property (4) of Proposition 5, on which the proof relies, is false — the derivatives of $\psi_d$ at $z=0$ diverge as $d\to 0^+$, not converge to 0. This makes the argument for Theorem 3 unsound. The proof sketch is too sparse to verify independently, and the experiments are too minimal to compensate. The paper cannot be accepted in its current form.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>
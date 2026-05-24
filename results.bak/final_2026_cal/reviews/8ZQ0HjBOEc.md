Now I have sufficient anchors for calibration. Let me compose the final review.

**Round-1 bracketing**: I initially bracketed this paper between 2 and 4, based on comparing to the 0.50 anchor (completely broken proof, withdrawn) and the 3.50–4.50 anchors (varying issues but no fatal proof error).

**Round-2 narrowing**: Comparing to anchors at 3.50 (Loss Kernel, Empirical NTK), 4.00 (Solvable GF), and 4.50 (Near-Linear Width), all these papers had issues of scope or insufficient rigor but NOT a demonstrably false mathematical claim at the core. The current paper's property (4) is mathematically false, which sinks Theorem 3 — a more severe problem than any of those papers faced. Therefore the paper lands below 3.0, near the 2.00 anchor range (papers withdrawn for fundamental proof issues), but slightly above the 0.50 anchor (which was completely broken in its entirety). The final score is **2.5**.

---

## Summary

This paper studies the normalized Neural Tangent Kernel (NTK) of infinitely wide ReLU networks as depth increases. Its two main theoretical claims are: (1) the normalized kernel converges pointwise to the all-ones matrix (Theorem 2), and (2) the closed-form predictor $\tilde{\Theta}_\infty^{(L)}(x^\top X)^\top (\tilde{\Theta}_\infty^{(L)}(X X^\top))^{-1}$ converges to a well-defined limit even as the kernel becomes singular, using rough differential equations (Theorem 3). The paper also provides empirical illustrations on synthetic data and MNIST.

## Strengths

- **Lemma 1 (convergence of $\rho^{(L)}\to 1$) and Proposition 4 (alternative formulation of the normalized kernel)** are clean, self-contained results that correctly build on known formulas for the ReLU NTK (Cho & Saul 2009; Arora et al. 2019b) and provide the foundation for the subsequent analysis.

- **Theorem 2 (convergence of $\bar{\Theta}_\infty^{(L)}$ to 1)** states a clear, non-trivial claim about how depth collapses the normalized NTK to the matrix of ones. If its proof in Appendix C is correct, this is a meaningful contribution to understanding depth effects in the NTK literature.

- **The paper identifies three sufficient conditions** that any kernel sequence must satisfy to exhibit the same limiting behavior, providing a template for extending the analysis beyond ReLU activations to other architectures.

## Weaknesses

### Fatal

- **Property (4) of Proposition 5 is mathematically false, invalidating the proof of Theorem 3.** The function $\psi_d(z) = 1/(1+\exp(-2z/(d(1-z^2))))$ is stated to satisfy $\lim_{d\to 0^+} \frac{d^k}{dz^k}\psi_d(z) = 0$ for all $k$. Direct computation shows $\psi_d'(0) = 1/(2d)$, which diverges to $+\infty$ as $d\to 0^+$, not $0$. The proof of Theorem 3 explicitly relies on this property to argue that the drivers $v_{ij}^{(L)}$ converge to $0$ in $1$-variation. Since the interpolation $A_n^{(L+1)}(t)$ crosses $z=0$ (where $2t-1=0$), the derivatives blow up rather than vanish as $\mathcal{D}\to 0$, and the central convergence argument is unsupported. Without a valid proof of Theorem 3, the paper's core contribution — that the predictor converges despite a singular kernel — is unsubstantiated. This is not a speculation; it is a verifiable mathematical error on the page (Section 5, Definition 6 and Proposition 5).

### Major

- **The proof of Theorem 3 contains additional gaps beyond the $\psi_d$ error.** The inequality chain that bounds the Cramer's rule expression is presented without clear justification for several steps: the denominator manipulation using $\det(\tilde{\Theta}^{(L+1)})^{\psi_{\mathcal{D}}(2t-1)}\det(\tilde{\Theta}^{(L)})^{1-\psi_{\mathcal{D}}(2t-1)}$ and the claim that "strictly positive determinants are all smaller than 1 for large $L$" have unclear directionality. These are not merely presentation issues — they reflect that the proof sketch, as written, does not constitute a valid argument.

- **The claimed novelty over Xiao et al. (2020) is not convincingly established.** The final bound from Theorem 3 is $u_\infty(t) < C'\mathbf{1}_n$, which shows boundedness but does not characterize the limit beyond that. Xiao et al. already analyze the ordered phase and show the predictor collapses to a constant. Even if Theorem 3 were correct, it is unclear whether the limit is data-dependent/non-trivial or simply a constant — the paper asserts the former but only proves the latter.

### Minor

- **The function $\psi_d$ has a singularity at $z=\pm 1$** due to the $(1-z^2)$ factor in the denominator. While the cases $z=\pm 1$ are handled explicitly, the $C^\infty$ claim (Property 3) near these boundary points is non-trivial and unaddressed. However, this is secondary to the main fatal issue.

- **The experiments are illustrative but not confirmatory.** Only one synthetic dataset (dimension 128, depth up to 30) and MNIST are tested, without error bars or statistical significance. The hypothesis that "small determinants indicate fast convergence" is speculative and not tested. The experiments do not compute the actual limiting predictor directly, only the kernel matrix products.

### Trivial

- There is a minor typo: $x^\top x^\top$ on lines 159 and 223 should be $x^\top X$.

## Nice-to-Haves

- If the proof of Theorem 3 is to be salvaged, the authors should consider a different interpolation function that does not rely on vanishing derivatives, or a direct spectral analysis of the singular kernel limit (e.g., spherical harmonic expansions as in Bietti & Bach 2021 or Murray et al. 2023).
- The experiments would be substantially strengthened by computing the limiting predictor directly (e.g., by solving kernel regression with the limit kernel after appropriate regularization) to demonstrate that the limit is non-trivial and matches the theoretical prediction.
- A more precise characterization of the limiting predictor — beyond just boundedness — would clarify whether the result actually goes beyond what is already known from the ordered phase.

## Removed Points

These points were raised by reviewers but removed after verification against the paper:

- *Scaling concern about Proposition 1/Definition 4* (harsh critic): The critic questioned whether the normalization yields $\bar{\Theta}_\infty^{(L)}\to (1/2)\|x\|\|x'\|$. Direct calculation using Proposition 1 and Definition 4 gives $\bar{\Theta}_\infty^{(L)} = \|x\|\|x'\|$ for the $\rho=1$ case, consistent with Theorem 2. This concern reflects a miscalculation, not a paper error.
- *Criticism about missing related works*: Removed per instructions — I cannot verify which related works exist.
- *Formatting/style nitpicks*: Removed per instructions — these reflect parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The core observation (NTK becomes singular with depth yet the predictor may stabilize) is genuinely interesting, but it cannot be evaluated as a contribution when the proof claiming to establish it is invalid.

## Suggestions

1. **Fix or replace the proof of Theorem 3.** Property (4) of Proposition 5 must be corrected — the derivatives of $\psi_d$ at $z=0$ blow up as $d\to 0^+$, not vanish. An alternative approach (e.g., analyzing the eigensystem of the limiting kernel, or using spherical harmonic expansions) may be more promising than the rough-path construction used here.
2. **Characterize the limit more precisely.** Show whether the limiting predictor is data-dependent, constant, or the projection onto a specific eigenfunction. Without this, it is unclear what the result adds beyond the ordered-phase analysis of Xiao et al. (2020).
3. **Strengthen the experimental evaluation.** Include error bars, test on more diverse datasets, and directly compute the limiting predictor to validate the theoretical prediction.

## Score and Decision

**MY FINAL SCORE: <score>2.5</score>**
**MY FINAL DECISION: <decision>Reject</decision>**

### Calibration details

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| IKy24F8tGn | 2.00 | R1 | Residual network depth paper — withdrawn for insufficient contribution and a theorem that was technically correct but practically meaningless. Worse in contribution, but its theorem was correct. Our paper has a verifiably false claim, making it slightly worse. |
| b36drMoKir | 0.50 | R1 | Gradient flow convergence — withdrawn for an incorrect proof that didn't prove what it claimed. Similar kind of fatal flaw, but that paper was more completely broken. Our paper is better (has some correct lemmas and experiments). |
| buuwRBYfrP | 4.67 | R1 | KAN convergence analysis — accepted poster. Correct theory with incremental contribution. Our paper has a fatal proof error, significantly worse. |
| 0elvad3gEu | 5.50 | R1 | NTK width determination — accepted poster. Solid theory and experiments. Our paper is substantially weaker. |
| HksswvbYIp | 3.50 | R2 | Empirical NTK tracks task complexity — rejected for limited scope. Had correct empirical work and some theory. Our paper's flaw is more fundamental (incorrect mathematical claim). |
| xa3oLRQG55 | 4.00 | R2 | Solvable gradient flow — rejected for narrow scope and non-rigorous analysis. Not a fatal error, just insufficient generality. Our paper is worse. |
| wGc6aWvRLa | 4.50 | R2 | Near-linear width ReLU networks — rejected for questionable assumptions but mostly correct analysis. Our paper's flaw is more severe. |
| c8p1zuTA33 | 3.50 | R2 | Loss kernel interpretability — withdrawn for limited experiments. No mathematical errors. Our paper is worse. |
| CiB4te6gGq | 2.00 | R2 | Adam convergence — withdrawn for massive proof gaps and missing references. Comparable severity to our paper's flaw. |

**Round-1 bracket**: 2–4. The paper's fatal proof error excludes it from the 3.5+ range (where papers have mostly correct reasoning) and places it near the 2.00 range.

**Round-2 narrowing**: The paper sits between the 0.50 anchor (purely broken) and the 2.00–3.50 anchors (partial contributions with varying issues). The verifiable mathematical error in Proposition 5(4) is a fatal flaw that invalidates the paper's central theorem. Score **2.5**.
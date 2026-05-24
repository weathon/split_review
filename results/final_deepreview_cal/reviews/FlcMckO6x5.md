## Summary

This paper establishes theoretical foundations for separable neural networks (SepNNs), an architecture class that factorizes multivariate functions into linear combinations of univariate factor networks. It makes three contributions: (1) a universal approximation theorem for CP, TT, and Tucker SepNNs using Stone–Weierstrass plus universal approximation; (2) a neural tangent kernel (NTK) analysis characterizing the training dynamics under different asymptotic regimes (infinite vs. fixed width/rank); and (3) SepPGD, a separable preconditioned gradient descent method that exploits the factorized structure to apply preconditioners with \(\mathcal{O}(n D)\) per-iteration cost for \(n^D\) grid samples, along with experiments on KRR, INR image/surface representation, and PINNs demonstrating faster convergence.

## Strengths

- **Universal approximation theorem (Theorem 1):** Proves rigorously that CP, TT, and Tucker SepNNs with non-polynomial activations can approximate any continuous multivariate function on compact sets. The Stone–Weierstrass approach is clean and applies uniformly across all three decomposition forms, filling a genuine theoretical gap.
- **NTK characterization (Lemma 1, Theorem 2, Corollary 1):** Derives a closed-form NTK for CP SepNNs as a weighted sum of factor NTKs (Lemma 1, Eq. 4), proves convergence to a deterministic kernel under infinite width *and* infinite rank (Theorem 2), and identifies a stochastic kernel limit under fixed rank (Corollary 1). The empirical validation in Figure 1 confirms these predictions across multiple seeds.
- **SepPGD algorithm (Definition 1, Lemma 2):** Lemma 2 cleanly connects SepPGD to classical NTK-based PGD via a Kronecker-structured preconditioner \(\tilde{\mathbf{S}} = \mathbf{S}_1 \otimes \mathbf{I} + \mathbf{I} \otimes \mathbf{S}_2\) for the \(D=2\) case. The decomposition of a large \(n^2 \times n^2\) preconditioner into smaller \(n \times n\) factor-level operations is a genuine efficiency insight.
- **Consistent empirical speed-up across diverse tasks:** Figures 2–4 show SepPGD converging faster than MLP, SepNN, and MSK baselines in wall-clock time for KRR, image/surface INR representation, and PINN-based PDE solving, with visual quality improvements (Figure 3).

## Weaknesses

### Fatal
None.

### Major

- **Missing Lemma 3 leaves a gap in the spectral-adjustment claim.** The abstract and Section 4 state that SepPGD "provably adjusts the NTK spectrum." This depends on the assertion that the factor-NTK proxy \(\tilde{\mathbf{K}} = \mathbf{K}_{\Theta_1} \otimes \mathbf{I} + \mathbf{I} \otimes \mathbf{K}_{\Theta_2}\) is close to the true SepNN NTK \(\mathbf{K}\). Lemma 3 is referenced for this ("Suppose that \(\tilde{\mathbf{K}}\) is close to the true NTK matrix \(\mathbf{K}\) which can be verified using the NTK matrix formulation in Lemma 3") but its statement, bounds, or conditions do not appear anywhere in the main text. Without Lemma 3, the theoretical chain from Lemma 2 (equivalence to classical PGD) to "provably adjusts the spectrum" is incomplete. This is the paper's most significant weakness and must be addressed — at minimum by stating Lemma 3's claim in the main text, even if the proof is deferred to the appendix.

### Minor

- **Abstract overstates complexity advantage.** The abstract claims "efficient \(\mathcal{O}(n D)\) complexity" without qualification. Footnote 3 acknowledges that constructing the mode-\(d\) preconditioner \(\mathbf{M}_d\) via Eq. (8) involves an \(\mathcal{O}(n^{D-1})\) matrix product. For large \(D\) this term can be significant. The table is correctly scoped to "applying the preconditioner," but the abstract should reflect the full picture.
- **Spectral bias alleviation is not directly measured.** The experiments (Figures 2–4) show faster MSE convergence but do not decompose the residual onto NTK eigenmodes to verify that small-eigenvalue components are specifically accelerated. The empirical evidence for spectral bias alleviation is therefore indirect.
- **Theorem 1 proof sketch omits the multiplication-closure step.** The main text says "We carefully examine that \(\mathcal{A}\) meets these requirements" for the Stone–Weierstrass conditions, but provides no hint of how the product of two CP-form functions yields another CP-form function. The full proof is in Appendix A.5 (stripped by the parser), but a one-line algebraic demonstration in the main text would make the theorem's credibility self-contained.

### Trivial
None.

## Nice-to-Haves

- An ablation study varying the decomposition rank \(R\) and factor-MLP width \(W\) would clarify how SepPGD's effectiveness depends on proximity to the infinite-width/rank regime.
- A direct eigenmode decomposition of the residual error, showing that small-eigenvalue components converge faster under SepPGD, would strengthen the spectral-bias narrative.

## Removed Points

*These points were flagged for removal; treat them with caution.*

- **Harsh critic's claim that the per-iteration complexity is "misleading"** — The paper addresses the \(\mathcal{O}(n^{D-1})\) preconditioner construction cost in Footnote 3, and Table 1 is explicitly scoped to the "gradient formulation" / preconditioner application cost. The concern is valid as a qualification (retained as Minor above) but the framing as "misleading" is too strong.
- **Harsh critic's demand for full closure-under-multiplication verification in the main text** — The full proof is in Appendix A.5. This is an exposition preference, not a flaw in the result. Retained as Minor above for presentation clarity.
- **Strength Finder's claim about "provable complexity reduction"** — The complexity advantage for gradient application is genuine and verified by Lemma 2; the "provable" qualifier for spectral adjustment is what's weakened by the missing Lemma 3.
- **Strength Finder's generic strength about "important problem"** — Removed as superficial; the paper's strengths are grounded in specific results, not problem importance.
- **Harsh critic's concern that experiments "only cover infinite-width/rank phenomena qualitatively"** — Figure 1 is explicitly a qualitative verification of the asymptotic theory, which is appropriate for its purpose.

## Novel Insights

The NTK decomposition in Lemma 1 — expressing the SepNN's NTK as \(K_\Theta(\mathbf{x}, \mathbf{x}') = \frac{1}{R} \sum_{d=1}^D \mathbf{a}_d(\mathbf{x})^\top \mathbf{K}_{\Theta_d}(x_d, x'_d) \mathbf{a}_d(\mathbf{x}')\) where the factor NTKs \(\mathbf{K}_{\Theta_d}\) are modulated by cross-factor products \(\mathbf{a}_d\) — is elegant and non-obvious. It reveals that the SepNN's training dynamics are governed by a structured combination of factor-level kernels, which directly motivates the separable preconditioner design. This structural insight may generalize to other factorized architectures beyond the CP/TT/Tucker forms considered here.

## Suggestions

- **State Lemma 3 explicitly in Section 4**, even as a one-sentence claim: "Under conditions X, \(\|\tilde{\mathbf{K}} - \mathbf{K}\| \leq \epsilon\) with \(\epsilon\) bounded by Y." The full proof can remain in the appendix, but the statement must appear in the main text to close the theoretical gap.
- **Add a one-line algebraic demonstration** of how the product of two CP-form functions yields another CP-form function (e.g., expanding the double sum and re-indexing), making the Stone–Weierstrass closure step self-evident.
- **Qualify the complexity claim in the abstract**, e.g., "\(\mathcal{O}(n D)\) per-iteration cost for applying the preconditioner (with an \(\mathcal{O}(n^{D-1})\) one-time construction cost)."
- **Add an eigenmode convergence plot** to one experiment (e.g., KRR noiseless) showing that residual components aligned with small NTK eigenvalues converge faster under SepPGD than under standard gradient descent.

## Score and Decision

**Round 1 bracket:** 5.0–7.0. The paper is clearly stronger than the weak-band anchors (2.3–3.4) and clearly weaker than the strong-band anchors (7.6–8.0). It compares most closely with middle-band anchors like ydlDRUuGm9 (KAN expressiveness/spectral bias, avg 6.25) and O6znYvxC1U (Bayesian NTK spectrum, avg 6.33).

**Round 2 narrowing:** Compared directly with TNYLCF7vZA (4.75, the IGA/Shi et al. paper this work builds on and cites), this paper is substantially stronger — it provides more comprehensive theory (universal approximation + NTK regimes), a novel architecture-specific algorithm, and cleaner experiments. Compared with 5xwx1Myosu (6.50, expressivity of random-weight networks) and ydlDRUuGm9 (6.25), this paper is comparable in theoretical depth but adds a practical algorithm with empirical validation. The missing Lemma 3 is a genuine gap that prevents it from reaching the 7+ range, but it is likely addressable in rebuttal.

**Anchor summary:**
| Anchor | Score | Round | Comparison |
|---|---|---|---|
| fUz6Qefe5z | 3.00 | R1 | Much weaker — narrow NTK scope, no algorithm |
| 2NwHLAffZZ | 2.33 | R1 | Much weaker — speculative theory, no experiments |
| xpmDc76RN2 | 2.33 | R1 | Much weaker — limited theoretical contribution |
| kkVTeMvC9D | 3.40 | R1 | Weaker — empirical study of Jacobian, no algorithm |
| YN4uWzcbtt | 4.25 | R1 | Weaker — single NTK property result |
| TNYLCF7vZA | 4.75 | R2 | Clearly weaker — same research lineage, less comprehensive |
| mMjSc5fspq | 5.25 | R2 | Weaker — application-focused, less theoretical depth |
| Ge7okBGZYi | 5.25 | R2 | Weaker — narrower scope |
| GqI4fTVUXC | 6.00 | R2 | Slightly weaker — mainly critical analysis |
| PJjHILiQHC | 6.25 | R1/R2 | Comparable — empirical approach to spectral dynamics |
| ydlDRUuGm9 | 6.25 | R1 | Most comparable — this paper adds algorithm contribution |
| 1Wi0Ys33Nm | 6.25 | R2 | Comparable — theoretical extension of NTK theory |
| O6znYvxC1U | 6.33 | R1 | Comparable — strong theory, weaker experiments |
| 92btneN9Wm | 6.33 | R2 | Comparable — architecture design for INRs |
| 5xwx1Myosu | 6.50 | R2 | Comparable — this paper has broader empirical scope |
| STUGfUz8ob | 7.60 | R1 | Stronger — more complete theory+experiments |
| AoraWUmpLU | 8.00 | R1 | Stronger — more polished contribution |
| TTrzgEZt9s | 8.00 | R1 | Much stronger — different domain |
| OeQE9zsztS | 8.00 | R1 | Stronger — more complete theoretical framework |

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
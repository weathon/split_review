- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
Now I have a thorough understanding of the paper and both reviews. Let me carefully construct the consolidated review.

## Summary

This paper studies a specific MLP construction with batch normalization (BN), orthogonal Haar-distributed weight matrices, linear activations, and batch size equal to width. It proves two non-asymptotic results: (1) the isometry gap decays exponentially with depth (Theorem 1), implying perfect orthogonalization in the infinite-depth limit, and (2) expected log-gradient norms are bounded by a depth-independent constant (Theorem 2), in stark contrast to the exponential explosion known for Gaussian-weight BN networks. The paper also proposes an empirical activation shaping scheme to extend some benefits to non-linear activations (tanh, sin). The theory uses Weingarten calculus for finite-width analysis, moving beyond prior mean-field/infinite-width regimes.

---

## Strengths

1. **First non-asymptotic bounded-gradient guarantee for BN networks.** Theorem 2 (Eq. 2) proves that the expected log-gradient norm is bounded by \(O(d^5)\) independent of depth, directly contradicting the long-held belief from Yang et al. (2019, Thm. 3.9) that gradient explosion is unavoidable in BN networks. The bound is non-asymptotic and applies at finite width.

2. **Exponential decay of isometry gap (stronger than prior work).** Theorem 1 (Eq. 1) proves that the isometry gap decays as \(O(e^{-\text{depth}/C})\), meaning representations become *perfectly* orthogonal in the infinite-depth limit. This improves on Daneshmand et al. (2021), who only guarantee convergence to within an \(O(\text{width}^{-1/2})\) ball of orthogonality. Figure 1 empirically confirms the predicted rate.

3. **Rigorous finite-width analysis using Weingarten calculus.** The proof technique (Section 3, Theorem 3) is a genuine technical contribution. It provides explicit eigenvalue-based bounds on the expected isometry increase under random orthogonal matrices, without resorting to mean-field or infinite-width limits that have characterized virtually all prior work on BN gradient propagation.

4. **Empirical validation of core theoretical claims.** Figure 2 empirically confirms that gradients remain bounded for non-degenerate inputs while exploding for degenerate inputs, validating the necessity of the full-rank condition. Figure 3 shows nearly depth-independent training convergence (CIFAR10, linear activations) with vanilla SGD, confirming that the theoretical guarantees translate to stable optimization.

---

## Weaknesses

### Fatal

None.

### Major

1. **Theory covers only linear activations; non-linear extension is purely empirical without guarantees.** The main theorems (1 and 2) are proved exclusively for identity activations. While the paper transparently acknowledges this limitation (abstract, line 37), the activation shaping scheme in Section 5—the paper's only bridge to non-linear activations—is entirely heuristic. The paper states that tuning gains yields "faster decay than a harmonic series" (line 243), but provides no principled selection rule for \(\alpha_\ell\) and no theoretical bound. Figure 4 shows the growth rate of log-gradient norms is *reduced* by shaping, not eliminated. The claim that shaping "effectively avoids gradient explosion" (line 243) is not provably established; the curves still trend upward with depth, just more slowly. Without any theoretical handle, the non-linear extension remains a promising experiment rather than a validated solution, which limits the practical scope suggested by the title "Towards Training Without Depth Limits."

2. **Activation shaping lacks theoretical grounding and a concrete design rule.** The paper proposes tuning a per-layer gain \(\alpha_\ell\) to make activations more linear, but provides no formula, optimization procedure, or even a worked example for how to set \(\alpha_\ell\) in practice. The only guidance is "faster decay than a harmonic series" (line 243), which is too vague to be reproducible or actionable. This section reads as a separate empirical study rather than a principled extension of the theory, leaving a substantial gap between the paper's theoretical core and its claimed practical relevance.

### Minor

3. **Assumption \(n = d\) (batch size = width) is restrictive and unrelaxed.** The paper treats this as part of the construction (line 71), which is acceptable for a theoretical paper, but there is no discussion of how the results degrade when \(n \neq d\), which is the overwhelmingly common setting (e.g., batch size 512 with width 100). A brief remark on what changes when \(n < d\) or \(n > d\) would significantly improve practical relevance without requiring new proofs.

4. **Simplified BN (no mean reduction) is used in the theory, and the justification for standard BN is only empirical.** The BN operator in Eq. (6) omits mean reduction, which the paper acknowledges (line 69) and claims experimentally does not affect results (citing Figure~\ref{fig:mean_reduction}, which is in the stripped appendix). While this is a common simplification in theoretical BN work (Daneshmand et al., 2021), a theoretical characterization of how mean reduction affects the isometry gap and gradient bounds would be more satisfying, even as a short remark or lemma.

5. **Training comparison with Gaussian-weight BN is shown only at initialization, not during optimization.** Figure 2 and the main gradient comparison (Figures in Section 3.3) contrast orthogonal vs. Gaussian weights at initialization. While Figure 3 shows training curves for the orthogonal construction, there is no direct training comparison (e.g., epochs to reach a target accuracy) against Gaussian-weight BN networks. This would calibrate whether avoiding gradient explosion at initialization actually translates to a practical training advantage.

### Trivial

None.

---

## Nice-to-Haves

- A more explicit derivation in the main text showing how the exponential decay of the isometry gap (Theorem 1) translates into the geometric series bound on log-Jacobian norms in Theorem 2. The current proof sketch (lines 198–199) outlines the idea but leaves many steps implicit.
- An empirical estimate of the variance of gradient norms across random seeds, to complement the expectation bound in Theorem 2. Practitioners would benefit from knowing whether the bound is tight or whether worst-case gradients can occasionally explode.
- A brief discussion of whether the results are robust to *approximate* orthogonality (e.g., near-orthogonal matrices from spectral normalization during training), which would help bridge to practical training dynamics.

---

## Removed Points

Points flagged to be removed; treat with caution.

- **"The phrase 'isometry gap' is introduced later; abstract could define it briefly."** — This is a presentation nitpick. The abstract focuses on high-level claims; definitions are appropriately placed in Section 3.
- **"Double standard about 'hard to validate' assumptions."** — The paper's criticism of prior work (line 54) is a standard scientific argument about different assumptions. This is not a weakness of the paper itself.
- **"The constant C in Theorem 1 could be more explicit."** — Moved to Nice-to-Haves. The constant is characterized (\(k := Cd^2(1 + d\cdot IG(X_0))\)), which is reasonable for a non-asymptotic bound.
- **"Implicit orthogonality bias section could be shortened/moved to appendix."** — This is a subjective presentation preference, not a weakness. The section reports an interesting empirical finding.
- **"Comparison to LayerNorm/GroupNorm."** — Scope creep. The paper is about BN specifically, motivated by the specific theoretical result of Yang et al. (2019) on BN.
- **"Variance of gradient estimates."** — Moved to Nice-to-Haves. An expectation bound is standard for this type of theoretical analysis; requesting high-probability bounds is a strengthening suggestion, not a flaw.
- **"Missing appendix content / proofs deferred to appendix."** — Per policy, the parser strips appendices from all papers. These sections exist in the original submission and cannot be reviewed here.
- **"The claim about standard BN is only supported by a single experiment in the appendix."** — As above, the appendix is stripped. The paper states it provides experimental evidence.
- **Harsh Critic's "Section-by-Section Notes" about the abstract, introduction, and related work being clear/well-cited.** — These are not weaknesses; they are positive observations that belong in the strengths section if needed, but the Strength Finder already covers the key points.
- **Strength Finder's generic strengths:** "This paper addressed an important problem" — Removed as generic/superficial. The important problem is well-established in prior work (Yang et al., 2019); the paper's contribution is the specific solution, not recognizing the problem.

---

## Novel Insights

The key insight that emerges from synthesizing the reviews is that this paper's contribution is clearest when viewed as a *disproof of an impossibility claim*: it constructs a counterexample (orthogonal weights + BN + linear activations + \(n = d\)) to the prevailing belief that gradient explosion is inevitable in BN networks. The reviewers converge on the assessment that this is a solid theoretical result—rigorous, non-asymptotic, and clearly communicated. However, both also agree that the paper's framing overreaches. The title and narrative imply broader applicability than the theory supports (linear activations only), and the activation shaping section—the paper's main bridge to practical nonlinear networks—is empirically suggestive but theoretically disconnected. The paper would be strengthened by either (a) clearly scoping the contribution as the theoretical construction alone (with activation shaping as a speculative appendix), or (b) providing even a weak theoretical bound for shaped activations. The most valuable follow-up direction suggested by this work is a combined analysis: can the Weingarten-calculus technique be extended to activations with bounded derivatives, yielding a quantitative trade-off between non-linearity and gradient growth?

---

## Suggestions

1. **Clearly reposition activation shaping as an empirical exploration**, removing the claim that it "effectively avoids gradient explosion" (which implies a guarantee) and instead stating it "reduces the growth rate." This would align the section's language with its evidence.
2. **Add a brief remark on the \(n \neq d\) case** (even a speculative paragraph) discussing whether the isometry gap bound degrades gracefully, to help readers assess practical applicability.
3. **Add a small training comparison experiment** (e.g., a table showing epochs to 50% accuracy for orthogonal vs. Gaussian weights at varying depths) to directly demonstrate the optimization benefit of the proposed construction.
4. **Provide at least one concrete example** of the activation gain schedule (e.g., \(\alpha_\ell = 1/\ell\) or similar) to make the shaping scheme reproducible without relying on the appendix.

---

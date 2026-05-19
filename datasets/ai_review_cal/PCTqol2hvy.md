- Decision: Reject
- Avg Score: 6.25
- Scores: 6, 8, 3, 8
Now I have all the information I need. Let me compose the final consolidated review.

---

## Summary

This paper studies the approximation capability of ResNet (specifically bottleneck ResNet, or b-ResNet) in terms of tunable-parameter complexity. It provides upper-bound constructions showing that b-ResNet can approximate monomials, polynomials, smooth functions, and a KST-based function class with a factor-of-\(d\) reduction in tunable weights compared to known ReLU FNN constructions. The paper also attempts to derive lower bounds via a conversion from ResNet to FNN (Proposition 1) and claims near-optimality for some of its upper bounds. The core contribution is the upper-bound result (Theorem 3): a b-ResNet approximates any \(d\)-dimensional degree-\(p\) monomial to accuracy \(\varepsilon\) using \(\mathcal{O}(p\log(p/\varepsilon))\) tunable weights, versus \(\mathcal{O}(dp\log(p/\varepsilon))\) for the best-known ReLU FNN construction.

---

## Strengths

- **Factor-\(d\) reduction in tunable weights for monomial approximation (Theorem 3).** The paper provides the first explicit construction (in the appendix) showing that a b-ResNet with constant-width activation layers can approximate any \(d\)-dimensional monomial of degree \(p\) using \(\mathcal{O}(p\log(p/\varepsilon))\) non-zero tunable weights. The comparison with the ReLU FNN construction from DeVore et al. (2021), which requires \(\mathcal{O}(dp\log(p/\varepsilon))\) tunable weights, is clearly stated in the main text (line 149) and is a concrete, verifiable contribution.

- **Honest acknowledgment of limitations.** The paper explicitly notes (lines 200–201) that its approximation rates for Sobolev and continuous functions are suboptimal by an exponential factor of \(1/2\) compared to quantization-based methods, and identifies this as an open direction. This candor is appropriate for a theory paper.

- **KST-based application to overcome the curse of dimensionality (Theorem 8).** The paper constructs a ResNet with \(\mathcal{O}(d^{4}\varepsilon^{-1})\) tunable parameters to approximate functions in a dense subclass \(K_C\) of \(C([0,1]^d)\), avoiding exponential dependence on \(d\). This is a nontrivial extension that leverages Lipschitz continuity of the inner and outer KST functions.

- **CPwL exact representation by narrow ResNet (Theorem 6).** Proving that a ResNet with one neuron per activation layer can exactly represent any continuous piecewise-linear function extends prior step-function results and is a clean theoretical observation.

---

## Weaknesses

### Fatal

None. The paper's upper-bound constructions are a genuine contribution that does not depend on the lower-bound reasoning. The flaws in the lower-bound argument are significant but do not invalidate the main results.

### Major

- **The lower-bound reasoning does not support the "nearly tight" claim for Theorem 5, and the optimality framing is overreaching.** Proposition 1 shows that a ResNet with \(W\) tunable parameters, depth \(L\), and identity-layer width \(k\) can be converted to an FNN with \(\Theta(W+kL)\) parameters. From this, the paper concludes (lines 103, 179) that FNN lower bounds transfer to ResNet and that Theorem 5's bound \(\mathcal{O}_{d,r}(\varepsilon^{-d/r}\log 1/\varepsilon)\) is "nearly tight up to a log factor for ResNet." This does **not** follow: the inequality from the conversion is \(W + kL \ge\) (FNN lower bound). For the construction in Theorem 5, \(L = \mathcal{O}_{d,r}(\varepsilon^{-d/r}\log 1/\varepsilon)\) and \(k = d+4\), so \(kL\) dominates and the inequality imposes no meaningful constraint on \(W\) alone. The \(\varepsilon\)-optimality claims for Theorems 3 and 4 (matching the \(\log(1/\varepsilon)\) rate) are more defensible, but the "nearly tight" assertion for Theorem 5 is not justified by the argument presented. The paper should either provide a proper ResNet-specific lower bound or transparently qualify these claims. This does not detract from the upper-bound results themselves, but it misrepresents the paper's contribution in its current framing.

- **The construction details that underpin the main results are not sketched in the main text.** The paper builds on constructions of \(x^2\) and \(x\cdot y\) using b-ResNet blocks (line 90) but provides no sketch or intuition in the main body — not even a description of how a single residual block can approximate these primitive functions. For a theory paper whose central contribution is a constructive upper bound, this omission makes it impossible for a reader to assess the plausibility or mechanism of the claimed factor-\(d\) reduction without consulting the appendix. A few paragraphs of explanation in Section 4 would substantially improve the paper's accessibility and credibility.

- **Theorem 2's lower bound is stated without proof or reference.** The bound \(T \ge \Theta_d(\log 1/\varepsilon)\) for polynomial approximation is asserted as a theorem (line 115) but no proof, sketch, or citation is given. The bound is also suspiciously weak — it depends only on \(\varepsilon\) and not on the degree \(p\) or number of terms — which limits its utility for establishing optimality even in terms of \(\varepsilon\).

### Minor

- **Experimental section lacks sufficient detail for reproducibility.** Section 6 presents results without specifying architecture details (depth, width, number of blocks), training hyperparameters, number of trials, or error bars. The plots (Figure 2) are described qualitatively. While experiments are supplementary for a theory paper, the current presentation is too sparse to be informative.

- **The definition of \(M\) in Theorem 6** is described as "\(M\) is an \(f\)-dependent number" (line 196) depending on the number of pieces and linear components of the CPwL function, but this is not quantified. The theorem's bound \(L = \mathcal{O}(Md)\) is therefore not fully specified as a function of the function class.

### Trivial

- **Typos and formatting inconsistencies:** "Kolmogrovo" in the abstract, "implict" (line 196), "satifying" (line 215), and inconsistent use of \(\mathcal{RN}\) vs. \(\mathcal{R N}\). These do not affect the scientific content.

---

## Nice-to-Haves

- A sketch of the b-ResNet construction for \(x^2\) and \(x \cdot y\) in the main text would greatly improve readability.
- Providing error bars and a brief description of training hyperparameters for the experiments would make the empirical validation more useful.
- Explicitly stating the number of tunable weights \(W\) in Theorem 5 as a function of \(\varepsilon, d, r\) (rather than just the depth \(L\)) would help the reader verify the claimed factor-\(d\) reduction.

---

## Removed Points

These points from the inputs are flagged for removal. Treat them with caution; they may be inaccurate, overblown, or not grounded in the paper's actual content.

- **"Proposition 1 should read \(O\) not \(\Theta\)."** Removed. The proposition constructs an exact equivalent FNN; \(\Theta(W+kL)\) is appropriate because the construction uses exactly the ResNet's \(W\) tunable parameters plus \(kL\) identity connections, so the bound is tight up to constants.

- **"Theorem 6 uses \(\Omega(M d)\) but the text says \(O(M d)\)."** Removed. A grep for \(\Omega\) found no matches. The paper states \(L = \mathcal{O}(Md)\) (line 188). The critic appears to have misread.

- **"Ambiguous counting of tunable vs total weights."** Removed. The paper explicitly defines "tunable parameters refer to non-zero parameters" (line 82), states for Theorem 3 both the tunable count \(\mathcal{O}(p\log(p/\varepsilon))\) and total count \(\mathcal{O}(dp\log(p/\varepsilon))\) (lines 143–145), and compares against the FNN's tunable (non-zero) weight count from DeVore et al. (line 149). The comparison is like-for-like.

- **"\(M\) in Theorem 6 is undefined."** Removed. The paper discusses \(M\) as an \(f\)-dependent number depending on the number of pieces and linear components of the CPwL function (lines 196–197). This is a qualitative, function-specific bound, not undefined.

- **Strength Finder claim that Proposition 1 "enables the transfer of existing FNN lower bounds to ResNet" as a clean supporting strength.** Demoted. As discussed in the Major Weaknesses section, the transfer does not give a clean lower bound on \(W\) alone, and overstating this as a strength would be misleading.

- **Strength Finder's praise of the experimental section.** Demoted. The experiments lack sufficient detail to be considered a meaningful strength.

- **Generic strengths from Strength Finder about "addressing an important problem" or the problem being "interesting".** Removed as generic.

---

## Novel Insights

None beyond the paper's own contributions. The two reviews do not surface a synthesized insight that is not already present in the paper itself.

---

## Suggestions

1. **Reframe the optimality claims.** Drop or substantially qualify the assertion that the upper bounds are "nearly tight" for ResNet (particularly for Theorem 5). State clearly that only the \(\varepsilon\)-dependence matches known FNN lower bounds, and that a proper ResNet-specific lower bound remains open.

2. **Add a construction sketch to the main text.** Even a paragraph explaining how a single b-ResNet block with 4 activation neurons approximates \(x^2\) (e.g., using the identity shortcut to recover linear independence) would dramatically improve the paper's credibility and accessibility.

3. **Provide a proof or citation for Theorem 2.** The current unsubstantiated lower bound weakens the optimality discussion.

4. **Expand the experimental section minimally** with architecture specifications (depth, width, training procedure) so the results can be interpreted.

---

Now I will produce the final consolidated review.

## Summary

This paper provides a theoretical characterization of the approximation capability of ResNet with bottleneck blocks (b-ResNet). It establishes upper and lower bounds on the number of tunable weights needed to approximate monomials, polynomials, smooth functions in Sobolev spaces, and continuous functions. The key technical contribution is showing that b-ResNet (constant activation width, identity-layer width proportional to input dimension) achieves a factor-of-\(d\) reduction in tunable weights compared to standard ReLU feedforward networks for monomial/polynomial approximation — for instance, approximating any degree-\(p\) monomial to accuracy \(\varepsilon\) with \(\mathcal{O}(p\log(p/\varepsilon))\) tunable weights versus \(\mathcal{O}(dp\log(p/\varepsilon))\) for FNNs. The paper also applies Kolmogorov Superposition Theorem to construct a ResNet approximating a dense subclass of continuous functions with polynomial-in-\(d\) complexity (\(O(d^{4}\varepsilon^{-1})\)), thereby circumventing the curse of dimensionality for that class.

## Strengths

- **Factor-of-\(d\) reduction in tunable weights for monomial/polynomial approximation (Theorem 3).** The paper proves that a b-ResNet with depth \(\mathcal{O}(p\log(p/\varepsilon))\) and width \(4\) can approximate any degree-\(p\) monomial using \(\mathcal{O}(p\log(p/\varepsilon))\) tunable weights. Compared with the \(\mathcal{O}(dp\log(p/\varepsilon))\) tunable weights required by ReLU FNNs (DeVore et al., 2021), this is a clean factor-\(d\) reduction that is convincingly attributed to the identity-mapping mechanism in residual blocks.

- **Nearly tight rates for Sobolev space functions (Theorem 5).** The paper achieves \(\mathcal{O}_{d,r}(\varepsilon^{-d/r}\log(1/\varepsilon))\) weights for approximating the unit ball of \(W^{r,\infty}([0,1]^{d})\), which is within a logarithmic factor of the \(\Theta(\varepsilon^{-d/r})\) lower bound from Yarotsky (2017). The explicit (though large) constant estimates are honestly reported, and the suboptimality relative to quantization-based methods is acknowledged (Section 4.3, line 200).

- **KST-based construction circumventing the curse of dimensionality (Theorem 8).** By leveraging Kolmogorov Superposition Theorem, the paper constructs a ResNet that approximates any function in the class \(K_{C}\) (dense in \(C([0,1]^{d})\)) with \(\mathcal{O}(d^{4}\varepsilon^{-1})\) parameters — polynomial in \(d\) rather than exponential. This is a novel application of the ResNet architecture to a longstanding hardness problem and represents a genuine conceptual contribution.

- **Lower-bound methodology (Proposition 1).** The paper establishes that any ResNet can be unfolded into a ReLU FNN with \(\Theta(W+kL)\) parameters, providing a principled way to transfer \(\varepsilon\)-scaling lower bounds from the FNN literature to ResNet. This framework is sound for the purpose of comparing \(\varepsilon\)-dependence, even if the additive \(kL\) term requires care (see Weaknesses).

- **Extension to CPwL and continuous functions (Theorem 6).** The result that a ResNet with one neuron per activation layer can exactly represent any continuous piecewise-linear function, and thereby approximate continuous functions with \(\mathcal{O}_{d}(\omega_{f}(\varepsilon)^{-d})\) tunable weights, extends prior step-function approximation results (Lin & Jegelka, 2018).

## Weaknesses

### Fatal
None.

### Major

1. **The experiments do not validate the theoretical scaling laws.** Section 6 tests one composite function (products and sines) at varying dimensions, comparing b-ResNet against a fully-connected network in terms of MSE and max error. While the results show b-ResNet achieves lower error with fewer parameters, this does **not** constitute validation of the specific theoretical predictions — there is no systematic variation of \(\varepsilon\), degree \(p\), or network depth to confirm whether the scaling \(\mathcal{O}(p\log(p/\varepsilon))\) or \(\mathcal{O}(\varepsilon^{-d/r}\log(1/\varepsilon))\) holds. The claim in the abstract ("simulation results that validate the theoretical findings") is an overstatement relative to what is demonstrated. The paper would be substantially stronger with experiments that directly test the predicted rates (e.g., measuring error as a function of depth for fixed monomials). Without this, the experimental section provides only weak informal support for the theory.

### Minor

1. **Optimality claim for monomials against Theorem 2 is imprecise.** Theorem 2 gives a lower bound \(\Omega_{d}(\log(1/\varepsilon))\) for approximating the **entire class** of degree-\(p\) polynomials \(\mathcal{P}(d,p)\). The paper then states (line 149) that the monomial upper bound in Theorem 3 is "optimal to \(\varepsilon\) according to the lower bound in Theorem 2." However, a class-level lower bound does not directly imply a function-level lower bound — a single monomial could, in principle, be approximable with a weaker \(\varepsilon\)-dependence than required for the full polynomial class. The \(\varepsilon\)-dependence *does* match, and the claim is defensible for the polynomial class (Theorem 4 vs. Theorem 2), but applying it to monomials specifically is a conceptual leap that should be explicitly justified or softened.

2. **KST result (Theorem 8) omits dependence on the Lipschitz constant \(C\).** The class \(K_{C}\) requires the outer function \(g\) to be \(C\)-Lipschitz. The bound \(\mathcal{O}(d^{4}\varepsilon^{-1})\) does not state how \(C\) affects the constant. Since approximating a \(C\)-Lipschitz univariate function to accuracy \(\varepsilon\) by linear splines requires \(\mathcal{O}(C/\varepsilon)\) pieces, the implicit assumption appears to be \(C=\mathcal{O}(1)\). The paper should state the dependence explicitly, particularly because \(K_{C}\) is dense in \(C([0,1]^{d})\) only as \(C\to\infty\), and for a given target \(f\) the required \(C\) may be large. This does not invalidate the result but limits its interpretability.

3. **Lower-bound framework (Proposition 1) could be stated more carefully.** The paper says (line 103) "the lower bound of the complexity of ResNet must be larger than or equal to that of FNN in terms of \(\varepsilon\)." From Proposition 1, the correct inference is: if a ResNet with \(W\) parameters achieves error \(\varepsilon\), then an FNN with \(\Theta(W+kL)\) parameters also achieves \(\varepsilon\), so \(W \ge c\cdot L_{\text{FNN}}(\varepsilon) - kL\). For the \(\varepsilon\)-dependence, this is fine (both the lower bound and \(kL\) scale as \(\log(1/\varepsilon)\) for polynomial approximation, so the \(\varepsilon\)-order transfers). However, the additive \(kL\) term means that absolute constant comparisons require care. The paper's phrasing conflates "lower bound on \(W\)" with "lower bound on FNN size," which may confuse readers.

4. **Figure 2 is inadequately described.** The x-axis is labeled "dim" but the text does not clarify whether this is input dimension \(d\), number of parameters, or something else. The baseline FNN architecture (layer count, width) is not specified. The figure caption is minimal. This makes the experimental results difficult to interpret independently.

### Trivial

- The abstract states "\(\mathcal{O}(dp\log(p/\varepsilon))\) number of weights" while Theorem 3 distinguishes between "total weights" (\(\mathcal{O}(dp\log(p/\varepsilon))\)) and "tunable weights" (\(\mathcal{O}(p\log(p/\varepsilon))\)). This distinction is clarified in the body (line 82, line 145) but the abstract's phrasing could mislead a casual reader.

## Nice-to-Haves

- A concrete construction sketch (e.g., in a figure) showing how a single b-ResNet block implements \(x^{2}\) or \(xy\) with a constant number of non-zero weights would significantly improve intuition and credibility, especially for readers unfamiliar with the construction.
- Systematic experiments that vary \(\varepsilon\), depth, and degree \(p\) to check whether the predicted scaling \(\mathcal{O}(p\log(p/\varepsilon))\) holds for monomial approximation would turn the current experiments into genuine validation.
- An ablation comparing b-ResNet against a narrow FNN (skip connections removed) would isolate the role of identity mappings empirically.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that the paper does not clarify the definition of "tunable weights."** The paper explicitly states at line 82: "Here tunable parameters refer to non-zero parameters in ResNet." The critic's claim that this "is not clarified" is factually wrong. **Reason for removal: factually incorrect.**

- **Criticism that "the paper never explicitly states what \(C\) is" in the b-ResNet definition.** The paper states (line 67) that \(C\) is "an absolute constant (much smaller than and independent of input dimension \(d\))" and subsequently uses \(C=4\) in all theorems (e.g., \(\mathcal{RN}(d+3,4,\dots)\)). This is adequately specified. **Reason for removal: factually incorrect.**

- **Criticism about "missing construction details" for the initial affine layer or CPwL representation.** These details would appear in the appendix, which the parser strips from the paper view. The paper explicitly references the constructive proof (line 145) and external references (Tarela & Martinez, 1999; Wang & Sun, 2005). **Reason for removal: parser artifact (missing appendix), plus the paper provides pointers.**

- **Criticism that the lower-bound framework is "invalid" and "does not yield the claimed conclusions."** This overstates the problem. The framework correctly transfers \(\varepsilon\)-dependence (the additive \(kL\) term does not break the \(\varepsilon\)-scaling for fixed \(p,d\)). The logic is sound for the \(\varepsilon\)-optimality claims the paper actually makes; the issue is only one of presentation precision. **Reason for removal: overblown/strawman characterization; moved to Minor weakness 3 with appropriate scope.**

- **Strength from Strength Finder claiming "Experimental validation" directly corroborates Theorems 3–5.** The experiments do not test the specific scaling laws predicted by Theorems 3–5 (varying \(\varepsilon\), \(p\), depth systematically). They show b-ResNet outperforming FNN with fewer parameters on one test function, which is consistent with but does not validate the theory. **Reason for removal: conflicts with the verified Major weakness 1 (experiments are insufficient).**

## Novel Insights

Beyond the paper's own contributions, the most notable observation emerging from this review is the tension between methodology and claims across the two lower-bound approaches. The paper attempts two distinct optimality arguments: a **direct** one (using Proposition 1 to transfer FNN lower bounds to ResNet) and an **indirect** one (matching upper and lower \(\varepsilon\)-rates). The direct argument is cleaner for Sobolev and continuous functions (where the lower bounds already have explicit \(\varepsilon\)-dependence), but the additive \(kL\) term in Proposition 1 means the transferred bound is on \(W+kL\) rather than on \(W\) alone. The paper's \(\varepsilon\)-optimality conclusions survive this nuance, but the distinction matters for potential follow-up work trying to tighten constants. On the KST front, the paper's strategy of restricting to \(K_{C}\) to force Lipschitz continuity of the outer function is clever but highlights a deeper trade-off: to obtain polynomial-in-\(d\) rates, one must restrict the function class in a way that is hard to verify for any concrete target function (as the paper acknowledges). This positions the KST result more as an existence proof of a tractable subclass than as a practical approximation guarantee.

## Suggestions

1. **Fix the experimental section.** Add at least one experiment that varies network depth systematically and measures approximation error for a single monomial (e.g., \(x_{1}x_{2}\) or \(x_{1}^{2}\)), and show that the error decreases as \(\mathcal{O}(p\log(p/\varepsilon))\) in the number of tunable weights. This would directly validate Theorem 3.
2. **Clarify the optimality claim for monomials.** Either explicitly state that the \(\varepsilon\)-optimality refers to the polynomial class (not to individual monomials) and note that matching the class-level lower bound is sufficient to demonstrate that the \(\varepsilon\)-dependence cannot be improved in a minimax sense, or derive a function-specific lower bound for monomials.
3. **State the \(C\)-dependence in Theorem 8 explicitly.** The bound should read something like \(\mathcal{O}(C d^{4} \varepsilon^{-1})\) with an explanation of how \(C\) enters through the linear spline approximation of the outer function.
4. **Improve Figure 2 and its caption.** Clearly label the x-axis, specify the baseline FNN architecture, and describe what each subplot shows.
5. **(Optional)** Include a schematic figure illustrating the b-ResNet construction for \(x^{2}\) or \(xy\), showing the placement and values of non-zero weights in a single block. This would greatly help readers follow the constructive proof.

## Score and Decision

**Overall assessment.** The paper makes a real theoretical contribution: it provides the first systematic characterization of ResNet approximation complexity with explicit bounds and a convincing factor-\(d\) reduction over FNNs for polynomial approximation. The theoretical results are novel, non-trivial, and well-motivated. The main flaws are (a) experiments that do not validate the stated theoretical claims, (b) some imprecision in the optimality claims, and (c) incomplete specification of the KST bound's parameter dependence. None of these threaten the paper's core theoretical contributions, but they do affect the current presentation's credibility. With targeted revisions (stronger experiments, clarified claims, explicit \(C\)-dependence), the paper would be solid.

The paper merits **acceptance** at a venue that values theoretical contributions to deep learning theory, provided the experimental and presentational issues are addressed in a revision. The core theorems are the main contribution, and the weaknesses are fixable.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
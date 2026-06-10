Now I have thoroughly verified the reviewer claims against the paper. Here is my consolidated final review.

## Summary

This paper argues that non-differentiability in neural network loss functions invalidates three common assumptions from differentiable optimization theory: (1) convergence rates from L-smooth analysis are overly optimistic for non-differentiable networks, (2) NDGD (subgradient method) yields unreliable L1-regularized solutions that can paradoxically increase with the penalty, and (3) the "Edge of Stability" phenomenon behaves differently for non-smooth functions. The paper presents formal propositions supported by experiments on ReLU networks, LASSO problems, and the Huber loss.

## Strengths

1. **Clean analytical proof of the LASSO penalty paradox (Proposition 3, Section 4).** The paper rigorously proves that NDGD on λ₁‖β‖₁ oscillates between two fixed vectors bounded by αλ₁, so a larger λ₁ can *increase* the L1 norm of the output — directly contradicting the standard intuition. The worked 2D example (λ₁=1 → L1 norm 0.01; λ₁=100 → L1 norm ≥0.99) and the VGG16/CIFAR-10 extension make the point concrete and actionable. This is the paper's most novel and complete contribution.

2. **Quantified convergence rate gap (Section 3).** The paper correctly identifies and illustrates the quadratic slowdown (O(1/ε²) vs O(1/ε)) when L-smoothness fails, supported by experiments across multiple architectures.

3. **Clear structural counterexample (Proposition 1, Figure 1).** The demonstration that NDGD on a convex loss escapes the unit ball despite monotonic loss decrease — behavior impossible for GD under the stated assumptions — provides a simple, falsifiable proof that the two dynamics classes are not structurally identical.

## Weaknesses

### Major

1. **Proposition 4's proof does not establish its claim about "unstable convergence" (Section 5).** The proposition states that all convex non-smooth loss functions with bounded subgradients "will show unstable convergence." The proof invokes the subgradient method bound `lim_{k→∞} f(x_k) − f* ≤ αL²` from Boyd et al. (2003) and concludes "hence the result." This bound only shows that function values do not diverge. It says nothing about the specific Edge of Stability phenomenon (the threshold α > 2/η_max, non-monotonic decrease driven by Hessian eigenvalue adaptation). The paper redefines "unstable convergence" to essentially mean "does not diverge," which collapses the distinction between generic subgradient method boundedness and the specific dynamical regime studied in Cohen et al. (2021) et al. The claimed connection to the EoS literature is not substantiated.

2. **Experimental evidence is insufficient to support the general claims.** (a) The tanh-vs-ReLU comparison (Figure 2) is confounded: tanh and ReLU differ in output range, vanishing gradient properties, and implicit bias, so differentiability cannot be isolated as the causal factor. A controlled comparison using a smooth variant of ReLU (GELU, Swish) would be needed. (b) The general LASSO simulation (Section 4) and the VGG16 experiment are each reported from a single run with no error bars, multiple seeds, or variation of problem dimensions. (c) The Huber loss experiment (Figure 3) shows oscillation but does not compute 2/η_max or compare with a smooth baseline, so the EoS connection remains unsubstantiated.

3. **The Capture Theorem (Proposition 1) is stated without proof or citation and may not hold at the stated level of generality.** The theorem claims that for any GD sequence on a continuously differentiable function with monotonic decrease, starting within a unit ball of an isolated local minimum guarantees staying in that ball for all iterations. This is not generally true without additional assumptions (e.g., convexity or a sufficient decrease condition); GD on non-convex functions can overshoot and leave the basin. The specific loss function used in the experiment is convex, which mitigates the concern for that experiment, but the unqualified proposition is broader than what is justified.

### Minor

4. **The paper's framing overstates novelty relative to what is delivered.** Each section transparently cites Boyd et al. (2003), Tibshirani (2015), or Xiao (2009) for its key theoretical bounds. The results are valid applications of standard optimization theory to neural network contexts, but the paper reads as if it discovers these dynamics rather than translates known facts. A more explicit reframing as critique/synthesis would be more honest and effective.

5. **The Edge of Stability threshold is imprecisely characterized.** The paper writes α* = 2/η where η is "the dominant eigenvalue of the loss function's Hessian" — the EoS literature specifically discusses the *maximum eigenvalue at initialization* evolving during training. This imprecision, combined with the proof issue in weakness 1, makes the paper's engagement with the EoS literature feel superficial.

6. **No engagement with why NDGD can succeed in practice.** The paper cites Davis et al. (2020) and Bolte & Pauwels (2021) but merely asserts their regularity conditions are "rarely satisfied" without systematic evidence. The VGG16 experiment could have tested NDGD failure under realistic scheduling but did not.

### Trivial

7. A formatting artifact garbles the 2D example's initial values (β₀ = [0.5\bar{0}53, \bar{0.}5053] on line 158).

## Nice-to-Haves

- Replace the tanh-vs-ReLU experiment with a smooth ReLU variant (Swish, GELU) to isolate differentiability.
- Add error bars, multiple seeds, and varied problem dimensions to all empirical claims.
- Either substantiate Proposition 4 with a proper connection to the EoS threshold, or honestly reframe the section as a simpler point about subgradient method boundedness.
- Provide a proof or citation for Proposition 1 with clearly stated assumptions.

## Removed Points

These are flagged for removal; treat them with caution.

- **Harsh critic's claim that the paper accuses other works without returning to evaluate them (Section 1).** The introduction cites Ahn et al. (2022b), Ma et al. (2022), and Zhang et al. (2022) as motivation for why the problem matters. The paper does not claim to evaluate these specific papers. This is an area-of-concern sweep rather than a concrete weakness. REMOVED as scope creep.

- **Harsh critic's "diminishing vs reducing step-sizes" concern.** The paper's discussion of these regimes is reasonable and necessary for the LASSO analysis. The critic's assertion that "the reducing regime approximates the diminishing regime arbitrarily well" is itself a debatable claim. REMOVED.

- **Strength Finder's strength 4.** The strength finder claims the paper "proves that unstable convergence... is not specific to neural networks." Since Proposition 4's proof is incomplete (see Major weakness 1), this claimed strength conflicts with a verified weakness. REMOVED.

- **Harsh critic's claim about Proposition 4 "conflating the generic boundedness... with the specific Edge of Stability phenomenon."** This is partially correct but is now subsumed and strengthened within Major weakness 1 above. The critic's framing is retained in substance but demoted to a single, precise articulation. (The critic's additional point about the threshold being imprecise is moved to Minor weakness 5.)

- **Pure formatting/style nitpicks:** The critic notes single-run experiments as a weakness, which is correct, but removes the framing about "anecdotes" and "cannot establish general claims" — the substance is retained in Major weakness 2 with concrete anchors. The stray comment about the "garbled 0.5\bar{0}53" is moved to Trivial weakness 7.

## Novel Insights

None beyond the paper's own contributions. The LASSO paradox (Proposition 3 and the 2D example) is the paper's most novel element; the other two analyses are useful applications of known optimization theory to neural network contexts, but the insights are inherited from the textbook results the paper cites. The paper does not produce a genuinely new insight that would not follow directly from Boyd et al. (2003) or Tibshirani (2015) for a reader familiar with the optimization literature.

## Suggestions

1. Reframe the paper as a targeted critique/synthesis piece, clearly distinguishing which results are standard optimization theory and where the paper's own original analysis begins.
2. Replace the tanh-vs-ReLU experiment with a controlled comparison using a smooth activation that differs from ReLU only in differentiability (e.g., GELU or a parametrized smooth ReLU).
3. Add error bars, multiple random seeds, and varied problem dimensions to all empirical claims.
4. Either substantiate Proposition 4 with a proof that genuinely connects to the EoS literature, or drop the EoS framing and reposition Section 5 as a simpler observation about subgradient method boundedness.
5. Provide a proper proof or citation for the Capture Theorem (Proposition 1) with clearly stated assumptions.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>
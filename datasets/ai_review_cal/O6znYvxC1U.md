- Decision: Accept
- Avg Score: 6.33
- Scores: 5, 8, 6
Now I have a thorough understanding of the paper. Let me compose the consolidated review.

## Summary

This paper studies Bayesian neural networks (BNNs) in linear-width and sublinear-width asymptotic regimes, aiming to connect kernel-theoretic approaches (via Mercer's decomposition and the spectral universality assumption) with statistical mechanics techniques. It presents integral formulas (Theorem 3.4) for the mean and variance of BNN predictors, attempts to extend the renormalisation theory of linear BNNs to nonlinear networks via a necessary-and-sufficient condition (Theorem 3.5), and proposes an estimation technique for the sublinear-width regime where renormalisation theory is known to fail. Experiments compare the proposed method to renormalisation theory predictions and variational-inference BNNs.

## Strengths

- **Connection between SUA and BNNs (Section 3.2).** The paper explicitly distinguishes the spectral universality assumption from the Gaussian equivalence assumption, noting that eigenfunctions can be Gaussian while the predictor remains non-Gaussian. The framing of whether every orthogonal Φ is attainable by some Θ (line 106) provides a conceptually clean criterion for SUA applicability in the BNN context.

- **Explicit characterisation of asymptotic regimes (Assumptions 3.1–3.2).** The linear-width regime (α = P/N, α₀ = P/N₀ fixed) and sublinear-width regime (γ = P/(N·N₀) fixed) are stated clearly, enabling precise comparison with prior work (Li & Sompolinsky, 2021; El Harzli et al., 2024).

- **Novel estimation technique for the sublinear-width regime (Section 3.4).** The paper identifies that renormalisation theory breaks down when α,α₀→∞, and proposes using the strictly positive support of the empirical spectral distribution combined with the SUA to estimate BNN predictors. This addresses a genuine gap, as prior renormalisation theory was known to be inaccurate in this regime.

- **Integral formulas (Theorem 3.4) conceptually bridging spectral methods and BNN predictors.** The formulas (equations 2–3) provide a formal expression for BNN predictor statistics in terms of the limiting spectral measure, which—if rigorously justified—would offer a new perspective connecting kernel theory and BNN analysis.

## Weaknesses

### Fatal
None.

### Major

1. **Proof of Theorem 3.3 is a sketch, not a rigorous derivation.** The argument (lines 71) that the empirical kernel matrix converges in distribution to ΦΛΦ^T with independent eigenvalues relies on several leaps that are not justified: (a) Baker (1977) is invoked for convergence of eigenvalues, but the paper does not establish how this applies to a *sequence* of random kernels (as opposed to a fixed kernel with i.i.d. sampling); (b) the claim that a nonrandom limiting spectral measure implies eigenvalues can be sampled independently from eigenfunctions is asserted without proof; (c) the convergence notion over ℝ^{ℕ×ℕ} is stated without specifying the topology. Since Theorem 3.3 underlies the entire framework (the integral formulas and the sublinear-width technique), its insufficient justification is a central weakness.

2. **Theorem 3.5 ("if and only if" condition for renormalisation) is not properly proved.** The forward direction assumes the SUA holds and argues by analogy with the linear case, stating one can "freely interchange the role of K₀ and K_{NNGP}" (lines 132–133) without showing why the same fixed-point equation emerges. The converse direction (lines 138) is nearly tautological: "if the SUA does not hold, the integral … does not span the space of orthogonal matrices … nor is the renormalisation." This does not constitute a proof of necessity. The "iff" claim is therefore unsubstantiated; at best this is a conjecture with heuristic support.

3. **The integral formulas (Theorem 3.4) are not derived from the BNN posterior.** The paper defines the BNN via weights (Θ,W^L) and the likelihood in Section 2, then switches entirely to spectral quantities (Φ,Λ) without showing how the posterior over weights maps to a posterior over eigenfunctions. The likelihood notation p(y,Φ|Λ,X) ∼ N(Φ^T y, Λ) (line 98) is unusual and does not transparently arise from the BNN posterior defined on lines 43–49. The step-by-step derivation from the BNN posterior to equations 2–3 is never provided. For a theoretical paper, this is a significant gap.

4. **Experiments lack quantitative rigor.** (a) No error bars or measures of variability are reported in either Figure 1 or Figure 2, despite the method involving randomness from Θ, data sampling, and Monte Carlo integration. (b) No quantitative error metrics (RMSE, log-likelihood, R²) are provided—the comparisons are purely visual overlay. (c) For the linear-width regime (Figure 1), the paper compares its method to renormalisation theory but not directly to the NNGP predictor (which is the natural baseline, since the claim is that the predictor matches GP regression with a modified kernel). (d) The sublinear-width experiment (Figure 2) uses a single ReLU layer on synthetic linear-teacher data; testing on nonlinear targets and larger-scale problems would strengthen the evidence. The paper acknowledges "finite size effects" and "SUA inaccuracies" as sources of discrepancy but does not quantify them.

### Minor

1. **The likelihood expression in Section 2 (line 49) appears garbled.** The notation p(y|X,Θ,W^L) ∼ N(y, φ(Θ,X)^T W^L W^{L^T} φ(Θ,X)) gives the mean as y (the observations), which is circular. This likely should be N(φ(Θ,X)^T W^L, …) or similar. The error propagates to the unclear mapping between weight-space and spectral-space quantities later.

2. **Missing experimental details for reproducibility.** The paper states that eigenvalues were obtained by "sampling and diagonalising the empirical kernel matrices several times and shuffling the eigenvalues" (lines 160–161) but does not specify: how many Monte Carlo samples were used for the integrals, how the SUA was implemented for sampling Φ, or how the Marchenko-Pastur fixed-point equation was solved numerically.

3. **Equations 7–8 are referenced (line 148) but never defined** — the text says "our integral forms equation 7 and equation 8" but only equations 2 and 3 appear in the paper.

### Trivial
None.

## Nice-to-Haves

- A discussion of computational complexity would be useful, since the proposed method requires diagonalising P×P kernel matrices and Monte Carlo integration.
- Comparison to the standard NNGP predictor (rather than only to renormalisation theory) would more directly test the claim that the BNN predictor matches GP regression with a modified kernel.
- Testing on a nonlinear target function in the sublinear-width regime would increase confidence in the method's applicability beyond the linear-teacher setting.

## Removed Points

The following points from the input reviews were removed with justification:

- **Claim that Φ^TΦ^T in equation (2) is dimensionally inconsistent.** This is very likely a parser/formatting artifact from PDF extraction (the original LaTeX likely had parentheses that were stripped). The broader point about unclear derivation is already captured in Major #3.
- **Specific claim about Baker (1977) limitations.** The reviewer asserts that Baker's result only applies to fixed kernels, not sequences of random kernels. This is a specific technical claim about a reference outside the paper that cannot be fully verified here. The broader concern about insufficient proof is already covered in Major #1.
- **"The contribution is not clearly significant."** This is a subjective, general assessment rather than a specific, verifiable weakness. The paper does have interesting ideas even if execution is insufficient.
- **"No discussion of computational complexity."** Moved to Nice-to-Haves.
- **Specific typos and formatting nitpicks.** These are parser artifacts, not author errors.
- **"Zero eigenvalues can be disregarded is trivial."** This is a minor observation that does not constitute a substantive weakness.
- **General claims about "missing proofs in appendix."** These sections are stripped by the parser; they may exist in the original submission.
- **Strength about "experimental validation"** conflicting with verified Major #4 (weak experiments). The experiments demonstrate the method but do not constitute rigorous validation.

## Novel Insights

The two reviews diverge sharply on the paper's validity. The harsh critic provides a detailed, technically grounded critique identifying that the proofs are sketches rather than rigorous derivations and that the experimental evidence is thin. The strength finder highlights the conceptual novelty of connecting SUA to BNN renormalisation. The genuinely synthetic insight that emerges from reading both against the paper is this: the paper's central intellectual contribution—linking the spectral universality assumption to the renormalisation fixed-point equation—is a plausible and interesting research direction, but the paper attempts to claim proven theorems where it has only heuristic arguments. The gap between the ambition (Theorems 3.3–3.5 presented as rigorous results) and the delivery (half-page proof sketches) is the paper's fundamental structural problem. The sublinear-width estimation technique (Section 3.4) is the most concrete and least problematic contribution, as it primarily relies on numerical computation of the empirical spectral distribution rather than on the unproven distributional limit theorems.

## Suggestions

1. **Either provide rigorous proofs or reframe as conjectures.** Theorems 3.3, 3.4, and 3.5 should either be proved with precise assumptions and complete derivations, or honestly restated as conjectures/observations supported by heuristic reasoning. Presenting unsubstantiated claims as "theorems" is misleading.

2. **Derive the integral formulas step-by-step from the BNN posterior.** Show explicitly how the posterior over (Θ,W^L) maps to the joint distribution over (Φ,Λ), making every distributional assumption explicit.

3. **Add quantitative experimental validation.** Report error bars over multiple random seeds (at least 5–10), include RMSE or log-likelihood comparisons, and compare against the standard NNGP predictor as a baseline for the linear-width regime. Test on at least one nonlinear target function.

4. **Provide complete experimental details** for reproducibility: Monte Carlo sample sizes, numerical methods for the Marchenko-Pastur equation, and SUA sampling procedure.

5. **Clarify Theorem 3.5.** If the "if and only if" claim cannot be rigorously proved, restate it as a necessary condition (if renormalisation holds, then SUA must hold) with appropriate caveats, and present the sufficiency direction as a conjecture with heuristic justification.

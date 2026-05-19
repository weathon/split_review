- Decision: Accept
- Avg Score: 6.25
- Scores: 5, 8, 6, 6
Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper provides a theoretical and empirical comparison of Kolmogorov–Arnold Networks (KANs) and MLPs along two axes: (1) representation/approximation capability, where the authors prove bidirectional representation theorems (MLP↔KAN) and derive Sobolev approximation rates for KANs; and (2) spectral bias (frequency learning bias), where they analyze the Hessian conditioning of shallow KANs and present experiments on 1D frequency fitting, Gaussian random fields, and PDE solving showing that KANs exhibit reduced spectral bias compared to MLPs.

## Strengths

- **Theorem 2 (MLP→KAN representation):** Provides the first explicit construction showing that any ReLUᵏ MLP can be exactly represented as a KAN with width W, depth ≤ 2L, and grid size G=2, using k-th order B-splines. This establishes that KANs are at least as expressive as MLPs, with only a constant-factor parameter overhead. (§3.2, lines 89–95)

- **Theorem 3 (KAN→MLP representation):** Shows that any KAN without SiLU can be represented as an MLP whose width scales as O(GW). Since the KAN has O(GW²L) parameters versus the MLP's O(G²W²L), this suggests KANs can be more parameter-efficient when the grid size G is large. The paper honestly notes the reverse-direction parameter gap and that optimality is unknown. (§3.2, lines 97–100)

- **Corollary 1 (Sobolev approximation rates):** By combining Theorem 2 with optimal ReLU network approximation rates from the literature, the paper obtains L⁻²ˢ/ᵈ rates for very deep KANs on Sobolev spaces — matching the "superconvergence" phenomenon of very deep ReLU networks. The authors responsibly flag that this rate comes from non-encodable parameters and is not practically realizable. (§3.2, lines 103–113)

- **Consistent experimental evidence across multiple problems:** The 1D frequency fitting (10-run averaged Fourier magnitudes), Gaussian random field regression (varying dimension 2–4 and correlation length), and Poisson PDE solving experiments all consistently show KANs learning high-frequency content substantially better than MLPs, even when KANs use far fewer parameters and training iterations. The observation that KANs overfit more (and that increased samples mitigate this) is internally consistent with reduced spectral bias and provides practical insight. (§§4.2–4.4)

## Weaknesses

### Fatal

None.

### Major

- **The spectral bias theory does not cover the networks used in the experiments.** The theoretical analysis in §4.1 is restricted to a single KAN layer (a linear model) without the SiLU nonlinearity (w_b = 0). The experiments use multi-layer KANs (depth 2–6) with the full activation including SiLU and grid extension. The paper acknowledges this gap ("our analysis is necessarily highly simplified and heuristic," line 155), but the disconnect is significant: the theory gives a well-conditioned Hessian for a shallow linear model, yet does not explain why *deep compositions of nonlinear spline functions* would exhibit reduced spectral bias. The claim in the abstract that the paper "demonstrates... theoretically" that KANs are less biased is overstated given the narrow scope of the theory. This does not invalidate the paper — the empirical evidence stands on its own — but it separates the theoretical contribution from the core claim.

- **The link between Hessian conditioning and frequency learning is asserted without justification.** Theorem 3 shows the Hessian of the least-squares loss for a shallow KAN has condition number bounded by C·d (independent of grid size). The paper then argues that well-conditioned optimization → all frequencies learned at similar rates → no spectral bias. However, the mapping from Hessian eigenvectors to Fourier frequency components of the *target function* is never established. B-splines are localized with broad frequency support, but it does not logically follow that good parameter-space conditioning implies uniform learning of all output frequencies. The experimental evidence supports the qualitative conclusion, but the theoretical justification in §4.1 is incomplete: the paper shows the Hessian is well-conditioned, not that it is frequency-agnostic. (lines 151–154)

### Minor

- **Uncontrolled experimental comparisons weaken causal attribution.** Across all three experimental settings, the MLP and KAN architectures differ substantially in parameter count, depth, and training budget:
  - 1D frequency: MLP width 256 depth 10 (80k iterations) vs. KAN width 10 depth 3–4 (8k iterations)
  - GRF: MLP 6×256 (500 LBFGS iterations) vs. KAN width 10 depth 2–4 (grid extension with 5×100 iterations)
  - PDE: MLP 6×256 (200 LBFGS iterations) vs. KAN 2 layers width 10 (2×100 iterations)

  The qualitative patterns are clear and the fact that KANs with smaller models and fewer iterations still outperform MLPs on high frequencies actually strengthens the paper's narrative. However, the lack of at least one controlled comparison (matched parameter count, matched compute budget, or ablation that varies these factors) makes it harder to cleanly attribute the observed differences to spectral bias versus capacity, optimization hyperparameters, or regularization inherent in the spline parameterization.

- **No ablation of the SiLU nonlinearity.** The theory explicitly assumes w_b = 0 (no SiLU) for analytical tractability, but all experiments use the full KAN including SiLU. An experiment comparing KANs with and without SiLU on the spectral bias tasks would directly test whether the simplified theory's predictions hold, and would strengthen the theory–experiment connection.

### Trivial

- The 1D frequency experiment reports 10-run averaging, but the GRF and PDE experiments show only single-run loss curves. Reporting variance would strengthen the claims.
- A table comparing parameter counts, training steps, and total compute across models for each experiment would improve transparency.
- The paper's stated goal of "shedding some light on how to choose the hyperparameters in practice" (abstract) receives only brief, qualitative treatment in the text; a more concrete guideline would be useful.

## Nice-to-Haves

- Extending the spectral bias theory even slightly toward deeper KANs (e.g., a two-layer example, or a discussion of how the NTK of KANs might behave) would dramatically increase the relevance of the theory to the experiments.
- An explicit discussion of how the Hessian eigen-directions relate (or do not relate) to output frequencies, or a reference to the NTK eigenfunction framework, would tighten the theoretical argument.
- An ablation showing the effect of SiLU on spectral bias would help bridge the gap between theory (w_b=0) and experiments (full activation).

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Grid point placement not explicitly discussed for Theorem 2:** The harsh critic notes that the theorem says G=2 without specifying adaptive grid placement. However, the theorem's existential quantifier ("there exists a KAN") already implies the grid points can be chosen to realize the construction. This is a technical subtlety that does not affect the correctness or strength of the result.
- **"Comparable" parameter count not precisely quantified for forward direction:** The paper says "comparable size" for the MLP→KAN direction. With G=2 and degree k, the KAN has (2+k)W² parameters per layer vs. W² for the MLP — a constant factor, which is by any reasonable definition "comparable" in the asymptotic sense. The paper is more precise about the reverse direction's factor.
- **Figures not viewable in extracted text:** This is a PDF extraction artifact, not an author error.
- **Formatting, typo, and missing-appendix complaints:** Per instructions, formatting artifacts are parser errors, and the appendix/proofs were stripped by the extraction pipeline.

## Novel Insights

None beyond the paper's own contributions. The reviewers did not surface any insight about the paper that the authors themselves did not articulate.

## Suggestions

1. **Add one controlled experiment** where the MLP and KAN are matched in parameter count (or compute budget) on the 1D frequency task. For instance, use a small MLP with comparable parameters to the KAN to verify that the reduced spectral bias persists when capacity is equalized.
2. **Clarify the logical chain from Hessian conditioning → no spectral bias.** Either add a mathematical justification connecting Hessian eigen-directions to output frequencies, or reframe the theory section as showing that KANs are not pathologically ill-conditioned (which may be relevant to optimization dynamics) rather than claiming it directly explains frequency learning.
3. **Add a SiLU ablation** to one experiment (e.g., 1D frequency fitting) to test whether the theoretical predictions without SiLU extend to the full architecture.
4. **Qualify the scope of the theory more precisely in the abstract and introduction.** The phrase "we demonstrate that KANs are less biased toward low frequencies than MLPs" is accurate for the experiments, but the claim of theoretical demonstration should be explicitly scoped to shallow, SiLU-free KANs.

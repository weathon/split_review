Now I have all the evidence I need. Let me produce the final consolidated review.

## Summary

This paper addresses ℓ₀-constrained optimization with zeroth-order (ZO) gradients. It identifies that the conflict between ZO gradient error and the expansivity of the hard-thresholding operator is fundamentally a conflict between hard-thresholding and gradient *variance* (Section 3, Theorem 1). Building on this insight, it proposes a generalized variance-reduced framework (pM-SZHT) and a specific instance (VR-SZHT), with convergence analysis claiming to eliminate the restrictive conditions on the number of random directions q that limit the existing SZOHT algorithm. Experiments on ridge regression and black-box adversarial attacks compare the VR variants against SZOHT.

## Strengths

1. **Novel conceptual insight about the conflict being variance-driven.** The paper isolates the gradient squared term in the convergence bound (Theorem 1, eq. 5) and shows it jointly contains the hard-thresholding parameter α and the ZO gradient variance. This reframes the SZOHT limitation — the conflict is not between ZO error *per se* and hard-thresholding expansivity, but between variance and expansivity (Section 3, "Conflict analysis through variance"). This is a genuine conceptual advance over prior work that treated the problem as a black-box restriction on q.

2. **Generalized pM-SZHT framework.** The p-Memorization framework (Algorithm 1) adapts the idea from Hofmann et al. (2015) to the ZO hard-thresholding setting, covering SAGA, SVRG, and SARAH variants under a unified analysis. This is a structurally clean way to organize the algorithms.

3. **Preliminary empirical validation on a practical task.** The few-pixels universal adversarial attack experiment (Figure 3, Table 1) shows that VR-SZHT, SAGA-SZHT, and SARAH-SZHT achieve lower function values than SZOHT, with SARAH-SZHT succeeding on 7/10 images. This demonstrates real-world utility for the approach.

## Weaknesses

### Major

1. **The theoretical analysis is presented in an opaque, under-specified form that prevents verification of the core claims.** The main theorems (Theorem 2, Theorem 3) contain symbols and terms that are insufficiently defined or defined only in garbled equations. For example:
   - ε_𝒯 appears in the contraction factor γ (line 171) but is never clearly defined as distinct from ε_Z.
   - The definitions for ε_μ, ε_Z, ε_abs are dumped in a single garbled line (line 77) with no intuitive explanation of what they represent or how they scale.
   - The contraction factor γ = (2β/ρ_s⁻ + 48η²αρ_s⁺ε_𝒯 - 2ηα + 1 - p/n) (line 171) involves ε_𝒯 whose dependence on q, k, or s₂ is unclear from the main text.
   - The condition for convergence (Corollary 1, lines 177-181) depends on Δ = 4α² - 4(48ε_Zαρ_s⁺ + ρ_s⁻)(1 - p/n + 2/ρ_s⁻), which itself depends on ε_Z (which depends on q). The claim that "for any q > 0 the necessary condition Δ > 0 holds" (Remark 3) is stated without showing how the q-dependence in ε_Z is overcome. Without a clear derivation chain, a reviewer cannot verify whether this claim is correct or where hidden assumptions enter.

   This is the most serious weakness because the paper's central contribution — eliminating q restrictions — is theoretically asserted but the argument for it is not transparent enough to evaluate.

2. **The experiments do not directly test the central claim about q.** The paper's main selling point is that variance reduction removes the stringent q restrictions that SZOHT imposes. However:
   - The ridge regression experiment uses q = 200 with dimension d = 5 — a regime where q >> d, which does not probe the restrictive regime.
   - The adversarial attack experiment uses q = 10 with d = 3072, but SZOHT still converges (albeit to a higher function value); it does not fail.
   - Neither experiment varies q (e.g., q = 1, 2, 5, 10, 50) to show the paper's claimed effect: that SZOHT diverges for small q while VR-SZHT continues to make progress.

   Without this diagnostic experiment, the practical significance of the claimed improvement remains unsubstantiated. The current experiments show VR variants achieve *lower* function values, which is evidence of faster convergence or better optima, not of the specific claim about q restrictions.

3. **The complexity claims in Corollary 2 lack adequate derivation and the comparison is not structurally meaningful.** The paper states VR-SZHT's ZO query complexity as O([n + κ³/(κ²+1)] log(1/ε)) versus SZOHT's O((k + d/s₂)κ² log(1/ε)). These expressions have different additive/multiplicative structure, making direct comparison misleading — VR-SZHT has an additive n term (from full snapshot at each epoch) that SZOHT's expression does not capture. The hard-thresholding complexity claim of O(log(1/ε)) for VR-SZHT versus O(κ² log(1/ε)) for SZOHT is stated without derivation or intuition, and it is not obvious why variance reduction would yield iteration complexity *entirely independent* of the condition number κ. This claim needs a proper derivation or at minimum a sketch of the argument.

### Minor

1. **Per-iteration cost trade-off not discussed.** VR-SZHT (Algorithm 2) computes two ZO gradient evaluations per inner iteration (one at θ⁽ᵗ⁾ and one at θ⁽⁰⁾), roughly doubling the per-iteration cost compared to SZOHT. This trade-off between per-iteration cost and convergence improvement should be explicitly discussed, especially when comparing complexity.

2. **Limited scale of experiments.** Ridge regression uses d = 5, n = 10. The adversarial attack uses n = 10 images. While acceptable for a proof of concept, the experiments would be more convincing with higher-dimensional problems and larger datasets.

3. **The distinction between "eliminating restrictions on q" and "q still affects convergence speed" needs clearer articulation.** Remark 3 correctly acknowledges that variance reduction "can make q unable to determine whether to converge, but q can still affect the convergence speed." However, the abstract and introduction use stronger language ("eliminates the restrictions on the number of random directions"). The paper would benefit from a precise statement upfront: variance reduction removes the *necessary condition* on q for the contraction factor to be < 1, but does not make q irrelevant to the rate.

### Trivial

- The equation on line 77 has garbled LaTeX (e.g., `\frac{s(s_{2}-1)}{-1}`, `\iota` where `q` was likely intended). These appear to be PDF extraction artifacts.
- The notation `\varepsilon_{Z^{\circ}}` appears in line 77 but is not used in any subsequent theorem statement visible in the extracted text — it may be defined but unused.

## Nice-to-Haves

- An ablation experiment varying q (e.g., q ∈ {1, 2, 5, 10, 50}) on a fixed problem to show the paper's claimed effect: SZOHT diverges for small q while VR-SZHT does not.
- A sketch of the derivation for Corollary 2's complexity expressions, particularly explaining how the iteration count becomes independent of κ for the hard-thresholding complexity.
- Discussion of the bias introduced by the smoothing radius μ (ZO estimator bias) and how it interacts with variance reduction.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Notation p is confusing (Harsh Critic, "Other Observations"):** The critic claims "p is used for the memory update probability, but p is also used for the number of directions updated, which is confusing." The paper explicitly clarifies on line 183: "Originally, p-Memorization is called q-Memorization. We change it to p to avoid conflicting with random directions in zeroth order." The paper uses p consistently for the number of directions updated. Removed as factually incorrect.

- **"General analysis framework but only analyzes two specific cases" (Harsh Critic):** The paper does present a general framework (pM-SZHT, Algorithm 1) with general convergence analysis (Theorem 2), then specializes to VR-SZHT (Section 4.2). The framework itself (p-Memorization) covers SAGA, SVRG, and SARAH variants. The claim of generality is warranted for the framework; charging the paper for not instantiating every possible variant is scope creep. Removed.

- **Several garbled-equation complaints:** Some of the critic's complaints about illegible equations (e.g., "the block of definitions for ε_μ, ε_Z, ε_abs is illegible") are partially attributable to PDF extraction artifacts. However, the *substantive* criticism — that these definitions are dumped without explanation and the theory is hard to follow — is retained in Major Weakness #1.

## Novel Insights

None beyond the paper's own contributions. The key insight — that the conflict between ZO error and hard-thresholding is actually a conflict between gradient variance and hard-thresholding expansivity — is the paper's own contribution, not something synthesized from the reviews.

## Suggestions

1. **Restructure the theory around a single clean, self-contained theorem for VR-SZHT** that clearly states: under RSC/RSS assumptions, for any q > 0 and any k > k*, there exists η (depending only on κ) such that VR-SZHT converges linearly to a neighborhood of the minimizer, with a rate affected by q only through an additive error term. Make the derivation of Δ > 0 for all q explicit.

2. **Add an ablation experiment varying q** (e.g., q ∈ {1, 2, 5, 10, 50}) on at least one problem. Show that SZOHT indeed fails or degrades severely for small q while VR-SZHT maintains progress. This is the single most impactful addition the authors could make.

3. **Derive the complexity bounds properly**, or at minimum provide a proof sketch in the main text. The claim that hard-thresholding complexity becomes O(log(1/ε)) independent of κ is surprising and needs justification.

4. **Precisely calibrate the language** in the abstract and introduction. Replace "eliminates the restrictions on q" with "removes the necessary condition on q for the contraction factor to be less than one" (or similar) to match what Remark 3 actually says.

## Score and Decision

**Originality:** The variance-analysis perspective on the SZOHT conflict is genuinely novel. The application of variance reduction to ZO hard-thresholding is new. **Importance:** The problem (ℓ₀-constrained ZO optimization) is practically relevant. **Claims well-supported:** Not in the current form — the theory is too opaque to verify, and the experiments don't target the central claim. **Soundness:** Potentially sound but unverifiable from the presented text. **Clarity:** Poor. Equations are garbled, key symbols are under-defined, and derivations are omitted. **Value to community:** The core insight is valuable, but the execution does not yet make it accessible or convincing.

The paper has a genuinely novel perspective and a plausible algorithmic solution to a real problem. However, in its current form, the theoretical analysis is too opaque to verify the central claim, the experiments do not directly test that claim, and the complexity comparisons are stated without adequate derivation. The contribution is not yet convincingly established. Major revision is needed.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
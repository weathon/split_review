Now let me perform calibration search to score the paper.Round 1 bracket: **6–8**. The paper has a genuine novel theoretical contribution (first adaptive+near-optimal method for (L₀,L₁)-smooth functions) and clean analysis, placing it above the 4–5 band. The question is whether it reaches the 8 tier or sits in the 6–7 range due to the lack of experiments and some parameter condition gap.Now I have enough data to write the review. Let me synthesize everything.

---

## Summary

This paper develops **Accelerated GRAAL** (Algorithm 1), an adaptive first-order method that combines Nesterov acceleration with the local-curvature-adaptive stepsize rule of GRAAL. The central technical contribution is a novel "additional coupling step" (eq. 15–16) that allows the Nesterov momentum parameters α_k to be set adaptively — rather than at a predefined sublinear rate as in prior work (AC-FGM, AdaNAG) — while still guaranteeing β_k ∈ (0, 1]. This enables geometric (rather than merely sublinear) stepsize growth, yielding near-optimal O(√(L‖x₀−x*‖²/ε) + log(1/η₀L)) complexity for L-smooth convex functions (Corollary 2) and, more significantly, the **first adaptive near-optimal complexity** result under (L₀, L₁)-smoothness (Corollary 3).

---

## Strengths

- **Genuine first-of-its-kind result for (L₀,L₁)-smooth adaptive optimization.** Corollary 3 and Theorem 3 establish an iteration complexity of O(√(L₀𝒟²/ε) + (L₁𝒟)³ + (1+L₁²𝒟²)·log(1/(η₀L₀))) under (L₀,L₁)-smoothness. Table 1 shows this is the only result in the literature that is simultaneously adaptive (no hyperparameter tuning or line search) and near-optimal in the √(L₀𝒟²/ε) leading term. All prior near-optimal methods (Vankov et al. 2024, Tyurin 2025) require either a non-standard small-dimensional oracle or parameter tuning.

- **Precisely identified mechanism enabling improvement.** Section 3.2 cleanly isolates the deficiency of AC-FGM and AdaNAG: eqs. (28)–(29) show their complexities degrade by a factor of 1/√(η₀L) (for small η₀) or max{1, η₀L} (for large η₀) due to sublinear stepsize growth. Algorithm 1 handles both directions at the cost of a logarithmic additive term — a fair and well-calibrated improvement.

- **Transparent algorithm derivation.** The development in Section 2.1 explains each component before presenting the full algorithm: the choice of Option II for curvature estimation, the interpretation of Kovalev & Borodich (2024) for Nesterov acceleration, the specific obstruction caused by condition (14), and how the coupling step circumvents it. This makes the algorithm's design reproducible and understandable.

- **General convergence foundation (Theorem 1 / Corollary 1).** The Lyapunov-based descent inequality (20) is stated under only convexity and continuous differentiability — no smoothness needed — and provides a reusable basis for both the L-smooth and (L₀,L₁)-smooth analyses. Lemma 2's two inequalities (18) cleanly encode the role of the coupling step.

- **Geometric stepsize growth from first principles.** Lemma 1 proves β_k ∈ (0, 1], and the adaptive choice α_k = (1+γ)η_{k-1} / (H_{k-1} + (1+γ)η_{k-1}) (line 5 of Algorithm 1) guarantees η_{k+1} ≤ (1+γ)η_k — a strict improvement over AC-FGM/AdaNAG's O(1/k) growth — while depending only on quantities already computed, not requiring knowledge of L or future stepsizes.

---

## Weaknesses

### Fatal
None.

### Major

- **Parameter conditions of Theorem 1 (eq. 19) lack explicit verification.** The second condition in eq. (19) reads: 1 + 2γ + 2γθ²/(1+θ)² ≤ θ/(1+θ)² + θ²/λ_k. This involves the adaptive quantity λ_k, which varies across iterations. For L-smooth functions, Lemma 3 gives λ_k ≥ 1/L, but provides no upper bound on λ_k. When λ_k is large (e.g., when gradient differences are small relative to Bregman divergence), θ²/λ_k approaches 0, making the RHS approach θ/(1+θ)² ≤ 1/4, while the LHS is 1 + 2γ + ... > 1 for any γ > 0. This means the condition cannot hold uniformly for all possible λ_k without some implicit upper bound on λ_k — an upper bound that is neither stated nor proved in the body. The paper's claim "it is easy to verify that such parameters exist" (p. 5) is asserted without proof or example. The paper should: (a) provide at least one explicit valid triple (θ, γ, ν), or (b) argue that the proof only invokes Theorem 1 when λ_k ≤ some computable bound, or (c) state and prove such an upper bound on λ_k. Without this, the reader cannot verify that Theorem 1's hypotheses are ever satisfied, and by extension, cannot fully trust Theorems 2 and 3.

- **No numerical experiments.** The paper contains no algorithmic experiments. While the non-accelerated predecessors (GRAAL, AdGD, Malitsky & Mishchenko's heuristic accelerated AdGD) have established strong empirical track records, Algorithm 1 is a new algorithm with multiple moving parts, and there is no evidence — even on a toy quadratic — that (a) the logarithmic initialization overhead of choosing η₀ = 10⁻¹⁰ is harmless in practice, (b) geometric stepsize growth provides observable benefit over AC-FGM and AdaNAG beyond what theory predicts, or (c) the algorithm behaves correctly on an (L₀, L₁)-smooth function. For ICLR, which spans theory and systems, this is a notable gap.

### Minor

- **Additive gap (L₁𝒟)³ vs (L₁𝒟)^{5/3} in the (L₀,L₁) case.** Table 1 shows that Vankov et al. (2024) achieves a better additive constant (L₁𝒟)^{5/3} compared to Algorithm 1's (L₁𝒟)³. The authors honestly acknowledge this, but do not discuss whether the gap is an artifact of the proof technique or potentially intrinsic to the adaptive (no auxiliary oracle) setting. A brief remark on this would aid readers interested in tightening the bound.

- **Section 3.2 claim about AC-FGM/AdaNAG geometric growth needs one more sentence.** The statement "Li & Lan (2025, Corollary 2) and Suh & Ma (2025, Theorem 6) tried to resolve these issues... but could not provably achieve geometric growth" (p. 6) is stated as a conclusion without a supporting sentence indicating what specifically prevents them from proving geometric growth. A single-sentence pointer to the relevant property in their stepsize rules would make this claim self-contained.

### Trivial

- Line 10 of Algorithm 1 defines λ_{k+1} = min{Λ(x̄_{k+1}; x̃_k), Λ(x̃_{k+1}; x̃_{k+1})}. By definition (eq. 11), Λ(x̃_{k+1}; x̃_{k+1}) = +∞ always (since ∇f(x) = ∇f(x) trivially), making the second term vacuous. The same formula appears identically in the text of Section 2.1, suggesting it is consistent in both places — possibly a PDF parser artifact from a subscript ‌(intended: x̃_k). The algorithm is well-defined as written (min with +∞ is just the first term), but the redundant term is confusing and should be clarified or corrected.

---

## Nice-to-Haves

- A brief worked example or remark connecting the coupling step's properties specifically to the geometric growth condition (rather than just calling it a "bookkeeping device") would clarify the mechanism for readers.
- For the (L₀,L₁) comparison in Table 1, one sentence characterizing the per-iteration cost of Vankov et al.'s "one-dimensional relaxation oracle" would make the table self-contained; currently readers must consult that paper to understand the practical cost difference.
- Even a minimal experiment on a simple L-smooth quadratic or logistic regression problem would significantly strengthen the empirical credibility of Algorithm 1.

---

## Removed Points

*These points are flagged to be removed, treat them with caution:*

- **Harsh critic's claim that Line 10 "makes the algorithm undefined."** As shown above, Λ(x̃_{k+1}; x̃_{k+1}) = +∞ by eq. (11)'s own case analysis. The algorithm is well-defined (the min with +∞ simply returns the first term). The critic's description of this as "undefined" is factually incorrect; it is at most a presentation issue.

- **Harsh critic's framing of the initial stepsize condition as a "methodological gap."** The paper honestly and correctly notes that choosing η₀ = 10⁻¹⁰ introduces only an additive (1+L₁²𝒟²)·log(1/(η₀L₀)) term (eq. 41), which is independent of ε. This is the same suggestion used in AdGD (Malitsky & Mishchenko 2020), making it standard practice in this line of work. This is a limitation but not a gap — the paper positions the result accurately as "near-optimal."

- **Strength Finder's generic claim** that "the problem of combining Nesterov acceleration with adaptive stepsizes is important" — this is true but generic and not a specific strength of *this* paper. Removed in favor of concrete, evidence-backed strengths above.

- **Strength Finder's framing** of Lemma 1 (β_k ∈ (0,1]) as a "supporting strength." This is a technical lemma needed for the proof, not an independent contribution. Not significant enough to list as a standalone strength.

---

## Novel Insights

The key conceptual advance in this paper is that the obstacle to combining Nesterov acceleration with geometric adaptive stepsizes is not a fundamental incompatibility, but a specific algebraic coupling constraint (eq. 14) that forces prior methods (AC-FGM, AdaNAG) to either fix α_k = 2/(k+2) (forfeiting adaptivity) or accept sublinear stepsize growth. The additional coupling step (eq. 15) is a minimal perturbation of the standard STM recursion that relaxes this constraint: instead of requiring η_k/α_k ≤ η_{k-1}/α_{k-1} + η_k (eq. 14), it replaces the coupling constant with an additional degree of freedom β_k and shows that β_k ∈ (0, 1] can always be guaranteed by choosing α_k adaptively. This "free variable" approach may have broader applicability in designing adaptive accelerated methods beyond the specific setting of this paper.

---

## Suggestions

1. Provide at least one explicit valid parameter triple (θ, γ, ν) satisfying eq. (19), or add an argument in the body (not deferred to the appendix) bounding λ_k from above to show the second condition in (19) is always satisfied — this directly addresses the most significant verifiable concern.
2. Add a minimal numerical experiment (e.g., a quadratic or logistic regression problem) demonstrating that Algorithm 1 behaves correctly with η₀ = 10⁻¹⁰ and showing the geometric stepsize growth in practice.
3. Clarify the second term in Line 10 of Algorithm 1 (Λ(x̃_{k+1}; x̃_{k+1})) to resolve reader confusion about whether this is intentional, a simplification, or a typo.
4. Add one sentence in Section 4.2 on whether the (L₁𝒟)³ vs (L₁𝒟)^{5/3} gap relative to Vankov et al. is likely fundamental or an artifact of the proof technique.

---

## Score and Decision

**Calibration summary (all anchors retrieved):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|-----------|
| 1NYhrZynvC.md | 2.50 | R1 | Weak: requires knowledge of x* for stepsize, no novel insight |
| 5nldnvvHfw.md | 2.50 | R1 | Weak: ad hoc adaptive Adam variant, no strong guarantees |
| Og7ZZd7hDm.md | 3.25 | R1 | Middle-low: federated composition, incremental |
| Fj6Yv5rPRe.md | 4.25 | R1 | Middle: Adam theory, lacks novelty |
| O0FOVYV4yo.md | 5.00 | R1 | Middle: local convergence for linear networks, solid but narrower |
| DIAaRdL2Ra.md | 5.00 | R1 | Middle: Adafactor analysis, solid but narrow |
| CuupjjjT3U.md | 4.00 | R1 | Middle: parameter-free AdaGrad++/Adam++, incremental |
| fMTPkDEhLQ.md | 8.00 | R1 | Strong: tight lower bounds for Hölder smooth optimization — comparable difficulty but tighter result |
| ZuazHmXTns.md | 7.60 | R1 | Strong: problem-parameter-free federated learning, has experiments |
| **GQ1Tc3vHbt.md** | **6.50** | **R2** | **Most topically similar: (L₀,L₁)-smooth gradient methods, accepted. Less novel (analysis of known methods), but has experiments. Our paper is more focused and novel but lacks experiments** |
| nuX2yPejiL.md | 7.00 | R2 | Accepted: Polyak stepsizes + momentum, has both theory and experiments; less novel than ours but better experimental support |
| SrGP0RQbYH.md | 6.25 | R2 | Accepted: adaptive backtracking line search, has many experiments |
| AcoXPIPh4A.md | 6.00 | R2 | Accepted: accelerated SGD generalization bounds, solid but narrower |
| YwJkv2YqBq.md | 6.75 | R2 | Accepted: Nesterov acceleration in benign non-convex landscapes, somewhat comparable scope |
| Cpr6Wv2tfr.md | 6.25 | R2 | Accepted: high-order methods with superlinear convergence, similar theory + experiments |
| Qzd4BloAjQ.md | 6.75 | R2 | Accepted: SGD with memory, first-principles analysis |

**Round 1 bracket:** 6–8.  
**Round 2 narrowing:** Round 2 anchors cluster at 6.0–7.0. Our paper is comparable to GQ1Tc3vHbt (6.50) and nuX2yPejiL (7.00) in quality, but:
- Clearly *more novel* than GQ1Tc3vHbt: ours introduces a new algorithm and the first adaptive near-optimal result for (L₀,L₁)-smooth functions, whereas GQ1Tc3vHbt analyzes existing algorithms. Favors scoring above 6.5.
- Lacks experiments entirely (worse than nuX2yPejiL, which has both theory and experiments). Weighs against scoring at 7.0.
- The parameter condition gap (eq. 19) is a genuine Major weakness without an analog in nuX2yPejiL. Weighs against 7.0.

Balancing these: the theoretical contribution is genuinely first-of-its-kind and technically non-trivial, landing this paper between GQ1Tc3vHbt (6.5) and nuX2yPejiL (7.0). Given the lack of experiments and the parameter condition gap, I score this at **6.5** — above the most topically similar anchor (which had more writing issues and less novel contributions) but below the anchor that combines strong theory with extensive experiments.

**Originality:** High — the specific combination of Nesterov acceleration, geometric adaptive stepsizes, and (L₀,L₁)-smooth optimality is genuinely new.  
**Importance:** Moderate-high — answers a clear open question and extends GRAAL's adaptive capabilities to the accelerated regime.  
**Claims support:** Mostly well-supported; the parameter condition gap in Theorem 1 is the main concern.  
**Experimental soundness:** Not applicable (no experiments).  
**Clarity:** Good — transparent derivation, well-organized.  
**Value to community:** Positive — provides the first adaptive accelerated method for (L₀,L₁)-smooth convex optimization.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
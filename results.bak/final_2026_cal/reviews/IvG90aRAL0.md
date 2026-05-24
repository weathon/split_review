Now I have all the information needed. Let me produce the final review.

## Summary

This paper proposes quantum algorithms for accelerating the Frank-Wolfe (conditional gradient) method for projection-free sparse convex optimization. For the **vector domain** (ℓ₁-ball, simplex, latent group norms), the algorithms achieve query complexity Õ(√d/ε) using a function-value oracle, compared to the classical O(d) LO-oracle cost. For the **matrix domain** (nuclear-norm constraint), two algorithms (QTSVE and QPM) achieve per-iteration update costs of Õ(rd/ε²) and Õ(√(rd)/ε³) respectively, claiming at least an O(√d) speedup over classical power/Lanczos methods.

## Strengths

- **First quantum treatment of Frank-Wolfe for matrix (nuclear-norm) constraints.** The paper explicitly states this and provides two complementary approaches (QTSVE and QPM) tailored to different gradient matrix regimes. This extends prior quantum FW work (Chen & de Wolf 2023) which only addressed vector-domain problems with closed-form gradients.

- **Quadratic speedup in query complexity for vector constraints (ℓ₁-ball, simplex).** Theorem 1 and Table 1 show quantum query complexity Õ(√d/ε) versus the classical FW coordinate-scan cost O(d) per iteration. The finite-difference gradient estimation combined with quantum maximum finding is a clean and plausible subroutine for this setting.

- **Extension to latent group norm constraints.** Theorem 6 develops quantum subroutines for group-norm atoms, achieving Õ(√|𝒢|·|𝒢|_max) query complexity with error propagation analysis via Hölder's inequality. This generalizes beyond the ℓ₁-ball and simplex cases.

- **Multiple algorithmic pathways across two domains.** The paper presents a systematic framework covering vector and matrix domains, multiple constraint types, and two gradient estimation methods (finite-difference and Jordan's algorithm for the Lipschitz case), demonstrating a thorough exploration of the design space.

## Weaknesses

### Major

- **Oracle-model mismatch in the vector-domain speedup claim.** The paper states "reducing a factor of O(√d) over the best classical algorithm," but the comparison is between fundamentally different computational models. The classical Frank-Wolfe baseline (Jaggi 2013) solves the linear subproblem by scanning the coordinate-wise gradient via a **gradient/LO oracle** at cost O(d) arithmetic operations. The quantum algorithm uses a **function-value oracle** and estimates gradients via finite differences. These are different resources. If the classical algorithm were restricted to the same function-value oracle, it would require O(d) function evaluations per iteration for finite-difference gradient estimation. The paper never acknowledges this mismatch or discusses the appropriate comparison model. The claimed speedup is in query complexity to different oracles, which is potentially misleading as presented.

- **The O(√d) speedup for matrix-domain algorithms is not universally supported by the complexity expressions.** Table 2 gives classical update complexities O(d²/ε) (power method) and quantum complexities Õ(rd/ε²) (QTSVE). The ratio dε/r only yields an O(√d) speedup when r ≤ √d·ε, which is a restricted regime. The paper states "at least O(√d)" without discussing the parameter regimes (rank, precision, spectral gap) where this holds or fails. The speedup claim is not robust as stated.

- **Quantum maximum finding for singular vectors in Algorithm 3 is underspecified.** After QSVE produces a state Σᵢ σᵢ|uᵢ⟩|vᵢ⟩|σ̃ᵢ⟩, the paper states "Apply quantum maximum finding to the third register to get |u_top⟩|v_top⟩|σ̃₁⟩." Quantum maximum finding typically outputs a classical index, not a quantum state of the associated entangled singular vectors. The paper does not explain how the state of the singular vectors is preserved and extracted during this process, nor does it provide a circuit-level description or reference that addresses this specific use case. The non-uniform initial state version (Lemma 4, bottom) partially addresses this but the application to singular vectors raises additional concerns about entangled-state coherence.

### Minor

- **Missing discussion of QRAM preprocessing cost for the matrix case.** Assumption 4 provides quantum access to the gradient matrix via a QRAM-type data structure with Õ(1) query time. However, constructing this data structure from the (classically computed) gradient matrix could cost Ω(d²) or more, potentially negating the asymptotic advantage. The paper notes (Remark 3) that it follows "the classical convention of excluding gradient evaluation time" (Jaggi 2013), but unlike the classical setting where the matrix is simply stored in RAM, the quantum setting requires a specialized data structure. A brief discussion of this cost would improve honesty.

- **The parameter γ′ₘᵢₙ for the quantum power method (Algorithm 4, Theorem 4) is not bounded in terms of problem parameters.** It is defined as the minimum over i ∈ [k] of ‖(MᵀM)ⁱ b‖, but no realistic bound is given. This quantity could be exponentially small, making the quantum algorithm worse than classical. This limits the interpretability of the QPM complexity.

- **Error propagation from gradient estimation to the FW linear subproblem condition (Eq. 5) is not analyzed in the main text.** The analysis is relegated to the appendix. While this is common practice, the main text should at least sketch how the gradient approximation error σₜ and the maximum-finding tolerance combine to satisfy the δ-approximate subproblem condition.

### Trivial

- None (no formatting/typo issues worth noting).

## Nice-to-Haves

- The paper mentions Theorem 5 (Jordan's algorithm) achieving O(1/ε) query complexity as an appendix result. Since this dominates the finite-difference approach, it should be elevated to a main result and its limitations (more qubits, more gates) discussed more prominently.

- A discussion of the success probability over T = O(1/ε) iterations via a union bound would be a useful addition to the main text.

## Removed Points

- **"Classical FW does not need a function-value oracle for the linear subproblem"** — This is correct but the paper explicitly states it uses a function-value oracle (Assumption 3) and describes this as "a more general problem" than prior work. The issue is about the comparison framing, not a factual error. Kept as Major (reformulated).

- **"QTSVE complexity missing tomography term"** — The tomography cost is O(d log d / δ²). With δ set in Theorem 3 as O(ε/σ₁), this becomes O(d σ₁²/ε²). This is consistent with the Õ(rd/ε²) when r ≥ 1. The dependence may be clearer in the appendix. Removed as the concern may be addressed there.

- **"No discussion of probability of success over iterations"** — This is standard to relegate to appendix analysis. Removed.

- **"Section 4 description of classical power method/Lanczos is too brief"** — This is a scope/nitpick complaint. The description is adequate. Removed.

- **Strength: "This paper addressed an important problem"** — Generic, not specific to this paper. Removed.

- **Strength: "Quadratic speedup... concrete, dimension-dependent improvement"** — Kept as it is specific and grounded in Theorem 1/Table 1.

## Novel Insights

None beyond the paper's own contributions. The key insight is the systematic application of quantum gradient estimation and quantum maximum finding to accelerate the FW linear subproblem, with the first extension to the matrix (nuclear-norm) domain.

## Suggestions

1. **Clarify the oracle-model comparison.** Explicitly state that the classical FW operates with a gradient/LO oracle while the quantum algorithm uses a function-value oracle. Either compare within the same oracle model (both function-value: classical would be O(d) queries) or clearly qualify the speedup claim as a cross-model comparison.
2. **Discuss the parameter regimes for the matrix speedup.** Add a paragraph or table specifying when (r, ε, spectral gap) the Õ(rd/ε²) complexity actually beats classical O(d²/ε), including when it does not.
3. **Provide a more explicit description of the quantum maximum finding for singular vectors** in Algorithm 3, or replace it with a repeat-until-success / tomography-based approach that avoids the entanglement-preservation issue.
4. **Bound γ′ₘᵢₙ** in terms of the spectral gap and distribution of the initial vector, or acknowledge that it can cause the QPM to be slower than classical in worst-case scenarios.
5. **Move the Jordan-gradient result (Theorem 5) to the main text** and explain its tradeoffs (query complexity vs. qubit/gate cost).

## Score and Decision

**Calibration.** Round 1 bracket: the paper sits between weak anchors (avg ~2–3.33) and medium anchors (avg ~4–5.2), clearly above the weakest papers (which had severe flaws or irrelevance) and below the 6+ range. Round 2 narrowing compared against three most similar anchors:

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| "Quantum Speedups for Sampling... Stochastic Zeroth Oracles" (4irIRIxhs2) | 5.00 | Similar quantum optimization paper with oracle-model concerns; this paper is slightly weaker due to the comparison framing issue not being acknowledged |
| "Accelerating Regression Tasks with Quantum Algorithms" (2H2aNzDeYX) | 4.00 | Similar QRAM-reliant quantum algorithms paper criticized as incremental; this paper is stronger on novelty but has more significant claim-accuracy issues |
| "Sublinear Time Quantum Sensitivity Sampling" (8slDXCAVXS) | 5.00 | Similar quantum algorithms paper with QRAM assumptions; comparable in contribution depth |

The paper has genuine algorithmic novelty (first quantum FW for matrix constraints) and a systematic framework, but the comparison framing for the vector case and the overstated generality of the matrix speedup are notable weaknesses that reduce confidence in the headline claims.

**Score: 4.5** — A borderline paper with interesting algorithmic ideas that would significantly benefit from clarifying the comparison model, discussing parameter regimes, and providing technical details for the matrix subroutines.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
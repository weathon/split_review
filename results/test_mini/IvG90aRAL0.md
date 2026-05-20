## Summary

This paper proposes quantum Frank-Wolfe (FW) algorithms for projection-free sparse convex optimization. For the vector domain (ℓ₁-ball, simplex, latent group norms), the quantum algorithms achieve per-iteration query complexity of O(√d log(1/ε)) using a function-value oracle, an O(√d) improvement over the optimal classical approach. For the matrix domain (nuclear norm ball), the paper presents two quantum subroutines (QTSVE and QPM) for computing the top singular vectors of the gradient matrix, yielding time complexities claimed to be Õ(rd/ε²) and Õ(√rd/ε³) per update step—improving at least an O(√d) factor over classical power/Lanczos methods.

---

## Strengths

1. **First quantum acceleration of Frank-Wolfe for the matrix domain.** The paper explicitly states (Section 1, line 39) that it is "the first one to consider accelerating the matrix case of the FW algorithm by quantum computing." Theorems 3–4 and Table 2 give concrete per-iteration time complexities for computing the update direction under nuclear norm constraints, with explicit comparisons to classical power and Lanczos methods.

2. **Concrete query-complexity speedup for the vector domain.** Theorem 1 (Section 3.1) and Table 1 show that the quantum FW algorithm for the ℓ₁ ball achieves per-iteration query complexity O(√d log(C_f/ε)) using a function-value oracle, compared to O(d) for the optimal classical algorithm. This O(√d) improvement is supported by explicit quantum subroutines (gradient estimation via finite differences in superposition + quantum maximum finding).

3. **Novel subroutine for latent group norm constraints.** The paper develops a quantum subroutine that computes dual norms coherently across all groups via quantum superposition and maximum finding (Theorem 6), achieving Õ(√|𝒢|·|𝒢|_max) query complexity — an O(√|𝒢|) speedup over the classical baseline. This extends the framework to a broader class of atomic sets beyond simple ℓ₁ sparsity.

4. **Two complementary quantum approaches for the matrix update.** The paper provides two algorithms — QTSVE (Theorem 3) and QPM (Theorem 4) — with different trade-offs: QTSVE is simpler and suited to higher-rank gradient matrices, while QPM reduces rank dependence at the cost of higher sensitivity to precision. This design choice is explicitly motivated and compared in Table 2 and Section 4.

---

## Weaknesses

### Fatal
None. The paper's core methodology is sound; the issues below are significant but addressable.

### Major

1. **Unaddressed cost of maintaining quantum access to a gradient matrix that changes every iteration (matrix case).** The matrix-domain algorithms (Algorithms 3–4) rely on Assumption 4, which assumes efficient quantum access to the gradient matrix *M* = ∇f(*X_t*) supporting row-norm and Frobenius-norm queries in Õ(1) time. In a Frank-Wolfe setting, *M* changes every iteration. The paper states (line 221) that "the analysis focuses on the update direction computation and assumes that the gradient has been pre-computed and stored in the memory (Remark 3), following the classical convention of excluding gradient evaluation time." This convention is standard for excluding *gradient computation*, but it does not address the cost of *loading the newly-computed gradient into the quantum-accessible data structure* each iteration. The standard QRAM data structure (Kerenidis & Prakash, 2020b) requires Õ(d²) time to load a dense d×d matrix. This cost, when included, would dominate the per-iteration complexity and could negate the claimed speedup in regimes where *r* is not extremely small. The paper should either (a) analyze settings where the gradient is sparse or structured (allowing sub-quadratic QRAM updates) or (b) explicitly acknowledge this overhead and discuss parameter regimes where the claimed advantage survives it.

2. **Oversimplified complexity comparison in the abstract and introduction.** The abstract states the matrix-domain complexities as Õ(*rd*/ε²) and Õ(√*rd*/ε³) and claims "at least a factor of O(√d)" speedup. The actual theorems (Theorems 3–4) include dependence on spectral quantities — σ₁(*M_t*), the spectral gap (σ₁−σ₂), and γ′ₘᵢₙ — giving, for example, Õ(*r*σ₁³*d*/((σ₁−σ₂)ε²)) for Theorem 3. These spectral quantities can be large or small (the gap can be near zero), potentially making the quantum complexity exceed the classical one. The abstract and introduction should present the full form of the bounds or explicitly state the simplifying assumptions (bounded spectral gap, bounded σ₁, low-rank gradients). The claim of "at least O(√d)" is also imprecise: the d-dependence ratio from Table 2 is O(d) (d² → d), which is technically "at least O(√d)" but misleading.

### Minor

3. **Asymmetric oracle model in the vector-domain comparison.** The quantum FW algorithm (Theorems 1–2) is analyzed under a function-value oracle (Assumption 3), while the classical comparison (Jaggi, 2013) assumes gradient access. The paper states that the classical algorithm has per-iteration cost O(d) — which is correct under gradient access — but does not explicitly note that under the same function-value oracle, the classical algorithm would also need O(d) function evaluations for finite-difference gradient estimation. The core O(√d) quantum speedup is genuine and survives this adjustment, but the comparison should be framed more transparently.

4. **Dependence on poorly-characterized quantities in the QPM bound.** Theorem 4 includes γ′ₘᵢₙ (the lower bound of ∥(M_t^T M_t)ⁱ b∥ for all i ∈ [k]) in the denominator of the complexity expression. This quantity depends on the randomly initialized vector b and the singular value distribution of the gradient matrix. Its value across Frank-Wolfe iterations is not characterized or bounded in the paper. While standard power method analysis handles this probabilistically, the complexity claim in Table 2 and the abstract effectively suppresses this dependence, making the bound potentially vacuous in the worst case.

5. **Absence of discussion on when the gradient is low-rank.** The matrix-domain complexities depend on the rank *r* of the gradient matrix, used as if it is typically small. The paper does not discuss which applications yield low-rank gradients or what happens when *r* = O(d) (where the quantum complexity becomes O(d²) and no advantage remains). The classical algorithms being compared against do not depend on *r*, making the comparison regime-dependent in a way the paper does not characterize.

### Trivial
None.

---

## Nice-to-Haves

- A small numerical illustration or scaling plot of the theoretical bounds (e.g., showing *d* vs. complexity for fixed ε and *r*) would help readers assess where the claimed speedups are meaningful.
- A discussion of the ε-dependence (1/ε² or 1/ε³ in the quantum matrix-case vs. 1/ε classical) and the resulting crossover point where the quantum method becomes advantageous.
- The claim in the abstract that the speedup is "at least O(√d)" should be updated to reflect the actual O(d) dimension improvement from the table entries.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"Unaccounted cost of maintaining quantum access... alone invalidates the claimed time complexity advantages"* — The harsh critic frames this as fatal/structural. I have kept it as a Major weakness (weakening the "invalidates" framing). The paper follows a standard convention of excluding gradient evaluation time, and the data structure cost is not discussed, but it is not directly verifiable from the paper as a fatal error — it is an important unaddressed concern.

- *"Tomography cost cancels the dimension speedup"* — This criticism speculates about the derivation without seeing the full appendix (which is stripped by the parser). Per instructions, missing appendix content cannot be used as a weakness. The paper claims Lemma 7 combines QSVE and tomography into a specific bound.

- *"Missing related works (quantum LP, quantum SDP)"* — Removed per instructions: missing related works cannot be flagged without external verification.

- *"Lack of empirical validation"* — The paper is entirely theoretical, which is standard for quantum algorithms papers at this stage. Empirical validation is a nice-to-have, not a weakness.

- *Formatting/typo nitpicks* — Removed per instructions (parser artifacts, not author errors).

- *Strength Finder strengths about "importance of the problem"* — These are generic and not specific to the paper's content. Removed.

---

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any perspective on the paper that its authors would not already be aware of. The core tension — that the matrix-case speedup rests on Assumption 4 and the un-costed QRAM update — is a standard concern in quantum optimization theory and was already partially acknowledged by the paper's decision to scope its analysis to update-direction computation.

---

## Suggestions

1. **For the matrix case:** Either (a) propose a method to update the quantum data structure with sub-quadratic cost (e.g., if the gradient update has special structure in the target application), or (b) clearly identify regimes (e.g., gradient is sparse or extremely low-rank) where the QRAM update does not dominate, and explicitly state the per-iteration cost including QRAM loading. Without this, the matrix-domain contribution remains incomplete.

2. **For the abstract and introduction:** Present the full complexity expressions from Theorems 3–4, including dependence on σ₁, the spectral gap, and γ′ₘᵢₙ. The simplified forms Õ(*rd*/ε²) and Õ(√*rd*/ε³) should be explicitly qualified as assuming bounded spectral quantities.

3. **For the vector case:** Explicitly note that the quantum comparison is against a classical algorithm under gradient access, and state that under the same function-value oracle, the classical cost would be O(d) per iteration, preserving the O(√d) quantum speedup.

4. **Clarify the rank assumption:** Add a discussion of applications where the gradient is naturally low-rank (or not), and state clearly that for *r* = O(d) the quantum advantage disappears.

---

## Score and Decision

**Calibration:** 

**Round 1 (bracketing).** Three queries on "quantum algorithms for convex optimization Frank-Wolfe" with score bands:
- Weak (<3.5): returned papers with avg scores 2.0–3.33 (e.g., "Quantum mechanical framework for quantization-based optimization" avg 2.0, "Do you know what k-means?" avg 3.33). These are significantly weaker papers with less cogent contributions.
- Middle (3.5–7.5): returned papers with avg scores 4.0–6.0. Relevant anchors: "Sublinear Time Quantum Sensitivity Sampling" (avg 5.00, Reject), "Quantum Speedups for Sampling" (avg 5.00, Reject), "Beyond Short Steps in Frank-Wolfe" (avg 6.00, Accept Poster), "Accelerating Regression Tasks" (avg 4.00, Reject).
- Strong (>7.5): returned papers with avg scores 8.0–8.5 (e.g., "Feedback-driven recurrent QNN" avg 8.0, "The Polar Express" avg 8.0). These are very different in topic and nature (hardware-adjacent or empirical), not comparable.

**Round 1 bracket:** Between 4.0 and 6.0.

**Round 2 (narrowing within bracket).** Three queries targeting (3.0–5.5) on topical variants:
- "Sublinear Time Quantum Sensitivity Sampling" (avg 5.00): similar quantum ML theory paper with QRAM assumptions. Structured similarly but this paper had cleaner accounting of quantum subroutines and broader application scope.
- "Accelerating Regression Tasks" (avg 4.00): less novel (mostly applying existing quantum tricks to known classical algorithms), but cleaner contribution.
- "Quantum Speedups for Sampling" (avg 5.00): similar oracle-model concerns as present paper, comparable level of theoretical rigor.

The present paper sits between these anchors. It is more novel than "Accelerating Regression Tasks" (avg 4.00) — first quantum FW for matrix domain is a genuinely new algorithmic idea. It is comparable to but slightly weaker than "Sublinear Time Quantum Sensitivity Sampling" (avg 5.00) and "Quantum Speedups for Sampling" (avg 5.00) because the QRAM update concern is more central to the matrix-domain claims (the gradient changes every FW iteration), and the complexity claims are oversimplified in a way that masks important spectral dependencies. The vector-domain results are solid and comparable in quality to these anchors.

**Round 2 narrows the bracket to 4.0–5.0.**

**Final score:** 4.5 — The paper has a genuine and novel contribution (first quantum FW for the matrix domain, concrete vector-domain speedups with clean subroutines), but the unaddressed QRAM data structure update cost and the oversimplified complexity presentation for the matrix case prevent the contribution from being fully reliable as stated. The vector case could stand alone as a solid contribution, but the matrix case — which constitutes half the paper's claimed contributions — has a gap that needs to be closed.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
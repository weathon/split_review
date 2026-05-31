## Summary

This paper proposes quantum Frank-Wolfe (QFW) algorithms for projection-free sparse convex optimization in both vector and matrix domains. For the vector case under ℓ₁/simplex/latent group norm constraints, quantum maximum finding yields an O(√d) speedup in function oracle queries per FW iteration (total O(√d/ε) queries) compared to classical O(d/ε). For the matrix case under nuclear norm constraints, two quantum subroutines—QTSVE (Quantum Top Singular Vector Extraction) and QPM (Quantum Power Method)—reduce the per-iteration update complexity to Õ(rd/ε²) and Õ(√rd/ε³), respectively, claiming an O(√d) speedup over classical Lanczos.

---

## Strengths

- **Vector case quantum speedup is clean and well-motivated.** The core idea—computing all d finite-difference gradient components in quantum superposition followed by quantum maximum finding—directly applies Grover search to FW's argmax linear subproblem. The O(√d) speedup per iteration (Lemma 4, Theorem 1) is technically sound and follows naturally from the oracle model. The total query complexity O(√d/ε) vs classical O(d/ε) is a genuine improvement.

- **Comprehensive treatment of constraint types.** The paper covers ℓ₁ norm balls, the simplex, and latent group norms in a unified framework, with explicit error propagation via Hölder's inequality for the dual norm computation. The generalization to group norms (Theorem 6, O(√|G|) speedup) adds meaningful breadth.

- **Two complementary matrix algorithms.** The paper proposes distinct quantum subroutines for high-rank vs. low-rank gradient matrices—QTSVE and QPM—with different tradeoffs in rank dependence r and precision dependence ε. The identification of this tradeoff is insightful.

- **Cross-validation with independent work.** The authors note that for dense full-rank matrices, their QPM complexity is consistent with an independent concurrent work (Chen et al., 2025a), which provides mutual validation.

---

## Weaknesses

### Fatal
None.

### Major

1. **QRAM assumption undermines the matrix-case speedup claims.** The entire matrix domain analysis rests on Assumption 4—quantum access to M in Õ(1) time—which requires a pre-loaded Quantum RAM data structure (e.g., KP-tree). Loading or updating this structure after each gradient evaluation requires O(d²) classical operations per FW iteration. The paper explicitly excludes gradient computation time "following classical convention," but the QRAM data structure update cost is distinct from gradient evaluation and is not classical overhead in any standard sense. Not accounting for this O(d²) per-iteration cost renders the complexity comparison in Table 2 potentially misleading. For Theorem 3 claiming Õ(rd/ε²) per update step vs. classical O(d²/ε), the net runtime advantage collapses if the QRAM reload dominates. The paper should at minimum quantify this overhead or discuss whether incremental updates can reduce it.

2. **The ε-dependence tradeoff is not adequately discussed.** The claimed quantum speedups in the matrix case are in d alone, but the ε-dependence worsens: QTSVE gives 1/ε² vs. classical Lanczos 1/ε; QPM gives 1/ε³. For the claimed "O(√d) speedup" to hold, one needs ε = Ω(1/√d) for QTSVE and ε = Ω(1/d^(1/4)) for QPM—conditions that are not stated. When ε is small (e.g., for high-precision solutions), the classical Lanczos method can outperform both quantum algorithms. The paper should clearly state the regime in which the speedup holds.

3. **Quantum state tomography overhead not correctly incorporated.** Lemma 6 states that extracting a classical vector u ∈ ℝᵈ with precision δ requires O(T(U_x) · d log d / δ²) time. With δ = O(ε) and T(U_x) = Õ(‖M‖_F/ε) from Lemma 5, the tomography cost per iteration is Õ(d/ε³), which already matches or exceeds the claimed QTSVE speedup in Theorem 3. The analysis in Theorem 3 appears to account for this (the Õ(rd/ε²) result), but the derivation leading to the exponent 2 on 1/ε requires careful verification across the chain of lemmas.

### Minor

1. **Theorem 5 (Jordan algorithm, O(1/ε) queries) requires O(d log d/ε) qubits.** This is exponential in d relative to classical O(log d) bits of state and constitutes a massive space overhead that makes the result impractical. The paper mentions this "at the cost of more qubits and additional gates" but does not properly contextualize how this limits the result's applicability.

2. **The quantum access state preparation cost for the vector case is glossed over.** The paper argues in Section 3.1 that preparing |x^(t)⟩ is efficient because x^(t) is sparse with at most t non-zeros. However, the argument that "gate complexity is O(t) per iteration" should be verified more carefully since the actual quantum state needs to encode real-valued amplitudes, not just an integer index.

3. **Table 2 header references γ'_min without a clear definition in the main text.** Its dependence on the algorithm's trajectory makes it hard to evaluate the complexity of Theorem 4 without knowing how γ'_min behaves relative to d and ε in practice.

### Trivial
- The notation C_t vs. C_f/C_L appears inconsistently across theorems and algorithms, making parameter tracking difficult.

---

## Nice-to-Haves

- A discussion of classical dequantization (à la Tang et al.) for the matrix case would significantly strengthen the paper by showing whether the QRAM-based speedups are robust to classical simulation.
- Numerical experiments on small problem instances using quantum simulation would help validate the practical feasibility of the proposed subroutines.
- The claim "at least O(√d) speedup" in Table 2 should be accompanied by explicit conditions on ε and r under which this holds.

---

## Novel Insights

The most genuinely novel insight is that FW's linear subproblem over the ℓ₁ ball and simplex—which reduces to finding the argmax of |∇f(x)|—is an instance of unstructured search with quantum-computable comparators, enabling a √d Grover speedup without ever forming an explicit gradient vector. The key technical realization is that quantum superposition allows all d finite-difference gradient estimates to be computed coherently in one quantum circuit, followed by quantum maximum finding on the resulting amplitudes. This framing could generalize to other first-order projection-free methods where the linear subproblem reduces to an extremal coordinate search. The error propagation analysis via Hölder's inequality for the group norm case is also a clean technical contribution.

---

## Suggestions

- Explicitly state in the matrix case theorems the regime of ε and r for which the quantum algorithm outperforms Lanczos in total complexity (accounting for worse ε dependence).
- Address the QRAM data structure update cost per FW iteration, either by showing it can be done incrementally in sub-O(d²) time or by including it in the complexity accounting.
- Provide a formal comparison in Theorem 4 making clear that γ'_min is algorithm-dependent and discuss worst-case vs. typical behavior.
- Justify more carefully how the ℓ∞ gradient approximation guarantee needed for Lemma 4 follows from the forward-difference setup; while individually each component has error Lσ/2, this should be stated explicitly rather than relying on Lemma 2 which bounds the ℓ₂ error.

---

## Score and Decision

The vector case results are solid: the O(√d) per-iteration query speedup via quantum maximum finding over the FW argmax is a natural, clean, and verifiable quantum advantage. The matrix case is more nuanced—the contributions are meaningful but the QRAM assumption masks significant hidden costs, and the ε-dependence analysis is incomplete. The paper makes a genuine systematic contribution to quantum optimization, but the matrix case claims require more careful qualification. The work is above-average for the venue and addresses an important question, but the major caveats around QRAM and the ε-regime keep it from clear acceptance.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
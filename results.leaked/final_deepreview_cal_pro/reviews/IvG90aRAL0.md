Now I have thoroughly cross-checked every critic concern against the paper. Let me compose the final review.

---

## Summary

This paper proposes the first quantum algorithms for Frank-Wolfe (projection-free) convex optimization, covering both vector domains (ℓ₁-ball, simplex, latent group norms) and matrix domains (nuclear norm). The core idea is to accelerate the linear minimization subproblem — the computational bottleneck of FW — using quantum maximum finding, quantum singular value estimation, and quantum power methods. For vectors, the paper achieves a query complexity of \(O(\sqrt{d}\log(1/\varepsilon))\) per iteration (a \(\sqrt{d}\) speedup over classical linear search). For matrices, two complementary quantum top-singular-vector extraction subroutines (QTSVE and QPM) yield time complexities of \(\tilde{O}(rd/\varepsilon^2)\) and \(\tilde{O}(\sqrt{rd}/\varepsilon^3)\) per update, with at least \(O(\sqrt{d})\) speedup over classical power/Lanczos methods.

## Strengths

- **First systematic quantum treatment of Frank-Wolfe optimization.** The paper is, to the best of my knowledge, the first to study quantum acceleration of FW across both vector and matrix domains with multiple constraint types (ℓ₁, simplex, latent group norms, nuclear norm). This fills a natural gap in the quantum optimization literature.
- **Clean integration of quantum primitives with FW convergence analysis.** The authors carefully set the precision parameters for each quantum subroutine (finite-difference step size \(\sigma_t\), tomography precision \(\delta_t\), singular value precision \(\epsilon_t\)) to degrade with iteration \(t\) in a way that preserves the standard \(O(1/\varepsilon)\) FW convergence rate (Theorems 1–4, 6). This error-propagation analysis, tying quantum subroutine accuracy to the FW step-size schedule, is a genuine technical contribution.
- **Clear \(\sqrt{d}\) speedup in query complexity for the vector case.** Theorem 1 gives \(O(\sqrt{d}\log(1/\varepsilon))\) queries to \(U_f\) per iteration, replacing the classical \(O(d)\) linear scan. The reduction to \(O(1)\) queries under Lipschitz continuity (Theorem 5, using Jordan's gradient algorithm) is a nice demonstration that the framework can absorb stronger quantum gradient oracles.
- **Well-structured presentation with informative comparison tables.** Tables 1 and 2 give side-by-side classical vs. quantum complexity across all settings, making the claimed speedups easy to parse. The algorithms are presented in clear pseudocode (Algorithms 2–4).

## Weaknesses

### Fatal

None.

### Major

None. The harsh critic raised several concerns that, on close inspection, do not rise to the level of fatal or major flaws (see Removed Points for detailed rebuttals).

### Minor

- **Gate complexity entries in Table 1 are underspecified.** The "Gates" column reports \(O(\sqrt{d})\) and \(O(d\log d)\) for the quantum variants but the paper provides no derivation of these numbers. The \(O(\sqrt{d})\) figure appears to count iterations of the maximum-finding loop but does not account for the cost of implementing \(U_g\) per iteration (state preparation, arithmetic, uncomputation). While the paper's primary theorems (Theorems 1, 2, 5, 6) are stated in terms of query complexity — and thus unaffected — the gate counts as presented could mislead readers about end-to-end practicality. The paper should either derive the gate counts properly or remove the column.
- **Quantum data-access assumption in the matrix case deserves more discussion.** Assumption 4 (quantum access à la Kerenidis–Prakash) grants \(\tilde{O}(1)\)-time row-norm and row-preparation mappings. The paper follows the classical FW convention of excluding gradient-evaluation time \(T_\nabla\) (Remark 3), which is defensible. However, the KP data structure must be built from the gradient matrix \(M_t\) — which changes every iteration — and its construction cost is at least linear in \(\text{nnz}(M_t)\). The paper does not discuss whether this cost can be amortized, updated incrementally, or absorbed into \(T_\nabla\). A brief discussion (even acknowledging the limitation) would strengthen the contribution.
- **Non-uniform maximum finding claim (Lemma 4) stated without sufficient justification in the main text.** Lemma 4 asserts a query complexity of \(O(1/\sqrt{p}\log(1/\epsilon))\) for maximum finding on a non-uniform initial state, where \(p\) is the initial probability of the maximum component. While this is a plausible extension of amplitude amplification to the maximum-finding setting, the main text provides no derivation or citation beyond the standard Durr–Høyer reference. The proof is deferred to Appendix B.2 (stripped). A self-contained sketch in the main text would improve verifiability. Notably, even if this claim were reverted to standard \(O(\sqrt{r})\) scaling, the dimensional speedup (\(\sqrt{d}\) factor from tomography) would still hold, so this does not threaten the core results.
- **Several key proofs are appendix-only.** Lemmas 3, 4, 7, 9 and Theorems 1–6 have their proofs in Appendices B.1–B.11, which were stripped by the parser. While this is not the authors' fault, it means that central technical claims (the gradient circuit construction, the non-uniform maximum finding analysis, the QTSVE and QPM error propagation) cannot be verified from the main body alone.

### Trivial

- The paper switches between "query complexity" (vector case) and "time complexity" (matrix case) — the abstract acknowledges this but the distinction could be made more prominent in Section 3 to avoid confusion.
- The notation \(C_f\) and \(C_L\) (used in Theorems 3–4) appears to refer to the same curvature constant but uses different subscripts. Minor inconsistency.

## Nice-to-Haves

- A discussion of whether the KP data structure for the matrix gradient can be updated incrementally across FW iterations (since each update is rank-1) rather than rebuilt from scratch, which would make the time-complexity claims more realistic.
- Explicit separation of query counts and gate counts in Table 1, or removal of the "Gates" column until a full derivation is provided.
- A brief proof sketch for Lemma 4's non-uniform extension in the main text, to reduce reliance on the appendix.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **Harsh critic: State-preparation overhead requires \(\Omega(d)\) gates, invalidating Theorems 1, 2, 6.** **Removed.** The paper's main theorems (1, 2, 6) state *query complexity* — the number of calls to the function-value oracle \(U_f\). Within the standard quantum query model, state-preparation cost is not counted against the query budget; it is a gate-level concern. The paper does discuss state-preparation efficiency in Section 3.1, arguing that the sparsity of FW iterates makes the digital encoding \(O(1/\varepsilon)\)-sized and independent of \(d\). The \(\Omega(d)\) claim by the critic assumes a particular (unfavorable) encoding without QRAM or addressability, which is not the standard model for quantum query complexity results. This criticism conflates query and gate complexity and does not invalidate the stated theorems.

2. **Harsh critic: KP data-structure construction cost \(\Omega(d^2)\) omitted, structural error in matrix case.** **Removed from fatal/major.** The paper explicitly states (Remark 3, Section 4) that it follows the classical FW convention of excluding gradient evaluation/preprocessing time \(T_\nabla\). Table 2 lists \(T_\nabla\) separately for classical methods. The KP construction cost is the quantum analog of the classical gradient computation — both are \(O(d^2)\) — and excluding it from the *update* complexity is methodologically consistent. This is not a structural error; it is a modeling choice that the paper discloses. I have retained a softened version as a Minor point requesting more discussion.

3. **Strength Finder: "practical overhead analysis" and "well-defined access models."** **Partially removed / softened.** The access models are well-defined (Assumptions 3–4) and standard in the quantum algorithms literature. However, calling the overhead analysis "practical" overstates things — the paper is theoretical and the overheads (e.g., KP data structure construction) are acknowledged only in passing. I have kept the "well-defined access models" strength but dropped the "practical" qualifier.

4. **Strength Finder: "Theorem 3 yields Õ(rd/ε²) for high-rank and Theorem 4 yields Õ(√rd/ε³) for low-rank."** The "high-rank"/"low-rank" framing is from the introduction (referencing Appendix A.5, stripped). I have kept the speedup claim but avoided asserting which algorithm suits which rank regime without the appendix to verify.

## Novel Insights

The paper's most interesting insight is that Frank-Wolfe is unusually well-suited to quantum speedup because its per-iteration linear subproblem reduces to *extremal atom identification* — essentially a search problem over the atoms of the constraint set. This maps cleanly onto quantum maximum finding (Grover/Durr–Høyer), yielding a \(\sqrt{|\mathcal{A}|}\) speedup in the number of atoms. The error-propagation analysis showing that quantum subroutine errors can be absorbed into the FW step-size schedule without degrading the \(O(1/\varepsilon)\) iteration count is a useful template for future quantum-first-order methods.

## Suggestions

- Derive the gate counts in Table 1 or remove the column. If kept, clarify what is and is not included (e.g., state preparation, oracle implementation, arithmetic).
- Add a paragraph in Section 4 discussing the cost of building/maintaining the KP data structure across FW iterations, and whether incremental rank-1 updates are possible or whether the cost can be absorbed into \(T_\nabla\).
- Provide a proof sketch for Lemma 4's non-uniform extension in the main text (2–3 lines of intuition would suffice).

---

### Calibration anchors consulted

| Anchor ID | Avg Score | Round | Comparison to this paper |
|-----------|-----------|-------|--------------------------|
| pB1FeRSQxh | 6.00 | R1,R2 | Stronger: cleaner results, includes lower bounds, more polished. Our paper is broader but less deep in any one setting. |
| rUx0zQFwD1 | 5.33 | R1,R2 | Comparable technical depth; our paper is broader in scope and makes a clearer contribution to a new problem (first QFW). |
| XaARrKTNh3 | 5.25 | R1,R2 | Similar tier — quantum algorithm for classical optimization primitive; our paper covers more ground. |
| XABvLUXQ45 | 4.80 | R2 | Clearly weaker: narrower scope, less rigorous analysis, speedup only under restrictive conditions. |
| TUiEgloner | 4.75 | R1 | Less relevant (quantum Hamiltonian learning); our paper is stronger. |

**Round-1 bracket:** 4.0 – 7.0. **Round-2 narrowing:** placed between XABvLUXQ45 (4.80, Reject) and pB1FeRSQxh (6.00, Accept). The paper is clearly stronger than XABvLUXQ45 (more comprehensive, more rigorous, broader scope) and somewhat weaker than pB1FeRSQxh (no lower bounds, less polished complexity claims). The paper lands closest to the rUx0zQFwD1 (5.33) anchor in technical depth but with broader applicability, justifying a score slightly above it.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>
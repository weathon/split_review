Now let me finalize and write the consolidated review.

## Summary

The paper proposes quantum Frank-Wolfe (QFw) algorithms for projection-free sparse convex optimization over both vector domains (ℓ₁-ball, simplex) and matrix domains (nuclear-norm ball). For the vector domain, it achieves a query complexity of Õ(√d/ε), a √d improvement over classical FW, by combining quantum finite-difference gradient estimation with quantum maximum finding. For the matrix domain, it proposes two algorithms based on quantum singular value estimation (QTSVE) and the quantum power method (QPM), claiming complexity Õ(rd/ε²) and Õ(√(rd)/ε³) respectively for the update step, representing at least an O(√d) dimensional speedup over classical methods.

## Strengths

1. **First quantum speedup for vector-domain Frank-Wolfe with ℓ₁/simplex constraints.** The vector algorithms (Section 3) are well-designed and represent a legitimate contribution. The combination of quantum finite-difference gradients (Lemma 3) with quantum maximum finding over coordinates (Lemma 4) is a natural and appropriate application of quantum techniques, yielding a clean Õ(√d/ε) query complexity — a √d improvement over the classical O(d/ε). The convergence analysis with error propagation from the approximate subproblem solution (Appendix B.3) appears sound.

2. **Well-motivated extension to atomic sets and latent group norms.** The framework's generalization to simplex constraints (Theorem 2) and latent group norm balls (Theorem 6) demonstrates genuine flexibility beyond the basic ℓ₁ case. The use of quantum maximum finding to identify the dominant atom in superposition is a principled approach, and the O(√|𝒢|) speedup in the group count is meaningful.

3. **Systematic side-by-side comparison with classical baselines.** Tables 1 and 2 provide explicit per-iteration and total complexity comparisons against classical FW, power-method, and Lanczos-method baselines. This transparency helps the reader assess where the claimed advantages come from and what parameters they depend on.

4. **Addresses a natural and well-motivated question.** Whether quantum computing can accelerate the bottleneck linear subproblem in Frank-Wolfe optimization is a natural and important question. The paper's framing (Section 1) clearly motivates why FW is a good target: the projection-free nature means the core computational task is a structured linear optimization over the constraint set, which is well-suited to quantum search techniques.

## Weaknesses

### Major

1. **Insufficient justification of Algorithm 3's use of quantum maximum finding on the QSVE state.** The paper claims (Algorithm 3, line 9; Lemma 7) that quantum maximum finding (QMF) can be applied to the QSVE output state
   $\frac{1}{\|M\|_F} \sum_i \sigma_i |u_i\rangle|v_i\rangle|\bar{\sigma}_i\rangle$
   to extract the top singular vectors. The standard Durr-Hoyer QMF algorithm assumes items indexed by computational basis states with an oracle that maps $|i\rangle$ to $f(i)$. Here, the "items" are entangled with singular vector states $|u_i\rangle|v_i\rangle$ that are not computational basis states. While amplitude-amplification-based variants could potentially be used, the paper does not explain how the required reflections would be implemented given the QSVE state structure. Lemma 4's brief note about "non-uniform input states" is insufficient — the main text needs a clear description of how the Grover-style iteration is realized in this setting and why the claimed query complexity $O(1/\sqrt{p})$ follows. The proof is deferred to Appendix B.2 (stripped from the extracted version), making the algorithm unverifiable as presented. This undermines the confidence in Theorem 3's complexity bound.

2. **Quantum data structure overhead is not adequately addressed for the matrix algorithms.** Assumption 4 assumes efficient quantum access to the gradient matrix $M$ (row states and norm state in $\tilde{O}(1)$ time). This data structure must be updated each Frank-Wolfe iteration since the gradient $M = \nabla f(X_t)$ changes. For a dense gradient, rebuilding costs $O(d^2)$ — the same leading order as the classical power method's per-iteration cost. The paper states it excludes gradient evaluation time (Remark 3), following classical convention, but the data structure cost is *not* part of classical gradient evaluation $T_\nabla$ — it is an additional quantum overhead. A honest accounting of this cost is essential for any claim of quantum advantage in the matrix setting. The paper's silence on this issue gives an incomplete picture of the actual resource requirements.

3. **Algorithm 4 (QPM) is sketchily described.** The quantum power method algorithm is presented with minimal detail. The initial state preparation with "two copies of $|b\rangle$" and the simultaneous application of quantum matrix-vector multiplication for both left and right singular vectors are not explained. Lemma 9's power method analysis depends on the parameter $\gamma'_{\min}$ (a lower bound on $\|(M^\top M)^i b\|$), which is not discussed in terms of how it interacts with the matrix $M$'s properties or how it affects the final complexity bound. Theorem 4's complexity expression $\tilde{O}\left(\frac{\sqrt{r}\sigma_1^4(M_t)d}{(1-\sigma_1(M_t))^3\gamma_{\min}^{2.5}}\right)$ involves several parameters whose roles and reasonable values are not clarified.

### Minor

4. **Oversimplified speedup claims in the abstract.** The abstract states "reducing at least a factor of $O(\sqrt{d})$ over the best classical algorithm" for the matrix domain. The actual comparison (Table 2) shows quantum complexity Õ(σ₁²d/((σ₁-σ₂)ε²)) vs classical O(σ₁d²/((σ₁-σ₂)ε)), yielding a dimensional factor of $d$ (not $\sqrt{d}$) in the clean case. The worse ε-dependence (ε⁻² vs ε⁻¹) and dependence on the spectral gap and rank make the claimed $\sqrt{d}$ speedup a selective simplification. The vector-domain claims are more accurate and better supported.

5. **Inconsistency in Algorithm 3's pseudocode.** Line 8 writes the QSVE output as $\frac{1}{\sqrt{\sum_i \sigma_i^2}} \sum_i^r \sigma_i |u_i\rangle |\bar{\sigma}_i\rangle$, omitting the $|v_i\rangle$ register that appears in Lemma 5's output and is needed for line 9's $|\bar{v}_{top}\rangle$. This makes the pseudocode confusing to follow.

6. **Success probabilities and repetition counts are not explicitly multiplied into the reported complexities.** Lemmas 6 and 7 (tomography and QTSVE) succeed with probability $1-1/\text{poly}(d)$, but the overall success probability of the Frank-Wolfe iteration (which may need $O(1/\varepsilon)$ rounds) is not analyzed. The paper mentions "repeating logarithmic times and then taking the average" but does not factor this into the complexity bounds stated in Theorems 3 and 4.

### Trivial

7. **The "Qubits" and "Gates" columns in Table 1 are not discussed in the main text.** These resource estimates appear without explanation of how they are derived or what they mean for implementation feasibility.

8. **The latent group norm extension is mentioned prominently in the abstract but appears only in the appendix.** A brief summary in the main text would improve coherence.

## Nice-to-Haves

- A self-contained explanation (in the main text) of how amplitude amplification can be used as a substitute for standard QMF when applied to the QSVE state, with explicit construction of the reflection and comparison oracles.
- A discussion of regimes (e.g., sparse gradients, low-rank structure in the gradient) where the quantum data structure update cost can be managed, to bound the overhead more concretely.
- A worked example or resource estimate for a concrete problem instance (e.g., matrix completion of size $d=1000$) showing how the quantum and classical complexities compare numerically.

## Removed Points

- *"Flawed application of quantum maximum finding in Algorithm 3 (QTSVE) — fatal error that invalidates the complexity and speedup."* **Reason:** Downgraded from Fatal to Major. While the algorithm is insufficiently justified, the approach is potentially salvageable via amplitude amplification (reflection about the initial state rather than the uniform superposition). The criticism that "there is no efficient way to index the singular values by a computational basis index" is too strong — amplitude amplification does not require computational basis indexing. However, the lack of clear explanation makes this a Major weakness, not a Fatal one.
- *"Comparison of classical and quantum complexities in different units."* **Reason:** Both Table 2 column headers show the same type ("Complexity of the Update Computing"), and both include $T_\nabla$ for gradient evaluation. The comparison is in consistent units. The criticism appears to be a misreading.
- *"Missing related works"* and *"Missing appendix, missing proofs in appendix"* **Reason:** These are parser artifacts; the appendix exists in the original submission.
- *"Pure formatting/style nitpicks"* and *"Typos, spelling, grammar"* **Reason:** Parser errors, not author errors.
- *"Assumption 4 is a strong assumption"* [as a standalone weakness]. **Reason:** This is standard in the QML literature and papers are evaluated against their own community's assumptions. The specific concern about *updating* the data structure is genuine and is kept in Major weakness #2. The generic criticism is removed.

## Novel Insights

The paper makes a genuine connection between two areas: the Frank-Wolfe algorithm's structured linear subproblem (which is naturally suited to quantum search) and quantum techniques for gradient estimation and maximum finding. The insight that the FW update direction for ℓ₁-constrained problems reduces to finding the coordinate with the largest gradient magnitude (a maximum-finding task) is clean and well-exploited. For the vector domain, this connection yields a clear quadratic speedup. The matrix domain extension is less clean, but the recognition that the nuclear-norm FW update direction reduces to computing the top singular vector pair provides a natural target for QSVE and quantum power methods. The error-propagation analysis bounding how gradient approximation errors propagate through the subproblem solution (via Hölder's inequality) is a nice technical contribution that enables the quantum speedup without sacrificing convergence guarantees.

## Suggestions

1. **Focus the revision on the vector-domain results and substantially rework the matrix section.** The vector algorithms are solid and could form the basis of a strong, well-scoped paper. For the matrix section, either (a) remove it entirely and save it for future work, or (b) provide a complete, verifiable description of how QMF/amplitude amplification is applied to the QSVE state, with explicit oracles and reflection operators. Without this, Algorithm 3 should be dropped.

2. **Acknowledge the data structure overhead transparently.** Even a brief paragraph discussing regimes where the gradient is sparse or low-rank (so the data structure can be updated efficiently) would significantly strengthen credibility. Failing that, explicitly state that the claimed complexities assume amortized constant-time data structure access and note that this is a strong assumption shared with other quantum linear algebra works.

3. **Make the speedup claims precise.** Replace "at least a factor of $O(\sqrt{d})$" with a statement that explicitly factors in the dependence on $\varepsilon$, the spectral gap, and the rank $r$, possibly with a discussion of when the $\sqrt{d}$ speedup materializes (e.g., when $r=O(1)$ and $\varepsilon$ is fixed).

## Score and Decision

**Calibration Procedure:**

**Round 1 (Bracketing):** I retrieved three bands of anchors:
- **Weak anchors (avg < 3.5):** Papers on quantum optimization with avg scores 1.67–3.40. These are clearly weaker than the current paper — they lack substantive contributions or have fundamental errors. The current paper is above this band.
- **Middle anchors (3.5–7.5):** 
  - *Near-Optimal Quantum Algorithm for Minimizing the Maximal Loss* (6.00, accept) — cleaner quantum optimization with matching bounds; the current paper is clearly weaker due to the matrix-part issues.
  - *Quantum Speedups in LP* (5.33, reject) — solid but incremental quantum optimization with presentation issues; comparable in ambition but cleaner technically.
  - *Quantum Algorithm for Sparse Online Learning* (4.80, reject) — quantum ML speedup with access assumptions; similar in structure (vectors + quantum access) but narrower scope.
  - *Catalyst Framework for QLSP* (5.25, reject) — solid quantum algorithm.
  - *Quantum (Inspired) D²-sampling* (6.50, accept) — clean quantum algorithm with dequantization; stronger technically.
- **Strong anchors (avg > 7.5):** Papers with avg scores of 8.00. The current paper is clearly not at this level.

**Initial bracket:** 3.5–6.5, likely on the lower side.

**Round 2 (Narrowing):** I retrieved anchors in the 4.0–6.0 and 5.0–7.5 bands focusing on quantum optimization and conditional-gradient-style methods. The most directly comparable anchor is the *Sparse Online Learning* paper (4.80) — both use quantum access assumptions to achieve speedups for convex optimization with sparsity constraints. The current paper has a more ambitious scope (matrix domain, multiple constraint types) and more extensive theoretical framework, but its matrix results are less credible than the sparse online learning paper's focused contribution. The *Quantum Speedups in LP* paper (5.33) is cleaner in its technical execution. I conclude that the current paper sits slightly below the *Sparse Online Learning* anchor due to the unverifiable matrix algorithms and data structure issues, placing it around 4.5.

**Final score:** 4.5. The paper has a real contribution in the vector domain (clean √d speedup for FW with ℓ₁ constraints) which is well-described and appears correct. However, the matrix-domain results, which form a substantial part of the claimed novelty, are undermined by an algorithm that is not adequately justified (Algorithm 3 / QTSVE) and a data structure overhead that is not discussed honestly. The QPM-based algorithm (Algorithm 4) is too sketchily described to be independently evaluated. The paper as a whole presents itself as a systematic treatment of both domains, but the matrix part is not ready for publication. The vector results alone, while solid, would benefit from a focused presentation rather than being paired with fragile matrix claims.

**Anchor papers used:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| hqxzi4d3Ws (PQRC noise-resilient) | 3.00 | R1 | Much weaker; less relevant topic |
| wgnMdxS2nZ (MQFL-FHE) | 3.40 | R1 | Much weaker; distant topic |
| pB1FeRSQxh (Near-Optimal Quantum Max Loss) | 6.00 | R1,R2 | Cleaner quantum optimization paper; stronger technically |
| XABvLUXQ45 (Sparse Online Learning) | 4.80 | R1,R2 | Similar quantum-ML speedup paper; comparable scope, cleaner execution |
| rUx0zQFwD1 (Quantum LP Speedups) | 5.33 | R1,R2 | Solid quantum optimization; similar in having complex parameter dependencies |
| XaARrKTNh3 (Catalyst QLSP) | 5.25 | R1,R2 | Clean quantum algorithm paper |
| tDIL7UXmSS (Quantum D²-sampling) | 6.50 | R1 | Significantly stronger technically |
| dLrhRIMVmB (TDA on noisy QC) | 8.00 | R1 | Much stronger; full implementation |

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
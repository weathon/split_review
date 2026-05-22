I have verified all claims against the paper. Here is the consolidated review.

---

## Summary

This paper provides a complete characterization of polynomial (and analytic) tensor-to-tensor maps equivariant under the diagonal action of the orthogonal, Lorentz, and symplectic groups. The main theoretical result (Theorem 1) states that every O(d)-equivariant polynomial on tensors can be expressed as a sum of tensor products of inputs contracted with isotropic tensors, which are built from Kronecker deltas and Levi-Civita symbols. For the practical case of vector inputs, this yields an explicit parameterization (Corollaries 1 and 3) where the learnable functions depend only on invariant inner products. Experiments on stress-strain learning in materials science, path signature prediction for time series, and sparse vector estimation in theoretical computer science show large improvements over non-equivariant baselines and, in the stress-strain case, over a prior equivariant method (TFENN).

## Strengths

1. **Explicit, usable parameterization via invariant theory.** Corollaries 1, 2, and 3 give concrete algebraic recipes that practitioners can implement directly, without needing to compute Clebsch–Gordan coefficients or decompose into irreducible representations. This is validated by the open-source code.

2. **Generality across classical groups.** The theoretical framework covers O(d), the indefinite orthogonal groups (including Lorentz), and the symplectic group in a unified manner. This goes substantially beyond prior work that was restricted to O(3)/SO(3) (e3nn, escnn) or to the orthogonal group alone. The extension is non-trivial and uses the appropriate invariant tensors for each group (Minkowski metric for Lorentz, symplectic form for Sp(d)).

3. **Consistent and large empirical gains.** On the stress-strain problem (Table 1), the equivariant model achieves test error 4.057×10⁻⁶ (n=5,000), an order of magnitude better than the next best baseline (2.020×10⁻⁵) and better than the existing equivariant method TFENN. On path signature (Table 2), the O(d)-equivariant model scores 0.002 vs. 0.007 for the augmented MLP. On sparse vector estimation (Table 3), the equivariant model outperforms both SoS methods and the MLP baseline in many settings, especially when SoS assumptions are violated.

4. **Honest scoping and limitations discussion.** The paper explicitly states the computational complexity (k′! n^{k′}), notes that practicality is limited to small k′ ∈ {1,2,3,4}, and acknowledges where it is uncertain about extending the characterization to all continuous equivariant functions. Remark 1's treatment of Stone–Weierstrass approximation is appropriately cautious.

## Weaknesses

### Fatal
None.

### Major
None. The core theoretical contribution is sound, the experiments support the claimed improvements, and the paper is clearly written.

### Minor

1. **Missing equivariant baselines for two of three experiments.** The stress-strain experiment compares against TFENN (an existing equivariant method), which is appropriate. However, the path signature and sparse vector experiments compare only against non-equivariant MLPs and domain-specific methods (discrete signature, SoS). While e3nn is not applicable to these settings (it is limited to d=2,3), the paper could have constructed a simple alternative equivariant architecture (e.g., using the same Corollary 1 but with restricted q-functions, or a hand-crafted equivariant baseline) to further isolate the benefit of the specific parameterization. This would strengthen the claim that the proposed architecture is preferable over other plausible equivariant designs.

2. **No symplectic group experiment.** The symplectic group appears in the title, abstract, and Section 4's theory, but no experiment demonstrates its use. While the theoretical treatment is complete (Corollary 3), an empirical demonstration — even a small synthetic example — would strengthen the claim of broad applicability across all three groups.

3. **Typo in Corollary 1.** The summation in Eq. (11) reads "σ ∈ S_k" but should be "σ ∈ S_{k′}" since the permutation acts on the k′ indices of the output tensor. The surrounding text on line 174 correctly discusses "permutations of the k′ axes," so the intent is clear, but the equation is technically incorrect as written.

### Trivial

- The path signature metric expression in Table 2's caption contains a garbled element ("d_F/d_F") — a parser artifact, but worth correcting in a final version.

## Nice-to-Haves

- A runtime/memory comparison between the proposed method and the MLP baselines would help practitioners assess the computational trade-off of imposing equivariance.
- A qualitative example of the path signature prediction (e.g., a reconstructed path from predicted vs. true signature) would illustrate what a test error of 0.002 means in practice.
- Adding a brief remark after Corollary 1 explaining that the form would differ when inputs or output have parity − (requiring Levi-Civita contractions) would prevent reader confusion, even though the corollary is correctly scoped to parity +.

## Removed Points

These points were raised in reviews but removed from the main weaknesses for the stated reasons:

- **"Missing comparison to e3nn/Clebsch-Gordan methods for path signature and sparse vector"**  — The paper's related work explicitly states that e3nn/escnn are restricted to SO(d)/O(d) for d=2,3, while the paper's experiments operate in settings where those restrictions do not hold. The stress-strain experiment already provides a comparison to an existing equivariant method (TFENN). The critic's request assumes the existence of off-the-shelf equivariant baselines for these specific setups, which is not the case. (Moved from Major → Removed.)

- **"Scalability limitations noted but not addressed"** — The paper explicitly states the O(k′! n^{k′}) complexity and honestly notes that "evaluating f is only practical for small values of k′; however, since k′ is the rank of the output tensor, k′ ∈ {1,2,3,4} already captures many cases of practical interest." This is an appropriate scoping discussion, not an omission. (Moved from potential criticism → Removed.)

- **"Parity restriction in Corollary 1 not sufficiently emphasized"** — The corollary itself states the parity conditions: "+" for both input and output. The paper cannot be faulted for not discussing what lies outside the corollary's explicitly stated scope. (Moved → Removed.)

- **"Metric in path signature mixes errors across orders"** — The metric is an average of normalized Frobenius norms, which is a standard practice for comparing sequences of tensors of different orders. (Moved → Removed.)

- **"Standard deviations not reported for O(d) case"** — The paper states "when it is at least 1e-3" for reporting std. The O(d) result of 0.002 without std implies the std was below 1e-3, which is plausible and honestly reported. (Moved → Removed.)

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface an insight about the paper that the paper itself does not articulate.

## Suggestions

1. Fix the S_k → S_{k′} typo in Corollary 1.
2. Add a brief remark after Corollary 1 noting that the parity + restriction means Levi-Civita terms are absent because they carry parity −.
3. If feasible, add a small synthetic experiment for the symplectic group to match the theory's breadth.
4. Add a simple equivariant baseline (e.g., a reduced version of the same Corollary 1 parameterization with fewer q-functions) for the path signature or sparse vector task to clarify that the benefit comes from the specific parameterization and not just from imposing any form of equivariance.

## Score and Decision

**Evaluation along key axes:**
- **Originality:** High. The unified characterization of equivariant tensor polynomials via invariant theory for O(d), Lorentz, and symplectic groups in a machine learning context is novel.
- **Importance of research question:** High. Symmetry-aware models are central to scientific ML, and tensors are ubiquitous in physics, materials science, and time series.
- **Claims well supported:** Yes. The theoretical results are correctly stated, and the experiments consistently show large gains over non-equivariant baselines and, where compared, over an existing equivariant method.
- **Soundness of experiments:** Good. Multiple trials with standard deviations, comparisons across dataset sizes, and honest reporting of mixed results (e.g., SoS sometimes beating the method). The main gap is the lack of equivariant baselines for two of three tasks, which is mitigated by domain-specific baselines and the paper's honest scope.
- **Clarity of writing:** Good. The mathematical exposition is accessible, and the corollaries are clearly separated from the general theory.
- **Value to the community:** High. Provides a practical recipe for building equivariant tensor models without the overhead of representation-theoretic machinery, applicable to a wider set of groups than prior work.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
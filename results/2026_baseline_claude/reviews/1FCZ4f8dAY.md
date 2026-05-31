## Summary

This paper develops a unified theoretical framework for constructing machine learning models that are equivariant with respect to the diagonal action of classical Lie groups (orthogonal O(d), indefinite orthogonal O(s,d−s) including the Lorentz group, and symplectic Sp(d)) on tensors. The core result (Theorem 1 / Corollary 1) characterizes all equivariant polynomial functions from tensors to tensors using invariant theory—expressing them as linear combinations of tensor products of input vectors weighted by scalar functions of pairwise inner products—thereby avoiding the need for Clebsch-Gordan coefficients. The method is applied to three problems: stress-strain tensor learning, path signature estimation, and sparse vector recovery.

---

## Strengths

- **Unified and principled characterization.** Theorem 1 and Theorem 2 together cleanly extend classical tensor invariant theory to a format suitable for machine learning, covering O(d), O(s,d−s), and Sp(d) in one framework. Corollary 1 is particularly elegant: all O(d)-equivariant polynomial maps from n input vectors to a k'-tensor can be expressed via scalar MLPs on pairwise inner products plus fixed tensor and Kronecker structure, with no Clebsch-Gordan coefficients.

- **Strong experimental results on two of three tasks.** On stress-strain tensors (Table 1), the method achieves 4.057e-6 vs. 2.020e-5 (MLP augmented) and 5.3e-5 (TFENN) at n=5,000—roughly a 5× improvement over the next-best method. On path signatures (Table 2), the Lorentz result (0.005 vs. 0.186 for MLP augmented) is striking and demonstrates genuine value of encoding the correct group symmetry.

- **Broader group coverage than prior art.** Existing CG-based methods (e3nn, escnn) are specific to SO(2)/SO(3)/O(3). By contrast, the invariant-theory approach here extends naturally to the Lorentz group and the symplectic group, which are physically important (special relativity, Hamiltonian mechanics) and had no comparable equivariant ML framework.

- **Practical parameterization is implementation-friendly.** Corollary 2's reduction of O(d)-equivariant symmetric-matrix functions to permutation-equivariant eigenvalue functions is particularly clean and yields a directly implementable architecture with known theoretical grounding (Maron et al., 2019 for the permutation-equivariant part).

- **Transparent discussion of approximation scope.** Remark 1 honestly acknowledges that universality over all continuous equivariant functions is unproven, while correctly noting that Stone–Weierstrass closure ensures polynomial-expressive architectures suffice for compact-domain approximation.

---

## Weaknesses

### Fatal
None.

### Major

- **Mixed and unexplained failures in the sparse vector experiment.** Table 3 reveals that "Ours" performs very poorly in several settings: for Bernoulli-Gaussian with Diagonal covariance it achieves 0.463 vs. SoS's 0.949 and even Ours (Diag)'s 0.914; with Identity covariance it achieves 0.342 vs. SoS's 0.962 and Ours (Diag)'s 0.908. The paper offers no substantive explanation for why the richer model ("Ours") performs drastically worse than its own ablation ("Ours (Diag)") in these settings. This inconsistency calls into question whether the method reliably extracts the equivariant structure in practice—and undermines the paper's claim that equivariant models outperform non-equivariant baselines, since Ours (Diag) is structurally simpler. The absence of any analysis (overfitting? optimization? representation collapse?) is a significant gap.

- **Computational complexity analysis is incomplete.** The paper states that evaluating Corollary 1 costs O(k'! n^{k'} (Qdn² + d^{k'})) and says this is "only practical for small values of k'." However, the path signature experiment requires estimating tensors up to order M for paths in R^d—the number of terms can grow rapidly with n (the number of sample points). There is no discussion of how n scales in experiments, what degree polynomials are used, or how the actual runtime compares to baselines. For practitioners choosing between this method and CG-based alternatives, this information is essential.

### Minor

- **Corollary 3 restricts all inputs and the output to be of the same type** (same order k and trivial character χ_0), which is significantly more constrained than Corollary 1. The paper does not discuss what is lost by this restriction for practical Lorentz/symplectic applications, nor whether relaxing it is feasible.

- **Lack of ablation on degree of the polynomial/MLP capacity.** It is unclear how sensitive the results are to the degree of the polynomial (or depth/width of the q-MLPs). Without this, it is hard to distinguish the benefit of equivariance from the benefit of more parameters or greater model capacity.

### Trivial
None worth listing.

---

## Nice-to-Haves

- A dedicated section or table analyzing the sparse vector failures (Table 3, Diagonal/Identity rows for BG) would substantially improve the paper—even if the conclusion is simply that the model trains poorly with more capacity in those settings.
- Runtime comparison with CG-based methods (e3nn/escnn) on the stress-strain task would help practitioners decide when to prefer the invariant-theory approach.
- A small toy demonstration or figure showing the Lorentz/symplectic isotropic tensors (analogous to the Kronecker delta for O(d)) would make Section 4 more concrete for readers unfamiliar with those groups.

---

## Novel Insights

The paper's most genuinely novel insight is that the Clebsch-Gordan decomposition—long considered the standard route for equivariant tensor architectures—is unnecessary for a large class of problems, and can be replaced by a simpler framework: compute all pairwise inner products under the relevant bilinear form, pass them through a shared scalar MLP, and reconstruct the output tensor using outer products and the group-appropriate isotropic tensors (Kronecker delta for O(d), the indefinite metric for Lorentz, the symplectic form for Sp(d)). This not only yields cleaner architectures for O(d) (at comparable computational cost to e3nn/escnn per Corollaries 1/3), but—more importantly—immediately generalizes the equivariant ML toolkit to Lorentz and symplectic settings where no CG-based implementation existed. The path signature + Lorentz experiment is a compelling proof-of-concept for this generalization.

---

## Suggestions

- Diagnose and explain the poor performance of "Ours" vs. "Ours (Diag)" in Table 3 for Bernoulli-Gaussian settings—this is the most important open question raised by the experiments.
- Report the number of terms in the equivariant expansion and training/inference time alongside accuracy for at least one experiment to give practitioners concrete complexity intuition.
- Discuss whether Corollary 3 can be extended to mixed-order inputs under the Lorentz/symplectic groups, or state a formal obstruction.
- For the path signature task, clarify how the single shared MLP for all q_{t,σ,J} functions relates to parameter efficiency vs. expressiveness.

---

## Score and Decision

The theoretical contributions are solid, cleanly stated, and fill a genuine gap—particularly the extension to Lorentz and symplectic groups without Clebsch-Gordan coefficients. Two of three experiments are convincing wins. The sparse vector experiment has unexplained failures that the paper does not adequately address, and the computational complexity discussion is incomplete; but neither issue invalidates the core theoretical claims or the other two experiments. The paper is a meaningful contribution to the equivariant ML community.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
Now I have thoroughly analyzed the paper and all reviewer claims. Let me produce the final consolidated review.

---

## Summary

This paper proposes the Gaunt Tensor Product, a method to accelerate E(3)-equivariant operations by reinterpreting the Clebsch-Gordan tensor product through Gaunt coefficients (integrals of three spherical harmonics). This transforms the tensor product into multiplication of spherical functions, which can be computed efficiently using a 2D Fourier basis and Fast Fourier Transforms — reducing complexity from O(L⁶) to O(L³). The approach is applied to three operation classes (Equivariant Feature Interactions, Convolutions, and Many-body Interactions) and validated on OC20 and 3BPA benchmarks with substantial speedups and competitive accuracy.

## Strengths

- **Novel theoretical connection enabling complexity reduction from O(L⁶) to O(L³).** The paper mathematically connects Clebsch-Gordan coefficients to Gaunt coefficients (Eqn. 4, derived from the Wigner-Eckart theorem), showing that the tensor product of irreps is equivalent to multiplication of spherical functions. This insight is then leveraged with a 2D Fourier basis and FFT to reduce the complexity of full tensor products from O(L⁶) to O(L³) (Section 3.2, lines 138–140). This is a concrete, mathematically grounded improvement over prior implementations.

- **Empirical speedups of multiple orders of magnitude across three operation classes.** Figure 1 reports wall-clock acceleration against e3nn, eSCN, and MACE. For Equivariant Feature Interactions, speedup exceeds 10× at L=9 and grows to >100× at higher L. For Many-body Interactions on 3BPA, MACE-Gaunt achieves 43.7× speedup over e3nn and 33.2× over MACE, while reducing memory by 82.3% vs. MACE (Table 2). These efficiency gains are the paper's strongest evidence.

- **Controlled sanity check confirms the Gaunt parameterization does not harm expressivity.** The N-body task comparison (SEGNN) in Figure 1 keeps all hyperparameters identical and compares only the parameterization (Gaunt vs. CG), showing nearly identical performance (~1.5×10⁻³ MAE after 500 epochs). This directly supports the claim that the basis change preserves model capacity.

- **Demonstrated generality across three distinct operation classes.** Sections 3.3 shows how the Gaunt Tensor Product applies to Equivariant Feature Interactions, Equivariant Convolutions (with an additional sparsification trick from Passaro et al.), and Equivariant Many-body Interactions (with a divide-and-conquer strategy), covering the main building blocks of modern E(3)-equivariant models.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **The OC20 experiment does not isolate the effect of the Gaunt parameterization from the addition of a new operation.** The paper adds a "Selfmix" (Equivariant Feature Interaction) operation to EquiformerV2 and reports improved performance (EFwT 1.95% vs. 1.67%, lines 202–203, 221). However, the baseline EquiformerV2 does not have this operation at all. The improvement could come from the additional parameters/computation rather than from the Gaunt parameterization specifically. A controlled comparison (e.g., EquiformerV2 + CG-based Selfmix vs. EquiformerV2 + Gaunt Selfmix, even at small L where CG is tractable) would be needed to attribute the improvement to the Gaunt method. The paper's claim of "improved performance" (lines 31, 269) is overly strong without this control. However, note that this does not undermine the paper's primary contribution (efficiency), which is validated separately.

2. **The mathematical presentation of the 2D Fourier basis conversion is imprecise.** The paper states that "both spherical harmonics and 2D Fourier bases form an orthonormal basis set for spherical functions" (line 120). The 2D Fourier basis e^{i(uθ+vψ)} for θ∈[0,π], ψ∈[0,2π) is not orthonormal under the standard inner product — the functions {e^{iuθ}} are not orthogonal on the interval [0,π]. The paper relies on the existence of the expansion coefficients y^{l,m,*}_{u,v}, which is mathematically correct (spherical harmonics are finite trigonometric polynomials in both θ and ψ, so the conversion is exact for bandlimited functions without approximation). However, the presentation is sloppy about the underlying function space and measure, and the paper does not reference standard spherical harmonic transform literature (e.g., Driscoll-Healy sampling theorem) that would clarify the discretization. This does not invalidate the approach but should be tightened.

3. **The paper does not provide an algorithm or reference for computing the conversion coefficients y^{l,m,*}_{u,v}.** While the sparsity pattern (m=±v) is stated (line 120), the paper gives no explicit formula or citation for how these coefficients are computed in practice. A reader implementing the method would need this information. This is a reproducibility gap, though the relationship between associated Legendre polynomials and Fourier series is standard knowledge in the field.

4. **The reparameterization of weights w^l_{l1,l2} as w_{l1}·w_{l2}·w_l (line 146) reduces expressivity compared to the full rank-3 weight tensor.** The paper does not discuss the capacity trade-off or provide an ablation comparing the factorized vs. full weight parameterization at small L where the latter is tractable.

5. **No numerical verification of equivariance.** While the method is mathematically derived and the N-body sanity check provides indirect evidence, a direct numerical check (e.g., applying random rotations and measuring the difference) would strengthen the paper, especially given the non-trivial multi-step pipeline (SH → 2D Fourier → multiply → FFT → SH).

6. **No discussion of limitations.** The paper does not mention limitations (e.g., handling of parity, extension to general O(3) beyond rotations, potential numerical issues with FFT-based convolution on the sphere, boundary effects at the poles).

### Trivial

- The phrase "both form an orthonormal basis set for spherical functions" (line 120) is a minor technical imprecision as discussed above. The paper should clarify that each is a basis under its own inner product on L²(S²).

## Nice-to-Haves

- A numerical equivariance error report (applying random rotations and measuring deviation from exact equivariance).
- At small L, an ablation comparing the factorized weight parameterization (w_{l1}·w_{l2}·w_l) vs. the full rank-3 weight tensor.
- A citation to standard spherical harmonic transform references (e.g., Driscoll-Healy) to clarify the discretization underlying the basis conversion.

## Removed Points

- **"The claimed exact equivalence between tensor product computation and 2D Fourier multiplication is mathematically unsupported — this is a structural flaw."** — This criticism is factually incorrect. The spherical harmonics Y^m_l(θ,ψ) = P^m_l(cosθ)e^{imψ} involve associated Legendre polynomials P^m_l(cosθ), which are finite trigonometric polynomials in θ (degree ≤ l). The representation as a finite 2D Fourier series is exact for bandlimited functions, not approximate. The critic's argument about different inner products confuses orthonormality conditions with the existence of the expansion, which is a standard mathematical fact.

- **"The Fourier series in θ is infinite unless L is taken to infinity."** — Factually wrong. P^m_l(cosθ) expressed in terms of e^{iuθ} has finite bandwidth ≤ l.

- **"The performance claim on OC20 is confounded by the addition of a new operation (Selfmix), not by the Gaunt Tensor Product itself."** — Kept but downgraded from the critic's framing as a fatal confound to Minor. The OC20 result is a combined improvement from adding a new operation + efficient computation, but the paper's main claim is about efficiency, which is validated separately. The N-body sanity check provides the controlled ablation.

- **"The intended user would not know how to actually implement the method because the critical steps are underspecified."** — Kept but downgraded to Minor. The sparsity pattern and conversion formulas are given, though no algorithm for computing the coefficients is provided.

- Criticisms about missing appendix, missing proofs, or missing references — removed per instructions (parser strips appendix from submissions).

- The Strength Finder's generic strengths (e.g., "addressed an important problem") — removed as they are generic and not specific to the paper's evidence.

## Novel Insights

None beyond the paper's own contributions. The two reviewer inputs largely agree on the paper's core strengths (theoretical complexity reduction, empirical speedups) and converge on the main weaknesses (OC20 confound, missing implementation details). No novel synthesis emerges beyond what the paper already states.

## Suggestions

1. **Clarify the mathematical presentation of the basis conversion** — explicitly state that both spherical harmonics and 2D Fourier bases separately form bases (under their respective inner products) for bandlimited functions on S², and cite standard references (e.g., Driscoll-Healy sampling theorem) for the discrete conversion.

2. **Add a controlled ablation on OC20** — compare EquiformerV2 + CG-based Selfmix (at small L where tractable) vs. EquiformerV2 + Gaunt Selfmix to isolate the effect of the Gaunt parameterization.

3. **Include an algorithm or reference** for computing the conversion coefficients y^{l,m,*}_{u,v} in practice, to aid reproducibility.

4. **Discuss limitations** explicitly — parity, numerical stability, boundary effects — to improve the paper's completeness.

## Score and Decision

The paper introduces a theoretically sound and empirically validated method for accelerating E(3)-equivariant tensor products, with a clear complexity reduction from O(L⁶) to O(L³) and demonstrated speedups of 10–100× in practice. The mathematical core (Gaunt coefficient connection) is correct, the efficiency experiments are comprehensive, and the sanity check confirms no loss of expressivity. The weaknesses are minor and addressable: imprecise presentation of the basis conversion, a confounded OC20 performance comparison, and missing implementation details. The paper's primary contribution (efficiency) is well-supported, and its applicability across three operation classes demonstrates generality.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>
Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper provides a theoretical characterization of polynomial (and entire) tensor-valued functions equivariant under the orthogonal, indefinite orthogonal (Lorentz), and symplectic groups, and uses it to build machine learning architectures. The key results are explicit parameterizations (Theorem 1, Corollary 1 for O(d); Theorem 2, Corollary 3 for Lorentz/Sp(d)) that express equivariant functions as linear combinations of tensor products and isotropic tensors, with coefficients given by scalar functions of invariant inner products. The authors test the resulting architectures on three diverse problems — stress-strain prediction in materials science, path signature estimation for time series, and sparse vector recovery — showing that the equivariant models substantially outperform non-equivariant baselines.

## Strengths

- **Complete explicit parameterization of O(d)-equivariant tensor polynomials (Theorem 1, Corollary 1).** The paper provides a constructive, fully-characterized description of all O(d)-equivariant polynomial functions from tensors to tensors, expressed in terms of isotropic tensors (δ, ε) and invariant scalar functions. This is a clean synthesis of invariant theory into a form directly usable for building learnable architectures. Example 1 shows the recipe concretely for a simple case.

- **Extension to Lorentz and symplectic groups that prior methods do not cover (Theorem 2, Corollary 3).** The paper explicitly states (p. 2) that "Clebsch–Gordan–based methods... are specific for SO(d) and O(d) for d=2,3, whereas our method applies to other groups as well." The generalization to O(s,d‑s) and Sp(d) via the same invariant-theoretic framework is a genuine broadening of the literature, not an incremental modification.

- **Large and consistent performance gains across three diverse applications (Tables 1–3).** In the path-signature task (Table 2), the equivariant model reduces error from 0.071 (best baseline) to 0.002 for O(d) and from 0.186 to 0.005 for Lorentz — improvements of 35–70×. In the stress-strain task (Table 1), the proposed method outperforms all baselines including a prior equivariant method. In the sparse-vector problem (Table 3), the learned equivariant model exceeds the SoS methods in 8 of 12 settings, especially when SoS assumptions are violated. These results provide strong evidence that imposing the correct symmetries via this framework improves learning performance.

- **No Clebsch–Gordan coefficients required.** The parameterization avoids the need for CG decomposition, relying instead on isotropic tensors (Kronecker delta, Levi-Civita, and their Lorentz/symplectic analogues). This is a practical simplification relative to representation-theory-based approaches.

- **Learned equivariant models outperform theoretical SoS methods when assumptions are violated.** Table 3 shows that in the sparse-vector problem, the equivariant learned model matches or beats sum-of-squares methods when the covariance is non-identity (Random or Diagonal), while the SoS methods only excel under their strict assumptions (Identity covariance). This demonstrates the robustness of the learned approach.

- **Unified architecture across O(d), Lorentz, and Sp(d).** The same architectural template (Corollaries 1 and 3) works for all three groups by simply replacing the invariant inner product and invariant tensor. The path-signature experiments (Table 2) explicitly demonstrate both an O(d)-equivariant and a Lorentz-equivariant model built from the same procedure.

## Weaknesses

### Major

- **Unfair TFENN comparison in the stress-strain experiment (Table 1).** The TFENN baseline numbers are taken directly from Garanger et al. (2024) — reported as single values without variance — while the proposed method and all other baselines include standard deviations over 5 independent trials. Differences in dataset split, random seed, or training protocol could skew the comparison. The paper explicitly acknowledges this ("The TFENN errors are the results reported in Garanger et al. (2024)"), but this asymmetry undermines the quantitative claim that the proposed method "dramatically" outperforms a prior equivariant approach. The core claim of outperforming non-equivariant baselines still holds (those were rerun), but the head-to-head comparison with TFENN needs to be placed on equal footing.

### Minor

- **No experimental validation for the symplectic group.** The paper's scope explicitly includes Sp(d) and provides theoretical results for it (Section 4, Corollary 3). However, none of the three experiments involve a symplectic-equivariant task. While the theory is likely correct, the empirical component for Sp(d) is untested. A small synthetic experiment (e.g., learning a Hamiltonian vector field or another symplectic-structured problem) would have strengthened the completeness of the work.

- **General tensor-input architecture (Theorem 1) not implemented or tested.** The paper's most general result (Theorem 1) covers inputs of arbitrary tensor order and parity. The practical implementations (Corollaries 1 and 3) specialize to vector inputs, and the only non-vector experiment uses symmetric 2‑tensors via Corollary 2. The general multi-tensor-input case is never tested. The paper acknowledges computational limits, but a small higher-order example or a more explicit discussion of the practical domain of Theorem 1 would be valuable.

- **Missing limitations discussion.** The paper ends abruptly with Section 6 (Discussion), which is only a summary paragraph. There is no dedicated limitations section that acknowledges the practical restrictions: the architectures are limited to low output ranks (k′ ∈ {1,2,3,4}), the combinatorial cost for larger ranks, and the fact that experiments only cover O(d) and Lorentz (not Sp(d)). Adding a brief limitations paragraph would substantially improve the paper's candor and usefulness to practitioners.

### Trivial

- None that are not parser artifacts.

## Nice-to-Haves

- Rerun the TFENN baseline under identical train/test splits and report mean and standard deviation to place that comparison beyond reproach.
- Add a small symplectic experiment (e.g., a Hamiltonian dynamics regression task) to empirically validate the Sp(d) theory.
- Provide a more detailed complexity analysis for the expansion in (11), discussing how the number of terms grows with output rank k′ and what that implies for scaling beyond k′=4.

## Removed Points

- **"d_F/d_F" formatting artifact in Table 2 metric definition.** This is a PDF-parser artifact, not an author error. Removed per hard rules on formatting issues.
- **Criticism about the SoS method not being clearly named/referenced.** The paper cites Hopkins et al. (2016) and Mao & Wein (2022) and describes what the SoS methods do; this is adequate for a venue where the audience is expected to be familiar with these references. Removed as an overly nitpicky reproducibility concern.
- **Criticism about missing complexity analysis for (11).** The paper actually does provide a complexity expression: "O(k′! n^{k′} (Q d n² + d^{k′}))" and notes that "k′ ∈ {1,2,3,4} already captures many cases of practical interest." While a deeper discussion would be welcome (moved to Nice-to-Haves), the paper already addresses this. Removed as a claim that the paper lacks something it in fact contains.

## Novel Insights

The most interesting observation across the reviews is the relationship between the current paper and its earlier version ("Learning equivariant tensor functions with applications to sparse vector recovery," which scored 5.75 and was rejected). The earlier version had the same theoretical core but only the sparse-vector experiment; the addition of the stress-strain and path-signature applications substantially strengthens the empirical side and directly addresses the earlier reviewers' complaint about narrow experimental scope. This trajectory shows that the current paper is a significantly matured version that turned a theoretically-interesting-but-narrowly-validated contribution into one with demonstrated broad applicability.

## Suggestions

1. Rerun the TFENN baseline under the same conditions as the other methods and report mean ± std. If computational constraints prevent this, at minimum add a clear disclaimer about the asymmetry and discuss how different data splits might affect the comparison.
2. Add a brief Limitations paragraph (either in Section 6 or as a separate subsection) discussing the practical restrictions on output rank, the untested symplectic group, and the gap between Theorem 1's general tensor inputs and the implemented vector/two-tensor cases.
3. Clarify the metric formula in Table 2 — the current parsed text contains "d_F/d_F" which appears to be a formatting artifact.

## Score and Decision

I assign a score of **6.5**. This paper makes a solid theoretical contribution (explicit equivariant parameterizations for three classical groups, going beyond the CG-based methods) and validates it across three diverse applications with convincing performance gains. The main weakness — the unfair TFENN comparison — is fixable and does not undermine the core claim that equivariance helps (the non-equivariant baselines, which were properly rerun, are also outperformed). The unresolved issues (no Sp(d) experiment, no limitations section) are minor and do not threaten the paper's validity. Relative to the calibration anchors: this paper is clearly stronger than its earlier 5.75-scored version (which was rejected for narrow experiments) and is comparable to accepted papers in the 6.0–7.0 range. I recommend acceptance with minor revisions.

**Anchor calibration report:**
- *NukRlEUICA* (3.00, round 1): Affine invariance in CNNs — weaker theory and results; current paper is substantially stronger.
- *OopiU1q328* (2.00, round 1): Quasi-equivariant PowerNet — much weaker empirical support; current paper is stronger.
- *kyVzYpDxHg* (5.75, round 1/2): Earlier version of this paper (only sparse-vector experiment) — rejected. Current paper adds two more experiments and is clearly stronger.
- *79FVDdfoSR* (7.00, round 1): Characterization theorem for equivariant networks with pointwise activations — strong theory paper accepted at ICLR. Current paper has comparable theory depth but more diverse experiments; the TFENN issue and missing Sp(d) experiment keep it slightly below this anchor.
- *p34fRKp8qA* (6.83, round 1/2): Lie group decompositions for equivariant NNs — accepted. Comparable quality; current paper has cleaner theory but the TFENN issue.
- *tzpXhoNel1* (4.25, round 1): GRepsNet — rejected; current paper is significantly stronger.
- *LvTSvdiSwG* (5.00, round 1): EquiLoPO Network — accepted but with lower scores; current paper has stronger theoretical novelty.
- *SqMVI1GFnp* (5.50, round 2): Lie Neurons — rejected due to weak motivation and limited baselines; current paper is stronger.
- *smy4DsUbBo* (6.00, round 2): Energy-conserving equivariant GNN — accepted; current paper has stronger theoretical novelty but similar empirical quality.
- *64t9er38Zs* (5.75, round 2): Deep O(n)-equivariant hyperspheres — rejected; current paper is stronger.
- *5i6ZZUjCA9* (5.75, round 2): Affine steerable equivariant layer — accepted; similar quality but current paper has broader group coverage.

**Round 1 bracket:** [5.5, 7.5] — narrowed from the low (≤3.5) and high (≥7.5) bands, placing the paper clearly in the middle range above the weak/poor papers but below the top-scoring ones.

**Round 2 narrowing:** The most directly comparable anchor (kyVzYpDxHg, 5.75) is the earlier version of this paper; the current version is clearly a significant improvement. The 6.00 and 6.83 anchors are accepted papers of similar scope. The current paper sits between the 5.75 and 7.00 anchors, closer to the 6.83 anchor (Lie Group Decompositions) in overall quality, justifying a 6.5.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
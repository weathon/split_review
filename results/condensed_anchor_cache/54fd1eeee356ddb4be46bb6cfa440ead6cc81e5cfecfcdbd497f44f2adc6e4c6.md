- Decision: Accept
- Scores: 8, 8, 6, 5

## Merged Review

### Summary
This paper revisits the Hamming weight preserving ansatz for constrained variational quantum algorithms, links its expressivity and trainability to dynamical Lie algebra and overparameterization theory, and tests it on unitary approximation, ground state energy estimation (electron number constraint), and feature selection (feature count constraint). Reviewers generally agree the paper provides a useful synthesis of theory and extensive experiments, but opinions on novelty and contribution vary: two reviewers assign 8/8, one 6, and one 5. Positive reviewers highlight the clear theoretical framework and practical demonstrations; the more critical ones note that much of the material is review, that the trainability of the HW preserving ansatz was already established (e.g., arXiv:2303.16585), and that the core linking to subspace controllability is not sufficiently novel.

### Strengths
- Novel application of Dynamical Lie Algebra and overparameterization theory (via quantum Fisher information rank) to quantify expressivity of symmetry-preserving ansätze, with verification on unitary approximation.
- Very clear explanation of theoretical tools (DLA, controllability) and their relation to circuit design.
- Extensive numerical experiments on three representative tasks (unitary approximation, ground state energy, feature selection) using well-chosen baselines, showing positive results.
- Bottom-up approach to circuit design (guided by symmetry) compared to previous top‑down methods (e.g., Sim et al. 2019) that rely on sampling‑based expressivity measures.
- Hard constraints (HW preservation) are argued to be more favorable than soft constraints in industrial use cases requiring solution validity and robustness.
- Paper is well‑written with a clear structure and helpful appendices that provide background and additional details.
- Provides a nice summary of the HW preserving ansatz and its gate set (e.g., BS gate, controlled rotations) that generates all HW preserving unitaries (full controllability).
- Numerical experiments show modest but consistent improvement over existing methods.

### Weaknesses
- Literature review: it is unclear why previous XY‑mixer QAOA work is categorized as “soft constraints” given its circuit components (ZZ gates + mixer) already preserve Hamming weight.
- No analysis of the impact of bit‑flip (X) errors on NISQ hardware – such errors would break Hamming weight preservation. More discussion or simulation results under noise are needed.
- Trainability and Barren Plateau (BP) analysis is insufficient. Earlier work on FBS‑based circuits showed polynomial gradient decay; it is not discussed whether the same holds for the proposed ansatz.
- Numerical detail: the penalty weight α in Eq. 16 is chosen as [0.5, 1, 5, 10]; typically much larger values (e.g., 100) are used in practice – the choice and its effect need justification.
- Figure 2 uses gate infidelity as the metric for unitary approximation but plots “Success Probability” – it should be clarified whether this is a transformation of infidelity (e.g., log10(1e‑5)/log10(1e‑10) = 0.5).
- Missing discussion about connections between HW‑preserving VQE and XY‑mixer QAOA or other constrained QAOA variants.
- The basis set used for ground state energy estimation (e.g., STO‑3G) is not stated.
- The choice of feature selection as a test case is unusual – why is it a hard classical problem? More motivation is needed.
- Figure 4 shows many overlapping circuit ansatz lines (e.g., RBS‑full points are barely visible); revision with varied colors, sizes, or ordering is needed.
- Several typos: “relative” for “relatively”; “Haar measurement” for “Haar measure”; “Hartree‑Fork”; “the dimension of the dimension of DLA” (duplicated word); y‑axis of Fig. 3 and Fig. 7 should be logarithmic; “qubit” in Appendix B.1.
- The BS gate is artificial and not native to current hardware. Using parameterized XX rotations with single‑qubit Z rotations may be more practical. The provided decomposition using CNOTs (Fig. 5, Fig. 6) is unnecessarily complex for many architectures; alternative decompositions (e.g., with XX, YY, ZZ rotations) could improve practical applicability.
- The core contribution of linking trainability to subspace controllability is not sufficiently novel: the HW preserving ansatz’s trainability was already established (arXiv:2303.16585, though not explicitly linked to Larocca et al. 2023). The present work does not introduce a fundamentally new perspective or result beyond that.
- The specific advantage of using HW‑preserving ansatz for constrained VQAs (e.g., over the finance problems in arXiv:2303.16585) is not clearly articulated.
- In Eq. 8, should the maximization be over M such that M ≥ M_c?
- Where does the construction for the BS gate originate?
- The paper states it “revisits” the HW preserving ansatz – what are the specific improvements over previous proposals?
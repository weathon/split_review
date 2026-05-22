Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper makes three contributions to the theory and practice of separable neural networks (SepNNs): (1) a universal approximation theorem for CP, TT, and Tucker SepNNs via a clean Stone-Weierstrass argument; (2) an NTK analysis showing convergence to deterministic (infinite rank) and random (fixed rank) kernels, with spectral bias characterization; (3) a separable preconditioned gradient descent (SepPGD) method that factorizes the NTK-based preconditioner into per-factor smaller preconditioners to reduce computational cost. Experiments on kernel ridge regression, INRs, and PINNs demonstrate wall-clock speedups.

## Strengths

- **Universal approximation theorem for CP, TT, and Tucker SepNNs (Theorem 1, Section 2).** The proof via Stone-Weierstrass is clean, unified across architectures, and extends prior bivariate-only results (Cho et al., 2023) and sine-activation-specific results (Yu et al., 2024) to any non-polynomial activation. This fills a genuine gap in the SepNN literature.

- **First NTK analysis for SepNNs (Lemma 1, Theorem 2, Corollary 1, Section 3).** The paper derives the SepNN NTK explicitly, proves convergence to a deterministic kernel under infinite width and rank, and characterizes the fixed-rank random regime. The empirical validation in Figure 1 (four subplots showing convergence with width/rank and spectral decay) is convincing and supports the theoretical claims.

- **Concept of separable preconditioning (Definition 1, Section 4).** The idea of factorizing the preconditioner to operate on small n×n factor matrices instead of an n^D×n^D matrix is creative and well-motivated by the separable architecture. The equivalence to classical NTK-PGD for D=2 (Lemma 2) provides a solid theoretical anchor.

- **Consistent empirical acceleration across multiple domains (Figures 2–4).** SepPGD achieves lower MSE in less wall-clock time than plain SepNN training and the MSK baseline on kernel ridge regression, image INRs, 3D surface representation, and PINNs (including 3D diffusion, Klein-Gordon, and Helmholtz equations). The improvement is visually clear and consistent.

## Weaknesses

### Fatal
None.

### Major

- **Imprecise complexity analysis for SepPGD.** The paper claims O(nD) for "applying the preconditioner" (Table 1) and O(n^{D-1}) for the matrix product in (8) (footnote 3). However, the matrix product in (8) involves multiplying an (R × n^{D-1}) matrix by an (n^{D-1} × n) matrix, which costs O(R n^D) by naive multiplication — not O(n^{D-1}). Additionally, computing the second term ∑_{d=1}^D (R ×_d S_d) involves D mode-d tensor-matrix products, each costing O(n^{D+1}). While the claim that SepPGD is more efficient than O(n^D) classical PGD is likely still true (the factor eigenvalue decompositions cost O(D n^3) vs O(n^{3D})), the specific cost numbers given in the paper are not correctly derived. The central efficiency contribution needs a corrected and more transparent complexity analysis that separates per-iteration cost, preconditioner construction cost, and amortized cost under infrequent updates.

- **Overclaimed scope of the "provable" spectral bias alleviation.** The abstract and contributions list state that SepPGD "provably adjusts its NTK spectrum" and "provably adjusts the eigenvalue distribution of NTK matrix." The proof of equivalence to classical NTK-PGD (Lemma 2) and the spectral bias argument hold only for D=2. The paper explicitly says "It is believed that the result in Lemma 2 (and the analysis following) can be readily extended to multivariate cases D > 2" (line 208) — a conjecture, not a proof. However, neither the abstract nor the introduction carries this qualification. The paper should either provide the proof for D>2 or clearly qualify the scope of the theoretical guarantee.

### Minor

- **The spectral bias argument for D=2 is heuristic.** The reasoning after Lemma 2 (lines 208-209) uses "Suppose that K̃ is close to the true NTK matrix…" without formally establishing this closeness. The claim that "K̃ is close to the true NTK matrix" references Lemma 3 (in the appendix, which is stripped) but even then, the argument uses "can possibly be verified" and "We can ultimately show" rather than providing a rigorous bound. The D=2 case would benefit from a formal statement (e.g., bounding ‖K − K̃‖ in terms of network parameters).

- **No wall-clock time breakdown.** The paper plots MSE vs. wall-clock time but does not decompose the time into (a) factor NTK matrix construction, (b) eigenvalue decompositions, (c) computing M_d via the matrix product in (8), and (d) the factor network forward/backward passes. Without this breakdown, the claimed O(nD) efficiency cannot be fully separated from implementation optimizations.

- **No ablation of preconditioner update frequency.** The paper notes that the preconditioner is updated every ten iterations but does not ablate this choice to study the trade-off between construction cost and convergence speed.

- **Gap between asymptotic NTK theory and finite-width/rank practice.** Theorem 2 requires W → ∞ and R → ∞ for the deterministic kernel; Remark 2 bounds the drift as O(1/√W + 1/√R). The paper acknowledges this (Remark 3) and provides empirical validation (Figure 1), but does not examine how quickly the finite-width/rank approximation degrades. This is a standard limitation of NTK analysis rather than a flaw, but noting it would strengthen the paper.

### Trivial

- M_d is described as an "n-by-n" matrix in Remark 4 but is actually R×n (line 177). This minor inconsistency should be corrected.

## Nice-to-Haves

- A visualization of the eigenvalue distribution of K S̃ for the D=2 Kronecker-sum preconditioner, showing that the condition number actually improves, would strengthen the spectral bias argument.
- A complexity comparison with the mini-batch method of Shi et al. (2025) when applied **to SepNNs specifically** (i.e., SepNN + mini-batch MSK) would further clarify the regime where SepPGD is advantageous.
- Formalizing the D>2 extension using tensor Kronecker-product structure of the SepNN's NTK (acknowledged as a next step in line 208) would turn the conjecture into a theorem.

## Removed Points

- **Criticism that SepPGD's complexity is "incorrect" or "fatal."** The harsh critic claimed the matrix product cost is O(R n^D) and that this invalidates the paper's core claims. While the specific O(n^{D-1}) claim in footnote 3 is inaccurate, the overall efficiency advantage over O(n^D) classical PGD is still clearly real (factor eigenvalue decompositions cost O(n^3) vs O(n^{3D}), and factor NTK construction costs O(n^2 P) vs O(n^{2D} P)). The O(nD) entry in Table 1 refers to "applying the preconditioner" (per-iteration cost after M_d is constructed), consistent with how O(n^D) for Geifman et al. refers to the per-iteration cost of S·r. The issue is imprecision, not fundamental incorrectness. Accordingly, this is downgraded from Fatal to Major.

- **Criticism about missing comparison with mini-batch method of Shi et al. (2025).** The paper explicitly compares "SepNN (MSK)" in Figures 2–4 (lines 200, 228). MSK is the method from (Shi et al., 2025). This criticism is factually incorrect and removed.

- **Complaint about non-grid input extension being "not derived or validated."** The paper provides a formula (line 206-207) and states "We use this formulation to test SepPGD for non-grid inputs; see Section A.2." Since the appendix is stripped from the parser, this criticism cannot be verified and is removed.

- **Criticism that the spectral bias characterization (5) requires fixed NTK which requires large W,R.** This is standard NTK theory and acknowledged by the paper (Remark 2 provides bounds as O(1/√R) and O(1/√W) for the drift). The point is valid but well-understood and not specific to this paper.

- **Generic "Missing Experiments" and "Deeper Analysis" items** (scaling of gradient computation with D, rigorous proof for D>2) that are suggestions rather than factual weaknesses are moved to Nice-to-Haves.

- **Strength Finder's generic praise** about the problem being "important" without specific anchoring is dropped.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Correct the complexity analysis: provide explicit per-iteration cost (forward/backward passes), preconditioner construction cost (including the matrix product in (8) and the mode-d tensor products), and amortized cost under the chosen update frequency. Qualify the O(nD) entry in Table 1 to make clear it refers to per-iteration cost after preconditioner construction.

2. Qualify the "provably" claim in the abstract and introduction to reflect that the theoretical guarantee for spectral bias alleviation is established for D=2 with grid inputs, with D>2 remaining an empirically supported conjecture (or provide the D>2 proof).

3. Provide a wall-clock time breakdown in the experiments to empirically decompose the cost components.

4. Include an ablation of the preconditioner update frequency to validate the claimed efficiency trade-off.

5. Clarify the spectral bias argument for D=2 with a formal statement (bounding ‖K − K̃‖) rather than the current heuristic language.

## Score and Decision

**Originality:** 7/10 — Universal approximation theorem for SepNNs is novel; NTK analysis is a useful extension of existing frameworks; SepPGD is a creative adaptation.

**Importance of Research Question:** 7/10 — Understanding representation capacity and optimization of SepNNs is timely given their growing use in INRs and PINNs.

**Claims Support:** 5/10 — The approximation theorem and NTK analysis are well-supported. The SepPGD complexity and provability claims are overstated relative to the evidence provided.

**Soundness of Experiments:** 6/10 — Experiments show consistent speedups but lack ablation studies and cost breakdowns needed to fully verify the efficiency claims.

**Clarity of Writing:** 7/10 — Generally well-organized but the complexity analysis and scope of theoretical guarantees need clarification.

**Value to Community:** 7/10 — The approximation theorem, NTK analysis, and SepPGD algorithm are all potentially useful to researchers working with SepNNs.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
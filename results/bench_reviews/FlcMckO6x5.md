Now I have a thorough understanding of the paper and can write the final consolidated review.

---

## Summary

This paper establishes three theoretical foundations for separable neural networks (SepNNs): (1) a universal approximation theorem proving SepNNs can approximate any continuous multivariate function; (2) a neural tangent kernel (NTK) analysis characterizing convergence regimes under infinite/fixed rank, including spectral bias; and (3) a separable preconditioned gradient descent algorithm (SepPGD) that applies factor-wise NTK-based preconditioners at O(nD) cost for n^D grid-structured training points. Experiments on KRR, image/surface INRs, and PINNs demonstrate that SepPGD accelerates SepNN convergence over unpreconditioned training and prior NTK-based preconditioning methods.

## Strengths

- **Universal approximation theorem (Theorem 1):** The paper rigorously extends prior bivariate results (Cho et al., 2023) to D ≥ 2 variables and multiple SepNN forms (CP, TT, Tucker) using a clean proof combining Stone-Weierstrass with classical MLP universal approximation. The construction via Cauchy-Schwarz error bounds is sound and the result is proper.

- **Rigorous NTK analysis (Lemma 1, Theorem 2, Corollary 1):** The derivation of the SepNN NTK as a weighted sum of factor-MLP NTKs (Lemma 1) is neat and well-executed. The convergence proofs under joint width/rank scaling (Theorem 2) and fixed-rank regime (Corollary 1) are standard but correctly applied. Figure 1 provides convincing empirical validation of these asymptotic predictions.

- **Efficient and well-motivated SepPGD algorithm:** The core algorithmic idea—applying small n×n preconditioners factor-wise to exploit grid separability—is genuinely clever. The O(nD) per-iteration cost (Table 1) is a real computational improvement over prior NTK-based PGD methods (O(n^D) or O(n^D/p) with mini-batching). Lemma 2 proves equivalence between SepPGD and full NTK-based PGD with a Kronecker-structured preconditioner S̃ = S₁⊗I + I⊗S₂ for the bivariate case, connecting the algorithm to the established preconditioning framework of Geifman et al. (2024).

- **Thorough empirical validation and sensitivity analysis:** The paper tests across KRR, image representation, surface representation, and PINNs, with consistent convergence improvements. The appendix includes extensive sensitivity studies on rank R, modulation parameter k, preconditioner update frequency, activation functions (including Fourier features), network width, and noise levels—demonstrating robustness.

- **Efficient NTK matrix computation (Lemma 3):** The Kronecker-sum formulation for grid inputs is practically useful and enables the NTK-based analysis to be computationally feasible.

## Weaknesses

### Fatal

None.

### Major

- **The "provably" claim about spectrum adjustment is an overclaim (abstract, §4, conclusion).** The paper states that SepPGD "provably adjusts the eigenvalue distribution of the NTK matrix" (abstract, line 23) and "provably and efficiently adjust the spectrum" (§4, line 812). The supporting argument in §4 establishes: (i) Lemma 2—equivalence to NTK-based PGD with S̃ for D=2 (a genuine proof); (ii) heuristic eigenvalue reasoning—S_d has better-conditioned spectrum than K_Θ_d (by construction), therefore S̃ has better spectrum than K̃ (Kronecker sum of factor NTKs), and since K̃ ≈ K, KS̃ has better spectrum than K. This chain relies on verbal reasoning ("would have," "can possibly be verified," "suppose that") rather than formal bounds. No quantitative condition-number reduction is proved. The paper's own discussion (§A.1.2, lines 1177-1182) acknowledges this: "In future work, we can derive quantitative bounds on the condition number." The abstract and introduction should calibrate "provably" to reflect what is actually proved (Lemma 2's equivalence) vs. what is heuristically argued (the spectrum improvement). This can be addressed by revised wording in a rebuttal and does not undermine the algorithm's empirical effectiveness, but it is a notable overstatement of a core theoretical claim.

### Minor

- **Insufficient discussion of the SepNN-MLP accuracy gap.** The paper reports that standard MLP achieves PSNR Inf (perfect training-grid reconstruction) on image representation, while SepNN + SepPGD reaches only 33.30 dB (Figure 3). This reflects a fundamental capacity limitation of rank-constrained SepNNs. The paper does not explicitly discuss this speed-accuracy tradeoff, and the positive framing (showing SepPGD improvement over unpreconditioned SepNN at 26.48 dB) would benefit from acknowledging that SepNNs do not and are not expected to match the representational capacity of unconstrained MLPs.

- **Gap between infinite-rank NTK theory and finite-rank practice.** The spectral bias characterization (Eq. 5) and the convergence analysis require R → ∞ for a deterministic, fixed NTK. SepPGD is used in practice at finite ranks (e.g., R = 64–700). The paper acknowledges this in Remark 3 and §A.1.2, and the empirical results show SepPGD works at finite R, but the theoretical justification would be stronger with even a sketch of how the preconditioner's behavior relates to finite-rank dynamics.

### Trivial

- The KRR experiments use Adam with weight decay, which introduces implicit regularization beyond the preconditioner's effect. This follows prior work (Geifman et al., 2024) and the relative comparison with MSK remains fair, but it is worth noting.

## Nice-to-Haves

- A direct comparison of SepNN + SepPGD against other efficient INR architectures (e.g., SIREN, hash-grid encodings) would strengthen the practical efficiency claims, though this is partly outside the paper's scope of improving SepNN training and Fourier features are already included.
- Extending SepPGD to handle derivative-based PDE residual losses in PINNs, which the paper identifies as future work.
- Empirical visualization of the NTK eigenvalue distribution before and after preconditioning.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **"The claim that SepPGD provably adjusts the eigenvalue distribution is unsubstantiated" (Harsh Critic #1):** Partially valid but overstated. Lemma 2 is a genuine proof of equivalence to NTK-based PGD. The eigenvalue argument is heuristic but well-motivated by established NTK preconditioning theory. The issue is wording ("provably"), not absence of reasoning. Retained above as a major weakness with the correct framing.

- **"Experimental validation omits comparisons with contemporary efficient INR/PINN architectures" (Harsh Critic #2):** Scope creep. The paper's goal is to improve SepNN training, not to compete with all INR architectures. The paper does include Fourier feature baselines (Table 5). Requiring SIREN, hash encoding, etc., asks the paper to address a different question than the one it sets out to answer.

- **"The NTK convergence theorems require R→∞ while SepPGD is designed for finite rank" (Harsh Critic #3):** The paper explicitly acknowledges this in Remark 3 and §A.1.2. This is a known limitation of NTK theory in general, not unique to this paper, and empirical results at finite R validate the practical utility. Retained as a minor point above.

- **"Adam with weight decay confounds the preconditioner effect in KRR" (Harsh Critic #4):** The setup follows Geifman et al. (2024) exactly, and all compared methods use the same optimizer. The relative comparison is valid.

- **"The approximation theory contribution has limited novelty" (Harsh Critic):** The extension from bivariate to multivariate and from CP-only to CP+TT+Tucker is a genuine contribution beyond Cho et al. (2023) and Yu et al. (2024), and the proof technique is simpler and more general. This is properly scoped in the paper.

- **All formatting/parser-artifact criticisms:** These are parser issues, not author errors. Removed.

- **Missing appendix concerns:** The parser strips appendix sections; the original submission includes full proofs.

- **"No comparison with simple schedulers, second-order methods, or other preconditioners" (Harsh Critic):** The paper compares against MSK (Geifman et al., 2024) and the mini-batch variant (Shi et al., 2025). This is the most directly relevant baseline for NTK-based preconditioning.

- **Strength Finder's generic strengths** (e.g., "this paper addressed an important problem"): Dropped for being superficial or lacking specific citation.

## Novel Insights

The reviewers' discussion converges on an interesting tension: SepNNs exhibit spectral bias analogous to standard MLPs (validated both theoretically and in Figure 1(d)), yet their separable structure makes this bias addressable at dramatically lower computational cost—O(nD) vs. O(n^D). This suggests a broader principle: architectures that decompose computation along input dimensions may admit dimension-wise preconditioning strategies with complexity scaling linearly in D rather than exponentially. Whether similar Kronecker-structured preconditioning can be applied to other factorized architectures (e.g., tensor-decomposed weight networks, KAN layers) is an open and promising question raised implicitly by this work.

## Suggestions

1. **Revise the "provably" language.** Replace with phrasing like "designed to adjust" or "motivated by spectral analysis of," and move the formal statement to what Lemma 2 actually proves (equivalence to NTK-based PGD).
2. **Add a brief discussion of the SepNN-MLP accuracy gap** in the image representation section, framing it as an expected capacity-efficiency tradeoff rather than a shortcoming.
3. **Include a sketch or discussion** of how the finite-rank NTK (Corollary 1) relates to the preconditioner's expected behavior, even if a full proof is deferred to future work.
4. For the PINN experiments, clarify in the main text that SepPGD is applied only to data/IC/BC losses and not to PDE residual losses, with a note on why (derivative handling).

## Score and Decision

### Anchor Comparison

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| `bzhCJQz35M` (Weak-to-Strong Generalization) | 2.00 | Fundamentally flawed with math errors; our paper has no errors of comparable severity. Our paper is substantially stronger. |
| `DZKGX3wLGQ` (HyperINR) | 3.00 | Low novelty, missing baselines, misreported data. Our paper has genuine theoretical novelty and properly conducted experiments. |
| `P2m7gvtfrE` (Preconditioning Feature Learning) | 4.50 | Interesting theory but limited practical relevance, synthetic-only experiments. Our paper has broader theory and experiments across multiple real tasks. |
| `CXlsqTAf1E` (Preconditioned GD Convergence) | 5.00 | Good theory linking PGD to spectral bias/grokking, limited experiments, reviewers noted limited novelty. Our paper has more contributions and more extensive validation. |
| `0elvad3gEu` (NTK Width Selection) | 5.50 | Rigorous NTK theory with a practical application. Similar breadth of theory-to-practice contributions. Comparable quality. |
| `EB2Qgp5Vb0` (Learnable Product-Structured Activations) | 6.50 | Novel architecture with strong theory + thorough experiments across many domains. Our paper is weaker on architectural novelty and the "provably" overclaim. |

The paper makes three genuine contributions (approximation theory, NTK regimes, efficient preconditioning algorithm) with rigorous theory for the first two and a well-motivated, empirically validated algorithm for the third. The main weakness is the "provably" overclaim about spectral adjustment, which can be fixed with revised wording. Compared to anchors, the paper sits between the 5.0–5.5 range: stronger than CXlsqTAf1E (5.0) in breadth and empirical depth, comparable to 0elvad3gEu (5.5) in contribution quality, but below EB2Qgp5Vb0 (6.5) due to the overclaim and narrower architectural scope.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
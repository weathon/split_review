Now I have read the full paper. Let me write my review.

---

## Summary

This paper develops a comprehensive theoretical and algorithmic framework for Separable Neural Networks (SepNNs), which factorize multivariate functions into linear combinations of univariate factor networks. The three main contributions are: (1) a universal approximation theorem proving SepNNs (CP, TT, Tucker variants) can approximate any continuous multivariate function on compact sets; (2) derivation of NTK regimes—showing the NTK converges to a deterministic kernel under infinite width and rank, and to a random kernel under infinite width but fixed rank; and (3) a Separable Preconditioned Gradient Descent (SepPGD) algorithm that alleviates spectral bias with only O(nD) complexity for n^D training samples, an exponential improvement over prior O(n^D) methods. Experiments on KRR, image/surface representation (INR), and PINNs demonstrate consistent gains.

---

## Strengths

- **Exponential complexity reduction in SepPGD is well-motivated and rigorously grounded.** Lemma 2 formally proves the equivalence between the proposed SepPGD and classical NTK-based PGD (Geifman et al., 2024) for D=2, showing that the Kronecker structure of the preconditioner S̃ = S₁⊗I + I⊗S₂ allows computation in the O(n) space rather than O(n²). Table 1 cleanly summarizes the O(nD) vs. O(n^D) gap. This is a substantive algorithmic contribution.

- **The NTK analysis for SepNNs reveals a genuinely novel dichotomy.** Theorem 2 establishes deterministic NTK under joint infinite width/rank, while Corollary 1 shows fixed rank yields a stochastic kernel driven by Gaussian processes from the factor MLPs. This infinite-rank requirement (absent in standard MLP NTK analysis) is an original finding with practical implications—it explains why rank matters for optimization stability, not just approximation. The NTK Kronecker product structure (Section A.3) is additionally elegant and practically useful.

- **Experimental results are compelling across multiple tasks.** SepNN+SepPGD achieves PSNR 33.30 vs. SepNN's 26.48 and MLP's 26.64 on image representation (a >6 dB gain). Similarly, the PDE solver (Fig. 4) shows faster convergence and lower final MSE (0.037 vs. 0.042 vs. 0.092) under the same wall-clock time. The convergence curves consistently reflect the theoretical spectral bias alleviation claim.

- **Unified proof framework for universal approximation.** Using Stone-Weierstrass combined with classical universal approximation cleanly handles CP, TT, and Tucker in a single proof strategy, extending beyond the D=2 case (Cho et al., 2023) and the sine-activation–specific proof (Yu et al., 2024). Theorem 1 provides a more general and cleaner foundation than existing scattered results.

---

## Weaknesses

### Fatal
None.

### Major

- **The theoretical case for SepPGD under practical (finite rank) conditions is incomplete.** The paper acknowledges in Remark 3 that under fixed rank (the common practical setting), training dynamics "cannot be characterized uniformly using a fixed NTK matrix." Yet SepPGD's derivation and spectral bias argument in Section 4 relies on the NTK framework that strictly requires infinite rank. The spectral analysis of KS̃ (showing it has better conditioning than K) is sketched only for the deterministic NTK regime, leaving the practical justification for finite-rank SepNNs largely empirical. Given that all experiments use finite rank, bridging this gap is important.

- **The preconditioner S̃ = S₁⊗I + I⊗S₂ is a heuristic approximation to the optimal full preconditioner, and its quality is not fully analyzed.** Lemma 2 shows equivalence to a specific classical PGD with preconditioner S̃, but this S̃ is not the same as the full optimal NTK-based preconditioner S for the joint system. The paper argues (correctly) that S̃ has better spectrum than K̃ (Kronecker approximation to K), but the reasoning depends on K̃ being close to the true K, which is only informally verified via the NTK convergence results. A more careful bound on the spectral approximation error would strengthen the contribution.

### Minor

- **The approximation theory contribution (Section 2) is incremental relative to the existing literature.** The D=2 CP case was already proven by Cho et al. (2023); the extension to D>2 and TT/Tucker via Stone-Weierstrass is conceptually straightforward. The paper is transparent about this, but this section is better framed as a necessary foundation than as a standalone contribution.

- **Experiments are limited to modest-scale problems.** Image and surface representation use single samples; PDE experiments cover three equations. Demonstrating SepPGD at larger resolution (e.g., HD images, finer 3D meshes) or in multi-sample settings would more convincingly establish scalability.

### Trivial

- The statement in Remark 4 that preconditioner construction has complexity O(D(n³ + n²P)) while prior methods scale as O(n^{3D} + n^{2D}P) implicitly assumes P scales differently between the two settings, which deserves a brief note for clarity.

---

## Nice-to-Haves

- A theoretical or empirical analysis of the sensitivity to the hyperparameter k (top-k eigenvalue truncation for S_d) would help practitioners choose this value.
- Extending Lemma 2's equivalence argument to D>2 explicitly (even as a corollary) would close a small gap between the D=2 analysis and the multivariate algorithm.
- A wall-clock vs. PSNR comparison that includes the preconditioner construction cost would make the efficiency claims more complete.

---

## Novel Insights

The most novel insight in this paper is the **rank-dependent NTK dichotomy** for SepNNs: infinite rank is required to obtain a deterministic NTK, whereas fixed rank leads to a stochastic NTK governed by Gaussian processes from the factor MLPs. This is qualitatively different from standard MLP NTK analysis (where rank plays no role), and has immediate consequences for optimization stability and the validity of spectral bias characterizations. The subsequent observation that the SepNN NTK matrix admits a Kronecker product structure over grid inputs leads directly to the exponential complexity reduction in SepPGD—making the theory and algorithm tightly coupled rather than loosely related.

---

## Suggestions

- Provide at least an empirical or heuristic analysis of when the deterministic NTK approximation is a good stand-in for fixed-rank SepNNs (e.g., how small a condition number gap exists as a function of rank R).
- Extend the spectral improvement argument for S̃ vs. K to D>2 formally, even if briefly.
- Consider ablating rank R vs. convergence speed in experiments to connect the NTK theory (which predicts rank matters) to practice more concretely.

---

## Score and Decision

This paper presents a well-integrated theoretical and algorithmic contribution to understanding and optimizing separable neural networks. The SepPGD algorithm's exponential complexity reduction over prior NTK-based preconditioning is its strongest contribution, and the experimental improvements are substantial. The NTK rank dichotomy (deterministic vs. random under different rank regimes) is a genuinely novel theoretical finding. The paper's main weakness is that the theoretical grounding for SepPGD under practical finite-rank conditions is incomplete—the spectral bias alleviation argument depends on the infinite-rank NTK regime, while experiments operate in the finite-rank regime. This gap is acknowledged but not resolved. The approximation theory section is foundational but incremental. Overall, the combination of contributions is solid and valuable to the community working on efficient neural architectures for scientific computing.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
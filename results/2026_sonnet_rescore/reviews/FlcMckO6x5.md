Now I have sufficient information to write the final consolidated review. Let me verify one more claim about the NTK regime discussion.Now I have enough verified material to write the final consolidated review.

---

## Summary

This paper provides a comprehensive theoretical and algorithmic treatment of separable neural networks (SepNNs), which factorize multivariate functions into linear combinations of univariate MLPs. It makes three contributions: (1) a universal approximation theorem for CP, TT, and Tucker SepNNs, (2) an NTK regime analysis showing convergence to a Kronecker-structured deterministic kernel under joint infinite width and rank, and (3) a separable preconditioned gradient descent (SepPGD) that exploits the Kronecker structure to reduce preconditioning complexity from O(n^D) to O(nD). Experiments across kernel ridge regression, image and 3D surface INRs, and PINNs validate the algorithm's efficiency.

---

## Strengths

- **Universal approximation (Theorem 1)**: Rigorously establishes that CP, TT, and Tucker SepNNs can approximate any continuous function on compact sets using non-polynomial activations. This extends the bivariate CP result of Cho et al. (2023) to general D and multiple decomposition forms, closing an acknowledged gap in the theory.

- **NTK structure (Lemma 1, Equation 4)**: The NTK of a CP SepNN is derived as a weighted Kronecker sum of the factor NTKs, a clean and non-obvious structural result. The empirical validation in Figure 1 (panels a–c) independently tests fixed-rank stochasticity, joint W/R convergence, and NTK stability during training — a well-designed suite of checks.

- **Concrete and verified computational gain (Table 1, Remark 4)**: SepPGD reduces preconditioner application from O(n^D) to O(nD) and construction from O(n^{3D} + n^{2D}P) to O(D(n^3 + n^2P)). These are large, accurately-stated efficiency improvements rooted in the Kronecker factorization.

- **Broad experimental validation**: Results span diverse modalities — KRR (Fig. 2a), image representation (Fig. 2b, Fig. 3), 3D surface reconstruction (Fig. 3), and 3D PINNs (Fig. 4) — with consistently faster convergence per wall-clock time, supporting the paper's central practical claim.

---

## Weaknesses

### Fatal
None.

### Major

- **Abstract claims "provably" but the body does not deliver a proof.** The abstract states SepPGD "alleviates the spectral bias of SepNN by *provably* adjusting its NTK spectrum." The actual argument in Section 4 (line 201) uses "This can possibly be verified, because..." and "We can ultimately show that..." — explicitly hedged, informal language. The convergence and solution consistency guarantees for SepPGD relative to standard gradient descent are explicitly deferred: *"This is left for future research."* The word "provably" in the abstract and in the bullet on line 50 misrepresents the current state of the theory. A reader trusting the abstract will be misled. This should be corrected either by completing the proof or by re-scoping the language to "we argue that" or "we empirically demonstrate that."

- **Lemma 2 — the linchpin connecting SepPGD to NTK-based PGD — is proved only for D=2.** The statement (line 197) is explicitly $f_\Theta(\mathbf{x}) = f_{\Theta_1}(x_1)^\top f_{\Theta_2}(x_2) : \mathbb{R}^2 \rightarrow \mathbb{R}$. The D>2 extension is stated as: *"It is believed that the result in Lemma 2 (and the analysis following) can be readily extended to multivariate cases D > 2."* Since the practical experiments — 3D diffusion PINNs, 3D surface representation — involve D ≥ 3, the formal theoretical grounding for those experiments is incomplete. The Kronecker sum structure for D>2 and its relationship to the full NTK requires non-trivial verification. The gap between what is proved (D=2) and what is claimed and experimentally exercised (general D) is a meaningful methodological weakness, even if the empirical results are consistent with the extrapolation.

### Minor

- **The NTK theory is formally valid only in the R→∞ regime that no practical SepNN uses.** Corollary 1 and Remark 3 explicitly acknowledge that under fixed rank, the NTK is stochastic and "training dynamics cannot be characterized uniformly." The spectral bias characterization (Equation 5 and the eigenvalue decay argument) formally applies only when both W and R go to infinity simultaneously. The practical SepPGD uses small R for efficiency. Remark 3 acknowledges this and mentions empirical validation in Appendix Table 3, which is honest, but the paper's framing treats the theory and practice as more aligned than they are. A brief clarifying remark in the main text about how large R needs to be in practice would help.

- **No guidance on choosing the hyperparameter k (number of eigenvalues flattened by the preconditioner), and no sensitivity analysis.** The preconditioner $\mathbf{S}_d = \mathbf{I} - \sum_{i=1}^k (1-g(\lambda_i)/\lambda_i)\mathbf{v}_i\mathbf{v}_i^\top$ depends critically on k, which directly controls the quality of spectral adjustment. The paper says it follows Shi et al. (2025) but gives no guidance on how to choose k for SepNNs or how sensitive results are to this choice. Since k is the primary tuning knob for SepPGD, practitioners need at least a heuristic.

- **The approximation quality of the sum-of-logits pseudo-NTK for SepNNs is unaddressed.** SepPGD computes a pseudo-NTK for each factor MLP via sum-of-logits (Mohamadi et al., 2023). Whether this approximation is accurate for the Kronecker-structured factor NTKs specific to SepNNs is not discussed. Since preconditioner quality directly determines convergence improvement, even a brief empirical check (e.g., comparing pseudo vs. true factor NTK for small cases) would strengthen confidence in the method.

### Trivial

- The PINN final-accuracy improvement (SepPINN+SepPGD MSE 0.037 vs. SepPINN MSE 0.042, ~12% gain) is visually emphasized in Figure 4 alongside the output fields, which may overstate the benefit relative to the convergence speed claim — which is the paper's actual thesis. This framing choice could be made clearer.

---

## Nice-to-Haves

- **Comparison to spectral-bias-aware architectures (e.g., SIREN, positional-encoding MLPs)** in the INR experiments would sharpen the argument that SepPGD achieves comparable spectral coverage through optimization rather than architectural modification, complementing the paper's optimizer-focused thesis.
- **Practical guidance on R**: Given that the NTK theory requires R→∞ but experiments use small R, an informal discussion of what rank is "large enough" for the theory to be approximately relevant would bridge the theory-practice gap for practitioners.
- **Ablation on k**: A brief sweep of k values showing how convergence speed changes would help practitioners set this hyperparameter without guesswork.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic's concern about Stone-Weierstrass closure conditions for Tucker/TT not being verified in the main text.** The paper (line 82) states "We carefully examine that A meets these requirements" and defers the full argument to Appendix A.5. Per review policy, absent appendix content cannot be criticized — the parser strips appendices. Removed.

- **Harsh critic's suggestion to add SIREN/positional-encoding MLP baselines as a major flaw.** The paper's scope is explicitly the training of SepNNs via preconditioning, not a claim that SepNNs are SOTA INR architectures. Comparing against architecturally different spectral-bias-free models is scope creep. Moved to Nice-to-Haves.

- **Harsh critic's characterization of the PSNR comparison (33.30 vs. 26.48) as misleading.** Fig. 2 shows full convergence curves vs. wall-clock time, so the comparison is not limited to a single fixed-iteration snapshot. The visual in Fig. 3 is at matched iterations, which is a legitimate illustration of spectral bias effects. Not a flaw. Removed.

- **Strength Finder's "Explicit spectral bias formalization (Equation 5)" as an independent strength.** This is derivative of the NTK analysis and Lemma 1, not an independently verifiable contribution. Removed as a separate bullet; it is already subsumed by the NTK strength.

---

## Novel Insights

The most technically distinctive finding is Lemma 1 (Equation 4): the NTK of a CP SepNN decomposes as a weighted Kronecker sum of per-dimension NTK matrices, $K_\Theta(\mathbf{x},\mathbf{x}') = \frac{1}{R}\sum_{d=1}^D K_{\Theta_d}(x_d, x_d') \cdot \prod_{d'\neq d} \langle f_{\Theta_{d'}}(x_{d'}), f_{\Theta_{d'}}(x_{d'}')\rangle$. This structural result is non-obvious, and the subsequent exploitation of Kronecker algebra to achieve exponential complexity reduction in the preconditioner (O(nD) vs. O(n^D)) is a clean and practically significant corollary. The core insight — that the separability of the network architecture translates into separability of the NTK, which in turn enables separability of the preconditioner — is a genuinely useful conceptual contribution for anyone designing optimizers for tensor-factored networks.

---

## Suggestions

1. **Fix the abstract**: Replace "provably adjusts its NTK spectrum" with "empirically and theoretically motivates adjustment of its NTK spectrum" (or equivalent). Reserve "provably" for results where a formal proof is complete and present in the paper.
2. **Complete or re-scope Lemma 2**: Either prove the D>2 case explicitly (even under additional assumptions), or formally restrict the scope of SepPGD's theoretical justification to D=2 and present D>2 experiments as preliminary/empirical evidence.
3. **Add a k-sensitivity ablation**: A two- or three-value sweep of k in one experiment (e.g., image representation) placed in the appendix would substantially increase confidence in SepPGD's robustness.
4. **State the NTK stability bound explicitly in the main text**: Remark 2 defers the O(1/√R) and O(1/√W) stability bound to Appendix A.4. Stating the rate in the main text would help readers assess how large W and R must be for the theory to be informative.

---

## Evaluation Summary

**Originality**: The approximation theorem is incremental but well-executed; the NTK Kronecker structure (Lemma 1) and the derived SepPGD are original contributions. Moderate–high originality.

**Importance of research question**: SepNNs are an active area with applications in INRs and PINNs; principled theory and efficient optimizers are directly useful to the community. High importance.

**Claims supported**: The computational efficiency claim is fully supported. The spectral bias alleviation is empirically well-supported but formally overstated (the "provably" language in the abstract is not backed by a completed proof in the body). Moderate support.

**Soundness of experiments**: Well-designed, with execution-time axes, diverse tasks, and appropriate baselines. The theoretical regime (R→∞) used for justification does not match the small-R practical setting, though this is acknowledged. Moderate–good soundness.

**Clarity**: Well-written, logical structure, honest about gaps in Remarks 2–3. The main clarity issue is the mismatch between abstract language and body hedging. Good overall.

**Value to the research community**: Meaningful — provides a unified theoretical framework, a concrete efficiency improvement, and validated practical tools for SepNN users.

---

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>
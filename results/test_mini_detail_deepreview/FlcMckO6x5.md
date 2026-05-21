Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper makes three contributions to separable neural networks (SepNNs): (1) a universal approximation theorem covering CP, TT, and Tucker SepNN architectures via Stone-Weierstrass and universal approximation theory; (2) an NTK analysis for CP SepNNs in both the deterministic (infinite width and rank) and random (fixed rank) regimes; and (3) a separable preconditioned gradient descent method (SepPGD) that leverages the Kronecker-product structure of the SepNN's NTK to precondition training at O(nD) per-iteration cost for n^D grid-sampled points. Experiments on kernel ridge regression, image/surface INRs, and PINNs show that SepPGD accelerates convergence over baselines.

## Strengths

- **Universal approximation theorem for multiple SepNN architectures (CP, TT, Tucker).** Theorem 1 proves that all three architectures can approximate any continuous multivariate function on compact sets. The proof sketch uses the Stone-Weierstrass theorem combined with universal approximation of vector-valued MLPs, which is a clean and unified framework that extends prior results limited to the bivariate CP case (Cho et al., 2023). This is a genuine theoretical contribution.

- **NTK analysis with two distinct regimes.** Theorem 2 derives the limiting deterministic NTK under joint W,R → ∞, and Corollary 1 covers the fixed-rank, infinite-width regime where the NTK becomes a stochastic kernel. The paper correctly distinguishes these regimes and validates the convergence empirically (Figure 1). Lemma 1 provides a closed-form expression for the SepNN NTK as a sum over factor MLP NTKs, which is structurally insightful.

- **SepPGD algorithm with principled efficiency.** The method connects to classical NTK-based PGD (Geifman et al., 2024) via Lemma 2, showing that the separable preconditioner is equivalent to a Kronecker-sum preconditioner on the full NTK. The per-iteration gradient computation costs O(R n D) rather than O(n^D) for standard NTK-PGD, and the preconditioner construction scales as O(D n^3) rather than O(n^{3D}). This is a genuine and well-motivated complexity improvement.

- **Empirical validation across diverse tasks.** Experiments on KRR (noiseless and noisy), image representation (PSNR 26.48 → 33.30), 3D surface representation (IoU 0.983 → 0.992), and PINNs for PDE solving demonstrate consistent convergence speedups in wall-clock time across multiple application domains.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are supported by its theory and experiments.

### Minor

- **The O(nD) complexity headline glosses over the M_d construction cost.** The abstract and Table 1 state O(nD) complexity without qualification. However, constructing M_d in equation (8) involves a Khatri-Rao product and a matrix product whose cost scales as O(n^{D-1}) (acknowledged in footnote 3). While the paper correctly notes this cost is lower than the O(n^D) of standard NTK-PGD and that preconditioners are updated infrequently, the headline claim could mislead readers about the full per-iteration cost when preconditioners are freshly constructed. This is a presentation issue, not a technical error — the paper's efficiency advantage over prior work remains substantial — but the complexity analysis should be stated more precisely.

- **The spectral bias characterization relies on an asymptotic regime that may not hold in practice.** The deterministic NTK (Theorem 2) requires both W → ∞ and R → ∞. The random NTK regime (Corollary 1, fixed R) is acknowledged to not allow uniform fixed-NTK training dynamics (Remark 3). The spectral bias characterization in equation (5) therefore applies strictly only when both width and rank are large enough for the NTK to be nearly constant during training. In practice, rank is often small (R=10–50), and the paper does not reconcile this gap beyond noting empirical effectiveness. The experimental results are encouraging, but the theoretical link between SepPGD and spectral bias mitigation is cleaner under asymptotic conditions that may not match the deployment regime.

- **No per-iteration convergence curves.** All convergence plots show MSE vs. wall-clock time. Since SepPGD has faster per-iteration cost, time-to-solution improvements conflate cheaper iterations with genuine condition-number improvement. A per-iteration convergence curve for at least one experiment (e.g., KRR) would cleanly separate these effects and strengthen the spectral bias claim.

- **Ablation of rank R and preconditioner update frequency is missing.** The paper uses fixed settings for these hyperparameters but does not explore how SepPGD's convergence depends on the rank R or how often the preconditioner should be recomputed. These are important for understanding robustness and practical deployment.

- **MSK baseline is absent for SepNN in the PINN experiments.** Figure 4 compares SepPINN(SepPGD) against PINN and SepPINN, but not SepPINN+MSK. Since MSK is the primary prior-art baseline for NTK-based preconditioning, its absence in one of the three experimental settings makes the comparison less complete. (The MSK baseline is included in KRR and image experiments, so this is a partial omission.)

### Trivial

- Remark 4 states that SepPGD scales as O(nD) "by multiplying D n-by-n preconditioning matrices {M_d}", but M_d as defined in (8) is R × n, not n × n. This minor inconsistency in the remark should be aligned.

## Nice-to-Haves

- A per-iteration convergence curve would help separate the effect of faster iterations from genuine condition-number improvement.
- An ablation study of rank R and preconditioner update frequency would help users understand SepPGD's sensitivity to these hyperparameters.
- Extending the empirical validation of TT/Tucker SepNNs (which are covered by the approximation theorem but not tested) would strengthen the paper's breadth.

## Removed Points

- **Reviewer's claim that ⟨f_{Θ_d}(x̂_d), M_d⟩ costs O(R n²) for D=2:** This is factually wrong. The Frobenius inner product ⟨A,B⟩ = Σ_{i,j} A_{ij}B_{ij} for two R×n matrices is O(R n), not O(R n²). Removed as a factual error.

- **Complaint about Lemma 3 being in the appendix:** The paper parser strips appendix content from all submissions; Lemma 3 exists in the original submission. Removed per hard rules.

- **Criticism about missing related works:** Removed per hard rules — external verification of completeness is not possible.

- **Criticism about typos, formatting, or notation:** Removed per hard rules — these are parser artifacts, not author errors.

- **Strength Finder claims that are generic or unsupported:** Removed claims that were generic praise ("important problem", "addressed a gap") without specific evidence.

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder largely recapitulate the paper's own claims rather than contributing cross-cutting observations that the authors themselves missed.

## Suggestions

1. **Clarify the complexity accounting.** State explicitly in the abstract or introduction: "SepPGD's per-iteration gradient computation costs O(R n D); constructing the preconditioner M_d costs O(n^{D-1}) per update (which occurs infrequently)." This would eliminate the misleading impression from the bare O(nD) claim while keeping the compelling comparison against O(n^D).

2. **Add one per-iteration convergence curve** for the KRR experiment to demonstrate that SepPGD improves the effective condition number, not just wall-clock speed.

3. **Add an ablation study** showing how SepPGD's convergence varies with rank R (e.g., R = 5, 10, 50, 100) and preconditioner update frequency.

4. **Provide a two-sentence bridge** between the asymptotic NTK theory and practical finiteness: e.g., note that while the deterministic NTK requires W,R→∞, prior NTK literature (Lee et al., 2019; Arora et al., 2019) has shown that finite-width networks are often well-approximated by their infinite-width limits, and similarly moderate ranks suffice for the Kronecker-structure intuition to hold approximately.

## Score and Decision

**Round 1 bracketing:** I queried for anchors in three bands using topics related to the paper (separable neural networks, NTK-based preconditioning, spectral bias). The weak band (score < 3.5) returned papers averaging 2.3–3.0 that had major flaws (incorrect theory, lack of novelty). The middle band (3.5–7.5) returned anchors including "Inductive Gradient Adjustment for Spectral Bias in INRs" (avg 4.75, Reject), "Preconditioning for PINNs" (avg 5.00, Reject), "Generalization Bounds for KANs" (avg 6.20, Accept), and "Minimum Width for Universal Approximation" (avg 7.00, Accept). The strong band (7.5+) returned papers at 7.6–8.0 that are more polished, impactful, and free of structural weaknesses. **Initial bracket: between 5.0 and 7.0.**

**Round 2 narrowing:** I queried within (5.5, 7.0) and (6.0, 8.5) to find finer-grained anchors. "Generalizability of Neural Networks" (avg 6.00, Accept) and "Bayesian Treatment of Kernel Spectrum" (avg 6.33, Accept) are comparable-quality papers with solid but not exceptional contributions. **Comparison against anchors:** The current paper is clearly stronger than the IGA paper (4.75) — better theory, clearer writing, more principled method. It is comparable to the KAN generalization bounds paper (6.20) — both have solid theory and reasonable experiments. However, it has more minor unresolved weaknesses than the Minimum Width paper (7.00). The paper sits between 6.0 and 6.5.

**Final score: 6.0.** The paper makes three substantive contributions (approximation theory, NTK analysis, and an efficient algorithm) that fit together coherently. The weaknesses are all minor and addressable; none threaten the core claims. The complexity headline should be more precise, and a few ablations would strengthen the evaluation, but the overall package is solid and value-adding to the SepNN community.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>
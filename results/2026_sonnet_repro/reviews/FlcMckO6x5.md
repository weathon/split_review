Now let me run calibration searches to anchor the score.Now I have sufficient calibration data. Let me compose the final review.

---

## Summary

This paper provides a comprehensive theoretical and algorithmic treatment of separable neural networks (SepNNs), making three interrelated contributions: (1) a universal approximation theorem for CP, TT, and Tucker SepNNs (Theorem 1), extending prior bivariate results to general D; (2) a neural tangent kernel (NTK) characterization of SepNNs under infinite-width/infinite-rank (deterministic NTK, Theorem 2) and infinite-width/fixed-rank (stochastic NTK, Corollary 1) regimes, with associated spectral bias analysis; and (3) a separable preconditioned gradient descent (SepPGD) method that exploits Kronecker structure in the SepNN's NTK to reduce preconditioning complexity from O(n^D) to O(nD). Empirical validation spans kernel ridge regression, image/surface implicit neural representations, and physics-informed neural networks.

---

## Strengths

- **Universal approximation theorem (Theorem 1, Section 2):** Extends prior bivariate CP analysis (Cho et al., 2023) to multivariate CP, TT, and Tucker SepNNs using a unified Stone–Weierstrass + universal approximation argument. The proof sketch verifies that the separable function class A satisfies density in C(X) for the CP case, and the approach handles all three decomposition types under a single framework. This closes a genuine theoretical gap.

- **NTK decomposition result (Lemma 1, Equation 4):** The derivation of SepNN's NTK as a weighted sum of factor NTK matrices, K_Θ(x, x') = (1/R) Σ_d a_d(x)^T K_{Θ_d}(x_d, x'_d) a_d(x'), is technically non-trivial and structurally clean. Theorem 2 (deterministic NTK as W, R → ∞) and Corollary 1 (stochastic NTK under fixed R) are both empirically validated in Figure 1 with well-designed experiments across (a) fixed-rank convergence, (b) joint W/R convergence at initialization, (c) NTK stability during training, and (d) eigenvalue decay.

- **O(nD) complexity advantage (Table 1, Remark 4):** The computational reduction from O(n^D) preconditioning to O(nD) by decomposing the large preconditioner into D small n×n factor preconditioners is real, large, and correctly derived. Table 1 concretely situates SepPGD against prior methods. The construction complexity (O(D(n^3 + n^2P)) vs. O(n^{3D} + n^{2D}P)) is stated explicitly and accurately.

- **Empirical results:** Figures 2–4 report convergence in execution time (not iterations), which correctly reflects the wall-clock advantage. The PSNR 33.30 (SepPGD) vs. 26.48 (SepNN) vs. 26.64 (MLP) in Figure 3 is a large qualitative improvement. Convergence curves across KRR, INR, and PINNs consistently show SepPGD accelerating convergence relative to baselines.

---

## Weaknesses

### Fatal

None.

### Major

- **"Provably" in abstract vs. "left for future research" in body.** The abstract states SepPGD "provably adjusts its NTK eigenvalue distribution." Section 4 delivers an informal argument ("This can possibly be verified, because…", "We can ultimately show that KS̃ has better spectrum than K") and then explicitly defers: *"This is left for future research."* This is a direct contradiction between advertised and delivered theoretical content. Readers trusting the abstract will be misled. The underlying reasoning is plausible and the empirical results support the claim, but the paper does not provide the formal proof it claims to provide.

- **Lemma 2 proved only for D=2 while all practical experiments use D≥3.** Lemma 2—the linchpin connecting SepPGD to classical NTK-based PGD via the Kronecker sum S̃ = S₁⊗I + I⊗S₂—is formally stated and proved only for bivariate SepNNs. The multivariate generalization is handled by: *"It is believed that the result in Lemma 2 can be readily extended to multivariate cases D > 2."* This extension is not straightforward: the Kronecker sum S̃ for D > 2 has a more complex spectral structure, and the relationship to the full NTK of a D-variable CP SepNN requires separate analysis. Since all PINN experiments (D=3 diffusion, Klein-Gordon, Helmholtz) and surface representation (D=3) operate in exactly this unproved regime, the theoretical grounding for the primary experimental use cases is weaker than the paper presents.

### Minor

- **NTK theory applies to a regime (W→∞, R→∞) that no practical SepNN uses.** Corollary 1 and Remark 3 explicitly acknowledge that fixed-rank training dynamics cannot be characterized by the NTK framework. Since practical SepNNs favor small R for generalization, the formal spectral bias characterization (Equation 5) applies to the infinite-rank regime that practitioners never use. The authors are transparent about this, and the appendix (Table 3) provides some empirical evidence for small R, but the framing in the paper does not sufficiently flag the distance between theory and practice.

- **The modulation hyperparameter k is not ablated.** SepPGD's preconditioner flattens the top k eigenvalues of each factor NTK K_{Θ_d}. The choice of k directly controls convergence improvement and is practically important, but no sensitivity analysis or guidance for choosing k is given. This makes it difficult to reproduce or tune SepPGD in new settings.

- **PINN accuracy gains at convergence are modest.** Figure 4 shows SepPINN (SepPGD) MSE 0.037 vs. SepPINN MSE 0.042 (12% reduction). While the convergence speed improvement is clearer in the curve, the final-accuracy margin is small. The figure's visual emphasis on output fields could overstate the benefit.

### Trivial

None that survive the filtering rules.

---

## Nice-to-Haves

- Complete the proof of Lemma 2 for general D > 2. The paper already has the pieces—Kronecker structure of the NTK (Appendix A.3), equivalence for D=2 (Lemma 2), and the eigenvalue product argument for Kronecker sums. Formalizing these into a proposition for general D would bring the theoretical claims in line with the experimental scope.
- Convert the "can possibly be verified" argument in Section 4 into a formal proposition, even under stated assumptions (e.g., approximate Kronecker factorization of the NTK), so that the abstract's "provably" language is justified.
- Provide an ablation over k (number of preconditioned eigenvalues) and a brief discussion on setting R vs. the theoretical regime (R → ∞).
- The comparison is against MLP and SepNN baselines; a comparison against SIREN or positional-encoding MLPs (which address spectral bias architecturally) would sharpen the argument that SepPGD achieves comparable spectral-bias mitigation without architectural changes.

---

## Removed Points

*These points are flagged for removal — treat them with caution.*

- **Stone-Weierstrass conditions for TT/Tucker not verified in main text (harsh critic, Section 2).** The main text proof sketch only explicitly checks the CP case for the S-W conditions. However, the paper explicitly states proofs for all three cases are in Appendix A.5, and the rule against penalizing absent appendix sections applies here. Additionally, the paper's approach is conceptually sound for TT/Tucker (the product structure can be handled by rank increase arguments). Removed.

- **Comparison fairness with SIREN.** SIREN is cited but not compared against. However, the paper does not claim to outperform SIREN; SepPGD is positioned as an optimizer for SepNNs. Comparing against architectures designed to address spectral bias would be a nice-to-have, not a flaw. Moved to Nice-to-Haves.

- **Reproducibility / hyperparameter sensitivity beyond k.** Generic reproducibility concerns about learning rate, number of layers, etc. Per filtering rules, trivial implementation details not included in the paper should be removed.

- **Strength claim: "Explicit spectral bias formalization (Equation 5)"** — Equation 5 is the standard NTK convergence decomposition, not new to this paper (identical to Jacot et al., 2018; Shi et al., 2025). Removed as a claimed original strength; retained as useful background the paper correctly builds on.

---

## Novel Insights

The paper's most genuinely novel observation is the Kronecker product factorization of the SepNN NTK (Appendix A.3, Lemma 1), which shows that the multivariate NTK has a Kronecker structure that naturally decomposes across factor networks. This insight is what makes SepPGD possible: the large n^D × n^D preconditioner of classical PGD can be replaced by D small n × n preconditioners because the Kronecker structure of the preconditioner (S̃ = S₁⊗I + I⊗S₂) can be applied via vectorized matrix products (ABC) in O(n) rather than Kronecker products in O(n²). The random-vs-deterministic NTK dichotomy depending on whether R → ∞ (Theorem 2 vs. Corollary 1) is a clean and practically informative characterization of how rank acts as a regularity parameter for SepNNs, analogous to how width acts for MLPs.

---

## Suggestions

1. Revise the abstract to replace "provably adjusts" with language that accurately reflects what is proved (e.g., "the proposed SepPGD is equivalent to a classical NTK-based PGD with an explicitly constructed Kronecker-structured preconditioner, and we present evidence that this preconditioner improves the NTK eigenvalue distribution"). Keep "provably" only for results with actual proofs.
2. Either prove Lemma 2 for general D > 2, or explicitly scope the theoretical claims to D=2 and reframe the D > 2 experiments as preliminary empirical evidence consistent with the D=2 theory.
3. Add a short ablation on k in the appendix showing how convergence changes for k ∈ {small, moderate, large} on at least one task.
4. In Section 3, add at least an informal discussion of what values of R are "large enough" for the NTK stability (Remark 2) to hold approximately in practice, so that the gap between theoretical regime and experimental regime is explicit rather than implicit.

---

## Score and Decision

**Calibration summary:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| TNYLCF7vZA (Inductive gradient adjustment for spectral bias in INRs) | 4.75 | R1 | Closely related method (Shi et al. 2025 baseline); paper under review is more comprehensive with 3 contributions but has similar proof gaps |
| ydlDRUuGm9 (KAN expressiveness and spectral bias) | 6.25 | R1 | Similar structure (theory + algorithm); KAN paper delivers complete proofs, no "provably" gaps |
| Ge7okBGZYi (NTK analysis of multigrid parametric encodings) | 5.25 | R1/R2 | NTK analysis for INR architecture; accepted but narrow scope; paper under review is broader but has D>2 gap |
| 2C3CWCPxNS (Preconditioning for PINNs) | 5.00 | R2 | Preconditioning for PINNs with theory; rejected at 5.0; paper under review clearly stronger (broader theory, more tasks, explicit complexity advantage) |
| Oqk1Ui6m0n (Hessian-Free NGD for PINNs) | 5.00 | R2 | Second-order optimization for PINNs; rejected; paper under review stronger in theoretical depth |

**Round 1 bracket:** 4.75–6.25

**Round 2 narrowing:** The paper is substantially stronger than the 5.0 rejected papers (deeper theory, more tasks, genuine complexity gain). It is comparable to but weaker than the 6.25 KAN paper, which delivers complete proofs for all its claimed results. The core gap — "provably" in abstract but "left for future research" in body, and Lemma 2 D=2 only — is a real and non-trivial mismatch between claims and delivery. The paper sits between 5.25 (Ge7okBGZYi, accepted, narrower but complete) and 6.25 (KANs, accepted, broader and complete). Given the proof gaps center the paper at the lower end of this range: **5.5**.

**Axes:**
- *Originality:* Moderate-high. The three contributions are individually incremental but together form a novel theoretical+algorithmic package for SepNNs. The Kronecker factorization insight is genuinely new.
- *Importance:* High for the SepNN/INR/PINN community. SepNNs are gaining traction in scientific computing; a theoretical foundation has clear value.
- *Claims supported:* Partially. Approximation theory and NTK regime characterization are well-supported. Spectral bias "provably alleviating" is not formally proved.
- *Soundness of experiments:* Good. Time-based convergence reporting is appropriate; results are consistent across tasks.
- *Clarity:* Good. The paper is clearly organized; proof sketches are informative.
- *Community value:* High if the D>2 gap is closed. The current version is a meaningful step but incomplete.

**Decision:** Borderline reject. The paper's contributions are real and the theoretical framework is valuable, but the mismatch between the abstract's "provably" and the body's "left for future research," combined with Lemma 2 covering only D=2 while all practical experiments use D≥3, constitute meaningful overstatement of the theoretical contribution. These gaps are fixable in revision, but in current form the paper does not fully deliver what it advertises.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
Now let me synthesize the final review.

---

I've read the paper and carefully verified the reviewer claims against the actual content. Let me now produce the consolidated review.

## Summary
This paper provides a theoretical and algorithmic framework for separable neural networks (SepNNs). It proves a universal approximation theorem for multivariate SepNNs in CP, TT, and Tucker forms using Stone-Weierstrass; derives the NTK regimes under both infinite-rank/fixed-rank asymptotics; and proposes SepPGD, a preconditioned gradient method that exploits the Kronecker structure of the SepNN's NTK to reduce preconditioner cost from O(n^D) to O(nD) for grid-structured data with n^D samples. Experiments on KRR, INR-based image/surface representation, and PINNs show SepPGD accelerates wall-clock convergence.

## Strengths
- **First universal approximation theorem for multivariate SepNNs (CP, TT, Tucker).** Theorem 1 fills a clear gap in the literature. The proof via Stone-Weierstrass + universal approximation is clean, covers D≥2, and subsumes the prior bivariate-only result of Cho et al. (2023). This is a concrete, verifiable theoretical contribution.

- **Rigorous NTK characterization under two asymptotic regimes.** Lemma 1 derives the CP SepNN NTK; Theorem 2 shows convergence to a deterministic kernel when both width and rank →∞; Corollary 1 shows convergence to a random kernel under fixed rank. These results are empirically verified with variance plots over 10 seeds (Fig. 1), and they go beyond standard NTK analysis by explicitly treating the decomposition rank as an asymptotic parameter. The spectral bias characterization (Eq. 5) is standard but correctly applied to SepNNs.

- **SepPGD algorithm with O(nD) complexity and proven equivalence to classical PGD for D=2.** Definition 1 is fully specified. Lemma 2 proves that for D=2, SepPGD's factorwise update is equivalent to the full NTK-based PGD of Geifman et al. (2024) with preconditioner S̃ = S₁⊗I_n + I_n⊗S₂, while requiring only O(nD) per iteration (Table 1) instead of O(n^D). The complexity improvement is dramatic and well-documented.

- **Empirical validation across three distinct tasks (KRR, image/surface INRs, PINNs) with consistent speedups.** The experiments use real metrics (PSNR, IoU, PDE error) and show SepPGD accelerates convergence across all settings. Visual results (Fig. 3) demonstrate improved reconstruction quality under equal iteration counts for surface representation. The appendix includes additional experiments (image inpainting, additional PDEs).

## Weaknesses

### Major
- **"Provably adjusts the NTK spectrum" is overstated relative to what is actually proven.** The abstract and contributions list claim SepPGD "provably" adjusts the NTK spectrum. However, the theoretical argument in Section 4 is a sketch rather than a theorem: the paper says "This can possibly be verified" and "Suppose that K̃ is close to the true NTK matrix K which can be verified using the NTK matrix formulation in Lemma 3." No explicit bound on ‖K − K̃‖ is stated in the main text, and the claim that K·S̃ has "better spectrum" than K does not follow rigorously from the comparison of S̃ to K̃ without additional spectral approximation guarantees. The use of "could provably" in Section 4 itself is hedged, but the abstract and contributions do not carry this hedge. The algorithm is empirically effective and the motivation is sound, but the paper's strongest advertised claim is not matched by the evidence provided in the main text.

- **The equivalence between SepPGD and a full preconditioner is proven only for D=2; the D>2 case used in experiments lacks the same theoretical justification.** Lemma 2 is explicitly restricted to D=2, and the paper states "It is believed that the result in Lemma 2 (and the analysis following) can be readily extended to multivariate cases D > 2." Definition 1 provides the algorithm for arbitrary D, and the 3D surface and 3D PDE experiments use SepPGD without a proven connection to any full NTK preconditioner. Since the main efficiency claim of SepPGD scales with D, the lack of formal justification for D>2 weakens the theoretical contribution.

### Minor
- **Convergence curves are plotted against execution time, not iteration count, making it difficult to isolate the effect of the preconditioner on the optimization trajectory from the effect of reduced per-iteration cost.** The paper explicitly states it uses time-based plots "because the efficiency advantage of SepNN and SepPGD comes from the lower complexity in an iteration." While this is a valid choice for demonstrating practical speed, it conflates two distinct effects. The surface representation and PINN experiments include some iteration-matched comparisons (Fig. 3 right, Fig. 4 right visual examples), but the main convergence curves in Figs. 2 and 4 (left) lack iteration-based plots. Adding iteration-count curves for at least one experiment would cleanly separate the preconditioner's effect on spectral bias from the computational speedup.

- **No error bars or variance estimates on the main optimization convergence results (Figs. 2 and 4 left).** The NTK verification in Fig. 1 properly shows variance over 10 seeds, but the core convergence experiments do not report statistical variability. While the trends appear clear, single-run curves are insufficient to assess the significance of observed speedups.

- **The approximation theorem (Theorem 1) does not provide a quantitative bound on the required rank R for a given accuracy ε.** The result is existential — it shows SepNNs are universal approximators — but does not characterize how R must scale with D and the target function's regularity. This limits its practical utility compared to the qualitative insight.

### Trivial
- Footnote 3 in Table 1 notes that the matrix product in (8) has complexity O(n^{D-1}), but the table entry reads O(nD) without qualification. The footnote explains the relative magnitude, but the table is slightly misleading without it.

## Nice-to-Haves
- An NTK eigenvalue distribution comparison before and after applying SepPGD (e.g., for a small 2D grid) would visually confirm the claimed spectral adjustment.
- A discussion of how SepPGD relates to other factorized preconditioners such as KFAC would help contextualize novelty.
- A brief limitations paragraph (e.g., when the Kronecker structure breaks for non-grid data or very high D) would improve rigor.

## Removed Points
The following points from the harsh critic are removed under the filtering guidelines:
- "Missing comparison to full NTK preconditioner applied to SepNN (even if prohibitively slow)" — REMOVED: asking for a comparison the paper explicitly states is infeasible due to O(n^D) complexity.
- "The paper does not discuss when SepPGD might fail" — REMOVED: this is a scope requirement, not a paper flaw; no paper is required to enumerate failure modes.
- "Missing related works like KFAC, Shampoo" — REMOVED: the reviewer did not verify these comparisons exist in the appendix; also "do not mention missing related works" rule applies.
- "The paper does not state the number of seeds for optimization experiments" — REMOVED: the paper provides a code link; trivial reproducibility nitpick.
- "The proof sketch for approximation theory is not surprising" — REMOVED: surprisingly is not a valid weakness criterion.
- "The NTK efficiency advantage is a missed opportunity to connect to SepPGD" — REMOVED: the paper does connect the Kronecker structure (Appendix A.3) to SepPGD's efficiency; this is a misreading.
- "The image inpainting result is mentioned but not shown in the main paper" — REMOVED: standard practice for space-constrained papers; the appendix exists for this.
- "The SepPGD presentation is dense and the notation is hard to verify" — REMOVED: presentation density is a style nitpick, not a substantive weakness.

## Novel Insights
None beyond the paper's own contributions. The strength finder and harsh critic substantially agree on the paper's core contributions and limitations; no new synthesis emerges from their combination beyond what each independently states.

## Suggestions
1. Soften the "provably" claim in the abstract and contributions to reflect what is actually proven (equivalence for D=2, empirical demonstration). Alternatively, provide a complete theorem with explicit bounds in the main text.
2. Add at least one iteration-count convergence curve to separate the preconditioner's effect on optimization trajectory from the computational speedup.
3. Add variance/error bars to the main convergence experiments (Figs. 2, 4).
4. Explicitly state the D>2 case as an empirical extension rather than claiming the theory "readily extends" without proof.
5. Consider including a quantitative bound linking approximation accuracy to rank R as a corollary or remark.

## Score and Decision

### Calibration Report

**Round 1 — Bracketing:** Initial bracket [5.0, 7.5] based on:
- Weak band (<3.5): anchors at 2.0–3.2 — clearly below this paper
- Middle band (3.5–7.5): relevant anchors include "On the Convergence Behavior of Preconditioned Gradient Descent" (5.00), "How Does Preconditioning Guide Feature Learning" (4.50), "On the Spectral Differences Between NTK and CNTK" (6.00)
- Strong band (>7.5): anchors at 8.0–8.5 — papers from different subfields with cleaner contributions

**Round 2 — Narrowing:** Retrieved anchors in (4.5, 6.0) and (6.0, 7.5):
- Q2D1PI6zY1 (avg 5.00): Universality of equivariant networks — pure theory, narrower scope than this paper; this paper is stronger
- buuwRBYfrP (avg 4.67): KAN convergence — mixed reviews, narrow setting; this paper is stronger
- vokk8t1gnp (avg 5.33): Weak correlations/linearization — theory-only; comparable quality but different topic
- 2Q0U2rV2Jz (avg 5.50): Multi-index learning — theory paper; this paper has more breadth
- U6SnDgI3gG (avg 6.00): NTK/CNTK spectral comparison — accepted poster, cleaner theoretical contribution but narrower scope; comparable to this paper
- xDLE5n3x9Y, X63V2CWjj3, VOK6LNaZ3N (avg 6.50): Stronger theory papers with oral/poster acceptances; this paper has weaker theoretical guarantees

**Final score rationale:** 6.0. The paper makes genuine contributions (approximation theorem, NTK analysis, efficient algorithm) and the empirical validation is solid. However, the gap between the "provably" claim and the actual theoretical argument, combined with the D>2 justification gap, prevents it from reaching the 6.5+ tier where papers have cleaner theoretical support. The paper is clearly stronger than the 4.5–5.5 range papers which have narrower scope or weaker empirical support. Comparable to the 6.00 NTK spectral paper.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
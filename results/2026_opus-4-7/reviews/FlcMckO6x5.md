## Summary
The paper studies Separable Neural Networks (SepNNs) — multivariate functions factorized via CP/TT/Tucker tensor decompositions of univariate factor MLPs — and contributes three things: (i) a universal approximation theorem (Theorem 1) for CP/TT/Tucker SepNNs, (ii) NTK regimes (Theorem 2: deterministic NTK under W,R→∞; Corollary 1: random NTK under fixed R), and (iii) SepPGD, an O(nD) preconditioned gradient descent shown equivalent to standard NTK-based PGD for D=2 (Lemma 2), with experiments on KRR, image/surface INRs, and 3D PINNs.

## Strengths
- Unified Stone–Weierstrass + Leshno-Pinkus argument covers CP, TT, and Tucker SepNNs for general D≥2 (Theorem 1), extending Cho et al. 2023 (D=2 CP only) and the sine-activation-specific argument in Yu et al. 2024 via a simpler, more general proof.
- Lemma 1 gives a clean factorized NTK decomposition K = (1/R) Σ_d a_d^⊤ K_{Θ_d} a_d that is the technical bridge enabling both Theorem 2 and the factor-wise preconditioner construction.
- SepPGD reduces preconditioner application from O(n^D) to O(nD) and construction from O(n^{3D}+n^{2D}P) to O(D(n^3+n^2P)) (Table 1, Remark 4); Lemma 2 proves exact equivalence to classical NTK-PGD with Kronecker-sum preconditioner at D=2.
- Dual NTK regimes (deterministic with W,R→∞; random with fixed R) acknowledge and analyze the low-rank regime practitioners actually use, with consistent empirical validation in Fig. 1(a–c).
- Wall-clock gains across four task families (KRR, image INR, surface INR, 3D PINNs); e.g., PSNR 26.48 → 33.30 on image INR (Fig. 3).

## Weaknesses

### Fatal
None.

### Major
- **The "provably adjusts the NTK spectrum" headline claim is not actually proved.** The argument (p.8, after Lemma 2) reads "This can possibly be verified…" and "Suppose that K̃ is close to the true NTK matrix K… We can ultimately show that KS̃ has better spectrum than K." This is a sketch resting on two unverified suppositions, not a theorem. The only formal equivalence (Lemma 2) is for D=2 with the Kronecker-sum preconditioner S̃ = S_1⊗I + I⊗S_2; extension to D>2 is asserted ("It is believed that the result in Lemma 2 … can be readily extended") but not proved, despite SepPGD being benchmarked at D≥2. The strongest claim in the abstract is overstated relative to what is established.
- **Theory/practice regime mismatch.** The spectral-bias narrative driving SepPGD (Eq. 5 and surroundings) presumes a fixed NTK, which Theorem 2 only provides as W,R→∞. Corollary 1 + Fig. 1(a) and Sec. 3 ("the rank R of SepNNs is often chosen to be smaller") show that in practice the NTK is stochastic; Remark 3 explicitly defers fixed-R training-dynamics analysis to future work. The motivation for SepPGD therefore applies cleanly only outside the typical deployment regime.

### Minor
- No reported seed variance on the convergence curves (Figs. 2–4); the single-image / single-surface qualitative results are not aggregated over a benchmark.
- No Adam (or K-FAC) baseline applied to SepNN, only vanilla GD and MSK; for a "use this optimizer" claim this is the most natural comparison.
- The headline O(nD)-vs-O(n^D) advantage scales with D, but experiments stop at D=3; a D≥4 demonstration would directly test the regime where the gain is largest.
- Theorem 2 is proved only for two-layer factor MLPs; Remark 1 punts the multi-layer extension.
- The 1/√R scaling inside the SepNN definition (footnote 1) is needed for NTK convergence but not the normalization used in the applied SepNN literature cited; this gap between analyzed and deployed model deserves to be flagged in the main text rather than footnoted.
- Wall-clock-only convergence plots are sensitive to implementation; per-iteration plots would help separate algorithmic from engineering speedups.

### Trivial
- Eq. (8) is dense; a worked D=3 example in the main text would aid readability (only D=2 is unrolled).

## Nice-to-Haves
- Generalize Lemma 2 to D>2 with an explicit preconditioner family and replace the verbal spectrum argument with a quantitative κ(KS̃) vs. κ(K) bound.
- Either analyze SepPGD on the random NTK of Corollary 1, or sweep R empirically to show benefits do not depend on the W,R→∞ regime.
- Add seed-variance bands, an Adam-on-SepNN baseline, and at least one D≥4 experiment.

## Removed Points
These points are flagged to be removed; treat them with caution.
- "Three contributions are loosely coupled" (harsh critic): framing critique, not a concrete defect; the UAT, NTK, SepPGD form a coherent representation/optimization arc and the paper does not claim a chained derivation.
- "UAT is routine Stone–Weierstrass" (harsh critic): correctness is conceded and the extension to CP/TT/Tucker for general D is a legitimate contribution; significance assessment is subjective.
- Strength Finder's panel-by-panel Figure 1 endorsement and "first comprehensive theoretical treatment" framing — kept only where backed by specific theorems.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- Either upgrade the SepPGD spectrum claim from sketch to theorem (D>2, explicit κ bound) or downgrade the abstract wording from "provably adjusts" to "empirically/heuristically adjusts."
- Add seed-variance bands and per-iteration plots; include an Adam-on-SepNN baseline.
- Add at least one D≥4 experiment.
- State explicitly in the main text the regime where the NTK theory is faithful and what it does not say about fixed-R SepNNs.

## Calibration anchors
- /…/xpmDc76RN2.md — avg 2.33 (R1 weak) — operator-network optimization theory; thinner contributions than this paper.
- /…/kkVTeMvC9D.md — avg 3.40 (R1 weak) — training Jacobian analysis; less applied scope.
- /…/2NwHLAffZZ.md — avg 2.33 (R1 weak) — NTK linearization theory; weaker results.
- /…/fUz6Qefe5z.md — avg 3.00 (R1 weak) — NTK with derivative labels; narrower than this paper.
- /…/TNYLCF7vZA.md — avg 4.75 (R1 mid; closest anchor) — Shi et al. 2025-style NTK gradient adjustment for INR spectral bias. Very topically close (and cited by this paper); this paper extends to separable architectures with broader theory but inherits similar overclaim/evidence concerns.
- /…/2C3CWCPxNS.md — avg 5.00 (R1 mid) — PINN preconditioning with condition-number theory; cleaner theorems, narrower scope.
- /…/b6juTJZ1I9.md — avg 5.00 (R1 mid) — alternating preconditioned GD for matrix sensing; tighter convergence proofs than this paper's spectrum-sketch.
- /…/YN4uWzcbtt.md — avg 4.25 (R1 mid) — NTK positive definiteness; pure theory.
- /…/AoraWUmpLU.md — avg 8.00 (R1 strong) — Neural ODE NTK activation analysis; sharper theory, accepted; this paper is weaker on rigor.
- /…/P7KIGdgW8S.md — avg 8.00 (R1 strong) — Hölder stability of GNNs; very different topic.
- /…/STUGfUz8ob.md — avg 7.60 (R1 strong) — transformer abstract reasoning; off-topic anchor.
- /…/uKZdlihDDn.md — avg 7.60 (R1 strong) — diffusion GNs for fluid sim; off-topic.
- /…/7Cx05z4pUc.md — avg 5.00 (R2) — SVD-based decomposed learning; weaker theory.
- /…/SkeoEFlF0E.md — avg 4.75 (R2) — neural CP tensor decomposition; methodologically adjacent, rejected.
- /…/NxLWeK4P3q.md — avg 5.00 (R2) — group-equivariant UAT; comparable rigor level.
- /…/8wAL9ywQNB.md — avg 6.00 (R2) — expressive-power generalization bounds; accepted; sharper theory than this paper.
- /…/Oqk1Ui6m0n.md — avg 5.00 (R2) — Hessian-free natural gradient for PIML; closely related optimization, rejected.
- /…/Tkkrm3pA35.md — avg 5.25 (R2) — GNN preconditioners; broadly accepted, less ML-theoretic.

Round-1 bracket: [4.0, 6.0], anchored most tightly to TNYLCF7vZA (4.75) and 2C3CWCPxNS (5.0). Round 2 narrowed within (4, 6.5): the closest anchors (TNYLCF7vZA 4.75, 2C3CWCPxNS 5.0, SkeoEFlF0E 4.75, Oqk1Ui6m0n 5.0) cluster near 5. This paper has a broader contribution arc than TNYLCF7vZA but a clearer overclaim ("provably" without proof for D>2) and thinner experiments (no seed variance, no Adam baseline), and the spectral-bias justification applies most cleanly outside the typical SepNN regime. Net: comparable to or slightly below the TNYLCF7vZA/2C3CWCPxNS cluster.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
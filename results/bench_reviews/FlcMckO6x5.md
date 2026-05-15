Now I have all the evidence I need. Let me produce the final consolidated review.

---

## Summary

This paper makes three contributions to the theory and practice of Separable Neural Networks (SepNNs): (1) a universal approximation theorem showing CP, TT, and Tucker SepNNs can approximate any continuous multivariate function on compact sets; (2) a characterization of SepNN NTK regimes (deterministic under infinite width+rank, random under fixed rank) with spectral bias analysis; and (3) an efficient separable preconditioned gradient descent method (SepPGD) that exploits the Kronecker structure of SepNN's NTK over grid inputs to achieve O(nD) per-iteration cost for n^D samples, along with an equivalence to classical NTK-based PGD (Lemma 2). Experiments on kernel ridge regression, image/surface representation via INRs, and PINNs demonstrate wall-clock speedups.

## Strengths

- **First universal approximation theorem for multivariate SepNNs across multiple decomposition formats.** Theorem 1 proves that CP, TT, and Tucker SepNNs can approximate any continuous multivariate function on compact sets, extending prior work (Cho et al., 2023) from the bivariate CP case. The proof approach (Stone-Weierstrass + universal approximation of vector-valued MLPs) is elegantly simple and unifies the analysis across decomposition types. The paper correctly notes this subsumes earlier bivariate results.

- **Systematic NTK analysis of SepNNs with both deterministic and random regimes.** Lemma 1 derives the NTK of CP SepNNs; Theorem 2 shows convergence to a deterministic kernel under infinite width and rank; Corollary 1 characterizes the random kernel under fixed rank. The spectral bias analysis (Section 3, Eq. 5) connects NTK eigenvalues to convergence rates, providing the first rigorous account of how SepNNs learn different frequency components. Figure 1 empirically validates the NTK convergence behavior over multiple seeds.

- **Formal connection between SepPGD and classical NTK-based PGD with O(nD) complexity.** Lemma 2 proves that SepPGD is equivalent to the classical PGD of (Geifman et al., 2024) in the bivariate case, with the preconditioner taking the explicit Kronecker-sum form \\(\tilde{\mathbf{S}} = \mathbf{S}_1 \otimes \mathbf{I}_n + \mathbf{I}_n \otimes \mathbf{S}_2\\). Table 1 shows SepPGD's per-iteration cost is O(nD) vs. O(n^D) for standard NTK-based PGD — an exponential improvement that makes preconditioning feasible for grid-based SepNN training. The equivalence proof is rigorous and correctly leverages the identity \\((\mathbf{C}^\top \otimes \mathbf{A})\mathrm{vec}(\mathbf{B}) = \mathrm{vec}(\mathbf{ABC})\\).

- **Diverse empirical validation across four tasks.** The method is tested on kernel ridge regression (noisy/noiseless), image representation, 3D surface representation with INRs, and three PDEs (diffusion, Klein-Gordon, Helmholtz) with PINNs. SepPGD consistently achieves lower MSE and faster convergence than MLP, SepNN, and MSK-preconditioned baselines.

## Weaknesses

### Major

- **The claim that SepPGD "provably adjusts" the NTK spectrum is not fully supported by the reasoning presented.** The abstract and introduction assert that SepPGD "provably adjusts the eigenvalue distribution of NTK matrix" and "provably alleviates spectral bias," but the actual argument in Section 4 (lines 203-208) relies on hedged language: "This can possibly be verified," "Suppose that \\(\tilde{\mathbf{K}}\\) is close to the true NTK matrix \\(\mathbf{K}\\) which can be verified using the NTK matrix formulation in Lemma 3," and "the proposed SepPGD **could** provably... adjust the spectrum." Lemma 2 (equivalence to classical PGD with a Kronecker-structured preconditioner) is rigorously proven, and the spectral reasoning about \\(\tilde{\mathbf{S}}\\) vs. \\(\tilde{\mathbf{K}}\\) is directionally correct. However, the gap from factor-level spectral improvement to full-NTK spectral improvement (the "closeness" of \\(\tilde{\mathbf{K}}\\) to \\(\mathbf{K}\\) and the transfer of spectral conditioning to \\(\mathbf{K}\tilde{\mathbf{S}}\\)) is acknowledged as unverified by the paper's own text. The paper overstates what is actually proved. The authors should either close this gap or downgrade the "provably" language to reflect the heuristic nature of the spectral claim.

### Minor

- **No error bars or multi-seed statistics for main experimental results.** Figure 1 reports statistics over 10 seeds, but Figures 2-4 (KRR, image representation, surface, PINNs) show single-run convergence curves and single-instance visual results without error bars or confidence intervals. While time-to-solution plots with error bars are uncommon, it is unclear whether the PSNR/IoU improvements in Figure 3 (e.g., SepPGD achieves PSNR 33.30 vs. SepNN's 26.48 on the bird image) are representative or cherry-picked. Reporting results over multiple seeds would strengthen the empirical claims.

- **Convergence is primarily shown against wall-clock time, not iterations, partially conflating efficiency gains with genuine spectral bias alleviation.** The paper states (line 228): "Because the efficiency advantage of SepNN and SepPGD comes from the lower complexity in an iteration, we plot the convergence curve w.r.t. execution time rather than iteration number." This is a reasonable choice for demonstrating practical speedup, but it makes it difficult to disentangle whether SepPGD improves per-iteration convergence rate (spectral bias alleviation) or merely computes iterations faster. The surface representation results ("under the same iteration number," line 232) and PINN results ("under the same iteration," line 234) partially address this concern, but the main convergence curves (Fig. 2, Fig. 4) are time-based. Presenting iteration-based plots alongside time-based ones would cleanly separate the two effects.

- **The extension of the UAT proof to TT and Tucker is stated without a sketch in the main text.** The main text (Section 2) describes the proof sketch only for the CP case. While the full proof is in Appendix A.5 (which is stripped by the parser), the main text would benefit from at least noting how the Stone-Weierstrass conditions (especially closure under multiplication) extend to TT and Tucker representations, since the function classes have different algebraic structures. A brief indication of the argument would improve readability.

### Trivial

None.

## Nice-to-Haves

- An empirical comparison of SepPGD against SepNN trained with a simple learning-rate schedule tailored to the factor NTK eigenvalues would provide a more natural baseline for spectral bias alleviation (though this is a non-standard baseline and not required).
- Showing the eigenvalue distribution of \\(\mathbf{K}\\) vs. \\(\mathbf{K}\tilde{\mathbf{S}}\\) for a small synthetic problem would visually confirm whether the condition number is indeed reduced, directly supporting the spectral bias alleviation claim.
- A brief discussion of how the factor preconditioners \\(\mathbf{S}_d\\) are constructed in practice (which modulation function \\(g\\) is used and how \\(k\\) is chosen) would improve reproducibility.

## Removed Points

These points were raised by reviewers but are removed per policy:

- **TT/Tucker UAT not covered in appendix/insufficient proof:** Removed because the full proof is in Appendix A.5, which the parser strips. Per policy, missing appendix content is a parser artifact, not an author error.
- **\\(1/\sqrt{R}\\) scaling missing from approximation theorem:** Removed because the paper explicitly addresses this in footnote 1 (line 125): "which does not affect the universal approximation Theorem 1."
- **Lemma 3 not presented in main text:** Removed because the lemma is part of the appendix (stripped by parser). The paper defers to it appropriately.
- **Missing related works / formatting / typos:** Removed per policy (parser artifacts; lack of external sources to verify missing related works).
- **Reproducibility nitpicks about undisclosed hyperparameters:** Removed per policy (trivial implementation details).

## Novel Insights

None beyond the paper's own contributions. The paper's main insights — that SepNNs are universal approximators via Stone-Weierstrass, that their NTK decomposes into factor NTKs with deterministic/random regimes, and that the Kronecker structure of the NTK over grids enables efficient preconditioning — are clearly articulated by the authors. The reviews do not introduce additional novel interpretations.

## Suggestions

1. **Tone down the "provably" claim** in the abstract and introduction, or close the gap in the spectral argument. The paper's genuine contributions (Lemma 2 equivalence, O(nD) complexity, empirical speedups) are strong enough to stand without overselling the theoretical justification of spectral adjustment. Replace "provably adjusts" with "empirically adjusts" or "provably adjusts (under the equivalence to classical PGD with factor-preconditioners)."

2. **Add iteration-based convergence plots** (e.g., MSE vs. iteration) alongside the time-based plots for KRR and image representation, at least in the appendix. This would cleanly separate the efficiency advantage from the spectral bias alleviation effect.

3. **Report multi-seed statistics** for the key quantitative results (final PSNR/IoU/MSE) across at least 5 random seeds with mean and standard deviation.

4. **Add a small-scale eigenvalue visualization** showing the spectrum of \\(\mathbf{K}\\) vs. \\(\mathbf{K}\tilde{\mathbf{S}}\\) for a bivariate problem (e.g., small \\(n\\)), which would directly substantiate the spectral adjustment claim.

## Score and Decision

**Calibration anchors used** (from human-reviewed corpus, avg human score shown):

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/CXlsqTAf1E.md` (PGD + spectral bias) | **5.00** | Similar topic; the current paper has more theoretical breadth (UAT + NTK + algorithm) but also a more significant overclaiming issue. Roughly comparable quality. |
| `/home/wg25r/review_agent/human_reviews_2026/P2m7gvtfrE.md` (preconditioning + feature learning) | **4.50** | That paper was rejected for shallow observations and limited realism. The current paper has substantially stronger theoretical contributions. |
| `/home/wg25r/review_agent/human_reviews_2026/Q3yLIIkt7z.md` (scaling laws, feature learning) | **7.00** | More mathematically rigorous and complete theory. The current paper is less tight theoretically but has broader scope (UAT + NTK + algorithm + experiments across 4 tasks). |
| `/home/wg25r/review_agent/human_reviews_2026/UJvkXnuozY.md` (Tucker-FNO, UAT) | **5.00** | Very similar paper structure (UAT + tensor decomposition + experiments). The current paper adds NTK analysis and a PGD algorithm beyond UAT. |
| `/home/wg25r/review_agent/human_reviews_2026/U6SnDgI3gG.md` (NTK spectral differences) | **6.00** | Cleaner, more focused claims but narrower scope. The current paper is broader but has the overclaiming liability. |
| `/home/wg25r/review_agent/human_reviews_2026/rDhCPKrZw7.md` (PINN convergence) | **3.00** | Weaker overall; the current paper is significantly stronger in both theory and experimental breadth. |
| `/home/wg25r/review_agent/human_reviews_2026/bP6eScSxm2.md` (spectral algorithms) | **5.33** | Sound theory paper rejected partly for overstating connections to NNs. The current paper has a similar weakness (overclaiming "provably") but stronger empirical validation. |

The paper makes genuine contributions — the UAT for CP SepNNs, the NTK characterization, and the SepPGD algorithm with proven equivalence to classical PGD and exponential complexity reduction — but is hampered by overclaiming the theoretical support for spectral bias alleviation and limited statistical rigor in experiments. The theoretical contributions (UAT, NTK analysis) are solid; the algorithmic contribution (SepPGD) is practically valuable but oversold. Positioned relative to the calibration anchors, the paper sits in the 5.0 range — it has more theoretical content than the 4.5-level reject but less mathematical completeness than the 7.0 Oral.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
Now I have a good calibration set. Let me compile my final analysis.

**Round 1 bracket**: Based on the initial searches, I placed this paper between the weak anchors (avg ~3.0) and strong anchors (avg 8.0), likely in the 4.5–6.5 range. Papers in the middle band (avg 6.0–6.33) like Wasserstein Flow Matching, Wasserstein Proximal Algorithm, and Continuous GWOT all had weaknesses around insufficient experiments or theory-practice gaps. The current paper has a similar profile but with a **more severe** evaluation gap for GPCAGEN.

**Round 2 narrowing**: 
- PGPCA (avg 7.33, Accept) — significantly stronger experimentally; the current paper is clearly below this.
- WFM (avg 6.33, Reject) — somewhat comparable in "interesting idea + incomplete evaluation" but had at least some quantitative comparison; the current paper has weaker GPCAGEN eval.
- Continuous GWOT (avg 6.20, Reject) — similar profile but with a stronger experimental analysis component.
- Wasserstein Proximal (avg 6.0, Reject) — closer to the current paper in having a solid theoretical core and weak experiments.

The current paper's Gaussian GPCA experiments are well-done (100 trials, 10 runs, cost comparisons validating Proposition 4). But GPCAGEN — arguably the paper's main contribution — has no quantitative validation at all. This pulls the score down more than for the anchors that at least attempted quantitative evaluation.

Final score: **5.5** — The paper has genuine theoretical substance (Gaussian GPCA) and a principled approach (GPCAGEN via Otto's geometry), but the absence of quantitative evaluation for the main algorithmic contribution is a decisive gap that prevents acceptance in current form.

Let me write the final review.

Let me list all anchors for reporting:

**Round 1 anchors:**
1. /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/9WG1ga39Dq.md — avg 3.00 — Consistent OT; weak paper
2. /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/FjifPJV2Ol.md — avg 3.40 — Schrödinger Bridge; weak paper
3. /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/Bh4BW69ILq.md — avg 2.60 — Unbalanced OT; weak paper
4. /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/F5UgXkPgSn.md — avg 3.00 — Grassmannian fusion; weak paper
5. /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/RmOXAa5H5Y.md — avg 3.00 — Simplicial Wasserstein; weak paper
6. /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/WPz5e5V85k.md — avg 6.00 — Wasserstein Proximal; theory paper with experimental gaps
7. /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/HB4lr0ykTi.md — avg 6.33 — Wasserstein Flow Matching; interesting idea, weak experiments
8. /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/rY8xdjrANt.md — avg 6.20 — OT Barycenter; algorithm with evaluation issues
9. /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/CrOHzVtWmH.md — avg 3.80 — RW distance; lower quality
10. /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/EKaVO0ceh8.md — avg 6.00 — Projection OT; decent paper
11. /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/cNmu0hZ4CL.md — avg 8.00 — Neural population dynamics; strong paper
12. /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/g7ohDlTITL.md — avg 8.00 — Flow Matching; strong paper
13. /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/TTrzgEZt9s.md — avg 8.00 — DRO; strong paper
14. /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/sbG8qhMjkZ.md — avg 8.00 — SVGD; strong paper
15. /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/4xWQS2z77v.md — avg 8.00 — Loss landscape; strong paper

**Round 2 anchors:**
16. /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/kvByNnMERu.md — avg 5.25 — Shape distances; mixed quality
17. /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/EyWKb7Ltcx.md — avg 5.00 — SPD manifolds; mixed
18. /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/4IRYGvyevW.md — avg 5.60 — Feature learning; mixed
19. /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/DZxU0q2S11.md — avg 5.75 — Network widths; okay
20. /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/mkDam1xIzW.md — avg 7.33 — Probabilistic GPCA; stronger paper
21. /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/HB4lr0ykTi.md — avg 6.33 — WFM (already listed)
22. /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/gxhRR8vUQb.md — avg 7.00 — Diffeomorphic mesh; strong
23. /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/sRaAt9OOnW.md — avg 6.20 — Continuous GWOT; similar profile

The current paper is clearly below PGPCA (7.33) — PGPCA had proper experiments with quantitative comparisons. It's below the diffeomorphic mesh paper (7.00) which had thorough evaluation. It's below Wasserstein Flow Matching (6.33) in terms of evaluation completeness (WFM at least had some quantitative comparison). It's comparable to the Wasserstein Proximal paper (6.0) and Continuous GWOT (6.20) in terms of having genuine contributions held back by experimental gaps, but I'd argue the current paper's GPCAGEN evaluation gap is MORE severe because there's NO quantitative validation at all.

Score: 5.5Now let me write the final consolidated review.

---

## Summary

This paper proposes two algorithms for Geodesic PCA (GPCA) in Wasserstein space: (1) a closed-form-inspired solution for centered Gaussian distributions using Bures-Wasserstein geometry (lifting to GL_d), and (2) a neural-network-based method (GPCAGEN) for general absolutely continuous measures using Otto's parametrization. The Gaussian case is handled rigorously with theoretical characterization of when GPCA differs from Tangent PCA, while GPCAGEN avoids input-convex neural networks by leveraging Otto's construction where the geodesic-defining function need not be convex.

## Strengths

- **First exact GPCA solver for ℝᵈ-valued probability measures that does not linearize Wasserstein geometry.** The paper fills a gap identified in the literature (line 26): prior work either linearized (TPCA), restricted to 1D, or used generalized geodesics. The Gaussian case (Proposition 3, Section 3) provides a clean solution via lifting to GL_d with optimization over rotation matrices Q_i ∈ SO_d.

- **The Gaussian GPCA analysis is theoretically rigorous and well-evaluated.** Proposition 4 gives a closed-form expression (equation 14) quantifying TPCA distortion as a function of eigenvalue ratio (a−b)/(a+b) and orientation θ, validated experimentally with systematic cost-improvement curves (Figure 4 right, up to ~35% improvement). Proposition 5 proves GPCA stays Gaussian in 1D. The experiments use 100 trials with 10 runs and honest reporting of the <1% average improvement in generic settings.

- **GPCAGEN's use of Otto's parametrization (equation 9) avoids input-convex neural networks.** This is a genuine architectural simplification: as the paper emphasizes (line 92), f need not be convex in Otto's formulation, unlike McCann's parametrization which requires convex u and thus ICNNs. This is a practical insight that opens a cleaner parametrization path.

- **Intellectual honesty about limitations.** The paper transparently reports that GPCA and TPCA differ by <1% in cost for generic 2D Gaussian settings (line 208), candidly discusses when GPCA can be "worse-behaved" (boundary projections, poor separation), and acknowledges the open question of whether GPCA stays Gaussian for multivariate data (line 150).

## Weaknesses

### Major

- **GPCAGEN evaluation is purely qualitative with no reported objective values.** This is the most significant weakness. For the paper's main algorithmic contribution (GPCAGEN for general a.c. measures), every experiment (MNIST, 3D point clouds, landscape images) is qualitative — the reader is shown interpolations along learned geodesics (Figures 5, 6) and asked to accept they "capture meaningful modes of variation." Critically:
  - No value of the objective ℒ (equation 15) — the quantity the algorithm is supposed to minimize — is ever reported.
  - No convergence curves during training are shown.
  - No quantitative comparison against any baseline on a shared task is provided (clustering purity, reconstruction error, classification accuracy, etc.).
  
  For a paper whose central claim is a new algorithm solving a well-defined optimization problem (equation 1), the absence of any numerical evidence that the algorithm actually achieves low cost on that problem is a decisive gap that prevents assessing whether GPCAGEN works as claimed.

### Minor

- **The "exact" claim is somewhat overreaching for GPCAGEN.** The abstract states methods are "exact in the sense that they do not rely on a linearization of the Wasserstein space, and the components are true geodesics that minimize the cost in equation 1." For GPCAGEN, the objective minimized (equation 15, line 168) uses Sinkhorn divergence S_ε as an approximation of W_2². The entropic bias means the objective is not exactly equation 1. While the paper acknowledges the Sinkhorn approximation (line 168), the abstract and contributions do not qualify the "exact" framing, which could mislead readers about the gap between the geometric ideal and the implemented algorithm. (The components are true geodesics geometrically, but the optimization minimizes an approximation of the stated cost.)

- **No ablation study or sensitivity analysis for the regularization coefficients λ_I, λ_O.** The paper states λ_I = λ_O = 1 "ensures the algorithm works as expected in all experiments" (line 256) without showing supporting evidence. Given that ℐ enforces equality of diffeomorphisms in Diff(Ω) — a strong condition — the behavior under different λ values is unclear. The paper references Appendix E, but even with an appendix, the main text contains no diagnostic that constraint satisfaction or violation evolves during training.

- **Computational cost and practical runtime are not discussed.** GPCAGEN involves second-order Hessian eigenvalue computations (backward-through-Hessian), differentiation through Sinkhorn iterations, and joint optimization over n scalar t_i plus MLP parameters. No runtime or scaling information is provided, making it impossible to assess practical viability.

- **No sensitivity analysis for the Sinkhorn blur parameter ε or batch size m.** Both are free parameters that control the approximation bias and optimization quality; their chosen values and stability are not discussed in the main text.

### Trivial

- The diffeomorphism constraint (I_d + tH_f(x) ≻ 0) is enforced only on m Monte Carlo samples (line 168). The paper acknowledges this, but it means the "geodesic" interpretation is not guaranteed at unobserved points.

## Nice-to-Haves

- Report convergence curves and final objective values for GPCAGEN on the experiments shown.
- Provide an ablation study on λ_I, λ_O over at least one to two orders of magnitude, showing how constraint satisfaction and data-fitting cost trade off.
- Compare GPCAGEN and TPCA on a proxy quantitative task — the paper already has labeled categories (chairs vs. armchairs, hanging vs. standing lamps) that could support clustering purity or classification accuracy.
- Report stability of learned geodesics across random seeds.
- Discuss sensitivity to the choice of reference measure ρ.

## Removed Points

These points from the reviews are removed with justification:

- **"GPCAGEN declines to compare to TPCA, sidestepping evaluation"** — The paper gives a valid reason (TPCA acts on discrete measures; continuous-vs-discrete comparison is not directly meaningful, line 264) and shows qualitative TPCA results in Appendix A.2. The real weakness is the absence of *any* quantitative metric, not the choice of baseline. Removed because the specific criticism about declining comparison is not a flaw per se.

- **"Practical significance of Gaussian GPCA is unclear"** — The paper is transparent about the <1% difference in generic settings (line 208) and discusses when GPCA matters (pathological eigenvalue cases, Figure 4). Honest reporting of limitations is a strength, not a weakness.

- **"No higher-order components shown"** — The paper describes how to compute higher-order components (line 198) and demonstrates the first two, which is standard for PCA papers. Not a missing element.

- **"Choice of reference measure ρ not explored"** — This is a design choice. Exploring every design alternative is not required.

- **"Geodesic constraint enforced only at sample points"** — The paper acknowledges this limitation; it is a practical constraint addressed in the text. Moved to Trivial.

- **Formatting, typo, and parser artifact complaints** — These are parser errors, not author errors.

- **Speculation about missing appendix content** — The parser strips appendix sections; they exist in the original submission.

- **"No discussion of whether GPCAGEN recovers known geodesics with quantified error" on MNIST** — The MNIST experiment constructs a synthetic ground truth (digit shape + color variation) and shows the method recovers it qualitatively. While quantified error would strengthen the evaluation, calling this a fatal omission is excessive — it falls under the broader "no quantitative metrics" criticism already captured as Major.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Report the achieved value of equation 15 (or its Sinkhorn approximation) for each experiment, with convergence curves during training.** This is the most basic sanity check for whether GPCAGEN solves the optimization problem it claims to solve.
2. **Add quantitative comparison on a proxy task** — even if "direct" TPCA comparison is imperfect, clustering purity on labeled categories (chairs vs. armchairs) or reconstruction error would ground the qualitative improvements.
3. **Ablate λ_I and λ_O** over a range (e.g., 0.01, 0.1, 1, 10) and show constraint satisfaction vs. cost trade-off.
4. **Report runtime** and scaling behavior with d and n, and specify the chosen ε and m values.

## Score and Decision

**Round 1 (Bracketing):** Searched across low (avg <3.5), middle (3.5–7.5), and high (>7.5) bands for Wasserstein/GPCA/optimal-transport papers. Weak anchors (avg 2.6–3.4) were clearly below this paper's theoretical level. Strong anchors (avg 8.0) were substantially more polished with thorough experiments. The middle band (avg 5.0–6.33) contained papers with similar profiles: interesting methodology held back by experimental gaps. This placed the paper in a [4.5, 6.5] bracket.

**Round 2 (Narrowing):** Compared against PGPCA (avg 7.33, Accept) — significantly stronger experimentally; Wasserstein Flow Matching (avg 6.33, Reject) — comparable idea quality but with at least some quantitative comparison; Continuous GWOT (avg 6.20, Reject) — similar profile of theory + insufficient experiments; Wasserstein Proximal (avg 6.0, Reject) — theory paper with weak experiments. The current paper's GPCAGEN evaluation gap is more severe than any of these because there is *no* quantitative validation at all for the general-case method.

**Calibration anchors across rounds:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| 9WG1ga39Dq (Consistent OT) | 3.00 | R1 | Clearly weaker — much less theory |
| FjifPJV2Ol (Schrödinger Bridge) | 3.40 | R1 | Weaker methodology |
| Bh4BW69ILq (Unbalanced OT) | 2.60 | R1 | Much weaker |
| WPz5e5V85k (Wasserstein Proximal) | 6.00 | R1 | Similar profile: theory with weak experiments |
| HB4lr0ykTi (Wasserstein Flow Matching) | 6.33 | R1,R2 | Similar idea + evaluation gaps, but had quantitative comparison |
| rY8xdjrANt (OT Barycenter) | 6.20 | R1 | Algorithm paper with evaluation concerns |
| mkDam1xIzW (Probabilistic GPCA) | 7.33 | R2 | Stronger — proper quantitative experiments |
| sRaAt9OOnW (Continuous GWOT) | 6.20 | R2 | Similar — theory + insufficient experiments |
| kvByNnMERu (Shape Distances) | 5.25 | R2 | Mixed quality |
| EyWKb7Ltcx (SPD Manifolds) | 5.00 | R2 | Weaker contribution |
| gxhRR8vUQb (Diffeomorphic Mesh) | 7.00 | R2 | Stronger — thorough evaluation |

The paper sits below WFM (6.33), OT Barycenter (6.20), and Continuous GWOT (6.20) because those papers at least included quantitative evaluation metrics; the current paper's GPCAGEN evaluation is purely qualitative. It sits above the 5.0–5.75 range because the Gaussian GPCA theory (Propositions 3–5) and evaluation (100 trials, cost comparisons) are solid, and the GPCAGEN method is geometrically principled.

**Final score: 5.5.** The paper has genuine theoretical substance and a principled algorithmic approach, but the absence of quantitative evaluation for the main contribution (GPCAGEN) is a decisive gap that prevents acceptance in its current form. Substantial revision with quantitative validation is needed.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
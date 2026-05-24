## Summary

The paper introduces **Count Bridges**, a stochastic bridge process on $\mathbb{Z}^d$ built from independent Poisson birth/death processes. The key contribution is a closed-form local bridge kernel (Bessel slack × Binomial × Hypergeometric — Prop. 3.1) that satisfies the bridge consistency and projective-posterior identities required of a diffusion-style sampler. The framework is extended via an EM-style algorithm with a projection-guided E-step (Algorithms 3–4, Prop. 4.1) to handle aggregated observations, and is applied to nucleotide-resolution single-cell RNA-seq + bulk deconvolution and to spatial-transcriptomic deconvolution.

## Strengths

- **Exact closed-form integer bridge kernels (Prop. 3.1).** The change of variables to $(N_t, B_t)$ and the Bessel-form slack posterior yield an exact, tractable local kernel via Binomial × Hypergeometric draws. This is a genuinely novel construction — a clean integer analogue of Gaussian diffusion bridges that does not rely on Euclidean relaxations or categorical CTMCs.
- **Discrete-OT / Schrödinger bridge unification.** Section 3.1 shows Count Bridges solve an entropy-regularized OT problem, and as $\kappa \downarrow 0$ recover discrete OT with $L^1$ cost (equation following line 135). This puts the framework on the same theoretical footing as the Gaussian Schrödinger bridge, with $\kappa$ playing the role of $\sigma$.
- **Distributional scoring rule tailored to lattice geometry (Sec. 3.2).** Using a strictly proper energy score with semimetric $\rho(x,x') = \|x-x'\|^\beta$ avoids the factorization that cross-entropy forces, allows joint modeling across coordinates, and is theoretically justified by the discrete-generator ELBO analysis.
- **High-dimensional scaling on the low-rank Gaussian-mixture task (Fig. 3).** Count Bridges maintain near-zero $W_1$ across $d \in \{4, \ldots, 512\}$ while CFM and DFM degrade sharply, demonstrating scalability that the competing approaches lack.
- **Real biological gains on the headline metrics.** Table 1 shows CB beats fine-tuned Enformer on nucleotide MSE (0.601 vs 2.590 bulk; 1.410 vs 3.142 cell-type). Table 2/3 show JSD 0.113 vs CIBERSORTx 0.194 / MuSiC 0.313 for bulk deconvolution; Table 4 shows JSD 0.231 vs STDeconvolve 0.288 on spatial deconvolution. Whatever the asymmetries (see Weaknesses), CB does produce unit-level count profiles that downstream collapse to competitive proportions.

## Weaknesses

### Fatal
None. The bridge construction itself is sound, and none of the criticisms below threaten the core theoretical contribution.

### Major

- **Blackout Diffusion is named as the closest prior method but never benchmarked.** The related-work section (line 270) and Section 3.1 explicitly frame CB as a strict generalization of Blackout Diffusion (Santos et al., 2023), recovered as $\kappa \to 0$. Yet the synthetic comparisons in Fig. 2/3 and the deconvolution tables include only CFM (continuous, mismatched to counts) and DFM (categorical, ignores ordinality). Without the one count-specific competitor in the comparison, the synthetic story — which motivates the whole framework — is hard to credit on its own terms. A head-to-head against Blackout Diffusion on Figures 2 and 3 should be a rebuttal priority.
- **Headline distributional metrics versus a point-estimate baseline are not a fair comparison (Table 1 right half, Table 5).** "Bulk mean" and "Spot mean" are Dirac distributions; losing to a distributional model on MMD / $W_2$ / Energy is mechanical, not informative. The paper acknowledges (Sec. 6.3) that the spot mean is biologically motivated under intra-spot correlation, but the tables still present these as evidence that CBs "learn meaningful unit-level distributions." That claim should be defended against a baseline that is itself distributional (e.g., per-spot empirical distribution, or a generative baseline).
- **Deconvolution comparisons against CIBERSORTx, MuSiC, and STDeconvolve mix tasks (Tables 2–4).** Those baselines output cluster-level proportions; CB outputs unit-level counts and is post-processed (nearest-cell-type assignment) into proportions. The added flexibility is real, but no baseline that *also* produces count profiles (e.g., DestVI, mentioned in related work) is compared. As written, "state-of-the-art deconvolution" overshoots the evidence shown — the right framing is "matches/beats proportion-only methods while additionally producing count profiles," which is the contribution.

### Minor

- **Bulk RNA-seq evaluation is on synthetically aggregated single-cell data (Sec. 6.2).** Held-out patients are "synthetically bulked," so the aggregate is by construction a sum of the unit-level counts the model is trained on, with no library-prep mismatch between bulk and scRNA-seq — which is the main reason real-world bulk deconvolution is hard. The numbers in Tables 1–3 are therefore an optimistic upper bound, and the "state-of-the-art bulk deconvolution" claim should be softened or supplemented by a real-bulk evaluation.
- **Spatial application uses synthetically aggregated MERFISH, not real Visium (Sec. 6.3).** Same observation: this is a clean benchmark but is not the target deployment regime. Showing CB on at least one true Visium dataset would substantially strengthen the spatial claim.
- **The projection-guided E-step is the only mechanism linking theory to applications, yet it is justified only as a first-order surrogate (Prop. 4.1, also flagged in Sec. 7 limitations).** The closed-form rescaling $\Pi(\mathbf{x}_0)_g = a_0 x_{g0}/(\sum x_{g'0})$ produces non-integer values, in tension with the paper's central thesis that integer structure matters. The learned $\Pi_\psi$ exists (Sec. 6.2) but no ablation isolates its contribution from the closed-form rescaling, so we cannot tell whether the deconvolution gains come from the bridge or the heuristic projection.
- **No ablation on $\beta$ in the energy score** ($\beta=1$ fixed everywhere — Sec. 3.2). Given the framework's emphasis on lattice geometry, this would be informative.
- **Independence assumption across units (Sec. 4).** The EM formulation assumes a product prior over $\mathbf{X}_0$, yet the paper itself argues in Sec. 6.3 that intra-spot cells are correlated. This tension is not addressed in the modeling.

### Trivial

- Apparent parser/formatting issue around Table 3 caption (line 333) — the caption appears without a clearly associated data block. Authors should verify in the final version.

## Nice-to-Haves

- Empirical demonstration of the OT limit: show that as $\kappa \to 0$ the trained model's couplings converge to discrete OT on a small problem. This would substantiate the Schrödinger-bridge framing, which is currently only a few lines of asymptotic algebra.
- An ablation isolating the infinitesimal (score-style) vs. distributional (scoring-rule) parameterizations — the paper asserts (Sec. 3.2) that the infinitesimal route fails to admit a clean closed form, but the actual penalty is not measured beyond the App. D.1 cross-entropy comparison.
- A clean theoretical statement of the EM identifiability regime ("under heterogeneity condition X, the EM fixed point recovers the unit-level law"). The synthetic results in Fig. 4 are consistent with the limits in App. B.2/B.3 but a sharper statement would convert the projection-EM construction from heuristic to method.
- Comparison against more than one sequence-to-expression baseline beyond Hingerl et al.'s fine-tuned Enformer.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- *(From the harsh critic)* Concerns about table-3 caption being merged with table-1 — this is a parser artifact, not an author error.
- *(From the harsh critic)* Speculation that the favorable Fig. 3 scaling result might be "suspicious" because birth-death dynamics enjoy a structural advantage on low-rank lattice projections. This is unfounded suspicion — the experiment design is disclosed (App. D.2), CFM/DFM are reasonable baselines for that task, and the gap is a legitimate empirical observation.
- *(From the strength finder)* "Outperforming specialized biological baselines on real data" — this strength conflicts with the verified major weakness that the bulk comparison is on synthetically aggregated single-cell data and the proportion comparisons mix tasks. Keeping the more nuanced strength above instead.
- *(From the strength finder)* "Connection to entropy-regularized optimal transport" framing retained, but downgraded — the $\kappa \to 0$ limit is asserted with brief calculation rather than empirically substantiated.

## Novel Insights

None beyond the paper's own contributions. The bridge construction itself — independent Poisson birth/death processes with Bessel-slack reparameterization and Binomial × Hypergeometric descent — is the genuinely novel object, and the OT-limit observation ($\kappa \to 0$ recovers discrete $L^1$ OT) is the cleanest unification with the Gaussian case in the discrete bridge literature.

## Suggestions

- Add a Blackout Diffusion baseline to Fig. 2 and Fig. 3. This is the most important missing experiment.
- Reframe Tables 1 (right), 5 to use a *distributional* baseline (e.g., empirical per-spot/patient distribution, or an off-the-shelf count-profile method like DestVI) rather than point-estimate means.
- Add an ablation comparing closed-form rescaling vs. learned $\Pi_\psi$ on the deconvolution tasks, since this is the bridge between the theory and the headline applications.
- Demonstrate the framework on at least one real Visium dataset, even qualitatively, to support the spatial-transcriptomics claim.
- Soften "state-of-the-art bulk deconvolution" to reflect the synthetic-aggregation regime, or add real bulk RNA-seq evaluation.
- Briefly address how the product-prior assumption over units interacts with the (acknowledged) intra-spot correlation.

## Evaluation on Key Axes

- **Originality:** High. The Poisson birth-death bridge with closed-form local kernels is a genuinely new construction, not a recombination of existing ideas. The OT-limit unification is clean.
- **Importance of the research question:** Solid. Integer-valued generative modeling is genuinely under-served, and biological count data is a natural application; aggregate-to-unit deconvolution is a problem of real practical interest.
- **Claims well-supported:** Mixed. Theoretical claims (Sec. 3) are clean and supported. Empirical claims about "state-of-the-art" deconvolution overshoot because the most relevant count-specific competitor is missing and several headline comparisons are structurally asymmetric.
- **Soundness of experiments:** Mixed. Synthetic comparisons against CFM/DFM are valid demonstrations of geometric structure but omit the relevant count-specific baseline. Biological evaluations are in a synthetically-aggregated regime that favors the method.
- **Clarity of writing:** Good. Sec. 3 is mathematically crisp; the algorithms are clearly stated; limitations are explicitly acknowledged.
- **Value to the research community:** Substantial. The construction will be reusable, the CUDA Bessel sampler is a real engineering contribution, and the framework opens a design space (count-native diffusion + scoring-rule training + aggregate EM) that future work can build on.

## Calibration

**Anchors retrieved:**

Round 1 (bracketing):
- `kKXIYUi8ff.md` (avg 3.0, R1 low) — DynamicsDiffusion: diffusion for molecular trajectories. Much weaker theoretical novelty than CB.
- `4u0ruVk749.md` (avg 3.0, R1 low) — DFITE: diffusion for ITE. Not topically close.
- `46tjvA75h6.md` (avg 3.0, R1 low) — EBM via diffusion synergy. Not topically close.
- `vK8C37eHXM.md` (avg 3.2, R1 low) — Sample what you can't compress. Not topically close.
- `IcbC9F9xJ7.md` (avg 6.5, R1 mid, **read**) — scDiff for single-cell. Applies existing diffusion machinery to biology; reviewers praise execution but flag limited ML innovation. CB has substantially more theoretical novelty.
- `CWoIj2XJuT.md` (avg 4.5, R1 mid) — Unbalanced Schrödinger Bridge with birth/death terms. Topically related; CB's exact closed-form construction looks stronger.
- `pq1WUegkza.md` (avg 7.0, R1 mid) — Convergence of score-based discrete diffusion. Pure theory.
- `6awxwQEI82.md` (avg 7.0, R1 mid) — Discrete and continuous diffusion meet (Lévy-type). Closely related stylistically.
- `zMPHKOmQNb.md` (avg 8.0, R1 high) — Discrete Walk-Jump Sampling for proteins. A more polished discrete generative-modeling paper; CB is less mature on the empirical side.
- `RuP17cJtZo.md` (avg 8.0, R1 high, **read**) — Generator Matching with arbitrary Markov processes. A general framework that CB instantiates more concretely; CB is narrower but more biologically grounded.
- `EO8xpnW7aX.md` (avg 8.0, R1 high) — Permutation via discrete diffusion. Strong specific construction; CB is comparable in flavor.
- `tyEyYT267x.md` (avg 8.0, R1 high) — SAR diffusion language models. Strong empirical record.

**Round-1 bracket:** [5, 7.5]. The paper is clearly above the avg-3 anchors (it has real theoretical novelty and working biological applications), and it has more mature theory than scDiff (6.5) but less polished empirical evaluation than Generator Matching (8.0) or Discrete Walk-Jump (8.0).

Round 2 (narrowing within bracket):
- `tNE0Y3S4fE.md` (avg 5.75, R2) — Stochasticity-controlled Diffusion Bridge. Reject. Comparable in flavor as a "design-space" bridge paper.
- `jZPqf2G9Sw.md` (avg 5.50, R2) — Dynamics-Informed Protein Design. Accept but lukewarm.
- `Q1QTxFm0Is.md` (avg 6.80, R2, **read**) — Underdamped Diffusion Bridges. Accept. Strong theoretical bridge construction; reviewers question novelty/significance. CB is more clearly novel (new state space) but less mature evaluation.
- `UYZRaUCLAg.md` (avg 5.33, R2) — Inverse problems in protein space. Reject.
- `4anfpHj0wf.md` (avg 7.0, R2, **read**) — Point Set Diffusion. Accept. New diffusion model for a new discrete domain (point processes), with concrete experiments; the closest structural analogue I have. Reviewer complaints (limited evaluation, conditional sampling not fully validated) are exactly the kind of empirical-evaluation gaps CB has.
- `Ombm8S40zN.md` (avg 6.25, R2) — Steering masked discrete diffusion. Accept.
- `XsgHl54yO7.md` (avg 6.5, R2) — Guidance for discrete state-space diffusion. Accept.
- `FtjLUHyZAO.md` (avg 6.67, R2) — Diffusion for spatially resolved gene expression. Accept. Related biological application.
- `FDsWd0NOB5.md` (avg 5.5, R2) — Diffusion for 3D microscopy. Reject.

**Narrowing:** Point Set Diffusion (7.0) and Underdamped Diffusion Bridges (6.8) are the closest structural matches: a new bridge/diffusion framework for a new state space with a few clean experiments and some empirical-evaluation gaps. Count Bridges has comparable theoretical novelty (perhaps cleaner: closed-form local kernels and an OT limit), broader application scope, but a more material gap in the form of the missing Blackout-Diffusion comparison and the synthetic-bulk regime. That places CB right around the 6.5–7.0 band — comparable to Point Set Diffusion (7.0) on contribution but slightly below on empirical execution.

**Final position:** 6.5. The theoretical contribution justifies acceptance; the missing key baseline and the asymmetric/synthetic empirical setups prevent pushing higher.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
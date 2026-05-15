Now I have all the information I need. Let me write the consolidated review.

## Summary

The paper integrates Quasi-Monte Carlo (QMC) point sets on the 2-sphere into the Sliced Wasserstein (SW) distance computation for 3D probability measures. It surveys five construction methods (Gaussian mapping, equal-area mapping, generalized spiral points, max-distance, min-Coulomb energy), proposes deterministic Quasi-Sliced Wasserstein (QSW) and Randomized Quasi-Sliced Wasserstein (RQSW) estimators, proves asymptotic convergence of QSW and unbiasedness of RQSW, and evaluates these estimators on approximation quality, point-cloud interpolation, image style transfer, and deep point-cloud autoencoder training.

## Strengths

- **First systematic integration of QMC point sets on the hypersphere for SW distance approximation.** The paper goes beyond earlier ad-hoc mentions of Halton sequences by examining five distinct construction methods, assessing their uniformity via spherical cap discrepancy, and providing both deterministic and randomized variants. (Section 3.1, lines 23, 85–104)
- **Theoretical guarantees for both estimator families.** Proposition 1 (line 118) proves asymptotic convergence of QSW to SW for nearly all constructions. Proposition 2 (line 165) proves unbiasedness of RQSW under Gaussian-based mapping and random rotation. These provide a principled foundation that prior work on QMC for SW lacked.
- **Empirical superiority of RQSW over standard MC SW across multiple 3D tasks, with clear failure-mode analysis of deterministic QSW.** In point-cloud interpolation (Table 1), RQSW variants achieve lower Wasserstein-2 distances at convergence (e.g., RCQSW: 0.002 vs SW: 0.004) while deterministic QSW stagnates. In deep autoencoder training (Table 2), RCQSW matches or improves upon SW (W2: 9.12 vs 9.21 at epoch 400). This demonstrates that the RQSW advantage transfers to practical settings.
- **Principled handling of the deterministic-vs-randomized trade-off.** The paper identifies that deterministic QSW gradients hinder stochastic optimization (lines 124, 128) and proposes two randomization strategies (pushforward and random rotation) that preserve low-discrepancy properties while yielding unbiased gradient estimates (Proposition 2). The interpolation experiments (Table 1) cleanly validate this design choice.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Spherical cap discrepancy values are not reported numerically.** The "Empirical comparison" paragraph (line 104) gives only a qualitative ranking: "generalized spiral points and optimization-based points yield the lowest discrepancies, followed by equal area mapping construction. The Gaussian-based mapping construction performs worst." Since the paper claims to be "the first to make use of the recent numerical formulation of spherical cap discrepancy" (line 23) and this metric is the natural analogue of star discrepancy for the sphere, a table or figure of actual discrepancy values across construction methods and varying L (e.g., L=100, 500, 1000, 5000) would substantiate the qualitative claims. The absence of these numbers does not threaten the paper's core claims — which are demonstrated through direct SW approximation experiments (Figure 2) — but it is an incomplete empirical thread.

2. **The "ground truth" in the approximation error experiment (Section 4.1) is itself an MC estimate with L=100,000.** The paper treats the MC estimate at L=100,000 as the population SW value (line 214). While 100,000 samples yields a small MC error (~O(1/√L)), this systematic noise in the reference is unaccounted for. The experiment would be more rigorous with an analytical SW value for a tractable case (e.g., Gaussians) or with multiple independent runs to quantify uncertainty. In practice, the consistency of QSW's advantage across all four point-cloud pairs and the corroborating downstream tasks (interpolation, autoencoder) mitigate this concern.

3. **Approximation error experiment uses only four point-cloud pairs without statistical replication or confidence bands.** Figure 2 shows a single set of curves; there is no indication of variance across different random seeds or across a broader random sample of point-cloud pairs. The claim of "better approximation" would be strengthened by reporting mean error with confidence intervals over, e.g., 50 randomly selected pairs from ShapeNet.

4. **Style transfer evaluation lacks a proper quantitative table.** The results paragraph (line 310) mentions Wasserstein-2 distances but the only displayed output is a visual figure (Figure 4). A table comparable to Tables 1–2 reporting Wasserstein distances and run times would make the evaluation more rigorous and comparable to the other experiments.

5. **No ablation of the number of projections L in the autoencoder experiment.** All main experiments fix L=100. The paper would benefit from showing whether the QSW/RQSW advantage persists, shrinks, or grows at other L values (e.g., L=10, 50, 500, 1000). This is particularly relevant since QMC's relative advantage over MC is expected to diminish as L grows large.

### Trivial
None.

## Nice-to-Haves

- Ablate the number of projections L in the autoencoder experiment to characterize when QSW/RQSW provides the greatest benefit.
- Provide quantitative Wasserstein distances for the style transfer experiment in a table format.
- Compare against the Max-Sliced Wasserstein distance, which also uses a carefully chosen (rather than random) set of directions.
- Analyze the one-time construction cost of optimization-based point sets (max-distance, min-Coulomb energy) at varying L to help practitioners assess the trade-off.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Criticism about missing proofs in the main text for Propositions 1 and 2 (and for the gradient Leibniz rule justification).** The paper explicitly states (line 29) that proofs are deferred to the appendix. The appendix was stripped by the PDF parser; these proofs exist in the original submission. Similarly, the claim about RQMC point sets being "uniformly distributed" has its justification in the appendix.
- **Harsh reviewer's characterization of the missing spherical cap discrepancy values as "the empirical backbone of Section 3" and "the paper's central claim is unsupported."** This overstates the issue. The paper's central claim — that QSW provides better approximation than MC — is demonstrated directly through the approximation error experiment (Figure 2) and downstream tasks. The spherical cap discrepancy is a supporting theoretical justification, not the primary evidence.
- **Request for "error bars or statistical replication" framed as a fatal structural problem.** The lack of error bars in Figure 2 is a minor presentational weakness, not a fatal flaw, especially since the four pairs consistently show the same pattern and the downstream tasks corroborate the finding.
- **Strength Finder claims about style transfer performance being "consistent empirical superiority" without noting the absence of a quantitative table.** This strength is dropped from the Strengths section because it conflates qualitative visual results with empirical evidence. (The interpolation and autoencoder results, which do have quantitative tables, remain valid strengths.)
- **Strength Finder's claim that theoretical proofs are "correctly claimed and, if proven in the appendix, are solid contributions."** This is vague speculation about unread content. The strengths section above retains only the cited existence of the propositions, not speculation about their correctness.
- **Criticism about "no proof" that the gradient (Leibniz rule) interchange of expectation and differentiation holds.** The paper states this "follows directly" from unbiasedness (lines 171–172). In a conference paper, this is a standard level of justification for a well-known regularity condition; it does not need a full proof in the main text.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a table or figure reporting spherical cap discrepancy values for all five construction methods at several values of L (e.g., 100, 500, 1000, 5000). This is a one-line computation using the cited Heitsch (2021) code and would close the main evidential gap.
2. In the approximation error experiment (Section 4.1), add an analytical ground-truth case (e.g., SW between two Gaussians, which has a closed form) to eliminate reference noise, or run the experiment over 20–50 random point-cloud pairs and report mean error with confidence bands.
3. Add a quantitative table for the style transfer experiment (Section 4.3) reporting Wasserstein-2 distances between transferred and target palettes, mirroring the presentation in Tables 1 and 2.
4. Include an ablation of L in at least one experiment (e.g., the autoencoder) to show how the QSW/RQSW advantage varies with the number of projections.

## Score and Decision

The paper makes a clear, well-motivated contribution: integrating QMC into SW distance computation with multiple construction methods, both deterministic and randomized estimators, theoretical guarantees, and evaluation across several 3D tasks. The weaknesses are minor and addressable — they do not threaten the core claims. The missing spherical cap discrepancy values and limited statistical rigor are gaps in presentation, not fatal flaws. The theoretical contributions (convergence of QSW, unbiasedness of RQSW) and consistent empirical evidence across interpolation and autoencoder training provide solid support for the paper's claims.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
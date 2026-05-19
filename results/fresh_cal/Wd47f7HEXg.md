Now I have a thorough understanding of the paper. Let me write the final consolidated review.

## Summary

This paper introduces Quasi-Monte Carlo (QMC) approximations for the Sliced Wasserstein (SW) distance, focused on 3D. The authors propose deterministic Quasi-Sliced Wasserstein (QSW) using QMC point sets on the 2-sphere, and Randomized Quasi-Sliced Wasserstein (RQSW) for unbiased stochastic optimization. They provide theoretical guarantees (asymptotic convergence for QSW, unbiasedness for RQSW), a taxonomy of QMC sphere constructions evaluated via spherical cap discrepancy, and experiments on approximation error, point-cloud interpolation, image style transfer, and point-cloud autoencoder training.

## Strengths

1. **Well-supported reduction in approximation error.** The approximation error experiment (Figure 1) varies L from 10 to 10,000 across four point-cloud pairs and shows that all QSW variants consistently achieve lower absolute error than standard MC estimation, with CQSW and DQSW performing best. This is the cleanest and strongest experiment in the paper, and it directly validates the core methodological thesis — that QMC point sets yield better numerical integration for the SW distance.

2. **Sound theoretical backing.** Proposition 1 establishes asymptotic convergence of QSW to the population SW distance for all constructions except maximizing-distance. Proposition 2 proves unbiasedness of RQSW estimators. These formal guarantees go beyond prior work (e.g., Lin et al. 2020, which mentioned a heuristic mapping without analysis) and provide a principled foundation for the proposed approximations.

3. **Systematic treatment of QMC point sets on the sphere.** Section 3.1 provides a useful survey of five construction methods (Gaussian mapping, equal-area mapping, generalized spiral points, maximizing distance, minimizing Coulomb energy), evaluated via the numerical spherical cap discrepancy of Heitsch (2021). This provides practical guidance for practitioners selecting point sets for spherical integration.

4. **CQSW achieves best autoencoder reconstruction.** In the deep point-cloud autoencoder experiment (Table 2, epoch 400), CQSW attains W₂=9.06±0.02 vs SW's 9.21±0.06 — the best result overall. This shows that deterministic QSW can be advantageous when the model class is misspecified and L=100 is sufficient, an interesting nuance.

## Weaknesses

### Major

1. **Deterministic QSW fails in the point-cloud interpolation task without sufficient analysis.** In Table 1, all deterministic QSW variants plateau at W₂ ≈ 0.065–0.069 at step 500, while standard MC SW reaches 0.004±0.001 and RQSW variants reach 0.002–0.003. This is an order-of-magnitude failure for a direct gradient-based optimization of the SW objective. The paper acknowledges this (line 256: "QSW variants cannot make the curves terminate") and proposes RQSW as the fix, but it does not analyze *why* the fixed-direction gradient is biased nor characterize when the bias is tolerable vs. fatal. Given that the paper presents QSW as a central contribution and then demonstrates it failing on its first optimization test, this gap weakens the overall narrative. The reader is left without guidance on whether QSW is ever suitable for optimization tasks, or whether RQSW is always required.

2. **RQSW's claimed superiority over MC SW is modest and not statistically verified.** In the autoencoder experiment (Table 2), the best RQSW variant at epoch 400 achieves W₂=9.12±0.02 vs SW's 9.21±0.06 — a ~1% difference, within overlapping error bars. In interpolation (Table 1), RQSW yields W₂=0.002–0.003 vs SW's 0.004±0.001. These improvements are directionally positive but small, and no statistical significance testing (e.g., paired tests, confidence intervals) is reported. For the style transfer experiment, the paper states "we report the Wasserstein-2 distances at the final time step" but provides only qualitative image comparisons (Figure 3) without a quantitative table, making the claimed "considerably lower Wasserstein distances" unverifiable from the text.

3. **GQSW catastrophic failure in autoencoder training is unexplained.** In Table 2, GQSW yields reconstruction losses of SW₂=11.17±0.07 and W₂=32.58±0.06 at epoch 100, compared to 2.25 and 10.58 for standard SW — a 3–5× degradation that worsens (not improves) with more training. The paper states GQSW "suffers from some numerical issues" (line 316) without further diagnosis. For a paper proposing five QSW variants, having one fail this severely without analysis raises concerns about robustness and leaves the Gaussian-mapping construction's suitability in question.

### Minor

1. **L is fixed at 100 in all optimization experiments.** The approximation error experiment elegantly varies L from 10 to 10,000, but the interpolation, style transfer, and autoencoder experiments all use L=100 without justification or sensitivity analysis. Varying L (e.g., 10, 50, 100, 200) in at least one optimization task would strengthen the demonstration that RQSW's advantage is robust and not an artifact of a particular L choice.

2. **Spherical cap discrepancy is discussed only qualitatively.** Section 3.1 provides a useful qualitative ranking ("generalized spiral points and optimization-based points yield the lowest discrepancies") but reports no numerical discrepancy values. For a paper that relies on discrepancy as a key justification for QMC point set selection, reporting the actual computed values would strengthen the link between construction quality and downstream performance.

### Trivial

None.

## Nice-to-Haves

- A controlled experiment comparing QSW vs. MC gradient estimates to a high-precision reference gradient, to characterize the bias introduced by deterministic QSW directions. This would turn the interpolation failure into insight.
- An analysis of the bias-variance tradeoff between QSW (low variance, biased gradient) and RQSW (unbiased, higher variance) across varying L.

## Removed Points

The following points from the input reviews are excluded with justifications:

- **Reproducibility nitpicks (seeds, software libraries, scrambling details):** Per rules, trivial implementation details not required for submission are excluded.
- **Comparison with alternative acceleration strategies (importance sampling, control variates, spherical harmonics):** The paper is scoped to QMC-based improvements; demanding coverage of unrelated methods is scope creep.
- **Proposition 1 characterized as "trivial":** Providing formal convergence guarantees is standard and valuable for a new method; asserting triviality without justification is opinion-based.
- **"The paper would need substantially stronger evidence" (overall assessment):** This conflates the well-supported approximation contribution with the optimization experiments; the core claim (better approximation) IS well-supported, and criticisms of the optimization experiments are retained in the weaknesses above.
- **"Broader discussion of QMC in higher dimensions":** The paper already mentions this in the conclusion (line 324) and the title explicitly scopes to 3D.
- **Strength Finder's generic strengths ("addressed an important problem", "targeted an interesting question"):** Removed as generic; only concrete, evidence-backed strengths are retained.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a perspective that the paper itself does not already address or acknowledge.

## Suggestions

1. **Diagnose the GQSW failure.** Provide analysis (or at minimum a clear hypothesis) of why the Gaussian-mapping construction causes catastrophic failure in autoencoder training but not in interpolation. If the variant is unreliable, remove it from the recommendation or clearly state its limitations.
2. **Provide quantitative style transfer results.** Include a table of Wasserstein-2 distances at the final iteration across multiple source/target image pairs, with standard deviations, to match the level of reporting in the other experiments.
3. **Add sensitivity analysis over L in at least one optimization task.** Show that RQSW's advantage over MC holds across L ∈ {10, 50, 100, 200} in the interpolation or autoencoder task.
4. **Report spherical cap discrepancy values numerically** (a simple table) to strengthen the connection between point set quality and downstream QSW approximation performance.
5. **Add a brief discussion of when deterministic QSW may be preferable to RQSW.** The autoencoder result suggests CQSW can excel under model misspecification — articulating this tradeoff sharpens the paper's practical recommendations.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
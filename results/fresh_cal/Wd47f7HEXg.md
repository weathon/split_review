Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper introduces Quasi-Sliced Wasserstein (QSW) and Randomized Quasi-Sliced Wasserstein (RQSW) approximations to the Sliced Wasserstein distance, replacing standard Monte Carlo (MC) integration with Quasi-Monte Carlo (QMC) point sets on the unit sphere. The paper surveys five QMC construction methods for $\mathbb{S}^2$ (Gaussian-based mapping, equal-area mapping, generalized spiral points, max-distance points, min-Coulomb points), proves asymptotic convergence of QSW and unbiasedness of RQSW, and provides empirical comparisons on point-cloud approximation, interpolation, style transfer, and autoencoder training.

## Strengths

1. **Theoretical guarantees for QSW convergence and RQSW unbiasedness**: Proposition 1 (Section 3.2) proves that QSW converges to the true SW distance as $L\to\infty$ for Gaussian mapping, equal-area mapping, spiral points, and min-Coulomb energy constructions. Proposition 2 (Section 3.3) proves that Gaussian-based and random-rotation RQSW variants are unbiased estimators of the SW distance. These results are non-trivial and directly support the paper's central claims.

2. **Clear empirical improvement in approximation error**: Figure 1 (Section 4.1) shows that QSW variants (particularly CQSW, DQSW, SQSW) consistently yield lower absolute error than MC-SW across four point-cloud pairs, often by an order of magnitude at moderate $L$. This is the most direct and unambiguous evidence for the paper's thesis.

3. **Systematic survey and comparison of spherical QMC point sets**: Section 3.1 catalogues five construction methods for QMC point sets on $\mathbb{S}^{d-1}$, covering both general-dimension and $\mathbb{S}^2$-specific constructions, and provides a relative ordering via spherical cap discrepancy. This serves as a useful reference for practitioners.

4. **Identification and principled resolution of deterministic gradient bias**: The paper explicitly recognizes (Section 3.2) that deterministic QSW gradients can hinder convergence in optimization and proposes RQSW as an unbiased alternative (Section 3.3). Table 1 validates that RQSW variants indeed overcome the QSW stalling issue in point-cloud interpolation.

5. **Computational efficiency analysis**: Sections 3.2–3.3 note that QSW point sets can be precomputed and reused, and that the added randomization cost for RQSW in the 3D setting is negligible relative to the $\mathcal{O}(n\log n)$ per-projection Wasserstein computation, demonstrating that gains come without significant overhead.

## Weaknesses

### Fatal
None.

### Major

1. **GQSW numerical failure unexplained**: In the autoencoder experiment (Table 2, epoch 400), GQSW produces a reconstruction Wasserstein-2 distance of $37.99 \pm 0.05$, while all other methods (SW, EQSW, SQSW, DQSW, CQSW, all RQSW variants) fall in the range $9.06$–$9.21$. The paper attributes this to "some numerical issues" (line 316) without any analysis of the root cause — whether it stems from the inverse Gaussian CDF amplifying perturbations, normalization overflow, or optimization dynamics. This is a serious gap: it undermines confidence in the Gaussian-mapping construction and leaves practitioners without guidance on how to avoid the failure mode. A paper advocating QMC constructions should either fix the issue, explain it, or clearly delineate which constructions are reliable.

2. **Downstream optimization advantage of RQSW over MC is modest and not statistically grounded**: While QSW clearly improves approximation error (Strength 2), the optimization gains are less conclusive.
   - **Point-cloud interpolation (Table 1)**: At step 500, SW achieves $\text{W}_2 = 0.004 \pm 0.001$; the best RQSW variants achieve $0.002$–$0.003 \pm 0.001$. The advantage is real but small. Only three runs are reported with no statistical test.
   - **Autoencoder (Table 2)**: At epoch 400, the best RQSW variants achieve $\text{W}_2 \approx 9.12$ vs. SW's $9.21 \pm 0.06$ — again a modest gap, and the deterministic CQSW ($9.06 \pm 0.02$) outperforms all RQSW variants. Run-to-run variability (standard deviations $0.02$–$0.11$) is comparable to the differences between methods.
   - The paper claims "better gradient approximation" for RQSW but provides no direct variance comparison between RQSW and MC gradient estimators. Without such evidence, the claim rests primarily on small point estimates from three runs.

### Minor

1. **Spherical cap discrepancy values not numerically reported**: Section 3.1 states the relative ordering of discrepancy (spiral/optimization best, equal-area middle, Gaussian worst, all better than random) but provides no numbers, table, or plot. Since the paper's argument for QMC rests on low discrepancy, showing these values quantitatively would make the empirical comparison in Figure 1 more interpretable and diagnostic (e.g., does lower discrepancy always correlate with lower SW approximation error?).

2. **Theoretical link between spherical cap discrepancy and the SW integrand is not established**: The paper correctly notes (line 93) that the Koksma-Hlawka-type bound "holds for some functions belonging to suitable Sobolev spaces" but does not verify that the SW integrand $g(\theta) = W_p^p(\theta\sharp\mu,\theta\sharp\nu)$ for empirical measures belongs to such a space. The paper's motivation for QMC superiority is therefore heuristic, not proven. This is not fatal — the contribution is primarily empirical — but it should be acknowledged more explicitly as a gap.

3. **Proposition 1 omits maximizing-distance construction without justification**: The proposition lists Gaussian mapping, equal-area mapping, spiral points, and min-Coulomb energy as convergent, but excludes the maximizing-distance construction. The paper only notes that max-distance "may suffer from sub-optimal optimization" (line 103), which does not explain why it is omitted from the convergence guarantee. The omission is unexplained.

4. **Approximation error evaluation uses MC with $L=100000$ as "ground truth"**: The reference SW distance (line 214) is itself approximated via MC with $L=100000$, so the absolute error values in Figure 1 reflect approximation to that MC estimate, not to the true (intractable) SW distance. The paper does not quantify how close $L=100000$ MC is to the true value.

5. **Conclusion's recommendation of RCQSW is based on limited evidence**: The conclusion recommends "RQSW with random rotation of QMC point sets minimizing Coulomb energy" as a safe choice with "consistent and stable behavior across tested applications" (line 324). This recommendation rests on experiments with one dataset (ShapeNet Core-55 $\to$ ModelNet40). Its generality across different data modalities and higher dimensions is unverified.

### Trivial
None that are not already covered above.

## Nice-to-Haves

- A direct variance comparison of RQSW vs. MC gradient estimators (either theoretical or empirical) would substantially strengthen the claim of "better gradient approximation" for optimization.
- Diagnosing and fixing the GQSW numerical failure (e.g., clipping, alternative mapping) or explicitly demoting it to a less-reliable variant.
- Reporting the numerical spherical cap discrepancy values as a function of $L$ for each construction, ideally correlated with SW approximation error, would turn the empirical comparison into a diagnostic tool.
- Increasing the number of runs (e.g., 10) for the optimization experiments and reporting statistical significance would improve reliability.

## Removed Points

These points were flagged by reviewers but are removed after verification against the paper:

- *"Reporting 0.00 std for deterministic QSW is misleading"* — This is technically correct and standard practice; the paper accurately reports zero variance for deterministic methods.
- *"Training/evaluation L mismatch in autoencoder"* — Using $L=100$ for training and $L=10000$ for evaluation is standard practice; all methods are compared under identical conditions.
- *"More runs needed" phrased as a structural weakness* — Covered in the Major weakness above with specific context; generic "needs more runs" without acknowledging the reported std devs is removed.
- *"Low-discrepancy sequence rate not verified"* — The paper provides empirical spherical cap discrepancy comparison; demanding verification of asymptotic rates is beyond the scope of an empirical paper.
- *"Maximizing distance not included in Proposition 1 is inconsistent"* — Kept as Minor (see above) after rephrasing; the original language suggesting "inconsistency" is removed.
- *Strength: "Improved performance on end-to-end 3D tasks" as originally phrased* — Modified to reflect the modest optimization gains; the original overclaimed.
- *Generic criticisms about missing related works* — Removed per instructions (cannot confirm existence of missing references).

## Novel Insights

None beyond the paper's own contributions. The reviewers did not surface an insight that the paper itself does not already articulate or imply.

## Suggestions

1. Diagnose and document the GQSW failure mode, or explicitly restrict GQSW to non-optimization settings with a caveat about numerical instability.
2. Add a table or plot reporting the numerical spherical cap discrepancy values for each construction across a range of $L$, with a brief discussion of how they correlate with the SW approximation errors in Figure 1.
3. For the optimization experiments, add a small-scale variance analysis of the gradient estimator (even on a synthetic pair of distributions) to substantiate the claim that RQSW reduces gradient variance relative to MC.
4. Soften or qualify the claim that RQSW provides "better gradient approximation" to reflect the modest and statistically uncertain improvements in Tables 1–2.
5. Run the autoencoder experiment with at least 5–10 seeds to improve confidence in the reported differences.

---

## Score and Decision

The paper introduces a novel and well-motivated idea — replacing MC with QMC point sets for SW approximation — provides theoretical guarantees for convergence and unbiasedness, and offers a systematic survey of constructions. The approximation-error evidence (Figure 1) is clear and compelling. However, the downstream optimization evidence is modest, the unexplained GQSW failure is concerning, and key diagnostic data (numerical discrepancy values) are absent. These are addressable issues that do not invalidate the core contribution.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
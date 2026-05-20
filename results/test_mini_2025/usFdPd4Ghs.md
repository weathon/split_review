Now I have sufficient data for calibration. Let me synthesize my final review.

**Calibration summary:**

**Round 1 (Bracketing):**
- Low band (<3.5): Papers on NTK linearization, neural processes, wide RL, etc. Scores 1.5-3.0. All rejects. Clearly below our paper.
- Middle band (3.5-7.5): Heavy-tailed robust regression (6.33), functional BDL (4.0), q-exponential policy (6.67), NTK-NNGP unification (6.0), Beyond IID weights (6.25). Our paper sits in this band.
- High band (>7.5): Residual deep GPs on manifolds (7.6), etc. Oral presentations. Clearly above our paper.

**Round 2 (Narrowing):**
- *Beyond IID weights* (avg 6.25, Accept Poster): Extends infinite-width GP results to non-iid weights. Clean theory, incremental extension. Our paper has more novel destination (stable processes) but messier presentation and a real gap. Slightly weaker.
- *NTK-NNGP unification* (avg 6.0, Reject): Ambitious but mixed reviews on rigor. Our paper is more focused.
- *q-exponential policy* (avg 6.67, Accept Poster): Clean empirical study. Different domain but comparable quality level.

**My score: 5.5** — The paper has a genuinely novel core contribution and clear computational advances over prior work, but the output-layer specification gap in the main text weakens the claimed theoretical grounding, and several experimental aspects could be strengthened. This is slightly below the "Beyond IID weights" anchor (6.25) because that paper's theory was cleaner despite being incremental, while this paper's core theory has a notable gap that needs resolution.

---

## Summary

This paper develops deep α-stable kernel processes (Dα-KP) as the infinite-width limit of Bayesian neural networks with infinite-variance elliptical priors at each layer. The key insight is that the limiting process at each layer is conditionally Gaussian with a stochastic covariance kernel, enabling a recursive formula (extending Cho & Saul 2009) for the kernels across layers. This avoids the exponential complexity of the feature-space approach in Loria & Bhadra (2024) and scales to multi-layer networks and higher dimensions. Experiments on synthetic discontinuous functions and UCI datasets show competitive predictive performance.

## Strengths

1. **Novel theoretical framework connecting infinite-variance BNNs to deep kernel processes.** Theorem 1 derives the infinite-width limit of deep BNNs with infinite-variance elliptical priors, yielding an elliptical α-stable process with a conditionally Gaussian representation. This is the first result that produces a naturally stochastic deep kernel (via positive α/2-stable scales) without artificial noise injection, directly addressing the deterministic-kernel limitation of deep GPs.

2. **Computationally efficient recursive kernel formula.** The paper extends the Cho & Saul (2009) recursion to the heavy-tailed regime, enabling O(n³) kernel-space computation instead of the O(n^(I+2)) exponential complexity of Loria & Bhadra (2024). This makes posterior inference feasible in multi-layer settings and higher input dimensions where prior work is intractable.

3. **Formal demonstration of feature learning.** Proposition 3 shows theoretically (and Figure 3 confirms empirically) that for α < 2 the posterior of the features depends on the observations, enabling representation learning — a capability absent in deterministic deep GP kernels and achieved here without the ad hoc noise injection of DIWP.

4. **Competitive empirical performance.** On synthetic discontinuous functions (Table 1), Dα-KP matches or beats GP Bayes, GP MLE, NNGP, and DIWP across 1D, 2D, and 10D settings, and is a close second to the feature-space "Stable" method where that method is tractable. On UCI benchmarks (Table 3), Dα-KP achieves best RMSE on 2 of 3 datasets.

## Weaknesses

### Fatal
None.

### Major

1. **Unspecified output-layer specification and scaling.** The paper defines the output ψ(x) in Equation (3) as an unscaled sum over the last hidden layer, and never explicitly states the prior distribution or scaling of the output weights w_j^(L). Theorem 1 analyzes pre-activations z_j^(ℓ) with a 1/M_ℓ^{1/2} scaling factor for ℓ = 2, ..., L. However, Proposition 2 assumes the predictive distribution has covariance Σ^(L) from Theorem 1 without clarifying how the unscaled output ψ connects to the scaled pre-activation z_j^(L) or whether the output weights themselves carry a 1/M_L^{1/2} scaling. The proof is deferred to Appendix C (not visible), but the main text as presented does not make this connection clear. If the proof resolves this, the text still needs revision; if the output layer treatment is indeed missing from the limit analysis, the claimed derivation of the predictive distribution from the infinite-width limit is incomplete. Either way, this gap undermines the paper's central narrative that the method arises *naturally* as an infinite-width limit.

2. **Limited evidence for depth benefits and representation learning.** Table 2 shows no meaningful predictive improvement from depth (L=3 to L=16 results are nearly identical). The paper attributes this to a "rich enough" function class, but this undercuts the motivation for a *deep* kernel process rather than a shallow one. Additionally, the claim of "representation learning" is supported mainly by Proposition 3 (a formal statement) and the qualitative q-q plot in Figure 3, but no quantitative measure of how posterior kernel stochasticity translates to improved predictions (e.g., comparing to a version with fixed scales) is provided.

3. **MCMC details and convergence diagnostics are absent from the main paper.** Algorithm 1 depends on Algorithms 2 and 3 (in the inaccessible appendix) for the MCMC updates of the positive α/2-stable variables. The paper does not describe proposal distributions, acceptance probabilities, or provide any convergence diagnostics (trace plots, effective sample sizes) in the main text. Given that positive stable variables have no closed-form density and the posterior predictive intervals are used to demonstrate uncertainty quantification, the lack of any convergence assessment is a notable gap.

### Minor

1. **Experiments lack statistical significance testing.** The paper reports mean ± SD over 20 splits but does not test whether Dα-KP's improvements over competing methods are statistically significant (e.g., paired t-tests or signed-rank tests). Given that many comparisons are close (e.g., Dα-KP RMSE 8.08 vs GP MLE 8.32 in 10D), significance testing would strengthen the claims.

2. **Missing credible interval coverage in main text.** The paper claims uncertainty quantification benefits from the heavy-tailed prior but defers interval coverage rates to the appendix. Table 1 shows RMSE/MAE only; coverage percentages would substantially strengthen the UQ claims.

3. **Depth ablation is narrow.** Table 2 fixes α=1 and δ=1 for all depth comparisons. The interplay between α and depth is not explored, and the "trainable depth" conjecture is left as speculation.

### Trivial
None.

## Nice-to-Haves
- A sketch of the proof of Theorem 1 in the main text (explaining how the recursion handles the mixture-of-Gaussians structure at ℓ=2) would help readers assess soundness.
- A sensitivity analysis for α in the main text (currently deferred to appendix).
- Empirical coverage of 90% predictive intervals, even for one or two key experiments, would strengthen the UQ claims.

## Removed Points
- **"Theorem 1 proof is deferred to appendix"** — This is standard practice in ML conferences and not a weakness.
- **"Notation φ_{z|Σ} is confusing"** — The notation is sufficiently clear from context. Minor stylistic preference.
- **"The recursion drops the 1/√(M_ℓ) factor"** — The factor is present in Theorem 1's definition of z; the critic misread.
- **"Missing related works"** — Cannot verify without external sources.
- **"Formatting/typo nitpicks"** — Removed per hard rules; these are parser artifacts.
- **"Reproducibility concerns about cited entities/references"** — Removed per hard rules; cited references exist.
- **"Comparison to Stable method is unfair"** — The paper explicitly acknowledges the exponential complexity limitation. The "close second" characterization is accurate and the 2D gap (0.57 vs 0.86) is discussed.

## Novel Insights
The strongest insight emerging from reading the reviews together is that the paper's central contribution (a stochastic deep kernel process arising naturally from infinite-variance priors) is genuinely novel and well-motivated, but the specific theoretical path from the BNN to the predictive distribution is not fully traced in the paper. The output layer gap is the most consequential issue because it sits at the intersection of the paper's two selling points: the "natural" infinite-width limit and the computationally tractable posterior. If the output layer were handled with the same care as the hidden layers, the paper would be substantially stronger. Conversely, if the method works as an empirical kernel process regardless, the paper should reframe its claims accordingly.

## Suggestions
1. **Clarify the output layer.** Explicitly state the prior distribution and scaling of the output weights w_j^(L). Show (either in main text or a clear appendix reference) how Proposition 2 follows from Theorem 1 applied to the output layer. If the scaling differs from the hidden layers (e.g., 1/M_L instead of 1/M_L^{1/2}), state it explicitly.
2. **Add MCMC diagnostic plots** for at least one experiment (trace plots of scales, effective sample size) in the main paper or supplement to validate the posterior sampling.
3. **Quantify representation learning benefits** by comparing predictive performance against a version of Dα-KP where the scales s_+^(ℓ) are fixed at their prior mean (i.e., removing kernel stochasticity), showing that the random kernel actually drives improved predictions.
4. **Add interval coverage** for one or two key experiments and statistical significance tests for the main comparisons.

## Score and Decision

**Score anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| /home/wg25r/review_agent/human_reviews/2NwHLAffZZ.md | 2.33 | R1 | Far below — NTK linearization paper with fundamental issues |
| /home/wg25r/review_agent/human_reviews/rZzcaduYU1.md | 3.00 | R1 | Below — score-based NGP with limited expressivity |
| /home/wg25r/review_agent/human_reviews/brOAVSPPjw.md | 2.50 | R1 | Far below — wide RL training dynamics |
| /home/wg25r/review_agent/human_reviews/WoJzHQIIUk.md | 1.50 | R1 | Far below — MinMax BNN with weak experiments |
| /home/wg25r/review_agent/human_reviews/fUz6Qefe5z.md | 3.00 | R1 | Below — NTK with derivative labels |
| /home/wg25r/review_agent/human_reviews/BydD1vNMCV.md | 5.00 | R2 | Similar — StoNet paper with statistical inference framing |
| /home/wg25r/review_agent/human_reviews/ohHtdp3jDi.md | 4.00 | R1 | Below — functional BDL with shaky theory |
| /home/wg25r/review_agent/human_reviews/AZVmYg3LvS.md | 4.50 | R1 | Slightly below — function space VI with interpretability issues |
| /home/wg25r/review_agent/human_reviews/B21c9hT1D7.md | 6.33 | R1/R2 | Above — heavy-tailed regression with rigorous asymptotics; cleaner theory but different contribution type |
| /home/wg25r/review_agent/human_reviews/OyyE1FDdrQ.md | 6.67 | R1 | Above — clean empirical study of heavy-tailed policies, different domain |
| /home/wg25r/review_agent/human_reviews/5EtSvYUU0v.md | 6.00 | R2 | Comparable — NTK-NNGP unification with mixed review scores; our paper's novelty is higher but presentation is less clean |
| /home/wg25r/review_agent/human_reviews/1Wi0Ys33Nm.md | 6.25 | R2 | Above — Beyond IID weights; cleaner theory for incremental extension; our paper is more novel but has a significant gap |
| /home/wg25r/review_agent/human_reviews/uClUUJk05H.md | 6.17 | R2 | Above — different topic (compositional SBI) |
| /home/wg25r/review_agent/human_reviews/rnL3OafDdw.md | 5.75 | R2 | Similar — Bayesian image regression with ST-CAR prior |
| /home/wg25r/review_agent/human_reviews/JWtrk7mprJ.md | 7.60 | R1 | Well above — residual deep GPs on manifolds; rigorous theory + thorough experiments (oral) |

**Round-1 bracket:** [3.5, 7.5] — clearly above weak rejects, clearly below oral-quality papers.

**Round-2 narrowing:** The paper is comparable to mid-5-to-low-6 papers. It is stronger than the functional BDL paper (4.0) and the StoNet paper (5.0), comparable to the ST-CAR paper (5.75). It is weaker than the "Beyond IID weights" paper (6.25, Accept Poster) because that paper's theory is fully traced and its only weakness is incrementality, whereas this paper has a genuine gap in the output-layer specification. The core contribution is more novel than the "Beyond IID weights" paper, but the gap pulls the score down.

**Final score: 5.5**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
Now let me write the final consolidated review.

## Summary

The paper introduces SCaSML, a framework that corrects pre-trained surrogate PDE solvers at inference time by deriving a "Structural-preserving Law of Defect" — a new PDE describing the surrogate's error that retains the semi-linear structure of the original problem — and solving it via Multilevel Picard (MLP) Monte Carlo simulation. The key theoretical result is a product-form error bound (Theorem 2.5) yielding an improved convergence rate O(m^{-γ-1/2}) that beats both the surrogate alone (O(m^{-γ})) and naive Monte Carlo (O(m^{-1/2})). Empirical results on semi-linear parabolic PDEs up to 160 dimensions show the method reduces errors by 20–80% relative to the base surrogate and succeeds where pure MLP simulation fails catastrophically (HJB/LQG).

## Strengths

1. **Structural-preserving Law of Defect (Fact 2.3, Section 2.2).** The derivation showing that the defect PDE inherits the semi-linear parabolic structure of the original problem is the paper's key mathematical insight and a genuine technical contribution. This structural preservation is what makes high-dimensional Monte Carlo solvers (specifically MLP) applicable to the correction step — without it, the method would be limited to low-dimensional grid-based solvers.

2. **Product-form error bound (Theorem 2.5, Corollary 2.6).** The paper proves that the final SCaSML error factorizes as the product of the MLP simulation error and the surrogate model error. This multiplicative structure is what drives the accelerated convergence rate and implies that the correction cost decreases as the surrogate improves. The result that the cost to reach error ε reduces from O(d ε^{-(2+δ)}) for naive MLP to O(d ε^{-(2+δ)} e(û)^{2+δ}) is clean and meaningful.

3. **Empirical demonstration on HJB where pure MLP fails (Table 1, LQG rows, Section 3.3).** On 100d–160d Hamilton–Jacobi–Bellman equations, the naive MLP solver produces relative L² errors of 5.27–5.63 (complete failure), while SCaSML reduces these to 0.055–0.099, even beating the base PINN surrogate. This is the strongest experimental evidence for the method's practical value — the hybrid approach provides robustness that neither pure simulation nor pure ML achieves alone.

4. **Empirical verification of scaling law across dimensions (Figure 4).** Log-log plots for d ∈ {20, 40, 60, 80} on the viscous Burgers equation show SCaSML consistently has steeper error-vs-collocation-points slopes than the GP surrogate, providing mechanistic evidence for the accelerated convergence claimed in Corollary 2.6, not just final error numbers.

## Weaknesses

### Major

1. **The central claim that "a smaller base PINN can outperform a larger PINN under the same inference-time compute budget" (line 33) is stated as a contribution but the key evidence is deferred to Appendix G.7, which is not in the main paper.** The only cost-effectiveness data in the main paper is Table 1, which shows SCaSML's runtime is 20–234× that of the surrogate alone, with error reductions as modest as 7–11% (DR at 100–160d). Without the fixed-budget Pareto comparison showing SCaSML's compute-for-accuracy tradeoff dominates training a larger surrogate, the reader cannot evaluate whether the method is practically cost-effective. The runtime overhead is reported but never contextualized or justified in the main text.

2. **The theoretical analysis in the main text (Section 2.4) is heuristic and relies on strong assumptions whose validity is not established for the models used.** The "intuition" (line 105) and Section 2.4 argue surrogate error ∼ m^{-γ}, residual ε inherits this order, MC variance ∼ m^{-2γ}, and averaging over m paths gives error ∼ m^{-γ-1/2}. However: (a) Assumption 2.4 requires the surrogate error to be bounded in W^{1,∞} norm — a strong condition rarely established for neural network approximations; (b) The residual ε involves spatial/temporal derivatives of û (∇û, Hess(û)), which can be orders of magnitude larger than function values — no empirical evidence is given that residual magnitude tracks function error for the networks used; (c) The analysis treats m training points and m MC paths as interchangeable, though they consume compute in fundamentally different ways. Rigorous proofs are deferred to the appendix, which is stripped, so the reader cannot verify them from the main paper.

3. **The claim that the defect PDE is "easier" to solve is not adequately justified.** Fact 2.3 shows structural preservation, but this alone does not imply ease: the modified nonlinearity F̃(ũ, σᵀ∇ũ) = F(û+ũ, σᵀ(∇û+∇ũ)) − F(û, σᵀ∇û) + ε can have a Lipschitz constant comparable to or larger than F's, especially when ∇û is large. Computing ε itself requires evaluating the full PDE operator on the surrogate (Hessian cost O(d²) per evaluation), which the paper partially addresses with Hutchinson's estimator (line 288) but without analyzing how its approximation error propagates into the defect PDE solution.

### Minor

4. **No error bars or confidence intervals in Table 1.** The main results table reports single numbers without variance estimates, despite the paper claiming "high statistical significance (p ≪ 0.001)" (line 33). This claim is referenced to Appendix G.4, but the main paper should at minimum show one representative confidence interval.

5. **Asymmetric clipping thresholds between MLP and SCaSML.** For LQG, MLP uses a clipping threshold of 10 while SCaSML uses 0.1 (line 251). The paper notes this "reflect[s] the smaller magnitude of the defect," but since clipping directly affects stability and accuracy, this asymmetry makes the MLP baseline comparison less clean. A controlled experiment where both methods use the same threshold (even if it harms one) would strengthen the comparison.

### Trivial

6. The phrasing "closed-form unbiased correction in a single step" (line 129) could be read as claiming the correction itself is closed-form, when what is meant is that the defect PDE identity is exact (vs. iterative correction). The correction still requires iterative Monte Carlo approximation.

## Nice-to-Haves

- Moving the fixed-budget Pareto comparison (Appendix G.7) to the main paper would significantly strengthen the central claim.
- A direct empirical characterization of when the defect PDE is genuinely easier (e.g., measuring Lipschitz constants, residual magnitudes, or MLP variance for the defect vs. original PDE).
- Error bars or confidence intervals on the key numbers in Table 1.

## Removed Points

- **Criticism that the "inference-time scaling" analogy is imprecise.** The paper explicitly draws the analogy at the level of "allocating more compute at inference time for better accuracy," which is standard usage. Remark 2.2 (lines 103–107) addresses the point directly. The mechanism differs but the conceptual framing is valid.
- **Criticism that including the failed MLP baseline inflates SCaSML's apparent advantage.** The paper clearly acknowledges MLP failure (line 290) and presents it as evidence that the hybrid approach provides robustness — this is a genuine strength, not a deceptive comparison.
- **Criticism about conflating training points and MC paths in the intuition.** This paragraph is explicitly labeled as "intuition" (line 105). The pedagogical simplification is appropriate for the main text, with rigorous proofs deferred to the appendix.
- **Criticism that the paper should "lead with the control variate interpretation."** The conclusion (line 328) already frames it as a control variate. This is a presentation preference, not a weakness.
- **Demand for comparison against training a better surrogate as a fatal omission.** The paper references exactly this comparison in Appendix G.7. The concern is valid but moved to Major weakness #1 above in its proper form (the comparison should be in the main paper).
- **Request for error bars beyond what is standard in the field.** Single-run evaluation for large-scale MC benchmarks is common practice; this is a nice-to-have.
- **Claim that sections are "under-specified" with details in the appendix.** Given page limits, deferring implementation details to the appendix is standard practice.
- **Claim about missing related works.** The reviewer is in no position to verify this without external sources.

## Novel Insights

The harsh critic's observation that the control variate framing (which the paper itself uses in the conclusion) is a more natural description of what SCaSML does than the "inference-time scaling" framing is worth noting. The paper would benefit from leading with this interpretation: the surrogate model serves as a control variate that reduces the variance of the MLP estimator for the PDE solution. This framing has known guarantees and limitations in the Monte Carlo literature, and adopting it would make the theoretical analysis cleaner and the limitations more transparent. Conversely, the "inference-time scaling" framing invites comparisons to LLM test-time compute scaling that are imprecise and may set unrealistic expectations about the method's cost profile.

## Suggestions

1. Move the fixed-budget efficiency comparison (Appendix G.7) into the main paper as a dedicated figure or table. This comparison — whether SCaSML's error-compute tradeoff dominates training a larger surrogate with the same total budget — is essential to the paper's central claim about inference-time scaling.

2. Add error bars or confidence intervals to the key results in Table 1, or at minimum show the statistical test results for one representative case in the main text rather than deferring entirely to the appendix.

3. Strengthen the theoretical narrative in Section 2.4 by either (a) including the key steps of the rigorous analysis from the appendix, or (b) explicitly characterizing Assumption 2.4 with empirical validation (e.g., measuring the W^{1,∞} error for the surrogates used in experiments).

4. Clarify the "closed-form" phrasing and consider reducing emphasis on the "inference-time scaling" analogy in favor of the control variate interpretation already present in the conclusion.

## Score and Decision

**Bracket analysis (Round 1):** I compared the paper against weak (avg 2.5–3.3), middle (avg 4.0–6.8), and strong (avg 8.0) anchors. The paper is clearly above the weak band (those papers have fundamental execution flaws the SCaSML paper does not share). It is well below the strong band (those are rigorous theory papers with complete proofs and clean evaluations). Initial bracket: 5–6.5.

**Narrowing (Round 2):** I read 6 anchors in the 4.0–7.0 range in full. Key comparisons:
- vs. "Automatic Neural Spatial Integration" (4.0, rejected): SCaSML is substantially stronger — more principled mathematics, higher-dimensional experiments (160d vs. 3d), and a cleaner theoretical result.
- vs. "SINGER" (6.33, accepted): Comparable quality. SINGER has cleaner theoretical guarantees but SCaSML solves a harder problem (MLP failure on HJB, 160d vs. 20d) and has a more novel mathematical framework.
- vs. "HyPER" (5.00, accepted with mixed scores): SCaSML has stronger mathematical foundations but HyPER has more practical cost analysis.

The paper's genuine mathematical contribution (Fact 2.3), clean theoretical result (Theorem 2.5), and impressive 160d experiments outweigh the significant presentation gaps (deferred cost-benefit evidence, heuristic main-text theory, no error bars). Final score: **6.0**. This reflects an interesting, novel contribution with addressable weaknesses.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
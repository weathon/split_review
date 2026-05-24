Now I have sufficient calibration data. Let me produce the final consolidated review.

**Calibration Summary:**

**Round 1 (Bracketing):**
- Low band (<3.5): Papers about UQ for surrogates with weak theory (avg 2.33-3.40). Our paper is clearly stronger.
- Middle band (3.5-7.5): Papers from 4.50 to 5.25. The 4.50 paper (Calibrated PI-UQ) had no theoretical results and weak experiments. The 5.25 paper (Constrained Learning) had a mixed reception (3,8,5,5) with concerns about comparison standards.
- High band (>7.5): Papers at 8.0. These are different in nature (solving PDEs, not UQ) and more thorough.

**Round 2 (Narrowing):**
- 6.00 anchor (Non-Exchangeable CRC): Clean theoretical extension, accepted, but noted as incremental. Our paper has more PDE-specific novelty but a worse evaluation issue.
- 6.00 anchor (KOWCPI): Well-executed time-series CP with strong guarantees. Clean empirical evaluation. Our paper has more domain-specific novelty but less clean evaluation.
- 6.67 anchor (WR-CP): Strong theoretical contribution with some practical concerns. Cleaner than our paper.

**My bracket:** 4.5-6.5 after round 1. After round 2, I place the paper at **5.0** — between the 4.50 (Calibrated PI-UQ) and the 5.25 (Constrained Learning). It has genuine theoretical contributions but a significant evaluation flaw that undermines the central empirical claim.

---

## Summary

This paper studies conformal prediction for surrogate models of time-dependent PDEs. It proves that in infinite-dimensional function space, solution distributions at different times are mutually singular (Theorem 4.1), making exact CP impossible. For discretized linear PDEs with Gaussian initial conditions, it derives closed-form Gaussian distributions of the solution (Theorem 4.2), enabling exact likelihood-ratio weights for weighted conformal prediction. Experiments on a second-order linear PDE and a real-world pulsed-thermography dataset show that WCP outperforms naive CP and LSCI.

## Strengths

- **Theorem 4.1 (mutual singularity in function space):** Proves that for the heat equation with Gaussian initial condition, the TV distance between solution measures at different times is 1, rigorously establishing that exact CP is impossible in the infinite-dimensional setting. This is a novel theoretical contribution that connects the PDE and conformal prediction literatures, cited in the paper with reference to Hairer (2023) on mutual singularity of infinite-dimensional measures.

- **Theorem 4.2 (closed-form Gaussian distributions for discretized linear PDEs):** Provides explicit formulas for the mean and covariance of the discretized solution at any time under a Gaussian initial condition, for any linear PDE with linear boundary conditions. This is the core technical enabler, allowing exact density-ratio computation for weighted CP. The proof is given in the main text.

- **Empirical demonstration of WCP advantage over baselines:** Table 1 and Figure 3 show that across varying PDE parameters (a, b, c) and prediction horizons, WCP maintains coverage closer to the 90% target compared to naive CP and LSCI, which systematically undercover as the horizon increases. The real-world pulsed-thermography example (Section 5) demonstrates applicability beyond synthetic data.

## Weaknesses

### Fatal
None.

### Major

- **Misleading coverage evaluation that contradicts the paper's own claims.** The paper excludes samples with infinite bands from the reported coverage (Table 1, Figure 3), then shows coverage values below 90% (e.g., 0.88 for a=-0.005, horizon 15; 0.85 for a=-0.005, horizon 20; 0.84 for a=-0.0075, horizon 15). The paper's explanation ("stochastic noise when n∞ is large") does not cover cases like a=-0.005, horizon 15, where n∞=0% and coverage is 0.88 — here all samples are included and coverage is genuinely below 90%. This directly contradicts the claim that "WCP consistently meets its coverage guarantees." The paper should report overall coverage including infinite-band samples (which contribute 100% coverage) and provide a principled discussion of why coverage drops below 90% even without infinite-band exclusion. The core theory (Theorem 4.2 + weighted CP) is sound, but the evaluation as reported is inconsistent with the paper's claims.

- **Scope overstated in abstract and introduction.** The paper claims to address "a broad class of PDE problems" and provide "exact coverage guarantees for PDEs without limiting assumptions on their time-dependent behavior." The method requires linear PDEs with linear boundary conditions and Gaussian initial conditions (Theorem 4.2). While this is indeed a broad class (heat, advection-diffusion, wave equations, etc.), the framing is more ambitious than the actual scope. The Discussion section (line 303) correctly states "We established coverage for the class of linear PDEs," which is more accurate. The abstract and introduction should be revised to match.

### Minor

- **No analysis of discretization error's effect on coverage guarantee.** Remark 4.5 mentions that coverage guarantees can be transferred to the original PDE solution by leveraging "numerical error guarantees of the scheme," but provides no concrete bound or analysis. Since the method operates on the discretized solution, the relationship between coverage on the discretized system and coverage on the true PDE solution is not formally established.

- **Real-world example does not validate the Gaussian assumption.** The pulsed-thermography experiment (Section 5) is presented as evidence of practical applicability. The cooldown phase "approximately follows the heat equation," but the paper does not test whether the solution distribution is actually Gaussian, nor does it quantify the approximation error. The method's coverage guarantee depends on this assumption. The experiment demonstrates implementation feasibility but not validity under realistic assumption violations.

- **Lack of discussion of weight degeneracy / effective sample size.** In cases with large distribution shifts, the likelihood-ratio weights can become extremely skewed (n∞ approaching 100%). The paper does not discuss how the effective sample size for weighted quantile estimation degrades in these cases, which is directly relevant to the observed coverage drops (e.g., a=-0.005, horizon 15 where coverage is 0.88 without any infinite-band samples).

### Trivial
None.

## Nice-to-Haves

- A comparison to an adaptive quantile tracker (e.g., Gibbs & Candès, 2021) or a simple sliding-window baseline would strengthen the empirical story, even if those methods only provide asymptotic guarantees.
- A brief discussion of the computational cost of computing the matrix exponential Σ_t = exp(tA)Σ₀ exp(tAᵀ) for large spatial discretizations would help practitioners assess scalability.
- Theorem 4.1 could be shortened or moved to the appendix without loss, as the paper itself notes its practical relevance is limited.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"LSCI comparison is unfair because LSCI is not designed for long-range prediction"** — REMOVED. The paper's comparison is valid: it shows that when local exchangeability is violated (at long horizons), LSCI fails, which is exactly the point of demonstrating WCP's advantage. The paper explicitly acknowledges LSCI's intended setting and argues that local exchangeability is unverifiable, which is a fair characterization.

- **"Missing comparison to simple adaptive baseline"** — MOVED to Nice-to-Haves. The absence of this comparison is not a weakness; the paper already compares to the most relevant methods (naive CP, LSCI) and discusses other time-series CP methods.

- **"No discussion of computational cost"** — MOVED to Nice-to-Haves. This is a useful suggestion but not a weakness.

- **"Theorem 4.1 practical relevance is unclear"** — REMOVED. The paper itself notes this result is for the function-space setting and that practice uses discretization, so it's self-aware about the limitation.

- **"The real-world example should be in the main body"** — REMOVED. Conference papers have space constraints, and appendix details are standard.

- **"Non-Gaussian/nonlinear cases should be discussed"** — The paper does discuss this in the Discussion (line 303): "extending the analysis to nonlinear PDEs is a natural next step." This is sufficient.

## Novel Insights

The harsh critic's observation about the coverage evaluation inconsistency is the most penetrating insight: the paper reports coverage on a subset of data (excluding infinite-band samples) in a way that makes the method appear to undercover, when the theoretical guarantee actually holds for the full set. What neither reviewer noted is that this problem is actually more severe than the critic described — the coverage drops below 90% even for cases with n∞=0% (e.g., a=-0.005, horizon 15), where no samples were excluded. This suggests a more fundamental issue with how the method behaves under moderate distribution shifts, beyond the exclusion problem. The likely mechanism is weight degeneracy (skewed likelihood ratios reducing effective sample size for weighted quantile estimation), which the paper does not discuss.

## Suggestions

1. **Fix the coverage evaluation.** Report overall coverage including infinite-band samples (which contribute 100% coverage). This will show that the theoretical guarantee is always met. Separately, provide a discussion of why coverage on finite-band samples sometimes drops below 90% — this could be due to finite-sample effects, weight degeneracy, or violation of the covariate-shift assumption for the neural operator residuals.

2. **Tone down the scope claims.** Replace "a broad class of PDE problems" with "a class of linear PDEs" or "linear PDEs with Gaussian initial conditions" in the abstract and introduction.

3. **Add a brief discussion of weight degeneracy.** When the distribution shift is large, the likelihood-ratio weights become concentrated on a few samples, reducing the effective sample size for the weighted quantile. This is a known limitation of weighted CP and should be acknowledged.

4. **Provide a bound or discussion of discretization error propagation to coverage.** Even a rough bound would significantly strengthen the theoretical contribution.

## Score and Decision

Round 1 bracket: I placed the paper between 4.5 and 6.5 after comparing to weak anchors (2.33-3.40), middle anchors (4.50-5.25), and strong anchors (8.0).

Round 2 narrowing: I examined 4 anchors in the 4.5-6.7 range. The paper is clearly stronger than the 4.50 Calibrated PI-UQ paper (which had no theory, weak experiments). It is comparable to the 5.25 Constrained Learning paper (mixed reviews, 3,8,5,5). It is weaker than the 6.00 Non-Exchangeable CRC and 6.00 KOWCPI papers, which have cleaner evaluations and no reporting inconsistencies. The 6.67 WR-CP paper is more polished. The evaluation issue is the primary factor preventing a higher score.

**Final anchors used:**
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/cF6OoaYcRa.md` (avg 4.50, Round 1): Calibrated PI-UQ — no theoretical results, limited experiments. Our paper is clearly stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/5KqveQdXiZ.md` (avg 5.25, Round 1): Constrained Learning — mixed reviews, concerns about baselines. Comparable to our paper.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/j511LaqEeP.md` (avg 6.00, Round 2): Non-Exchangeable CRC — clean extension, accepted. Our paper has more domain novelty but a worse evaluation.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/oP7arLOWix.md` (avg 6.00, Round 2): KOWCPI — well-executed time-series CP. Cleaner evaluation than our paper.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/aJ3tiX1Tu4.md` (avg 6.67, Round 2): WR-CP — strong theory, accepted. Cleaner than our paper.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/fU8H4lzkIm.md` (avg 8.00, Round 1): PhyMPGN — high-quality PDE solving, extensive experiments. Different sub-area, but more polished.

The paper has solid theoretical contributions (Theorems 4.1, 4.2) that are genuinely novel for the PDE + CP intersection. However, the evaluation issue is significant — reporting coverage on a subset of data while claiming "exact coverage guarantees" is misleading, and the fact that coverage drops below 90% even without infinite-band exclusion is unexplained. The scope is overstated. These issues are fixable. I score the paper at 5.0, reflecting a paper with real contributions held back by a significant but addressable evaluation flaw.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>
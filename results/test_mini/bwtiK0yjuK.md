## Summary

This paper studies offline change point localization and inference in dynamic multilayer random dot product graphs (D-MRDPGs). It proposes a two-stage algorithm combining seeded binary segmentation with low-rank tensor estimation (TH-PCA), establishes consistency for estimating both the number and locations of change points, and—for the first time in the network change point literature—derives the limiting distributions of the refined estimators under both vanishing and non-vanishing jump regimes. A data-driven confidence interval construction procedure is also provided. Simulation experiments across four scenarios demonstrate strong performance against existing methods (gSeg, kerSeg), and a real-data application to worldwide agricultural trade networks yields interpretable change points.

## Strengths

1. **First limiting distribution results for change point estimators in network data.** Theorem 2 (and its non-vanishing counterpart in Appendix A) derives the asymptotic distribution of the refined estimator. The paper explicitly and correctly claims this as a first result in the network literature, and the contribution is genuine and significant.

2. **Provable consistency of the two-stage algorithm with explicit rates.** Theorem 1 establishes that with high probability the estimated number of change points equals the true number and that localization errors satisfy \(|\tilde{\eta}_k-\eta_k|\le C_c\kappa_k^{-2}\log T\). This is a clean, non-asymptotic guarantee that extends prior single-layer results (Wang et al., 2021) to the multilayer setting.

3. **Strong empirical performance across diverse and challenging scenarios.** Table 1 shows that CPDmrdpg substantially outperforms gSeg and kerSeg in nearly all settings. For example, in Scenario 1 with \(n=100\), CPDmrdpg achieves exact recovery (\(|\hat{K}-K|=0\), \(d(\hat{\mathcal{C}},\mathcal{C})=0\)) while the best competitor (kerSeg nets.) has \(d(\mathcal{C},\hat{\mathcal{C}})=2.82\). The method also performs well in Scenarios 2–3, which intentionally violate Model 1, demonstrating robustness.

4. **Real-data interpretability.** The application to worldwide agricultural trade networks identifies four change points (1991, 1999, 2005, 2013) that align with well-documented geopolitical and policy events (German reunification, WTO ministerial conferences, the Bali Package). Confidence intervals are provided.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Confidence intervals are implausibly narrow and lack meaningful uncertainty quantification.** The average CI lengths in Table 2 are as small as 0.001 (Scenario 1, \(n=150\)) and at most 1.528 (Scenario 3, \(n=100\)). On a discrete integer grid with spacing 1, a CI of width < 1 effectively says "the change point is at the exact time estimated." While the CI procedure is mathematically consistent with Theorem 2 (the argmin is over \(\mathbb{R}\), and the simulated process produces discrete values at multiples of \(1/T\)), the near-zero widths in simulations paired with 100% coverage in three of four scenarios suggest the procedure essentially returns a trivial interval \([\hat{\eta}_k,\hat{\eta}_k]\) when the signal is strong. This undermines the claim of providing genuine uncertainty quantification. The real-data CIs in Table 4 (e.g., (5.97, 6.03)) raise similar concerns. The paper would benefit from (a) discussing what information these narrow CIs convey, and (b) evaluating coverage empirically under the vanishing-jump regime for which the asymptotic theory is designed.

2. **Comparisons with relevant multilayer-specific methods are relegated to the appendix.** The abstract and Section 1.1 claim that the method "substantially outperform[s] existing state-of-the-art algorithms." Yet the main text (Table 1) only compares against gSeg and kerSeg—general-purpose graph methods originally designed for single-layer networks. Comparisons with Wang et al. (2025) (online D-MRDPG detection) and Li et al. (2024) (deep learning for dynamic networks) are mentioned but deferred to Appendix G.1. A reader of the main paper cannot assess whether the proposed method improves over methods *actually designed for the same problem*. At minimum, key metrics for these comparisons should be summarized in the main text.

3. **Remark 1 overstates the rate comparison.** The paper claims a "substantially sharper rate" than Wang et al. (2025) (\(\kappa_k^{-2}\log T\) vs. \(\kappa^{-2}(d^2 m_{\max}+nd+L m_{\max})\log(\Delta/\alpha)\)). However, the paper's rate hides dimension-dependent terms (\(n, L, d, m_{\max}\)) in the SNR condition (Assumption 2), which requires \(\kappa\sqrt{\Delta}\) to dominate those terms. The comparison is apples-to-oranges without specifying the relative scaling of these parameters. The remark should be toned down or qualified.

4. **Simulation results report only means.** Table 1 reports means of evaluation metrics over 100 trials, but no standard deviations or quantiles. For metrics like \(d(\hat{\mathcal{C}},\mathcal{C})\) where occasional large errors are possible (e.g., Scenario 3, \(n=50\), 9.64), variability matters. Reporting standard errors or quantiles would give a more complete picture.

5. **CUSUM statistic notation is not formally defined.** Algorithm 1 uses \(|(\tilde{\mathbf{A}}^{\alpha,\beta}(t),\tilde{\mathbf{B}}^{\alpha,\beta}(t))|\) but the notation \(|(\cdot,\cdot)|\) is not defined in Section 1.2 (where \(\langle\cdot,\cdot\rangle\) is defined). From context it is the absolute value of the tensor inner product \(|\langle\cdot,\cdot\rangle|\), but this should be specified.

### Trivial
None.

## Nice-to-Haves

- The simulation design uses \(T=200\) fixed. Testing sensitivity to \(T\) (e.g., 500, 1000) would help validate the predicted rates from Theorem 1.
- Reporting computation time or scaling would strengthen the paper's practical claims, even though analytical complexity is given.
- The odd-even splitting reduces effective sample size by half; the impact on the required SNR could be discussed explicitly for practitioners.
- The TH-PCA algorithm (Algorithm 2, deferred to Appendix D) would benefit from a brief intuitive description in the main paper.

## Removed Points

- **"Mismatch between discrete theory and continuous CI procedure" (Critic's Critical Issue 1)**: REMOVED. Theorem 2 gives \(\arg\min_{r\in\mathbb{R}}\) and the CI procedure takes \(\arg\min_{r\in(-M,M)}\). The simulated process is piecewise linear with argmin at multiples of \(1/T\). Non-integer CI endpoints are consistent with the theory. There is no mismatch. The critic's claim that the theory gives argmin over integers is incorrect — the theorem explicitly states \(\arg\min_{r\in\mathbb{R}}\).

- **"Tucker-rank assumption is not adequately grounded" (Critic's Critical Issue 3)**: REMOVED. Assumption 1(ii)–(iii) are stated as conditions on \(\tilde{Q}^{s,e}(t)\) and \(Q^{s,e}\) derived from the weight matrices \(Q(t)\) — i.e., conditions on the data-generating process. The paper clarifies (line 205) that Appendix E shows the bound follows from each working interval containing one change point with high probability. There is no circularity.

- **"Missing related works"**: REMOVED per hard rules — I cannot verify what references exist outside the paper.

- **"Formatting/style nitpicks"**: REMOVED per hard rules (parser artifacts are not author errors).

- **"Reproducibility concerns" about missing hyperparameters, training logs**: These are standard artifacts that cannot be included in a paper submission.

- **"Strawman weaknesses"**: Any criticism that misunderstands the paper content or claims something already addressed by the paper.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Contextualize the CI narrowness.** Add a paragraph discussing why the confidence intervals can be sub-unit wide on a discrete grid: the CI is on the scale of \(\eta_k\) but its width is driven by \( \hat{\kappa}_k^{-2} \); a large estimated jump produces a narrow CI. Report coverage under the vanishing-jump regime where \(\kappa_k\to0\) to validate the asymptotic theory. Show what the CIs look like in settings where the signal is weaker and the estimator has non-trivial localization error.

2. **Move or summarize the appendix comparisons into the main paper.** At minimum, report key metrics for Wang et al. (2025) and Li et al. (2024) in a row of Table 1, or add a sentence in Section 4.1 stating the main takeaway (e.g., "As shown in Appendix G.1, CPDmrdpg also outperforms these methods by ...").

3. **Add standard deviations or quantiles to Table 1.** For each metric and each method, report \(\text{mean}\pm\text{sd}\) or the 25th/75th percentiles.

4. **Qualify Remark 1.** Replace "substantially sharper rate" with "the rate depends on fewer explicit problem dimensions due to the SNR absorbing those terms" and reference Assumption 2.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- *Weak anchors (score < 3.5)*: e.g., lhY8Pa0u8d (3.33, online CPD for Poisson processes), I30HO3xth3 (3.00, Ricci curvature for networks). The paper under review is far stronger — it has rigorous theory, extensive experiments, and a genuinely novel contribution that these papers lack.
- *Middle anchors (score 3.5–7.5)*: T-GINEE (4.00, tensor-based multilayer networks), High-Dimensional Online CPD (4.50), ℓ₁ LD-CTGR (6.40, continuous-time graph representation, accepted poster). The paper under review has a more significant theoretical contribution than 6.40-anchor ℓ₁ LD-CTGR (which largely replaced L2 with L1 distance) and stronger empirical results, but shares some minor presentation concerns.
- *Strong anchors (score > 7.5)*: Papers scoring 8.0 in this batch are in different areas (kernel functions, multilevel control functionals, matrix sign methods, transduction). They represent extremely clean, complete work — a higher tier.

**Round 1 bracket**: Between 5.5 and 7.5.

**Round 2 (Narrowing):**
Additional middle-band anchors clustered around 6.0–6.67 (ℓ₁ LD-CTGR at 6.40, From Fields to Random Trees at 6.67, Topological Causal Effects at 6.00). The paper under review is at least as strong as the 6.40-anchor (ℓ₁ LD-CTGR, accepted poster) in terms of theoretical novelty and empirical validation, but falls short of the 8+ tier due to the CI narrowness concern and the comparison-deferred-to-appendix issue.

**Final calibration**: The paper is in the 6–7 range. Compared to the 6.40-anchor (ℓ₁ LD-CTGR), it has a more significant theoretical contribution (first limiting distribution result in network change point literature vs. replacing L2 with L1 norm) but shows a similar pattern of minor presentation concerns. The CI issue, while not structural, prevents the paper from reaching the 7+ tier. Score of 6.5 reflects a solid paper with genuine contributions and addressable weaknesses.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
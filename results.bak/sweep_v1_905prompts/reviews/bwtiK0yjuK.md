Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper tackles offline change point localization and inference in dynamic multilayer random dot product graphs (D-MRDPGs), a problem not previously addressed. The authors propose a two-stage algorithm (seeded binary segmentation + tensor denoising refinement), prove consistency for both the number and locations of change points, derive the first limiting distributions for change point estimators in network data (under both vanishing and non-vanishing jump regimes), and provide a data-driven confidence interval procedure. Experiments on four simulation scenarios and two real datasets demonstrate strong empirical performance against generic competitors.

## Strengths

1. **First limiting distributions for network CPD estimators (Theorem 2).** As the paper correctly states, these are the first such results in the network literature. The derivation covers both vanishing-jump and non-vanishing-jump regimes, and the result is nontrivial — a two-sided Brownian motion limit. This is a genuine theoretical advance over prior work (e.g., Wang et al. 2021, Madra Padilla et al. 2023) that only provided localization rates.

2. **Sharp consistency rate (Theorem 1).** The localization error bound $\epsilon_k = C_c \log(T)/\kappa_k^2$ removes dependence on latent dimension and layer complexity present in prior online-setting rates (Wang et al. 2025), improving from $\kappa^{-2}(d^2 m_{\max} + nd + L m_{\max})\log(\Delta/\alpha)$ to $\kappa_k^{-2}\log(T)$. The SNR condition is carefully extended from single-layer to multilayer settings.

3. **Honest empirical evaluation that tests model violations.** Scenarios 2 and 3 explicitly violate Model 1 (the assumed data-generating process), allowing robustness assessment. The method degrades gracefully in Scenario 3 (coverage drops to 76.67% at n=100 but recovers to 95.33% at n=150), and the paper transparently discusses this — the evaluation is not cherry-picked to show only successes.

4. **Practical data-driven CI procedure.** Section 3.1 provides a concrete, implementable pipeline (Steps 1–4) for constructing confidence intervals from the limiting distribution, including variance estimation and quantile simulation. This bridges a significant gap between theory and practice for network CPD.

5. **Interpretable real-data findings.** The detected change points (1991, 1999, 2005, 2013) in the agricultural trade network align with documented geopolitical/economic events (German reunification, WTO negotiations, Bali Package), demonstrating practical utility.

## Weaknesses

### Major

1. **Gap between theoretical independence assumption and practical implementation.** The theory (Theorems 1, 2, Algorithm 1) assumes *four mutually independent* tensor sequences {A(t)}, {A'(t)}, {B(t)}, {B'(t)}. In practice, the paper states (line 119): "the same two split tensor sequences via the odd-even splitting approach" are used for both Stage I and Stage II. The paper describes this as "for theoretical convenience" but provides no argument that the odd-even split preserves the independence structure across stages that the theorems require. Since the whole theoretical edifice (consistency rates, limiting distributions) depends on this independence, a clear justification — or a modification of the algorithm to match the theory — is needed. At minimum, a sensitivity analysis comparing the four-sequence ideal to the two-sequence odd-even split would help.

2. **CI coverage not validated in the regime the theory covers.** Theorem 2 derives the limiting distribution and CI procedure under the *vanishing-jump regime* ($\kappa_k \to 0$). However, the simulation experiments in Section 4.1 use fixed (non-vanishing) jump sizes. The paper does not report a controlled experiment where $\kappa_k$ decreases with $T$ (e.g., $\kappa_k \propto T^{-\gamma}$) and checks nominal vs. actual coverage. Without this, it is unclear whether the CI procedure works in the regime for which it is theoretically justified. The very narrow intervals in Table 2 (e.g., length 0.003 for Scenario 1, n=100) suggest strong signal, not the vanishing-jump setting — and the coverage properties may differ in the vanishing regime. A dedicated coverage experiment with decreasing $\kappa_k$ is needed to substantiate the inference claim.

### Minor

3. **Real-data analysis with T=35 pushes the asymptotics.** The theory requires $T \to \infty$ and $\Delta = \Theta(T)$. The agricultural trade network has $T=35$ time points. The confidence intervals in Table 4 (e.g., (5.97, 6.03) for time point 6) are reported with two-decimal precision, which overstates what a sample of 35 observations can support. The paper should discuss the small-sample limitations of the asymptotic approximation and treat the intervals as approximate.

4. **No tensor-based baseline results in the main text.** The paper claims to "substantially outperform existing state-of-the-art algorithms" but the main text only compares against gSeg and kerSeg, which are generic methods not designed for multilayer tensor data. The paper mentions comparisons with Wang et al. (2025) and Li et al. (2024) in the (stripped) appendix. A summary of those results in the main body would substantially strengthen the benchmarking claim.

### Trivial

- None that survive filtering (parser artifacts removed).

## Nice-to-Haves

- A diagnostic plot of CI length as a function of $\kappa$ (signal strength) would help the reader assess the behavior.
- A sensitivity analysis showing how performance changes with input Tucker ranks (mentioned as done in Appendix G.1, but the main text would benefit from a summary figure).
- A brief runtime comparison across different $(n, L, T)$ settings, beyond the complexity expression.

## Removed Points

The following points raised by reviewers are removed as they do not represent valid weaknesses:

- **CUSUM notation "u ∈ [t][s]" garbled.** This is a PDF-extraction parser artifact. The original submission's LaTeX is not available for inspection, and such formatting issues do not affect content validity.
- **Refined scan statistic (Definition 5) notation appears garbled.** Same reason — parser artifact from PDF extraction.
- **Near-perfect results "suspicious."** The method performs near-perfectly on well-specified scenarios (1, 2, 4) and degrades honestly under model violations (Scenario 3: 76.67% coverage at n=100). This pattern is expected and not suspicious; it demonstrates both the method's strength and the evaluation's honesty.
- **Rank sensitivity not validated.** The paper explicitly states (line 285) that sensitivity analysis with $r \in \{10, 15, 20\}$ and $c_{\tau,1} \in \{0.05, 0.08, \dots, 0.25\}$ is conducted and reported in Appendix G.1. The criticism is addressed in the paper.
- **Missing related work.** Cannot verify without external sources; rule forbids mentioning missing related works.

## Novel Insights

The key insight that emerges from synthesizing the reviews — beyond the paper's own contributions — is that the paper's most significant practical vulnerability is the misalignment between its theoretical framework (four independent sequences, vanishing-jump asymptotics) and its actual deployment (odd-even split of two sequences, finite/large jumps). This gap is common in statistics papers, but here it touches every major claim: consistency, limiting distributions, and CI validity. The authors would substantially strengthen the paper by either (a) modifying the algorithm to genuinely use four independent splits, or (b) proving that the odd-even split satisfies the essential independence conditions, or at minimum (c) providing simulation evidence that the practical algorithm matches the theoretical guarantees. Similarly, a dedicated vanishing-jump simulation would close the loop between Theorem 2 and the empirical CI evaluation.

## Suggestions

1. **Resolve the data-split gap.** Either (a) adapt the algorithm to use four genuinely independent sequences (possible in simulations; for real data, use a bootstrap-type argument), or (b) prove that the odd-even split preserves the required independence across stages, or (c) provide simulation evidence that the two-sequence odd-even implementation achieves the same rates as the four-sequence ideal.

2. **Add a vanishing-jump coverage experiment.** Simulate data where $\kappa_k \propto T^{-\gamma}$ for several $\gamma > 0$, construct CIs via Section 3.1, and report coverage vs. nominal level as a function of $T$. This directly validates the regime Theorem 2 covers.

3. **Include a brief summary of tensor-based competitor results in the main text.** Even a sentence or two about how the method compares with Wang et al. (2025) and Li et al. (2024) would make the benchmarking claims more concrete.

4. **Discuss small-sample limitations of asymptotic CIs in the real-data analysis.** Acknowledge that $T=35$ makes the asymptotic approximation approximate, and interpret the CIs accordingly.

## Score and Decision

### Calibration Report

**Round 1 — Bracketing.** Three queries on "change point detection in dynamic networks" with bands $<3.5$, $(3.5, 7.5)$, $>7.5$. Low-band anchors (scores 2.3–3.3, Reject) were on tangential topics (anomaly detection, continual learning). Middle-band anchors included "Change Point Detection via Variational Time-Varying Hidden Markov Model" (4.75, Reject) and "Valid Conformal Prediction for Dynamic GNNs" (5.80, Accept). High-band anchors (7.6–8.0) were on unrelated theory topics (neural network loss landscapes, graphon networks). **Initial bracket:** 5.0–6.5.

**Round 2 — Narrowing.** Queried on "change point detection network data tensor method" (4.5–7.0), "statistical inference change point estimation asymptotic distribution" (5.5–7.5), and "multilayer network change point localization" (4.0–6.5). Relevant anchors: TV-HMM (4.75, Reject) — weaker on all dimensions; "Performance Gaps in Multi-view Clustering" (6.20, Accept) — comparable theoretical depth, fewer experimental weaknesses. The current paper is clearly stronger than the TV-HMM paper (which was rejected for lacking improvement over baselines and having unclear practical advantages) and comparable to the performance-gaps paper (which was accepted despite limited experiments).

**Final position.** The paper's theoretical contributions (first limiting distributions for network CPD) are genuinely novel and the empirical evaluation is well-designed with robustness checks. However, the unaddressed gap between theoretical assumptions (four independent sequences) and practical implementation (odd-even split), combined with the missing vanishing-jump CI validation, keeps it from being a strong accept. The paper sits between the TV-HMM reject (4.75) and the multi-view clustering accept (6.20) — closer to the latter but with resolvable weaknesses that prevent clear recommendation at the higher end.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
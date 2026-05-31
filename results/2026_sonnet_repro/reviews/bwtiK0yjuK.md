Now let me do the calibration search to anchor my score.Round 1 bracket: **5.0 – 7.0**. Now let me narrow further.Now I have enough information to write the final review. Let me compile my findings.

---

## Summary
This paper proposes the first offline change point localization and inference framework for dynamic multilayer random dot product graphs (D-MRDPGs), where multilayer networks share node latent positions but have time-varying layer-specific weight matrices. The core contribution is a two-stage algorithm—seeded binary segmentation with CUSUM statistics followed by Tucker-decomposition-based TH-PCA refinement—that achieves consistency in estimating both the number and locations of change points (Theorem 1, with localization error $|\tilde{\eta}_k - \eta_k| \leq C_c \log(T)/\kappa_k^2$) and, crucially, derives the first limiting distributions for change point estimators in any network setting (Theorem 2, a two-sided Brownian motion limit), enabling data-driven confidence intervals. Empirically, the method substantially outperforms general-purpose baselines (gSeg, kerSeg) across four simulation scenarios and identifies interpretable structural changes in the worldwide agricultural trade network.

---

## Strengths

- **First offline CPD consistency result for D-MRDPGs (Theorem 1):** The paper establishes $\mathbb{P}\{\tilde{K} = K \text{ and } |\tilde{\eta}_k - \eta_k| \leq C_c \log(T)/\kappa_k^2, \forall k\} \geq 1 - CT^{-c}$, extending the minimax-optimal single-layer guarantees of Wang et al. (2021) to the multilayer setting without sacrificing accuracy. The localization rate also sharply improves on the online multilayer bound of Wang et al. (2025), which is of order $\kappa^{-2}(d^2 m_{\max} + nd + Lm_{\max}) \log(\Delta/\alpha)$, versus $\kappa_k^{-2}\log(T)$ here (Remark 1).

- **First limiting distributions for change point estimators in network data (Theorem 2):** The derivation of a two-sided Brownian motion limit for $\kappa_k^2(\hat{\eta}_k - \eta_k)$ in the vanishing-jump regime is genuinely novel in the network literature. This unlocks a fully data-driven CI construction (Section 3.1, Steps 1–4) that requires no parametric resampling and is, to the best of the reviewers' knowledge, the first such inference procedure for network change points.

- **Decisive empirical performance on four diverse scenarios (Table 1):** CPDmrdpg achieves near-zero Hausdorff distances and correct $\tilde{K}$ across Scenarios 1–4, even under violations of Model 1 (Scenarios 2 and 3). For example, in Scenario 3 ($n=100$), segment coverage is 99.98% vs. below 80% for all kerSeg variants. The performance gap is not marginal.

- **Principled algorithmic design:** Algorithm 1 cleanly separates coarse detection (seeded binary segmentation with CUSUM over tensor sequences) from fine refinement (TH-PCA–based local scan statistic). The Tucker low-rank structure of the expected CUSUM tensor is explicitly derived (Section 2.3) to justify the TH-PCA step, giving a theoretical basis for each algorithmic choice.

---

## Weaknesses

### Fatal
None.

### Major

- **CI coverage failure in Scenario 3 without diagnosis (Table 2):** At $n=100$, the reported 95% CI coverage is 76.67% — an 18-point shortfall from nominal. The paper attributes this to "violations of Model 1 and relatively small, layer-specific changes" in one sentence (Section 4.1). This explanation is unsatisfying because Scenario 3 is not a pathological stress test — it involves changes confined to a single layer (community sizes shift only in Layer 1 while three others stay fixed), precisely the case where a multilayer method should leverage cross-layer pooling to strengthen inference. The paper does not diagnose whether the failure stems from biased variance estimation in Step 2 of Section 3.1, from the limiting distribution approximation being inaccurate at $T=200$ under model misspecification, or from an identifiability problem when the signal is layer-sparse. Without this diagnosis, practitioners cannot know when the CI procedure is trustworthy.

- **Implausibly narrow confidence intervals in the real-data application (Table 4):** The agricultural trade network data has $T = 35$ annual time points. Table 4 reports a 95% CI of $(5.97, 6.03)$ for the 1991 change point — a width of $0.06$ on the integer time scale, far narrower than the 1-year data resolution. The CI construction in Section 3.1 is asymptotic (it relies on Theorem 2 as $T \to \infty$); the simulations in Table 2 use $T=200$. Whether the asymptotic approximation is valid at $T=35$ is entirely unaddressed, and the extreme CI narrowness raises a genuine concern that the procedure is operating outside its valid regime in the real-data example.

### Minor

- **Theory-to-practice gap from sample splitting is unresolved for inference:** Algorithm 1 formally requires four mutually independent copies of the network sequence, but in practice only a single observed sequence is available; the paper uses odd-even temporal splitting (Section 2.2). This is openly acknowledged, but the paper does not analyze what happens to the limiting distribution in Theorem 2 under split data: odd-even splitting halves the effective time horizon and induces temporal sub-sampling correlations that the theoretical framework does not account for. Since Theorem 2 establishes a precise limiting distribution (not just a consistency rate), even small residual correlations in the pseudo-independent sequences could perturb the limit. A brief empirical sensitivity check (e.g., comparing CI coverage with and without split data to artificially independent data) would bridge this gap.

- **Most informative comparison relegated to appendix:** The most directly comparable prior work — Wang et al. (2025), which addresses the same D-MRDPG model but in the online setting — is compared only in Appendix G.1. Given that the paper's abstract and introduction emphasize the gap between offline and online methods, and that Remark 1 claims a rate improvement, moving this comparison to the main text would substantially strengthen the evidential case. The present main-text comparisons with gSeg and kerSeg (general-purpose graph-kernel methods that do not exploit multilayer low-rank structure) are too unfavorable to the baselines to be maximally informative.

### Trivial
None that rise above parser-artifact level.

---

## Nice-to-Haves

- Table 1 reports mean metrics across 100 Monte Carlo trials but no standard deviations. For scenarios where CPDmrdpg and a competitor are within a few percent on segment coverage (e.g., Scenario 3 at $n=50$), one cannot assess statistical significance without variance information.
- The CI procedure covers only the vanishing-jump regime ($\kappa_k \to 0$); non-vanishing results are in Appendix A. A brief discussion of which simulation/real-data scenarios fall in which regime would help practitioners identify when each CI formula applies.
- Wall-clock runtimes for the proposed method vs. baselines are absent. The stated complexity $O(Tn^2 Lr \log^2(T\vee n))$ involves Tucker decomposition at every seeded interval; an empirical timing comparison would ground the computational claim.

---

## Removed Points

*These points are flagged as removed; treat them with caution.*

- **Baselines too weak (critic's Point 1, "non-parametric methods cannot exploit multilayer structure"):** While factually correct that gSeg and kerSeg do not exploit the D-MRDPG structure, comparison with weaker general-purpose baselines is not inherently unfair. The paper does include the most relevant structured baseline (Wang et al., 2025) in Appendix G.1. The issue has been demoted to a Minor weakness about *organization* (main text vs. appendix), not a fundamental comparison flaw. The asymmetry favors the baselines' generality, not the authors' method's special assumptions, so no Hard Rule applies.

- **SNR condition verification in experiments:** The critic notes that Assumption 2 is never verified empirically. This is a reasonable observation but is a nitpick standard in much of the theoretical statistics literature — Assumption 2 is a parameter-level condition that the simulation setups implicitly satisfy by construction. Flagging it as a weakness would apply to essentially every theory-plus-simulation paper in this tradition.

- **Request for narrowest-over-threshold experiments in main text:** The paper explicitly scopes this to future work and Appendix G.1. Demoting a clearly-flagged extension to a weakness is scope creep.

- **Strength: "Principled algorithm combining seeded binary segmentation with tensor PCA"** (from Strength Finder): Retained as a strength above with a concrete description of what makes it principled.

- **Generic strength: "Realistic model and transparent assumptions"** (from Strength Finder): Removed as too generic. The transparency of Assumptions 1 and 2 is genuine; the "realistic model" framing is not specific enough to retain as a standalone strength.

---

## Novel Insights

The combination of seeded binary segmentation with Tucker-decomposition TH-PCA is more than a routine extension: the paper explicitly proves (Section 2.3) that the *expected CUSUM-transformed adjacency tensor* inherits a Tucker low-rank structure from the MRDPG model, with mode-3 rank bounded by $m_{\max}$ (the rank of the weight-matrix sequence). This structural insight justifies why tensor PCA on CUSUM statistics, rather than simply on raw adjacency tensors, achieves the sharper localization rate. The identification of this structural insight as the key bridge between single-layer and multilayer change point theory is the most technically original contribution in the paper. A secondary novel observation is that the limiting distribution in Theorem 2 (two-sided Brownian motion parameterized by variance $\sigma_{k,k'}^2 = \text{Var}(\langle \Psi_k, \mathbf{E}_{k'}(1)\rangle)$) inherits its parameters directly from the inner product of the normalized jump tensor $\Psi_k$ with the adjacency noise, giving the CI plug-in estimators a clear statistical interpretation.

---

## Suggestions

1. **Diagnose the Scenario 3 coverage failure**: Run additional experiments isolating whether the coverage gap is due to biased variance estimation ($\hat{\sigma}_{k,k'}^2$), the limiting approximation quality at $T=200$, or the MRDPG approximation to MSBM. A simple diagnostic is to compare $\hat{\sigma}_{k,k'}^2$ against the empirical variance of $\langle \Psi_k, \mathbf{A}(t) - \mathbf{P}(\eta_{k'}) \rangle$ computed with oracle $\Psi_k$ and $\mathbf{P}(\eta_{k'})$.

2. **Add a real-data calibration check**: For the agricultural trade data, report the estimated jump sizes $\hat{\kappa}_k$ for each detected change point and discuss whether the asymptotic theory is plausible at $T=35$. The CI width formula $\propto \hat{\kappa}_k^{-2}$ implies that if $\hat{\kappa}_k$ is large, the CI collapses — which may be happening here — but this should be stated explicitly and checked against finite-sample simulation at $T=35$.

3. **Move Wang et al. (2025) comparison to the main text** or at minimum add a brief tabular summary in Section 4.1 cross-referencing Appendix G.1, since this is the most relevant competitor for the paper's central claim.

4. **Characterize the regime for the practical CI procedure**: Clarify in Table 2 or its caption which scenarios are in the vanishing vs. non-vanishing jump regime (i.e., whether $\kappa_k$ is calibrated to shrink with $T$), so readers understand the theoretical scope of the coverage claims.

---

## Score and Decision

**Anchor summary:**

| Path | Avg Human Score | Round | Comparison to paper under review |
|---|---|---|---|
| I5MquO1g7R (TV-HMM CPD) | 4.75 | R1/R2 | Clearly weaker: no improvement over competitors, algorithmic correctness issues, rejected |
| E2OAT195Le (Network Evolution) | 3.75 | R1 | Much weaker; different topic |
| i3T0wvQDKg (Conformal Prediction for Dynamic GNNs) | 5.80 | R1 | Comparable: first theoretical guarantees for a novel dynamic graph inference task; paper under review has stronger novelty claim (first limiting distributions) and more decisive empirical gains |
| ILqA09Oeq2 (Multi-view Clustering Tensor Theory) | 6.20 | R2 | Comparable/slightly below: similarly principled tensor-based statistical theory paper, accepted; paper under review has broader contribution (method + theory + CI + real data) but has CI coverage failure |
| nUBLhhVM1l (Tight Rates Outlier Transfer) | 6.33 | R2 | Comparable: clean theoretical statistics paper accepted at similar score; paper under review has comparable depth but weaker real-data validation of inference |

**Round 1 bracket:** 5.0–7.0.

**Round 2 narrowing:** The two closest anchors are ILqA09Oeq2 (6.20, tensor/network theory, accepted) and i3T0wvQDKg (5.80, dynamic graph inference theory, accepted). The paper under review is:
- **Stronger than i3T0wvQDKg** in novelty of theoretical contribution (first limiting distributions in network data) and decisive empirical advantage.
- **Comparable to ILqA09Oeq2** in theoretical depth but has added breadth (consistency + limit theory + CI procedure + experiments + real data), though the CI procedure has an unresolved coverage failure and the real-data CIs are dubiously narrow.

These two weaknesses (Scenario 3 and real-data CIs) are Major and unresolved in the current submission, but they do not invalidate the core theoretical results (Theorems 1 and 2) which represent genuine firsts. The paper is best positioned between the two round-2 anchors, slightly above the lower one (5.80) but not quite at the upper one (6.20) because of the unresolved inference issues.

**Final score: 6.0 (Accept)**

The theoretical contributions—first offline CPD consistency for D-MRDPGs and first limiting distributions for change point estimators in network data—are genuine and sound. The empirical performance is strong. The weaknesses (CI coverage failure in Scenario 3, narrow real-data CIs, relevant comparison in appendix) are real and the authors should address them, but they do not undermine the paper's central claims. The paper is a meaningful contribution to a specialized but well-motivated subfield of statistical network analysis.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
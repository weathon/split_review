## Summary

This paper addresses offline change point localization and inference in dynamic multilayer random dot product graphs (D-MRDPGs), where multilayer networks share node latent positions while having time-varying, layer-specific connectivity. The authors propose a two-stage algorithm combining seeded binary segmentation (Stage I) with low-rank tensor estimation via TH-PCA (Stage II), establish consistency for estimating the number and locations of change points, and — as a first in the network literature — derive limiting distributions for the refined change point estimators in both vanishing and non-vanishing jump regimes. A data-driven procedure for constructing confidence intervals is also provided and validated empirically.

---

## Strengths

- **First offline change point framework for dynamic multilayer networks.** The paper clearly establishes its novelty gap: prior multilayer network work (Wang et al., 2025) was online-only, and prior offline work treated single-layer networks. The model is well-motivated, with the D-MRDPG allowing heterogeneous, time-varying layer connectivity under a shared latent geometry.

- **First limiting distributions for change point estimators in network data.** Theorem 2 derives Brownian-motion-based limiting distributions in both the vanishing ($\kappa_k \to 0$) and non-vanishing jump regimes, enabling principled confidence interval construction. This is a meaningful advance even for the single-layer setting, and the derivation is technically non-trivial due to the high-dimensional tensor structure.

- **Sharper rate than the online counterpart.** Theorem 1 achieves a localization error of order $\kappa_k^{-2}\log T$, which is demonstrably sharper than Wang et al. (2025)'s online rate of $\kappa^{-2}(d^2 m_{\max} + nd + Lm_{\max})\log(\Delta/\alpha)$, consistent with the information-theoretic advantage of the offline setting.

- **Comprehensive and convincing numerical experiments.** The simulation study covers four scenarios including cases where Model 1 is deliberately violated (Scenarios 2 and 3), assessing robustness. The method consistently dominates gSeg and kerSeg across all metrics. The real-data experiments on agricultural trade and air transport networks yield historically interpretable change points that competitors miss or incorrectly date.

- **Complete inference pipeline.** The paper provides a fully data-driven confidence interval procedure (Steps 1–4 in Section 3.1), with Table 2 confirming nominal coverage in most settings and identifying exactly where violations occur (Scenario 3, small jumps, model misspecification).

---

## Weaknesses

### Fatal
None.

### Major

- **Theory-practice gap on sample independence.** Algorithm 1 formally requires four mutually independent tensor sequences $\{\mathbf{A}(t)\}, \{\mathbf{A}'(t)\}, \{\mathbf{B}(t)\}, \{\mathbf{B}'(t)\}$, but in all numerical experiments only two sequences are used via odd-even splitting. This is standard in the literature but the theoretical guarantees as stated do not formally cover the practical implementation. The paper acknowledges this in one sentence but does not provide even an informal argument for why the guarantees transfer, leaving a notable gap between theoretical claims and empirical validation.

- **Weak choice of competitors in the main body.** gSeg and kerSeg are general-purpose sequence change point tests not designed for network or tensor data. The natural baseline — applying Wang et al. (2021)'s single-layer offline method layer-by-layer or aggregated — is only in the appendix. The advertised comparison with Wang et al. (2025) (online multilayer) and Li et al. (2024) (deep learning) is also relegated to the appendix, making the main paper's competitive evaluation understated for ICLR's ML-focused audience.

### Minor

- **Assumption $\Delta = \Theta(T)$ is restrictive.** The requirement that consecutive change points be linearly separated in $T$ bounds the total number of changes to $O(1)$. While the paper correctly positions this as a limitation and mentions relaxations (Appendix G.1 and narrowest-over-threshold), the main theoretical results do not cover the high-frequency-change regime. Scenario 2 already probes this boundary with change points at $\{20, 60, 80, 160, 180\}$ (spacing as small as 20 out of $T=200$), and the paper does not comment on which aspects of the theory apply or what safeguards exist.

- **Confidence intervals on real data are unnervingly narrow.** Table 4 reports intervals such as $(5.97, 6.03)$ for the 1991 trade event (time units are years, $T=35$). Intervals of half-width $\approx 0.03$ years ($\approx$11 days) for annual-resolution data appear overly optimistic, possibly reflecting asymptotic noise calibration that is not appropriate for $T=35$. The paper does not discuss finite-sample reliability of the confidence procedure in small-$T$ regimes.

- **Under-coverage in Scenario 3.** At $n=100$, coverage is 76.67% against a nominal 95% level, a substantial shortfall. The explanation (model violation and small layer-specific jumps) is brief; a quantitative discussion of when and how severely misspecification degrades coverage would strengthen the inference claims.

### Trivial

- The Tucker-rank input to TH-PCA is set heuristically ($r_1=r_2=15, r_3=L$) using guidance from Wang et al. (2025), without connecting this choice to the theoretical rank bounds established in the paper itself.

---

## Nice-to-Haves

- An empirical comparison specifically against Wang et al. (2021) applied per-layer (with aggregation) in the main body would strengthen the case for the multilayer model by isolating the benefit of joint tensor estimation over layer-wise analysis.
- Some discussion of computational scaling: for large $n$ and $L$, Stage II costs $O(Tn^2Lr\log^2(T\vee n))$, which can be significant; practical approximations or sketching strategies would broaden applicability.
- A small simulation studying $T=35$ (matching the real-data experiment) to validate the CI procedure in finite-horizon regimes would address the real-data confidence interval concern.

---

## Novel Insights

The paper's most genuinely novel observation is that offline change point inference in network data — historically studied only at the localization level — admits rigorous limiting distributions that take the form of a two-sided Brownian motion process, analogous to classical univariate change point theory but now with noise variance determined by the projection of the adjacency residuals onto the normalized jump tensor $\Psi_k$. This projection structure neatly captures how the signal-to-noise geometry of the multilayer adjacency tensor governs inference, unifying the roles of latent dimension $d$, number of layers $L$, and layer rank $m_{\max}$ in a single variance formula. The sharper offline rate $\kappa_k^{-2}\log T$ versus the online rate $\kappa^{-2}(d^2 m_{\max}+nd+Lm_{\max})\log(\Delta/\alpha)$ makes precise the cost of not having access to the full dataset, extending classical online-versus-offline intuition to the network tensor setting.

---

## Suggestions

- Provide a brief informal argument or simulation showing that the odd-even sample-splitting implementation preserves the theoretical guarantees, or formally state which results carry over under a mild mixing/correlation assumption.
- Move at least the comparison against Wang et al. (2021) applied per-layer into the main body as a direct ablation of the multilayer pooling benefit.
- Add a finite-$T$ simulation ($T \approx 35$, matching the real data) for the confidence interval procedure, to validate or caveat the real-data results in Table 4.
- Discuss Scenario 2 specifically in light of the $\Delta = \Theta(T)$ assumption — spacing of 20 with $T=200$ is borderline, and explaining why the method still works there adds insight.

---

## Score and Decision

The paper makes three independently valuable contributions — a novel algorithm with optimal localization guarantees, the first limiting distributions for network change point estimators, and a complete data-driven inference procedure — in a problem setting (offline D-MRDPG) that was genuinely unaddressed. The theory is rigorous and the experiments are broadly convincing. The main concerns (theory-practice independence gap, limited main-body competitors) are significant but not fatal; they call for clarification rather than fundamental revision.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
Now I have sufficient calibration data. Let me synthesize everything into the final review.

## Summary

This paper studies offline change point localization and inference in dynamic multilayer random dot product graphs (D-MRDPGs), a setting not previously addressed. The authors propose a two-stage algorithm combining seeded binary segmentation with low-rank tensor estimation (TH-PCA), establish consistency guarantees for the number and locations of change points, derive limiting distributions for the refined estimators (the first such results for network data), and provide a data-driven confidence interval construction procedure. Numerical experiments on simulated and real-world agricultural trade networks demonstrate the method's efficacy.

## Strengths

- **First theoretical treatment of offline change point detection in dynamic multilayer networks with full consistency guarantees.** Theorem 1 proves that Algorithm 1 simultaneously estimates the number of change points correctly and localizes them at rate \(|\tilde\eta_k - \eta_k| \le C_c \kappa_k^{-2}\log T\), with high probability. This extends the single-layer minimax-optimal rate of Wang et al. (2021) to the multilayer setting, and Remark 1 documents a sharp improvement over the online rate of Wang et al. (2025).

- **First derivation of limiting distributions for change point estimators in network data, together with a data-driven confidence interval procedure.** Theorem 2 gives the limit of \(\kappa_k^2(\hat\eta_k - \eta_k)\) as the argmin of a two-sided Brownian motion process under the vanishing-jump regime. Section 3.1 translates this into a fully operational CI construction, and Table 2 shows 100% coverage in 3 out of 4 scenarios for \(n=150\) with average lengths as small as 0.001.

- **The two-stage algorithm (SBS + TH-PCA refinement) is well-conceived**, and the computational cost analysis is provided: \(O(T n^2 L r \log^2(T \vee n))\) overall. The robustness checks (Scenarios 2 and 3, which violate Model 1) demonstrate that the method does not rely on the model being exactly correct, and the sensitivity analysis for threshold and rank parameters is reported.

- **Real-data application yields interpretable change points** that align with documented geopolitical and trade-policy events (German reunification, WTO Ministerial Conferences, the Bali Package), illustrating practical utility.

## Weaknesses

### Major

- **Main-text experimental comparison relies on generic baselines that do not exploit network structure.** The main experiments (Section 4.1, Table 1) compare only against gSeg and kerSeg applied to flattened network vectors or Frobenius norms — general-purpose high-dimensional change point methods. The paper mentions comparisons with network-specific methods (Wang et al. 2025, Li et al. 2024) but relegates them to Appendix G.1. While the appendix exists in the original submission, the asymmetry in the main presentation makes the headline claim of "substantially outperform[ing] existing state-of-the-art algorithms" (Section 1.1) only weakly supported by the evidence the reader sees in the main body. At minimum, a network-specific baseline (e.g., averaging adjacency matrices across layers and applying a single-layer network CPD method, or using tensor decomposition as a preprocessing step before a standard detector) should appear in the main experiments.

- **The confidence interval procedure is theoretically derived for the vanishing-jump regime (\(\kappa_k\to 0\)) but is applied in simulation and real-data settings where jump sizes are non-vanishing and large.** The paper acknowledges this limitation in the conclusion ("our inference procedure is limited to vanishing jumps"), but the empirical presentation in Sections 4.1–4.2 does not flag this mismatch or discuss why the intervals might still be reliable. The suspiciously narrow CIs in Table 4 (e.g., (5.97, 6.03) for a year-indexed time point) would benefit from a bootstrap-based alternative or an explicit caveat.

### Minor

- **The assumption \(\Delta = \Theta(T)\) (minimal spacing scales with the time horizon) is restrictive** and precludes frequent change points. The paper mentions a possible relaxation via narrowest-over-threshold (Baranowski et al., 2019) in the conclusion but does not provide any theoretical or empirical support for this extension. While this is a known limitation, its impact on the applicability of the method is non-trivial for settings with many change points.

- **Performance in Scenarios 1 and 2 is nearly perfect (100% metrics for several settings),** which suggests the signal-to-noise ratio in those scenarios is high enough that the detection problem is easy. Reporting the actual jump magnitudes \(\kappa_k\) or a summary of the signal-to-noise ratio per scenario would allow readers to calibrate the difficulty of the detection task. Scenario 4 provides more informative variation, but the method's perfect scores in easier settings do little to differentiate it from competitors.

- **The signal-to-noise condition (Assumption 2) involves composite quantities** (\(m_{\max}\), Tucker ranks of averaged \(Q\) matrices, the combination \(n L^{1/2} + d^2 m_{\max} + nd + L m_{\max}\)) that are difficult to interpret or verify in practice, and the paper offers no guidance on how practitioners might check whether the condition holds for their data.

### Trivial

None.

## Nice-to-Haves

- Providing a simple adapted baseline (e.g., averaging layers and applying a single-layer CPD method like Wang et al. 2021) in the main experiments would substantially strengthen the empirical claims.
- A small simulation or sensitivity analysis that varies the jump size \(\kappa_k\) to test CI coverage across a range of vanishing-to-non-vanishing regimes would help clarify the practical import of the vanishing-jump limitation.
- A brief informal statement of when Assumptions 1–2 are likely to hold (e.g., "the Tucker ranks are bounded when the weight matrices are themselves low-rank") would help bridge the theory-practice gap.

## Removed Points

- **Harsh critic's claim about inadequate baseline comparison due to appendix being stripped:** The paper does compare against Wang et al. (2025) and Li et al. (2024) in Appendix G.1; the parser removed this section. The remaining criticism about weak baselines in the main text is kept and moved to Major weakness 1. The "reader cannot evaluate" argument is removed per rule about missing appendix.
- **Harsh critic's criticism that "the paper does not discuss the validity of applying this procedure outside the vanishing regime":** The paper explicitly states in Section 3.1 "in the vanishing regime" and the conclusion flags this as a limitation. Kept as a Minor weakness about the presentation gap but removed the stronger framing.
- **Strength Finder's strength about "consistently superior empirical performance":** The generic phrasing is removed; the specific metrics from Table 1 are incorporated into the strengths above.
- **Strength Finder's strength about "interpretable real-data results":** Kept as a brevity-adjusted strength.
- **Harsh critic's point about missing quantification of change magnitudes:** Kept as a Minor weakness.
- **Harsh critic's "missing discussion of CI validity for non-vanishing jumps":** Merged into the Major weakness about regime mismatch.

## Novel Insights

None beyond the paper's own contributions. The two-stage design (seeded binary segmentation for coarse detection followed by TH-PCA refinement for accurate localization and inference) is a natural but non-trivial extension of single-layer techniques, and the theoretical analysis that yields both consistency and limiting distributions is the paper's core contribution.

## Suggestions

1. Move one or two network-specific baselines (e.g., averaging layers into a single weighted network and applying a single-layer CPD method, or using tensor decomposition features with a standard classifier) into the main-text experiments.
2. Add an explicit caveat when presenting CIs in non-vanishing simulation settings, and consider a bootstrap-based CI as a complement to the theoretically-motivated vanishing-jump CIs.
3. Report approximate jump magnitudes \(\kappa_k\) or SNR values for each simulation scenario so readers can gauge detection difficulty.
4. Consider adding a brief discussion (even a paragraph) on how practitioners might reason about whether Assumptions 1 and 2 are plausible for their data.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Three queries on "change point detection in dynamic networks multilayer" with score filters \((<3.5), (3.5, 7.5), (>7.5)\).  
- Low band returned papers with avg 2.00–3.33 (Poisson CPD, causal discovery, dynamic GNNs) — clearly weaker.  
- Middle band returned papers with avg 4.00–4.50 (SWCPD, KM-ARL/ADD) — some theory but limited novelty or incremental.  
- High band returned papers with avg 8.00 (control functionals, language models, rotation estimation) — strong but topically unrelated.  

**Round 1 bracket:** 5.0–7.0. The paper is substantially stronger theoretically than the 4.0–4.5 anchors but not at the 8+ level.

**Round 2 (Narrowing):** Two queries on "network change point detection theoretical guarantees" and "change point detection limiting distribution confidence interval" with filters \((4.5, 6.5)\) and \((5.5, 7.5)\).  
- Returned papers with avg 4.67–6.5 (column thresholding, matrix denoising, conformal p-values).  
- Compared to these, the current paper has stronger novelty (first results in a new problem setting) but weaker experimental presentation (limited main-text baselines).  

**Final score:** 6.0. The paper makes a genuinely novel theoretical contribution with consistency guarantees, limiting distributions, and a data-driven CI procedure — all firsts for network data. This places it above the 4.5-level "incremental theory" papers. The gap between theoretical strength and empirical presentation, particularly the reliance on generic baselines in the main text and the unresolved regime mismatch for CIs, prevents a higher score.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
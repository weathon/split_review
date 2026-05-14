Now I have all the information I need. Let me compose the final review.

---

## Summary

This paper presents the first framework for offline change point localization and inference in dynamic multilayer random dot product graphs (D-MRDPGs). The authors propose a two-stage algorithm (seeded binary segmentation followed by low-rank tensor refinement via TH-PCA) with strong theoretical guarantees, and derive the first limiting distributions for change point estimators in network data — enabling principled confidence interval construction. Extensive simulations and real-data analyses on agricultural trade and air transport networks demonstrate consistent empirical performance.

## Strengths

- **Novel problem formulation**: The paper fills a clear gap by being the first to study offline change point detection in dynamic multilayer networks, with a clean model (D-MRDPG, Model 1) that extends static multilayer RDPG to time-varying weight matrices over a shared latent structure.

- **Non-trivial theoretical contributions**: Theorem 1 establishes consistency with localization error \(O(\kappa_k^{-2} \log T)\), improving on online rates by a logarithmic factor. Theorems 2–3 provide the first limiting distributions for change point estimators in network data — under both vanishing (two-sided Brownian motion) and non-vanishing (two-sided random walk) jump regimes. These are genuinely novel results that open the door to principled inference in network change point analysis.

- **Actionable inference procedure**: The four-step CI construction (Section 3.1) translates the limiting distribution theory into a practical, data-driven procedure for constructing confidence intervals — a capability absent from competing methods. Coverage is strong in most scenarios (Table 2).

- **Thorough empirical validation**: Four simulation scenarios (including two that violate Model 1) test the method across diverse structural changes. CPDmrdpg consistently outperforms gSeg and kerSeg baselines, nearly always recovering the exact number of change points with negligible Hausdorff distance (Table 1). Sensitivity analysis (Appendix G.1) demonstrates robustness to threshold choice and input ranks. Real-data change points align with well-documented geopolitical and economic events (Section 4.2).

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Theory-practice gap in independence assumptions**: The theoretical guarantees (Theorems 1–3) require four mutually independent adjacency tensor sequences, while the practical implementation uses only two sequences via odd–even splitting (Section 2.2). The paper acknowledges this gap and it is common in the change point literature, so the consistency and distributional results do not formally apply to the algorithm as actually run. The gap is mitigated by the strong empirical evidence, but it means the theory does not directly cover the implemented procedure.

- **Threshold calibration requires a null model**: The constant \(c_{\tau,1} = 0.1\) is calibrated by evaluating false positive rates on a null MSBM simulation with no changes (Appendix G.1). A practitioner without access to a reasonable null model would lack guidance for setting this parameter. The sensitivity analysis (Tables 5–8) does show robustness across a range of \(c_{\tau,1}\) values, which partially mitigates this concern.

### Trivial

- **Competitor adaptation could be better documented**: The description of how gSeg and kerSeg are adapted to multilayer network data (Section 4.1) — via "networks (nets.)" and "layer-wise Frobenius norms (frob.)" — is brief. A few additional sentences clarifying the exact input format for each competitor would improve reproducibility. The paper does test both natural adaptations and reports results for both, so the comparison is not unfair.

## Nice-to-Haves

- Confidence intervals are currently limited to the vanishing jump regime. Extending the inference procedure to the non-vanishing regime (e.g., via bootstrap methods) would broaden practical applicability — a limitation the authors already acknowledge (Section 5).

- Adding time-series plots of detected change points overlaid on network summary statistics for the real-data analysis would strengthen the qualitative assessment of whether detected changes correspond to visible structural breaks.

## Removed Points

*These points were flagged in the input reviews but are removed from the main assessment with justification.*

- **"Competitor evaluation is insufficiently described and potentially unfair"**: The harsh critic argues the paper does not explain how competitors are applied to multilayer data. The paper does describe the two input types (nets. and frob.) and the specific scan statistics used. The description, while brief, is present and reasonable. The performance gaps are large and consistent across scenarios — well beyond what suboptimal adaptation could explain.

- **"Explicit conditions for TH-PCA errors should be restated"**: The harsh critic suggests restating conditions from Wang et al. (2025) verbatim. This is a presentation preference, not a weakness. The paper cites the source and relies on established results; restating them would add length without substance.

## Novel Insights

None beyond the paper's own contributions. The paper's core novelty — the first limiting distributions for change point estimators in network data and their use for inference — is already a significant contribution to the literature.

## Suggestions

- Consider adding a brief discussion (even one paragraph) on whether the theoretical guarantees for four independent sequences can be extended to the two-sequence odd–even splitting regime, or what barriers prevent such an extension. This would strengthen the connection between theory and practice.

- In the competitor description (Section 4.1), add a sentence or two clarifying what data structure gSeg receives under "nets." input (e.g., "each time point's adjacency tensor is flattened into a vector of length \(n^2 L\) for the similarity graph construction").

---

### Anchor Comparison

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| EnVaI6s64d (Causal inference in dynamic networks) | 6.00 (Accept Poster) | Similar level of novelty; current paper has deeper theory (first limiting distributions) and fewer major weaknesses |
| dbaGyviiYF (Dynamic Low-Rank FGT) | 5.60 (Reject) | Strong theory but no experiments; current paper has both strong theory and extensive experiments |
| ilhWL2WPvS (HD Online CPD with SW distance) | 4.50 (Reject) | CPD-related but weaker theory; current paper substantially stronger in theoretical depth |
| R3dkexJWju (CPD evaluation via survival analysis) | 4.50 (Reject) | Narrower contribution (evaluation metrics only); current paper has broader scope |
| lhY8Pa0u8d (Online CPD for Poisson processes) | 3.33 (Reject) | Oversimplified setting, single CP only; current paper far more comprehensive |
| Hz96UqwkNW (Deep stratigraphic CPD) | 2.67 (Reject) | Heuristic-heavy, limited novelty; current paper far stronger theoretically and empirically |

The paper is clearly stronger than the 4.50 anchors (comparable CPD topic but much deeper theory) and the 3.33 anchor. It is at least as strong as the 6.00 anchor (EnVaI6s64d), with deeper theoretical contributions and fewer major weaknesses. The combination of genuine theoretical novelty (first limiting distributions in network CPD), strong empirical validation, and practical inference tools places this paper comfortably in the acceptance range.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
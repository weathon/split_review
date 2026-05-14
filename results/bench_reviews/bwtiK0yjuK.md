Now I have all the information needed. Let me construct the final consolidated review.

## Summary

This paper studies offline change point localization and inference in dynamic multilayer random dot product graphs (D-MRDPGs). The authors propose a two-stage algorithm combining seeded binary segmentation with low-rank tensor estimation (TH-PCA), establish consistency for estimating the number and locations of change points, and derive the first limiting distributions for change point estimators in network data under both vanishing and non-vanishing jump regimes. A data-driven confidence interval construction procedure is also provided.

## Strengths

- **First limiting distributions for change point estimators in network data (Theorems 2 and 3):** This is the paper's strongest contribution. Prior work on network change point detection (e.g., Wang et al. 2021 for single-layer, Wang et al. 2025 for online multilayer) only established consistency rates. Deriving limiting distributions in both vanishing and non-vanishing regimes, and using these to construct data-driven confidence intervals, is a genuine theoretical advance. The proofs in Appendices E and F are detailed and technically sound.

- **Well-motivated two-stage algorithm with clear computational complexity:** The combination of seeded binary segmentation (Stage I) for coarse candidate generation followed by tensor-based TH-PCA refinement (Stage II) is natural and principled. The overall cost of O(T n² L r log²(T∨n)) is clearly stated and reasonable for the problem scale considered. The use of TH-PCA for low-rank estimation in this context is novel.

- **Comprehensive empirical evaluation across multiple scenarios:** The paper evaluates four simulation scenarios (covering both the assumed D-MRDPG model and violations), provides sensitivity analyses for threshold choice (Tables 5–8), input ranks (Table 9), frequent change points (Table 10), random locations (Table 11), and temporal dependence (Table 12). Two real-data analyses (agricultural trade network, U.S. air transport network) show detected change points aligning with known events. Comparisons with CPDonline (Wang et al., 2025) and AutoCPD (Li et al., 2024) are provided in the appendix (Table 13).

## Weaknesses

### Major

- **The four-sequence independence assumption required by the theory is not satisfied in the experiments.** Algorithm 1 and all theoretical results (Theorem 1, 2, 3) assume four mutually independent tensor sequences {A(t)}, {A'(t)}, {B(t)}, {B'(t)}. The proofs explicitly condition on events from one pair of sequences without affecting the other pair (Appendix E). However, the paper states (lines 298–301) that in practice it uses "the same two split tensor sequences via the odd–even splitting approach," which produces only *two* dependent sequences. This means the theoretical guarantees (consistency rates, limiting distributions) do not formally apply to the actual algorithm used in experiments. The paper is transparent about this gap, but it is a structural disconnection between theory and practice that weakens the overall contribution. This issue is common in the sample-splitting change point literature, but the severity here is notable because the proofs depend on independence in multiple places (e.g., to condition on Stage I success without affecting Stage II distributions).

- **The main experimental comparison does not adequately support the claim of "superior performance" over structured alternatives.** The headline comparisons (Table 1) are against gSeg and kerSeg, which are generic change point methods not designed for multilayer networks. Their poor performance on this task is expected and does little to validate the proposed method's advantages. The paper does include comparisons with CPDonline (Wang et al., 2025) and AutoCPD (Li et al., 2024) in Appendix G.1 (Table 13), but these are relegated to a single scenario (Scenario 1), and CPDonline (an online method) is evaluated in an offline setting without adaptation. A more convincing evaluation would compare against a method that also uses multilayer structure but differently (e.g., per-layer CPD with aggregation).

### Minor

- **Confidence interval coverage degrades substantially under model misspecification.** Table 2 shows 76.67% coverage for Scenario 3 (n=100) vs. the nominal 95%, a gap of nearly 20 percentage points. While the paper acknowledges this ("Coverage is lower in Scenario 3, where violations of Model 1...pose greater challenges"), no diagnostic or adjustment is provided to help practitioners know when the intervals are unreliable. For a method whose key selling point is inference (not just detection), this limits practical utility.

- **Gap between theoretical threshold condition and empirical implementation.** Theorem 1 requires τ to lie between c_{τ,1} n√L log^{3/2}(T) and c_{τ,2} κ²Δ, with c_{τ,2} being a "sufficiently small" absolute constant. In practice, τ = 0.1 n√L log^{3/2}(T) is used, with no verification that the upper bound c_{τ,2}κ²Δ is satisfied across scenarios with different jump sizes κ and spacings Δ. The sensitivity analysis (Tables 5–8) tests different c_{τ,1} values but does not check whether the theoretical condition holds. This is a common gap in theoretical CPD papers, but it means the theoretical guarantee may not apply to the empirical results.

- **Real-data confidence intervals appear suspiciously narrow.** For the agricultural trade network (T=35), confidence intervals are extremely tight (e.g., [5.97, 6.03] for a detected change point at time 6, spanning only ~0.06 years). This suggests the variance estimator σ̂² may be systematically underestimating uncertainty, or the intervals are over-confident due to the limited time horizon. The paper does not validate the variance estimator's accuracy.

- **The Δ=Θ(T) spacing assumption is violated in Scenarios 2 and 4 (min spacing of 20 vs T=200) and is implausible for the real agricultural trade data (T=35).** The paper acknowledges that Scenarios 2 and 4 serve as robustness checks and notes this limitation in the conclusion. However, since the main theoretical results (and the confidence interval construction) depend on this assumption, the applicability to realistic settings with multiple densely-spaced change points is unclear.

### Trivial

- Table 4 lists a confidence interval for the year 2005 as (17.97, 18.05), while noting the detected time point is 20; this minor inconsistency in indexing could cause confusion.
- In the confidence interval procedure Step 4 (line 639), the division by κ̂_k includes a term 1{κ̂_k = 0} which appears to be a guard against division by zero, but κ̂_k=0 would imply no detected change — the handling of this edge case could be clarified.

## Nice-to-Haves

- A data-driven method for selecting the threshold τ (e.g., based on residual-based adaptive thresholding) would substantially strengthen the practical utility.
- A diagnostic check for whether the D-MRDPG assumption holds in a given segment would help practitioners know when confidence intervals are reliable.
- Ablation study comparing Stage I only vs. Stage I+Stage II to quantify the improvement from the tensor refinement stage.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The paper does not compare against any method that leverages D-MRDPG structure"** — The paper *does* compare against CPDonline (Wang et al., 2025) which is designed for D-MRDPGs, in Appendix G.1 (Table 13). The reviewer overlooked this.
- **"Missing appendix" style complaints** — The paper has a full appendix with proofs and additional results; the parser strips these sections for some readers but they exist.
- **"The confidence intervals are suspiciously narrow...suggests the variance estimator may be underestimating"** — This is speculation rather than a verified flaw. It's reasonable to flag but kept as a minor concern above rather than a major weakness.
- **"The comparison is not apples-to-apples: gSeg and kerSeg are general-purpose CPD methods"** — Kept as a real concern but adjusted from "fundamental design flaw" to a more measured "the main experimental comparison does not adequately support the claim."
- Generic strengths from Strength Finder that are superficial (e.g., "rigorous theoretical foundation") — These are merged into the core strengths with specific evidence.

## Novel Insights

The most notable insight across the reviews is the tension between the paper's theoretical ambition and practical execution. On one hand, the paper achieves something genuinely novel — deriving limiting distributions for change point estimators in network data — which opens the door to statistical inference (confidence intervals, hypothesis tests) in a domain that previously only had consistency results. On the other hand, the four-sequence independence assumption creates a formal gap between the theory and the implemented algorithm that is unusually explicit: the proofs require independence that the odd-even splitting cannot provide, yet the paper acknowledges this without bridging the gap. This pattern — strong theory with acknowledged but unresolved practical violations — is the central tension that the reviews converge on.

## Suggestions

1. **Address the four-sequence independence gap explicitly.** Either modify the algorithm to use proper four-way data splitting (e.g., split the time series into four independent blocks), or state clearly that the theoretical results apply to an idealized version of the algorithm and discuss what the practical consequences of the approximation might be. A simulation study comparing the theoretical four-sequence version against the practical two-sequence version would be highly informative.

2. **Strengthen the baseline comparisons.** Move the CPDonline and AutoCPD comparisons into the main text and add a baseline that aggregates per-layer CPD results (e.g., run Wang et al. 2021 on each layer separately, then merge). This would substantiate the claim of superior performance over structured alternatives.

3. **Validate the variance estimator** used in confidence interval construction via a simulation where the true σ² is known, and report estimated vs. true values. This would either confirm that the narrow real-data intervals are valid or reveal underestimation.

4. **Add an ablation study** removing Stage II to quantify the improvement from tensor refinement.

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/Ahdsg2nkNH.md` (Multilevel Control Functional) | 8.00 | Clean theory + experiments, no major flaws — stronger than this paper |
| `/home/wg25r/review_agent/human_reviews_2026/8J3GTeQmwl.md` (Graphon Cross-Validation) | 5.50 | Accepted as poster; minor concerns about proof clarity and scope — similar tier to this paper |
| `/home/wg25r/review_agent/human_reviews_2026/TeDkzf34hs.md` (Dense Associative Memory) | 7.00 | Strong theoretical work with verification experiments — stronger theoretical execution than this paper |
| `/home/wg25r/review_agent/human_reviews_2026/ilhWL2WPvS.md` (High-Dim Online CPD) | 4.50 | Rejected; some theory but experimental validation concerns — this paper has stronger theory |
| `/home/wg25r/review_agent/human_reviews_2026/lhY8Pa0u8d.md` (Poisson CPD) | 3.33 | Rejected; narrow scope and limited generalizability — this paper is stronger |
| `/home/wg25r/review_agent/human_reviews_2026/OH7joQ9jpl.md` (SPIDER) | 2.50 | Rejected; fundamentally flawed experiments — this paper is much stronger |
| `/home/wg25r/review_agent/human_reviews_2026/1CR1MTIgmq.md` (Attack on TPAMI) | 0.00 | Desk-reject level — not comparable |

This paper makes a genuine theoretical contribution (first limiting distributions for network change point estimators) that is stronger than the rejected CPD papers (4.50, 3.33) and comparable in theoretical depth to the accepted Graphon CV paper (5.50). However, the gap between the theoretical assumptions (four independent tensor sequences) and practical implementation (odd-even splitting), together with the baseline selection issue, are notable weaknesses that prevent it from reaching the 6+ range. The paper's theoretical novelty and thoroughness of the proofs are real strengths. Positioned relative to the anchors, this paper sits in the borderline accept range — comparable to the 5.50 Graphon CV paper in overall quality but with different trade-offs (stronger theory, weaker experimental validation).

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
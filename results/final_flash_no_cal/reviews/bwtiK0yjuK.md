Now I have all the information needed. Let me synthesize the final review.

## Summary

This paper studies offline change point localization and inference in dynamic multilayer random dot product graphs (D-MRDPGs). It proposes a two-stage algorithm combining seeded binary segmentation with low-rank tensor estimation (TH-PCA), establishes consistency for both the number and locations of change points, and derives the first limiting distributions for change point estimators in network data. A fully data-driven confidence interval procedure is developed and validated on simulations and a real agricultural trade network.

## Strengths

1. **First consistency guarantee for offline change point detection in dynamic multilayer networks.** Theorem 1 shows that with high probability the two-stage algorithm correctly estimates the number of change points and bounds localization error at \(O(\kappa_k^{-2}\log T)\). This extends single-layer results (Wang et al., 2021) to the multilayer setting while maintaining comparable rates (Remark 1). The result is non-trivial because the multilayer structure introduces tensor-valued observations and requires low-rank estimation.

2. **First derivation of limiting distributions for change point estimators in network data.** Theorem 2 obtains the asymptotic distribution of the refined estimator under vanishing jumps, leading to a two-sided Brownian motion process. The paper claims this is the first result of its kind in the network literature, and given the state of the field this claim is credible. The accompanying data-driven confidence interval procedure (Section 3.1) is a practical translation of this theory and achieves strong coverage in simulations (Table 2: 100% coverage in three of four scenarios at \(n=100\)).

3. **Empirical outperformance across diverse scenarios.** Table 1 shows CPDmrdpg consistently achieving lower \(|\hat{K}-K|\), smaller Hausdorff distances, and higher time-segment coverage than gSeg and kerSeg across four settings, including two scenarios (2 and 3) that violate Model 1 assumptions, demonstrating robustness. The improvement is substantial: competitors often yield infinite Hausdorff distances (indicating missed change points) while CPDmrdpg produces nearly perfect estimates.

4. **Computational efficiency.** The overall complexity \(O(T n^2 L r \log^2(T \vee n))\) is polynomial in all key dimensions and is explicitly stated, aiding reproducibility and scalability assessment.

## Weaknesses

### Fatal
None.

### Major

**1. Gap between theoretical independence assumption and practical implementation.**  
The theoretical guarantees (Theorems 1 and 2) are derived under the assumption of four mutually independent adjacency tensor sequences \(\{\mathbf{A}(t)\},\{\mathbf{A}'(t)\},\{\mathbf{B}(t)\},\{\mathbf{B}'(t)\}\). As defined in Algorithm 1, Stage I uses \(\mathbf{A},\mathbf{B}\) and Stage II uses \(\mathbf{A}',\mathbf{B}'\) in the refined scan statistics (Definition 5). The paper explicitly states (Section 2.2, after Algorithm 1) that in practice—and in all numerical experiments—only *two* sequences obtained via odd-even splitting are used, with both stages operating on the same two splits. This means independence across all four roles cannot hold (e.g., \(\mathbf{A} = \mathbf{A}'\) in practice). The paper acknowledges this as "imposed for theoretical convenience" but provides no argument—either theoretical or via controlled simulations—that the odd-even implementation preserves the required stochastic properties or that the theoretical results remain valid under the actual data reuse pattern. Because the core consistency and distributional claims rest on this independence structure, the connection between theory and evidence is incomplete. This is a significant gap that the authors should address in revision.

### Minor

**2. Mismatch between Table 4 presentation and the CI construction procedure.**  
Table 4 reports "Detected change point from Algorithm 1" alongside 95% confidence intervals constructed via Section 3.1. The CI procedure uses the *refined* estimators \(\hat{\eta}_k\) from equation (5), not the Algorithm 1 output \(\tilde{\eta}_k\). For the 2005 detection (time point 20), the reported CI is (17.97, 18.05), which does not contain 20; similarly for 2013 (time point 28) the CI is (25.99, 26.06), not containing 28. If \(\hat{\eta}_k\) differs from \(\tilde{\eta}_k\), the table is presenting mismatched information without explaining the distinction. If the CIs are for the same estimates, the misalignment suggests a calibration problem at \(T=35\). Either way, the table as presented is unclear and potentially misleading.

**3. Limited baseline comparison.**  
The main-text comparison is restricted to gSeg and kerSeg, two generic graph-sequence methods not designed for multilayer networks. The paper mentions additional comparisons with an online method (Wang et al., 2025) and a deep-learning approach (Li et al., 2024) but defers all results to the appendix. The claim of "substantially outperform[ing] existing state-of-the-art algorithms" (Section 1.1) is therefore only weakly supported in the main text, since the methods compared are not SOTA for this specific problem. Including a summary of the appendix comparisons in the main text would strengthen the evidence.

**4. No small-sample validation of the CI procedure.**  
The real-data analysis uses \(T=35\) time points, but the CI coverage simulations (Table 2) use \(T=200\). The CIs reported in Table 4 have widths on the order of 0.04–0.08 time units, which is very narrow for \(T=35\). Without a simulation study at \(T=35\) (with comparable \(n=75\), \(L=4\)), it is unclear whether the coverage is reliable in the real-data setting.

**5. Rank selection for TH-PCA not addressed.**  
The input ranks \((d, d, m_{b_k}^{s_k,e_k})\) for TH-PCA require knowledge of the rank of the CUSUM-transformed weight matrices, which is unknown in practice. The simulations use fixed generous ranks (\(r_1=r_2=15\), \(r_3=L\)) with a brief sensitivity check in the appendix, but no data-driven rank-selection procedure is provided or discussed. This limits the off-the-shelf applicability of the method.

### Trivial
None.

## Nice-to-Haves

- Provide a simulation study at \(T=35\) matching the real-data dimensions to validate CI coverage in small samples.
- Summarize the appendix comparisons with Wang et al. (2025) and Li et al. (2024) in the main text, or temper the "state-of-the-art" language.
- Clarify the relationship between \(\tilde{\eta}_k\) (Algorithm 1 output) and \(\hat{\eta}_k\) (Section 3 refinement) in Table 4, or report a single consistent set of estimates.
- Provide guidance or a reference for rank selection in TH-PCA when the true ranks are unknown.

## Removed Points

These points from the inputs are removed per the consolidation rules:

- **"Typographical issue in Definition 3"** – This is a formatting/rendering artifact, not a content error. Removed.
- **"Missing appendix proofs for non-vanishing regime"** – The rules disallow penalizing missing appendix content that the parser strips. Removed.
- **"Theorem 2 limiting process defined for integers but involving continuous Brownian motion"** – This is a standard technical presentation pattern in the change-point literature (the argmin is taken over integer \(r\), but the driving process is continuous). Not a genuine weakness. Removed.
- **"Normalization factor mismatch between Theorem 2 and Section 3.1"** – The \(\sqrt{T}\) scaling in \(\hat{\mathcal{P}}_k^b(r)\) is explained by the simulation-based approximation to the limiting process; the connection is standard in this literature (cf. Xu et al., 2024). Removed as a nitpick.
- **"Threshold choice sensitivity"** – The paper mentions a sensitivity analysis in the appendix; this is standard practice. Removed.
- **"Computational complexity notation missing dependence on seeded intervals"** – The paper notes \(|\mathcal{J}|=O(\log T)\), which is absorbed. Removed.
- **"Harsh critic claims about the confidence intervals being 'unrealistic' and 'implausible'"** – The critic's assertion that CIs of width 0.06 time units are "implausible" is an opinion, not a demonstrable error. The narrowness could follow from strong signal. However, the *underlying concern* about small-\(T\) validation is retained as Minor weakness 4 above. The "implausible" framing is removed.
- **Strength Finder's claim about "real-world validation with interpretable change points"** – This is moderate evidence but not generic; retained in Strengths but scaled down in tone.
- **Strength Finder's claim about "explicit computational complexity"** – This is a minor but specific point; kept in Strengths.

## Novel Insights

None beyond the paper's own contributions. The most striking observation from the reviews is that the independence gap, though acknowledged in one sentence, is the single issue that most directly affects the connection between theory and practice. The paper would be significantly strengthened by either (a) a theoretical argument showing why the two-sequence implementation inherits the same guarantees, or (b) a modification of the algorithm to genuinely use four independent sequences.

## Suggestions

- Address the independence gap directly: either prove that the odd-even splitting preserves the required properties for the two-stage procedure (e.g., by conditioning arguments or by showing the stages operate on independent time blocks), or adjust the algorithm to use four genuinely independent splits.
- Add a small-\(T\) simulation matching the agricultural trade network dimensions (\(T=35\), \(n=75\), \(L=4\)) to validate CI coverage before presenting real-data intervals.
- Clarify Table 4: distinguish between Algorithm 1 output (\(\tilde{\eta}_k\)) and the Section 3 refined estimates (\(\hat{\eta}_k\)) used for CI construction, or report a unified set.
- Include a brief summary of the appendix comparisons (Wang et al., 2025; Li et al., 2024) in the main text, or moderate the "state-of-the-art" claim to reflect the baseline scope.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
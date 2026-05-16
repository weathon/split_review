Now I have all the information I need to synthesize the final review. Let me compose it.

**Important note**: The tables (Table 1, Table 2, Table 3) are embedded as JPG images in the PDF. I cannot read the actual numerical values from these images. The specific numbers the harsh critic cites (70.9 for UGM, 72.0 for URL, etc.) do not appear anywhere in the text of the paper — they can only come from reading the image-based tables. This means I cannot independently verify the critic's central claim about a Table 1 contradiction. I will note this clearly.

---

## Summary
This paper proposes Universe Graph Matching (UGM) for partial graph matching, decomposing the problem into two sub-problems: (1) a learned structured universe graph (with both node and edge embeddings) that handles occlusions by serving as a bridge between input graphs via $\mathbf{X}_{ij}=\mathbf{X}_{iu}\mathbf{X}_{ju}^\top$, and (2) an energy-based out-of-distribution (OOD) detection module that filters annotation-error outliers *before* matching. Evaluated on Pascal VOC and Willow Object datasets across occlusion, random outlier, and combined settings, UGM shows consistent improvements over several learning-based baselines.

## Strengths

- **Clean conceptual separation of two distinct partial-matching challenges.** The paper clearly identifies that occlusion-caused missing points and annotation-error outliers require fundamentally different treatments (Section 1, lines 29–30). Occluded keypoints can still be matched through a universe graph, while erroneous annotations are meaningless and should be removed. This framing is well-motivated and leads to a principled two-component design.

- **Structured universe graph goes beyond universe point representations.** Unlike URL (Nurlanov et al., 2023), which only learns universe *point* embeddings, UGM learns both node *and* edge embeddings for a complete directed universe graph (Section 3.1, lines 68–74). The ablation study (Table 4) confirms that edge learning contributes positively: removing it drops F1 from 65.1 to 60.2 in the Pascal VOC random-outlier setting.

- **Pre-matching OOD filtering avoids the pitfalls of post-hoc outlier removal.** Prior work like AFAT discards matches after the matching solution is already computed — by which point outliers may have already corrupted the solution. UGM filters outliers *before* solving the matching (Section 3.2, Eqs. 10–14), and the energy-based formulation requires no additional trainable parameters. The ablation confirms this component is critical: removing the filter causes the largest single drop (62.1 → 54.7 in Table 4).

- **Consistent gains across multiple challenging settings.** On Willow Object in the occlusion+outlier setting, UGM achieves 71.1% F1 vs. 65.2% for the next best (GCAN), a 5.9-point margin. On Willow occlusion-only, the lead over GCAN is 9.7 points (Table 3). These margins are substantial in the graph matching literature.

- **Hyperparameter sensitivity analysis.** Figure 4 examines the impact of temperature $T$, threshold $\tau$, and margin values $m_{in}, m_{out}$, showing that performance is relatively stable across reasonable ranges. This strengthens confidence in the method's robustness.

## Weaknesses

### Fatal
None.

The harsh critic raises a potentially fatal concern about a contradiction between Table 1 and the paper's text claim that "UGM outperforms the best-performing SOTA model by 2.2% in terms of average F1 score" (line 196). However, **the tables are embedded as images in the PDF and the specific numerical values cited by the critic (e.g., UGM 70.9, URL 72.0) do not appear in the paper's text and cannot be independently verified from the available file.** If the numbers in Table 1 indeed show URL outperforming UGM as claimed, this would be a fatal inconsistency requiring immediate correction. If the critic has misread the table (e.g., swapped column positions), then no contradiction exists. This ambiguity must be resolved by the authors — they should explicitly state the numerical values from Table 1 in the text and confirm whether the 2.2% claim is accurate.

### Major

- **Strongest competitor (URL) is missing from two of three main evaluation settings.** The paper honestly reports it could not replicate URL and DLGM due to unavailable code (line 182). Consequently, URL — which, if the critic's reading of Table 1 is correct, is the top performer in the unfiltered Pascal VOC setting — is absent from Table 2 (Pascal VOC random outlier) and Table 3 (all Willow Object settings). This means the claim "consistently outperforms state-of-the-art methods across all tested scenarios" is not fully supported by the evidence, since the strongest competitor from Table 1 is not compared in most settings. The paper should explicitly discuss how this gap affects the strength of its comparative claims.

- **No validation that the OOD filter does not harm occlusion-only performance.** The OOD filter removes nodes with energy scores above a threshold. Occluded keypoints may produce poor affinity scores against the universe graph (since the visual evidence is missing), potentially leading to high energy and erroneous removal. The ablation study (Table 4) only evaluates the Pascal VOC *random outlier* setting, not an occlusion-only setting. A comparison of UGM with and without the OOD filter on Willow occlusion-only (where no synthetic outliers are present) is missing. If the filter degrades performance when no outliers exist, its design would need revision. This is a straightforward experiment the paper should include.

### Minor

- **OOD training uses only synthetic outliers; no evaluation on realistic annotation errors.** The OOD margin loss (Eq. 9) requires out-of-distribution training data $\mathcal{D}_{out}$, generated as random coordinate points (line 178). Real annotation errors (e.g., mislabeled keypoints, systematic shifts) may differ from uniformly random coordinates. The paper acknowledges that "erroneously annotated outliers are generated through random and unpredictable factors" (line 119), but provides no experiment with realistic or manually-introduced annotation errors. This limits the strength of the OOD detection claim.

- **No measure of variance or confidence intervals.** All tables report point estimates of F1 scores without standard deviations, confidence intervals, or multi-run statistics. When performance margins are narrow (e.g., 1.7% on Willow random outlier), it is unclear whether the differences are statistically significant. While single-run evaluation is common in graph matching benchmarks, reporting some measure of stability would strengthen the paper.

- **Missing URL baseline from Willow experiments lowers confidence in occlusion-setting claims.** The 9.7% lead over GCAN on Willow occlusion is impressive, but GCAN is a 2022 method. URL (2023) — which, like UGM, uses a universe representation — is not included. Since URL's code is unavailable, this is understandable, but it means the claim of "outperforms SOTA" in the occlusion setting rests on comparison with older methods.

### Trivial
- Line 182 cites "URL (Lin et al., 2023)" while lines 27 and 52 correctly cite "URL (Nurlanov et al., 2023)" — a citation inconsistency.
- Line 196: "unflitered" → "unfiltered."
- Some notation in the edge supervision derivation ($y_e = y_n(EdgeID(0)) \times n_u + y_n(EdgeID(1))$ at line 99) would benefit from a brief explanation that this creates a unique class for each directed edge pair by flattening the $n_u \times n_u$ edge space.

## Nice-to-Haves
- Compare the OOD filter against a simpler alternative (e.g., thresholding on max node affinity or a learned binary classifier) to show the energy-based formulation adds value beyond generic outlier removal.
- Evaluate on real annotation errors (e.g., artificially mislabeling keypoints in the test set) to validate synthetic-data generalization.
- Add standard deviation or confidence intervals across multiple runs or seeds.

## Removed Points
These points are flagged to be removed; treat them with caution.

1. **Criticism about "unfair comparison" with classical solvers (pre-trained BBGM affinities used).** The paper explicitly states this procedure (line 182) and it is standard practice — it ensures a fair comparison of solvers with identical affinities. If anything, this favors classical solvers by giving them modern learned features.

2. **Criticism about missing reproducibility details (backbone, optimizer, learning rate, etc.).** These details are standard for an appendix, which the parser strips from all papers. The paper provides sufficient methodological description for a main-text submission (uses BBGM framework, Spline Convolution backbone, cross-entropy loss, LPMP solver, etc.).

3. **Criticism about the edge supervision derivation being "underspecified."** The formulation $y_e = y_n(EdgeID(0)) \times n_u + y_n(EdgeID(1))$ is a standard way to create multi-class labels for directed edges from node labels in a complete graph. While dense, it is correct and reproducible.

4. **Criticism about missing values in Table 2 (empty entries / "—").** Cannot be verified from the image-based table. If some methods were not evaluated on certain categories, the paper should clarify how averages are computed — but this is not confirmed as a real issue.

5. **The Strength Finder's claimed strength about "comprehensive and fair evaluation"** — conflicts with the verified weakness about missing URL baselines, so it is removed.

## Novel Insights
None beyond the paper's own contributions. The reviews do surface one useful observation not foregrounded in the paper: the need to validate that the OOD filter does not interfere with occlusion handling. This tension between the two components is worth examining but does not constitute a novel insight per se.

## Suggestions
1. **Clarify the Table 1 numbers.** Since the text claims a 2.2% improvement but the critic reads the table differently, explicitly state the F1 values of all methods (including URL) in the text alongside the 2.2% claim, and identify which method is considered "best-performing SOTA."
2. **Add an occlusion-only ablation** on Willow comparing full UGM vs. UGM without the OOD filter. This directly tests whether the filter has any negative side effect on occlusion handling.
3. **Acknowledge and discuss the URL absence** from Tables 2–3 more prominently. If URL is the strongest method on unfiltered Pascal VOC, its absence from the other settings is a notable gap that should be addressed in the limitations.
4. **Consider reporting multi-run statistics** or at minimum explaining why single-run results are standard and reliable in this benchmark.

## Score and Decision

The paper proposes a conceptually clean and well-motivated decomposition of the partial matching problem, with a reasonable two-component design. The Willow Object results are strong, and the ablation studies support the contribution of each component. However, the evaluation is weakened by the absence of the strongest competitor (URL) from most settings, and the potential Table 1 inconsistency (which cannot be verified without the image) creates uncertainty around the paper's flagship quantitative claim. These issues are addressable in a major revision but prevent full acceptance in the current form.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
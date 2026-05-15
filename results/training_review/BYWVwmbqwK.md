Now I have a thorough understanding of the paper. Let me produce the consolidated review.

---

## Summary

The paper proposes Wavelet Optimal Transport (WOT), a multi-resolution optimal transport framework that aligns unpaired datasets by minimizing discrepancies across spectral graph wavelet coefficients at multiple scales. Two filter implementations are introduced — entropy-based (E-WOT) and learned (L-WOT) — to suppress uninformative or noisy signal components. The method is evaluated on bifurcation matching, shape correspondence (SHREC20), and two real single-cell multi-omics datasets (scGEM, SNARE-seq), where it achieves substantial improvements over prior OT-based alignment methods.

## Strengths

- **Multi-scale wavelet representation enables robust alignment under noise and non-isometry.** The WOT distance (Eq. 3) leverages spectral graph wavelet coefficients across multiple scales, capturing both local and global structure. In the bifurcation experiment (Figure 3), WOT maintains significantly lower FOSCTTM than GW-OT at high noise levels (variance 0.065–0.15 of average distance) and under high dropout fractions, directly supporting the paper's claim of robustness advantages.

- **Two principled filtering strategies systematically remove uninformative signal components.** E-WOT (Eq. 5) uses entropy estimated via KDE as scale-specific weights, while L-WOT (Algorithm 1) jointly learns filters to maximize structural mismatch under a norm constraint. These are validated on real single-cell data (Table 2): E-WOT achieves 0.961 label transfer accuracy on SNARE-seq, and L-WOT achieves 0.616 on scGEM, both substantially outperforming prior methods.

- **State-of-the-art results on two real single-cell multi-omics datasets in a completely unpaired setting.** On scGEM (gene expression + DNA methylation, 177 cells) and SNARE-seq (chromatin accessibility + gene expression, 1047 cells), WOT variants achieve the highest label transfer accuracy in Table 2. For example, L-WOT (simple tight) at 0.616 on scGEM exceeds the next best method (SCOTv2 at 0.509), while E-WOT (heat kernel) at 0.961 on SNARE-seq exceeds SCOT at 0.852 — representing a meaningful advance over prior OT-based approaches.

- **Strong performance on non-isometric manifolds, a key challenge in single-cell modality alignment.** On SHREC20 shape correspondence (Table 1, Figure 4), WOT achieves the lowest mean relative geodesic error and highest percentage of matches within 0.25 error on test sets with highly non-isometric shapes (test set 2: WOT mean 0.076 vs. GW-OT 0.136). The sharp "elbow" of WOT's cumulative error curve (Figure 4) indicates it finds accurate correspondences at low error tolerances.

- **Theoretical connection to Gromov-Wasserstein distance (Remark 1).** The paper shows that with a single-scale heat kernel and identity filters, WOT reduces to a geodesic-RBF-based GW distance, establishing that the proposed framework subsumes existing GW-OT as a special case.

## Weaknesses

### Fatal
None. The paper's core claims are supported by experimental evidence, and no fundamental flaw invalidates the overall contribution.

### Major

- **Graph construction is underspecified, affecting reproducibility.** The entire WOT framework depends on a "fully connected weighted graph" with adjacency matrix \(W\) (Section 3.1), but the paper never specifies the weighting function — what similarity metric, kernel, bandwidth, or normalization is used to compute \(W\)? This choice propagates through the graph Laplacian, wavelet coefficients, and ultimately the transport cost. Without this detail, the method cannot be independently reproduced, and it is unclear whether the strong results on real data are driven by the wavelet framework or by a particular graph construction that happens to work well. (This is fixable in revision by stating the chosen similarity function and any hyperparameters used.)

### Minor

- **The aggregation operation ("agg") is enumerated but not specified for experiments.** The paper lists "sum, max, and mean" as possible aggregation operations over scales (Section 3.2) but never states which one is used in the experiments. This is a missing implementation detail that should be clarified.

- **The dropout experiment uses a non-standard definition that limits its relevance.** The paper explicitly redefines dropout as adding high-variance noise to a fraction of points (Section 4.1) rather than the standard zero-inflation masking found in single-cell data. While the experiment still tests robustness to corruption, the paper acknowledges this deviation ("We revise the conventional definitions of dropout to a more difficult scenario"), and the results should be interpreted accordingly. The claim of advantage "in higher regimes of dropout" would be strengthened by also testing actual zero-inflation.

- **Standard deviations or error bars are not reported for the main single-cell results (Table 2).** The paper notes in the bifurcation experiment that "the variance of WOT's mean FOSCTTM is significantly greater than GW" (Section 4.1), yet the headline results in Table 2 are reported as point estimates without variance. Given the small sample size of scGEM (177 cells) and the observed variance in the controlled experiment, error bars are needed to assess whether the reported improvements are statistically significant.

- **The choice of a fully connected graph over a k-NN graph (standard in single-cell analysis) is not justified.** A fully connected graph with a similarity kernel can be dominated by spurious correlations in high dimensions; k-NN graphs are more commonly used for single-cell data. The paper does not discuss this design choice or its potential impact on results.

- **No limitations section.** The paper does not discuss limitations such as sensitivity to the graph construction, computational scaling to larger datasets, or the choice of wavelet kernel — all of which would be useful for practitioners.

### Trivial

- Remark 1 mentions a "geodesic-RBF kernel discrepancy" without defining the term, making the theoretical connection slightly imprecise.
- The "average distance between samples" used to scale noise in the bifurcation experiment is not explicitly defined (e.g., mean pairwise Euclidean distance? in the original or PCA-reduced space?).
- The heuristic that L-WOT filters are "weighted by the squared root of the entropy" (Section 3.4) appears as an ad-hoc addition without experimental justification.

## Nice-to-Haves

- An ablation comparing the three aggregation operations (sum, max, mean) would help users select the appropriate variant.
- Ablating the filter components in E-WOT (comparing entropy-based weighting against uniform weighting) would demonstrate that the entropy heuristic specifically contributes to performance.
- Testing with actual zero-inflation dropout would make the robustness experiments directly relevant to the motivating application.
- A runtime comparison between WOT and competing methods would help assess practical deployability.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Label transfer accuracy metric is not defined."** REMOVED because the paper states it uses barycentric projection (line 167) and references the standard metric from Cao et al. (2020). The reviewer's claim that it is "never stated" is factually inaccurate.

- **"Unsupervised hyperparameter tuning procedure is hidden in the appendix."** REMOVED per hard rule: the parser strips appendix content from all papers, and this content exists in the original submission.

- **"Missing specialized shape matching methods in SHREC20 experiment."** REMOVED because the paper explicitly scopes this out: "We omit comparisons with shape-specific matching methods since they cannot be scaled to higher dimensions than 3D and would therefore not be useful for single-cell modality alignment." This is a deliberate scope choice, not an omission.

- **"Remark 1 overclaim"** about the limit analysis. REMOVED because the remark is explicitly stated as a theoretical connection, not a formal proof, and it serves its purpose of establishing that WOT subsumes GW-OT.

- **"Comparison may be unfair because SCOT/SCOTv2 may not use unsupervised tuning."** REMOVED because the competing results are taken from the original published paper (Demetci et al., 2022a), which is standard benchmarking practice. There is no evidence that the comparison is unfair.

## Novel Insights

Beyond the paper's own contributions, the reviews surface a recurring tension in this line of work: the method's reliance on a fully connected graph (which is not standard practice in single-cell analysis) and the underspecification of that graph construction. This suggests a broader observation — that spectral-graph-based optimal transport methods need to be more explicit about their preprocessing pipelines, as the graph construction choices can interact nontrivially with the downstream alignment quality. The community would benefit from a systematic study of graph construction sensitivity in single-cell OT alignment.

## Suggestions

1. **Specify the graph construction explicitly** — state the similarity function (e.g., Gaussian kernel with bandwidth \(\sigma\)), how \(\sigma\) is chosen (e.g., median pairwise distance heuristic), and whether any sparsification (e.g., k-NN thresholding) is applied.
2. **State which aggregation operation ("agg") is used in all experiments** — if it varies by dataset, report the choice per experiment.
3. **Add error bars or standard deviations to Table 2** to enable assessment of statistical significance, especially for scGEM (177 cells) where variability is a concern.
4. **Replace or complement the dropout experiment** with a standard zero-inflation masking procedure to strengthen the relevance to real single-cell data.
5. **Add a brief limitations paragraph** discussing sensitivity to graph construction, choice of wavelet kernel, and computational scaling.

## Score and Decision

**Originality:** High. The use of spectral graph wavelets to define a multi-scale structure-aware OT distance is novel and extends Gromov-Wasserstein in a principled direction.  
**Importance of research question:** High. Unpaired single-cell alignment is a practically important problem, and the paper directly addresses its unique challenges (noise, dropout, non-isometry).  
**Claims well-supported:** Mostly yes, though the unspecified graph construction and missing variance estimates for real-data results temper confidence.  
**Soundness of experiments:** Generally solid. Controlled experiments are well-designed, and the real-data results show large improvements. The dropout definition deviation and lack of error bars are the main weaknesses.  
**Clarity of writing:** Reasonable. The notation is sometimes dense but the framework is explained clearly.  
**Value to the research community:** Positive. The method is novel, the results are strong, and the approach is directly applicable to an active problem.

The paper presents a genuinely novel and empirically strong method for unpaired single-cell alignment. The core contribution — leveraging multi-scale spectral graph wavelets to define a robust OT distance — is creative and well-motivated. The reported results on real datasets represent a meaningful advance. The main weaknesses (underspecified graph construction, missing aggregation choice, no error bars on real-data results) are significant but fixable in revision and do not undermine the core claims. On balance, the paper merits acceptance.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
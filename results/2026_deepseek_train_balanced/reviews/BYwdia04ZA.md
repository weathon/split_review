## Summary

This paper proposes NNGS (Nearest Neighbor Graph Similarity), a metric that compares paired embedding spaces by computing the average Jaccard similarity of k-nearest-neighbor index sets across corresponding points. The metric has tunable locality via the neighborhood size k, is invariant to scaling, translation, orthonormal transformations, and dimensionality, and has a theoretically grounded lower bound under random data. The paper demonstrates NNGS's behavior on synthetic data (showing qualitative advantages over CKA), and presents two case studies (GloVe analogies and CLIP zero-shot classification) where NNGS correlates with task accuracy.

## Strengths

- **Tunable locality with a clear advantage over CKA demonstrated on synthetic data.** Table 1 convincingly shows that varying k lets NNGS detect local vs. global structural changes that CKA (even with RBF kernel and aggressive σ values) misses. The "Noise Within Blobs" row (NNGS(k=5)=0.03 vs. CKA Linear=0.99) is particularly striking — NNGS correctly identifies that local neighborhoods are destroyed while global structure is preserved. This is the paper's strongest evidence and is specific, concrete, and well-grounded.

- **Clean theoretical grounding for a null baseline.** Equation 6 derives a closed-form lower bound H(k)=k/(2(n-1)-k) from the hypergeometric distribution, giving practitioners a principled reference point: unrelated point clouds → H(k), identical clouds → 1. The derivation correctly acknowledges the dependence between neighborhoods and treats H(k) as a bound rather than an exact expectation.

- **Invariance properties are systematically characterized.** The paper demonstrates invariance to scaling/translation/orthonormal transformations (by construction, via rank invariance), to dimensionality above ~10 dimensions (Figure 5), and to point cloud size n when using relative neighborhood size c = k/(n-1) (Figure 4). These properties are non-trivial and practically useful for comparing embedding spaces of different dimensionalities or sizes.

- **Reproducibility is well-supported.** The paper provides anonymous code repositories for the method and all experiments, and specifies hardware and runtime (~1h total), which is uncommon in many submissions.

## Weaknesses

### Fatal

None.

### Major

- **Missing experimental details undermine the core correlational claims.** The paper reports Pearson's ρ=0.86 (p<10^{-4}) between NNGS and analogy accuracy but never states: (a) the number of analogy tasks/categories used (directly relevant to whether a correlation of 0.86 is reliable), (b) the GloVe embedding dimensionality, (c) how per-task accuracy is computed (e.g., 3COSADD?), and crucially (d) which k or c value was used to compute the reported ρ=0.86. Figure 4 shows NNGS curves across a range of c, but the correlation is a single number — it is unclear whether this is the best-case, average, or a specific c. Without these details, the headline result cannot be properly interpreted or reproduced.

- **No confidence intervals or uncertainty quantification for any correlation.** The paper claims that NNGS outperforms CKA in correlating with task accuracy (ρ=0.86 vs 0.74 for GloVe; ρ=0.77 vs 0.71 for CLIP original prompts; Table 2). These margins (0.06–0.12) are modest, and the paper provides no confidence bounds, bootstrap estimates, or significance tests for the difference between correlations. It is impossible for the reader to judge whether these gaps are meaningful or statistical noise. The synthetic experiments use bootstrapping responsibly, making this omission in the case studies more conspicuous.

- **The CLIP experiment's strongest headline number (ρ=0.90) is acknowledged as misleading, and the honest comparison shows only a marginal improvement.** The paper itself notes that the "all prompts" ρ=0.90 is "skewed because the added prompts seem to form a series of poorly-performing elements" (line 240). The fair comparison is ρ=0.77 (NNGS) vs. 0.71 (CKA) — a 0.06 difference on what appears to be ~80 data points (original prompt templates), with no confidence interval. The paper frames this as NNGS being "more effective in highlighting similarity aspects that correlate to the task-specific performance," which overstates the evidence.

### Minor

- **The two case studies test conceptually different types of paired representations without acknowledging the distinction.** The GloVe experiment compares two groups of points (countries vs. capitals) *within the same embedding space*, where a translation vector is assumed to map between them. The CLIP experiment compares the *same items* represented in *two different embedding spaces* (image encoder vs. text encoder), which are trained to be aligned. The meaning and interpretation of a high or low NNGS score differ between these settings; the paper treats them uniformly as "paired embedding similarity" without discussing how this affects interpretation or generalizability.

- **The CKA comparison in the case studies is underspecified.** For the GloVe experiment, the paper compares NNGS to *Linear* CKA (line 215), so the σ-tuning concern does not apply. However, the paper does not explain why Linear CKA (rather than RBF) is the appropriate baseline, or whether a different CKA configuration could yield higher correlation. For CLIP, the paper simply states "Results for the linear and the RBF kernel in CKA are similar" without reporting the actual values or the σ used for RBF. The comparison would be stronger with a systematic report.

- **The conclusion overclaims applications unsupported by current evidence.** The paper suggests NNGS could serve as an early-stopping criterion, guide model development via analogy task analysis, and inform prompt engineering (Conclusion, lines 266–267). The paper has only shown correlation in two specific settings — not that NNGS can *drive* improvements. These forward-looking claims should be hedged or removed.

- **No discussion of limitations or caveats.** The paper presents no limitations section. Important caveats — the correlational nature of the evidence, the small scale of the case studies, the potential sensitivity to the choice of k in practice, and the computational cost of computing k-NN graphs — are not discussed.

- **No computational complexity analysis.** k-NN graphs require O(n²) distance computations (or O(n log n) with approximate methods). For large n, this matters, especially compared to linear-kernel CKA which also costs O(n²). The paper should at least acknowledge scaling behavior.

### Trivial

- The lower bound derivation (Equation 6) correctly states E[J] ≥ H(k) but compresses the reasoning. The bound follows from plugging expected intersection size into the worst-case union denominator, which is reasonable, but readers unfamiliar with this argument would benefit from a step.

## Nice-to-Haves

- A sensitivity analysis over k for the CLIP experiment (e.g., k=3, 5, 10) would strengthen the justification for choosing k=3.
- Showing the GloVe scatter plot (Figure 5) with each analogy category labeled would help readers assess which categories drive the correlation.
- Reporting the ρ=0.86 for multiple k values would demonstrate robustness rather than dependence on a specific configuration.
- A systematic sweep over σ for CKA-RBF in both case studies, reporting the best achievable CKA correlation, would make the comparison more rigorous.

## Removed Points

The following points from the inputs were removed with reasons:

1. **Concern about CKA σ selection in case studies** — For GloVe, the paper compares against *Linear* CKA (no σ parameter). For CLIP, the paper states both linear and RBF kernels give similar results. The σ-tuning concern is largely addressed by the paper's own framing.
2. **"Standard GloVe analogy benchmarks have between 5 and 14 category-level comparisons"** — This is the critic's speculation, not stated in the paper. The paper simply omits the count, which is already captured as a missing-detail weakness above.
3. **"Equation (6) reasoning is sketchy"** — The paper correctly derives a conservative lower bound and explicitly acknowledges the dependence issue. The bound is mathematically sound; the presentation is compressed but not incorrect.
4. **Strength Finder's claim that NNGS "identifies categories of words not represented adequately for the analogy task"** — The paper shows correlation with accuracy, not a diagnostic capability for identifying problematic categories. This overclaim is already flagged as a minor weakness above.
5. **Generic/superficial strengths from Strength Finder** — Several strengths were repetitive framings of the same core contributions (e.g., multiple invariances listed separately when they are presented together in the paper). These are consolidated.

## Novel Insights

None beyond the paper's own contributions. The reviews largely affirm the paper's framing of its contributions (tunable locality, theoretical lower bound, invariance properties) and surface the gap between the clean synthetic evidence and the weaker real-world validation. No reviewer identified a genuinely novel interpretation or unexpected implication that the paper itself did not already articulate.

## Suggestions

1. **Provide full experimental details for the GloVe case study** — state the number of analogy tasks, the accuracy computation protocol, the GloVe dimensionality, and explicitly say which k (or c) value was used for the reported ρ=0.86. If the correlation was averaged over multiple k values, say so and report the range.

2. **Add bootstrap confidence intervals** for all reported correlations (GloVe and CLIP) and, where possible, for the *difference* between NNGS's and CKA's correlations. This is the single highest-leverage improvement.

3. **Add a limitations paragraph** that discusses: the correlational nature of the evidence, the small scale of the case studies, the need for sensitivity analysis on k, computational complexity, and the distinction between the two types of paired-representation settings tested.

4. **Tone down the forward-looking claims** in the conclusion (early stopping, prompt engineering guidance) unless they are explicitly supported by evidence in the paper.

5. **For the CLIP experiment**, report the correlation at multiple k values (e.g., k=3, 5, 10) to show robustness, and explicitly state the number of prompt templates used.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
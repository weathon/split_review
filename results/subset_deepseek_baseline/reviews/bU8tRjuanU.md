## Summary

The paper proposes LRACA, a deep multi-view clustering framework that combines three components: (1) category-aware anchor sampling to align semantic prototypes across views, (2) a dynamic low-rank attention mechanism with entropy regularization for efficient feature refinement, and (3) pseudo-label-guided cluster-level contrastive learning. The goal is to improve scalability and cross-view consistency on large-scale datasets. Experiments on six multi-view datasets are reported with comparisons to eight baselines.

## Strengths

- **Addresses a relevant problem**: Scalability and cross-view semantic alignment are genuine bottlenecks in deep multi-view clustering, and the paper identifies them clearly.
- **Novel combination of ideas**: The integration of category-aware anchors (via sub-clustering of pseudo-labels) with a learnable low-rank projection matrix and cluster-level contrastive learning is a reasonable design direction.
- **Evaluation on moderately large datasets**: The datasets used (up to 126k samples) go beyond typical small-scale MVC benchmarks, giving some credence to the scalability claims.

## Weaknesses

### Fatal
None.

### Major
- **Lack of clarity on dataset construction**: The paper does not specify how multi-view features are obtained for any dataset. For CIFAR-10, baselines such as k-means achieve 89.35% ACC and BMVC achieves 99.14% ACC—these values are implausible for raw pixel clustering and strongly suggest the use of pre-extracted, already discriminative features. Without this information, the experimental results cannot be properly interpreted, and the claimed superiority of LRACA may be an artifact of the chosen feature set.
- **Flawed complexity analysis**: The derived complexity formula (Section 3.3) contains terms like \(O(n_v^2 m^2 K)\) that are quadratic in batch size \(m\), contradicting the claim of linear complexity. The derivation mixes variables (batch size vs. dataset size, K-means iterations) without a clear asymptotic cost, making the efficiency argument unsubstantiated.
- **Incomplete ablation of the contrastive component**: The ablation study (Table 3) tests only the anchor alignment (AAC) and low-rank projection (LRP) modules, but the base “LC” (which apparently includes the contrastive loss) is never removed. Thus the contribution of the cluster-level contrastive learning itself is not quantified.
- **Inconsistent state-of-the-art claims**: LRACA does not consistently outperform all baselines. For example, on YouTubeFaceSel, GC-CMVC achieves higher ACC (34.10 vs. 33.75); on NUSWIDEOBJ, FSMSC achieves higher ACC (19.03 vs. 17.64). The claim of “significantly outperforming” is not supported across all metrics and datasets.
- **Unaddressed risk of error propagation**: Pseudo-labels are obtained from K-means on fused features, then used to generate anchors via per-cluster K-means, and anchors are aligned across views. If the initial pseudo-labels are noisy, anchors may reinforce incorrect semantics. No analysis of pseudo-label quality, convergence, or robustness to noise is provided.

### Minor
- **Equations 10 lack clarity**: \(\tilde{K}\) and \(\tilde{V}\) are computed identically (both as \(\text{softmax}(\mathbf{X}\Theta^\top)^\top \mathbf{X}\)), whereas keys and values typically use different projections. The intention is unclear.
- **Attention output dimension**: The output of Equation 11 is \(\mathbb{R}^{N \times k}\), yet multi-head concatenation (Equation 13) projects to \(\mathbb{R}^{N \times d}\). The relationship between \(k\) and \(d\) is not discussed, and no analysis of rank choice is given beyond the sensitivity study on \(k\).
- **Missing runtime or memory comparisons**: The paper claims computational benefits but does not provide wall-clock time, GPU memory usage, or actual speed comparisons against baselines—only a theoretical complexity sketch.
- **Baseline descriptions** omit important details: For instance, the paper does not state whether views for comparison methods are used as-is or if preprocessing (e.g., PCA) is applied.

### Trivial
- Some equation numbers (e.g., for Equations 9, 10, 11) are not labeled in the main text, making cross-referencing awkward.
- Figure 1 caption is garbled due to parsing, but this is a parser artifact.

## Nice-to-Haves

- Clearly describe the multi-view feature extraction for each dataset (e.g., which pre-trained models or hand-crafted features are used) to allow reproducibility.
- Provide empirical runtime and memory consumption charts to validate the linear-complexity claim.
- Include an ablation that removes the cluster-level contrastive loss entirely, to isolate its effect.
- Report the stability of pseudo-labels across training epochs (e.g., label purity or cluster assignment changes).

## Novel Insights

None beyond the paper’s own contributions.

## Suggestions

1. Revise the complexity analysis to derive a clean per-iteration cost and empirically verify linear scaling with sample size (e.g., plotting time vs. N).
2. Add a table describing the view construction procedure for each dataset, and if pre-computed features are used, note their dimensionality and source.
3. Perform an ablation that compares the full LRACA against a version without the contrastive loss (i.e., only reconstruction + anchor alignment + entropy) to quantify the benefit of contrastive learning.
4. Discuss limitations: under what conditions might the iterative pseudo-label refinement fail (e.g., severe view heterogeneity, very large number of clusters)?
5. Report standard deviations over multiple runs to assess statistical significance of the performance gains.

## Score and Decision

The paper tackles an important problem and proposes a reasonable combination of techniques. However, major weaknesses—including unclear dataset construction that makes baseline numbers suspect, an unsupported complexity analysis, incomplete ablation of the core contrastive module, and inconsistent SOTA performance—prevent acceptance. The work would benefit from substantial revisions and additional experiments before being suitable for a top venue.

MY FINAL SCORE: <score>4.0</score>  
MY FINAL DECISION: <decision>Reject</decision>
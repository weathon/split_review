## Summary

The paper proposes LRACA, a deep multi-view clustering framework that introduces category-aware anchor generation for cross-view semantic alignment, a dynamic low-rank attention mechanism with entropy regularization for efficient discriminative feature extraction, and pseudo-label-guided cluster-level contrastive learning. Experiments on six multi-view datasets report state-of-the-art performance.

## Strengths

- **Addresses a practical problem**: The paper targets scalability and cross-view consistency in deep multi-view clustering, which are real bottlenecks for large-scale applications.
- **Clear motivation of design**: The anchor alignment loss (𝒲_{align-anchor}) and entropy regularization (𝒲_{ent}) are well-motivated to address semantic drift and degenerate attention.
- **Strong empirical results**: Table 2 shows that LRACA achieves superior or competitive ACC/NMI/PURITY across all six datasets, often outperforming previous methods by non-trivial margins (e.g., +2% ACC on YouTubeFace50, +1pt NMI on TinyImageNet).
- **Ablation validates components**: Table 3 demonstrates that both the anchor alignment constraint (AAC) and low-rank projection (LRP) contribute positively, with their combination giving best performance.

## Weaknesses

### Major

1. **Missing specification of multi-view dataset construction**: The paper uses CIFAR-10, TinyImageNet, Fashion (likely Fashion-MNIST), YouTubeFace, and NUSWIDEOBJ—all originally single-view or without multi-view splits. It does not describe how multiple views are generated for each dataset (e.g., different feature types, image partitions, or augmentations). This omission makes the experimental setup irreproducible and the reported results unverifiable. In multi-view clustering literature, such specification is standard; its absence is a critical reproducibility issue.

2. **Mischaracterization of “cluster-level” contrastive learning**: The proposed contrastive loss (Eq. 15) defines positive pairs as the same sample across views and negative pairs as different samples, which is standard *instance-level* contrastive learning. The use of soft probability vectors derived from pseudo-labels does not change the pairing logic to cluster-level. The claim that this is “cluster-level contrastive learning” is misleading and the novelty over instance-level methods (e.g., MFLVC) is overstated.

3. **Incomplete and internally inconsistent complexity analysis**: Section 3.3 claims linear complexity, but the derived expression includes a term O(n_v² m² K), which is quadratic in batch size and cluster count—undermining the central scalability argument. Moreover, no empirical runtime or memory usage comparisons against baselines are provided, so the practical scalability claim is unsubstantiated.

4. **Insufficient ablation study**: Table 3 evaluates variants by removing AAC or LRP, but it does not ablate the contrastive loss itself (i.e., a baseline without 𝒲_c). Since cluster-level contrastive learning is one of the three key contributions, its individual contribution must be isolated to validate the design.

### Minor

- The paper states that on large-scale datasets, some baselines encounter out-of-memory errors, but it does not report which, nor provide runtime or memory numbers for LRACA.
- Parameter sensitivity analysis (Figs. 2–3) is limited to two datasets; the generalizability to the other four large datasets is not shown.
- The algorithm outline (Algorithm 1) is too coarse to be reproducible; steps like “Calculate entropy regularization” lack detail on when anchors are updated relative to pseudo-labels.

### Trivial

- Some figure captions are garbled by OCR, but this does not affect evaluation.

## Nice-to-Haves

- Provide a clear description of how each dataset is turned into a multi-view dataset (e.g., hand-crafted features, random augmentations, or data splits).
- Include a table comparing actual training time and peak memory usage against the strongest baselines on the largest datasets.
- Perform an ablation that removes the contrastive loss entirely to quantify its specific benefit.

## Novel Insights

None beyond the paper’s own contributions, which are not fully validated. The integration of anchor alignment with low-rank attention is plausible, but the cluster-level contrastive claim lacks novelty.

## Suggestions

- Specify **exactly** how each dataset was made multi-view (e.g., “for CIFAR-10, we extract CNN features from three different pre-trained architectures” or “we partition images into four non-overlapping patches”). Without this, the experiments cannot be repeated.
- Rename “cluster-level contrastive learning” to “pseudo-label-guided instance contrastive learning” to accurately describe the method.
- Provide a corrected complexity analysis with a clear breakdown that justifies the claimed O(N) complexity and clarify the contradictory quadratic term.
- Add an ablation row for “LC only” (i.e., without AAC and LRP) so the contribution of contrastive loss itself is measurable.

## Score and Decision

**Score**: 3  
**Decision**: Reject

The paper tackles a relevant problem and shows strong empirical results, but the missing dataset-view specification critically undermines reproducibility, and the core novelty of “cluster-level contrastive learning” is mischaracterized. The complexity analysis is inconsistent, and the ablation is incomplete. These major weaknesses prevent acceptance.

MY FINAL SCORE: <score>3</score>  
MY FINAL DECISION: <decision>Reject</decision>
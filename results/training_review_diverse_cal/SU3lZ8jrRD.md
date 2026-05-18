Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper proposes Spectral Spatial Traversing (SST), a set of three strategies to improve Mamba-based networks for point cloud processing. The core idea is to use the eigenvectors of the Random Walk Laplacian of the patch-adjacency graph to define an isometry-invariant traversal order (SAST), complemented by a hierarchical recursive partitioning strategy for segmentation (HLT) and a token repositioning mechanism for masked autoencoding (TAR). The method is evaluated on ModelNet40, ScanObjectNN, ShapeNetPart, and few-shot benchmarks, showing improvements over the Point-Mamba baseline.

## Strengths

- **SAST provides a principled, isometry-invariant token ordering.** Using the low-frequency eigenvectors of the Random Walk Laplacian to define traversal order is well-motivated theoretically (Section 3.1, Property 4). Unlike 3D-grid-based traversals (Point-Mamba, PCM), this approach is rotation/viewpoint-invariant and respects the surface manifold structure. The paper reports consistent improvements over Point-Mamba across multiple benchmarks.

- **HLT adapts spectral traversal to segmentation via recursive binary partitioning.** By combining all \(s\) smallest eigenvectors through a normalized-cuts-inspired partitioning, HLT enables the network to distinguish spatially localized regions (e.g., limbs, head) that SAST's per-eigenvector traversals cannot separate (Section 3.4, Figure 3). The paper reports that SST+HLT outperforms SST+SAST on ShapeNetPart segmentation (Table 2).

- **TAR addresses a genuine problem with MAE in Mamba networks.** Transformers can place masked tokens anywhere because self-attention is position-agnostic, but Mamba's order-sensitivity makes this harmful. TAR's solution — restoring learnable tokens to their original positions rather than appending them — is clean and effective, yielding a ~0.9% improvement in linear SVM accuracy (Figure 5).

- **Ablation studies validate key design choices.** Figure 4 shows that four non-constant eigenvectors are optimal (more degrade performance by encoding high-frequency noise) and that 20 nearest neighbors for the adjacency graph is best. These provide practical guidance for practitioners.

- **Evaluation across multiple tasks and settings.** The method is tested on object classification (ModelNet40, ScanObjectNN), few-shot learning (ModelNet40), and part segmentation (ShapeNetPart), under both from-scratch and pretrained settings (Tables 1–4).

## Weaknesses

### Fatal

None.

### Major

1. **Missing comparison to PCM, the other Mamba-based point-cloud method.** The paper cites PCM (Zhang et al., 2024) as a key predecessor in the abstract, intro, related work, and method sections (lines 13, 31, 93), describing it as one of "two key works" for Mamba-based point cloud analysis. Yet none of the experimental tables include a PCM column. Since the paper's central claim is "superiority over SOTA baselines" and the core contribution is a new traversal strategy, omitting the most directly comparable Mamba baseline means the reader cannot tell whether spectral traversal adds value beyond what PCM's Consistent Traverse Serialization already achieves. This is the single most consequential gap in the evaluation.

2. **Individual contributions are not isolated in the main results tables.** The method comprises three distinct strategies (SAST, HLT, TAR), but Tables 1, 3, and 4 report only "Ours (PointMamba + SST)" — the combination of all three — against Point-Mamba. For classification (the main benchmark), HLT is not used, so the gain should come from SAST and TAR jointly. However, the paper does not report the performance of SAST alone (without TAR) or TAR alone (without SAST) on the classification benchmarks. The ablation studies (Figures 4, 5) validate eigenvector count and the TAR effect, but they do not decompose SAST vs. TAR on the actual classification tables. Similarly, for segmentation (Table 2), the text claims HLT outperforms SAST but the numerical comparison is only in the table image. Without this decomposition, the reader cannot attribute gains to specific components.

3. **The canonicalization procedure for eigenvectors is fragile and unanalyzed.** The sign-flip rule (flip if the first element is negative) and eigenvector-reordering rule (swap pairs with near-identical eigenvalues if the first element of the larger-index eigenvector is larger) are described without justification or robustness analysis (Section 3.3). The first element of an eigenvector is an arbitrary coordinate that can be zero or near-zero, making sign determination unreliable. Degenerate or near-degenerate eigenvalues are common when the point cloud has symmetries, and the proposed reordering may not converge or may produce inconsistent orderings across small perturbations. The paper does not investigate how often these ambiguities arise or whether downstream performance is sensitive to them. A method that claims isometry invariance but uses a fragile canonicalization step may not provide the invariance in practice.

### Minor

- **No limitations section.** The paper lacks a discussion of (a) the computational cost of eigen-decomposition, (b) sensitivity to the choice of \(K\) and \(\sigma\) in graph construction, (c) the assumption that the patch-adjacency graph is a good proxy for the underlying surface, and (d) failure cases such as point clouds with disconnected components or irregular sampling.

- **Missing ablation on several hyperparameters.** The paper ablated eigenvector count and nearest-neighbor count \(K\), but not the Gaussian kernel width \(\sigma\), the number of patches \(N_c\), or the number of eigenvectors \(s\) for the HLT strategy. These could significantly affect performance.

- **Code not mentioned.** Given the number of implementation details (canonicalization, eigenvalue computation, recursive partitioning, TAR), releasing code would substantially aid reproducibility and adoption.

- **The HLT threshold choice is not justified.** The paper uses the mean of each eigenvector as a binary threshold rather than the zero-crossing threshold standard in spectral clustering and normalized cuts (Section 3.4). No justification or ablation is provided for this choice.

- **Comparison to latest Transformer backbones is limited.** The paper compares to MAE-based Transformers (Point-MAE, Point-M2AE, Point-BERT) but not to the strongest general Transformer backbones cited in related work (Point Transformer v3, Stratified Transformer). While the paper's focus on MAE-based methods is defensible, the claim of "SOTA" is somewhat undercut by this omission.

- **Few-shot evaluation covers only ModelNet40 with two standard settings.** While the results look positive, the evaluation is limited to 10-way 5-shot and 5-way 10-shot on a single dataset.

### Trivial

- The HLT method sorts remaining tokens within a segment randomly to add stochasticity. This is a minor implementation detail that could be better justified or ablated.
- The paper uses mean eigenvector value as HLT threshold without noting that for symmetric Laplacians, eigenvectors are centered around zero, so the mean is typically near zero — making the difference from zero-crossing small in practice but worth clarifying.

## Nice-to-Haves

- Evaluation on large-scale segmentation benchmarks (ScanNet, S3DIS) would strengthen the claim of practical significance.
- A head-to-head comparison with PCM using the same training settings would be the single highest-leverage addition.
- Visualization of the spectral traversal order on sample point clouds, compared to the 3D-grid ordering, would provide intuitive evidence for the "surface manifold" claim.
- Stability experiments: running eigenvector computation with small perturbations (e.g., random rotations) and measuring how often the traversal order changes, plus variance in downstream accuracy.

## Removed Points

These points were flagged by reviewers but removed as invalid or not applicable:

1. **Tables as images preventing verification** — This is a parser artifact. The original paper contains properly formatted tables. Not a paper weakness.
2. **SVM for linear evaluation is "older protocol"** — Point-MAE and other papers in this line use the same SVM protocol. Standard practice, not a weakness.
3. **Computational overhead analysis in supplementary not visible** — Per policy, missing appendix content (stripped by parser) is not a paper weakness. The paper states this analysis exists in the supplementary.
4. **"TAR is essentially a positional-reinsertion trick"** — This is a reductive description rather than a weakness. The method is motivated and ablated; simplicity is not a flaw.
5. **"The paper should also test on X dataset / Y baseline" beyond reasonable scope** — Several requests for additional comparisons were scope creep. The most critical missing baseline (PCM) is kept as a major weakness above.

## Novel Insights

The reviews collectively surface a tension at the heart of this paper: the spectral traversal idea is genuinely novel and well-grounded in spectral graph theory, but the experimental validation is structured in a way that makes it impossible to separate the signal from the scaffolding. The harsh critic correctly identifies that without per-component ablation and without a PCM comparison, the paper's central causal claim ("spectral traversal is better") remains circumstantial — we see that the full method beats Point-Mamba, but not whether it's SAST, TAR, or their combination that drives the gain, nor whether a different Mamba traversal (PCM's CTS) would do equally well. The strength finder correctly identifies that the core idea is principled and supported by some ablations (eigenvector count, K, TAR). The disconnect is not between the reviewers but between the paper's ambition and its evidence structure: the contribution is a family of three techniques, but the experiments treat them as a single compound treatment.

## Suggestions

1. **Add PCM to all experimental tables.** This is the single most important addition. If the method outperforms PCM, the core claim is credible; if not, the contribution of spectral ordering per se is unclear.

2. **Provide per-component ablation on the main classification benchmarks.** Report accuracy for (i) Point-Mamba baseline, (ii) Point-Mamba + SAST alone, (iii) Point-Mamba + TAR alone, and (iv) Point-Mamba + SAST + TAR (full SST) on ModelNet40 and ScanObjectNN.

3. **For segmentation, provide a numerical comparison** of HLT vs. SAST vs. a 3D-grid traversal baseline, ideally in a separate small table if the main table is crowded.

4. **Analyze canonicalization stability.** Run eigenvector computation with small perturbations (random rotations, different point samplings) and report how often the traversal order changes. Also discuss the edge cases (first element near zero, degenerate eigenvalues).

5. **Add a limitations section** discussing computational cost, hyperparameter sensitivity, and failure cases.

6. **Release code** to support reproducibility given the many implementation details.

## Score and Decision

The paper introduces a novel and intellectually well-grounded idea — using spectral graph analysis to define traversal orders for Mamba networks on point clouds — and the three strategies (SAST, HLT, TAR) are clearly motivated. The TAR ablation in particular is cleanly demonstrated. However, the experimental validation has two significant gaps: the missing PCM comparison (the other Mamba point-cloud baseline) and the absence of per-component ablation on the main benchmarks. These gaps mean the paper's central claims are not fully supported by the evidence presented. The canonicalization robustness concern, while not fatal, also needs attention.

The paper is a promising proposal that requires major revision before its claims can be accepted at face value. The score reflects a borderline submission with genuine contributions but incomplete evidence.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
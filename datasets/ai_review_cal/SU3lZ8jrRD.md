- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 6, 3, 5
Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper targets the problem of token traversal ordering in Mamba networks for point clouds. It proposes three contributions: (1) Surface-Aware Spectral Traversing (SAST), which uses eigenvectors of the Random Walk Laplacian of the patch-connectivity graph to define an isometry-invariant traversal order; (2) Hierarchical Local Traversing (HLT), a recursive binary partitioning scheme using spectral information for segmentation; and (3) Traverse-Aware Repositioning (TAR), which restores masked learnable tokens to their original positions during MAE pretraining rather than appending them at the end. The method is evaluated on ModelNet40 classification, ShapeNetPart segmentation, few-shot learning, and ScanObjectNN.

## Strengths

- **TAR is a simple, well-motivated, and well-ablated contribution.** The problem it addresses — that Mamba's directional sensitivity makes standard MAE token placement (appending at the end) suboptimal — is clearly identified. The ablation in Figure 5 shows TAR improves pretraining SVM accuracy from 90.11% to 91.05% on ModelNet40, and the fine-tuning curves on ScanObjectNN show a consistent gap. This is the strongest single piece of evidence in the paper.

- **SAST is a principled approach to a genuine problem.** The paper correctly identifies that 3D grid-based traversal (used by Point-Mamba and PCM) is view-dependent and ignores manifold structure — patches that are adjacent on a grid may be far apart on the object surface. Using Laplacian eigenvectors to define a surface-aware traversal order is well-motivated by spectral graph theory (Section 3.1, properties 1–4), and the use of low-frequency eigenvectors (s=4) for smooth traversal is physically grounded via Courant's Nodal Line Theorem.

- **Systematic ablation of key hyperparameters.** The paper analyzes the number of eigenvectors and the K in KNN for the adjacency graph, showing clear trends (peak at s=4, K=20) with a sensible explanation for the drop-off (higher eigenvectors are less smooth). This provides practical guidance.

## Weaknesses

### Fatal
None.

### Major

1. **The claimed isometry invariance and viewpoint robustness are asserted but never experimentally validated.** The paper explicitly motivates SAST by stating that grid-based traversal is "view dependent, thus rotating the point cloud or moving the camera yields a different traversal order" (Section 3.3), and claims the spectral traversal is "robust to the viewpoint (due to isometry invariance)" (Section 3.1). However, no experiment tests this property — for example, by evaluating classification accuracy under SO(3) rotations of the test set and comparing whether SAST's accuracy degrades less than grid-based traversal, or by measuring the consistency of traversal orders under isometric transformations. The only mention of rotation in experiments is that "random rotation" is used as training augmentation for ScanObjectNN (Section 4.2), which is standard and does not validate the invariance claim. This is a central gap: a key advertised advantage is completely untested.

2. **The empirical gains over baselines are modest and not accompanied by confidence intervals or significance tests for the main results.** The improvement over Point-Mamba on ModelNet40 classification and ShapeNetPart segmentation appears to be in the range of ~0.3–0.8 percentage points based on numbers referenced from the (image-embedded) tables. For few-shot learning (Table 3), standard deviations are reported and some improvements fall within one standard deviation of baselines. For the main classification and segmentation benchmarks, no confidence intervals, standard deviations, or statistical tests are reported, so the reader cannot assess whether the differences reflect genuine improvement or random variation. Combined with claims of "superior performance over state-of-the-art baselines" and "marked improvements" (conclusion), the paper overstates its evidence.

3. **The HLT contribution for segmentation introduces considerable complexity without clearly demonstrated benefit.** The paper motivates HLT by arguing that SAST's separate traversals per eigenvector may not capture the precise relationships needed for segmentation (Section 3.4). However, the reported improvement of HLT over SAST in the pretrained setting appears small (claimed ~0.2–0.4 percentage points from the image tables). The paper does not compare HLT against a simpler baseline (e.g., using SAST with more eigenvectors, or a learned grouping) on the same segmentation task, nor does it evaluate on a more challenging segmentation dataset (e.g., S3DIS or PartNet) where spatial partitioning might be more consequential. The paper's own acknowledgment that "the trend of improvement in previous methods is minor" (Section 4.2) partially contextualizes this, but it does not justify HLT as a separate contribution given the additional complexity.

4. **The canonicalization procedure for eigenvector sign and order ambiguity has a fragility that is not discussed.** The proposed canonicalization (Section 3.3) flips eigenvector signs based on whether the *first element* is negative, and resolves eigenvalue multiplicity by comparing the first element of consecutive eigenvectors. As the harsh critic correctly notes, the "first element" depends on the indexing of patches (which is not isometry-invariant), so the canonicalized traversal is not guaranteed to be isometry-invariant. This is not necessarily fatal — the procedure may work well in practice — but the paper does not acknowledge this limitation or test whether the canonicalization yields consistent results under transformations.

### Minor

- **PCM (Zhang et al., 2024), another Mamba-based point cloud method, is discussed in the method motivation (Section 3.3) and related work but is not quantitatively compared in any experiment.** Since PCM also proposes an alternative traversal strategy (Consistent Traverse Serialization), a direct comparison would strengthen the paper.

- **No discussion of limitations.** The paper does not acknowledge any limitations — e.g., sensitivity to graph construction parameters (KNN kernel width σ, number of neighbors K), computational overhead of eigenvector computation, or the failure cases of the canonicalization heuristic. A limitations section would improve the paper's intellectual honesty.

### Trivial
None of note.

## Nice-to-Haves

- Validate the isometry invariance claim directly: compare classification accuracy under random rotations for SAST vs. grid-based traversal, and measure traversal-order consistency under isometric transformations.
- Report confidence intervals or standard deviations for the main classification (ModelNet40, ScanObjectNN) and segmentation (ShapeNetPart) results.
- Include a direct quantitative comparison with PCM on the same benchmarks.
- Evaluate HLT on a more challenging segmentation dataset to demonstrate its value.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Computational cost deferred to supplementary"** — The paper explicitly states (Section 4) that "a comprehensive analysis of the computational efficiency, runtime, and memory usage of our SAST approach is provided in the Supplementary Material." Since the parser strips supplementary material, this is not a valid weakness in the submitted review.
- **"Garbled Table 4" / "tables are garbled by the parser"** — Parser artifacts from PDF extraction are not author errors.
- **"No results on ScanObjectNN in the main body"** — This is factually incorrect; Table 4 and Section 4.2 discuss ScanObjectNN results.
- **"Missing related works" / "discussion of spectral graph analysis not contextualized in related work"** — These are presentation preferences, not substantive weaknesses. The related work section adequately covers the relevant topics.
- **Various formatting/style nitpicks** (parser artifacts) — removed.

## Novel Insights

The most interesting observation from the reviews is the tension between the spectral graph theory framing and the practical canonicalization procedure. The paper argues convincingly that the Laplacian spectrum is isometry-invariant (property 4, Section 3.1), but the sign-flipping and reordering steps needed to make the eigenvectors usable as a traversal order break that invariance because they depend on an arbitrary patch indexing. This raises a subtle but important question for spectral methods in learned representations: the theoretical guarantee applies to the spectrum as a set, but any algorithm that must produce a *deterministic ordering* from eigenvectors must break the invariance through some canonicalization. Whether this matters in practice — i.e., whether the resulting traversal is "robust enough" even if not strictly invariant — is exactly the kind of question the authors should address experimentally.

## Suggestions

1. **Add an explicit experiment testing isometry invariance/vievpoint robustness.** The simplest is: evaluate classification accuracy on ModelNet40 under random SO(3) rotations of the test set, comparing SAST against Point-Mamba's grid-based traversal. Report accuracy degradation curves. This is the single most important addition.

2. **Either provide a clearer justification for HLT or simplify the paper.** Run HLT on S3DIS or PartNet to show it matters for fine-grained segmentation, or reduce HLT to an ablation variant rather than presenting it as a co-equal contribution.

3. **Add confidence intervals to the main results (Table 1, 2, 4) and temper the language.** Replace "marked improvements" and "superior performance over state-of-the-art baselines" with more measured claims commensurate with the observed gains.

4. **Acknowledge the canonicalization limitation** and discuss whether the procedure is empirically consistent under transformations.

5. **Include PCM in the benchmark comparisons** since it is discussed as a key related Mamba-based point cloud method.

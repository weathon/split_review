- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 5, 5, 5
Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper introduces "level-set parameters" (the weights of an SDF neural network) as a novel continuous data modality for 3D shape analysis. It contributes: (1) a hypernetwork (HyperSE3-SDF) that transforms first-layer SDF parameters to reflect SE(3) poses, (2) a two-stage procedure that learns a shared prior μ to align parameter representations across shapes, and (3) encoder-based methods for classification, retrieval, and correspondence-free 6D pose estimation using only the SDF reconstruction loss. Experiments on ShapeNet and Manifold40 demonstrate that the proposed continuous representation achieves competitive semantic analysis performance under arbitrary rotations and enables pose estimation on partial observations with large rotations and noise.

## Strengths

- **Level-set parameters work as an independent data modality for semantic analysis without relying on discrete 3D data.** Table 2 reports strong classification accuracy on ShapeNet (reference pose and z/SO(3) settings), and Table 3 reports 81.1% accuracy / 72.9% mAP on Manifold40 — outperforming point-cloud baselines under the same rotation conditions. This directly supports the central claim that SDF parameters can replace discrete representations for pose-aware semantic analysis.

- **HyperSE3-SDF produces transformed level-set parameters that preserve semantic content far better than standard Euclidean transformations.** Table 1 (as summarized in the paper text) shows a large gap — e.g., HyperSE3-SDF achieving 97.8% vs. 73.1% in the reference pose — directly demonstrating the advantage of the learned, architecture-aware transformation over Eq. (4).

- **The two-stage construction with a learned shared mean μ yields level-set parameters that are well-correlated across shapes.** Figure 3 shows t-SNE embeddings where a learned μ produces clear category clusters while a random μ yields no structure. Table 1 quantitatively confirms that normalized residuals Δθ (with learned μ) outperform raw θ.

- **Registration-based pose estimation that requires no correspondences, no training data, and no global features.** Table 4 reports competitive RRE/RTE on clean partial-to-full pairs and maintains reasonable performance under noise/outliers, while ICP and FGR fail on large rotations. The method includes an ablation (V1 vs. V2) that compares the hypernetwork and Euclidean transformation variants.

## Weaknesses

### Fatal
None.

### Major

- **No fully controlled comparison with point-cloud baselines in semantic analysis.** The paper's method is trained on 200 shapes/class (ShapeNet) and 50% of shapes/class (Manifold40), while the published PointNet/DGCNN/equivariant-network results it compares against were trained on the full datasets. Although using *less* training data typically disadvantages the proposed method (making its competitive results more noteworthy, not less), the lack of a controlled experiment where baselines are retrained on the identical subsets means the reported performance gaps cannot be cleanly attributed to the representation itself. This is the most significant methodological limitation.

### Minor

- **The pose-dependent/pose-independent separation claim lacks direct validation.** The paper asserts that first-layer parameters are pose-dependent and the remaining layers are pose-independent, but the only evidence is the indirect performance comparison in Table 1. A direct experiment — e.g., fixing all non-first-layer parameters, varying only the first layer via the hypernetwork, and checking whether the SDF reconstructions for a rotated shape match those of the original shape rotated — would substantially strengthen this central claim.

- **Missing ablation on the number of shapes used to learn μ.** The paper uses 20 shapes/class (ShapeNet) and 7 shapes/class (Manifold40) for the first stage, with no sensitivity analysis. The choice is motivated as a trade-off between prior work, but downstream results may depend on this hyperparameter.

- **No architecture ablation for the semantic encoder.** The encoder design (BaseNet, BasePool, tensor reshaping, transformer head) is described without alternatives or rationale. A minimal ablation (e.g., removing one branch, varying pooling strategy) would demonstrate that the design choices matter.

- **Retrieval results only reported on Manifold40, not ShapeNet.** The paper claims retrieval capability but only provides retrieval metrics (mAP, top-k recall) on the smaller Manifold40 dataset. ShapeNet results would strengthen the generality claim.

- **Pose estimation lacks sensitivity analysis for hyperparameters T, S, N, M.** These control the initialization grid density and optimization rounds but are not ablated. Runtime (~50s) is reported without comparison to baseline runtimes, making it hard to assess the practical trade-off.

- **No error bars or statistical significance for classification/retrieval.** Given the variability of training on subsets and the filtering step (Chamfer distance threshold), standard deviations across multiple runs would increase confidence.

### Trivial

- The unstructured surface reconstruction loss line (line 151) contains garbled text — a PDF parsing artifact that was presumably not present in the original submission.

## Nice-to-Haves

- Retraining point-cloud baselines (PointNet, DGCNN, an equivariant network) on the same 200-shapes/class subsets would provide a fully controlled semantic-analysis comparison. This would isolate the contribution of the representation from the data regime.
- Adding an SDF-based pose estimation baseline (e.g., optimizing R,t using the plain SDF loss without the hypernetwork but with a better initialization strategy) would help isolate the hypernetwork's contribution in registration.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Unfair comparison in pose estimation because method has SDF access while baselines only have point clouds."** — This is inherent to comparing across representations. The paper's claim is that level-set parameters (a new modality) enable better pose estimation than point-cloud-based methods. The comparison with V2 (Euclidean transformation) is SDF-vs-SDF. The baselines (ICP, FGR, TEASER++) have access to the full reference point cloud, which is also a strong prior. The reviewer's request for an SDF-based baseline is fair and moved to Nice-to-Haves, but the "unfair" framing is overstated.

2. **"If a method fails in simpler settings, we cease testing."** — This is standard practice in registration papers; testing a method on harder data after it already failed on easier data produces meaningless numbers.

3. **"The paper's claim of novelty is overstated given prior works (Luigi et al., 2023; Erkoç et al., 2023)."** — The paper explicitly cites these works, discusses their different SDF architectures and limitations (periodic activations causing artifacts, small networks limiting quality), and clearly states how it differs. This is a proper related-work positioning, not an overclaim.

4. **"Notation hard to follow / diagram reference parsed from PDF."** — These are PDF-parser artifacts. The original submission has proper figures and diagrams.

5. **Formatting/style nitpicks and missing related work suggestions.** — Removed per instructions.

6. **"The t-SNE visualization is qualitative."** — The visual evidence is accompanied by Table 1's quantitative classification results, so this criticism lacks force.

7. **"The comparison does not specify whether DGCNN was trained with random rotations."** — The paper's rotation setup is clearly defined (z/SO(3) protocol following Esteves et al., 2018). This speculation does not constitute a verified weakness.

8. **"Strawman strength" from Strength Finder.** — After verification, the listed strengths (level-set parameters as viable modality, hypernetwork superiority, learned μ benefits, correspondence-free pose estimation) are all supported by specific evidence in the paper. No strengths were removed as invalid.

## Novel Insights

None beyond the paper's own contributions. The key innovation — treating SDF parameters as a data modality rather than just a reconstruction tool, and using a hypernetwork to handle pose variation in parameter space — is well articulated by the paper itself.

## Suggestions

1. **Controlled semantic comparison:** Retrain PointNet, DGCNN, and one equivariant network on the exact 200-shapes/class subsets used by the proposed method. Report all methods with standard deviations over 3-5 runs. This single experiment would address the most significant weakness.

2. **Direct pose-parameter separation validation:** For a set of test shapes, (a) rotate the shape, (b) only update the first-layer parameters via the hypernetwork while freezing all other layers, (c) compare SDF reconstruction fidelity against the ground-truth rotated SDF. If errors are comparable, the separation claim is directly validated.

3. **Ablate the μ-training set size** (e.g., 5, 10, 20, 50 shapes/class) to show the sensitivity of downstream classification accuracy to this hyperparameter.

4. **Report retrieval results on ShapeNet** to match the claim of "shape retrieval" made in the abstract and contributions.

5. **Sensitivity analysis for pose estimation parameters** T (grid density), S (candidates), and optimization iterations, along with runtimes for all baselines.

Now I have all the information I need. Let me write the consolidated review.

## Summary

The paper introduces a parent-child tree representation for 3D Gaussian Splatting where only a sparse set of "parent" points are stored, and "children" points and their attributes are predicted on-the-fly during rendering using a shared hash-grid, tiny MLPs, and a self-attention mechanism. An adaptive tree manipulation (ATM) strategy promotes important children to parents and prunes unnecessary trees. The method achieves 10–20× storage reduction over 3DGS while maintaining or improving rendering quality on three standard benchmarks.

## Strengths

- **Dramatic storage reduction with maintained/improved quality**: The method consistently achieves 10–20× storage reduction over 3DGS across Mip-NeRF 360, Tanks&Temples, and Deep Blending, while improving or matching PSNR. On Mip-NeRF 360, C3 uses only 27 MB (vs. 525 MB for 3DGS) at 27.01 PSNR vs. 26.90. This is the paper's core contribution and is well-supported by quantitative results (Tab. 1, Fig. 3).

- **Novel and well-motivated parent-child representation**: Storing only position and scale of parent points and predicting everything else via a hash grid and tiny MLPs is a clever and principled approach to exploiting spatial redundancy. The use of a depth‑1 tree (≤2 children) keeps prediction complexity low while enabling densification through promotion.

- **Thorough ablation study**: The paper ablates the hash grid (vs. frequency encoding), the self-attention mechanism, the adaptive tree manipulation, scene contraction, and MLP input features (position, distance, SH degree). Each component is shown to contribute positively with quantified PSNR differences (Tabs. 2–4). The attention ablation also shows it reduces the number of parent points (884K vs. 1.06M), improving storage efficiency.

- **Consistent results across three datasets and multiple configurations**: Three hash-grid dimension configurations (C1–C3) are evaluated, showing a clear quality–storage trade-off. The method generalizes across indoor, outdoor, and large-scale urban scenes.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Missing rendering speed evidence for the "negligible overhead" claim**: The paper states that the prediction MLPs add "negligible overhead" (line 46) but provides no FPS, runtime, or latency measurements — neither on GPU nor on the iPhone 14 used for on-device tests. While the paper's primary contribution is storage reduction, this unsupported speed claim weakens the overall presentation. The authors should report FPS for their method and comparable approaches on the same hardware.

- **On-device demonstration lacks quantitative detail**: The on-device section (line 183) reports that 3DGS and ScaffoldGS run out of memory on iPhone 14 while the proposed method "can successfully run on device" with "better rendering quality" than LightGS and CompactGS — but provides no FPS, peak memory usage, or on-device PSNR numbers. Given the paper's emphasis on mobile deployment, these numbers would significantly strengthen the practical contribution.

- **No comparison against a simple interpolation baseline**: The paper does not compare against a trivial baseline where the trained 3DGS point cloud is subsampled to the same number of stored parents and missing points/attributes are reconstructed via nearest-neighbor or bilinear interpolation from the stored set. Such a baseline would directly test whether the learned predictor (hash grid + attention + MLPs) adds value beyond spatial locality — a basic sanity check that the current ablations (which compare learned alternatives) do not fully address.

- **ATM deletion rule may miss important children**: The paper deletes trees based only on parent statistics, justified by "if a child node was important then it would have been already promoted" (line 125). However, children may have low gradients simply because the parent's neighborhood already represents the region adequately, not because the child itself is unimportant. The ablation (Tab. 4) shows ATM helps, but the baseline deletes based on parent stats only — it does not include a version that also tracks children for deletion. This leaves a theoretical gap in the pruning strategy.

- **No statistical variance reported**: The paper reports single-point averages across scenes without error bars or multiple-seed runs. This is standard practice in the current 3DGS literature (original 3DGS, ScaffoldGS, LightGS, CompactGS all follow the same convention), so it does not invalidate the results. However, given the remarkable claim of simultaneously improving PSNR while drastically reducing storage, a small number of repeated runs would help rule out lucky initializations and increase confidence.

### Trivial

- The ablation for removing self-attention ("w/o Attn") does not specify how features are aggregated in its absence — averaging, summation, or another mechanism. This should be clarified.
- The dual use of the hash grid for both displacement features and attribute features is not ablated. A version that queries the hash grid only at parent positions (skipping the second query at child positions) would test whether the locality of the hash grid is needed at both stages.
- In the FE ablation (hash grid replaced by frequency encoding), the MLP capacity is not explicitly matched in terms of parameter count, though the feature dimension is matched.

## Nice-to-Haves

- Compare against a ScaffoldGS-style anchor-point baseline with matched storage budget, as both methods use a prediction network from sparse anchors/parents.
- Provide a per-component storage breakdown (parent positions, parent scales, hash grid entries, MLP weights) to clarify where the savings come from.
- Visualize the distribution of parent-to-child displacements to validate the assumption that children are consistently near parents.

## Removed Points

- **Criticism about rendering speed being central to "lightweight" in the title**: The paper's use of "lightweight" is explicitly scoped to storage reduction ("a lightweight Gaussian Splat representation, with storage significantly reduced" — line 38). The rendering speed claim is secondary and the missing evidence is already captured in the Minor weaknesses.
- **Criticism about missing warm-up ablation**: The paper states the warm-up is detailed in the supplementary material (line 137). The parser strips supplementary content; this is not a paper flaw.
- **Criticism about per-scene results not being in the main text**: The paper states "Per-scene quantitative results are in the Supplementary material" (line 155), which is standard practice. The main text reports averaged metrics.
- **Criticism about the teaser claim being "not qualified"**: The teaser figure is an informal illustration; the formal results are provided in Tab. 1. This is a presentational choice, not a flaw.
- **Criticism about the FE ablation capacity mismatch**: The hash grid and frequency encoding are different architectural families; exact parameter matching is not standard for this type of ablation. The paper matches feature dimension, which is a reasonable comparison.

## Novel Insights

The reviews surface an interesting tension in the paper's evaluation strategy: the method's core strength — storage reduction — is convincingly demonstrated with thorough quantitative evidence, yet the secondary claims about rendering efficiency and mobile deployability rest on much weaker qualitative statements. This asymmetry is common in compression papers that prioritize storage metrics, but it leaves the paper in an awkward position where the full title's promise ("Lightweight...") is only partially supported. A second observation is that the ATM mechanism, while clearly helpful, may have a blind spot: by relying solely on parent statistics for deletion, it implicitly assumes that the promotion threshold and the deletion threshold are perfectly coordinated, which may not hold during early training when gradients are noisy. This design trade-off is worth exploring in future work.

## Suggestions

1. **Add rendering speed benchmarks** — report FPS on a standard GPU (e.g., RTX 3090) for all compared methods, plus FPS and peak memory on the iPhone 14. Even a single-row table would substantiate the "negligible overhead" claim.
2. **Add a simple interpolation baseline** — subsample the trained 3DGS point cloud to the same parent count and reconstruct via k-NN interpolation. This directly validates whether the learned prediction justifies its complexity.
3. **Report variance** — even 2–3 runs with different random seeds would significantly strengthen confidence in the headline results.
4. **Clarify the "w/o Attn" baseline** — specify the feature aggregation method used when attention is removed.

## Score and Decision

The paper presents a novel and well-executed method for reducing the storage footprint of 3D Gaussian Splatting. The core contribution — a parent-child tree with learned prediction — is clearly motivated, carefully designed, and convincingly validated on three standard benchmarks. The weaknesses are addressable and do not undermine the paper's primary claims. I recommend acceptance with minor revisions.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
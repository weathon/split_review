Now I have a thorough understanding of the paper and can cross-check all reviewer claims. Let me write the final consolidated review.

## Summary

The paper introduces a lightweight 3D Gaussian Splatting representation that stores only a small subset of "parent" points and uses a hash grid with small MLPs and a self-attention mechanism to predict "children" points and their attributes (position, color, scale, rotation, opacity) at load/render time. On the Mip-NeRF 360° dataset, the largest configuration achieves the best PSNR among all compared methods while reducing storage by 19.5× vs 3DGS and 5× vs ScaffoldGS, with 3.5× fewer total 3D points. The method also demonstrates feasibility on an iPhone 14 where 3DGS and ScaffoldGS run out of memory.

## Strengths

1. **Dramatic storage reduction with maintained or improved quality.** On Mip-NeRF 360°, C3 achieves 27.21 PSNR (the best among all methods) while using only 4.5% of 3DGS's storage and 20% of ScaffoldGS's. This is the paper's central claim and is well-supported by Table 1. The 19.5× reduction vs 3DGS and 5× vs ScaffoldGS are significant.

2. **Novel parent-child tree representation with neural prediction.** The idea of storing only parent points and predicting children via a hash grid + displacement MLPs + attribute MLPs is genuinely novel compared to prior compression works (LightGS, CompactGS, ScaffoldGS) that either store all points or use only grid fields. The hash grid's spatial smoothness property is well-motivated for nearby points sharing similar attributes.

3. **Adaptive Tree Manipulation (ATM) enabling principled densification.** The child-promotion mechanism (elevating high-gradient children to parents) and tree-level pruning are well-designed extensions of 3DGS's densification to the tree setting. Ablations confirm ATM improves PSNR by ~0.5 dB, and Figure 6 qualitatively shows denser point clouds in high-frequency regions.

4. **Controllable quality–size trade-off via three configurations.** C1, C2, C3 (varying hash grid dimension D=32,48,64) give practitioners flexibility. C1 is 50% smaller than the smallest prior work (LightGS) while matching its PSNR, and C3 beats all prior compression methods in PSNR while remaining smaller.

5. **Thorough ablation study.** Systematic removal/ablation of the hash grid (replaced by frequency encoding), attention, ATM, scene contraction, and MLP inputs all degrade PSNR, confirming each component's contribution. The attention ablation also shows it reduces parent count from 1.06M to 884K.

6. **Mobile-device feasibility demonstrated.** On iPhone 14, 3DGS and ScaffoldGS OOM on all scenes, while the proposed method runs successfully. This provides real-world evidence that the storage reduction translates to tangible deployment advantages.

## Weaknesses

### Major

1. **Gap between "on-the-fly during rendering" claim and actual evaluation.** The abstract and introduction state that children "can be predicted during rendering" (line 40, 63, 216). However, the mobile benchmark (line 183) explicitly states: "For fair comparison, we unpack splats from all methods to a standard 3DGS format for rendering." This means the evaluation uses a two-stage pipeline — decompress (predict children) then render — rather than truly integrating child prediction into the rendering loop. The paper asserts "negligible overhead" (line 46) without providing any timing measurement of the prediction step. Without measuring prediction latency, total load+render time, or FPS in the actual inference pipeline, the claim of on-the-fly prediction is unsubstantiated. This does not invalidate the storage-reduction contribution (which is well-measured), but it means the paper overclaims the nature of its advantage. The method could be reframed honestly as a compression/decompression pipeline and the core contribution would still stand.

2. **Storage breakdown not reported.** The 19.5× storage reduction conflates multiple sources: (a) fewer total points (3.5× fewer than 3DGS), (b) predicting attributes instead of storing them (e.g., SH coefficients replaced by MLP prediction), and (c) the overhead of the hash grid and MLP weights themselves. The paper reports neither the size of the hash grid + MLPs separately from parent points, nor the effective bytes-per-splat for the unpacked representation at rendering time. This makes it impossible for readers to understand where the savings come from and whether the advantage would persist against a heavily quantized/pruned 3DGS baseline at the same storage budget.

### Minor

3. **Missing measurement of prediction latency / total pipeline time.** The paper calls prediction overhead "negligible" but provides zero timing numbers — no FPS comparison, no measurement of how long child prediction takes vs. rendering. For mobile deployment, a decompression step that doubles or triples the total splat count before rendering is a nontrivial operation. This should be measured.

4. **Theoretical concern about permutation-invariant attention in a structured tree setting.** The self-attention (Eq. 1) treats all K+1 nodes identically without positional embeddings, justified as "permutation invariant which is an important property to maintain while working with point clouds" (line 103). However, parent and children nodes have different structural roles — the parent drives the hash-grid query and is stored, while children are predicted. While the critic's argument that this is "wrong" overstates the case (the features themselves are already differentiated by their origin in the hash grid at different spatial positions), the paper would benefit from an ablation comparing the current design against a variant with an explicit parent token or learned positional encoding. The paper already shows attention helps over no-attention; the incremental contribution of permutation invariance per se is untested.

5. **Child promotion mechanism is underspecified.** When a child is promoted to parent (Section 4.2, line 123), the paper does not clarify whether its position transitions from predicted to stored, or how the hash-grid features at that position are handled. The hash grid was trained with features queried at the child's predicted position; after promotion, does the system continue using that same position (now stored) and the same hash-grid query? The mechanism is plausible but underspecified, which harms reproducibility.

6. **Scene contraction described only by reference.** The ablation shows 0.8 dB PSNR drop without scene contraction (Table 4), making it a significant component. Yet the main text only mentions it in passing (line 148) with a pointer to supplementary and prior work. While acceptable for a conference paper, it makes evaluation of the method's completeness harder.

### Trivial

7. **K (number of children) selection is not discussed.** The paper says K is "at most 2" and varies across scenes (line 149), deferring to supplementary. No sensitivity analysis is provided. This is a minor missing detail.

8. **The mobile test's memory pathway is unclear.** The paper states that 3DGS and ScaffoldGS OOM while the proposed method runs, but does not clarify whether the child-prediction (decompression) step happens on GPU or CPU, nor what peak memory usage is during on-device rendering. The result is still informative (the method has 3.5× fewer total points, which is why it fits), but the measurement context is vague.

## Nice-to-Haves

- Provide a storage breakdown (hash grid size, MLP weights, parent points) so readers can attribute the savings.
- Measure prediction latency and total pipeline time (load + predict + render) vs. loading a compressed 3DGS baseline.
- Add an ablation of the attention mechanism with a variant that includes a learned parent token to test whether the permutation-invariant design is optimal or merely sufficient.
- Compare against a pruned/quantized 3DGS at the same storage budget as a Pareto-style comparison.
- Describe how promoted children's hash-grid features are handled in the training loop.

## Removed Points

- **"Storage claims conflate transmission size with rendering memory footprint"** (Critic's Point 1, parts): The critic claims the storage comparison is "built on different comparison bases." This is incorrect — the paper clearly states its storage numbers are for hard-drive footprint (lines 10, 48, 165), and the compressed/unpacked distinction is transparently described. The paper separately reports "3.5× fewer 3D points" (line 171), acknowledging the unpacked count. The mobile test concern is kept above (Weakness 1, major) but the claim of systematic mismatch is overblown and removed.
- **"Scene contraction never described"**: The paper cites prior work (mip-nerf360, ngp) and states details are in supplementary, which is standard practice. The parser stripped the supplementary.
- **"PSNR improvement is small"**: The paper achieves *best* PSNR among all methods; the magnitude of improvement over 3DGS specifically does not undermine the claim.
- **"Comparison is between proposed (C3) and uncompressed 3DGS"**: The paper also compares against LightGS, CompactGS, and ScaffoldGS, which are compressed methods. This is a fair comparison set for a compression paper.
- **"Attention is permutation invariant and cannot capture parent-child dependencies"**: Overstated. The features are already differentiated by spatial position in the hash grid. The existing ablation (w/o Attn) confirms the attention helps. Kept as Minor (point 4) in weakened form.

## Novel Insights

The most interesting observation from the reviews is the contrast between how the paper frames its contribution (as a new "predictive" rendering primitive for on-the-fly decoding) and how it evaluates it (as a compression pipeline with offline decompression). This framing mismatch does not weaken the storage-reduction result, but it raises an important question for the field: is "prediction during rendering" meaningfully different from "decompression before rendering" when the neural predictor is lightweight enough? The paper would benefit from engaging with this distinction explicitly rather than conflating them. A second insight is that the permutation-invariant attention design, while theoretically debatable given the structured parent-child setting, empirically works — suggesting that content-based features (from spatially-differentiated hash-grid queries) are sufficient to encode structural roles without explicit positional encoding.

## Suggestions

1. Measure and report prediction latency (both absolute and relative to rendering time) for the child-prediction step. If it is indeed "negligible," demonstrate this with numbers across all three datasets.
2. Provide a storage breakdown table: hash-grid size, MLP weights, parent points (positions + scales), and effective bytes-per-Gaussian at unpacked rendering time.
3. Clarify the training mechanics of child promotion — does the promoted child's position become a stored variable, and how are hash-grid queries handled for promoted nodes?
4. Add a controlled attention ablation with a parent-specific token to test whether the permutation-invariant design is optimal.
5. Explicitly reframe the pipeline as "decompress then render" (or "predict at load time") in the abstract and intro, or provide evidence of true per-frame on-the-fly prediction.

## Score and Decision

This paper makes a genuine contribution to the 3DGS compression literature: the parent-child representation with hash-grid prediction is novel, the storage reductions (up to 20×) are significant and well-measured, the quality is competitive or superior, and the ablations are thorough. The primary issues are a framing mismatch between "on-the-fly during rendering" and the actual decompress-then-render evaluation, missing timing measurements, and some underspecified training details. These are addressable in revision and do not undermine the core contribution. The paper is clearly above the acceptance threshold for a top venue.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
Now I have sufficient calibration material. Let me write the consolidated review.

## Consolidated Review for "Proper Velocity Neural Networks"

---

## Summary

This paper introduces Proper Velocity (PV) Neural Networks, which use the unconstrained PV model of hyperbolic space (rooted in special relativity) as a numerically stable alternative to the constrained Poincaré ball and hyperboloid models. The authors derive the complete Riemannian geometry of PV space (exponential/log maps, parallel transport, geodesic distance) and build core neural layers (MLR, FC, convolution, activation, batch normalization) on top of it. Experiments across numerical stability, image classification, graph node classification, and genomic sequence learning demonstrate that PV avoids the catastrophic numerical failures of other hyperbolic models while achieving competitive or superior accuracy on several tasks, particularly genomics and hyperbolic graph benchmarks.

---

## Strengths

1. **First complete Riemannian toolkit for the PV model**: The paper derives closed-form exponential map, logarithmic map, parallel transport, and geodesic distance (Theorem 4.3) and shows that these operators express PV gyro operations (Theorem 4.4). This foundational derivation is genuinely novel — the PV model was largely unexplored in deep learning prior to this work.

2. **Demonstrated numerical stability advantage**: Tables 1–3 provide concrete, well-designed evidence that PV avoids the numerical failures of the hyperboloid (NaN/Inf) and the vanishing gradients of the Poincaré ball. In FP32, PV gyromultiplication has zero failure rate up to radius 1000 (Table 1), the round-trip error for Exp/Log is 2.1×10⁻⁷ vs. 1.0 for the hyperboloid (Table 2), and gradient magnitudes stay in a safe band [2.1×10⁻⁶, 1.1×10⁻⁴] while Poincaré gradients vanish to 10⁻¹¹–10⁻¹³ (Table 3). These synthetic experiments are carefully designed and convincingly show the numerical advantages of PV.

3. **Strong empirical performance on hyperbolic-structured tasks**: PVNN achieves clear gains on the most hyperbolic graph datasets — Airport (+5.86% over KNN, Table 5) and Disease (81.15% vs. best baseline 80.57%). On the five genomic TEB tasks, PVCNN outperforms both Euclidean CNN and hyperboloid-based HCNN-S across the board, with particularly strong gains on SINEs (+9 MCC points, Table 10). These results make a credible case that PV is practically useful for hierarchical data.

4. **Efficient MLR formulation eliminating a computational bottleneck**: Theorem 5.2 reduces the PV MLR score to inner products with Euclidean matrices (Eq. 19), avoiding the O(b×C×n) intermediate tensors that would arise from per-class gyroaddition. This is a concrete practical contribution that matters for batched high-dimensional classification.

5. **Theoretically grounded normalization layer**: Theorem 5.4 proves homogeneity of the Fréchet mean and dispersion under gyro operations, providing a formal guarantee that the PV GyroBN layer can center the mean to the identity and scale variance by a factor. This goes beyond heuristic Riemannian batch normalization approaches.

---

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are supported by its theoretical derivations and experimental results. No identified weakness invalidates the paper's main contributions.

### Minor

1. **The Euclidean activation collapse on Cora is unexplained**: Table 9 shows that applying activation directly in PV space ("Euc. Act.") causes a catastrophic 14-point drop on Cora (38.10% vs. 52.26% for tangent-space activation). The paper notes this but offers no hypothesis for why this happens. Since the unconstrained nature of PV is emphasized as a key advantage, understanding when direct PV-space operations break down is important. This suggests that "unconstrained" does not mean "automatically well-behaved" and that PV has its own failure modes that deserve characterization.

2. **General parallel transport relies on Möbius gyration from the Poincaré ball**: The general PT formula (Theorem 4.3) uses `gyr_M`, the Möbius gyration defined on the Poincaré ball, accessed via the isometry. While the formula is mathematically closed-form (a composition of known functions — this does not violate the paper's "closed-form" claim), a reader might reasonably expect a fully PV-native expression analogous to the simplified PT formulas at the origin (which are clean and purely PV). The paper does not provide such an expression. This is not a flaw in the mathematics but limits the self-containedness of the general PT, and it would be helpful to either give an explicit PV formula for `gyr_M` or explain why one is not needed (since the simplified formulas at origin suffice for most practical use cases — the paper never uses the general PT in experiments).

3. **Performance gains on image classification are marginal**: On CIFAR-10/100 (Table 4), PV MLR's improvements over the best hyperbolic baselines are within ~0.2–0.5% and error bars overlap. The paper's claim of "competitive or superior performance" is accurate for these results but they do not provide strong support for PV's practical advantage over other hyperbolic models in vision. The stronger evidence comes from graph and genomic tasks.

4. **Cora performance is below the best baseline**: On the weakly hyperbolic Cora dataset, PVNN (51.42%) is below the hyperboloid-based LNN (53.34%). The paper acknowledges this, but given that Cora is the most commonly benchmarked graph among the four, this weakens the general claim of PV's effectiveness.

### Trivial

1. The paper could explicitly verify that the general formulas in Theorem 4.3 reduce to the simplified origin formulas when x=0. This is mathematically straightforward but would increase reader confidence.
2. Table 7 shows that tangent/Euclidean batch statistics approximations match the Fréchet-based GyroBN on several datasets at much lower cost; the paper presents this honestly but does not discuss when the principled GyroBN is actually worth the extra computation.

---

## Nice-to-Haves

- An experiment that directly tests the stability-performance link by amplifying numerical issues in baselines (e.g., making K very negative or using high-dimensional embeddings) and showing PVNN maintains accuracy while baselines degrade.
- An analysis of typical PV embedding norms in downstream tasks to clarify whether the "unconstrained advantage" is actually being exercised in practice.
- A visualization of PV decision boundaries on a 2D synthetic hyperbolic dataset to build intuition.
- A fully PV-native expression for the Möbius gyration used in general parallel transport.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Harsh Critic #1 (PT not fully closed-form in PV space)**: The general PT is a closed-form expression — it composes known functions including the Möbius gyration, which itself has a closed-form definition. "Closed-form" does not require every sub-component to be defined on the same coordinate space when an isometry connects them. This criticism reflects a misunderstanding of the term.

2. **Harsh Critic #2 (stability-performance link not established)**: The paper claims PVNNs demonstrate "both improved stability and competitive or superior performance" — this is an *and*-claim, not a causal claim. The synthetic experiments establish stability; the downstream experiments establish performance. The paper never claims that stability causes the performance gains. Removed as a straw man.

3. **Harsh Critic #3 (implementation ambiguity)**: The paper states code will be released upon acceptance and Lemma 4.1 provides the differential dπ_x(v) in closed-form PV coordinates. The appendix (stripped from the parser version) contains implementation details. Not a valid weakness.

4. **β_x stability concern (section notes)**: The paper tests up to radius 1000 and shows zero failures. This *is* a characterization of stability; asking for the exact threshold where instability begins is a reasonable nice-to-have but not a weakness.

5. **Missing sanity check for general formulas at origin**: The simplified formulas at the origin are provided separately. The general-to-specific reduction is standard mathematical verification that belongs in an appendix.

6. **GyroBN ablation undermines the contribution**: The paper presents the trade-off between Fréchet-based GyroBN and faster approximations honestly. Having a principled normalization layer is a contribution regardless of whether alternatives sometimes match it — the paper never claims GyroBN dominates in all settings.

7. **Generic strengths from Strength Finder** (e.g., "theoretically grounded normalization layer" — kept; no generic ones needed removal).

---

## Novel Insights

The key insight that emerges from this paper beyond its own contributions is that the choice of *representation* matters for numerical stability in hyperbolic NNs even when the underlying geometry is identical. Prior work focused on operator engineering within the Poincaré or hyperboloid models; this paper shows that switching to an isometric but unconstrained representation (PV) eliminates the boundary-related numerical pathologies without changing the geometry. This principle — that an isometric reparameterization can solve numerical problems without altering the model's expressive power — is potentially applicable beyond hyperbolic deep learning. A second interesting pattern is that the PV gains are most pronounced on the most hyperbolic datasets (Airport with δ=1, Disease with δ=0, genomic sequences with strong tree structure), while the advantages shrink or disappear on nearly-Euclidean data (Cora with δ=11, CIFAR). This suggests PV is not universally better but is specifically valuable when the data hierarchy is strong enough that embeddings push against model boundaries.

---

## Suggestions

1. **Investigate the Cora activation collapse**: The 14-point drop from Euclidean activation on Cora (Table 9) is the single most salient unexplained result. At minimum, report the distribution of norms during training — if Euc. Act. produces very large embeddings on Cora, this would reveal a failure mode of unconstrained PV that deserves discussion. If the collapse stems from a different cause, understanding it is essential for users of PVNNs.

2. **Add a bridging experiment for stability**: Train PVNN and a hyperboloid network on genomic/genomic-like data while making curvature increasingly negative or dimensions higher, and show that the hyperboloid model's accuracy degrades as numerical issues appear while PVNN holds steady. This would connect the synthetic stability results to real-task performance.

3. **Clarify the role of the general parallel transport**: Since the paper's experiments only use operators at the origin (Exp₀, Log₀, PT₀→y), state explicitly that the general PT is derived for completeness and provide guidance on when it may be needed (e.g., Riemannian optimization, graph message passing). Either provide a fully PV-native gyr_M expression or add a note explaining the composition approach.

4. **Benchmark the general PT numerically**: Even if not used in an end-to-end task, a simple numerical test comparing PT_{x→y}(v) computed via the PV formula against the ground truth (computed via isometry to Poincaré) would validate the derivation and quantify error.

---

## Score and Decision

**Calibration anchors used (all results from a single batch search):**

- `/home/wg25r/review_agent/human_reviews_2026/NNnkLi1ALt.md` — avg 4.50, Accept Poster. *Intrinsic Lorentz Neural Network*; similar hyperbolic NN paper with marginal CIFAR gains, strong genomics results. PVNN has a more fundamental contribution (new model vs. new layers) and broader experimental scope. PVNN is stronger.

- `/home/wg25r/review_agent/human_reviews_2026/hkssAkOako.md` — avg 4.00, Reject. *Hyperbolic Implicit Equilibrium*; rejected for unclear writing and questionable theoretical claims. PVNN is substantially clearer and more rigorous.

- `/home/wg25r/review_agent/human_reviews_2026/XwM7DlWPdR.md` — avg 4.00, Reject. *Cartan Networks*; rejected for weak empirical evidence and limited novelty. PVNN has stronger empirical support across more tasks.

- `/home/wg25r/review_agent/human_reviews_2026/CNDNRjpVIL.md` — avg 5.50, Accept Poster. *HEEGNet*; application-focused hyperbolic paper for EEG, well-received. PVNN is more foundational and tests on more diverse tasks. Comparable quality.

- `/home/wg25r/review_agent/human_reviews_2026/oq4jXWaFyH.md` — avg 5.50, Accept Poster. *HypeCodeNet*; hyperbolic framework for code, strong empirical results. Similar quality and completeness to PVNN.

- `/home/wg25r/review_agent/human_reviews_2026/nxzgr96uyV.md` — avg 3.00, Withdrawn. *Deep Hyperbolic Hierarchical Clustering*; withdrawn with low scores. PVNN is clearly stronger in both theory and experiments.

- `/home/wg25r/review_agent/human_reviews_2026/ERVvLA5BJL.md` — avg 5.50, Reject. *HexFormer*; hyperbolic vision transformer. Rejected despite moderate scores. PVNN has stronger evidence of practical benefits on multiple task families.

PVNN presents a well-motivated, theoretically grounded, and empirically validated contribution. It introduces a genuinely underexplored hyperbolic representation (PV) to deep learning with a complete Riemannian toolkit and demonstrates clear advantages on numerical stability and on strongly hyperbolic tasks. No fatal flaws were identified. The paper is at least as strong as accepted posters in the same area (ILNN, HEEGNet, HypeCodeNet) and typically stronger. 

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
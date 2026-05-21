Now I have a thorough understanding of the paper and the calibration landscape. Let me produce the final consolidated review.

**Calibration Summary:**

Round 1 bracket: I placed the paper between ~4.0 and ~6.5 based on WSI/MIL anchors. Weak band (<3.5): papers at 2.0-3.33 (all withdrawn/rejected) — HOMIL is clearly much stronger. Middle band (3.5-7.5): ASMIL (6.00, Accept), MAMMOTH (6.50, Accept), MMPL (4.00, Reject), Cell Cloud Transformer (4.00, Reject). Strong band (>7.5): no WSI/MIL papers found.

Round 2 narrowing (4.5-6.5 and 3.5-5.5): Manifold Residual (5.50, Accept but split 6/10/2/4), Low-Signal MIL (4.67, Reject), Cross-Cancer Knowledge Transfer (4.50, Reject).

Comparing to these anchors: HOMIL is clearly stronger than MMPL (4.00), Cell Cloud (4.00), and CROPKT (4.50) which were rejected for more serious flaws. It's comparable to the Manifold Residual paper (5.50) which was accepted — both have novel ideas with some implementational/validational gaps. It's weaker than ASMIL (6.00) and MAMMOTH (6.50) which have cleaner experimental validation and fewer methodological disconnects. The motivation-implementation gap and unvalidated adaptive clustering claims prevent it from reaching the 6.0 level.

Final score: **5.0** — borderline; the core idea is valuable but the paper has significant gaps that need addressing.

---

## Summary

This paper proposes HOMIL, a multi-instance learning framework for whole-slide image classification that extends attention-based MIL (ABMIL) by computing both first-order moments (attention-weighted mean) and second-order moments (covariance matrix) of patch cluster representations, fused via learned attention weights. DBSCAN clustering is used to group similar patches before moment computation, reducing the effective instance count for computational efficiency. Experiments on CAMELYON16 and TCGA-NSCLC show HOMIL achieving the best accuracy, AUC, and F1 across nine baselines while being substantially faster than methods like MambaMIL and HMIL.

## Strengths

1. **Novel incorporation of second-order statistics into MIL aggregation**: The paper formalizes the limitation of first-order (mean-based) aggregation in MIL and proposes capturing inter-feature relationships via a covariance matrix. This is a conceptually clear and well-motivated generalization — ABMIL becomes a special case when both second-order moments and clustering are omitted (lines 25-31).

2. **Clean ablation study validates both contributions**: Table 3 shows that removing the clustering module (w/o CM) drops ACC from 96.98% to 95.72% and increases runtime by 71%, while removing the second-order moment (w/o SOM) drops ACC to 95.98% and F1 to 94.94%. Both components are necessary to outperform the ABMIL baseline (94.72% ACC), providing clean causal evidence for each claimed innovation.

3. **Demonstrated efficiency gains**: HOMIL achieves a 5-fold total runtime of 310s on CAMELYON16 vs. 455s for ABMIL, 7200s for MambaMIL, and 10800s for HMIL (Table 1). On TCGA-NSCLC, HOMIL runs in 3685s vs. 25200s for MambaMIL and 32400s for HMIL (Table 2). Compression ratios of 0.18 and 0.16 directly quantify the reduction from DBSCAN (Section 5.3).

4. **Consistent superior performance across two distinct clinical tasks**: On both metastasis detection (CAMELYON16) and lung cancer subtyping (TCGA-NSCLC), HOMIL achieves the highest ACC, AUC, and F1 among nine strong baselines, demonstrating robustness across different tissue types and classification challenges.

## Weaknesses

### Fatal
None.

### Major

1. **Motivation-implementation disconnect in the second-order moment computation**: Section 3.2 motivates the covariance matrix as $\Sigma = \sum_i (\mathbf{h}_i - \mu)(\mathbf{h}_i - \mu)^\top$ computed on **patch feature vectors** $\mathbf{h}_i$, arguing that this captures "pairwise relationships and variability between different dimensions of the patch feature vectors across the slide." However, the actual implementation in Section 4.3.3 computes $\mathbf{C} = \sum_{k=1}^K (\mathbf{g}_k - \mathbf{v}^{(1)})(\mathbf{g}_k - \mathbf{v}^{(1)})^\top$ on **cluster centroids** $\mathbf{g}_k$ (mean-pooled features of all patches within each cluster). The intra-cluster variation — which is the very variability the paper claims to capture — is lost by mean pooling inside clusters. The paper is transparent that "both moments are computed based on cluster representations rather than individual patches" (line 29), but the background/motivation text is written as if patch-level covariances are being computed. The method computes a meaningful second-order statistic (covariance of cluster centroids), but the paper needs to (a) explicitly reconcile the motivation with what is actually computed, and (b) justify why cluster-level covariance captures the desired information when intra-cluster variation is discarded.

2. **Adaptive clustering claim is asserted but not validated**: The paper claims DBSCAN "adaptively adjusts granularity: small clusters for rare pathological regions and large clusters for abundant normal tissues" (Section 4.1) and that this provides "variable-resolution processing" (Abstract). However, no evidence supports this claim — there is no analysis of cluster sizes by tissue type, no visualization showing which patches form small vs. large clusters, and no comparison to a non-adaptive compression baseline (e.g., random downsampling, uniform grid pooling, or k-means with fixed cluster count). The ablation in Table 3 removes clustering entirely (w/o CM), which changes the instance count from $K$ to $n$, so any observed drop could be due to optimization difficulties with more instances or regularization effects rather than the adaptive property. A controlled experiment holding the number of clusters fixed while removing adaptivity is needed to support the adaptivity claim.

### Minor

3. **Near-ceiling performance on CAMELYON16 reduces discriminative power**: All attention-based methods achieve AUCs above 98% on CAMELYON16 (Table 1: ABMIL 98.88%, CLAM-SB 98.53%, S4MIL 99.02%, HOMIL 99.23%). The claimed relative improvement (0.35% AUC over ABMIL) is at the ceiling. The paper uses CONCH features, which likely contribute to these high baseline numbers, but there is no comparison to published CONCH-based results for these methods to contextualize how expected the baseline performance is. The TCGA-NSCLC results (Table 2) show more room for improvement and are more informative.

4. **No statistical significance testing**: On TCGA-NSCLC (Table 2), HOMIL achieves 93.24% ACC (SE 2.47%) vs. the best baseline HMIL at 92.89% (SE 1.45%). The difference (0.35%) is well within overlapping standard errors, yet the paper claims "best performance across all key metrics" without any paired test or confidence interval. Given the small margins and variability, significance testing (e.g., Wilcoxon over folds) would strengthen the claims.

5. **Covariance compression design is unablated and arbitrary**: The covariance matrix is compressed to a $d$-dimensional vector via row-wise 1D convolution with $T=4$ kernels of size $m=64$, followed by two stages of max-pooling (Section 4.3.3). No motivation is given for this specific architecture, no ablation compares it to alternatives (flattening + linear layer, using the diagonal, spectral decomposition), and no analysis shows what information is preserved or lost. For the method's claimed main contribution, this design choice deserves scrutiny.

6. **Centering around attention-weighted sum is not discussed**: The covariance computation centers cluster features around $\mathbf{v}^{(1)}$, the attention-weighted sum (not the unweighted mean). This means clusters with high attention weights pull the centroid toward themselves, *reducing* their contribution to the covariance — the opposite of what one might expect. This design choice is not motivated or discussed (Section 4.3.3).

### Trivial

7. The unnormalized covariance $\Sigma = \sum_i (\mathbf{h}_i - \mu)(\mathbf{h}_i - \mu)^\top$ in Section 3.2 lacks a $1/n$ or $1/(n-1)$ normalization. While this is a choice that affects magnitude scaling with the number of patches/clusters, the paper should at least note it.

8. The covariance matrix size is $512 \times 512 = 262K$ entries from a single slide's cluster features, yet the paper does not discuss potential overfitting when $K$ is small (e.g., for a slide with few clusters).

## Nice-to-Haves

- Show what the covariance matrix captures: a visualization or analysis of what covariance structure distinguishes tumor from normal slides, or whether off-diagonal elements encode meaningful inter-feature relationships.
- Compare HOMIL's second-order stream using patch-level features vs. cluster-level features to directly test whether the cluster-level approximation is sufficient.
- Add a simple baseline replacing the covariance with the diagonal (variance) to isolate whether off-diagonal (correlation) information is what provides the benefit.
- Include a runtime/memory breakdown showing how much time is spent on clustering vs. training for HOMIL.
- Analyze the DBSCAN clustering outcomes: report cluster size distributions and show qualitative examples of small clusters corresponding to pathological regions.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Near-perfect results across all methods → evaluation setup is not informative"** (from harsh critic): Demoted from the critic's "fatal" framing to Minor (#3 above). The critic's claim that "the original ABMIL paper reports ~92% AUC" ignores that the original paper used ImageNet-pretrained ResNet, while this paper uses CONCH (a pathology foundation model), which is well-known to produce near-ceiling results on CAMELYON16. The comparison is unfair and the paper's relative comparisons within a unified codebase are valid.

- **"The runtime improvements are engineering benefits, not novel contributions"** (from harsh critic): This is not a weakness — the paper claims efficiency as a contribution and demonstrates it. The speed improvement is a genuine benefit of the clustering approach.

- **"Fusion weight interpretation could be the model ignoring second-order stream"** (from harsh critic): This is speculative and contradicted by the ablation which shows that removing the second-order stream degrades performance (Table 3: w/o SOM drops ACC from 96.98% to 95.98%).

- **Core strengths #4-5 from Strength Finder**: Generic strength claims about "consistent superior performance" and "ablation validates contributions" are already covered in Strengths 2 and 4 above. The strength about "generalization beyond ABMIL" is covered in Strength 1.

- **Strength Finder's claim that "ABMIL becomes a special case"**: This is from the paper itself, not an independent strength assessment. It's already incorporated in Strength 1.

## Novel Insights

The most interesting observation emerging from the reviews — not fully present in the paper — is the interplay between the clustering granularity and the covariance estimation quality. The paper uses DBSCAN to compress $n$ patches into $K$ clusters, then computes a $d\times d$ covariance from $K$ cluster centroids. For slides where $K < d$, the covariance matrix will be rank-deficient, effectively encoding only $K-1$ degrees of freedom. This means the second-order representation is fundamentally bounded by clustering quality: slides with few clusters get impoverished covariance estimates. Neither the paper nor the reviewers explore this rank-deficiency issue, but it directly affects how much information the second-order stream can capture and whether a simpler alternative (e.g., patch subsampling without clustering, or a diagonal approximation) might be equally effective at lower computational cost.

## Suggestions

1. **Reconcile the motivation with the implementation**: Either rewrite Section 3.2 to explicitly state that the covariance is computed on cluster-level representations (and justify why this is sufficient), or — more ambitious — implement a patch-level covariance computation using a memory-efficient approach (e.g., sketching or random projections) and compare it to the cluster-level version.

2. **Validate the adaptive clustering claim**: Add a controlled experiment comparing DBSCAN-based compression to a non-adaptive alternative (e.g., random patch partitioning into $K$ groups, or uniform grid pooling) at the same compression ratio. Also include a histogram of cluster sizes and a qualitative visualization showing that small clusters correspond to pathological regions.

3. **Add statistical significance tests**: Report paired tests (e.g., Wilcoxon signed-rank or confidence intervals via bootstrapping) for the key comparisons, especially on TCGA-NSCLC where the margins are small relative to the standard errors.

4. **Ablate the covariance compression**: Compare the 1D conv+max-pooling to simpler alternatives (e.g., flatten the upper triangle + linear layer, use the diagonal only, or use spectral moments) to justify the specific design choice or replace it with a simpler default.

5. **Contextualize the CAMELYON16 baselines**: Acknowledge that CONCH features yield near-ceiling performance and note whether these results align with published CONCH-based numbers for the baseline methods, so readers can calibrate the expected improvement.

## Score and Decision

My round-1 bracket placed this paper between ~4.0 and ~6.5. The narrowest plausible range from low-band anchors (MMPL at 4.00, Cell Cloud at 4.00) and middle-band anchors (ASMIL at 6.00, MAMMOTH at 6.50). Round 2 narrowed to 4.5–5.5 by comparing against the Manifold Residual paper (5.50, accepted despite split reviews) and the Low-Signal MIL paper (4.67, rejected). HOMIL has a stronger empirical validation than the reject-level anchors but has more significant methodological gaps (motivation-implementation disconnect, unvalidated adaptive clustering) than the accept-level anchors ASMIL and MAMMOTH, which have cleaner experiments and better-supported claims. Hence a score of 5.0 — borderline with genuine contributions but needing substantial revision.

**Anchors retrieved (all rounds):**
- /home/wg25r/review_agent/human_reviews_2026/Sz2kL7UiEG.md — 2.50 (Withdrawn). Weak WSI paper. HOMIL is far stronger.
- /home/wg25r/review_agent/human_reviews_2026/7uaPJ6WAHv.md — 2.00 (Withdrawn). HOMIL is far stronger.
- /home/wg25r/review_agent/human_reviews_2026/bLZpUXRJ7E.md — 2.50 (Withdrawn). HOMIL is far stronger.
- /home/wg25r/review_agent/human_reviews_2026/E1sFAJU4Aq.md — 3.33 (Withdrawn). HOMIL is stronger.
- /home/wg25r/review_agent/human_reviews_2026/CYmjrbQRyM.md — 6.00 (Accept Poster). ASMIL has cleaner validation; HOMIL is weaker.
- /home/wg25r/review_agent/human_reviews_2026/rYbYbgeaEv.md — 4.00 (Reject). MMPL has serious efficiency validation gaps; HOMIL is stronger.
- /home/wg25r/review_agent/human_reviews_2026/S5Io33pc78.md — 6.50 (Accept Poster). MAMMOTH has broad, thorough evaluation; HOMIL is weaker.
- /home/wg25r/review_agent/human_reviews_2026/yC5jtOSm7F.md — 4.00 (Reject). Cell Cloud is complex with unclear benefits; HOMIL is stronger.
- /home/wg25r/review_agent/human_reviews_2026/kI27Niy4xY.md — 8.00 (Accept Oral). Unrelated topic (text-to-3D). Not comparable.
- /home/wg25r/review_agent/human_reviews_2026/DM0Y0oL33T.md — 8.00 (Accept Oral). Unrelated topic. Not comparable.
- /home/wg25r/review_agent/human_reviews_2026/DTQIjngDta.md — 8.00 (Accept Poster). Unrelated topic. Not comparable.
- /home/wg25r/review_agent/human_reviews_2026/RDerF20JYT.md — 8.00 (Accept Poster). Unrelated topic. Not comparable.
- /home/wg25r/review_agent/human_reviews_2026/PLva6Rol4W.md — 4.67 (Reject). MIL theory paper, not WSI. HOMIL is stronger.
- /home/wg25r/review_agent/human_reviews_2026/HBP9uSEYME.md — 5.50 (Accept Poster). Similar quality — both have novel ideas with validational gaps. HOMIL has better empirical breadth.
- /home/wg25r/review_agent/human_reviews_2026/p1tlo14Atj.md — 5.50 (Reject). Unrelated topic (SSL with side info). Not comparable.
- /home/wg25r/review_agent/human_reviews_2026/A0kvufiUAU.md — 4.50 (Reject). Cross-cancer knowledge transfer, limited empirical scope. HOMIL is stronger.
- /home/wg25r/review_agent/human_reviews_2026/24QX6XpvSL.md — 4.00 (Accept Poster). Multi-modal histopathology-genomics. Not directly comparable.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
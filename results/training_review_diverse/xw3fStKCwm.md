Here is my consolidated meta-review:

---

## Summary

This paper proposes using tensor-train (TT) low-rank decomposition to compress point clouds by framing compression as density estimation with Sliced Wasserstein and nearest-neighbor distance losses. This probabilistic approach avoids the ordering sensitivity of standard TT-SVD. The TT point cloud is evaluated for OOD detection (replacing coreset subsampling in PatchCore on MVTec AD) and as an indexing structure for ANN search (on Deep1B), where its hierarchical structure yields better bucket coverage than GNO-IMI.

---

## Strengths

- **Superior compression quality on MVTec AD:** At both 100× and 1000× compression ratios, the TT point cloud trained with SW + NN losses outperforms coreset subsampling on pixel-level metrics, with the gap widening at higher compression (Section 3.2). This directly validates the core compression claim.

- **Better bucket coverage than GNO-IMI on Deep1B:** The TT-based indexing has roughly 6× fewer empty buckets and a 5× lower expected bucket size (at TT-rank 32) compared to GNO-IMI, and the recall-difference curve shows sustained advantage across most of the recall spectrum (Section 3.3, Figs. `fig:expected-bucket-sizes`, `fig:empty-buckets`, `fig:delta-recall-curve`).

- **Probabilistic formulation cleanly addresses ordering sensitivity:** By treating compression as distribution approximation with density-estimation losses, the method becomes invariant to row ordering — a known limitation of direct TT-SVD that the paper identifies and solves (Section 2, lines 68–76).

- **Clear memory-advantage derivation tied to experimental design:** The paper derives the complexity reduction from O(ND) to O(D N₁ r + k r² N_max) and explicitly matches parameter counts to baselines in both the MVTec and Deep1B experiments, making the memory-efficiency claims concrete and verifiable (lines 65–66, 173–175, 214).

---

## Weaknesses

### Fatal
None.

### Major

1. **Underspecified ANN algorithm and missing efficiency metrics.** The hierarchical beam-search method is described in only a single paragraph (~4 lines, lines 145–148). No formulas, pseudocode, or search algorithm are given in the main text. The paper references `\cref{eq:ttm-centroids}` (line 157) and may contain details in the appendix, but the main-text description alone is insufficient. More critically, despite the title promising "Efficient Approximate Nearest Neighbor Search," the paper itself states that it "focus[es] on indirect characteristics such as the quality of dataset coverage, rather than providing actual queries-per-second values" (line 191). Without any latency, throughput, or distance-computation measurements, the "efficiency" claim is unsupported. The paper's own "proof-of-concept" framing (line 190) does not relieve it of the need to justify the efficiency asserted in the title. This is the most significant gap in the paper.

2. **Missing experimental hyperparameters for the MVTec experiments.** The paper states that for the MVTec AD experiments, it uses a TT representation with two cores and chooses N₁, N₂, and r to match the parameter count of the coreset (lines 173–175), but the actual numerical values of N₁, N₂, and r are never reported. Without these, the number of points in the TT cloud (N₁×N₂) is unknown, and the experiments are not fully reproducible. The paper's statement that it uses "the same hyperparameters for all MVTec datasets" (line 175) only underscores the need to disclose what they are.

### Minor

3. **No analysis of training cost or convergence.** The paper acknowledges using a random subset to estimate the NN loss efficiently (line 114) and mentions SGD optimization (line 77), but provides no training time, iteration count, or convergence discussion. Given that computing the Sliced Wasserstein loss requires generating and sorting all TT points per projection (O(N log N)), the computational overhead of training could be substantial, and the paper offers no guidance on whether this cost is acceptable in practice.

4. **No ablation of the loss trade-off parameter α.** The NN loss uses a linear combination with coefficient α (line 122–124), but no sensitivity analysis or ablation is provided to show how α affects compression quality. Similarly, the initialization of the TT cores is not specified, which is a standard concern for non-convex optimization.

5. **No validation that the probabilistic training improves over TT-SVD.** The paper motivates the probabilistic approach by arguing that direct TT-SVD is sensitive to row ordering, but never directly compares the trained TT cloud against a TT-SVD baseline (e.g., TT-SVD applied after a learned row permutation) to demonstrate that the density-estimation losses are actually beneficial. The claim that the probabilistic training is necessary therefore lacks direct supporting evidence.

### Trivial

- The paper states "exellent" instead of "excellent" (line 272).
- The ANN experiment uses a 10M subset of Deep1B, so the scalability to the full billion-scale dataset is unknown — this is acknowledged by the authors but worth flagging.

---

## Nice-to-Haves

- Comparison with alternative compression approaches such as TT-SVD with a learned row permutation, low-rank matrix factorization (SVD-based coreset generation), or a simple autoencoder would further validate the necessity of the proposed training framework. However, the existing comparison against the relevant SOTA (coreset subsampling for PatchCore) is sufficient for the paper's stated scope.

- An analysis of how the factorization lengths N₁,…,N_k should be chosen (e.g., as a function of data dimensionality and desired compression ratio) would strengthen the method's practical usability.

---

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Unfair comparison due to different point counts" (Harsh Critic Issue 1, part):** The reviewer argued that if N₁N₂ > cN, the TT cloud has an unfair advantage. However, the paper matches *parameter counts* (memory budget), which is the standard way to compare compression methods. Having more generated points from the same parameter budget is a legitimate advantage of parametric compression, not a confound. The valid core of this concern (missing N₁,N₂ values) is retained in Weakness #2 above.

- **"Missing centroid formulas / hierarchical derivation" (Harsh Critic Issue 2, part):** The paper references `\cref{eq:ttm-centroids}` (line 157), suggesting that centroid computation formulas exist in the appendix, which the parser strips from all submissions. Per policy, this criticism is removed as it concerns content likely present in the original submission.

- **"No comparison with TT-SVD, SVD, autoencoder" as a major omission (Harsh Critic Issue 3):** The paper's comparison target (coreset subsampling) is the relevant SOTA for the OOD application domain. Demanding comparisons against generic compression methods not used in this application is scope creep. Moved to Nice-to-Haves.

- **Generic strengths from Strength Finder:** Some strengths were generic (e.g., the paper addresses an important problem). These are dropped as they lack specific evidentiary content.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface no new interpretation of the results — they primarily request better specification and more thorough evaluation.

---

## Suggestions

1. **Report N₁, N₂, r for every experimental setting** (at least for MVTec) and explicitly state the resulting TT point cloud size (N₁×N₂) alongside the coreset size (cN) so readers can directly compare point counts.

2. **Provide the beam-search algorithm and centroid computation formulas** in the main text or a clearly referenced appendix. Even a brief pseudocode listing would suffice for reproducibility.

3. **Add at least a rough runtime measurement** for the ANN search (e.g., queries per second on the 10M Deep1B subset compared to GNO-IMI) to substantiate the "efficient" claim in the title. Alternatively, re-scope the title to avoid promising efficiency that is not evaluated.

4. **Include an ablation of α** and specify the initialization strategy for the TT cores to improve reproducibility and scientific rigor.

5. **Add a direct comparison between trained TT and TT-SVD** on a simple metric (e.g., SW distance to the original cloud) to empirically validate the necessity of the probabilistic training.

6. **Briefly discuss training time** (e.g., wall-clock hours for the MVTec or Deep1B experiments) so readers can assess practical applicability.

---

## Score and Decision

**Originality:** 3/5 — The idea of using TT decomposition for point cloud compression with density losses is reasonably novel.  
**Importance:** 3/5 — The problem (efficient point cloud representation for OOD and ANN) is relevant, but the paper's contribution is incremental in a crowded space.  
**Claims support:** 2/5 — The core compression claim is supported, but the ANN efficiency claim is unevaluated, and some experimental details are missing.  
**Soundness:** 3/5 — The methodology is sound, but the evaluation gaps (missing hyperparameters, no training cost, no runtime) weaken empirical support.  
**Clarity:** 3/5 — The method is clearly explained, but the ANN algorithm description is too brief.  
**Value:** 3/5 — If the experimental gaps are addressed, the paper would be a useful contribution; in its current form, it is suggestive but incomplete.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
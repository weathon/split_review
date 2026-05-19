- Decision: Reject
- Avg Score: 3.25
- Scores: 3, 6, 1, 3
Now I have all the information I need. Let me compose the final consolidated review.

---

## Summary

This paper proposes a method for video tracking and 3D map creation that operates on motion vectors extracted from standard video encoders. The core theoretical contribution is a coreset construction (Algorithms 1–2) for the segment-clustering problem (Problem 1), which approximates the continuous integral loss over segments using a weighted point set. The authors apply this to motion-vector clustering for tracking (Section 3) and outlier filtering for SLAM (Section 4), reporting real-time frame rates on low-end single-board computers.

## Strengths

- **Provable coreset for segment clustering with continuous integrals**: Lemma 2.8 and Theorem 2.9 provide formal guarantees that Algorithm 1 (SEG-CORESET) and Algorithm 2 (CORESET) yield $(\epsilon,k)$-coresets for individual segments and sets of segments respectively. The paper correctly identifies this as a generalization of Har-Peled (2006) from discrete to continuous integrals (Section 5), which appears to be a genuine theoretical contribution.

- **Real-time clustering speed on low-end boards**: Section 3.2 reports that the coreset + k-means clustering step processes at >94 fps on a Le Potato single-board computer (4.23s for 400 frames). Section 4 reports >40 fps for the clustering/outlier-filtering step on a Raspberry Pi Zero. These throughput numbers are impressive and demonstrate the computational efficiency of the coreset-based approach.

- **Deterministic coreset construction**: Algorithm 1 is explicitly deterministic (the paper contrasts it with random sampling which would introduce failure probability), which is a legitimate technical advantage over randomized alternatives.

## Weaknesses

### Fatal

None. The theoretical contribution (coreset for segment clustering) appears fundamentally sound. The weaknesses are in the experimental validation and connection between theory and practice, which are major but not fatal.

### Major

1. **No quantitative accuracy metrics for tracking or mapping.** The paper claims to perform "video tracking" but reports only qualitative results (Figures 4 and 5). No bounding-box overlap, precision, recall, success rate, or any other standard tracking metric is reported. For the map creation experiment (Section 4), no map accuracy metric (RMSE, trajectory error, etc.) is given. Speed numbers alone do not validate a tracking or mapping method — a system that outputs random clusters could run at any speed. The paper's central applied claims are unsubstantiated without accuracy evaluation.

2. **"Provably good tracking" is misleading.** The theoretical guarantee (Theorem 2.9) is for the segment-clustering problem (Problem 1), not for tracking accuracy on video. The paper never formally establishes a connection between solving Problem 1 and producing correct tracking output. The abstract's phrasing "provably good tracking algorithm" overstates what the theory actually certifies. This is a significant framing gap between the paper's headline claims and its technical content.

3. **Gap between theory and the implemented pipeline.** The empirical method (Section 3, steps i–v) diverges from the proven Algorithm 2 in several ways:
   - **Uniform pre-subsampling** (step ii): motion vectors are uniformly subsampled to at most 1000 when there are more, *before* the coreset construction. This ad-hoc heuristic is not part of Algorithm 2, so the theoretical guarantees of Theorem 2.9 do not carry over to the pipeline actually tested.
   - **Coreset size fixed to 10 without reporting ε** (step iii): the paper says "calibrated such that the coreset size for each segment is 10" but Algorithm 1 takes ε and k, not a fixed size. What ε was used, and what approximation error was achieved in practice? Neither is reported.
   - **4D encoding is not justified**: adding angular information as two extra dimensions (scaled to (0,1) and (1,0)) is an ad-hoc representation whose effect on the theoretical guarantees is not discussed.

   These gaps mean the experimental results do not test the theory; they test a heuristic that uses some of the same building blocks.

4. **Motion vectors extracted offline for the low-end board experiment.** Section 3.2 states: "Due to missing support for Arm architecture, we extracted the motion vectors beforehand and transferred them as a Numpy array." The 94 fps figure on Le Potato excludes motion-vector extraction, which is the most computationally expensive step. The paper acknowledges this but the speed claims (title, abstract) are qualified by this caveat. The full pipeline on the board reaches only 23 fps once decoding is included, and the paper does not actually demonstrate motion-vector extraction running on the board.

5. **Missing hardware context for the YOLOv8 comparison.** Section 3.1 reports YOLOv8 at 12 fps without specifying whether it was run on CPU or GPU, making this speed comparison uninterpretable. A proper comparison would specify the hardware, inference configuration, and include tracking-specific baselines (e.g., CSRT, KCF, SORT) under comparable conditions.

6. **No robustness evaluation despite claiming M-estimator support.** The abstract states "Our method supports M-estimators that are robust to outliers," but the experiments use sum-of-squared distances (Section 3: "for simplicity"). No evaluation with outliers, occlusions, camera motion, or noise is performed.

### Minor

- **No ablation study isolating the coreset contribution.** The paper does not compare tracking with vs. without the coreset, or with different coreset sizes, to measure the approximation error achieved in practice. This makes it impossible to tell whether the coreset helps or hurts.

- **No comparison to existing motion-vector-based or lightweight tracking methods.** The paper compares only to YOLOv8 (a detector, not a tracker) and ORB-SLAM (a SLAM system). No comparison is made to CPU-compatible trackers (e.g., CSRT, KCF, or even simple optical-flow clustering), which would be more informative baselines for the claimed setting.

- **Single-run, single-scene evaluation for the SLAM experiment.** Section 4's 3D map experiment uses one indoor drone video, one run, and no quantitative map accuracy (RMSE, trajectory error). This is insufficient to support a claim that motion-vector features are superior for SLAM or even adequate.

### Trivial

None worth listing.

## Nice-to-Haves

- Evaluate the coreset directly: compare k-means clustering on the full motion-vector set vs. on the coreset, measuring both the Problem 1 loss and downstream tracking accuracy.
- Report the ε values and effective coreset sizes used in experiments.
- Add a standard tracking benchmark (e.g., OTB-100 subset) with standard metrics (precision, success rate) to validate the tracking claim.

## Removed Points

These points are removed per filtering criteria (see explanations below):
- **"Privacy claims not evaluated"** — The paper states "privacy preservation to some degree" as a qualitative observation (Section 3, one sentence). This is not a tested claim and is presented as an inherent property of using motion vectors rather than RGB. The critic's demand for evaluation goes beyond what the paper asserts.
- **"Section 1.1 overstates GPU requirements for neural tracking"** — The paper says "frequently requires at least mid-level GPUs ability to achieve 30-fps," which is a general observation, not a formal claim. This is a scope nitpick.
- **"Quote from Denisov et al. is lengthy"** — Pure presentation/style critique; removed.
- **"Coreset for convex shapes claim is hand-wavy"** — The paper briefly mentions this as a generalization direction (not a tested result). Not a substantive weakness.
- **"Missing proofs in appendix"** — Per the rubric, missing appendix content is a parser issue, not an author error.
- **"Ties broken arbitrarily could produce different results"** — Speculative; the paper says "essentially the same results" and ties are a known minor source of non-determinism in k-means.
- **Strength: "Privacy preservation by design"** — Generic/superficial strength. The paper mentions this in one sentence without evidence. Removed.
- **Strength: "Large speedup over YOLOv8"** — Retained in weakened form as a minor point under weaknesses (missing hardware context). The strength description calling YOLOv8 a "state-of-the-art deep-learning tracker" is inaccurate (YOLOv8 is a detector), and the comparison lacks sufficient context to be presented as a strength.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the gap between theory and practice clearly, but this is a critique of the paper's presentation, not a novel insight.

## Suggestions

1. Reframe the paper around the coreset contribution (segment clustering approximation) and present the tracking/mapping experiments as case-study demonstrations of the coreset's computational efficiency. Remove or qualify the "provably good tracking" language.
2. Add quantitative accuracy evaluation on a standard tracking benchmark (even a small subset like OTB-50) with standard metrics.
3. Add an ablation study comparing the full Algorithm 2 pipeline (with reported ε values) vs. the heuristic pipeline vs. k-means on raw motion vectors.
4. Run the full pipeline on the low-end board including on-device motion-vector extraction (or at minimum, document why this is infeasible and what steps remain).
5. Report the hardware configuration (CPU/GPU) for the YOLOv8 baseline and consider adding a lightweight CPU-based tracker as a more informative comparison.

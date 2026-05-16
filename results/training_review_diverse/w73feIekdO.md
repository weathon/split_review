I have thoroughly read the paper and verified all reviewer claims against the actual content. Let me now construct the consolidated review.

---

## Summary

This paper proposes a coreset construction for the problem of clustering segments (functions [0,1] → ℝ^d) with an integral loss, reducing each segment to a small set of weighted points that approximate the loss up to (1±ε). The authors apply this coreset to video tracking and 3D map creation using motion vectors extracted from standard video encoders (H.264/H.265), targeting real-time performance on low-end boards without GPUs. The theoretical contribution (Theorem 2.9, Lemma 2.8, Algorithms 1–2) provides explicit size and runtime bounds. The experiments demonstrate impressive throughput (tracking >1,400 fps on a laptop, >94 fps on Le Potato; 11.1 fps vs. 6.6 fps for ORB-SLAM on Raspberry Pi Zero) but lack quantitative accuracy metrics, proper baselines, and ablation of the coreset itself.

## Strengths

- **Provable coreset for segment clustering with explicit guarantees.** Theorem 2.9 and Lemma 2.8 provide an (ε,k)-coreset for the segment clustering problem (Problem 1) with rigorous size and runtime bounds. Algorithm 1 (SEG-CORESET) gives a deterministic construction for a single segment. This is a genuine theoretical contribution that generalizes prior work on coresets for points (Feldman & Schulman 2012) to non-discrete integrals over segments.

- **Real-time throughput on extremely resource-constrained hardware without GPUs.** The tracking algorithm processes 400 frames in 0.28 seconds (>1,400 fps) on a standard laptop (Section 3.1) and 4.23 seconds (>94 fps) on a Le Potato board (Section 3.2). The 3D mapping system achieves 11.1 fps on a Raspberry Pi Zero, outperforming ORB-SLAM's 6.6 fps on the same hardware (Section 4). These numbers directly demonstrate the paper's stated goal of real-time vision on micro-computers.

- **No training data, no labeled data, no neural networks required.** The method leverages motion vectors computed in hardware by existing video encoders (Section 1.2), requires no training, and operates solely on vector data (not RGB frames), which also provides a degree of privacy preservation (Section 1.3, line 227). This contrasts sharply with deep-learning approaches that require expensive training and GPU inference.

## Weaknesses

### Fatal

None.

### Major

1. **No quantitative accuracy evaluation for tracking or mapping.** The tracking evaluation (Section 3) is purely qualitative: a few example frames from one video (Figure 4) and runtime numbers. No accuracy metric (bounding-box overlap, center error, trajectory error, success rate) is reported. The 3D mapping evaluation (Section 4) is similarly anecdotal: the maps are shown qualitatively (Figure 5) with no map quality metric (point-cloud accuracy, trajectory recovery error, number of correct correspondences). Without accuracy numbers, the runtime advantage is uninterpretable — a fast method that produces incorrect results is not useful. The paper's abstract claims "provably good tracking," but the guarantee applies only to the coreset's approximation of the segment-clustering loss, not to tracking accuracy. This gap between the theoretical claim and the experimental evidence is the paper's central weakness.

2. **The coreset contribution is not isolated.** The tracking pipeline (Section 3) uses: (i) uniform sampling if >1,000 vectors, (ii) Algorithm 1 (SEG-CORESET) on each segment with coreset size 10, (iii) k-means on the resulting weighted points. The paper never compares against k-means on the raw motion vectors (or on uniform samples) *without* the coreset. The reader cannot tell whether the coreset improves speed, accuracy, robustness, or does nothing at all. An ablation study — e.g., varying the coreset size or replacing it with uniform sampling — is essential to validate the practical benefit of the theoretical contribution.

3. **Inappropriate and insufficient baselines.** For tracking, the only comparison is YOLOv8 — an object detector, not a tracker — and only runtime (12 fps vs. 278–1,400+ fps) is reported, not accuracy. A speed comparison against a detector operating on full RGB frames tells the reader nothing about whether the proposed method is competitive for the task of tracking. For 3D mapping, ORB-SLAM is compared only on runtime (6.6 fps vs. 11.1 fps), with no comparison of map quality, drift, or reconstruction error. Standard benchmarks (e.g., OTB, VOT for tracking; TUM RGB-D or KITTI for SLAM) are not used, making the results incommensurable with prior work.

4. **Incomplete description of the 3D mapping pipeline.** Section 4 describes the outlier removal via clustering but is vague on how the 3D map is actually constructed: "take the start of each motion vector as a feature and map this feature to the end of the motion vector" (line 283). There is no mention of pose estimation, camera calibration, triangulation, bundle adjustment, or map representation. The comparison to ORB-SLAM is therefore difficult to interpret — it is unclear whether the two pipelines are solving the same problem with the same output.

### Minor

1. **Tracking algorithm parameters are not justified or ablated.** The tracking method (Section 3, steps i–v) introduces several arbitrary choices: 10 consecutive frames per batch, uniform sampling threshold at 1,000 vectors, coreset size 10 per segment, k=2. No sensitivity analysis or justification is provided for any of these parameters. A brief study varying one or two parameters would strengthen the robustness claims.

2. **Motion vector extraction details are missing.** The paper does not specify the codec, block size, search range, or frame granularity used for motion vector extraction (Section 1.2 only provides a high-level description referencing H.264/H.265). This information is essential for reproducibility.

3. **Single-run runtime measurements without variance.** Runtimes are reported as single values with no confidence intervals or standard deviations. Given randomness from uniform sampling and k-means initialization, multiple runs would be appropriate.

4. **The connection between the theoretical segment-clustering problem and the tracking heuristic is under-explained.** The theory (Problem 1) defines a loss as an integral over segments, and the coreset preserves this loss. The tracking algorithm converts motion vectors to 4D segments, applies the coreset, then runs k-means on the resulting points. The paper states (lines 65–66) that the coreset "approximates the loss function" and enables "efficient approximation," but the mapping from the integral loss to tracking quality (e.g., why k=2 is the right choice, how cluster centers relate to object position) is not made explicit. The connection is present but could be much clearer.

### Trivial

- Algorithm 1 is presented as an image rather than text (line 172), making it unsearchable and harder to follow.

## Nice-to-Haves

- **A sensitivity analysis** varying the coreset size (e.g., 5 to 50) and the uniform sampling threshold to demonstrate robustness.
- **A discussion of failure modes** beyond objects entering the field of view (e.g., camera motion, occlusions, illumination changes).
- **Standard deviation or confidence intervals** for runtime measurements.
- **Specification of codec parameters** (block size, search range) for reproducibility.

## Removed Points

These points were flagged by reviewers or the strength finder but are removed or downgraded for the following reasons:

- **"The 1,400+ fps claim is misleading because it excludes decoding/saving."** — Removed. The paper transparently separates tracking-only time from total time (decoding + tracking + saving), and reports both (278 fps total). This is honest reporting, not misleading.
- **"The low-end board test pre-computes motion vectors, sidestepping the main claimed advantage."** — Removed as stated, but kept as a minor caveat: the paper acknowledges this limitation (line 262), and the claim that the *clustering* runs in real-time on low-end hardware is still valid.
- **"Weak connection between theory and application"** — Downgraded from Major to Minor. The paper does explain the connection (lines 65–66: the coreset approximates the segment-clustering loss, enabling k-means on the resulting points), though it could be more explicit. The criticism that "the original segment structure and integral loss seem discarded" misunderstands the coreset's purpose, which is precisely to preserve that loss via weighted points.
- **Strength Finder's "Concrete speed comparison against strong baselines"** — Weakened. The YOLOv8 comparison is a detector-vs-tracker mismatch; the ORB-SLAM comparison is only runtime. The throughput numbers are real but the baseline comparisons are not apples-to-apples.
- **"The paper should also cover additional tasks/datasets"** — Scope-creep suggestions (e.g., OTB, VOT, MOT benchmarks) are moved to Nice-to-Haves. The paper's main contribution is the coreset; full benchmark comparisons would strengthen the application but are not strictly required for the theoretical claim.
- **"Algorithm 1 is in an image"** — This is a formatting artifact of the PDF extraction; however, even in the original submission, the pseudo-code would benefit from being typeset in text for searchability and accessibility. Kept as Trivial.

## Novel Insights

Beyond the paper's own contributions, the reviews surface one genuinely novel observation: the paper identifies a core tension between provable coreset guarantees and heuristic application pipelines. The coreset guarantees hold for the segment-clustering loss (Problem 1), but the downstream tracking/mapping pipelines introduce several additional heuristic steps (degree embedding, uniform pre-sampling, k-means with arbitrary k, outlier removal rules). This creates a gap where the theoretical guarantee no longer directly bounds the application output quality. Bridging this gap — either by extending the theory to cover the full pipeline, or by designing the application to better respect the theoretical formulation — is an interesting open problem that the paper does not address but implicitly highlights.

## Suggestions

1. **Add a controlled ablation** comparing the tracking pipeline with and without Algorithm 1 (SEG-CORESET). At minimum, compare: (a) k-means on raw motion vector points, (b) k-means on uniform samples, (c) k-means on coreset outputs. Report both runtime and a simple accuracy metric (e.g., center error on Big Buck Bunny frames).
2. **Report at least one quantitative accuracy metric** for tracking. Even a simple per-frame center-vs-ground-truth distance on a few manually annotated frames would be far more informative than the current qualitative snapshots alone.
3. **Clarify the 3D mapping pipeline** by describing the actual reconstruction method (pose estimation, triangulation, map representation) or, if the pipeline is simply ORB-SLAM with motion-vector features, state this explicitly.
4. **Replace or supplement the YOLOv8 baseline** with a lightweight tracker that uses motion or flow (e.g., Farnebäck optical flow + clustering, or a simple Kalman-filter tracker). Compare both speed *and* accuracy.
5. **Explain the theory-to-application mapping** more explicitly: how does solving Problem 1 (segment clustering) relate to tracking a moving object? What does k=2 correspond to conceptually (foreground vs. background motion?), and why is the integral loss the right objective for tracking?

## Score and Decision

This paper has a genuine theoretical contribution (coreset for segment clustering) and demonstrates impressive throughput on low-end hardware. However, the empirical evaluation is fundamentally incomplete: there are no quantitative accuracy metrics for either tracking or mapping, the coreset's contribution is not isolated via ablation, and the baselines are mismatched. The paper claims "good tracking" and "map creation" in the abstract but provides no evidence that the outputs are actually correct — only that they are fast. Given that the experiments are central to the paper's framing as an applied method, these gaps are too large to overlook.

With major revisions (especially proper quantitative evaluation), the paper could be significantly strengthened. In its current form, the experimental validation does not support the claimed applications.

**Score: 5.0** — Borderline; the theoretical contribution is real but the empirical validation is insufficient for the claimed applications.

**Decision: Reject** — The paper's main weakness (no quantitative accuracy evaluation, no coreset ablation, mismatched baselines) cannot be addressed in a rebuttal. The theoretical contribution is valuable but the paper is framed primarily around its applications, which are not adequately validated.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
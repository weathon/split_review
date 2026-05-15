Now I have all the verification I need. Let me produce the consolidated review.

## Summary

This paper proposes real-time computer vision methods (video tracking and map creation) for low-end hardware by clustering motion vectors extracted from standard video encoders. The core theoretical contribution is a deterministic coreset construction (SEG-CORESET, Algorithm 1) that reduces continuous segments to weighted point sets with provable approximation guarantees for the k-segment mean problem, plus a combined algorithm (Algorithm 2) that further compresses via Feldman & Schulman (2012). Empirically, the paper reports high throughput (278 fps on laptop, 94 fps on Le Potato for tracking; 11.1 fps on Raspberry Pi Zero for map creation) on 720×1280p video.

## Strengths

- **Provable coreset for continuous integrals over segments**: Lemma 2.8 and Theorem 2.9 provide a formal, deterministic coreset for the continuous k-segment mean problem — a setting the paper identifies as not previously addressed with hard bounds (contrasting with discrete-integral results such as Har-Peled, 2006). The theoretical machinery (Algorithm 1 → Algorithm 2) gives clear size and time guarantees.

- **Impressive throughput on low-end single-board computers**: The tracking pipeline achieves 94 fps (algorithm alone) on a Le Potato board, and the map creation pipeline runs at 11.1 fps on a Raspberry Pi Zero. These concrete measurements directly support the paper's central goal of enabling real-time vision on micro-computers without GPUs.

- **Order-of-magnitude speed advantage over a deep-learning baseline**: On the Big Buck Bunny clip, the proposed method processes 278 fps (including decoding) versus YOLOv8's 12 fps on the same hardware. While YOLOv8 is a detector rather than a tracker, this speed disparity illustrates the practical motivation for the approach.

- **Privacy preservation via motion-vector-only processing**: The method uses only computed motion vectors and never accesses RGB pixel data, which intrinsically limits visual reconstruction of the scene. This is a genuine practical advantage for privacy-sensitive applications.

## Weaknesses

### Fatal
None.

### Major

- **No quantitative tracking accuracy evaluation**: The tracking experiment reports only running time (278/94 fps). There are no standard tracking metrics — precision, recall, bounding-box overlap, center-location error, ID switches, or success rate — across the 400-frame clip. The qualitative results (Figure 4) show a known failure case (motion vectors pointing opposite to motion when an object enters the field of view) plus two frames where tracking appears reasonable. Without accuracy metrics, the claim of a "tracking algorithm" is unvalidated.

- **No comparison to lightweight classical trackers**: The paper compares running time only to YOLOv8 (a heavyweight object detector), not to any established real-time tracker such as KCF, CSRT, MOSSE, or a simple optical-flow baseline. Comparing speed against a method designed for a fundamentally different task (detection vs. tracking) does not establish the proposed method's competitiveness as a tracker. A comparison to lightweight trackers on standard tracking benchmarks with quantitative metrics is essential.

- **Ablation of the coreset is missing**: The experiments use a fixed coreset size of 10 points per segment. The paper itself acknowledges (lines 174) that "a uniform sample could have been used as an efficient sampling at the price of introducing failure probability and larger coreset size." Yet there is no experiment comparing the full pipeline (with coreset) against a baseline that skips Algorithm 1 entirely (i.e., uses raw sampled points without coreset weighting). Without this ablation, the practical necessity of the theoretical coreset contribution is not demonstrated for the application.

- **Map creation evaluation is purely qualitative**: The 3D map creation experiment (Section 4) provides only qualitative images (Figure 5) and running time. There are no standard SLAM/mapping accuracy metrics such as absolute trajectory error (ATE), relative pose error (RPE), or map reconstruction error on a known benchmark (e.g., TUM RGB-D, EuRoC). The comparison to ORB-SLAM is further confounded by simultaneous differences in feature extraction (motion vector endpoints vs. ORB features) and the use of gyroscope data for rotation, making it impossible to attribute the observed speed difference to the proposed clustering method alone.

### Minor

- **Practical coreset size undermines the claimed advantage over uniform sampling**: The tracking method uses only 10 points per segment via the coreset. At this small fixed size, the distinction between deterministic coreset sampling and simple uniform sampling is practically negligible — the deterministic guarantee adds little value when the sample is this small. The paper does not report actual coreset sizes derived from the theoretical bounds (Theorem 2.9), leaving a gap between theory and practice.

- **Known failure mode unquantified and unmitigated**: The paper acknowledges that motion vectors point opposite to actual movement when objects enter the field of view (Section 3.1). This is a systematic limitation of using motion vectors alone, but it is neither quantified (how many frames in the 400-frame clip exhibit this?) nor mitigated (does the center-of-cluster still provide useful tracking?). Any practical tracking system would need to handle this case.

- **Hyperparameter choices are unanalyzed**: The method uses several arbitrary thresholds and parameters (k=2 for tracking, k=10 for mapping, 10 points per segment, 1000 vector limit, outlier removal by mean+std threshold) without any sensitivity analysis. It is unclear how robust the results are to these choices or how to set them for new videos.

### Trivial
None.

## Nice-to-Haves

- Evaluating on additional videos with diverse motion patterns, lighting conditions, and background complexity (beyond Big Buck Bunny and the drone video) would strengthen generality claims.
- A failure case analysis showing frames with multiple moving objects or partial occlusion would help calibrate practical expectations.
- End-to-end real-time evaluation on target hardware with live video input (not pre-extracted motion vectors on Le Potato) would strengthen the hardware-feasibility claims.

## Removed Points

These points are flagged to be removed per the instructions; treat them with caution:

- **Criticism about missing appendix / inability to verify proofs** — removed because Lemma F.4 and Theorem G.1 were stripped by the parser; the proofs exist in the original submission.
- **"The paper never actually defines a tracking algorithm"** — removed as factually incorrect; the paper provides a numbered pipeline (lines 220–223) describing the tracking method.
- **Formatting/style nitpicks** — removed as these stem from parser artifacts, not the original paper.
- **Criticism that the coreset contribution "cannot be evaluated" due to missing appendix** — removed per above.

## Novel Insights

The most interesting observation emerging from these reviews is that the paper's theoretical and empirical contributions operate on two largely disjoint tracks. The theoretical side (Section 2) develops a novel coreset for continuous segment integrals with formal guarantees — a genuine contribution to the coreset literature. The empirical side (Sections 3–4) implements a practical pipeline that uses a fixed, small number of sampled points per segment (10) and does not exercise the coreset's key theoretical properties (adaptive size, deterministic vs. probabilistic guarantees). The reviews collectively reveal that the paper does not bridge this gap: there is no experiment showing that the coreset's guarantees translate to better tracking/mapping than a simple uniform sample, nor a demonstration that the coreset's size bound (which grows rapidly in k and r) is actually needed. This suggests that the strongest version of the paper would either (a) present the coreset result as a standalone theoretical contribution with minimal empirical illustration, or (b) redesign the experiments to actively demonstrate when the coreset matters (e.g., regimes where uniform sampling fails or where the coreset size bound yields genuine compression).

## Suggestions

1. **Add quantitative tracking evaluation**: Report standard metrics (precision plot, success rate, center location error) on a benchmark such as OTB-100 or a custom dataset with ground-truth annotations. This is the single most impactful improvement.
2. **Compare to lightweight trackers**: Include KCF, CSRT, or MOSSE as baselines for both accuracy and speed on the same hardware.
3. **Ablate the coreset**: Compare against a pipeline that skips Algorithm 1 (uses raw point samples without coreset weighting) to isolate the coreset's empirical contribution.
4. **Report actual coreset sizes**: Show the theoretical coreset size from Theorem 2.9 for the experimental parameters, and compare it to the fixed size of 10 used in practice.
5. **Quantify map creation**: Evaluate on a standard SLAM benchmark (TUM RGB-D or EuRoC) with ATE/RPE metrics, not just qualitative images.
6. **Analyze the failure mode**: Quantify how often motion vector reversal occurs in the test video and assess whether the cluster center remains useful despite it.

## Score and Decision

The paper presents a genuine theoretical contribution (coreset for continuous segment integrals) and demonstrates impressive throughput on low-end hardware. However, the experimental evaluation has major gaps: no quantitative tracking accuracy, no comparison to existing lightweight trackers, no ablation of the coreset, and purely qualitative map evaluation. These gaps prevent validation of the paper's core applied claims. The theoretical result is valuable but the experiments do not adequately support the claimed applications.

**MY FINAL SCORE: <pineapple>5.0</pineapple>**
**MY FINAL DECISION: <orange>Reject</orange>**
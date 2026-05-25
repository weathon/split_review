Now I have all the information I need. Let me compile the final review.

## Summary

The paper introduces Long-Form Spatio-Temporal Video Grounding (LF-STVG), a new problem setting for localizing targets in videos spanning 1–5 minutes, and proposes ART-STVG, an autoregressive transformer that processes frames sequentially with selective spatio-temporal memory banks and a cascaded decoder. The authors extend HCSTVG-v2 to create LF-STVG benchmarks and demonstrate substantial improvements over existing STVG methods on long videos (e.g., 23.0 vs 13.9 m.tIoU on 3-min videos) while remaining competitive on short-form STVG.

## Strengths

1. **Substantial and consistent gains across all video lengths.** Table 1 shows ART-STVG outperforms all prior methods on every LF-STVG benchmark (1–5 min). On 3‑minute videos it achieves 23.0 % m.tIoU vs. 13.9 % for the next best (TA‑STVG), and the gap grows with video length, directly supporting the claim that the autoregressive design handles long-form video effectively.

2. **Ablation studies validate the core design choices.** Tables 2–5 demonstrate that (a) using *all* temporal memories degrades performance (16.7 %→9.6 % m.tIoU) while the proposed selection recovers and improves to 23.0 %, (b) spatial memory selection provides additive gains, and (c) the cascaded decoder outperforms a parallel design by 1.5 % m.tIoU. These experiments directly support the claimed contributions of selective memory and cascaded decoding.

3. **Introduction of LF-STVG benchmarks.** The paper is the first to formulate long-form STVG and extends HCSTVG-v2 to create evaluation sets at five lengths (1–5 min). The rapid drop of existing methods on these sets (Table 1, Fig. 2) validates the need for the new problem and provides a standardized testbed for future work.

4. **Competitive short-form performance.** ART-STVG achieves 59.2 % m.tIoU and 39.2 % m.vIoU on HCSTVG-v2 (Table 7), only 1.2 %/1.0 % behind the dedicated short-form SOTA (TA‑STVG), showing the autoregressive framework does not sacrifice capability on short videos.

## Weaknesses

### Fatal
None.

### Major

1. **Undisclosed baseline evaluation protocol on long videos.** The paper compares ART-STVG with TubeDETR, STCAT, CG‑STVG, and TA‑STVG on videos up to 5 minutes but never describes how these methods (designed for ~20–35 second videos) were adapted. Crucially missing: how many frames each baseline received, whether subsampling or sliding windows were used, and any modifications to handle GPU memory constraints. Without this information, it is impossible to assess whether the comparison is fair — the large gap (e.g., 15.0 vs 8.1 m.tIoU on 5 min) could partly reflect unequal frame budgets rather than architectural superiority. **Mitigating evidence**: (i) the gap grows smoothly with video length, consistent with a genuine advantage; (ii) Table 6, where all methods are trained on 40‑second videos, shows ART‑STVG still outperforms by a large margin (28.3 vs 20.8 m.tIoU), replicating the advantage under a fairer training setup. Nevertheless, the inference protocol for baselines must be disclosed.

2. **Temporal grounding inference procedure is unspecified.** The temporal head outputs per-frame start/end probabilities \(h_i \in \mathbb{R}^2\), but the paper never explains how these frame-wise predictions are converted into a single temporal interval for m.tIoU computation (e.g., argmax, thresholding + grouping, or joint optimization). The loss function is deferred to supplementary material, and the inference step is omitted entirely. This is a gap in reproducibility, though the convention in STVG literature (selecting the frame with maximum start probability as start and maximum end probability as end) is standard enough that the intended approach can be inferred with high confidence.

### Minor

3. **Clarity of dataset extension annotations.** The paper states that LF‑STVG benchmarks were created by extending videos "based on original YouTube videos, not concatenated clips" and that they "manually review the extended videos to ensure their quality," but does not explicitly state whether the original temporal annotations (from 20‑second clips) were reused verbatim or re-annotated for the longer videos. The paper should clarify this to avoid ambiguity about the task's difficulty. (Note: the reviewer's concern about m.tIoU being "trivially bounded" by the original event length is incorrect — tIoU measures intersection/union, which is not inherently capped by ground-truth length.)

4. **Memory selection similarity metric unspecified for spatial branch.** For spatial memory selection, the paper says "calculate the similarity between each spatial memory and the textual feature" without specifying whether this is cosine similarity, dot product, or another metric (cosine similarity is specified for the *temporal* branch via Fig. 4 caption). The threshold for temporal boundary detection is also not given.

5. **No statistical significance / error bars.** All ablations and main results are reported without variance across multiple runs. While single-run evaluation is common in this domain, modest improvements (e.g., 1.5 % for the cascaded design over parallel) would benefit from confidence intervals to rule out noise.

### Trivial

6. **Memory bank growth over long videos.** The paper states memories are inserted "without removing any existing memories." For very long videos (960+ frames at 3.2 FPS) the memory bank becomes large, and the paper does not discuss the resulting computational cost of cross-attending over a growing memory. A brief note on this practical consideration would be helpful.

## Nice-to-Haves

- **Computational analysis**: Adding runtime (per frame), peak GPU memory, and total inference time for ART‑STVG vs. a representative baseline on a long video would substantiate the claimed advantage in avoiding computational bottlenecks.
- **Failure case / qualitative analysis**: A brief discussion of where ART‑STVG still underperforms (e.g., on 5‑min videos m.tIoU is only 15.0 %) would strengthen the paper's presentation.
- **Code release**: The paper states code and models will be released, which will address many reproducibility concerns.

## Removed Points

These points from the inputs were removed or demoted after verification against the paper:

1. **"m.tIoU bounded by original event length" argument** (Critical Issue 3, part): The harsh critic claimed that if the original 20‑second interval is used in longer videos, the m.tIoU "numerator (intersection) would be limited by the short ground‑truth interval." This is incorrect — tIoU = intersection/union, not intersection/video_length, and a perfect prediction achieves 1.0 regardless of ground-truth length. Removed as factually wrong.

2. **"Overstates computational bottlenecks without runtime comparison"** (Section notes): A fair observation but the paper's claim about computational bottlenecks is made in the Introduction as motivation for the autoregressive design, not as a measured result. The paper does not claim to benchmark runtime, so this is a scope-expansion criticism. Demoted to Nice-to-Have (computational analysis suggestion).

3. **Generic concerns about confounders / speculation without paper evidence**: The harsh critic's framing includes area-of-concern sweeps (e.g., "could the metric be measuring a proxy?"). These lack concrete anchors in the paper and are removed per the filtering rules.

## Novel Insights

None beyond the paper's own contributions. The paper itself is the first to identify the gap between short-form STVG research and long-video applications, and the review surfaces no deeper insight that the paper does not already articulate.

## Suggestions

1. **Document baseline inference protocol in full.** For each compared method, state the number of frames input at inference, any subsampling/windowing strategy, GPU configuration, and modifications to the original codebase. If official implementations were used as-is, confirm this explicitly.

2. **Specify how per-frame start/end probabilities become a temporal interval.** Add 2–3 sentences in §3.2 or §3.4 describing the inference-time aggregation (e.g., argmax over start probabilities for start timestamp, argmax over end probabilities for end timestamp, or a threshold-based procedure).

3. **Clarify dataset annotation rules.** State whether the original temporal boundaries from the 20‑second HCSTVG-v2 clips were preserved or re-annotated for the LF‑STVG benchmarks.

4. **Specify the similarity metric** used for spatial memory selection (and any threshold for temporal boundary detection) in §3.3.

5. **Add error bars** (3 seeds) for the main results and key ablations, especially where improvements are modest (e.g., cascaded vs. parallel, Table 4).

## Score and Decision

The paper introduces a well-motivated new problem (LF‑STVG), proposes a clean and sensible autoregressive architecture with selective memory, and backs it with extensive experiments showing large and consistent improvements. The weaknesses are in documentation completeness, not in the soundness of the method or the validity of the core findings. With the evaluation protocol and inference details clarified, the paper would make a solid contribution to the field.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
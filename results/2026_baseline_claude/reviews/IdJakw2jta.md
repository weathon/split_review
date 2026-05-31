Now I have read the full paper. Let me write a thorough review.

---

## Summary
This paper introduces **Long-Form Spatio-Temporal Video Grounding (LF-STVG)**, a new problem setting extending the conventional short-form STVG (videos of ~20 seconds) to long-form videos (1–5 minutes). To address it, the authors propose **ART-STVG**, an autoregressive transformer that processes video frames one at a time, augmented with spatial and temporal memory banks with learned selection strategies, plus a cascaded spatial-to-temporal decoder design. Five new evaluation benchmarks (LF-STVG-1min to 5min) are created by extending HCSTVG-v2 validation sets, and ART-STVG substantially outperforms all existing STVG methods on these benchmarks while remaining competitive on short-form STVG.

---

## Strengths

- **Novel and practically significant problem framing.** Being the first work to systematically address LF-STVG is a genuine contribution. The gap between the ~20-second videos in academic benchmarks and real-world surveillance/retrieval scenarios (minutes to hours) is well-motivated. Figure 2 compellingly illustrates that all existing methods degrade monotonically with video length while ART-STVG degrades less severely.

- **Sound empirical gains across five benchmarks.** ART-STVG consistently outperforms the best prior method (TA-STVG) across all five LF-STVG settings (m.tIoU/m.vIoU improvements of 0.7/0.9, 6.5/5.1, 9.1/6.8, 6.2/4.9, 7.3/5.5 pp for 1–5 min respectively). The gains grow with video length, directly validating the design philosophy of streaming/autoregressive processing. Table 6 further shows that even when all competitors are retrained on 40-second videos, ART-STVG maintains clear leadership.

- **Ablations clearly isolate each design choice.** Tables 2–5 individually justify selective temporal memory (+13.4 pp m.tIoU vs. using all memories), selective spatial memory (+0.9 pp beyond using all memories), the cascaded vs. parallel decoder design (+1.5 pp), and the optimal hyperparameter N_s = 32. The ablation structure is disciplined and each decision is supported.

- **Competitive short-form STVG performance.** Despite being designed for streaming long-form inference, ART-STVG achieves 59.2%/39.2% m.tIoU/m.vIoU on the HCSTVG-v2 short-form benchmark, outperforming all methods except TA-STVG (60.4%/40.2%). This suggests the approach does not sacrifice short-form capability.

- **Principled and elegant temporal memory selection.** Adapting TextTiling (Hearst 1997) to segment the temporal memory into events using cosine similarity of adjacent query states is conceptually clean and demonstrably effective: using all temporal memories actually *hurts* performance vs. no memory (9.6 vs. 16.7% m.tIoU), making the selective strategy essential and well-motivated.

---

## Weaknesses

### Fatal
None.

### Major

1. **Autoregressive baseline is consistently weaker than existing non-autoregressive methods at shorter durations.** On LF-STVG-1min, the memory-free baseline achieves 30.1%/19.7% m.tIoU/m.vIoU—significantly behind TA-STVG (38.4%/25.2%) and all other competitors. This indicates the autoregressive architecture is not inherently superior at 1-minute scale; the memory banks are compensating for an architectural disadvantage. The paper's framing suggests the streaming design is the core advantage, but the ablations show it is the memory that is doing the heavy lifting. This framing mismatch should be addressed.

2. **Evaluation restricted to a single extended dataset.** All LF-STVG results come from extensions of HCSTVG-v2 validation (2,000 samples from a single dataset of multi-person indoor/outdoor scenes). VidSTG (average 35 seconds) was not extended, nor was any truly long-form dataset employed. Conclusions about LF-STVG generality are limited to one domain. Given the paper positions this as the first LF-STVG study, demonstrating robustness on a second domain would substantially strengthen the claim.

3. **Training set is never extended to long-form videos in the primary experiments.** All main comparisons train exclusively on 20-second videos. The LF-STVG extension covers only the validation set. This means no method—including ART-STVG—is ever supervised on long-form examples, and the performance gap may reflect differences in how gracefully each architecture extrapolates rather than a fundamental capability advantage. Tab. 6 (training on 40-second clips) shows all methods improve, but ART-STVG is the only one with an LF-compatible design. A training set extended to, e.g., 3 minutes would be the strongest possible evaluation.

### Minor

1. **Memory bank growth is unbounded.** The memory bank size grows with the number of processed frames (each frame's query is added to the bank without eviction). For very long videos (e.g., hours), this creates a potential scalability issue. While the paper focuses on 1–5 minute videos and this may not be immediately problematic, analysis of memory bank size vs. inference time and GPU memory would be informative.

2. **Temporal grounding per-frame output semantics are ambiguous.** The temporal head outputs per-frame start/end *probabilities* (h_i ∈ ℝ²). How these per-frame probabilities are aggregated into a final temporal segment prediction (start/end timestamps) across all frames is not described in the main text. Understanding this post-processing is important for assessing reproducibility.

3. **Cascaded design improvement is modest.** The cascaded vs. parallel design yields +1.5%/+1.4% m.tIoU/m.vIoU (Table 4). While positive, this is a small margin relative to the overall gains from the memory system, and the claim that this is a key contribution of the paper seems slightly over-stated relative to the evidence.

### Trivial

None worth noting.

---

## Nice-to-Haves

- A qualitative failure analysis showing when ART-STVG struggles (e.g., target that never reappears after the grounded tube, or very sparse appearance of the target across a 5-minute video) would help characterize remaining challenges.
- An inference speed/memory comparison vs. existing methods to make the computational bottleneck claim concrete (e.g., GPU memory usage at 1-min vs. 5-min video length for all-frames processing vs. streaming).

---

## Novel Insights

The paper's most novel insight is that the *temporal memory selection strategy* (event-boundary detection via adjacent-query cosine similarity) is crucial not just for efficiency but for correctness: adding all temporal memories from a long video actively *hurts* performance compared to no memory at all (9.6% vs. 16.7% m.tIoU), because long videos contain multiple distracting events. This is a non-obvious and practically important finding that could inform memory-augmented architectures in other long-video understanding tasks. The cascade from spatial to temporal decoder (RoI-pooling the spatial prediction to focus temporal motion features on the target region) is also a clean and transferable design pattern.

---

## Suggestions

1. Add per-frame memory bank size statistics (average entries at 1min, 3min, 5min) alongside a GPU memory / inference-time table to quantify scalability.
2. Clarify the post-processing step that converts per-frame start/end probabilities into a final temporal segment—this is necessary for reproducibility.
3. Extend HCSTVG-v2 *training* set to at least one longer duration (e.g., 1 or 2 minutes) for a primary experiment, as this directly tests whether models trained on LF data benefit further.
4. Consider including VidSTG (even if only a small extended validation split) to demonstrate cross-dataset generalization of LF-STVG.
5. Rephrase the paper's framing to more accurately reflect that the *memory* (not the autoregressive architecture alone) is the core performance driver, noting the baseline underperforms existing methods at 1-minute.

---

## Score and Decision

The paper tackles a well-motivated and practically important problem (LF-STVG), proposes a technically sound method with selective memory banks that are convincingly ablated, creates new benchmark data, and demonstrates consistent empirical advantages. The core weaknesses—single dataset evaluation, training-evaluation length mismatch, and the fact that the base autoregressive framework without memory underperforms existing methods—are real concerns but do not invalidate the contribution. For a first exploration of a genuinely new problem setting with competitive overall results, this is a solid borderline-accept paper.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
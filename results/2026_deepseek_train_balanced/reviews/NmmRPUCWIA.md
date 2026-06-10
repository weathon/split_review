## Summary

This paper proposes Free Video-LLM, a training-free framework that reduces visual token count during video LLM inference by using the input prompt to guide both temporal frame selection (selecting frames most similar to the prompt embedding) and spatial RoI cropping (cropping a region of interest from each frame based on prompt-similar token distributions). The temporal component selects frames via CLIP cosine similarity between pooled frame features and the prompt; the spatial component computes a bounding box from the mean spatial position of top-K prompt-similar tokens. Experiments on MSVD-QA, MSRVTT-QA, ActivityNet-QA, and TGIF-QA show competitive accuracy at 1026–2600 tokens versus 2304–3680 tokens for prior training-free methods, with pre-filling latency reduced to 0.578s (vs. 0.878–1.583s).

## Strengths

- **Prompt-guided dual sampling (temporal + spatial) is a clean, novel idea for token reduction in training-free video LLMs.** The decoupled design uses the CLIP text encoder to compute prompt features and applies cosine similarity at both the frame level (to select prompt-relevant frames) and the spatial patch level (to crop prompt-relevant regions). This differs from prior work (IG-VLM uses composite grids, FreeVA uses uniform temporal aggregation, SlowFast-LLaVA uses dual streams without prompt conditioning). The temporal ablation provides clean evidence: prompt-guided temporal sampling (75.0) outperforms uniform sampling (71.7) at the same 3-frame/864-token budget on MSVD.

- **Substantial inference speed gains with maintained accuracy.** Table 5 (reported in text) shows the method achieves 0.578s pre-filling latency and 20.4 TPS on a V100 GPU, versus IG-VLM (0.878s, 14.9 TPS) and SF-LLaVA (1.583s, 11.6 TPS) — while using 2,648 tokens vs. 3,456–3,680. Accuracy on benchmarks like MSVD-QA (76.8/4.0 with 1026 tokens) is competitive with FreeVA (73.8/4.1 with 2304 tokens) and IG-VLM (73.0/4.0 with 3456 tokens on TGIF-QA).

- **Component-level ablation provides decomposition of contributions.** Tables 6–8 (described in text) isolate temporal sampling, spatial RoI cropping, and RoI ratio effects. The temporal ablation (uniform 71.7 → prompt-guided 75.0 at same token count) is particularly clean and directly supports the core claim. The RoI ratio analysis (diminishing returns beyond α=0.6) offers a practical design guideline.

- **Consistency across two model scales (7B and 34B).** The efficiency gains hold at both LLaVA-v1.6-7B and LLaVA-v1.6-34B, showing the approach is not brittle to model capacity.

## Weaknesses

### Fatal

None.

### Major

- **The "hybrid" temporal ablation comparison is confounded by token budget.** The paper (line 190) compares uniform temporal sampling (3 frames, 864 tokens, 71.7), prompt-guided temporal sampling (3 frames, 864 tokens, 75.0), and a "combination" of uniform + prompt-guided (6 frames, 1728 tokens, 77.2). The third condition uses twice as many frames and twice as many tokens, so the gain from 75.0→77.2 could entirely reflect the additional information from more frames. This experiment does not support the claim that a hybrid approach is beneficial. To test synergy, the comparison would need to hold token count fixed (e.g., 3 prompt-guided + 3 uniform vs. 6 prompt-guided at the same total token budget).

- **No variance or uncertainty reported despite small performance gaps and GPT-based evaluation.** The evaluation uses GPT-3.5-Turbo-0125 for scoring, which has known variability. Accuracy differences between the proposed method and baselines are sometimes very small (e.g., 78.2 vs. 78.1 on MSVD; 65.6 vs. 64.1 on MSRVTT). Single-point estimates without confidence intervals or multiple runs make it impossible to determine whether these differences are meaningful. This is particularly important because the paper's efficiency claim (fewer tokens, comparable accuracy) depends on the "comparable" part being statistically credible.

### Minor

- **The spatial RoI method has several unaddressed limitations.** (1) The bounding box center is computed as the mean of top-K token positions (Eq. 6). If prompt-relevant content is spatially distributed across multiple disjoint regions (e.g., "What color is the left woman's shirt and the right woman's shoes?"), the mean center would fall in empty space between them, cropping nothing useful. (2) Out-of-bounds handling is not described — when the computed RoI center is near a frame boundary, the sqrt(α)H × sqrt(α)W box will extend beyond the feature map. (3) The RoI is constrained to the same aspect ratio as the original frame (Eq. 5), which is not justified. These are not necessarily fatal (the method may still work well on average across standard benchmarks), but the paper should explicitly discuss when and why the RoI strategy would succeed or fail.

- **The frame selection mechanism is underspecified.** The paper states (line 119): "We sample the frames based on the similarities so as to maintain the most related frames to the prompt and discard the useless ones." It does not specify whether the number of selected frames is a fixed K per video, a fixed K per dataset, or determined by a similarity threshold. The ablation uses 3 frames, suggesting a fixed budget, but the main results use varying token counts (1026 and 2600), making it unclear how many frames are selected and how. This is a reproducibility gap.

- **Temporal sampling uses global average pooling over spatial dimensions, potentially diluting small-object signal.** Frame-level features are obtained via global average pooling over spatial dimensions (F_V ∈ ℝ^{T×D}, line 113). A frame containing a small but prompt-relevant object (e.g., an apple in a busy scene) would have its signal diluted by surrounding content. Since temporal sampling is applied first and errors propagate, this could cause the method to miss frames where the key information is spatially localized. The paper does not discuss this or test such scenarios.

- **Spatial ablation lacks comparison against trivial baselines at the same token budget.** The spatial ablation compares prompt-guided temporal + RoI (74.9, 513 tokens) against prompt-guided temporal + adaptive average pooling (73.8, 513 tokens). While this is a valid baseline at the same token count, it would be more informative to also compare against a non-prompt-guided spatial reduction at the same token count (e.g., center cropping or uniform grid subsampling to 513 tokens). Without this, it is unclear how much of the RoI benefit comes from prompt guidance versus simply having fewer tokens processed at the same resolution.

- **The conclusion overstates performance relative to the evidence.** The paper claims the method "not only matches but often exceeds the performance of current state-of-the-art video LLMs." The actual results show approximate parity with occasional small advantages (e.g., 78.2 vs. 78.1 on MSVD; 65.6 vs. 64.1 on MSRVTT), and the clear advantage is in efficiency, not accuracy. The claims should be calibrated to reflect that the method is competitive rather than superior.

### Trivial

- The spatial RoI formula (Eq. 5) uses sqrt(α)·H and sqrt(α)·W to achieve area α·H·W. This is correct but constrains the RoI to the original aspect ratio — a brief justification would be helpful.

## Nice-to-Haves

- Testing on a benchmark requiring temporal reasoning (e.g., NextQA, EgoSchema) would strengthen the claim that aggressive token reduction does not discard information needed for structured temporal reasoning.
- Testing with a generic/uninformative prompt (e.g., "Describe this video") would reveal how much of the efficiency gain is from prompt guidance versus discarding information.
- Testing on an additional base model (e.g., InternVL) would strengthen the claim that the approach is framework-agnostic.

## Removed Points

These points were raised by reviewers but removed after verification against the paper:

- **Tables are unreadable images / cannot be verified** → Removed. Tables are images that the PDF parser could not extract; the original submission contains them. This is a parser artifact, not a paper weakness.
- **Missing baseline: random cropping for spatial ablation** → Removed and demoted to Nice-to-have. The paper already compares against adaptive average pooling at the same token count, which is a reasonable baseline. Requesting additional baselines (random crop, center crop) is a strengthening suggestion, not a flaw.
- **The spatial RoI method has a structural flaw that limits generality** → Partially kept (demoted from Fatal/Major to Minor). The critic framed this as "structural" and "fatal," but the method demonstrably works on standard benchmarks. The issue is that limitations are not discussed, not that the method is broken.
- **"Method as described cannot handle spatially distributed relevant content"** → Kept but downgraded. This is a valid limitation that should be acknowledged, but it does not invalidate the positive results on standard benchmarks where relevant regions tend to be spatially contiguous.
- **Efficiency comparison is confounded because baselines use more tokens** → Removed. The paper's efficiency claim is precisely that it achieves comparable accuracy with fewer tokens. That the comparison involves different token counts is the point of the analysis, not a confound.
- **Criticism that a larger dataset or more models should be tested** → Removed. The evaluation covers four benchmarks and two model scales, which is adequate.

## Novel Insights

None beyond the paper's own contributions. The reviews surfaced known methodological concerns (ablation confounds, missing variance, underspecified implementation details) but did not contribute a novel synthesis or reinterpretation of the paper's findings.

## Suggestions

1. **Address the confounded hybrid ablation**: Either re-run the experiment with a controlled token budget (same total tokens, different frame selection strategies) or remove the claim about the hybrid approach being beneficial.
2. **Add variance reporting**: Run each experiment at least 3 times (or re-evaluate with different GPT calls) and report mean ± std. This is critical for interpreting the small performance differences.
3. **Specify the frame selection protocol**: Clearly state whether the number of selected frames is fixed per video, fixed per dataset, or threshold-based. Provide the actual K values used for the main results (1026 and 2600 token configurations).
4. **Acknowledge spatial RoI limitations**: Add a discussion of when the mean-of-top-K approach would fail (disjoint relevant regions, boundary effects) and describe how out-of-bounds coordinates are handled.
5. **Add a controlled spatial baseline**: Compare prompt-guided RoI against center cropping at the same token count to isolate the value of prompt guidance for spatial reduction.
6. **Calibrate claims in the conclusion**: Replace "not only matches but often exceeds" with "achieves competitive accuracy while using significantly fewer tokens."

## Score and Decision

**MY FINAL SCORE:** <score>4.0</score>
**MY FINAL DECISION:** <decision>Reject</decision>
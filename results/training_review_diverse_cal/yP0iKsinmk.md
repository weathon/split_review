Now I have all the information I need. Let me compose the final review.

## Summary

AdaFlow proposes a training-free method for long video editing that combines two innovations — Adaptive Attention Slimming (AAS) to reduce the KV sequence length in extended self-attention, and Adaptive Keyframe Selection (AKS) to adaptively pick representative frames based on DIFT-based content similarity. The method achieves joint editing of over 1,000 frames on a single A800 GPU, roughly 10× more than prior approaches, while also improving runtime and quantitative quality metrics. The paper additionally contributes LongV-EVAL, a benchmark of 75 one-minute videos with editing prompts.

## Strengths

1. **Demonstrated long-video editing at scale.** AdaFlow edits an average of ~1,117 frames per video on a single 80GB GPU (Table 1), an order of magnitude more than TokenFlow (~128 frames), FLATTEN (~32), and RAVE (~16). This directly addresses the memory bottleneck that has limited prior work to short clips.

2. **Adaptive Keyframe Selection is ablated and shown to improve quality in dynamic scenes.** Figure 4 provides a concrete ablation showing that AKS avoids blurring and artifacts during rapid content changes (e.g., a car entering the frame, a cat yawning), whereas uniform keyframe sampling produces visibly worse results. This validates one of the two proposed mechanisms.

3. **Training-free and computationally efficient.** The method uses off-the-shelf SD 2.1 and DIFT without additional training or test-time tuning. Table 1 reports 24 minutes average total inference time per video, roughly half that of the fastest baseline, while editing substantially more frames.

4. **New benchmark for long video editing.** LongV-EVAL provides 75 one-minute videos across diverse scenes with three high-quality prompts each, filling a gap in evaluation resources for long-video editing. The benchmark is used in all quantitative comparisons (Table 1) and user study (Table 2).

5. **Consistent quantitative superiority.** AdaFlow achieves the best scores in Video Quality (DOVER), Object Consistency (DINO), and Semantic Consistency (CLIP) among five baselines (Table 1). A user study with 18 participants (Table 2) confirms human preference for AdaFlow on both video quality and temporal consistency.

## Weaknesses

### Major

1. **Missing ablation of Adaptive Attention Slimming (AAS).** AAS is presented as a core contribution — the mechanism that "greatly alleviates the computation burden" without harming quality — yet no controlled experiment isolates its effect. The paper provides an ablation for AKS (Figure 4) but not for AAS. Without comparing full ESA (no slimming) vs. AAS at matched keyframe counts, or AAS vs. random token pruning at the same compression ratio, it is impossible to determine whether the similarity-based pruning actually preserves quality or whether the gains come entirely from AKS or the overall pipeline design. The claim that "not all tokens… hold equal importance" and that AAS preserves quality while reducing computation remains unvalidated at the component level. This is a significant gap because AAS is named as a core contribution alongside AKS.

2. **No reported peak GPU memory consumption.** The paper's central practical claim is enabling editing of 1000+ frames on a single A800 (80GB) GPU — a problem explicitly framed as a *memory* bottleneck (Section 1: "extremely high GPU memory footprint becomes a bottleneck for long video editing"). Yet Table 1 reports only inference time ("Mins/Video"), not peak memory usage. While the fact that 1,117 frames fit in 80GB is implicit evidence, explicit memory numbers for AdaFlow and for each baseline (including per-chunk memory for chunked baselines) are needed to quantify the claimed advantage and enable meaningful comparison. A method could be slower but achieve the memory reduction necessary for long videos; without memory figures, the primary engineering claim is only partially supported.

### Minor

1. **Baseline comparison confound from chunking.** TokenFlow, FLATTEN, and RAVE are adapted to long videos by segmenting into chunks (128, 32, 16 frames respectively). The chunk sizes are reported as chosen "based on their computational resource usage" without explicit justification of the specific constraints or a demonstration that these are the maximum feasible sizes. Chunk boundaries may produce visible seams or inconsistencies that the metrics (frame-to-frame DINO/CLIP similarity) might penalize differently than AdaFlow's joint approach. The comparison therefore somewhat conflates the advantages of joint editing with the specific proposed mechanisms.

2. **AAS source-similarity assumption unvalidated.** AAS uses DIFT features from the *source* video to decide which KV tokens to retain during *edited* keyframe translation. The similarity between source frames is assumed to predict which tokens will be relevant after editing. This is a strong inductive bias: editing can change appearance (add objects, alter colors, change style), and tokens that were dissimilar in the source may become highly relevant in the edited domain. The paper provides no validation — e.g., comparing the set of tokens retained under AAS with the set of tokens that actually receive high attention in the *edited* ESA computed with full KV. Without this check, it is unclear whether AAS silently discards editing-relevant tokens in cases not captured by aggregate metrics.

3. **User study inherits the chunking confound.** The user study (18 participants, 20 sets) compares AdaFlow against the chunked outputs of baselines. The results should be interpreted as "AdaFlow is preferred under this particular comparison mode" rather than as a fundamental superiority judgment, since the baselines are not operating in their optimal long-video regime.

### Trivial

1. **DIFT extraction at t=0 needs clarification or correction.** The paper states (Section 5.2): "When extracting DIFT, we select the features corresponding to t=0 for each frame of the source video." In the original DIFT work, features are extracted after adding noise at a specific timestep t (typically t in [0.1, 0.7] of the normalized schedule). Using t=0 (no noise) is a departure from standard practice. The paper should clarify whether this is an intentional adaptation and why it remains effective, or correct a notation error.

## Nice-to-Haves

- Sensitivity analysis of AKS thresholds (0.75 for clip division, 0.6 for sliding window) to demonstrate robustness across different video content types.
- Breakdown of total computation time into precomputation (DIFT extraction, correspondence calculation), keyframe translation, and propagation phases, to give a clearer efficiency picture.
- Release of the generated editing prompts (if not already) to improve reproducibility of the LongV-EVAL benchmark.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The prompts are not released or exemplified, making it hard to judge their quality or diversity."* — This criticizes the release/availability status of benchmark data, which per hard rules is removed. The benchmark itself is presented as a contribution.
- *"The paper does not yet meet the bar for acceptance in its current form."* — This is the reviewer's opinion, not a factual weakness; the substance behind this opinion is captured in the Major weaknesses above.
- *"AKS threshold values (0.75, 0.6) appear arbitrary."* — This is a wish-list item for sensitivity analysis, not a structural flaw; moved to Nice-to-Haves.
- *"No analysis of token retention rate vs. number of keyframes."* — Similarly a sensitivity-analysis request, moved to Nice-to-Haves; the core impact on the central claim is secondary.

## Novel Insights

None beyond the paper's own contributions. The harsh critic correctly identifies the missing AAS ablation and absent memory numbers as the key gaps; no genuinely novel synthesis emerges beyond that observation.

## Suggestions

1. **Add a controlled ablation of AAS.** Fix AKS (use uniform sampling for simplicity) and compare full ESA vs. AAS at various token retention ratios (100%, 50%, 25%, 10% of original KV length). Report both quality metrics and peak memory (or maximum keyframe count reachable). This directly tests whether AAS preserves quality at the claimed compression levels.
2. **Report peak GPU memory** for each method on a set of fixed-length videos (e.g., 256, 512, 1024 frames). Show that AdaFlow stays within 80GB while baselines fail or require chunking. This would cleanly substantiate the central memory-efficiency claim.
3. **Validate the AAS assumption** by comparing, on a small set of edited keyframes, the top-k tokens selected by source-DIFT similarity with the top-k tokens receiving the highest attention in the edited ESA (computed with full KV). Show the overlap, or document failure cases.
4. **Clarify the DIFT timestep.** Either correct the notation from "t=0" to the actual timestep used or provide a methodological note explaining why t=0 was chosen and how it differs from the standard DIFT protocol.

**Evaluation Summary:**

- **Originality:** Good — the combination of AAS and AKS is a novel approach to the memory bottleneck in long video editing. Using DIFT similarity for both tasks is a coherent design choice.
- **Importance:** High — enabling minute-long video editing on a single GPU is a practical and timely problem.
- **Claims:** Partially supported — the overall system works and achieves impressive results, but the component-level attribution for AAS is weakened by the missing ablation, and the memory-efficiency claim lacks direct memory consumption evidence.
- **Soundness:** Adequate but incomplete — the system-level comparisons are solid, but the experimental design lacks controlled isolation of the core technical contribution.
- **Clarity:** Good — the paper is well-structured, the figures are informative, and the writing is clear.
- **Value:** Positive — LongV-EVAL is a useful resource, and the method shows genuine practical potential. However, the evaluation gaps reduce confidence in the contribution claims.

The paper identifies a real and important bottleneck and proposes plausible mechanisms to address it. However, the evaluation is incomplete in two critical ways: (1) one of the two named contributions (AAS) is never ablated, making it impossible to attribute the quality–efficiency trade-off to the proposed mechanism, and (2) the central memory-efficiency claim lacks direct supporting evidence (peak GPU memory numbers). These gaps are addressable but significant enough that the paper does not yet meet the acceptance bar.

**MY FINAL SCORE:** <pineapple>5.5</pineapple>
**MY FINAL DECISION:** <orange>Reject</orange>
Now I have all the information I need. Let me construct the final consolidated review.

## Summary

ACDC proposes a zero-shot, training-free method that combines pre-trained autoregressive models (ARMs) with diffusion models (DMs) at inference time. The key idea is to use a pre-trained DM (via SDEdit) to locally correct visual artifacts in ARM-generated frames, coupled with an LLM-based memory module that summarizes prior context to condition the DM correction. Experiments on story generation (Show-o, UIO-2) and autoregressive video generation (LWM) show consistent improvements across multiple metrics.

## Strengths

- **Zero-shot integration of pre-trained ARMs and DMs without fine-tuning**: ACDC works with off-the-shelf models across three ARMs (Show-o, UIO-2, LWM) and two DMs (Stable Diffusion, AnimateDiff), showing consistent improvements in Tables 1 and 3. This avoids expensive retraining or architectural modification required by prior works (SEED-X, Pandora, Transfusion).
- **LLM memory module demonstrably preserves global context in story generation**: The ablation in Table 2 shows ACDC with memory improves Frame Consistency (0.888 vs. 0.835) and CLIP similarity (30.85 vs. 29.43) over ACDC without memory, directly supporting the claim that maintaining global context matters for the diffusion correction.
- **Consistent quantitative improvements across tasks and metrics**: For story generation, ACDC raises Show-o's Frame Consistency from 0.8211 to 0.9062 (▲10.4%). For video generation, ACDC improves LWM's Subject Consistency from 0.7369 to 0.7622 (▲3.43%) and Aesthetic Quality from 0.4105 to 0.4406 (▲7.33%).
- **Architecture-agnostic design validated across diverse model families**: ACDC works with both discrete-token ARMs (Show-o, UIO-2, LWM) and both image/video DMs (SD, AnimateDiff), demonstrating generality beyond a single model pair.
- **Physical constraint incorporation without additional training**: Figure 5 demonstrates that ACDC can leverage DM controllability (inpainting) to correct physically implausible ARM outputs (e.g., a rabbit with three ears), a unique capability not present in standard ARM pipelines.
- **Ablation on correction frequency provides insight into error propagation**: Table 2 ablates the number of corrected frames (0, 2, 4, 6) and shows that even partial correction improves results, while full correction yields the best outcomes.

## Weaknesses

### Fatal

None.

### Major

- **FID computed against another generative model's outputs as pseudo-ground truth is not a valid reference distribution.** The paper uses SDXL-lightning–generated images as pseudo-ground truth for FID (Table 1) and then evaluates SD v1.5 against this same reference. Since SD v1.5 and SDXL are different models, and the "ground truth" is itself a generative sample, the FID ranking is ambiguous — it conflates distributional distance with model preference. The authors acknowledge this concern in the text (line 192: "this can be partly attributed to the fact that we consider SDXL-generated images as ground truth"), but this does not resolve the issue. The other metrics (Frame Consistency, CLIP similarity, ImageReward) are not affected by this problem, so the core claim does not collapse, but the FID column in Table 1 should be interpreted with strong caution or removed.

- **The video experiment does not ablate the memory module, and the single-prompt setting makes the memory module's role unclear.** In the video setup (Eq. 123–125), a single prompt is used for all 32 frames. The LLM memory module therefore receives the same prompt repeatedly — it has no meaningful causal summarization to perform. Yet the paper treats the memory module as a core ACDC component throughout. The ablation in Table 2 covers only story generation (where multiple distinct prompts exist). Without a video ablation that compares ACDC with and without the memory module, the reader cannot determine whether the video improvements come from the SDEdit correction alone or from the full memory-conditioned system. This oversells the generality of the "memory" component.

- **Video experiment corrects only 16 of 32 frames without comparison to correcting more frames (or all frames).** The paper acknowledges that T2V models have length constraints (line 127), but does not explore whether a sliding-window correction strategy (e.g., correct frames 1–16, then frames 9–24, then 17–32) would yield further improvements. Without this comparison, the extent to which ACDC reduces error propagation across the full 32-frame sequence — as opposed to simply cleaning up the first half — is less clear than claimed.

### Minor

- **No human evaluation for subjective quality claims.** The paper argues that ACDC improves "coherence" and "quality" — properties inherently about human perception. While automated metrics (frame consistency, CLIP similarity, VBench scores) provide some support, they are not sufficient substitutes for human judgment, especially given the questionable FID baseline. Adding pairwise human preference judgments would substantially strengthen the evidence for the paper's central claim.

- **Synthetic benchmark generated by GPT-4o-mini with no validation against existing story generation benchmarks.** The 1k-story dataset is constructed via self-instruct with 10 seed examples (line 185). The dismissal of ChangeIT as "out-of-distribution" is stated without supporting analysis. While this does not invalidate the results (the paper's real contribution is the method, not the dataset), it makes it difficult to assess how results would transfer to more realistic story-generation tasks.

- **No comparison against other inference-time correction methods.** The paper compares ARM → ARM+ACDC and shows SD v1.5 as a baseline, but does not compare to alternatives such as frame-wise diffusion refinement without memory (partially ablated as "ACDC #6 w/o memory" but only in story generation), or post-hoc frame polishing with a single DM call. Adding such a comparison would help isolate the benefit of the memory module and re-encoding step.

- **Computational overhead is not discussed.** Each correction step adds a full diffusion sampling call and token re-encoding. For a paper positioning ACDC as a practical correction technique, a brief note on runtime (e.g., frames per second relative to baseline) would be useful for readers evaluating deployment feasibility.

### Trivial

- The exact value of the SDEdit hyperparameter \(t'\) used in experiments is not reported — only ranges are given (0.4–0.5 for images, 0.4–0.6 for video). Specifying the exact value would improve reproducibility.

## Nice-to-Haves

- Testing with additional ARM/DM combinations beyond the three ARMs and two DMs tested would further strengthen the architecture-agnostic claim, though the current set is already adequate as a proof of concept.
- A sliding-window correction strategy for video (e.g., correct frames 1–16, then 9–24, then 17–32) would more cleanly quantify how much error propagation ACDC mitigates versus simply cleaning early frames.

## Removed Points

- **Theorem 4.1 not in main text**: Removed per rule — the parser strips appendix sections; the theorem exists in the original submission.
- **Architecture-agnostic claim needing more model combinations**: Downgraded from a weakness to Nice-to-Haves — testing three ARMs and two DMs is already a solid demonstration; asking for more combinations is scope creep.
- **"The claim would be stronger with at least one additional combination"**: Moved to Nice-to-Haves — insufficient breadth to count as a weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an interpretation of the results that the paper itself missed.

## Suggestions

1. **Replace or supplement the FID column** in Table 1 with a metric not requiring a reference distribution, or use real images as ground truth. If FID must be kept, clearly state in the table caption that the reference set is SDXL-generated and discuss the implications.
2. **Ablate the memory module in the video setting** (Table 3). Add a row showing LWM + ACDC without the memory module (i.e., SDEdit with the raw single prompt) so readers can assess whether the memory module contributes anything beyond plain SDEdit for single-prompt video.
3. **Compare against a sliding-window correction** in the video experiment: if AnimateDiff has a 16-frame window, apply ACDC in overlapping windows (e.g., correct frames 1–16, then frames 9–24, then 17–32) and report whether this further improves metrics.
4. **Add a human evaluation** (e.g., pairwise preference on Amazon Mechanical Turk, 50–100 samples per condition) comparing ADC-corrected outputs to baseline ARM outputs on story coherence and video naturalness. If resources are limited, even a small study would add credibility.
5. **Report the exact \(t'\) value** used in each experiment and discuss sensitivity to this hyperparameter (even briefly).
6. **Add a brief computational cost analysis** — e.g., wall-clock time per frame for ARM vs. ARM+ACDC, or number of DM forward passes per generated frame.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
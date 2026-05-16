Now I have all the information I need. Let me synthesize the final review.

## Summary

This paper investigates when and how to introduce image data during VLM pre-training, challenging the standard two-stage pipeline (fully pre-train LLM, then add vision). Training ~300 models across two scales (79M and 1.4B), the authors study the timing of image introduction, the optimal image-text ratio, and the interaction with instruction fine-tuning. The main finding is that introducing visual tokens at ~80% of text-only pre-training (during the cooldown phase) yields better downstream performance than the standard approach of starting from a fully pre-trained model.

## Strengths

1. **Large-scale, systematic ablations.** The paper trains approximately 300 models across two parameter scales (79M and 1.4B), varying checkpoints, image-text ratios, and fine-tuning epochs. This level of empirical thoroughness is rare in VLM literature and provides a useful foundation for practitioners (Sections 2, 3).

2. **Identification of scale-dependent optimal image-text ratio.** The paper finds that for a 1B model, 10–20% of tokens should be visual, while smaller 79M models prefer larger visual fractions (abstract, intro). This goes beyond prior work (e.g., MM1 tests only up to 33% text; DeepSeek-VL uses a fixed 70% text) and has practical implications for data mixing at different model sizes.

3. **Disentangling instruction fine-tuning from pre-training.** The paper demonstrates that mixing instruction-tuning data during the image-text pre-training phase hurts downstream performance, while separate instruction fine-tuning (up to 4 epochs) improves vision-language tasks at modest text-task cost (intro). This clarifies a common conflation in VLM training pipelines.

4. **Reproducible design using public checkpoints.** The experiments leverage publicly available DCLM-1B checkpoints at 20%, 40%, 60%, and 80% of text pre-training, enabling straightforward replication without training language models from scratch (Section 2.1.1).

## Weaknesses

### Fatal
None.

### Major

1. **Confounded comparison between 80% and 100% checkpoints (Section 3.1, Figure 4).** The paper's central claim—that introducing images at 80% of text-only pre-training outperforms the fully pre-trained (100%) baseline—is undermined by a learning-rate schedule confound. For intermediate checkpoints (20%–80%), the paper resumes the cosine schedule from its current value. For the 100% checkpoint (and 0%), "the learning rate would be too low," so the authors adopt a separate linear warmup-cosine decay with a maximum learning rate of 3×10⁻³. This changes two variables simultaneously: the amount of text-only pre-training *and* the LR dynamics during image-text training. The observed degradation at 100% could be caused by the re-warmup itself (a known instability when restarting a fully converged model) rather than by the timing of image introduction. The paper acknowledges this issue (line 128: "the learning rate schedule is different and could affect the results") and marks the 100% points with hollow circles, but still draws the conclusion that "continued training is preferable to re-training a 100% fully pre-trained text model" from confounded evidence. A controlled comparison—e.g., applying the same re-warmup to all checkpoints—is needed to isolate the effect of timing. This directly weakens the headline claim in the abstract and conclusion.

### Minor

2. **No measure of variability or statistical significance.** The paper trains ~300 models but reports all results as single points without error bars, confidence intervals, or multiple seeds. Given the modest performance differences (e.g., the headline 2% improvement), it is impossible to assess which differences are reliable. While running multiple seeds for 300 models is expensive, at minimum the core 80% vs. 100% comparison should include variance estimates.

3. **Text dataset mismatch between stages.** The text-only pre-training uses DCLM-Baseline + StarCoder + ProofPile, while the image-text pre-training stage replaces ProofPile with MathPile (Section 2.1.2). The paper claims this "ensure[s] continuity," but it is a genuine change in data composition that could affect results, especially on reasoning-heavy tasks.

4. **Frozen vs. trained image encoder not specified for main experiments.** Section 2.1.2 discusses both options ("The vision encoder can be kept frozen... or trained end-to-end") but does not state which choice was used in the main experiments reported in Section 3. This design decision affects how image-text ratio results should be interpreted.

### Trivial

- The aggregate "stable score" metric (average accuracy minus random baseline) is described but the exact set of tasks and their random baselines are not listed in the main text.

## Nice-to-Haves

- Running a controlled ablation where the same re-warmup schedule is applied to the 80% checkpoint (not just the 100% checkpoint) would cleanly isolate the timing effect.
- Reporting variance (at least 2–3 seeds) for the 80% vs. 100% comparison would substantially strengthen the empirical contribution.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Missing Sections 3.2–3.5**: The reviewer faults the paper for missing experimental sections, but these are parser artifacts. The original submission contains these sections (the paper explicitly references results from Sections 3.2–3.5 in the abstract, intro, and conclusion). Following the instructions, parser-stripped content is not a paper flaw.
- **LR handling for 0% is confusing/allegedly wrong**: The reviewer claims "at 0% the LR is at its peak after warmup." This is incorrect—at 0% (model initialization), no training has occurred, so the LR is near 0 (pre-warmup). The paper's claim that the LR "would be too low" for the 0% checkpoint is correct.
- **Scale dependence claim unsubstantiated**: The reviewer says no 79M results are shown, but these results are reported in Sections 3.2 and 3.3, which were stripped by the parser. The paper's claims about scale-dependent ratios are made with reference to these sections.
- **"Not yet released / cannot be verified" concerns**: Any such framing about model/dataset availability is removed per instructions; the paper's cited models and datasets are assumed to exist.

## Novel Insights

Beyond the paper's own contributions, the reviews do not surface genuinely novel observations that the paper itself does not make. The key insight confirmed by meta-review is that the LR-schedule confound is the paper's most significant vulnerability, and that the paper's other findings (ratio, instruction timing) are likely more robust because they do not depend on the same comparison.

## Suggestions

1. **Control the LR schedule across all checkpoints** for the timing experiment: apply the same re-warmup cosine schedule to every checkpoint (including 80%). This would isolate the effect of text-only pre-training length from restart dynamics and either confirm or refute the headline claim.
2. **Add variance estimates** (at minimum 3 seeds) for the critical 80% vs. 100% comparison so readers can assess whether the reported 2% improvement is statistically significant.
3. **Explicitly state whether the vision encoder is frozen or trained** in the main experiments (Section 2.1.2), and note any interaction this has with the reported image-text ratio findings.
4. **Either use ProofPile consistently across both stages** or justify the switch to MathPile and discuss its potential impact on results.

## Score and Decision

The paper addresses a timely and practically important question with impressive experimental scale (~300 models, two parameter scales). The findings about optimal image-text ratio and instruction fine-tuning timing are useful contributions. However, the central claim about when to introduce images during pre-training is weakened by a confound between checkpoint timing and learning-rate schedule that the paper acknowledges but does not resolve. This prevents the paper from being a strong accept, but the remaining contributions are sufficient for borderline acceptance.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
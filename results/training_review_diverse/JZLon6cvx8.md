Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper proposes Storybooth, a training-free approach for multi-subject consistent storyboard generation. The method combines (1) LLM-based layout planning to localize subjects across frames, (2) a bounded cross-frame self-attention layer with dropout to reduce inter-character attention leakage, and (3) a cross-frame token-merging layer (with a negative unmerging variant) to align fine-grain details. The core insight—diagnosing self-attention leakage as the root cause of multi-character inconsistency in cross-frame attention—is a genuine contribution.

## Strengths

- **Novel diagnosis of inter-character self-attention leakage.** Section 3 provides a clear analysis showing that cross-frame self-attention (used in StoryDiffusion, ConsiStory) causes tokens from one character (e.g., dog) to attend to tokens from another (e.g., cat), producing feature mixing. This insight directly motivates the bounded attention design and differentiates the paper from prior training-free approaches that overlook the problem.

- **Well-motivated technical pipeline combining layout planning, bounded attention, and token merging.** The bounded self-attention (Section 4.2) is a clean solution to the identified leakage problem. The dropout-based relaxation (β_d) that preserves image quality while reducing leakage is empirically motivated (Fig. 5). The cross-frame token merging (Section 4.3) and negative unmerging (Section 4.4) for improving fine-grain consistency and pose variance are technically interesting extensions.

- **Training-free, fully automatic pipeline.** The use of multi-modal chain-of-thought LLM reasoning with in-context exemplars for layout planning (Section 4.1) enables the entire pipeline to operate without any per-subject training, learned detectors, or human annotation. This is a genuine practical advantage over optimization-based personalization methods.

- **Inference-time comparison under controlled conditions.** All methods are benchmarked on the same hardware (single H100) and base model (SDXL), providing a fair speed comparison. The 8.7s inference time (vs. 6.5s for StoryDiffusion, ~5–7.5 min for optimization-based methods) is clearly reported and contextualized.

## Weaknesses

### Fatal
None.

### Major

- **The LLM layout planning subroutine is not evaluated.** The method's bounded attention and token merging both depend entirely on accurate per-frame bounding-box layouts from the LLM. The paper provides no evaluation of layout quality—no accuracy metrics, no analysis of how errors cascade into final images, no discussion of robustness to layout failures. For a claimed training-free method whose main differentiator is being "fully automatic and zero-shot," this is the most significant evidential gap: the reader cannot assess whether the method is reliable or brittle. Because the paper already demonstrates working outputs, this is not fatal, but it is the single issue that most limits confidence in the approach.

### Minor

- **Quantitative results lack error bars, standard deviations, and statistical significance tests.** Table 1 reports VQAScore and DreamSim comparisons across methods, but no variance or significance measures are provided. For generative evaluation where per-instance scores can be noisy, this makes it impossible to tell whether the reported improvements over baselines are statistically reliable or within the noise. This is a standard expectation for empirical papers in this area.

- **Multi-character evaluation dataset is not specified.** The paper states that "the storyboard prompt dataset from Tewel et al. (2024) is used for evaluating single-subject generation," but does not describe the multi-character evaluation dataset—how many prompts, how they were curated, or whether a new dataset was collected. This makes the quantitative results difficult to interpret or reproduce.

- **Ablation study is purely qualitative.** Figure 9 shows that removing each component degrades output quality (bear-lion mixing, bear color variation, reduced pose variance), which is informative, but the absence of quantitative ablations (e.g., DreamSim and VQAScore for each variant) means the reader cannot judge the relative importance of each component or confirm that trends generalize beyond the shown examples. Since the paper's contribution hinges on three distinct components, quantitative ablations would substantially strengthen the evidence.

- **Self-attention leakage is not quantified.** The analysis in Section 3 convincingly visualizes leakage (Fig. 3), but the paper does not report any quantitative measure of leakage (e.g., average cross-character attention weights). A simple metric would strengthen the motivation and provide a baseline for evaluating whether bounded attention reduces leakage as claimed.

- **Key hyperparameters lack sensitivity analysis.** Three parameters (β_d, α_positive=0.4, α_negative=−0.5) and two timestep ranges (1000–950, 950–600) are hand-picked with no sensitivity study. While these choices are plausible, their robustness is unknown. The paper would benefit from a sensitivity analysis on even a subset of prompts.

### Trivial

- The mapping of bounding-box masks to token grids at different UNet self-attention resolutions is not explicitly described (e.g., how H×W masks are rescaled to the feature resolution of each layer). The paper states masks are "flattened and reshaped to the number of tokens N for the corresponding self-attention layer," but details of the interpolation/rescaling are omitted, affecting full reproducibility.

## Nice-to-Haves

- A failure analysis showing cases where the LLM layout is incorrect and how the method degrades would improve credibility.
- Quantification of the self-attention leakage (e.g., mean cross-character attention) as a diagnostic metric.
- A parameter sensitivity study for β_d, α values, and timestep ranges.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **"Speed comparison is misleading"** (from Harsh Critic Point 3). The paper explicitly compares the 30× speedup against *optimization-based* methods (Dreambooth-LoRA, Textual Inversion) and separately reports 8.7s vs 6.5s for training-free methods (StoryDiffusion, ConsiStory). The claim is properly scoped and contextualized; there is no misleading framing.

2. **"Unfair comparison against StoryGen/SeedStory"** (from Harsh Critic's Section-by-Section notes). The paper explicitly groups baselines into three classes (subject-personalization, training-based autoregressive, training-free) and does not claim apples-to-apples comparison. These are included for comprehensive context, which is appropriate.

3. **"Figures not visible"** and **"Table image stripped"** (from Harsh Critic). These are parser-induced artifacts, not author errors. The original submission contains these figures and tables.

4. **"Human study details not reported"** and **"Missing appendix details"** (from Harsh Critic). The paper states "refer App. C for details" for the user study and "refer supplementary material" for implementation details. These sections exist in the original submission but were stripped by the parser. Criticizing content known to be in the appendix is not a valid weakness of the paper.

5. **Strength Finder's "Ablation studies validate each novel component independently"** — downgraded because the ablation is qualitative only, not a quantitative validation. The qualitative trends are informative but the word "validate" overstates the evidence. Moved here for completeness.

## Novel Insights

Beyond the paper's own contributions, the reviews surface the following insight: the paper's most significant vulnerability is not a flaw in its core technical idea but rather a mismatch between the claimed "fully automatic and zero-shot" framing and the lack of evaluation of the LLM planning subroutine on which the entire method depends. The bounded-attention and token-merging ideas are well-motivated and technically sound; the evidential bottleneck is the unverified upstream dependency. A second insight is that the paper's components form a chain with no explicit robustness check between the LLM planning step and the downstream diffusion modifications—an evaluation of this coupling would be the single highest-impact addition.

## Suggestions

1. **Evaluate the LLM layout planning step.** Report the accuracy of predicted bounding-box masks (e.g., via a grounded segmentation model or human judgment) on the evaluation prompts. Show failure cases and discuss how the method handles incorrect layouts. This is the most important addition.

2. **Add error bars / confidence intervals to all quantitative results** and, if possible, a statistical significance test against the strongest baseline. Even reporting standard deviations over multiple seeds would substantially improve confidence in the reported improvements.

3. **Provide quantitative ablation results.** Report DreamSim and VQAScore for the full method vs. variants without bounded attention, without token merging, and without negative unmerging. This would directly attribute performance to each component.

4. **Specify the multi-character evaluation dataset** (number of prompts, curation process) for reproducibility.

5. **Add a brief parameter sensitivity study** for β_d and the α values, even on a subset of prompts, to demonstrate robustness.

## Score and Decision

The paper identifies a genuine problem, provides a well-motivated technical solution, and presents initial evidence that the method works. The analysis of self-attention leakage and the bounded-attention design are novel contributions. However, the evaluation has significant gaps: the core LLM planning subroutine is unassessed, quantitative results lack variance measures, the multi-character evaluation dataset is unspecified, and the ablation study is only qualitative. These gaps do not invalidate the method but substantially weaken the evidence that the paper's claims are reliable.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
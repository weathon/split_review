Here is my final consolidated review.

---

## Summary

This paper proposes GoodDrag, a diffusion-based drag editing method with two technical innovations: (1) Alternating Drag and Denoising (AlDD), which interleaves drag and denoising steps across multiple diffusion timesteps rather than performing all drags at a single timestep, and (2) Information-Preserving Motion Supervision (IP), which anchors the dragged features to the original handle point features throughout editing. The paper also contributes a 100-image benchmark (Drag100) with labeled masks and control points, plus two evaluation metrics (DAI for drag accuracy, GScore for perceptual quality via Gemini). Extensive qualitative comparisons, quantitative results, and a user study (27 participants) show GoodDrag outperforming DragDiffusion and SDE-Drag.

## Strengths

- **AlDD framework is well-motivated and convincingly supported.** The core insight — that accumulated perturbations from performing all drags at a single timestep cause fidelity loss, and that distributing drags across denoising steps mitigates this — is clearly articulated and validated. The toy experiment (adding noise at one vs. multiple timesteps) provides useful intuition, and the ablation (Fig. "ablation_aldd") cleanly shows that without AlDD, edited results exhibit noticeable inconsistencies (owl body example), while reducing drag count without AlDD sacrifices drag effectiveness. The method introduces no additional computational overhead ("only changes the order of the computations," Sec. 3.3).

- **User study provides strong independent confirmation of overall method quality.** With 27 participants ranking 12 images × 3 methods, GoodDrag is consistently preferred over DragDiffusion and SDE-Drag on both drag accuracy and perceptual quality (Fig. "userstudy"). This is the most compelling evidence in the paper and validates that GoodDrag as a whole outperforms existing approaches.

- **Drag100 dataset fills a genuine need in the field.** Existing drag editing benchmarks lacked standardized indication masks (leading to uncontrolled comparisons) and explicit diversity considerations. Drag100 provides 100 images with masks and control points across 5 task types (relocation, rotation, rescaling, content removal, content creation) and multiple categories. This is a reusable contribution that should benefit future research.

- **IP heatmap analysis provides mechanistic evidence for feature drift reduction.** The feature distance maps (Fig. "heatmap") show that IP produces more concentrated heatmaps with higher variance (enabling more precise point tracking) and keeps feature distances substantially smaller throughout the editing process. This is independent of the gradient-step-count confound and supports the underlying motivation for IP.

## Weaknesses

### Fatal
None.

### Major

1. **The IP ablation is confounded with the number of gradient steps per drag operation.** The paper's ablation (Fig. "drag multiple times") compares: (b) baseline w/o IP (1 gradient step) — fails; (c) IP with 1 step — fails; (d) IP with 3 steps — succeeds. The missing control is: does the *original* motion supervision loss (Eq. 1) also succeed when using 3 gradient steps per drag (with point tracking after every 3 steps)? The paper partially addresses this via DragDiffusion* (210 total gradient steps structured as 210 single-step drags), which still underperforms GoodDrag. However, this comparison changes both the loss function *and* the grouping structure (1 step per drag vs. 3 steps per drag with interleaved tracking), so it does not isolate the effect of the IP loss. A proper control — original loss with 3 steps per drag — is needed to determine whether IP itself drives the improvement or whether the benefit comes from using multiple gradient steps per drag operation regardless of the loss.

2. **DAI's construct validity for non-relocation tasks is unexamined.** The DAI metric (Eq. 8) computes MSE between a patch around the source handle point in the original image and a patch around the *target* point in the edited image. This assumes rigid appearance transfer, which is appropriate for relocation tasks but questionable for rotation, rescaling, content removal, and content creation — all included in Drag100 — where the appearance at the target location would legitimately differ from the source. The paper presents DAI as the primary quantitative measure of drag accuracy (Table 1) without discussing this limitation or validating that DAI correlates with human judgments of drag accuracy. No correlation between DAI and the user study's drag accuracy rankings is reported.

### Minor

3. **GScore validation rests on a small sample with coarse rankings.** The Spearman correlation of 0.708 between GScore and human quality rankings is computed from 12 images × 3 methods. With only 3 methods per image, per-image Spearman ρ can only take the values {−1, −0.5, 0, 0.5, 1.0}, making the average of 0.708 a coarse estimate. While the gap versus competing metrics (TReS: 0.250, MUSIQ: −0.125, TOPIQ: 0.083) is large enough to be meaningful even with noise, the sample is too small to confidently rank GScore's reliability. No comparison to other LMM-based scorers (e.g., GPT-4V with alternative prompts) is provided despite the paper mentioning GPT-4V was tested.

4. **No discussion of failure cases or limitations.** The paper does not analyze what kinds of images, tasks, or configurations GoodDrag still struggles with. A few representative failure cases would strengthen credibility and guide future work.

5. **No runtime or memory comparison with baselines.** GoodDrag's own runtime (~1 min for editing, 17 s for LoRA on A100) is reported, but comparable numbers for DragDiffusion and SDE-Drag are not provided, making it difficult to assess the practical trade-offs.

### Trivial

6. **DAI and GScore results lack confidence intervals or significance tests.** Table 1 (DAI) and Table 2 (GScore) report point estimates without standard deviations or statistical tests, even though the 100-image dataset is large enough to support them.

## Nice-to-Haves

- An ablation comparing the baseline motion supervision loss (Eq. 1) with 3 gradient steps per drag vs. IP with 3 gradient steps per drag. This would cleanly isolate the effect of the IP loss.
- A scatter plot or correlation analysis between DAI and the user study's drag accuracy rankings to validate the metric.
- Expanding the GScore-human correlation study to the full 100-image Drag100 dataset (or a larger subset).
- A brief failure analysis section showing which drag tasks or image types remain challenging for GoodDrag.

## Removed Points

These points from the reviews were removed with brief justification:

- **Harsh Critic's critique of the toy experiment** ("random Gaussian noise is not the same as the structured changes from feature alignment"): The paper presents this only as illustrative intuition, not as formal validation. The criticism demands a standard of proof the paper does not claim for this figure.
- **"Missing related works" / "Comparison with more recent methods"**: Speculative — per guidelines, the paper's cited references are assumed to exist and be current. No external evidence confirms newer methods should exist.
- **"The paper should also cover Y / domain Z" type demands** beyond the paper's stated scope were removed.
- **Formatting/style nitpicks and parser artifacts** removed per guidelines.

## Novel Insights

The harsh critic's most insightful point is the identification of the IP confound — the failure to test the original loss with an equivalent number of gradient steps per drag. This is a genuinely subtle experimental design issue that could affect how the community interprets the paper's second claimed contribution. The observation about DAI's face-validity problem for non-relocation tasks is also perceptive and points to a broader issue in drag editing evaluation: most current metrics implicitly assume simple translation, but real drag edits often involve deformation, rotation, or generation. Neither reviewer identified a structural flaw in the AlDD contribution — both the ablation and the toy experiment support it cleanly.

## Suggestions

1. **Run the missing IP control**: Compare (a) baseline loss with 3 gradient steps per drag vs. (b) IP loss with 3 gradient steps per drag (everything else equal). If (a) matches (b), recalibrate the paper's claims; if (b) remains superior, the IP contribution is strongly validated.
2. **Validate DAI against the user study**: Compute the Spearman correlation between DAI and the user study's drag accuracy rankings for the same 12 images. Report the result openly, including any cases where DAI disagrees with human judgment.
3. **Expand GScore validation to the full Drag100**: If feasible, collect human quality ratings for a larger subset (50–100 images) to make the correlation more statistically robust.
4. **Add a limitations section**: Discuss what types of drag tasks (e.g., large rotations, fine-grained deformation) remain challenging for GoodDrag.

## Score and Decision

This paper has a genuine core contribution in the AlDD framework, which is well-supported by ablation, intuition, and the user study. The IP contribution and the new metrics are potentially valuable but need cleaner experimental validation. The weaknesses are fixable in revision (adding one ablation, correlating DAI with the user study, expanding GScore validation) and do not invalidate the paper's main thesis that GoodDrag outperforms prior methods — which is independently confirmed by the user study.

**Score**: 6.5

**Decision**: Accept

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
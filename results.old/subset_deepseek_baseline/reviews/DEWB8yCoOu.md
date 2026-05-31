## Summary

This paper proposes XTalker, a real-time controllable talking portrait animation framework based on flow matching. The authors systematically analyze parameter-based facial representations and discover that facial keypoint dynamics can be decomposed into three interpretable subspaces: lip-phoneme synchronization governed by audio envelope, emotion modulation conditioned on semantic labels, and head motion controlled by user-defined curves. Building on this insight, they design a unified MM-DiT backbone with three lightweight prediction heads—talking, emotion, and pose—to disentangle these components. The framework achieves real-time inference (28 FPS on RTX 4090) and demonstrates competitive lip-sync accuracy while significantly improving emotion expressivity and head motion diversity.

## Strengths

- **Clear and well-motivated decomposition of facial dynamics.** The paper provides an empirical analysis (Figures 1 and 2) showing that implicit keypoints can be grouped into lip-sync, emotion, and pose subspaces, and that the audio envelope correlates strongly with mouth keypoints. This analysis directly motivates the architectural design and is a genuine contribution beyond simply proposing another model.

- **Modular and efficient design.** The three-head architecture (talking, emotion, pose) with a shared lightweight MM-DiT backbone is elegant and enables explicit control over each dimension. The computational breakdown showing the DiT takes only ~0.48 ms per frame (2.2% of warping time) confirms that the additional control modules add negligible overhead.

- **Strong empirical results on expressivity and speed.** XTalker achieves the best EmoACC (0.6476), highest head motion variance (21.22), top CSIM (0.9395), and lowest LPIPS (0.0432) among all baselines. The inference speed of 28 FPS on RTX 4090 (33 FPS on A100) is substantially faster than all competitors—over twice as fast as the nearest baseline (Float at 14.17 FPS on A100).

- **Thorough ablation study.** Table 2 systematically ablates each design choice (heads, dynamic weighting, noise initialization, envelope conditioning) and quantifies their contributions. The variant analysis confirms that each component serves a distinct and meaningful role.

## Weaknesses

### Fatal
No fatal errors are identified.

### Major

**1. Insufficient detail on how the emotion and pose conditioning modules are trained, limiting reproducibility.**  
The "Emotion Expression Transformer" (Sec 3.3) and "LLM-Guided Curve-Pose Synthesis" are described only briefly, with details deferred to the appendix. Critically, the paper does not explain what training data these modules require, whether they are trained separately from the main model, or how the emotion label supervision is sourced. The emotion transformer apparently regresses target embeddings in keypoint space from a source embedding and one-hot emotion vector—but without a clear training protocol (e.g., paired emotional keypoint data), it is unclear how this is achieved. Similarly, the LLM's role in generating curves is described vaguely, and the "diagonal transform" mapping curves to PYR increments seems almost trivial. The reader is left to wonder whether the real innovation lies in these modules or just in the flow-matching backbone.

**2. Head motion variance metric is not convincingly linked to naturalism.**  
The paper measures "Pose-Variance" to evaluate head motion diversity. A higher variance could simply reflect random jitter rather than natural, speech-appropriate head motion. Without qualitative validation (e.g., a user study) or correlation with other naturalness metrics, it is unclear that the 21.22 value is actually better than the 9.66 of Float or 5.96 of SadTalker. The posed controllability experiment (Figure 7) shows that variance increases linearly with scaling parameter γ, but does not assess whether the resulting motions are realistic.

**3. The comparison with baselines is not fully controlled.**  
The paper trains XTalker on HDTF but evaluates against baselines presumably using their released checkpoints (which may have been trained on completely different datasets). Metrics like CSIM and LPIPS are sensitive to resolution and training data distribution. A fairer comparison would involve retraining all baselines on HDTF or, alternatively, evaluating XTalker on the same test sets used by each baseline. The observed gap in Sync-C (where Float scores an implausible 1.0579, above the theoretical maximum of 1.0) further suggests metric or evaluation inconsistencies that should be explained.

### Minor

- The claim of "real-time" performance (28 FPS) is specific to RTX 4090. The paper acknowledges that some baselines run out of memory, but the comparison could be extended to include settings where all baselines run at lower resolutions or inference steps.
- The paper uses synthetic reference images from "GPT-5" for evaluation, but GPT-5 is not publicly released, making this portion of the evaluation non-reproducible.
- The qualitative results (Figure 4) show XTalker frames with noticeably sharper emotion, but the video frame grids are small and do not include side-by-side renderings aligned in time, making direct comparison difficult.

### Trivial

- The figures appear to have repeated captions due to parser artifacts, which is not a paper flaw.
- Minor notation inconsistencies (e.g., using `δ_s` vs `s_s` for scale) do not hinder understanding.

## Nice-to-Haves

- Adding a user study to validate that the higher head motion variance indeed leads to more natural or preferred animations.
- Providing clear evaluation protocols for the emotion and pose conditioning modules, including how emotion labels are assigned to test samples and how curve-driven control is measured quantitatively beyond variance.
- Ablating the number of flow-matching inference steps to show the trade-off between speed and quality.

## Novel Insights

Beyond the paper's own contributions, the key novel insight is the empirical demonstration that in parameter-based facial representations (specifically LivePortrait-style implicit keypoints), the audio amplitude envelope correlates strongly with vertical mouth keypoint displacements. This simple but underexplored observation provides a low-cost, interpretable conditioning signal for lip synchronization that avoids the need for complex cross-modal attention over large latent spaces. The recognition that emotion bias can be injected by modulating only source keypoints via a lightweight transformer (rather than full-video emotion conditioning) is also valuable for low-data regimes.

## Suggestions

1. Clarify the training protocol for the Emotion Expression Transformer and the LLM-guided curve-pose module. Specifically, describe the training data, loss functions, and whether these modules are pretrained or trained jointly with the main model.
2. Provide a more rigorous analysis of head motion naturalness, such as using motion dynamics metrics (e.g., velocity/acceleration distributions) or a small user preference study.
3. Fix the Sync-C anomaly for Float (1.0579) by explaining if a different metric variant was used or if this indicates dataset mismatch.
4. Consider including an additional baseline that explicitly controls emotion and pose (e.g., VASA-1 with parameter editing) to highlight XTalker's controllability advantage.

## Score and Decision

**Score:** 8.0  
**Decision:** Accept

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>
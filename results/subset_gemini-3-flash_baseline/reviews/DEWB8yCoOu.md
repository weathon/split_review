## Summary
The paper introduces XTalker, a parameter-based framework for audio-driven portrait animation that emphasizes controllability and expressivity. By disentangling facial motion into three interpretable subspaces—lip-phoneme synchronization (driven by audio envelopes), emotional modulation (via discrete labels), and head motion (via user-defined curves)—the authors build a lightweight MM-DiT backbone with specialized prediction heads. XTalker achieves real-time performance (28+ FPS on consumer GPUs) and demonstrates superior emotion and pose diversity compared to existing diffusion-based and parameter-based baselines.

## Strengths
- The paper provides a systematic analysis of implicit keypoint disentanglement, demonstrating how specific keypoints correlate with the audio envelope and how redirection can be used for emotion and pose control.
- The proposed architecture is highly efficient, achieving 28.21 FPS on an RTX 4090, which is significantly faster than many recent diffusion-based competitors (e.g., EchoMimic, Hallo3) that often struggle with real-time constraints.
- The method offers explicit control handles (emotion labels and drawn curves) that are more intuitive for end-users than the implicit latent controls found in many SOTA models.
- The use of Dynamic Weight Averaging (DWA) and homoscedastic uncertainty to balance the multi-head flow-matching loss is a sound technical choice that addresses the difficulty of training multi-task generative models.

## Weaknesses
### Fatal
None.

### Major
- **Limited Training Scale:** The model is trained on the HDTF dataset, which contains only ~350 videos. While the results are impressive for this scale, the quantitative lip-sync metrics (Sync-C/D) lag behind some baselines. It is unclear if the parameter-based bottleneck or the data scale is the primary cause, and the paper would benefit from a discussion on how the model scales to larger, more diverse datasets like VoxCeleb2.
- **Dependency on Pre-trained Components:** The framework relies heavily on the LivePortrait/Face-Vid2Vid backbone. While this is a common practice, the "expressivity" is bounded by the capacity of these pre-trained implicit keypoints to represent complex deformations.

### Minor
- **Evaluation of Curve-Pose Synthesis:** While the paper mentions LLM-guided curve synthesis, the evaluation of how well the model follows *complex* user-defined trajectories (beyond simple scaling $\gamma$) is somewhat brief.
- **Sync-C/D Performance:** The quantitative gap in Sync-C compared to "Float" is quite large (0.75 vs 1.05). While the authors attribute this to data scale, it suggests that the audio-envelope-driven talking head might be less precise than landmark-conditioned diffusion models for fine-grained phoneme articulation.

### Trivial
- The correlation analysis in Figure 6 shows a "weaker" correlation in generated videos compared to real ones, which is acknowledged but not fully explained in terms of its impact on perceived naturalness.

## Nice-to-Haves
- A user study comparing the "controllability" aspect specifically, asking users to rate how well the output matches a specific drawn curve or emotion label compared to baselines.
- Comparison with other parameter-based methods like MediaPipe-based or 3DMM-based models to justify the choice of implicit keypoints.

## Novel Insights
The most significant insight is the empirical validation that the audio envelope—a low-level signal feature—can serve as a robust prior for lip-phoneme synchronization when mapped to specific disentangled keypoint subspaces. Furthermore, the paper successfully demonstrates that "emotion redirection" (transferring keypoint residuals from a single reference frame) can be effectively internalized into a generative flow-matching head, allowing for label-based emotion control without requiring per-frame emotion annotations during training.

## Suggestions
- To address the Sync-C gap, consider incorporating a small amount of landmark-based supervision or a lip-sync discriminator during the fine-tuning phase.
- Provide more examples of the "LLM-guided" aspect in the demo/appendix to show how natural language prompts translate into the "drawn curves" that drive the pose head.

## Score and Decision
The paper presents a well-motivated, efficient, and highly controllable framework for portrait animation. Its strength lies in the balance between speed and expressivity, making it a practical contribution to the field. While the lip-sync metrics are not SOTA, the gains in controllability and inference speed are significant.

MY FINAL SCORE: 7.0
MY FINAL DECISION: Accept
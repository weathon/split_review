## Summary

This paper proposes XTalker, a real-time controllable talking portrait animation framework that decomposes facial motion into three interpretable subspaces (lip-sync, emotion, head pose) and applies a flow-matching generation paradigm with a unified MM-DiT backbone followed by three lightweight heads. The method leverages audio envelope dynamics for lip articulation, emotion labels for expression modulation, and user-defined curves for head motion control, achieving competitive lip-sync accuracy while significantly outperforming prior works in emotion expressiveness, head motion diversity, and inference speed.

## Strengths

- **Clear and actionable decomposition of facial motion.** The paper presents a systematic analysis of implicit keypoint representations (from LivePortrait) and demonstrates that mouth keypoints correlate strongly with audio envelope, emotion keypoints can redirect expressions, and pose keypoints can transfer head motion patterns. This analysis motivates a principled three-subspace design that goes beyond lip-sync only methods.
- **Efficient and effective architecture for controllable generation.** XTalker's MM-DiT backbone plus three lightweight heads yields real-time performance (28.21 FPS on RTX 4090) while maintaining fine-grained control. The separation of emotion, talking, and pose heads with distinct conditioning signals (emotion label, envelope, user-defined curves) enables explicit modulation that prior audio-driven methods lack.
- **Strong experimental validation.** The method is compared against seven strong baselines across six metrics. XTalker achieves the best results in identity preservation (CSIM 0.9395), perceptual quality (LPIPS 0.0432), emotion accuracy (EmoACC 0.6476), head pose variance (21.2243), and inference speed (33.14 FPS on A100). Extensive ablation studies confirm the contribution of each head and design choice.
- **Practical real-time performance with high expressivity.** The system runs at >28 FPS on a consumer GPU while delivering superior emotion and motion diversity, making it suitable for practical deployment in interactive applications.

## Weaknesses

### Fatal

None.

### Major

- **Limited evaluation scale and synthetic data concerns.** Quantitative evaluation uses only 100 test samples (20 from GPT-5, 80 from FFHQ). Synthetic images from GPT-5 may not reflect real-world portrait distribution, and 100 samples is modest for measuring emotion accuracy with statistical confidence. Larger-scale evaluation on established benchmarks (e.g., HDTF test set, VoxCeleb) would strengthen the claims.
- **EmoACC reliability depends on an external classifier whose accuracy is not discussed in the main paper.** Emotion classification is noisy, and the reported 64% / 46% preservation rates from the redirection analysis are moderate. The paper acknowledges the appendix (D.3) for details, but the core claim of "superior emotion expressivity" would benefit from human evaluation or per-class breakdowns in the main text.
- **The disentanglement analysis is correlational, not causal.** The paper shows that modifying certain keypoints affects specific facial regions and that mouth keypoints correlate with audio envelope. However, the claim of "interpretable subspaces" that are fully disentangled is not rigorously proven; interactions between emotion and lip movements (e.g., smiling while speaking) may still couple the subspaces. The ablation study (Table 2) shows that pose and emotion heads can sometimes conflict (e.g., All w/o DWA has higher Pose-Variance but lower Sync-C and CSIM).
- **LLM-guided curve-pose synthesis is underelaborated.** The paper describes an LLM that "generates predefined curves" and a diagonal transform to map curves to PYR increments, but gives no details on prompts, LLM model choice, or quantitative evaluation of curve quality. This component feels underspecified relative to its role in pose controllability.

### Minor

- The Sync-C score (0.7548) is lower than Float (1.0579), Hallo3 (0.7907), JoyVASA (0.7550), and Sonic (0.7288), placing XTalker as fourth best. The paper attributes this to limited training data, but the gap to Float is notable.
- Some baselines (Float, Hallo3, JoyVASA) are reported as OOM on RTX 4090, making direct hardware comparison incomplete. This is not a flaw of XTalker, but it limits the fairness of efficiency comparisons.

### Trivial

None.

## Nice-to-Haves

- Large-scale evaluation on public benchmarks (e.g., HDTF test split, VoxCeleb2, CelebV-HQ test) to increase statistical reliability.
- Human evaluation of emotion expressiveness and naturalness of head motion to complement automatic metrics.
- Ablation on the LLM component: comparison with alternative curve generation strategies (e.g., handcrafted curves, random curves) to quantify the benefit of LLM guidance.
- Exploration of more granular emotion control (e.g., continuous valence-arousal) instead of discrete labels.

## Novel Insights

None beyond the paper's own contributions. The core insight—that facial keypoint representations can be decomposed into lip, emotion, and pose subspaces and that audio envelope provides a natural control signal—is well-motivated by the empirical analysis and cleanly operationalized in the XTalker architecture. However, similar decomposition principles are known in the graphics and animation literature, and the primary novelty lies in the efficient integration with flow-matching for controllable audio-driven animation.

## Suggestions

- Expand the evaluation to a larger test set (e.g., entire HDTF test set or a random 1,000-sample subset from CelebV-HQ) and report per-emotion accuracy and per-head-pose variance distributions.
- Provide a detailed description of the LLM-guided curve generation process (models, prompts, filtering) in the main paper or appendix, and ablate whether LLM conditioning significantly improves pose controllability over simple random or sinusoidal curves.
- Include a user study on emotion and motion naturalness to complement automatic metrics, especially to validate that the high EmoACC and Pose-Variance correspond to perceptually improved expressivity.

## Score and Decision

The paper presents a well-motivated method that cleanly decomposes facial animation into three controllable subspaces, achieves real-time performance, and demonstrates convincing quantitative improvements over recent baselines. The evaluation scale and the correlational nature of the disentanglement analysis are limiting factors, but the overall contribution—especially the practical real-time controllable framework—is solid and valuable to the community.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: Accept
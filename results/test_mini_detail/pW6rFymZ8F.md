## Summary

EmbodiedMAE proposes a unified 3D multi-modal representation learning framework for robot manipulation. The paper contributes (1) DROID-3D, a large-scale supplement to the DROID dataset with high-quality depth maps and point clouds (76K trajectories, 350 hours) processed via ZED SDK, and (2) a multi-modal masked autoencoder trained on DROID-3D that jointly learns representations across RGB, depth, and point cloud through stochastic masking and cross-modal decoding. Evaluated on 70 simulation tasks (LIBERO, MetaWorld) and 20 real-world tasks across two robot platforms (SO100, xArm), EmbodiedMAE consistently outperforms SOTA vision foundation models (DINOv2, SPA, SigLIP, R3M, VC-1) in both training efficiency and final success rate.

## Strengths

- **Large-scale, high-quality 3D robot dataset (DROID-3D).** Processing all 76K trajectories of the DROID dataset using ZED SDK (temporal fusion, AI-augmented enhancement, metric depth) provides temporally consistent depth maps and point clouds, unlike prior works that use subsets or lower-quality AI-estimated depth. This is a substantial resource for the community (Section 2.1).

- **Well-motivated multi-modal MAE architecture with stochastic masking.** The symmetric Dirichlet allocation of unmasked patches across RGB, depth, and point cloud avoids modality bias and enables cross-modal inference. The qualitative reconstructions (Figure 3) demonstrate genuine cross-modal understanding, including the compelling re-coloring experiment suggesting emergent semantic segmentation.

- **Extensive and consistent evaluation across diverse settings.** The paper evaluates on 40 LIBERO tasks, 30 MetaWorld tasks, and 20 real-world tasks on two robot platforms (low-cost SO100 and high-performance xArm), substantially more than typical VFM-for-robotics papers. EmbodiedMAE outperforms all baselines in both simulation and real-world settings, with results that are directionally convincing.

- **Scaling behavior and practical distillation.** Performance improves monotonically from Small through Giant model variants (Figure 6), and the feature-alignment distillation (Section 2.4) produces compact models that retain strong performance, making the approach practically deployable.

- **Effective 3D integration compared to naive fusion.** EmbodiedMAE-RGBD outperforms both EmbodiedMAE-RGB and DINOv2-RGBD (which degrades with depth), demonstrating that the multi-modal pre-training design is critical — the 3D benefit is not just from having more data but from how it is learned (Section 3.3, Finding 3).

## Weaknesses

### Fatal
None.

### Major

- **No statistical uncertainty reported for any experiment.** The paper reports only average success rates for all simulation benchmarks (Table 1, Figure 6) and 10-trial raw counts for real-world results (Figure 8), with no confidence intervals, standard deviations, or multiple-seed runs. Given the typical variance in robot rollouts and the small trial counts for real-world tasks (10 per task), differences that look large (e.g., 76.2 vs. 54.4 on MetaWorld RGBD) cannot be assessed for statistical reliability. This weakens the paper's central claim of "consistently outperforming all baselines." The LIBERO results (150 trials per task) are more robust, but the real-world results need error bars to be interpretable. This is the single most important improvement the paper needs.

### Minor

- **DINOv2-RGBD baseline construction may disadvantage that baseline.** The paper states that "adding a trainable depth branch for DINOv2" causes performance degradation (Section 3.3), but provides no ablation or analysis of the depth branch design (architecture, training protocol, tuning effort). Since this baseline is central to the claim that naive 3D fusion hurts performance, more transparency about its construction is needed. (The paper references Section A.3 for details, which was stripped by the parser — these details should be prominent in the main text.)

- **Claim about point-cloud policies underperforming due to sensor noise lacks direct evidence.** The paper attributes EmbodiedMAE-PC's limitations to "sensor noise from object reflectivity and lighting variations" (Section 3.4, Finding 2) but does not present any quantitative analysis (e.g., per-frame noise statistics, controlled experiments with synthetic noise) to support this attribution. The comparison between EmbodiedMAE-PC and DP3 also may confound representation quality with architectural differences — the paper should clarify whether both use the same point preprocessing pipeline.

- **Single qualitative example supports the "object-level semantic segmentation" claim.** The re-coloring experiment (Figure 3, column 12) is striking, but the paper generalizes from a single example to claim the model "has implicitly learned object-level semantic segmentation" (Section 3.2). Additional examples or a quantitative evaluation would strengthen this claim.

- **No quantitative evaluation of DROID-3D data quality.** The depth quality of DROID-3D is only shown qualitatively (Figure 2). A quantitative comparison (e.g., absolute relative error vs. AI-estimated depth on held-out stereo pairs, temporal consistency metrics) would substantiate the claimed improvement over prior depth estimation approaches and demonstrate the marginal benefit of the ZED SDK processing pipeline.

### Trivial

- The usage example in Figure 4 has a syntax error (`model(rgb= None, None)`) that should be corrected.
- The paper says "rest of paper is removed" for the appendix, but since this is a parser artifact the actual submission likely includes it.

## Nice-to-Haves

- A dedicated scalability plot (performance vs. model parameters) would be more informative than the learning curves alone for the scaling claim.
- Reporting inference speed and VRAM usage would support the claimed practical deployability.
- An ablation of the shared decoder vs. separate decoders would quantify the claimed 3× computational saving.

## Removed Points

- **VFM weight freezing ambiguity**: The harsh critic claimed the paper never specifies whether VFM weights are frozen or fine-tuned during policy training. The paper explicitly references "Section A.1 for more details" about the policy architecture and says "in which only VFMs are modular" (Figure 5). Since the appendix was stripped by the parser, this criticism is about content that exists in the full submission. **Removed per rule about missing appendix content.**

- **DP3 integration methodology unclear**: The critic questioned how DP3 (a full policy) is dropped into the RDT framework. The paper describes "all baselines and EmbodiedMAE share the same architecture" (Figure 5) and the ACT ablation (Table 3) compares "ACT Policy + DP3" vs "ACT Policy + EmbodiedMAE-PC," suggesting DP3's 3D encoder is used as a feature extractor. The Appendix (Section A.1, stripped) likely clarifies this. **Removed per rule about missing appendix content.**

- **Missing related works**: Per rules, the reviewer should not mention missing related works without external sources to verify. **Removed.**

- **Formatting/style nitpicks**: Various minor presentation complaints from the harsh critic. **Removed per formatting nitpick rule.**

## Novel Insights

The most interesting finding that emerges from the reviews, beyond the paper's own claims, is that the re-coloring experiment (Figure 3, column 12) is both the paper's most impressive qualitative result and its weakest-evidenced claim. The phenomenon — where modifying a single visible RGB patch causes only the corresponding object to change color in the depth-to-RGB reconstruction — suggests genuine semantic understanding, but a single example cannot rule out alternative explanations (e.g., texture or color gradient artifacts). This tension between a striking observation and thin evidence is common across the paper: the experiments are broad and directionally clear, but lack the statistical precision needed to fully trust the margins. A second meta-observation is that the paper's main methodological contribution (stochastic multi-modal masking + cross-modal decoder) is clean and sensible, but the evaluation that would most directly validate it — ablating the masking strategy or decoder design on the target policy tasks — is deferred to ablation studies on distilled models only.

## Suggestions

1. **Add error bars.** Report success rates with confidence intervals (bootstrap or across 3-5 seeds) for at least the main simulation benchmarks. For real-world experiments, report per-task success counts or binomial confidence intervals. This single change would substantially raise the paper's reliability.

2. **Clarify the policy training protocol.** State explicitly in the main text whether VFM weights are frozen or fine-tuned during RDT policy training. If fine-tuned, include an ablation comparing frozen vs. fine-tuned to separate representation quality from trainability.

3. **Provide quantitative depth quality metrics for DROID-3D.** A simple table comparing ZED SDK depth against AI-estimated depth on held-out frames (e.g., absolute relative error, temporal consistency) would substantiate the claimed data quality improvement.

4. **Strengthen the re-coloring evidence.** Add 2-3 more examples or a small-scale quantitative evaluation (e.g., does the recolored patch consistently map to the correct object region across multiple scenes?).

## Score and Decision

**Round 1 Bracketing.** I queried for topically similar papers in three bands: weak (avg < 3.5), middle (3.5-7.5), and strong (>7.5). The weak band returned papers averaging ~3.0 (e.g., "From Appearance to Motion," "Vision-Based Grasping," "Masked VAE") — all withdrawn/rejected with clear fatal flaws. The middle band (3.5-7.5) returned papers ranging from 5.0-6.5 (e.g., "Mastering Robot Manipulation with Multimodal Prompts" at 5.5, rejected; "Joint Representations for RL" at 5.25, rejected; "3D-Spatial Multimodal Memory" at 6.5, accepted poster). The strong band (>7.5) returned papers at 8.0-8.5 (oral/spotlight). The current paper clearly sits above the weak band and below the oral/spotlight level. **Initial bracket: 5.0–7.5.**

**Round 2 Narrowing.** I retrieved additional anchors inside the bracket. "Multiview Equivariance Improves 3D Correspondence" (6.0, accepted poster) has comprehensive experiments but limited practical impact — the current paper has broader evaluation and a dataset contribution, making it slightly stronger. "Selective Visual Representations" (7.5, accepted spotlight) has a clean method with thorough ablations and error bars — the current paper is comparable in ambition but weaker on statistical rigor. "3D-Spatial Multimodal Memory" (6.5, accepted poster) has a more novel methodology but less downstream validation — similar overall quality. Comparing against all anchors, the paper sits closest to the 6.5 anchor: a solid contribution with clear strengths and fixable weaknesses, but not at the rigor level of the 7.5 spotlight papers.

**Final Score: 6.5.** The paper proposes a well-motivated architecture and contributes a valuable large-scale 3D dataset, with evaluation that is impressively broad (90 tasks across simulation and real-world). The main limitation is the absence of statistical confidence measures, which prevents stronger claims about the margins of improvement. The contributions are real and the results are directionally convincing; with the addition of error bars the paper would comfortably sit in the 7+ range.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
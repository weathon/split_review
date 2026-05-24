Now I have all the calibration data I need. Let me synthesize the final review.

**Round 1 bracket**: Between 4.0 and 6.5, narrowing to 5.0–6.5.

**Round 2 narrowing**: The paper is clearly stronger than 5.0 papers (AnyPos, Capturing Visual Structure) due to its large-scale dataset contribution and comprehensive evaluation. It's comparable to Embodied-R1 (6.0) and FSD (6.0) — similar profile of solid empirical contributions with some novelty concerns. It's weaker than Manipulation as in Simulation (6.5) which has a cleaner novel contribution.

**Final score**: 5.5. The paper makes real contributions (DROID-3D dataset, comprehensive evaluation across 90 tasks) but has notable weaknesses: overclaiming in RGB-only results (ties SPA on MetaWorld average), no error bars/variance reporting anywhere, and incremental architectural novelty over MultiMAE. The paper needs several concrete improvements before it's a clear accept.

Now writing the review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths

## Weaknesses

### Fatal
None

### Major
- 

### Minor
- 

### Trivial
- 

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and DecisionNow I have all the information needed. Let me compose the final consolidated review.

---

## Summary

EmbodiedMAE constructs DROID-3D, a large-scale supplement to the DROID dataset (76K trajectories, 350 hours) with high-quality depth maps and point clouds processed via ZED SDK, and trains a multi-modal masked autoencoder on it that jointly learns representations from RGB, depth, and point clouds. The pre-trained encoder is evaluated as a visual backbone for policy learning across 70 simulation tasks (LIBERO, MetaWorld) and 20 real-world tasks on two robot platforms (SO100, xArm). The main claims are consistent outperformance over prior VFMs, effective use of 3D inputs, and strong scaling with model size.

## Strengths

1. **Large-scale, high-quality 3D robot dataset.** DROID-3D processes the complete DROID collection (76K trajectories, 350 hours) using ZED SDK temporal fusion and AI-augmented enhancement, producing metric depth maps and point clouds that are qualitatively superior to existing alternatives (Figure 2). This is a significant engineering contribution that enables embodied-specific 3D pre-training at scale, and the paper makes clear that this dataset is intended as a resource for the community.

2. **Comprehensive and multi-platform evaluation.** The paper evaluates on 70 simulation tasks from LIBERO (40 tasks across 4 suites) and MetaWorld (30 tasks across 3 difficulty levels), plus 20 real-world tasks on two different robot platforms — a low-cost open-source SO100 and a high-performance xArm with a LiDAR camera. This breadth of evaluation across simulation and diverse real platforms provides more evidence than most papers in this space.

3. **Consistent multi-modal advantage.** The key technical success is that EmbodiedMAE effectively leverages 3D inputs (RGBD and point cloud) for policy learning, where naïve fusion baselines (DINOv2-RGBD) degrade relative to RGB-only. On MetaWorld, EmbodiedMAE-RGBD reaches 76.2% (vs. DINOv2-RGBD 54.4%) and EmbodiedMAE-PC reaches 77.7% (vs. DP3 65.8%). The LIBERO results (Figure 6) show the RGBD variant even outperforms the Giant-scale RGB-only model on some suites. The re-coloring visualization (Figure 3, column 12) provides compelling qualitative evidence of object-level semantic understanding learned through the multi-modal objective.

4. **Scaling behavior and architectural generality.** Performance improves monotonically with model size (Small → Base → Large → Giant) on LIBERO, and the learned representations transfer to a different policy architecture (ACT), with EmbodiedMAE-PC achieving 56.2% vs. DP3's 33.1% on MetaWorld Very Hard tasks (Table 3).

## Weaknesses

### Major

1. **The claim of "consistent outperformance" is overbroad for the RGB-only setting.** On MetaWorld (Table 1), the RGB-only variant of EmbodiedMAE ties SPA at 73.0% average success rate and trades wins across difficulty levels (Easy: 81.8 vs. 80.9; Medium: 60.4 vs. 62.8; Very Hard: 57.8 vs. 55.8). The headline in the abstract and introduction — "EmbodiedMAE consistently outperforms state-of-the-art VFMs" — does not hold for RGB-only on MetaWorld. The real advantage of EmbodiedMAE comes from multi-modal inputs; the paper should explicitly qualify the RGB-only claim as task-dependent and state that the main benefit is unlocked with depth or point cloud inputs. The abstract currently says "achieves SOTA performance in both RGB-only and multi-modal settings," which is defensible, but "consistently outperforms" in the same paragraph is too strong.

2. **No variance reporting or statistical significance across any experiment.** No error bars, standard deviations, confidence intervals, or trial-level variance are reported anywhere in the paper. This is a significant concern for the real-world results (Figure 8), which are evaluated over only 10 trials per task — differences of 10–20% could easily be within the noise of a single 10-trial run. The LIBERO learning curves (Figure 6) average across tasks within a suite but show no per-task variance. For the MetaWorld table (Table 1), single numbers are reported with no indication of how many seeds or runs were used. Without any measure of spread, the reader cannot assess whether observed differences are reliable.

3. **The DROID-3D dataset release is not explicitly committed.** The paper states "source code will be made public upon publication" (Reproducibility Statement) and "We believe both the DROID-3D dataset and EmbodiedMAE provide a valuable resource" (Conclusion), but the paper never explicitly states that the processed depth maps and point clouds will be released. The DROID-3D dataset is arguably the most valuable contribution, and its processing pipeline relies on proprietary ZED SDK, making it non-trivial for others to reproduce. The paper needs a clear, unambiguous release statement for DROID-3D.

### Minor

4. **Incremental architectural novelty.** The core architecture closely follows MultiMAE (Bachmann et al., 2022) for the multi-modal masked autoencoding framework and DINOv2 (Oquab et al., 2024) for the ViT structure and distillation approach. The primary adaptations are adding a DP3-based point cloud encoder and training on a robot-specific dataset. While these are valid engineering contributions that the paper demonstrates work well, the framing as a "unified 3D multi-modal representation framework" overstates the architectural novelty. The contribution is better characterized as a successful instantiation of existing ideas at scale on a domain-specific dataset.

5. **No direct ablation isolating data quality vs. multi-modal pre-training.** The paper attributes EmbodiedMAE's success to two factors: the DROID-3D dataset quality/scale and the multi-modal pre-training objective. However, there is no controlled experiment comparing (a) EmbodiedMAE pre-trained on DROID-3D vs. (b) EmbodiedMAE pre-trained on the original DROID (without depth/point cloud, e.g., RGB-only MAE). Without this, it is unclear how much of the improvement comes from the dataset scale/quality versus the multi-modal training signal. This is addressable but would strengthen the paper.

6. **Missing comparison with alternative 3D pre-training approaches.** Given the focus on 3D representations, the paper does not compare with point-cloud-based VFMs pre-trained on large 3D data (e.g., PointMAE on ShapeNet, or similar). The only 3D baseline is DP3, which is a policy architecture rather than a pre-trained representation. A comparison with a point-cloud foundation model would help isolate whether the robot-specific dataset is the key factor.

### Trivial

7. **Table 1 header formatting.** The header "DINOv2<br>RGB" appears twice; the second instance should read "DINOv2<br>RGBD" as confirmed by the text in Finding 3 and the substantially different values (average 70.7 vs. 54.4). Similarly, the second "EmbodiedMAE<br>RGB" should be "EmbodiedMAE<br>RGBD." This appears to be a formatting artifact.

8. **No FLOPs or runtime comparison for the shared decoder.** The paper claims the modality-shared decoder "reduces computational cost by approximately a factor of three" (Section 2.3) but provides no actual compute measurements to support this.

## Nice-to-Haves

- Report results with standard deviations across multiple seeds (at least 3 for simulation) and bootstrap confidence intervals for the 10-trial real-world results, so readers can assess reliability of reported differences.
- Conduct a controlled experiment ablating DROID-3D vs. original DROID (RGB-only MAE pre-training) to isolate the source of improvement.
- Provide GPU hours and model sizes in a table to contextualize resource claims.
- For real-world results, include a systematic categorization of failure modes (grasp, collision, localization) with counts across models, rather than only qualitative examples.

## Removed Points

- *"The DROID-3D processing relies on ZED SDK which is proprietary and not publicly described in sufficient detail."* — Removed because the paper describes the processing at a reasonable level of detail (temporal fusion, AI-augmented enhancement, hardware-calibrated metric depth), and the dataset release question is already captured in Weakness #3. Criticizing proprietary SDK usage is a scope creep issue; many papers use commercial tools.
- *"No comparison with alternative 3D pre-training methods like PointMAE on ShapeNet or PCN."* — Partially retained as Minor weakness #6. The stronger version (calling it a "missing critical baseline") is removed because the paper's contribution is specifically about *robot-domain* pre-training, and the 3D baselines included are policy-level for fair comparison.
- *"Missing details on the DINOv2-RGBD baseline."* — Removed because details are in Appendix A.3 (which was stripped from the parsed version but exists in the original submission). The paper states "See Section A.3 for details of this variant" which is sufficient for the main text.
- *"The claim that existing models fall short is not quantified in the introduction."* — Removed because this is a standard rhetorical framing in introductions and is subsequently quantified by the full evaluation section.
- *"The 500 hours of processing time is mentioned without discussing cost-benefit."* — Removed. This is a reasonable resource investment for a dataset of this scale, and the value is demonstrated by downstream results.
- *"The paper does not ablate whether asymmetric masking would be beneficial."* — Removed. The symmetric Dirichlet is a deliberate design choice; requesting all possible ablations is scope creep.
- *"Hyperparameters may have been tuned differently per baseline."* — Removed as speculative; the paper states all VFMs share the same architecture and policy network, which is standard for fair comparison.
- *"Strength: EmbodiedMAE outperforms all baselines on MetaWorld."* — Weakened in the strengths section because EmbodiedMAE RGB ties SPA RGB on MetaWorld average (73.0% each).
- *"The paper addresses an important problem"* — Generic strength, removed.
- *"The evaluation scale is commendable"* — Generic, absorbed into the specific strength about comprehensive evaluation.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Tone down the RGB-only claim.** Replace "consistently outperforms" with language that acknowledges the RGB-only results are competitive but task-dependent, and clearly state that the main advantage is in multi-modal settings. This is the single highest-leverage fix.
2. **Add variance reporting.** Report standard deviations across 3+ seeds for simulation results and bootstrap confidence intervals for real-world 10-trial results. Even a table in the appendix would substantially improve credibility.
3. **Explicitly commit to releasing DROID-3D.** Add a clear statement about whether the processed depth maps and point clouds will be released, and under what license.
4. **Add the controlled ablation** comparing pre-training on DROID-3D vs. DROID without multi-modal data to separate dataset quality effects from multi-modal training effects.
5. **Fix Table 1 headers** to correctly label the RGBD columns.

## Score and Decision

**Calibration anchors used:**

Round 1 (bracketing):
- Weak band (<3.5): ViTacFormer (avg 3.00), Multimodal Masked Polymer Autoencoder (avg 3.00), Robu-MARC (avg 1.50) — all rejected/withdrawn. The paper is far stronger than these.
- Middle band (3.5–7.5): Embodied-R1 (avg 6.00, Accept Poster), FSD (avg 6.00, Accept Poster), LAC-WM (avg 4.00, Reject), AnyPos (avg 5.00, Reject).
- Strong band (>7.5): NavFoM (avg 8.00), π³ (avg 8.00), VIST3A (avg 8.00) — the paper is not at this level.

Round 2 (narrowing 5.0–6.5):
- 3D-aware Disentangled Representation (avg 5.33, Accept) — comparable evaluation breadth but less dataset impact. EmbodiedMAE is slightly stronger.
- Capturing Visual Structure (avg 5.00, Accept) — interesting proxy metric but no practical robot demo. EmbodiedMAE is clearly stronger in actionable contribution.
- Manipulation as in Simulation (avg 6.50, Accept) — cleaner novel contribution (CDM plugin), stronger empirical story. EmbodiedMAE is slightly weaker.
- Geometry-aware 4D Video Generation (avg 6.00, Accept) — comparable strength.

**Bracket**: Round 1 placed the paper between 4.0 and 7.5, narrowing to 5.0–6.5. Round 2 anchors confirm the paper is well above the 4.0–5.0 band but below the 6.5+ band. Comparing against Embodied-R1 (6.0) and FSD (6.0), EmbodiedMAE has a stronger dataset contribution and comparable evaluation breadth, but worse overclaiming and missing variance reporting. The paper is closest to the 5.5–6.0 range.

**Final score**: 5.5. The paper's contributions (DROID-3D, comprehensive multi-platform evaluation, effective 3D fusion) are real and valuable, but the overclaiming in the abstract, lack of any statistical rigor (no error bars anywhere), and absence of the controlled ablation needed to substantiate the source of improvements prevent a higher score.

<score>5.5</score>
<decision>Reject</decision>
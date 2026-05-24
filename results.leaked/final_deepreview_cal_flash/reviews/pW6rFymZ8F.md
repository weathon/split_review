## Summary

EmbodiedMAE proposes a unified 3D multi-modal representation for robot manipulation, built on two main contributions: (1) DROID-3D, a large-scale dataset of 76K robot manipulation trajectories (350 hours) with high-quality ZED-SDK-derived depth maps and point clouds, and (2) a multi-modal masked autoencoder trained on DROID-3D that jointly learns representations across RGB, depth, and point cloud through stochastic Dirichlet masking and cross-attention decoding. The model is evaluated on 70 simulation tasks (LIBERO, MetaWorld) and 20 real-world tasks across two robot platforms (SO100, xArm), showing consistent improvements over several VFMs (DINOv2, SigLIP, R3M, VC-1, SPA).

## Strengths

1. **DROID-3D dataset as a significant infrastructure contribution.** The authors process the complete DROID dataset (76K trajectories, 350 hours) using ZED SDK to produce temporally consistent, high-quality metric depth maps and point clouds — unlike prior work (e.g., SPA) that processes only a small subset with lower-quality AI-estimated depth. This is a genuine resource for the community (Section 2.1, Figure 2).

2. **Extensive evaluation across 70 simulation and 20 real-world tasks.** The evaluation breadth is genuinely impressive: LIBERO (40 tasks in 4 suites), MetaWorld (30 tasks across 3 difficulty levels), plus two real-world robot platforms. This far exceeds the typical evaluation scope in this area and provides strong evidence that the approach works across diverse settings (Section 3.3–3.4, Figures 6–8).

3. **Within-model controlled evidence that multi-modal pre-training helps 3D utilization.** The comparison between EmbodiedMAE-RGB (73.0%) and EmbodiedMAE-RGBD (76.2%) on MetaWorld (Table 1), alongside the finding that naively adding depth to DINOv2 *degrades* performance (54.4% vs 70.7%), provides controlled evidence that the multi-modal design specifically enables effective 3D perception — unlike standard VFMs. This within-model contrast is the paper's cleanest evidence for its core claim.

4. **Scaling behavior and policy-architecture generalization.** Performance improves monotonically with model size (Small→Base→Large→Giant, Figure 6), and the representation transfers to a different policy architecture (ACT, Tables 2–3), showing the learned features are not tied to a specific policy. The teacher-student distillation pipeline (Section 2.4) produces efficient smaller models that still outperform comparably-sized baselines.

## Weaknesses

### Major

1. **Unfair comparison with DINOv2 / missing single-modal pre-training baseline.** EmbodiedMAE is initialized from DINOv2 and then pre-trained on DROID-3D with a multi-modal MAE objective. The DINOv2 baseline receives no additional pre-training on DROID-3D. Any observed improvement could therefore arise from additional in-domain pre-training on 76K robot trajectories, regardless of the multi-modal design. The paper does not include a controlled baseline where DINOv2 (or an identical ViT) is fine-tuned on DROID-3D with a single-modal MAE (RGB-only) under comparable conditions. While the comparison against SPA (which is pre-trained on a DROID subset) partially mitigates this, SPA uses a different pre-training objective and only 1/15 of the data. This gap undermines the central claim that the multi-modal architecture itself is responsible for the reported gains.

2. **Missing ablation isolating multi-modal vs. single-modal pre-training.** The ablation studies in Section 3.5 focus entirely on distillation hyperparameters (masking ratio, feature alignment positions, loss ratio). They do not evaluate whether multi-modal masked autoencoding on RGB+depth+point cloud is superior to single-modal pre-training on the same data with equivalent compute. Without a comparison to an EmbodiedMAE variant pre-trained on RGB images only (or RGBD concatenated as channels), the benefit of the unified 3D multi-modal representation is not empirically isolated.

### Minor

3. **Limited statistical rigor.** Real-world results are based on only 10 trials per task with no confidence intervals, error bars, or significance tests (Figure 8). For simulation experiments, the number of policy training seeds is not reported, making it impossible to assess result stability. The 10-trial real-world evaluation is acknowledged but the lack of any variance information weakens confidence in the reported rankings, particularly for small performance gaps.

4. **DP3 comparison not fully controlled for policy architecture.** In the main MetaWorld (Table 1) and real-world results (Figure 8), EmbodiedMAE-PC (using the RDT diffusion-transformer policy) is compared against DP3, which likely uses a different policy architecture. While the ACT-based experiments (Table 3) partially address this by showing both methods under the same ACT policy, the main results do not isolate representation quality from policy architecture differences.

5. **Missing quantitative validation of key claims.** (a) DROID-3D depth quality is demonstrated only qualitatively (Figure 2) without metrics (e.g., RMSE, temporal consistency). (b) The claim that EmbodiedMAE "implicitly learned object-level semantic segmentation" (Section 3.2, Figure 3) is based on a single re-coloring example without any segmentation evaluation. (c) The assertion that the bias term in projection layers "implicitly encodes modality-specific information" (Section 2.2) is stated without evidence or ablation.

### Trivial

6. The "approximately a factor of three" computational savings claim (Section 2.3) is stated without any quantification or reference.

## Nice-to-Haves

- Quantitative depth quality metrics for DROID-3D (e.g., against known ground truth or downstream policy learning comparisons using DROID-3D depth vs. AI-estimated depth).
- An ablation comparing Dirichlet masking with uniform modality masking or fixed ratios to justify the stochastic allocation design.
- Discussion of failure modes related to 3D representation limitations (e.g., sensitivity to sensor noise, transparent/reflective objects), beyond the brief mention of PC noise in Section 3.4.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Missing MultiMAE citation in the main text"** (from Harsh Critic Section-by-Section Notes). The paper explicitly cites Bachmann et al. (2022) in Section 2.2 ("Following Bachmann et al. (2022)") and lists MultiMAE in the references. This criticism is factually incorrect.
- **Reproducibility concern about undisclosed hyperparameters / missing appendix details.** The paper references Section A.1 (now stripped by the parser). Appendix content was removed during PDF extraction and cannot be evaluated.
- **"Missing citation of MultiMAE"** (from Harsh Critic's "Missing Parts" section). Same as above — the citation is present.
- **"The paper does not critically differentiate EmbodiedMAE from prior multi-modal masked autoencoders"** (from Related Work critique). This is a generic observation, not a specific weakness supported by evidence of a concrete omission.
- **Strength Finder: "Consistent SOTA performance across 70 simulation and 20 real-world tasks"** — retained as a strength but with the important qualification that the DINOv2 comparison confounds additional pre-training with architectural benefit. This qualification is noted in the weakness section.

## Novel Insights

None beyond the paper's own contributions. The main novel observation — that multi-modal MAE pre-training on in-domain robot data enables effective 3D perception in a way that standard VFMs cannot — is partially supported by the within-model RGBD vs. RGB comparison but needs stronger controlled evidence.

## Suggestions

1. **Add a controlled single-modal baseline:** Pre-train DINOv2 (or an identical ViT encoder) on DROID-3D using a single-modal MAE (RGB-only) under identical compute and hyperparameter settings. This would directly quantify whether the multi-modal design provides benefit beyond additional in-domain pre-training.

2. **Report statistical variance:** Include confidence intervals or standard deviations across multiple policy training seeds for all simulation experiments. For real-world results, at minimum report per-trial outcomes or binomial confidence intervals.

3. **Provide quantitative depth quality metrics** for DROID-3D (e.g., RMSE against known ground truth, or a downstream control experiment comparing DROID-3D depth against AI-estimated depth under the same policy learning setup).

4. **Clarify the DP3 comparison:** Either (a) integrate DP3 as a visual encoder within the same RDT policy and report results, or (b) clearly acknowledge the policy architecture confound and reframe the comparison as system-level.

## Score and Decision

### Calibration

**Round 1 (Bracketing):** Queried "multi-modal masked autoencoder robot manipulation representation learning" across three score bands.

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| wl1Kup6oES (From Appearance to Motion...) | 3.00 | R1 | Much weaker evaluation (3 envs, 21 tasks); our paper is stronger |
| sXF5P4N7e8 (Vision-Based Grasping...) | 3.00 | R1 | Significantly less scope; our paper is much stronger |
| 9GKMCecZ7c (Building Generalist Robot Policy...) | 3.40 | R1 | Similar topic but weaker evaluation; our paper is stronger |
| tt0SCefKQL (Masked VAE...) | 3.00 | R1 | Different domain; less relevant |
| FMsmo01TaI (Power of the Senses, M3L) | 4.33 | R1 | Most topically similar; our paper has much broader evaluation (70+20 vs 3 sim tasks), stronger baselines |
| NtQqIcSbqv (Learning to Jointly Understand Visual and Tactile) | 6.00 | R1 | Different focus (visuo-tactile); comparable thoroughness |
| IsGsv8qEHp (Human-oriented Repr Learning) | 5.00 | R1 | Similar scope; our paper has clearer methodology and more consistent results |
| bw9bvwVwMH (Point Cloud SSL via 3D to Multi-view) | 6.00 | R1 | Rejected despite 6.00; similar issues with missing ablations, but our evaluation is broader |
| 7gUrYE50Rb (EQA-MX) | 8.00 | R1 | Very different topic; much stronger paper |
| 7BLXhmWvwF (Geometry-aware RL) | 8.00 | R1 | Different topic; stronger paper |

**Round 1 bracket:** 4.5–6.5.

**Round 2 (Narrowing):** Queried for robot manipulation representation learning papers.

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| NxoFmGgWC9 (Unleashing Large-Scale Video Generative Pre-training) | 5.50 | R2 | Accepted; comparable in ambition and evaluation gaps (missing baselines); our paper has broader task coverage |
| jf7C7EGw21 (VTDexManip) | 5.50 | R2 | Accepted; dataset+benchmark contribution similar to ours; comparable quality |
| KTtEICH4TO (CORN) | 4.75 | R2 | Different focus; weaker evaluation |
| c0chJTSbci (Zero-Shot Robotic Manipulation...) | 6.25 | R2 | Stronger in novelty; different approach |
| TqM0hifngW (JEPT) | 7.00 | R2 | Stronger paper overall; cleaner evaluation |
| 4VHiptx7xe (STRAP) | 6.25 | R2 | Stronger evaluation design; different approach |
| o2IEmeLL9r (PTGM) | 7.33 | R2 | Stronger paper; cleaner claims |

**Final score determination:** The paper sits between the 5.0–5.5 anchors. It is stronger than "The Power of the Senses" (4.33) and "Human-oriented Repr Learning" (5.00) in both evaluation breadth and results consistency. It is comparable to "Unleashing Large-Scale Video Generative Pre-training" (5.50, Accept) — both have genuine contributions alongside evaluation gaps. The paper's weaknesses (unfair DINOv2 comparison, missing single-modal ablation) are significant but fixable and do not negate the dataset and architectural contributions.

**Score: 5.5 — Accept.** The paper makes real contributions (DROID-3D dataset, multi-modal MAE architecture, extensive evaluation) that advance the field. The main methodological gaps can be addressed with additional controlled experiments.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>
- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 3, 6, 5
I have all the information I need. Let me now produce the final consolidated review.

---

## Summary

This paper proposes fine-tuning a music-to-dance diffusion model (EDGE) using reinforcement learning, where the reward is provided by a physics-based motion imitation policy trained in Isaac Gym. The key idea is that physically implausible motions (body interpenetration, foot sliding) are harder for the imitation policy to replicate, so the imitation error serves as a proxy for physical implausibility. An anti-freezing reward counteracts the tendency of the physics reward to favor small-amplitude motions. Experiments on AIST++ show a 48% reduction in penetration rate and improved foot contact plausibility compared to the base EDGE model, with user studies confirming perceptual improvement.

## Strengths

1. **Significant and well-measured reduction in body interpenetration**: The paper reports a 48% decrease in penetration rate compared to the EDGE baseline (Table 1), with a clear quantitative definition (average number of intersected mesh faces per frame). This directly addresses the skinned-mesh physical implausibility the paper targets.

2. **User study confirms perceptual gains**: Human judges prefer the proposed method over EDGE, Bailando, and FACT in both "Overall" (52.08% vs. 26.32% for EDGE) and "Physical" plausibility ratings (Table 1). This bridges the gap between quantitative metrics and human perception.

3. **Anti-freezing reward demonstrably addresses an identified failure mode**: The ablation (Table 3, Fig. 3b) shows that without the anti-freezing reward, motion magnitude drops to ~0.4710 (near FACT's freezing level), while the full method achieves 0.6877 (close to EDGE). The paper identifies and solves a genuinely non-obvious problem with the imitation reward.

4. **Clear justification for RL fine-tuning over post-processing**: The comparison to "EDGE w/ projection" (Table 2, Fig. 3a) shows that direct post-processing with the imitation policy degrades foot contact (PFC) and causes falling artifacts, while RL fine-tuning avoids these issues by learning to replace problematic motions. This evidence supports the paper's central design choice.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are supported by the evidence; the concerns below are about missing detail and depth of validation rather than fundamental flaws.

### Minor

1. **Missing penetration rate in the anti-freezing ablation**: The ablation for "Ours w/o AF" (Table 3) reports motion magnitude but not penetration rate. Since removing the anti-freezing reward reduces motion amplitude, which could *decrease* penetration (less motion = fewer collisions), it is unclear whether the anti-freezing reward trades off physical plausibility for motion dynamics. Reporting penetration rate for this ablation would clarify whether the physics reward remains effective when freezing is avoided.

2. **Reward combination weights α and β not reported**: Equation 7 (line 106) introduces weights α and β for combining the imitation and anti-freezing rewards. The implementation details (line 132) report weights for the imitation policy's internal reward components (w_s, α_s, w_r, α_r), but the values of α and β for the RL fine-tuning gradient update are not given. This hinders reproducibility.

3. **Smoothness evaluation not conducted**: The anti-freezing reward is defined as \(\overline{v(x_0)^2} + \overline{a(x_0)^2}\). This could incentivize high-frequency jitter (large accelerations) rather than genuinely dynamic motion. No smoothness metric (e.g., jerk, velocity consistency) is reported. The conclusion itself acknowledges the need to "further refine both the physical plausibility and smoothness," suggesting the authors recognize this gap.

4. **User study reporting lacks statistical rigor**: The win rates for "Overall" (52.08% Ours vs. 26.32% EDGE) sum to 78.4%, which implies 21.6% ties or undecided comparisons, but this is not explained. No confidence intervals, standard deviations, or significance tests are reported for the user study or any quantitative metric.

5. **Imitation reward's correlation with physical plausibility is asserted but not directly validated**: The paper argues (Section 3.1) that motions violating physical laws are harder to imitate, so imitation error proxies physical plausibility. While the physics simulator provides face validity, and the downstream metrics (penetration, PFC) improve as expected, the paper does not include a controlled experiment (e.g., taking ground-truth motions, artificially introducing penetrations or foot skating, and demonstrating that the imitation reward drops monotonically with violation magnitude). Such a study would strengthen the chain of reasoning and rule out confounds (e.g., motion speed or style affecting imitation difficulty independently of physical plausibility). This is not a fatal gap—the indirect validation via outcome metrics is reasonable—but it limits interpretability.

6. **Comparison to physics-guided baselines is limited**: The paper implements "EDGE w/ projection" as a post-processing baseline described as "similar to Yuan et al. (2023)." However, PhysDiff (Yuan et al., 2023) integrates physics guidance *within* the diffusion loop at each denoising step, not as a one-shot post-process. The implemented baseline may therefore represent a weaker variant, and a direct comparison with PhysDiff's published results or a faithful re-implementation would better substantiate the advantage of RL fine-tuning over inference-time physics guidance.

### Trivial

- **Penetration rate units lack interpretability context**: The paper reports "average number of intersected faces per frame" (e.g., 434 for Ours vs. 843 for EDGE). Without knowing the total number of mesh faces or a human motion baseline, it is hard for readers to judge whether 434 faces/frame is visually negligible or noticeable.

## Nice-to-Haves

- A controlled experiment corrupting ground-truth motions with known physical violations to directly validate the imitation reward's sensitivity to penetration and foot skating.
- Reporting convergence behavior, number of RL fine-tuning iterations, and wall-clock time for the full pipeline.
- Sensitivity analysis on the reward weight ratio α/β.

## Removed Points

*These points were flagged by the reviewers but are removed or demoted for the reasons given below.*

- **"Circular validation" of the imitation reward**: The harsh critic claimed the reward is "evaluated by the same metrics it is designed to improve," which is factually inaccurate. The imitation reward measures discrepancy between generated and imitated motion; the evaluation metrics (penetration rate, PFC) are independent constructs. Removed as factually incorrect.
- **Generalizability critique (only tested on AIST++ with EDGE)**: The paper explicitly scopes its contribution to the EDGE model and AIST++ dataset. Demanding multi-dataset or multi-model generalization is scope creep. Removed.
- **Missing related work**: The reviewer guidelines instruct not to mention missing related works, as external confirmation is not available. Removed.
- **"Formulation of denoising process as MDP" (Strength Finder)**: This directly follows DDPO (Black et al., 2024) and is a standard adaptation, not a novel strength specific to this paper. Removed.
- **"Two-stage training of imitation policy" (Strength Finder)**: This is a practical implementation detail rather than a core contribution. Removed.

## Novel Insights

None beyond the paper's own contributions. The key observation—that the imitation policy's preference for small-magnitude motions creates a "freezing" problem that requires a separate anti-freezing reward—is the most interesting and non-obvious finding, and it is already well-articulated in the paper.

## Suggestions

1. Report the missing penetration rate for the "Ours w/o AF" ablation and add a brief discussion of whether the anti-freezing reward trades off physical plausibility for motion amplitude.
2. State the values of α and β used in Eq. (7) and, ideally, include a sensitivity analysis.
3. Add a smoothness metric (e.g., mean jerk or acceleration derivative) to verify that the anti-freezing reward does not induce jitter.
4. Clarify how ties are handled in the user study and report confidence intervals or significance tests for win rates.
5. Provide context for the penetration rate (e.g., total mesh face count, a "human motion" reference value) or reframe it as a percentage of total faces.

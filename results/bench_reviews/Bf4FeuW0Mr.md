Now I have all the information I need. Let me write the final review.

## Summary

DemoGrasp proposes a novel framework for universal dexterous grasping that reformulates the task as a single-step MDP where an RL policy learns to edit a single demonstration trajectory — applying SE(3) wrist transformations and delta hand joint angles — rather than exploring in the full low-level action space. A vision-based student policy is then trained via imitation learning on successful RL rollouts for sim-to-real transfer. The method achieves strong simulation results (95.2% state-based success on 3.2K DexGraspNet objects with the Shadow Hand, surpassing prior SOTA by ~4%) and demonstrates zero-shot real-world transfer across 110 objects (86.5% overall, 71.1% on small/thin objects), cross-embodiment generalization across 6 hand types, and extensions to cluttered and language-conditioned grasping.

## Strengths

- **Novel demonstration-editing formulation** dramatically reduces RL exploration complexity. By compactly parameterizing grasping as SE(3) transformation + delta hand joints applied to a single trajectory, the method replaces standard long-horizon RL with a single-step MDP. This is evidenced by Table 5, where RL (96.24%) far outperforms sampling+BC (77.56%) on the same action space.
- **State-of-the-art simulation results on DexGraspNet** (Table 1): 95.2% state-based and 92.2% vision-based success with the Shadow Hand, outperforming UniGraspTransformer (91.2%/88.9%) by meaningful margins. The generalization gap between training and unseen categories is only ~1%.
- **Real-world results on small and thin objects** are genuinely impressive: 71.1% combined success on objects <1.5 cm thick or <3.5 cm diameter, with 95.3% on normal-sized objects across 110 items. This capability is explicitly identified as a novel contribution beyond prior work.
- **Extensive cross-embodiment validation**: Evaluated on 6 different hand types (5-finger, 4-finger, 3-finger, parallel gripper) across 6 object datasets without hyperparameter tuning, achieving an average 84.6% success rate (Table 10). This goes well beyond most prior work that focuses on a single hand.
- **Data efficiency**: Training on only 175 objects yields success rates within 2.4% of training directly on test sets (Table 7), and performance is robust to demonstration quality (Table 9).
- **Thorough ablation studies**: The paper systematically ablates the necessity of RL (Table 5), the contribution of each action component (Table 8), camera configurations (Table 6), and demonstration quality (Table 9).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Uncontrolled baseline comparison in Table 1**: The paper acknowledges that baselines (UniDexGrasp, UniDexGrasp++, UniGraspTransformer) are tested *without* object position randomization, while DemoGrasp uses a 50 cm × 50 cm reset region. The paper frames this as a harder test for their own method, which is reasonable, but the lack of a controlled comparison (baselines with the same randomization, or DemoGrasp without randomization) makes the 4–5% margin uninterpretable as a clean apples-to-apples comparison. A simple ablation removing position randomization for DemoGrasp would clarify how much of the gain is due to the method vs. the different test conditions.
- **Terminology imprecision around "closed-loop"**: The paper correctly acknowledges in Section A that "the policy learned in the RL stage is open-loop," and the vision-based student (which operates per-timestep with action chunking) is indeed closed-loop. However, multiple passages in the abstract and introduction refer broadly to "closed-loop grasping policies" without sufficiently distinguishing the two stages. This creates unnecessary confusion for readers and gives the harsh critic ammunition. The paper would benefit from precise language distinguishing the open-loop RL teacher from the closed-loop vision student.
- **Real-world failure mode analysis is absent**: Table 3 reports per-category success rates but provides no breakdown of *why* objects failed (perception errors, collisions, slips, missed grasps). The paper would be significantly strengthened by a 1-paragraph analysis of the most common failure types, especially given the claim of being "first to grasp" thin/small objects.
- **No confidence intervals or error bars in simulation results**: Tables 1, 2, 5, 7, 8, 9, and 10 report single-run success rates without standard deviations or multiple seeds. While single-run evaluation is common in large-scale robotics RL benchmarks, this is worth noting as a limitation.
- **Motion planner success rate not reported**: The method relies on an interpolation-based motion planner to align the robot to the first demonstration step (Appendix E.1). The paper says the planner works with "minimal tracking error" but does not report its success rate, which is a potential failure source.

### Trivial
- The abstract's "71.1%" for "small, thin objects" is the combined average of the "Flat & Thin" (68.3%) and "Small" (76.7%) categories, which is consistent when properly interpreted. However, the main text reports 68.3% for flat & thin, creating a minor apparent discrepancy that should be clarified.
- The "robust RL framework" claim in the conclusion is somewhat overstated — the method still requires careful simulation setup, demonstration collection, motion planning, and two-stage training.

## Nice-to-Haves

- Controlled baseline comparison with matched position randomization
- Failure mode analysis for real-world experiments
- Confidence intervals / multiple-seed reporting in simulation results

## Removed Points

These points from the harsh critic are flagged for removal; treat them with caution:

1. *"The vision-based student policy is also trained to imitate these open-loop rollouts, meaning it too is an open-loop policy"* — **Factually wrong.** The vision-based policy (Section 2.4) takes observations at each timestep and outputs actions via action chunking with receding-horizon control (per-timestep observations → per-timestep actions), which is closed-loop. The data source does not determine whether the policy is open- or closed-loop.
2. *"The paper provides no insight [about vision-to-state gap]"* — **Factually wrong.** The paper shows the gap (95.2% → 92.2%, Table 1) and provides extensive analysis in Appendix D.3 comparing vision-based vs. state-based RL training curves (Figures 9, 10).
3. *"The 71.1% [flat & thin average] doesn't add up"* — **Misunderstanding.** 71.1% is the combined average of Flat & Thin (68.3%, 24 objects) and Small (76.7%, 12 objects): (24×68.3 + 12×76.7)/36 ≈ 71.1%. The paper's abstract says "small, thin objects" (both categories), and the main text separately reports 68.3% and 76.7%. The math is consistent.
4. *"Table 8 test set success rates (82.74%) are surprisingly low compared to Table 1 (95%+)"* — **Misreading.** Table 8 uses 175 training objects tested on 5 unseen out-of-distribution datasets (DGA, EGAD, etc.). Table 1 uses 3,200 training objects tested on DexGraspNet test sets. These are different experimental setups, clearly described in Sections 3.2 and 3.3.
5. *"The paper does not discuss how varying T_ee and Δq covers different approach strategies (scooping vs. pinching)"* — **Scope creep.** The paper focuses on grasping, not general manipulation. Scooping vs. pinching are different manipulation primitives, not different grasping strategies.
6. *"The paper claims SOTA without sufficient evidence"* — The evidence is substantial: large-scale simulation (3,200 objects), cross-embodiment (6 hands), and real-world (110 objects). The baseline comparison concern is acknowledged but doesn't invalidate the SOTA claim.

## Novel Insights

The reviewer criticism about the closed-loop/open-loop framing, while overblown, actually points to an interesting tension in the paper: the demonstration-editing formulation is elegantly simple *because* it is open-loop at the RL stage, but the paper simultaneously claims closed-loop capability through the vision-based student. This two-stage design (open-loop teacher for efficient exploration, closed-loop student for reactive deployment) creates a genuine and under-explored design space — breaking manipulation trajectories into edit parameters at one level and re-synthesizing reactive control at another. The paper's approach of having the RL stage optimize coarse trajectory parameters (where and how to grasp) while the imitation stage learns per-timestep visuomotor mappings is a clean division of labor that future work could extend to other manipulation domains (e.g., breaking trajectories into segments for segment-level editing to achieve finer-grained closed-loop behavior, as the paper itself suggests in limitations). The ablation showing that the method works robustly regardless of which specific demonstration is used (Table 9) is an underappreciated result — it suggests the editing parameter space is sufficiently expressive to absorb large variations in initial trajectory quality, which has practical implications for real-world deployment where obtaining "optimal" demonstrations is costly.

## Suggestions

1. Add a controlled ablation where baselines are evaluated *with* the same position randomization, or where DemoGrasp is evaluated *without* it, to cleanly separate the contribution of the method from the test conditions.
2. Add a 1-paragraph failure mode analysis for the real-world experiments (perception vs. collision vs. slip vs. missed grasp), even if qualitative.
3. Clarify the terminology throughout: clearly distinguish the open-loop RL teacher from the closed-loop vision student early in the paper, not just in the limitations appendix.
4. Report simulation results with standard deviations across 3 random seeds for the main tables.
5. Clarify the "71.1%" / "68.3%" discrepancy between the abstract and the main text with a brief note.

## Score and Decision

**Calibration anchors** (all from /home/wg25r/review_agent/human_reviews_2026/):

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| EquAct (d1wuA8oIH0.md) | 7.00 | Stronger theoretical contribution (equivariance guarantees) but narrower evaluation scope. DemoGrasp has more practical real-world validation. |
| DexNDM (80vjyj5o7l.md) | 6.00 | Comparable — strong sim-to-real for in-hand rotation. DemoGrasp has broader object/hand generalization but lacks theoretical grounding. Similar tier. |
| D-REX (13jshGCK9i.md) | 5.50 | Accept — good real-to-sim-to-real pipeline but limited real-world object diversity. DemoGrasp stronger on real-world scale and novelty of formulation. |
| XDex (VJqfoHU4Op.md) | 4.50 | Withdrawn/reject — grasp synthesis without closed-loop control. DemoGrasp is a more complete system. |
| FastGrasp (Q60D8jF4KI.md) | 4.00 | Reject — low real-world success rates (20-25%), narrower scope. DemoGrasp substantially stronger. |
| ACPPO (WFQnqY1c39.md) | 3.00 | Withdrawn/reject — incremental RL improvement. DemoGrasp has a genuinely novel formulation. |

In the low range, Score<2 papers (HeMyWG4uYe.md, YAYhkZYRNY.md, 1CR1MTIgmq.md — scores 0.67–2.00) are clearly much weaker than DemoGrasp (fundamentally flawed or off-topic). DemoGrasp sits comfortably above the reject-range papers and is comparable to mid-range accepts.

Relative to the anchors, DemoGrasp is stronger than typical reject-scoring robot learning papers (3.0–4.5) and comparable to accept-scoring papers (5.5–6.0). Its weaknesses are real but addressable and do not undermine the core contribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
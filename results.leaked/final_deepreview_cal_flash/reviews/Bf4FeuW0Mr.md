## Summary

DemoGrasp proposes a simple yet effective framework for universal dexterous grasping. The core idea is to formulate each grasping trial as a *single-step MDP* where a policy outputs editing parameters (SE(3) wrist transformation + delta hand joint angles) that modify a single demonstration trajectory, which is then replayed open-loop. This reformulation collapses the long-horizon exploration problem into a compact, low-dimensional decision, enabling a simple binary success + collision penalty reward to suffice. The state-based RL policy achieves 95.2% on DexGraspNet objects (Shadow hand), and the vision-based policy (trained via flow-matching imitation learning from rendered rollouts) transfers zero-shot to a real robot, achieving 86.5% success on 110 unseen objects including small and thin items. The method also demonstrates strong cross-embodiment transfer across six different hands and extends to language-guided cluttered grasping.

## Strengths

- **Clean problem reformulation that dramatically simplifies exploration.** Modeling grasping as editing a single demonstration via a single-step MDP is a genuinely clever idea. By restricting the action space to SE(3) + delta joint angles and the horizon to a single decision, the paper eliminates the need for dense reward shaping, curriculum learning, or multi-stage distillation that prior methods require. This is well-supported by the method description (Sections 2.2–2.3) and the ablation in Table 8 showing monotonic improvement as each editing dimension is added.

- **Strong empirical results across simulation and real-world settings.** On DexGraspNet (Table 1), DemoGrasp achieves 95.2% state-based and 92.2% vision-based success rates, outperforming UniGraspTransformer by 4–5 points. The cross-dataset generalization (Table 2) matches or exceeds RobustDexGrasp on 4/5 datasets despite training on only 175 objects. Cross-embodiment results (Figure 3) show an average 84.6% success across six different hands on unseen datasets. The real-world evaluation on 110 objects—covering normal (95.3%), thin/<1.5cm (68.3%), and small/<3.5cm (76.7%) objects—is extensive and convincing.

- **Thorough ablation studies that validate the core design choices.** Table 5 directly shows RL substantially outperforms sampling+BC (96.24% vs. 77.56%), confirming that RL's unimodal optimization is critical. Table 8 decomposes the action space contributions. Table 9 demonstrates robustness to demonstration quality (all demonstrations produce ≈95% policy success despite replay ranging from 3.88% to 75.29%). Table 7 shows training on just 175 objects is nearly as good as training on the test sets directly (+2.4% marginal gain).

- **Practical sim-to-real transfer with sensible design.** The vision-based pipeline uses flow-matching on rendered images with domain randomization, comparing multiple camera configurations (Table 6). Two-view RGB outperforms depth on small/thin objects, and the extension to language-conditioned cluttered grasping (Table 4) shows the framework's extensibility.

## Weaknesses

### Fatal
None.

### Major

- **DexGraspNet comparison (Table 1) is not under a fully matched evaluation protocol.** The paper openly states that baseline methods do not randomize object initial positions, whereas DemoGrasp is trained and tested with 50 cm × 50 cm spatial randomization. While the paper argues this makes DemoGrasp's condition *harder* (and DemoGrasp still wins by 4–5 points), this is a reasonable argument rather than a controlled apples-to-apples comparison. The headline claim of "surpassing previous state-of-the-art methods by a large margin" would be on firmer ground if the baselines were evaluated under the same random-position condition (or DemoGrasp under the fixed-position condition). The concern is that we do not know how the baselines would fare with position randomization—they could drop further, making the gap larger, or they could hold steady. Without this control, the exact margin is uncertain. This issue is acknowledged by the paper but not addressed experimentally.

### Minor

- **The "first to grasp small, thin objects" claim lacks direct comparative evidence.** The paper states that prior work (Singh et al. 2024, Zhang et al. 2025b) "still fall short on grasping small, thin objects" and claims that DemoGrasp is "to our knowledge, the first" to succeed on these objects. However, no direct comparison with those methods is provided on the same objects or in a controlled simulation setting. The real-world results on thin/small objects are impressive on their own terms, but the priority claim would be strengthened by even a small-scale comparison on a shared test set. The paper's framing mildly over-reaches here.

- **Cross-embodiment results (Section 3.3) are reported only for the state-based policy.** The vision-based policy, which is what runs on the real robot, is trained via imitation learning from state-based rollouts. On DexGraspNet (Table 1), the vision-based policy is ~3 points lower than the state-based one. Since no vision-based numbers are reported for the cross-embodiment or cross-dataset settings, readers cannot assess how much of the strong simulation performance would survive the state→vision drop in those more challenging generalization regimes. This limits the ability to connect the simulation and real-world results.

- **No systematic failure analysis.** The paper mentions regrasp behavior (Figure 7 caption) but does not break down why failures occur (perception errors, grasp instability, collisions with the table or object, etc.). A brief discussion of common failure modes would help readers understand the practical limitations of the method.

- **Missing RL-from-scratch baseline.** The ablation in Table 5 compares RL against sampling+BC, but does not include what would happen if RL were trained from scratch in the original high-dimensional action space without demonstration editing. While the paper motivates why this is infeasible, having a quantitative comparison—even showing near-zero success—would strengthen the motivation for the demonstration-editing formulation.

### Trivial
None.

## Nice-to-Haves

- Reporting standard deviations or confidence intervals for simulation results (especially Table 1, Table 2) would improve statistical rigor, though single-run large-scale evaluation is standard in this sub-field.
- The cluttered-scene real-world evaluation (Table 4) would benefit from stating the number of trials explicitly alongside the percentages.
- A more explicit discussion of limitations (e.g., reliance on known initial object pose during state-based training, sensitivity to camera placement) in the conclusion would improve the paper's completeness.

## Removed Points

These points were flagged by the reviewers but are removed or downgraded after cross-checking against the paper:

- **"Details of the RL algorithm and point cloud encoder missing from main text"** — The paper defers these to Appendix E, which is standard practice for conference papers. Not a weakness.
- **"Reproducibility concern: undisclosed hyperparameters"** — Appendix E is stripped by the parser; these details exist in the original submission.
- **"Statistical variability not reported"** — Demoted to Nice-to-Have. Large-scale simulation benchmarks in the dexterous grasping literature routinely report point estimates without variance, so this is not a weakness relative to community standards.
- **"Radar chart table shows identical numbers"** — This is a PDF extraction artifact. The actual figure in the original PDF contains varying values as the surrounding text confirms ("FR3+Gripper performs worse on EGAD and DGA, because the Panda gripper's limited stroke hinders grasping wide or large objects").
- **Claims questioning the existence/availability of cited methods** — All cited works are assumed to exist as per the review guidelines.

## Novel Insights

The review process surfaces a genuinely useful observation beyond the paper's own contributions: the single-step MDP formulation effectively separates the *decision* problem (where and how to edit the demonstration) from the *execution* problem (replaying the edited trajectory). This separation is what enables the simple binary reward to work—the policy never needs to reason about low-level dynamics or contact sequences, only about the geometric editing parameters. An interesting question this raises is whether the same principle could apply to other long-horizon manipulation tasks (e.g., insertion, folding) where a single successful demonstration can be decomposed into task-relevant editing parameters and fixed execution patterns. The paper's demonstration-robustness results (Table 9) further suggest the editing policy learns a surprisingly general mapping from object geometry to editing parameters, independent of the demonstration specifics—hinting that the demonstration primarily serves as a motion prior rather than a task template.

## Suggestions

- **Address the evaluation protocol mismatch:** The single highest-impact improvement would be to evaluate DemoGrasp *without* position randomization on the DexGraspNet test set to match the baseline protocol, and report both settings side by side. This would either confirm the margin (if the gap holds) or bound it (if it narrows), and either outcome would be informative.
- **Add a small-scale real-world baseline comparison on thin objects:** Even testing one prior method (e.g., RobustDexGrasp's provided checkpoint) on 10–15 challenging thin objects on the same hardware would substantially back the "first to grasp" claim.
- **Report vision-based simulation results for cross-embodiment settings** to bridge the simulation-to-real interpretability gap.
- **Include a brief failure-mode analysis** (e.g., "80% of failures were due to perception errors on transparent objects, 20% due to grasp instability on very heavy objects") in the real-world experiments section.

## Score and Decision

**Calibration protocol summary:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Cross-Embodiment Dexterous Grasping | 5.00 | R1 | Weaker: limited real-world, less comprehensive experiments |
| ManiBox | 5.25 | R1 | Weaker: simpler task (parallel gripper), limited object diversity |
| SparseDFF | 6.00 | R2 | Slightly weaker: narrower scope, less extensive evaluation |
| ResDex (Efficient Residual Learning with MoE) | 7.00 | R2 | Comparable: similar topic but simulation-only; DemoGrasp adds real-world but has comparison fairness concern |
| DexTrack | 6.25 | R1 | Different focus (tracking control); broader scope of DemoGrasp makes it stronger |
| One-Step Diffusion Policy | 5.75 | R3 | Different focus (distillation); DemoGrasp more comprehensive |

**Round 1 bracket:** I identified weak (<3.5), middle (3.5–7.5), and strong (>7.5) bands. The paper clearly sits in the middle-to-strong band given its extensive experiments, real-world transfer, and novel formulation. Papers in the weak band lack real-world experiments or have much narrower scope. Papers in the strong band (>7.5) tend to have exceptional breadth or a transformative result that this paper, despite its strengths, does not quite match.

**Round 2 narrowing:** Within the 3.5–7.5 bracket, I narrowed to compare against papers scoring 5.5–8.0. ResDex (7.0) is the most directly comparable anchor: both address universal dexterous grasping with RL, both achieve SOTA on DexGraspNet. DemoGrasp is stronger on experimental breadth (real-world, cross-embodiment, ablations) and raw performance (95.2% vs. 88.8%), but the comparison protocol issue in Table 1 is a concern that ResDex does not share. On balance, the paper is comparable to ResDex (7.0) and clearly stronger than papers at 5.0–6.25.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
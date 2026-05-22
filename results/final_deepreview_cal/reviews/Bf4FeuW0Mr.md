Here is the final consolidated review.

---

## Summary

DemoGrasp proposes a framework that uses a single demonstration trajectory and a single-step MDP with a compact action space (SE(3) transformation + delta hand joints) to learn a universal dexterous grasping policy via RL, eliminating complex reward engineering. The policy is trained across hundreds of objects in parallel in simulation with a simple binary success × collision-penalty reward, then distilled into a flow-matching vision policy for sim-to-real. The paper reports 95% success on DexGraspNet (Shadow Hand), 84.6% average across six unseen datasets and six different embodiments, and 86.5% on 110 real-world objects including small/thin items.

## Strengths

- **Genuinely novel formulation elegantly addresses the exploration challenge.** The insight of treating universal grasping as demonstration editing — decomposing the problem into "where to grasp" (SE(3) wrist transformation) and "how to grasp" (delta hand joints) via a single-step MDP — is clean and principled. This eliminates the need for complex reward shaping and curriculum learning that prior methods require (Section 2.2–2.3).

- **Extensive and convincing evaluation across multiple axes.** The paper evaluates on (a) DexGraspNet with Shadow Hand (Table 1: 95.2% state-based, beating UniGraspTransformer by 4–5%), (b) cross-dataset generalization across 5 unseen datasets with the Allegro Hand (Table 2), (c) cross-embodiment transfer across 6 different hands including parallel gripper (Figure 3, Table 10: 84.6% average), (d) real-world grasping on 110 objects (Table 3: 95.3% normal-sized, 71.1% flat/thin, 76.7% small), and (e) cluttered scenes and language-guided grasping (Table 4: >80%).

- **Demonstrated first-of-its-kind capability on small/thin objects in tabletop settings.** The paper achieves 68.3–76.7% success on flat/thin and small objects in the real world (Table 3), which prior work has explicitly struggled with (Section 1). The reward design with 50% collision detection disabling (Section 2.3) enables finger-table contact when needed, a practical insight validated by real-world results.

- **Thorough ablations support the design choices.** Tables 5 (sampling vs. RL), 8 (action space components), 7 (training set size), and 9 (demonstration quality) systematically validate each component. The demonstration quality ablation (Table 9) is particularly strong: even with a poor demo achieving 3.88% direct replay, the RL policy recovers to 95.27%.

- **Strong cross-embodiment results without hyperparameter tuning.** Training on 175 objects and transferring to six embodiments (including multi-fingered hands and a parallel gripper) with zero tuning (Figure 3) demonstrates the method's universality beyond the typical single-hand evaluation common in this area.

## Weaknesses

### Major

- **Asymmetric baseline comparison on DexGraspNet undermines the headline SOTA claim.** The paper explicitly states (Section 3.2, line 149) that "the baseline methods do not randomize object initial positions, whereas our method is trained and tested with a large reset region of 50 cm × 50 cm." This means the reported 4–5% improvement over prior methods is not an apples-to-apples comparison: baselines were tested on fixed-position objects while DemoGrasp was tested on spatially randomized ones, and vice versa. The paper's explanation — that spatial randomization does not hurt DemoGrasp due to translation invariance of the replay mechanism — is plausible, but no controlled experiment is provided (e.g., evaluating DemoGrasp without spatial randomization, or retraining baselines with it). The abstract, Figure 1, and headline claims present the DexGraspNet result as direct SOTA superiority without this caveat. This does not invalidate the overall contribution — which rests on much broader evaluation — but it weakens the most prominent quantitative claim.

### Minor

- **Vision-based policy lacks ablation against simpler alternatives.** The real-world pipeline uses flow matching (Section 2.4) trained on successful RL rollouts. The paper claims flow matching models multimodal action distributions but provides no comparison to a simpler alternative (e.g., behavioral cloning with MSE loss, Gaussian mixture model, or diffusion policy) on the same rollout data. Without this, it is unclear whether the choice of imitation learning method matters for the reported real-world performance.

- **No discussion of limitations or failure modes.** The paper lacks any limitations section and the conclusion does not discuss scenarios where the method may fail. The linear interpolation in Equation (2) preserves the relative timing of finger closure from the demonstration, which may be suboptimal for objects requiring different coordination patterns (e.g., scooping, in-hand reorientation before lifting). The assumption that all successful grasps are small deviations from a single template trajectory is not bounded. While the strong empirical results partially mitigate this, an explicit discussion would strengthen the paper.

- **The 50% collision-detection disabling rate is not ablated.** The reward design (Section 2.3) uses a 50% random disable rate for robot-table collision detection to enable finger-table contact for thin objects. This hyperparameter is not subjected to a sensitivity analysis, leaving the reader to wonder whether performance on thin objects is sensitive to this specific rate.

### Trivial

- **Per-object real-world results are not reported.** Table 3 aggregates successes into categories (bottles, boxes, flat/thin tools, etc.) but individual object results would allow identification of systematic failure modes and improve reproducibility.

## Nice-to-Haves

- A controlled comparison on DexGraspNet where baselines are retrained with spatial randomization, or DemoGrasp is evaluated without it, to establish a direct apples-to-apples margin.
- A per-object success table for the 110 real-world objects.
- A visualization or analysis of what the learned editing parameters actually change for diverse objects (e.g., for a thin object, does the wrist rotate downward and hand open more?).

## Removed Points

The following points from the source reviews are removed:

- **"Duplicate rows in radar chart table"**: The table under Figure 3 shows identical numbers across all six rows. This is a PDF parsing/formatting artifact — the radar chart clearly shows different values for different embodiments. Not a paper error.
- **"Cannot independently verify cited models"**: The paper cites models, benchmarks, and datasets that exist in the literature. Removing per the hard rules about doubting cited entities.
- **"Comparative baseline asymmetry favors the baseline" complaint about RobustDexGrasp**: Table 2 compares DemoGrasp against RobustDexGrasp on unseen datasets in a zero-shot setting; both methods see these datasets for the first time. The paper explains this forms a fair comparison (line 160). This criticism is factually incorrect about the comparison being unfair.
- **Various formatting/style nitpicks**: Removed per hard rules about parser artifacts.
- **Generic strength claims** ("addresses an important problem," "well-written"): Dropped per the filter on generic/superficial strengths.

## Novel Insights

Beyond the paper's own contributions, the reviews surface an interesting tension: DemoGrasp's key strength (the strong priors from a single demonstration that dramatically simplify RL) is also its key architectural limitation (the linear editing parameterization bounds the space of expressible grasps). The paper resolves this tension empirically — showing the approach works across remarkably diverse objects and embodiments — rather than theoretically characterizing the grasp space it can and cannot represent. This empirical-first strategy is well-suited to the current state of robotic manipulation research, where the space of "things that work" is not yet well-mapped, but it means the method's fundamental limits remain undefined.

## Suggestions for Authors

1. **Provide a fair baseline comparison on DexGraspNet.** Either retrain the strongest baseline (UniGraspTransformer) with spatial randomization in the same 50 cm × 50 cm region, or evaluate DemoGrasp without spatial randomization and report both conditions. This would either validate or bound the 4–5% improvement claim.
2. **Add a simple ablation for the vision policy.** A comparison against BC with MSE loss or a Gaussian mixture model on the same rollout data would confirm whether flow matching's multimodality matters.
3. **Write a brief limitations paragraph** in the conclusion or a dedicated section, discussing when the linear editing assumption may fail (e.g., objects requiring in-hand reorientation, scooping motions, or significantly different lifting strategies).
4. **Add per-object real-world results** (even as supplementary material) to allow identification of systematic failure modes.

## Score and Decision

**Bracket (Round 1):** 5–8, based on comparison to cross-embodiment grasping (5.0), ResDex (7.0), and top-tier manipulation papers (8.0).

**Narrowing (Round 2):** Compared to ResDex (7.0 avg, pure simulation, no real-world, no cross-embodiment), DemoGrasp has more complete evaluation but the spatial randomization issue weakens its headline SOTA claim. Compared to PIDM (7.5 avg, broader manipulation scope), DemoGrasp is narrower but achieves more impressive results in its domain. The paper is positioned between these anchors: stronger than ResDex due to real-world and cross-embodiment results, but held back from the 7.5+ range by the asymmetric comparison.

**Final score:** 7.0

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
Now I have a thorough understanding of the paper and the calibration anchors. Let me synthesize the final review.

---

## Summary

DemoGrasp proposes a framework for universal dexterous grasping that reformulates the problem as demonstration editing: a single successful grasp demonstration is adapted to novel objects by having an RL policy output SE(3) wrist transformations and hand joint deltas in a single-step MDP. This compact action space dramatically reduces exploration burden, enabling a simple binary success + collision reward to achieve 95.2% state-based success on DexGraspNet (surpassing prior SOTA by 4–5%). A vision-based flow-matching policy distilled from RL rollouts transfers zero-shot to a real robot, grasping 110 unseen objects with 86.5% overall success (95.3% on normal-sized, 71.1% on thin/flat). The method also generalizes across six diverse robotic embodiments without per-hand tuning.

## Strengths

- **Novel and effective problem reformulation.** The demonstration-editing formulation reduces the long-horizon, high-dimensional grasping problem to a single-step MDP with a compact action space (Section 2.3). This enables simple RL with a binary reward, yet achieves 95.2% state-based success on DexGraspNet — 4% higher than the previous SOTA UniGraspTransformer (Table 1). The simplicity of the reward (Eq. 3) contrasts sharply with the complex reward shaping used by prior work.

- **Strong cross-embodiment generality with zero hyperparameter tuning.** Trained on only 175 objects, DemoGrasp achieves an average 84.6% success rate across six unseen object datasets and six different robotic hands (five-fingered, four-fingered, three-fingered, and parallel gripper), all mounted on arms (Table 10, Figure 3). This demonstrates the method is not hand-specific and transfers across dramatically different morphologies without any tuning.

- **Thorough ablation studies.** The paper systematically ablates every design choice: RL vs. sampling+BC (Table 5, 77.6% → 96.2%), action-space components (Table 8, incrementally adding wrist translation, rotation, and hand deltas), demonstration quality (Table 9, robust to different demos), training set size (Table 7, 175 objects nearly matches training on all test sets), and camera configurations (Table 6). These provide convincing evidence for each component.

- **Substantial real-world evaluation.** The vision-based policy is tested on 110 real-world objects across diverse categories (Table 3), including challenging thin/flat and small objects that prior work struggled with. The policy also handles cluttered scenes with language instructions at >80% success in both simulation and real-world tests (Table 4), and exhibits emergent regrasp behavior (Figure 7).

- **Versatile input modalities and scene configurations.** The method supports RGB and depth, monocular and two-camera setups, and extends to language-conditioned grasping in clutter with randomized backgrounds and lighting (Tables 4, 6). This practical extensibility is well-demonstrated.

## Weaknesses

### Fatal

None.

### Major

- **No real-world baseline comparison.** The paper claims state-of-the-art performance in real-world dexterous grasping (lines 155–156, 141–142), yet Section 3.4 reports only standalone success rates without any side-by-side comparison against prior sim-to-real methods (e.g., RobustDexGrasp, DextrAH-RGB) on the same hardware, object set, and protocol. The simulation comparisons (Tables 1–2) are strong, and the absolute real-world numbers (86.5% on 110 objects) are impressive, but the claim of real-world SOTA is not directly substantiated. Reproducing other sim-to-real pipelines is admittedly a high bar, but without it the "state-of-the-art" framing for real-world results overreaches. The claim about being "the first to grasp small, thin objects without severe collisions" is better supported by the related-work discussion (Appendix B, lines 1109–1125) documenting prior methods' failures on these object types, though a direct comparative experiment would be more convincing.

### Minor

- **Teacher penetration reward lacks quantitative analysis.** The reward design that randomly disables robot–table collision detection for half the environments (Section 2.3, lines 322–330) is well-justified conceptually — thin/flat objects genuinely require slight table contact for the fingers to reach underneath. And the real-world success rates (71.1% on thin objects) and qualitative results (Figure 7, "Slight robot–table contact is leveraged to grasp tiny objects") show the approach works. However, the paper provides no quantitative analysis of how frequently the teacher policy uses the penetrating mode, what proportion of the student's imitation dataset comes from penetrating rollouts, or collision-force statistics from real-world trials. Such analysis would strengthen confidence that the teacher is not exploiting physically unrealistic penetration and that the student policy has learned safe behaviors.

- **Success criteria alignment with baselines not independently verified.** Table 1 compares DemoGrasp against UniDexGrasp, UniDexGrasp++, and UniGraspTransformer using a success criterion (lift ≥ 10 cm, hand–object distance < 12 cm). The paper states it "follows the settings of previous … methods" (line 410) but does not confirm that the compared works use identical thresholds, hold times, or termination conditions. If baselines used stricter criteria, the reported 4–5% gap could be slightly inflated. The gap magnitude makes it unlikely that threshold differences would reverse the conclusion, but explicit verification would remove this doubt.

### Trivial

- The open-loop nature of the RL teacher is explicitly acknowledged as a limitation in Appendix A (lines 1057–1062), and the vision-based student policy operates closed-loop with demonstrated regrasp behavior (Figure 7). This is not a hidden flaw.

## Nice-to-Haves

- A real-world head-to-head comparison against RobustDexGrasp or DextrAH-RGB on a shared subset of objects would elevate the real-world claims from "strong standalone results" to "demonstrated superiority."
- Quantitative collision statistics (contact forces, penetration depth, frequency) from real-world trials, particularly for thin/small objects, would directly address any remaining sim-to-real safety concerns.
- Letting the RL policy also modify the lifting timestep `T_lift` (currently fixed by the demonstration) could increase expressiveness and is a natural extension of the editing framework.
- An analysis of what proportion of the student's imitation dataset comes from penetrating teacher rollouts would illuminate how the teacher's permissive collision mode influences the final policy.

## Removed Points

These points from the Harsh Critic were considered but either misread the paper, are scope creep, or are standard-practice issues that do not constitute weaknesses:

- **"Unverified alignment of success criteria" is elevated to a fatal gap.** Removed from fatal/major tier. The paper explicitly states it follows prior methods' settings. While explicit verification would be ideal, this is standard practice in the field and unlikely to meaningfully change conclusions given the 4–5% margin.

- **"Open-loop single-step teacher vs. closed-loop deployment" presented as a methodological gap.** The paper explicitly discusses this limitation in Appendix A and the student policy is closed-loop by design. The critic's framing as an undisclosed gap misrepresents the paper.

- **Demand for adaptive `T_lift` and safety-constrained distillation.** These are scope creep — reasonable future work, not weaknesses of the current contribution.

- **Formatting/style/typo nitpicks.** These are parser artifacts and not present in the original submission.

Strength Finder points removed:
- None of the Strength Finder's points were dropped — all were verified as substantiated by specific citations and concrete evidence.

## Novel Insights

The paper's key insight — that a single demonstration trajectory encodes transferable patterns (approach direction, hand closure, lifting) that can be edited via a compact parameterization to achieve universal grasping — is genuinely novel for the dexterous grasping literature. Prior work either used demonstrations for imitation learning (requiring many demonstrations) or used RL from scratch with complex rewards. The single-step MDP reformulation effectively bridges these paradigms: the demonstration provides structure, and RL provides optimization. The finding that this simple formulation, with only 175 training objects, generalizes across six hand embodiments without tuning is a non-trivial empirical result that suggests demonstration editing captures task structure in a way that transfers across morphology. Beyond the paper's own contributions, this suggests a broader principle: for tasks where a single demonstration encodes the task's "grammar," RL over a compact editing space may be more effective than RL over raw actions or pure imitation.

## Suggestions

- Tone down the real-world SOTA claim or reframe it as "demonstrates strong real-world performance" unless a direct comparison is added. The simulation SOTA claim is fully supported.
- Add a brief quantitative analysis in the camera-ready: what fraction of teacher rollouts use penetration mode for thin vs. normal objects, and what collision rate is observed in real-world trials. Even approximate numbers would substantially address the penetration concern.
- Explicitly confirm (e.g., via a footnote or appendix note) that the success criteria for Table 1 baselines match your own, or report what criteria the baselines originally used.

## Score and Decision

**Calibration anchor comparison:**

- `/home/wg25r/review_agent/human_reviews_2026/80vjyj5o7l.md` (DexNDM, avg 6.00, Accept Poster): Had real-world results on 1 hand, theoretical component with mixed reception. DemoGrasp has broader cross-embodiment evaluation (6 hands), more real-world objects (110), and a cleaner method. **DemoGrasp is stronger.**

- `/home/wg25r/review_agent/human_reviews_2026/13jshGCK9i.md` (D-REX, avg 5.50, Accept Poster): Novel differentiable-physics approach but with limited generalization and missing evaluation components. DemoGrasp has more comprehensive evaluation and stronger absolute results. **DemoGrasp is stronger.**

- `/home/wg25r/review_agent/human_reviews_2026/cVX3VqO8BO.md` (UniHM, avg 5.50, Accept Poster): Vision-language dexterous manipulation, trained on human-object interaction data. Different task but comparable scope. DemoGrasp has more thorough real-world evaluation. **DemoGrasp is comparable or stronger.**

- `/home/wg25r/review_agent/human_reviews_2026/3c6bnSJwDg.md` (DexMachina, avg 5.50, Reject): Bimanual dexterous manipulation with curriculum learning. Had mixed reviews. DemoGrasp has clearer contributions and stronger results. **DemoGrasp is stronger.**

- `/home/wg25r/review_agent/human_reviews_2026/aoNqu2N8MC.md` (ExDex, avg 4.50, Withdrawn/Reject): Non-prehensile manipulation. Niche scope, limited evaluation. **DemoGrasp is significantly stronger.**

- `/home/wg25r/review_agent/human_reviews_2026/VJqfoHU4Op.md` (XDex, avg 4.50, Withdrawn/Reject): Cross-embodiment grasp generation, missing appendix. DemoGrasp has more thorough evaluation and real-world results. **DemoGrasp is significantly stronger.**

- `/home/wg25r/review_agent/human_reviews_2026/Q60D8jF4KI.md` (FastGrasp, avg 4.00, Reject): Mobile grasping, 20–25% real-world success, limited novelty. **DemoGrasp is vastly stronger.**

- `/home/wg25r/review_agent/human_reviews_2026/WFQnqY1c39.md` (AC-PPO, avg 3.00, Withdrawn/Reject): Incremental PPO variant on DexGraspNet. **DemoGrasp is vastly stronger.**

DemoGrasp compares favorably against all retrieved anchors. It has a genuinely novel method, SOTA simulation results with thorough ablations, impressive cross-embodiment generalization, and substantial real-world evaluation. The main gap — no real-world baseline comparison — is real but does not undermine the core contributions. This is a clear accept with a score above the 5.5–6.0 range.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
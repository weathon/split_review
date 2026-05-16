Now I have all the evidence needed. Let me write the consolidated review.

## Summary

MS-HAB presents a GPU-accelerated implementation of the Home Assistant Benchmark (HAB) that replaces Habitat 2.0's teleport-based "magical grasp" with physics-based low-level manipulation. The paper contributes: (1) a 3× faster simulation (4109 SPS) via GPU parallelization, (2) extensive RL/IL baselines (150 policies, 1.83B samples), (3) an automated trajectory categorization/filtering system, and (4) a dataset with controlled demonstration filtering. The strongest result is the per-object vs. all-object policy analysis, which demonstrates that overfitting to specific object geometries meaningfully improves grasping success on difficult objects (e.g., the Cracker Box).

## Strengths

- **Validated 3× simulation speedup over Habitat 2.0**: Section 4.2 and Figure 1 show MS-HAB achieves 4109 SPS with 1024 parallel environments vs. Habitat 2.0's 1397 SPS peak, at similar GPU memory, while supporting low-level control and rendering two RGB-D cameras. This is a clear, measurable engineering contribution.

- **First GPU-accelerated HAB with non-teleport low-level control**: The paper replaces magical grasp with joint-level physics-based manipulation, requiring the Fetch robot to learn valid, stable, and reachable grasp poses. This is a genuine capability upgrade over the original HAB and Habitat 2.0, which the paper consistently contrasts and differentiates.

- **Extensive baselines with systematic evaluation**: Training 150 policies across 3 seeds (1.83B environment samples) and reporting per-subtask success rates (Table 1), long-horizon progressive completion (Figure 3), and specific failure-mode analysis (e.g., Close Fridge failing on validation due to door-into-wall geometry) provides concrete performance targets and diagnostic tools for future work.

- **Per-object vs. all-object policy analysis yields actionable insight**: Table 2 shows that for the YCB Cracker Box (object #003), the all-object policy is 1.88–2.42× more likely to fail from excessive collisions and 1.87–12.37× more likely to fail to grasp compared to the per-object policy. This is the most informative experimental result in the paper — it reveals a genuine design principle for low-level control under tight tolerances.

- **Honest limitation disclosure**: Section 7 explicitly states "we do not claim transfer to real robots" and acknowledges significant room for improvement. The optimistic upper bound in Figure 3 is clearly labeled as incorrect. This candor builds credibility.

## Weaknesses

### Major

- **No floor characterization for the benchmark tasks**. The long-horizon completion rates are very low (TidyHouse RL ~8%, SetTable RL ~4%, PrepareGroceries ~2%), and the paper does not establish whether these tasks are genuinely difficult or underspecified. No random policy baseline, no hand-designed scripted policy, and no analysis of variance across seeds is provided. Without knowing chance performance or the minimum success floor, readers cannot determine whether the tasks are *differentiating* — i.e., whether the gap between methods would be detectable above noise. For a benchmark paper, this is the most significant gap: the utility of the benchmark for comparing methods is asserted, not demonstrated. The per-subtask success rates (Pick 30–70%+) are more reasonable, but the long-horizon compounding is not contextualized.

- **The "realistic" language is overclaimed relative to what is validated**. The words "realistic" or "realistic grasping/manipulation" appear approximately a dozen times across the abstract, introduction, and Section 4. The paper validates that the simulation uses low-level joint control rather than teleportation, which is a meaningful distinction from magical grasp. However, it does not validate that the resulting physics is *realistic* in any measurable sense — no analysis of grasp stability, joint torque limits, contact force magnitudes relative to physical limits, or kinematic plausibility of learned grasps within the simulator itself. The paper disclaims real-robot transfer, but the "realistic" claim is about simulation fidelity, not transfer. The contrast with magical grasp is clear and valuable; the rhetorical frame of "realistic" goes beyond what the experiments demonstrate.

### Minor

- **The trajectory filtering system's demonstrated utility is modest**. The IL filtering experiment (Table 3) shows that filtering by behavior mode biases policy output only partially — even the "place" filtered policy produces a 42:58 place:drop ratio. The paper honestly acknowledges this limitation, but the contribution is presented as a major feature while the evidence shows a tool that influences behavior weakly and without comparison to simpler alternatives (e.g., threshold filtering by final reward). The event definitions (Contact, Grasped, Dropped, Excessive Collisions) are straightforward uses of privileged simulator state. As a practical engineering convenience this is fine, but as a research contribution it is thin.

- **No wall-clock training time reported**. The paper reports 1.83 billion environment samples but does not state how long training took. For a benchmark that users may want to reproduce or extend, this is relevant practical information.

- **No direct comparison to HAB's magical grasp baselines on the same tasks**. The paper repeatedly contrasts its approach with magical grasp, but never quantifies the "cost of realism" — e.g., how much harder the tasks become when switching from teleport to physics-based grasping. A direct comparison using the original HAB policy paradigm on MS-HAB would be informative.

- **Dataset statistics are surface-level**. 1000 demonstrations per subtask-object combination is reported, but there is no analysis of trajectory diversity, multimodality, length distributions, or state-space coverage. For a dataset release, these are standard characterizations.

### Trivial

- The choice of SAC for Pick/Place and PPO for Open/Close is stated but not justified. If the authors selected algorithms based on empirical performance, stating this would help.
- The 125× speed comparison to RoboCasa is technically correct (RoboCasa 31.9 SPS without rendering vs. MS-HAB 4109 SPS while rendering), but the framing is asymmetric — RoboCasa includes AI-generated textures and human demos at different capability levels. A footnote or more careful contextualization would help.
- The SetTable skill chain in Section 3.2 appears to have three consecutive `Nav(g_pos)` calls, which may be a formatting artifact but should be verified.

## Nice-to-Haves

- Adding a random-policy or scripted-policy floor for all tasks would substantially strengthen the benchmark's credibility.
- Simulation-level validation of grasp quality (e.g., stability under perturbation, contact force profiles, kinematic reasonableness) would support the "realistic" framing.
- Reporting wall-clock training times would help users assess the cost of reproducing/extending baselines.
- A direct comparison of the original HAB magical-grasp policies on the same tasks (to quantify the difficulty added by low-level control) would be informative.

## Removed Points

These points are flagged to be removed; treat them with caution.

- The harsh critic's claim that "the core value proposition of 'realistic low-level manipulation' is asserted but never validated" as a **fatal structural issue**: Downgraded to minor overclaim because (a) "realistic" in context primarily contrasts with "magical grasp" (teleportation), which IS validated — the paper shows joint-level PD control, rigid-body dynamics, force limits, and non-teleport grasping; (b) the paper explicitly disclaims real-robot transfer; and (c) demanding simulation-level physical validation goes beyond what is standard for benchmark papers that adopt an existing physics engine.
- The harsh critic's claim that the trajectory categorization is "over-claimed" as a major weakness: Downgraded to minor. The paper presents it as one of four contributions, honestly discusses the modest results, and never claims it is a sophisticated research contribution.
- The harsh critic's claims about the RoboCasa comparison being "misleading": Downgraded to trivial. The paper discloses RoboCasa's configuration ("without rendering") and its own configuration ("while rendering 2 128×128 RGB-D images"). The numbers are technically correct; the framing could be more careful but is not deceptive.
- The harsh critic's request for justifying why not to extend the benchmark to learned navigation: Removed as scope creep — the paper explicitly scopes itself to low-level manipulation and uses teleport for navigation by design.
- The harsh critic's complaint about SAC vs. PPO choice: Kept but moved to trivial as a minor documentation gap, not a substantive issue.
- The Strength Finder's generic strengths about "addressing an important problem" or "targeting an interesting question": These were not present in the Strength Finder output; all listed strengths had specific citations and concrete evidence.

## Novel Insights

Beyond the paper's own contributions, the reviews surface one genuinely novel observation: the per-object vs. all-object policy analysis (Table 2) reveals that object-geometry overfitting is not merely a quantitative improvement but changes the *qualitative* failure profile — reducing excessive-collision failures by 1.88–2.42× and grasp failures by 1.87–12.37× for difficult geometries. This suggests that for low-level manipulation under tight tolerances, the bottleneck is not just learning a grasp but learning to avoid self-collision and environmental collision during approach, which object-specific geometry information helps with. This insight is more significant than the paper emphasizes.

## Suggestions

1. Add a random-policy floor and/or a hand-designed scripted baseline to establish that the benchmark tasks are differentiating (i.e., that methods can be meaningfully compared).
2. Tone down the "realistic" language or add simulation-level validation (grasp stability analysis, contact force statistics) to support it. Even a qualitative assessment of whether learned grasps are kinematically reasonable would help.
3. Report wall-clock training times for the baselines.
4. Either strengthen the trajectory filtering experiments (e.g., compare against a simple reward-threshold baseline, or show that filtering improves downstream IL/offline-RL performance) or reframe it as a practical engineering tool rather than a research contribution.

## Score and Decision

The paper makes real contributions: a validated 3× simulation speedup, a first low-level implementation of HAB, extensive baselines, and an insightful per-object policy analysis. The main gaps are the missing floor characterization (which weakens the benchmark's claim to be a useful comparison platform) and overclaimed "realistic" language relative to what is validated. Neither is fatal, but both need addressing. The paper is a competent engineering release with honest limitation disclosure; with the floor characterization added, it would be a solid contribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
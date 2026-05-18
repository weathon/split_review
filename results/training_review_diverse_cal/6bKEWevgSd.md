I have all the evidence I need to produce a fair and verified consolidated review. Here is my final synthesis:

---

## Summary

MS-HAB presents a GPU-accelerated implementation of the Home Assistant Benchmark (HAB) supporting realistic low-level whole-body control for the Fetch robot, along with extensive RL and IL baselines across three long-horizon rearrangement tasks (TidyHouse, PrepareGroceries, SetTable). It contributes an automated trajectory labeling and filtering system that uses privileged simulator state to categorize demonstrations by success/failure mode, enabling controlled data generation at scale. The paper trains 150 RL policies (1.83B environment samples) and provides IL baselines using behavior cloning on filtered datasets.

## Strengths

- **GPU-accelerated HAB with low-level control provides a meaningful infrastructure contribution.** The paper ports HAB to ManiSkill3's GPU-parallel simulation backend, achieving up to 2.94× the simulation speed of Habitat 2.0 (4109 SPS at 1024 parallel environments vs. 1398 SPS at 24 environments). Critically, this enables low-level joint-based and end-effector control that Habitat 2.0 does not support — a genuine capability gap this benchmark fills. The speed advantage is real and significant, even if the "similar memory" qualifier requires correction.

- **Per-object RL policies show measurable improvement over all-object policies for objects with tight geometric constraints.** Table 2 demonstrates that for the Cracker Box (YCB #003), the all-object policy is 1.88–2.42× more likely to fail from excessive collisions and 1.87–12.37× more likely to fail to grasp. Table 1 further shows aggregate per-object improvements across TidyHouse Pick (+14.1%), PrepareGroceries Pick (+8.8%), and PrepareGroceries Place (+20.8% train / +14.4% val). The evidence that geometry-specialized policies help is credible within the demonstrated scope.

- **The automated trajectory labeling system is a novel and practically useful contribution.** The system defines events from ground-truth simulator state (Contact, Grasped, Dropped, Excessive Collisions) and composes them into mutually exclusive success/failure modes. Table 3 shows that filtering demonstrations by these modes measurably biases IL policy behavior (e.g., place-in-goal vs. drop-to-goal ratios shift from 0.86:1 to 1.96:1 or 0.34:1 depending on filter). No prior home-scale rearrangement benchmark provides this capability.

- **The paper identifies a concrete failure mode specific to low-level control that does not arise with magical grasping.** The Close Fridge policy completely fails on validation scenes because the fridge door opens into a wall, blocking the arm — a problem invisible in the original HAB's teleport-based setup. This finding provides a clear actionable direction for future work (more scene diversity for low-level control policies).

## Weaknesses

### Fatal
None.

### Major

- **The headline quantitative claim — "3× faster than Habitat 2.0 at similar GPU memory usage" — is not supported by the paper's own data.** The paper twice asserts "similar GPU memory" (abstract line 4 and Section 4 line 16, echoed in Figure 1's caption at line 108), but Figure 1 reportedly shows that at the point where MS-HAB achieves ~2.94× speed (1024 environments, 4109 SPS), GPU memory usage is substantially higher than Habitat's peak (~20 GB vs. ~7.5 GB on a 24 GB RTX 4090). At comparable memory budgets (~7.5 GB), MS-HAB achieves roughly 2000 SPS — approximately 1.4× Habitat. The paper does not report the memory numbers in text, relying on the figure alone, and the "similar memory" claim is misleading for the data point highlighted as the primary speed comparison. For a benchmark paper, accurate characterization of the headline performance metric is essential. The authors should either qualify the speedup by memory regime or restate the claim accurately.

- **Evidence that per-object policies are "necessary" for certain objects rests on a single object deep-dive.** Table 2 provides detailed failure-mode analysis for only the Cracker Box (YCB #003). While Table 1 shows aggregate per-object vs. all-object differences across tasks, it does not report per-object success rates individually for all objects involved (nine objects across TidyHouse and PrepareGroceries). The claim that per-object policies are "necessary to learn grasping for certain objects" (line 183) is too strong for the evidence provided — the paper demonstrates necessity for one object and aggregate improvement across tasks, but cannot show the claim holds for all objects with difficult geometries without per-object breakdowns.

### Minor

- **The comparison with Habitat uses a modified benchmark setup with acknowledged differences.** The paper modifies the robot's initial pose, increases the number of interactive objects from 2 to 5, adds two cameras, and changes the control frequency. The authors acknowledge that exact replication is "exceedingly difficult" (line 118), but the cumulative changes mean the speed comparison is not apples-to-apples. A clearer quantification of how each modification affects SPS would help the community interpret the benchmark.

- **No justification is given for using SAC (Pick/Place) vs. PPO (Open/Close).** The paper reports using different algorithms and network architectures for different subtasks (lines 146–147) without explaining the rationale. While not necessarily a flaw (different subtasks may genuinely benefit from different algorithms), the omission weakens the paper as a reference benchmark — future work cannot tell whether the choice reflects empirical tuning or a methodological principle.

- **The base velocity control is underspecified for reproducibility.** The paper states the action space includes linear/angular velocity for the base and a PD joint delta position controller for the arm (line 110), but does not specify whether base velocities are executed open-loop or through a low-level controller. This detail matters for reproducing the benchmark results.

- **The trajectory labeling system defines thresholds (e.g., 5000N cumulative force for "excessive collisions") without justification or sensitivity analysis.** While the events themselves are ground-truth simulator states (not learned classifiers) and thus accurate by construction, the choice of thresholds is arbitrary. A brief rationale or ablation showing that results are not sensitive to threshold choice would strengthen the system's credibility.

### Trivial
- **Data release status.** The reproducibility statement (line 219) indicates the dataset "is uploading to HuggingFace," with a workaround of generating data via provided scripts. The paper should clarify the expected timeline or provide a permanent fallback. This is a practical concern, not a scientific flaw.

- **The IL baseline uses only Behavior Cloning.** The paper acknowledges this limitation explicitly (line 167: "indicating a need for methods and architectures which can handle multimodalities in the data"), so this is not a weakness of the paper — BC-only baselines are standard for establishing a lower bound. No action needed.

## Nice-to-Haves
- A per-object success rate violin plot or table covering all objects in TidyHouse and PrepareGroceries Pick would cleanly settle whether the per-object advantage generalizes.
- A sensitivity analysis for the trajectory labeling thresholds (e.g., varying the 5000N collision limit) would strengthen confidence in the filtering system.
- An analysis of dataset diversity (e.g., object pose histograms, collision force distributions) would help users understand coverage.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Trajectory labeling needs validation of accuracy"** — The reviewer called for validation that the labeling system correctly classifies trajectories. However, the events (Contact, Grasped, Dropped, Excessive Collisions) are defined from ground-truth simulator state queries (nonzero forces, grasp state transitions, cumulative forces), not from learned classifiers. There is no classification accuracy to validate — the simulator state is ground truth by definition. The remaining concern about threshold choice (5000N) is retained as a minor weakness above. The framing as an accuracy/validation issue is removed.

- **"IL baselines using BC only adds limited insight"** — The reviewer noted this negative result is predictable. But the paper explicitly acknowledges this limitation (line 167) and uses BC as a standard lower-bound baseline. Benchmark papers routinely include simple baselines; this is not a weakness. Removed as a strawman that the paper already addresses.

- **"The paper should also cover Y / domain Z / additional tasks"** — Not present in this review; no action needed.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no genuinely novel interpretation that the paper's authors missed.

## Suggestions

1. **Correct the benchmark comparison.** Replot Figure 1 with explicit GPU memory annotations for every data point. Restate the speed claim honestly — e.g., "up to 2.94× faster than Habitat 2.0 (using proportionally more GPU memory); at comparable memory budgets, 1.4× faster." Transparency about the speed–memory tradeoff will strengthen rather than weaken the paper's credibility.

2. **Add per-object success rates for all objects across all tasks.** A single table or violin plot showing per-object and all-object success rates for every object in TidyHouse and PrepareGroceries Pick would directly support (or appropriately bound) the claim about per-object policy necessity.

3. **Provide a brief rationale for the 5000N collision threshold** and, if feasible, a sensitivity check at one alternative threshold to show results are not brittle.

4. **Clarify the base velocity control** — specify whether the linear/angular velocity commands are applied open-loop or through a low-level tracking controller.

5. **Explicitly justify or ablate the SAC vs. PPO choice** across subtasks in the main text or appendix.

---

**MY FINAL SCORE: <pineapple>5.0</pineapple>**
**MY FINAL DECISION: <orange>Reject</orange>**
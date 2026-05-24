Now I have all the evidence needed. Here is the consolidated review.

---

## Summary

CoRAL proposes a modular neuro-symbolic framework for zero-shot contact-rich manipulation that separates vision-based perception (FoundationPose for 6-DoF tracking, VLM for physical parameter estimation) from an LLM-driven strategist that generates MPPI cost functions, symbolic contact strategies, and online adaptation loops. A memory unit based on RAG retrieves and reuses past successful strategies. The framework is evaluated on six challenging simulated manipulation tasks against OpenVLA-OFT, π₀.₅, and human-expert-designed cost baselines.

## Strengths

1. **VLM/LLM role separation is convincingly validated by the Unified VLM ablation.** The CoRAL (Unified VLM) variant — mashing perception and planning into a single VLM — scores 0/10 on four of six tasks and at most 2/10 overall, while the separated-role framework achieves nonzero success on all six tasks (Table 1). This directly supports the paper's core architectural claim.

2. **LLM-generated contact strategy yields dramatic efficiency gains on the hardest task.** On the "Flip with Wall" task (T6), providing the LLM's symbolic contact strategy makes the planner **83.9% faster** (32 vs. 199 steps) with **63.9% less end-effector travel** (1.33 m vs. 3.69 m). This goes well beyond prior work (IMPACT, VLMPC) where the foundation model only produces cost maps or sub-goals rather than explicit contact biasing that prunes the search space.

3. **Memory unit delivers consistent, measurable improvements.** Across the four hardest tasks, the full CoRAL with memory outperforms the w/o memory variant on every one (T1: 4/10 vs. 2/10; T3: 10/10 vs. 9/10; T5: 9/10 vs. 7/10; T6: 7/10 vs. 5/10), with consistently lower completion times. This demonstrates that RAG-based retrieval of past successful strategies is more than a cosmetic addition.

4. **Ablation studies comprehensively isolate each component's contribution.** The paper does four ablations (w/o Memory, w/o Refinement, Unified VLM, w/o Pose Tracking), and each creates a clear, interpretable failure pattern. The w/o Refinement variant collapsing on T1 (0/10 from 4/10) cleanly demonstrates the outer loop's role in correcting physical parameter misestimation. This is more thorough ablation coverage than most comparable papers.

5. **Approaches expert-designed cost performance on the hardest tasks.** CoRAL achieves 4/10 and 7/10 on T1 and T6 respectively, vs. the expert-FSM upper bound of 8/10 and 9/10 (Table 1), while substantially outperforming the single-stage expert (0/10 and 3/10). This shows the LLM can automatically recover much of the structure a human expert would hand-engineer.

## Weaknesses

### Major

1. **Figure 4 mass-correction experiment contains an unexplained numerical inconsistency.** The text (Section 4.1.4) states: *"We intentionally initialized the Evaluation World with a severely overestimated mass (2.0 kg vs. a ground truth of 0.1 kg)."* However, Figure 4's y-axis ranges from 0.75 to 1.00, shows an initial mass of 1.0 kg, and the corrected value settles at ~0.85 kg — none of which are consistent with the textual claim (not 2.0 kg, not approaching 0.1 kg). The ground truth of 0.1 kg does not even appear on the displayed axis. This is not a parser artifact; it is a substantive discrepancy between two numerical claims in the paper. The paper's claim of "converged remarkably close to their true values" is unsupported by the figure as presented. This undermines the specific robustness claim about online parameter correction of mass. The paper's other evidence for the outer loop (the w/o Refinement ablation collapsing on T1) is unaffected, but the authors must clarify or correct this experiment.

2. **Statistical reliability is weak for the stronger claims.** All results report binary success over 10 trials per condition with no confidence intervals, variance bars, or significance tests. Given that each trial randomizes object masses, friction coefficients, dimensions, and initial poses, variance is expected to be high. On T1, the memory variant scores 4/10 vs. w/o memory's 2/10 — a difference of two successes with N=10. This is within the noise range of binomial sampling with such randomization. The paper frames this as "significantly improved" (Section 4.1.3), but the evidence is too thin to support that. For the stronger claims about memory and refinement, 30+ trials with bootstrapped confidence intervals would be needed.

3. **All evaluation is in simulation, with no real-world validation.** While the paper briefly acknowledges this in the limitations section, the gap is significant for contact-rich manipulation, where MuJoCo's simplified contact and friction models may not capture real-world behaviors. The system's reliance on FoundationPose (trained on real data) and GPT-4o (pre-trained on web data) suggests some sim-to-real potential, but the paper provides no evidence for how the reactive control term (Equation 7) handles real sensor noise, latency, or calibration errors. The T4 (Push with Constant Force) task is the most affected by this limitation, yet the paper draws conclusions about force-aware control.

### Minor

1. **The "w/o Pose Tracking" ablation is less informative than it could be.** Removing FoundationPose and relying on the VLM for 6-DoF tracking predictably fails (0/10 on most tasks). This confirms that VLMs cannot do precise tracking — a point that is already well-known and does not specifically inform the architecture's design. A more informative comparison would pit FoundationPose against a different dedicated pose estimator (e.g., ICP or a simpler learned tracker) to isolate FoundationPose's specific contribution.

2. **Several components are underspecified for reproducibility.** The memory unit's similarity metric is described only as *"the LLM embeds the current task into a latent semantic space"* — no embedding model, similarity threshold, or storage format is given. The mechanism for biasing MPPI control perturbations toward the LLM-proposed contact regions (Section 3.2) is described only as *"biasing the initial control perturbations"* without specifying how this is implemented (cost shaping, sequence initialization, or sampling distribution modification). The LLM-generated cost function's parsing and integration into MPPI (code, JSON, or natural language) is also unclear.

3. **Completion time reported for successful trials only is potentially misleading.** Faster completion may occur on easier randomizations (e.g., favorable initial pose or friction). Reporting times across all trials (with a penalty or imputation for failures) or reporting the distribution of times would be more informative.

### Trivial

- The indicator function 𝕀{no contact at t} in Equation 2 is a discrete term in an otherwise continuous cost; the paper does not discuss how this interacts with MPPI's sampling-based optimization, but this is common practice in MPPI literature and not a substantive weakness.

## Nice-to-Haves

- Compare FoundationPose against a simpler but still dedicated pose estimator (e.g., ICP) rather than the VLM-only ablation to isolate FoundationPose's specific contribution.
- Report memory retrieval success rates and show qualitative examples of retrieved vs. generated plans.
- Report the end-to-end runtime of the full pipeline (LLM API calls + MPPI rollouts) to contextualize the "computational latency" mentioned in limitations.

## Removed Points

These points were raised in the source reviews but are removed from the main assessment for the following reasons:

- **"Baseline comparison is structurally unfair due to different simulation platforms"** (Harsh Critic #1): Removed. The baselines use official LIBERO checkpoints. LIBERO is built on Robosuite/MuJoCo — the same simulation framework CoRAL uses. The paper states this explicitly: *"evaluation world, implemented using ROBOSUITE library, which is based on the MUJOCO physics engine."* The claim that baselines are evaluated in "a different simulation from their training distribution" is factually incorrect. That CoRAL outperforms these baselines on *novel contact-rich tasks* (T1, T4, T5, T6) that were not in the baseline training distribution is a legitimate finding, not an artifact.
- **"w/o Pose Tracking ablation is a straw-man"** (Harsh Critic #3): Downgraded from Major to Minor. The ablation does validate that the system architecture's role separation is necessary, since a VLM cannot substitute for a dedicated tracker. However, the point that comparing against a different dedicated tracker would be more informative is valid, so this is retained as a Minor weakness.
- **"The LLM formulates the cost function — difference from IMPACT/VLMPC is one of degree, not kind"** (Harsh Critic, Related Work): Removed. The paper's methodology section clearly articulates that the LLM generates the *structure* and *weights* of the cost function (Eq. 2) and symbolic contact strategies (Eq. 3), which goes beyond prior work that generates cost maps or sub-goals. This is a genuine distinction of kind, not just degree.
- **"LLM-generated cost function includes an indicator function poorly suited for MPPI"** (Harsh Critic, Methodology): Removed. MPPI routinely handles non-smooth costs; the indicator merely penalizes a discrete condition (no contact) via the weight w_c in the sample weighting. This is standard practice and not a flaw.
- **Strength Finder claims about Figure 4 showing correction "toward the true value of 0.1 kg"**: Removed as it conflicts with the verified weakness — the figure does not show convergence toward 0.1 kg. This strength is invalid.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Resolve the Figure 4 inconsistency.** Provide the correct figure with axes and values that match the text (initial mass 2.0 kg, ground truth 0.1 kg) and show the corrected values approaching the ground truth. If the figure is correct and the text is wrong, correct the text. This is the most actionable fix.
2. **Increase trial counts to at least 30 per condition** and report 95% confidence intervals (e.g., via bootstrapping) for the binary success metric. This is standard for the simulation-based manipulation literature and would make the memory/refinement claims convincing.
3. **Add a more informative pose-ablation.** Compare FoundationPose to a dedicated but simpler tracker (e.g., ICP) rather than the VLM-only condition, to isolate FoundationPose's specific value.
4. **Specify the memory retrieval mechanism concretely** (embedding model, similarity metric, storage format) to enable reproduction.
5. **Clarify how the contact strategy biasing is implemented** in the MPPI framework — is it cost shaping, initialization, or sampling distribution modification?
6. **Include a sim-to-real discussion** with specific analysis of which components would transfer and which would require re-tuning, even if real experiments are deferred to future work.

## Score and Decision

**Round 1 bracket:** I searched three bands: weak anchors (avg ≤ 3.5, mostly Reject papers like GRAIL at 3.0, LARG2 at 3.0, EF-VLA at 3.33), middle anchors (3.5–7.5, which returned LLMPhy at 4.00, CORN at 4.75, GenBot at 5.50, RDT-1B at 7.00), and strong anchors (≥ 7.5, which returned GenSim at 8.00 and others at 8.00). CoRAL is clearly above the 3.0–3.33 papers (which have weaker evaluation or methodological flaws), but below the 7.0–8.0 papers (which have extensive real-world validation or large-scale studies). The narrowest plausible bracket from round 1 was **4.0–5.5**.

**Round 2 narrowing:** I searched within (4.0, 6.5) and (3.5, 6.0) to find closer anchors. Key anchors: LLMPhy (4.40, Reject), CORN (4.75, Accept), CrayonRobo (5.20, Reject), Make a Donut (5.25, Reject), Instruct2Act (5.00, Reject), GENOME (5.75, Accept). CoRAL is stronger than LLMPhy (more tasks, better ablations) and comparable to CrayonRobo and Make a Donut — but those papers include real-world validation that CoRAL lacks, while CoRAL has more comprehensive ablations. The Figure 4 inconsistency is a significant issue that pulls the paper down relative to similarly-scored papers.

**Final score:** Placing the paper relative to these anchors, I give **5.0**. The paper has genuine architectural insight and better-than-average ablation coverage, but the Figure 4 numerical inconsistency, lack of real-world validation, and thin statistical support prevent it from reaching the 5.5–6.0 tier occupied by papers that address these concerns.

**All anchors retrieved (all rounds):**

| Anchor ID | Avg Score | Round | Comparison to CoRAL |
|---|---|---|---|
| Q6HYM1EMu8 | 3.00 | R1 | Weaker — limited scope, weaker evaluation |
| oyXoGJQlUf | 3.00 | R1 | Weaker — narrow task domain |
| wl1Kup6oES | 3.00 | R1 | Weaker — focused on pre-training, not interactive control |
| KBSHR4h8XV | 3.33 | R1 | Weaker — limited real-world evidence |
| WtHKqtHVXo | 4.00 | R1 | Slightly weaker — fewer tasks, but has real robot experiments |
| KTtEICH4TO | 4.75 | R1, R2 | Similar — contact-based manipulation, real-world validation but mixed reviews |
| J4D5WVoc5g | 4.50 | R1 | Different domain (hand-object reconstruction) |
| yAzN4tz7oI | 7.00 | R1 | Stronger — large-scale bimanual foundation model with real-world eval |
| OI3RoHoWAN | 8.00 | R1 | Stronger — task generation at scale |
| 7BLXhmWvwF | 8.00 | R1 | Stronger — rigorous RL benchmark with real validation |
| 7gUrYE50Rb | 8.00 | R1 | Different domain (EQA) |
| pISLZG7ktL | 8.00 | R1 | Stronger — large-scale data scaling study |
| qGL6fE1lqd | 4.40 | R2 | Slightly weaker — similar LLM+physics approach, simpler task |
| iTsHStJKcm | 5.25 | R2 | Similar — zero-shot LLM planning, real robot experiments |
| Aqfwhna1D7 | 5.20 | R2 | Similar — visual prompting, both sim and real |
| fZZ4ubttru | 5.50 | R2 | Similar — generative simulation, but weaker quantitative results |
| MNShbDSxKH | 5.75 | R2 | Stronger — neuro-symbolic reasoning, cleaner evaluation |
| D1w3huGGpu | 4.75 | R2 | Different domain (compositional generalization) |
| JWrl5pJCnl | 5.00 | R2 | Similar — LLM-based manipulation, simulation only |
| ysAX5ORQoX | 4.25 | R2 | Weaker — LLM as planner, simpler tasks |
| VZTFUtldbC | 4.75 | R2 | Different domain (modular control for locomotion) |
| 6I7UsvlDPj | 5.67 | R2 | Different domain (language as priors for perception) |
| SLDqCpHPuP | 5.00 | R2 | Different domain (pose estimation) |
| s3sJenvY5H | 4.75 | R2 | Different domain (evaluation of generative simulations) |
| bpdIZTIVq8 | 4.50 | R2 | Different domain (action representation learning) |

**Decision:** Reject

The paper presents a well-motivated architecture with clean ablations and concrete efficiency results. However, the Figure 4 mass-correction inconsistency undermines a core robustness claim, the statistical evidence is too thin (10 trials, no confidence intervals) to support the stronger claims about memory and refinement, and the all-simulation evaluation limits real-world relevance. These issues are addressable — the core idea is sound — but the paper in its current form does not provide sufficiently reliable evidence for its claims.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
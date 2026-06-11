Now I have a clear picture. Let me finalize the review.

**Calibration comparison summary:**

- **WtHKqtHVXo (4.00, Reject)**: LLM generates policy code for contact-rich tasks, but evaluation is thin (2 task types, weak baselines, limited ablations). CoRAL is clearly stronger with 6 tasks, comprehensive ablations, and SOTA VLA baselines.

- **iTsHStJKcm (5.25, Reject)**: LLM hierarchical planning for deformable objects. Has real-robot experiments and reasonable ablations, but LLM plan is open-loop and error recovery is incomplete. CoRAL has a more integrated architecture with nested feedback loops and cleaner ablations — comparable or slightly stronger.

- **NxoFmGgWC9 (5.50, Accept)**: Video generative pre-training for manipulation. Strong CALVIN results + real robot, but reviewers flagged missing baselines and weak real-robot tasks. CoRAL has better-structured ablations but is simulation-only and has the parameter adaptation discrepancy — roughly comparable.

- **c0chJTSbci (6.25, Accept)**: Diffusion-based subgoal planning with CALVIN SOTA + real robot. Stronger evaluation than CoRAL, but planning/control are decoupled without feedback. CoRAL's architecture has better integration (nested loops) but weaker overall evaluation (sim-only, parameter adaptation issue). CoRAL is weaker than this anchor.

**Final placing: 5.5, Reject.** The paper has genuine strengths (clean architecture, convincing ablation study, competitive results against expert-designed costs) but the parameter adaptation discrepancy (Major weakness) — where the text claims convergence "remarkably close to true values" but Figure 4 shows convergence to ~0.85 kg vs. 0.1 kg ground truth — undermines confidence in the robustness claims. Combined with missing LLM+MPC baselines and narrow evaluation scope, this lands below the accept threshold.

---

## Summary

CoRAL proposes a modular neuro-symbolic framework for zero-shot contact-rich robotic manipulation. It decouples vision (VLM for physical parameter estimation, FoundationPose for pose tracking) from an LLM that generates MPPI cost functions and contact strategies, with nested feedback loops for online adaptation and a RAG-based memory for experience reuse. Evaluated on six tasks in simulation (including two LIBERO benchmarks), CoRAL outperforms SOTA VLAs on contact-rich tasks and approaches expert-designed cost functions without manual engineering.

## Strengths

- **LLM-generated cost functions achieve competitive zero-shot performance against expert-designed alternatives.** CoRAL (with Memory) reaches 9/10 on T4 (Push Const. Force), 9/10 on T5 (Flip Box), and 7/10 on T6 (Flip w/ Wall), closely tracking the Expert FSM upper bound (10/10, 10/10, 9/10) while requiring no manual cost-function engineering (Table 1).

- **The separation of VLM perception from LLM reasoning is causally validated by a clean ablation.** The CoRAL (Unified VLM) variant collapses perception and planning into a single multimodal prompt and fails catastrophically: 0/10 on 5 of 6 tasks (T1, T3, T5, T6) and 1/10 on T4 (Table 1). This directly supports the paper's central architectural claim.

- **The online adaptation loop demonstrably enables recovery from world-model errors.** The w/o Refinement ablation drops T1 from 4/10 to 0/10 and T3 from 10/10 to 3/10 (Table 1), showing the outer loop is essential for multi-stage tasks where initial estimates are imperfect.

- **LLM-proposed contact strategies dramatically prune the action search space.** On T6 (Flip with Wall), the contact-strategy ablation shows an 83.9% reduction in planning steps (32 vs. 199) and a 63.9% shorter end-effector path (1.33 m vs. 3.69 m) compared to uninformed random sampling with the same cost function (Section 4.1.4).

- **The dedicated pose estimator (FoundationPose) is shown to be non-negotiable.** The w/o Pose Tracking ablation yields 0/10 on five of six tasks, and the paper provides a clear diagnosis (VLM "hallucinated" poses unsuitable for precision tracking).

## Weaknesses

### Fatal

None.

### Major

- **Parameter adaptation results contain a factual discrepancy between text and figure.** Section 4.1.4 states the Evaluation World was initialized with mass 2.0 kg (ground truth 0.1 kg), but Figure 4 shows the "Initial Mass" at 1.0 kg — a contradiction. Furthermore, the text claims the mass estimate "converged remarkably close to their true values," yet Figure 4 shows convergence to ~0.85 kg, which is 8.5× the stated ground truth of 0.1 kg. The friction coefficient adaptation is mentioned in the text but never plotted. These inconsistencies undermine confidence in the claimed robustness of the online parameter adaptation, which is presented as "a cornerstone for deploying robots in unknown environments."

### Minor

- **Memory unit evidence is suggestive but not statistically conclusive.** The memory unit improves success from 2/10 to 4/10 on T1, 7/10 to 9/10 on T5, and 5/10 to 7/10 on T6 — all 2-trial differences out of 10 with no statistical tests reported. On T2 and T4, memory provides zero success-rate benefit. The paper describes the memory unit as a key contribution; the success-rate evidence alone does not strongly support this, though the completion-time improvements are more consistent.

- **No direct comparison to closely related LLM+MPC methods.** VLMPC and IMPACT are cited in related work as predecessors that use VLMs for perceptual guidance in MPC. The paper claims CoRAL elevates the LLM's role from perceptual guide to cost-function strategist, but without a head-to-head comparison against at least one of these methods on the paper's own tasks, the claimed advance over the prior state of the art in LLM+MPC integration remains asserted rather than demonstrated.

- **Narrow evaluation scope.** All six tasks use the same Franka Emika Panda arm in the same ROBOSUITE/MuJoCo simulator with objects whose 3D models are known. The generalization boundaries of the framework — to different robots, simulators, or objects without CAD models — are untested.

- **VLA baseline comparison conflates in-distribution and OOD performance.** VLAs (OpenVLA-OFT, π₀.₅) were fine-tuned on LIBERO and perform well on the LIBERO-derived tasks (T2, T3) but fail on the custom contact-rich tasks (T1, T4, T5, T6). While this demonstrates CoRAL's zero-shot advantage on OOD contact-rich tasks, the framing does not clearly distinguish between these two regimes, somewhat overstating the strength of the head-to-head comparison.

### Trivial

- The tasks corresponding to the LIBERO benchmark are not explicitly identified in the text (T2 and T3 are likely these, but this is not stated clearly on line 151).

## Nice-to-Haves

- Statistical reporting (confidence intervals, multiple random seeds) would strengthen the conclusions, particularly for the memory unit results where differences are small relative to trial counts.
- Reporting VLM physical parameter estimation accuracy against ground truth would help characterize the starting point the online adaptation loop must overcome.
- Including examples of actual LLM-generated cost functions and prompts in the main body would improve transparency of the method's core mechanism.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic #2 (LLM outputs invisible, deferred to appendix):** REMOVED. The paper references an appendix for prompt/cost-function details; the parser strips appendices from all submissions. Per instructions, missing appendix content is a parser artifact, not an author error. The paper's main body describes the mechanism and shows system-level results.

- **Harsh Critic #1 (Expert FSM gap "understated"):** REASSESSED AND DEMOTED. The paper explicitly acknowledges CoRAL is "below the FSM upper bound" and the "narrows the gap" claim is relative to the single-stage expert (which scores 0/10 on T1 vs. CoRAL's 4/10), not the FSM. The framing is honest. The 4/10 vs. 8/10 gap on T1 is real but the paper does not misrepresent it.

- **Strength Finder: "The memory unit provides consistent, measurable gains across diverse tasks":** WEAKENED. While there are gains, the 2-trial differences on several tasks with only 10 trials and no statistical tests make "consistent" an overstatement. Moved to Minor weakness.

- **Strength Finder: Generic strengths about "addressing an important problem":** REMOVED as non-concrete.

- **Harsh Critic: "Statistical rigor is absent" as a standalone criticism:** DEMOTED to Nice-to-Haves. 10 trials with binary success is standard practice in many robotics evaluation protocols.

- **Harsh Critic: Claims about VLM physical parameter estimation being unverified:** ABSORBED into the verified parameter adaptation discrepancy (Major weakness) and the Nice-to-Haves suggestion about reporting VLM estimation accuracy.

- **Harsh Critic: Section 3.2 prompting strategy details missing:** The appendix (parser-stripped) likely contains these details. Not flagged as a weakness per hard rules about missing appendix content.

## Novel Insights

The most novel finding is the causal validation of role separation: collapsing VLM perception and LLM reasoning into a single prompt causes near-total failure across all tasks. While multi-module architectures are common in robotics, the starkness of this result — 0/10 on 5 of 6 tasks — provides unusually compelling evidence that the specific modular decomposition (geometric pose tracking + semantic perception + symbolic reasoning + model-based control) is not merely an architectural preference but a functional necessity for this class of problems. This has implications beyond this paper for how foundation models should be integrated into robotic control pipelines.

## Suggestions

- Resolve the discrepancy between the text (2.0 kg Evaluation World mass) and Figure 4 (1.0 kg initial mass). Clarify whether the figure shows Planning World or Evaluation World values, and either correct the figure or the text.
- Either report the true convergence value relative to ground truth honestly (0.85 kg vs. 0.1 kg is not "remarkably close"), or reframe the claim: the adaptation moves in the correct direction but does not converge to the true physical parameter — which may be acceptable if the Planning World becomes sufficiently predictive for task success.
- Add a comparison against at least VLMPC or IMPACT on one contact-rich task to ground the claimed advance over the LLM+MPC state of the art.
- Explicitly identify which tasks (T2, T3) are the LIBERO benchmark tasks.

---

**Calibration anchors referenced:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| wl1Kup6oES | 3.00 | R1 (weak) | CoRAL is clearly stronger — better evaluation, architecture, and baselines |
| oyXoGJQlUf | 3.00 | R1 (weak) | CoRAL is clearly stronger |
| Q6HYM1EMu8 | 3.00 | R1 (weak) | CoRAL is clearly stronger |
| xcHIiZr3DT | 2.50 | R1 (weak) | CoRAL is clearly stronger |
| WtHKqtHVXo | 4.00 | R1 (mid) | CoRAL is stronger — more tasks, better ablations, SOTA baselines |
| iTsHStJKcm | 5.25 | R1+R2 (mid) | Comparable; CoRAL has better closed-loop integration but simulation-only |
| qGL6fE1lqd | 4.40 | R1 (mid) | CoRAL is stronger — more complete system with manipulation results |
| MWHIIWrWWu | 6.25 | R1 (mid) | Different subfield (musculoskeletal MPC); not directly comparable |
| OI3RoHoWAN | 8.00 | R1 (strong) | CoRAL is clearly weaker |
| KsUh8MMFKQ | 8.00 | R1 (strong) | CoRAL is clearly weaker |
| 7BLXhmWvwF | 8.00 | R1 (strong) | CoRAL is clearly weaker |
| pISLZG7ktL | 8.00 | R1 (strong) | CoRAL is clearly weaker |
| Aqfwhna1D7 | 5.20 | R2 (low) | CoRAL is comparable; different approach (visual prompting vs LLM+MPC) |
| NxoFmGgWC9 | 5.50 | R2 (low) | Comparable; CoRAL has better ablations but is simulation-only with parameter discrepancy |
| KTtEICH4TO | 4.75 | R2 (low) | CoRAL is stronger — better architecture evaluation |
| c0chJTSbci | 6.25 | R2 (high) | CoRAL is weaker — less evaluation breadth, no real robot, parameter discrepancy |
| 9pKtcJcMP3 | 7.00 | R2 (high) | CoRAL is clearly weaker |
| lFYj0oibGR | 6.50 | R2 (high) | CoRAL is weaker — less evaluation breadth, no real robot |
| hQVCCxQrYN | 6.67 | R2 (high) | CoRAL is weaker — less evaluation depth and breadth |

**Round 1 bracket:** 5.0–7.0. **Round 2 narrowing:** Comparison to NxoFmGgWC9 (5.50) and c0chJTSbci (6.25) places CoRAL closer to the lower bound, at 5.5, due to the parameter adaptation discrepancy (Major) and simulation-only evaluation.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
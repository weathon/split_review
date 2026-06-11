Now I have a clear picture. Let me finalize my assessment through direct comparison:

- CoRAL is clearly above **WtHKqtHVXo (4.00)** — more tasks, better ablations, more principled LLM-controller interface
- CoRAL is somewhat stronger than **Instruct2Act (5.00)** — more novel core idea, more challenging tasks, cleaner ablation design, but Instruct2Act has real-world experiments
- CoRAL is comparable to **"Make a Donut" (5.25)** — similar LLM+physics paradigm, both have strong ablation stories, but CoRAL's closed-loop refinement is a genuine advantage over the open-loop LLM plan in Make a Donut
- CoRAL is clearly below **SuSIE (6.25)** and **HAMSTER (6.00)** — those have real-world validation, standard benchmark results, and more rigorous experimental design

The structural unfairness in the headline VLA comparison, the black-box treatment of the core LLM cost-function generation mechanism, and the thin statistical evidence pull CoRAL down. But the genuinely novel architecture, well-designed ablation studies, and human-expert baselines prevent it from falling below 5.0.

**Final score: 5.0**

---

Now writing the final review.

## Summary
CoRAL proposes a modular neuro-symbolic framework for contact-rich robotic manipulation that separates perception (FoundationPose + VLM for pose tracking and physical parameter estimation) from reasoning (LLM for formulating MPPI cost functions and contact strategies), executed through a nested two-loop architecture with a memory unit for experience reuse. The paper evaluates on six contact-rich tasks, comparing against VLA baselines (OpenVLA-OFT, π₀.₅), human-expert cost function designs, and several internal ablations.

## Strengths
- **Novel LLM-to-controller interface**: The LLM directly formulates the mathematical structure of the MPPI cost function (Eq. 2) and contact strategy (Eq. 3), grounding abstract reasoning in the optimal control formulation. This goes beyond prior work (IMPACT, VLMPC) where foundation models serve as perceptual guides outputting subgoals or waypoints.
- **Well-validated architectural decomposition**: The ablation study (Table 1) provides strong causal evidence for the core design choices. The "Unified VLM" variant (merging perception and planning into one model) fails on nearly all tasks (0/10 on T1, T3, T5, T6), the "w/o Refinement" ablation cripples multi-stage tasks (T1: 4→0/10, T3: 10→3/10, T5: 9→4/10), and the "w/o Pose Tracking" collapses entirely — together showing each component is load-bearing.
- **Clean contact-strategy isolation experiment (Section 4.1.4)**: Removing only the LLM's contact strategy C₀ while keeping the cost function J₀ results in 83.9% more steps (32 vs. 199) and 63.9% longer end-effector path on T6 — a tightly controlled ablation isolating one specific mechanism.
- **Online parameter adaptation demonstration (Figure 4)**: Deliberately initializing with severely overestimated mass (2.0 kg vs. true 0.1 kg) and friction (0.9 vs. true 0.5) and showing the LLM-driven outer loop iteratively corrects both parameters toward ground truth addresses a realistic deployment challenge.
- **Inclusion of human-expert cost-function baselines** (single-stage and FSM) provides a meaningful upper-bound reference using the same MPPI/simulation infrastructure, enabling apples-to-apples assessment of the LLM's cost-function design quality.

## Weaknesses

### Fatal
None.

### Major
- **The comparison against VLA baselines is structurally confounded, undermining the headline result.** CoRAL receives known 3D object models (for FoundationPose), a full MuJoCo physics simulator (for MPPI rollouts), and engineered prompts to GPT-4o. The VLA baselines receive only RGB images and a language instruction, and are evaluated using LIBERO checkpoints on tasks (T1, T4, T5, T6) far outside their training distribution. The paper attributes the performance gap to architectural superiority, but the comparison confounds architectural differences with radically different information access and task-specific infrastructure. This is not a gap that can be closed by adding experiments; the comparison as designed cannot support the conclusion drawn. A fairer test would give VLAs comparable information or test CoRAL without its privileged components.

- **The LLM's cost-function generation — the paper's core mechanism — is treated as a complete black box.** The paper states the LLM is "free to introduce any cost terms constructible from the available state, pose, and action variables" (Section 3.2), with Eq. 2 described as "only an illustrative example." No analysis is provided of what cost functions the LLM actually generates across tasks, how consistent they are across multiple LLM calls for the same task, or how sensitive MPPI performance is to the specific generated cost. Given that the entire method hinges on the LLM producing sensible cost functions, this gap substantially limits the paper's scientific contribution.

### Minor
- **Statistical evidence is thin for the strength of some claims.** All results use N=10 trials with no confidence intervals or statistical tests. Differences like memory ablation on T1 (2/10→4/10) and T3 (9/10→10/10) are within sampling noise at this sample size, yet the paper draws categorical conclusions ("boosted the success rate significantly"). The contact-strategy ablation on T6 (Section 4.1.4) reports specific step counts (32 vs. 199) but does not clearly indicate whether these are from a single illustrative run or averaged across trials.

- **Key implementation details are under-specified for reproducibility.** The VLM's physical parameter estimation (Section 3.1) has no prompt structure, few-shot examples, or accuracy characterization. The memory retrieval mechanism (Eq. 1) states the "LLM embeds the current task into a latent semantic space" but provides no details on how similarity is computed or how experiences are indexed. Randomization ranges for mass, friction, and object dimensions are never specified.

- **LLM-generated cost functions fall short of expert-designed ones on the hardest multi-stage tasks.** The Expert (FSM) baseline — using the same MPPI controller — substantially outperforms CoRAL on T1 (8/10 vs. 4/10) and T6 (9/10 vs. 7/10). The paper's claim that CoRAL "can recover much of the structure of expert-designed costs automatically" overstates performance on the tasks that are the paper's main focus.

### Trivial
- The abstract mentions "picking up a thin object from a table" as an example task, but no such task appears among the six evaluated tasks.
- The reference "Appendix ??" on line 238 is an incomplete cross-reference.

## Nice-to-Haves
- A latency breakdown (GPT-4o API vs. MPPI optimization vs. other components) to help assess feasibility for real-time deployment.
- Evaluating multiple LLM calls per task to characterize variance in cost function quality.
- A study measuring how performance scales with number of stored experiences in the memory unit.
- A fair VLA comparison baseline, e.g., giving VLAs access to the same simulator and 3D models, or testing CoRAL without its privileged infrastructure.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **HC claimed single-stage expert baseline matches or beats CoRAL on T1**: Factually wrong — Table 1 shows single-stage expert gets 0/10 on T1 while CoRAL gets 4/10. Removed.
- **HC claimed "Unified VLM" ablation is a "deliberately broken baseline"**: Speculation about author intent not supported by the paper. The ablation tests the architectural hypothesis of role separation. Removed.
- **HC's criticism that the "zero-shot" framing is "critically misleading"**: The paper defines "zero-shot" as not requiring teleoperated demonstration data, which is a standard usage in the field. The real issue is the asymmetric comparison with VLAs, captured in the Major weakness above. Demoted.
- **SF's claim that memory improvement from 2/10→4/10 is "consistent" evidence**: This difference is within sampling noise at N=10. Kept the weakness but removed the strength claim.
- **SF's claim about explainability as a strong differentiator**: The explainability demonstration relies on a single anecdote with an incomplete appendix reference. Kept the concept noted but not elevated to a major strength.

## Novel Insights
The paper's most genuinely novel contribution is the specific LLM-to-controller interface where the LLM directly formulates the mathematical structure of an MPPI cost function rather than outputting subgoals, waypoints, or cost maps. This bridges abstract reasoning and optimal control in a more direct way than prior work, and the ablation showing that the LLM's symbolic contact strategy alone reduces planning steps by ~84% on T6 provides concrete evidence that this interface is functionally load-bearing. The nested two-loop design (high-frequency MPPI inner loop + low-frequency LLM outer loop for diagnosis and adaptation) is also a clean architectural contribution.

## Suggestions
- Rebuild the VLA comparison: either give VLAs equivalent infrastructure (simulator access, 3D models) or test CoRAL without privileged components, so the comparison isolates architectural differences rather than information access.
- Characterize the LLM's cost-function generation: run multiple LLM calls per task, report variance, perturb weights to test sensitivity, and show examples of generated cost functions across tasks.
- Add confidence intervals or statistical tests for the 10-trial results, and clarify whether the contact-strategy ablation numbers are single-run or averaged.
- Specify randomization ranges and provide prompt templates for the VLM physical parameter estimation.

## Score and Decision

**Anchor comparison summary:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| WtHKqtHVXo (LLM policy code for contact-rich) | 4.00 | R1 | CoRAL is clearly stronger — more tasks, better ablations, more principled LLM-controller interface |
| qGL6fE1lqd (LLMPhy) | 4.40 | R1 | CoRAL has broader task diversity and better ablation design |
| KTtEICH4TO (CORN) | 4.75 | R2 | Different approach; CoRAL's LLM-controller interface is more novel |
| JWrl5pJCnl (Instruct2Act) | 5.00 | R1 | CoRAL has more novel core idea and better ablation, but Instruct2Act has real-world experiments |
| Afjf6izLvJ (Visuomotor Language Guidance) | 5.33 | R2 | CoRAL is comparable in quality |
| iTsHStJKcm (Make a Donut) | 5.25 | R2 | Similar LLM+physics paradigm; CoRAL's closed-loop refinement is an advantage over Make a Donut's open-loop LLM plan |
| h7aQxzKbq6 (HAMSTER) | 6.00 | R2 | CoRAL is below — HAMSTER has real-world validation, more rigorous experimental design |
| c0chJTSbci (SuSIE) | 6.25 | R2 | CoRAL is clearly below — SuSIE has SOTA benchmark results, real-world experiments, stronger validation |
| lFYj0oibGR (RoboFlamingo) | 6.50 | R2 | CoRAL is clearly below |

Round 1 bracket: 4.5–6.5. Round 2 narrowed to 5.0–5.5 based on comparison with Instruct2Act (5.00) and Make a Donut (5.25). CoRAL is modestly stronger than Instruct2Act (more novel interface, better ablations) but below the 6.0+ papers that have real-world validation. The structural confound in the headline VLA comparison and black-box treatment of the core mechanism prevent a higher score.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
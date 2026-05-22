Now let me write the consolidated review.

## Summary

CoRAL proposes a modular neuro-symbolic framework for zero-shot contact-rich robotic manipulation. It separates a VLM (GPT-4o) for environment perception and parameter estimation from an LLM for high-level strategy formulation (generating MPPI cost functions and contact strategies), couples these to an MPPI controller with reactive feedback, and adds a memory unit and an online adaptation loop. Evaluated across 6 simulated manipulation tasks and compared against OpenVLA, π₀.₅, and expert-designed cost baselines, the paper shows that the modular design outperforms monolithic VLA variants and that the adaptation loop and memory unit provide measurable gains.

## Strengths

1. **Modular separation of VLM and LLM roles is empirically validated as critical.** The Unified VLM ablation (Table 1) collapses to 0/10 on 4 of 6 tasks while the full system succeeds — directly supporting the paper's central architectural claim.

2. **Comprehensive ablation study covering four architectural components.** The paper systematically ablates the memory unit, the online refinement loop, the pose estimator, and the VLM/LLM role separation across all 6 tasks. This provides a clear picture of each component's contribution.

3. **Online adaptation and memory unit show tangible behavioral improvements.** The w/o Refinement ablation on T1 (0/10 vs. 4/10) and the memory benefit on T1 (2/10 → 4/10) and T6 (5/10 → 7/10) demonstrate that both mechanisms contribute beyond baseline MPPI.

4. **LLM-generated contact strategies quantitatively reduce planning complexity.** The guided vs. unguided "Flip with Wall" comparison (83.9% fewer steps, 63.9% shorter path) cleanly isolates the value of the LLM's symbolic contact reasoning.

5. **Natural-language explainability of failure diagnosis** is a genuine advantage over black-box VLA policies, and the paper provides a concrete example of this capability.

## Weaknesses

### Fatal
None.

### Major

1. **Figure 4 does not support the claimed mass correction and the text overstates the result.** The text (Section 4.1.4) states that the evaluation world was initialized with mass 2.0 kg (ground truth 0.1 kg) and friction 0.9 (true 0.5), and that the LLM's adaptation converged "remarkably close to their true values." Figure 4, however, shows the corrected mass starting at 1.0 kg and converging to ~0.85 kg — still 8.5× the true value of 0.1 kg. The y-axis range (0.75–1.00 kg) cannot even display the ground truth. The figure also shows the "Initial Mass" as 1.0 kg, not 2.0 kg as claimed in the text. This discrepancy between the described experiment and the presented evidence directly undermines a core demonstration claim. The broader qualitative claim that the adaptation loop helps is still supported by the w/o Refinement ablation, but this specific quantitative evidence for online parameter correction is invalid as presented.

2. **VLA baseline comparison is overclaimed.** OpenVLA-OFT and π₀.₅ are evaluated zero-shot using LIBERO-OBJECT/G OAL checkpoints on custom tasks (T1, T4–T6) that are not in the LIBERO benchmark. The paper frames the results as "even fine-tuning an end-to-end policy is insufficient for scenarios that demand explicit physical modeling" — but the baselines were never fine-tuned on these tasks. The zero-shot comparison itself is standard practice, but the conclusion that *fine-tuning* would be insufficient does not follow from the evidence presented. The human-expert cost baselines are the more appropriate comparators, and against them CoRAL's performance is below the FSM variant on every task (e.g., T1: 4/10 vs 8/10; T6: 7/10 vs 9/10), a comparison the paper presents but does not sufficiently discuss.

3. **The LLM interface for generating cost functions and contact strategies is critically underspecified.** The paper states that the LLM generates J₀ and C₀ as mathematical expressions and surface regions, and that it is "free to introduce any cost terms constructible from the available state, pose, and action variables." No prompt templates, output formats, parsing strategies, or examples of generated cost functions are provided. Equation (2) is explicitly labeled as an "illustrative example." The memory retrieval mechanism (Eq. 1) is described as "RAG_Retrieve" with no specification of the embedding model, similarity metric, or retrieval threshold. Without these details, the paper's central technical contribution cannot be independently reproduced or assessed.

4. **The "failure" condition that triggers the outer loop is never defined.** The outer loop activates after N_retry = 15 "persistent failures," but what constitutes a failure in the inner loop (the MPPI retry loop) is not specified. This makes it impossible to interpret the outer loop's behavior or compare retry counts across conditions.

### Minor

1. **Simulation-only evaluation with no real-world validation.** The paper claims to address "contact-rich manipulation" and "dynamic manipulation scenarios," and the reactive control module is described as using "real-time sensors (e.g., force/torque)." All experiments are conducted in ROBOSUITE/MuJoCo simulation with noiseless sensors. While simulation-only evaluation is common and acceptable, the paper's framing (especially the "robustness" and "adaptive manipulation" language) implies a scope that the experiments do not fully cover. The limitations section acknowledges latency but does not mention the simulation-only setting.

2. **Statistical rigor is weak.** All experiments use 10 trials per condition. Several ablation differences are 1/10 or 0/10 between variants (T2, T4), which is noise-level at this n. No confidence intervals, significance tests, or variance measures are reported. The 83.9% and 63.9% improvement claims for guided vs. unguided "Flip with Wall" lack any error reporting.

3. **The VLM's parameter estimation (mass, friction) is not ablated separately.** The paper does not test whether VLM-estimated parameters outperform random initialization or fixed defaults. If the online adaptation loop is doing all the corrective work, the VLM's role as a parameter estimator could be superfluous or even harmful.

### Trivial
None.

## Nice-to-Haves

- A dedicated ablation comparing VLM-estimated parameters vs. ground-truth parameters vs. fixed defaults would clarify whether the VLM contributes beyond what the adaptation loop can recover from.
- Alternative pose estimators (e.g., a simple keypoint detector) could be compared against FoundationPose to test whether the catastrophic failure in the w/o Pose Tracking ablation is specific to the VLM or general to any non-specialized pose estimator.
- Reporting confidence intervals or running more trials (20–30) per condition would strengthen the quantitative evidence.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that the mass correction shows only one step (at 1 second) rather than "iterative refinement":** The figure does show a correction step and then a plateau; the "iterative" claim in the text could be overstated but the figure itself shows the correction happening. This is subsumed by the larger Figure 4 discrepancy.
- **Criticism about no real-world experiments being "insufficient for the level of claim":** The harsh critic's framing ("insufficient") is too strong. Simulation-only is a common limitation for methodological papers in this area. Rated as minor.
- **Criticism about 10 trials being too few for statistical significance:** While true, this is standard for the field. Moved from its standalone position to Minor weakness #2.
- **Strength about "zero-shot performance surpasses fine-tuned end-to-end VLA baselines":** Partially removed because the baselines were not fine-tuned on these tasks; the framing is misleading. The zero-shot comparison result itself is still valid.
- **Various formatting/presentation nitpicks:** Removed per instructions.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Correct Figure 4 and the associated text.** Either replace the figure with data that matches the described experiment (initial 2.0 kg → convergence to a value meaningfully close to 0.1 kg), or honestly report the correction achieved (e.g., from 1.0 kg to 0.85 kg) and discuss why the correction plateaus far from the truth. This single fix would most improve the paper's credibility.

2. **Reframe the VLA baseline comparison.** Replace the claim about "fine-tuning being insufficient" with a more measured statement about zero-shot transfer. If possible, add a fine-tuned baseline on the custom tasks, or lean into the human-expert comparison which is more informative.

3. **Provide the LLM prompts, output format, and parsing logic** in an appendix or on the project website. The paper's core mechanism is opaque without these details.

4. **Define the inner-loop failure condition** that triggers N_retry and the outer loop.

5. **Add confidence intervals or run additional trials** for the main results, especially for ablation comparisons where differences are small (1–2/10).

## Score and Decision

### Calibration

**Round 1 (Bracketing, 3 queries on "LLM-based robotic manipulation control contact-rich zero-shot"):**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| wl1Kup6oES - "From Appearance to Motion" | 3.00 | 1 | Weaker: narrower scope, less novel architecture. |
| oyXoGJQlUf - "GRAIL" | 3.00 | 1 | Weaker: focuses on PDDL generation, less comprehensive evaluation. |
| Q6HYM1EMu8 - "LARG2" | 3.00 | 1 | Weaker: RL-based, less direct relevance. |
| KBSHR4h8XV - "Early Fusion VLA" | 3.33 | 1 | Weaker: standard VLA fine-tuning, less novel architecture. |
| **WtHKqtHVXo - "Generating Robot Policy Code"** | **4.00** | **1** | **Most comparable: same topic (LLM for contact-rich), weaker evaluation (2 tasks), has real robot. CoRAL is stronger in breadth but has Figure 4 issue.** |
| cbVnJa4l2o - "LLM+A" | 4.00 | 1 | Similar: LLM for planning+control, weaker evaluation. |
| iTsHStJKcm - "Make a Donut" | 5.25 | 1 | Stronger: real-world experiments, cleaner evaluation, narrower scope (deformable objects). |
| Aqfwhna1D7 - "CrayonRobo" | 5.20 | 1 | Comparable: similar level of evaluation, different approach. |
| OI3RoHoWAN - "GenSim" | 8.00 | 1 | Much stronger: accepted, real-world, comprehensive. |
| 7BLXhmWvwF - "Geometry-aware RL" | 8.00 | 1 | Much stronger. |
| KsUh8MMFKQ - "Thin-Shell" | 8.00 | 1 | Much stronger. |
| pISLZG7ktL - "Data Scaling Laws" | 8.00 | 1 | Much stronger. |

Initial bracket from round 1: **[4.0, 5.5]**

**Round 2 (Narrowing within bracket):**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| qGL6fE1lqd - "LLMPhy" | 4.40 | 2 | Comparable: LLM+simulator for physics reasoning, CoRAL has more comprehensive evaluation but Figure 4 issue. |
| KTtEICH4TO - "CORN" | 4.75 | 2 | Comparable: different approach (RL), similar evaluation depth. |
| baQ0ICrnCR - "RoboPro" | 4.25 | 2 | Weaker: code generation for manipulation, less novel architecture. |
| VaoeAi5CW8 - "Diffusion Trajectory-guided Policy" | 4.25 | 2 | Weaker: different paradigm (diffusion + imitation), less novel architecture. |
| MWHIIWrWWu - "MPC²" | 6.25 | 2 | Stronger: accepted, clean evaluation, different domain (musculoskeletal). |
| gVnJFY8nCM - "Residual-MPPI" | 6.25 | 2 | Stronger: accepted, clean evaluation. |

**Narrowing reasoning:** CoRAL sits near the upper end of the 4.0–5.0 band based on architectural novelty and evaluation breadth. However, the Figure 4 discrepancy is a significant credibility concern that pulls it below papers like "Make a Donut" (5.25), which has real-world validation and cleaner evidence. CoRAL is stronger than "Generating Robot Policy Code" (4.0) because of wider task coverage and more informative ablations. It is comparable to "CORN" (4.75) — both have interesting architectures but notable limitations.

**Final score:** 4.5

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 8, 6
Now I have all the information I need. Let me compose the final consolidated review.

## Summary

CLoSD presents a closed-loop system that integrates a fast autoregressive diffusion planner (DiP) with a physics-based motion tracking controller (PHC) for multi-task text-driven character control. The key insight is that the diffusion planner operates online, continuously receiving simulated motion as prefix feedback, which enables interactive control, physical plausibility correction, and object interaction — all with a single policy. The method demonstrably succeeds on goal-reaching, striking, sitting, and get-up tasks, and achieves strong text-to-motion benchmark results.

## Strengths

1. **Real-time diffusion planner enables the closed-loop architecture.** DiP generates 40-frame motion plans in 11.4 ms (3,500 fps, 175× real-time) using only 10 diffusion steps (vs. 50 for MDM). This speed is the technical enabler of the entire closed-loop system and is clearly documented with concrete measurements (Section 4.1, lines 203–207).

2. **Closed-loop fine-tuning is empirically shown to be critical for interaction tasks.** The paper's ablations (Table 1) show that without closed-loop fine-tuning, striking success falls from 82% to 31% and sitting from 83% to 34%. The fine-tuning procedure adapts the PHC tracker to the distribution of DiP-generated plans and object interactions, directly validating the core claim that the loop between planner and executor is essential.

3. **Single policy handles multiple distinct tasks without task-specific reward engineering.** The same fine-tuned tracking policy, using only the original PHC rewards, achieves strong success rates on goal-reaching (94%), striking (82%), sitting (83%), and get-up (71%) simultaneously. This contrasts with prior work (ASE, InterPhys) that required dedicated policies per task.

4. **Outperforms the leading physics-based text-to-motion controller (MoConVQ) on HumanML3D.** CLoSD surpasses MoConVQ on all standard metrics (R-precision, FID, Diversity, Multimodal distance) while also dramatically reducing physical artifacts (penetration, floating, skating) compared to kinematic diffusion models. The comparison uses released code and follows the authors' procedures (Section 5.3).

5. **Adaptive target conditioning with validity signals enables seamless task switching.** The design allows arbitrary joints to serve as targets, changed on the fly via boolean validity signals (Section 4.1). This directly underpins the multi-task capability and is evaluated in the striking task where end-effector and text are sampled per episode.

6. **Systematic ablation studies isolate contributions of key design choices.** Experiments ablate closed-loop feedback, fine-tuning, and plan length (Table 1), and fine-tuning and plan length for text-to-motion (Table 2). These provide quantitative evidence for why each component matters and justify the chosen 40-frame trade-off.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims — that the closed-loop design improves interaction-task performance and that the fast diffusion planner makes online replanning feasible — are well-supported by the open-loop vs. closed-loop comparisons and ablations. No identified weakness undermines the central contribution.

### Minor

1. **Limited set of multi-task baselines weakens the "state-of-the-art" claim.** The paper claims to "outperform both the current leading text-to-motion controller and the state-of-the-art multi-task controller" (line 61). For multi-task performance, only UniHSI is compared, and the paper itself acknowledges that UniHSI "was designed for contact-point reaching without semantic text input" and "touches the target instead of striking it" (lines 294–296). PADL/SuperPADL are discussed in related work (line 91) but not compared, even on a common subset of tasks. While the paper's internal ablations (open-loop vs. closed-loop) convincingly validate the closed-loop contribution, the external comparison is weaker than the text-to-motion evaluation. The authors should either add comparisons on a feasible subset or scope the multi-task claim more precisely.

2. **Insufficient analysis of diffusion planner generalization to object-interaction tasks.** DiP is trained on HumanML3D, which contains everyday motions without object interactions (as the paper notes in lines 159–162). For tasks like sitting on a sofa and striking a kickboxing bag, the planner must generalize to motions aligning specific joints with object geometries never seen in training. The paper does not analyze how this generalization works, what the planned motions look like before simulation, or what failure cases occur when the planned motion is inconsistent with the object geometry. While the closed-loop system demonstrably works, the paper would benefit from an analysis of planner quality for these out-of-distribution scenarios.

3. **Physics metrics comparison is not fully contextualized.** CLoSD's physics metrics (penetration, floating, skating) are computed on the simulated motion, while the same metrics for kinematic baselines are computed on their raw output. The paper states "physics-based text-to-motion significantly improves the physical metrics" (line 320) without explicitly discussing this asymmetry. The improvement over kinematic methods is expected but should be stated more carefully; the fairer comparison is with MoConVQ (also physics-based), where CLoSD wins on all metrics.

4. **Some reproducibility details for fine-tuning are omitted.** The paper states "We use the original PHC rewards and reset conditions" (line 239) and fine-tunes for 4K PPO epochs (line 266), but does not report the learning rate, discount factor, reward weights for the multi-component PHC reward, or whether any hyperparameters changed from the original PHC setup. While referencing the PHC paper is standard, the fine-tuning is a central contribution and would benefit from explicit hyperparameter reporting.

5. **Failure modes not discussed.** The paper reports only success rates. Understanding when and why the method fails (e.g., Does the character fall during striking? How often does the character miss the bag? Are there systematic failures for certain text prompts or object positions?) would substantially strengthen the evaluation.

6. **Open-loop baseline implementation underspecified.** The description says DiP "generates the motion offline, fed by its own prediction, and then the tracker follows this fixed trajectory" (line 269). It is unclear whether the diffusion model iterates autoregressively using its own predictions (prefix from its own output) or generates the entire motion in one pass. Since the open-loop vs. closed-loop gap is a key result, this should be replicable.

### Trivial

- **State machine detection thresholds not specified.** Tasks signal completion via criteria like "pelvis is on the sitting area of the sofa" (line 244), but the exact geometric threshold or detection mechanism is not described. This is a minor clarity issue unlikely to affect reproducibility.

## Nice-to-Haves

- Provide confidence intervals or standard deviations for success rates (Table 1), since tasks involve stochastic initialization.
- Analyze the planner-tracker gap quantitatively (e.g., compare planned vs. simulated trajectories for a few episodes) to further validate the closed-loop benefit.
- Add visualization of DiP's planned motions for the sofa and bag tasks to demonstrate planner generalization qualitatively.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"175× real-time claim overstates the entire system"** — The critic claimed the 175× figure overstates the full system speed. The paper explicitly says "Our **diffusion planner** generates 40-frame plans at 3,500 fps" (line 62) and "It [DiP] generates 2 seconds of reference motion in 11.4 ms" (line 204). The claim is correctly scoped to the planner. REMOVED (misreading).

- **"Target loss at each diffusion step deviates from standard practice"** — The critic claims applying the target loss at each diffusion step is a deviation. The paper states "we follow MDM" (line 186), and MDM (Tevet et al., 2023) — a widely-cited paper — also applies geometric losses at each denoising step for x₀-prediction models. This is standard practice. REMOVED (factually incorrect).

- **"Text-to-motion ablation unclear on how target conditioning is disabled"** — The paper's adaptive target conditioning uses validity signals (line 183: "a boolean validity signal vⱼ per joint which indicates if it is currently used as a condition"). Disabling target conditioning means setting these to false, which is described. REMOVED (already addressed).

- **Missing appendix content, missing proofs, missing related works** — REMOVED per hard rules: the parser strips appendix content; missing related works cannot be confirmed without external sources.

- **Pure formatting/style nitpicks and reproducibility complaints about trivial implementation details** — REMOVED per hard rules.

- **"PADL/SuperPADL code not available" or similar existence doubts** — REMOVED per hard rule: all cited references are assumed to exist.

## Novel Insights

None beyond the paper's own contributions. The reviews affirm the paper's main claims but do not surface a new angle or unexpected implication that the paper itself does not already articulate.

## Suggestions

1. **Add baseline comparisons on a common subset for multi-task claims.** Even if PADL or SuperPADL cannot perform all four tasks, compare on goal-reaching with text prompts. Explicitly state why certain baselines are excluded (e.g., "PADL does not support object interaction, so we compare on goal-reaching only"). Alternatively, scope the multi-task claim to the evaluated baselines.

2. **Analyze planner generalization to object interaction.** Provide visualizations or quantitative metrics (e.g., joint-angle plausibility, contact consistency) of the motions DiP generates for sofa and bag tasks *before* simulation. Show what the closed-loop corrects.

3. **Clarify the physics metrics comparison.** Explicitly state that physics metrics for kinematic baselines are computed on their raw output, while CLoSD's are computed on simulated motion, and clarify that the more informative comparison is against MoConVQ (a fellow physics-based method).

4. **Report fine-tuning hyperparameters.** Provide learning rate, discount factor, reward component weights (or state explicitly they are unchanged from PHC), and any environment configuration changes.

5. **Add a failure analysis section.** Describe common failure modes, their frequency, and qualitative examples. This would significantly improve the paper's assessment of robustness.

6. **Provide more detail on the open-loop baseline.** Specify whether DiP feeds its own predictions as prefix autoregressively or generates the full trajectory in one shot during open-loop evaluation.

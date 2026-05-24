Now let me write the final consolidated review.

## Summary

CoRAL proposes a modular neuro-symbolic framework that integrates a vision pipeline (FoundationPose + VLM) with an LLM that generates cost functions and contact strategies for an MPPI controller, enabling zero-shot execution of contact-rich manipulation tasks. The key architectural ideas are: (i) explicit separation of VLM (perception) and LLM (planning/reasoning) roles, (ii) an LLM-driven outer loop for online parameter and strategy adaptation, and (iii) a memory unit for retrieval-augmented experience reuse. Experiments across six simulated manipulation tasks show the full system outperforming end-to-end VLA baselines (OpenVLA-OFT, π₀.₅) on contact-rich tasks, with ablations confirming the importance of each component.

## Strengths

- **Separation of VLM and LLM roles is clearly beneficial.** The *Unified VLM* ablation, which collapses perception and planning into a single multimodal call, catastrophically fails on nearly all contact-rich tasks (0/10 on T1, T3, T4, T5, T6, Table 1). This provides direct evidence that dedicating the VLM to perception and the LLM to strategy formulation is a critical design choice.

- **Zero-shot outperformance of end-to-end VLAs on contact-rich tasks.** CoRAL achieves non-trivial success on tasks where OpenVLA-OFT and π₀.₅ completely fail (e.g., T1: 4/10 vs. 0/10; T6: 7/10 vs. 0/10, Table 1). This demonstrates that the modular architecture can handle dynamic contact scenarios without teleoperation data or task-specific fine-tuning.

- **LLM-guided contact strategy dramatically reduces planning cost.** On T6 (Flip with Wall), providing the LLM's symbolic contact strategy makes the planner 83.9% faster (32 vs. 199 steps) and reduces end-effector path length by 63.9% (1.33 m vs. 3.69 m) compared to uninformed sampling (§4.1.4). This quantifies a concrete benefit of the LLM's output.

- **Memory unit provides measurable improvement.** CoRAL with Memory consistently outperforms the w/o Memory variant in both success rate and completion time (e.g., T1: 4/10 vs. 2/10, T6: 7/10 vs. 5/10, Table 1), supporting the value of retrieval-augmented experience reuse.

- **Competitive with expert-designed costs on hard tasks.** On T5 and T6, CoRAL (9/10, 7/10) approaches the Expert FSM upper bound (10/10, 9/10) while far exceeding the single-stage expert (9/10, 3/10), indicating the LLM automatically recovers much of the structure of carefully engineered costs (§4.1.2).

## Weaknesses

### Major

- **Figure 4 is inconsistent with the text, undermining the online adaptation claim.** The text (§4.1.4) states the *Evaluation World* was initialized with mass = 2.0 kg (ground truth = 0.1 kg). However, Figure 4 shows estimated mass on a 0.75–1.00 kg axis, with the "Initial Mass" at 1.0 kg and the "Corrected Mass" converging to ~0.85 kg. The numerical values do not match the described experimental condition (no trajectory approaches 2.0 kg or 0.1 kg), and the claim that "the agent's belief about mass converged remarkably close to their true values" (0.1 kg) is unsupported by the presented data, which shows convergence to 0.85 kg. This is not a minor labeling error — it is a structural inconsistency in the evidence for a claimed contribution (online physical parameter correction). The adaptation mechanism may still be real, but the paper's primary illustration of it is compromised.

- **Factual inconsistency in the w/o Pose Tracking ablation discussion.** The paper states (§4.1.3) that removing FoundationPose "resulted in a catastrophic failure across all tasks (0/10 success)." However, Table 1 shows CoRAL (w/o Pose Tracking) achieves 9/10 on T2 (Pick+Place Box). While T2 is the simplest task, the categorical "0/10 across all tasks" is factually incorrect. This undermines trust in the paper's reporting.

### Minor

- **Limited statistical reporting for binary success metrics.** With only 10 trials per condition, the differences the paper treats as meaningful (e.g., 2/10 vs. 4/10 on T1, 6/10 vs. 9/10 on T4) have wide confidence intervals. No confidence intervals, exact binomial p-values, or acknowledgment of sampling uncertainty are provided. This does not invalidate the results but makes the strength of the ablation conclusions unclear.

- **The VLA comparison does not isolate the LLM's contribution.** OpenVLA-OFT and π₀.₅ are reactive policies without access to a dynamics model or planner, while CoRAL uses MPPI with MuJoCo rollouts — a fundamentally more powerful capability for contact-rich tasks. The paper does include Expert (hand-designed cost) baselines with the same MPPI controller, which partially addresses this concern. However, the main framing ("CoRAL significantly outperforms state-of-the-art baselines") overclaims because the comparison tests *planning vs. reactive control* rather than the LLM's specific reasoning ability. A cleaner ablation would compare against a version of the same MPPI controller with a fixed (non-LLM, non-expert) generic cost function.

- **Explainability claim lacks systematic evidence.** The paper states CoRAL "enhances explainability" and can "articulate why it failed," but provides only a single anecdotal example (with reference to an appendix that was not available in the reviewed manuscript). Given that LLMs can produce post-hoc rationalizations not corresponding to their internal decision process, a systematic evaluation (or at minimum, a stronger warning about this caveat) is needed. This claim should be downscaled or accompanied by a clear limitation.

- **Methodological details are underspecified for reproducibility.** The interface between the LLM's textual output and the MPPI planner's cost function is described at a high level but critical details are absent: the exact prompt templates, whether the cost function is output as code/JSON/natural language, the embedding model and similarity computation for memory retrieval, and the format of logged episode data fed to the online adaptation module.

### Trivial

- "The VLM, while powerful for semantic understanding, is ill-suited..." — minor grammatical issues.
- References to "Appendix ??" in the text indicate a cross-reference that was not resolved in the reviewed version.

## Nice-to-Haves

- A controlled baseline using the same MPPI controller with a fixed, generic (non-expert, non-LLM) cost function would cleanly isolate the LLM's contribution.
- Real-robot validation, or at minimum a more detailed discussion of how the reactive control augmentation (Eq. 7) bridges the sim-to-real gap on physical hardware. The current framing about "deploying robots in unknown environments" is speculative without this.
- Sensitivity analysis on key hyperparameters (temperature λ, number of rollouts K, retry threshold N_retry).

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Missing related works"** — Removed per instructions (cannot confirm existence of unmentioned works).
- **Weakness about the paper needing real-robot experiments** — Removed as scope creep; the paper explicitly focuses on simulation evaluation and discusses sim-to-real limitations. This is a nice-to-have, not a weakness.
- **Weakness about the Unified VLM ablation being "poorly controlled"** — Removed; the ablation tests exactly the separation-of-roles hypothesis it claims to test. The failure is informative regardless of whether the prompt could be engineered differently.
- **"The paper's conclusion that CoRAL narrows the gap to the expert should be qualified"** — Removed; the paper already reports the gap honestly (Table 1 shows CoRAL at 4/10 vs. Expert FSM at 8/10 on T1, 7/10 vs. 9/10 on T6).
- **"Reproducibility concerns about undisclosed hyperparameters"** — The key hyperparameters (K=200, H=50, λ=0.1, N_retry=15) are stated. The harsh critic's request for complete training logs and prompt templates is beyond typical reproducibility expectations for a conference submission.
- **Strength Finder claim #3 (online adaptation converging "close to true value")** — Removed from Strengths because it is factually contradicted by the Figure 4 inconsistency identified above. The adaptation direction is correct, but the claim of convergence to ~0.1 kg is not supported by the evidence.
- **Strength Finder claim about "0/10 on all complex tasks" for w/o Pose Tracking** — The accuracy of "all complex tasks" depends on whether T2 counts as complex. Since T2 is the simplest pick-and-place baseline, the strength remains approximately correct but is qualified.

## Novel Insights

None beyond the paper's own contributions. The review process did not surface a perspective that fundamentally reframes or deepens the paper's findings beyond what the authors already present.

## Suggestions

1. **Fix the Figure 4 / §4.1.4 inconsistency.** Clarify what the figure actually shows: is this the VLM's initial estimate being corrected by the LLM? What were the actual numerical values used? If the Evaluation World had mass=2.0 kg, why does the figure show estimates on a 0.75–1.00 kg axis? Correct the claim about "converging remarkably close to true values" (0.1 kg) to accurately reflect what the data supports.
2. **Correct the w/o Pose Tracking description** to match Table 1 (9/10 on T2, not 0/10 across all tasks).
3. **Add confidence intervals or exact binomial test results** for the 10-trial success-rate comparisons, or explicitly acknowledge the uncertainty when drawing conclusions from small binary samples.
4. **Downscale the explainability claim** to a qualitative observation with a clear caveat about post-hoc rationalization, or remove it.
5. **Add a baseline** using the same MPPI controller with a fixed, task-agnostic cost function to isolate the LLM's contribution from the planning advantage.
6. **Provide key implementation details** in an appendix: prompt templates, LLM output format (code/JSON/structured text), memory embedding model and similarity metric.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):**
- *Weak band (< 3.5)*: Searched for "LLM-based robotic control contact-rich manipulation zero-shot". Retrieved anchors at 3.00 (wl1Kup6oES), 3.00 (oyXoGJQlUf), 3.00 (Q6HYM1EMu8), 3.40 (EODzbQ2Gy4), 3.33 (KBSHR4h8XV). All rejected. This paper is clearly stronger than all of these.
- *Middle band (3.5–7.5)*: Searched for "LLM for robot manipulation planning modular neuro-symbolic control". Retrieved anchors at 6.67 (hQVCCxQrYN, Plan-Seq-Learn, accept), 4.00 (WtHKqtHVXo, Generating Robot Policy Code, reject), 5.25 (iTsHStJKcm, Make a Donut, reject), 4.00 (cbVnJa4l2o, LLM+A, reject), 5.00 (JWrl5pJCnl, Instruct2Act, reject).
- *Strong band (> 7.5)*: Retrieved anchors at 8.00 (all accept). This paper is clearly below these.

**Round 2 (Narrowing within bracket):**
- *Narrow search (3.5–5.5)*: Retrieved anchors at 4.00 (Generating Robot Policy Code), 5.25 (Make a Donut), 4.00 (LLM+A), 4.40 (LLMPhy).
- *Narrow search (4.5–6.5)*: Retrieved anchors at 5.50 (GenBot), 4.75 (On Evaluation of Generative Robotic Simulations), 5.00 (Instruct2Act), 6.25 (Online Self-Improvement).

**Anchor comparisons informing final score:**
- *Generating Robot Policy Code (4.00)* — Very similar topic (LLMs for contact-rich tasks). That paper had no baselines, weaker experiments. CoRAL is clearly stronger → CoRAL above 4.0.
- *LLMPhy (4.40)* — LLM+physics engine for physical reasoning. Had very limited experiments (3 categories). CoRAL has more extensive evaluation → CoRAL above 4.4.
- *Instruct2Act (5.00)* — LLM maps instructions to actions. Comparable modular approach and experimental thoroughness. CoRAL is roughly at this level.
- *Make a Donut (5.25)* — LLM-guided hierarchical planning with real-world validation. CoRAL has more extensive ablations but weaker evidence on one key claim (Figure 4). CoRAL slightly below.
- *Plan-Seq-Learn (6.67, accept)* — Stronger paper with 25+ tasks, thorough evaluation. CoRAL is below this.
- *Online Self-Improvement (6.25)* — Real-world validation, stronger methodology. CoRAL is below this.

**Initial bracket:** Between 4.0 and 5.5.
**Final score anchored at:** 5.0. CoRAL is comparable to Instruct2Act (5.00), above Generating Robot Policy Code (4.00) and LLMPhy (4.40), but below Make a Donut (5.25) due to the Figure 4 evidence inconsistency and below the accept-level papers (6.25+). The paper has a promising architecture and several well-supported design insights, but the evidence problems with the online adaptation claim and the factual inaccuracy about w/o Pose Tracking prevent it from being a stronger paper.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
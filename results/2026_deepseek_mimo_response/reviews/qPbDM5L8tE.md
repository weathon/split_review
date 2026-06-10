Now I have enough comparison data. Let me finalize.

**Round 1 bracket:** 5.0–6.5 (clearly above weak anchors like RePLan at 4.25 and policy code gen at 4.00, but clearly below GenSim at 8.00)

**Round 2 narrowing:** The paper is comparable to HAMSTER (6.00, borderline accept with mixed reviews) but has a significant evidential integrity issue (Figure 4) that HAMSTER doesn't have. It's below Plan-Seq-Learn (6.67, clean accept) which has broader evaluation (25+ tasks, real-world). I'd position CoRAL slightly below HAMSTER due to the Figure 4 contradiction and information asymmetry.

**Final score: 5.5** — The paper has a genuinely novel architectural idea (LLM-generated cost functions for MPPI) and a comprehensive ablation study supporting most claims. However, the Figure 4/text contradiction undermines the online adaptation claim, the VLA comparison is structurally unfair, and statistical evidence is limited. These prevent it from reaching the borderline-accept range.

---

## Summary
CoRAL proposes a modular neuro-symbolic framework for contact-rich robotic manipulation that uses FoundationPose for 6-DoF pose tracking, GPT-4o as VLM for physical parameter estimation and as LLM for MPPI cost function and contact strategy generation, with a RAG-based memory unit for experience reuse. Evaluated on 6 simulated tasks with a Franka Panda arm, the system demonstrates strong zero-shot performance against fine-tuned VLA baselines and ablation studies supporting the necessity of each architectural component.

## Strengths
- **Comprehensive ablation study with clean, large performance gaps:** Table 1 demonstrates that removing pose tracking yields 0/10 across all non-trivial tasks; the Unified VLM variant achieves 0/10 on T1, T3, T5, T6; removing refinement drops T1 from 4/10 to 0/10; removing memory reduces T6 from 7/10 to 5/10. These substantial gaps across four ablation axes provide strong evidence for the architectural claims.
- **LLM-generated contact strategies dramatically prune the search space:** Section 4.1.4 shows that the LLM-guided approach on T6 is 83.9% faster (32 vs 199 steps) and uses a 63.9% shorter end-effector path (1.33m vs 3.69m) compared to uninformed sampling, directly validating the symbolic reasoning contribution.
- **Genuinely novel architectural concept:** Elevating the LLM's role from perceptual guide (as in VLMPC, IMPACT) to a strategist that formulates the mathematical structure and weights of the MPPI controller's cost function is a distinct and well-motivated contribution that grounds abstract reasoning directly into optimal control.
- **Strong zero-shot performance against fine-tuned VLA baselines on contact-rich tasks:** CoRAL achieves 9/10 on T4 and T5 while OpenVLA-OFT achieves 0/10 and 1/10, and π₀.₅ achieves 0/10 and 3/10 (Table 1).
- **Honest inclusion of expert-designed baselines as upper bounds:** The FSM and single-stage expert baselines provide meaningful reference points, and the paper honestly reports that CoRAL approaches but does not surpass the FSM expert, framing this as "approaching expert-level performance while reducing manual tuning effort."

## Weaknesses

### Fatal
None.

### Major
- **Figure 4 contradicts the text — evidential integrity concern.** The text in Section 4.1.4 (lines 220–222) states: "we intentionally initialized the Evaluation World with a severely overestimated mass (2.0 kg vs. a ground truth of 0.1 kg) and friction coefficient (0.9 vs. 0.5)." However, Figure 4 (lines 244–246) shows the y-axis ranging from 0.75 to 1.00 kg, with Initial Mass at 1.00 kg and corrected mass converging to ~0.85 kg — nowhere near the stated 2.0 kg or 0.1 kg. This figure is the primary evidence for online parameter adaptation, one of the paper's four key contributions. The contradiction must be resolved: either the figure is from a different experiment, or the text contains wrong numbers.
- **Structurally unfair comparison to VLA baselines due to massive information asymmetry.** CoRAL operates with known 3D geometric object models (for FoundationPose), a full physics engine for forward-simulating 200 MPPI rollouts of 50 steps per control cycle, force/torque sensor data from the engine, and GPT-4o for both perception and adaptation. The VLA baselines receive only RGB-D images and task descriptions (lines 163–164). Yet the paper draws the strong conclusion (line 193) that "even fine-tuning an end-to-end policy is insufficient for scenarios that demand explicit physical modeling" — a claim that conflates architectural advantage with informational advantage. The comparison should be explicitly reframed or made fairer.

### Minor
- **Only 10 trials per condition with no statistical analysis.** All results in Table 1 are based on 10 trials with binary success. Differences like 4/10 vs 2/10 (T1, memory ablation) and 9/10 vs 7/10 (T5, memory ablation) are within noise for 10 Bernoulli trials. The paper draws component-necessity conclusions from these differences without confidence intervals or statistical tests.
- **Memory retrieval mechanism underspecified.** Lines 75–79 describe RAG-based retrieval where "the LLM embeds the current task into a latent semantic space" but do not specify: whether this uses GPT-4o's internal embeddings or a separate embedding model, the similarity metric, or the threshold for "sufficiently similar." This makes the component difficult to reproduce.
- **LIBERO benchmark integration unclear.** The paper claims to incorporate "two benchmark tasks from the LIBERO suite" (line 150–151), but all six described tasks (T1–T6) appear to be custom. It is unclear which tasks are from LIBERO or how the VLA baselines (fine-tuned on LIBERO) perform specifically on those tasks.
- **Reactive control augmentation claimed for sim-to-real but only validated in simulation.** Equation 7 and lines 126–130 present the reactive control augmentation as mitigating the "sim-to-real gap," but all experiments are purely in simulation. This claim is entirely unvalidated.
- **Cost function generality claim overstated.** The paper claims the LLM can "introduce any cost terms constructible from the available state, pose, and action variables" (line 91), but all examples and the shown cost function (Eq. 2) are weighted sums of squared distances, indicator functions, and control penalties. No case is demonstrated where the LLM generates a genuinely novel cost term structure.

### Trivial
None.

## Nice-to-Haves
- Latency analysis: The paper acknowledges "computational latency from its sequential pipeline" as a limitation (line 242) but never reports per-component timing (LLM calls, MPPI rollouts, FoundationPose). This would help assess practical deployability.
- Prompt engineering details: The system's behavior depends heavily on GPT-4o prompts for cost function generation, contact strategy, and online adaptation. Representative prompt examples would help assess robustness to prompt variation.
- Demonstrate a genuinely novel cost term structure produced by the LLM to substantiate the generality claim.

## Removed Points
These points are flagged to be removed, treat them with caution.
- **Expert baselines consistently outperform CoRAL (from harsh critic):** Weakened because the paper acknowledges this honestly in Section 4.1.2 and frames CoRAL as approaching expert-level while reducing manual effort. CoRAL matches or exceeds the single-stage expert on hard tasks (T1: 4/10 vs 0/10, T6: 7/10 vs 3/10). The value proposition is automated cost generation, not beating hand-tuned FSMs.
- **Missing appendix/proofs:** Parser strips appendices; these exist in the original.
- **Typos/formatting/formatting artifacts:** Parser issues, not paper problems.

## Novel Insights
The most valuable conceptual contribution is elevating the LLM's role from perceptual guide (as in VLMPC, IMPACT) to a high-level strategist that formulates the mathematical structure and weights of the MPPI controller's cost function. This is a genuinely distinct architectural approach that grounds abstract reasoning directly into the control formulation. The nested feedback-loop architecture (fast inner MPPI loop + slow outer LLM adaptation loop at N_retry=15 failures) is a principled design that mirrors human fast-reactive/slow-deliberative reasoning and could influence future LLM-guided control systems. The comprehensive ablation study, with its large clean gaps across four axes, provides a valuable empirical template for evaluating modular neuro-symbolic systems.

## Suggestions
1. **Resolve the Figure 4 contradiction immediately.** Either provide the correct figure matching the 2.0→0.1 kg experiment described, or correct the text to match the figure's actual parameters.
2. **Reframe the VLA comparison.** Acknowledge the information asymmetry and position the comparison as "modular physics-based planning with LLM specification vs. end-to-end learning from observations" — which is a legitimate and interesting comparison if honestly framed.
3. **Increase trial count to ≥30** and report bootstrap confidence intervals, especially for the ablation study where fine-grained differences drive key conclusions.
4. **Clarify which tasks are from LIBERO** and which are custom. If the VLA baselines were fine-tuned on LIBERO, report their performance specifically on the LIBERO-derived tasks.

## Calibration Report

### Anchors Retrieved

**Round 1 (Bracketing):**
- `/I0To0G5J7g.md` — "Online Self-Improvement for Embodied Multimodal Foundation Models" — avg 3.20 (weak anchor, score -1–3.5)
- `/oyXoGJQlUf.md` — "GRAIL" — avg 3.00 (weak anchor)
- `/BW8O4wHgbo.md` — "Why Solving Multi-agent Path Finding with LLMs has not Succeeded" — avg 3.00 (weak anchor)
- `/jOuHjFw71C.md` — "Planning in Strawberry Fields" — avg 3.00 (weak anchor)
- `/WtHKqtHVXo.md` — "Generating Robot Policy Code for Contact-Rich Manipulation" — avg 4.00 (middle anchor, score 3.5–7.5) — **Read in full.** Weaker than CoRAL: ad-hoc approach, limited baselines, only 2 tasks, no ablation study.
- `/gisAooH2TG.md` — "RePLan" — avg 4.25 (middle anchor) — **Read in full.** Similar modular LLM+VLM idea but with weaker evaluation, fewer tasks, insufficient details on key components. CoRAL is clearly better.
- `/cbVnJa4l2o.md` — "LLM+A" — avg 4.00 (middle anchor)
- `/JWrl5pJCnl.md` — "Instruct2Act" — avg 5.00 (middle anchor)
- `/OI3RoHoWAN.md` — "GenSim" — avg 8.00 (strong anchor, score 7.5–11) — **Read in full.** Clearly stronger than CoRAL: more novel contribution, real-world experiments, universal acceptance.
- `/KsUh8MMFKQ.md` — "Thin-Shell Object Manipulations" — avg 8.00 (strong anchor)
- `/7BLXhmWvwF.md` — "Geometry-aware RL for Manipulation" — avg 8.00 (strong anchor)
- `/pISLZG7ktL.md` — "Data Scaling Laws in Imitation Learning" — avg 8.00 (strong anchor)

**Round 2 (Narrowing):**
- `/VZTFUtldbC.md` — "MeMo: Meaningful Modular Controllers" — avg 4.75 (score 4.5–6.0)
- `/JWrl5pJCnl.md` — "Instruct2Act" — avg 5.00 (score 4.5–6.0)
- `/s3sJenvY5H.md` — "On Evaluation of Generative Robotic Simulations" — avg 4.75 (score 4.5–6.0)
- `/pUKJWr5zOE.md` — "Differentiable Physical Simulation for Soft Robots" — avg 5.00 (score 4.5–6.0)
- `/lFYj0oibGR.md` — "Vision-Language Foundation Models as Effective Robot Imitators" — avg 6.50 (score 5.5–7.0)
- `/h7aQxzKbq6.md` — "HAMSTER" — avg 6.00 (score 5.5–7.0) — **Read in full.** Borderline accept with mixed reviews. CoRAL has a better ablation study but HAMSTER has real-world experiments. The Figure 4 issue puts CoRAL slightly below.
- `/hQVCCxQrYN.md` — "Plan-Seq-Learn" — avg 6.67 (score 5.5–7.0) — **Read in full.** Clean accept with 25+ tasks and real-world validation. Clearly stronger than CoRAL.
- `/qi5Xa2cOZg.md` — "Learning with Language-Guided State Abstractions" — avg 5.67 (score 5.5–7.0)

### Calibration Logic
- Round 1 bracket: 5.0–6.5. CoRAL is clearly above the rejected weak anchors (3.0–4.25) which have ad-hoc approaches, limited evaluation, and insufficient baselines. CoRAL's ablation study is more comprehensive and its architectural contribution more novel. However, CoRAL is clearly below GenSim (8.00) which has a more novel contribution, real-world validation, and universal acceptance.
- Round 2 narrowed to 5.0–6.0. CoRAL is comparable to HAMSTER (6.00, borderline accept) but the Figure 4 evidential integrity issue and information asymmetry in VLA comparison put it slightly below. It is below Plan-Seq-Learn (6.67) which has broader evaluation and cleaner evidence. The 5.5 score reflects a paper with genuine architectural novelty and a strong ablation study, held back by an unresolved evidential contradiction and an unfair comparison framing.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
Now I have sufficient calibration. Let me write the final consolidated review.

---

## Summary

CoRAL is a modular neuro-symbolic framework for zero-shot contact-rich robotic manipulation that separates perception (FoundationPose + VLM for physical parameter estimation) from reasoning (LLM for cost function design, contact strategy, and online adaptation), grounding high-level plans in an MPPI reactive controller. The system includes a memory unit (RAG-based) for reusing successful experiences, and two nested feedback loops — a fast inner loop for reactive execution and a slower outer loop for diagnosing failures and refining the world model. Experiments on six simulated MuJoCo tasks compare CoRAL against two end-to-end VLA baselines (OpenVLA-OFT, π₀.₅) and human-expert-designed cost baselines, alongside ablations isolating each component.

## Strengths

- **Clean separation of VLM/LLM roles validated by convincing ablation.** The "Unified VLM" variant (a single VLM handling both perception and planning) catastrophically fails — 0/10 on four of six tasks, at most 2/10 on the remaining two (Table 1). This directly supports the paper's core architectural claim that dedicated vision and language models are necessary for robust contact-rich manipulation.

- **LLM-generated contact strategy dramatically accelerates planning.** In the "Flip with Wall" robustness analysis, the guided strategy completes the task in 32 steps vs. 199 steps without (83.9% fewer), with 63.9% shorter end-effector path (1.33 m vs. 3.69 m). This quantifies a concrete benefit of using the LLM to prune the action space — a capability the paper demonstrates with specific trajectory-level evidence.

- **Memory unit yields measurable gains.** The full CoRAL (with Memory) outperforms the no-Memory variant: T1 success climbs from 2/10 to 4/10, T3 from 9/10 to 10/10, and completion times drop across tasks (e.g., T4: 109s → 52s). These results show the RAG-based experience retrieval is not an auxiliary feature but an active performance contributor.

- **Zero-shot performance on contact-rich tasks surpasses fine-tuned end-to-end VLAs.** On tasks requiring force control and multi-contact reasoning (T4: Push with Constant Force, 9/10; T5: Flip Box, 9/10; T6: Flip with Wall, 7/10), CoRAL substantially outperforms OpenVLA-OFT and π₀.₅, both fine-tuned on LIBERO, which achieve at most 3/10 on any of these tasks.

## Weaknesses

### Fatal

None.

### Major

1. **Overstated claim about physical parameter estimation accuracy (evidential gap).** Section 4.1.4 states that after online adaptation, "the agent's belief about both mass and friction converged remarkably close to their true values." However, Figure 4 shows the corrected mass converging to ~0.85 kg while the ground truth (stated in the same paragraph) is 0.1 kg — a ~750% error. There is also an internal inconsistency: the text says the initial mass was 2.0 kg, while Figure 4 shows an initial mass of 1.0 kg. The friction coefficient is mentioned in the text but not shown in any figure. This overstatement undermines trust in the paper's characterization of its own results. The practical claim that adaptation *helps task success* (T1: 0/10 w/o Refinement → 4/10 full CoRAL) may still hold, but the paper's specific numerical account of the adaptation is inaccurate. This must be corrected.

2. **Missing comparison against the most relevant modular baselines.** The paper cites IMPACT (Ling et al., 2025) and VLMPC (Zhao et al., 2024) as prior work that also integrates VLMs with motion planners, but does not compare against them experimentally. Since these frameworks represent the closest prior paradigm to CoRAL (VLM + planner/controller vs. end-to-end VLA), their omission weakens the claim that CoRAL's specific design (LLM-generated cost functions and contact strategies) provides a decisive advantage over simpler integration schemes. Including at least one such baseline would substantially strengthen the evaluation.

3. **No confidence intervals or statistical tests on 10-trial results.** The primary results in Table 1 report binary success counts over 10 trials per condition without any error quantification. With only 10 trials, the difference between, e.g., 4/10 and 2/10 on T1 is not statistically meaningful on its own. While 10 trials is not unusual in robotics evaluation, the paper would benefit from reporting bootstrap confidence intervals or running additional seeds.

### Minor

- **Simulation-only evaluation with no discussion of sim-to-real transfer.** The paper is titled "Robotic Manipulation" and mentions "contact-rich manipulation" but conducts all experiments in MuJoCo. While simulation-only studies are common at ICLR and the paper does not explicitly claim real-robot deployment, the reactive control augmentation (Eq. 7) is described as addressing the "sim-to-real gap" without being tested for this purpose. A brief discussion of what would be required to transfer CoRAL to hardware, or an acknowledgment that this remains future work, would set appropriate expectations.

- **The "zero-shot" claim could be clarified with respect to the memory unit.** The paper defines zero-shot as not requiring task-specific demonstration data for pre-training, which is standard. However, the memory unit stores successful episodes from earlier trials of the *same* task during evaluation. If memory persists across trials (10 runs per task), later trials benefit from prior successes on that specific task. Whether memory is reset between the 10 trials is not stated. This does not invalidate the zero-shot framing but deserves clarification.

### Trivial

- In Section 4.1.4, the text states an initial mass of 2.0 kg while Figure 4 shows 1.0 kg. This numerical discrepancy should be resolved.
- Figure 4 shows only mass correction; the friction coefficient correction mentioned in the text is not plotted, making the claim about friction adaptation unverifiable from the presented evidence.
- The table header "Pick+Place Cluster" should be "Pick+Place Clutter" (consistent with the task description).

## Nice-to-Haves

- An accuracy table of VLM-estimated mass and friction vs. ground truth (across multiple random seeds) would substantiate the physical parameter estimation claim without relying on a single adaptation curve.
- A comparison against IMPACT or VLMPC on a subset of tasks would strengthen the evaluation against the most relevant prior paradigm.
- Sensitivity analysis of the outer-loop trigger threshold `N_retry` would help understand the adaptation dynamics.

## Removed Points

- "No real-world validation is a structural flaw" — Simulation-only studies are standard at ICLR for manipulation work, and the paper does not claim real-robot experiments. Demoted from Fatal to Minor limitation.
- "Zero-shot claim conflicts with memory unit" — The paper's use of "zero-shot" refers to not requiring task-specific pre-training data, which is standard. Memory helps within-task improvement across trials, not pre-training. Removed as a misunderstanding.
- "Human-expert FSM outperforms CoRAL, undercutting the argument" — The paper explicitly frames the FSM as an "upper bound from carefully engineered, task-specific objectives" and discusses the gap honestly. Not a weakness.
- "Missing appendix/proofs" — Parser-stripped sections that exist in the original submission. Removed per instructions.
- Various generic/speculative criticisms (e.g., "could the metric be measuring a proxy") — Removed as lacking concrete anchor in the paper.

## Novel Insights

None beyond the paper's own contributions. The two reviewers' perspectives largely converge on the paper's strengths (clean architecture, convincing ablation of VLM/LLM separation, memory benefits) and weaknesses (overclaimed mass estimation accuracy, missing modular baselines), with the Harsh Critic overstating several issues and the Strength Finder providing well-grounded positive evidence.

## Suggestions

1. **Correct the mass estimation narrative in Section 4.1.4.** Either present evidence that the corrected parameters actually converge close to ground truth, or reframe the claim as "adaptation improves task success even when parameter estimates remain imperfect." Resolve the inconsistency (2.0 kg vs. 1.0 kg) between text and Figure 4.
2. **Add at least one modular baseline comparison** (IMPACT or VLMPC) to the experimental setup to position CoRAL against its closest prior paradigm.
3. **Report confidence intervals or run additional seeds** for the 10-trial success rates to quantify statistical uncertainty.

## Score and Decision

**Calibration anchors** (all from deepreview_13k_calibration):

| Anchor | Avg Score | Comparison to CoRAL |
|--------|-----------|---------------------|
| Thin-Shell Manipulations (KsUh8MMFKQ) | 8.00 | Stronger — includes real-world deployment and rigorous evaluation. CoRAL is clearly below. |
| SuSIE (c0chJTSbci) | 6.25 | Similar topic (zero-shot manipulation), but SuSIE includes real-world experiments. CoRAL has more informative ablations. Comparable but slightly weaker overall. |
| HAMSTER (h7aQxzKbq6) | 6.00 | Comparable — both propose modular architectures, both have evaluation limitations. CoRAL handles more complex contact-rich tasks but lacks real-world validation. |
| LLM Policy Code (WtHKqtHVXo) | 4.00 | Similar intersection (LLM + contact-rich tasks). CoRAL is substantially stronger — more principled architecture, better ablation design, more comprehensive evaluation. |
| UniContact (Cf8HBieRzL) | 3.50 | Weaker evaluation, narrower scope. CoRAL is clearly stronger. |
| EF-VLA (KBSHR4h8XV) | 3.33 | Different methodology (VLA architecture). CoRAL's evaluation is more informative. CoRAL is stronger. |

Positioning: CoRAL sits between the 4.00 and 6.25 anchors. It has a well-motivated architecture and informative ablations that convincingly demonstrate the benefits of its design choices. However, it is weakened by an overclaimed parameter estimation result (contradicted by its own figure), missing comparison with the most relevant modular baselines (IMPACT, VLMPC), and limited statistical rigor. These are addressable weaknesses, but in their current form they meaningfully reduce confidence in the headline claims.

**Score: 5.0**

**Decision: Reject** — Borderline. The core architecture is sound and the ablations are informative, but the overstatement of the parameter estimation results and the omission of the most relevant baselines prevent acceptance at the current revision level. The paper would benefit from correcting the factual inaccuracies, adding a modular baseline comparison, and strengthening the statistical presentation before resubmission.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
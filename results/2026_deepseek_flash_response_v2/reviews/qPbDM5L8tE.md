Now I have all the calibration data I need. Let me synthesize the final review.

## Calibration Summary

**Round 1 bracket:** 4–6

**Round 2 anchors (read in full):**
- Generating Robot Policy Code (avg 4.0, Reject) — CoRAL is clearly stronger (more tasks, baselines, ablations)
- LLM+A (avg 4.0, Reject) — similar prompt-engineering approach; CoRAL has more rigorous evaluation
- Make a Donut (avg 5.25, Reject) — comparable; both zero-shot neuro-symbolic; Make a Donut has real-robot but fewer ablations. CoRAL is slightly stronger on ablation rigor but lacks real-robot validation.
- LLaRP (avg 5.75, Accept) — more thorough evaluation scale (1000 tasks vs 6); CoRAL has a more novel architecture (LLM→cost functions for MPPI) but weaker evidence
- SuSIE (avg 6.25, Accept) — stronger evaluation, real-robot validation; CoRAL is clearly weaker

**Final position:** CoRAL sits between the 4.0 papers (weaker) and the 5.75–6.25 papers (stronger), closest to Make a Donut at 5.25. The Figure 4 inconsistency prevents a score above 5.5. **Score: 5.0**

---

## Summary

This paper proposes CoRAL, a neuro-symbolic framework for contact-rich robotic manipulation that integrates LLMs/VLMs with a Model Predictive Path Integral (MPPI) controller. The LLM generates cost functions and contact strategies; an outer loop enables online adaptation of world parameters through failure diagnosis; and a memory unit enables experience reuse. The paper evaluates CoRAL on six simulated manipulation tasks against OpenVLA, π_0.5, human-designed cost baselines, and several ablations.

## Strengths

1. **Zero-shot outperformance of fine-tuned VLA models on contact-rich tasks.** Table 1 shows CoRAL achieves 9/10 on T4 (Push with Constant Force) and 7/10 on T6 (Flip with Wall) where OpenVLA-OFT and π_0.5 — both fine-tuned on LIBERO — score 0/10. This provides concrete evidence that the decoupled reasoning-then-control paradigm can handle contact dynamics that end-to-end imitation learning cannot.

2. **LLM-driven contact strategy quantitatively reduces planning complexity.** Section 4.1.4 reports that the LLM-guided contact strategy reduces steps by 83.9% (32 vs 199 steps) and path length by 63.9% (1.33 m vs 3.69 m) on T6. These are clean, specific efficiency gains that directly demonstrate the value of the symbolic contact strategy.

3. **Online adaptation corrects misestimated physical parameters.** Section 4.1.4 demonstrates that the system iteratively refines initial mass and friction estimates when the inner loop fails, converging toward ground truth. This provides direct evidence that the closed-loop feedback mechanism (Section 3.4) goes beyond re-prompting.

4. **Separation of VLM/LLM roles is experimentally validated as critical.** The Unified VLM ablation (Table 1) scores 0/10 on 4 of 6 tasks and only 2/10 on the simplest pick-and-place, while the separated architecture succeeds on all tasks. This directly supports the paper's core design claim.

5. **Memory unit provides measurable, repeatable improvement.** CoRAL with Memory outperforms without Memory on 4 of 6 tasks in success rate (e.g., T1: 4/10 vs 2/10; T5: 9/10 vs 7/10) and achieves faster completion times across all tasks.

## Weaknesses

### Major

- **Figure 4 contains a clear internal inconsistency that undermines the central adaptation demonstration.** The text in Section 4.1.4 states: "we intentionally initialized the Evaluation World with a severely overestimated mass (2.0 kg vs. a ground truth of 0.1 kg)." However, Figure 4 shows a y-axis ranging from 0.75 to 1.00 kg, an "Initial Mass" (dashed line) constant at **1.00 kg**, and a "Corrected Mass" converging to approximately **0.85 kg**. None of these numbers match the described scenario (initial 2.0 kg, ground truth 0.1 kg, correction toward 0.1 kg). This discrepancy must be resolved before the adaptation mechanism can be trusted as demonstrated. The figure appears to depict a different experiment or has labeling errors.

### Minor

- **Small sample size with no statistical rigor.** Each condition is evaluated on only 10 binary-outcome trials. With 10 trials, a single outcome shift changes the success rate by 10 percentage points, yet the paper reports differences like 2/10 vs 4/10 and 9/10 vs 10/10 without confidence intervals, standard errors, or statistical testing. These differences could arise from noise.

- **Gap to Expert (FSM) baseline is substantial on the hardest tasks.** On T1 (Push+Pick Board), CoRAL achieves 4/10 vs the Expert FSM's 8/10. On T6 (Flip with Wall), 7/10 vs 9/10. While the paper frames this as "narrowing the gap," the gap remains large on tasks requiring multi-stage reasoning. This tempers the claim that the LLM's cost formulation is competitive with careful manual engineering.

- **"Zero-shot" claim is somewhat overstated.** The system requires known 3D geometric object models (M), FoundationPose for pose tracking, GPT-4o accessed via API, a fully specified MuJoCo physics simulator for MPPI rollouts, and manually tuned MPPI hyperparameters (K=200, H=50, λ=0.1, N_retry=15). The paper defines "zero-shot" as no task-specific demonstration data — a valid but limited use of the term. A clearer qualifier (e.g., "zero-shot with respect to task demonstrations") would avoid overclaim.

- **No analysis of VLM physical parameter estimation quality.** The paper does not quantify how accurate the VLM's mass and friction estimates are, how errors propagate through the pipeline, or how sensitive results are to estimation quality. Given that the VLM-generated parameters are a bottleneck in the perception pipeline (Section 3.1), this gap weakens the claim that the component is essential.

- **No prompt examples for the LLM.** The paper describes LLM-driven cost function generation, contact strategy formulation, and failure diagnosis but provides no example prompts. This is a substantial reproducibility gap.

- **Simulation-only evaluation.** Contact-rich manipulation is notoriously sensitive to sim-to-real gaps, yet the paper never validates on a real robot. The reactive controller (Eq. 7) is explicitly designed to address such gaps, which makes the absence of hardware validation particularly notable.

### Trivial

- None beyond the formatting artifacts common to PDF extraction.

## Nice-to-Haves

- Real-robot validation for at least one task would transform the strength of the contribution.
- Wall-clock time and computational cost analysis (API call latency, MPPI planning time per step) would help assess practical viability.
- Details on how the memory unit computes task similarity (beyond the RAG description) would aid reproducibility.
- Analysis of the LLM's failure diagnosis accuracy (how often does the outer loop correctly identify the source of failure?).

## Removed Points

These points were raised by reviewers but are removed from the main assessment:

- **"The comparison to VLA baselines is less informative because they weren't trained on these tasks."** Removed — the paper's framing is transparent about this limitation, and the comparison still demonstrates that even fine-tuned VLAs fail on contact-rich tasks. The asymmetry favors the baseline, not the proposed method.

- **"Missing related works discussion."** Removed per meta-reviewer instructions, as confirming the existence of related works requires external sources.

- **"Missing appendix content / broken appendix references."** Removed per meta-reviewer instructions — appendix sections are stripped by the parser.

- **"No discussion of prior work on learning cost functions for MPC from language."** Removed — this is speculative scope creep; the paper explicitly positions against VLMPC and IMPACT as the closest related work.

- **"The cost function in Eq. 2 only shows a single template."** While true, the paper explicitly states this is illustrative and the LLM is "free to introduce any cost terms." This is adequately scoped.

- **Various formatting, style, and typo nitpicks.** Removed per meta-reviewer instructions (parser artifacts, not author errors).

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any observation about the paper that the authors themselves do not articulate.

## Suggestions

1. **Fix the Figure 4 inconsistency.** Clarify whether the figure depicts a different experiment (e.g., a different object or initial condition) or correct the text/figure so they match. This must be resolved before any further evaluation.
2. **Increase trial counts** to at least 50 per condition and report bootstrapped confidence intervals or standard errors.
3. **Include prompt examples** for cost function generation, contact strategy formulation, and failure diagnosis in an appendix.
4. **Quantify VLM parameter estimation accuracy** — report mean absolute error for mass and friction estimates across objects and analyze downstream impact on task success.
5. **Add at least one real-robot task** to demonstrate that the reactive controller bridges the sim-to-real gap as claimed.
6. **Report wall-clock time** for the full pipeline (perception + LLM calls + MPPI planning) to establish practical feasibility.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
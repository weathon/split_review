Now I have all the evidence I need. Let me synthesize the final review.

---

## Summary

CoRAL proposes a modular neuro-symbolic framework for zero-shot contact-rich robotic manipulation. The system uses a VLM (GPT-4o) to estimate physical parameters from vision, an LLM to generate cost functions and contact strategies for an MPPI controller, and a memory unit for experience reuse. The key architectural claim is that explicitly separating perception (VLM) from reasoning (LLM) is beneficial. Ablations show each component contributes meaningfully: the full system achieves 4/10–10/10 across six contact-rich tasks, while state-of-the-art VLA baselines (OpenVLA-OFT, π₀.₅) largely fail on the hardest tasks.

## Strengths

- **LLM-generated cost functions and contact strategies for MPPI are genuinely novel and well-motivated.** The idea of having an LLM produce the mathematical structure of a cost function (not just a verbal plan) and propose symbolic contact regions is a clean departure from both end-to-end VLAs and prior LLM-as-planner work. The contact-strategy ablation (Sec. 4.1.4) quantifies the benefit: 83.9% fewer steps and 63.9% shorter path on the "Flip with Wall" task (32 vs. 199 steps, 1.33 m vs. 3.69 m).

- **Comprehensive ablation study demonstrates that every architectural component contributes.** The "w/o Refinement" variant drops from 4/10→0/10 on T1, the "w/o Memory" variant underperforms on most tasks, the "Unified VLM" variant collapses (0/10 on 4 of 6 tasks), and the "w/o Pose Tracking" variant fails catastrophically. These ablations give readers clear evidence for the design choices.

- **The human-expert cost-function comparison grounds the contribution honestly.** Rather than only comparing against VLAs that are mismatched for contact-rich tasks, the paper benchmarks against hand-designed MPPI costs (single-stage and FSM). This shows that CoRAL closes much of the gap to expert-tuned controllers without human effort — on T5 it reaches 9/10 vs. the FSM expert's 10/10, and on T6 it reaches 7/10 vs. 9/10.

- **Memory-driven experience reuse is convincingly shown to improve both success rate and efficiency.** The "with Memory" variant consistently beats "w/o Memory" (e.g., T1: 4/10→2/10, T6: 7/10→5/10) and reduces completion times, providing direct evidence that retrieval of past successful episodes bootstraps better plans.

## Weaknesses

### Major

- **The mass-correction experiment (Figure 4) contains a concrete numerical inconsistency that undercuts the robustness analysis.** The text states: "we intentionally initialized the *Evaluation World* with a severely overestimated mass (2.0 kg vs. a ground truth of 0.1 kg) and friction coefficient (0.9 vs. 0.5) for the cutting board" (lines 332–333). However, Figure 4 shows "Initial Mass" constant at **1.00 kg** and the "Corrected Mass" dropping to only **~0.85 kg** (not converging to 0.1 kg), with a y-axis ranging from 0.75 to 1.00 kg. The figure does not depict the experiment described in the text. This is not a formatting artifact — the figure caption clearly describes what is shown. One of the paper's most important qualitative claims (online world-model correction) rests on evidence that is self-contradictory. The authors must clarify whether the figure is mislabeled, the text numbers are wrong, or the experiment was performed differently.

- **The central comparative claim against VLA baselines is overframed.** The paper pits CoRAL against OpenVLA-OFT and π₀.₅ using their **LIBERO fine-tuned checkpoints**, which are trained on pick-and-place data. That these models fail on pushing, flipping, and sustained force-control tasks (T1, T4–T6) is expected — end-to-end imitation-learned policies do not generalize to out-of-distribution contact dynamics. The paper's framing ("significantly outperforms state-of-the-art VLA models") reads as stacking the deck. The *meaningful* comparison is against the human-designed cost baselines, where CoRAL's results are more modest (best variant still substantially below the FSM expert on T1: 4/10 vs. 8/10). The paper would be stronger if it foregrounded the trade-off between automation and performance rather than claiming superiority over mismatched baselines.

- **No statistical rigor.** All 6 tasks are evaluated with only 10 trials and binary success/failure. No confidence intervals, standard deviations, or statistical tests are reported anywhere. For tasks where multiple variants achieve 10/10 or 9/10 (e.g., T2, T3), it is impossible to assess whether observed differences are meaningful. Given the small trial count, even the 4/10 vs. 2/10 differences on T1 could fall within noise.

### Minor

- **The evaluation is entirely in simulation.** While the paper acknowledges sim-to-real considerations and includes a reactive control term (Eq. 7) motivated by the sim-to-real gap, no real-robot experiments are conducted. The robustness experiment relies on deliberately introducing errors in the simulator, which is not equivalent to real-world sensing noise, calibration errors, or unmodeled dynamics. A discussion of what would be needed for real deployment would strengthen the paper.

- **The "Unified VLM" ablation does not cleanly validate the claimed architectural insight.** The paper argues that separating VLM (perception) from LLM (reasoning) is critical, and supports this by showing that "CoRAL (Unified VLM)" — a single GPT-4o prompt handling both roles — fails on nearly all tasks. But GPT-4o is simultaneously a VLM *and* an LLM; the failure could stem from prompt complexity or task difficulty rather than the architectural conflation per se. A cleaner test would keep the same backbone model but split the pipeline into two structured asynchronous calls — the actual difference the paper proposes.

- **Computational cost is not reported.** The system makes multiple LLM/VLM API calls per episode (initial formulation, outer-loop refinements, memory retrieval). No wall-clock times per episode, token counts, or API costs are provided, making it difficult to assess practical feasibility.

- **The memory retrieval mechanism is underspecified.** The paper states that the LLM embeds the current task "into a latent semantic space" and retrieves similar past experiences, but no embedding model, similarity metric, or retrieval threshold is specified (Eq. 1), making this component non-reproducible as described.

### Trivial

- Figure 3 appears in the text before it is referenced, which is a minor ordering issue.
- The y-axis label in the description of Figure 4 is "Estimated Mass (kg)" rather than something like "Mass Estimate (kg)" — very minor.

## Nice-to-Haves

- A real-robot validation on even one contact-rich task would significantly strengthen the claims about practical applicability.
- Reporting confidence intervals (e.g., via bootstrapping) for the success rates would allow readers to assess whether the ablation differences are reliable.
- A comparison against force-aware VLA policies (e.g., ForceVLA, TLA, RDP) mentioned in the related work would provide a more informative baseline for contact-rich tasks.
- Reporting token costs and wall-clock time per episode would clarify the practical compute requirements.

## Removed Points

- **"Zero-shot framing is misleading because memory is used"** — The paper evaluates both "with Memory" and "w/o Memory" variants; the w/o Memory variant is genuinely zero-shot. The term "zero-shot" in the paper refers to the absence of task-specific training data, which is accurate. REMOVED.
- **"w/o Pose Tracking ablation is a straw-man"** — Testing whether a VLM can replace a dedicated pose estimator is a standard ablation. The result that it fails is informative; it confirms that geometric perception requires a specialized module. REMOVED.
- **"Explainability demonstration is insufficient (single anecdote)"** — The paper does provide a concrete example with specific diagnosis and weight adjustments. The appendix (stripped by the parser) may contain more. As a single quantitative demonstration, it is acceptable for a conference paper. REMOVED.
- **"Missing related work"** — Cannot verify without external sources. REMOVED per protocol.
- **"VLM hallucination" phrasing** — This is a descriptive term, not a weakness. REMOVED.
- **"Computational latency" mentioned as limitation but not quantified** — The paper acknowledges this in the Conclusion. It is a valid point but already in Minor weaknesses above. REMOVED as redundant.
- Several strengths from the Strength Finder were generic or contradictory with verified weaknesses and have been removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the Figure 4 / text inconsistency immediately.** Clarify what experiment was actually run and what the figure depicts. If the correction was from 2.0 kg toward 0.1 kg, show that on the figure. If the figure is from a different run, relabel it.
2. **Reframe the comparative narrative.** Lead with the human-designed cost baselines and frame CoRAL's contribution as *automating the design of cost functions for contact-rich tasks*, achieving results close to expert-tuned controllers. Treat the VLA comparison as supporting evidence that end-to-end methods fail on out-of-distribution contact tasks, not as the headline result.
3. **Report confidence intervals** for at least a subset of tasks, even if via bootstrapping from the 10 trials per condition.
4. **Add wall-clock time or token cost** per successful episode to help readers assess practicality.
5. **Specify the memory retrieval mechanism** (embedding model, similarity metric, threshold) for reproducibility.

## Score and Decision

**Round 1 bracket**: Between the weak anchors (avg 3.0–3.4, strongly rejected papers with limited evaluation) and the strong anchors (avg 8.0, top-tier accept papers). I placed CoRAL in the middle band.

**Round 2 narrowing**: I read the following anchor papers in full:
- **WtHKqtHVXo** (avg 4.0, Reject): "Generating Robot Policy Code for High-Precision and Contact-Rich Manipulation Tasks" — similar topic (LLM + contact-rich), rejected due to weak comparisons and limited experiments. CoRAL is more thorough (more tasks, ablations, memory unit) but has the figure inconsistency that the anchor paper does not.
- **c0chJTSbci** (avg 6.25, Accept): "Zero-Shot Robotic Manipulation with Pre-Trained Image-Editing Diffusion Models" — has real-world experiments + simulation. CoRAL is entirely simulation-only, which is a clear gap.
- **iTsHStJKcm** (avg 5.25, Reject): "Make a Donut" — LLM for zero-shot deformable object manipulation, simulation-only. Similar tier to CoRAL in thoroughness but rejected.
- **Aqfwhna1D7** (avg 5.20, Reject): "CrayonRobo" — real-world experiments but still rejected due to practicality concerns.
- **qGL6fE1lqd** (avg 4.40, Reject): "LLMPhy" — LLM+physics simulator, limited experiments. CoRAL has more tasks and ablations but shares the simulation-only limitation.
- **h7aQxzKbq6** (avg 6.00, Accept): "HAMSTER" — hierarchical models, has real-world validation.

CoRAL is clearly stronger than the 4.0 anchor (WtHKqtHVXo) and comparable to the 5.25 and 4.40 anchors in terms of experimental breadth. However, the concrete figure inconsistency distinguishes it negatively from these papers. It is weaker than the 6.0–6.25 anchors primarily due to the absence of real-robot validation and the figure error.

**Final score**: The core idea is innovative and the ablations are thorough, but the central robustness experiment contains a concrete numerical contradiction, and the main comparative framing oversells the VLA comparison. The paper needs correction and reframing before it meets the acceptance bar. Score: **4.5**.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
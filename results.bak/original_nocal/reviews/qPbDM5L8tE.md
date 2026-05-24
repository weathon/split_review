Now I have all the evidence I need. Let me synthesize the final review.

## Summary

CoRAL proposes a modular framework that integrates a dedicated pose estimator (FoundationPose), a VLM (GPT-4o) for physical parameter estimation, an LLM for generating cost functions and contact strategies, an MPPI reactive controller, and a memory unit for experience reuse. The key idea is to decouple perception, reasoning, and control into separate modules, with nested feedback loops (inner loop for reactive control, outer loop for LLM-driven online adaptation). Evaluated on six contact-rich manipulation tasks in simulation, the paper shows that CoRAL achieves nonzero success rates on tasks where end-to-end VLA baselines (OpenVLA-OFT, π0.5) fail entirely, and the ablation studies demonstrate the necessity of each architectural component.

## Strengths

1. **Zero-shot success on contact-rich tasks where state-of-the-art VLAs fail**. Table 1 shows CoRAL achieves nonzero success on T1 (4/10), T4 (9/10), T5 (9/10), and T6 (7/10), while OpenVLA-OFT and π0.5 score 0/10 on these same tasks (both models achieve only 0-1/10 on T5). This provides direct evidence that the modular neuro-symbolic approach can handle contact-rich manipulation without task-specific demonstrations.

2. **Separation of VLM and LLM roles is experimentally necessary**. The "Unified VLM" ablation, which gives a single model both perception and planning responsibilities, scores 0/10 on 5 out of 6 tasks (2/10 on T2). This sharp failure relative to the full CoRAL demonstrates that the decoupled design is not merely philosophical — it is critical for performance.

3. **Online refinement loop enables recovery from initial errors**. The "w/o Refinement" ablation drops from 4/10 to 0/10 on the multi-stage T1 and from 7/10 to 4/10 on T5. This validates that the outer loop's ability to diagnose failures and adjust cost functions/parameters is crucial for the harder tasks.

4. **Memory unit provides measurable improvement**. The "w/o Memory" variant scores 2/10 on T1 vs. 4/10 with memory, and 5/10 on T6 vs. 7/10. Completion times are also consistently lower with memory (e.g., T4: 109 s vs. 52 s; T6: 164 s vs. 106 s). This confirms the practical benefit of RAG-based experience retrieval.

5. **LLM-generated contact strategy dramatically reduces planning complexity**. On T6 (Flip with Wall), the LLM-guided contact strategy shortens the end-effector path by 63.9% (1.33 m vs. 3.69 m) and reduces planning steps by 83.9% (32 vs. 199). This shows concretely that the symbolic contact strategy prunes an otherwise intractable search space.

6. **Explainability demonstrated during failure recovery**. The paper documents that when the outer loop is triggered, the LLM produces a natural-language diagnosis of the failure (e.g., identifying a poorly weighted cost function) and logs corrective actions — an advantage over black-box end-to-end policies.

## Weaknesses

### Fatal
None.

### Major

1. **Mass correction evidence contradicts the textual claim (Figure 4 vs. Section 4.1.4)**. The text (Section 4.1.4) states: "we intentionally initialized the *Evaluation World* with a severely overestimated mass (2.0 kg vs. a ground truth of 0.1 kg)." However, the Figure 4 caption describes a y-axis ranging 0.75–1.00 kg, an "Initial Mass" (dashed line) constant at 1.0 kg, and the "Corrected Mass" converging to approximately 0.85 kg. Neither the initial estimate (1.0 kg vs. the claimed 2.0 kg) nor the converged value (0.85 kg vs. the ground truth 0.1 kg) matches the experimental setup described in the text. The figure also claims to show friction correction but the caption only mentions mass. This is a verifiable discrepancy between the presented evidence and the claimed result. The paper's argument that "the agent's belief about both mass and friction converged remarkably close to their true values" is not supported by the figure as described. This weakens the paper's central claim about robust online parameter adaptation. The authors must clarify: is the figure mislabeled, is the text wrong, or is the experiment different from what is described?

### Minor

2. **Small trial count (N=10) limits statistical reliability of fine-grained comparisons**. All results are based on 10 trials per condition with no confidence intervals or statistical tests. For binary success metrics, 10 trials yields wide 95% confidence intervals (e.g., 4/10 ≈ [12%, 74%]). Several key comparisons rely on differences of 1–2 successes: memory boosting from 2/10 to 4/10 on T1, refinement dropping from 4/10 to 0/10 on T5, etc. While 10 trials is common in robotics manipulation papers due to experimental cost, the paper should at minimum acknowledge this limitation and avoid over-interpreting small numerical differences.

3. **Human-expert baseline (FSM) outperforms CoRAL on most diagnostic tasks, and this gap is underexplored**. Expert FSM achieves higher success rates on T1 (8/10 vs. 4/10), T4 (10/10 vs. 9/10), T5 (10/10 vs. 9/10), and T6 (9/10 vs. 7/10). On T1, the gap is 4× in favor of the expert. The paper characterizes this as "narrowing the gap," which is fair, but does not analyze the failure modes responsible. Understanding why CoRAL fails on 6/10 T1 trials (e.g., grasp failure, parameter mismatch, insufficient LLM cost structure) would inform whether the gap is fundamental or addressable with better prompting or refinement.

4. **No failure analysis for unsuccessful trials**. The paper reports success/failure counts but does not categorize failure modes. For example, on T1 where CoRAL achieves only 4/10, it is unclear whether failures stem from poor initial cost weights, inadequate pose tracking during contact, insufficient outer-loop adaptation, or something else. This limits the scientific value of the ablation studies — without understanding *why* the w/o Refinement variant fails, it is difficult to confirm that the outer loop is actually fixing the right problem.

### Trivial

None.

## Nice-to-Haves

- **Real-world validation**: The entire evaluation is in simulation. Contact-rich manipulation is especially sensitive to sim-to-real gaps in friction, contact stiffness, and sensor noise. A real-robot experiment (even on one task) would substantially strengthen the robustness claims.
- **Prompt sensitivity analysis**: The paper uses GPT-4o with unspecified prompt templates. LLM outputs can be sensitive to prompt phrasing; testing 2–3 alternative phrasings would strengthen the methodology.
- **Computational latency breakdown**: Wall-clock times are reported but not broken down by component (VLM inference, LLM calls, MPPI rollouts). This would help assess practical deployability.

## Removed Points

These points were flagged by reviewers but removed with justification:

- **"Unfair baseline comparison — VLA models fine-tuned on different tasks"**: The paper explicitly states (Section 4) that this setup "tests CoRAL's zero-shot capabilities against powerful policies." Both CoRAL and the VLA baselines are evaluated zero-shot on these tasks. The VLA models were fine-tuned on LIBERO (a manipulation benchmark); the finding that their fine-tuning does not transfer to contact-rich scenarios is the paper's legitimate observation, not an unfair comparison.
- **"W/o Pose Tracking completion time shown as '-' is unclear"**: The dash for completion time on T2 (where success is 9/10) is a minor formatting choice, not an error. Time may not be meaningful without the tracking system.
- **"Unified VLM ablation is poorly specified / prompt artifact"**: The ablation is clearly described as using a single multimodal prompt for both perception and planning. Whether the failure is due to role merging or prompt quality is exactly what the ablation tests — the specific failure mode doesn't invalidate the conclusion.
- **Generic criticisms lacking concrete paper evidence** (e.g., "the evaluation lacks rigor," "could the metric be measuring a proxy?"): These were area-of-concern sweeps without specific anchor points in the paper and are removed per filtering discipline.

## Novel Insights

The most striking finding that emerges from the review is the tension between CoRAL's modular design and the mass correction experiment. The modular architecture is well-supported by the ablation studies: every removed component causes measurable degradation. This makes the Figure 4 discrepancy especially puzzling — if the framework genuinely can correct physical parameters online (as the w/o Refinement ablation indirectly supports), then the mass-correction experiment should be the cleanest demonstration of that capability. That the evidence here is contradictory suggests either a presentation error (mislabeled axes, wrong figure) that can be fixed or a deeper issue with the adaptation mechanism that the authors have not disclosed. Beyond this, the reviewers' strengths and weaknesses converge on the same assessment: the core architectural idea is sound and partially validated, but the experimental rigor in one critical area needs repair.

## Suggestions

1. **Correct and clarify the mass-correction experiment (Figure 4)**. Provide a properly scaled figure showing the stated initial estimate (2.0 kg), ground truth (0.1 kg), and the LLM's evolving estimate over time. If the experiment was different from what the text describes, align text and figure unambiguously.
2. **Add failure-mode analysis** for at least the hardest task (T1). Classify the 6 failed trials into categories (e.g., cost function error, pose tracking failure, refinement not triggered, refinement insufficient).
3. **Run at least 20–30 trials** for the main comparison (CoRAL vs. VLA baselines on T1/T5/T6) and report confidence intervals or use statistical tests for key ablation comparisons.
4. **Add a prompt-sensitivity check** — even 2–3 alternative phrasings for the most critical LLM prompt (cost function generation) would strengthen the claim that the approach is robust, not prompt-engineered.
5. **In the rebuttal, clarify what "initialized the Evaluation World with ... 2.0 kg" means** — is this the simulation's true mass, or the planning world's initial estimate? The current phrasing is ambiguous.

## Score and Decision

The paper proposes a genuinely novel and well-motivated modular architecture that produces meaningful results on challenging contact-rich manipulation tasks. The core strengths (zero-shot success where VLAs fail, strong ablation evidence, explainability) are solid. However, the verified discrepancy between the mass-correction text and Figure 4 is a significant weakness that undermines a key robustness claim. This is fixable (likely a presentation/annotation error), but in its current form the evidence does not fully support all stated claims.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
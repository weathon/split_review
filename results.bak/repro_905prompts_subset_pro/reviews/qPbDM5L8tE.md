Now I have a thorough understanding of the paper and calibration landscape. Let me write the consolidated review.

---

## Summary

CoRAL proposes a neuro-symbolic framework for zero-shot contact-rich robotic manipulation that decouples perception (VLM + pose tracker) from planning (LLM-generated cost functions and contact strategies). The LLM formulates the cost function and contact strategy for an MPPI controller, which executes reactively. A nested outer loop enables LLM-driven online adaptation when the inner loop fails, and a memory unit stores successful experiences for retrieval. Evaluated on six simulated tasks, CoRAL significantly outperforms end-to-end VLAs (OpenVLA-OFT and π₀.₅) on contact-rich scenarios where VLAs fail, approaches human-expert-designed FSM performance, and provides informative ablation studies demonstrating each component's necessity.

## Strengths

- **Convincing ablation evidence for architectural choices**: The Unified VLM ablation collapses to 0/10 on most tasks, the w/o Refinement variant drops from 4/10 to 0/10 on the multi-stage T1 task, and the w/o Pose Tracking variant fails catastrophically across all tasks (0/10). These results directly and cleanly support the paper's central thesis that role separation, online adaptation, and dedicated pose tracking are essential for robust contact-rich manipulation.

- **Quantitative demonstration of LLM contact strategy value**: On the Flip with Wall task (T6), the LLM's symbolic contact strategy reduces planning steps by 83.9% (32 vs. 199 steps) and end-effector path length by 63.9% (1.33m vs. 3.69m). This is a concrete, well-measured result showing how high-level reasoning makes long-horizon contact problems tractable.

- **Honest comparison to human-engineered baselines**: The paper includes both single-stage and FSM human-designed cost baselines that use the same MPPI controller. The FSM baseline outperforms CoRAL on most tasks (e.g., 8/10 vs 4/10 on T1, 10/10 vs 9/10 on T5), and the paper acknowledges this. This credible comparison shows where LLM-generated costs currently stand relative to expert engineering, and provides a meaningful upper bound.

- **Strong zero-shot performance on tasks where VLAs fail**: On Flip Box (T5) and Flip with Wall (T6), OpenVLA-OFT and π₀.₅ achieve at most 1/10 and 3/10 respectively, while CoRAL attains 9/10 and 7/10. These are the tasks most clearly requiring physical reasoning about forces and multi-contact strategies — precisely the regime where the proposed approach shines.

- **Well-motivated architectural design**: The nested inner/outer loop structure (high-frequency MPPI replanning + low-frequency LLM-driven adaptation) is clearly explained and thoughtfully designed. The reactive control augmentation (Eq. 7) that combines planned actions with real-time sensor errors is a sensible mechanism for handling the sim-to-real gap.

## Weaknesses

### Fatal

None.

### Major

- **Limited statistical evidence for core performance claims**: All results use only 10 trials per task with no error bars, confidence intervals, or statistical tests. On the flagship multi-stage task (T1, Push and Pick Cutting Board), the full CoRAL achieves only 4/10 success — a binary outcome where moving from 4 to 5 or 3 successes changes the apparent performance substantially. The paper's strongest results (T5: 9/10, T6: 7/10) are more robust, but the adaptation and memory analyses rely entirely on single-trial anecdotes. For a paper making claims about robustness and adaptability, the absence of any distributional characterization of outcomes (per-trial results, number of refinement cycles, adaptation success rate) is a significant evidential gap. Ten trials with no variance reporting makes it impossible to assess whether observed differences (e.g., memory's 2/10 → 4/10 on T1) are signal or noise.

- **Memory unit contribution is weak and oversold**: The memory module improves success from 2/10 to 4/10 on T1 and 9/10 to 10/10 on T3. These are marginal gains — on T1, just one additional success separates the two conditions. The paper claims this demonstrates "few-shot performance improvements" and that "the system becomes more adept as it gathers successful episodes," but with only 10 trials, the evidence for a learning curve does not exist. No retrieval accuracy metrics, no analysis of how memory scales or degrades with stored experiences, and no characterization of the semantic embedding space are provided. The memory unit is presented as a contribution but the evidence does not yet substantiate it as one.

### Minor

- **Online adaptation analysis is anecdotal**: Section 4.1.4 demonstrates parameter adaptation with a single injected bias scenario (mass 2.0→0.1 kg, friction 0.9→0.5) shown in Figure 4, and a single trajectory comparison for contact strategy. The paper claims the system can "learn from its failures and adapt its entire approach," but provides no quantitative summary: how often does the outer loop trigger? How many adaptation cycles are needed on average? When does adaptation fail? These questions go unanswered.

- **"Zero-shot" framing could be more precise**: The paper uses "zero-shot" to mean without demonstration data or task-specific training. However, the system requires known 3D object meshes, a calibrated simulation environment matching the test world, a physics engine for planning rollouts, and VLM-estimated physical parameters. While this is zero-shot with respect to action/strategy learning, the framing could be more carefully scoped — particularly since the paper's VLA baselines are "zero-shot" in a different sense (no task-specific environment model). The paper already acknowledges simulator fidelity as a limitation; extending this honesty to the "zero-shot" label would strengthen rather than weaken the contribution.

- **Missing reproducibility details**: The exact prompts for the VLM parameter estimation, the LLM task formulation, and the online adaptation module are not provided in the main paper. The definition of "persistent failure" for the N_retry = 15 trigger is vague. The Unified VLM ablation is described as using a "single multimodal prompt" but neither the prompt nor how its output was parsed into actions is specified, making it difficult to assess whether this is a fair ablation or an underengineered straw man.

### Trivial

- The paper references an appendix (e.g., for explainability details, Figure 5, limitations discussion) that is not included in the main text. While this is a parser artifact and not an author error, it does mean some claims (particularly around explainability) are unsupported in the visible text.

## Nice-to-Haves

- **Real-world validation**: The framework is entirely simulation-based. A single real-world demonstration, even on a simpler task, would substantially strengthen the practical relevance claim.
- **Quantification of VLM physical parameter accuracy**: Knowing how far off the initial mass/friction estimates typically are would contextualize the adaptation module's importance and the overall robustness claim.
- **Per-task cost function analysis**: Showing the actual cost functions the LLM produces for 2-3 representative tasks, and comparing them to the human-designed FSM costs, would directly illuminate where LLM reasoning succeeds or falls short relative to expert engineering.
- **Distribution of adaptation outcomes**: Instead of one anecdote, a histogram or table of how many refinement cycles different tasks require, and what fraction of adaptations succeed, would make the adaptation contribution significantly more convincing.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **Harsh Critic: "Unfair comparison to end-to-end VLAs invalidates the main performance claim"** — REMOVED as a fatal/major criticism. The paper includes human-designed cost baselines (single-stage and FSM) that use the *same* MPPI controller and *same* privileged information (pose tracking, simulator) as CoRAL. The FSM baseline outperforms CoRAL in most cases, which directly isolates the LLM's contribution relative to expert design. The VLA comparison tests a different claim: that decoupled neuro-symbolic architectures can handle contact-rich tasks zero-shot where end-to-end learned policies fail. Both paradigms bring different kinds of prior knowledge (demonstration data vs. object models + simulator) — this is a comparison of paradigms, not an unfair setup. The paper is transparent about what each approach requires.

- **Harsh Critic: "The term zero-shot is used in a misleading way"** — DEMOTED to Minor. The paper uses "zero-shot" in the standard robotics sense (no task-specific demonstration data or training). Requiring object meshes and a simulator is an upfront engineering requirement, not task-specific learning.

- **Harsh Critic: "The ablation of Unified VLM is too extreme to be informative" / "straw-man comparison"** — REMOVED. The Unified VLM ablation directly tests the paper's core hypothesis about role separation. Collapsing to 0/10 on most tasks is informative regardless of prompt engineering. The critic's claim that "no details are given about what the prompt was" is a separate reproducibility concern, not evidence the ablation is invalid.

- **Strength Finder: "Explainability through natural-language failure diagnosis"** — REMOVED as a standalone strength. The paper provides only one anecdotal example, and the relevant appendix is not available in the visible text. The claim of explainability is not sufficiently supported by systematic evidence.

- **Strength Finder: "Rigorous evaluation with randomized physics"** — PARTIALLY RETAINED. The randomization is a genuine strength in task design, but 10 trials with no error bars prevents the evaluation from being described as "rigorous."

- **Harsh Critic: Discussion of controller frequency, LLM latency, real-world assumptions** — These are legitimate concerns but are scope creep for a simulation paper. Moved to Nice-to-Haves.

- **Harsh Critic: Missing appendix, missing proofs, formatting issues** — REMOVED per hard rules (parser artifacts).

- **Strength Finder: "Memory unit improves success and speed through experience reuse"** — WEAKENED and merged into Major weakness. The gains are marginal and not statistically assessed.

## Novel Insights

The paper's most genuinely novel contribution is the demonstration that an LLM can formulate *both* the cost function structure and contact strategy for an MPPI controller, and that this combination — when embedded in a nested adaptation loop — can solve contact-rich manipulation tasks that defeat state-of-the-art end-to-end VLAs. Unlike prior work where LLMs serve as perceptual guides or subgoal generators for learned policies, CoRAL grounds the LLM's reasoning directly in the mathematical formulation of the optimal control problem. The contact strategy ablation (83.9% planning step reduction) provides particularly crisp evidence that symbolic reasoning about *where* to make contact is the bridge between abstract LLM reasoning and computationally tractable physical planning. This insight — that the LLM's value is not in direct action prediction but in structuring the optimization landscape — is well-supported and points to a promising research direction.

## Suggestions

- Run additional trials (at minimum 20-30 per task) and report confidence intervals or at minimum standard deviations. This alone would address the most significant weakness.
- For the memory unit: show a learning curve (success rate vs. number of stored experiences) across a larger number of runs, and report retrieval precision/recall. If the gains remain marginal at scale, consider repositioning the memory unit as preliminary rather than a core contribution.
- For online adaptation: report aggregate statistics (trigger frequency, cycles-to-convergence distribution, adaptation success rate) rather than relying on a single anecdote.
- Include 2-3 example LLM-generated cost functions alongside the corresponding human-designed FSM costs, with analysis of where the LLM succeeds or fails relative to the expert. This would directly illuminate the value and current limits of the LLM-driven approach.

## Score and Decision

**Round 1 bracket:** The paper sits between the weak anchors (avg 2.5-3.0, clearly reject-level work with fundamental flaws) and the strong anchors (avg 8.0, mature contributions with large-scale evaluation). Compared to middle anchors: CoRAL is clearly stronger than "Generating Robot Policy Code for Contact-Rich Manipulation" (avg 4.00, which had fewer tasks, no baselines, weaker evaluation) and "Make a Donut" (avg 5.25, which had weaker baselines and less thorough ablations). Initial bracket: 5.25–7.5.

**Round 2 narrowing:** Compared to SuSIE (avg 6.25, diffusion-model subgoal generation + real robot + CALVIN benchmark) and Plan-Seq-Learn (avg 6.67, LLM+motion planning+RL, 25 tasks, 85%+ success). CoRAL has stronger and more diagnostic ablations than SuSIE but lacks real-world validation and has thinner per-task evidence (10 trials vs. CALVIN's standard evaluation). Plan-Seq-Learn has substantially larger-scale evaluation but requires per-task RL training, making it a different paradigm. CoRAL's zero-shot ability is a differentiating strength but the simulation-only evaluation and 4/10 on the hardest task weigh against it. The paper lands near SuSIE in overall quality — slightly below due to weaker statistical evidence and simulation-only results.

**Anchor comparison summary:**
- `oyXoGJQlUf` (avg 3.00, Round 1): GRAIL, LLM for PDDL action rule induction. Reject-level. CoRAL is substantially stronger in evaluation and contribution.
- `WtHKqtHVXo` (avg 4.00, Round 1): LLM policy code generation for contact-rich tasks. Fewer tasks, weaker baselines. CoRAL is clearly stronger.
- `iTsHStJKcm` (avg 5.25, Round 1): LLM-guided deformable object manipulation. Weaker baselines and analysis. CoRAL is stronger.
- `c0chJTSbci` (avg 6.25, Round 2): SuSIE, diffusion subgoals + real robot. Comparable quality; CoRAL has better ablations but no real-world results.
- `hQVCCxQrYN` (avg 6.67, Round 2): Plan-Seq-Learn, LLM+RL for long-horizon tasks. Stronger evaluation scale; CoRAL is zero-shot while PSL needs RL training.
- `KTtEICH4TO` (avg 4.75, Round 2): Contact-based object representation. Different problem domain. CoRAL is stronger in architectural novelty.

**Final score:** 6.0. The paper presents a clear, well-motivated architecture with convincing ablation evidence. The core contribution — LLM-generated cost functions + contact strategies enabling zero-shot contact-rich MPPI control — is novel and well-demonstrated for the tasks where VLAs fail. The evaluation is thorough in its design (multiple baselines, five ablations, human-engineered upper bounds) but thin in its statistical grounding. The memory unit is under-evidenced. These weaknesses are addressable and do not invalidate the core contribution. The paper merits acceptance.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
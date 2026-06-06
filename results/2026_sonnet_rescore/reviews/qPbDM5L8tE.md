## Summary

CoRAL is a modular neuro-symbolic framework for zero-shot, contact-rich robotic manipulation. The system decouples VLM-based physical parameter estimation from LLM-driven MPPI cost function generation, adds a closed-loop online adaptation module and an RAG-based memory unit, and evaluates the resulting architecture on six contact-rich tasks in ROBOSUITE/MuJoCo. The core claim is that explicit role separation between a vision model for perception and an LLM for reasoning, combined with iterative world-model correction, enables robust zero-shot contact-rich manipulation that outperforms end-to-end VLA baselines on tasks requiring force control and multi-contact reasoning.

---

## Strengths

- **Ablation study strongly supports modular architecture.** The *CoRAL (Unified VLM)* variant — a single model for both perception and planning — collapses on nearly every complex task (0/10 on T1, T3, T5, T6; Table 1), while the decoupled system succeeds. Removing FoundationPose (*w/o Pose Tracking*) causes complete failure across nearly all tasks (0/10 on five of six). These two ablations, having different failure patterns in Table 1, provide genuine evidence for each component's distinct and non-redundant contribution.

- **Online refinement loop demonstrated as essential via ablation.** The *w/o Refinement* condition drops to 0/10 on T1 (Push+Pick Board), compared to 4/10 with the full system. Section 4.1.3 provides a plausible mechanistic account: without the outer loop, friction estimation errors accumulate and cause grasp failures at the pick stage.

- **Human expert-designed cost baselines provide meaningful context.** Including both a single-stage and FSM expert baseline calibrates CoRAL's performance in an unusually rigorous way — the expert FSM (e.g., 9/10 on T6 vs. CoRAL's 7/10) provides a direct upper bound on what a well-engineered system can achieve on the same tasks with the same randomized conditions.

- **Contact strategy contribution is clearly illustrated.** The targeted ablation on T6 (Section 4.1.4) comparing guided vs. unguided MPPI sampling shows a meaningful qualitative difference in trajectory quality, with supporting statistics (83.9% fewer planning steps, 63.9% shorter path). This is a concrete mechanistic demonstration of what the LLM contact strategy buys.

---

## Weaknesses

### Fatal

None that fully invalidate the architecture or all experimental results. However, the Figure 4 contradiction rises to a level that significantly undermines the paper's most novel empirical claim and must be addressed before acceptance.

### Major

- **Figure 4 is internally inconsistent with its own text.** Section 4.1.4 states: *"we intentionally initialized the Evaluation World with a severely overestimated mass (2.0 kg vs. a ground truth of 0.1 kg) and friction coefficient (0.9 vs. 0.5)."* The described experiment requires the estimated mass to start near 2.0 kg and converge near 0.1 kg, a 20× correction. Yet Figure 4's y-axis spans only 0.75–1.00 kg, with the Corrected Mass line starting at 1.00 kg and converging to approximately 0.85 kg — values entirely inconsistent with the stated initial condition and ground truth. The text narrative ("converged remarkably close to their true values") is incompatible with the figure as plotted. This is the paper's primary empirical showcase of online parameter adaptation, described in the abstract as a cornerstone capability. Either the experiment was run differently than described, or the wrong figure was included. The discrepancy is unambiguous and verifiable directly from the paper.

- **The VLA baseline evaluation tests a straw-man deployment scenario for the contact-rich tasks.** Section 4.1.1 acknowledges that OpenVLA-OFT and π₀.₅ are evaluated using LIBERO checkpoints. The paper claims this comparison demonstrates CoRAL's superiority at contact-rich manipulation, but the VLA models receive no task-specific signal, demonstrations, or fine-tuning for tasks T4–T6 (constant-force pushing, box flipping, wall-fixture flipping), which are entirely outside the LIBERO distribution. The result — that a system purpose-built for zero-shot contact-rich manipulation outperforms a fine-tuned imitation policy with zero relevant data on a specialized contact task — is unsurprising and does not establish that CoRAL is superior to a well-adapted VLA approach. The comparison on T2 and T3 (in-distribution LIBERO tasks) is informative; the comparison on T4–T6 is not. This does not undermine CoRAL's own performance, but the framing in Section 4.1.1 overreaches.

### Minor

- **Contact strategy quantitative evidence is from a single trajectory pair.** Section 4.1.4 presents "83.9% faster (32 vs. 199 steps)" and "63.9% shorter path (1.33 m vs. 3.69 m)" as quantitative findings, but the paper does not state these are averaged over multiple trials. As presented these are single-run observations, not distributional claims. The directional point about strategy pruning is still visually compelling, but the precision of the reported numbers is misleading.

- **n=10 trials per condition yields low statistical power for component-level conclusions.** Differences of one or two successes (e.g., T1 from 2/10 to 4/10 for memory; T6 from 5/10 to 7/10) are attributed to specific component benefits without uncertainty quantification. No confidence intervals, binomial confidence bounds, or repeated-seed evaluations are reported. The directional findings may well be correct, but the stated conclusions about individual module contributions warrant more hedging.

- **Equation 7's $x_\text{des}$ is undefined.** Section 3.3 defines the reactive control command as $\nu_t = u_t + K_f \cdot (x_\text{des} - x_\text{measured})$ but does not define $x_\text{des}$: it is unclear whether this is the next planned waypoint, the goal state, or a force setpoint. The feedback gain $K_f$ is also uncharacterized. For a paper that emphasizes reactive force control as a key capability, this is a meaningful gap.

### Trivial

- The memory module similarity threshold (Section 3.2: "sufficiently similar") and the embedding mechanism are described only at the level of Eq. 1 without specifying what quantity is embedded or the retrieval threshold.

---

## Nice-to-Haves

- The parameter adaptation story would be substantially strengthened by a controlled experiment: vary the degree of initial parameter error (e.g., 2×, 5×, 10× overestimation) and measure success rate as a function of error magnitude, with and without the adaptation loop. This would transform the current qualitative anecdote into a characterization of the module's operating range.

- Logging and reporting a representative set of LLM-generated cost functions across tasks (e.g., showing that $w_c$ is systematically higher for contact-requiring tasks) would directly validate that the LLM is contributing physically meaningful structure, not just syntactically valid expressions.

- Reporting control loop frequency and LLM API latency would provide context for the framework's practical viability in online settings.

- Evaluating at least one VLA baseline with a small number of task-specific demonstrations (few-shot fine-tuning) would sharpen the comparison in Section 4.1.1 and let CoRAL's zero-shot advantage be stated more precisely.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Unified VLM ablation conflates two independent variables (Harsh Critic):** The critic claims the Unified VLM ablation also removes FoundationPose, confounding the inference. However, examination of Table 1 shows distinct failure patterns: *w/o Pose Tracking* gets 9/10 on T2, while *Unified VLM* gets only 2/10 on T2 — they are clearly different ablations with different failure modes. Unless the paper explicitly states the Unified VLM removes FoundationPose (it does not), this is speculative. The concern is moved to Removed as the evidence does not support the claim of confounding.

- **"Generalization" overstated in contribution bullet (Harsh Critic):** The critic notes the memory unit is tested within a single task family. This is a fair precision note, but the contribution bullet says "across diverse manipulation scenarios," which the paper partially supports across its six tasks. Marginal and does not affect the main evaluation.

- **Missing related work (Harsh Critic general area):** Per hard rules, removed — cannot verify existence of uncited works.

- **Undisclosed hyperparameters (Harsh Critic):** The paper does report the main MPPI hyperparameters (K=200, H=50, λ=0.1, N_retry=15) in Section 4. Removed per hard rule on trivial reproducibility nitpicks.

- **Strength: "Online refinement loop enables recovery from incorrect physical assumptions" (Strength Finder):** The Strength Finder claims Figure 4 validates convergence near true values, but this conflicts with the verified Figure 4 inconsistency. The ablation evidence (0/10 w/o refinement) still supports the loop's value, but the specific convergence evidence cited by the Strength Finder is unreliable.

- **Strength: "LLM-generated cost functions allow zero-shot manipulation where VLA baselines fail" (Strength Finder):** This is directionally correct for T4–T6 but overstates the informativeness of the comparison for the reasons noted under Major weaknesses. Retained in weakened form — CoRAL's own performance on these tasks is real; the *comparative* claim is what is weakened.

---

## Novel Insights

The most genuinely novel mechanism in CoRAL is using an LLM not as a policy head or a subgoal generator but as a *cost function architect* for an MPPI optimizer, combined with an outer loop where the LLM acts as a model-based diagnostician that corrects its own internal world-model parameters from physical feedback. The ablation showing that removing the refinement loop eliminates all success on the multi-stage Push+Pick Board task (0/10 vs. 4/10) provides good evidence that this feedback loop is genuinely doing useful work. If the Figure 4 inconsistency can be resolved and the adaptation experiment properly characterized, this closed-loop world-model correction capability would constitute a meaningful empirical contribution beyond the architecture itself.

---

## Suggestions

1. **Resolve the Figure 4 / Section 4.1.4 inconsistency immediately.** Either re-run the described experiment (starting at 2.0 kg, ground truth 0.1 kg) and replace the figure, or correct the text to match the actual figure. This is the highest-priority revision.

2. **Hedge the memory and contact-strategy conclusions appropriately**, either by increasing n or by adding binomial confidence intervals. Differences of 1–2 successes out of 10 should be presented with explicit uncertainty acknowledgment.

3. **Clarify the Unified VLM ablation spec**: does it retain FoundationPose for pose tracking while merging the VLM/LLM roles, or does it also remove FoundationPose? A one-sentence clarification would resolve ambiguity.

4. **Reframe Section 4.1.1 comparison.** Present T2/T3 (in-distribution) and T4–T6 (out-of-distribution) comparisons separately, acknowledge that the VLA baselines lack task-specific data for contact tasks, and frame the finding as: "even LIBERO-fine-tuned VLAs fail at zero-shot contact tasks" rather than a general superiority claim.

5. **Define $x_\text{des}$ in Eq. 7** and characterize how $K_f$ is set (e.g., constant gains, task-dependent).

---

## Evaluation on Key Axes

- **Originality:** Moderate. The idea of using an LLM to define MPPI cost functions rather than learned policies is a meaningful design distinction, but all individual components (FoundationPose, MPPI, GPT-4o, RAG) are existing tools. The architectural composition is the contribution.
- **Importance of research question:** High. Zero-shot contact-rich manipulation with physical adaptability is a genuine gap.
- **Claims supported by evidence:** Weak-to-moderate. The ablation study supports the architecture's design choices well. The online adaptation claim — the most novel — is contradicted by its own figure. Strategy analysis claims are single-trial.
- **Soundness of experiments:** Fair. Randomized initial conditions and human-expert cost baselines are methodologically thoughtful. The Figure 4 contradiction and n=10 without confidence intervals are significant concerns.
- **Clarity of writing:** Generally clear; Eq. 7 and memory module details are underspecified.
- **Value to the community:** Real but contingent on resolving the Figure 4 issue. The architecture and ablation design offer a useful blueprint for neuro-symbolic manipulation systems.

---

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>2</claims_supported>
<soundness>2</soundness>
<clarity>3</clarity>
<community_value>3</community_value>
</subscores>
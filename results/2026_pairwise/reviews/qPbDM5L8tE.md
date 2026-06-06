Now let me compile my draft review based on the paper reading, then run calibration searches.Now let me read a few of the most comparable calibration anchors to better bracket the score.Now I have sufficient information to produce the final review.

---

## Summary
CoRAL is a modular neuro-symbolic framework for zero-shot, contact-rich robotic manipulation that integrates FoundationPose (6-DoF pose tracking), GPT-4o as VLM (physical parameter estimation) and LLM (MPPI cost function and contact strategy generation), and a RAG-based memory unit. The architecture features nested inner (high-frequency MPPI reactive) and outer (low-frequency LLM diagnostic) feedback loops. Evaluation is conducted entirely in MuJoCo/ROBOSUITE simulation across six contact-rich manipulation tasks, with ablation studies targeting each core component.

---

## Strengths

1. **LLM-driven MPPI cost function formulation is a concrete architectural contribution.** Rather than having the LLM output a high-level plan for a downstream learned policy, CoRAL grounds the LLM's symbolic reasoning directly in the MPPI cost function structure (Equation 2). The LLM specifies weights $w_d, w_c, w_u$ and a contact strategy $C_0$ (Equation 3) that biases MPPI sampling — a concrete and novel mechanism for coupling language reasoning with optimal control.

2. **The modular role separation is empirically supported by a sharp ablation.** CoRAL (Unified VLM), which collapses both perception and planning into a single multimodal prompt, fails on nearly all complex tasks (0/10 on T1, T4, T5, T6), while the decoupled system achieves 4/10, 9/10, 9/10, 7/10 respectively (Table 1). This provides direct experimental support for the paper's architectural hypothesis.

3. **The online refinement loop is demonstrably essential.** Disabling the outer loop (w/o Refinement) drops T1 from 4/10 to 0/10 and T3 from 10/10 to 3/10. The paper attributes this to the outer loop's ability to diagnose and correct friction parameter errors during multi-stage tasks — a plausible and well-described mechanism (Section 4.1.3).

4. **Contact strategy guidance provides concrete search-space pruning on T6.** The guided approach was 83.9% faster (32 vs. 199 planning steps) and achieved 63.9% shorter end-effector path (1.33 m vs. 3.69 m) compared to unguided MPPI sampling (Section 4.1.4). This directly validates the utility of the LLM-generated $C_0$.

5. **Expert FSM cost baselines provide a meaningful and honest performance upper bound.** The paper includes both single-stage and FSM human-designed cost baselines, tuned independently and evaluated on the same randomized test environments. This gives an informative ceiling against which to evaluate CoRAL's zero-shot results (Table 1, Section 4.1.2).

6. **Human-interpretable failure diagnostics are a practical advantage.** The LLM's natural-language explanation of failure causes and corrective actions (Section 4.1.4) provides transparency not available in black-box VLA systems — a legitimate differentiator for trustworthy deployment.

---

## Weaknesses

### Fatal

- **Figure 4 directly contradicts the described experiment, invalidating the online parameter adaptation claim.** Section 4.1.4 states: *"we intentionally initialized the Evaluation World with a severely overestimated mass (2.0 kg vs. a ground truth of 0.1 kg) and friction coefficient (0.9 vs. 0.5)."* Yet Figure 4's y-axis spans only 0.75–1.00 kg, with the "Corrected Mass" starting at exactly 1.00 kg and converging to approximately 0.85 kg — neither the described initial condition (2.0 kg) nor the ground truth (0.1 kg) appears anywhere in the figure. The figure caption itself confirms this range. This is an order-of-magnitude inconsistency and is not a parser artifact. Since this section is the paper's primary empirical demonstration of online physical parameter correction — described as *"a cornerstone for deploying robots in unknown environments"* — the discrepancy undermines the credibility of the paper's most novel contribution. Either the correct experiment was not the one described, or the wrong figure was included.

### Major

- **The VLA comparison conclusions are overclaimed relative to the experimental setup.** Section 4.1.1 concludes: *"even fine-tuning an end-to-end policy is insufficient for scenarios that demand explicit physical modeling and reasoning."* But the experimental setup uses OpenVLA-OFT and π₀.₅ with pre-existing LIBERO-OBJECT and LIBERO-GOAL checkpoints — neither model was fine-tuned on the six contact-rich test tasks. The comparison legitimately demonstrates that CoRAL performs well zero-shot where these VLA checkpoints do not transfer. But the claim about fine-tuning ineffectiveness is not supported by the experiments as run.

- **The Unified VLM ablation does not cleanly isolate the role-separation effect.** The paper describes "CoRAL (Unified VLM)" as using "a single multimodal prompt for both perception and planning" but does not explicitly state whether FoundationPose remains active in this condition (Section 4.1.3, Table 1). Separately, "w/o Pose Tracking" (which removes FoundationPose alone) causes near-catastrophic failure across nearly all tasks (0/10 on T1, T3–T6; 9/10 only on T2). The Unified VLM condition shows nearly identical failure patterns. Without a clear statement that FoundationPose is retained in the Unified VLM variant, it is unclear whether the failures reflect the role-separation hypothesis or simply the loss of precise pose tracking. The claimed conclusion — *"separating the role of a VLM for perception from a dedicated LLM for strategy formulation is crucial"* — is not separately supported by the current ablation design.

### Minor

- **n=10 trials with no uncertainty quantification, yet small differences are stated as definitive.** Differences of 1–2 successes (T1: 2/10 → 4/10 with memory; T6: 5/10 → 7/10 with memory) are presented as clear demonstrations of each component's benefit. With n=10, binomial confidence intervals overlap substantially for all these comparisons. The directional conclusions may be correct, but the quantitative certainty implied throughout Sections 4.1.3–4.1.4 is not warranted by the data.

- **Equation 7: $x_{des}$ is undefined in context.** The reactive control term $\nu_t = u_t + K_f \cdot (x_{des} - x_{measured})$ is presented in Section 3.3 without defining $x_{des}$. The surrounding text mentions "real-time sensors (e.g., force/torque, proprioception)" but does not clarify whether $x_{des}$ is the MPPI next waypoint, the goal state, or a force setpoint. $K_f$ is described as a "feedback gain matrix" without further specification.

- **Contact strategy improvement figures (83.9%, 63.9%) appear to be single-trajectory observations, not trial averages.** The text presents these as "quantitative results" but the values (32 vs. 199 steps; 1.33 m vs. 3.69 m) come from a single compared trajectory pair in Figure 5 (Appendix), not averaged over multiple trials. The paper would benefit from clarifying whether these are representative single-trajectory comparisons or aggregated measurements.

### Trivial

- The memory module's "sufficiently similar" retrieval threshold is not defined beyond "the LLM embeds the current task into a latent semantic space" (Section 3.2). For a component credited with measurable success rate improvements, a sentence clarifying the retrieval criterion would improve precision.

---

## Nice-to-Haves

- Replace the Figure 4 single-instance demonstration with a controlled experiment: vary the degree of initial parameter error systematically and measure success rate as a function of that error with and without the adaptation loop. This would turn a qualitative anecdote into a genuine evaluation of the adaptation capability.
- Report MPPI control loop frequency and LLM API latency to contextualize the framework's real-time deployability.
- Clarify exactly how many stored memory episodes are used across conditions and whether T1's 2/10 → 4/10 improvement is reproducible across multiple experimental seeds.
- Log and analyze a sample of LLM-generated cost functions to verify that assigned weights are physically meaningful and correlate with task success (e.g., $w_c$ is higher for contact-requiring tasks).

---

## Removed Points

*These points are flagged as removed; treat them with caution.*

- **Generic "important problem" strength** about contact-rich manipulation being widely relevant — removed as non-specific to this paper.
- **Harsh Critic claim that the VLA comparison makes Table 1 "essentially uninformative"** — partially removed. The zero-shot comparison is a legitimate experimental contribution; only the specific overclaim about fine-tuning ineffectiveness is retained as a Major weakness.
- **Harsh Critic claim that "Unified VLM" failure is structural/fatal** — downgraded to Major, since the paper does describe this as a separate ablation condition and the failure pattern may partially reflect the confound.
- **Reproduced claims about missing appendix proofs or missing references** — removed per hard rules (parser strips appendices).
- **Harsh Critic claim about underspecified hyperparameters (N_retry, etc.)** — removed; K=200, H=50, λ=0.1, N_retry=15 are all clearly reported in Section 4 Implementation Details.
- **Strength Finder claim that Figure 4 "confirms convergence to true values"** — removed as directly contradicted by reading the figure, which shows convergence to ~0.85 kg, nowhere near the stated ground truth of 0.1 kg.

---

## Novel Insights

CoRAL's most distinctive technical insight is the explicit lifting of LLM reasoning into the mathematical structure of the optimal control problem: instead of generating a natural-language plan or picking from a fixed skill library, the LLM specifies the cost function terms and weights that the MPPI controller then optimizes (Equations 2–5). This creates a tighter and more explainable coupling between high-level symbolic reasoning and low-level physical execution than prior work in the "LLM as high-level planner + learned low-level policy" paradigm. The nested loop architecture — separating high-frequency MPPI correction from low-frequency LLM re-diagnosis — is also a natural and principled decomposition of the adaptation timescales involved in contact-rich tasks. However, the paper's most novel specific claim (online physical parameter correction from 2.0 kg to near 0.1 kg) is undermined by the Figure 4 inconsistency and cannot be credited in the current form.

---

## Suggestions

1. **Correct Figure 4** by either (a) replacing it with the figure from the described experiment (2.0 kg initial, 0.1 kg ground truth), or (b) correcting the text in Section 4.1.4 to match what was actually run. This is the highest-priority fix.
2. **Clarify the Unified VLM ablation** with a single sentence explicitly confirming whether FoundationPose is retained in that condition — this directly affects the strength of the role-separation claim.
3. **Correct Section 4.1.1** to remove the unsupported claim about fine-tuning insufficiency; reframe as "CoRAL performs robustly in zero-shot settings where pre-trained VLA checkpoints do not transfer to contact-rich tasks."
4. **Add binomial confidence intervals** (or at minimum ±1σ) to Table 1 to allow readers to assess the statistical reliability of small differences.

---

## Evaluation on Key Axes

- **Originality:** Moderate-to-good. The LLM→MPPI cost function approach is a meaningful step beyond "LLM as task planner," and the contact strategy generation mechanism (Equation 3) is concrete and novel. The overall system architecture is well-motivated.
- **Importance of research question:** High. Zero-shot contact-rich manipulation without teleoperation data is a significant open challenge.
- **Claims supported by evidence:** Mixed. Table 1 ablation results are solid. The VLA comparison overclaims. The most novel adaptation claim (Figure 4) is empirically broken as written.
- **Soundness of experiments:** Moderate. Simulation-only with n=10 trials, one major evidential inconsistency, and a partially confounded ablation.
- **Clarity of writing:** Generally clear. System design sections are well-organized.
- **Value to research community:** Moderate. The LLM→MPPI cost coupling is a useful idea, and the ablation structure is informative for the field.

---

## Score and Decision

The paper presents a genuinely novel architectural idea (LLM-formulated MPPI cost functions for zero-shot contact-rich manipulation) with a well-structured ablation study. However, the most novel empirical claim — online physical parameter correction — is directly undercut by the Figure 4 discrepancy, which is verifiable from the paper as written (not speculative). Combined with an overclaimed VLA comparison conclusion and a partially confounded ablation, the current submission does not provide credible evidence for its strongest claims. The core framework and Table 1 ablation results remain valuable and would support a substantially revised submission.

**Score: 4.5 / 10**
**Decision: Reject**

---

# Selected Anchors

<related>["QOfswj7hij", "hQVCCxQrYN", "9pKtcJcMP3", "c0chJTSbci", "lFYj0oibGR", "iTsHStJKcm", "VoZ0nSy0Ry", "qGL6fE1lqd", "JsVIGVntnQ", "ysAX5ORQoX", "EODzbQ2Gy4", "Cf8HBieRzL", "gw4hYNFUIC"]</related>

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
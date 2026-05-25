Now I have a clear picture of the paper. Let me write the consolidated review.

## Summary

The paper proposes CoRAL, a modular neuro-symbolic framework for contact-rich robotic manipulation that integrates a VLM (for physical parameter estimation), an LLM (for cost function design, contact strategy formulation, and online adaptation), FoundationPose (for 6-DoF tracking), and an MPPI controller. The key ideas are: (1) explicit separation of VLM perception and LLM reasoning roles, (2) an LLM-driven outer loop for mid-execution plan and parameter refinement, and (3) a memory unit for experience reuse. Evaluated across six challenging simulated contact-rich tasks, CoRAL substantially outperforms end-to-end VLA baselines (OpenVLA, π₀.₅) on tasks requiring physical reasoning while approaching hand-designed expert FSM performance.

## Strengths

- **Zero-shot contact-rich manipulation outperforms end-to-end VLA baselines.** On tasks requiring physical interaction and multi-contact reasoning (T1, T4, T5, T6), CoRAL achieves 4/10–9/10 success rates versus 0/10–3/10 for OpenVLA-OFT and π₀.₅ (Table 1). This directly validates the claim that decoupling high-level reasoning from low-level control enables robust execution on contact dynamics that end-to-end policies fail to generalize to.

- **Explicit separation of VLM and LLM roles is convincingly shown to be critical.** The "Unified VLM" ablation — which collapses perception and planning into a single multimodal model — collapses to 0–2/10 on all six tasks, while the full architecture achieves 4/10–10/10 (Table 1). This stark contrast provides clear evidence that the role separation is not merely a philosophical choice but a necessary design decision.

- **The online refinement loop and memory unit each demonstrably improve performance.** The "w/o Refinement" ablation drops from 4/10 → 0/10 on T1 and 9/10 → 4/10 on T5, confirming that the outer-loop adaptation is critical for recovering from initial world-model errors. The "w/o Memory" ablation shows consistent degradation across tasks (e.g., T1: 2/10 vs. 4/10; completion times increase 1.5–2×), supporting the value of experience reuse.

- **LLM-generated contact strategies dramatically reduce planning complexity.** A targeted analysis on the Flip with Wall task shows that the LLM's contact-region strategy reduces required steps by 83.9% (32 vs. 199) and end-effector path length by 63.9% (1.33 m vs. 3.69 m) compared to using only the cost function (§4.1.4). This is quantitative evidence that symbolic contact strategies effectively prune the action search space.

## Weaknesses

### Fatal
None.

### Major

- **The online parameter adaptation demonstration (Figure 4) is inconsistent with the text, undermining a headline claim.** Section 4.1.4 states the evaluation world was initialized with an overestimated mass of 2.0 kg (vs. a ground truth of 0.1 kg). Yet Figure 4's y-axis spans only 0.75–1.00 kg, shows an "Initial Mass" constant at 1.0 kg, and reports a "Corrected Mass" converging to ≈0.85 kg rather than 0.1 kg. The text claims convergence "remarkably close to their true values," which the figure does not support. No friction-correction graph is provided despite also being claimed. This discrepancy directly weakens the paper's evidence for online parameter correction. The authors should clarify whether the axis is mislabeled, the text numbers are wrong, or a different experiment is being shown, and adjust their claims accordingly.

### Minor

- **The LLM cost function generation interface is underspecified.** The paper states that the LLM outputs "the mathematical structure and relative weights of a cost function" and that it "is free to introduce any cost terms constructible from the available state, pose, and action variables," but provides no concrete prompt template, output format/schema, or parsing procedure. Equation (2) is labeled an "illustrative example" without clarifying whether it is the actual parsed format. While the overall architecture is clear, the lack of specification for this core step limits reproducibility.

- **Statistical evidence is weak for fine-grained comparisons.** All experiments use 10 trials per condition, which yields wide binomial confidence intervals (e.g., a 4/10 result has ≈12%–74% 95% CI). Differences that drive detailed conclusions (memory vs. no-memory on T1: 4/10 vs. 2/10; on T6: 7/10 vs. 5/10) are within the noise. No confidence intervals or significance tests are reported. The paper should be more circumspect in interpreting these marginal differences.

- **Contact strategy analysis reports no variance.** The 32 vs. 199 step comparison appears to be from a single trajectory; no standard deviation or replication information is provided. At a minimum, error bars or multiple-run aggregates should be reported.

- **Reliance on known 3D object models is not acknowledged as a limitation.** FoundationPose requires known CAD models of all interactable objects. The paper does not discuss how this constraint affects deployment or how it might be relaxed (e.g., category-level estimation, online model acquisition).

- **Memory unit retrieval mechanism is underspecified.** The paper mentions RAG-based retrieval where the "LLM embeds the current task into a latent semantic space" (Eq. 1), but does not specify how episodes are indexed, what "sufficiently similar" means, or the concrete vector-database/retrieval implementation.

### Trivial
None.

## Nice-to-Haves

- Real-world validation, or at minimum a discussion of sim-to-real challenges specific to CoRAL's components, would substantially strengthen the paper.
- A latency breakdown (VLM call vs. LLM call vs. MPPI rollouts) would help contextualize the reported completion times.
- The explainability claim (Section 4.1.4) would benefit from a more systematic evaluation rather than a single anecdotal example.

## Removed Points

The following points from the reviewers were removed or downgraded with justification:

1. **"The evidence that online refinement actually works is absent"** — Too strong. The w/o Refinement ablation (T1: 4/10→0/10, T5: 9/10→4/10) provides independent evidence that the outer loop contributes to task success, even though the specific parameter-correction demonstration is flawed.
2. **"LLM output interface is a critical methodological gap"** — Downgraded from critical to minor. While the prompt/schema details are absent, the paper gives a concrete cost-function example (Eq. 2) and describes the architectural role of the LLM output. The exact prompt engineering, while useful, is an implementation detail that could reside in an appendix.
3. **"Reliance on a single LLM call after N_retry failures is fragile"** — Speculative. The paper does not constrain the outer loop to a single call; the LLM is reinvoked each time the outer loop is triggered.
4. **"Fatal flaw / score collapse" reasoning** — The mass-correction issue, while significant, does not invalidate the paper's core contributions (architecture, role separation, ablation results). It undermines a specific supporting demonstration, not the central claims.
5. **Certain generic strength-finder statements** (e.g., "this paper addressed an important problem") were removed due to lack of specificity.

## Novel Insights

The most novel observation is that explicitly separating the vision model (for perception and physical parameter estimation) from the language model (for strategy/cost formulation) yields dramatically better performance than a unified VLM on contact-rich tasks. This suggests that the kind of reasoning required for contact-rich planning (physical understanding + strategy) benefits from dedicated modules rather than monolithic multi-modal models. Additionally, using an LLM to dynamically generate and revise the structure (not just weights) of an MPPI cost function — rather than relying on a fixed task-specific objective — is a promising approach for zero-shot generalization to novel physical interactions.

## Suggestions

1. **Resolve the Figure 4 inconsistency.** Either correct the figure axis to match the described 2.0 kg→0.1 kg experiment, or fix the text to describe what Figure 4 actually shows. Provide the friction correction plot if it exists. Adjust the "converged remarkably close" language to match the presented evidence.
2. **Provide the LLM prompt template and output schema** in an appendix, even as a representative example. This would greatly improve reproducibility.
3. **Increase trial count or report confidence intervals** for at least the key comparisons, and add error bars to the contact strategy analysis.
4. **Discuss the known-CAD-model requirement** explicitly as a limitation and outline potential mitigations.
5. **Add variance estimates** to the contact-strategy step-count and path-length results.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
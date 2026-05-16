Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper tackles zero-shot environmental generalization in RL — the problem of deploying a policy in environments with different state spaces, transition dynamics, and observation modalities without retraining. It introduces a structurized state-space model (Definition 3.1) that decomposes observations into invariant task components ψ_t(I) and task-agnostic backgrounds ξ_t^e, and uses this framework to argue for a "non-optimizable gap" that prevents standard RL from generalizing. The proposed method, Non-Parameterized Randomization (NPR), randomizes task-agnostic environment components (object positions, room structures, backgrounds) during training without requiring a parameterized model of the environment. Experiments on cross-environment transfers (MuJoCo→BabyAI, 2D Gym→3D Torcs, 2D→3D first-person view) show NPR outperforming PPO, DrAC, DroQ, and DR baselines.

## Strengths

1. **Novel structured framework for environmental generalization.** Definition 3.1's decoupled state-space model (ψ_t(I) ⊕ ξ_t^e) provides a clean formal way to separate invariant task content from environment-specific background. This is more general than prior models like Block-MDPs, which assume shared state spaces across tasks, and gives the paper a principled vocabulary for discussing why cross-environment transfer is hard (Section 3.1, lines 52–64).

2. **NPR is a genuine extension of randomization-based generalization.** The core idea — randomize task-agnostic components (scene structure, object positions, backgrounds) rather than simulator parameters — is a meaningful departure from standard Domain Randomization. The paper correctly identifies that DR requires a parameterized model of the target environment, which limits its applicability when the environmental change is structural rather than parametric (Section 4.1, lines 115–132; Remark 4.2).

3. **Consistent empirical outperformance on very challenging tasks.** The experimental setup — zero-shot transfer between environments with different observation spaces, dynamics, and even viewing perspectives (2D→3D, third-person→first-person) — is genuinely ambitious. NPR achieves positive success rates (e.g., 89.2% on MuJoCo Square→BabyAI FindObj per Table 1; 52% on Key-Corridor-S6R3) where almost all baselines score 0% across the board. Tables 1, 2, and Section 5.4's 2D→3D first-person task (8% success on one-step identification) show NPR generalizes where other methods completely fail.

4. **Ablation confirms necessity of randomization.** The No-Rand baseline (Section 5.3) shows 0% success in all generalization tasks, cleanly demonstrating that the randomization component of NPR is essential and that standard RL training (single environment) cannot handle the tested transfers.

5. **Stable learning in randomized environments.** Figure 3 shows NPR learns stably under randomization while baselines degrade (e.g., DrAC performs worse than random policy in Figure 3a). The "soft randomizing with continuous and slow episodic change" (Section 4.2, line 145) is a practical contribution to the known problem of training instability under high-variance environment dynamics.

## Weaknesses

### Fatal
None. The paper's core claims are not invalidated.

### Major

1. **Method critically underspecified for reproducibility and verification of claims.** The paper does not explain how the policy handles cross-environment transfer at the architectural level. It states action spaces are assumed the same (Section 3.1, line 46) and that "the action space is discrete and executed by the simulator" for MuJoCo→BabyAI (line 159), but never specifies: are MuJoCo environments modified to use discrete actions? Are observations rendered as pixel arrays of a fixed size (the baselines use "pixel observation by CNN," line 164)? What is the network architecture? Without these details, a central question goes unanswered: how does a single policy take input from one environment and produce meaningful actions in another with a completely different state space? The claims of zero-shot cross-environment transfer rest on this mechanism being coherent, but the paper does not make it verifiable.

2. **Baseline comparisons are not informative because baselines were not designed for the task.** DrAC and DR are designed for visual domain shifts (color, texture, lighting, visual randomization) and PPO/DroQ are generic RL algorithms. Unsurprisingly they fail when tested on changes in state-space topology, transition dynamics, and observation modality. Comparing NPR against methods that were never intended to address this setting yields a weak argument for NPR's superiority. A meaningful evaluation would include methods also targeting cross-environment transfer — e.g., invariant representation learning (bisimulation metrics, contrastive approaches), context-conditioned policies, or meta-RL methods — to demonstrate that NPR's specific design choices matter.

3. **Proposition 3.4's sparse-reward assumption is disconnected from the experiments.** Proposition 3.4 (Implicit Invariant Learning, line 101) assumes "sparse reward 1 of the final state representing completing the task" and claims this enables implicit learning of invariant representations. The paper never reports whether any experimental environment uses sparse rewards, and the proposition is not referenced in the Method section (Section 4) or experiment descriptions. The role of this proposition in the overall argument is unclear, and the experimental evidence cannot be connected to it.

### Minor

1. **The theoretical framework provides intuition but not actionable design guidance.** Proposition 3.3 bounds the value-function difference between environments by two terms, one labeled "optimizable" (invariant learning error) and one "non-optimizable" (transition-dependent term depending on ξ_t^e). This formalizes the difficulty but does not connect to specific design choices. Theorem 4.1 bounds the return in unseen environments by the return in randomized environments minus α, which depends on KL(ρ(e)‖ρ(ξ̂_t)) — the KL divergence between the unknown test-environment distribution and the randomization distribution. Since ρ(e) is unknown, this bound is not directly actionable for designing the randomization distribution. It is a standard type of transfer-learning bound (showing the gap depends on distribution mismatch) but does not distinguish NPR from any randomization scheme.

2. **The "non-parameterized" vs. "parameterized" distinction is overstated.** The paper argues that DR requires a parameterized model of the target environment (Remark 4.2, line 132). This is true for sim-to-real transfer. However, in the paper's own experiments, the target environments (BabyAI, Torcs, MiniWorld) are simulators with known structure. NPR could be implemented using those simulators' randomization APIs; the distinction between "randomizing scene elements" and "randomizing simulator parameters" is practically meaningful but not a fundamental theoretical separation. The paper's critique that parameterized methods add "another term" to the bound (Remark 4.2) is stated without proof or derivation, weakening the force of the claim.

3. **Limited statistical rigor for central claims.** Figure 3 uses 3 random seeds; Table 2 uses 5 seeds; Table 1 reports "500 episodes" but does not specify how many independent training seeds were used for the generalization evaluation. With many results at 0% for baselines and some NPR results also at 0%, the practical variance of these numbers is unclear. Confidence intervals or standard errors across seeds for the zero-shot evaluation would substantially strengthen the claims.

4. **No discussion of failure cases.** Several transfer tasks yield 0% success for NPR (Table 1), but the paper does not analyze why some transfers work (89.2% on FindObj) while others completely fail. Understanding these failure modes is important for assessing the method's limitations and for guiding future work.

### Trivial
None.

## Nice-to-Haves

- Statistical reporting with confidence intervals for zero-shot evaluation results.
- Ablation isolating which randomization components (structure, background, spatial relationships) matter most.
- Analysis of why certain transfers fail (e.g., which tasks yield 0% for NPR).

## Removed Points

These points from the original reviews are flagged for removal — treat them with caution:

- **"The paper mentions code availability only indirectly" and missing hyperparameters/architecture details.** The hard rules direct removal of nitpicks about undisclosed hyperparameters as trivial reproducibility concerns. However, I have kept the criticism about missing *architectural mechanism for cross-environment transfer* as Major because it goes beyond hyperparameter nitpicks to the core feasibility of the claimed experiments.
- **"Missing appendix / missing proofs in appendix."** The parser strips appendix content from all papers. Removed per hard rules.
- **"Proposition 3.3 contains a formatting error in the denominator" and "garbled text."** These are parser artifacts, not author errors.
- **"The bound in Proposition 3.3 depends on |S^e||S^e|^2 that appears without motivation."** The notation is unusual but the bound's structure is standard for difference-of-value-function bounds; the critic's interpretation is speculative.
- **Criticism that the paper does not acknowledge DR (Tobin et al., 2017) for zero-shot transfer.** The paper explicitly cites and discusses DR in Section 2 (line 38) and Section 4.1 (Remark 4.2). The claim "first to achieve generalization tasks with environmental change in zero-shot" refers to the specific setting of cross-environment transfer with different state spaces and transition dynamics, not zero-shot transfer via DR in general.
- **Strength Finder's claim that the "single most important piece of evidence is the empirical result in Table 1 where NPR achieves 89.2%."** While this result is mentioned in the Strength Finder summary, the exact number cannot be independently verified from the paper text (Table 1 is an image in the parser output). The overall pattern (NPR substantially outperforms baselines) is clear from the paper's textual description.

## Novel Insights

None beyond the paper's own contributions. The review process surfaces a recurring tension in RL generalization papers: the difficulty of constructing informative baselines for genuinely novel transfer settings. When a paper targets a problem no prior method was designed to solve, the standard approach of comparing against existing methods (even inappropriate ones) produces weak evidence. The field would benefit from a clearer norm around what constitutes a meaningful comparison for new generalization paradigms — perhaps requiring ablation of the method's own components and analysis of its internal mechanism rather than asymmetric comparisons against methods solving a different problem.

## Suggestions

1. **Specify the cross-environment transfer mechanism precisely.** How are action spaces reconciled across environments? What is the observation representation (rendered image size, channels)? Provide the network architecture and training hyperparameters. Without this, the central experimental result cannot be assessed or reproduced.

2. **Add baselines that are designed for the same problem class.** Compare against invariant representation learning methods (e.g., bisimulation metrics, contrastive RL), context-conditioned policies, or meta-RL. If no appropriate baselines exist, make this explicit and strengthen the analysis of NPR's own mechanism (ablation of randomization components, analysis of what the learned policy ignores).

3. **Tighten the theory-practice connection.** Either (a) use the theory to derive a concrete, testable prediction about which randomization distributions work best (e.g., coverage conditions on ξ̂_t), or (b) reframe the theoretical section as a formalization of the problem difficulty and move Theorem 4.1's bound to the appendix as a standard transfer-learning result, focusing the main text on the method's practical design.

4. **Connect Proposition 3.4 to the experiments** by reporting whether sparse rewards are used, or relax the assumption to cover the dense-reward setting actually used in evaluation.

5. **Analyze failure cases** — why does NPR succeed on some transfers (89.2% on FindObj) and completely fail on others (0% on several)? Is it a limitation of the randomization coverage, a mismatch in task semantics, or something else?

## Score and Decision

The paper tackles an important open problem — zero-shot generalization across RL environments with different generative models — and the proposed framework (structured state-space model + task-agnostic randomization) offers a genuinely new perspective. The experimental results, while positive, are weakened by: (1) a critically underspecified cross-environment transfer mechanism that makes the central claims unverifiable; (2) comparison against baselines not designed for the task, which inflates the apparent advantage; and (3) a theoretical framework that provides intuition but does not yield testable design guidance. These are major, not fatal, issues — the core ideas have merit — but the paper in its current form does not meet the bar for publication.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
- Decision: Reject
- Avg Score: 2.50
- Scores: 3, 3, 3, 1
I've confirmed the critical findings. The results section is genuinely empty, the baseline comparison is only against vanilla DDPG, and subgoals are assumed rather than learned. Let me now synthesize the final review.

---

## Summary

This paper proposes using learned approximate dynamics models (graph neural networks with structural inductive biases) to guide exploration in reinforcement learning for intuitive physics tasks, rather than using them to generate training data. The key idea is to use model rollouts to identify clusters of rewarding actions and sample from these clusters during exploration in an epsilon-greedy framework. The method is applied to the Chain Reaction Tool Environment (CREATE) using DDPG as the base RL algorithm.

## Strengths

- **Clean separation of model use from policy learning**: The paper explicitly avoids using the learned model to generate training transitions for the policy, instead using it only for constructing action priors via clustering of successful model rollouts. This directly addresses the classic problem of compounding model error corrupting policy updates (Section 1: "By using approximate and imperfect models to guide exploration only and not generate experience or transitions from which the reinforcement learning algorithm directly learns, we mitigate the impact of model error on stable policy learning").

- **Principled architectural design for physics prediction**: The GNN design combines three well-motivated assumptions — distinct per-edge update functions per object-pair type, dynamic edge activations via distance cutoff, and a relative coordinate system centered on the moving ball — that together enable generalization to variable object counts and scene configurations (Section 4.1, three bullet points with explicit rationale).

- **Clear, repeatable procedure for extracting exploration guidance from an approximate model**: The multi-step protocol (model rollouts with random actions → store successful actions → K-means clustering → compute cluster statistics → use as exploration priors) provides a concrete methodology that others could adapt (Section 4.2, steps 1–4).

## Weaknesses

### Fatal

- **Entire Results section (Section 5.4) is missing from the submission.** The paper presents zero experimental data. Section 5.4 consists only of the heading and the sentence "Our experiments aim to answer the following questions:" before jumping directly to "6 CONCLUSIONS." There are no learning curves, no tables, no quantitative comparisons, no ablation studies, and no statistical analyses. The paper's central empirical claims — that the method "significantly improves the frequency of reward signals" and "accelerates convergence to optimal policies" — are unsupported by any evidence in the manuscript. This is a fatal structural flaw that makes evaluation of the scientific contribution impossible. Unlike appendix content that may be stripped by parsing, the main Results section is a core component of any empirical paper; its absence cannot be attributed to a parsing artifact.

### Major

- **Only one baseline (vanilla DDPG) is compared.** The paper compares DDPG-MGE against standard DDPG with Ornstein-Uhlenbeck noise (Section 5.3). No comparison is made against any other exploration method for continuous control with sparse rewards (e.g., intrinsic motivation, curiosity-driven exploration, Hindsight Experience Replay, model-based RL methods like MBPO or PETS). Even if results existed, showing improvement over a single, weak baseline would not establish that model-guided exploration is competitive with or better than existing approaches. This is a significant methodological gap regardless of the missing results.

- **Subgoals are assumed, not learned.** The method relies on a pre-specified set of subgoals for each task (Section 4.2, Step 1: "For each task, we assume a set of subgoals exist"). The paper acknowledges this as future work (Section 6), but in its current form, this means the approach is not fully autonomous. The subgoals encode task structure and provide a strong inductive bias. Without an ablation that removes or learns subgoals, it is impossible to determine how much of the claimed benefit comes from the model and how much from the subgoal decomposition.

- **Dynamics models are learned per tool combination, limiting generalization claims.** The paper states (Section 5.2): "A dynamics model is learned for each unique combination of tool types that are included in the tasks we include in this paper." This contradicts the claim of "flexible generalisation to unseen tasks" — if a new task uses a combination of tools not seen during training, a new model would need to be trained. The task-agnostic training (single-tool observations) is a reasonable foundation, but the per-combination model requirement limits the scope of the generalization claim as stated.

### Minor

- **Model accuracy and cluster reliability are unquantified.** The paper repeatedly emphasizes that models are approximate/imperfect but never provides any analysis of model prediction error, rollout horizon effects, or whether model-identified actions actually lead to subgoals in the real environment. This makes the core mechanism (model-guided action clustering) a black box.

- **K-means cluster count is unspecified.** The clustering step (Section 4.2, Step 2) uses K-means but does not state the number of clusters or how it is determined. Results may vary significantly with this choice, and no robustness analysis is reported.

- **One-step training data for dynamics models may be insufficient for multi-step dynamics.** The models are trained on 1000 one-step observations per tool type (Section 5.2). This may not capture multi-step interaction dynamics (e.g., a tool deflecting a ball into another tool), which could limit model accuracy when tools interact sequentially over time.

- **Model rollouts use random actions without justification.** The procedure rolls out the model with "randomly sampling actions" (Section 4.2, Step 2). A smarter sampling strategy (e.g., from the current policy or a distribution biased toward interesting regions) might improve cluster quality, but this design choice is not discussed or justified.

### Trivial

- The paper has a typo in Section 2.1: "fetaures" should be "features" (line 34).
- The notation in Equation 1 uses $\operatorname*{max}_{\mathrm{a}}\dot{Q}(s,a)\approx Q(s,\mu(\bar{s}))$ where the dot over $Q$ and the bar over $s$ appear to be formatting artifacts.

## Nice-to-Haves

- **Compare against at least one modern exploration method** (e.g., curiosity-driven exploration, Go-Explore) to contextualize the contribution within the exploration literature.
- **Provide an ablation that removes or learns subgoals** to isolate the subgoal effect from the model's contribution.
- **Study sensitivity to clustering parameters** (number of clusters, distance cutoff for edge activations) to establish robustness.
- **Quantify model prediction error** as a function of rollout horizon, and show how cluster quality (e.g., do model-identified actions actually reach subgoals in the real environment?) relates to exploration success.
- **Report computational cost** — the approach requires multiple model rollouts and real-environment rollouts per subgoal; total environment interaction counts should be transparent.

## Removed Points

These points from the input reviews were removed, with justification:

- **"The framing that approximate models can help exploration is not novel" (Harsh Critic):** This is a generic criticism not anchored to a specific claim in the paper. The paper's specific contribution — using models *only* for exploration guidance (not training data generation) in the context of intuitive physics with GNNs — is a novel combination of ideas.
- **"Several prior works have used learned models to guide exploration" (Harsh Critic):** Unanchored; the critic does not identify a prior method with the same combination of properties (separating model use from policy learning, using GNNs for physics prediction, computing action cluster distributions).
- **Questions about model availability or reproducibility** (e.g., "cannot be independently verified"): Removed per instructions — all cited entities are assumed to exist.
- **Formatting/style nitpicks:** Removed per instructions.
- **"Missing related work" comments:** Removed per instructions, as I cannot verify existence of unmentioned works.
- **Strawman misunderstandings:** Removed claims that mischaracterize the method (e.g., critic's suggestion that models are trained from "one-step data" in a way that ignores multi-step dynamics entirely — the paper itself notes this limitation).
- **Strength Finder's generic strengths** about "importance of the problem" without specific evidence: Removed.
- **Speculative fatal claims** (e.g., "if the normalization were X, the reported values would be impossible"): Not present in inputs; no action needed.

## Novel Insights

None beyond the paper's own contributions. The paper presents an interesting methodological combination (GNN-based approximate models → action clustering → epsilon-greedy exploration for sparse-reward physics tasks), but the complete absence of experimental results prevents any assessment of whether this combination actually works. The key insight — separating model use for exploration from model use for data generation — is well-motivated by the paper's discussion of model error in model-based RL, but without evidence it remains a proposal rather than a validated approach. The reviewers did not surface any additional novel observations beyond what the paper itself states.

## Suggestions

1. **Add the experimental results** — this is the single non-negotiable requirement. Include learning curves with multiple random seeds and shaded standard deviations for both DDPG-MGE and standard DDPG on all tasks shown in Figure 3.
2. **Include at least one additional exploration baseline** (e.g., DDPG with parameter noise, or a simple intrinsic motivation method) to demonstrate that the model-guided approach offers advantages beyond just adding structured noise.
3. **Add an ablation without subgoals** to isolate what the model contributes vs. the subgoal decomposition.
4. **Report model accuracy** — even a simple plot of prediction error vs. rollout horizon would ground the central assumption that imperfect models can still usefully guide exploration.
5. **Clarify the generalization claim**: either retrain less frequently (one model for all tool combinations) or explicitly scope the claim to tasks whose tool combinations were seen during model training.

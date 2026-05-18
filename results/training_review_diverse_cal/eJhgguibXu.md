I have thoroughly verified each claim against the paper. Here is my consolidated review.

---

## Summary

This paper proposes using approximate learned dynamics models (GNNs with structured edge functions, dynamic edges, and relative coordinates) to guide exploration in reinforcement learning for intuitive physics tasks. The key idea is not to use the model for generating training experience (which would suffer from compounding model error), but rather to use it to compute distributions over rewarding actions via subgoal-decomposed rollouts and K-means clustering, then incorporate these into an epsilon-greedy exploration strategy. The paper is motivated by cognitive science findings about human use of imperfect intuitive physics models.

## Strengths

- **Principled decoupling of model use**: The paper clearly articulates why the model is used for exploration only, not for generating training experience: "By using approximate and imperfect models to guide exploration only and not generate experience or transitions from which the reinforcement learning algorithm directly learns, we mitigate the impact of model error on stable policy learning" (Section 1). This directly addresses a central difficulty in model-based RL and is a well-motivated design choice.

- **GNN architecture with explicit structural inductive biases**: The three design principles in Section 4.1 — distinct per-edge update functions for different object-pair types, dynamic edge activations via a distance cutoff, and relative coordinate frames — are concrete, motivated choices intended to enable cross-task generalization. The rationale for each (e.g., "Newtonian physics is invariant to changes in absolute object positions") is clearly stated.

- **Subgoal decomposition as a practical mitigation for compounding model error**: The paper identifies that compounding prediction error over long horizons is a core challenge and uses subgoals to shorten model rollout horizons (Section 4.2, step 1), connecting the imperfect model to a feasible exploration strategy. This is a sensible mechanism.

- **Action clustering pipeline that translates model predictions into actionable exploration distributions**: The process in Section 4.2 (model rollouts → store rewarding actions → K-means clustering → approximate as Gaussians → sample in epsilon-greedy) is a concrete, computable bridge between model outputs and policy exploration.

- **Grounded interdisciplinary motivation**: The paper draws on cognitive and developmental psychology findings about human intuitive physics (Piloto et al., 2022; Allen et al., 2020) to motivate why imperfect models can still be useful for guiding search, providing a richer justification than typical technical limitations alone.

## Weaknesses

### Fatal

- **The experimental results section is absent from the provided manuscript.** Section 5.4 ("RESULTS") contains only the section heading and the fragment "Our experiments aim to answer the following questions:" before jumping directly to Section 6 ("CONCLUSIONS"). No empirical outcomes — no plots, tables, or even textual descriptions of results — are present. The paper's central claim is that the proposed method improves sample efficiency and accelerates convergence, and the contribution is fundamentally empirical. Without the results, the core claims cannot be evaluated, verified, or assumed to hold. This is not a formatting artifact (other figure captions and section text are preserved); the section content is genuinely missing. This single issue is fatal for a paper whose contribution rests on experimental validation.

### Major

- **The method assumes subgoals are given as part of the problem specification, with no mechanism for obtaining them.** Section 4.2 states: "For each task, we assume a set of subgoals exist that provide reward signals over shorter intervals." The paper does not explain how these subgoals are obtained — whether from environment design, human annotation, or automatic discovery. The applicability of the method is therefore limited to settings where a suitable task decomposition is already available. While the paper acknowledges this in the future work section ("Future work that learns subgoals for tasks instead of relying on them being specified would significantly improve our approach"), this does not address the severity of the limitation for the present contribution. Without knowing what subgoals were used (and there are no results to describe them), the reader cannot assess how much work the method is doing versus how much is done by the hand-specified decomposition.

- **The baseline comparison is weak for an exploration paper.** The only baseline is standard DDPG with Ornstein-Uhlenbeck noise (Section 5.3). For a method whose contribution is improving exploration in continuous action spaces, comparison against a broader set of exploration baselines is needed — DDPG with Gaussian noise, parameter noise (Plappert et al., 2018), or count-based intrinsic motivation methods would be natural choices. Showing improvement over a single baseline that is not known for strong exploration does not convincingly isolate the effect of model-guided exploration.

- **No analysis of sensitivity to model error.** The paper's central motivation is that approximate models can still be useful for exploration. Yet there is no analysis of how model prediction error affects the identified action clusters, nor any characterization of when the model is trustworthy enough to guide exploration. The method uses the model to simulate random rollouts and selects actions that "lead to the subgoal being achieved as predicted by the model." If the model is systematically biased, these clusters could point to wrong action regions entirely. An analysis of how cluster quality (e.g., Earth Mover's Distance between model-derived and ground-truth action distributions) varies with model accuracy would directly support the core claim.

- **Potential sample efficiency overhead not accounted for.** Step 3 of Section 4.2 involves rolling out the *real environment* between subgoals to obtain initial states for the next phase. These real-environment rollouts incur interaction cost that the baseline (standard DDPG) does not incur. The paper does not discuss whether this overhead is factored into the claimed sample efficiency comparisons.

### Minor

- **The epsilon threshold and the number of K-means clusters are unspecified.** Section 4.3 describes epsilon-greedy exploration with a threshold $\epsilon_{\text{threshold}}$ but does not explain how this is set or whether it is annealed. Section 4.2 uses K-means clustering without specifying the number of clusters — a hyperparameter that could significantly affect the discovered action distributions.

- **The claim that models "flexibly generalise to unseen tasks" lacks supporting evidence in the provided manuscript.** This claim appears in the abstract, introduction, and conclusion, but (a) the results section is missing, and (b) the generalization tested would be combinatorial (new arrangements of seen tool types) rather than to fundamentally new tool types or physical phenomena. The paper's framing may overstate the scope of generalization demonstrated.

### Trivial

- None beyond the fact that the above issues would be partly addressable if the results section were present.

## Nice-to-Haves

- An ablation of the epsilon threshold and cluster count would strengthen the empirical contribution.
- A study comparing the model-derived action distributions against those computed from ground-truth rollouts would directly validate whether the approximate model identifies genuinely useful action regions.
- An analysis of how model prediction error (e.g., MSE on held-out one-step predictions or rollout accuracy over the subgoal horizon) relates to downstream policy learning performance.

## Removed Points

- **Criticism about missing appendix details (A.1, A.2):** The appendix is stripped by the parser. This is a known artifact; the content exists in the original submission. Removed per instruction.
- **Criticism about "the main missing part is the experimental results section" being re-stated as a separate point:** Already captured in the Fatal section above; not removed, just deduplicated.
- **Strength Finder's generic framing:** The strengths listed were all grounded with specific citations to paper sections, so none were removed as generic/superficial.

## Novel Insights

None beyond the paper's own contributions, given that the experimental validation needed to assess the novelty is absent. The core idea — using imperfect models for exploration guidance rather than experience generation — is interesting but cannot be evaluated without results.

## Suggestions

1. **Provide the experimental results.** Without this, the paper cannot be accepted. The results section must include learning curves, sample efficiency comparisons (e.g., cumulative reward vs. environment steps), and ideally statistical significance across multiple seeds. This is the single highest-priority fix.
2. **Expand the baseline set.** Add at least DDPG with parameter noise and DDPG with Gaussian noise to isolate the effect of the model-guided exploration from the basic noise used for exploration.
3. **Clarify the subgoal situation.** Either (a) explain how subgoals are obtained in the experiments (e.g., they are implicit in the environment's reward structure for each CREATE task), or (b) provide a mechanism for automatic subgoal discovery. If subgoals are provided by the environment/task design, state this explicitly and qualify the contribution accordingly.
4. **Account for the real-environment rollout overhead in sample efficiency comparisons**, or explain why it does not affect the comparison.
5. **Add a model-error sensitivity analysis** — even a simple one showing whether model prediction error correlates with exploration benefit.
6. **Specify the epsilon threshold setting, the number of clusters K, and the number of model rollouts** in the method description.

## Score and Decision

This paper presents a well-motivated idea and a reasonable technical approach (GNN design, action clustering pipeline, integration with DDPG). The methodological description is generally clear. However, the fatal absence of experimental results means the paper's core claims — that the method improves sample efficiency and accelerates convergence — cannot be evaluated. For an empirical paper, this is disqualifying. Additionally, even if results existed, the weak baseline comparison and unaddressed reliance on given subgoals would need significant strengthening. The current manuscript does not meet the bar for acceptance.

MY FINAL SCORE: <pineapple>3.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
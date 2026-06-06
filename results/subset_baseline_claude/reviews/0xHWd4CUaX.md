## Summary

The paper proposes a framework that combines contrastive self-supervised pre-training of code graph embeddings with reinforcement learning (RL) for automated code refactoring. A syntax-guided graph attention encoder learns structural invariant representations via augmentation-based InfoNCE, which are then used in a composite reward function alongside traditional code quality metrics and differential-test-based semantic preservation. The resulting policy network (PPO-trained) is evaluated on refactoring quality, semantic preservation, and cross-language generalization.

---

## Strengths

- **Reasonable overall motivation.** Learning refactoring-aware representations without expert labels is a legitimate problem, and the three-stage pipeline (contrastive pre-training → frozen encoder → PPO fine-tuning) is architecturally clean and modular.
- **Ablation study present.** Table 2 systematically removes each major component, and the results plausibly rank components: contrastive pre-training matters most for SI, semantic tests matter most for SP. The relative ordering is defensible.
- **Learning curve comparison (Figure 1)** concretely shows faster convergence, a meaningful efficiency claim.

---

## Weaknesses

### Fatal
None that fully invalidate every aspect of the paper.

### Major

1. **Reward term for embedding dynamics is conceptually problematic.** The second term in Eq. (5), $\alpha \tanh(\beta \|\mathbf{h}_t - \mathbf{h}_{t-1}\|_2)$, rewards larger movement in latent space. This is not grounded: the encoder is fixed during RL, so embedding dynamics reflects code change magnitude rather than quality. An agent can trivially maximize this term by making large but meaningless edits. No analysis rules out this degenerate strategy. Figure 3 compounds the concern: by stage 100, embedding dynamics dominates the reward at ~70%, meaning the agent is guided primarily by an unvalidated proxy.

2. **Internal inconsistency between Eq. (5) and Eq. (8) for semantic preservation.** In Eq. (5), $\delta_t = \mathbb{I}[\text{test}(G_t) = \text{test}(G_{t-1})]$ is binary (0/1). In Eq. (8), $\delta_t$ is defined as a continuous normalized Hamming distance over execution traces ($0 \leq \delta_t \leq 1$). These two formulations are incompatible and it is impossible to tell which is actually used in experiments.

3. **Action space never defined.** The paper does not specify what the legal atomic refactoring actions are, how the code graph $G_t$ is updated after applying an action, or how the discrete/continuous action space is structured. This is a central missing piece for reproducibility and soundness.

4. **Cross-language generalization results undercut the narrative.** In Table 3, the proposed method achieves lower semantic preservation (SP) on Python (88.9%) than PyLint (90.4%) — a rule-based baseline — yet this is not discussed. The positive SP of cross-language transfer is not uniform and the cherry-picked framing overstates generalization.

5. **Results lack statistical rigor.** Table 1 shows the proposed method strictly dominating every baseline on every single metric (5/5) with no error bars, confidence intervals, or significance tests. The clean sweep without variance information raises serious concerns about result reliability on all three datasets.

### Minor

1. The "GraphRL" baseline (Darvari et al., 2024) cited in Table 1 is a survey of graph RL for combinatorial optimization, not a code refactoring system. Using a survey paper as a baseline is unconventional and the adaptation is not explained.
2. BigCloneBench is a code clone dataset, not a refactoring dataset. Its use as an evaluation set for code refactoring is not motivated.
3. Figure 2 shows $r=0.72$ correlation between $\Delta h$ and SI but only post-hoc; since SI also drives $w_q^\top \phi(q_t)$, both quantities are causally linked through the reward, making this correlation circular rather than validating the embedding.

### Trivial
- Figure 1 caption is duplicated.

---

## Nice-to-Haves

- Visualize a handful of actual before/after refactored code snippets with concrete metric values, rather than just abstract qualitative patterns.
- Run an experiment that holds the contrastive embedding reward $\alpha=0$ and replaces it with random noise to bound how much of the gain comes from the reward shaping vs. the encoder as a state representation.

---

## Novel Insights

The framing of contrastive pre-training augmentations (subtree masking, edge rewiring, identifier shuffling) as semantics-preserving positive pairs specifically tailored to refactoring invariances is a genuinely useful conceptual contribution, distinguishing this from generic code contrastive learning. The idea of using embedding-space distance from high-reward prototype states to bias exploration (Eq. 6) is also interesting in principle, though it lacks empirical validation of its actual effect.

---

## Suggestions

- Resolve the Eq. (5)/Eq. (8) inconsistency by specifying one definition and re-deriving the gradient accordingly.
- Include error bars or at least repeat experiments across 3 seeds to support the main results table.
- Add an ablation where the embedding dynamics reward term ($\alpha = 0$) is removed to isolate whether it helps or is a distractor; report the degenerate-action rate.
- Define the action space explicitly and state whether it is discrete or continuous.

---

## Score and Decision

The paper proposes a plausible idea but is let down by a reward term whose validity is not established, a clear internal inconsistency in its core semantic preservation formulation, an undefined action space, results presented without statistical rigor, and cross-language findings that partially contradict the stated claims. These are not surface issues — they concern whether the reward function and evaluation are internally consistent and whether the claimed improvements can be trusted. The contribution does not meet the bar for ICLR acceptance in its current form.

MY FINAL SCORE: <score>3</score>
MY FINAL DECISION: <decision>Reject</decision>
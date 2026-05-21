Now I have all the calibration data I need. Let me synthesize the final review.

**Round 1 Bracket:** Based on comparison with anchors, this paper sits between ~4.5 and ~6.0. It's clearly stronger than "Compositional World Models" (3.00) which had incomplete formalization and missing baselines, and weaker than "Discovering modular solutions that generalize compositionally" (6.50) which had theoretical contributions plus experiments.

**Round 2 Narrowing:** Within the 4-6 range, the paper compares as follows:
- vs. "Permutation Invariant Learning with High-Dimensional Particle Filters" (5.50): that paper has theoretical results; ours is less theoretical → ours is below this
- vs. "On Provable Length and Compositional Generalization" (5.25): theoretical paper with idealized setting; ours is more empirical but narrower scope → comparable, slightly below
- vs. "MeMo" (4.75): modular controllers, robotics sim; ours has more principled methodology → ours is slightly above
- vs. "Compositional Interfaces" (4.75): modular architecture, synthetic; ours has better ablations and probabilistic framework → ours is above

**Final score: 5.0** — a well-executed proof-of-concept with systematic ablations and a principled framework, held back by synthetic-only scope and simple compositional structure.

---

## Summary

This paper proposes a compositional meta-learning framework that learns a probabilistic generative model of tasks by decomposing them into reusable module RNNs (capturing within-module dynamics) and a gating RNN (capturing between-module sequential statistics). New tasks are solved via particle-filter-based probabilistic inference rather than parameter updates. The model is demonstrated on two synthetic domains — rule learning (shift operations) and motor learning (composite trajectories) — where it recovers ground-truth module operations and transition statistics, performs one-shot inference on held-out tasks, and maintains accurate hypotheses under sparse feedback through constrained hypothesis testing.

## Strengths

- **Principled architecture with clear separation of concerns.** The decomposition into module RNNs and a gating RNN maps cleanly onto the within-module / between-module distinction, formalized as a probabilistic generative model (Eqs. 1-4, Figure 1b). This is well-motivated and clearly presented.

- **Accurate recovery of ground-truth structure.** The learned modules precisely mirror the true shift operations (Figure 2b) and the gating RNN captures non-Markovian transition statistics that a standard HMM could not (Figure 2c). The same holds in the motor domain (Figure 4b-c). This validates that the training procedure works as intended.

- **Systematic and informative ablations.** The flat-transitions control (Figure 3c vs 3d) cleanly isolates the gating network's contribution to sparse-feedback robustness. RNN baselines with and without task identity (Figure 3a-b) contextualize why the architecture matters. The comparison to gradient-based meta-learning (MAML, MLDG) in Figure 3e-f demonstrates the qualitative speed advantage of inference over parameter updates.

- **Compelling sparse-feedback behavior.** The posterior dynamics under sparse feedback (Figure 2e, 4e) — where hypotheses branch at learned switch points and collapse upon feedback — provide a vivid demonstration of how the learned grammar constrains inference. This is the paper's strongest empirical result.

- **Length extrapolation without retraining.** The model generalizes to tasks 4× longer than training examples (Figure 2f, 3f), showing the grammar captures length-independent structure.

## Weaknesses

### Fatal

None.

### Major

- **Missing comparison to non-modular amortized inference baselines.** The paper frames its contribution as solving tasks "without parameter updates" and contrasts against gradient-based meta-learning (MAML, MLDG). However, a family of amortized inference methods (conditional neural processes, variational latent-variable RNNs, Bayesian meta-learning with inferred task embeddings) also solve new tasks without gradient steps. The flat-transitions ablation (Figure 3c) partially addresses this by showing the gating structure matters, but a comparison to a non-modular RNN with the same particle-filter inference machinery would isolate whether the gains come from modularity, the learned grammar, or amortized inference itself. Without this, the claimed advantage of the specific architecture over inference-only alternatives is not fully established.

- **Limited compositional complexity in the evaluation tasks.** The task grammar is highly constrained: each module repeats a fixed, predetermined number of timesteps (3, 4, or 5), and tasks always concatenate exactly three modules. The gating RNN essentially learns a deterministic repetition counter with fixed transition points. There are no stochastic transitions, no variable-length modules, no hierarchical nesting, and no interpolation to unseen module durations. While the paper acknowledges this as "proof-of-principle" (line 184), the gap between these demonstrations and the paper's framing around "learning a grammar" and "compositional meta-learning" is substantial. The length-extrapolation result (Figure 2f) is the most compelling evidence for generalization, but even this relies on the same rigid template with more repetitions.

- **Narrow experimental scope.** Both domains are synthetic and low-dimensional. There is no investigation of: sensitivity to particle count K, behavior under module count mismatch (beyond the brief Figure A1), robustness when the true modular structure deviates from the model's inductive bias, or scaling to more than 6 modules. The paper acknowledges these limitations but does not mitigate them.

### Minor

- **Gradient flow through the particle filter resampling is not specified in the main text.** The loss in Eq. 8 is computed from pre-resampling likelihoods, which avoids the need to backpropagate through the categorical resampling in Eq. 6. However, whether and how gradients flow through the resampling step for the particle propagation (affecting subsequent timesteps' losses) is not discussed. The stripped appendix may contain these details; a brief clarification in the main text would improve reproducibility.

- **The number of modules N is predefined and fixed.** The paper acknowledges this (line 185) and discusses continual learning as a future direction, but it means the model currently requires knowing the true number of operations in advance — a strong assumption for practical use.

- **The framing around "avoiding parameter updates" could be more precisely positioned.** The introduction (lines 27-28) contrasts against gradient-based meta-learning but does not acknowledge the existing body of amortized inference methods that also avoid test-time parameter updates (e.g., Alet et al. 2019 and Hummos et al. 2024 are cited later but not in the introduction's positioning). This makes the claimed novelty appear broader than it is.

### Trivial

None of substance. The paper is well-written and clearly structured.

## Nice-to-Haves

- Stochastic transitions or variable-length modules would more convincingly demonstrate grammar learning.
- An ablation on the number of particles K and its effect on inference quality would be informative.
- Testing on a domain where the modular structure is not perfectly aligned with the model's inductive bias would reveal robustness.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **Harsh critic's claim about gradient flow being a "methodological gap that undermines soundness."** Removed because the marginal likelihood loss in Eq. 8 is computed from pre-resampling likelihoods, so the training loss does not require backpropagation through the resampling step. The Gumbel-softmax is correctly identified for the discrete sampling in Eq. 2. This criticism reflects a misreading of the loss formulation.

2. **Harsh critic's claim that "the test tasks are drawn from exactly the same distribution as the training tasks" with "no novel combination of modules."** Removed as overstated. The paper evaluates on held-out test tasks with different module sequences (Figure 2d, 4d) — these are novel combinations. The grammar structure (fixed repetition counts) is the same, but the specific module orderings in test tasks were not seen during training. The real issue is the simplicity of the grammar, not the absence of novel combination.

3. **Harsh critic's claim that "the gating RNN learns nothing more than a deterministic counter."** Removed as inaccurate. Figure 2c shows the gating RNN has learned history-dependent transition statistics that vary based on how many times a module has been repeated — more nuanced than a simple counter. The non-Markovian nature of the learned transitions (which an HMM could not capture) is a genuine result.

4. **Strength Finder's generic strengths about "important problem" / "interesting question."** Removed as superficial. Only concrete, evidence-backed strengths were retained.

5. **Harsh critic's demand for "a sensitivity analysis of the particle count K and its effect on inference quality and training speed."** Moved to Nice-to-Haves. While valuable, this level of hyperparameter analysis is not standard for proof-of-concept papers in this area.

## Novel Insights

The paper's most interesting insight — visible in the sparse-feedback posterior dynamics (Figures 2e, 4e) — is that the learned gating network functions as a *temporal prior* that constrains hypothesis branching during inference. When feedback is absent, the posterior remains certain about the current module until the learned duration elapses, then becomes uniform — and this switch is driven entirely by the gating RNN's internal state, not by external input. This demonstrates a form of "inference-time compositionality" where the grammar actively shapes which hypotheses are entertained, going beyond simply selecting modules.

## Suggestions

- Add a non-modular amortized inference baseline (e.g., an RNN with the same particle filter but no module decomposition) to isolate the benefit of modularity from the benefit of amortized inference.
- Introduce at least one task variant with stochastic transitions or variable module durations to demonstrate that the gating RNN can learn more than a deterministic counter.
- Briefly clarify in the main text that the training loss (Eq. 8) is computed from pre-resampling likelihoods and therefore does not require backpropagation through the resampling step.

---

### Anchor Comparison Summary

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Compositional World Models (EHmjRIA4l2) | 3.00 | R1 | Our paper is substantially better — clean formalization, systematic ablations, working method |
| Compositional Interfaces (D1w3huGGpu) | 4.75 | R1/R2 | Our paper has stronger methodology and better ablations; comparable synthetic scope |
| MeMo (VZTFUtldbC) | 4.75 | R2 | Our paper has more principled framework; MeMo has more realistic simulation domain |
| When and how are modular networks better? (Olb8JwUGZ3) | 4.25 | R2 | Our paper is stronger in methodology and ablation design |
| How Capable Can a Transformer Become? (tHHzfZSP6T) | 5.00 | R2 | Comparable — both synthetic compositional tasks with systematic experiments |
| On Provable Length and Compositional Generalization (Hxm0hOxph2) | 5.25 | R2 | That paper has theoretical depth; ours has cleaner empirical demonstrations; ours slightly below |
| Permutation Invariant Learning with High-Dimensional Particle Filters (6XodKiDS3B) | 5.50 | R2 | That paper has theory + benchmark experiments; ours is proof-of-concept only |
| Latent Task-Specific Graph Network Simulators (3lDxKQepvn) | 5.75 | R2 | That paper uses established benchmarks; ours is synthetic only |
| Breaking Neural Network Scaling Laws with Modularity (5Qxx5KpFms) | 6.00 | R1 | That paper has theory + CIFAR experiments; clearly stronger |
| Discovering modular solutions that generalize compositionally (H98CVcX1eh) | 6.50 | R1 | That paper has theory + experiments; clearly stronger |

Round 1 bracket: 4.5 – 6.0. Round 2 narrowed to 4.75 – 5.50. The paper is closest in quality to "How Capable Can a Transformer Become?" (5.00) and slightly below "On Provable Length and Compositional Generalization" (5.25). Final score: **5.0**.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
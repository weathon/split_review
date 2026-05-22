Now I have all the calibration data I need. Let me write the final consolidated review.

---

## Summary

This paper proposes a compositional meta-learning framework that formalizes solving new tasks as probabilistic inference in a learned generative model. The architecture separates between-module dynamics (a gating RNN) from within-module dynamics (module RNNs), trained jointly by maximizing marginal likelihood via particle filtering. At test time, new tasks are solved purely by inferring the module sequence through particle filtering, without any parameter updates. Experiments on synthetic rule-learning and motor-learning tasks demonstrate recovery of ground-truth components, one-shot inference under full and sparse feedback, and generalization to longer test tasks.

## Strengths

- **Principled reformulation of meta-learning as inference.** The paper casts compositional meta-learning as inference in a learned probabilistic generative model. This is a genuinely different approach from the dominant gradient-based paradigm (MAML, Reptile, etc.) and is well-motivated. The particle filtering framework for both training (marginal likelihood) and test-time inference is clean and principled.

- **Empirical demonstration of sparse-feedback inference through learned non-Markovian constraints.** The model recovers the correct module sequence from a single episode even when output feedback is available at only a minority of timesteps (Figure 2e, Figure 4e). This works because the gating RNN learns the exact durations of each module, enabling the particle filter to maintain and collapse hypotheses in the absence of feedback. The control experiment showing that the same architecture without the gating RNN (uniform transitions) fails under sparse feedback (Figure 3c) cleanly validates this claimed mechanism.

- **Exact recovery of ground-truth components and statistics.** In the rule-learning domain, module RNNs learn shift operations that perfectly match ground truth (Figure 2b), and the gating RNN learns history-dependent transition matrices that capture the precise non-Markovian repetition counts (Figure 2c). This verifies that the model actually identifies the intended modular structure rather than just fitting the data.

- **Generalization to tasks longer than training.** The model infers correct solutions for test tasks four times longer than training tasks (Figure 2f) without any degradation, and does so even under sparse feedback. This is a strong indicator that the gating RNN has learned the general sequencing grammar rather than memorizing training-length patterns.

## Weaknesses

### Major

- **Missing direct comparison to the most closely related prior work (Alet et al., 2019).** The paper explicitly states (line 440) that the method "effectively replace[s] [Alet et al.'s] search by probabilistic inference on learned structure, greatly improving sample efficiency," yet provides no empirical comparison to Alet et al. on the same tasks. Since Alet et al.'s method also avoids parameter updates at test time (by fixing module parameters and searching configurations), it is the natural baseline for evaluating the claimed advantage of probabilistic inference. The absence of this comparison is a significant evidential gap for one of the paper's central claims.

- **Evaluation is limited to synthetic, low-dimensional tasks with known ground-truth structure.** Both the rule-learning and motor-learning domains are synthetic, low-dimensional, and hand-designed so that the ground-truth modules are known and the number of modules matches the number of ground-truth operations. The motor-learning domain (Section 2.4) is further structurally identical to the rule-learning domain (same skill durations, same transition structure), differing mainly in input dependence. While the paper acknowledges this as a proof-of-principle, it limits the force of claims about "domain generality" and leaves open whether the approach scales to high-dimensional or real-world tasks where modules are not predefined.

### Minor

- **The comparison to MAML/MLDG (Figures 3e,f) is informative but asymmetric.** The paper correctly notes that gradient-based meta-learning methods require hundreds of episodes while the proposed method works in one episode. However, this comparison pits a method with a fully pre-trained generative model + inference against methods that must adapt weights through gradient descent. The key insight—that learned transition statistics can dramatically constrain the search space at test time—is real, but the framing overstates the speed advantage relative to methods designed for a different regime. A more clearly scoped comparison (e.g., "our method trades pre-training for fast inference; gradient-based methods trade more test-time computation for less constrained pre-training") would be more accurate.

- **The extended-task experiment (Figure 2f) conflates two confounds.** The demonstration of 4×-length generalization is done under sparse feedback. While Figure 3f separately shows 2×-length generalization under full feedback (providing partial evidence that length generalization does not require sparsity), the absence of a 4×-length full-feedback ablation makes it unclear whether the sparse-feedback condition is crucial for the extreme length generalization or incidental.

- **The number of modules is set equal to the number of ground-truth operations in the main experiments.** The appendix (Figure A1) explores mismatch, which is good, but the core results rely on oracle knowledge of the module count. The paper acknowledges this as a limitation (line 460), but it nonetheless softens the "discovery" narrative—the model is partially guided by the correct architectural capacity.

### Trivial

- The motor learning section references "Figure 4c" in a way that text says "analogous to Figure 4c" (line 145) but should refer to the previous figure's panel numbering.
- The paper uses "learning" vs. "inference" as a crisp dichotomy throughout, but the training procedure itself involves gradient-based learning of the generative model—this framing, while useful rhetorically, can confuse readers.

## Nice-to-Haves

- A sweep over particle count K showing inference accuracy vs. K for different levels of feedback sparsity would provide practical guidance about the robustness of the inference mechanism.
- A failure analysis: the paper does not discuss when inference fails (e.g., out-of-distribution task combinations, near-sparse feedback that misleads the posterior). Including such examples would strengthen the empirical analysis.
- The motor-learning domain is structurally very similar to the rule-learning domain; a genuinely different domain (e.g., continuous control with learned skills, or language-like composition) would better demonstrate domain generality.

## Removed Points

These points were raised in the reviews but are removed for the reasons stated:

- **"Unfair comparison to MAML/MLDG"** — The comparison is not unfair; it compares methods on the same tasks and shows a qualitative difference in the required number of episodes. The asymmetry is inherent to the different approaches (inference vs. gradient adaptation) and is the point of the comparison. However, the framing has been downgraded to a Minor weakness as noted above.

- **Criticisms about missing hyperparameters, reproducibility details, or appendix content** — The paper provides a reproducibility statement and code. The appendix (which was stripped by the parser) contains implementation details. These are standard for the field and not valid criticisms of the submission as it exists.

- **"Particle filter hyperparameters only in appendix"** — The paper explicitly states this is in the appendix and provides the full codebase. This is standard practice.

- **"The motor task is structurally identical to rule learning"** — While structurally similar, the paper explicitly acknowledges this and explains the practical differences (no input, module state reset, module-specific parameters). Downgraded to Nice-to-Have.

## Novel Insights

The most interesting observation that emerges across the reviews is not captured by the paper's own framing: the gating RNN learns exact duration counts for each module, which effectively turns the particle filter's search into a near-deterministic tracking problem under sparse feedback. The posterior collapses deterministically for a learned number of timesteps and only then opens up to uniform hypotheses. This interaction between learned non-Markovian structure and particle-filter inference is subtler and more interesting than the paper's "inference vs. learning" headline suggests—it reveals that the model is doing something closer to learned program execution with temporal constraints than Bayesian model averaging in the usual sense.

## Suggestions

1. **Add a direct comparison with Alet et al. (2019)** on the same synthetic tasks, measuring the number of episodes needed to reach correct task inference. This would directly validate the claimed improvement in sample efficiency and is the most impactful addition the authors could make.

2. **Disentangle the extended-task ablation:** add a version of the 4×-length experiment under full feedback to isolate whether the length generalization depends on sparse feedback or is a property of the gating RNN alone.

3. **Discuss and ideally quantify when inference fails.** The paper notes (Figure A1e) that out-of-distribution data produces low episode likelihood, but does not characterize the boundary of the in-distribution regime or provide examples of incorrect inference.

4. **Add a brief scaling discussion** (theoretical or empirical) about how the approach scales with task length, number of modules, and number of particles—this would strengthen the practical relevance of the proof-of-concept.

## Score and Decision

**Round 1 bracket (bracketing pass):** Weak anchors for topically similar papers cluster at ~3.0 (rejected papers with limited novelty or clarity). Middle-range anchors cluster at ~6.0–6.5 (modular compositional learning papers, accepted with concerns). Strong anchors cluster at ~7.5–8.0 (more comprehensive evaluations or theoretical treatments). The plausible range for this paper is between 4.0 and 7.0.

**Round 2 narrowing (comparison anchors):**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| H98CVcX1eh — "Discovering modular solutions that generalize compositionally" | 6.50 | R1 middle | Similar topic (modular compositional learning). That paper has theoretical analysis but weaker clarity; this paper has cleaner experiments and a novel inference-based framing but no theory. Comparable quality. |
| 5Qxx5KpFms — "Breaking Neural Network Scaling Laws with Modularity" | 6.00 | R1 middle | Theory + experiments on modularity. This paper has stronger empirical demonstration of modular recovery but narrower task scope. Slightly higher overall. |
| D1w3huGGpu — "Compositional Interfaces for Compositional Generalization" | 4.75 | R1 middle | Rejected for limited novelty and synthetic-only evaluation. This paper has clearer novelty (inference-based framework vs. modular architecture application). Clearly stronger. |
| MVe2dnWPCu — "A Probabilistic Framework for Modular Continual Learning" | 7.50 | R2 high | Stronger empirical evaluation across multiple benchmarks. This paper is weaker in evaluation breadth. |
| 6XodKiDS3B — "Permutation Invariant Learning with High-Dimensional Particle Filters" | 5.50 | R2 low | Particle filter paper with mixed reviews and theoretical concerns. This paper is cleaner and better formulated. |

The paper is closest in quality to the ~6.0–6.5 anchors. It is clearly stronger than the rejected papers (~4.75) and the mixed-review particle filter paper (5.50). It is not as strong as the 7.50 anchor, which has more comprehensive evaluation across multiple benchmarks. The main weakness (missing Alet comparison) is significant but addressable and does not undermine the core novel framework. Final score: 6.0.

**Final score:** 6.0 — A solid paper with a genuine novel contribution (inference-based compositional meta-learning) that is well-executed on synthetic tasks. The missing comparison to the most closely related prior work and the synthetic-only evaluation are notable but addressable weaknesses that do not invalidate the core contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
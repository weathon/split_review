Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper proposes SEED, an exemplar-free class-incremental learning method using a fixed-size ensemble of experts that share initial layers. The central idea is to train only one expert per task (selected via maximum KL divergence between new-class distributions in each expert's latent space) rather than updating all experts. This promotes diversity, mitigates forgetting, and enables task-agnostic inference via an ensemble of Bayes classifiers using multivariate Gaussian class representations. SEED achieves large margins over prior exemplar-free methods (e.g., +15.4 pp on CIFAR-100 T=10, +11.5 pp on DomainNet T=12), with consistent improvements across equal-split, large-first-task, and task-incremental settings.

## Strengths

- **State-of-the-art performance in exemplar-free equal-split CIL.** On CIFAR-100 with T=10, SEED achieves 61.7% average incremental accuracy, surpassing the next-best method FeTrIL (46.3%) by a large 15.4 pp margin (Table 1). The advantage grows with more tasks (T=50: 42.6% vs. FeTrIL's 27.0%). These margins convincingly show that SEED maintains high plasticity where methods relying on frozen/regularized backbones fail.

- **Robust to domain shift between tasks.** On DomainNet (T=12), SEED reaches 45.0% vs. FeTrIL's 33.5% (Table 1), demonstrating that the expert selection and diversification strategy generalizes to real-world distribution shifts spanning six domains.

- **Expert selection via KL-max is empirically validated.** Figure 5 shows that the proposed minimum-overlap selection yields higher mean and median accuracy over 10 runs than random, round-robin, or maximum-overlap baselines on CIFAR-100. This directly supports the paper's core design rationale.

- **Ablation study confirms each component is necessary.** Removing multivariate Gaussians drops accuracy from 61.7% to 53.5%; removing covariance drops to 54.1%; removing temperature lowers performance to 59.2% (Table ablation). These ablations isolate the contribution of each design choice.

- **Superior plasticity–stability trade-off.** Figure 6 (left) shows SEED achieves lower intransigence than EWC/LwF while keeping forgetting lower than FeTrIL, a key advantage in the many-task equal-split setting where most methods must sacrifice one axis for the other.

- **Parameter-efficient relative to prior ensemble methods.** In the task-incremental setting, SEED uses 3.2M parameters vs. CoSCL's 4.6M while achieving 86.8% vs. 79.4% on CIFAR-100 20-split (Table 3).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Ambiguous description of the distribution lifecycle for non-selected experts.** During selection (lines 101–108), distributions for new classes are computed for *all* trained experts (k ≤ t). After fine-tuning the selected expert, line 108 states "update distributions of Q_{k̄}" — only the selected expert's distributions are recomputed. For non-selected experts, the distributions computed during selection are retained unchanged (their weights did not change), which is the correct procedure. However, this lifecycle is never stated explicitly, leaving the reader to infer it. A step-by-step algorithmic description (or a single clarifying sentence) would substantially improve reproducibility.

- **Overstated claim of "no computational overhead during training."** Lines 32 and 38 state that SEED "causes no computational overhead" and "does not require more computation than single-model solutions." This is misleading: the expert selection step (line 101) requires forward passes through all trained experts' g_k modules on all new-task data to compute Gaussian distributions and pairwise KL divergences. While this cost is smaller than backpropagating through a full model, it is real overhead relative to training a single model. The claim should be qualified (e.g., "no overhead in gradient computation" or "negligible overhead from forward passes") and ideally quantified.

- **Selection strategy noise under small-sample regimes is not discussed.** For T=50 on CIFAR-100, each task has only ~2 classes with ~100 samples each. Covariance estimates from such small data in a moderate-dimensional latent space can be noisy, yet the paper does not discuss when the KL-max criterion might degrade. A brief analysis or practical guideline would strengthen empirical rigor.

### Trivial
- The latent space dimension S is mentioned only in passing (line 86) and in the limitations (line 342), with no guidance on how it interacts with the number of classes per task. Given that singular covariance matrices are addressed by reducing S, a practical recommendation would be helpful.

## Nice-to-Haves
- A quantitative breakdown of the computational cost of the selection step (number of forward passes, wall-clock time vs. single-model training).
- Discussion of how often individual experts are re-selected across tasks and whether knowledge distillation (L_KD) sufficiently mitigates forgetting in that case.
- A note on how the latent space dimension S should be set relative to the class count per task.

## Removed Points
- *Criticism about missing appendix / supplementary material* — The paper states code is in the supplementary material; parser-stripped sections are not author omissions.
- *Generic "missing related work" concern* — Not verifiable without external sources.
- *Formatting/style nitpicks* — These are parser artifacts, not author errors.

## Novel Insights
The key structural insight emerging from this review is that SEED decouples the *training cost* from the *model capacity* in ensemble-based continual learning: by training only one expert per task but keeping all experts at inference, the method achieves a rare combination of high plasticity (each new task gets a dedicated update) and high stability (most parameters remain unchanged). This contrasts with prior ensemble methods like CoSCL where all experts are updated at every task — a design that limits plasticity through regularization. The KL-max selection criterion operationalizes a "minimal disruption" principle that is novel in the CL ensemble literature.

## Suggestions
1. Add a pseudocode or algorithmic box in Section 3 that explicitly states: (a) during selection, compute distributions for all trained experts; (b) after fine-tuning the chosen expert, recompute only its distributions; (c) non-selected experts retain the distributions computed in step (a) because their weights are unchanged.
2. Qualify the "no computational overhead" claim to reflect the forward-pass cost of selection, or replace it with "negligible overhead" / "no overhead in gradient computation."
3. Add a brief discussion of when the KL-max selection might be unreliable (e.g., very few samples per class, high latent dimension relative to class count) and how practitioners should set S.

## Score and Decision

This is a strong paper. The core idea is novel and well-motivated, the experiments are extensive and cover multiple challenging settings, the ablations convincingly isolate each component's contribution, and the gains over prior work are large and consistent. The weaknesses are limited to presentation clarity and a slightly overstated efficiency claim — neither undermines the central contribution. I recommend acceptance.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
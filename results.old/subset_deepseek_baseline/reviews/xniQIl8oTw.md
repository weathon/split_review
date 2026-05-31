## Summary

The paper proposes COREctifier, a new learning paradigm for neural combinatorial optimization (NCO) that interleaves reinforcement learning with hierarchical expert guidance. During RL training, partial segments of policy-generated trajectories are probabilistically replaced by high-quality segments from reference solutions, with control at batch, instance, and intra-instance levels. The approach aims to mitigate reward sparsity and sample inefficiency that plague standard RL for CO, while maintaining the sequential decision-making advantage of RL for enforcing complex constraints. Extensive experiments on TSP, ATSP, PCTSP, CVRP, and KP, including scalability up to 500 nodes and generalization to real-world benchmarks, show consistent and often substantial improvements over both RL-based and SL-based baselines.

## Strengths

- **Novel hybrid learning framework**: The paper introduces a principled way to combine supervised/imitation learning with RL for CO by injecting expert segments at multiple granularities, rather than using full expert trajectories or static heatmaps. This addresses a known limitation of pure RL methods (reward sparsity, poor exploration) while retaining flexibility for constraint satisfaction.

- **Extensive and thorough empirical evaluation**: The paper covers 5 diverse CO problems (TSP, ATSP, PCTSP, CVRP, KP) across multiple scales (up to 500 nodes), comparing against a wide range of RL, SL, UL, and classical baselines. It includes ablation studies, hyperparameter sensitivity analysis, generalization to real-world benchmarks (TSPLIB, CVRPLIB), and diversity/entropy analyses that convincingly demonstrate the effectiveness of the proposed components.

- **Consistent and significant performance gains**: In almost all settings, COREctifier reduces the optimality gap compared to standard RL methods (e.g., 47–60% relative improvement on TSP, ATSP, PCTSP, CVRP). Notably, it achieves substantially better scalability (e.g., 89.8% gap reduction on TSP-500) and strong generalization, which are well-documented bottlenecks for RL4CO.

- **General applicability as a plug-in mechanism**: The method is shown to work with multiple backbone architectures (POMO, AM, MatNet) and across different problem types (routing, assignment-type tasks like ATSP, non-routing like KP), validating its broad utility.

## Weaknesses

### Fatal
None.

### Major

- **Theoretical soundness of the gradient estimator is not addressed**: The policy gradient (Eq. 11–12) uses log-probabilities of rectified actions that may not have been sampled from the current policy. In standard policy gradient methods, the actions used in the gradient update must be sampled from the policy to obtain an unbiased estimate of the gradient. Using forced expert actions without any importance weighting or correction can introduce bias. The paper presents this as a straightforward REINFORCE extension but does not discuss why the estimator remains valid (or whether it is a surrogate objective). This is a nontrivial issue that needs justification, either theoretical or empirical (e.g., showing that the gradient direction correlates with the true objective). Without it, the mathematical foundation of the method is incomplete.

- **Lack of clarity on when and how the two-stage training is applied**: The paper mentions that Stage 1 (IL pre-training) is “optional” and that rectifiers start “once overfitting is observed in the IL phase.” No details are given on how overfitting is detected, what threshold is used, or whether this choice significantly impacts performance. The ablation shows that IL pre-training helps on TSP and ATSP but not PCTSP, suggesting the two-stage pipeline requires careful tuning per task. This undermines the generality of the reported results.

- **Comparison to SL/heatmap methods is informative but not entirely fair**: The paper claims superiority over SL-based solvers (e.g., 26.5% gain on TSP), but these methods rely on heatmap + separate decoder, often trained with different backbones and loss functions. The comparison is one-sided: COREctifier uses the same base architecture as RL methods while SL methods are constrained to heatmap prediction. The paper acknowledges this but still presents the comparison as a core strength. A more controlled comparison (e.g., using the same transformer architecture for SL policy) would strengthen the claims.

### Minor

- **Hyperparameter sensitivity is incompletely explored**: The paper tests only a few values for \(p_{\text{batch}}\), \(p_{\text{inst}}\), and \((\alpha,\beta)\), and only on two problems. The optimal setting likely depends on problem size and label quality. The cosine annealing schedule is introduced but not ablated against static values. The paper’s conclusion that the method is “stable” is based on a narrow range.

- **The “tri-level” contribution is overstated**: The hierarchical design (batch, instance, intra-instance) is essentially three hyperparameters with independent sampling. While convenient, it is not a fundamental architectural innovation. The core idea is segment-level replacement, which could be described more succinctly.

### Trivial
None.

## Nice-to-Haves

- Would strengthen the paper to include an analysis or discussion of the gradient bias/variance trade-off introduced by action replacement. Experiments comparing the proposed estimator to a corrected version (e.g., with importance sampling) would be illuminating.
- Providing convergence curves for larger problems (e.g., TSP-500) would help assess training stability.
- Reporting variance across multiple training runs (not just evaluation) would give a better picture of reliability.

## Novel Insights

Beyond the paper’s own contributions, the most interesting observation is that injecting *segments* of expert trajectories (rather than full trajectories or heatmap targets) into RL training can simultaneously improve exploration and maintain constraint satisfaction. This suggests that the combinatorial action space of CO problems has a structure where local optimality is transferable, and that the key difficulty for RL is not just the scale but the sparsity of meaningful reward signals. The paper’s empirical finding that even a small fraction (10%) of rectified trajectories is effective (and that higher fractions can hurt) indicates that expert guidance serves as a gentle regularizer rather than a hard constraint. This nuance could inform future hybrid methods.

## Suggestions

1. Provide a formal or informal justification for why the gradient estimator in Eq. 11–12 is reasonable (e.g., as an off-policy policy gradient, or as a surrogate objective with bounded bias). Even an empirical validation on a small problem (e.g., comparing against a corrected gradient) would greatly increase confidence.
2. Clarify the two-stage training protocol: how overfitting is detected, how many IL epochs are used, and whether the performance is sensitive to this threshold. Consider reporting results without IL pre-training for all tasks.
3. Expand hyperparameter ablation to include more values and at least two different problem sizes to demonstrate robustness.
4. In the main results tables, include variance across test instances (already partially provided) and also note whether results are averaged over multiple training seeds.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
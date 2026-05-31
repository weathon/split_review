## Summary

This paper proposes replacing the standard softmax parameterization for categorical random variables with a hierarchical binary decomposition called "catnat" that yields a diagonal Fisher Information Matrix. The authors provide theoretical analysis showing that softmax produces a dense FIM with geometric distortions, while catnat's hierarchical structure naturally diagonalizes the FIM, creating a flatter optimization landscape more amenable to gradient descent. Empirical evaluations across graph structure learning, variational autoencoders, and reinforcement learning demonstrate consistent improvements over softmax, with the natural activation function variant performing best in most settings.

## Strengths

- **Strong theoretical foundation**: The paper provides rigorous information-geometric analysis, proving that softmax yields a dense Fisher Information Matrix (Proposition 4.1) while catnat produces a diagonal FIM (Theorem 4.2), with clear proofs in the appendices. This theoretical grounding distinguishes the work from purely empirical approaches.

- **Broad empirical validation**: The method is evaluated across three fundamentally different domains (graph structure learning, VAEs, reinforcement learning) with different gradient estimators (score function with LOO baseline, Gumbel-Softmax, PPO), demonstrating generalizability. The GSL experiments are particularly thorough, testing across five different entropy settings with multiple metrics.

- **Practical simplicity**: The catnat parameterization is straightforward to implement and can be dropped into existing codebases as a direct replacement for softmax, requiring no changes to training pipelines, gradient estimators, or other components. This lowers the barrier to adoption.

- **Consistent improvements**: Across all experimental settings, catnat matches or outperforms softmax, with particularly striking gains in the GSL experiments where MAE on θ is reduced by factors of 2-3× in high-entropy settings.

## Weaknesses

### Fatal
None.

### Major

- **Limited analysis of the natural activation function's practical behavior**: The natural activation ν(x) uses a sinusoidal transition region that is non-monotonic in its derivative and has zero gradient outside the interval [C-A/2, C+A/2]. This could cause vanishing gradient problems when scores fall outside this range, yet the paper does not analyze how often this occurs in practice, how to set A adaptively, or whether the sigmoid variant might be more robust despite not achieving the idealized diagonal FIM. The VAE results show catnat with sigmoid and natural activation are statistically equivalent, suggesting the theoretical advantage of ν may not translate to practice.

- **Missing comparison with alternative parameterizations**: The paper only compares catnat against softmax, but there exist other parameterizations for categorical distributions (e.g., stick-breaking, softmax with temperature annealing, or using the natural parameters of the categorical distribution directly). Without these baselines, it's unclear whether the improvements come specifically from the diagonal FIM property or simply from using a hierarchical decomposition.

- **Reinforcement learning experiments are underpowered**: The RL results show high variance (standard deviations of 25-533) and modest improvements (406 vs 398 for Breakout, 2164 vs 1875 for Seaquest). The paper acknowledges the computational burden prevented exhaustive hyperparameter search, but the results are not statistically compelling. The Seaquest improvement is within one standard deviation, and the Breakout improvement is marginal. Stronger evidence (e.g., learning curves, multiple environment comparisons, or statistical significance tests) would strengthen the claims.

### Minor

- **The GSL experiments only test K=2 (Bernoulli) case**: Since catnat's theoretical advantages grow with K (the FIM becomes increasingly dense for softmax as K increases), testing only binary variables in GSL does not showcase the method's potential benefits for larger K. The VAE experiments do test larger K, which partially addresses this.

- **The paper claims catnat is "compatible with standard training stabilization techniques" but provides no experiments demonstrating this compatibility**: For example, does catnat work well with gradient clipping, learning rate schedules, or weight decay? Are there any interactions?

### Trivial
None.

## Nice-to-Haves

- An ablation study varying the depth of the hierarchical tree (e.g., using ternary or higher-order splits instead of binary) to understand whether the binary structure is optimal or merely sufficient.
- Analysis of training dynamics (e.g., gradient norms, loss curves) comparing softmax vs catnat to provide intuition about why catnat converges to better solutions.
- Investigation of whether catnat's benefits persist when using natural gradient methods directly (since catnat already approximates some benefits of natural gradient).

## Novel Insights

The key insight is that the softmax function's dense Fisher Information Matrix creates coupling between all parameters, meaning gradient updates in one parameter inadvertently affect the geometry in other directions. By decomposing the categorical distribution into hierarchical binary decisions, catnat decouples these interactions, resulting in a diagonal FIM. This is conceptually elegant because it achieves the benefits of natural gradient preconditioning (flattening the statistical manifold) without the computational cost of computing and inverting the FIM. The paper also makes the subtle observation that the activation function choice matters: the natural activation ν(x) further simplifies the FIM by making the diagonal entries independent of the local score, though in practice the sigmoid variant performs similarly.

## Suggestions

1. Add comparisons with at least one alternative parameterization (e.g., stick-breaking representation or softmax with learned temperature) to isolate whether the benefits come from the hierarchical structure or specifically from the diagonal FIM property.

2. For the RL experiments, include learning curves (episodic return vs. training steps) to show whether catnat converges faster, to higher asymptotic performance, or both. Also consider reporting interquartile ranges or confidence intervals given the high variance.

3. Discuss practical considerations for the natural activation function: how to set A and C, what happens when scores fall outside the linear region, and whether adaptive schemes could be beneficial.

4. Consider adding a small-scale experiment (e.g., synthetic classification with varying K) to directly demonstrate the relationship between K and the performance gap between softmax and catnat, validating the theoretical prediction that catnat's advantages grow with K.

## Score and Decision

The paper makes a solid theoretical contribution by identifying and addressing a fundamental limitation of softmax from an information-geometric perspective, and provides reasonable empirical support across diverse domains. The main limitations are the lack of comparison with alternative parameterizations and the underpowered RL experiments. However, the theoretical analysis is sound)Skip, the method is practically useful, and the core claims are well-supported.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>
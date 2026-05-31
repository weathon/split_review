## Summary

This paper proposes replacing the standard softmax parameterization of categorical distributions with a novel hierarchical binary parameterization called "catnat" that yields a diagonal Fisher Information Matrix. The authors argue from an information-geometric perspective that the dense FIM of softmax creates geometric distortions hindering gradient descent, while their proposed approach flattens the statistical manifold. Through experiments in graph structure learning, variational autoencoders, and reinforcement learning, they demonstrate that catnat consistently matches or outperforms softmax across diverse settings.

## Strengths

- **Novel information-geometric perspective**: The paper provides a principled theoretical justification for replacing softmax, grounding the proposal in Fisher Information Matrix analysis and natural gradient concepts. This is a genuinely new angle on a long-standing problem.
- **Clear theoretical contribution**: Theorem 4.2 rigorously proves that the hierarchical binary parameterization yields a diagonal FIM, and Corollary 4.3 shows that with the proposed natural activation function, the diagonal entries become particularly simple. The proofs are provided in appendices.
- **Broad experimental validation**: The method is tested across three fundamentally different domains (GSL, VAE, RL) with diverse gradient estimators (REINFORCE with baseline, Gumbel-Softmax, PPO), demonstrating robustness and general applicability.
- **Practical simplicity**: The catnat parameterization is straightforward to implement and can replace softmax in existing codebases with minimal changes, making adoption easy for practitioners.
- **Consistent empirical improvements**: Across all experiments, catnat variants match or outperform softmax, often with statistically significant gains. The improvements in latent parameter recovery in GSL (Table 2) are particularly compelling.

## Weaknesses

### Fatal

None.

### Major

1. **Limited theoretical depth in explaining why diagonal FIM helps**: While the paper correctly notes that a diagonal FIM is desirable from a natural gradient perspective, it does not formally connect the diagonal FIM property to improved gradient descent dynamics or convergence guarantees. The argument that a diagonal FIM "reduces geometric distortions" and allows the optimizer to "follow a more direct path" is intuitive but not rigorously supported. A more formal treatment (e.g., showing that the optimization landscape becomes better conditioned, or that gradient descent steps track natural gradient directions more closely) would strengthen the paper.

2. **The natural activation function \(\nu(x)\) has support issues**: The function defined in Equation (12) has flat regions where the derivative is zero (for \(|x-C| > A/2\)). This means that once scores move outside the linear region, the gradient of the categorical probabilities with respect to those scores vanishes entirely, which could cause training to stall. The paper does not discuss this potential failure mode or provide theoretical guarantees that scores will remain in the active region during training. This is particularly concerning for RL where policy gradients naturally push probabilities toward 0 or 1.

3. **No comparison with other softmax alternatives**: The paper compares catnat only against standard softmax. There are other parameterizations in the literature (e.g., softmin, sparsemax, various temperature-scaled variants) that could also improve training dynamics. Without comparison to these alternatives, it's unclear whether the benefits come specifically from the diagonal FIM property or from any change away from softmax.

### Minor

1. **RL experiments are limited**: Only two Atari environments were tested, and the performance gains in Breakout are marginal (398 vs 406). The high variance in RL results makes it difficult to assess statistical significance. A more comprehensive RL evaluation with more environments and statistical significance testing would strengthen these claims.

2. **Computational efficiency not discussed**: While catnat replaces softmax with \(O(\log K)\) binary decisions, the paper does not discuss whether this introduces any computational overhead or whether it could be faster/slower than softmax in practice. Given that the method is proposed as a better alternative to softmax, this is a practical consideration.

3. **The "natural" terminology is somewhat overclaimed**: Calling the hierarchical parameterization "natural" based on the diagonal FIM property is somewhat imprecise. In Amari's original work, "natural" refers to the gradient preconditioned by the FIM inverse, not to a parameterization that happens to have a diagonal FIM. While the connection is reasonable, this terminology could be confusing to readers familiar with natural gradient methods.

### Trivial

None of note.

## Nice-to-Haves

- An ablation study comparing catnat with sigmoid vs. catnat with natural activation would help isolate which component of the proposal drives improvements.
- A synthetic experiment with controlled conditions (known ground-truth FIM, known optimal parameters) could more directly validate the claim that diagonal FIM leads to better optimization trajectories.
- Discussion of potential limitations or failure cases of the hierarchical binary parameterization (e.g., when categories have no natural hierarchical structure).

## Novel Insights

The key insight—that parameterizing categorical distributions through hierarchical binary splits yields a diagonal Fisher Information Matrix, while softmax yields a dense one—is genuinely novel and well-articulated. This connects information geometry to a practical architectural choice in a way that is both theoretically grounded and empirically demonstrated. The identification that the FIM diagonal entries depend on ancestor-node visitation probabilities provides a clean characterization of the optimization geometry. The natural activation function is a clever construction that further simplifies the FIM, though its practical benefits over sigmoid are modest in the experiments shown.

## Suggestions

- Address the support issue of the natural activation function: either prove that scores remain in the active region under reasonable training dynamics, or provide a modified activation that maintains the diagonal FIM property while guaranteeing non-zero gradients everywhere.
- Add comparisons with at least one other softmax alternative (e.g., sparsemax or a temperature-scaled softmax) to isolate whether the benefits are specific to the diagonal FIM property or simply from using a different parameterization.
- Include a more rigorous evaluation of the RL experiments: compute confidence intervals via bootstrapping, test on additional environments, and discuss practical training stability.

## Score and Decision

The paper makes a novel theoretical contribution with a practical, easy-to-implement method that consistently outperforms the standard softmax across diverse domains. While the theoretical analysis could be deeper and the RL evidence is limited, the overall strength of the contribution—a principled replacement for a fundamental building block used throughout deep learning—warrants acceptance. The experiments convincingly demonstrate benefits in two out of three domains, and even in RL the results are positive if not definitive.

MY FINAL SCORE: <score>8</score>
MY FINAL DECISION: <decision>Accept</decision>
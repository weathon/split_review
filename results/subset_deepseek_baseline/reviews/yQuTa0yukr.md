## Summary

This paper introduces Transformer-Augmented Parallel Tempering (TAPT), a hybrid algorithm that integrates a learned generative model (IsingFormer) into the Parallel Tempering (PT) framework. The IsingFormer generates full spin configurations as proposals for global moves within PT, which are accepted or rejected via a Metropolis criterion. The authors demonstrate that this generator-verifier approach accelerates both sampling (2D Ising model) and combinatorial optimization (3D spin glasses, integer factorization), with the factorization experiments showing generalization to unseen problem instances.

## Strengths

- **Novel and well-motivated framework**: The generator-verifier architecture that couples a learned neural proposal generator with a principled MCMC verifier is conceptually elegant and addresses a fundamental limitation of both approaches—neural networks lack correctness guarantees, while MCMC gets stuck in local minima. This synthesis is genuinely novel and practically valuable.

- **Strong empirical validation across diverse domains**: The paper demonstrates effectiveness on three distinct problem types (2D Ising sampling, 3D spin glass optimization, integer factorization), showing both sampling quality and optimization performance improvements. The factorization experiments are particularly compelling as they demonstrate generalization across problem instances, which is rare in neural optimization methods.

- **Temperature generalization**: The IsingFormer's ability to interpolate to unseen inverse temperatures (including the critical region) is a significant technical achievement, as it allows a single trained model to provide proposals across the entire temperature ladder without per-temperature retraining.

- **Principled integration with existing methods**: The algorithm is generator-agnostic and can incorporate future advances in generative modeling. The autoregressive architecture provides a path to exact Metropolis-Hastings correction, which is a theoretically sound design choice.

## Weaknesses

### Fatal
None.

### Major

- **Computational cost of training is not properly accounted for**: The paper acknowledges that "transformer training time is not factored into optimization performance" but this is a significant omission. For the 3D spin glass experiment, training a transformer on a single instance and then using it for optimization may not be computationally competitive with simply running longer PT or simulated annealing. The paper would benefit from a wall-clock time comparison or a discussion of when the training cost is amortized.

- **Limited generalization in the spin glass setting**: The authors note that the generator "does not generalize to other instances (its proposals were entirely rejected)" for spin glasses. This is a serious limitation that undermines the practical utility of the approach for many optimization problems. The factorization experiments show generalization, but this relies on the specific structure of the multiplier circuit, which may not extend to arbitrary Ising problems.

- **The acceptance probability in Eq. 2 is not fully justified**: The paper states that the Metropolis criterion in Eq. 2 is "theoretically valid if the transformer samples from the Boltzmann distribution at β_r," but then acknowledges that the learned model is an imperfect approximator. The authors mention that the autoregressive nature enables exact MH correction but do not implement it. This creates a gap between the theoretical guarantees claimed and what is actually implemented. The paper would be stronger with either the MH correction implemented or a more rigorous analysis of the approximation error.

- **Missing ablation studies on key design choices**: The paper does not systematically ablate important hyperparameters such as the number of transformer proposals per cycle, the frequency of proposals vs. local updates, or the number of replicas augmented. Understanding how these choices affect performance would strengthen the practical guidance for using TAPT.

### Minor

- **The 2D Ising experiments, while clean, are somewhat limited in scope**: The model is evaluated on a single system size (50×50) with open boundary conditions. Testing on larger systems or periodic boundary conditions would strengthen the claims about scalability and generalization.

- **The factorization experiments use relatively small problem instances** (8-bit and 16-bit). While the generalization results are promising, it is unclear how the approach scales to practically relevant factorization sizes (e.g., 1024-bit RSA numbers).

- **The paper does not compare against other learned proposal methods**: Given the extensive related work on Boltzmann generators, normalizing flows, and autoregressive samplers, a direct comparison (even on the 2D Ising benchmark) would help contextualize the improvements.

### Trivial
None.

## Nice-to-Haves

- A wall-clock time comparison between TAPT and standard PT, including training time amortized over multiple runs or instances.
- An analysis of the acceptance rate of transformer proposals as a function of temperature and training data quality.
- A discussion of how the approach might scale to larger systems, including computational complexity estimates.

## Novel Insights

The key insight beyond the paper's own contributions is that the generator-verifier framework provides a natural resolution to the tension between learned generative models (which capture global structure but lack guarantees) and MCMC methods (which provide guarantees but mix slowly). This suggests a broader design principle for combining deep learning with classical algorithms: rather than replacing principled methods, neural networks can serve as "proposal engines" that exploit learned structure while leaving correctness guarantees to the verifier. The factorization results further suggest that when problem instances share structural invariances (e.g., the same circuit topology with different clamped outputs), the generator can learn to propose useful configurations across the entire family, amortizing the training cost over many instances.

## Suggestions

- Implement the full Metropolis-Hastings correction using the autoregressive probability computation, or provide a theoretical analysis of the bias introduced by the uncorrected acceptance rule. This would significantly strengthen the theoretical foundations of the work.

- Add a wall-clock time comparison for at least one experiment (e.g., the 3D spin glass) that includes training time, to help practitioners understand the practical trade-offs.

- Include an ablation study varying the number of transformer proposals per cycle and the number of augmented replicas, to provide practical guidance for deploying TAPT.

## Score and Decision

The paper presents a novel and well-executed framework that bridges two important research directions. The empirical results are convincing across multiple domains, and the generalization to unseen factorization instances is particularly noteworthy. The major weaknesses—primarily the lack of wall-clock time accounting and the incomplete theoretical justification of the acceptance rule—are addressable and do not invalidate the core contribution. The paper represents a significant step forward in combining learned generative models with principled MCMC methods.

MY FINAL SCORE: <score>8</score>
MY FINAL DECISION: <decision>Accept</decision>
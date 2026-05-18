- Decision: Accept
- Scores: 8, 6, 6, 6

## Merged Review

### Summary
This paper proposes PRDP (progressively refined differentiable physics), a method to reduce computational cost when training neural networks that include an iterative linear PDE solver in the pipeline. The key idea is that full network accuracy can be achieved with a solver that has not fully converged. The method starts with a coarse (few iterations) solver and adaptively increases the number of solver iterations during training based on plateauing of the validation loss. Two sources of savings are identified: *progressive refinement* (fewer iterations early in training) and *incomplete convergence* (never needing fully converged solver). The method is validated on inverse problems, linear/nonlinear neural emulator learning, and neural-hybrid solvers, with training time reductions up to 62–81% depending on the problem.

### Strengths
- The paper is well-written and clearly explains the intuitions and motivations behind the method.
- The main result—that progressively increasing solver accuracy during end-to-end training converges to the same performance as a fully converged solver while substantially reducing compute—is original.
- The benefit from *incomplete convergence* is very interesting and unexpected; computational experiments show it accounts for most of the savings.
- A notable finding is that unrolled differentiation performs similarly to the more sophisticated implicit differentiation, which is an interesting observation.
- The proposed algorithm is straightforward and effectively delivers the intended results, as seen in validation loss reduction with refinement (notably Figure 4 for 2D Heat and 2D Navier-Stokes).
- Savings in training time and computational resources are substantial (e.g., 81% reported for 2D heat equation; Reviewer 1 notes 72%IC + 14%PR = 86%, though text reports 81%).
- The appendix is thorough and well-organized, providing detailed derivations and information on iterative linear solvers for each problem.
- The topic is interesting: it is intuitive that due to noise and approximation in neural network training, the solver need not fully converge, and the paper provides an adaptive strategy to exploit this.
- The paper is complete, with several experiments that isolate and illustrate the two kinds of cost reduction, along with discussion of impact and limitations.

### Weaknesses
- **Weak baselines**: The primary use case is iterative solvers for large linear systems, yet the experiments use only 1D and 2D examples (heat equation) that could be solved efficiently with direct solvers. A 3D example (e.g., 3D heat equation) is needed to demonstrate where an iterative solver is necessary. More complex linear models (e.g., Helmholtz equation) should also be considered. (Reviewer 1: strong request; Reviewer 2: all solvers rely on iterative linear solvers, would like to see applicability to other physics solvers like explicit time-stepping.)
- **Diminishing savings in harder problems**: The benefit is significantly smaller in the nonlinear neural emulator learning case. A discussion of the potential harmful mechanisms that limit computational savings there is missing. (Reviewer 1: concerning and needs explanation.)
- **Limited technical novelty**: The main contribution is the algorithm for iterative refinements; the overall idea is somewhat incremental. (Reviewer 2: technical contribution limited.)
- **Missing comparison with existing methods**: For the Navier-Stokes neural-hybrid experiment (Section 4.4), the paper does not compare performance or training time against the method of Um et al. or other relevant methods from the related work. Such a comparison is necessary to evaluate the method’s benefits. (Reviewer 4: strong criticism.)
- **Lack of training time reporting**: The paper’s main claim is computation savings, but training times with and without PRDP are not presented. A clear comparison against standard methods is missing. (Reviewer 4: critical omission.)
- **Justification of validation loss metric**: The choice to monitor validation loss for refinement is not fully justified; an ablation study comparing training loss vs. validation loss would strengthen this choice. It is also unclear how the method behaves when validation loss plateaus and then decreases again (common with learning rate schedulers). (Reviewer 4: needs clarification.)
- **Unclear experiment settings**: The role of the neural network in each experiment is not clearly presented. For example, it is unclear where the NN is used in the global framework, what the inner/outer optimization problems are, and what the parameters θ represent. (Reviewer 3: hard to follow; Reviewer 4: needs pseudo code or a scheme.)
- **Lack of background on differentiable physics**: Readers not expert in the field may find the paper hard to follow and may be unaware of the broader context. (Reviewer 3: more background needed.)
- **Simplified examples**: Except for the neural-hybrid example, the other cases are simplified/illustrative without clear concrete applications. The method’s potential on more complex, real-world scenarios (complex boundary conditions, irregular meshes) is not explored. (Reviewer 2: would like to see broader applicability.)
- **Missing analyses** (Reviewers 2 & 4): Sensitivity of PRDP parameters; effect of noise in observations; behavior if physics solver contains incomplete physics; whether savings would hold with larger/ more expressive NNs; comparison of performance w/ and w/o PRDP (difference looks very small in Fig. 1); what happens at inference for new physical systems.
- **Reported savings correction**: Reviewer 1 notes that the reported savings for the 2D heat equation and the maximum in the conclusion are inconsistent (72%IC + 14%PR = 86% but text reports 81%). This should be corrected.
- **Applicability beyond physics**: Reviewer 4 questions whether the method could be applied to any iterative process in the forward pass, but the paper does not discuss this generalization.
- **Incomplete convergence and NN size**: Reviewer 4 wonders if IC savings would be reduced with a more expressive NN (i.e., if the NN could achieve full accuracy without relying on solver inaccuracies). The paper does not test this.
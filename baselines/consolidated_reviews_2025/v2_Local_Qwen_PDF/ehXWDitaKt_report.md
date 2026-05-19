## Summary
# Final Review Report

## Summary
This paper proposes **Newton Losses**, a method for improving the optimization of non-convex, hard-to-optimize algorithmic losses by locally approximating them with a quadratic function using second-order curvature information. The core insight is to split the training loop into two steps: (1) optimizing the loss function directly with respect to its output using Newton's method (or an empirical Fisher approximation) to find a curvature-aware target $z^\star$, and (2) updating the neural network parameters via gradient descent to match this target. The authors evaluate two variants—Hessian-based and empirical Fisher-based—across eight differentiable algorithm methods on MNIST sorting and Warcraft shortest-path benchmarks. Results demonstrate substantial accuracy improvements, particularly for methods suffering from vanishing/exploding gradients, while maintaining computational efficiency and not degrading performance on standard convex losses.

## Strengths
1. **Novel Methodological Insight**: The proposal to apply second-order optimization to the loss function output space rather than the high-dimensional network parameter space is a clever and practically viable adaptation. It successfully bypasses the computational bottlenecks of full Newton methods while retaining curvature benefits.
2. **Broad Empirical Validation**: The method is evaluated across eight differentiable algorithm families (NeuralSort, SoftSort, DSNs, AlgoVision, Stochastic Smoothing, Perturbed Optimizers) on two distinct benchmarks. The consistent improvements, especially for methods prone to gradient instability, strongly support the core claim.
3. **Practical Implementation Variants**: Providing both a Hessian-based variant (for maximum curvature fidelity) and an empirical Fisher-based variant (for ease of implementation and stability) makes the method highly accessible to practitioners working with differentiable algorithms.
4. **Theoretical Grounding**: The inclusion of equivalence lemmas (Appendix D) demonstrating that the split optimization preserves stationary points under certain conditions adds valuable theoretical rigor to the empirical observations.

## Weaknesses
1. **Hyperparameter Sensitivity**: The method introduces a Tikhonov regularization parameter $\lambda$ that heavily influences performance. The current grid search approach is manual and dataset-dependent. Without adaptive scheduling or theoretical bounds for $\lambda$, reproducibility and ease of use are compromised.
2. **High Variance in Certain Settings**: Table 1 shows substantial variance for Logistic DSN (e.g., ±18.04). This suggests that Newton Losses may amplify instability in already fragile relaxations, or that the curvature estimates are noisy. The lack of median reporting or failure-case analysis limits confidence in these specific results.
3. **Unqualified Efficiency Claims**: The abstract and introduction claim computational efficiency, but the Hessian variant can incur significant overhead (up to 2.6× in Appendix B) for complex differentiable algorithms. This claim should be bounded to the Fisher variant or explicitly qualified.
4. **Limited Generalization Evidence**: All experiments are conducted on established algorithmic benchmarks (MNIST sorting, Warcraft shortest-path). There is no evaluation on out-of-distribution shifts or more complex real-world algorithmic tasks, leaving the robustness of the method under distributional shifts unverified.

## Key Issues
1. **Hyperparameter Tuning Burden**: The regularization strength $\lambda$ requires careful manual tuning per algorithm and dataset. The current ablation (Figure 4) shows robustness over orders of magnitude, but the optimal $\lambda$ varies significantly across methods (Table 8). This limits the "drop-in" usability claimed in the introduction.
2. **Variance and Stability Risks**: The high variance observed in Logistic DSN results indicates that curvature approximation can sometimes destabilize training rather than stabilize it. The mechanism behind this variance (e.g., poor Hessian conditioning, relaxation sensitivity) is not analyzed.
3. **Computational Overhead for Hessian Variant**: While the Fisher variant is efficient, the Hessian variant's overhead is non-trivial for complex differentiable algorithms (e.g., AlgoVision Bellman-Ford). The claim of general computational efficiency is misleading without distinguishing between the two variants.

## Actionable Suggestions
1. **Implement Adaptive $\lambda$ Scheduling**: Instead of fixed grid search, propose a simple adaptive rule for $\lambda$ (e.g., based on gradient norm or Hessian condition number) to reduce tuning burden. Even a warm-up schedule would improve practical usability.
2. **Report Median and IQR for High-Variance Cases**: For methods like Logistic DSN where variance is high, report median performance and interquartile range alongside the mean. This provides a more robust summary of typical performance and highlights outlier sensitivity.
3. **Qualify Efficiency Claims**: Revise the abstract and introduction to explicitly state that computational efficiency is guaranteed for the empirical Fisher variant, while the Hessian variant incurs overhead proportional to the cost of second-derivative computation.
4. **Analyze Failure Modes**: Add a short discussion on when Newton Losses might fail (e.g., highly ill-conditioned Hessians, non-smooth relaxations) and how the Tikhonov regularization mitigates or exacerbates these cases.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem)**: Weakly-supervised learning often relies on algorithmic losses that are non-convex and prone to vanishing/exploding gradients, hindering optimization.
- **S2 (Gap)**: Standard first-order optimizers struggle with these complex landscapes, while full second-order methods are computationally prohibitive for neural networks.
- **S3 (Solution)**: We propose Newton Losses, which locally approximates the loss function with a quadratic using second-order curvature information, decoupling loss optimization from network training.
- **S4 (Method)**: By splitting training into a curvature-aware target generation step and a gradient descent matching step, we provide Hessian and empirical Fisher variants that are efficient and easy to integrate.
- **S5 (Result)**: Evaluated on eight differentiable algorithm methods across sorting and shortest-path benchmarks, Newton Losses substantially improves accuracy for hard-to-optimize losses without degrading performance on convex objectives.

### Introduction Outline (Complete)
- **P1 (Motivation)**: Contrast convex losses with algorithmic losses; highlight optimization difficulties (non-convexity, gradient instability) in weakly-supervised settings.
- **P2 (Prior Work & Limitations)**: Discuss second-order optimization benefits but note their prohibitive cost and generalization risks when applied to high-dimensional network parameters.
- **P3 (Core Insight)**: Introduce the key idea: loss functions operate in lower-dimensional output spaces, making second-order approximation tractable. Propose the split optimization framework.
- **P4 (Method Overview)**: Briefly describe Newton Losses, the two-step update rule, and the Hessian/Fisher variants.
- **P5 (Contributions)**: Summarize theoretical grounding, empirical validation across multiple benchmarks, and practical implementation benefits.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0** | Qualify efficiency claims in Abstract/Intro to distinguish Fisher vs Hessian variants. | Improves scientific accuracy and prevents reviewer pushback on overhead. | Low |
| **P0** | Address high variance in Logistic DSN results (report median/IQR, discuss causes). | Strengthens statistical reliability and robustness claims. | Low |
| **P1** | Add adaptive $\lambda$ scheduling or theoretical bounds for regularization strength. | Reduces hyperparameter tuning burden and improves usability. | Medium |
| **P1** | Expand Conclusion with explicit limitations and concrete future work directions. | Enhances scientific rigor and transparency. | Low |
| **P2** | Include out-of-distribution or noise-perturbation robustness tests. | Validates generalization beyond IID benchmarks. | High |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | Newton Losses improves ranking supervision | MNIST sorting (n=5,10), 4 sorting methods | % correct rankings/ranks | Substantial gains for NeuralSort/SoftSort | Yes | High variance for Logistic DSN |
| E2 | Newton Losses improves shortest-path supervision | Warcraft 12x12, AlgoVision/SS/PO methods | % perfect matches | Consistent improvements, especially for SS | Yes | Hessian unavailable for AlgoVision |
| E3 | Newton Losses does not harm convex losses | MNIST classification, 5 models, 2 optimizers | Accuracy | Indistinguishable from baseline | Yes | Limited to simple convex losses |
| E4 | Runtime overhead analysis | Same as E1/E2 | Training time | Fisher negligible, Hessian varies | Yes | Hessian overhead up to 2.6x |

### Research-Theme Gap Diagnosis
The core claim of robust optimization improvement is well-supported, but the method's sensitivity to $\lambda$ and potential instability in high-variance regimes are not fully characterized. Additionally, generalization to distributional shifts or noisy algorithmic outputs remains untested.

### Proposed Research Experiments
| Target Claim | Hypothesis | Minimal Design | Controls | Metrics | Success Criterion | Cost | Gain |
|---|---|---|---|---|---|---|---|
| Robustness to $\lambda$ | Adaptive scheduling reduces tuning burden | Implement gradient-norm based $\lambda$ decay | Fixed $\lambda$ grid search | Accuracy, tuning time | Comparable accuracy with less tuning | Low | Usability |
| Stability under noise | Newton Losses stabilizes training under noisy supervision | Add Gaussian noise to sorting targets | Baseline with noise | Accuracy drop | Smaller drop than baseline | Low | Robustness |
| OOD Generalization | Curvature awareness improves transfer | Train on n=5, test on n=10 without fine-tuning | Baseline transfer | Accuracy | Higher transfer accuracy | Medium | Generalization |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score**: 7/10
**Post-Revision Target**: [8, 9]/10

**Rationale**: The paper presents a novel and practically valuable method for stabilizing the training of algorithmic losses by leveraging second-order curvature information in the output space. The empirical validation is broad and convincing, demonstrating significant improvements across multiple differentiable algorithm families. The theoretical grounding via split optimization equivalence adds rigor. However, the score is moderated by the hyperparameter sensitivity of $\lambda$, the high variance observed in certain settings (e.g., Logistic DSN), and unqualified claims regarding computational efficiency. Addressing these weaknesses through adaptive scheduling, robust statistical reporting, and clearer efficiency bounding would significantly strengthen the manuscript and justify a higher score.
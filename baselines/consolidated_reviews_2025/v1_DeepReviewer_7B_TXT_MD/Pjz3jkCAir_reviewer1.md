### Summary

This paper introduces a method for inferring parameters of PDEs governing a signal from data. The method combines an autoencoder to encode the signal and a neural network to approximate the PDE parameters. The method is trained by minimizing a loss function that combines the autoencoder loss and a loss enforcing the PDE to be satisfied. The method is evaluated on a few PDEs and compared to a few baselines.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

* The paper is well written and easy to follow.
* The method is evaluated on a few PDEs.

### Weaknesses

#### Some Related Works

[1] PDEBench: A Benchmark for Scientific Machine Learning
[2] Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations
[3] Deep learning for universal linear PDE solvers: An operator learning approach
[4] Learning in the frequency domain for solving time-dependent inverse problems
[5] Learning in the Fourier Domain for Solving Time-Dependent Inverse Problems

#### comment

 * The paper is missing a large part of related work. In particular, the authors should consider physics-informed neural networks (PINNs) [2] and operator learning approaches (see [1] for a recent survey) as well as other methods for inverse problems involving PDEs (see [3,4,5] for a few examples). The authors should also consider the references provided by the reviewers below.
* The method is only evaluated on a few PDEs and the baselines are weak. The authors should consider evaluating their method on a more diverse set of PDEs, including more complex and higher-dimensional systems. The baselines used in the paper are not state-of-the-art, and the authors should compare their method to more competitive baselines.
* The authors should consider evaluating their method on the benchmarks provided in [1].

### Suggestions

The authors should significantly expand the related work section to include a more comprehensive discussion of physics-informed neural networks (PINNs) and operator learning methods. Specifically, they should discuss the similarities and differences between their approach and PINNs, which also incorporate PDE constraints into the training process. Furthermore, they should explore operator learning techniques, which aim to learn mappings between function spaces, and discuss how their method compares to these approaches in terms of both methodology and performance. The authors should also consider the references provided by the reviewers, which offer additional perspectives on the field. A more thorough literature review would help to better position the contribution of this work and highlight its unique aspects.

To strengthen the experimental evaluation, the authors should evaluate their method on a more diverse set of PDEs, including more complex and higher-dimensional systems. For example, they could consider evaluating their method on systems with non-linearities, time-varying coefficients, or multiple spatial dimensions. Furthermore, the authors should compare their method to more competitive baselines, including state-of-the-art methods for solving inverse problems involving PDEs. This would provide a more rigorous evaluation of the performance of their method and help to demonstrate its advantages over existing approaches. The authors should also consider evaluating their method on the benchmarks provided in [1], which offer a standardized set of PDEs for evaluating inverse problem solvers.

Finally, the authors should provide a more detailed analysis of the performance of their method, including a discussion of the limitations and potential failure modes. For example, they should discuss how the performance of their method varies with the complexity of the PDE, the amount of training data, and the choice of hyperparameters. They should also discuss the computational cost of their method and compare it to the computational cost of other methods. A more thorough analysis of the performance of their method would help to provide a more complete understanding of its strengths and weaknesses.

### Questions

* How does the proposed method compare to PINNs and operator learning methods?
* How does the proposed method compare to other methods for inverse problems involving PDEs?
* How does the proposed method perform on the benchmarks provided in [1]?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

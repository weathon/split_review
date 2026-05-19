### Summary

This paper proposes a physics-informed neural PDE solver that demonstrates robust generalization across various aspects of PDE configurations, including initial conditions, PDE coefficients, and training time horizons. The key idea is to project the PDE solutions into a latent space via auto-decoding and subsequently learning the dynamics of these latent embeddings conditioned on the PDE coefficients. The authors also propose two regularization techniques to enhance temporal extrapolation ability and training stability.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow. The authors provide sufficient details about the model architecture and training procedure.
2. The authors conduct extensive experiments on various benchmarks, including 1D combined equations and 2D Navier-Stokes equations. The results demonstrate that the proposed method outperforms existing data-driven approaches in terms of generalization performance.
3. The authors investigate the transferability of the learned representations to downstream tasks like long-term integration and inverse problems. The results show that the pre-trained model can be fine-tuned to achieve good performance on these tasks.

### Weaknesses

#### Some Related Works

[1] Neural operators for learning nonlinear spatio-temporal dynamics
[2] Learning solution operators for parameterized evolutive PDEs
[3] DINO: Deep inference of nonlinear operators for probabilistic PDE solvers
[4] Physics-informed neural operator for solving spatiotemporal partial differential equations

#### comment

1. The novelty of the proposed method is limited. The idea of using a latent space to represent PDE solutions has been explored in previous works [1,2]. The idea of using neural ODE to model the latent dynamics has also been studied in [3]. The proposed regularization techniques are also not very novel, as similar techniques have been used in other physics-informed neural networks.
2. The experimental results are not very convincing. The authors only compare their method with a few baselines, and the improvements are not significant. For example, in Table 2, the proposed method only outperforms the baselines by a small margin. The authors should compare their method with more state-of-the-art approaches, such as [4], to demonstrate the superiority of their method.
3. The authors do not provide any theoretical analysis of the proposed method. It is unclear why the proposed method can generalize well to unseen initial conditions, PDE coefficients, and training time horizons. The authors should provide some theoretical insights into the proposed method, such as convergence analysis or generalization bounds.

### Suggestions

The paper's primary weakness lies in its incremental contribution over existing methods. While the combination of latent space representation, neural ODEs for latent dynamics, and physics-informed learning is presented as novel, each component has been explored in prior work. The use of a latent space for PDE solutions, as seen in [1,2], is not a new concept. Similarly, modeling latent dynamics with neural ODEs, as in [3], has been previously investigated. The proposed regularization techniques, while helpful, are not fundamentally novel and have been used in other physics-informed neural networks. To strengthen the paper, the authors should clearly articulate the specific novelty of their approach, highlighting the unique combination of these existing techniques and demonstrating how this combination leads to a significant improvement over existing methods. A more detailed comparison with existing methods, focusing on the specific differences and advantages of the proposed approach, would be beneficial.

Furthermore, the experimental evaluation needs to be more comprehensive. The current comparison with a limited set of baselines does not convincingly demonstrate the superiority of the proposed method. The improvements shown in Table 2 are marginal, and the authors should include comparisons with more state-of-the-art approaches, such as [4], to provide a more robust evaluation. The authors should also consider including a wider range of PDE problems and initial conditions to demonstrate the generalization capabilities of the proposed method. A more thorough analysis of the experimental results, including a discussion of the limitations and potential failure cases, would also be valuable. For example, the authors could analyze the sensitivity of the method to different hyperparameter settings and provide guidelines for selecting appropriate values.

Finally, the lack of theoretical analysis is a significant drawback. The paper does not provide any theoretical justification for why the proposed method can generalize well to unseen initial conditions, PDE coefficients, and training time horizons. The authors should provide some theoretical insights into the proposed method, such as convergence analysis or generalization bounds. This would help to establish the theoretical foundations of the method and provide a deeper understanding of its behavior. Without such analysis, it is difficult to assess the reliability and robustness of the proposed method. The authors should also discuss the limitations of their approach and potential areas for future research.

### Questions

1. How does the proposed method compare to other physics-informed neural PDE solvers, such as [4]?
2. Can the authors provide any theoretical analysis of the proposed method, such as convergence analysis or generalization bounds?
3. How does the proposed method perform on more challenging PDE problems, such as high-dimensional PDEs or PDEs with complex geometries?
4. How does the proposed method perform on different types of initial conditions, such as random initial conditions or initial conditions with discontinuities?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

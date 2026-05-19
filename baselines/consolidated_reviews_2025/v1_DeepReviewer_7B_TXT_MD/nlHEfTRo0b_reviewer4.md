### Summary

This paper proposes a physics-informed latent dynamics model for solving PDEs. The authors propose a new method to improve the training stability and extrapolation of the latent dynamics model. The authors conduct experiments on 1D and 2D PDEs to show the effectiveness of the proposed method.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The proposed method is well-motivated and novel. The authors propose a new method to improve the training stability and extrapolation of the latent dynamics model.
2. The authors conduct experiments on 1D and 2D PDEs to show the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The authors only conduct experiments on 1D and 2D PDEs. It is unclear whether the proposed method can be generalized to 3D PDEs. Specifically, the computational cost of training and inference for 3D problems could be significantly higher, and the latent space might need to be adapted to capture the increased complexity. The paper lacks a discussion on the potential challenges and adaptations required for 3D applications.
2. The authors only conduct experiments on the synthetic dataset. It is unclear whether the proposed method can be generalized to real-world datasets. The synthetic datasets, while useful for initial validation, may not capture the complexities and noise present in real-world data. The performance of the method on real-world data, such as weather simulations or fluid dynamics in complex geometries, remains uncertain.
3. The authors do not conduct ablation studies on the proposed method. It is unclear whether the proposed method is better than the existing methods. The paper lacks a systematic comparison of the proposed method against other state-of-the-art physics-informed neural networks (PINNs) or latent dynamics models. Without ablation studies, it is difficult to isolate the impact of each component of the proposed method and to justify its superiority over existing approaches.

### Suggestions

The authors should provide a more detailed discussion on the scalability of their method to 3D PDEs. This should include an analysis of the computational complexity of the proposed approach and potential strategies for mitigating the increased computational cost. For example, the authors could explore techniques such as adaptive mesh refinement, parallel computing, or dimensionality reduction methods to handle the higher dimensionality. Furthermore, the authors should discuss the potential limitations of the latent space representation in capturing the intricate dynamics of 3D systems and propose possible solutions. It would be beneficial to include a theoretical analysis of the method's convergence properties for 3D problems, if possible, or at least provide a discussion of the expected behavior.

To address the concern about the generalization to real-world datasets, the authors should conduct experiments on benchmark datasets that are commonly used in the field of physics-informed machine learning. This would involve using datasets that contain noise, boundary conditions, and complex geometries, which are typical of real-world applications. The authors should also compare their method against other state-of-the-art methods on these datasets to demonstrate its effectiveness. Furthermore, the authors should provide a detailed analysis of the performance of their method on different types of real-world data, highlighting any potential limitations or challenges. This would provide a more comprehensive evaluation of the method's practical applicability.

Finally, the authors should conduct a thorough ablation study to evaluate the contribution of each component of their proposed method. This should include experiments where each component is removed or modified to assess its impact on the overall performance. For example, the authors could investigate the effect of different choices of the latent space dimensionality, the architecture of the neural network used to model the latent dynamics, and the specific form of the regularization terms. The ablation study should also compare the proposed method against other state-of-the-art methods to demonstrate its superiority. This would provide a more rigorous evaluation of the method's effectiveness and justify its design choices.

### Questions

1. Can the proposed method be generalized to 3D PDEs?
2. Can the proposed method be generalized to real-world datasets?

### Rating

6

### Confidence

3

**********

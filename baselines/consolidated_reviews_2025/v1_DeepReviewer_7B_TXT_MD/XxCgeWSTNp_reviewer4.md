### Summary

The paper introduces a novel sampling algorithm for Lévy-Itô diffusion models, which are diffusion models that utilize α-stable noise instead of Gaussian noise. The authors propose a parametric family of stochastic differential equations (SDEs) that can be used to sample from these models. The proposed algorithm allows for more flexibility in the reverse diffusion process by introducing a parameter ηt that controls the amount of noise added at each step. The authors demonstrate the effectiveness of their method on image generation tasks and show that it achieves better performance with fewer function evaluations (NFE) compared to the standard approach. They also apply their method to a text-to-speech model, showing that it can handle imbalanced datasets effectively.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper provides a solid theoretical foundation for the proposed sampling algorithm, with detailed proofs and derivations. The authors clearly explain the connection between their method and existing approaches, and they provide a clear motivation for their work.

2. The paper is well-written and organized, making it easy to follow the authors' arguments and understand the technical details. The authors use clear and concise language, and they provide sufficient background information to make the paper accessible to a broad audience.

3. The paper provides a comprehensive evaluation of the proposed method, including experiments on image generation and text-to-speech modeling. The authors compare their method to existing approaches and show that it achieves better performance with fewer function evaluations (NFE). The authors also provide a detailed analysis of the results, including ablation studies and visualizations.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a clear explanation of how the proposed method can be applied to other types of diffusion models, such as those used in audio or video generation. While the authors mention that their method can be applied to any diffusion model that uses a stochastic differential equation (SDE) to model the forward process, they do not provide any specific details or examples of how this can be done. This makes it difficult to assess the generalizability of the method and its potential impact on other areas of research.

2. The paper does not provide a detailed analysis of the computational cost of the proposed method, particularly in comparison to existing approaches. While the authors mention that their method can achieve better performance with fewer function evaluations (NFE), they do not provide any information about the actual runtime or memory usage of their method. This makes it difficult to assess the practical benefits of the method and its suitability for real-world applications.

3. The paper does not provide a detailed analysis of the sensitivity of the proposed method to the choice of hyperparameters, such as the step size and the number of function evaluations (NFE). While the authors mention that their method is robust to the choice of hyperparameters, they do not provide any specific details or experiments to support this claim. This makes it difficult to assess the robustness of the method and its potential for practical use.

### Suggestions

The authors should provide a more detailed explanation of how their method can be applied to other types of diffusion models, such as those used in audio or video generation. This should include specific examples of how the reverse-time SDE is adapted for different data modalities, and how the noise schedule is chosen for each modality. For instance, in video generation, the noise schedule might need to account for the temporal dependencies between frames, which is not the case in image generation. The authors should also discuss the challenges of applying their method to high-dimensional data, such as video, and how these challenges can be addressed. A more thorough discussion of these points would greatly enhance the paper's impact and make it more accessible to a broader audience.

Furthermore, the authors should provide a more detailed analysis of the computational cost of their proposed method. This should include a comparison of the runtime and memory usage of their method with existing approaches, such as DDIM and DPM-Solver, under various settings. The analysis should be performed on a standard hardware setup to ensure reproducibility. The authors should also discuss the trade-offs between computational cost and performance, and provide guidelines for choosing appropriate hyperparameter values for different applications. For example, the authors could show how the performance of their method varies with different step sizes and NFE values, and discuss how to choose the optimal values for a given task. This would help readers to better understand the practical benefits of the proposed method.

Finally, the authors should provide a more detailed analysis of the sensitivity of their method to the choice of hyperparameters. This should include a systematic study of the impact of different step sizes and NFE values on the quality of the generated samples. The authors should also discuss the trade-offs between computational cost and performance, and provide guidelines for choosing appropriate hyperparameter values for different applications. For example, the authors could show how the performance of their method varies with different step sizes and NFE values, and discuss how to choose the optimal values for a given task. This would help readers to better understand the robustness of the method and its potential for practical use.

### Questions

1. How does the proposed method compare to other state-of-the-art sampling algorithms for diffusion models, such as DDIM and DPM-Solver, in terms of both performance and computational cost?

2. Can the proposed method be applied to other types of diffusion models, such as those used in audio or video generation? If so, what modifications would be necessary?

3. How sensitive is the proposed method to the choice of hyperparameters, such as the step size and the number of function evaluations (NFE)? Are there any guidelines for choosing appropriate hyperparameter values for different applications?

### Rating

6

### Confidence

3

**********

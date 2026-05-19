### Summary

The paper proposes a new sampling algorithm for Lévy-Itô diffusion models, which are a variant of diffusion models that use α-stable noise instead of Gaussian noise. The key idea is to introduce a parameter ηt that controls the amount of noise added at each step of the reverse diffusion process. The authors show that when ηt = 1, the proposed algorithm reduces to the standard deterministic sampling method, while when ηt < 1, it allows for more flexibility in the reverse process. The authors demonstrate the effectiveness of their method on image generation tasks, showing improved performance with fewer function evaluations (NFE) compared to the standard approach. They also apply their method to a text-to-speech model, showing that it can handle imbalanced datasets effectively.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

The paper is well-written and organized, making it easy to follow the authors' arguments and understand the technical details. The authors use clear and concise language, and they provide sufficient background information to make the paper accessible to a broad audience. The paper provides a comprehensive evaluation of the proposed method, including experiments on image generation and text-to-speech modeling. The authors compare their method to existing approaches and show that it achieves better performance with fewer function evaluations (NFE). The authors also provide a detailed analysis of the results, including ablation studies and visualizations.

### Weaknesses

#### Some Related Works


#### comment

The paper does not provide a clear explanation of how the proposed method can be applied to other types of diffusion models, such as those used in audio or video generation. While the authors mention that their method can be applied to any diffusion model that uses a stochastic differential equation (SDE) to model the forward process, they do not provide any specific details or examples of how this can be done. This makes it difficult to assess the generalizability of the method and its potential impact on other areas of research.

The paper does not provide a detailed analysis of the computational cost of the proposed method, particularly in comparison to existing approaches. While the authors mention that their method can achieve better performance with fewer function evaluations (NFE), they do not provide any information about the actual runtime or memory usage of their method. This makes it difficult to assess the practical benefits of the method and its suitability for real-world applications.

The paper does not provide a detailed analysis of the sensitivity of the proposed method to the choice of hyperparameters, such as the step size and the number of function evaluations (NFE). While the authors mention that their method is robust to the choice of hyperparameters, they do not provide any specific details or experiments to support this claim. This makes it difficult to assess the robustness of the method and its potential for practical use.

### Suggestions

The paper would benefit from a more thorough discussion of the practical implications of the proposed method. While the theoretical framework is well-presented, the paper lacks concrete examples of how the method can be applied to different types of diffusion models. For instance, the authors could provide a detailed explanation of how their method can be adapted to audio or video generation, including specific examples of how the reverse-time SDE is modified for each modality. This would involve discussing the challenges of applying the method to high-dimensional data and how these challenges can be addressed. Furthermore, the authors should provide a more detailed analysis of the computational cost of their method, including a comparison to existing approaches such as DDIM and DPM-Solver. This analysis should include a discussion of the runtime and memory usage of the method, as well as the trade-offs between computational cost and performance. This would help readers to better understand the practical benefits of the proposed method and its suitability for real-world applications.

To address the lack of sensitivity analysis, the authors should provide a more detailed discussion of how the choice of hyperparameters affects the performance of the method. This should include a systematic study of the impact of different step sizes and numbers of function evaluations (NFE) on the quality of the generated samples. The authors should also discuss the trade-offs between computational cost and performance, and provide guidelines for choosing appropriate hyperparameter values for different applications. This would help readers to better understand the robustness of the method and its potential for practical use. For example, the authors could show how the performance of their method varies with different step sizes and NFE values, and they could discuss how to choose the optimal values for a given task. This would provide a more complete picture of the method's behavior and its limitations.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method. While the authors mention that their method is robust to the choice of hyperparameters, they do not provide any specific details or experiments to support this claim. The authors should discuss the potential limitations of the method and its applicability to different types of diffusion models. This would help readers to better understand the scope of the method and its potential for future research. For example, the authors could discuss the limitations of their method in terms of the types of noise distributions that it can handle, or the types of data modalities that it can be applied to. This would provide a more balanced and comprehensive assessment of the method's strengths and weaknesses.

### Questions

How does the proposed method compare to other state-of-the-art sampling algorithms for diffusion models, such as DDIM and DPM-Solver, in terms of both performance and computational cost?

Can the proposed method be applied to other types of diffusion models, such as those used in audio or video generation? If so, what modifications would be necessary?

How sensitive is the proposed method to the choice of hyperparameters, such as the step size and the number of function evaluations (NFE)? Are there any guidelines for choosing appropriate hyperparameter values for different applications?

### Rating

5

### Confidence

3

**********

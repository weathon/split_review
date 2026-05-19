### Summary

This paper proposes a novel training-free conditional generation framework that leverages pretrained diffusion models and off-the-shelf neural networks with minimal additional inference cost for a broad range of tasks. Specifically, the authors leverage the manifold hypothesis to refine the guided diffusion steps and introduce a shortcut algorithm in the process. The authors also propose two methods for on-manifold guidance using pre-trained autoencoders. The authors demonstrate the effectiveness of the proposed method on various conditional generation tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is training-free and requires minimal additional inference cost.
3. The authors propose two methods for on-manifold guidance using pre-trained autoencoders.
4. The paper provides a comprehensive evaluation of the proposed method on various conditional generation tasks.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the limitations of the proposed method, such as the types of conditions that can be effectively handled and the potential failure cases.
2. The paper does not provide a detailed comparison with existing methods for conditional generation, such as classifier guidance and classifier-free guidance.
3. The paper does not provide a detailed analysis of the computational cost of the proposed method, including the number of inference steps and the memory requirements.
4. The paper does not provide a detailed analysis of the robustness of the proposed method to different types of noise and perturbations.
5. The paper does not provide a detailed analysis of the sensitivity of the proposed method to different hyperparameters.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations of the proposed method. Specifically, it is important to understand the types of conditions that the method is well-suited for and those where it might struggle. For instance, how does the method perform with highly complex or abstract conditions, or conditions that require a deep understanding of the underlying data distribution? A detailed analysis of failure cases would also be valuable, including scenarios where the method might produce artifacts or fail to converge. This analysis should include a discussion of the sensitivity of the method to the quality of the pre-trained autoencoders and the potential for artifacts or distortions in the generated samples. Furthermore, it would be beneficial to explore the limitations of the manifold hypothesis in the context of the proposed method and how it might affect the performance in certain scenarios.

In addition to the limitations, a more comprehensive comparison with existing methods for conditional generation is needed. The paper should not only focus on the performance of the proposed method but also on its computational cost, memory requirements, and robustness to different types of noise and perturbations. A detailed comparison with methods like classifier guidance and classifier-free guidance would be valuable. This comparison should include a discussion of the trade-offs between the different methods in terms of their ability to handle complex conditions and their computational efficiency. The paper should also discuss the potential for combining the proposed method with existing techniques to further improve performance. A table summarizing the key characteristics of each method, including their strengths and weaknesses, would be a useful addition.

Finally, the paper needs a more detailed analysis of the computational cost and robustness of the proposed method. The number of inference steps and the memory requirements should be analyzed in detail, including how they scale with the complexity of the task and the size of the input data. The robustness of the method to different types of noise and perturbations should also be investigated, including a discussion of how the method performs when the input data is corrupted by different types of noise, such as Gaussian noise or salt-and-pepper noise. The sensitivity of the method to different hyperparameters should also be analyzed, including a discussion of how the performance varies with different settings of the learning rate, batch size, and number of inference steps. A more detailed analysis of these aspects would provide a more complete understanding of the practical implications of the proposed method.

### Questions

1. How does the proposed method compare to existing methods for conditional generation, such as classifier guidance and classifier-free guidance?
2. What are the limitations of the proposed method, and what types of conditions can it effectively handle?
3. What is the computational cost of the proposed method, including the number of inference steps and the memory requirements?
4. How robust is the proposed method to different types of noise and perturbations?
5. How sensitive is the proposed method to different hyperparameters?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

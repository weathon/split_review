### Summary

The paper proposes a method for training-free conditional generation using pretrained diffusion models and off-the-shelf neural networks with minimal additional inference cost for a broad range of tasks. The method is based on the manifold hypothesis and the idea of preserving the manifolds when applying guidance gradients. The paper also proposes two methods for on-manifold guidance using pre-trained autoencoders and demonstrates the effectiveness of the proposed method on various conditional generation tasks.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is training-free and requires minimal additional inference cost.
- The paper proposes two methods for on-manifold guidance using pre-trained autoencoders.
- The paper provides a comprehensive evaluation of the proposed method on various conditional generation tasks.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the limitations of the proposed method, such as the types of conditions that can be effectively handled and the potential failure cases.
- The paper does not provide a detailed comparison with existing methods for conditional generation, such as classifier guidance and classifier-free guidance.
- The paper does not provide a detailed analysis of the computational cost of the proposed method, including the number of inference steps and the memory requirements.
- The paper does not provide a detailed analysis of the robustness of the proposed method to different types of noise and perturbations.
- The paper does not provide a detailed analysis of the sensitivity of the proposed method to different hyperparameters.

### Suggestions

The paper should include a more thorough analysis of the limitations of the proposed method. Specifically, it should explore the types of conditions that the method can and cannot handle effectively. For example, it would be beneficial to analyze the performance of the method on conditions that are highly complex or that require a deep understanding of the underlying data distribution. Furthermore, the paper should discuss potential failure cases and scenarios where the method might not perform well. This analysis should include a discussion of the sensitivity of the method to the quality of the pre-trained autoencoders and the potential for artifacts or distortions in the generated samples. A more detailed analysis of these aspects would provide a more complete understanding of the strengths and weaknesses of the proposed approach.

The paper should also provide a more detailed comparison with existing methods for conditional generation, such as classifier guidance and classifier-free guidance. The comparison should not only focus on the performance of the methods but also on their computational cost, memory requirements, and robustness to different types of noise and perturbations. For example, the paper should discuss the trade-offs between the different methods in terms of their ability to handle complex conditions and their computational efficiency. It would be beneficial to include a table that summarizes the key characteristics of each method, including their strengths and weaknesses. This would allow the reader to better understand the advantages and disadvantages of the proposed method compared to existing approaches. The paper should also discuss the potential for combining the proposed method with existing techniques to further improve performance.

Finally, the paper should provide a more detailed analysis of the computational cost of the proposed method, including the number of inference steps and the memory requirements. The paper should also analyze the robustness of the proposed method to different types of noise and perturbations. For example, the paper should investigate how the method performs when the input data is corrupted by different types of noise, such as Gaussian noise or salt-and-pepper noise. The paper should also analyze the sensitivity of the proposed method to different hyperparameters, such as the learning rate, the batch size, and the number of inference steps. A more detailed analysis of these aspects would provide a more complete understanding of the practical implications of the proposed method.

### Questions

- How does the proposed method compare to existing methods for conditional generation, such as classifier guidance and classifier-free guidance?
- What are the limitations of the proposed method, and what types of conditions can it effectively handle?
- What is the computational cost of the proposed method, including the number of inference steps and the memory requirements?
- How robust is the proposed method to different types of noise and perturbations?
- How sensitive is the proposed method to different hyperparameters?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

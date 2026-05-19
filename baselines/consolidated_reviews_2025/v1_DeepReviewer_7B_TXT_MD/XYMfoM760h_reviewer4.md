### Summary

This paper addresses the problem of controlling the number of generated objects in text-to-image diffusion models. The authors propose a method that leverages the self-attention layers of the diffusion model to identify object features and instance identity. They train a U-Net model to correct the number of instances in the generated layout and use this layout to guide the image generation process. The method is evaluated on two benchmark datasets, demonstrating improved accuracy in counting the number of objects compared to existing baselines.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and effective, and the experimental results demonstrate its superiority over existing baselines.
- The authors provide a detailed analysis of the method's performance and limitations.

### Weaknesses

#### Some Related Works


#### comment

 - The method relies on training a U-Net model to correct the number of instances in the generated layout, which may limit its applicability in real-time or resource-constrained scenarios.
- The paper primarily focuses on generating scenes with a limited number of objects (up to 10). It would be beneficial to evaluate the method's performance on more complex scenes with a larger number of objects to demonstrate its scalability.
- The method requires manual specification of the number of objects, which may not always be feasible in real-world applications where the desired number of objects is not known in advance.

### Suggestions

The reliance on a trained U-Net model for correcting object counts introduces a potential bottleneck for real-time applications. While the authors mention that the U-Net is trained offline, the inference time for this module could still be a significant factor, especially when dealing with high-resolution images or complex scenes. Exploring alternative methods for instance correction that do not require training a separate model could be beneficial. For example, incorporating attention mechanisms directly into the diffusion model or investigating knowledge distillation techniques to transfer the knowledge of the U-Net to a smaller, faster model could be promising directions. Furthermore, the paper should provide a more detailed analysis of the computational cost, including the training time and inference time for the U-Net, to better understand the practical limitations of the proposed method.

The evaluation of the method is limited to scenes with a small number of objects (up to 10), which may not accurately reflect real-world scenarios. It would be crucial to assess the method's performance on more complex scenes with a larger number of objects to demonstrate its scalability and robustness. This could involve evaluating the method on datasets with a wider range of object counts and scene complexities. Additionally, the paper should analyze how the accuracy of the object count changes as the number of objects increases and whether there are any trade-offs between object count accuracy and image quality. This analysis would provide a more nuanced understanding of the method's strengths and limitations.

The requirement for manual specification of the number of objects is a significant limitation that needs to be addressed. In many real-world applications, the desired number of objects is not known in advance, or the user may want to explore different numbers of objects interactively. To overcome this limitation, the authors could explore methods for automatically determining the optimal number of objects based on the input text prompt or the scene context. For example, they could investigate using reinforcement learning to train an agent that can adaptively adjust the number of objects during the generation process. Another approach could be to develop a user interface that allows users to interactively control the number of objects and provide feedback to the model. This would make the method more user-friendly and applicable to a wider range of real-world scenarios.

### Questions

Please see the weaknesses above.

### Rating

8

### Confidence

3

**********

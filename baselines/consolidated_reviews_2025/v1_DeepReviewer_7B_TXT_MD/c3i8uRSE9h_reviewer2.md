### Summary

The paper proposes an algorithm for fast constrained sampling in pre-trained diffusion models. The proposed algorithm is based on a numerical approximation to the gradients, which is computationally efficient and avoids backpropagation. The authors demonstrate the effectiveness of their method on image inpainting and super-resolution tasks, showing comparable results to state-of-the-art methods with significantly reduced inference time.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The proposed algorithm is computationally efficient, as it avoids backpropagation and uses a numerical approximation to gradients.
2. The authors validate their approach on standard benchmarks like ImageNet for inpainting and super-resolution, demonstrating its practical applicability.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a thorough comparison with existing methods, particularly in terms of computational efficiency and performance. While the authors claim their method is computationally efficient, they do not provide a detailed analysis of the computational cost compared to other methods. A more rigorous comparison, including metrics such as FLOPs, runtime, and memory usage, is needed to substantiate this claim.
2. The experiments are limited to relatively simple tasks like inpainting and super-resolution. The authors should consider evaluating their method on more complex tasks, such as text-guided image editing or image inpainting with irregular masks, to demonstrate its versatility and robustness. The current experiments do not fully explore the potential of the proposed method.
3. The paper does not discuss the limitations of the proposed method or potential failure cases. For example, it is unclear how the method would perform on images with complex structures or textures, or under extreme noise conditions. A discussion of these limitations would provide a more balanced view of the method's capabilities.

### Suggestions

The authors should provide a more detailed analysis of the computational cost of their method, including a breakdown of the time spent on each step, such as the forward passes through the diffusion model and the numerical gradient approximation. This analysis should be compared to existing methods, such as those based on backpropagation, to clearly demonstrate the computational advantages of the proposed approach. Furthermore, the authors should investigate the scalability of their method to larger image sizes and more complex inverse problems. It would be beneficial to show how the computational cost scales with the size of the input image and the number of iterations required for convergence. This would provide a better understanding of the practical applicability of the method.

To address the limitations in the experimental evaluation, the authors should consider evaluating their method on more challenging tasks, such as text-guided image editing or image inpainting with irregular masks. These tasks would provide a more comprehensive assessment of the method's versatility and robustness. For example, in text-guided image editing, the authors could demonstrate the ability to modify specific regions of an image based on a text prompt, while preserving the overall structure and details of the image. In image inpainting with irregular masks, the authors could show the method's ability to handle non-rectangular masks and complex mask boundaries. These experiments would provide a more rigorous evaluation of the method's performance and its potential for real-world applications. Additionally, the authors should explore the method's performance on images with complex structures or textures, as well as under extreme noise conditions. This would help to identify the limitations of the method and provide guidance for future research.

Finally, the authors should provide a more thorough discussion of the limitations of their method and potential failure cases. This discussion should include an analysis of how the method performs on images with complex structures or textures, as well as under extreme noise conditions. The authors should also discuss the sensitivity of the method to the choice of hyperparameters, such as the step size for the numerical gradient approximation. This analysis would provide a more balanced view of the method's capabilities and limitations, and would help guide future research in this area. It would also be beneficial to explore the robustness of the method to different types of noise and corruption, as this is a critical factor in many real-world applications.

### Questions

Please see the weaknesses above.

### Rating

3

### Confidence

3

**********

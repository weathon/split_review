### Summary

This paper proposes a new approach for molecule generation that uses a coarse-to-fine generation process. The model first generates a shape graph, which is then used to generate the molecular graph. The model is trained as a variational autoencoder (VAE), and the generation process is conditioned on the latent code. The authors evaluate the model on several benchmarks and show that it outperforms existing methods in terms of reconstruction and sampling of shapes, as well as generative performance.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper proposes a novel approach for molecule generation that uses a coarse-to-fine generation process.
- The model is trained as a variational autoencoder (VAE), and the generation process is conditioned on the latent code.
- The authors evaluate the model on several benchmarks and show that it outperforms existing methods in terms of reconstruction and sampling of shapes, as well as generative performance.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the model's limitations and potential failure cases. It would be helpful to understand the types of molecules that the model struggles to generate and the reasons behind these failures.
- The paper does not discuss the potential ethical implications of using the model for molecule generation. It would be helpful to address any potential risks or concerns related to the use of the model in real-world applications.

### Suggestions

The paper should include a more thorough investigation into the model's limitations, specifically focusing on the types of molecular structures that pose challenges for the proposed coarse-to-fine generation approach. For instance, it would be beneficial to analyze the model's performance on generating molecules with complex ring systems, such as fused rings or macrocycles, and to identify any systematic biases or failure modes. A detailed analysis of the latent space could also reveal regions that correspond to problematic molecular structures, providing insights into the model's limitations. Furthermore, the authors should explore the impact of the shape graph representation on the final molecular graph generation, and whether certain shape graph topologies are more prone to generating invalid or unrealistic molecules. This analysis should include both qualitative examples of failure cases and quantitative metrics that capture the model's performance on challenging molecular structures.

In addition to the technical limitations, the paper should also address the potential ethical implications of using the model for molecule generation. While the authors mention the potential for generating novel molecules, they should also consider the potential for misuse, such as the generation of harmful or toxic compounds. A discussion of the safeguards that are in place to prevent such misuse, or the limitations of the model that would make such misuse difficult, would be valuable. The authors should also consider the potential for bias in the training data to be reflected in the generated molecules, and how this could impact the fairness and equity of the model's applications. This discussion should include specific examples of potential ethical concerns and how the authors plan to address them.

Finally, the paper should provide a more detailed analysis of the computational cost of the proposed approach, including the time and memory requirements for both training and inference. This analysis should include a comparison to existing methods and should consider the scalability of the approach to larger datasets and more complex molecules. The authors should also discuss the potential for optimizing the model's architecture and training procedure to reduce the computational cost. This analysis should be presented in a clear and concise manner, with specific metrics and comparisons to existing methods.

### Questions

- Can you provide more details on the computational cost of the proposed approach? How does it compare to existing methods in terms of training time and inference time?
- Can you provide more details on the model's limitations and potential failure cases? What are the types of molecules that the model struggles to generate, and what are the reasons behind these failures?

### Rating

8: accept, good paper

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

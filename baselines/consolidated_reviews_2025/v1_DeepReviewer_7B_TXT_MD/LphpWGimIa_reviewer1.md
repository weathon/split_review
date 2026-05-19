### Summary

This paper applies sparse autoencoders to decompose transformer activations into sparse, interpretable features. The authors apply their method to attention layer outputs across multiple models and use the resulting features to better understand model computations. The paper demonstrates that attention output SAEs can identify three families of interpretable features: long-range context, short-range context, and high-level context. The authors also demonstrate that their method can be used to better understand attention head polysemanticity, and improve our understanding of the Indirect Object Identification circuit.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper applies sparse autoencoders to attention layer outputs, providing a novel perspective on how attention heads process information. This approach allows for a more fine-grained analysis of model computations compared to previous methods that focused on individual attention heads.
- The paper provides a thorough analysis of the features learned by the SAEs, identifying three families of interpretable features: long-range context, short-range context, and high-level context. This analysis provides valuable insights into how transformers process information and how attention layers contribute to this process.
- The paper demonstrates the utility of the SAEs for understanding model behavior in several ways. First, the authors show that attention output SAEs can identify polysemantic attention heads, which are attention heads that perform multiple tasks. This finding is important because it highlights the limitations of individual attention heads and suggests that attention heads may need to be analyzed in groups.
- The paper also demonstrates that attention output SAEs can improve our understanding of the Indirect Object Identification circuit. By analyzing the features learned by the SAEs, the authors are able to identify the positional signal used by the circuit and confirm that it is based on the position of the duplicate name relative to the "and" token. This finding is important because it provides a causal explanation for how the circuit works.

### Weaknesses

#### Some Related Works


#### comment

 - The paper primarily focuses on analyzing attention layer outputs, but it is not clear why this is the most appropriate place to apply sparse autoencoders. The authors should provide a more detailed justification for their choice of attention layer outputs, and discuss why other parts of the model, such as the input or output embeddings, might not be as suitable for this analysis. Specifically, the paper lacks a discussion on why the non-linearities within the attention mechanism are crucial for the sparse coding to be effective, and how this compares to applying SAEs directly to the input or output layers which are linear transformations of the embeddings.
- The paper does not provide a detailed explanation of how the sparse autoencoders are trained, including the specific loss function, optimization algorithm, and hyperparameters used. This lack of detail makes it difficult to reproduce the results and to assess the robustness of the method. The paper should include a more thorough description of the training procedure, including the specific initialization scheme for the SAE weights, and the learning rate schedule used during training.
- The paper does not provide a detailed comparison of the proposed method with other existing interpretability techniques, such as activation patching or gradient-based attribution methods. While the paper mentions that the proposed method is more effective than these alternatives, it does not provide a quantitative comparison to support this claim. A more detailed comparison, including a discussion of the strengths and weaknesses of each method, would be beneficial. The paper should also discuss the computational cost of the proposed method compared to other interpretability techniques.
- The paper does not provide a detailed analysis of the limitations of the proposed method. For example, it is not clear how the method would perform on larger models or on more complex tasks. The paper should discuss the potential limitations of the method and suggest directions for future research. Specifically, the paper should address how the method scales with model size and how it might be affected by different architectural choices.

### Suggestions

The paper would benefit from a more thorough discussion of the theoretical underpinnings of applying sparse autoencoders to attention layer outputs. While the authors demonstrate that the method works, they should provide a more detailed explanation of why the non-linearities within the attention mechanism are crucial for the sparse coding to be effective. Specifically, they should discuss how the sparse coding is achieved through the non-linear transformations within the attention layers, and how this differs from applying SAEs to the input or output layers, which are linear transformations of the embeddings. A more detailed explanation of the mathematical properties of the attention mechanism and how they interact with the sparse coding objective would be beneficial. Furthermore, the authors should discuss the potential limitations of this approach, such as the possibility that the learned features are not truly representative of the underlying computations, but rather artifacts of the training process.

To improve the reproducibility and robustness of the method, the authors should provide a more detailed description of the training procedure for the sparse autoencoders. This should include a clear specification of the loss function, optimization algorithm, and hyperparameters used. The authors should also discuss the initialization scheme for the SAE weights and the learning rate schedule used during training. Furthermore, the authors should provide a more detailed explanation of how the SAEs are used to interpret model behavior. For example, they should discuss how the learned features are mapped back to the input space and how this mapping can be used to understand the model's computations. A more detailed explanation of the feature attribution method used to identify polysemantic attention heads would also be beneficial. The authors should also discuss the potential limitations of this approach, such as the possibility that the feature attributions are not truly representative of the underlying computations.

Finally, the paper would benefit from a more detailed comparison of the proposed method with other existing interpretability techniques. While the authors mention that their method is more effective than activation patching and gradient-based attribution methods, they do not provide a quantitative comparison to support this claim. A more detailed comparison, including a discussion of the strengths and weaknesses of each method, would be beneficial. The authors should also discuss the computational cost of the proposed method compared to other interpretability techniques. Furthermore, the authors should discuss the potential limitations of the proposed method, such as the possibility that the learned features are not truly representative of the underlying computations, but rather artifacts of the training process. The authors should also discuss how the method would perform on larger models or on more complex tasks, and suggest directions for future research.

### Questions

- How does the proposed method compare to other existing interpretability techniques, such as activation patching or gradient-based attribution methods? While the paper mentions that the proposed method is more effective than these alternatives, it does not provide a quantitative comparison to support this claim.
- How would the proposed method perform on larger models or on more complex tasks? The paper focuses on relatively small models and simple tasks, but it is not clear how the method would scale to larger models or more complex tasks.

### Rating

6

### Confidence

4

**********

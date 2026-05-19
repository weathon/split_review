### Summary

This paper introduces a new technique to analyze attention layer outputs using sparse autoencoders (SAEs). The authors demonstrate that SAEs can decompose attention layer outputs into sparse, interpretable features, which can be used to better understand model behavior. They also introduce Recursive Direct Feature Attribution (RDFA), a technique to trace model computations on arbitrary prompts. The authors apply their methods to analyze attention head polysemy and improve understanding of the Indirect Object Identification circuit.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel technique for analyzing attention layer outputs using sparse autoencoders (SAEs). This approach provides a new way to decompose model computations into interpretable features, which can be used to better understand model behavior.
2. The authors demonstrate that SAEs can identify polysemantic attention heads, which are attention heads that perform multiple tasks. This finding highlights the limitations of individual attention heads and suggests that attention heads may need to be analyzed in groups.
3. The authors introduce Recursive Direct Feature Attribution (RDFA), a technique to trace model computations on arbitrary prompts. This technique can be used to better understand how transformer models process information and make decisions.
4. The paper applies its methods to analyze attention head polysemy and improve the understanding of the Indirect Object Identification circuit in transformer models. The results of these analyses are compelling and provide valuable insights into the behavior of transformer models.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on analyzing attention layer outputs, but it is not clear why this is the most appropriate place to apply sparse autoencoders. The authors should provide a more detailed justification for their choice of attention layer outputs, and discuss why other parts of the model, such as the input or output embeddings, might not be as suitable for this analysis. Specifically, the paper lacks a discussion on the non-linearities within the attention mechanism and how they interact with the sparse coding objective. It is not clear how the sparse autoencoders are able to disentangle the complex representations learned by the attention layers, and whether this approach is limited by the inherent non-linearity of the attention mechanism itself.
2. The paper does not provide a detailed explanation of how the sparse autoencoders are trained, including the specific loss function, optimization algorithm, and hyperparameters used. This lack of detail makes it difficult to reproduce the results and to assess the robustness of the method. The paper should include a more thorough description of the training procedure, including the specific initialization scheme for the SAE weights, and the learning rate schedule used during training. Furthermore, the paper should discuss the sensitivity of the results to different hyperparameter choices, such as the sparsity level of the autoencoder and the size of the hidden layer.
3. The paper does not provide a detailed comparison of the proposed method with other existing interpretability techniques, such as activation patching or gradient-based attribution methods. While the paper mentions that the proposed method is more effective than these alternatives, it does not provide a quantitative comparison to support this claim. A more detailed comparison, including a discussion of the strengths and weaknesses of each method, would be beneficial. The paper should also discuss the computational cost of the proposed method compared to other interpretability techniques.

### Suggestions

The authors should provide a more detailed justification for their choice of attention layer outputs as the primary target for analysis using sparse autoencoders. This should include a discussion of the specific properties of attention layers that make them suitable for this type of analysis, as well as a comparison to other potential targets, such as the input or output embeddings. The authors should also discuss the limitations of their approach, particularly in light of the non-linearities within the attention mechanism. It would be beneficial to explore how the sparse autoencoders are able to disentangle the complex representations learned by the attention layers, and whether this approach is limited by the inherent non-linearity of the attention mechanism itself. Furthermore, the authors should consider the potential impact of different activation functions used in the attention layers on the effectiveness of the sparse autoencoders.

To improve the reproducibility and robustness of the results, the authors should provide a more detailed explanation of the training procedure for the sparse autoencoders. This should include the specific loss function, optimization algorithm, and hyperparameters used, as well as a discussion of the initialization scheme for the SAE weights and the learning rate schedule. The authors should also discuss the sensitivity of the results to different hyperparameter choices, such as the sparsity level of the autoencoder and the size of the hidden layer. It would be beneficial to include a sensitivity analysis to demonstrate the robustness of the method to different hyperparameter settings. This would allow other researchers to reproduce the results and build upon the work presented in the paper.

Finally, the authors should provide a more detailed comparison of their method with other existing interpretability techniques, such as activation patching or gradient-based attribution methods. This comparison should include a quantitative evaluation of the performance of each method on a range of tasks, as well as a discussion of the strengths and weaknesses of each method. The authors should also discuss the computational cost of their method compared to other interpretability techniques. It would be beneficial to include a table that summarizes the key differences between the proposed method and other interpretability techniques, including the type of analysis performed, the computational cost, and the interpretability of the results. This would allow readers to better understand the advantages and limitations of the proposed method.

### Questions

1. How does the proposed method compare to other interpretability methods, such as activation patching or gradient-based attribution methods? What are the relative strengths and weaknesses of each method?
2. How would the proposed method perform on larger models or on more complex tasks? Are there any limitations to the scalability of the method?
3. How does the proposed method relate to other interpretability methods, such as causal intervention methods? What are the similarities and differences between these methods?

### Rating

6

### Confidence

3

**********

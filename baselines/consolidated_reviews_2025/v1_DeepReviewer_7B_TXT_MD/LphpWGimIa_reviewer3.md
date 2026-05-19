### Summary

This paper proposes to use sparse autoencoders to decompose attention layer outputs into sparse, interpretable features. The authors apply their method to transformer models and show that SAEs can be used to decompose attention layer outputs into sparse, interpretable features. The authors also demonstrate that SAEs can be used to analyze attention head polysemy and improve our understanding of the Indirect Object Identification circuit.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and effective.
- The paper provides a comprehensive analysis of the features learned by the SAEs and their relationship to model behavior.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed discussion of the limitations of the proposed method. For example, it is not clear how the method would perform on larger models or on more complex tasks.
- The paper does not provide a comparison to other interpretability methods. It would be helpful to see how the proposed method compares to other approaches for analyzing transformer models.
- The paper does not provide a discussion of the computational cost of training and using the SAEs. It would be helpful to know how long it takes to train the SAEs and how much memory they require.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations of the proposed sparse autoencoder (SAE) approach. Specifically, the authors should address how the method scales with model size and complexity. For instance, it would be valuable to explore the performance of the SAEs on larger transformer models, such as those with hundreds of billions of parameters, and on more complex tasks, such as those involving natural language understanding or generation. The authors should also discuss the potential impact of different hyperparameter choices on the performance of the SAEs, such as the sparsity level and the size of the hidden layer. Furthermore, it would be useful to analyze the interpretability of the learned features in more detail. For example, the authors could investigate whether the learned features correspond to specific concepts or patterns in the input data, and whether these features are consistent across different models or tasks. This would provide a more comprehensive understanding of the strengths and weaknesses of the proposed method.

In addition to the limitations, the paper should include a more comprehensive comparison to other interpretability methods. The authors should compare their approach to existing techniques for analyzing transformer models, such as activation patching, gradient-based attribution methods, and causal intervention methods. This comparison should include a discussion of the relative strengths and weaknesses of each method, as well as a quantitative evaluation of their performance on a range of tasks. For example, the authors could compare the ability of each method to identify polysemantic attention heads or to trace model computations on arbitrary prompts. This would provide a more complete picture of the proposed method's contribution to the field of interpretability. Furthermore, the authors should discuss the computational cost of training and using the SAEs in more detail. This should include a breakdown of the time and memory requirements for training the SAEs, as well as the time required for inference. It would also be useful to compare the computational cost of the proposed method to other interpretability methods.

Finally, the paper should include a more detailed discussion of the relationship between the learned features and the model's behavior. The authors should investigate whether the learned features can be used to predict the model's performance on different tasks, and whether they can be used to identify potential biases or vulnerabilities in the model. For example, the authors could analyze the relationship between the learned features and the model's accuracy on different types of inputs, or the relationship between the learned features and the model's tendency to generate biased or harmful outputs. This would provide a more comprehensive understanding of the practical implications of the proposed method. Furthermore, the authors should discuss the potential ethical implications of using SAEs to analyze transformer models, and whether there are any potential risks associated with this approach.

### Questions

- How does the proposed method compare to other interpretability methods?
- What are the limitations of the proposed method?
- What is the computational cost of training and using the SAEs?

### Rating

6

### Confidence

3

**********

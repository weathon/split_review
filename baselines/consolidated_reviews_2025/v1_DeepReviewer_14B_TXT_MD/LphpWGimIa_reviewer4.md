### Summary

This paper proposes to use sparse autoencoders (SAEs) to decompose the attention layer outputs into sparse, interpretable features. The authors show that SAEs can find a sparse, interpretable decomposition of attention layer outputs and that they can be used to explain model behavior in greater detail than prior work. The authors also introduce a new technique called Recursive Direct Feature Attribution (RDFA) that exploits the linear structure of transformers to discover sparse feature circuits through the attention layers. The authors validate their findings with experiments on GPT-2 Small and Gemma-2B.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a thorough evaluation of their method, including both quantitative and qualitative results.
3. The authors validate their findings with experiments on GPT-2 Small and Gemma-2B.
4. The authors open-source their code and data, making it easy for others to reproduce their results and build upon their work.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a clear explanation of how the SAEs are trained or how the features are extracted from the attention layer outputs. It would be helpful to provide more details on the training process and the feature extraction process.
2. The paper does not provide a clear explanation of how the weight-based head attribution technique works. It would be helpful to provide more details on this technique and how it is used to associate features with specific attention heads.
3. The paper does not provide a clear explanation of how the RDFA technique works. It would be helpful to provide more details on this technique and how it is used to discover sparse feature circuits through the attention layers.

### Suggestions

The paper would benefit from a more detailed explanation of the Sparse Autoencoder (SAE) training process. Specifically, the authors should clarify the architecture of the SAE, including the number of layers, the activation functions used, and the size of the hidden layers. Furthermore, it would be beneficial to describe the optimization algorithm used for training, such as Adam or SGD, along with the learning rate, batch size, and number of training epochs. A more detailed explanation of how the input to the SAE is constructed from the attention layer outputs is also needed. For example, are the attention weights directly fed into the SAE, or are they preprocessed in some way? Providing these details would significantly enhance the reproducibility of the results and allow other researchers to build upon this work more easily. Additionally, the authors should clarify how the sparsity constraint is enforced during training, such as through L1 regularization or other techniques.

To improve the clarity of the weight-based head attribution technique, the authors should provide a more detailed explanation of how the weights are used to associate features with specific attention heads. It is not clear how the weights are computed and how they are used to determine the contribution of each head to a particular feature. A step-by-step explanation of the process, including the mathematical formulation, would be beneficial. For example, are the weights simply the connection strengths between the attention heads and the SAE features, or is there a more complex transformation involved? Furthermore, the authors should clarify how they handle cases where multiple heads contribute to the same feature. Are the contributions simply added together, or is there a more sophisticated method for resolving conflicts? Providing these details would help readers understand the method and its limitations.

Finally, the paper needs a more thorough explanation of the Recursive Direct Feature Attribution (RDFA) technique. The authors should provide a detailed description of how the technique exploits the linear structure of transformers to discover sparse feature circuits. It is not clear how the recursion is implemented and how the feature circuits are identified. A step-by-step explanation of the algorithm, including the mathematical formulation, would be beneficial. For example, how are the direct feature attributions calculated, and how are they used to identify the sparse feature circuits? Furthermore, the authors should clarify how they handle cases where the feature circuits are complex and involve multiple layers. Are there any limitations to the technique, and how can these limitations be addressed? Providing these details would help readers understand the method and its potential applications.

### Questions

1. How do the SAEs decompose attention layer outputs into sparse, interpretable features? Can you provide a more detailed explanation of the process?
2. How does the weight-based head attribution technique work? Can you provide a more detailed explanation of the technique and how it is used to associate features with specific attention heads?
3. How does the RDFA technique exploit the linear structure of transformers to discover sparse feature circuits through the attention layers? Can you provide a more detailed explanation of the technique and how it is used to discover sparse feature circuits?

### Rating

8

### Confidence

3

**********

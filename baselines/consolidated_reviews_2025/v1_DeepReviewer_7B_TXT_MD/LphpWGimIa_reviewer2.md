### Summary

This paper investigates the interpretability of attention layers in transformer models by training sparse autoencoders (SAEs) on the activations of these layers. The authors demonstrate that SAEs can effectively decompose attention layer outputs into sparse, interpretable features, which can be used to better understand the inner workings of transformer models. The paper also introduces a novel technique called Recursive Direct Feature Attribution (RDFA) to trace models' computations on arbitrary prompts. The authors apply their methods to analyze attention head polysemy and improve the understanding of the Indirect Object Identification circuit in transformer models. Overall, the paper provides a valuable contribution to the field of mechanistic interpretability by introducing a new technique for analyzing attention layers and improving our understanding of transformer model behavior.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel technique for analyzing attention layers in transformer models using sparse autoencoders (SAEs). This approach provides a new way to decompose model computations into interpretable features, which can be used to better understand the inner workings of transformer models.
2. The paper provides a thorough analysis of attention head polysemy, demonstrating that many attention heads in transformer models perform multiple tasks. This finding highlights the limitations of individual attention heads and suggests that attention heads may need to be analyzed in groups.
3. The paper introduces a novel technique called Recursive Direct Feature Attribution (RDFA) to trace models' computations on arbitrary prompts. This technique can be used to better understand how transformer models process information and make decisions.
4. The paper applies its methods to analyze attention head polysemy and improve the understanding of the Indirect Object Identification circuit in transformer models. The results of these analyses are compelling and provide valuable insights into the behavior of transformer models.

### Weaknesses

#### Some Related Works


#### comment

1. The paper focuses primarily on attention layers and does not explore the interpretability of other components of transformer models, such as the input and output embeddings. This narrow focus limits the generalizability of the findings and leaves open questions about how the results might extend to other parts of the model.
2. The paper does not provide a detailed analysis of the computational cost of training and using the SAEs. This lack of analysis makes it difficult to assess the practicality of the proposed method for large-scale models.
3. The paper does not compare its results to other interpretability methods, such as activation patching or gradient-based attribution methods. This lack of comparison makes it difficult to assess the relative strengths and weaknesses of the proposed method.

### Suggestions

The authors should broaden their analysis to include other components of transformer models, such as the input and output embeddings. This would provide a more comprehensive understanding of how different parts of the model contribute to its overall behavior. Specifically, it would be valuable to investigate whether the sparse features learned by the SAEs on attention layers are also present in the input and output embeddings, and how these features relate to each other. This could involve training SAEs on the embeddings and comparing the resulting feature representations. Furthermore, the authors should explore the possibility of using the SAEs to analyze the interactions between different components of the model, which could provide a more holistic view of the model's behavior.

To address the lack of computational cost analysis, the authors should provide a detailed breakdown of the training and inference time for their method, as well as the memory requirements. This analysis should include a comparison to other interpretability methods, such as activation patching and gradient-based attribution methods. This would allow readers to assess the practicality of the proposed method for large-scale models. The authors should also discuss the scalability of their method and identify potential bottlenecks. For example, they could investigate the impact of model size and input sequence length on the computational cost of training and using the SAEs. This would provide valuable insights into the limitations of the method and suggest directions for future research.

Finally, the authors should compare their results to other interpretability methods, such as activation patching and gradient-based attribution methods. This comparison should include a discussion of the relative strengths and weaknesses of each method, as well as a quantitative evaluation of their performance on a range of tasks. For example, the authors could compare the ability of each method to identify polysemantic attention heads or to trace model computations on arbitrary prompts. This would provide a more comprehensive understanding of the proposed method and its place within the broader landscape of interpretability research. The authors should also discuss the limitations of their method and suggest directions for future research.

### Questions

1. How does the proposed method compare to other interpretability methods, such as activation patching or gradient-based attribution methods? What are the relative strengths and weaknesses of each method?
2. How would the proposed method perform on larger models or on more complex tasks? Are there any limitations to the scalability of the method?
3. How does the proposed method relate to other interpretability methods, such as causal intervention methods? What are the similarities and differences between these methods?

### Rating

6

### Confidence

3

**********

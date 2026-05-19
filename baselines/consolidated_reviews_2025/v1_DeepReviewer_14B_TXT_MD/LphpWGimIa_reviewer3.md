### Summary

This paper applies sparse autoencoders (SAEs) to attention layer outputs to decompose them into interpretable features. The authors demonstrate that SAEs can effectively extract sparse, meaningful features from attention outputs across different model families and sizes. They identify three main feature families: long-range context, short-range context, and induction features. The paper also introduces a weight-based head attribution technique to associate features with specific attention heads, addressing the challenge of polysemanticity. Additionally, the authors propose Recursive Direct Feature Attribution (RDFA) to trace model computations through attention layers, enhancing circuit analysis. The paper validates its findings through various experiments, including analyzing the Indirect Object Identification circuit and investigating induction heads. The authors open-source the trained SAEs and a tool for exploring model behavior through attention output SAEs.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper provides a comprehensive analysis of attention layer outputs using SAEs, identifying distinct feature families and offering insights into model behavior.
2. The introduction of weight-based head attribution and RDFA contributes to the field of mechanistic interpretability by enabling finer-grained analysis of attention layers.
3. The paper addresses the open question of redundant induction heads by distinguishing between long-prefix and short-prefix induction heads, advancing our understanding of model redundancy.
4. The authors validate their findings with rigorous experiments and provide open-source tools for further research and exploration.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on attention layer outputs, leaving other components of transformers, such as QK circuits, less explored. A more comprehensive analysis of the entire transformer architecture could provide a fuller understanding of model behavior.
2. The analysis relies on qualitative assessments and human judgment, which can be subjective and may not fully capture the complexity of model behavior. Incorporating more quantitative metrics could strengthen the findings.
3. The paper's main contribution is the application of SAEs to attention outputs, which might be seen as incremental given the existing work on SAEs for other transformer components. Highlighting unique insights gained specifically from attention outputs could strengthen the paper's impact.

### Suggestions

The paper would benefit from a more thorough investigation into the QK circuits within the transformer architecture. While the focus on attention outputs is valuable, the interaction between the query, key, and value vectors is crucial for understanding how attention is computed and how information flows through the network. A deeper analysis of the QK circuits could reveal how these components contribute to the feature families identified by the SAEs. For example, examining the attention scores and gradients with respect to the QK parameters could provide insights into which features are most influential in the attention mechanism. Furthermore, exploring how different initialization schemes or training strategies affect the learned features in the QK circuits could provide a more complete picture of the model's behavior. This would require a more detailed analysis of the attention weights and the flow of information through the QK circuitry, potentially using techniques like attention rollout or gradient-based attribution methods.

To address the subjectivity of qualitative assessments, the authors should incorporate more quantitative metrics to evaluate the interpretability of the learned features. While human judgment is useful for initial understanding, it is essential to validate these findings with objective measures. For example, the authors could use metrics like feature sparsity, reconstruction error, or the ability of the features to predict specific model behaviors. Additionally, the authors could explore the correlation between the learned features and known properties of the input data, such as syntactic or semantic features. This would provide a more rigorous and less subjective way to assess the quality of the learned features. Furthermore, the authors could investigate the stability of the learned features across different training runs or datasets, which would provide insights into the robustness of the method. This would require a more systematic approach to evaluating the learned features, potentially using techniques like cross-validation or bootstrapping.

Finally, the authors should more clearly articulate the unique insights gained from applying SAEs to attention outputs, beyond what is already known from applying SAEs to other transformer components. While the identification of long-range context, short-range context, and induction features is valuable, the authors should emphasize how these features are specifically related to the attention mechanism and how they differ from features learned in the value or MLP layers. For example, the authors could investigate how the attention mechanism modulates the contribution of different features, or how the learned features interact with the attention weights. This would require a more detailed analysis of the attention mechanism and its role in shaping the learned features. Furthermore, the authors could compare the features learned from attention outputs with those learned from other parts of the transformer, highlighting the unique contributions of the attention mechanism.

### Questions

1. How do the features learned from attention outputs compare to those learned from value vectors or MLP layers in terms of interpretability and model behavior?
2. What are the limitations of using SAEs for feature decomposition in transformers, and how might these limitations affect the interpretation of the results?
3. How does the proposed RDFA method compare to other circuit analysis techniques in terms of effectiveness and computational efficiency?

### Rating

6

### Confidence

3

**********

### Summary

The paper proposes a novel multimodal representation learning method, Information-Theoretic Hierarchical Perception (ITHP), which is inspired by neuroscience. The authors demonstrate the effectiveness of ITHP by conducting experiments on three different multimodal datasets.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow. 
2. The proposed method is well-motivated and demonstrated with solid experiments on multiple datasets.

### Weaknesses

#### Some Related Works


#### comment

1. The model architecture is somewhat unclear. Specifically, the interaction between the modality-specific encoders and the hierarchical information bottleneck is not well-defined. It's unclear how the latent representations from different modalities are combined and processed within the ITHP framework. The paper lacks a detailed explanation of the information flow, making it difficult to understand the exact mechanism of information fusion.
2. The authors claim that the model is inspired by neuroscience, but the connection to neuroscience is tenuous. The use of the term 'hierarchical' seems to be a superficial link to brain processing, without delving into the specific neural mechanisms that the model is intended to mimic. The paper does not provide any concrete evidence or detailed explanation of how the model's architecture or learning process reflects actual neural processes. The neuroscience perspective appears to be more of a motivational analogy rather than a rigorous scientific basis.

### Suggestions

To address the lack of clarity regarding the model architecture, the authors should provide a more detailed description of the information flow within the ITHP framework. This should include a clear explanation of how the modality-specific encoders interact with the hierarchical information bottleneck. Specifically, the paper should detail how the latent representations from different modalities are combined, processed, and how the information bottleneck is applied at each level of the hierarchy. A diagram illustrating the flow of information, including the input modalities, the encoders, the bottleneck layers, and the final fusion layer, would be beneficial. Furthermore, the authors should provide a mathematical formulation of the information bottleneck, explaining how it is implemented and how it affects the latent representations. This would help clarify the exact mechanism of information fusion and make the model architecture more transparent.

Regarding the connection to neuroscience, the authors should either provide a more substantial link to actual neural processes or refrain from making strong claims about the model being inspired by neuroscience. If the authors intend to draw parallels with neural mechanisms, they should delve into the specifics of how the model's architecture or learning process reflects actual neural processes. For example, they could discuss how the hierarchical structure of the model relates to the hierarchical organization of the brain, or how the information bottleneck mechanism mimics the brain's selective attention or information filtering processes. This would require a more detailed analysis of relevant neuroscience literature and a clear explanation of how the model's components map to specific neural structures or functions. Without such a detailed analysis, the neuroscience perspective should be presented as a motivational analogy rather than a core aspect of the model's design.

Finally, the authors should consider providing an ablation study to demonstrate the effectiveness of the hierarchical information bottleneck. This could involve comparing the performance of the full ITHP model with variants that lack certain aspects of the hierarchy or the information bottleneck. Such an analysis would help to quantify the contribution of each component of the model and provide further evidence for the effectiveness of the proposed method. Additionally, the authors could explore different configurations of the hierarchy, such as varying the number of levels or the type of information bottleneck used at each level, to determine the optimal configuration for different multimodal tasks.

### Questions

1. I am confused about the model architecture. What is the fusion layer? What is the prediction layer? 
2. What does the "prime modality" mean? Does it mean the most informative modality? 
3. The authors claim that the model is inspired by neuroscience, but the link to neuroscience is weak. The word "hierarchical" is used in both the paper and the neuroscience literature, but the authors do not elaborate on this connection.

### Rating

6

### Confidence

3

**********

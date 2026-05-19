### Summary

This paper explores the effectiveness of different visual encoders in MLLMs. The authors find that shallow layer features contain low-level detailed information which is helpful for fine-grained tasks such as grounding and region understanding. In contrast, the deep layer features of DINOv2 contain more fine-grained visual information. Based on the analysis, the authors propose a COMM framework that integrates CLIP and DINOv2. The COMM framework outperforms existing methods across various benchmarks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The authors conduct a comprehensive analysis of different visual encoders for MLLMs. The authors find that shallow layer features contain low-level detailed information which is helpful for fine-grained tasks such as grounding and region understanding. In contrast, the deep layer features of DINOv2 contain more fine-grained visual information. Based on the analysis, the authors propose a COMM framework that integrates CLIP and DINOv2. The COMM framework outperforms existing methods across various benchmarks.

2. The authors provide a detailed analysis of the effectiveness of different visual encoders for MLLMs. The authors find that shallow layer features contain low-level detailed information which is helpful for fine-grained tasks such as grounding and region understanding. In contrast, the deep layer features of DINOv2 contain more fine-grained visual information. Based on the analysis, the authors propose a COMM framework that integrates CLIP and DINOv2. The COMM framework outperforms existing methods across various benchmarks.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the reasons why DINOv2's deep layers are better at global understanding than shallow layers. The authors only mentioned that the pre-training objective of DINOv2 is to learn a representation that is invariant to different views of the same image, but did not explain why this leads to better global understanding. It is unclear if this is due to the model learning to capture more abstract features at deeper layers, or if it is simply a consequence of the self-supervised pre-training objective. A more in-depth analysis of the feature representations at different layers, perhaps using techniques like t-SNE or UMAP, would be beneficial.

2. The paper lacks an ablation study on the design of the COMM framework. For example, the authors did not compare different merging strategies, such as concatenation or attention-based merging, and did not explore the impact of different MLP architectures. The choice of a simple linear layer followed by an MLP for alignment seems arbitrary. It would be valuable to see a comparison of different alignment methods, such as using a cross-attention mechanism or a more sophisticated non-linear transformation. Furthermore, the paper does not explore the sensitivity of the model to the number of layers used from each visual encoder. It is possible that only a subset of the layers from each encoder are most relevant for the downstream tasks.

### Suggestions

The authors should conduct a more thorough investigation into the properties of DINOv2's learned representations. Specifically, they should explore the feature space of DINOv2 at different layers using dimensionality reduction techniques like t-SNE or UMAP. This would allow for a visual inspection of how the features evolve from shallow to deep layers and whether the claim of better global understanding is supported by the structure of these representations. For example, do the features in deeper layers cluster more according to semantic categories? Do they exhibit more robustness to image transformations? Quantifying these aspects would provide a more concrete understanding of the observed behavior. Furthermore, the authors should investigate the impact of different pre-training objectives on the learned representations. For example, how would a model trained with a contrastive loss or a masked image modeling objective perform in terms of global understanding? This would help to isolate the effect of the pre-training objective from the architecture of the model itself.

In addition to the analysis of DINOv2, the paper needs a more comprehensive ablation study of the COMM framework. The authors should compare different merging strategies, such as concatenation, attention-based merging, or even a simple averaging approach. This would help to determine the optimal way to combine the features from CLIP and DINOv2. Moreover, the authors should explore different MLP architectures for the alignment layer. For example, they could use a wider or deeper MLP, or they could use a different activation function. The authors should also investigate the impact of the number of layers used from each visual encoder. It is possible that only a subset of the layers from each encoder are most relevant for the downstream tasks. A systematic exploration of these design choices would make the paper more robust and provide a better understanding of the proposed method. The authors should also consider using a more sophisticated alignment method, such as cross-attention, which could allow for a more flexible and potentially more effective way to align the feature spaces of the two encoders.

Finally, the authors should provide a more detailed analysis of the computational cost of the proposed method. The authors should compare the training time and inference time of COMM with other methods. This is important for practical applications, as it is often necessary to balance performance with computational efficiency. The authors should also discuss the memory requirements of the proposed method, as this can be a limiting factor for large-scale applications. A thorough analysis of the computational cost would make the paper more practical and useful for the community.

### Questions

Please see the weakness.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

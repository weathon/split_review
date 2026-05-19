### Summary

This paper investigates the effectiveness of different visual encoders in multi-modal large language models. The authors have discovered that shallow layers of CLIP provide good performance for grounding and object positioning, while DINOv2's deep layers excel in global understanding. Based on this, this paper proposes COMM, which combines the shallow layers of CLIP with the deep layers of DINOv2 and aligns them using an MLP. The COMM has achieved good results on multiple tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The authors have conducted a detailed analysis of different visual encoders, and discovered that DINOv2's deep layers are better at global understanding than shallow layers, which is contrary to the common understanding that shallow layers are more effective for fine-grained understanding.
2. The authors have proposed a COMM framework that combines the advantages of different visual encoders. The proposed method has achieved good results on multiple tasks.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the reasons why DINOv2's deep layers are better at global understanding than shallow layers. The authors only mentioned that the pre-training objective of DINOv2 is to learn a representation that is invariant to different views of the same image, but did not explain why this leads to better global understanding. It is unclear if this is due to the model learning to capture more abstract features at deeper layers, or if it is simply a consequence of the self-supervised pre-training objective. A more in-depth analysis of the feature representations at different layers, perhaps using techniques like t-SNE or UMAP, would be beneficial.
2. The paper lacks an ablation study on the design of the COMM framework. For example, the authors did not compare different merging strategies, such as concatenation or attention-based merging, and did not explore the impact of different MLP architectures. The choice of a simple linear layer followed by an MLP for alignment seems arbitrary. It would be valuable to see a comparison of different alignment methods, such as using a cross-attention mechanism or a more sophisticated non-linear transformation. Furthermore, the paper does not explore the sensitivity of the model to the number of layers used from each visual encoder. It is possible that only a subset of the layers from each encoder are most relevant for the downstream tasks.

### Suggestions

The paper would benefit significantly from a more thorough investigation into the properties of DINOv2's learned representations. Specifically, the authors should explore the feature space of DINOv2 at different layers using dimensionality reduction techniques like t-SNE or UMAP. This would allow for a visual inspection of how the features evolve from shallow to deep layers and whether the claim of better global understanding is supported by the structure of these representations. For example, do the features in deeper layers cluster more according to semantic categories? Do they exhibit more robustness to image transformations? Quantifying these aspects would provide a more concrete understanding of the observed behavior. Furthermore, the authors should investigate the impact of different pre-training objectives on the learned representations. For example, how would a model trained with a contrastive loss or a masked image modeling objective perform in terms of global understanding? This would help to isolate the effect of the pre-training objective from the architecture of the model itself.

In addition to the analysis of DINOv2, the paper needs a more comprehensive ablation study of the COMM framework. The authors should compare different merging strategies, such as concatenation, attention-based merging, or even a simple averaging approach. This would help to determine the optimal way to combine the features from CLIP and DINOv2. Moreover, the authors should explore different MLP architectures for the alignment layer. For example, they could use a wider or deeper MLP, or they could use a different activation function. The authors should also investigate the impact of the number of layers used from each visual encoder. It is possible that only a subset of the layers from each encoder are most relevant for the downstream tasks. A systematic exploration of these design choices would make the paper more robust and provide a better understanding of the proposed method. The authors should also consider using a more sophisticated alignment method, such as cross-attention, which could allow for a more flexible and potentially more effective way to align the feature spaces of the two encoders.

Finally, the paper should include a more detailed analysis of the computational cost of the proposed method. The authors should compare the training time and inference time of COMM with other methods. This is important for practical applications, as it is often necessary to balance performance with computational efficiency. The authors should also discuss the memory requirements of the proposed method, as this can be a limiting factor for large-scale applications. A thorough analysis of the computational cost would make the paper more practical and useful for the community.

### Questions

1. The authors mention that DINOv2's deep layers are better at global understanding, but do not provide an analysis of the reasons. I am curious whether the authors have analyzed the feature space of DINOv2 and found that the features in the deep layers are more semantically meaningful than those in the shallow layers.
2. The COMM framework proposed in the paper is relatively simple. I am curious whether the authors have tried other merging strategies or alignment methods.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

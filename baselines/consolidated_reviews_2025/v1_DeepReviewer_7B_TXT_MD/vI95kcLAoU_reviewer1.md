### Summary

This paper proposes to reduce the computation of self-attention in ViT by reusing the self-attention results from the previous layers. The proposed method is very simple and effective. The authors conduct experiments on various tasks to demonstrate the effectiveness of the proposed method.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed method is simple and effective. It can be easily applied to various ViT-based models and tasks.
2. The authors conduct extensive experiments to demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The authors claim that the proposed method is orthogonal to existing efficient methods, such as MobileViT, MobileNeXt, etc. However, the authors do not compare with these methods. It is unclear how the proposed method compares in terms of computational cost and performance trade-offs with these existing efficient ViT architectures. The claim of orthogonality is not sufficiently supported by experimental evidence, as it is not shown how the proposed method interacts with or complements these other efficiency-focused approaches.
2. The authors only compare with the baseline ViT. It is unclear how the proposed method compares with other efficient ViT methods, such as MobileViT, MobileNeXt, etc. The lack of comparison with other efficient ViT methods makes it difficult to assess the true novelty and effectiveness of the proposed approach. It is important to understand if the performance gains are due to the proposed method or simply the skipping of attention layers, which could be a general strategy for improving efficiency.

### Suggestions

The paper would benefit significantly from a more thorough comparison with existing efficient ViT architectures. Specifically, the authors should include experiments that directly compare their method with models like MobileViT and MobileNeXt, using the same experimental setup and evaluation metrics. This would help to clarify the advantages and disadvantages of the proposed method compared to other approaches that also aim to reduce computational cost. It is important to understand if the proposed method offers a unique advantage or if it is simply another way to achieve similar results. The authors should also investigate the performance of their method when combined with other efficiency techniques, such as pruning or quantization, to demonstrate its orthogonality more clearly.

Furthermore, the authors should provide a more detailed analysis of the computational cost of their method. While the paper mentions that the method is efficient, it would be beneficial to include a breakdown of the FLOPs and memory usage for different layers and configurations. This would allow for a more precise comparison with other methods and help to identify the specific layers or operations that contribute most to the computational savings. The authors should also investigate the impact of the proposed method on the model's generalization performance, especially when applied to different tasks and datasets. It is important to ensure that the method does not compromise the model's ability to generalize to new data.

Finally, the authors should explore the limitations of their method. For example, it would be interesting to see how the method performs on very large-scale models or datasets. It is also important to understand the sensitivity of the method to different hyperparameters and training strategies. A more comprehensive analysis of these aspects would help to provide a more complete picture of the method's strengths and weaknesses and would make the paper more valuable to the research community.

### Questions

See weakness.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

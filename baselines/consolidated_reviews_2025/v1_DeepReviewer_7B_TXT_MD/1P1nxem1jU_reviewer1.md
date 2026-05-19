### Summary

This paper proposes a new graph data augmentation method based on spectral perspective. Specifically, the method selectively modifies the high-frequency components of the graph's Laplacian matrix while preserving the low-frequency components. The authors provide a theoretical analysis of the relationship between graph properties and the graph spectrum. They also conduct extensive experiments to demonstrate the effectiveness of their method.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a thorough theoretical analysis of the relationship between graph properties and the graph spectrum.
3. The proposed method is simple yet effective.

### Weaknesses

#### Some Related Works

[1] Graph random neural networks
[2] Graph Masking for Graph Neural Networks
[3] Graph Masked Autoencoder
[4] Graph Structure Learning with Interpretable Regularization
[5] Graph Structure Learning via Bilevel Programming
[6] Graph structure learning with self-supervision
[7] Graph structure learning with graph neural networks

#### comment

1. The paper lacks a comparison with some relevant graph augmentation methods, such as Graph Random Neural Networks [1], Graph Masking for Graph Neural Networks [2], Graph Masked Autoencoder [3], Graph Structure Learning with Interpretable Regularization [4], Graph Structure Learning via Bilevel Programming [5], Graph Structure Learning with Self-Supervision [6], and Graph Structure Learning with Graph Neural Networks [7]. These methods also focus on graph augmentation, and a comparison would help to better position the proposed method within the existing literature.

2. The authors should provide a more detailed explanation of how the proposed method can be applied to graph classification tasks. Specifically, it is unclear how the augmented graphs are used in the classification process. Are the augmented graphs used as input to the classifier, or are they used to generate new graph representations that are then classified? A clear description of this process is needed.

3. The authors should provide a more detailed discussion of the limitations of the proposed method. For example, under what conditions might the method fail to produce effective augmentations? Are there specific types of graphs or graph properties for which the method is not well-suited? Addressing these limitations would provide a more balanced view of the method's applicability.

### Suggestions

The paper would benefit from a more thorough comparison with existing graph augmentation techniques. While the authors mention that their method is spectral-based, it is crucial to understand how it compares to other approaches in terms of performance and computational cost. For instance, methods like Graph Random Neural Networks [1] and Graph Masking for Graph Neural Networks [2] also aim to improve graph representations through augmentation, but they operate in the spatial domain. A detailed comparison should not only focus on the final performance metrics but also on the underlying mechanisms of augmentation. It would be valuable to see a discussion on the trade-offs between spectral and spatial augmentation methods, and how the proposed method addresses the limitations of existing approaches. Furthermore, the comparison should include a discussion of the computational complexity of the proposed method compared to other augmentation techniques, as this is an important factor for practical applications.

To clarify the application of the proposed method to graph classification, the authors should provide a step-by-step explanation of the process. For example, if the augmented graphs are used as input to the classifier, the authors should explain how the augmented graphs are incorporated into the training process. If the method generates new graph representations, the authors should describe how these representations are obtained and used for classification. A concrete example, perhaps using a simple graph classification task, would greatly enhance the clarity of the explanation. This should include a description of how the augmentation parameters are chosen and how they affect the final classification performance. It would also be helpful to discuss the sensitivity of the method to different augmentation parameters and how these parameters can be tuned for optimal performance.

Finally, the authors should provide a more comprehensive discussion of the limitations of their method. This should include an analysis of the types of graphs or graph properties for which the method might not be effective. For example, it would be useful to discuss whether the method is suitable for graphs with specific structural properties, such as high clustering coefficients or certain types of node degree distributions. The authors should also discuss the potential impact of the method's parameters on its performance and whether there are any constraints on these parameters. A more thorough analysis of the limitations would provide a more balanced view of the method's applicability and help guide future research in this area. It would also be beneficial to discuss potential avenues for future research, such as exploring adaptive parameter selection or combining the proposed method with other graph augmentation techniques.

### Questions

Please see the weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

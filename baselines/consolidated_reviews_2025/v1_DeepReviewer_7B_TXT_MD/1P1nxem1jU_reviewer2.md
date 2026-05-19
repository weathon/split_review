### Summary

This paper proposes a novel graph data augmentation method, called Dual-Prism (DP), from a spectral perspective. The authors introduce DP-Noise and DP-Mask, which selectively modify the high-frequency components of the graph's Laplacian matrix while preserving the low-frequency components. The authors conduct extensive experiments to demonstrate the effectiveness of their proposed method.

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


#### comment

1. The paper lacks a comparison with some relevant graph augmentation methods, such as Graph Random Neural Networks (GRAND) [1], Graph Masking for Graph Neural Networks [2], Graph Masked Autoencoder [3], Graph Structure Learning with Interpretable Regularization [4], Graph Structure Learning via Bilevel Programming [5], Graph Structure Learning with Self-Supervision [6], and Graph Structure Learning with Graph Neural Networks [7]. These methods also focus on graph augmentation, and a comparison would help to better position the proposed method within the existing literature.

2. The authors should provide a more detailed explanation of how the proposed method can be applied to graph classification tasks. Specifically, it is unclear how the augmented graphs are used in the classification process. Are the augmented graphs used as input to the classifier, or are they used to generate new graph representations that are then classified? A clear description of this process is needed.

3. The authors should provide a more detailed discussion of the limitations of the proposed method. For example, under what conditions might the method fail to produce effective augmentations? Are there specific types of graphs or graph properties for which the method is not well-suited? Addressing these limitations would provide a more balanced view of the method's applicability.

### Suggestions

The paper would significantly benefit from a more thorough comparison with existing graph augmentation techniques. While the authors position their method as a spectral approach, it's crucial to understand how it compares to methods that operate in the spatial domain. For instance, methods like Graph Random Neural Networks (GRAND) and Graph Masking for Graph Neural Networks (GMN) also aim to improve graph representations through augmentation, but they do so by modifying the graph structure or node features directly. A detailed comparison should not only focus on the final performance metrics but also on the underlying mechanisms of augmentation. It would be valuable to see a discussion on the trade-offs between spectral and spatial augmentation methods, and how the proposed method addresses the limitations of existing approaches. This comparison should include a discussion of the computational complexity of each method, as well as their sensitivity to different graph properties. Furthermore, the authors should clarify how their method handles different types of graph data, such as those with varying degrees of homophily or heterophily, and whether the method is equally effective across these different graph structures.

To enhance the clarity of the paper, the authors should provide a more detailed explanation of how the proposed method is applied to graph classification tasks. Specifically, the paper should clearly articulate how the augmented graphs are used in the classification process. Are the augmented graphs used as input to the classifier, or are they used to generate new graph representations that are then classified? A concrete example, perhaps using a simple graph classification task, would greatly enhance the reader's understanding. The authors should also discuss the impact of the augmentation parameters on the final classification performance. For example, how does the choice of the number of high-frequency components to modify affect the classification accuracy? A sensitivity analysis of these parameters would be beneficial. Furthermore, the authors should clarify whether the augmentation is applied to the training set only, or to both the training and test sets, and what the implications of this choice are.

Finally, the authors should provide a more comprehensive discussion of the limitations of their method. This discussion should include an analysis of the types of graphs or graph properties for which the method might not be effective. For example, are there specific graph structures or node degree distributions for which the method performs poorly? Are there any constraints on the parameters of the method that could affect its performance? A more thorough analysis of these limitations would provide a more balanced view of the method's applicability and help guide future research. The authors should also discuss potential avenues for future research, such as exploring adaptive parameter selection or combining the proposed method with other graph augmentation techniques. This would help to position the method within the broader context of graph data augmentation and highlight its potential for future development.

### Questions

See the weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

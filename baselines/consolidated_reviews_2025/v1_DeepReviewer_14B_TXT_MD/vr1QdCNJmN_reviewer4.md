### Summary

This paper introduces a novel class of divergences on discrete spaces, called difference-of-submodular Bregman divergences (DBDs), which are more expressive than submodular Bregman divergences. The authors show that the DBD is a proper divergence, satisfying the non-negativity and identity-of-indiscernibles properties. They also show that the expressive power of the DBD increases with the richness of the set function class. The authors propose a learnable form of the DBD using permutation-invariant neural networks (NNs), particularly epsilon-PointNet. They demonstrate the effectiveness of the DBD in clustering and set retrieval tasks on the ModelNet40 dataset, showing that it outperforms existing submodular Bregman divergences.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper introduces a novel class of divergences on discrete spaces, called difference-of-submodular Bregman divergences (DBDs), which are more expressive than submodular Bregman divergences.
- The authors provide theoretical guarantees that the DBD is a proper divergence, satisfying the non-negativity and identity-of-indiscernibles properties.
- The paper shows that the expressive power of the DBD increases with the richness of the set function class.
- The authors propose a learnable form of the DBD using permutation-invariant neural networks (NNs), particularly epsilon-PointNet.
- The paper demonstrates the effectiveness of the DBD in clustering and set retrieval tasks on the ModelNet40 dataset, showing that it outperforms existing submodular Bregman divergences.
- The paper is well-written and clearly presents the theoretical results and experimental findings.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational complexity of the proposed method.
- The paper does not compare the proposed method with other state-of-the-art methods for clustering and set retrieval tasks.
- The paper does not provide a detailed analysis of the sensitivity of the proposed method to the choice of hyperparameters.
- The paper does not provide a detailed analysis of the limitations of the proposed method.

### Suggestions

The paper introduces an interesting class of divergences, but it would benefit from a more thorough analysis of its practical implications. Specifically, a detailed computational complexity analysis is needed, going beyond just stating the exponential complexity of finding the DS decomposition. The authors should provide a breakdown of the computational cost associated with each step of their algorithm, including the evaluation of the submodular functions, the computation of the Bregman divergence, and the training of the neural networks. This analysis should consider the impact of the size of the ground set and the dimensionality of the feature space on the overall runtime and memory requirements. Furthermore, it would be beneficial to explore potential approximations or heuristics that could mitigate the computational burden, especially for large-scale datasets. For example, could greedy algorithms or other optimization techniques be used to find approximate DS decompositions? A discussion of these practical considerations would greatly enhance the paper's impact.

In addition to the computational analysis, a more comprehensive experimental evaluation is necessary. The paper should compare the proposed method with a wider range of state-of-the-art clustering and set retrieval algorithms, including those based on other divergence measures or distance metrics. This comparison should not only focus on the final performance metrics but also on the convergence speed, robustness to noise, and sensitivity to the choice of hyperparameters. Furthermore, the authors should consider evaluating their method on a variety of datasets with different characteristics, such as varying sizes, dimensionality, and underlying structures. This would provide a more complete picture of the method's strengths and weaknesses and its applicability to different real-world scenarios. The current evaluation on ModelNet40 is a good starting point, but more extensive experiments are needed to fully validate the proposed approach.

Finally, the paper should provide a more detailed analysis of the sensitivity of the proposed method to the choice of hyperparameters. This analysis should include a systematic exploration of the hyperparameter space, using techniques such as grid search or random search, and should report the impact of different hyperparameter settings on the final performance. The authors should also discuss the potential trade-offs between different hyperparameter choices and provide guidelines for selecting appropriate values for different datasets and tasks. Furthermore, a discussion of the limitations of the proposed method is needed, including scenarios where it might not perform well or where alternative approaches might be more suitable. This would provide a more balanced and nuanced view of the proposed method and its potential impact.

### Questions

- Can you provide a detailed analysis of the computational complexity of the proposed method?
- Can you compare the proposed method with other state-of-the-art methods for clustering and set retrieval tasks?
- Can you provide a detailed analysis of the sensitivity of the proposed method to the choice of hyperparameters?
- Can you provide a detailed analysis of the limitations of the proposed method?

### Rating

6

### Confidence

3

**********

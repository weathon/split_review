### Summary

The paper studies the universal approximation property of permutation-invariant neural networks. The authors prove that such networks can approximate any continuous function with arbitrary precision. The paper also presents numerical experiments to support the theoretical findings.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The theoretical results are novel and provide new insights into the universal approximation property of neural networks.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not discuss the limitations of the proposed method. It would be helpful to provide a more comprehensive discussion of the limitations and potential future work.
2. The paper does not compare the proposed method with existing methods. It would be helpful to provide a more comprehensive comparison of the proposed method with existing methods.
3. The paper does not provide a detailed analysis of the computational complexity of the proposed method. It would be helpful to provide a more detailed analysis of the computational complexity of the proposed method.

### Suggestions

The paper would benefit significantly from a more thorough discussion of its limitations. While the theoretical results are interesting, it is crucial to understand the practical constraints of the proposed permutation-invariant neural networks. For example, the paper should discuss the potential challenges in training such networks, such as the non-convexity of the loss landscape or the difficulty in finding good initialization strategies. Furthermore, the paper should explore the scalability of the proposed method to larger networks and datasets. It would be helpful to analyze the computational cost of the proposed method and compare it with existing methods. This analysis should include both the training and inference costs. The paper should also discuss the potential impact of the permutation-invariant property on the generalization performance of the network. It is important to understand whether the permutation-invariance constraint might limit the network's ability to learn complex patterns in the data. A detailed discussion of these limitations would provide a more balanced view of the proposed method and guide future research in this area.

In addition to the limitations, the paper needs a more comprehensive comparison with existing methods. The paper should clearly articulate the advantages and disadvantages of the proposed method compared to other approaches for universal approximation. For example, the paper should compare the proposed method with standard neural networks that use random initialization. It would be helpful to analyze the performance of the proposed method in terms of approximation accuracy, training time, and generalization ability. The paper should also discuss the potential benefits of using permutation-invariant networks in specific applications. For example, the paper could explore the use of permutation-invariant networks in tasks where the input data has a natural permutation symmetry. A detailed comparison with existing methods would help to position the proposed method within the broader context of neural network research and highlight its unique contributions. The paper should also discuss the potential for combining the proposed method with other techniques, such as data augmentation or regularization, to further improve its performance.

Finally, the paper should provide a more detailed analysis of the computational complexity of the proposed method. While the paper mentions the use of a specific type of basis function, it does not provide a detailed analysis of the computational cost of the proposed method. The paper should analyze the time and space complexity of the proposed method and compare it with existing methods. This analysis should include both the training and inference costs. The paper should also discuss the potential impact of the choice of basis function on the computational complexity of the proposed method. It would be helpful to analyze the trade-off between the approximation accuracy and the computational cost of the proposed method. A detailed analysis of the computational complexity would provide a more complete understanding of the proposed method and help to assess its practical applicability.

### Questions

See weaknesses.

### Rating

5

### Confidence

3

**********

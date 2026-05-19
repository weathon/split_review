### Summary

The paper studies the universal approximation property of permutation-invariant neural networks. The authors prove that such networks can approximate any continuous function with arbitrary precision. The paper also presents numerical experiments to support the theoretical findings.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

The paper is well-written and easy to follow. The theoretical results are novel and provide new insights into the universal approximation property of neural networks. The numerical experiments are well-designed and provide strong support for the theoretical findings.

### Weaknesses

#### Some Related Works


#### comment

The paper does not discuss the limitations of the proposed method. It would be helpful to provide a more comprehensive discussion of the limitations and potential future work.

The paper does not compare the proposed method with existing methods. It would be helpful to provide a more comprehensive comparison of the proposed method with existing methods.

The paper does not provide a detailed analysis of the computational complexity of the proposed method. It would be helpful to provide a more detailed analysis of the computational complexity of the proposed method.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations of the proposed permutation-invariant neural network architecture. While the authors demonstrate universal approximation capabilities, it is crucial to acknowledge the practical constraints that might arise. For instance, the specific choice of basis functions and their associated parameters could limit the applicability of the method to certain types of problems or datasets. A discussion on the potential challenges in training such networks, such as the non-convexity of the loss landscape or the difficulty in finding good initialization strategies, would be valuable. Furthermore, the paper should address the scalability of the proposed method to larger networks and datasets. It would be beneficial to analyze the computational cost of the proposed method and compare it with existing methods. This analysis should include both the training and inference costs, and should consider the impact of the choice of basis function on the computational complexity. 

To strengthen the paper, a more comprehensive comparison with existing methods is needed. The authors should clearly articulate the advantages and disadvantages of their proposed method compared to other approaches for universal approximation. For example, the paper should compare the proposed method with standard neural networks that use random initialization, highlighting the trade-offs between permutation invariance and other properties such as generalization ability and training time. The paper should also discuss the potential benefits of using permutation-invariant networks in specific applications, such as tasks where the input data has a natural permutation symmetry. A detailed comparison with existing methods would help to position the proposed method within the broader context of neural network research and highlight its unique contributions. This comparison should include both theoretical and empirical aspects, and should consider the practical implications of the proposed method.

Finally, the paper should provide a more detailed analysis of the computational complexity of the proposed method. While the authors mention the use of a specific type of basis function, they do not provide a detailed analysis of the computational cost of the proposed method. The paper should analyze the time and space complexity of the proposed method and compare it with existing methods. This analysis should include both the training and inference costs, and should consider the impact of the choice of basis function on the computational complexity. It would be helpful to provide a theoretical analysis of the computational complexity, as well as empirical results that demonstrate the practical performance of the proposed method. This analysis should be presented in a clear and concise manner, and should be supported by appropriate experimental data.

### Questions

See weaknesses.

### Rating

6

### Confidence

2

**********

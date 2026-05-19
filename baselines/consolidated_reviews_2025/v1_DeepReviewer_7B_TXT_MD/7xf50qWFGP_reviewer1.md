### Summary

This paper studies the problem of representation learning in RL, specifically the Laplacian-based framework. The authors propose an online Laplacian-based representation learning method, where the graph-based representation is updated simultaneously with the policy. The authors provide theoretical analysis of the proposed method, and evaluate the performance of the proposed method on grid-world environments.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The proposed online Laplacian-based representation learning method is novel, to the best of my knowledge.
2. The theoretical analysis of the proposed method is comprehensive.

### Weaknesses

#### Some Related Works

[1] Representation learning in reinforcement learning with weighted importance sampling
[2] Revisiting generalization in reinforcement learning with general value functions
[3] Contrastive learning for offline reinforcement learning and inference

#### comment

1. The motivation of the proposed method is not clear. The authors claim that "The non-uniqueness of the fixed representation may not be effective for the policies encountered during RL". However, the non-uniqueness of the fixed representation is a well-known issue in the literature of representation learning in RL, and it is well-known that representation learning methods can learn unique representations under certain conditions (e.g., [1,2]). The authors should clarify why the non-uniqueness of the fixed representation is a problem in their specific context, and how their method addresses this issue. It is not clear how the proposed method avoids the pitfalls of existing representation learning methods that do achieve uniqueness under certain conditions.
2. The empirical evaluation is limited. The authors only evaluate their method on grid-world environments. The authors should evaluate their method on more complex environments, such as those in the D4RL benchmark. The current evaluation is insufficient to demonstrate the effectiveness of the proposed method in more challenging settings. The lack of comparison with existing representation learning methods is also a significant weakness.
3. The presentation of the paper can be improved. The authors should provide more intuition behind the proposed method and the theoretical analysis. The current presentation is dense and difficult to follow. The authors should also provide more details on the implementation of the proposed method, and the experimental setup.

### Suggestions

The authors should provide a more detailed explanation of the motivation behind their proposed method. Specifically, they need to clarify why the non-uniqueness of fixed representations is a problem in their context, especially given that methods exist to achieve unique representations under certain conditions. A more thorough discussion of the limitations of existing representation learning methods in the context of online updates is needed. The authors should also explain how their method avoids the pitfalls of these existing methods. For example, they could discuss the specific properties of their method that prevent the non-unique representations that are often observed in fixed representation methods. This discussion should be grounded in the existing literature and should clearly articulate the advantages of their approach over existing methods.

To strengthen the empirical evaluation, the authors should include experiments on more complex environments, such as those found in the D4RL benchmark. This would demonstrate the scalability and robustness of their method. Furthermore, the authors should compare their method against existing representation learning methods, both fixed and online, to provide a clear understanding of its performance relative to the state-of-the-art. This comparison should include a discussion of the strengths and weaknesses of each method. The authors should also provide a more detailed description of the experimental setup, including the specific hyperparameters used and the training procedures. This would allow for better reproducibility and a more thorough understanding of the results.

Finally, the authors should improve the presentation of the paper by providing more intuition behind the proposed method and the theoretical analysis. This could include more detailed explanations of the key concepts and a more intuitive description of the mathematical derivations. The authors should also provide more details on the implementation of the proposed method, including the specific algorithms used and the data structures employed. This would make the paper more accessible to a wider audience and would allow for easier reproducibility. The authors should also consider adding more visualizations to help illustrate the behavior of their method.

### Questions

1. What is the difference between the proposed method and the representation learning method in [3]?
2. How does the proposed method compare to other representation learning methods in terms of performance and computational cost?

### Rating

3

### Confidence

3

**********

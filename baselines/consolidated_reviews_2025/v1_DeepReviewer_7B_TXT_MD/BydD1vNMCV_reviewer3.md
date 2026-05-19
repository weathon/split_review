### Summary

This paper proposes a stochastic neural network (StoNet) to bridge the gap between linear models and deep neural networks (DNNs). StoNet is a probabilistic deep learning model that is asymptotically equivalent to the DNN in function approximation. The authors show that the sparse learning theory and methods developed for linear models can be adapted to the StoNet. They also propose a recursive method to quantify the prediction uncertainty for the StoNet. The proposed method is evaluated on several datasets and compared with conformal inference on extensive examples, demonstrating its superiority.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. The authors provide a thorough literature review on StoNet and its connection to DNNs. The authors also provide a detailed description of the numerical experiments and their results.

2. The proposed recursive method for uncertainty quantification is novel and can be used to improve the reliability of DNN predictions.

### Weaknesses

#### Some Related Works


#### comment

1. The authors claim that they are the first to establish the consistency theory supporting the usage of the Lasso penalty for the DNN. However, the authors do not provide any formal proof of this claim. It is unclear how the consistency theory for Lasso in linear models directly translates to DNNs, especially considering the non-convex optimization landscape of DNNs. The paper needs to clarify the specific conditions under which the Lasso penalty is consistent for DNNs, and how these conditions relate to the practical training of DNNs.

2. The authors claim that the proposed StoNet can be used to quantify the prediction uncertainty for large-scale DNNs. However, the authors do not provide any theoretical analysis of the computational complexity of the proposed method. It is unclear how the method scales with the size of the DNN and the dataset. The paper should include a discussion of the computational cost of the proposed method, and how it compares to existing uncertainty quantification methods for DNNs.

### Suggestions

The paper would benefit from a more rigorous treatment of the consistency theory for the Lasso penalty in the context of DNNs. Specifically, the authors should provide a formal proof or a detailed argument outlining the conditions under which the Lasso penalty is consistent for DNNs. This should include a discussion of how the non-convex optimization landscape of DNNs affects the consistency results. Furthermore, the authors should clarify how the consistency results for linear models can be extended to DNNs, and what specific assumptions are needed to make this extension valid. It would be helpful to provide a concrete example of a DNN architecture and show how the consistency theory applies to that specific case. The authors should also discuss the limitations of the consistency theory and the scenarios where it might not hold.

To address the concerns about computational complexity, the authors should provide a detailed analysis of the time and space complexity of the proposed method. This analysis should include a breakdown of the computational cost of each step in the algorithm, and how it scales with the size of the DNN, the dataset, and the number of iterations. The authors should also compare the computational cost of their method to existing uncertainty quantification methods for DNNs, such as Monte Carlo dropout and deep ensembles. It would be beneficial to provide a table or a graph that shows the computational cost of the proposed method and other methods as a function of the size of the DNN and the dataset. The authors should also discuss the practical implications of the computational cost, and how it affects the applicability of the method to large-scale problems.

Finally, the authors should provide a more detailed explanation of how the proposed method can be used to quantify prediction uncertainty for large-scale DNNs. This should include a discussion of the specific steps involved in the method, and how these steps can be implemented efficiently. The authors should also provide a concrete example of how the method can be applied to a large-scale DNN, and show the results of the uncertainty quantification. The authors should also discuss the limitations of the method and the scenarios where it might not be suitable. It would be helpful to provide a comparison of the uncertainty quantification results obtained by the proposed method and other methods, such as Monte Carlo dropout and deep ensembles. This comparison should include a discussion of the advantages and disadvantages of the proposed method compared to other methods.

### Questions

1. The authors claim that they are the first to establish the consistency theory supporting the usage of the Lasso penalty for the DNN. However, the authors do not provide any formal proof of this claim. Can the authors provide a formal proof or a detailed argument to support this claim?

2. The authors claim that the proposed StoNet can be used to quantify the prediction uncertainty for large-scale DNNs. However, the authors do not provide any theoretical analysis of the computational complexity of the proposed method. Can the authors provide a theoretical analysis of the computational complexity of the proposed method?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

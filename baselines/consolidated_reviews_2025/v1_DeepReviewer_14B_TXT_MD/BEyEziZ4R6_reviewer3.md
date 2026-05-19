### Summary

This paper proposes a new method for DP-SGD that avoids the need for per-sample gradient clipping. The main idea is to use Lipschitz constrained networks to provide sensitivity bounds. The authors establish a link between the Lipschitz constant with respect to the inputs and the one with respect to the parameters. By bounding the Lipschitz constant of each layer with respect to its parameters, they show that it is possible to train these networks with privacy guarantees. The proposed method is evaluated on several datasets and compared to existing DP-SGD approaches.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is novel and interesting.
- The experimental results are promising and show that the proposed method can achieve good performance while providing privacy guarantees.
- The paper provides a theoretical analysis of the proposed method, which is a strength.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed comparison of the proposed method with existing approaches in terms of computational cost and memory requirements.
- The paper does not discuss the limitations of the proposed method and potential directions for future research.

### Suggestions

The paper would benefit from a more thorough analysis of the computational overhead introduced by the Lipschitz constraint. While the authors mention that their method avoids per-sample gradient clipping, it is crucial to quantify the computational cost of enforcing the Lipschitz constraint during training. Specifically, the paper should provide a breakdown of the time spent on different operations, such as computing the Lipschitz constants, projecting the weights, and performing the forward and backward passes. This analysis should be compared to the computational cost of standard DP-SGD with per-sample clipping. Furthermore, the memory requirements of the proposed method should be explicitly stated, including the memory needed to store the Lipschitz constants and any additional data structures. A detailed comparison with existing methods in terms of both computational cost and memory usage would allow readers to better understand the trade-offs of the proposed approach.

In addition to computational cost, the paper should also discuss the limitations of the proposed method in terms of its applicability to different network architectures and datasets. For example, it is unclear how the Lipschitz constraint would affect the performance of very deep networks or networks with complex activation functions. The authors should also discuss the potential challenges of applying their method to datasets with high dimensionality or large numbers of classes. Furthermore, the paper should explore the sensitivity of the proposed method to the choice of the Lipschitz constant. It would be beneficial to investigate how the performance of the method varies with different values of the Lipschitz constant and provide guidelines for selecting an appropriate value. A more comprehensive discussion of these limitations would help readers understand the scope of the proposed method and identify potential areas for future research.

Finally, the paper should provide more specific directions for future research. While the authors mention that their method is not applicable to all network architectures, they should provide more details on the types of architectures that are not compatible with their approach. For example, they could discuss the challenges of applying their method to recurrent neural networks or transformers. Furthermore, the paper should explore potential ways to extend their method to handle these types of architectures. The authors should also discuss the potential of combining their method with other privacy-preserving techniques, such as federated learning or homomorphic encryption. A more detailed discussion of these future directions would help guide future research in this area and highlight the potential impact of the proposed method.

### Questions

- How does the proposed method compare to existing approaches in terms of computational cost and memory requirements?
- What are the limitations of the proposed method, and what are the potential directions for future research?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

### Summary

The paper proposes a unified framework for concept-based models that can perform concept correction and conditional interpretation. The framework is based on energy-based models that define the joint energy of candidate (input, concept, class) tuples. The framework can be used for concept correction and conditional interpretation. Experiments on three datasets show that the proposed framework outperforms the state-of-the-art on concept correction and conditional interpretation.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well written and easy to follow. The proposed approach is novel and interesting.

### Weaknesses

#### Some Related Works


#### comment

The proposed approach is more complicated than the baselines. It is not clear whether the improvement in performance is due to the increased complexity or the proposed approach itself.

### Suggestions

The paper introduces a novel approach using energy-based models for concept correction and conditional interpretation, which is a promising direction. However, the current presentation lacks a detailed analysis of the computational overhead introduced by the proposed framework. Specifically, the paper should include a breakdown of the computational cost associated with each component of the model, such as the concept embedding network, the class embedding network, and the joint energy network. This would allow for a more precise understanding of the computational bottlenecks and potential areas for optimization. Furthermore, it would be beneficial to compare the training and inference time of the proposed method with the baselines, providing a more comprehensive evaluation of its practical applicability. The authors should also consider exploring techniques to reduce the computational complexity of the model, such as using more efficient neural network architectures or approximation methods for the energy function.

To further strengthen the paper, the authors should provide a more in-depth discussion of the limitations of the proposed approach. For example, the paper should address the potential sensitivity of the model to the choice of hyperparameters, the potential for overfitting, and the scalability of the approach to larger datasets and more complex models. It would also be useful to discuss the assumptions made by the model and the potential impact of these assumptions on the performance of the model. A thorough discussion of the limitations would provide a more balanced and realistic assessment of the proposed approach. Additionally, the paper should include a more detailed analysis of the performance of the proposed approach on different types of datasets and tasks, highlighting the strengths and weaknesses of the method in different scenarios. This would provide a more comprehensive understanding of the applicability of the proposed approach.

Finally, the paper should provide more details on the implementation of the proposed approach, including the specific choices of neural network architectures, the optimization algorithms used, and the training procedures. This would allow for better reproducibility of the results and facilitate future research in this area. The authors should also consider releasing the code and the trained models to the public, which would further enhance the impact of the paper. In addition, it would be beneficial to include a more detailed comparison with other state-of-the-art methods for concept-based learning, including both concept-based models and other related approaches. This would provide a more comprehensive evaluation of the proposed approach and highlight its advantages and disadvantages compared to existing methods.

### Questions

Please see the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

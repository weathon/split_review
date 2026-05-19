### Summary

This paper addresses the challenge of efficiently training a Transformer model with differential privacy guarantees. The authors propose a novel approach called DPFormer, which incorporates Phantom Clipping and a Re-Attention Mechanism to overcome the computational overhead associated with per-sample gradient clipping and unintentional attention distraction. Theoretical analysis and empirical results on real-world datasets demonstrate the effectiveness and efficiency of DPFormer in training differentially private Transformers.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper proposes a novel approach, DPFormer, which combines Phantom Clipping and a Re-Attention Mechanism to address the challenges of efficiently training differentially private Transformers. This approach is innovative and addresses a significant problem in the field of differentially private deep learning.
2. The theoretical analysis provided in the paper demonstrates the effectiveness of DPFormer in reducing computational costs during gradient clipping and mitigating attention distraction. This analysis provides a solid foundation for the proposed approach.
3. The empirical results on real-world datasets validate the efficiency and effectiveness of DPFormer. These results demonstrate the practical applicability of the proposed approach in scenarios where data is limited and domain-specific, and differential privacy is a crucial requirement.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on the application of DPFormer to Transformer models. It would be beneficial to explore the applicability of this approach to other deep learning architectures and tasks. Specifically, the paper lacks a discussion on how the proposed Phantom Clipping and Re-Attention Mechanism would interact with different architectural choices, such as convolutional layers or recurrent neural networks. The current analysis is limited to the Transformer's attention mechanism, and it is unclear if the benefits would translate to models without this specific component.
2. The paper could benefit from a more detailed comparison with existing differentially private training methods for Transformers. While the paper mentions the computational overhead of per-sample gradient clipping, it does not provide a thorough comparison with other techniques that aim to reduce this overhead, such as those based on moments accountant or other gradient perturbation methods. A more detailed analysis of the trade-offs between DPFormer and these existing methods would be valuable.
3. The paper could provide more insights into the practical implications of using DPFormer in real-world applications. For example, it would be helpful to discuss the potential impact of the proposed approach on model accuracy and training time in different scenarios. The paper should also address the potential challenges of deploying DPFormer in resource-constrained environments, such as mobile devices or edge computing platforms. Furthermore, the paper should discuss the sensitivity of the method to hyperparameter choices and how these choices might affect the privacy-utility trade-off.

### Suggestions

The paper should broaden its scope by investigating the applicability of DPFormer to a wider range of deep learning architectures. Specifically, the authors should explore how the Phantom Clipping and Re-Attention Mechanism can be adapted for models that do not rely on the Transformer's attention mechanism. For instance, how would these techniques be applied to convolutional neural networks (CNNs) or recurrent neural networks (RNNs)? This would involve a detailed analysis of how the clipping and re-attention mechanisms interact with the different layer types and activation functions. Furthermore, the authors should provide empirical results on these alternative architectures to demonstrate the generalizability of their approach. This would significantly strengthen the paper's contribution by showing that DPFormer is not limited to a specific architecture.

To enhance the paper's comparative analysis, the authors should include a more detailed comparison with existing differentially private training methods for Transformers. This should include a discussion of the computational overhead, privacy guarantees, and utility trade-offs of DPFormer compared to other techniques. For example, the paper should compare DPFormer with methods that use moments accountant or other gradient perturbation techniques. The comparison should not only focus on theoretical aspects but also include empirical results on benchmark datasets. This would allow readers to better understand the advantages and disadvantages of DPFormer compared to existing state-of-the-art methods. The authors should also discuss the limitations of their approach and identify scenarios where other methods might be more suitable.

Finally, the paper should provide a more in-depth discussion of the practical implications of using DPFormer in real-world applications. This should include a detailed analysis of the impact of the proposed approach on model accuracy and training time. The authors should also address the potential challenges of deploying DPFormer in resource-constrained environments. For example, how would the computational overhead of DPFormer affect its performance on mobile devices or edge computing platforms? Furthermore, the paper should discuss the sensitivity of the method to hyperparameter choices and how these choices might affect the privacy-utility trade-off. This would provide valuable insights for practitioners who are considering using DPFormer in their applications.

### Questions

1. Can the authors provide more insights into the computational overhead of DPFormer compared to other differentially private training methods for Transformers?
2. How does the performance of DPFormer vary with different privacy budgets and dataset sizes?
3. Can the authors discuss the potential challenges and limitations of deploying DPFormer in real-world applications, such as commercial recommender systems?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

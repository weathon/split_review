### Summary

This paper proposes a neuron-enhanced autoencoder matrix completion method (AEMC-NE) for collaborative filtering. A theoretical analysis is provided to investigate the generalization ability of AEMC-NE. The experimental results demonstrate the effectiveness of AEMC-NE.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1.	The paper provides a theoretical analysis for AEMC-NE to investigate its generalization ability.
2.	The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1.	The novelty of AEMC-NE is limited. It is a straightforward combination of AEMC and element-wise neural networks. The performance improvement comes from the increased number of parameters. The authors should compare AEMC-NE with AEMC of the same model size.
2.	The paper should include more recent baselines, such as Neural Collaborative Filtering (Neural CF) and Multi-Layer Perceptron (MLP).
3.	The paper should include more recent baselines, such as Neural Collaborative Filtering (Neural CF) and Multi-Layer Perceptron (MLP).

### Suggestions

The core concern with the proposed AEMC-NE method is its incremental nature. While the theoretical analysis is a positive aspect, the practical contribution is somewhat diminished by the fact that it appears to be a relatively straightforward extension of existing AEMC techniques by incorporating element-wise neural networks. The authors should rigorously demonstrate that the performance gains are not simply due to an increase in model capacity. A crucial experiment would involve a direct comparison with an AEMC model that has been scaled up to have a comparable number of parameters as the AEMC-NE. This would involve carefully adjusting the number of hidden units in the AEMC model to match the parameter count of the AEMC-NE, including both the main autoencoder and the element-wise networks. Without this comparison, it is difficult to ascertain whether the proposed method offers a genuine improvement in generalization or merely benefits from a larger model size. Furthermore, the authors should provide a more detailed analysis of the computational cost of AEMC-NE compared to the standard AEMC, as the addition of element-wise networks will inevitably increase the computational overhead. This analysis should include both training and inference time, as well as memory requirements.

To further strengthen the empirical evaluation, the authors should include a wider range of collaborative filtering baselines, particularly those that have demonstrated strong performance in recent years. Specifically, methods such as Neural Collaborative Filtering (Neural CF) and Multi-Layer Perceptron (MLP) based collaborative filtering should be included. These methods represent important benchmarks in the field and would provide a more comprehensive understanding of the performance of AEMC-NE in the context of the current state-of-the-art. The inclusion of these baselines would also help to clarify the specific advantages of AEMC-NE over more established collaborative filtering techniques. The experimental setup should be carefully described, including the hyperparameter tuning process for all methods, to ensure a fair comparison. The authors should also consider reporting additional evaluation metrics beyond RMSE, such as Mean Absolute Error (MAE) or precision/recall, to provide a more complete picture of the performance of the proposed method.

Finally, the paper would benefit from a more in-depth discussion of the limitations of the proposed approach. For example, the authors should discuss the potential sensitivity of AEMC-NE to the choice of hyperparameters, as well as its performance on datasets with different characteristics. It would also be beneficial to explore the interpretability of the learned element-wise networks, as this could provide insights into the underlying mechanisms of the proposed method. The authors should also consider the potential for overfitting, especially given the increased number of parameters in AEMC-NE. Addressing these limitations would provide a more balanced and nuanced view of the proposed method and its potential impact on the field.

### Questions

See Weaknesses.

### Rating

3: reject, not good enough

### Confidence

5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

**********

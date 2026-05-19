### Summary

This paper proposes a novel UDA framework for time series classification, called LOLO. LOLO utilizes both global and local features to enhance domain-invariant feature alignment. The authors introduce a new metric learning method based on DTW to improve the robustness of feature alignment across domains. Additionally, they employ adversarial learning and center alignment to further enhance the transferability of learned features. The experimental results demonstrate that LOLO outperforms state-of-the-art methods on four time series datasets.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a comprehensive comparison with previous works, demonstrating the effectiveness of the proposed method.
3. The authors conduct extensive ablation studies to analyze the impact of different components and loss functions.

### Weaknesses

#### Some Related Works


#### comment

1. The authors should provide more details about the selection of hyperparameters, including the learning rate, batch size, and the number of training epochs. Specifically, the sensitivity of the model to these parameters should be discussed, as this is crucial for reproducibility and practical application. The interaction between these hyperparameters and the model's performance should be analyzed, as different datasets might require different settings.
2. The authors should provide more details about the computational complexity of the proposed method. This should include a breakdown of the time and memory requirements for each component of the model, such as the local encoder, patching transformer, and fusion module. A comparison of the computational cost with other state-of-the-art methods would also be beneficial. Furthermore, the impact of the number of local encoders on the computational complexity should be discussed, as this is a key design choice.

### Suggestions

The authors should provide a more detailed analysis of the hyperparameter selection process. Specifically, they should include a sensitivity analysis that systematically varies each hyperparameter (learning rate, batch size, number of training epochs, and potentially others) while keeping others constant, and observes the impact on the model's performance. This analysis should be presented in a clear and concise manner, possibly using tables or line plots to illustrate the relationship between hyperparameter values and performance metrics. Furthermore, the authors should discuss the interaction between hyperparameters, as changing one parameter might affect the optimal value of another. For example, the learning rate might need to be adjusted based on the batch size or the number of training epochs. The authors should also discuss the range of values they explored and the rationale behind their final choices. This detailed analysis will enhance the reproducibility of the results and provide valuable insights for practitioners.

Regarding computational complexity, the authors should provide a more detailed breakdown of the time and memory requirements for each component of the model. This should include a discussion of the computational cost associated with the local encoder, the patching transformer, and the fusion module. The analysis should also consider the impact of the number of local encoders on the overall computational cost. For example, increasing the number of local encoders might improve performance but could also significantly increase the computational burden. The authors should also compare the computational cost of their method with other state-of-the-art methods for time series classification. This comparison should be done on the same hardware and with the same datasets to ensure a fair evaluation. Furthermore, the authors should discuss the scalability of their method to larger datasets and longer time series. This analysis will provide a better understanding of the practical applicability of the proposed method.

Finally, the authors should provide more guidance on selecting the number of local encoders. While the ablation study is helpful, it does not provide a clear rule of thumb for choosing the optimal number of local encoders for a given dataset. The authors could explore the relationship between the number of local encoders and the characteristics of the dataset, such as the length of the time series, the number of channels, and the complexity of the patterns. This analysis could lead to a more principled approach for selecting the number of local encoders, rather than relying solely on empirical results. This would make the method more accessible and easier to use for practitioners.

### Questions

1. Could the authors provide more details about the selection of hyperparameters, including the learning rate, batch size, and the number of training epochs?
2. Could the authors provide more details about the computational complexity of the proposed method?

### Rating

6

### Confidence

4

**********

### Summary

The paper investigates the training dynamics of CLIP models, particularly focusing on those trained on smaller datasets. The authors observe that these models may be undertrained and propose a simple yet effective strategy to enhance their performance. The core idea involves resetting the learning rate scheduler and training for a few additional epochs. This approach is shown to significantly improve the zero-shot accuracy of CLIP models on downstream tasks, such as ImageNet classification. The paper also explores the effectiveness of this strategy when applied to models trained on larger datasets and compares it with other existing methods for improving CLIP performance.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper identifies a potential undertraining issue in CLIP models trained on smaller datasets, which is an interesting observation.
2. The proposed method is simple and easy to implement, making it accessible for practical use.
3. The authors demonstrate the effectiveness of their approach through experiments on various CLIP architectures and downstream tasks.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a thorough investigation into the reasons behind the undertraining phenomenon. It is not clear why the models trained on smaller datasets are undertrained, and what specific factors contribute to this issue. For instance, is it due to a lack of diversity in the training data, or are there inherent limitations in the optimization process when dealing with smaller datasets? A deeper analysis, perhaps involving visualization of the loss landscape or the learned representations, would be beneficial.
2. The comparison with existing approaches is limited. While the paper claims that the proposed method achieves competitive results, it does not provide a comprehensive comparison with other state-of-the-art methods. It is unclear how the proposed method compares to other techniques that aim to improve CLIP performance, such as those that modify the training objective or use different data augmentation strategies. A more detailed comparison, including quantitative results and qualitative analysis, is needed to establish the true value of the proposed method.
3. The paper does not provide a detailed analysis of the computational cost associated with the proposed method. While the method is simple to implement, it is important to understand the additional computational overhead it introduces, especially when compared to other methods. The paper should include a discussion of the training time and resource requirements, and how these scale with the size of the dataset and the complexity of the model. This is crucial for assessing the practical applicability of the method.

### Suggestions

To strengthen the paper, the authors should delve deeper into the undertraining phenomenon. This could involve analyzing the training dynamics of CLIP models on smaller datasets, perhaps by visualizing the loss landscape or the learned representations. For example, the authors could investigate whether the model gets stuck in poor local minima or if the learned representations are not sufficiently discriminative. Furthermore, it would be beneficial to explore the impact of different training hyperparameters on the undertraining issue. This could include varying the learning rate, batch size, or the number of training epochs. By systematically analyzing these factors, the authors can gain a better understanding of the underlying causes of undertraining and provide more concrete guidance for practitioners.

In addition, the authors should provide a more comprehensive comparison with existing approaches for improving CLIP performance. This should include a detailed analysis of the strengths and weaknesses of the proposed method compared to other techniques. For example, the authors could compare their method to techniques that modify the training objective, use different data augmentation strategies, or employ different optimization algorithms. The comparison should include quantitative results on a variety of downstream tasks, as well as qualitative analysis of the learned representations. This would help to establish the true value of the proposed method and provide a more complete picture of its performance relative to other state-of-the-art techniques. The authors should also consider including a discussion of the computational cost of different methods, including their own, to provide a more practical perspective.

Finally, the authors should provide a more detailed analysis of the computational cost associated with their proposed method. This should include a discussion of the training time and resource requirements, and how these scale with the size of the dataset and the complexity of the model. The authors should also consider comparing the computational cost of their method to other existing approaches. This would help to assess the practical applicability of the method and provide a more complete picture of its trade-offs. For example, the authors could report the training time in hours or days, the GPU memory usage, and the number of GPU hours required to train the model. This information is crucial for practitioners who want to use the method in real-world applications.

### Questions

1. What are the specific reasons behind the undertraining phenomenon observed in CLIP models trained on smaller datasets?
2. How does the proposed method compare to other state-of-the-art methods for improving CLIP performance in terms of both accuracy and computational cost?
3. What is the impact of the proposed method on the robustness of CLIP models to distribution shifts and adversarial attacks?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

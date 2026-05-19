### Summary

The paper studies the transferability of the pre-training task of monocular depth prediction to the downstream task of semantic segmentation. It concludes that monocular depth prediction is a suitable pre-training task for semantic segmentation. The conclusion is drawn from experiments using ResNet as the encoder for depth prediction and semantic segmentation. The paper also explores other factors that may affect transferability, such as the form of depth supervision, the amount of training data, and the resolution of pre-training data.

### Soundness

2

### Presentation

1

### Contribution

2

### Strengths

The paper addresses an interesting problem of understanding what types of pre-training tasks are most effective for semantic segmentation. It conducts a thorough analysis of various factors that may affect transferability between monocular depth prediction and semantic segmentation, such as the form of depth supervision, the amount of training data, and the resolution of pre-training data. The results show that pre-training on monocular depth prediction can improve the performance of semantic segmentation in some cases. Gained insights can be useful for practical applications of pre-training.

### Weaknesses

#### Some Related Works


#### comment

The main weakness of the paper is that the tested pre-training task (monocular depth prediction) and downstream task (semantic segmentation) are considered to be too specific. The conclusions drawn from these specific tasks may not generalize well to other pre-training and downstream tasks. A more generalizable approach would be to explore a wider range of pre-training tasks and downstream tasks to understand the factors that contribute to successful transfer learning. Specifically, the paper does not explore how the choice of architecture for the depth prediction model impacts the transferability of learned features. It is possible that certain architectures are better suited for capturing features that are useful for both depth and segmentation, and this aspect is not investigated. Furthermore, the paper lacks a detailed analysis of the types of features learned during depth pre-training and how these features align with the requirements of semantic segmentation. For example, it would be beneficial to analyze the receptive field sizes and spatial frequencies of the learned features to understand why depth pre-training is beneficial for segmentation in some cases but not others. 

Another weakness is that the paper does not adequately address the potential impact of dataset bias on the results. The datasets used for both depth prediction and semantic segmentation may contain biases that artificially inflate the performance of the proposed approach. For example, if the datasets used for depth prediction and semantic segmentation share similar scene layouts or object distributions, the model may learn to exploit these correlations rather than learning generalizable features. It is important to evaluate the proposed approach on more diverse datasets to ensure that the conclusions are robust and generalizable. The paper also does not explore the impact of different data augmentation techniques on the transferability of learned features. It is possible that certain augmentation techniques are more effective for promoting transfer learning than others, and this aspect is not investigated. 

The clarity of the paper can be improved by providing more details about the experimental setup, including the specific hyperparameters used for training and evaluation, and the evaluation metrics. For example, the paper should specify the learning rate, batch size, and optimization algorithm used for both depth prediction and semantic segmentation. Additionally, the paper should provide more details about the evaluation metrics used for semantic segmentation, such as mean Intersection over Union (mIoU) or pixel accuracy. It is also unclear how the results are averaged across multiple runs, and whether statistical significance tests are performed to determine the robustness of the findings. 

The paper also lacks a thorough comparison with other pre-training tasks that have been explored in the literature. While the paper compares against ImageNet pre-training, it does not explore other self-supervised pre-training methods that may be more relevant to the task of semantic segmentation. For example, it would be useful to compare against pre-training tasks that explicitly learn scene understanding or object recognition. This would provide a more comprehensive understanding of the relative benefits of depth pre-training compared to other approaches.

### Suggestions

To address the limitations of the current study, future work should explore a wider range of pre-training tasks and downstream tasks to understand the factors that contribute to successful transfer learning. Specifically, the authors should consider incorporating pre-training tasks that are more closely related to semantic segmentation, such as object detection or instance segmentation. This would provide a more direct comparison to the proposed depth pre-training approach and help to identify the specific aspects of depth that are beneficial for segmentation. Furthermore, the authors should investigate the impact of different architectures for the depth prediction model on the transferability of learned features. This could involve experimenting with different convolutional neural network architectures, such as ResNet, DenseNet, or EfficientNet, and analyzing how the choice of architecture affects the performance of semantic segmentation. It would also be beneficial to explore the use of transformer-based architectures, which have shown promising results in both depth prediction and semantic segmentation. 

In addition to exploring different pre-training tasks and architectures, future work should also focus on analyzing the types of features learned during depth pre-training and how these features align with the requirements of semantic segmentation. This could involve visualizing the learned features using techniques such as activation maximization or feature map visualization. It would also be useful to analyze the receptive field sizes and spatial frequencies of the learned features to understand why depth pre-training is beneficial for segmentation in some cases but not others. Furthermore, the authors should investigate the impact of different data augmentation techniques on the transferability of learned features. This could involve experimenting with different augmentation techniques, such as random cropping, flipping, rotation, and color jittering, and analyzing how these techniques affect the performance of semantic segmentation. It would also be beneficial to explore the use of more advanced augmentation techniques, such as CutMix or MixUp, which have been shown to improve the robustness of models to variations in the input data. 

Finally, the authors should provide more details about the experimental setup, including the specific hyperparameters used for training and evaluation, and the evaluation metrics. This should include specifying the learning rate, batch size, and optimization algorithm used for both depth prediction and semantic segmentation. Additionally, the paper should provide more details about the evaluation metrics used for semantic segmentation, such as mean Intersection over Union (mIoU) or pixel accuracy. It is also important to report the standard deviation of the results across multiple runs and perform statistical significance tests to determine the robustness of the findings. The authors should also consider evaluating the proposed approach on more diverse datasets to ensure that the conclusions are robust and generalizable. This could involve using datasets with different scene layouts, object distributions, and lighting conditions. Furthermore, a more thorough comparison with other pre-training tasks that have been explored in the literature is needed to provide a more comprehensive understanding of the relative benefits of depth pre-training compared to other approaches.

### Questions

What are the insights gained from the experiments on the transferability between monocular depth prediction and semantic segmentation? How can these insights be applied to other pre-training and downstream tasks?

How does the choice of architecture for the depth prediction model impact the transferability of learned features?

How does the choice of dataset impact the transferability of learned features?

How does the choice of hyperparameters impact the transferability of learned features?

What are the limitations of the proposed approach, and how can they be addressed in future work?

What are the ethical implications of using pre-trained models for semantic segmentation, and how can they be mitigated?

### Rating

3

### Confidence

4

**********

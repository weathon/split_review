### Summary

This paper presents a method for generative pre-training of a model on videos and images. The model is trained to predict the next patch of tokens in a video, using a causal transformer architecture. The authors use a large dataset of videos and images for pre-training, and evaluate the model on a variety of downstream tasks, including image recognition, video classification, object tracking, trajectory prediction, and robotic manipulation. The results show that the model achieves competitive performance across all tasks, despite minimal inductive biases.

### Soundness

3

### Presentation

2

### Contribution

2

### Strengths

* The paper is well-written and easy to follow.
* The authors have conducted a comprehensive evaluation of the model on a variety of downstream tasks, which provides a good understanding of the model's capabilities.
* The authors have also performed ablation studies to understand different design choices and compare their approach to strong baselines across different tasks.

### Weaknesses

#### Some Related Works


#### comment

 * The paper lacks a clear motivation for why generative pre-training is a good approach for learning representations for downstream tasks. The authors do not provide a strong theoretical or empirical justification for why learning representations in a generative manner is beneficial for the specific downstream tasks considered in the paper. It is not clear why learning to predict the next patch of tokens is a good proxy for learning representations that are useful for tasks like image recognition, video classification, object tracking, trajectory prediction, and robotic manipulation. The paper would benefit from a more detailed explanation of the underlying principles that guide this choice.
* The paper does not provide a clear explanation of how the model is trained on videos and images jointly. The authors mention that the model is trained on a mixture of video and image data, but they do not provide details on how the different modalities are handled during training. For example, how are the different token sizes for images and videos handled? How are the different modalities balanced during training? The lack of clarity on these points makes it difficult to understand the training process and to reproduce the results.
* The paper does not provide a clear explanation of how the model is used for downstream tasks. The authors mention that the model is used as a backbone for different downstream tasks, but they do not provide details on how the model is adapted to different tasks. For example, how are the features extracted from the model used for image recognition? How are the features used for video classification? The lack of clarity on these points makes it difficult to understand the practical implications of the proposed approach.

### Suggestions

The paper would benefit significantly from a more detailed explanation of the motivation behind using generative pre-training for downstream tasks. The authors should provide a theoretical justification for why learning to predict the next patch of tokens is a good proxy for learning representations that are useful for tasks like image recognition, video classification, object tracking, trajectory prediction, and robotic manipulation. For example, they could discuss the relationship between the generative objective and the discriminative objectives of the downstream tasks. They could also provide empirical evidence to support their claims, such as by showing that models trained with generative pre-training perform better on downstream tasks than models trained with other pre-training methods. This would help to establish the validity of the proposed approach and to justify the use of generative pre-training for these specific downstream tasks.

To address the lack of clarity regarding the training process, the authors should provide a detailed description of how the model is trained on videos and images jointly. They should explain how the different modalities are handled during training, including how the different token sizes are handled and how the modalities are balanced. They should also provide details on the training procedure, such as the learning rate, batch size, and optimization algorithm used. This would make it easier for other researchers to reproduce the results and to build upon the proposed approach. Furthermore, the authors should provide an ablation study to show the impact of different training strategies on the performance of the model. For example, they could compare the performance of the model when trained only on videos, only on images, and on a mixture of both modalities.

Finally, the authors should provide a clear explanation of how the model is used for downstream tasks. They should explain how the features extracted from the model are used for image recognition, video classification, object tracking, trajectory prediction, and robotic manipulation. They should also provide details on the specific architectures used for each task and the training procedures used to adapt the model to each task. For example, they could provide details on the number of layers and the size of the hidden layers used in each task. This would make it easier for other researchers to understand the practical implications of the proposed approach and to apply it to their own problems. The authors should also provide an ablation study to show the impact of different feature extraction methods on the performance of the downstream tasks.

### Questions

* What is the motivation behind using generative pre-training for downstream tasks? How does this approach compare to other pre-training methods?
* How is the model trained on videos and images jointly? What are the details of the training procedure?
* How is the model used for downstream tasks? What are the details of the feature extraction and adaptation procedures?

### Rating

5

### Confidence

3

**********

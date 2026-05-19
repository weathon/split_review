### Summary

This paper proposes Toto, a causal transformer model for generative pre-training from videos. Toto is trained on a large-scale dataset of videos and images, and is evaluated on a variety of downstream tasks, including image recognition, action recognition, object tracking, robotic manipulation, and scaling behaviors. The results show that Toto achieves competitive performance across all tasks, despite minimal inductive biases.

### Soundness

3

### Presentation

2

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The authors conduct a comprehensive evaluation of the model on a variety of downstream tasks, which provides a good understanding of the model's capabilities.
3. The authors perform ablation studies to understand different design choices and compare their approach to strong baselines across different tasks.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a clear motivation for why generative pre-training is a good approach for learning representations for downstream tasks. The authors do not provide a strong theoretical or empirical justification for why learning representations in a generative manner is beneficial for the specific downstream tasks considered in the paper. It is not clear why learning to predict the next patch of tokens is a good proxy for learning representations that are useful for tasks like image recognition, video classification, object tracking, trajectory prediction, and robotic manipulation. The paper would benefit from a more detailed explanation of the underlying principles that guide this choice.
2. The paper does not provide a clear explanation of how the model is trained on videos and images jointly. The authors mention that the model is trained on a mixture of video and image data, but they do not provide details on how the different modalities are handled during training. For example, how are the different token sizes for images and videos handled? How are the different modalities balanced during training? The lack of clarity on these points makes it difficult to understand the training process and to reproduce the results.
3. The paper does not provide a clear explanation of how the model is used for downstream tasks. The authors mention that the model is used as a backbone for different downstream tasks, but they do not provide details on how the model is adapted to different tasks. For example, how are the features extracted from the model used for image recognition? How are the features used for video classification? The lack of clarity on these points makes it difficult to understand the practical implications of the proposed approach.

### Suggestions

The paper would significantly benefit from a more thorough discussion of the motivation behind using a generative approach for pre-training. While the authors mention that it is inspired by iGPT, they do not delve into the specific reasons why this approach is expected to be effective for downstream tasks. A deeper analysis of the theoretical underpinnings of generative pre-training, particularly in the context of the diverse tasks considered in this paper, is needed. For instance, the authors could explore how the generative objective encourages the model to learn representations that capture the underlying structure of the data, which could be beneficial for tasks such as image recognition and action recognition. Furthermore, a comparison with discriminative pre-training methods, highlighting the advantages and disadvantages of each approach, would provide a more comprehensive understanding of the proposed method's strengths and weaknesses. This would help to justify the choice of a generative approach and provide a stronger theoretical foundation for the paper.

To address the lack of clarity regarding the joint training of videos and images, the authors should provide a detailed description of the training procedure. This should include a discussion of how the different modalities are handled, specifically addressing how the different token sizes for images and videos are handled. For example, are the images and videos tokenized using the same method, or are there differences in the tokenization process? If different tokenization methods are used, how are these differences accounted for during training? Furthermore, the authors should explain how the different modalities are balanced during training. Are the images and videos sampled with equal probability, or are there any weighting schemes used to balance the two modalities? A clear explanation of these details is crucial for reproducibility and for understanding the training process. An ablation study exploring the impact of different training strategies on the performance of the model would also be valuable.

Finally, the paper needs to clarify how the model is used for downstream tasks. The authors should provide a detailed explanation of how the features extracted from the model are used for image recognition, video classification, object tracking, trajectory prediction, and robotic manipulation. For example, how are the features used in a supervised learning setting for image recognition? Are the features directly used as input to a classifier, or are they further processed? Similarly, how are the features used in a supervised learning setting for video classification? Are the features extracted from different frames concatenated, or is there a different approach? The authors should also provide details on the specific architectures used for each task and the training procedures used to adapt the model to each task. This would make it easier for other researchers to understand the practical implications of the proposed approach and to apply it to their own problems.

### Questions

Please refer to the weaknesses.

### Rating

5

### Confidence

3

**********

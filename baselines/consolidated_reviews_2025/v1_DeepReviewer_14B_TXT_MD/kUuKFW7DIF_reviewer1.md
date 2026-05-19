### Summary

This paper proposes to use multi-resolution transformers as a backbone of self-supervised learning from speech. In detail, the speech features are first extracted from a convolutional encoder. Then the features are fed into a hierarchical multi-resolution transformer encoders that gradually downsamples the input features and then gradually upsamples the features back to the original resolution. The final output features from the multi-resolution encoder are used to predict the masked frames at multiple resolutions. The whole model is pre-trained with lots of unlabeled speech data. Experiment results show that the proposed method performs better than the baseline method in many downstream tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed method is sound and intuitive.
2. The experiment results are extensive and show the proposed method has better performance than the baseline method.

### Weaknesses

#### Some Related Works


#### comment

1. The pre-training of the proposed method may cost more time than the baseline method since it needs to generate pseudo labels iteratively.

### Suggestions

The paper introduces a multi-resolution transformer architecture for self-supervised learning (SSL) from speech, which is a promising direction. However, the paper could benefit from a more detailed analysis of the computational overhead associated with the proposed method. While the authors mention that the iterative generation of pseudo-labels might increase pre-training time, a more rigorous comparison of the actual training time and resource consumption (e.g., GPU hours, memory usage) between the proposed method and the baseline would be beneficial. This should include a breakdown of the time spent on different stages of the pre-training process, such as feature extraction, pseudo-label generation, and model training. Furthermore, it would be valuable to explore techniques to mitigate the computational cost, such as using more efficient clustering algorithms for pseudo-label generation or exploring knowledge distillation methods to transfer the learned representations to a smaller model. 

To further strengthen the paper, a more in-depth analysis of the performance gains achieved by the multi-resolution approach is needed. While the results show that the proposed method outperforms the baseline, it is not clear which specific resolution levels contribute most to the performance improvement. An ablation study that systematically evaluates the impact of different resolution levels on downstream task performance would be valuable. This could involve training models with only a single resolution level or subsets of resolution levels and comparing their performance to the full model. Additionally, the paper could explore the potential benefits of using different downsampling and upsampling techniques within the multi-resolution architecture. For example, using learnable downsampling layers instead of fixed pooling operations might improve the model's ability to capture relevant features at different resolutions. 

Finally, the paper should provide more details on the specific implementation of the multi-resolution transformer encoder. This includes the number of layers, the size of the attention heads, and the activation functions used. It would also be helpful to discuss the choice of the clustering algorithm used for pseudo-label generation and the parameters used for the clustering process. Furthermore, the paper could explore the sensitivity of the model's performance to different hyperparameter settings. This could involve performing a grid search over a range of hyperparameter values and reporting the optimal settings for each downstream task. A more detailed analysis of the model's architecture and training process would make the paper more reproducible and allow other researchers to build upon the proposed method.

### Questions

1. In the experiment, is the performance of the baseline method reported in the original paper or re-implemented in the authors' experiments? If it is the former, there may be some other differences between the proposed method and the baseline method other than the multi-resolution encoder. That may make the comparison results less convincing.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

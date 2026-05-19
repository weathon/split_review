### Summary

This paper proposes a simple plug-in module, Skip-Attention, to reduce the costly self-attention computations in vision transformers (ViT). The authors leverage the dependency across MSA blocks and bypass attention computation by reusing attention from previous MSA blocks. To ensure that the metaphorical sharing is caring, the authors introduced a simple and light parametric function that does not affect the inductive bias encoded in MSA. The proposed method can be applied to various transformer architectures and was evaluated on 7 different tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple yet effective.
3. The proposed method can be applied to various transformer architectures.
4. The authors conducted extensive experiments to demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The authors should provide more details about the implementation of the proposed method. For example, how to choose the layers to skip attention? Are there any specific criteria or heuristics used to determine which layers are most suitable for skipping? What is the impact of skipping different numbers of layers on the performance and computational cost? A more detailed analysis of these aspects would be beneficial.
2. The authors should provide more details about the experimental settings. For example, what are the specific hyperparameter settings used for each task? What is the training procedure? What is the optimization algorithm and learning rate schedule? Providing these details would improve the reproducibility of the results.
3. The authors should provide more details about the computational resources used for the experiments. For example, what type of GPUs were used? How many GPUs were used? What is the memory capacity of the GPUs? This information is important for understanding the computational cost of the proposed method and for comparing it with other methods.
4. The authors should provide more details about the datasets used for the experiments. For example, what is the size of each dataset? What is the resolution of the images? What is the number of classes in each dataset? This information is important for understanding the generalizability of the proposed method.
5. The authors should provide more details about the evaluation metrics used for the experiments. For example, what is the definition of each metric? How is it calculated? Providing these details would improve the clarity of the results.

### Suggestions

The paper introduces an interesting approach to reduce computational costs in vision transformers by reusing self-attention computations. However, the current manuscript lacks sufficient detail regarding the implementation and experimental setup, which hinders a thorough evaluation of the proposed method. Specifically, the authors should provide a more detailed explanation of how the layers to skip attention are chosen. While the paper mentions that the method is applied to layers 3-8, it does not provide a clear rationale for this choice. A more in-depth analysis of the impact of skipping different layers, or combinations of layers, on both performance and computational cost is needed. For example, it would be beneficial to see results for skipping only one layer, skipping non-adjacent layers, or skipping layers based on some criteria such as the magnitude of attention weights or the similarity of attention maps. This analysis would help to understand the sensitivity of the method to the choice of skipped layers and provide guidance for applying the method to different architectures and tasks. Furthermore, the authors should explore the possibility of dynamically determining which layers to skip based on the input data or the training progress. This could potentially lead to further improvements in efficiency without sacrificing performance.

In addition to the layer selection strategy, the paper needs to provide more comprehensive details about the experimental settings. The current manuscript only provides a high-level overview of the experimental setup, which makes it difficult to reproduce the results. The authors should specify the exact hyperparameter settings used for each task, including the learning rate, batch size, weight decay, and dropout rate. They should also provide details about the training procedure, such as the number of training epochs, the optimization algorithm, and the learning rate schedule. Furthermore, the authors should provide more information about the data augmentation techniques used during training. It is also important to specify the exact version of the libraries used for the experiments, such as PyTorch and TensorFlow. This level of detail is crucial for ensuring the reproducibility of the results and for allowing other researchers to build upon this work. The authors should also consider releasing their code to further enhance the reproducibility and facilitate the adoption of their method.

Finally, the authors should provide more details about the computational resources used for the experiments. The current manuscript only mentions that the experiments were conducted on GPUs, but it does not specify the type or number of GPUs used. It is also important to specify the memory capacity of the GPUs and the time taken for training and inference. This information is crucial for understanding the computational cost of the proposed method and for comparing it with other methods. Furthermore, the authors should provide more details about the datasets used for the experiments, including the size of each dataset, the resolution of the images, and the number of classes. They should also provide more details about the evaluation metrics used for the experiments, including the definition of each metric and how it is calculated. This information is important for understanding the generalizability of the proposed method and for comparing it with other methods. The authors should also consider providing a more detailed analysis of the results, including error bars and statistical significance tests.

### Questions

Please see the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

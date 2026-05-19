### Summary

This paper addresses the challenge of learning with local openset noisy labels in federated learning. The authors propose a novel framework called FedDPCont to solve this problem. They define the openset noise problem in FL, propose a label communication mechanism with differential privacy, and demonstrate the effectiveness of FedDPCont through experiments on both synthetic and real-world datasets.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. This paper is well-written and easy to follow.
2. The authors provide a comprehensive theoretical analysis of FedDPCont, including convergence and robustness to label noise.
3. The authors conduct extensive experiments on both benchmark datasets and practical datasets to demonstrate the effectiveness of FedDPCont.

### Weaknesses

#### Some Related Works


#### comment

1. The authors should provide more details about the generation of openset noisy labels. Specifically, the process of generating the openset classes and the noisy labels needs to be more clearly defined. It is unclear how the authors ensure that the openset classes are distinct from the seen classes, and how the noise is introduced in a realistic manner. The description lacks the necessary detail for reproducibility.
2. The authors should provide more details about the experimental setup. The description of the datasets, the specific hyperparameters used, and the training procedures are not sufficiently detailed. For example, the specific ResNet architectures used, the optimization algorithms, and the learning rates are not clearly specified. This makes it difficult to reproduce the results.
3. The authors should provide more details about the baselines. The description of the baseline methods is too brief. The authors should provide more details about the implementation of the baselines, including the specific hyperparameters used and the training procedures. It is not clear how the baselines were adapted to the federated learning setting.
4. The authors should provide more details about the evaluation metrics. The authors should clearly define the evaluation metrics used and justify their choice. It is not clear how the metrics relate to the problem of learning with local openset noisy labels.

### Suggestions

The paper would benefit significantly from a more detailed explanation of the openset noisy label generation process. The authors should provide a step-by-step description of how the openset classes are generated, ensuring they are distinct from the seen classes. This should include a clear explanation of the criteria used to determine which classes are open and how these open classes are sampled or generated. Furthermore, the method for introducing noise should be clarified, including the specific parameters used and how they affect the noise distribution. For example, if a Dirichlet distribution is used to introduce noise, the parameters of the distribution should be specified, and the rationale for choosing this distribution should be provided. The authors should also include a discussion on the potential impact of different noise generation strategies on the performance of the proposed method. This would help the reader understand the robustness of the method under various noise conditions. Without these details, it is difficult to assess the validity and reproducibility of the experimental results.

To improve the reproducibility of the experiments, the authors should provide a comprehensive description of the experimental setup. This includes specifying the exact datasets used, the train/test splits, the specific ResNet architectures used (including the number of layers and any modifications), the optimization algorithms (e.g., SGD, Adam), the learning rates, batch sizes, and the number of training epochs. The authors should also provide details on how the data was preprocessed, including any normalization or augmentation techniques. Furthermore, the authors should provide a detailed description of how the baselines were implemented in the federated learning setting. This includes specifying the hyperparameters used for each baseline and the training procedures. It is important to ensure that all baselines are implemented correctly and fairly compared to the proposed method. The authors should also consider including a discussion on the computational resources used for the experiments.

Finally, the authors should provide a clear and detailed explanation of the evaluation metrics used. The authors should justify their choice of metrics and explain how they are relevant to the problem of learning with local openset noisy labels. For example, if accuracy is used as a metric, the authors should explain how it is calculated in the presence of openset noisy labels. If other metrics are used, the authors should explain why they are more appropriate than accuracy. The authors should also provide a discussion on the limitations of the chosen metrics and how they might affect the interpretation of the results. It is important to ensure that the evaluation metrics are appropriate for the problem being addressed and that they provide a comprehensive understanding of the performance of the proposed method.

### Questions

Please refer to the weakness.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

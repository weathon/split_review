### Summary

This paper proposes a novel neural layer, LogicMP, which performs mean-field variational inference over a Markov Logic Network (MLN). It can be plugged into any off-the-shelf neural network to encode FOLCs while retaining modularity and efficiency. By exploiting the structure and symmetries in MLNs, the authors theoretically demonstrate that their well-designed, efficient mean-field iterations greatly mitigate the difficulty of MLN inference, reducing the inference from sequential calculation to a series of parallel tensor operations. Empirical results in three kinds of tasks over images, graphs, and text show that LogicMP outperforms advanced competitors in both performance and efficiency.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed method is novel and interesting. It is a good attempt to integrate symbolic reasoning into deep learning. The proposed method is also efficient and can be easily integrated into existing neural network architectures.
2. The paper is well-written and easy to follow. The authors have provided a clear and concise explanation of their method, and the experimental results are presented in a clear and organized manner.
3. The experimental results are promising. The proposed method outperforms existing methods on several benchmark datasets, and the ablation study provides valuable insights into the contribution of each component of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is based on the mean-field approximation, which may not always be accurate. The authors should discuss the limitations of this approximation and how it might affect the performance of their method. Specifically, the mean-field approximation assumes independence between latent variables, which may not hold true in complex logical reasoning scenarios. This could lead to suboptimal solutions, especially when dealing with intricate dependencies between different parts of the knowledge graph. The paper should include a more detailed analysis of the potential impact of this approximation on the accuracy of the results, perhaps by comparing with exact inference methods on smaller datasets where it is feasible.
2. The proposed method is evaluated on several benchmark datasets, but these datasets may not be representative of all real-world scenarios. The authors should discuss the limitations of their evaluation and how their method might perform on more complex and diverse datasets. For example, the datasets used might not fully capture the complexity of real-world knowledge graphs, which often contain noisy, incomplete, and inconsistent information. The paper should discuss how the method would handle such scenarios and whether it would still be able to maintain its performance. Furthermore, the evaluation could be expanded to include datasets with varying degrees of logical complexity to better understand the method's limitations.
3. The authors should provide more details on the implementation of their method, including the specific choices of hyperparameters and the computational resources required to train and evaluate their model. This would help other researchers to reproduce their results and build upon their work. For instance, the paper should specify the learning rate, batch size, and the number of training epochs used. Additionally, the paper should provide details on the hardware used for training and evaluation, such as the type of GPUs and the amount of memory required. This information is crucial for ensuring the reproducibility of the results and for assessing the practical applicability of the method.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations of the mean-field approximation. While the method shows promising results, it is crucial to acknowledge that the mean-field assumption might not always hold, especially in complex logical reasoning tasks. The authors should consider including a theoretical analysis of the approximation error or an empirical comparison with exact inference methods on smaller datasets where exact inference is feasible. This would provide a better understanding of the trade-offs between computational efficiency and accuracy. Furthermore, the authors could explore alternative approximation techniques that might be more suitable for certain types of logical constraints or knowledge graph structures. For example, loopy belief propagation or other variational inference methods could be considered and compared to the mean-field approach.

To address the limitations of the evaluation, the authors should consider expanding their experiments to include more diverse and challenging datasets. This could involve using datasets with varying degrees of logical complexity, noise, and incompleteness. For example, datasets from different domains, such as social networks, biological networks, or knowledge bases with different types of entities and relations, could be used to evaluate the generalizability of the method. Additionally, the authors should discuss the potential impact of data quality on the performance of their method. This would provide a more comprehensive understanding of the method's strengths and weaknesses and its applicability to real-world scenarios. The authors should also consider including a sensitivity analysis to evaluate how the performance of the method is affected by different hyperparameters and training settings.

Finally, the paper should provide more detailed information about the implementation of the method. This includes specifying the exact architecture of the neural network used, the choice of activation functions, and the optimization algorithm. The authors should also provide details on the computational resources required to train and evaluate the model, such as the type of GPUs, the amount of memory, and the training time. This information is crucial for ensuring the reproducibility of the results and for assessing the practical applicability of the method. Furthermore, the authors should consider releasing the code and the trained models to the public, which would greatly facilitate the adoption of their method by other researchers.

### Questions

1. How does the proposed method handle the case where the logical constraints are not satisfied? Does it try to find the best possible solution that satisfies the constraints, or does it simply ignore the constraints?
2. How does the proposed method compare to other methods that integrate symbolic reasoning into deep learning, such as neural-symbolic systems or differentiable reasoning methods?
3. How does the proposed method handle the case where the input data is noisy or incomplete? Does it have any mechanisms to deal with uncertainty or ambiguity in the input data?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

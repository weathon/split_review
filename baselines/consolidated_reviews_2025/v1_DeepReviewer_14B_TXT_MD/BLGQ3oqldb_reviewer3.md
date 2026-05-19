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

1. The proposed method is based on the mean-field approximation, which may not always be accurate. The authors should discuss the limitations of this approximation and how it might affect the performance of their method.
2. The proposed method is evaluated on several benchmark datasets, but these datasets may not be representative of all real-world scenarios. The authors should discuss the limitations of their evaluation and how their method might perform on more complex and diverse datasets.
3. The authors should provide more details on the implementation of their method, including the specific choices of hyperparameters and the computational resources required to train and evaluate their model.

### Suggestions

The paper introduces an interesting approach by integrating symbolic reasoning with deep learning through a novel neural layer, LogicMP. However, the reliance on the mean-field approximation warrants further discussion. While the mean-field approach offers computational efficiency, it inherently assumes independence between latent variables, which may not hold in complex scenarios. The authors should explore the potential impact of this approximation on the accuracy of their method, especially when dealing with intricate logical constraints. It would be beneficial to include a theoretical analysis of the approximation error or an empirical comparison with exact inference methods on smaller datasets where it is feasible. Furthermore, the authors should consider discussing alternative approximation techniques that could potentially mitigate the limitations of the mean-field approach, such as loopy belief propagation or other variational inference methods. This would provide a more comprehensive understanding of the trade-offs between computational efficiency and accuracy in their proposed method.

To strengthen the evaluation, the authors should consider expanding their experiments to include more diverse and challenging datasets. The current evaluation, while promising, is limited to a few benchmark datasets. It is crucial to assess the generalizability of the proposed method to more complex and realistic scenarios. For example, the authors could explore datasets with varying degrees of logical complexity, noise, and incompleteness. Additionally, the authors should discuss the potential impact of data quality on the performance of their method. This would provide a more comprehensive understanding of the method's strengths and weaknesses and its applicability to real-world scenarios. Furthermore, the authors should consider including a sensitivity analysis to evaluate how the performance of the method is affected by different hyperparameters and training settings. This would provide valuable insights into the robustness of the method and its sensitivity to parameter choices.

Finally, the paper would benefit from a more detailed description of the implementation. The authors should provide specific details regarding the architecture of the neural network used, the choice of activation functions, and the optimization algorithm. Furthermore, the authors should provide details on the computational resources required to train and evaluate the model, such as the type of GPUs, the amount of memory, and the training time. This information is crucial for ensuring the reproducibility of the results and for assessing the practical applicability of the method. The authors should also consider releasing the code and the trained models to the public, which would greatly facilitate the adoption of their method by other researchers.

### Questions

1. How does the proposed method handle the case where the logical constraints are not satisfied? Does it try to find the best possible solution that satisfies the constraints, or does it simply ignore the constraints?
2. How does the proposed method compare to other methods that integrate symbolic reasoning into deep learning, such as neural-symbolic systems or differentiable reasoning methods?
3. How does the proposed method handle the case where the input data is noisy or incomplete? Does it have any mechanisms to deal with uncertainty or ambiguity in the input data?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

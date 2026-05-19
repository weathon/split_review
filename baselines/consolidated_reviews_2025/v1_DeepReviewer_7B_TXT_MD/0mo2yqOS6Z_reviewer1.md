### Summary

The paper proposes a new approach to weight parameterization using predictor networks. The proposed method is based on the Neural Representations for Neural Networks (NeRN) framework. The main idea is to decouple the training process into two stages: reconstruction and distillation. In the first stage, the predictor network is trained to reconstruct the original model weights using a reconstruction loss. In the second stage, the predictor network is fine-tuned using a distillation loss, which transfers knowledge from a high-performing teacher network to the predictor. The authors show that this two-stage approach leads to improved model accuracy and compression compared to the original NeRN framework and other state-of-the-art methods.

### Soundness

3

### Presentation

2

### Contribution

2

### Strengths

The paper presents a novel approach to weight parameterization using predictor networks, which is based on the Neural Representations for Neural Networks (NeRN) framework. The proposed method is well-motivated and addresses some of the limitations of the original NeRN framework, such as the trade-off between accuracy and model compression. The authors provide a comprehensive set of experiments on various datasets and architectures, which demonstrate the effectiveness of the proposed method. The results show that the proposed method outperforms the original NeRN framework and other state-of-the-art methods in terms of both accuracy and compression. The paper is well-written and easy to follow, with clear explanations of the proposed method and the experimental setup.

### Weaknesses

#### Some Related Works


#### comment

The paper could benefit from a more detailed discussion of the limitations of the proposed method and potential directions for future research. For example, the authors could discuss the computational cost of training the predictor network and the potential for overfitting. They could also explore the applicability of the proposed method to other types of neural networks, such as transformers. Additionally, the authors could provide a more in-depth analysis of the relationship between the predictor network and the original model weights, and how this relationship affects the performance of the proposed method. The paper lacks a thorough analysis of the sensitivity of the method to hyperparameter choices, particularly the size of the predictor network and the weighting of the reconstruction and distillation losses. A more rigorous exploration of these parameters is needed to understand the robustness of the approach. Furthermore, the paper does not adequately address the potential for the predictor network to learn a representation that is not directly related to the original model's weights, which could lead to a loss of fidelity. The authors should also consider the impact of different initialization strategies for the predictor network on the final performance. Finally, the paper would benefit from a more detailed comparison with other weight parameterization techniques, including a discussion of the trade-offs between accuracy, compression, and computational cost.

### Suggestions

The authors should provide a more thorough analysis of the computational cost associated with training the predictor network. Specifically, they should quantify the additional training time and memory requirements compared to training the original model and the NeRN framework. This analysis should include a breakdown of the computational cost for each stage of the training process, including the reconstruction and distillation phases. Furthermore, the authors should investigate the scalability of the proposed method to larger models and datasets. It would be beneficial to explore techniques for reducing the computational overhead of the predictor network, such as using smaller networks or employing more efficient training algorithms. The authors should also consider the impact of the predictor network's architecture on the final performance. For example, they could explore different network architectures and hyperparameters to determine the optimal configuration for different types of models and datasets. This analysis should include a discussion of the trade-offs between the complexity of the predictor network and the resulting performance gains.

To address the concerns about the sensitivity to hyperparameters, the authors should conduct a more comprehensive ablation study. This study should systematically vary the size of the predictor network, the weighting of the reconstruction and distillation losses, and other relevant hyperparameters. The results of this study should be presented in a clear and concise manner, with a focus on identifying the key factors that influence the performance of the proposed method. The authors should also provide a detailed explanation of the rationale behind their choice of hyperparameters. Furthermore, the authors should investigate the potential for the predictor network to learn a representation that is not directly related to the original model's weights. This could be done by analyzing the correlation between the predictor network's output and the original model's weights. If the predictor network is learning a representation that is not directly related to the original model's weights, this could lead to a loss of fidelity. The authors should also consider the impact of different initialization strategies for the predictor network on the final performance. For example, they could explore different initialization schemes and evaluate their impact on the convergence and stability of the training process.

Finally, the authors should provide a more detailed comparison with other weight parameterization techniques. This comparison should include a discussion of the trade-offs between accuracy, compression, and computational cost. The authors should also discuss the limitations of their approach and identify areas for future research. For example, they could explore the applicability of the proposed method to other types of neural networks, such as transformers. They could also investigate the use of different distillation techniques to improve the performance of the proposed method. The authors should also consider the potential for using the proposed method in other applications, such as model compression and acceleration. This discussion should provide a clear understanding of the strengths and weaknesses of the proposed method and its potential for future development.

### Questions

What are the computational costs associated with training the predictor network, and how do they compare to the computational costs of training the original model and the NeRN framework? How does the size of the predictor network affect the performance of the proposed method? What is the sensitivity of the proposed method to the weighting of the reconstruction and distillation losses? How does the proposed method compare to other weight parameterization techniques in terms of accuracy, compression, and computational cost?

### Rating

6

### Confidence

3

**********

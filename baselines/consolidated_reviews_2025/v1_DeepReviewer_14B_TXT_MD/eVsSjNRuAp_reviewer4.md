### Summary

The paper proposes a novel training framework called Predictive Differential Training (PDT) that leverages Koopman operator theory to predict the training dynamics of deep neural networks. By considering the training process as a nonlinear dynamical system in the weight space, the authors propose a method to bypass time-consuming Stochastic Gradient Descent (SGD) iterations by predicting network weights for future epochs. To address the issue of gradient explosion in complex models, PDT incorporates differential learning rates for different parts of the network. The framework includes a masking strategy based on Koopman analysis to select parameters with good prediction performance and an acceleration scheduler to manage prediction errors. The experimental results demonstrate that PDT consistently outperforms baseline methods in terms of faster convergence, lower training and testing loss, and fewer epochs to achieve the best loss.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach to deep neural network training by framing the training process as a nonlinear dynamical system and applying Koopman operator theory. This perspective is innovative and offers a fresh way to understand and optimize the training dynamics of neural networks.

2. The paper is well-organized and clearly written, making it accessible to readers with a background in machine learning and dynamical systems. The authors provide a thorough introduction to the necessary background concepts, such as Koopman operator theory and Dynamic Mode Decomposition (DMD), which helps readers understand the theoretical underpinnings of the proposed method.

3. The paper includes a comprehensive set of experiments on various benchmark models (e.g., AlexNet, ResNet, and ViT) and datasets (e.g., CIFAR-10 and ImageNet). These experiments provide strong empirical evidence for the effectiveness of the proposed PDT framework, demonstrating its ability to accelerate training and improve performance across different architectures and datasets.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's reliance on Koopman operator theory and Dynamic Mode Decomposition (DMD) for predicting training dynamics may introduce additional computational overhead. While the authors claim that the computational load is manageable, a more detailed analysis of the time and memory complexity, especially for very large models, would be beneficial. Specifically, the paper lacks a rigorous breakdown of the computational cost associated with the DMD computation, including the SVD operation, and how this scales with the number of parameters in the network. Furthermore, the memory footprint of storing the necessary snapshots for DMD reconstruction is not discussed, which could be a limiting factor for very large models.

2. The proposed masking strategy and acceleration schedule are based on heuristics derived from the properties of Koopman analysis. However, the paper does not provide a theoretical justification for why these specific criteria (quantity and direction) are optimal or sufficient for ensuring stable and efficient training. A more in-depth theoretical analysis of the masking strategy and its impact on the training dynamics would strengthen the paper's contributions. For example, it is unclear how the chosen criteria relate to the stability of the optimization process or the convergence properties of the algorithm. A formal analysis of the conditions under which the proposed masking strategy guarantees convergence would be valuable.

3. While the paper demonstrates the effectiveness of PDT on several benchmark models and datasets, it does not explore its applicability to other types of neural networks, such as recurrent neural networks (RNNs) or graph neural networks (GNNs). Additionally, the paper does not discuss the potential challenges and limitations of applying PDT to different domains, such as natural language processing or reinforcement learning. The dynamics of these models can be significantly different from CNNs, and it is not clear how the proposed method would adapt to these different scenarios. For instance, the temporal dependencies in RNNs or the structural dependencies in GNNs might require different masking strategies or prediction models.

### Suggestions

To address the computational overhead concerns, the authors should provide a more detailed analysis of the time and memory complexity of the DMD computation. This should include a breakdown of the cost associated with the SVD operation and how it scales with the number of parameters in the network. Furthermore, the authors should discuss the memory footprint of storing the necessary snapshots for DMD reconstruction and how this might limit the applicability of the method to very large models. It would be beneficial to include a comparison of the computational cost of PDT with standard SGD and other optimization methods, considering both the training time and the memory requirements. This analysis should be supported by empirical results on models of varying sizes to demonstrate the scalability of the proposed approach. Additionally, exploring low-rank approximations or other efficient DMD algorithms could help mitigate the computational burden.

To strengthen the theoretical foundations of the proposed method, the authors should provide a more rigorous analysis of the masking strategy and its impact on the training dynamics. This should include a formal justification for why the chosen quantity and direction criteria are effective in selecting parameters with good prediction performance. It would be valuable to explore the relationship between these criteria and the stability of the optimization process, as well as the convergence properties of the algorithm. A theoretical analysis of the conditions under which the proposed masking strategy guarantees convergence would be a significant contribution. Furthermore, the authors could investigate alternative masking strategies and compare their performance with the proposed approach, providing a more comprehensive understanding of the design choices.

To broaden the applicability of the proposed method, the authors should explore its performance on other types of neural networks, such as RNNs and GNNs. This should include a discussion of the potential challenges and limitations of applying PDT to these different architectures. For instance, the temporal dependencies in RNNs might require a different approach to predicting the weight dynamics, and the structural dependencies in GNNs might necessitate a different masking strategy. The authors should also discuss the potential applicability of PDT to other domains, such as natural language processing and reinforcement learning, and identify the specific challenges that might arise in these contexts. This would help to establish the generality of the proposed method and its potential impact on the broader machine learning community.

### Questions

1. How does the computational overhead of PDT compare to standard SGD and other optimization methods, especially for very large models? Can the authors provide a detailed analysis of the time and memory complexity of their approach?

2. What is the theoretical basis for the proposed masking strategy and acceleration schedule? Can the authors provide a more in-depth analysis of why these specific criteria are effective in selecting parameters with good prediction performance?

3. How does PDT perform on other types of neural networks, such as recurrent neural networks (RNNs) or graph neural networks (GNNs)? What are the potential challenges and limitations of applying PDT to different domains, such as natural language processing or reinforcement learning?

### Rating

6

### Confidence

3

**********

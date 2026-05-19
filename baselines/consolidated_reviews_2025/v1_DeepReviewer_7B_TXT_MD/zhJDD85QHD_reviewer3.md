### Summary

This paper proposes a concept-based explainable image representation learning method called CEIR. The main idea is to project input images into a concept vector space and then use a Variational Autoencoder (VAE) to learn the latent representation. The authors claim that this approach enhances interpretability and preserves the robustness of the learned representations. The method is evaluated on several datasets, including CIFAR10, CIFAR100-20, CIFAR100, STL10, and ImageNet, demonstrating its effectiveness in unsupervised clustering and representation learning.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper is well-organized and easy to follow.
2. The authors provide extensive experiments to evaluate the performance of the proposed method on multiple datasets.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of the proposed method is limited. The overall framework is similar to LF-CBM, which also involves projecting image features into a concept vector space and using a VAE for representation learning. The main difference is that the authors use a pretrained CLIP model to generate concept labels instead of manually defined labels. However, the use of pretrained models to generate concept labels has been explored in other works, such as T-CAV and LF-ImageNet. The core idea of using a concept bottleneck to extract interpretable features from a representation is not new, and the specific implementation using CLIP and VAE, while potentially useful, does not represent a significant conceptual leap.
2. The paper lacks a thorough discussion of the limitations of the proposed method. For example, the authors do not address how the method would perform on datasets with complex or abstract concepts, or how the choice of concept labels might affect the quality of the learned representations. Furthermore, the paper does not discuss the computational cost of the method, particularly the use of a large language model for concept generation and the training of the VAE, which could be a significant barrier for some users.
3. The evaluation metrics used in the paper are not comprehensive. While the authors report NMI, ACC, and ARI for clustering tasks, they do not provide a detailed analysis of the learned representations using other metrics, such as the ability to preserve semantic relationships between concepts or the robustness to adversarial attacks. The paper also lacks a comparison with other state-of-the-art representation learning methods, which makes it difficult to assess the true performance of the proposed approach.

### Suggestions

The authors should more clearly articulate the specific advantages of their approach over existing concept bottleneck methods, particularly in the context of unsupervised learning. While the use of CLIP for concept generation is a practical choice, the paper needs to demonstrate that this approach offers unique benefits compared to using manually defined concepts or other pre-trained models. A more detailed analysis of the concept space learned by CEIR, including the diversity and quality of the concepts, would be beneficial. For example, the authors could analyze the semantic coherence of the learned concepts and their ability to capture meaningful variations in the input data. Furthermore, the authors should provide a more thorough discussion of the limitations of their method, including its sensitivity to the choice of hyperparameters, the computational cost of training, and the potential for bias in the learned representations. 

To strengthen the evaluation, the authors should include a more comprehensive set of metrics that go beyond standard clustering metrics. For example, they could evaluate the quality of the learned representations by measuring their ability to preserve semantic relationships between concepts, or by assessing their robustness to adversarial attacks. The authors should also compare their method with other state-of-the-art representation learning methods, including both unsupervised and supervised approaches, to provide a more complete picture of its performance. This would help to better understand the strengths and weaknesses of the proposed method and its potential applications. Additionally, the authors should consider evaluating the method on a wider range of datasets, including those with more complex and abstract concepts, to demonstrate its generalizability. 

Finally, the authors should provide a more detailed explanation of the experimental setup, including the specific parameters used for each dataset and the training procedure. This would make it easier for other researchers to reproduce their results and build upon their work. The authors should also discuss the potential biases in the datasets and how these biases might affect the performance of the proposed method. A more thorough analysis of the results, including error analysis and visualization of the learned representations, would also be beneficial. This would provide a deeper understanding of the method's behavior and its limitations.

### Questions

1. How does the proposed method compare to other concept-based representation learning methods, such as LF-CBM and T-CAV, in terms of performance and interpretability?
2. What are the limitations of the proposed method, and how can they be addressed in future work?
3. How does the choice of concept labels affect the quality of the learned representations?

### Rating

5

### Confidence

4

**********

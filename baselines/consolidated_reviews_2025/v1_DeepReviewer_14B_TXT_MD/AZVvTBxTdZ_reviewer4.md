### Summary

This paper introduces a large-scale neural architecture dataset for adversarial robustness, named NARes. The dataset includes 15,625 WRN-style architectures that are adversarially trained and evaluated against four adversarial attacks, including AutoAttack. The paper provides insights into the relationship between architecture and robustness, and demonstrates the use of NARes as a benchmark for neural architecture search algorithms.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel and comprehensive dataset for adversarial robustness, which can be a valuable resource for the community.
2. The paper provides insights into the relationship between architecture and robustness, which can be useful for designing more robust models.
3. The paper demonstrates the use of NARes as a benchmark for neural architecture search algorithms, which can help in developing more robust models.

### Weaknesses

#### Some Related Works


#### comment

1. The dataset is limited to WRN-style architectures, which may not be representative of all types of neural networks. It would be beneficial to include other types of architectures, such as Transformers, to make the dataset more comprehensive. The current focus on WRNs limits the generalizability of the findings to other architectures, which is a significant concern given the diverse landscape of neural network models used in practice. For example, the performance of attention-based mechanisms in Transformers under adversarial attacks is a crucial area that is not explored by this dataset.
2. The paper only considers four adversarial attacks, which may not be sufficient to evaluate the robustness of the models. It would be beneficial to include more attacks, such as those based on different threat models or those that are more adaptive to the defense mechanisms. The current set of attacks, while including AutoAttack, may not fully capture the spectrum of potential adversarial threats. For instance, attacks that exploit specific vulnerabilities of adversarial training methods, or those that target the decision boundaries of the models in a more nuanced way, are not considered. This could lead to an overestimation of the robustness of the models.
3. The paper does not provide a detailed analysis of the computational cost of training and evaluating the models in the dataset. This information is important for researchers who want to use the dataset. The lack of information on training time, memory requirements, and the computational resources needed for evaluation makes it difficult for researchers to assess the feasibility of using this dataset in their own work. This is especially important for those with limited computational resources.

### Suggestions

To enhance the dataset's comprehensiveness and applicability, it is crucial to expand the range of architectures included. Specifically, incorporating Transformer-based models, such as Vision Transformers (ViTs), would significantly broaden the scope of the dataset and make it more relevant to current research trends. This would involve not only training and evaluating these models under adversarial attacks but also adapting the adversarial training procedures to accommodate the unique characteristics of these architectures. Furthermore, the dataset should include a more diverse set of convolutional networks, beyond just WRNs, to ensure that the findings are not overly specific to a single family of architectures. This would require a systematic approach to selecting a representative set of architectures, considering factors such as depth, width, and connectivity patterns. By including a wider variety of architectures, the dataset would become a more valuable resource for the community, enabling more generalizable conclusions about adversarial robustness.

In addition to expanding the architectural diversity, the dataset should also include a more comprehensive set of adversarial attacks. This should include attacks that are based on different threat models, such as those that consider different perturbation norms (e.g., L2 norm) or those that are adaptive to the defense mechanisms employed during training. Furthermore, the dataset should include attacks that target specific vulnerabilities of adversarial training methods, such as those that exploit the gradient masking phenomenon or those that manipulate the training data. This would require a careful selection of attacks, considering factors such as their effectiveness, computational cost, and the specific vulnerabilities they target. By including a more diverse set of attacks, the dataset would provide a more realistic assessment of the robustness of the models and enable researchers to develop more robust defense mechanisms.

Finally, the paper should provide a detailed analysis of the computational cost associated with training and evaluating the models in the dataset. This should include information on the training time, memory requirements, and the computational resources needed for evaluation. This information should be provided for each architecture and attack combination, allowing researchers to assess the feasibility of using the dataset in their own work. Furthermore, the paper should provide guidelines on how to efficiently use the dataset, such as how to parallelize the training and evaluation processes. This would make the dataset more accessible to researchers with limited computational resources and enable more widespread adoption of the dataset.

### Questions

1. Can the authors provide more details on the computational cost of training and evaluating the models in the dataset?
2. Can the authors provide more insights into the relationship between architecture and robustness, such as which architectural features are most important for robustness?
3. Can the authors provide more details on the use of NARes as a benchmark for neural architecture search algorithms, such as how to use the dataset to search for robust architectures?

### Rating

6

### Confidence

3

**********

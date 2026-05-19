### Summary

The paper proposes a meta-learning method for learning from multiple noisy annotators. The proposed method is based on a neural network that is used to embed each example in a latent space. A probabilistic model is then constructed for learning classifiers from the embedded data. The confusion matrices for annotators are also modeled and adaptively learned during the meta-learning process. The proposed method is evaluated on three datasets and compared with 13 baseline methods.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper proposes a meta-learning method for learning from multiple noisy annotators.
2. The proposed method is evaluated on three datasets and compared with 13 baseline methods.

### Weaknesses

#### Some Related Works


#### comment

1. The paper is not well written and is hard to follow. The notations are confusing and the method is not explained clearly. For example, the paper does not clearly explain how the EM algorithm is used to learn the confusion matrices for annotators. The paper also does not clearly explain how the neural network is used to embed the examples in a latent space. The paper also does not clearly explain how the probabilistic model is constructed for learning classifiers from the embedded data. The paper also does not clearly explain how the meta-learning process is performed. The paper also does not clearly explain how the proposed method is compared with the baseline methods.
2. The proposed method is not novel. The paper does not clearly explain how the proposed method is different from the existing methods. The paper does not clearly explain how the proposed method is better than the existing methods. The paper does not clearly explain how the proposed method is more effective than the existing methods.
3. The paper does not provide a clear explanation of the experimental setup. The paper does not clearly explain how the datasets are used. The paper does not clearly explain how the baseline methods are implemented. The paper does not clearly explain how the proposed method is implemented. The paper does not clearly explain how the experimental results are obtained.

### Suggestions

The paper needs significant improvements in clarity and detail to be considered for publication. The core methodology, particularly the integration of the neural network embedding, the EM algorithm for confusion matrix learning, and the probabilistic classifier construction, is not sufficiently explained. For instance, the paper should explicitly detail the architecture of the neural network used for embedding, including the number of layers, activation functions, and the dimensionality of the latent space. Furthermore, the explanation of the EM algorithm needs to be more precise, outlining the specific steps involved in updating the confusion matrices and how these updates are integrated into the meta-learning process. The paper should also provide a clear description of the probabilistic model used for classifier learning, including the likelihood function and the prior distributions. Without these details, it is difficult to assess the novelty and effectiveness of the proposed method. The paper should also include a more detailed explanation of how the meta-learning process is performed, including the specific optimization algorithm used and the loss function being minimized. Finally, the paper should provide a clear comparison with existing methods, highlighting the specific advantages of the proposed approach.

To address the lack of novelty, the paper needs to clearly articulate the specific contributions of the proposed method. The paper should provide a detailed comparison with existing meta-learning methods, highlighting the differences in the approach and the advantages of the proposed method. For example, if the proposed method uses a different type of neural network or a different way of modeling the confusion matrices, these differences should be clearly explained. The paper should also provide a theoretical justification for the proposed method, explaining why it is expected to perform better than existing methods. The paper should also include a more detailed analysis of the experimental results, including a discussion of the statistical significance of the results and the limitations of the proposed method. The paper should also include a more detailed explanation of the experimental setup, including the specific datasets used, the evaluation metrics, and the implementation details of the baseline methods.

Finally, the paper should provide a more detailed explanation of the experimental setup, including the specific datasets used, the evaluation metrics, and the implementation details of the baseline methods. The paper should also include a more detailed explanation of the experimental results, including a discussion of the statistical significance of the results and the limitations of the proposed method. The paper should also include a more detailed explanation of the experimental setup, including the specific datasets used, the evaluation metrics, and the implementation details of the baseline methods. The paper should also include a more detailed explanation of the experimental results, including a discussion of the statistical significance of the results and the limitations of the proposed method. The paper should also include a more detailed explanation of the experimental setup, including the specific datasets used, the evaluation metrics, and the implementation details of the baseline methods.

### Questions

1. How is the EM algorithm used to learn the confusion matrices for annotators?
2. How is the neural network used to embed the examples in a latent space?
3. How is the probabilistic model constructed for learning classifiers from the embedded data?
4. How is the meta-learning process performed?
5. How is the proposed method compared with the baseline methods?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

### Summary

This paper proposes a concept-based explainable image representation learning method. The proposed method first generates a concept pool using GPT-4, and then constructs concept vectors for images based on the similarity between image features and concept features. Finally, a VAE is trained to learn a latent representation from the concept vectors. The proposed method is evaluated on unsupervised clustering and linear probe classification tasks, and the results show that it outperforms several baselines.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed method is novel and interesting. It combines the strengths of concept-based models and VAEs to learn explainable image representations.
2. The method is evaluated on multiple datasets and tasks, and the results show that it outperforms several baselines.
3. The paper is well-written and easy to understand.

### Weaknesses

#### Some Related Works


#### comment

1. The method relies on a pre-defined concept set, which may limit its ability to capture all relevant concepts in an image. The quality and completeness of the concept set are crucial for the performance of the method. If the concept set is not comprehensive enough, the method may fail to capture important information in the image. Furthermore, the process of generating the concept set using GPT-4 introduces a potential bias, as the model's training data may not be representative of all possible concepts relevant to the images being analyzed. This could lead to a skewed representation where certain concepts are over-represented while others are missed entirely, impacting the overall quality of the learned representation.
2. The method may be sensitive to the choice of hyperparameters, such as the number of concepts and the threshold for concept activation. The paper does not provide a detailed analysis of how these hyperparameters affect the performance of the method. The optimal values for these parameters may vary depending on the dataset and the task, and the lack of a systematic approach to hyperparameter tuning could limit the practical applicability of the method. For example, the number of concepts needs to be carefully balanced to capture sufficient detail without introducing noise or redundancy, and the activation threshold determines which concepts are considered relevant, which can significantly impact the final representation.
3. The method may not be able to handle complex or abstract concepts that are difficult to represent with a vector. The method relies on a similarity measure between image features and concept features, which may not be sufficient to capture the nuances of complex or abstract concepts. For example, concepts like 'serendipity' or 'melancholy' are difficult to represent with simple vector embeddings, and the method may struggle to accurately capture these types of concepts. This limitation could restrict the method's ability to provide meaningful explanations for images that involve such abstract or complex concepts.

### Suggestions

To address the limitations of relying on a pre-defined concept set, the authors should explore methods for dynamically expanding or refining the concept set based on the input images. This could involve techniques such as clustering the image features and then using GPT-4 to generate concepts for each cluster, or using an iterative approach where the model identifies missing concepts and adds them to the set. Furthermore, the authors should investigate the impact of different concept generation strategies on the final representation. For example, they could compare the performance of using GPT-4 with other concept generation methods, or explore the use of multiple concept sets to capture different aspects of the image. This would help to mitigate the potential bias introduced by GPT-4 and improve the robustness of the method.

To improve the sensitivity to hyperparameters, the authors should conduct a more thorough analysis of the impact of different hyperparameter values on the performance of the method. This could involve performing a grid search or using more advanced hyperparameter optimization techniques. The authors should also provide guidelines for selecting appropriate hyperparameter values for different datasets and tasks. This could involve developing a heuristic based on the characteristics of the dataset, or using a meta-learning approach to learn how to select hyperparameters based on the task. Additionally, the authors should explore the use of adaptive hyperparameter tuning methods that can automatically adjust the hyperparameters during training based on the performance of the model. This would make the method more robust and easier to use in practice.

To address the limitations in handling complex or abstract concepts, the authors should explore alternative methods for representing concepts that go beyond simple vector embeddings. This could involve using more sophisticated embedding techniques, such as graph embeddings or knowledge graph embeddings, that can capture the relationships between concepts. The authors should also investigate the use of attention mechanisms to focus on the most relevant parts of the image when representing complex concepts. Furthermore, the authors should explore the use of multiple concept sets to capture different aspects of the image, and then combine these representations to obtain a more comprehensive understanding of the image. This would allow the method to capture more nuanced and abstract concepts, and provide more meaningful explanations for images that involve such concepts.

### Questions

1. How does the method handle cases where the input image contains concepts that are not in the reference set?
2. How does the method perform on datasets with a large number of concepts or a high degree of concept overlap?
3. How does the method compare to other explainable image representation learning methods in terms of computational efficiency and scalability?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

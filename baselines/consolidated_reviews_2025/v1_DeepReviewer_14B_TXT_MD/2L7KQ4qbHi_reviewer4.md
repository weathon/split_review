### Summary

This paper introduces a new problem setting called concept forgetting, which aims to remove the influence of undesired concepts from a pre-trained classification model. To address this problem, the authors propose a novel algorithm called Label Annealing (LAN). The LAN algorithm iteratively assigns pseudo-labels to samples based on the model's predictions and fine-tunes the model on the pseudo-labeled data. The authors demonstrate the effectiveness of LAN on various datasets and models, showing that it can reduce concept violation while maintaining high model accuracy.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper introduces a new problem setting called concept forgetting, which is an important and relevant problem in machine learning.
- The proposed LAN algorithm is novel and effective in addressing the concept forgetting problem.
- The paper provides a thorough evaluation of the proposed method on various datasets and models, demonstrating its effectiveness.
- The paper is well-written and easy to understand.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a clear definition of what constitutes a "concept" in the context of machine learning models. This lack of clarity makes it difficult to understand the scope and limitations of the proposed method.
- The paper does not discuss the potential limitations of the proposed method. For example, it is unclear how the method would perform on more complex concepts or in scenarios where the undesired concepts are highly correlated with the desired concepts.
- The paper does not provide a detailed analysis of the computational cost of the proposed method. It is unclear how the method scales with the size of the dataset and the complexity of the model.

### Suggestions

The paper should provide a more rigorous definition of what constitutes a 'concept' within the context of machine learning models. Currently, the notion of a concept is vague, making it difficult to assess the applicability and limitations of the proposed method. For instance, is a concept a high-level semantic feature, a specific pattern in the input space, or something else entirely? Providing a formal definition, perhaps using the language of information theory or representational similarity analysis, would greatly enhance the clarity and rigor of the work. This definition should also clarify how concepts are represented within the model's latent space, and how the proposed method interacts with these representations to achieve concept forgetting. Without a clear definition, it is hard to evaluate the method's effectiveness and generalizability.

Furthermore, the paper should include a more thorough discussion of the limitations of the proposed method. The current evaluation, while demonstrating the method's effectiveness on several datasets, does not explore scenarios where the undesired concepts are highly correlated with the desired concepts. In such cases, it is likely that removing the undesired concept will also negatively impact the model's performance on the desired concept. The paper should also investigate the method's performance on more complex concepts, such as those involving multiple features or abstract reasoning. For example, how would the method perform if the concept to be forgotten is not a simple attribute like 'color' but a more complex one like 'style' or 'mood'? A more comprehensive analysis of these limitations would provide a more realistic assessment of the method's applicability and potential for future research.

Finally, the paper should provide a detailed analysis of the computational cost of the proposed method. While the authors mention that the method is efficient, they do not provide any quantitative analysis of its runtime or memory usage. It is important to understand how the method scales with the size of the dataset, the complexity of the model, and the number of iterations required for convergence. This analysis should include a comparison with other relevant methods, such as retraining the model from scratch or using other concept forgetting techniques. This would allow readers to assess the practical feasibility of the proposed method and its suitability for different applications. The analysis should also include a discussion of the trade-offs between computational cost and performance, providing guidance on how to choose the appropriate parameters for the method.

### Questions

- Can you provide a more detailed explanation of how the LAN algorithm works, including the specific steps involved in the label annealing process?
- How does the proposed method compare to other existing methods for addressing similar problems, such as machine unlearning or adversarial debiasing?
- What are the potential limitations of the proposed method, and how can they be addressed in future work?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

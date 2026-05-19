### Summary

This paper introduces Graph-Induced Sum-Product Networks (GSPNs), a probabilistic framework for graph representation learning that can answer probabilistic queries. The authors show the model's competitiveness on scarce supervision scenarios, under missing data, and for graph classification in comparison to popular neural models.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The authors propose a probabilistic framework for graph representation learning, which is a novel contribution to the field.
2. The authors show the model's competitiveness on scarce supervision scenarios, under missing data, and for graph classification in comparison to popular neural models.

### Weaknesses

#### Some Related Works


#### comment

1. The authors claim that GSPNs can tractably answer probabilistic queries, but they do not provide any empirical evidence to support this claim. Specifically, while the paper mentions that the model can compute marginal probabilities, it does not demonstrate this capability on real-world graph data or compare it to existing methods for probabilistic inference on graphs. The lack of such experiments makes it difficult to assess the practical utility of this feature.
2. The authors do not discuss the limitations of their proposed framework. For example, how does the model perform on large graphs? What are the computational and memory requirements of the model? How does the model handle noisy or incomplete data? The paper lacks a discussion on the scalability of the approach, particularly concerning the computational complexity of inference and learning with respect to graph size and the number of parameters in the sum-product network. Furthermore, the paper does not address the potential impact of noisy or missing features on the model's performance, which is a critical consideration for real-world applications.

### Suggestions

To strengthen the paper, the authors should include experiments that explicitly demonstrate the model's ability to answer probabilistic queries on real-world graph data. This could involve tasks such as computing marginal probabilities of node or edge attributes, or performing conditional inference given partial observations. The experiments should compare the performance of GSPNs with existing probabilistic graph models, such as Markov Random Fields or Probabilistic Graphical Models, to highlight the advantages and limitations of the proposed approach. Furthermore, the authors should provide a detailed analysis of the computational complexity of the model, including the time and memory requirements for both training and inference. This analysis should consider the impact of graph size, number of features, and the depth of the sum-product network. It would be beneficial to include experiments on graphs of varying sizes to demonstrate the scalability of the approach. 

Additionally, the authors should investigate the robustness of the model to noisy or incomplete data. This could involve experiments where a portion of the node or edge attributes are randomly masked or corrupted. The performance of the model should be evaluated under different levels of noise and missing data, and the results should be compared to other graph representation learning methods. This analysis would provide valuable insights into the practical applicability of the proposed framework. The authors should also discuss the limitations of the model in terms of its expressiveness and its ability to capture complex dependencies in the data. For example, it would be useful to discuss whether the model can capture long-range dependencies or whether it is limited to local interactions. 

Finally, the authors should provide a more detailed discussion of the hyperparameter selection process. This should include a sensitivity analysis of the model's performance with respect to different hyperparameter values. The authors should also discuss the computational cost of hyperparameter tuning and provide recommendations for selecting appropriate values for different datasets. It would be beneficial to include a table or figure that summarizes the optimal hyperparameter values for the datasets used in the experiments. This would make it easier for other researchers to reproduce the results and apply the proposed framework to new problems.

### Questions

1. How does the model perform on large graphs?
2. What are the computational and memory requirements of the model?
3. How does the model handle noisy or incomplete data?
4. What are the limitations of the proposed framework?
5. How does the model compare to other probabilistic graph models in terms of performance and scalability?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

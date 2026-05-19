### Summary

The paper proposes a probabilistic framework for graph representation learning, called Graph-Induced Sum-Product Networks (GSPNs), which can answer probabilistic queries. The authors show the model's competitiveness on scarce supervision scenarios, under missing data, and for graph classification in comparison to popular neural models.

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

1. The authors claim that GSPNs can tractably answer probabilistic queries, but they do not provide any empirical evidence to support this claim. 
2. The authors do not discuss the limitations of their proposed framework. For example, how does the model perform on large graphs? What are the computational and memory requirements of the model?

### Suggestions

The paper introduces Graph-Induced Sum-Product Networks (GSPNs) as a novel probabilistic framework for graph representation learning. While the core idea of using sum-product networks within a graph context is interesting, the paper would benefit from a more thorough empirical evaluation of its ability to answer probabilistic queries. Specifically, the authors should provide concrete examples of how GSPNs can be used to perform tasks such as computing marginal probabilities of node or edge attributes, or predicting the likelihood of certain graph structures. These examples should be accompanied by quantitative results that demonstrate the accuracy and efficiency of the proposed approach compared to existing methods. Furthermore, the authors should clarify the specific types of probabilistic queries that GSPNs can handle effectively and discuss any limitations in terms of query complexity or graph size. This would help to better understand the practical applicability of the proposed framework.

To address the lack of discussion on limitations, the authors should include a more detailed analysis of the computational and memory requirements of GSPNs, especially when applied to large graphs. This analysis should consider the impact of graph size, the number of features, and the depth of the sum-product network on the overall performance. It would be beneficial to provide a theoretical analysis of the time and space complexity of the model, as well as empirical results on graphs of varying sizes. Additionally, the authors should discuss the potential challenges of applying GSPNs to graphs with noisy or incomplete data, and how the model can be made more robust to such issues. This would help to better understand the practical limitations of the proposed framework and guide future research in this area.

Finally, the authors should provide a more detailed comparison of GSPNs with other probabilistic graph models, such as Markov Random Fields or Probabilistic Graphical Models. This comparison should highlight the advantages and disadvantages of GSPNs in terms of expressiveness, computational efficiency, and ease of implementation. It would also be useful to discuss the potential for combining GSPNs with other graph learning techniques, such as graph neural networks, to leverage the strengths of both approaches. This would help to better position the proposed framework within the broader landscape of graph representation learning and identify potential avenues for future research.

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

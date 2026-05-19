### Summary

This paper introduces a new probabilistic framework for graph representation learning, called Graph-Induced Sum-Product Networks (GSPNs). The proposed model is a hierarchy of sum-product networks (SPNs) that can answer probabilistic queries and learn from unlabeled data. The paper evaluates the model on scarce supervision scenarios, under missing data, and for graph classification, and shows its competitiveness with neural models. The paper also provides qualitative analyses on hyper-parameters and the model's ability to answer probabilistic queries.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper proposes a novel and original model that combines the advantages of probabilistic circuits and deep graph networks, which is a significant contribution to the field of graph representation learning.
- The paper is well-written and organized, with clear explanations of the background, related work, methodology, and experiments. The paper uses appropriate notations and figures to illustrate the concepts and results.
- The paper conducts extensive experiments on various datasets and tasks, and compares the proposed model with several baselines, both neural and probabilistic. The paper shows that the proposed model is competitive or superior to the baselines in terms of performance, robustness, and efficiency.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a clear explanation of how the SPNs are constructed and parameterized, and how the learnable transformations are implemented and optimized. The paper could benefit from providing more details and examples of the SPN structure and parameters, and how they relate to the graph structure and attributes.
- The paper does not discuss the limitations and potential drawbacks of the proposed model, such as the sensitivity to the choice of hyper-parameters, the scalability to large graphs, or the interpretability of the learned representations. The paper could also compare the proposed model with other probabilistic models for graphs, such as Bayesian networks or Markov networks, and highlight the advantages and disadvantages of each approach.

### Suggestions

The paper should provide a more detailed explanation of the Sum-Product Network (SPN) construction and parameterization. Specifically, it should clarify how the scopes of the distribution units are determined, and how the parameters of these units are initialized and updated during training. For example, if Gaussian distributions are used, the paper should explain how the mean and variance parameters are associated with the vertex attributes and how these parameters are learned. Furthermore, the paper should elaborate on the specific form of the learnable transformations applied to the posterior probabilities of the sum nodes. It is crucial to understand how these transformations are implemented, what their functional form is (e.g., linear, non-linear), and how they are optimized within the overall learning process. Providing concrete examples of how these transformations operate on the posterior probabilities would greatly enhance the clarity of the method. For instance, if a linear transformation is used, the paper should specify the dimensionality of the weight matrix and how it relates to the number of children of a sum node. 

To address the lack of discussion on limitations, the paper should include a more thorough analysis of the model's sensitivity to hyperparameter choices. This should include a discussion of how the number of layers, the number of states in the categorical latent variable, and the choice of aggregation function affect the model's performance. The paper should also discuss the computational complexity of the proposed model, especially in relation to the size of the input graphs. While the paper mentions that the complexity is linear in the number of edges, it should provide a more detailed analysis of the memory requirements and the practical scalability of the model to large graphs. Furthermore, the paper should discuss the interpretability of the learned representations. While the model is probabilistic, it is not clear how the learned parameters and transformations can be interpreted in terms of the underlying graph structure and attributes. The paper should provide some analysis of the learned representations and discuss how they can be used to gain insights into the data.

Finally, the paper should include a more comprehensive comparison with other probabilistic models for graphs. While the paper compares the proposed model with neural models, it should also compare it with other probabilistic approaches such as Bayesian networks and Markov networks. The paper should discuss the advantages and disadvantages of each approach in terms of their expressiveness, computational complexity, and ability to handle uncertainty and missing data. For example, the paper could discuss how the proposed model compares to a Bayesian network in terms of its ability to capture conditional dependencies between variables, or how it compares to a Markov network in terms of its ability to model the joint distribution over the graph. This comparison would help to contextualize the proposed model within the broader landscape of probabilistic graph models and highlight its unique contributions.

### Questions

- How are the scopes of the distribution units in the SPNs determined? Are they fixed or learned? How do they relate to the vertex attributes?
- How are the parameters of the SPNs initialized and updated? What are the constraints on the parameters to ensure the validity of the SPNs?
- How are the learnable transformations of the posterior probabilities implemented and optimized? What is the functional form of the transformations? How do they affect the uncertainty and diversity of the representations?
- How does the proposed model handle edge attributes and different types of graphs, such as directed, undirected, or heterogeneous graphs?
- How does the proposed model compare to other probabilistic models for graphs, such as Bayesian networks or Markov networks, in terms of expressiveness, complexity, and performance?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

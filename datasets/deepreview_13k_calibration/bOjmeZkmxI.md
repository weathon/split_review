# Genetic-evolutionary Graph Nerual Networks: A Paradigm for Improved Graph Representation Learning

- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 3, 3, 6

## Abstract
Message-passing graph neural networks have become the dominant framework for learning over graphs. However, empirical studies continually show that message-passing graph neural networks tend to generate over-smoothed representations for nodes after iteratively applying message passing. This over-smoothing problem is a core issue that limits the representational capacity of message-passing graph neural networks. We argue that the fundamental problem with over-smoothing is a lack of diversity in the generated embeddings, and the problem could be reduced by preserving the embedding diversity in their generation process. To this end, we propose genetic-evolutionary graph neural networks, a new paradigm for graph representation learning inspired by genetic algorithms. We model each layer of a graph neural network as an evolutionary process and develop operations based on crossover and mutation to prevent embeddings from becoming similar to one another, thus enabling the model to generate improved graph representations. The proposed framework is interpretable, as it directly draws inspiration from genetic algorithms for preserving population diversity. We experimentally validate the proposed framework on six benchmark datasets on different tasks. The results show that our method significant advances the performance current graph neural networks, resulting in new state-of-the-art results for graph representation learning on the datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a novel framework for enhancing graph neural network (GNN) models by integrating genetic algorithm concepts such as crossover and mutation into the training process. This approach aims to combat the pervasive over-smoothing problem in conventional GNNs by maintaining diversity in node embeddings, thereby allowing the model to capture more complex graph structures and relationships. The results from experiments on several benchmark datasets indicate significant performance improvements over existing methods, making a compelling case for the use of evolutionary strategies in graph representation learning.

### Strengths
originality: medium
quality: good
clarity: good
significance: medium

### Weaknesses
1. "it is important to perserve the diversity of generated embeddings throughout their layerwisely generation process." It is true that a GNN with good performance needs some extent of diversity in the node embedding. However, is it also true that diverse embedding will definitely lead to good performance? In other words, is diverse embedding a sufficient condition for good GNN performance?

2. Equation (2) and (3) look like random pooling operations. Is there any relation?

3. How many layers does the model have in your experiments?

4. How does your model performance changes as the layer goes to deep? Need ablation study for different operations in your model.

5. How does your model work on node classification problem, especially on heterophilic graphs[1]?

### Questions
1. "it is important to perserve the diversity of generated embeddings throughout their layerwisely generation process." It is true that a GNN with good performance needs some extent of diversity in the node embedding. However, is it also true that diverse embedding will definitely lead to good performance? In other words, is diverse embedding a sufficient condition for good GNN performance?

2. Equation (2) and (3) look like random pooling operations. Is there any relation?

3. How many layers does the model have in your experiments?

4. How does your model performance changes as the layer goes to deep? Need ablation study for different operations in your model.

5. How does your model work on node classification problem, especially on heterophilic graphs[1]?




[1] When Do Graph Neural Networks Help with Node Classification? Investigating the Homophily Principle on Node Distinguishability. Advances in Neural Information Processing Systems. 2024 Feb 13;36.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a new approach, called Genetic-Evolutionary Graph Neural Networks, to enhance graph representation learning by tackling the well-known over-smoothing issue in message-passing graph neural networks (MP-GNNs). The method introduces three key operations — cross-generation crossover, sibling crossover, and mutation — within a genetic evolution-inspired framework. These operations are designed to sustain diversity in node embeddings, providing interpretability and adaptability to existing MP-GNNs. The paper validates the model’s performance across six benchmark datasets, achieving ideal results on graph-related tasks.

### Strengths
Originality: This application of genetic-inspired methods to maintain embedding diversity is a creative approach.

Quality: The proposed framework is validated through experiments on multiple benchmark datasets, and the results indicate an improvement over the baseline models. 

Clarity: The paper clearly outlines its methodology, with illustrative examples for the proposed genetic operations. 

Significance: By offering a generalizable approach to improving MP-GNNs without adding complex parameters, this work has potential relevance to broader applications in graph learning.

### Weaknesses
1. I recommend that the authors include a review of existing literature in the introduction to highlight the contribution of this study and its distinctions from previous work.

2. The over-smoothing problem can be mitigated through graph structure learning, residual connections, and similar techniques. I suggest that the authors add baseline experiments with these approaches.

3. The Related Work section have not evolutionary-based GNNs, but there has been considerable research in this area, like literatures [1,2]. I recommend including a discussion of these relevant studies.

4. I suggest that the authors use a more general pseudocode format (e.g., a higher-level process description) instead of framework-specific syntax to better adhere to pseudocode standards—focusing on the logical flow rather than the framework implementation. This will enhance the paper’s accessibility and allow readers without a specific framework background to more easily understand the algorithm’s principles.

5. To improve the transparency and reproducibility of this research, I recommend that the authors consider open-sourcing their code to promote academic exchange and development in this field.

6. The Crossover and Mutation operations in this paper are not sufficiently innovative.

### Questions
Please refer to the comments provided in the "Weaknesses" section for further details.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper deals with message passing on graph structures. The authors propose a method to tackle oversmoothing issue in the graph neural networks. They first posit that the main problem with over-smoothing is the lack of diversity in the embeddings, and propose to use techniques that can bias the embedding generation process to maintain diversity during message iterations. They propose an algorithm which mimics some operations from evolutionary theory i.e. crossover and mutation. Importantly, they introduce two crossover operations, i.e., generation crossover and sibling crossover, and a mutation operation, interleaved with the current message passing paradigm. Experiments on various datasets show that the method improves prediction capacity of GNNs.

### Strengths
1. The paper addresses an important problem of oversmoothing seen in GNNs..
1. The proposed crossover and mutation operations are interesting. However, the need and analysis of their effectiveness needs more detailed study.
1. The paper is easy to follow.

### Weaknesses
1. For evolutionary theory to work, it relies on randomness and scale i.e. over large number of iterations, small changes produce variety and adaptable traits.  How many iterations can GNN be applied for a reasonable analogy to the theoretical foundations of evolutionary theory is unclear. Specifically, the paper does not provide a clear justification for the number of message passing steps used in relation to the proposed evolutionary operations. The effectiveness of these operations may be highly dependent on the number of iterations, and without a proper analysis, it is difficult to assess the robustness of the method.

2. The authors say - This makes it interpretable and easy for understanding. It is not clear how does this make it more interpretable, when it is making more random and introducing distinctness, even in cases when there is no need based on features or structure. The introduction of crossover and mutation operations, while inspired by evolutionary algorithms, does not inherently lead to better interpretability. In fact, the increased randomness could make it harder to understand the learned representations, especially if the operations are applied without considering the underlying graph structure or node features. The paper needs to clarify how these operations enhance interpretability rather than simply increasing diversity.

3. After Crossover operation and mutation, evolutionary pressures which select the fit traits and the rest are discarded i.e. fail to reproduce enough. However, I do not see how these selection is happening in the GNN framework. If there is no selection, then it means all crossover and mutations are good, which is contrary to evolutionary theory. The absence of a selection mechanism is a significant deviation from the core principles of evolutionary theory. Without selection, the method risks introducing unhelpful or even detrimental changes to the node embeddings. The paper needs to address how the lack of selection impacts the overall performance and whether the proposed operations are truly beneficial in the absence of a selection process.

4. Typos: Line 125, 134, 208,

### Questions
Please see weaknesses.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a novel framework for graph neural networks (GNNs) called Genetic-Evolutionary Graph Neural Networks (GE-GNNs), aimed at enhancing graph representation learning by addressing the issue of over-smoothing in GNNs. Over-smoothing is a phenomenon where node representations become too similar, limiting the model’s effectiveness in distinguishing between different nodes. The authors propose to mitigate this by using genetic algorithms, specifically through evolutionary mechanisms such as crossover and mutation operations.

### Strengths
1. The paper clearly identifies the key issue of GNNs—over-smoothing—and proposes using genetic algorithms to address this problem.

2. The framework primarily relies on evolutionary operations, which is a compelling idea.

3. The evaluation appears very solid, covering different tasks and datasets.

### Weaknesses
1. The evaluation could be more balanced. GPS is a strong GNN model, and the authors should demonstrate that the proposed framework performs well with other GNN architectures, such as applying genetic algorithms with GCN.

2. The authors could consider adding more detailed descriptions of how the evolutionary operators function within the proposed framework. From my understanding, this framework operates similarly to other GNNs optimized by backpropagation, while evolutionary algorithms (EAs) traditionally do not rely on backpropagation. In this context, the evolutionary operators seem to act more like activation functions or non-parametric layers, primarily generating diverse outputs that are subsequently optimized through backpropagation. Clarifying this distinction would help readers better understand the role and novelty of these operators within the framework.

3. If I missed any details, please correct me. There are two types of crossover operators—why didn’t the authors consistently apply both across all datasets?

4. The ablation study is not convincing.

5. How many repeated experiments did you run, considering that crossover and mutation introduce randomness? Are all results statistically significantly different?

### Questions
see above

### Soundness
3

### Presentation
4

### Contribution
3

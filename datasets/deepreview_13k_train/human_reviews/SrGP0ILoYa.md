# TopER: Topological Embeddings in Graph Representation Learning

- Decision: Reject
- Scores: 6, 6, 5, 8

## Abstract
Graph embeddings play a critical role in graph representation learning, allowing machine learning models to explore and interpret graph-structured data. However, existing methods often rely on opaque, high-dimensional embeddings, limiting interpretability and practical visualization. 

In this work, we introduce Topological Evolution Rate (TopER), a novel, low-dimensional embedding approach grounded in topological data analysis. TopER simplifies a key topological approach, Persistent Homology, by calculating the evolution rate of graph substructures, resulting in intuitive and interpretable visualizations of graph data. This approach not only enhances the exploration of graph datasets but also delivers competitive performance in graph clustering and classification tasks. Our TopER-based models achieve or surpass state-of-the-art results across molecular, biological, and social network datasets in tasks such as classification, clustering, and visualization.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents TopER, an innovative method for graph embedding based on topological data analysis (TDA). TopER introduces an efficient approach to graph representation learning by simplifying Persistent Homology, particularly in creating embeddings that capture the evolution of graph substructures. Instead of traditional graph neural network (GNN)-based methods, TopER focuses on generating interpretable, low-dimensional embeddings through filtration and linear regression on subgraph evolution rates. It shows competitive performance in clustering and classification tasks across various datasets, such as molecular and social networks, underscoring its utility for interpretable, scalable graph embeddings.

### Strengths
Innovative Approach: The paper introduces TopER, a novel method based on Topological Data Analysis (TDA) that simplifies Persistent Homology for graph embedding. By tracking the evolution rate of graph substructures, TopER provides a low-dimensional, interpretable graph representation, enabling it to capture graph structure effectively without high computational costs.
ss
Computational Efficiency: The limitations in computational efficiency are crucial since they directly impact the scalability of TopER for large real-world applications, a primary goal of embedding methods. Improving this area could make TopER more viable for large-scale datasets in practice.

Good Interpretability and Visualization: The two-dimensional embeddings produced by TopER offer strong interpretability, allowing users to easily identify clusters, outliers, and structural features within datasets. Unlike higher-dimensional embeddings, which are often challenging to interpret, TopER is well-suited for data exploration and graph visualization.

### Weaknesses
Lack of Threshold Setting Details: The paper does not explain how thresholds are set for different filtration functions, nor how the number of subgraphs n is determined. Since both threshold choice and n could impact results, further analysis would be valuable. Specifically, the paper should detail the range of thresholds explored for each filtration function and the criteria used to select the final set of thresholds. The impact of varying the number of subgraphs, n, on the stability and performance of the embeddings should also be analyzed.

Clarity on Embedding Dimension: The paper lacks details on TopER’s final embedding dimension and does not directly compare it to the embedding dimensions of other algorithms. Embedding dimension is crucial for evaluating performance and computational efficiency, so specifying and comparing the dimensions of different methods would enhance the clarity and interpretability of the results. The paper should explicitly state the final dimensionality of the embeddings produced by TopER for each dataset and provide a rationale for these choices. A comparison with the embedding dimensions of other graph embedding methods, such as node2vec or GNN-based approaches, would help contextualize the computational cost and expressiveness of TopER.

Dataset-Specific Dimension Variability: Line 394 mentions "top-performing combinations of filtration and vectorization for each dataset," which suggests that embedding dimensions might vary across datasets. However, the paper does not clarify what these combinations are or discuss the impact of using different combinations across datasets, especially given the many possible configurations with the eight filtration functions. The paper needs to clarify how the selection of filtration functions is performed for each dataset, and how this selection impacts the final embedding dimension. A detailed analysis of the performance of different filtration function combinations across various datasets is needed to understand the generalizability of the approach.

Ablation Study Needs More Analysis: The ablation study does not analyze the effects of each filtration function on individual datasets, missing insights into how specific functions influence results across different types of data. The paper should include a detailed analysis of how each filtration function contributes to the overall performance on each dataset. This analysis should include not only the performance of each function individually but also how different combinations of functions affect the results.

### Questions
See from Paper Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a novel approach to train low-dimensional graph embeddings inspired by topological graph data analysis. Their method, Topological Evolution Rate (TopER), argues that the graph structure can be characterized by the linear function that relates how the number of edges relates to the number of nodes in the graphs induced by the nodes/edges that have a given value of a property such as degree. Through experiments, they show superior performance in graph classification, clustering, and interpretability. Furthermore, their method enables embedding different graph datasets in a shared embedding space, which is interesting.

### Strengths
- The paper is well-written with minimal typos and gives a good background of topological learning. 
- Experiments are mostly thorough and provide a comparison against different baselines, especially for graph classification. 
- The ability to train a shared interpretable embedding space of different graph datasets is interesting and has a lot of potential impact.
- The proposed method is computationally efficient and shows significant gains in performance.

### Weaknesses
 - Motivation behind the method is lacking: The paper provides very little motivation behind the actual methodology.
  - It is not clear what the correlation between the number of edges and number of nodes of the induced graphs wrt a filtration function has to do with how the graph is characterized/classified.
  - It is not clearly stated why there should be a linear correlation between the two numbers. The motivating figures also do not motivate a linear correlation, except for MUTAG.
  - If there is a relation with persistence homology, then it should be discussed.
- The method is limited to non-attributed graphs and cannot easily extend to attributed graphs, for which it might depend on other graph kernels to be devised.
- High sensitivity to filtration functions: As can be noted by the ablation study, the performance is highly sensitive to the filtration functions used for a particular dataset. This limits the strengths since it is not clear if the set of filtration functions considered in this work are even exhaustive.
- Training an MLP on top of (a, b) of different filtration functions also limits the interpretability since the discriminative features may be formed as a combination of different filtration trends. Furthermore, using a single filtration function is always less performative than using multiple functions, which means the evolution rate of no one function is capable of classifying the graphs accurately. 
- A simpler comparison should be provided that compares persistent homology and TopER in their time complexity and graph classification accuracy assuming the same filtration function. 
- Hyperparameter analysis of the number of thresholds is missing. 
- Empirical comparison with some important baselines is not provided:
  - Immonen, Johanna, Amauri Souza, and Vikas Garg. "Going beyond persistent homology using persistent homology." Advances in Neural Information Processing Systems 36 (2024).
  - Hofer, Christoph, et al. "Graph filtration learning." International Conference on Machine Learning. PMLR, 2020.
  - Rieck, Bastian, Christian Bock, and Karsten Borgwardt. "A persistent weisfeiler-lehman procedure for graph classification." International Conference on Machine Learning. PMLR, 2019.

### Questions
See above weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents Topological Evolution Rate (TopER), a novel low-dimensional embedding method based on topological data analysis for intuitive and interpretable graph representations. TopER achieves competitive performance in graph clustering and classification, with strong results across diverse datasets.

### Strengths
1. TopER introduces a topologically grounded, low-dimensional embedding approach that efficiently captures graph substructure evolution, simplifying the computation-heavy process of Persistent Homology.

2. TopER provides clear, low-dimensional embeddings that highlight key topological features such as clusters and outliers, enhancing the ability to analyze individual and cross-dataset graphs.

### Weaknesses
1. The methodology briefly mentions alternatives to linear fitting, such as polynomial fits, but lacks detailed explanations. This omission raises questions about the impact of different fitting methods on the TopER vector and its adaptability to diverse graph types.
2. Although the linear regression on filtration sequences is computationally simpler than full Persistent Homology, the paper does not clarify how this process scales for large graphs with numerous filtration levels, making it uncertain whether the approach maintains efficiency for complex, high-dimensional data. Specifically, the paper does not specify how the thresholds for the filtration functions are determined, nor how the number of subgraphs 'n' is chosen, both of which could significantly impact the results. Further analysis is needed to understand the sensitivity of the method to these parameters.
3. The ablation study shows that combining different filtration functions improves performance. However, it does not clearly explain how each function helps or why they work well together. This makes it hard to know which functions are truly needed and which may just add extra complexity without much benefit. Furthermore, the paper mentions using 'top-performing combinations of filtration and vectorization for each dataset' but does not specify what these combinations are or discuss the impact of using different combinations across datasets. Given the numerous possible configurations with the filtration functions, this lack of clarity is a significant concern.

### Questions
Can the authors clarify why combining these specific filtration functions enhances performance in ablation study?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper focuses on characterizing graph topological structures with persistent homology methods. The proposed TopER rerpesents graphs with a sereis of graph filtrations and characterizes graphs with merely two parameters. Experimental results validate the effectiveness of the proposed TopER in generating self-supervised graph representations.

### Strengths
+ A novel simple yet framework to represent graphs with persistence homology.
+ Compared with existing mainstream graph contrastive learning based method, the proposed TopER is parameter-free while achieving promising results.
+ Solid experiments and ablation studies on the proposed TopER.
+ The paper is well written and easy to follow.

### Weaknesses
 - The reason of adapting linear regression to fit the filtration sequences is mentioned in the Appendix, yet no theoretical or experimental support are provided. Specifically, the paper lacks a discussion on why a linear fit is appropriate for the relationship between the number of nodes and edges in the filtration process. While the authors mention that the relationship is monotonic, this does not inherently justify a linear model. The paper should explore the implications of this choice, especially considering that graph growth might exhibit non-linear patterns.
- The key parts of TopER's implementation are missing from the provided repo link. The absence of the core code makes it difficult to reproduce the results and verify the claims made in the paper. This lack of transparency is a significant concern for the reproducibility of the research.
- The used filtration functions require further introduction and explanation. The paper does not adequately describe the specific filtration functions used, making it difficult to understand how the graph sequences are generated. This lack of clarity hinders the understanding and potential adoption of the proposed method.

### Questions
1. The `functions_to_calculate_[a,b]` folder in the anonymous repository appears to be empty. Could you explain why?
2. Is there a theoretical basis for the linear correlation between $a$ and $b$ ? How would the model performance when applying other fitting functions, such as polynomials?

### Soundness
3

### Presentation
4

### Contribution
4

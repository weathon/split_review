# KA-GAT: Kolmogorov–Arnold based Graph Attention Networks

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 3, 5

## Abstract
Graph Neural Networks (GNNs) have demonstrated remarkable capabilities in processing graph-structured data, but they often struggle with high-dimensional features and complex, nonlinear relationships. To address these challenges, we propose KA-GAT, a novel model that integrates Kolmogorov-Arnold Networks (KANs) with Graph Attention Networks (GATs). KA-GAT leverages KAN to decompose and reconstruct high-dimensional features, enhancing representational capacity, while a multi-head attention mechanism dynamically focuses on key graph components, improving interpretability. Experimental results on benchmark datasets, including Cora and Citeseer, demonstrate that KA-GAT achieves significant accuracy improvements compared to baseline models like GAT, with a relative gain of 4.5\% on Cora. These findings highlight KA-GAT’s robustness and potential as an interpretable and scalable solution for high-dimensional graph data, paving the way for further advancements in GNN research.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents KA-GAT, a new graph neural network for representation learning. KA-GAT combines the Kolmogorov-Arnold layer and classical graph attention layer to construct the graph neural network. Thus, the Kolmogorov-Arnold layer is claimed to improve the capability of handling complex data, and the multi-head attention layer can improve the flexibility and interpretability of the proposed KA-GAT. Experimental results obtained from classical graph datasets demonstrate that KA-GAT can outperform empirical GNNs.

### Strengths
1. The idea of making use of the Kolmogorov-Arnold layer and graph attention layer is interesting.
2. The model is flexible to integrate with other GNN layers.

### Weaknesses
1. Experimental results are somewhat insufficient. More test datasets or learning tasks should be included in the experiments. I would like to recommend the authors conduct more experiments on well-established datasets, e.g., Pubmed, CoauthorCS, Cora-full, CoauthorPH, Flickr, and ogbn-arxiv, and test KA-GAT with more learning tasks, e.g., graph classification.
2. Many recent GNNs are not well investigated in the manuscript. Examples include GATv2, APPNP, ADSF GNN, and ARMA GNN. It is also recommended that authors investigate other GNNs recently published in top-tier venues (e.g., NeurIPS, ICLR, ICML, TPAMI, AIJ, and JMLR).
3. Given 2, More recent GNNs are not compared with the proposed KA-GAT.
4. The contribution regarding algorithmic and methodological perspectives is limited. The proposed KA-GAT is based on the direct combinations of the Kolmogorov-Arnold layer and graph attention layer. Such a strategy might lack motivation. The authors are suggested to explicitly discuss why combining the Kolmogorov-Arnold layer and graph attention layer is effective in graph representation learning. Moreover, how the Kolmogorov-Arnold layer influences the performance of the proposed KA-GAT should be clearly discussed based on the experimental results. The current version of the manuscript (see Sec. 4.4.1 - 4.4.2) does not provide a meaningful analysis of the presented results. 
5. Theoretical guarantees or analysis of the proposed method (e.g., expressive power) are not provided.

### Questions
1. How does KA-GAT perform compared with other GNN baselines on more test datasets?
2. How does KA-GAT perform when compared with more recent GNN baselines?
3. The motivations behind the proposed approach should be well discussed and more recent approaches should be investigated.
4. Is there any theoretical analysis demonstrating the learning capabilities of KA-GAT?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes KA-GAT, a Graph Neural Network (GNN) model combining Kolmogorov-Arnold Networks (KAN) and Graph Attention Networks (GAT) to handle high-dimensional, complex features in graph-structured data. It claims to achieve superior performance on the Cora and Citeseer datasets by using KAN for feature decomposition and a multi-head attention mechanism for dynamic graph component focusing.

### Strengths
The KA-GAT method proposed in the paper, which integrates KAN into GAT, suggests the potential for broader applications of KAN within Graph Neural Networks (GNNs) in the future.

### Weaknesses
1. Lack of Novelty: Integrating Kolmogorov-Arnold Networks (KAN) into Graph Attention Networks (GAT) does not offer sufficient novelty, as it primarily combines existing techniques without substantial innovation. The core idea of applying KAN for feature transformation before GAT processing lacks a strong justification for why this specific combination would yield significant improvements over other possible architectures. The paper does not explore alternative feature transformation methods or provide a comparative analysis to demonstrate the unique advantages of KAN in this context. The approach appears to be a straightforward concatenation of two existing methods without a deep exploration of their interaction or synergistic potential.

2. Poor Presentation: The overall presentation of the paper is unacceptable. The descriptions of the methods are vague and lack the necessary detail for reproducibility. The experimental setup is not clearly defined, making it difficult to understand how the results were obtained. The figures and tables are not well-explained, and their connection to the key insights is unclear. The paper lacks a clear narrative, making it hard to follow the authors' line of reasoning and understand the significance of their findings.

3. Insufficient Experimental Support: The experimental setup is limited, with only GCN and GAT used as baselines and tests conducted solely on the Cora and Citeseer datasets. The choice of baselines is not comprehensive, and the lack of comparison with other state-of-the-art GNN models limits the impact of the study. The datasets used are relatively small and may not be representative of real-world graph data. The paper does not include any ablation studies to understand the contribution of individual components of the proposed model. The absence of statistical significance tests further weakens the validity of the reported results.

### Questions
1. Could the authors perform additional experiments on a broader selection of datasets and include more baseline models for a comprehensive performance comparison?
2. Given the strong theoretical foundation of KAN, could the authors provide theoretical evidence that integrating KAN with GAT enhances model expressiveness?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents KA-GAT, a GNN that consists of different types of layers. First, a Kolmogorov-Arnold Network transforms the initial node features and then the new features are fed to multi-head attention mechanisms along with standard neighborhood aggregation layers such as GAT and GCN layers. The KA-GAT model is evaluated in two node classification datasets. On both datasets, it outperforms the baseline methods.

### Strengths
- The proposed KA-GAT model outperforms the baselines on both Cora and Citeseer. However, KA-GAT is only compared against GCN and GAT. Thus, the baselines that the authors chose to compare their model against are relatively weak and are not considered state-of-the-art.

- From the results shown in Table 2, it seems that the KAN layer is indeed one of the most important components of the KA-GAT model, and it suggests that those layers could potentially lead to further advancements in the field of graph machine learning.

### Weaknesses
 - The proposed KA-GAT model outperforms the baselines on both Cora and Citeseer. However, KA-GAT is only compared against GCN and GAT. Thus, the baselines that the authors chose to compare their model against are relatively weak and are not considered state-of-the-art.

- From the results shown in Table 2, it seems that the KAN layer is indeed one of the most important components of the KA-GAT model, and it suggests that those layers could potentially lead to further advancements in the field of graph machine learning.

- The KA-GAT model is only evaluated on two datasets, and those datasets correspond to rather small graphs. Therefore, it is not clear whether similar conclusions could be drawn for other datasets (that correspond to different types of graphs or to larger graphs). In my view, it would strengthen a lot the paper if the proposed model was evaluated on a large number of diverse datasets. 

- A lot of details about the experiments are missing from the paper. For instance, it is unclear to me how the two datasets were split into training, validation and test sets. It is also not clear whether the hyperparameters of the models were optimized or whether some fixed values were chosen. In addition, for small datasets such as Cora and Citeseer, it is common practice to repeat each experiment multiple times. Since no standard deviations are provided, I guess that the authors report the performance from a single run.

- Some details are missing from the paper. For example, the Multi-Head Attention GNN Layer is not properly explained in the paper. It is unclear whether this layer is also a neighborhood aggregation layer which computes new node representations. If it is indeed a neighborhood aggregation layer, the authors should discuss how this layer is different from a GAT layer.

- Several architectural choices are not well-motivated. No explanations are provided regarding the KA-GAT architecture. For example, the authors do not explain why did they choose to use a single KAN layer and not more of them. In addition, the proposed model consists of both GAT layers and GCN layers. What is the reason behind that? Typically, GNNs consist of instances of a single layer, and not of many of them.

- In l.95-96, the authors claim that KANs have not been widely applied to graph-structured data. This is not true since GNN models that consist of KANs have already been proposed in [1],[2],[3] and [4]. I would suggest the authors update the related work section and discuss the aforementioned works. This would properly demonstrate how this work is positioned with relation to previous works, and also help readers better understand its novelty.

- A large part of the paper is devoted to the discussion of well-known concepts. For instance, the evaluation metrics that are presented in subsection 4.2 are well-known and do not deserve discussion. I would suggest the authors remove the unnecessary content and devote more space to the experimental evaluation of the proposed model.

### Questions
see above

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper presents KA-GAT, a novel model that integrates Kolmogorov-Arnold Networks (KANs) with Graph Attention Networks (GATs) to address challenges in graph neural networks (GNNs) with high-dimensional, complex features. The KA-GAT model utilizes KANs to decompose and reconstruct features, enhancing its ability to handle nonlinear relationships, while multi-head attention mechanisms improve its interpretability and flexibility. Through extensive experiments on benchmark datasets like Cora and Citeseer, KA-GAT demonstrates superior performance in accuracy, precision, and F1-score compared to traditional models like GCN and GAT.

### Strengths
- The paper is well-written, clear, and easy to follow, making it accessible to a wide audience.
- It pioneers the introduction of Kolmogorov–Arnold Networks (KANs) into graph neural networks, which is an interesting and novel approach.
- Some experiments are conducted to validate the performance of the proposed model.

### Weaknesses
 - The main weakness of the paper is that it feels like a straightforward application of Kolmogorov–Arnold Networks to GATs, without providing a strong justification for doing so. The paper lacks deeper insights into why this integration is particularly necessary or impactful. Specifically, the paper does not sufficiently explore the theoretical underpinnings of why KANs, which are designed to approximate arbitrary functions, would provide a unique advantage when combined with the attention mechanisms of GATs for graph-structured data. The benefit of using KANs over simpler non-linear transformations within the GAT framework is not clearly established.
- The rationale for combining multiple GNN layers, such as GCN and GAT, in a single framework is unclear. It appears as if they were stacked together without a clear logical chain, raising concerns about whether sufficient tuning was done to optimize this architecture. It may limit the generalizability of the model and questions the necessity of introducing KAN. It would be interesting to see how the model performs using simpler configurations of GCN or GAT without these combinations. The paper does not provide a clear explanation of how the information flows between the GCN and GAT layers, or why this particular sequence is optimal. The lack of ablation studies on different layer combinations makes it hard to assess the individual contributions of each component.
- Related to the above, the authors themselves acknowledge that the model is complex due to the many components used. While KAN is introduced with the motivation of reducing the computational complexity of MLPs, the resulting model’s complexity seems to contradict this goal, casting doubt on the motivation behind the paper. The paper fails to quantify the computational cost of the proposed model compared to standard GNNs, making it difficult to evaluate the practical benefits of using KANs in this context. The increased number of parameters and operations introduced by KANs may negate any potential efficiency gains.
- In the limitations section, the suggestion that future work could explore techniques like model compression or pruning feels generic and lacks depth. The authors need to critically rethink the necessity and motivation for introducing KAN into GNNs, as the current reasoning is not well substantiated. The discussion of future work should focus on specific challenges related to the proposed architecture, such as the potential for overfitting or the need for more sophisticated regularization techniques, rather than generic model optimization strategies.
- The experiments are insufficient, as they are only conducted on small, simple datasets like Cora and Citeseer. These datasets may not be representative enough to support the claim that "traditional GNNs often fall short when dealing with high-dimensional features,” as Cora’s and Citeseer’s feature dimensions are not particularly high, which weakens the argument that KAN is essential for handling high-dimensional data. The paper lacks experiments on datasets with significantly higher feature dimensions to validate the claim that KANs are necessary for handling high-dimensional inputs. The absence of such experiments makes it difficult to assess the scalability and effectiveness of the proposed approach.
- Also, the claim that "traditional GNNs often fall short when dealing with high-dimensional features" lacks sufficient evidence. More justification and empirical support are needed for this assertion. The paper does not provide a theoretical or empirical analysis of the limitations of traditional GNNs when dealing with high-dimensional data. The claim is made without proper context or supporting evidence.
- In Section 4.4, the authors simply re-express the results in table form in the text form, but do not provide enough detailed analysis or interpretation of these results. A more thorough discussion of the findings would strengthen the paper. The paper does not discuss the statistical significance of the results or provide any error analysis. The lack of detailed analysis makes it difficult to draw meaningful conclusions from the experimental results.

### Questions
Please refer to weaknesses above.

### Soundness
1

### Presentation
2

### Contribution
2

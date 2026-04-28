# TGB-Seq Benchmark: Challenging Temporal GNNs with Complex Sequential Dynamics

- Decision: Accept
- Avg Score: 6.40
- Scores: 6, 6, 6, 8, 6

## Abstract
Future link prediction is a fundamental challenge in various real-world dynamic systems. To address this, numerous temporal graph neural networks (temporal GNNs) and benchmark datasets have been developed. 
However, these datasets often feature excessive repeated edges and lack complex sequential dynamics, a key characteristic inherent in many real-world applications such as recommender systems and ``Who-To-Follow'' on social networks. This oversight has led existing methods to inadvertently downplay the importance of learning sequential dynamics, focusing primarily on predicting repeated edges.

In this study, we demonstrate that existing methods, such as GraphMixer and DyGFormer, are inherently incapable of learning simple sequential dynamics, such as ``a user who has followed OpenAI and Anthropic is more likely to follow AI at Meta next.'' Motivated by this issue, we introduce the \underline{T}emporal \underline{G}raph \underline{B}enchmark with \underline{Seq}uential Dynamics (TGB-Seq), a new benchmark carefully curated to minimize repeated edges, challenging models to learn sequential dynamics and generalize to unseen edges. TGB-Seq comprises large real-world datasets spanning diverse domains, including e-commerce interactions, movie ratings, business reviews, social networks, citation networks and web link networks. Benchmarking experiments reveal that current methods usually suffer significant performance degradation and incur substantial training costs on TGB-Seq, posing new challenges and opportunities for future research. The datasets and benchmarking code are available at https://anonymous.4open.science/r/TGB-Seq-3F23.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors present a new, challenging benchmark for temporal graph modeling, specifically addressing scenarios with fewer or no repeated edges. They provide an analysis of the limitations of the existing methods and conduct experiments using both current temporal graph modeling methods and sequential recommendation methods.

### Strengths
1. The motivation behind this work is compelling, as it is meaningful and reasonable to consider the repeat behavior in the temporal graph.

2. The proposed benchmark spans multiple domains with different data sizes and includes both bipartite and non-bipartite graphs, offering diverse resources for the research community to investigate issues around unseen edges.

3. The paper is well-structured and easy to follow.

### Weaknesses
1. While the paper focuses on unseen edges in temporal graphs, the selected baselines are primarily general-purpose models within the graph or recommendation domains. There are specific works that address similar challenges. For example:

- In the temporal graph domain, there are models with the ability to handle the inductive nodes:

   - TREND: TempoRal Event and Node Dynamics for Graph Representation Learning. WWW’22.

    - On the Feasibility of Simple Transformer for Dynamic Graph Modeling. WWW’24

- In the recommendation domain, Models tailored to repeat and exploration behaviors, including:

    - RepeatNet: A Repeat Aware Neural Recommendation Machine for Session-Based Recommendation. AAAI’19
    - Repetition and Exploration in Sequential Recommendation. SIGIR’23
    - Right Tool, Right Job: Recommendation for Repeat and Exploration Consumption in Food Delivery. RecSys’24
    - To Copy, or not to Copy; That is a Critical Issue of the Output Softmax Layer in Neural Sequential Recommenders. WSDM’24

    - (the explore-only model) "Masked and Swapped Sequence Modeling for Next Novel Basket Recommendation in Grocery Shopping”, RecSys’23

Thus the review would like to see what the performance would be like using the specifically designed models on the new benchmark.

2. The toy example offers a controlled setting to assess sequential pattern recognition with the existing methods. However, it may oversimplify the problem, limiting its ability to reflect real-world dynamics. I think the authors should analyze the performance limitations in realistic settings to provide a more comprehensive understanding of the critical limitations of the existing methods, offering insights about the possible improvement areas.

3. The analysis in Tables 3 and 4 provides limited insights, focusing primarily on overall performance decreases with the new benchmark. Deeper insights should be included to inspire future model design for this benchmark. For example, evaluating models separately on seen and unseen edges to highlight how well they handle these distinct cases.

4. The authors claim that they include a state-of-the-art recommendation model named SGNN-HN. However, it was published in 2020, which is not the state-of-the-art recommendation model.

### Questions
The authors only use one metric MRR to measure the performance, what about other ranking metrics (such as NDCG, Recall)? Do we need to design other metrics to measure the performance?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces TGB-Seq, a new benchmark designed to challenge temporal GNNs with complex sequential dynamics. Existing datasets often have excessive repeated edges, which fail to capture the sequential patterns present in many real-world applications like recommender systems and social networks. TGB-Seq minimizes repeated edges and includes diverse domains such as e-commerce, movie ratings, and social networks. The study reveals that current temporal GNN methods struggle with these datasets, highlighting the need for models that can better generalize to unseen edges. The paper contributes by providing new datasets that emphasize sequential dynamics and exposing the limitations of existing GNN approaches.

### Strengths
1. This article highlights the issue of excessive repeated edges in existing dynamic graph datasets. The experiments presented in the text are very complete and convincing, and the presentation in Figure 2 is impressive. The motivation behind the construction of TGB-Seq is very sufficient, the problems it addresses are very clear, and it has significant practical implications.
2. The structure of this article is clear, and the expression is explicit. Overall, it is easy to follow.

### Weaknesses
 1. Section 3.2 is far from satisfactory. The conclusion of Section 3.2 is very interesting and quite important, but the entire section lacks formal expression, making the analysis of the limitations of existing dynamic graph models in this part very perfunctory. The discussion lacks precise definitions of the memory and aggregation mechanisms being critiqued, making it difficult to understand the specific shortcomings of existing models. For example, the analysis could benefit from a formal definition of how different models store and update node embeddings over time, and how these updates fail to capture the sequential dynamics present in the TGB-Seq datasets.
2. The assumptions and premises in Section 3.2 are not clear. There is a simple description of premises starting from line 212 in the text, but it is very vague. Are the node features of the three types of nodes u, v, and i all blank? If so, this assumption lacks rationality. The subsequent discussions on the model's memory and aggregation parts are all based on this. If all nodes have the same features (all nodes have no features), it will inevitably lead to the indistinguishability of many nodes, which is similar to the discussion of graph isomorphism problems. In such an extreme case, the limitations of dynamic graph models are difficult to be widely recognized. The authors should clarify whether this lack of features is intended to isolate the temporal dynamics, and if so, why this is a reasonable simplification given that real-world graphs often contain rich node features. The analysis should also consider how the absence of node features impacts the conclusions about the limitations of existing models.
3. Continuing from the previous point, the authors should discuss why SGNN-HN can achieve such good results under the toy example and what problems it overcomes. Of course, these contents should be formally expressed in the form of expressions. The existing theoretical discussion in the text is difficult to understand. The authors need to provide a more detailed explanation of the mechanisms within SGNN-HN that allow it to succeed where other models fail. This explanation should include a formal description of how SGNN-HN processes temporal information and how its architecture differs from the models that struggle with the toy example. A clear mathematical formulation of SGNN-HN's approach would greatly enhance the analysis.

### Questions
Please see my comments for details

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
TGB-Seq presents a novel benchmark for the temporal link prediction task by emphasizing that the key characteristic of temporal link prediction is that the model should learn how to rank the most likely destination node for a given source node at the queried time, which aligns well with practical, real-world settings, such as recommender systems.

### Strengths
1. Incorporates diverse datasets from different domains and different sizes (number of nodes/edges). 
2. Comprehensive report for experimental settings (hyperparameters search range, computational resources, etc.)  and assessment of SOTA Temporal GNNs baselines.
3. Clear presentation, and the paper is easy to read.

### Weaknesses
1. For validation and test set, TGB-Seq only retains nodes that appear in the training set. I do not think this setting is practical for real-world temporal graphs, as they continuously evolve, and this setting is not comprehensive enough to assess the model’s ability to reason on new information that emerges in future timestamps. Specifically, the exclusion of nodes unseen during training limits the evaluation of a model's ability to generalize to novel entities, a crucial aspect in many real-world applications where new nodes constantly appear. This design choice may lead to an overestimation of model performance in practical scenarios.

2. Previous work [1] (Poursafaei et al., 2022) also devised 2 other negative sampling strategies (NSS): (1) random NSS, which samples any possible node pairs, and (2) inductive NSS that samples edges that are unseen during the training stage. Therefore, previous works' inductive NSS also do not rely on historical edges, and random NSS samples are also from all possible nodes. How does TGB-Seq’s NSS differ from [1]’s inductive or random NSS? It is unclear how the proposed negative sampling strategy differs from existing methods, especially in terms of the specific constraints applied during the sampling process. A more detailed explanation of the differences is needed to justify the novelty of the approach.

3. TGB-Seq claims that the proposed evaluations of SOTA models show that achieving both efficiency and effectiveness in temporal GNNs remains an open problem, highlighting the distinctive feature of TGB-Seq. However, TGB [2] also presents large temporal graphs that could challenge any model’s efficiency, and some of their datasets have high surprise scores, which also challenge the performance of SOTA models that are listed in TGB-Seq. Compared to TGB [2], how distinctive is TGB-Seq’s capabilities in challenging Temporal GNNs? The paper needs to provide a more detailed analysis of how the proposed benchmark differs from existing benchmarks, especially in terms of the specific challenges it poses to temporal GNNs. The current explanation is not sufficient to justify the need for a new benchmark.

### Questions
Please refer to Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
In this work, the authors pointed out that existing methods are lacking in the learning of sequential dynamics while focusing primarily on predicting repeated edges. To this end, the authors first demonstrated that methods such as GraphMixer and DyGformer are unable to learn sequential dynamics in a toy dataset and then introduce a new benchmark, TGB-Seq, that contains a minimal amount of repeated edges. TGB-Seq contains large real-world datasets that spans diverse domains as well as both bipartite and non-bipartite networks.

### Strengths
This paper focuses on examining how well current models can learn sequential dynamics (predict unseen edges). I believe the limitations of existing methods pointed out in this work is quite interesting. Here are the strengths of the paper:

- the idea of a benchmark containing datasets with very low amounts of repeated edges are interesting while opening up new research directions that design novel methods for such datasets. This is significant for the temporal graph learning community. 

- The paper is well-written and clearly presented. 

- The new datasets spans a diverse range of domains and contains both bipartite and non-bipartite networks. The authors also provided code and dataset access.

### Weaknesses
Here are some weakness of the paper:

- **new but familiar idea**. The idea of measuring unseen edges and their effect in model performance is not entirely new. In the TGB work, the authors also mentioned the surprise index which measures the amount of test edges unseen during training (similar to the unseen edges idea in the paper though different).  The authors should further clarify any definition difference between the "unseen" edges as shown In Figure 2 versus the novel edges $E_{test} \ E_{train}$ as mentioned in the surprise index. Specifically, it's unclear if the 'unseen' edges are simply edges that appear for the first time in the entire dataset, or if they are defined relative to the training set, similar to the surprise index. A more precise definition of 'unseen' edges is needed, along with a clear explanation of how it differs from the surprise index and why this distinction is important for evaluating temporal graph learning models.

- **lack of node, edge features for the datasets**. The authors mentioned that this work excludes datasets with node and edge features. Were there datasets that you considered that has node or edge features? Is it possible to include some features for the datasets in TGB-seq benchmark? Because node / edge features might be crucial for the model to learn sequential dynamics. For example, one user might enjoy coffee and this user will choose to purchase a new type of coffee beans (a categorical feature of the item node)) at a future time. With node features on the items, the model can learn this dynamics easier while it might be difficult to learn if no feature is provided. The absence of such features limits the ability of the benchmark to evaluate models in more realistic scenarios where such information is often available and can be crucial for performance. Furthermore, the lack of node and edge features makes it difficult to evaluate how well models can integrate both structural and feature-based information for predicting future interactions.


- **OOT errors are not intuitive**. In terms of running time, memory based models such as TGN and DyRep are usually more efficient than DyGFormer and CAWN (such as compared in the TGB work). It is not very intuitive to me why these models can not finish a single epoch in 24 hours as they are able to scale to the largest datasets on TGB. More clarification / explanation from the authors are appreciated. The reported out-of-time (OOT) errors for memory-based models are surprising given their typical efficiency. It is necessary to understand the specific implementation details that lead to such high training times. The authors should provide a detailed breakdown of the computational bottlenecks in their implementation of these models, particularly focusing on memory access patterns and data structures used for storing node states and messages. This would help in understanding why these models are not scaling as expected and how the implementation differs from other efficient implementations.

### Questions
See weakness for the questions as well.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper begins with an experimental investigation exploring the comparison of recent temporal GNN methods on the recommendation datasets, where the results are surprisingly lower than the classical methods in the recommendation. The paper then investigates the reason for the datasets and proposes a more comprehensive benchmark to compare the existing methods more effectively. This paper presents an important perspective, often overlooked by many in the field, to reevaluate whether the current approach to future link prediction tasks is reasonable. I believe this work is valuable for encouraging a rethinking within the field and can inspire future research efforts.

### Strengths
1. This paper introduces a significant perspective that many in the field have often overlooked. It prompts a reevaluation of whether the current methods used for future link prediction tasks are truly appropriate.
2. This paper conducts insightful data analysis on existing datasets to examine the current evaluation standards.

### Weaknesses
1. In the illustration of Figure 3, the node features are omitted. However, this omission is not appropriate given that incorporating node features is one of the key advantages of Graph Neural Networks (GNNs) compared to ID-based recommendation models. The illustration, without considering node features, fails to adequately demonstrate the full capability of GNN models, particularly in highlighting their ability to leverage rich feature information.
2. Recently, some efforts not mentioned in this submission have been made to benchmark and evaluate existing work in continuous time domains, such as in [1]. Although this paper has a different focus, the range of GNN methods that can be evaluated is more extensive.

### Questions
See weakness for more details.

### Soundness
3

### Presentation
3

### Contribution
3

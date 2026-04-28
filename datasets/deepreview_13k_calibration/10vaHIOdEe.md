# One Model for One Graph: A New Perspective for Pretraining with Cross-domain Graphs

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
Graph Neural Networks (GNNs) have emerged as a powerful tool to capture intricate network patterns, achieving successes across different domains. However, existing GNNs require careful domain-specific architecture designs and training from scratch on each dataset, leading to an expertise-intensive process with difficulty in generalizing across graphs from different domains. Therefore, it can be hard for practitioners to infer which GNN model can generalize well to graphs from their domains. To address this challenge, we propose a novel cross-domain pretraining framework, "one model for one graph," which overcomes the limitations of previous approaches that failed to use a single GNN to capture diverse graph patterns across domains with significant gaps. Specifically, we pretrain a bank of expert models, with each one corresponding to a specific dataset. When inferring to a new graph, gating functions choose a subset of experts to effectively integrate prior model knowledge while avoiding negative transfer. Extensive experiments consistently demonstrate the superiority of our proposed method on both link prediction and node classification tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes the OMOG (One Model for One Graph) framework, which advances graph learning by pre-training a unique model for each graph within a model bank. By creating a bank of expert models, each pre-trained for a specific dataset, OMOG selects relevant experts for inference using gate modules tailored to the target graph’s domain. This approach mitigates negative transfer issues common in multi-domain pre-training, and it performs effectively in zero-shot and few-shot tasks like link prediction and node classification, showing its potential for cross-domain graph tasks.

### Strengths
1. The paper focuses on and attempts to address a crucial yet highly challenging problem in the field of graph analysis—constructing a Graph Foundation Model (GFM).
2. On commonly used graph datasets, the model OMOG presented in the paper achieves relatively good performance in both zero-shot and few-shot settings.

### Weaknesses
1. The paper does not clearly explain the differences from other MOE-based methods, such as GraphAlign and AnyGraph. The approach seems very similar to these methods, leaving it unclear what specific advantages OMOG has over them and why it achieves improved performance.
2. A core idea of OMOG is that each pre-training dataset requires a dedicated expert. This approach poses challenges for scalability: as the volume of pre-training data increases, the model grows linearly with the data, which is detrimental to pre-training efficiency.
3. Why is the expert model specifically a Transformer? How would the performance change if other models, such as GNN, Graph Transformer, or MLP, were used instead? Additionally, prior to entering the experts, the features and structure are fused through SGC. Why couldn’t this fusion step be incorporated within the experts themselves? After all, different graphs may require varying levels of neighbor aggregation.
4. The core part for achieving zero-shot in this paper relies on calculating the similarity between label embeddings and prediction embeddings to obtain the final label prediction. In fact, most models that work under few-shot settings can be adapted to zero-shot using a similar approach. Consequently, Table 1 lacks several relevant baselines, such as GraphAlign, GCOPE, and GraphMAE.
5. Do all experts contribute to downstream performance improvements? In Figure 6, while the number of experts is adjusted, the full set of pre-training data is still used to train the gating mechanism. Could you vary the number of pre-training datasets to examine how this affects downstream performance?
6. Although this paper discusses GFM, which should be applicable to various downstream tasks, there is still an absence of experiments on graph-level tasks, such as graph classification or graph regression.
7. Some parts of the paper lack clarity. For example, in Section 4.5, the phrase ‘select 10 samples from each dataset’ is ambiguous. Does this refer to selecting 10 nodes, subgraphs, or something else?

### Questions
See weaknesses.

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a novel cross-domain pretraining framework called "one model for one graph," by pretraining a bank of expert models and using a gating function to choose a subset of experts to effectively integrate prior model knowledge.

### Strengths
1. The presentation of this paper is good and most parts of the paper are clear.
2. This paper proposes a novel cross-domain pretraining framework.
3. The experimental results demonstrate the effectiveness of the proposed method.

### Weaknesses
1. The intuition of the generator and filter in Pretraining the gate module is not clear.
2. The authors lack the discussion about the difference between the proposed method and the mixture-of-experts based methods. 
3. I am concerned about the negative transfer issue in the proposed method. Since the knowledge in the proposed methods is extracted from graphs in different domains (and most of them are irrelevant), it inevitably increases the probability of facing the negative transfer issue. How does the proposed method address this issue? The top-k strategy seems to only filter out the low confidant knowledge, while it can not directly alleviate the negative transfer issue as the irrelevant knowledge might be included in the top k expert models. 
4. I try to reproduce the experimental results, but there is no instruction and datasets available in the provide GitHub link.

### Questions
1. What is the time complexity or running time of the proposed method given that the proposed method needs to pretrained the model on several graphs from different domains?
2. In line 207, the authors mention that the node-level feature are randomly maked, resulting in two maked views. Are these two masked views mutually exclusive? For instance, given a 10-d feature matrix, the first masked view is generated by masked 5 features and the second view is generated by masking the rest 5 features?
3. How do you ensure that the generator only generates a matrix to mask the domain irrelevant features such that the filter features are domain-related?
4. The authors mention that one key issue is negative transfer. Since the knowledge in the proposed methods is extracted from graphs in different domains, it inevitably increases the probability of facing the negative transfer issue. How does the proposed method address this issue? The top-k strategy seems to only filter out the low confidant knowledge, while it can not directly alleviate the negative transfer issue as the irrelevant knowledge might be included in the top k expert models. 
5. I try to reproduce the experimental results, but there is no instruction and datasets available in the provide GitHub link. The readme seems to be empty. Could you provide the datasets and the instruction to reproduce the results?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes OMOG, an innovative cross-domain graph learning framework designed to enhance the adaptability and performance of Graph Neural Networks (GNNs) across various domains. By training a distinct expert model for each pre-training graph and employing adaptive gating functions during inference, OMOG dynamically selects relevant experts for unseen graphs.

### Strengths
1.	By pretraining individual models for each graph dataset, OMOG effectively addresses the feature and structural heterogeneity found across diverse graphs.
2.	OMOG’s model bank allows the easy addition of new expert models without retraining the entire system, providing flexibility to expand the pretraining bank with new data and adapt quickly to novel domains.

### Weaknesses
1.	The primary motivation for adopting the “one model for one graph” approach is to alleviate the negative transfer limitations observed in the “one model for all graphs” method. It would be beneficial to provide comparisons and discussions on how this method differs from prior approaches that aim to reduce negative transfer through better pretraining data selection as [1]. Specifically, a more detailed analysis is needed on how the proposed method avoids the potential pitfalls of data selection, such as excluding potentially useful knowledge present in other datasets. The current discussion does not fully address how the dynamic model selection in OMOG compares to static data selection methods in terms of knowledge retention and generalization capabilities.
2.	It is recommended to identify which models, pretrained on specific graphs, are selected as the best match for various test graphs, with explanations for these selections. Additionally, I’m curious about whether pretraining data from different domains can contribute effectively or if only similar/same-domain data is more beneficial would strengthen the analysis. A case study is recommended to evaluate whether the proposed gating strategy actually mitigate issues stemming from conflicts across pre-training data from diverse domains. The analysis should include a discussion on the potential for negative transfer even with the gating mechanism, particularly if the selected models are not perfectly aligned with the target graph's characteristics. It would be beneficial to explore the sensitivity of the gating mechanism to noisy or irrelevant pre-trained models.
3.	It would be valuable to explore whether this pipeline could be adapted to other self-supervised learning approaches for pretraining graph-specific experts, and additional ablation studies are expected. The current study focuses on a single self-supervised method, and it is unclear how the framework would perform with other pretraining strategies. An investigation into the compatibility and performance of OMOG with different self-supervised techniques is needed to demonstrate its robustness and general applicability.
4.	OMOG’s design requires a separate model for each dataset and can result in a large model bank when many datasets are involved. Will it lead to high storage costs and maintenance overhead, especially in resource-constrained environments? A complexity analysis would also be helpful to understand OMOG’s computational feasibility at scale. The analysis should include a discussion on the memory footprint of the model bank and the computational cost of the gating mechanism during inference, especially when dealing with a large number of expert models. A detailed analysis of the scalability of the approach is needed to assess its practical applicability in real-world scenarios.

### Questions
see Weaknesses

### Soundness
2

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
3

### Summary
This paper proposes OMOG to pretrain one model for one graph in cross-domain transformation. OMOG uses SGC as message aggregation before experts learning, and uses the contrastive method for expert and gate training. In the inference stage, OMOG activates the top-k of experts to infer node labels. The experimental results proved the effectiveness of the method.

### Strengths
1. The approach of building an expert model for each graph intuitively addresses the issue of negative transfer in graph pre-training.
2. The problem addressed in this paper is a crucial part of foundational research on graph models and is currently a topic of significant interest among researchers.
3. The experiments involve graph data from multiple domains and include comparisons with recent, noteworthy methods in graph transfer learning.

### Weaknesses
1. According to the method statement, graphs from different domains are required to have input spaces of the same size, which seems difficult to satisfy with real-world data.
2. The construction of multiple experts for input graphs appears to be relatively naive, as it merely involves repeating several encoders and using similarity ranking with a central vector for averaging activation. This approach lacks a sophisticated mechanism for ensuring expert specialization, potentially leading to redundancy and limited diversity in the learned representations.

### Questions
1. What is the means of t in Equation (3)? How do you ensure that each expert has different parameters? Based on Equation (3), it seems that each expert has the same input and parameters, leading to identical outputs. What, then, is the purpose of having multiple experts?
2. In line 241, the mask matrix seems to be replaced by an MLP. Why are the node embeddings transformed by the MLP considered to be negative embeddings?
3. In Equation (4), is f_center ​the average output of a single graph across multiple experts, or the average output of multiple source graphs through their respective experts? How does this function as an anchor point for training the gate?
4. What are the parameters of the Gate in Equation (5)? Why is the Gate used before the Expert?
5. According to the inference process, an unseen graph activates the top k experts based on the highest correlation between each expert's output and the output average. How do you ensure that the pre-trained graph domain encompasses a sufficiently heterogeneous feature space to handle all potentially unseen graph domains?
6. How is the total number of experts determined, especially when the number of graph domains during pre-training and testing is uncertain?

### Soundness
2

### Presentation
2

### Contribution
2

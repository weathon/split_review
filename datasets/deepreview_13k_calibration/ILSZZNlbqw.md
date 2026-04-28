# Cross-Domain Graph Data Scaling: A Showcase with Diffusion Models

- Decision: Reject
- Avg Score: 4.67
- Scores: 3, 6, 5

## Abstract
Models for natural language and images benefit from data scaling behavior: the more data fed into the model, the better they perform.
This 'better with more' phenomenon enables the effectiveness of large-scale pre-training on vast amounts of data.
However, current graph pre-training methods struggle to scale up data due to heterogeneity 
across graphs. 
To achieve effective data scaling, we aim to develop a general model that is able to capture diverse data patterns of graphs and can be utilized to adaptively help the downstream tasks.
To this end, we propose \method, a universal graph structure augmentor built on a diffusion model.
We first pre-train a discrete diffusion model on thousands of graphs across domains to learn the graph structural patterns.
In the downstream phase, we provide adaptive enhancement by conducting graph structure augmentation with the help of the pre-trained diffusion model via guided generation.
By leveraging the pre-trained diffusion model for structure augmentation, we consistently achieve performance improvements across various downstream tasks in a plug-and-play manner.
To the best of our knowledge, this study represents the first demonstration of a data-scaling graph structure augmentor on graphs across domains.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a graph structure augmentation framework built on discrete diffusion models. They first pre-train a structure-only discrete diffusion model on graphs from multiple domains. During downstream adaptation, the model generates synthetic graph through guided generation, using a task-specific head to align these generated structures with the target task. This framework aims to enhance performance across various tasks, including node classification, link prediction and graph prediction. The experiment also shows that the downstream performance increases when the amount of pre-training data increases.

### Strengths
- The paper demonstrates an interesting cross-domain transfer ability, where the pre-trained model can be adapted to various downstream tasks at different levels (node, edge, and graph).
- The presentation is clear, with well-explained methods and experimental results, making it easy to follow the proposed approach and findings.

### Weaknesses
 - I have some concerns about the comparison of UniAug with baseline pre-training methods. The authors mention that they used the same pre-training dataset for UniAug and baselines. They also calculated node degrees as inputs and replaced node features with node degrees for downstream testing. However, these baseline models were not originally designed to be trained and tested in this way. As shown in Table 13, when evaluated in their original semi-supervised or self-supervised settings, these baselines achieve results similar to UniAug. This is different from the larger improvement suggested in Table 2. A more accurate comparison would keep the baselines in their original configurations, and it would also help to see similar comparisons for link prediction and node classification tasks.
- Additionally, a discussion of pre-training time for UniAug compared to the baselines would improve the analysis. This can offer a better understanding of UniAug’s efficiency compared to other methods.
- A more detailed description of the sizes of Small, Full, and Extra pre-training datasets should be provided. From the description, the Extra dataset includes 1,000 more subgraphs from the GitHub Star dataset than the Full dataset. This addition results in large improvements for link prediction tasks but shows little effect on graph classification tasks. Thus I am curious whether the improvements come from the increased amount of data or from the diversity added by the new subgraphs. A more detailed breakdown of the dataset sizes and an analysis of data diversity versus quantity would help clarify the reasons behind these improvements.
- The model shows strong performance on heterophilic node classification, but the baselines used for comparison are primarily designed for homophilic data. It would be more informative to include results on homophilic datasets like Cora and PubMed to provide a balanced comparison. Furthermore, to fairly evaluate performance in heterophilic settings, it is necessary to include baselines specifically designed for heterophily, such as PolyGCN and GREET.
- While the paper mentions that the model requires less training time per epoch, it also states that the total number of epochs is significantly larger. This makes it difficult to assess the overall training time efficiency. A clear comparison of total pre-training times would be beneficial.
- My primary concern is the positioning and practical utility of the proposed approach. While it aims to provide a general graph augmentor that can enhance various graph structures, the results suggest that it does not consistently outperform state-of-the-art baselines in specific domains. The pre-trained augmentor requires further fine-tuning for each individual task. Therefore, it is unclear under what specific circumstances this approach is particularly necessary or advantageous.
- It would be highly beneficial to demonstrate whether the proposed augmentor can enhance the performance of state-of-the-art methods when applied to them. Showing a measurable performance improvement when combined with existing SOTA models for each task would provide stronger evidence of the practical value of the approach.

### Questions
Please see the weakness part.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper explores a meaningful issue: How to effectively leverage the increasing scale of data across domains for graph learning? To achieve effective data scaling, this paper proposes a universal graph augmentation framework, UniAug. This framework pre-trains a discrete diffusion model on massive graphs across domains to learn the structural patterns, and conducts structure augmentation with the help of the pre-trained diffusion model. Experiments shows that this framework can leverage the data scaling laws and achieve performance improvements across various downstream tasks.

### Strengths
+ The research topic of this paper—How to effectively leverage the increasing scale of data across domains for graph learning, is highly significant and meaningful, representing a critical issue that urgently needs to be addressed in the current field.
+ This paper collects thousands of graphs from varied domains with diverse patterns to explore the potential of data scaling for graph learning.
+ This paper provides a solution based on the diffusion model from a structural augmentation perspective. This augmentation paradigm strategically circumvents feature heterogeneity and fully utilizes downstream inductive biases in a plug-and-play manner.

### Weaknesses
 + The authors should clearly illustrate the scale and domain variety of the pre-training data collection in the paper and make it public for the community to conduct further research on the issue. Meanwhile, providing code examples is also essential.
+ The authors should consider whether excessively introducing additional datasets for pre-training is appropriate and whether it might produce negative effects.
+ Related work about data scaling on graphs should be include in the paper [1, 2, 3].
1. [1] Liu J, Mao H, Chen Z, et al. Neural scaling laws on graphs[J]. arXiv preprint arXiv:2402.02054, 2024.
2. [2] Ma Q, Mao H, Liu J, et al. Do Neural Scaling Laws Exist on Graph Self-Supervised Learning?[J]. arXiv preprint arXiv:2408.11243, 2024.
3. [3] Wang Z, Li Y, Ding B, et al. Exploring Neural Scaling Law and Data Pruning Methods For Node Classification on Large-scale Graphs[C]//Proceedings of the ACM on Web Conference 2024. 2024: 780-791.

### Questions
See Weaknesses.

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
4

### Summary
The paper proposes a model called UniAug, based on a graph diffusion model. The approach consists of two steps: first, pretraining on diverse graphs from different domains, and second, using the model to generate synthetic structures for downstream tasks. Experimental results on approximately 30 cross-domain graphs demonstrate the empirical effectiveness of the method.

### Strengths
1. The paper is well-written and easy to follow, presenting a simple yet effective approach that uses diffusion models to augment structural data for cross-domain graphs.

2. Addressing the challenge of designing models for cross-graph learning is highly valuable and relevant.

3. The experiments are comprehensive, covering approximately 30 graphs across more than five domains.

### Weaknesses
1. The authors claim to propose a graph foundation model for cross-domain graphs. However, the method appears to be more of a universal graph structural augmentor that utilizes graph diffusion models for generating additional structures, rather than a foundation model capable of inference across various graph types, like [1,2,3]. Additionally, although the authors demonstrate that pretrained diffusion models can generate synthetic structures to enhance performance on various downstream tasks, the concept of using graph diffusion models to create structures is not entirely new [4,5], which may limit the novelty of the approach.

2. The experimental results are not entirely convincing. The authors use node degrees as features for self-supervised baselines, which can significantly impair model performance when replacing original node features with node degrees, whereas using original node features for the proposed method. Although the authors elaborate on this issue in Appendix D, the experimental descriptions still confuse me, and I cannot find strong evidence that the proposed UniAug outperforms existing SSL methods under comparable settings (i.e., using the same feature setup).

3. The applicability of the method may be limited in certain scenarios. When applying it to downstream tasks, such as node and graph classification, the authors use node labels to guide the generation of graph structures. However, the method may struggle with graphs that lack sufficient label information. It would be helpful to understand whether the approach can be effectively applied to downstream graphs with limited or no label data.

### Questions
1. The authors present experimental results with varying pretraining scales in Figure 3. Although there is a general performance improvement between the SMALL, FULL, and EXTRA scales, there are instances where the model pretrained on smaller graph datasets outperforms those pretrained on larger datasets, such as on the Enzymes and Erdos datasets. Could the authors provide a detailed explanation for these observations?

2. Can the proposed method be applied to more practical scenarios, such as few-shot or zero-shot learning?

3. The proposed method leverages a diffusion model to generate additional structural information. While the model demonstrates empirically desirable performance, I am curious whether there is a theoretical understanding that supports its efficacy.

### Soundness
2

### Presentation
3

### Contribution
2

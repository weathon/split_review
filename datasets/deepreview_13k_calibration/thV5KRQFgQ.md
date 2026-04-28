# Rationalizing and Augmenting Dynamic Graph Neural Networks

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 5, 6

## Abstract
Graph data augmentation (GDA) has shown significant promise in enhancing the performance, generalization, and robustness of graph neural networks (GNNs). However, contemporary methodologies are often limited to static graphs, whose applicability on dynamic graphs—more prevalent in real-world applications—remains unexamined. In this paper, we empirically highlight the challenges faced by static GDA methods when applied to dynamic graphs, particularly their inability to maintain temporal consistency. In light of this limitation, we propose a dedicated augmentation framework for dynamic graphs, termed $\texttt{DyAug}$, which adaptively augments the evolving graph structure with temporal consistency awareness. Specifically, we introduce the paradigm of graph rationalization for dynamic GNNs, progressively distinguishing between causal subgraphs (\textit{rationale}) and the non-causal complement (\textit{environment}) across snapshots. We develop three types of environment replacement, including, spatial, temporal, and spatial-temporal, to facilitate data augmentation in the latent representation space, thereby improving the performance, generalization, and robustness of dynamic GNNs. Extensive experiments on six benchmarks and three GNN backbones demonstrate that $\texttt{DyAug}$ can \textbf{(I)} improve the performance of dynamic GNNs by $0.89\\%\sim3.13\\%\uparrow$; \textbf{(II)} effectively counter targeted and non-targeted adversarial attacks with $6.2\\%\sim12.2\\%\\uparrow$ performance boost; \textbf{(III)} make stable predictions under temporal distribution shifts.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors identify limitations in applying existing graph data augmentation (GDA) techniques to dynamic graphs. Through a detailed investigation, they reveal that these methods often degrade performance by disrupting temporal consistency within the graph structures. To address this challenge, the authors introduce DyAug, a graph data augmentation approach specifically designed for dynamic graphs. DyAug achieves this by partitioning the input graph into a "rational" component, which preserves essential temporal consistency, and an "environmental" component, which can be modified to enrich the training data. Building on this partitioning, they propose three replacement strategies to selectively augment the dynamic graph without compromising consistency. Experimental results demonstrate that DyAug significantly improves both the performance and robustness of dynamic GNNs.

### Strengths
The paper has the following strengths:

- The authors focus on emerging dynamic graphs, a format increasingly common in real-world applications, making the approach highly relevant.

- The proposed approach is well-founded and effectively enhances the resulting model's performance and robustness.

- The authors thoroughly compare various existing GDA methods, demonstrating significant improvements in outcomes.

### Weaknesses
The paper has the following weaknesses:

- The proposed scheme's effectiveness is not evaluated on continuous-time dynamic graphs (CTDGs), which are also crucial in dynamic graph learning.

- The scalability of the approach is not thoroughly assessed, leaving uncertainty about its performance on larger graphs.

- The dynamic GNN models used in the evaluation are relatively outdated, potentially limiting the generalizability of the results.

- The adversarial attacks used for testing the approach are not as advanced as state-of-the-art methods, which may affect the robustness evaluation.

### Questions
Here are some questions that may help strengthen the overall merit of the paper:

1. Have you considered evaluating the proposed scheme on continuous-time dynamic graphs (CTDGs)? How do you anticipate the approach would perform on CTDGs compared to discrete-time settings?

2. Could you provide insights into the scalability of your approach? Have you tested it on larger graphs, and if so, how does performance scale with increasing graph size? Additionally, what are the associated overheads?

3. Could you share more evaluation results of the approach on recent models to provide a broader validation of its effectiveness? For instance, models such as TGAT [1], ROLAND [2], or DyGFormer [3]?

4. Given that the adversarial attacks used in the evaluation are not the most advanced, do you plan to test your approach against state-of-the-art adversarial attacks, such as [4]? How do you anticipate your method would perform in these more challenging scenarios?

[1] Xu, Da, et al. "Inductive representation learning on temporal graphs." arXiv preprint arXiv:2002.07962 (2020).

[2] You, Jiaxuan, Tianyu Du, and Jure Leskovec. "ROLAND: graph learning framework for dynamic graphs." Proceedings of the 28th ACM SIGKDD conference on knowledge discovery and data mining. 2022.

[3] Yu, Le, et al. "Towards better dynamic graph learning: New architecture and unified library." Advances in Neural Information Processing Systems 36 (2023): 67686-67700.

[4] Sharma, Kartik, et al. "Temporal dynamics-aware adversarial attacks on discrete-time dynamic graph models." Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining. 2023.

### Soundness
3

### Presentation
2

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
This paper introduces DyAug, a novel framework designed to enhance dynamic graph neural networks (DyGNNs) through graph rationalization and data augmentation, addressing the limitations of static graph augmentation methods when applied to dynamic graphs. DyAug utilizes temporal consistency-aware augmentation strategies to separate causal and non-causal graph components across time, leading to improved performance, generalization, and robustness against adversarial attacks and temporal distribution shifts. Extensive experiments demonstrate that DyAug consistently outperforms state-of-the-art methods.

### Strengths
1. The proposed DyAug framework extends GDA to dynamic graphs, a less explored area. It offers an innovative approach by focusing on maintaining temporal consistency, which is crucial for dynamic graphs.
2. DyAug effectively maintains temporal consistency, ensuring that augmentations do not disrupt the natural evolution of dynamic graphs.
3. DyAug introduces the concept of graph rationalization for dynamic GNNs, separating causal subgraphs from non-causal parts. This enables the model to learn more meaningful temporal representations.

### Weaknesses
1. DyAug introduces additional computational complexity from causal mask estimation, contrastive loss, and consistency loss, which could pose scalability issues for large graphs. The paper does not provide a detailed analysis of the computational overhead for each component, making it difficult to assess the practical limitations of the approach on very large dynamic graphs. Furthermore, the memory footprint of the method is not discussed, which is crucial for real-world applications where memory resources are limited.
2. While the paper includes comparisons with several GDA methods, some notable methods like DIR [1] and GREA [2] were excluded due to compatibility issues. This omission limits the scope of the empirical evaluation and raises questions about the generalizability of the proposed method compared to other state-of-the-art graph rationalization techniques. The justification for excluding these methods is not thoroughly explained, making it difficult to understand the practical constraints that led to their exclusion.
3. DyAug's augmentation techniques (spatial, temporal, spatial-temporal replacements) rely on heuristic selection strategies, which might not generalize well across all types of dynamic graphs. The paper lacks a clear explanation of the rationale behind these selection strategies, and it is unclear how the method would perform on dynamic graphs with different structural properties or temporal dynamics. The lack of a systematic approach to augmentation could lead to suboptimal performance in diverse scenarios.
4. Although an ablation study is provided, it could be more exhaustive, especially in terms of testing the impact of different hyperparameters and rationale generation methods on diverse datasets. The paper does not explore the sensitivity of the method to the choice of hyperparameters, which could significantly affect the performance of the model. Additionally, the rationale generation process is not thoroughly analyzed, and it is unclear how different rationale generation techniques would impact the overall performance.

### Questions
1. How does DyAug perform on large-scale dynamic graphs with millions of nodes and edges, especially considering the additional complexity introduced by rationalization and consistency regularization?
2. The current focus is on discrete-time dynamic graphs. How challenging would it be to adapt DyAug to continuous-time dynamic graphs (CTDGs)?
3. Could there be scenarios where the rationale-environment separation introduces new spurious correlations, and how can this be mitigated?
4. How sensitive is the model's performance to the choice of window size $w$ in the consistency regularization loss, and does this affect the robustness of DyAug?

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
This paper introduces a novel framework for dynamic graph data augmentation called DyAug, addressing a critical challenge in applying static GDA methods to dynamic graphs: maintaining temporal consistency across graph snapshots. By combining causal subgraph rationalization with environmental subgraph augmentation, DyAug performs augmentation across three dimensions: spatial, temporal, and spatiotemporal. Extensive experimental results demonstrate the effectiveness of DyAug.

### Strengths
1. This paper tackles the challenge of maintaining temporal consistency across graph snapshots, an issue that, according to the authors, has not been previously addressed. The approach of combining causal subgraph rationalization with environmental subgraph augmentation to enhance the graph from spatial, temporal, and spatiotemporal perspectives is some what novel.
2. The paper demonstrates the performance, robustness, and generalization capacity of DyAug through comprehensive experiments.
3. The paper is generally clear, with a structured presentation that facilitates understanding of the DyAug. The figures are particularly effective in illustrating key concepts, such as the causal and the proposed augmentation strategies.
4. The significance of DyAug lies in its potential impact on the field of robustness dynamic GNNs.

### Weaknesses
1. The claim of pioneering graph data augmentation (GDA) in dynamic graphs is overstated. Several works on out-of-distribution (OOD) handling in dynamic graphs [1,2,3] have already incorporated augmentation strategies tailored for dynamic graphs. These works, focusing on enhancing the generalization ability of dynamic GNNs, appear to predate the current work and should be thoroughly discussed and differentiated.
2. DyAug's approach of constructing a causal identification mask to separate rational and environmental factors, followed by disturbing the spurious factors, seems conceptually similar to techniques used in existing dynamic graph OOD works [1,2,3]. The paper needs to clearly articulate the distinctions between DyAug's methodology and these prior approaches, particularly in how causal discovery and perturbation are handled differently.
3. While the paper argues that prior static graph augmentation methods overlook temporal consistency, it remains unclear how DyAug's dynamic augmentation fundamentally ensures this consistency. The provided experimental evidence in Section 4.2 (Observation 1) is insufficient. A more detailed explanation is needed to clarify which specific modules or mechanisms within DyAug guarantee that augmentation does not disrupt the inherent temporal consistency of dynamic graphs. The current explanation lacks the necessary depth to fully understand how temporal consistency is maintained.

### Questions
1. What are the limitations of dynamic graph augmentation methods targeting dynamic graph OOD, and what is the motivation to design DyAug under these previous methods?
2. How does DyAug's approach to causal discovery and causal perturbation differ from that of existing dynamic graph OOD methods? A more detailed explanation is needed.
3. Which component of DyAug ensures that its augmentation does not disrupt the temporal consistency of dynamic graphs, and why? This requires further clarification.

For details, please refer to the Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel data augmentation method designed for dynamic graphs. Previous static graph data augmentation methods have shown poor performance on dynamic graphs, a phenomenon the authors attribute to the direct application of static graph augmentation techniques, which neglects the temporal consistency of graph structures. The authors introduce a learnable data augmentation method for dynamic graphs, incorporating a consistency loss function to ensure the temporal consistency of graph structures. Additionally, to enhance the performance of this data augmentation method in out-of-distribution generalization scenarios, the authors adopt a causal inference perspective to partition the original graph into rationale and environment subgraphs, thereby improving the algorithm's stability under data distribution shifts.

### Strengths
1. The authors present a new data augmentation approach motivated by the intuitive notion of temporal consistency in graph structures, which consistently achieves favorable performance in dynamic graph tasks. Furthermore, this method demonstrates stable augmentation in scenarios such as adversarial attacks and out-of-distribution generalization, showcasing the robustness of the algorithm.
2. The authors conducted extensive experiments based on various baselines, illustrating that this data augmentation method consistently provides enhancement across different baselines and scenarios.

### Weaknesses
1. The authors omitted ablation experiments in out-of-distribution generalization scenarios and adversarial attack scenarios other than structure attacks. Specifically, the paper lacks ablation studies evaluating the impact of the proposed method under distribution shifts, feature attacks, and Nettack attacks. This omission makes it difficult to fully assess the contribution of each component of the proposed method (temporal-conditioned rationalization, data augmentation, consistency regularization loss, and contrastive learning loss) under these diverse scenarios. The lack of these experiments reduces the persuasiveness of the algorithm's effectiveness explanation, particularly regarding its robustness and generalizability.
2. The complexity analysis presented in section 3.6 is potentially inaccurate. Specifically, during the computation of the consistency loss, the complexity associated with determining the similarity between two graphs is stated as constant. However, this complexity likely scales linearly with the number of edges, denoted as $\mathcal{O}(|\mathcal{E}|)$. Consequently, the overall complexity might be more accurately represented as $\mathcal{O}(\varpi T|\mathcal{E}|)$, where \varpi is the window size and T is the number of time steps. This revised complexity analysis could have implications for the scalability of the proposed method.
3. The paper does not include comparisons with some recent works on dynamic graphs. Incorporating more recent advancements in dynamic graph neural networks (DyGNNs) as baselines would provide a more comprehensive evaluation of the proposed method's performance and its standing within the current state-of-the-art.

### Questions
1. The source code repo is expired.
2. In section 3.4, the description of $\overline{M}=1_N-M$ and the specification that $1_N\in \set{1}^{N\times N}$ is an all-one matrix is somewhat perplexing. Given the typical sparsity of graphs, the transformation $\overline{M}=1_N-M$ would result in a very dense matrix, thereby significantly increasing computation as the number of edges grows. This raises the question of whether the intended expression was $\overline{M}=A-M$, where $A$ represents the adjacency matrix of the graph, rather than an all-one matrix.

### Soundness
3

### Presentation
3

### Contribution
2

# Benchmarking Positional Encodings for GNNs and Graph Transformers

- Decision: Reject
- Scores: 3, 5, 5, 5, 5

## Abstract
Recent advances in Graph Neural Networks (GNNs) and Graph Transformers (GTs) have been driven by innovations in architectures and Positional Encodings (PEs), which are critical for augmenting node features and capturing graph topology. PEs are essential for GTs, where topological information would otherwise be lost without message-passing. However, PEs are often tested alongside novel architectures, making it difficult to isolate their effect on established models. To address this, we present a comprehensive benchmark of PEs in a unified framework that includes both message-passing GNNs and GTs.
We also establish theoretical connections between MPNNs and GTs and introduce a sparsified GRIT attention mechanism to examine the influence of global connectivity. Our findings demonstrate that previously untested combinations of GNN architectures and PEs can outperform existing methods and offer a more comprehensive picture of the state-of-the-art. To support future research and experimentation in our framework, we make the code publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper studies the effect of different positional encodings across different graph transformer (GT) architectures. The goal of the paper is to understand their effect by isolating their contribution, instead of presenting the observed performance improvements that can be attributed to both the positional encoding technique and the specific architecture used. They also discuss a connection between MPNNs and GTs, although this connection is well-established in the literature, and proposed a sparsified variant of GRIT.

### Strengths
The goal of the paper (benchmarking positional encodings by isolating their contribution) is very clear at the beginning of the paper, although it gets lost while the paper progresses (see weaknesses). This goal is important, and therefore the research question is significant.

### Weaknesses
1. The paper lacks focus. While it starts by discussing the goal as understanding the effect of different position encodings, everything before the evaluation section does not discuss this point sufficiently. On the contrary, the paper presents the connection between MPNNs and GTs as a contribution, despite being well known in the literature (see for instance Velickovic 2023) and not central to the main focus of the paper.

2. Because of the lack of focus, the contributions of the paper related to the main goal are limited. The paper only tests few positional encoding techniques and few graph transformers. More importantly, *there is no discussion on the conclusions of the benchmarking study*: which PE is the best under which assumptions? The authors only discuss which PE is the best based on the dataset. I think it is necessary to have a section discussing when it is best to use a certain PE, based on the characteristics of the dataset (e.g., large graphs, local/global information needed for the prediction), of the task, or of the architecture used. Otherwise the paper does not help practitioners in their choice of PE, it simply lists which one is best for that particular dataset tested, and any variation in the dataset could lead to completely different conclusions.

Velickovic 2023. Everything is Connected: Graph Neural Networks

### Questions
1. Can you draw explicit conclusions about your findings? Specifically, please clarify conditions under which a particular PE may outperform others. I recommend that the authors include a specific section analyzing patterns in their results - for example, do certain types of PEs consistently perform better on larger graphs or tasks requiring more global information? This would help practitioners apply the findings more broadly beyond just the specific datasets tested.

2. I would encourage also to review the literature. For instance, the connection between MPNNs and GTs has been extensively studied (e.g., Cai et al., 2023, Müller et al., 2023) and you are missing a lot of related work. Also the introduction is missing citations to support your claims.

3. If you are benchmarking PE, why the tables report the best PE for each model? This naturally defeats the purpose of benchmarking PE, as you are only showing the best PE for that dataset and architecture.  Can you include tables or figures showing the performance of all PE-model combinations?


Cai et al., 2023. On the Connection Between MPNN and Graph Transformer

Müller et al., 2024. Aligning Transformers with Weisfeiler-Leman

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a unified evaluation framework and empirically investigates various combinations of positional encodings (PEs) and GNNs/GTs across multiple datasets, uncovering new combinations that surpass the current state-of-the-art. The results show that PEs can significantly impact model performance depending on the task, though they may sometimes reduce effectiveness. Additionally, the paper provides a theoretical analysis of the relationship between MPNNs and GTs using the WL test, and proposes a sparse MPNN architecture based on GRIT.

### Strengths
1. The paper is well-written and presented, with both theoretical and empirical analyses structured and clearly explained.

2. The extensive evaluation of PE and GNN/GT combinations across diverse datasets is commendable, establishing new state-of-the-art results on two sets of benchmark datasets.

3. The codebase, which includes implementations of all models and PEs, is a valuable resource for future researchers.

### Weaknesses
The primary limitation of this paper is its contribution.
1. Although the paper provides a valuable benchmarking evaluation on an important problem—understanding which PEs work best for specific tasks and architectures—the analysis offers limited new insights. Previous work has shown that different PEs yield different performance improvements based on the task. It would be more valuable if the authors provided deeper insights into this phenomenon, for instance, by characterizing tasks to explain why certain PEs (e.g., Laplacian-based, Random-walk-based, or others) are more beneficial. Even a theoretical analysis or synthetic tasks exploring this could help future researchers select the most suitable PEs based on task requirements.
2. Another contribution of the paper is the theoretical analysis of the relationship between MPNNs and GTs using the 1-WL test, interpreting GTs as message-passing on a new topology. However, the theorem’s significance is limited, as it is well-known that GTs with full attention can be seen as MPNNs on a fully-connected graph. Additionally, the theorem’s bounds on GT expressiveness based on the 1-WL test apply to the dependency graph rather than the original graph. The latter would have a more direct effect on downstream performance.

### Questions
1. How do the empirical results relate to theoretical analyses of PEs, such as [1]?
2. Were pretrained PEs, such as GPSE [2], considered?
3. Why are prediction heads included in the design space, given that they are typically task-specific?
4. Why was GRIT chosen as the basis for proposing a sparse version of GTs? Could this approach be generalized to other GTs?

[1] Comparing Graph Transformers via Positional Encodings. Black et al., ICML 2024. 
[2] Graph Positional and Structural Encoder. Cantrürk et al., ICML 2024.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper aims to systematically evaluate positional encodings (PEs) across various graph neural networks (GNNs) and graph transformer (GT) architectures. Positional encodings are critical for retaining graph topological information in GTs. The authors propose a unified benchmarking framework that isolates the effects of PEs from architectural innovations and find that previous untested combinations of PEs and architectures can lead to SOTA performance. The also explores the connection between message-passing networks and transformers and introduce a sparsified GRIT attention mechanism to balance local and global information.

### Strengths
1. The authors propose a unified benchmark, allowing for a comprehensive evaluation of PEs independent of architecture. They reproduces state-of-the-art MPNNs as well as GTs and integrate them into their codebase for comparison.
2. The experiments seem solid and provide insights into difference combinations of architectures and PEs. 
3. The authors provide extensive details on their experiment setups and results, which is good for reproduction.

### Weaknesses
1. The authors notes significant memory and computational demands for some random walk-based PEs (e.g., RRWP), which limits their practicality on large graphs. Could the authors provide more experiment results about time and space complexity? Specifically, it would be beneficial to see a more detailed breakdown of the computational cost, including the time taken for PE computation and the memory footprint for storing these encodings, especially as graph size increases. This should include not just the training time, but also the inference time, as the PE computation could be a bottleneck in real-world applications.
2. The authors may explore additional graph data types to confirm the consistency of PE impacts across different tasks beyond current settings. While the datasets used are standard benchmarks, it would be valuable to see how these PEs perform on graphs with different characteristics, such as graphs with varying node degree distributions, edge types, or graphs that represent different types of relationships (e.g., social networks vs. biological networks). This would help to understand the generalizability of the findings.
3. The authors may include more clarification and explanations on PEs in the main text, which may be challenging for readers unfamiliar with advanced PE concepts. For example, a more intuitive explanation of how different PEs capture graph structure and why certain PEs are more suitable for specific tasks would be beneficial. The current introduction assumes a certain level of prior knowledge, which might not be the case for all readers.

### Questions
1. The authors mention that the best PE choice varies depending on tasks and datasets, and sometimes the model can achieve good performance without any PE. Can the authors clarify more clearly why this happens or why PE doesn't work well sometimes? Are the existing PE designs not suitable for the particular case or it doesn't need any PE indeed?
2. The author provides their code but I couldn't open it. I don't know whether this is really a problem or is due to the network of my computer. 
3. For node-level tasks the author include arxiv dataset. Could the author evaluate the PE designs on a larger-scale dataset that can compare their performance on large graphs? Can the authors provide more insights into the scalabilid GRIT mechanism when applied to very large-scale graphs?

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
4

### Summary
The paper presents a benchmark study of positional encodings (PEs) in graph neural networks and graph transformers. The work encompasses three contributions: (1) the main one is a systematic evaluation of various PEs across different architectures, examining multiple PE methods across several benchmark datasets including very popular ones. This is accompanied by two other contributions: (2) theoretical insights connecting Graph Transformers (GTs) and the Weisfeiler-Lehman (WL) test, proving that GTs can be bounded by the 1-WL algorithm on fully connected graphs (can certain GTs can reach this bound), and (3) the introduction of SparseGRIT, a variant of GRIT that uses sparse connectivity while maintaining competitive performance.



Conclusion:
While the paper addresses an important practical need and provides valuable empirical insights, its contributions fall short of the novelty and depth expected at ICLR. The work would be more suitable for a venue focused on empirical machine learning studies or as a journal submission with expanded analysis. The authors should consider deepening their theoretical analysis, providing more interesting distinctions between different types of encodings before submitting to a more appropriate venue.

### Strengths
The paper addresses a significant practical need in the field, as the growth of PE schemes in recent years has made it challenging for practitioners to choose appropriate methods for their tasks. The authors examine multiple different PE methods across multiple architectures, providing valuable insights into their relative performance. Their comprehensive evaluation reveals that previously untested combinations can outperform existing methods. The authors provide a clear presentation of results including standard deviations across multiple runs, with detailed runtime and memory analysis for each PE method. The reproducibility of the work is strengthened by the authors' release of a unified codebase implementing all tested models and encodings.

### Weaknesses
The theoretical contributions of the paper are relatively modest. The classification of PEs into Laplacian-based, random walk-based, and others (Section 3.1) lacks depth, merely organizing existing methods without providing new insights into their relationships. For example, while Laplacian-based encodings are grouped together, there's no discussion of the spectral properties of the Laplacian and how different choices (e.g., normalized vs. unnormalized Laplacian) might impact the learned representations. Similarly, the random walk-based category could be further refined by considering the specific random walk process used (e.g., simple random walk vs. biased random walk) and its implications for capturing graph structure. The theoretical connection between GTs and WL test presented in Section 3.4 largely follows from existing work, with Theorem 3.2 being a straightforward extension of previous results. The paper would benefit from a more rigorous analysis of the conditions under which the bound is tight and whether specific PE choices affect the tightness of the bound. 

The paper would benefit from a clearer distinction between structural and positional encodings, as understanding their different roles is crucial for practitioners [see "On the Equivalence between Positional Node Embeddings and Structural Graph Representations" by Srinivasan and Ribeiro and followup papers]. The evaluation ignores this important distinction, treating all encodings as equivalent augmentations to node features. For example, the paper does not explore whether certain PEs are more effective at capturing global graph properties (e.g., graph diameter) while others are better at capturing local neighborhood information. This distinction is crucial because structural encodings like node degrees or graphlet counts provide information about the graph structure itself, whereas positional encodings aim to provide unique identifiers for nodes within the graph. The evaluation should have included experiments that specifically test the ability of different encodings to capture these distinct types of information. 

The presentation of SparseGRIT as a novel contribution requires more justification. The original GRIT paper may have already employed sparse variants in certain cases, and the paper would benefit from a more detailed discussion of how SparseGRIT differs from existing GRIT implementations beyond the simplified attention mechanism described in Equation 1. The authors should clarify whether the sparsity is applied to the attention matrix itself or to the underlying graph structure, and how this choice impacts the computational complexity and performance of the model. A more thorough comparison with existing sparse attention mechanisms would also be beneficial.

### Questions
The authors should clarify how SparseGRIT differs from sparse implementations in the original GRIT paper.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper provides a comprehensive benchmarking study on the effectiveness of various PEs for GNNs within a unified framework -- it investigates the impact of PEs on several types of models, including MPNNs and GTs, benchmarking the performance. The paper introduces a modified attention mechanism based on GRIT, denoted SparseGRIT, which facilitates localised graph convolutions through a sparsified attention mechanism.

### Strengths
1. **Comprehensive Benchmarking**: The study evaluates multiple PEs across MPNNs and GTs on several datasets, providing useful comparisons.
2. **Reproducibility**: A code for reproducing the results is provided.
3. **Clarity**: This paper is well written and easy to follow.

### Weaknesses
1. **Limited Novelty**: The paper mainly focuses on benchmarking PEs across various architectures, rather than introducing fundamentally new models or methodologies (beyond SparseGRIT, which is a straightforward extension of GRIT). While benchmarking is important, the lack of novelty limits the impact of the paper. The SparseGRIT modification, while presented as a contribution, appears to be a relatively minor adjustment to the existing GRIT attention mechanism, and its novelty is not thoroughly justified. A more in-depth exploration of the potential benefits and limitations of this modification is needed to establish its significance.

2. **Justification for PE Performance**: While the authors effectively demonstrate empirical differences in the performance of PEs across different models, they do not provide a theoretical explanation for the observed variations. Providing a theoretical explanation or justification to complement the empirical findings would enhance the depth and impact of the paper. For example, showing that certain PEs are more expressive (for example in graph separation power) than others would benefit the paper. Another option is to show and analyze empirically what structural information is captured via the different PEs. The lack of analysis into why certain PEs perform better in specific scenarios limits the practical utility of the benchmark, as it provides little guidance on which PEs to use in new tasks.

3. **Marginal Performance Gains**: The benchmarking results reveal no significant performance improvements over existing methods, except for the PCQM-Contact dataset. This raises concerns about the practical impact of the paper beyond its benchmarking contribution. The absence of substantial performance gains across most datasets suggests that the practical value of the proposed methods and the investigated PEs may be limited. The paper needs to demonstrate more clearly how the insights gained from the benchmarking can lead to tangible improvements in real-world applications.

### Questions
Do you have any theoretical justifications to support the empirical results observed for the different positional encodings across the different models? A theoretical perspective that could help explain why specific PEs outperform others, and in which cases, would improve the quality of the paper.

### Soundness
4

### Presentation
4

### Contribution
2

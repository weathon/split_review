# Do graph neural network states contain graph properties?

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 5, 3, 3

## Abstract
Deep neural networks (DNNs) achieve state-of-the-art performance on many tasks, but this often requires increasingly larger model sizes, which in turn leads to more complex internal representations. Explainability techniques (XAI) have made remarkable progress in the interpretability of ML models. However, the non-relational nature of Graph neural networks (GNNs) make it difficult to reuse already existing XAI methods. While other works have focused on instance-based explanation methods for GNNs, very few have investigated model-based methods and, to our knowledge, none have tried to probe the embedding of the GNNs for well-known structural graph properties. In this paper we present a model agnostic explainability pipeline for GNNs employing diagnostic classifiers. This pipeline aims to probe and interpret the learned representations in GNNs across various architectures and datasets, refining our understanding and trust in these models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a model-agnostic approach to interpreting Graph Neural Network (GNN) embeddings by probing for encoded graph properties across various architectures and datasets. Using diagnostic classifiers, the study examines whether these embeddings represent structural properties such as clustering, density, and centrality. The method is tested on synthetic (Grid-House), molecular (ClinTox), and brain connectivity (fMRI) datasets, assessing each GNN’s capability to linearly separate embeddings based on these key properties.

### Strengths
1. Novelty: Proposes a new model-agnostic explainability approach using probing techniques for GNNs, which is less explored than instance-level explanations.

2. Comprehensive Dataset Testing: Validates the method across diverse datasets, showcasing its versatility.

3. Insightful Comparisons: Provides detailed comparative analysis of different GNN architectures (e.g., GCN, GAT, GIN), noting their strengths in capturing specific graph properties.

### Weaknesses
1. The padding and sorting steps for node embeddings, while intended to address non-uniform node counts, might introduce ordering biases and disrupt permutation invariance. Specifically, sorting by the norm of the node embeddings, even if the norm is invariant to node permutations, could still introduce an artificial ordering that the diagnostic classifier might exploit, rather than truly capturing the graph properties. This is because the classifier could learn to associate specific positions in the sorted sequence with certain graph properties, which is not a desirable behavior for a model-agnostic approach.

2. Some limitations in dataset representativity for real-world scenarios, as synthetic datasets like Grid-House may oversimplify the types of structures a GNN may encounter. The Grid-House dataset, while useful for controlled experiments, does not capture the complexity and heterogeneity of real-world graphs. This raises concerns about the generalizability of the findings to more complex, real-world datasets, where the relationships between graph properties and node embeddings might be more nuanced and less easily separable.

3. Fails to fully address the explainability of intermediate GNN layers, focusing more on final representations; probing deeper layers would provide more comprehensive insights into feature evolution. The analysis primarily focuses on the final layer embeddings, neglecting the rich information encoded in intermediate layers. Understanding how graph properties are progressively captured and transformed across layers is crucial for a comprehensive understanding of GNN behavior. The current approach misses the opportunity to analyze the evolution of feature representations within the GNN, which could provide valuable insights into the model's learning process.

4. This is my first time reviewing the ICLR paper, but I believe there is a large space to improve this manuscript, especially the presentation of the paper, which is the basic requirement for a good work.

### Questions
1. For the first sentence in the abstract — 'Graph learning models achieve state of the art performance on many tasks, but so at ever larger model sizes. Accordingly, the complexity of their representations increase.' — I found it hard to follow. As I understand it, this could be rephrased as: 'Graph learning models achieve state-of-the-art performance on many tasks, but this often requires increasingly larger model sizes, which in turn leads to more complex internal representations.'

2. For the images in Fig. 1, it would be better to improve the drawing styles and fonts. For example: the large black right bucket is better to be thiner and move down a little to vertically center alight with the GNN model and Dense layers.
Could the authors elaborate further on how their approach differs from other model-agnostic techniques, and clarify any specific novelty and contributions to the interpretability of intermediate layers?

### Soundness
2

### Presentation
1

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
The paper investigates the explainability of GNNs by proposing a model-agnostic pipeline that uses diagnostic classifiers to probe the embeddings of GNNs for known graph properties. It addresses the challenge of interpreting GNNs due to their complex, non-Euclidean structure and presents findings on how different GNN architectures and regularization techniques affect the representation of graph properties. The study demonstrates that GNN embeddings can indeed reflect graph-theoretic and domain-specific properties, offering insights into the models' internal states and potentially enhancing trust in their predictions. The approach is validated through applications to toxicity and fMRI datasets, confirming the alignment of probed properties with domain knowledge and uncovering previously unexplored structural properties.

### Strengths
1. The investigation tackles a problem that is both intriguing and significant. To the best of the reviewer's knowledge, this is the inaugural paper to address it.

2. The proposed pipeline is streamlined yet yields effective results.

3. The experimental outcomes provide valuable insights that will benefit future research endeavors.

### Weaknesses
This paper has several weaknesses. Addressing Weakness 2 & 3 & 4 will make a compelling case for 'accept.' Specifically:

1. The section designated for findings focuses more on articulating the experimental setting rather than the findings themselves. A clearer exposition of the results will fortify this section. (Question 1)

2. The use of GNNs, which are based on message passing and 1-WL, suggests that the inclusion of stronger GNNs could substantiate the experimental framework. (Question 2)

3. The authors have missed discussing the supervision signal, an important element that merits attention. (Question 3)

4. There is a lack of comprehensive explanations for the experimental results. Elaborating on these would enhance the paper's contribution to the field. (Question 4)

### Questions
1. The reviewer suggests that the findings section should encompass both the experimental settings and the derived conclusions. For instance, while the paper mentions an investigation into the effects of regularization techniques on learning, it fails to present the subsequent conclusions. A more comprehensive analysis, including both the setup and outcomes, would be beneficial.

2. Considering the expressiveness of GNNs, it is anticipated that stronger GNNs would more effectively capture graph properties. However, this may not hold true in practice due to generalization effects. It is recommended that the authors explore GNNs equivalent to 3-WL and consider examining graph transformers to bolster the paper's contributions.

3. Drawing parallels from computer vision research, where the supervision signal plays a pivotal role, it would be insightful to examine if self-supervised models in GNNs also capture structural information more effectively than supervised ones (like the results in CV).

4. While the extensive experiments contribute significantly to the field of Explainable AI (XAI), understanding the reasons behind varying performance levels is crucial. Questions such as why certain layers outperform others, why some substructures are more accurate, whether these findings correlate directly with the labels, and how the type of supervision influences the results, are all critical for a deeper comprehension of the study.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper explores the types of topological information encoded in node embeddings when solving downstream graph classification tasks. To reveal this information, the authors apply linear probing classifiers to predict various graph properties. The inputs are node embeddings computed at different depths across all graphs in the training data. Some of these properties can be inferred after the global pooling stage and are closely tied to the downstream task.

### Strengths
Linear probing is a straightforward yet powerful method, demonstrating strong results across the tested datasets. Its simplicity makes it easy to implement, while still providing valuable insights into the graph properties encoded by the GNNs.

Layer-wise analysis holds significant potential for identifying patterns in GNNs, much like the successes achieved in CNNs. This approach allows for a deeper understanding of how GNNs progressively capture and abstract graph properties across different layers.

### Weaknesses
 "We addressed this by sorting the embeddings in descending order and padding with zeros at the end". However, this solution for handling node features before the global pooling stage seems somewhat arbitrary. An immediate alternative approach could be to consider different pooling strategies and even their concatenation. The chosen method of sorting node embeddings by norm and padding, while a practical solution, lacks a strong theoretical justification and may introduce biases. Specifically, sorting by norm could inadvertently emphasize nodes with larger embedding magnitudes, potentially skewing the information captured by the linear probe. Furthermore, the padding with zeros, while addressing variable graph sizes, might create artificial patterns that the probe could exploit, rather than focusing on the actual graph properties. A more rigorous approach would involve exploring permutation-invariant methods, such as Deep Sets or other aggregation techniques, which are designed to handle unordered sets of node embeddings without introducing such biases. These methods would provide a more robust and reliable way to probe pre-pooling layers.

Furthermore, Probing Graph Representations (Akhondzadeh et al., 2023) conducted a similar probing study, arriving at nearly identical conclusions. As a result, the amount of novel information introduced by this paper is limited. The authors also fail to compare their probing performance against that of Akhondzadeh et al., 2023, which would have been valuable. The lack of a direct comparison with the existing work makes it difficult to assess the unique contributions of this study. The authors should have clearly delineated the differences in methodology and the specific insights gained that were not already present in the previous work. Without this, the novelty of the paper remains questionable.

Several key details are missing, such as the performance of the models on the main task and the correlation between task accuracy and probing accuracy. Although the referenced tables are provided in an extensive appendix, the main paper should be more self-contained to allow readers to verify the claims and key points easily. The absence of these details in the main paper hinders the ability of the reader to fully grasp the significance and implications of the findings. The correlation between the main task performance and the probing results is crucial for understanding the relationship between the learned representations and the downstream task. Without this information, it's difficult to assess the practical relevance of the probing results. Additionally, the text in Figures 2 and 3 is difficult to read, which hinders clarity.

### Questions
How does this work differ from the study "Probing Graph Representations" (Akhondzadeh et al., 2023)? In particular, I would like to focus on the limitations of the previous approach and the new insights provided by this current study.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper claims that existing explainability methods are mostly instance-based and not well-suited for GNNs. It presents a model-agnostic explainability pipeline using diagnostic classifiers to better understand and trust GNN representations across various architectures and datasets. The findings are interesting and provide unique insights in the XAI for GNNs field. However, the paper has a confusing organization.

### Strengths
1. This paper discusses explainability from the model-agnostic aspect and explores the effectiveness of local graph properties.
2. This paper provides a comprehensive set of experiments on the local and global properties.

### Weaknesses
1. This paper is not well-organized. For example, in the introduction, the findings contain some figures and tables, but they can't be found in the main body. Since they are highly relevant to the findings, it would be better to present the results in the main body. The $R^2$ score is not well explained in the main body. In the appendix, there are some descriptions about the $R^2$ score; however, the mathematical formulation is not clear.
 2. Some key points are not clear about the experiments. For example, in line 133, it is confusing when discussing 'defining specific properties.' How to explore different local properties is not clear.
3. The figures are not well presented. For example, in Figure 3, the figures in the first row are hard to understand due to unclear captions. Additionally, it is not clear what $x$, $x_2$, and $x_3$ represent.

### Questions
1. What is the mathematical definition of $R^2$?
2. How are the different local properties discussed in the experiments?

### Soundness
2

### Presentation
2

### Contribution
2

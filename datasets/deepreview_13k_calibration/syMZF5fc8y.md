# Disentangled and Self-Explainable Node Representation Learning

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 5, 3, 3

## Abstract
Node representations, or embeddings, are low-dimensional vectors that capture node properties, typically learned through unsupervised structural similarity objectives or supervised tasks. While recent efforts have focused on explaining graph model decisions, the interpretability of \textit{unsupervised} node embeddings remains underexplored. To bridge this gap, we introduce \approach{} (\textbf{Di}sentangled and \textbf{Se}lf-Explainable \textbf{N}ode \textbf{E}mbedding), a framework that generates self-explainable embeddings in an unsupervised manner. Our method employs disentangled representation learning to produce dimension-wise interpretable embeddings, where each dimension is aligned with distinct topological structure of the graph. We formalize novel desiderata for disentangled and interpretable embeddings, which drive our new objective functions, optimizing simultaneously for both interpretability and disentanglement. Additionally, we propose several new metrics to evaluate representation quality and human interpretability. Extensive experiments across multiple benchmark datasets demonstrate the effectiveness of our approach.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces **DISENE (Disentangled and Self-Explainable Node Embedding)**, a novel framework designed to generate self-explainable and disentangled node embeddings in graph-based learning tasks. The method leverages disentangled representation learning to ensure that each dimension of the learned embeddings corresponds to a unique topological substructure in the input graph, aiming to improve the interpretability of learned representations. The authors propose new evaluation metrics, such as overlap consistency and dimensional sparsity, to quantify the degree of disentanglement and interpretability of the embeddings.

### Strengths
The paper presents a well-structured approach with clearly defined disentanglement objectives and proposed evaluation metrics. The experiments cover multiple datasets and tasks, providing a comprehensive evaluation of the proposed method.

### Weaknesses
1. While the paper claims to generate "self-explainable" embeddings, the interpretability largely relies on proposed metrics (e.g., overlap consistency) without providing direct, human-interpretable explanations for individual embedding dimensions. The method lacks intuitive explanations for individual nodes or substructures, limiting the practical utility of the "self-explainable" claim, particularly for non-technical users or domain experts who might expect more direct insights from the embeddings. The connection between the identified subgraphs and human-understandable concepts is not clearly established, making it difficult to assess the true interpretability of the learned representations beyond the proposed metrics.

2. The paper lacks comprehensive comparisons with other interpretability-focused methods in graph learning, such as **GNNExplainer** or **PGExplainer**, which provide more fine-grained explanations at node and edge levels. A detailed comparison with these methods in terms of interpretability (not just performance) would strengthen the paper's claims. Additionally, comparisons with simpler feature-based interpretability approaches would help highlight the unique advantages of the proposed method. The absence of a clear benchmark against methods that directly aim to explain model predictions, rather than just the embedding space, makes it difficult to position the contribution of this work within the broader landscape of graph interpretability.

3. **Evaluation metrics may be subjective**: While novel, the new evaluation metrics are somewhat subjective and not widely used in the graph learning community. Calibrating these metrics against more established interpretability evaluation standards or providing more detailed justification for why these metrics are appropriate would be helpful. For instance, how does overlap consistency relate to human ability to interpret the learned embeddings? More human-centric evaluations, such as user studies or expert assessments, could help validate the practical interpretability of the embeddings. The paper does not provide a clear link between the proposed metrics and the actual utility of the embeddings for human understanding, raising concerns about the practical relevance of the reported results.

### Questions
1. How does DISENE compare to graph interpretability methods like GNNExplainer in terms of explainability? A direct comparison with methods like GNNExplainer or PGExplainer would be helpful, not just in terms of performance but also in the quality of explanations provided. Can DISENE provide interpretable explanations at node or edge level similar to these methods?

2. How does DISENE scale to larger graphs? Could the authors provide more details about the computational complexity of the method? Specifically, how does the disentanglement objective affect training time and memory usage, and how does the method scale to larger graphs?

3. How do the proposed metrics relate to human interpretability? Since these metrics are novel, it would be useful to understand how well they align with human judgments of interpretability. While the proposed metrics help quantify disentanglement, it would be helpful to provide visualizations or examples where specific embedding dimensions correlate with interpretable graph structures (e.g., communities, topics). This would help demonstrate the practical interpretability of the method.

### Soundness
3

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
3

### Summary
In this paper, the authors propose a method for interpreting node embeddings. Their method is based on several desiderata in terms of graph structures. In addition, they also propose several new criteria to evaluate the explainability. Experimental results seem to validate their method on these criteria.

### Strengths
- The authors propose novel and interesting perspectives to consider node embedding interprebility. New metrics are also introduced to measure these perspectives.

- Experiment results seem to be promising.

### Weaknesses
 - The proposed method for node interprebility is based on graph structures but semantic information is omitted, as verified by experiments that in GNN methods, node embeddings are initialized by identity matrix. However, in real-world applications this may not be true. For example, in social networks, if each node represents a user, it does not make sense that the user information is not considered in initial features. Whether or not the proposed method can be applied to semantic-rich graph scenarios are not discussed in the paper.

- The three key desiderata is not well explained. In corresponding paragraphs, the authors directly derive how they achieve these goals without explaining them. The definition of Equation 1 does not make sense to me as well. Say when we have $\phi_{d_1} (u_1, v_1; h) > 0$, it only means the the dimension $d_1$ is more important for embeddings of $u_1$ and $v_1$ (to compute the edge likelihood as in the paper, but what is the physical meaning of edge likelihood by the way?) than $d_1$ to other node embeddings with edges. Why could we use it to assign edges to dimensions? The dimension is shared across all node embeddings but the edge is not.

- While the authors propose several metrics for evaluation, I am confused why they do not compare their methods with previous metrics and representative node classification explanation methods such as GNN Explainer. If there is a discrepancy, please specify.

Ying, Zhitao, et al. "Gnnexplainer: Generating explanations for graph neural networks." Advances in neural information processing systems 32 (2019).

### Questions
See the weakness above

### Soundness
2

### Presentation
2

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
The paper introduces DISENE, a novel approach to self-explanatory node embedding, addressing the increasing need for interpretability in graph representation learning. DISENE’s design emphasizes disentangled representations, allowing each embedding dimension to independently capture specific, non-overlapping structural features of the graph. This self-explanatory capability is achieved through a combination of disentangled representation learning and the embedding of interpretability directly within the model architecture, moving beyond traditional post-hoc interpretability approaches.

### Strengths
1. Innovative Self-Explanatory Node Embedding Method: This paper introduces the DISENE model, which leverages disentanglement and self-explanatory design to enable each embedding dimension to correlate directly with specific structural features within the graph. 
2. Disentangled Feature Representation: DISENE ensures that each embedding dimension independently captures a unique graph structure feature, minimizing overlap across dimensions. This disentangled representation improves both the interpretability and robustness of the embeddings, providing more granular structural information for downstream applications that require feature independence.

### Weaknesses
1. Reliance on Interpretability Metrics with Ambiguous Definitions: The paper relies heavily on various interpretability metrics, such as consistency and sparsity, to evaluate model performance. However, these metrics lack clear, systematic definitions in the text. For instance, Section 4.2: Evaluation Metrics introduces these terms conceptually but fails to provide precise mathematical definitions or specific calculation methodologies. This lack of clarity may lead to inconsistencies in metric implementation across studies, thereby impacting the reproducibility of the results and the fairness of comparisons. For interpretability metrics to serve as robust evaluation tools, a more rigorous definition and operationalization are essential.

2. Ambiguity in Interpretability Metric Definitions: While the paper presents novel interpretability metrics, it leaves substantial gaps in detailing how these metrics are quantified. Section 3.4: Explanation and Evaluation discusses the interpretability aspects of the model but lacks the necessary formalism and computation process, making it challenging to assess the reliability and generalizability of these interpretability metrics. This ambiguity undermines the objective measurement of the model’s self-explanatory capabilities, calling into question the effectiveness of the proposed interpretability criteria.

3. Lack of Competitive Edge in Link Prediction and Node Classification Tasks: DISENE exhibits only moderate performance in standard tasks like link prediction and node classification, without showcasing significant improvements. As reported in Table 3: Link Prediction Results and Table 4: Node Classification Results, DISENE’s accuracy and AUC scores do not exhibit a marked advantage over other established models. This highlights a trade-off between interpretability and predictive power, suggesting that while DISENE makes strides in interpretability, it may fall short in delivering competitive performance in traditional graph embedding tasks, limiting its overall efficacy in practical applications.

4. Limited Dataset Scope, Focused on Small-Scale Citation Networks: The paper’s empirical analysis relies heavily on established citation networks such as Cora, CiteSeer, and PubMed (Section 4.1: Datasets). While these datasets are standard in graph embedding research, they are relatively small and structurally simple, which raises concerns about the model’s generalizability to larger, more complex graph structures. The limited dataset scope restricts the evaluation of DISENE’s performance on diverse, real-world graphs and challenges the model’s claims of broad applicability.

5. Outdated Baseline Comparisons: The baseline models selected for comparison—primarily traditional graph embedding methods such as DeepWalk, node2vec, and GraphSAGE (Section 4.3: Baselines)—do not reflect the recent advancements in graph representation learning. Given the rapid evolution of graph neural networks, the lack of comparisons with modern methods, including GAT, Graph Transformers, and Graph Autoencoders, as well as other interpretable models, undermines the robustness of the empirical validation. Comparisons with more recent and sophisticated models would provide a stronger benchmark, allowing for a more accurate assessment of DISENE’s strengths and weaknesses in both interpretability and performance.

### Questions
See Weaknesses

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a framework that generates self-explainable embeddings in an unsupervised manner. The method employs disentangled representation learning to produce dimension-wise interpretable embeddings, where each dimension is aligned with distinct topological structure of the graph. The paper drives new objective functions and optimizes simultaneously for both interpretability and disentanglement. Additionally, the paper proposes new metrics to evaluate representation quality and human interpretability.

### Strengths
1. The paper formalizes new and essential criteria for achieving disentangled and explainable node representations
2. The paper introduces novel evaluation metrics to help quantifying the goodness of node representation learning

### Weaknesses
1. The paper introduces comprehensibility as a metric for evaluating explanations. However, how does the method perform on widely-used explanation metrics like AUC, Fidelity-, and Fidelity+? I strongly recommend that the authors also consider including these popular metrics to thoroughly assess the method's performance.

2. The paper proposes using comprehensibility and sparsity to enhance human interpretability. This raises a natural question: do these metrics truly support human understandability? I strongly recommend that the authors conduct human evaluations to validate that these metrics align with human comprehension.

3. The baselines are too weak. The authors compare with the node embedding methods: DeepWalk, Deep AE, DISE-GAE, DISE-FACE. I suggest the authors consider more modern methods to have the node embedding, such as normalizing flows [R1], diffusion models [R2], self-supervised methods [R3].

4. The method is self-explainable, but how effective is the visualization of its explanations? I suggest that the authors include a case study to show the visualization.

5. The paper claims utility for downstream tasks like link prediction and node classification. However, the baselines used for evaluating these tasks are relatively weak. I recommend that the authors consider incorporating more widely-used contrastive learning methods as baselines, such as [R4], to assess whether the proposed node embeddings achieve superior performance in these downstream tasks.

### Questions
See the weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

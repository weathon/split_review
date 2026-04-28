# Characterizing Massive Activations of Attention Mechanism in Graph Neural Networks

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 5, 3

## Abstract
Graph Neural Networks (GNNs) have become increasingly popular for effectively modeling data with graph structures. Recently, attention mechanisms have been integrated into GNNs to improve their ability to capture complex patterns. This paper presents the first comprehensive study revealing a critical, unexplored consequence of this integration: the emergence of Massive Activations (MAs) within attention layers. We introduce a novel method for detecting and analyzing MAs, focusing on edge features in different graph transformer architectures. Our study assesses various GNN models using benchmark datasets, including ZINC, TOX21, and PROTEINS. Key contributions include (1) establishing the direct link between attention mechanisms and MAs generation in GNNs, (2) developing a robust definition and detection method for MAs based on activation ratio distributions, (3) introducing the Explicit Bias Term (EBT) as a potential countermeasure and exploring it as an adversarial framework to assess models robustness based on the presence or absence of MAs. Our findings highlight the prevalence and impact of attention-induced MAs across different architectures, such as GraphTransformer, GraphiT, and SAN. The study reveals the complex interplay between attention mechanisms, model architecture, dataset characteristics, and MAs emergence, providing crucial insights for developing more robust and reliable graph models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper identifies the existence of Massive Activations (MAs) across various graph transformer models, emphasizing their adverse effects on model stability and performance. The paper proposes a novel mechanism called the Explicit Bias Term (EBT) that compares activation ratios between untrained and trained models to detect MAs. Subsequently, EBT is designed to stabilize activation values by integrating bias terms directly into the attention mechanism. Additionally, the study investigates the role of MAs in adversarial attacks, introducing a gradient ascent attack method to rigorously evaluate EBT’s effectiveness in mitigating MAs. Experimental results demonstrate that MAs are widely present across different GNN architectures and datasets, while EBT significantly reduces the impact of MAs and enhances model robustness.

### Strengths
1.	The paper employs a rigorous approach to define Massive Activations (MAs) and experimentally confirms that MAs are a widespread phenomenon across various attention-based models and datasets.
2.	The paper proposes the Explicit Bias Term (EBT) to mitigate the influence of Massive Activations (MAs), and this method is applicable across various downstream tasks.
3.	Experiments have shown that EBT can significantly reduce the influence of MAs and has proven to be effective in enhancing model robustness against the gradient ascent attack method.

### Weaknesses
1.	The paper introduces the Explicit Bias Term (EBT) as a countermeasure to reduce the impact of Massive Activations (MAs). However, it lacks sufficient theoretical justification or a detailed explanation of how EBT can effectively mitigate MAs. Specifically, the mechanism by which the bias terms, integrated into the attention mechanism, counteract the identified MAs is not clearly articulated. The paper does not provide a rigorous analysis of why these specific bias terms are effective, nor does it explore alternative bias mechanisms or provide a comparison to other potential mitigation strategies.
2.	The paper presents the fitting results of the logarithm of activation distributions in Figure 3, but it uses the same gamma distribution for different datasets, models (GraphTransformer, GraphiT, SAN), and network layers. This approach is not sufficiently reliable, as activation distributions may have different distributions across various datasets, models, and layers, requiring different fitting distribution to accurately capture these characteristics. The use of a single gamma distribution across such diverse scenarios raises concerns about the validity of the analysis and the conclusions drawn from it. It is essential to demonstrate that the chosen distribution is appropriate for each specific case, or to justify why a single distribution is sufficient.
3.	In Figures 1 and 2, the activation ratios of the base model appear within a stable range, while those of the trained model fluctuate with the edges. This inconsistent visualization hinders an intuitive comparison of the activation distributions between the base and trained models within the same figure. The lack of a consistent baseline makes it difficult to directly assess the impact of training on activation patterns. A more consistent visualization approach would be beneficial to facilitate a clearer understanding of the differences between the base and trained models.
4. The presentation of tables should be improved and contain at least two lines.

### Questions
1.	Figure 3 applies the gamma distribution to approximate the negative logarithm of activation magnitudes across distinct layers and datasets, such as layer 3 of GraphTransformer on ZINC, layer 0 of GraphiT on ZINC, and layer 1 of SAN on OGBN-PROTEINS. Is this single gamma distribution capable of accurately fitting the activation distributions across these diverse scenarios?
2.	While the paper demonstrates the existence of MAs in older models like GraphiT, GraphTransformer, and SAN, is this phenomenon also observed in more recent advancements, such as SGFormer?

### Soundness
2

### Presentation
2

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
This paper investigates an interesting and significant phenomenon in attention-based Graph neural networks (GNNs): Massive activations (MAs) in attention layers. The authors conduct a systematic analysis of this phenomenon in GNNs built with different Graph Transformer layers and propose a method for detecting MAs and analyzing their effects on edge features. Besides, the Explicit Bias Term (EBT) is proposed as a countermeasure, whose robustness bringing to attention-based GNNs is also validated on well-established datasets.

### Strengths
1. The phenomenon investigated in this paper is significant, and the exploration of it may influence the performance of attention-based GNNs.
2. Some empirical experiments are comprehensive.

### Weaknesses
1. The motivations of this paper are not clear enough. The authors claim that their focus is variants of Graph Transformers. Why conventional attention-based GNNs (e.g., GATs and corresponding variants) are not considered in this work is not mentioned in the Section of Introduction. It is not sufficient to simply state the focus is on Graph Transformers; a clear rationale is needed for excluding other attention mechanisms, especially since many GAT variants also incorporate edge features.
2. Some terms are not well defined or explained. For example, what does the edge feature stand for in this paper? The paper needs to provide a more precise definition of edge features, including the types of information they represent and how they are encoded within the model. The current description is too vague for a reader to fully understand the experimental setup.
3. The insights and observations presented in this paper are mainly based on the analysis of three test datasets, i.e., ZINC, TOX21, and PROTEINS. I’m wondering whether similar observations or insights can be obtained from a wide range of test datasets. The authors are suggested to conduct a more comprehensive analysis on more real-world datasets, e.g., ones from OGBN (for graph property prediction) and other publicly available datasets for graph-level tasks. The current scope is too limited to draw general conclusions about the behavior of attention mechanisms in GNNs.
4. More recent attention-based GNNs should be investigated in the paper, which may provide an overview of the advances of graph attention. For example, GATv2, Graph conjoint attentions networks, and Adaptive structural fingerprint GNN should be investigated in the manuscript. The paper should demonstrate awareness of the current state-of-the-art in graph attention mechanisms.
5. Some experiments can be extended. For example, the ablation studies shown in Table 2 can be extended to all three variants of Graph Transformers on all test datasets considered in this paper. The current ablation study is insufficient to fully validate the proposed method across different architectures and datasets.

### Questions
1. Why are conventional attention-based GNNs not considered in this work?
2. What does the edge feature stand for in this paper?
3. Are similar observations or insights obtained from a wide range of test datasets?
4. More recent attention-based GNNs should be investigated in the paper.
5. Some experiments, e.g., the ablation studies in Table 2 can be extended.

### Soundness
2

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
Graph neural networks (GNNs) are popular for effectively modeling data with graph structures. Recently, attention mechanisms have been integrated into GNNs to improve their ability to capture complex patterns. This paper presents a comprehensive study on the emergence of massive activations (MAs) within attention layers. This study assesses various GNN models on three datasets, ZINC, TOX21, and PROTEINS.

### Strengths
1. This work studies the existence of massive activations (MAs) in attention layers of graph neural networks, improving the understanding of attention in graph structures.
2. This work presents various types of visualization, providing a deep insight on the existence of MAs and their distributions.
3. The observations and insights presented in this work can be beneficial to the community, considering that many people are working on improving a graph transformer structure.

### Weaknesses
1. In such a benchmark study, I would expect a lot more combinations of models, datasets, and configurations to verify the generalizability of observations and insights. I don’t believe the current experiments are comprehensive enough to have conclusive claims. It would be also nice to include more recent graph transformer structures, particularly those that utilize attention mechanisms across all node pairs, not just adjacent ones. The limited scope of the experiments makes it difficult to assess the broader relevance of the findings.
2. This work is not motivated well, as it is not clear why we should study MAs, and why they are problematic. How exactly do they affect the final performance on downstream tasks? The authors provide Tables 1 and 2 in this regard, but they seem to be indirect evidence. The connection between the observed massive activations and their impact on model performance needs to be more clearly established. Without a direct link to performance degradation or other issues, the significance of studying MAs remains unclear.
3. The authors claim that they propose a robust detection methodology and the explicit bias term as a solution for MAs, but I’m not certain if any of these make a significant contribution. The methodology for detecting MAs needs to be more rigorously validated, and the effectiveness of the proposed bias term in mitigating the issue should be demonstrated more convincingly. The current evidence does not provide a strong case for the practical utility of these contributions. Overall, I believe the technical quality of the paper should be improved, and the insights presented in the paper should be connected to what happens in the actual models.

### Questions
1. In lines 191 - 194, the authors mention that “attention is computed between pairs of adjacent nodes only,” but many graph transformers compute attention also for non-adjacent node pairs. Do the authors consider only the model structures with this constraint?

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
3

### Summary
This paper investigates the emergence of Massive Activations (MAs) in attention-based Graph Neural Networks (GNNs). It identifies the link between attention mechanisms and MAs, which can destabilize models. The study proposes a method to detect and analyze MAs, introduces the Explicit Bias Term (EBT) as a countermeasure, and evaluates various GNN architectures like GraphTransformer and GraphiT on benchmark datasets. The findings emphasize the impact of MAs on model performance and robustness, offering insights for developing more resilient graph-based models.

### Strengths
1.	The paper provides a comprehensive study on the emergence of Massive Activations (MAs) in attention-based GNNs, highlighting a previously unexplored issue that affects model stability and performance.
2.	The writing is logically clear and coherent.

### Weaknesses
1.	The contribution is overstated. The core observation of Massive Activations (MAs) and the proposed solution, Explicit Bias Term (EBT), are not new. The work primarily transfers concepts from prior work [1] on LLMs to attention-based GNNs.
2.	The observations of MAs on attention-based GNNs lack deeper analysis. For instance, while massive activations are suggested to serve as an important bias in the attention mechanism, the paper mainly discusses their focus on unimportant features without thorough examination. Specifically, the paper does not define what constitutes an 'unimportant feature' in the context of graph data, nor does it provide a rigorous analysis of how these activations correlate with feature importance or node classification performance.
3.	The technical motivation is not clear. The authors do not clearly explain the fundamental advantage between using an untrained model to estimate MAs and using the median activation value within the layer for estimation. The paper lacks a clear justification for why the distribution of activations in an untrained model serves as a suitable baseline for identifying MAs, especially given that the untrained model's activations may not be representative of the activation patterns in a trained model. Furthermore, the method for normalizing activations using the median value within a layer is not well-justified, and it's unclear how this normalization affects the detection of MAs.
4.	All the figures and tables in the paper are not up to standard. The figures in the paper lack detailed explanations of the axes and the different lines, which may confuse readers. The tables also lack essential information, such as the variance across multiple trials, which is crucial for assessing the statistical significance of the results.
5.	The experimental results are not convincing, as the tables do not show the variance across multiple trials.

### Questions
1.	What is the main contribution of this paper compared to the previous work [1]? It’s important to identify what new insights or advancements this paper offers.
2.	On page 5, line 258, the authors mention, "When MAs appear, we have found two possible phenomena." This statement, “possible phenomena,” may leave readers confused. The paper could benefit from a more detailed mechanistic explanation of these observations.
3.	On page 4, line 197, the authors state, "MAs are an inherent characteristic of the attention-based mechanism in graph transformers and related architectures, not strictly dependent on the choice of the dataset." However, observations from Figure 1 suggest that the same architecture exhibits significant variations in MAs across different datasets. This raises questions about the potential dependency of MAs on the dataset, which should be addressed more thoroughly.

[1] Sun M, Chen X, Kolter J Z, et al. Massive activations in large language models[J]. arXiv preprint arXiv:2402.17762, 2024.

### Soundness
2

### Presentation
2

### Contribution
2

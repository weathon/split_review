# Multi-modal Prompt Learning Empowers Graph Neural Networks with Semantic Knowledge

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 3, 5

## Abstract
While great success has been achieved in building generalizable language models, three fundamental issues hinder GNN-based graph foundation models: the scarcity of labeled data, different levels of downstream tasks, and the conceptual gaps between domains. In depth, though the labels of real graphs are associated with semantic information, most graph learning frameworks ignore it by turning semantic labels into numerical labels. In this work, to address these issues, we present a new paradigm that leverages the text modality to align downstream tasks and data with any pre-trained GNN given only a few semantically labeled samples. Our paradigm embeds the graphs directly in the same space as the LLM by learning both graph prompts and text prompts simultaneously. To accomplish this, we improve state-of-the-art graph prompt method based on our theoretical findings. Then, we propose the first multi-modal prompt learning approach for exploiting the knowledge in pre-trained models. Notably, in our paradigm, the pre-trained GNN and the LLM are kept frozen, so the number of learnable parameters is much smaller than fine-tuning any pre-trained model. Through extensive experiments on real-world datasets, we demonstrate the superior performance of our paradigm in few-shot, multi-task-level, and cross-domain settings. Moreover, we build the first zero-shot classification prototype that can generalize GNNs to unseen classes. The code is provided in the supplementary materials.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes Morpher, which leverages the text modality to align downstream tasks and data with any pre-trained GNN given only a few semantically labeled samples. The key idea is to embed the graphs directly in the same space as the LLM by multi-modal prompt learning. Experiments demonstrate the superior performance of Morpher in few-shot, multi-task-level, and cross-domain settings.

### Strengths
1.  The proposed Morpher can generalize GNN to unseen classes.
2.  The authors provide codes for reproducibility.
3.  This paper is easy to follow.

### Weaknesses
1. The authors only show that AIO [76] is unable to learn good representations of the downstream data. In my opinion, some state-of-the-art graph prompt methods such as PRODIGY [Ref1] have addressed this issue.
2. From Appendix D.3 in [Ref1], PRODIGY can also apply to the zero-shot classification. Therefore, the comparison of PRODIGY and Morpher is necessary.
3. Some references such as [Ref2, Ref3] are missing.

### Questions
See Weaknesses.

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
This paper introduces a new paradigm for enhancing Graph Neural Networks (GNNs) through multi-modal prompt learning, which leverages text data to align downstream tasks with pre-trained GNNs using only a few semantically labeled samples. The approach embeds graphs in the same semantic space as large language models (LLMs) by jointly learning graphs and text prompts. Building on theoretical insights, the authors improve existing graph prompt methods and propose a multi-modal framework that fully utilizes knowledge from pre-trained models without requiring fine-tuning of either the GNN or LLM. This setup significantly reduces the number of learnable parameters. Extensive experiments on real-world datasets demonstrate the paradigm's effectiveness across few-shot, multi-task, and cross-domain settings. Additionally, the framework includes a zero-shot classification prototype that enables GNNs to generalize to previously unseen classes.

### Strengths
S1. The manuscript is well-organized and clearly written, with structured and detailed mathematical derivations. For instance, in the "Improved Graph Prompt Design" section, the paper rigorously derives the formulation for balancing cross-connections between input nodes and prompt nodes. 
S2. The proposed sparse cross-connection mechanism in Morpher prevents prompt features from overwhelming graph features, offering a balanced integration for improved feature alignment.
S3. Comprehensive experiments across diverse datasets, including Cora, CiteSeer, and synthetic zero-shot datasets, effectively demonstrate Morpher's adaptability and robustness.
S4. Results show that Morpher achieves superior performance over baselines in few-shot and zero-shot tasks, validating its cross-domain generalization capabilities.

### Weaknesses
W1. This paper proposes a sparse cross-connection mechanism for Morpher to prevent prompt features from overloading graph features, but could this also limit information exchange between graph and text modalities, weakening alignment quality? For complex tasks requiring richer feature fusion, this limited interaction may be insufficient. Specifically, the sparse connections might hinder the model's ability to capture intricate relationships between graph nodes and textual descriptions, potentially leading to suboptimal performance in tasks that demand a deep understanding of both modalities. The paper does not provide a detailed analysis of how the degree of sparsity affects the overall performance, which is crucial for understanding the trade-offs involved.

W2. Morpher’s reliance on graph-text fusion assumes complementary information from both modalities, but in tasks with weaker associations, might this integration introduce noise and reduce performance? For instance, if the text prompts are not highly relevant to the graph structure or node features, the fusion process could dilute the useful information present in the graph, leading to decreased accuracy. The paper lacks a discussion on how the model handles scenarios where the textual prompts are ambiguous or contain irrelevant information.

W3. The paper does not analyze how differences in data distribution between pre-training and target datasets influence transfer performance, which is crucial for domain adaptation. Quantifying these differences (e.g., via JS or KL divergence) could clarify Morpher’s sensitivity to dataset similarity. Specifically, the paper should investigate how the performance of Morpher varies when the pre-training data and the target data have different statistical properties, such as node degree distributions or feature distributions. This analysis is essential for understanding the model's generalization capabilities.

W4. The domain transfer experiment only tests on limited datasets (MUTAG and PubMed), which share similar characteristics in molecular biology. It is unclear if the findings generalize to more diverse domains like social networks. The lack of experiments on datasets from different domains, such as social networks or citation networks, limits the generalizability of the conclusions. It is important to evaluate the model on datasets with varying graph structures and node feature types to assess its robustness.

W5. In the "Zero-Shot Classification Prototype" section, the zero-shot experiment relies on synthetic datasets (ZERO-Cora, ZERO-CiteSeer), which are generated by modifying features and labels and may fail to capture the complexity of natural data distributions. I wonder about Morpher’s generalization performance on real-world datasets. The artificial nature of these datasets raises concerns about whether the observed performance gains would translate to real-world scenarios where the data distributions are more complex and less controlled. The paper should include experiments on real-world zero-shot datasets to validate the model's effectiveness.

W6. The author mentions "Figure 5" in the text, though no such figure exists; it seems they meant to refer to "Table 4" instead.

W7. Some relevant works are missing, e.g., Killing Two Birds with One Stone: Cross-modal Reinforced Prompting for Graph and Language Tasks, KDD 2024.
Natural Language Is All a Graph Needs. arxiv. 2023

### Questions
Please refer to the above weaknesses.

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
5

### Summary
This paper proposes a new framework for integrating pre-trained GNNs with LLMs, leveraging the reasoning capabilities of LLMs alongside the structural representation advantages of GNNs. Specifically, the authors prompt both the LLM and the GNN with trainable parameters while keeping the parameters of both base modules frozen. This prompting, along with a cross-model projector, assists in aligning the embeddings produced by the GNN and the LLM for an input instance, such as a graph. Additionally, they introduce a variant of a current GNN prompting method that addresses its shortcomings through an attention mechanism.

### Strengths
- The proposed method does not involve training the base GNN or LLM, which reduces the number of parameters needed for training and enhances complexity and versatility.
- The authors reasonably justify the shortcomings of one current state-of-the-art model and propose modifications to mitigate its issues, empirically demonstrating the improvements achieved by these modifications.
- The main part of the prompting method, Morpher, is explained clearly with formulations, making it easy to understand.
- The authors provide sufficient and clear visualizations for their proposed methods.

### Weaknesses
 - The authors do not compare their work with state-of-the-art approaches that combine LLMs and GNNs, such as [1]
- While the authors claim to provide a theoretical analysis that "in many cases, state-of-the-art graph prompt is unable to learn good representations," this analysis is limited to Lemma 3.1. This lemma presents a trivial conclusion that does not significantly contribute to the development of the method or elaborate on the effectiveness of current prompting methods. It may be beneficial to remove this lemma and its proof, as it has been widely discussed in the literature on GNNs, and cite related works [2], which would help streamline the paper.
- In the Background section, few-shot prompt learning is only addressed in the context of methods that learn trainable parameters. It would be valuable to also discuss methods that do not train parameters, particularly regarding the intrinsic in-context learning of these methods.
- Some definitions and formulations appear extraneous. For instance, Equation 2 addresses concepts that are reiterated in Equation 6 and relate to matching dimensionality. The term $\tilde{h}$ does not appear in subsequent equations, and similarly, the introduction of $e^t$ in Equation 5 is later replaced by $e^t_{norm,i}$ without further context. Streamlining these sections could reduce unnecessary complexity.
- The authors do not discuss the inference process of their method at test time. It would be helpful to clarify whether the same model must be used at inference time and whether the LLM or the GNN makes the final prediction.
- The claim that this method is the first to address zero-shot classification for GNNs to unseen classes may overlook existing approaches. Referencing works such as [1] and [3] and comparing with them would provide necessary context.
- While the authors mention generating textual features from numerical features of the original datasets, it appears that for node classification datasets, only the labels of the nodes are converted to text, as indicated in Appendix B.2, rather than the node features themselves. Moreover, converting high-dimensional feature vectors to text features is not trivial and could exceed the acceptable input length for LLMs. This oversight may limit the model's generalizability to node/edge-level tasks due to the neglect of node features.


### Questions
- In Section 3, it is stated that the number of cross-connections is controlled to $n_e$ by thresholding. How are the best edges selected? Is this selection random, or is there a specific criterion?
- The objective function used for training Morpher does not incorporate labels or the task but focuses solely on aligning the prompting parameters for the GNN and LLM. This raises concerns about potential misalignment with pre-trained task-specific information, as merely aligning representations without consideration of the task could lead to forgetting previously learned knowledge. What is the rationale behind this objective function, and how does it mitigate this issue?
- Given that the objective function does not involve labels and the GNN and LLM have frozen parameters, how is the model evaluated in a few-shot setting with labels? Does this imply that the base GNN and LLM are pre-trained, with prompting applied afterward without using labels? If so, the contributions to domain transfer and zero-shot learning may be limited, as the fundamental learning from one domain to another occurs prior to prompting. The proposed method may primarily align representations of the LLM and GNN, which has already been explored in few-shot settings within a single domain.

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a multimodal prompt learning method called Morpher that uses both graph and text prompts to align graph representations with LLM’s semantic embeddings. This method is able to do zero-shot classification for unseen graph classes. In their paradigm, the pre-trained GNN and the LLM are kept frozen, making it much more efficient than finetuning. They also introduce an improved graph prompting method that cross-connections between the prompt graph and the input graph share the same density with the input graph. By using a projection layer and training with contrastive loss, they align the graph and text prompt embeddings in the same space, allowing for effective adaptation to various tasks with limited downstream data.

### Strengths
1. Morpher is able to adapt to various downstream tasks with limited labels. It is also able to do zero-shot classification on unseen classes.
2. They introduce an improved method of graph prompting without overwhelming or limiting the input graph's features.
3. The use of a contrastive loss function to align the graph and text embeddings helps bridge the gap between graph structure and semantic text features, enhancing the model's flexibility across modalities.

### Weaknesses
1. The effectiveness of Morpher relies on the availability and quality of semantic labels in the text associated with graph data. When these labels are noisy, incomplete, or inconsistent, the alignment might be weakened and the performance of downstream tasks might be reduced. Specifically, the method's performance could degrade significantly if the text labels do not accurately capture the underlying semantics of the graph data, or if there are ambiguities in the labeling process. This dependence on high-quality labels is a potential bottleneck for real-world applications where such labels are often difficult to obtain.
2. Freezing GNN and LLM reduces the number of trainable parameters, but it also limits adaptation flexibility. Certain tasks might require fine-tuning the GNN or LLM to capture task-specific information. For instance, if the pre-trained GNN was trained on a different type of graph data, its representations might not be optimal for the target task, and the inability to fine-tune it could hinder performance. Similarly, the LLM might not be well-suited for the specific nuances of the graph-related text, and freezing it prevents the model from learning task-specific language patterns.
3. The independently pre-trained GNN and LLM may cause huge representation gaps between the two modalities, causing difficulty in the alignment process. The initial feature spaces of the GNN and LLM could be vastly different, making it challenging for the projection layer and contrastive loss to effectively bridge this gap. This could lead to suboptimal alignment and limit the model's ability to transfer knowledge between the two modalities. The projection layer might not be sufficient to capture the complex non-linear relationships between graph and text embeddings.
4. Applying the graph prompting might be computationally expensive on large and complex graphs. While the improved method reduces the number of connections, the process of creating and processing prompt graphs, especially for very large graphs with many nodes and edges, could still pose a significant computational burden. This could limit the scalability of the method to large-scale graph datasets.

### Questions
1. How does different text labels affect the model performance? Does randomizing the class text label lead to comparable performance in few-shot setting? How fine-grained text can the model take? Will adding explanations to the text label help improve the performance?
2. Why does the test accuracy of zero-shot class decrease as the training epoch increases?
3. What’s the distribution of graph and text representation? Does there still exist domain shift after the alignment? Can you visualize the distributions of graph and text representations before and after alignment, using t-SNE or UMAP?

### Soundness
3

### Presentation
3

### Contribution
3

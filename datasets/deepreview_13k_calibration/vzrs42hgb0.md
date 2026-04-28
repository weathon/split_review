# DistillHGNN: A Knowledge Distillation Approach for High-Speed Hypergraph Neural Networks

- Decision: Accept
- Avg Score: 6.33
- Scores: 8, 6, 5

## Abstract
In this paper, we propose a novel framework to significantly enhance the inference speed and memory efficiency of Hypergraph Neural Networks (HGNNs) while preserving their high accuracy. Our approach utilizes an advanced teacher-student knowledge distillation strategy. The teacher model, consisting of an HGNN and a Multi-Layer Perceptron (MLP), not only produces soft labels but also transfers structural and high-order information to a lightweight Graph Convolutional Network (GCN) known as TinyGCN. This dual transfer mechanism enables the student model to effectively capture complex dependencies while benefiting from the faster inference and lower computational cost of the lightweight GCN. The student model is trained using both labeled data and soft labels provided by the teacher, with contrastive learning further ensuring that the student retains high-order relationships. This makes the proposed method efficient and suitable for real-time applications, achieving performance comparable to traditional HGNNs but with significantly reduced resource requirements.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposed DistillHGNN, a novel framework designed to improve the inference speed of Hypergraph Neural Networks (HGNNs) without sacrificing accuracy. DistillHGNN utilizes a teacher-student knowledge distillation approach, where the teacher model comprises an HGNN and a Multi-Layer Perceptron (MLP), while the student model, TinyGCN, is a lightweight Graph Convolutional Network (GCN) paired with an MLP. The framework incorporates a dual knowledge transfer mechanism, passing both soft labels and structural knowledge from the teacher to the student. Trained on labeled data and teacher-provided soft labels with contrastive learning to retain high-order relationships, DistillHGNN achieves performance comparable to traditional HGNNs with significantly lower resource requirements.

### Strengths
- The dual knowledge distillation approach (soft labels and high-order structural knowledge) effectively transfers complex relationships, addressing limitations found in existing methods.

- Comparative accuracy with minimal inference time.

- The paper is well structured and well written.

- The paper includes a thorough experimental setup, covering multiple datasets and evaluation metrics.

### Weaknesses
 - The authors claim the proposed approach is memory efficient everywhere in the paper. In line 416, they mention, "As illustrated in Figure 2, DistillHGNN maintains competitive inference times and memory efficiency without sacrificing accuracy"; however, Figure 2 shows accuracy vs. inference time. Moreover, no other evidence shows that the proposed approach is memory efficient. The paper needs to provide a quantitative comparison of memory usage, especially against other distillation methods like LightHGNN, GLNN, and KRD, which also employ lightweight MLPs during inference. The claim of memory efficiency requires empirical validation, not just an architectural argument, as these other methods also have minimal memory footprints due to their MLP-based inference. Without this data, the claim remains unsubstantiated.

- Among the previous works in knowledge distillation, the authors only compared with LightHGNN. Since the authors compared with GNN and GCN, the authors are suggested to compare with GNN and GCN-based distillation approaches as well. 


Minor:

- In line 152, the authors mention "Framework 1". Since there is no Framework 1 in the paper, I suppose it should be "Figure 1".

- The caption for Figure 1 is too big. The authors should keep it concise and incorporate the details into the actual text of Section 3. Also, the authors didn't mention what happens with the soft labels after they are generated from the teacher model in the caption.

### Questions
- Figure 2 shows comparisons of models based on accuracy and inference time. Does that mean accuracy and inference time are dependent on each other? If not, these graphs create confusion. Currently, from the graphs it seems that if the inference time is longer, the accuracy could be higher, and vice versa. If this is not the case, I suggest keeping inference time separate from accuracy.

- Line 669 of Algorithm 1 states, "Update teacher model parameters via backpropagation". Typically, knowledge distillation keeps the teacher fixed once pre-trained, so if this algorithm intends otherwise, the authors should provide a justification.

- In Figure 6, can the authors keep the range of accuracy axis the same for all the graphs? It would be easier to visualize the differences. 

- It would be interesting to see how an adaptive knowledge distillation approach performs compared to the proposed fixed distillation approach. For instance, the model could prioritize contrastive learning for highly connected hypergraphs to capture complex relationships and rely more on soft labels for simpler ones to reduce model complexity even further.

### Soundness
2

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
5

### Summary
This paper introduces DistillHGNN, a novel knowledge distillation framework designed to enhance the inference speed and memory efficiency of Hypergraph Neural Networks (HGNNs) while maintaining high accuracy. DistillHGNN employs a teacher-student model where the teacher consists of an HGNN and a Multi-Layer Perceptron (MLP) that generates soft labels. The student model uses a lightweight Graph Convolutional Network (TinyGCN) paired with an MLP, optimized for faster online predictions. Additionally, contrastive learning is utilized to transfer high-order and structural knowledge from the HGNN to the TinyGCN. Experimental results on various real-world datasets demonstrate that DistillHGNN significantly reduces inference time and achieves accuracy comparable to or better than state-of-the-art methods like LightHGNN.

### Strengths
1. The proposed method combines knowledge distillation with contrastive learning in an innovative way, allowing for a more comprehensive transfer of both soft labels and high-order structural knowledge from the complex HGNN to the lightweight TinyGCN. This dual transfer mechanism enhances the student model's ability to capture intricate dependencies while maintaining computational efficiency.
2. The experimental evaluation is thorough and spans multiple real-world datasets, including CC-Citeseer, CC-Cora, IMDB-AW, and various DBLP datasets. The results consistently demonstrate that DistillHGNN achieves a favorable balance between accuracy and inference speed, often outperforming existing methods such as LightHGNN in both metrics.
3. The paper is well-structured and provides a clear and detailed explanation of the methodology, including the architecture of both the teacher and student models, the training process, and the loss functions used. This clarity facilitates understanding and potential replication of the proposed framework.

### Weaknesses
1. The method involves converting a hypergraph to a homogeneous graph, which can lead to the loss of high-order structural information inherent in hypergraphs. While contrastive learning helps mitigate this issue, the paper does not sufficiently address how the conversion process preserves the complex relationships that hypergraphs naturally capture. Specifically, the conversion to a simple adjacency matrix, $A = \mathcal{H}W\mathcal{H}^T - D_v$, where $\mathcal{H}$ is the hypergraph incidence matrix, $W$ is a diagonal weight matrix, and $D_v$ is the degree matrix, inherently flattens the higher-order interactions into pairwise relationships. This transformation may not fully retain the nuanced group relationships present in the original hypergraph, potentially limiting the model's ability to learn complex dependencies.

2. DistillHGNN relies on homogeneous graphs during the inference phase, which poses a significant limitation for inductive learning scenarios. When new samples are introduced, the need to reconstruct the graph and perform complex preprocessing steps can result in increased computational and time costs, limiting the model's applicability in dynamic or real-time environments. The process of recomputing the adjacency matrix $A$ for each new node or set of nodes requires recalculating the entire graph structure, which is computationally expensive and impractical for large-scale dynamic graphs. This limitation is particularly problematic in scenarios where the graph structure evolves frequently.

3. The evaluation is primarily conducted on datasets related to academic papers and movie databases. There is a lack of assessment on larger-scale or synthetic datasets, which raises concerns about the method’s scalability and generalizability to other domains or more complex real-world applications. The datasets used, such as CC-Citeseer, CC-Cora, and IMDB-AW, are relatively small and may not fully represent the challenges posed by larger, more complex hypergraphs. Testing the method on synthetic datasets with varying sizes and structures would provide a more comprehensive understanding of its scalability and robustness.

4. The selection of baseline methods, while covering traditional GNNs and some knowledge distillation approaches, does not include more recent or advanced hypergraph neural network models. This omission may limit the understanding of DistillHGNN's relative performance against the latest state-of-the-art techniques. Specifically, the paper lacks a comparison against other recent HGNN models that may employ different aggregation or attention mechanisms, which could provide a more nuanced evaluation of the proposed method's strengths and weaknesses.

### Questions
1. The proposed method converts a hypergraph into a homogeneous graph, potentially leading to the loss of high-order structural information. How do you address this information loss, and can you incorporate mechanisms similar to LightHGNN’s high-order soft-target constraints to better preserve high-order knowledge? Additionally, could you provide visualizations to enhance the interpretability of your method?
2. Since DistillHGNN depends on homogeneous graphs during inference, how does it handle inductive learning scenarios where new samples are added? Specifically, what strategies do you propose to minimize the need for graph reconstruction and complex preprocessing steps in such cases?
3. The experimental evaluation primarily focuses on datasets from academic papers and movie databases. Do you have plans to evaluate DistillHGNN on larger-scale or synthetic datasets to demonstrate its scalability and effectiveness across a broader range of applications?
4. Could you provide more technical details and visualizations regarding how contrastive learning and soft labels facilitate the transfer of high-order knowledge from the teacher model to the student model? This would help in better understanding the mechanisms behind knowledge preservation and transfer.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes **DistillHGNN**, a knowledge distillation framework designed to accelerate the inference of hypergraph neural networks (HGNNs) while maintaining their high accuracy. DistillHGNN leverages a teacher-student structure where the teacher model, an HGNN, captures complex relationships within hypergraphs and generates soft labels. The student model, a simplified TinyGCN, learns from these soft labels and employs contrastive learning to capture high-order structural knowledge.

### Strengths
1. The dual use of soft labels and structural knowledge distillation through contrastive learning enhances the capability of the student model, addressing limitations of previous distillation methods.
2. DistillHGNN achieves significant reductions in inference time (up to 80%) compared to traditional HGNNs, making it suitable for real-time applications.

### Weaknesses
1. **(Minor)** The writing could be improved for clarity and simplicity. For instance, the caption in Figure 1 (lines 175–188) could be condensed to improve readability, ideally to half its current length. If extensive detail is necessary, consider moving some information to the main text.
2. **(Minor)** The paper could use `\citet{}` for citations when referring to the authors directly. For example, in lines 280–281, instead of "Multilayer Perceptron (MLP) by \cite{author2020}," using `\citet{}` could enhance readability.
3. When mentioning the use of six popular datasets, it would be helpful to list the features and characteristics of each dataset to provide more context for the experiments. For instance, some datasets may have dense connections while others are sparse; some may benefit more from heterogeneous graphs compared to homogeneous ones. Without a detailed explanation of the datasets' biases or inductive properties, understanding the generalization of the proposed method becomes challenging.
4. **Scalability**: The scalability of the proposed method is unclear. According to Table 3, all datasets used in the experiments are relatively small, with node counts between 3k and 6k, similar in scale to the Cora dataset. It would be beneficial to provide insights on how the method scales to larger datasets, such as ogbn-arxiv or ogbn-products, if they have hypergraph structures.

### Questions
See Weaknesses part

### Soundness
2

### Presentation
2

### Contribution
2

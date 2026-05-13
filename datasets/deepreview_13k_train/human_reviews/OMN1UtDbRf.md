# KD-HGRL: Knowledge Distillation for Multi-Task Heterogeneous Graph Representation Learning

- Decision: Reject
- Scores: 3, 5, 3, 5, 5

## Abstract
Heterogeneous graphs, characterized by diverse node and edge types, are central to many real-world applications, including social networks, biological systems, and recommendation engines. While Graph Neural Networks (GNNs) are effective for graph representation learning, their reliance on extensive labeled data, high computational cost, and long inference times limit scalability, especially for heterogeneous graphs. To address these challenges, we propose KD-HGRL, which leverages \textbf{K}nowledge \textbf{D}istillation for multi-task \textbf{H}eterogenous \textbf{G}raph \textbf{R}epresentation \textbf{L}earning. KD-HGRL uses self-supervised contrastive learning across semantic and topological views to generate robust, label-free node embeddings in the teacher phase. These embeddings are distilled into a lightweight student model, enabling efficient task-specific outputs such as node classification and link prediction with significantly reduced inference time. Experiments on benchmark datasets demonstrate KD-HGRL’s superior performance and efficiency compared to state-of-the-art methods. The framework captures both local and global graph structures, eliminates the need for labeled data, and scales effectively to large graphs. Key novelties, such as a multi-view teacher model, contrastive alignment, and a lightweight student model, make KD-HGRL a versatile and efficient solution for heterogeneous graph representation learning.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a novel knowledge distillation framework called KD-HGRL for heterogeneous graph representation learning, consisting of a teacher model and a student model. The teacher model uses self-supervised contrastive learning with the semantic view and the topological view, while the student model learn the knowledge distillated by the teacher model.

### Strengths
1. This paper proposed to capture topological and semantic information of nodes.
2. The experimental results show that the proposed method outperform all baseline methods across multiple datasets in two tasks.

### Weaknesses
1. There are many typos in the paper.
- Please add the whitespace between the text and the corresponding citation.
- What is the $L_{supervised}$ in equation 17? Should it be $L_{bpr}$?
- In equation 10, the objective function is the summation over N different nodes. However, in figure 1, the objective function is the summation over C different node types. The authors should correct the mismatch between these two objective functions.
- In equation 16,  $Z_v^{s}td$ should be $Z_v^{std}$, $Z_v^{t}ch$ should be $Z_v^{tch}$, $Z_v^{s}$ should be $Z_v^{std}$ and $Z_v^{t}$ should be $Z_v^{tch}$.

2. The motivation of this paper is not appealing. Many existing methods have shown the great performance in the limited label scenarios. Besides, the pretrained models aims to address this issue. What's the advantage of the proposed method over the existing methods?

3. In the experiment, it's better to highlight the method with the best performance.

4. In the introduction, the authors mention that of main issue of current supervised learning method is that their performance is highly dependent on having access to large amounts of labeled data, which is the key motivation of the proposed method. However, in both node classification and link prediction task in the experiment, the training datasets is 60% (80%), which cannot reflect the performance of the proposed method in the limited label scenario. It's recommended to conduct the experiments in a limited label scenario, e.g. 5% or 1% labeled nodes in node classification problem.

5. What's the time complexity of the proposed method compared with the baseline methods?

### Questions
1. What is the input node feature for the student model? What is the $Z_j$ in equation 11?

2. What's the meaning of the second term in equation 13? Can you further explain on this term? 

3. Why do you incorporate the representation learned by teacher model in the final prediction in equation 14? If so, what's the point of distilling the knowledge from teacher model to student model? Why don't you just train the teacher model for the downstream task? Could you provide the intuition and the reason for that? In addition, in the summarization of contribution, the authors mention that the knowledge distillation mechanism balances performance and computational efficiency. If teacher model is used for final prediction, then how do you ensure the computational efficiency?

### Soundness
3

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
The paper proposes a framework for self-supervised learning on heterogeneous graphs. The self-supervised learning is based on node-level contrastive learning. The paper also proposes to utilize knowledge distillation to transfer the knowledge from the large pre-trained graph model. The framework is tested on node-level tasks, namely node classification and link prediction. Experimental results are promising for the proposed framework in comparison with the baseline models.

### Strengths
- Good presentation and readability
- Promising experimental results on node-level tasks

### Weaknesses
 - Unclear experimental design: the key in knowledge distillation is to transfer knowledge from large GNNs to smaller GNNs. In the experiments, the authors do not provide the size comparison between the teacher and student models. When comparing with the baseline models, it is also essential to show that smaller GNN models with transferred knowledge can outperform the other baseline GNN models with the same parameter scale. Specifically, the paper lacks a detailed analysis of the parameter counts for both the teacher and student models, and how these relate to the performance gains observed. It is crucial to demonstrate that the performance improvement is not simply due to a larger model size, but rather due to the effectiveness of knowledge transfer. A comparison of model sizes and computational costs alongside performance metrics is needed to validate the efficiency of the proposed approach.
- Only node-level tasks are evaluated: general graph structural knowledge is expected to benefit both graph-level and node-level tasks. Both the framework and the experiments seem to focus only on node-level knowledge. The paper does not explore how the learned representations could be leveraged for graph-level tasks such as graph classification or graph regression. The current evaluation limits the scope of the proposed framework, as it's unclear whether the learned representations are truly capturing generalizable graph knowledge or are merely optimized for node-level tasks. The lack of evaluation on graph-level tasks is a significant limitation, given the potential of the framework to learn more holistic graph representations.
- Lack of novelty: graph contrastive learning is widely adopted as a self-supervised task and there exist many similar prior works (e.g., [1]). The proposed framework does not introduce a fundamentally innovative self-supervised graph learning task and is mainly a combination of several previous graph self-supervised techniques. The contributions are more from the engineering perspective rather than the research perspective. The combination of contrastive learning and knowledge distillation, while potentially effective, is not a novel concept in itself. The paper needs to clearly articulate what specific aspect of their approach is novel and how it differs from existing methods, beyond a simple combination of known techniques. The current presentation does not adequately highlight the unique contributions of this work.

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The KD-HGRL employs knowledge distillation for multi-task heterogeneous graph representation learning. The teacher model generates node embeddings via self-supervised learning by incorporating both semantic and topological views. Then, knowledge is transferred from the teacher to the lighter weight student model. The framework improves performance on downstream tasks like node classification and link prediction.

### Strengths
Experiments on real-world benchmarks show that KD-HGRL outperforms current state-of-the-art methods.

### Weaknesses
The discussion surrounding the novelties of the proposed method is insufficient, and the distinctions between this work and existing methodologies remain unclear. While the concept of learning node embeddings from dual views is acknowledged in the literature, it lacks originality in this context. Additionally, the utilization of teacher-student models and knowledge distillation to transfer knowledge from a pretrained teacher model to a student model is not a new contribution. This technique has been well-established in graph representation learning for several years (e.g., [R1]) and has been applied recently to heterogeneous graphs as demonstrated in works such as [R2, R3, R4]. A more thorough exploration of the unique contributions of the proposed method in relation to these established approaches would enhance the clarity and impact of the submission.

2- It is not clear how the authors select the value of hyperparameters \alpha, \gamma, \lambda_1, \lambda_2

### Questions
1- What is the primary contribution of this work that distinguishes it from existing literature?

2- What methodology is employed to determine the hyperparameter settings?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper proposed a two-stage graph learning framework for heterogeneous graphs. In the first stage, the teacher model is pre-trained in SSL and the representations from two views will be learned for contrastive learning. Then the knowledge learned by the teacher model will be transferred to the student model with knowledge distillation for downstream tasks.

### Strengths
1. The proposed method achieves best performance compared with the baselines reported in the experiments, showing its effectiveness. 

2. Overall, the paper clearly presents the proposed method and the conducted experiments.

### Weaknesses
1. Since the proposed method includes the pre-training (teacher) stage, some self-supervised learning-based methods proposed for heterogeneous graphs should be compared in the experiments, like MVSE[1] and HGMAE[2]. Specifically, the comparison should not only focus on the final performance but also on the effectiveness of the pre-training stage itself. For example, how does the representation quality of the teacher model compare to those obtained by MVSE or HGMAE when evaluated on downstream tasks without distillation?

2. It seems the performance improvements are mainly brought by extra training stage, views and distillation process, the authors should provide complexity analysis in the paper to show if the sacrificed efficiency is worthwhile. The analysis should include not only the time complexity but also the space complexity, especially considering the memory overhead of maintaining two views and the class centroid representations. A detailed breakdown of the computational cost of each stage (pre-training, distillation, fine-tuning) would be beneficial.

3. The effectiveness of some designs in the paper is not very clear, like the incorporation of two views in the pre-training and the class centroid representations. The authors should conduct a more comprehensive ablation study to demonstrate the effectiveness of the components in the framework. For example, what is the performance when only one view is used in pre-training? How does the performance change when the class centroid representations are not used? It is also unclear how the two views are generated and whether they capture complementary information.

4. It is not clear how the hyper-parameters ($\alpha$, $\lambda$) are set in this work and their impacts on the final performance. The authors should provide a sensitivity analysis of these hyper-parameters and explain how they were tuned. It is important to understand how the performance changes with different values of these parameters and whether the reported results are robust to hyper-parameter variations.

5.	In line 292, the authors mention that a homogeneous graph is generated for the target graph, however, it is still not clear how the homogeneous graph is built. Does the graph build on a specific relation (meta-path) and why? The authors should provide a detailed explanation of the homogeneous graph construction process, including the specific relation or meta-path used and the rationale behind this choice. It is also unclear how the node features are handled in the homogeneous graph.

### Questions
Please refer to the question section.

### Soundness
2

### Presentation
2

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
This paper proposes a Knowledge Distillation Framework for Heterogeneous Graph Representation Learning (KD-HGRL) for node classification and link prediction tasks. The framework contains two phases: teacher and student. The teacher phase uses self-supervised comparative learning to learn graph node embeddings from both semantic and topological perspectives. The student phase passes these representations to a lightweight combined GCN and MLP model, which enhances the performance of the student model through knowledge distillation to supervise the loss to accomplish a specific task. The approach improves the performance of the student model in node classification and link prediction tasks.

### Strengths
1. Developed a novel knowledge distillation framework (KD-HGRL) tailored for heterogeneous graph representation learning, focusing on tasks like node classification and link prediction.
2. Integrates both local and global information to improve task-specific performance on node classification and link prediction.
3. Combines embeddings from a node and its class-specific neighbors, leveraging both self-supervised and supervised learning, to enhance the student's performance across heterogeneous graph tasks.

### Weaknesses
1. The need to employ knowledge distillation on reisomorphic maps is not presented clearly. Specifically, the paper does not adequately explain why mapping the teacher's embeddings to task-specific subgraphs in the student model via isomorphic maps is necessary or beneficial compared to other methods of knowledge transfer. The motivation for using isomorphic maps in this context is not well-established, and the paper lacks a clear explanation of the advantages this approach provides.
2. Although the student model implements a lightweight design, the computational overhead of the teacher model is not analyzed. The paper does not provide a detailed analysis of the computational cost associated with the teacher model, particularly during the pre-training phase. This lack of analysis makes it difficult to assess the overall efficiency of the proposed framework, especially when considering the computational resources required for the teacher model.
3. The authors claim that the proposed method can be better applied to large datasets, but there are no relevant experiments to prove it. The paper lacks empirical evidence demonstrating the scalability of the proposed method on large-scale heterogeneous graph datasets. The absence of experiments on datasets with varying sizes and complexities makes it difficult to validate the claim that the method is well-suited for large datasets. The experimental evaluation should include a wider range of datasets to support this claim.
4. Some of the diagrams in the paper are too scribbled to affect the reader's perception, such as Figures 2, 3. The visual quality of Figures 2 and 3 is poor, making it difficult for the reader to understand the proposed framework. The lack of clarity in these figures hinders the comprehension of the methodology.
5. Some of the writing in the text is problematic, such as line 412. The writing in the paper is not always clear and concise, with specific instances, such as line 412, where the language is problematic. This lack of clarity affects the overall readability and understanding of the paper.

### Questions
1. Existing methods on heterogeneous graphs already handle the node classification task well, what is the need to use knowledge distillation on heterogeneous graphs.
2. The paper claims that lightweight can be achieved through knowledge distillation, but no experimental verification is provided.
3. How to ensure that comparative learning under both views in the teacher phase does not weaken the complementary information of each of the semantic and topological views.
4. The experimental setup of the article does not cover all datasets for example lack of ablation experiments on Freebase and AMiner datasets.

### Soundness
2

### Presentation
2

### Contribution
2

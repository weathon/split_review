# New recipes for graph anomaly detection: Forward diffusion dynamics and graph generation

- Decision: Reject
- Scores: 5, 5, 5, 6, 5, 5

## Abstract
Distinguishing atypical nodes in a graph, which is known as graph anomaly detection, is more crucial than the generic node classification in real applications, such as fraud and spam detection. However, the lack of prior knowledge about anomalies and the extremely class-imbalanced data pose formidable challenges in learning the distributions of normal nodes and anomalies, which serves as the foundation of the state of the arts. We introduce a novel paradigm (first recipe) for detecting graph anomalies, stemming from our empirical and rigorous analysis of the significantly distinct evolving patterns between anomalies and normal nodes when scheduled noise is injected into the node attributes, referred to as the forward diffusion process. Rather than modeling the data distribution, we present three non-GNN methods to capture the evolving patterns and achieve promising results on six widely-used datasets, while mitigating the oversmoothing limitation and shallow architecture of GNN methods. We further investigate the generative power of denoising diffusion models to synthesize training samples that align with the original graph semantics (second recipe). In particular, we derive two principles for designing the denoising neural network and generating graphs. With our proposed graph generation method, we attain record-breaking performance while our generated graphs are also capable of enhancing the results of existing methods. All the code and data are available at \url{https://github.com/DiffAD/DiffAD}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors investigate the behaviors of normal and anomalous nodes in a diffusion process. The authors made two observations that may help design new algorithms for supervised/semi-supervised anomaly detection. The first observation leads to algorithms that are capable of capturing local information in egonet. The second observation leads to the generation of additional graphs based on the diffusion process that can be utilized as auxiliary data to enhance the anomaly detectors. The authors then demonstrate the benefit of the models compared with baselines on several public datasets.

### Strengths
Strengths:
- The authors present an interesting analysis of the diffusion process on a graph.
- The proposed approach based on the two observations is also interesting. 
- The first observation leads to three non-GNN methods for anomaly detection in graphs.
- The second observation leads to a graph generation technique that can help improve the performance of anomaly detectors.
- The authors demonstrate the benefit of the models against several GNN baselines.
- The graph generation procedure can be used to enhance many other GNN models with a slight modification of the training objective.

### Weaknesses
I have a few concerns and questions regarding the paper:
1) One of my biggest concerns about this paper is its clarity of presentation. The paper is hard to understand. One factor is that the authors did not describe enough about how the diffusion process works on graphs. Section 3.2 only explains the generic diffusion process on regular data (x). How it applies in the context of graphs, which contain structure and attributes, is not clearly explained. After explaining Section 3.2, the authors directly jump to the graph observations without explaining how the diffusion process on graphs works.
2) Since the authors did not clearly explain the diffusion process on graphs, many questions may arise about this, such as:
    - How does the structure of the graph (A) contribute to the next node feature representation (X_{t+1})?
    - Any effect of the neighboring node on a particular node representation in the next step?
    - The diffusion process itself tries to model the data distribution, i.e., for graph cases, it models the data distribution of G={A, X}. As the first approach utilizes the diffusion information, why do the authors claim that the approach does not need to learn P(A, X)?
    - And more questions that depend on the answer to the questions above.
3) The principle derived from the first observation is not surprising, i.e., "The denoising neural network should be capable of capturing the local information in egonets". In fact, I would argue that this principle is the bedrock of nearly all graph anomaly detection models.  
4) The baselines used in the experiments are relatively inadequate, particularly in the second group. I would suggest the authors to add more baselines in the comparisons, such as:
    - GHRN [1]
    - GDN [2]
    - H2-FDetector [3]
    - GAGA [4]
    - etc.

### Questions
Please answer my questions in the previous section.

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a model for anomaly detection in graphs, particularly "contextual" anomalies, which are nodes whose attributes are significantly different from neighboring nodes. The main proposed idea is to use a denoising diffusion probabilistic model (DDPM) to learn a distribution of the graph that can be used to add/remove noise and generate synthetic graphs. The authors then use the DDPM in 2 different ways. First, they combine it with an LSTM to learn to classify nodes in a sequence of increasingly noise graphs as anomalous or normal. Second, they use the DDPM to generate synthetic graphs that can be used to improve predictive performance of other previously proposed models for anomaly detection on graphs.

### Strengths
- Using a DDPM to model noise in a graph is interesting and avoids issues with over-smoothing when using graph neural networks for anomaly detection
- Preliminary study is insightful and effective at motivating the proposed methods

### Weaknesses
 - Limited experimental evaluation. No discussion of ablation or hyperparameter turning.
- No comparison to recently-proposed methods for graph anomaly detection, such as CoLA or CONAD. The justification is that such methods are not classifiers and the just assign an "anomaly score" to nodes. However, one could try a simple baseline of thresholding this anomaly score.
- No discussion of running time
- No discussion of inference for the DDPM

### Questions
1. Would it be possible to compare the proposed method to contrastive detectors by applying a threshold?
2. How is the inference for the DDPM performed?
3. What is the computational complexity of the proposed method as a whole?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the application of the forward (add noise) and backward (denoise) processes of the diffusion model to graph anomaly detection, respectively. During forward diffusion, the authors exploited the more significant egonet dissimilarity change of the anomalies and proposed the use of LSTM/Transformer/MLP to capture this change information and perform anomaly detection. During backward diffusion, the authors proposed a graph generation method that recovers low-frequency energy as a data augmentation. Theoretical analyses and comprehensive experiments are performed.

### Strengths
1. The paper is well written and the charts are professional.

2. The exploration experiment is very detailed and the two propositions are well illustrated.

3. Substantial theoretical analyses and experimental results are provided.

### Weaknesses
1.  The paper's focus on a limited type of anomaly (contextual anomaly).

2.  While the analysis of the forward diffusion process is well-done, the proposed method (Approach I) lacks sufficient evidence to demonstrate its superiority.

3.  The experiments presented in the paper have some shortcomings that should be addressed.

### Questions
1.  The primary focus of this paper is on contextual anomalies that exhibit marked differences from their neighbors. However, it raises concerns about the representativeness of such anomalies in real-world diverse datasets. This could limit the applicability of the proposed approach. To address this, expanding the experimental evaluation to real datasets[1] would enhance the paper's contributions.

2.  While it is intuitive that adding noise would lead to a rapid drop in egonet dissimilarity for anomalies, it raises questions about whether complex methods in Approach I are necessary for anomaly detection. At the initial stages, the egonet dissimilarity of anomalies significantly outweighs that of normal instances as illustrated in Fig.2. Therefore, it's worth considering if exploiting this difference directly could lead to more efficient detection.

3.  The experimental results in Table 1 highlight that Propositions 1-based methods (FSC, TRC) often fail to outperform baseline approaches on multiple datasets. This further emphasizes the need to scrutinize the necessity and validity of Approach I.

4.  Concerning loss function (Eq. 22), it's vital to ensure that the nodes in the graph $G_a$ generated using denoising techniques align with the class of the original graph $G$. Any inconsistencies could lead to conflicting optimization. Specifically, for an anomaly $v_i$ in graph $G$, how to ensure the generated corresponding node $v_i$ in $G_a$ is also an anomaly?

5.  Although unsupervised methods cannot make use of label information, many of them [2][3] also leverage local inconsistencies for anomaly detection. Providing a comparative analysis against these existing methods would help establish DIFFAD's superiority effectively.

6. The proposed method looks a bit complicated and it would be nice to have comparisons in terms of complexity and computational efficiency.


[1] GADBench: Revisiting and Benchmarking Supervised Graph Anomaly Detection(arxiv, 2023)

[2] Anomaly detection on attributed networks via contrastive self-supervised learning(, 2021)

[3] Reconstruction Enhanced Multi-View Contrastive Learning for Anomaly Detection on Attributed Networks (IJCAI 2022)

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a DiffAD, which is a DDPM-based anomaly detector to detect anomalous nodes in a graph that does not need to learn the data distribution explicitly to detect anomalies. The proposed model first learns the diffusion dynamics of ego-net dissimilarities of diffusion steps and then generates auxiliary training samples to enhance a detector's performance. The empirical results on six real-world datasets illustrate the effectiveness of the proposed model.

### Strengths
1. The paper provides evidence on the reason why the forward and denoised processes are designed. 
2. The empirical results are very promising, DiffAD outperforms SOTA  by a large margin.
3. The loss function can resolve the class imbalance in anomaly datasets.

### Weaknesses
1. The definition of 'ego-net dissimilarity` is actually a GNN embedding in literature, so 'dissimilarity` is an inaccurate word. The paper uses the term to describe the difference between a node's attributes and its neighbors, which is essentially a form of node embedding derived from local graph structure. This is not a novel concept and should be framed more accurately within the context of existing GNN literature.
2. The time complexity should be very high due to the nature of the transformer and DDPM. The transformer's self-attention mechanism scales quadratically with the number of nodes, and the iterative denoising process of DDPM also introduces significant computational overhead. The paper should provide a more detailed analysis of the computational cost, including both training and inference times, and discuss potential bottlenecks.
3. The motivation is to learn to classify anomalies and normal nodes by not explicitly learning the data distribution,  therefore you propose to learn from the trajectories produced by the forward process. I don't see a strong motivation for data generation for detectors. The paper's approach of generating auxiliary training samples seems disconnected from the core idea of learning diffusion dynamics for anomaly detection. The connection between the generated samples and the actual anomaly detection task is not clearly established.
4. The training process for the whole is not clear. The paper lacks a clear, step-by-step explanation of how the different components of the model (the transformer, the diffusion model, and the anomaly detector) are trained together. The interaction and dependencies between these components are not well-defined, making it difficult to understand the overall training procedure.
5.  DiffAD still needs sufficient data in order to train the model while anomalous nodes are usually very few. The paper acknowledges that the model requires sufficient training data, but it does not adequately address the inherent challenge of anomaly detection, where labeled anomalies are scarce. The proposed method relies on generating auxiliary data, but it is unclear how effective this approach is when the initial labeled data is extremely limited.

### Questions
1. How do you train the overall DDPM model?
2. Why does the forward process need a separate loss function that utilizes the label information?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes denoising diffusion and graph generative models for detecting graph anomalies. The denoising diffusion model learns to reconstruct the original graph from noisy samples, while the graph generative model learns to generate new graphs that align with the original graph semantics. The authors evaluate the proposed methods on six datasets and compare them with several state-of-the-art methods, showing promising results in terms of detection accuracy, precision, recall, and AUC. Overall, this paper presents valuable contributions to the field of graph anomaly detection, with potential applications in various domains.

### Strengths
1. the authors of this paper present their proposed methods and results in a clear and organized manner, and they provide a thorough discussion of related work and future research directions.

2. Authors integrate graph diffusion into the GAD task to address the challenges of limited prior information about anomalous nodes by generating more training samples.

### Weaknesses
1. Graph anomaly detection often includes two types: attribute anomalies and structural anomalies. The author disrupts the original distribution by continuously injecting noise, which may be useful for detecting attribute anomalies. However, is this also effective for detecting structural anomalies? Specifically, the method's reliance on attribute diffusion might not adequately capture deviations in graph topology, which are crucial for identifying structural anomalies. For instance, consider a scenario where an anomalous node is characterized by its unusual connections rather than its attribute values; the proposed diffusion process may not sufficiently highlight this type of anomaly.

2.  when injecting scheduled noise to node attributes as the forward diffusion process, anomalies’ egonet dissimilarities change more dramatically than normal nodes, Please provide a clear explanation for this phenomenon.   To calculate egonet dissimilarities, you utilize the formula: LX, which is a graph convolution operation without learnable parameters, why LX can be egonet dissimilarities? The explanation of why $LX$ represents egonet dissimilarity is not sufficiently clear. While the formula involves the Laplacian matrix and node features, it's not immediately obvious why this operation captures the difference between a node's attributes and its neighbors' attributes. A more detailed explanation, perhaps with a breakdown of how the Laplacian matrix affects the feature vectors, would be beneficial.

### Questions
1. Why are the results of the baseline methods you listed far lower than those reported in their paper？ For example, GCN\ GAT \GraphSage on Cora\ACM datasets

2. baselines are too few to demonstrate the superiority of your method,  you should choose some famous GAD methods, such as COLA,  SL-GAD rather than GCN GAT, etc

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper investigates the problem of graph anomaly detection in a semi-supervised setting where anomalous nodes tend to differ from their neighbors in terms of the distribution of node features (not structural differences). Under the assumption that the mean attribute values are the same across anomalous and non-anomalous nodes, the authors prove that in a step-wise diffusion process that adds incremental noise to the attribute matrix X, the egonet dissimilarity $\Omega = LX$ for nodes that have higher variance attributes will change more drastically than for those which have lower variance. Based on this observation, the authors propose (non-GNN) neural models that learn from the sequence of egonet dissimilarities to detect anomalies. Moreover, they prove that the relative accumulated energy present in low frequency signals decreases as X gets increasingly corrupted. In light of this observation, they propose a denoising network that utilizes one GCN (low-pass filter) per step. This allows them to generate additional attribute vectors for each node based on their fully-corrupted counterparts. The proposed model, DiffAD, is evaluated on six datasets w.r.t. Macro-F1 and AUC and compared with four graph anomaly detection baselines. In another set of experiments, they show that the generated attribute matrices X bring the performance of GraphSAGE very close to that of DiffAD.

### Strengths
S1. Proposes an alternative to GNN-based solutions for detecting anomalous nodes in a graph (which has applications related to spam and fraud detection).

S2. Proposed method, DiffAD, outperforms recent baselines on six datasets.

S3. Proposed graph generation technique leads to substantial performance improvements when used for training classic GNN methods.

S4. The proposed approaches are designed based on the theoretical principles proven in the paper.

S5. The overall writing quality is great, the text is easy to follow and the appendices are used in a thoughtful way.

S6. Overall reproducibility is high; code is also provided (in an anonymous github repo).

### Weaknesses
W1. In the preliminary study setup, the attribute distribution chosen for anomalous nodes is substantially different from that of the normal nodes. When noise is incrementally added through diffusion steps, it is not surprising that the egonet dissimilarity drops faster for anomalous nodes. This setup, while following prior work, may not accurately reflect real-world anomaly scenarios where the distinction between normal and anomalous node attributes might be more subtle, leading to an overestimation of the method's effectiveness in practice.

W2. The authors show that this rapid egonet dissimilarity decrease holds for CORA dataset, but the anomalies in the data were synthetically injected by Liu et al., 2022. For organic anomalies, this assumption might also be true on average (Liu et al., 2022), but the fact that DiffAD  does not account for structural anomalies will likely prevent it from detecting anomalies if their initial egonet dissimilarity is low. The reliance on attribute variance changes may limit the method's ability to detect anomalies that primarily manifest through structural deviations rather than attribute differences, especially if those structural anomalies do not also exhibit significant attribute variance changes.

W3. It is not clear how to extend these principles to consider for structural anomalies. The paper dismisses the need to consider structural anomalies that "form more densely [connected] links with other nodes", but there could be anomalies that also keep the density somewhat unchanged. The method's current focus on attribute-based anomalies neglects the possibility of structural anomalies that do not necessarily alter the local density, such as nodes bridging distinct communities or forming unique subgraphs, which are common in real-world scenarios.

W4. Some potential typos; some word choices can be improved.

### Questions
Q1. Is Observation I an expected result? If so, why?

Q2. A fundamental question not addressed by the paper is: what is the anomaly detection performance on anomalous nodes whose initial ego dissimilarity is low?

Q3. Is it possible to extend the diffusion model to a case where A is changed over time?

Q4. Please clarify:
- In Eq. (18), should one of the $Z_t$ in the concatenation of the first GCN layer be $\bar Z_t$?
- In Eq. (4), specify that this is the accumulated energy ration at rank $l$
- p.2: Confronting -> Adhering to the principles
- p.5: Eventual -> Eventually

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

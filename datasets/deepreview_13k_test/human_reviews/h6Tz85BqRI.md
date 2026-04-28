# VQGraph: Rethinking Graph Representation Space for Bridging GNNs and MLPs

- Decision: Accept
- Scores: 5, 6, 8, 8, 5

## Abstract
GNN-to-MLP distillation aims to utilize knowledge distillation (KD) to learn computationally-efficient multi-layer perceptron (student MLP) on graph data by mimicking the output representations of teacher GNN. 
Existing methods mainly make the MLP to mimic the GNN predictions over a few class labels.
However, the class space may not be expressive enough for covering numerous diverse local graph structures, thus limiting the performance of knowledge transfer from GNN to MLP. 
To address this issue, we propose to learn a new powerful graph representation space by directly labeling nodes' diverse local structures for GNN-to-MLP distillation.
Specifically, we propose a variant of VQ-VAE \citep{van2017neural} to learn a structure-aware tokenizer on graph data that can encode each node's local substructure as a discrete code.
The discrete codes constitute a \textit{codebook} as a new graph representation space that is able to identify different local graph structures of nodes with the corresponding code indices.
Then, based on the learned codebook, we propose a new distillation target, namely \textit{soft code assignments}, to directly transfer the structural knowledge of each node from GNN to MLP. 
The resulting framework \method achieves new state-of-the-art performance on GNN-to-MLP distillation in both transductive and inductive settings across seven graph datasets. We show that \method with better performance infers faster than GNNs by 828×, and also achieves accuracy improvement over GNNs and stand-alone MLPs by 3.90\% and 28.05\% on average, respectively

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a GNN-to-MLP distillation approach. During the teacher GNN training, a series of code embeddings are jointly optimized using a reconstruction loss, to make them encode local graph structures. The divergence between the soft code assignment of the teacher GNN and that of the student MLP is used as additional supervision for distillation. The proposed approach outperforms the teacher GNN and other existing GNN-to-MLP distillation methods in both transductive and inductive settings.

### Strengths
- The proposed approach is novel compared with existing GNN-to-MLP distillation methods.
- Experimental results are good, consistently better than NOSMOG
- Additional ablation studies

### Weaknesses
- Some details of the experimental setup are not clear enough to me. As far as I understand from the paper, in the inductive setting,  $G^L \cup G^U_{obs}$ is used for training the teacher GNN and for distillation. True labels $Y^L$ are used to train the teacher but are not used in distillation. Is it right? The paper mentions that "the edges between $G^L \cup G^U_{obs}$ and $G^U_{ind}$ are removed in training, while they are leveraged during inference to transfer positional features via average operator". What does this mean? Do you augment the node feature with the features of its neighbors for inference?
- What the student MLP can learn from distillation is ambiguous. Suppose two nodes have the same private feature but different neighborhoods, the teacher GNN would generate different representations and different soft code assignments for these two nodes. However, in distillation, the student MLP would always generate the same representation and soft code assignment for these two nodes (since they have the same private feature). As a result, the student MLP cannot learn their structural difference from the teacher

### Questions
Please see Weaknesses

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a novel KD method from GNNs to MLPs to achieve the improvement of inference efficiency, where a special codebook is designed to store the graph information. Experiments on a wide range of benchmarks show its superior performance in terms of both accuracy and time cost.

### Strengths
- How to make MLP more aware of the graph structure is a valuable topic for better inference performance. (while is also not that addressed in this paper, see the first weakness and question below)
- The whole paper is well structured, the explanation for each part is overall complete and clear to understand.
- The experimental results are convincing, indeed providing many interesting observations for discussion (see questions below).

### Weaknesses
- The connection between GNNs-to-MLPs distillation and the proposal of a local-structure-aware codebook is less developed, since they are actually separate goals; more explanation is needed to make the main claim of the paper clearer.
- In practice, one of the main concerns is that the hyper-parameter for the code distillation in equation 7 is quite small compared to the class distillation one. It makes the whole proposal more intended to be a node embedding booster for GNNs, the graph tokenizer, while the codebook is not significantly effective in the distillation phase.
- The volume of the codebook is very likely to be the same scale as the original node features, which makes the proposal still in the trade-off of time and space cost for sure; therefore, more information about the parameter volume should be provided.

### Questions
- Major
    - In the abstract, the authors mention that 'the class space may not be expressive enough to capture numerous different local graph structures'. I am somehow confused, since it is about GNNs-to-MLPs KD, better capturing the local structure information is an issue for GNNs part, instead of KD?
    - It is better to explain more about why it is appropriate to use VQ-VAE to encode graph structure, since it was originally designed for continuous data. For graph-structured data, it might be easier to convert to frequency information, i.e., each position in the "codebook" stores the volume of a specific frequency. I am just curious why VQ-VAE is suitable for encoding discrete and non-Euclidean data.
    - According to the inner product in the reconstruction loss of equation 3 and the benchmarks used, it is quite important to emphasize that the effective domain of the proposal is probably homophilic graphs, otherwise further discussion or experiments on heterophilic graphs are necessary.

- Minor
    - What is the data set used for Figure 1? Cora? All other figures/tables need further clarification on which dataset is used.
    - In equation 3, the node embeddings are still included, so the claimed local structural embedding is not that promising, can you compare or explain the difference of the two parts of the reconstruction function? Also, what's the nonlinear function here?
    - Figure 2 needs improvement- In equation 7, the loss of classification and class distillation should also be clarified.
    - The codebook does not seem to be so different from VGAE from the point of view of structure reconstruction, but the node feature reconstruction part makes it so different. Also, the graph structure part is not well designed, but an inner product.
    - In the figures and descriptions throughout the paper, it is not fair to say that the codebook really preserves the structural information as a substructure, since it is just another integrated embedding where the identifiability of specific structure is missing, therefore it is misleading to give the local structure in Figure 2.
    - An interesting point, which is worth to study further, is what the Figure 5(ii) implies: denser graph needs more space, which is parallel to the discovery from graph signal processing domain, that the structural information cannot be summarized only by some low-frequency filters, the high-frequency ones are also informative in such graphs.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes a new method of knowledge distillation for node classification. Essentially, VQGraph incorporates a VQ-VAE to learn a codebook that represents informative local structures, and use these local structures as additional information, distilling it to student MLPs. Empirically, this approach outperforms state-of-the-art methods, in both accuracy and inference speed.

### Strengths
1. Although VQ-VAE is not a new method, introducing a variant of VQ-VAE for KD for node classification sounds novel, and also make sense. 

2. The paper is well-written and easy to follow.

3. This approach is effective under both inductive and transdutive setting, and also works well for large-scale datasets.

4. The experiment is comprehensive and convincing.

### Weaknesses
1. The size of codebook is sensitive to different datasets, this may introduce some practical difficulty. 

2. It would be better to provide a theoretical understanding of this approach.

### Questions
1. It seems that for APPNP, all three KD approaches can't outperform the teacher model. Is there any discussion or explanation for this phenomenon?

2. In Table 4, Only-VQ outperforms Class-based and AE+Class-based, but Only-VQ only adopts class soft labels, the VQ component helps to train the codebook, why this approach is better than the other two? Can you give some discussions on it?

3. It would be better to provide an analysis what codebook entry is most informative to a class label, which can make this approach more convincing and intuitive.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the GNN-to-MLP distillation problem. The authors claim that the output representation of teacher GNN lack rich graph structural information. With this motivation, they propose to learn codebook embedding via VQ-VAE. After that, the prediction of teacher and student network is obtained by computing the distance between representation to each of the embedding in the learned codebook. Experimental results show that their methods possess faster inference speed and better performance against previous approaches.

### Strengths
- The idea of using VQ-VAE to learn structure-aware embedding is reasonable, which could also serve as an effective approach to extract graph structural feature. Furthermore, the proposed distillation target essentially encourages the representation of each node given by teacher and student network close to the same embedding in the codebook. Therefore, the overall process is more transparent and interpretable.
- This paper is well-organized and easy to follow. The experiments results are convincing and comprehensive, which are enough to support the effectiveness of the proposed method.

### Weaknesses
- Compared with previous method, extra memory space is required due to the introduced learnable codebook. As the authors show, the codebook size has influence on the performance of the model. How to effective tune this hyperparameter is worth exploring.
- The adopted datasets in this paper are generally homophilic, i.e., the connected nodes belong to the same category. It is still unclear whether the proposed method is applicable to heterophilic graphs.

### Questions
- The authors propose a generative approach learn codebook embedding. Is there any other way to learn the codebooks (such as self-supervised learning paradigm) or use other generative models (such as GAN) ?
- Could the proposed method be applied to heterophilic graphs [1,2]? 

[1]  Lim et al., Large scale learning on non-homophilous graphs. NeurIPS 2021.

[2] Platonov et al, A critical look at the evaluation of GNNs under heterophily: Are we really making progress? ICLR 2023.

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
The goal of this paper is to distill the knowledge of "teacher" graph neural networks to "student" MLPs for efficiency. Existing knowledge distillation methods for graph-structured data exploit labels of each node for the knowledge distillation. But, the number of labeled nodes is limited so that the class space may not be sufficient to cover the diverse graph structures. To address this issue, the paper proposes a variant of VQ-VAE to directly label the local graph structures. Specifically, it first learns a structure-aware tokenizer for dealing with graph structured datsets. The structure-aware tokenizer encodes the local substructure of each node as a discrete code. Then, the paper designs a new distillation target to directly transfer the structural knowledge of each node from GNN to MLP.

### Strengths
- The paper deals with one of the important research topics on graph representation learning.
- The proposed VQ-VAE is effective and efficient on various datasets and tasks from the author's experiments.
- The paper is well written and easy to follow.

### Weaknesses
- It would be better if more details about the production scenario were included in the paper. If the authors are not experts in the graph knowledge distillation domain, they are unlikely to know the details of the experiments. So, more details about the tasks need to be described.
- I wonder whether the proposed VQ-VAE pre-trains both graph tokenizer and graph neural networks simultaneously or pre-trains graph neural networks first and then the graph tokenizer.
- The paper claimed that capturing graph structure is important for knowledge distillation. Then, I think that learning representations with self-supervised learning [1] for graphs can be other option to capture local graph structure. In my thoughts, labeling nodes' local structure with discrete codes seems not different from learning node representation with self-supervision loss [1] if its purpose is capturing local structure.

[1]: Veličković, Petar, et al. "Deep graph infomax." ICLR 2019.

### Questions
Please refer to the above weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

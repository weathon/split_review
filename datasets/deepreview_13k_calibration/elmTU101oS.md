# Learning General Representations Across Graph Combinatorial Optimization Problems

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 6, 6, 3

## Abstract
Combinatorial optimization (CO) problems are classical and crucial in many fields, with many NP-complete (NPC) examples being reducible to one another, revealing an underlying connection between them. Existing methods, however, primarily focus on task-specific models trained on individual datasets, limiting the quality of learned representations and the transferability to other CO problems. Given the reducibility among these problems, a natural idea is to abstract a higher-level representation that captures the essence shared across different problems, enabling knowledge transfer and mutual enhancement. In this paper, we propose a novel paradigm CORAL that treats each CO problem type as a distinct modality and unifies them by transforming all instances into representations of the fundamental Boolean satisfiability (SAT) problem. Our approach aims to capture the underlying commonalities across multiple problem types via cross-modal contrastive learning with supervision, thereby enhancing representation learning. Extensive experiments on seven graph decision problems (GDPs) demonstrate the effectiveness of CORAL, showing that our approach significantly improves the quality and generalizability of the learned representations. Furthermore, we showcase the utility of the pre-trained unified SAT representations on related tasks, including satisfying assignment prediction and unsat core variable prediction, highlighting the potential of CORAL as a unified pre-training paradigm for CO problems.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a novel paradigm CORAL that treats each CO problem type as a distinct modality and unifies them by transforming all instances into representations of the fundamental Boolean satisfiability (SAT) problem. The approach aims to capture the underlying commonalities across multiple problem types via cross-modal contrastive learning with supervision, thereby enhancing representation learning.

### Strengths
1.	This paper attempts to address an important issue, which is training a pre-trained model for the SAT domain using data from different fields. However, there is controversy over whether this problem is solvable, as relevant studies have shown that the transferability between different SAT problems is poor [1], and SAT problems are highly sensitive to structure; minor modifications to the structure of the SAT model can lead to changes in results [2]. Additionally, SAT formulas lack extensive node features, while GNN model predictions entirely depend on structure and features, which raises concerns about the ability of GNN models to serve as cross-field pre-trained models for SAT.
2.	The experimental results presented in this paper are quite good. However, these results are only compared with GCN and NeuroSAT models, neither of which are state-of-the-art (SOTA) models for learning GDP problem representations and SAT formula representations. This suggests that the baseline models used are too weak.
3.	The writing in this paper is excellent, with no noticeable grammatical errors.

[1] Li Z, Guo J, Si X. G4satbench: Benchmarking and advancing sat solving with graph neural networks[J]. arXiv preprint arXiv:2309.16941, 2023.

[2] Shi Z, Li M, Khan S, et al. Satformer: Transformers for SAT solving[J]. arXiv preprint arXiv:2209.00953, 2022.

### Weaknesses
1.  From the problem description, I believe that SAT is merely a format for problem representation rather than a modality; the k-clique and k-color instances used in the paper are just SAT problems derived from different domains, not different modalities. Moreover, there are existing toolkits such as CNFGen [1] that can convert problems like k-clique and k-color into SAT problems, so the second claimed contribution of this paper does not hold.
2.  In terms of applicability, I do not think that all CO (Combinatorial Optimization) problems can be transformed into SAT problems; some complex CO problems with continuous variables need to be converted into Mixed Integer Programming (MIP) problems. Therefore, the universality of this method is quite limited.
3.  Regarding the optimization objective, the paper simply treats GDP problems and their corresponding SAT problems as positive examples, while other SAT problems within the same domain are treated as negative examples. This contrastive learning approach is overly simplistic and can easily generate false negatives because these SAT formulas may differ structurally but be logically equivalent or share the same satisfiability status.
4.  In terms of the model architecture, the paper addresses all GDP problems using a Graph Convolutional Network (GCN), which is a less precise method for solving combinatorial optimization problems [2][3], leading to low-quality learned representations. From an experimental standpoint, this implies that the baseline model is very weak. For SAT problems, the paper also employs the classic NeuroSAT model in a straightforward manner. Thus, I believe the rationality and innovation of the model are insufficient and do not effectively address the challenge of collaborative optimization across domains. Additionally, adopting different models for problems in each domain significantly increases the number of model parameters, affecting the scalability and generalization capability of the model to new domain problems (such as the Pigeonhole principle).

### Questions
1.	How do you justify the feasibility of constructing a cross-domain pre-training model for GDP problems based on GNN? Given that the distribution of GDP problems varies significantly and the prediction results heavily rely on logical reasoning, which is not a task that GNN excels at. For example, minor modifications to the structure of the SAT model can lead to changes in results. To answer my question, I suggest the authors to discuss these challenges more explicitly in the paper and propose ways to incorporate logical reasoning capabilities, or analyze the sensitivity of the model to structural changes.
2.	Why did you choose to use GCN (or GraphSAGE) as the baseline model for GDP representations? For GDP problems, these two models are not state-of-the-art; instead, they have been pointed out by existing work to be very weak baseline models. Since this paper does not introduce innovations at the model level but instead attempts to propose a universal architecture, you need to use SOTA graph learning models (stronger GNNs and graph transformers, such as PGN[1] and GraphGPS[2]) as backbones to validate the effectiveness of the architecture you have proposed.

[1] Cappart Q, Chételat D, Khalil E B, et al. Combinatorial optimization and reasoning with graph neural networks[J]. Journal of Machine Learning Research, 2023, 24(130): 1-61.

[2] Wang T, Payberah A H, Vlassov V. Graph Representation Learning with Graph Transformers in Neural Combinatorial Optimization[C]//2023 International Conference on Machine Learning and Applications (ICMLA). IEEE, 2023: 488-495.

3.	When you train specific models for data from each domain, how do you generalize this pre-training model to data from different domains, rather than just to data of varying difficulty levels within the same domain? How can you explain the necessity of building a model for each domain? This not only limits the model's generalization ability but also greatly increases its complexity.
4.	Why did you use other SAT problems from the same domain as negative examples? The selection of positive and negative examples in contrastive learning is a critical issue, and this paper also lists it as one of the core challenges. However, the solution provided in this paper is too blunt and can easily generate pseudo-negative examples, as these SAT formulas might differ in structure but be logically equivalent or have the same satisfiability status. Therefore, I believe you need to design a contrastive learning positive and negative sample selection method that can better balance structure, function, and domain knowledge. For instance, in terms of functionality, you could refer to papers like FGNN[3]. Such an innovation could significantly enhance the contribution of your paper.

[3] Wang Z, Bai C, He Z, et al. Functionality matters in netlist representation learning[C]//Proceedings of the 59th ACM/IEEE Design Automation Conference. 2022: 61-66.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper focuses on solving graph deision problems (GDPs) with graph neural networks by modeling each GDP type with task-specific graph modules. The correponding SAT bipartite graphs of each GDP are utlized as an intermediate modal of data that contrastively optmizes the graph representation modules. Experimental results validate the effectiveness of the proposed graph GDP model in generating representations and solving GDP probelems.

### Strengths
+ A pioneering effort that propose to process GDP problems with GNN frameworks.
+ Combining GDP problems with corresponding SAT graphs is a novel and well motivated idea.
+ The method is well presented and easy to follow.

### Weaknesses
 - The proposed model is introduced as a general solution to combinatorial optimization problems, yet it is limited to solving GDP problems. Although CO problems can be transformed GDPs in the sense of complexity, solving GDPs is not necessarily equivalent to practical solutions to correponding CO problems.
- It seems that the general SAT model significantly outperforms specific graph models, raising concerns about the expressiveness of the graph model.
- It would be more illustrative to have case studies on model outputs for specific GDP and correponding SAT problems.

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces CORAL, a novel learning paradigm that enhances generalizability and representation quality across various graph combinatorial optimization problems by unifying them as SAT problems through cross-modal contrastive learning.

### Strengths
1. This paper proposes CORAL, a new framework for learning universal representations of multiple CO problems.

2. This paper introduces SAT as an intermediate unified mode to bridge different CO problems and effectively learn the shared features.

3. Extensive experiments have been conducted on multiple problems and datasets to validate the effectiveness of the proposed method.

### Weaknesses
Please refer to questions.

### Questions
1. The goal of achieving high generalization through multiple losses[1] or collaborative representations of multiple models[2] seems to be a method that has been discussed multiple times outside of the GDP field. What is the core difference between the method proposed in this paper and those methods?

2. Why using the contrastive loss to align the representation of the GDP and SAT modalities is a way to get a higher-level, abstract representation?

3.  Are there any other comparable works in the experiment? There seems to be a lack of comparison with other similar types of work in the experiment.

[1] Automated Self-Supervised Learning for Graphs. Arxiv 2106.05470

[2] Decoupling Weighing and Selecting for Integrating Multiple Graph Pre-training Tasks. Arxiv 2403.01400


---

I work in graph pre-training, but I am not familiar with GDP problems. If authors can address my concerns, I will reconsider my score.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a novel paradigm called CORAL (Combinatorial Optimization Representation Alignment and Learning) for learning general representations across different combinatorial optimization (CO) problems. The main idea is to treat each graph decision problem (GDP) as a separate modality and use the Boolean satisfiability (SAT) problem as an intermediary to unify these problem types. The proposed CORAL framework employs cross-modal contrastive learning to align different GDPs through SAT representations, thereby enhancing the quality and generalizability of learned representations.

### Strengths
1. **Novel Unified Framework**: CORAL is the first to unify representation learning across different combinatorial optimization problems, which is innovative and addresses a significant gap in current methods.
  
2. **Effective Use of SAT as an Intermediary**: Leveraging SAT as a common modality effectively bridges the differences between various graph decision problems, promoting knowledge transfer and alignment.
  
3. **Enhanced Generalizability**: The cross-modal contrastive learning approach significantly improves the quality and generalizability of learned representations, as demonstrated by superior performance in both task-specific and generalization experiments.
  
4. **Comprehensive Experiments**: The paper provides extensive experimental validation across multiple problem types and tasks, highlighting the robustness and scalability of the proposed approach.

### Weaknesses
1. **Complexity of the Framework**: The introduction of SAT as an intermediary and cross-modal contrastive learning adds substantial complexity, potentially making the model challenging to implement and computationally expensive. The framework requires transforming graph decision problems into SAT instances, which involves additional encoding and decoding steps. This transformation process itself can be computationally intensive, especially for large graphs, and the overhead of managing these transformations is not fully addressed. Furthermore, the cross-modal contrastive learning necessitates training separate models for each domain and then aligning them, increasing the overall complexity of the training pipeline.

2. **Limited Comparison with Alternative Methods**: The paper lacks a comprehensive comparison with other state-of-the-art multi-task learning approaches or GNN-based optimization frameworks, limiting the understanding of CORAL's relative strengths. While the authors claim that no existing framework can be directly adopted for comparison, there are several multi-task learning methods and GNN architectures that could be adapted or used as baselines. For example, comparing against a multi-task GNN that directly learns representations across different graph problems, without the SAT intermediary, would provide valuable insights into the benefits of the proposed approach. The absence of such comparisons makes it difficult to assess the true novelty and effectiveness of CORAL.

3. **Scalability Concerns**: The approach may face scalability issues when dealing with larger, real-world problem instances due to the overhead of transforming GDPs into SAT representations and training multiple models. The transformation of large graphs into SAT instances can lead to a significant increase in the size of the problem, potentially exceeding the memory capacity of standard hardware. Additionally, the training of separate models for each domain, followed by cross-modal alignment, can be computationally expensive and time-consuming, making it challenging to scale the approach to very large datasets or complex problems. The paper does not provide sufficient analysis of the computational cost associated with scaling to larger instances.

4. **Insufficient Analysis of Computational Cost**: There is no detailed analysis of the training time, memory requirements, or computational resources needed for CORAL, which could be a barrier to real-world adoption. The paper does not provide information on the time required for training the models, the memory footprint of the framework, or the hardware requirements for running the experiments. This lack of information makes it difficult to assess the practical feasibility of the approach and limits its applicability in resource-constrained environments. A detailed analysis of the computational cost is essential for understanding the trade-offs between performance and resource utilization.

5. **Lack of Ablation Studies**: The paper does not include an ablation study to evaluate the contribution of each component (e.g., SAT transformation, contrastive learning) to the overall performance, making it difficult to determine their individual impact. While the authors claim that SAT transformation and contrastive learning are inherently linked, it is still possible to conduct ablation studies by varying the strength of the contrastive loss or by using different SAT encodings. Without such analysis, it is unclear which components of the framework are most critical for its performance and whether the complexity of the framework is justified by the performance gains.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
3

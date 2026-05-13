# DUAL-TASK VAE FOR NODE-LEVEL DATA AUGMENTATION

- Decision: Reject
- Scores: 3, 3, 3, 3

## Abstract
Graph Neural Networks (GNNs) have shown great promise in processing graph-structured data, but they often require large amounts of labeled data and are sensitive to noise. In this paper, we propose a novel node-level data augmentation approach that leverages a Variational Autoencoder (VAE) within a dual-task learning framework to address these challenges. Our method utilizes the VAE to generate enriched node representations that capture both structural and feature-related information, which are then combined with the original node features for classification by a Graph Attention Network (GAT). Experiments conducted on the Cora, Citeseer, and Pubmed datasets show that our approach outperforms baseline models, achieving up to 7.3\% higher accuracy in Pubmed, and surpassing recent state-of-the-art data augmentation techniques. This work highlights the effectiveness of dual-task learning for robust feature enhancement and advances data augmentation strategies in GNNs.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The paper presents a novel approach for node-level data augmentation in graph neural networks (GNNs) using a dual-task Variational Autoencoder (VAE). By encoding graph data into a latent space, it aims to improve node classification tasks through an augmentation strategy that combines raw features with latent representations. Experimental results on the Cora dataset suggest that this method could potentially enhance model performance.

### Strengths
1 - The paper proposes an original VAE-based framework for graph data augmentation, which could be valuable for improving data availability and robustness in GNNs.

2 - The use of a multi-channel convolutional layer in the VAE’s encoder, including various GNN models (e.g., GCN, GAT, SAGE, GIN), demonstrates a well-thought-out design to capture complex node representations.

3 - The authors evaluate their model’s effectiveness using multiple performance metrics, including accuracy, F1 score, and precision, providing a comprehensive set of evaluation perspectives.

### Weaknesses
1 - The paper lacks a comparison with more recent state-of-the-art GNNs, which limits the ability to contextualize the performance gains claimed. Evaluating against stronger baselines could more convincingly demonstrate the proposed method’s advantages.

2 - The quality of the figures and tables is inadequate. Important architectural details and quantitative comparisons are not well-visualized, making it challenging to interpret the findings effectively.

3 - Although the approach was tested on the Cora dataset, it’s unclear if the findings would hold across other datasets with different characteristics, limiting the method’s applicability.

### Questions
Why did you not include recent state-of-the-art GNNs as baselines? How would your approach compare to these models in terms of performance and computational cost?

Could you elaborate on the rationale behind the selection of the Cora dataset? Would you expect similar improvements on larger, more complex datasets?

Could you improve the visual clarity of figures and tables? Specifically, the architecture diagram and performance comparison tables would benefit from higher resolution and better layout.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work studies the data augmentation strategy for node-level classification. The authors propose to integrate a Variational Autoencoder (VAE) to augment the node features. They find this augmentation strategy achieves impressive performance on Cora, when applied to a specially designed GNN architecture.

### Strengths
(+) This work presents an interesting trial that tries to enrich the node features to perform the data augmentation;

(+) The authors integrate two strategies, including the feature fusion, and the VAE to augment the node features;

(+) Some simple experiments demonstrate certain effectiveness of the enriched features;

### Weaknesses
(-) The novelty is limited. For example, the fusion of multiple GNN convolutional features is one of the standard machine learning tricks in data science competitions like Kaggle;

(-) The presentation is clear, yet most of the contents in this paper are already known to the community;

(-) The results lack of convinceness, as it only covers simple datasets, single random seed and GNN backbones;

### Questions
1. The novelty is limited:
- For example, the fusion of multiple GNN convolutional features is one of the standard machine learning tricks in data science competitions like Kaggle;
- Meanwhile, it is also unclear why VAE features could help with the task;

2. The presentation is clear, yet most of the contents in this paper are already known to the community. 
- In addition, the current manuscript looks unready for publication due to the lack of formality in multiple sections, such as Table 1.

3. The results lack of convincingness:
- The experiments only cover simple datasets, single random seeds and GNN backbones;
- The visualization of features offer limited insights;

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
In this paper, the authors propose a Variational Autoencoder (VAE)-based method for node-level data augmentation to improve Graph Neural Network (GNN) performance on node classification tasks. The approach combines raw graph data with latent representations generated through a VAE, using a dual-task framework involving node classification and data reconstruction.

### Strengths
- The paper presents an attempt to use VAE-based data augmentation for GNNs, which could be beneficial in enhancing model robustness to noise and incompleteness.

### Weaknesses
 - The paper’s novelty is minimal.
- The methodology is somewhat incremental and lacks clarity.
- The experimental results are superficial.
- The writing quality is poor.

- Novelty and Motivation. While the paper claims to propose a novel VAE-based method for data augmentation in GNNs, it primarily combines standard techniques (VAE and GNNs) with minimal innovation. The authors should clarify how their approach distinguishes itself from existing data augmentation methods for graph neural networks or from previous work on dual-task models. 

- What is the rationale for combining multiple GNN architectures (GCN, GAT, SAGE, GIN) within the VAE model? In Section 3.2.1, the authors describe a multi-channel convolutional layer that integrates several GNN backbones but do not explain how these specific architectures complement each other or the benefits of combining them. For instance, why is it necessary to incorporate both GAT and SAGE, and how do they contribute to the model’s performance?

- No hyper-parameter analysis for the weighting parameters $a$ and $b$ introduced in Eq.5

- Section 4.7 discusses the impact of architectural complexity but does not compare the computational complexity and efficiency of the model's multi-GNN backbone architecture.

- The experimental results lack comparisons with adequate baselines. Why did the authors not compare their approach with other data augmentation methods, such as edge dropping, node dropping, feature masking, or subgraph sampling, to validate their results? Could the authors consider including more competitive baselines, such as GraphMAE [1] and GraphCL [2]?

- Could the authors explain why they used only the Cora dataset, a relatively small and well-known benchmark, instead of employing more challenging and widely adopted datasets, such as Citeseer, Pubmed, ogb-arxiv, or Wiki-CS?

- The paper’s figures are non-vector images, and its structure is disorganized with vague descriptions, impairing clarity. Specifically, figures such as the architecture diagrams in Sections 3 and 4 should be presented as vector graphics to improve visual quality, especially when zoomed in. These issues compromise the paper’s professionalism and readability, particularly for a technical audience.

### Questions
- Novelty and Motivation. While the paper claims to propose a novel VAE-based method for data augmentation in GNNs, it primarily combines standard techniques (VAE and GNNs) with minimal innovation. The authors should clarify how their approach distinguishes itself from existing data augmentation methods for graph neural networks or from previous work on dual-task models. 

- What is the rationale for combining multiple GNN architectures (GCN, GAT, SAGE, GIN) within the VAE model? In Section 3.2.1, the authors describe a multi-channel convolutional layer that integrates several GNN backbones but do not explain how these specific architectures complement each other or the benefits of combining them. For instance, why is it necessary to incorporate both GAT and SAGE, and how do they contribute to the model’s performance?

- No hyper-parameter analysis for the weighting parameters $a$ and $b$ introduced in Eq.5

- Section 4.7 discusses the impact of architectural complexity but does not compare the computational complexity and efficiency of the model's multi-GNN backbone architecture.

- The experimental results lack comparisons with adequate baselines. Why did the authors not compare their approach with other data augmentation methods, such as edge dropping, node dropping, feature masking, or subgraph sampling, to validate their results? Could the authors consider including more competitive baselines, such as GraphMAE [1] and GraphCL [2]?

- Could the authors explain why they used only the Cora dataset, a relatively small and well-known benchmark, instead of employing more challenging and widely adopted datasets, such as Citeseer, Pubmed, ogb-arxiv, or Wiki-CS?

- The paper’s figures are non-vector images, and its structure is disorganized with vague descriptions, impairing clarity. Specifically, figures such as the architecture diagrams in Sections 3 and 4 should be presented as vector graphics to improve visual quality, especially when zoomed in. These issues compromise the paper’s professionalism and readability, particularly for a technical audience.

[1] Hou, Zhenyu, et al. "GraphMAE: Self-supervised masked graph autoencoders." *Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining*, 2022.  
[2] You, Yuning, et al. "Graph contrastive learning with augmentations." *Advances in Neural Information Processing Systems* 33 (2020): 5812-5823.

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
5

### Summary
The paper proposes a two-stage training framework to alleviate the supervision shortage issue. In the first stage, the VAE is trained with the reparameterization method to model the distribution of node representations. Then its output will be used to improve the performance of the GNN in the second stage.

### Strengths
The paper provides a very detailed introduction to the backbone architectures used in the work.

### Weaknesses
The motivation of the paper is unclear. Numerous strategies already address label scarcity in graph machine learning (e.g., Graph SSL). Why is this new framework necessary, and what specific advantages does it offer over existing approaches?

The experimental evaluation is limited to the Cora dataset, which lacks comprehensiveness. Even within the scope of smaller datasets, the authors have many options to broaden the evaluation. Expanding experiments to more diverse datasets is encouraged. Additionally, the authors should consider the significance if the proposed framework cannot effectively handle larger datasets.

The paper’s presentation requires improvement. There is considerable redundant content, and the figures and tables lack clarity and effective demonstration.

### Questions
Please refer to the weakness part.

### Soundness
2

### Presentation
1

### Contribution
2

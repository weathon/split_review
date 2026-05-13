# MeshMask: Physics-Based Simulations with Masked Graph Neural Networks

- Decision: Accept
- Scores: 6, 5, 8

## Abstract
We introduce a novel masked pre-training technique for graph neural networks (GNNs) applied to computational fluid dynamics (CFD) problems. By randomly masking up to 40\% of input mesh nodes during pre-training, we force the model to learn robust representations of complex fluid dynamics. We pair this masking strategy with an asymmetric encoder-decoder architecture and gated multi-layer perceptrons to further enhance performance. The proposed method achieves state-of-the-art results on seven CFD datasets, including a new challenging dataset of 3D intracranial aneurysm simulations with over 250,000 nodes per mesh. Moreover, it significantly improves model performance and training efficiency across such diverse range of fluid simulation tasks. We demonstrate improvements of up to 60\% in long-term prediction accuracy compared to previous best models, while maintaining similar computational costs. Notably, our approach enables effective pre-training on multiple datasets simultaneously, significantly reducing the time and data required to achieve high performance on new tasks.
Through extensive ablation studies, we provide insights into the optimal masking ratio, architectural choices, and training strategies.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a masked pretraining strategy for learning mesh-based simulation. An asymmetric encoder/decoder architecture is proposed for doing masked-node reconstruction. Throughout numerical experiment, the authors showcase the pretraining can improve temporal prediction accuracy over other baselines.

### Strengths
* The proposed pretraining consistenly improves GNN’s performance on various physical systems.

* The numerical experiments are extensive and cover relatively challenging problems. Specifically, a large-scale 3D simulation with 250k nodes is studied.

### Weaknesses
 * The discussion related to the model architecture and the graph construction after masking is relatively vague. The authors say they used a multi-grid GNN with a W-cycle structure and is a Encoder-Processor-Decoder setup, but it is also stated that in the pretraining section the model for pertaining is an Autoencoder with graph encoder/decoder. Does the model architecture and grid structure change or remain the same in pretraining and fine-tuning? In addition, as the masking nodes are randomly sampled, is the masked mesh still valid after an excessively high masking ratio? Specifically, if the masking is performed randomly, it is unclear how the graph structure is preserved, and how the message passing is affected by the disconnected subgraphs.

* For the numerical experiments, the authors describes the detail for pre-training and fine-tuning of their proposed model, but it seems that there is not too much information in terms of the training budget of the baseline model (or I have missed them). For example, suppose training a GNN on next-step prediction without masking for 100k steps needs 1e9 flops, and then pretraining it for 100k steps needs another 1e9 flops. Then for the baseline models without pretraining, a fair comparison would be training them using 2e9 flops. It is crucial to have a clear comparison of the computational cost, including the number of parameters, training time, and inference time, for both the proposed method and the baselines.

* Following the last point, if the pretraining can be done on a dataset order-of-magnitude larger than almost all downstream tasks (for example, LLMs), then maintaining similar flops between pretraining/no pretraining model indeed becomes meaningless. However, according to the result shown in Table 3, pretraining on a mutli-physics dataset actually performs worse than pretraining on the same physics, and pretraining on a completely different physics is actually harmful to the downstream tasks. This raises concerns about the generalizability of the pretraining approach and whether the pretraining is truly learning transferable features or just overfitting to the pretraining dataset.

### Questions
* Does the masking algorithm consider irregular connectivity? For example, a sub-graph is detached from other sub-graphs after masking.

* Following point 2 in the Weakness, can authors provide more details in terms of the training time/ number of parameters of different models?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a masked pre-training technique for Graph Neural Networks (GNNs) aimed at solving physics simulations, particularly in computational fluid dynamics. The proposed approach uses an asymmetric encoder-decoder architecture in conjunction with gated multi-layer perceptrons. Extensive experiments are conducted, including independent training on multiple datasets, transfer learning, and multi-dataset pretraining. The results demonstrate that the MeshMask model delivers competitive performance compared to established baselines.

### Strengths
The paper introduces a novel approach by implementing masked pre-training for Graph Neural Networks (GNNs) in physics simulations. It is well-structured and easy to follow, with rich qualitative results and visualizations.

### Weaknesses
1. The introduction of gated MLP and encoder-decoder architecture potentially increases the model's computational complexity. There is a lack of detailed discussion on the computational demands (e.g. training/inference time,  training/inference RAMs) compared with baselines, which is critical for evaluating the feasibility of deploying MeshMask in real-time applications or on large-scale datasets. Specifically, the paper does not provide a breakdown of the computational cost associated with the gated MLP layers compared to standard MLPs, making it difficult to assess the trade-off between performance gains and computational overhead. Furthermore, the memory footprint of the model during training and inference is not reported, which is crucial for practical deployment, especially on resource-constrained devices.
2. The compared baselines are limited, authors should consider more GNN-based simulation models such as [1-4]. Furthermore, both GCN and U-Net baselines have only been tested on a few datasets. The selection of baselines does not adequately represent the current state-of-the-art in GNN-based physics simulation. The absence of comparisons with other recent GNN architectures tailored for similar tasks makes it difficult to ascertain the true novelty and effectiveness of the proposed method. The limited testing of GCN and U-Net on a small subset of datasets further weakens the comparative analysis.
3. The novelty of replacing standard MLPs with gated MLPs in the processor is somewhat limited. The authors should consider a wider variety of network architectures such as attention-based models [1,2,4] for comparison to make their findings more persuasive. The justification for using gated MLPs over other alternatives is not thoroughly explored. The paper lacks an ablation study that systematically compares the performance of gated MLPs with other architectural choices, such as attention mechanisms or other forms of non-linear transformations, which could provide a more comprehensive understanding of the contribution of this component.

### Questions
1. Given that your input mesh includes masked data, how do you effectively learn long-range interactions on the masked graph during the repeated message passing?
2. In Sec 4.3,  given that the input and output physics quantities differ across the datasets, the potential for a significant gap in the encoded latent space raises concerns about the legality and effectiveness of the transfer learning approach. How do you ensure that the latent spaces of the two datasets are compatible? Secondly, the length of input and output quantities varies across datasets; how do you exactly fine-tune the model when faced with these differing lengths?
3. What is the model's performance on out-of-distribution (OOD) mesh resolutions?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces MeshMask, a GNN masking pre-training technique designed to enhance the efficiency and performance of GNNs in solving CFD problems. Drawing inspiration from the success of masked autoencoders in NLP and CV, the authors adapt masking pre-training techniques to GNN models in the CFD domain. MeshMask demonstrates performance improvements across multiple CFD datasets.

### Strengths
1. The authors developed an appropriate masking pre-training scheme for GNNs in CFD tasks.

2. The method shows notable performance improvements compared to baseline approaches.

3. The paper is well-organized, with clear figures and visualizations that help the reader understand.

### Weaknesses
1. The comparison seems limited to very basic baseline methods~(i.e., MGN, Multigrid). Given the recent attention to GNN-based CFD modeling, more recent baselines could have been included in the comparison.

2. Despite multiple claims about *training efficiency*, there appears to be a lack of comprehensive discussion on efficiency metrics.

3. The experiments lack testing across varying *graph density* scenarios. The effectiveness of the method across different graph densities could have been better demonstrated.

### Questions
1. Please discuss and address the concerns raised in the weaknesses.

2.  Why is the transfer learning on CFDs effective? Could the authors provide some high-level discussion about the underlying mechanisms?

### Soundness
3

### Presentation
3

### Contribution
3

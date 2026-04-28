# Crystals with Transformers on Graphs, for predictions of crystal material properties

- Decision: Reject
- Avg Score: 3.25
- Scores: 1, 3, 3, 6

## Abstract
Graph neural networks (GNN) has found extensive applications across diverse domains, notably in the modeling molecules. Crystals differ from molecules by the ionic bonding across the lattice and the highly ordered microscopic structure, which provides crystals unique symmetry and determines the macroscopic properties. Therefore, long-range orders are essential in predicting the physical and chemical properties of crystals. GNNs successfully model the local environment of atoms in crystals, however, they struggle to capture long-range interactions due to a limitation of depth. In this paper, we propose CrysToGraph ($\textbf{Crys}$tals with $\textbf{T}$ransformers $\textbf{o}$n $\textbf{Graph}$s), a novel transformer-based geometric graph network designed specifically for crystalline systems. CrysToGraph effectively captures short-range dependencies with transformer-based graph convolution blocks and long-range dependencies with graph-wise transformer blocks. Our model outperforms most existing methods by achieving new state-of-the-art results on the MatBench benchmark datasets.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a method for predicting chemical properties of materials. Building on the results of previous work, the method utilizes the line-graph of the crystal graph for message passing. For this, the attention mechanism of the transformer architecture is adapted to the case of 3 nodes of the original graph. These 3 nodes are adjacent nodes in the line graph. Additionally, an additional transformer layer that performs message passing on the complete graph is added. For this module a positional encoding is introduced, which merges 4 different positional encodings.

### Strengths
The specifically tailored development of machine learning methods for crystal structures is an important problem with relevance for the society. Because of this also machine learning conferences like ICLR should be open for publications that develop these specific methods. However, this publication has certain weaknesses, please see below.

### Weaknesses
*Positional Encoding*

The positional encoding is not E(3) invariant and thus is not suitable for modeling the properties of materials. Nodes of the crystal graph are represented with a 3D coordinate of the particular atom in the crystal grid. For a machine learning model to successfully predict the material properties, the feature representation needs to be equivariant or invariant towards E(3) transformations of these coordinates. The proposed positional encoding is not invariant or equivariant to these transformations:

1. Cartesian coordinates: If I understand correctly, then these are extrinsic coordinates. Any function that directly depends on these extrinsic coordinates is not equivariant to E(3) transformations. Specifically, a rotation of the crystal structure will change the cartesian coordinates, but should not change the material properties. Therefore, using these coordinates directly in a machine learning model will not lead to a model that generalizes well to rotated versions of the same crystal structure.

2. Fractional coordinates: Are these intrinsic or extrinsic coordinates? I must assume that they are extrinsic, thus the same problems exist as described in 1. Similar to cartesian coordinates, fractional coordinates are also affected by rotations of the crystal structure. While they are defined with respect to the lattice vectors, they still represent a specific position in space and not an intrinsic property of the crystal structure itself. Therefore, they are not suitable for creating E(3) invariant representations.

3. and 4. Laplacian embedding and Random walk encoding: These might be useful as they are intrinsic, however Laplacian and Random walk are closely related: There is even a Laplacian associated to a Random walk. Therefore this seems redundant, at least terminology-wise the relationship of the two should be pointed out. Furthermore, while these encodings are intrinsic to the graph structure, they do not capture the full 3D geometry of the crystal, which is crucial for determining material properties. A combination of intrinsic and extrinsic features is necessary, but the extrinsic features must be E(3) invariant or equivariant.


*Multi Head Neighbor Attention*

Multi Head Neighbor Attention appears to be just normal multi head attention on the line graph and should be stated as such and not be presented as a new method. The description provided does not clearly distinguish it from standard multi-head attention mechanisms applied to a graph. The specific modifications, if any, should be explicitly stated.


*Technical remarks and writing style:*

"holistic representation of spatial information" seems to be an awkward terminology. More important would be that this representation results in E(3) equivariance which is a mathematical term which "holistic" is not and thus should be avoided.

Introduction, 2nd paragraph, typo: enxtends

### Questions
Which of the positional encodings are intrinsic and which are extrinsic?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors mainly tackle that GNNs are limited to capturing long-range interactions. To overcome this limitation, the authors propose a model architecture that can capture the local information with GNN and long-range interactions with a graph-wise transformer. Specifically, two building blocks are proposed: edge-engaged transformer graph convolution (eTGC) and graph-wise transformer (GwT). eTGC is a GNN-based architecture that applies the softmax attention mechanism while the message passing, and GwT is a transformer that is performed on the node embeddings. The authors evaluate their methods for predicting chemical properties on the periodic molecular dataset.

### Strengths
* Modeling the periodic molecules is an important subject for material discovery.
* The experiments are fairly conducted on a common benchmark for materials.

### Weaknesses
 * It is not described why modeling the long-range interaction is the key to modeling the periodic molecules. To my understanding, the tackled GNN's limitation is a general problem in the graph field and does not need to be restricted in modeling the periodic structures.
* From the results of Figure 5 and 6, the effectiveness of modeling the long-range interaction by using the transformer seems to be insignificant, even though the long-range interaction is the main point of this paper. In other words, if the number of eTGC blocks becomes larger, the effect of GwT seems to be weakened and the performances are similar. Specifically, the performance gains from adding the graph-wise transformer (GwT) are marginal, especially when the number of eTGC layers is increased. This suggests that the model may not be effectively leveraging the long-range interactions that the transformer is intended to capture, or that the local information captured by eTGC is sufficient for the task.
* Even though the proposed method leverages the transformers which require more memory space, the performances are not significant compared to the baselines. The computational overhead of the transformer architecture does not seem to be justified by the performance gains. The authors should provide a more detailed analysis of the computational cost and memory usage of their model compared to the baselines.
* It is not explained what the tasks are. The material properties may not be familiar to the AI researchers and noting the tasks as abbreviations without any explanation could confuse the readers. The abbreviations used for the tasks (e.g., in Figure 5 and 6) are not defined, making it difficult to understand the specific prediction goals. The authors should clearly state what material properties are being predicted and provide context for why these properties are important.

### Questions
* If many GwT blocks make the local information from the eTGC lost, have you ever applied the eTGC and GwT by crossovering them? (for example, $\text{GwT}(\text{eTGC}(\mathcal{G}, L(\mathcal{G})) \times N$)
* Why do you use softmax attention in eTGC?
* Why do you use the simple transformer architecture for GwT not the graph transformer architectures?
* Why is it insufficient to use deeper GNN layers instead of using transformers?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Paper aims to use a graph-transform to predict properties of crystal-graphs. Notably, transformers are well suited for this task because unlike traditional MPNNs they are able to capture both local and global information.

The paper has some interesting ideas, but it appears to be mostly a mixing and matching of existing methods with only moderately impressive numerical experiments. If it were more clearly different than existing methods or if it was clear that this method of combining existing results lead to a massive improvement numerically, I would more favorably inclined. However, as is, I do not think this paper is good enough in its current form.

That said, I am not an expert on transformers and have no experience with crystals. Therefore, my opinion should be taken with a grain of salt.

### Strengths
Numerical results seem moderately impressive and the authors seem knowledgeable about GNNs / Transformers in the context of crystallography.

### Weaknesses
Method seems only slightly different than existing approaches (essentially being a linear combination of existing methods) and only achieves moderately good numerical results. 

Less importantly, there are also numerous typos and grammar / spelling errors.

### Questions
What is meant by coordination number?

Is the $k$-nn graph an "or" k-nn, and "and" k-nn, or a directed graph?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a general framework, CrysToGraph, for crystal materials property prediction. The overall idea is to encode the crystal graph into an embedding representation, and use this representation for classification or regression tasks. More specifically, the inputs are composed of the atom node embeddings, edge embeddings and angle information for edge pairs. These features first go through edge-engaged transformer graph convolution (eTGC) to extract phase-1 embeddings for atoms and edges. Then the Graph-wise Transformer (GwT) iteratively update atom node encodings by absorbing `information` from connecting edges. The final output goes through an FFN layer and produce an embedding for regression or classification task. The proposed model is tested on 8 datasets and achieves significant improvements over prior papers.

### Strengths
1. Crystal materials property prediction is a complicated natural science task. I think the authors did a good job on delineating and explaining the concepts of this task, and break down break down into smaller modules easier to understand.
2. In section 3.3, while I think the contents are organized well by explaining the architecture of each sub-module one by one, it would be better to further explain the motivations behind each sub-module, since the proposed system is large and complicated. I can see section 4.2 gives some hints, but some more elaborated explanations would be better.
3. The authors did a quite thorough analysis on model depth and other hyper-params, on up to 8 datasets, comparing against 6 baselines. The results look promising and convincing.

### Weaknesses
1. In section 3.1.3, if I understand correctly, $u'$ and $v'$ actually represent edges? If so, it's better to use $e$ notations to differ from the atom nodes. If this purely represents the angle between edges, pls make this definition more clear and draw connections with $t_{ijk}$ from Fig. 1. The current description lacks clarity on whether $u'$ and $v'$ denote specific edges or are abstract representations of the angle between edges, which makes it difficult to follow the subsequent mathematical formulation. A more precise definition, relating these symbols to the crystal structure and the $t_{ijk}$ notation, is needed.
2. In section 3.2, I understand the motivations of adding positional encoding. But I hope authors can give more insights on why multiple encodings need to be used? What if you only choose 1 or 2? Some ablation studies on this point would be helpful. The paper introduces multiple positional encodings, but the rationale for using all of them is not fully explained. It is unclear how each encoding contributes to the model's performance and whether some encodings are redundant or more important than others. A more detailed explanation of the purpose of each positional encoding, along with ablation studies to justify their inclusion, would strengthen the paper.
3. There are many existing works on crystal materials property predictions. For example, [1, 2] uses GNN and contrastive learning to predict density of states, and [2] uses prototypical classifiers to analyze crystal structures. These works are worth discussing in the related work. The related work section should be expanded to include recent advances in crystal materials property prediction, especially those employing GNNs and contrastive learning techniques. The current related work section overlooks relevant studies that could provide a more comprehensive context for the proposed method.
4. To facilitate understanding, it would be better if you can use a running example (e.g., one simple crystal structure) like Fig 2 to explain how each module and inputs/outputs are hooked. The paper would greatly benefit from a step-by-step walkthrough of how the proposed model processes a simple crystal structure. This would make it easier for readers to understand how the different modules interact and how the inputs are transformed at each stage.

### Questions
1. I understand you used kNN to build up edges between atoms. I wonder what if you choose k=8 or k=6. How much difference does it make? Also, is it for simplicity purpose that you set the same k for all atom nodes?
2. For GwT, it seems that only the neighboring edges are added through $e_{ij}$, why it can capture long-range interactions? Do you expect that when N grows larger, it keeps drawing information from more distant neighbors?
3. How is the speed when training such a model? Are all the sub-modules trained together? Is there any speed analysis?
4. I didn't see $t_{ijk}$ in Fig 4. Is it used in encoding?
5. For edge-engaged transformer graph convolution, does it involve any convolution operations in Fig. 4 (a)?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

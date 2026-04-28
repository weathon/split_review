# Graph Vision Networks for Link Prediction

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6

## Abstract
The potential of the vision modality for enhancing graph structural awareness has long been overlooked in the mainstream graph neural network (GNN) community. In this paper, we propose a simple yet effective framework called Graph Vision Networks (GVN), which first incorporates vision awareness into Message Passing Neural Network (MPNN) and achieves effective performance for link prediction, highlighting this unexplored but promising direction. Specifically, GVNs transform graph structures into images and extract Visual Structural Features (VSFs) from those images, where VSFs are considered a novel type of structural feature. Similar to previous structural features, VSFs also mitigate the limitations of traditional MPNNs in expressive power and substructure awareness. Additionally, unlike most previous heuristic-based structural features (e.g., common-neighbor-based and path-based ones), which typically depend on fixed structural priors, VSFs are adaptive and capable of capturing varying structural insights to better suit different scenarios. Extensive experiments across seven commonly used benchmark datasets demonstrate that GVNs and their variants can significantly enhance MPNNs in link prediction tasks. Additionally, the straightforward design of the framework makes it highly compatible with current methods, providing additional performance gains to achieve new state-of-the-art performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes the Graph Vision Networks (GVN) for link prediction, which is designed to deal with the potential limitation of HSFs that it can only be derived based on the pre-defined structural prior and thus lacks sufficient adaptability to diverse real-world scenarios.

The core idea of GVN is very simple, it interprets either a link-centered subgraph or a node-centered subgraph as visual images and then extracts visual features from them as the structure features.

### Strengths
1. The idea is simple and the experiments show the effectiveness.

### Weaknesses
1. The technical novelty is limited. 
2. The method is not convincing. It first transforms the graph data to visual modality and extracts the visual features as the structural features, which is expected to be more effective than the HSFs learned based on structural priors in graph modality. Intuitively,  the visual features are more capable of learning appearance features or semantic features. In contrast, the graph data should have more expressive power than the visual modality in terms of the structural features.

### Questions
It is suggested to given more theoretical analysis and qualitative comparison to show why the method can learn more effective structure features from the visual modality than the graph modality.

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
2

### Summary
This paper focuses on the link prediction task. The authors introduce Graph Vision Network (GVN). By integrating vision awareness into MPNNs for link prediction, GVN models can adaptively extract learnable visual structural features (VSFs). Moreover, the authors propose two models under GVN framework: GVN-Link and GVN-Node. Experimental results demonstrate that the proposed method establishes new SOTA for link prediction.

### Strengths
1 The writing and the organization of this paper are generally OK.

2 Integrating vision modality into MPNNs for link prediction sounds interesting.

### Weaknesses
1 The motivation for incorporating vision modality into MPNNs for link prediction should be better clarified and discussed. Why is this design effective? Any theoretical evidence? Maybe a dedicated section for this discussion could be valuable.

2 The counterpart methods used for experimental comparison seem not SOTA enough. The authors should compare some 2024 SOTAs.

3 Minor Issues:  Ln 32 on Page 1, ‘Empiically’ should be ‘Empirically’

### Questions
See above weaknesses.

### Soundness
3

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
5

### Summary
This paper proposes a Graph Vision Networks (GVN) framework aimed at improving the expressive power of Message Passing Neural Networks (MPNNs) in link prediction tasks by integrating structural visual modalities. Extensive experiments on multiple datasets show that the framework exhibits potential in improving prediction accuracy and model robustness.

### Strengths
Originality: The idea of embedding local structural information of graphs using visual models is innovative. 

Quality: The author has demonstrated good performance across multiple datasets, particularly in challenging large-scale graph datasets.

### Weaknesses
1. While the idea of using visual modalities to model local neighborhoods is novel, the techniques utilized in this manuscript are very simple. For instance, the use of simple attention mechanisms to integrate node and neighborhood features. The attention mechanism, while computationally efficient, may not be sufficient to capture complex relationships between node features and their visual representations. More sophisticated fusion techniques, such as those that incorporate multi-head attention or learnable gating mechanisms, could potentially yield better results. The current approach risks underutilizing the rich information present in the visual modalities.

2. The author employs the graph visualizer (GV) to generate image modalities of subgraph structures. So what distinguishes the image modalities generated by GV for two isomorphic subgraphs? Are they random or identical? It appears that the improvement in representation learning performance is highly dependent on the effectiveness of GV. The lack of clarity on how GV handles isomorphic subgraphs raises concerns about the robustness of the approach. If the visual representations are identical for isomorphic subgraphs, the model might struggle to differentiate between them, limiting its expressive power. If they are random, the training process may become unstable and difficult to converge. The dependence on GV without a clear understanding of its behavior is a significant weakness.

3. The title and abstract of this manuscript are overly concise. It's hard to understand the work's significance and contributions.

4. The manuscript lacks a framework diagram to illustrate the proposed methodology, which could enhance clarity and comprehension.

5. The presentation of equations in the manuscript is uneven. For example, formulas in the PRELIMINARIES section are numbered, while those in the GRAPH VISION NETWORKS section are not, leading to potential confusion.

6. The writing quality of the manuscript requires improvement, with multiple errors. For instance, in the third paragraph of the INTRODUCTION, the quotation marks around “identity” are incorrectly used.

### Questions
Please see the Weaknesses section.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The author noticed that the MPNN model based on message passing can only obtain coarse-grained structural feature information, which makes the model unable to adaptively model fine-grained structural features, which limits the expressive power of the model. Therefore, inspired by Das et al., the author proposed to use the visual modality of the graph to provide fine-grained structural features for the model, and proposed the GVN model. The model first generates edge-oriented k-order subgraphs and node-oriented k-order subgraphs based on the query node pairs, and visualizes these subgraphs as 2D images. Then the cross-attention model is used to fuse the image features with the node features of the graph, and finally the readout module is used to implement the downstream prediction task.

### Strengths
1. Well-written, clearly organized, and easy to read and understand
2. The motivation of the article is clear. It is timely and necessary to use image modality for link prediction task on graphs.
3. Evaluating the model's effectiveness on multiple datasets with different scale and types.

### Weaknesses
1. The innovation of the method proposed in the article is relatively neutral. The main innovation of this article is to classify and discuss link images and node images. The remaining designs are just stacking existing modules (GNN, cross-attention, ResNet). First, inspired by the prior work, the authors use images to express the local structure of the graph. Secondly, the article uses the existing pre-trained visual encoding model to extract image features. Finally, the fusion of visual features and graph structure features utilizes the existing cross-attention.

I think the authors can further explore this idea in the following aspects. First, how to construct image representations of graph structures, such as the color and shape of nodes, etc. can be further explored. Secondly, how to construct effective image encodings of graphs instead of using existing pre-trained ResNet models can be explored. For example, can the features extracted by the visual encoder be used to reconstruct the local structure of the graph (regression graph adjacency matrix)?

2. The article claims to construct an adaptive fine-grained structure feature. However, the article only uses the image modality of the graph structure (which may be considered a fine-grained graph structure representation, but I have doubts about this), and cannot express adaptability.

3. There are some typos in the article, such as the period in line 025, the singular form of produce, and the misspelling of Empirical in line 032.

### Questions
1. What does $lO(\cdot)$ mean in Section 4.3?
2. There is already a projector in the formula on line 215, and there is another projector in the formula on line 220. The expressiveness of two linear projectors put together is the same as that of one projector because the product of two matrices is equivalent to one matrix.
3. Why are there no mapping matrices $W_Q, W_K, W_V$ in cross-attention?

### Soundness
3

### Presentation
3

### Contribution
2

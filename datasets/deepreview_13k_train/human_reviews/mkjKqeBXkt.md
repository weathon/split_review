# KITS: Inductive Spatio-Temporal Kriging with Increment Training Strategy

- Decision: Reject
- Scores: 6, 6, 5

## Abstract
Sensors are commonly deployed to perceive the environment. However, due to the high cost, sensors are usually sparsely deployed. Kriging is the tailored task to infer the unobserved nodes (without sensors) using the observed source nodes (with sensors). The essence of kriging task is transferability. Recently, several inductive spatio-temporal kriging methods have been proposed based on graph neural networks, being trained  based on a graph built on top of observed nodes via pretext tasks such as masking nodes out and reconstructing them. However, the graph in training is inevitably much sparser than the graph in inference that includes all the observed and unobserved nodes. The learned pattern cannot be well generalized for inference, denoted as \textit{graph gap}. To address this issue, we first present a novel \emph{Increment} training strategy: instead of masking nodes (and reconstructing them), we add virtual nodes into the training graph so as to mitigate the graph gap issue naturally. Nevertheless, the empty-shell virtual nodes without labels could have bad-learned features and lack supervision signals. To solve {\chengr these issues}, we pair each virtual node with its most similar observed node and fuse their features together; to enhance the supervision signal, we construct reliable pseudo labels for virtual nodes. As a result, the learned pattern of virtual nodes could be safely transferred to real unobserved nodes for reliable kriging. We name our new \underline{K}riging model with \underline{I}ncrement \underline{T}raining \underline{S}trategy as KITS. Extensive experiments demonstrate that KITS consistently outperforms existing kriging methods by large margins, e.g., the improvement over MAE score could be as high as \textbf{18.33\%}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses the challenge of inferring unobserved nodes using observed source nodes. While several inductive spatio-temporal kriging methods utilizing graph neural networks have been previously proposed, they often do not account for the discrepancies between the sparsity of training data and inference data (as the 'graph gap').

The author introduces an approach that adds virtual nodes into the training graph. This is done by 1) improve bad-learned features by finding similar nodes/feature fuse (Reference-based Feature Fusion module) 2) improve supervision signals by construct reliable pseudo labels for virtual nodes (Node-aware Cycle Regulation). Authors also show extensive experiments on 8 datasets with ablation study to support the method.

### Strengths
Admittedly, I am not a domain expert for inductive spatio-temporal kriging methods based on GNN, I do find this paper is:
* Well-written, and enjoyable to read.
* This looks like a novel method to address the sparsity gap between training graph and inference graph.

### Weaknesses
 * My main concern is that the introduction of virtual nodes does not add additional information to the dataset. Consequently, my intuition is that this strategy is more effective when the dataset size is small. In the case of the benchmark datasets, which contain a limited number of spatial data points (ranging from a maximum of 883 to a minimum of 80), the approach seems advantageous. However, in scenarios where there is a larger denser spatial dataset, it's worth considering whether the issue of sparsity remains as significant. Would the gap in sparsity still present a challenge in extensive populated spatial data environments? But again, I am not a domain expert for inductive spatio-temporal kriging methods based on GNN, maybe this is indeed the usual dataset size for this line of work. I am happy to change my score if this gets justified.

* This paper employs a thresholded Gaussian kernel to construct the adjacency matrix A among nodes, setting the values to zero when distances exceed a certain threshold. Have the authors explored the possibility of using non-stationary kernels or neural network-based kernels as alternatives?

### Questions
* When aggregating spatio-temporal features from neighboring nodes, is it worth exploring some attention mechanism to gain more global information (especially with so many timesteps in the datasets)?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses a spatio-temporal krigging problem. This is modeled as a node prediction task using graph convolution neural network (GCN) whose convolution operator is learned to compute the feature embeddings for each node, taking into account its topological connection to others (i.e., a training graph). 

The learned weights of the convolution operator can be applied to any topological graphs that contain the training graph, thus enabling inductive inference on new node: a forward pass of the (learned) convolution over an expanded graph that includes incorporate new connections to unobserved nodes will predict the features for those nodes, which can be subsequently input to a feed-forward net for node prediction.

Previous approaches addressing this problem often trains the GCN on the observed (training) part of the entire graph, which is later used to perform inductive inference on the unobserved (test) part of the graph. Their performance might therefore suffered from the disparity or gap between the train and test graphs. This is what this paper aims to address.

This is based on three main ideas:

Graph Augmentation (Increment Strategy): Observed nodes are sampled. For each observed node, a virtual node and a connection to the observed node is created. The virtual node's connection to the neighborhood of the observed node is also randomly generated. Multiple such augmented graphs are generated to train the GCN so its learned convolution is robust to potential variation in the structure of the (unseen) test graph. Original features for the virtual nodes are set to be zero. Also, features of the same node reported or computed within a window of +/- m steps are also concatenated before passing through the GCN

Feature Fusion between Virtual & Observed Nodes: Generated features of virtual nodes and observed nodes from the above steps are paired based on a similarity notion. Paired features are concatenated and passed through a (learnable) neural net, which returns the fused features for the virtual node. 

Pseudo-Label Generation: Pseudo-labels for virtual nodes are first generated using the learned GCN-based node prediction model. The model is then re-trained using only the pseudo-labels to predict labels of the observed nodes. The losses in two training phases can be combined to be optimized together.

### Strengths
The presented ideas are refreshingly interesting & novel to me. 

The problem being addressed is also practically significant. The gap between the train and test graphs in the inductive setting of node prediction is always a fundamental issue, which needs an in-depth treatment.

The empirical studies are sufficiently extensive, showing good results across a variety of datasets. 

Comprehensive ablation studies showing the effectiveness of each idea is also included.

### Weaknesses
Overall, I like this paper. It motivates well a fundamental issue of inductive inference with GCN.

But I do have a few concerns or questions regarding both the position, presentation and empirical evaluation of this paper that I want to discuss with the authors (mostly out of curiosity & for constructive feedback)

1. The main position of this paper is grounded in the spatio-temporal setting but the proposed treatment does not seem to have anything specific to the temporal aspect. The aggregation of temporal feature within +/- m steps is kind of a random treatment to me. I do not see a very particular reasoning why doing so makes sense. What if such aggregation erases important small-scale variation patterns in the time-series data? Furthermore, m is a value dependent on the nature of the data so even though the ablation studies conclude that m = 2 gives best result, it is still specific to the few set of experimental data and that should not be a generic guideline to choose m.

2. Although comparison with recent pure graph-based approaches has been well presented, I am still curious to know how well the proposed approach improves over a hybrid approach that integrates GCN with traditional krigging techniques. For example, the series of work on graph convolutional Gaussian processes. There is quite a substantial volume on that & I think the authors have not discussed that in the literature review. Such techniques can be used to address this krigging problem. After all, if I remember correctly, Gaussian processes were referred to as krigging in the past (in geo-statistics).

3. Last, in terms of the presentation, I believe it would be better if the authors spend some space on summarizing GCN which will highlight better the essence of transferability in the inductive setting of krigging. Otherwise, while the current presentation is fine for people who are familiar with graph neural network, it will still leave a lot of gap for generic readers.

### Questions
Based on the above, I have the following questions:

1. Could the authors position this work with the other literature on graph convolutional GPs, which is an integrative approach combining both elements of GCN & a traditional non-graph krigging method (i.e., GPs)?

2. Could the authors elaborate more on why this paper is specifically positioned in the temporal-spatial setting even though the proposed technique does not really have any new innovations for temporal modeling? I might have missed something important here.

3. It will be good to run some comparative experiments with a few representative graph convolutional GPs.

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
I've reviewed this paper for a previous conference and have discussed at length its merits and negative aspects with a long back and forth discussion with the authors. Unfortunately, none of my comments (and that of the other reviewers) were apparently taken into account as this submission is basically unchanged w.r.t. the previous iteration. Furthermore, several of the additional results presented during the previous discussion haven't been included in this version.

The paper introduces KITS, a novel approach for kriging based on graph neural networks. The main contribution of the paper is the introduction of an augmentation strategy based on the idea of adding virtual nodes to the input graph at training time. The augmentation strategy is then paired with a self-supervised training strategy yielding good results on several benchmark datasets. The method is presented as a solution to what the paper defines as the "graph gap", i.e., a mismatch between the graph at training and test time. Overall, the paper paper has merits, however, I do have some serious concerns that prevent me from recommending acceptance.

### Strengths
* The introduced data augmentation strategy paired with the self-supervised training routine is novel and appealing.
* Good empirical performance.
* Very good presentation.

### Weaknesses
 * There is a conceptual flaw in the main motivation behind the introduced methodology. While it is straightforward to see why using a drastically different graph at training and inference time is a problem ("graph gap" in the paper), I do not understand why every target node should be reconstructed in a single forward pass. This approach seems to conflate the inherent task of kriging with a specific, and perhaps unnecessary, evaluation protocol.
* Reconstructing a single node at a time would remove the "graph gap", this would be the proper way of carrying out the evaluation. By reconstructing all target nodes simultaneously, the method introduces an artificial dependency between predictions that is not present in the actual kriging task. This approach also obscures the true performance of the model on individual node predictions.
* After removing nodes for training, graphs can become sparse. However, this issue is only caused by the removal of nodes for evaluation, i.e., it is an issue of the training/evaluation procedure and not an inherent issue of kriging methods. This would not be a problem in any real-world application as you would eventually train the model on the full graph. The paper does not adequately address the implications of this artificial sparsity on the validity of the results.
* The considered datasets are quite small, removing many nodes at random might result in disconnected graphs that would explain the poor performance for some of the baselines. The paper does not provide a thorough analysis of the graph connectivity after node removal, and how this might affect the performance of different methods. This lack of analysis makes it difficult to ascertain whether the reported improvements are due to the proposed method or simply an artifact of the experimental setup.

### Questions
--

### Soundness
1 poor

### Presentation
3 good

### Contribution
3 good

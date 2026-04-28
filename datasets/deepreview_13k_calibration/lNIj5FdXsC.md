# Recurrent Distance-Encoding Neural Networks for Graph Representation Learning

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 6, 3, 6

## Abstract
Graph neural networks based on iterative one-hop message-passing have been shown to struggle in harnessing information from distant nodes effectively. Conversely, graph transformers allow each node to attend to all other nodes directly, but suffer from high computational complexity and have to rely on ad-hoc positional encodings to bake in the graph inductive bias. In this paper, we propose a new architecture to reconcile these challenges. Our approach stems from the recent breakthroughs in long-range modeling provided by deep state-space models on sequential data: for a given target node, our model aggregates nodes at different distances and uses a parallelizable linear recurrent network over the chain of distances to provide a natural encoding of its neighborhood structure. With no need for positional encoding, we empirically show that the performance of our model is competitive compared with that of state-of-the-art graph transformers on various benchmarks, at a drastically reduced computational complexity. In addition, we show that our model is theoretically more expressive than one-hop message-passing neural networks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work introduces a novel graph learning method that pools long-range information by aggregating nodes at different distances and using a linear recurrent network, leading to a computational efficient method that is competitive with state-of-the-art approaches for graph learning.

### Strengths
- The evaluation is very thorough and the results validate and support the effectiveness of the proposed method. The computational effectiveness of the proposed model compared to equivalent transformer models (Table 4) is very good.
- The proposed method is benchmarked against a wide range of methods and on multiple benchmarks.
- Transformer models are good at modeling long-range interactions in graphs, and have been outperforming MPNN models, they however struggle with scaling and require custom encoding of the node positional embedding. The proposed approach is simple and intuitive and provides an alternative path towards solving long-range graph problems.

### Weaknesses
1. A sensitivity analysis of GRED with respect to the choice of K is missing.
2. The training efficiency analysis is conducted against a transformer model only, but it would be useful to understand how this method compares to MPNNs. In particular, each node will have its own sequence of sets of nodes at distance k, so there might not be any shared computation that can be leveraged like in iterative 1-hop message passing methods. This could lead to significant computational overhead, especially for larger values of K and larger graphs, which needs to be quantified and compared against the computational cost of MPNNs. The analysis should include a breakdown of the computational cost of each step, including the preprocessing step of computing the k-hop neighbors, the aggregation step, and the recurrent network step.


### Questions
- How would this method perform on non long-range benchmarks? Would it underperform compared to MPNNs who might only need a local receptive field to solve a task?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a model architecture, GRED, for graph tasks by adopting a recurrent neural network (RNN) to propagate hidden states through multiple layers. It claims that the new architecture is more effective, utilizing the information of large neighborhoods with high efficiency, and theoretically proving the expressiveness. It also empirically shows that the performance of GRED is better than state-of-the-art graph transformers.

### Strengths
1.  The paper proposes a way to utilize RNN to adopt hidden states through multiple layers. It claims that the new method helps improve long-range information processing.
2. The paper compares the proposed method on multiple benchmarks, and demonstrates its effectiveness against traditional GNN models.
3. The description of the proposed method is well-written and easy to understand, though figure 1(a) is a bit unclear about what the "skip" stands for.

### Weaknesses
1. For the training efficiency evaluation, it would be nice to include the memory consumption for different methods. Also, the performance gap on the task between GRIT and GRED is still significant, which makes the comparison a bit unfair. It would be better to compare with the architecture that has similar task performance. Specifically, the reported speedup is not very meaningful without considering the absolute performance difference. A more detailed analysis of the computational cost, including FLOPs, would also be beneficial.
2. The method introduces a new hyperparameter K to be tuned. It would be nice to show how K is selected, and how the different selections of K can affect the task performance. The paper should include an ablation study on the impact of K, showing how performance varies with different K values, and provide guidelines for selecting an appropriate K for different graph structures. It is also unclear if the optimal K is consistent across different datasets.
3. Although the technique helps increase the range of nodes the model can process, unlike the graph transformer-based method, the distance is still limited by the selection of K and the number of layers of the model. It would be good to show some insights into how that super long-distance information affects the model performance. The paper should also discuss the limitations of the receptive field imposed by K and the number of layers, especially for graphs with large diameters. It would be beneficial to analyze the model's performance on graphs with varying diameters to understand the impact of this limitation.

### Questions
The following papers seem related as well:
1. Graph Transformers: Representing Long-Range Context for Graph Neural Networks with Global Attention, NeurIPS 2021
2. Issues with attention for long-range reasoning: Lite Transformer with Long-Short Range Attention, ICLR 2020

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a new graph learning architecture called Graph Recurrent Encoding by Distance (GRED). GRED aims to address the challenges faced by existing approaches, such as message-passing neural networks (MPNNs) and graph transformers, by efficiently encoding information from distant nodes while avoiding the need for ad-hoc positional encodings. The paper provides a detailed explanation of the GRED architecture and supports its claims with theoretical analysis and empirical results.

### Strengths
1. Theoretical Analysis: The paper provides a theoretical analysis of the expressiveness of GRED, demonstrating its superiority over one-hop MPNNs. This analysis adds depth to the understanding of the method's capabilities. Furthermore, the authors provide an interesting analysis regarding the RNN filtering of the k-hop neighbor features.

2. The presentation and clarity of the paper are very good. The authors provide comprehensive explanations of the key components of GRED, which is crucial for readers trying to understand the architecture at a deeper level. The theoretical analysis is rigorous, and the empirical results are presented in a well-organized manner, contributing to a comprehensive understanding of GRED's performance.

### Weaknesses
1. Firstly, the novelty of the proposed architecture is somewhat limited, as there are already several similar approaches in the field that operate on K-hop neighborhoods in a similar manner. While the combination of permutation-invariant neural networks and linear recurrent networks is a sensible choice, it may not present a significant departure from existing methods. Specifically, the proposed method is very similar to [1], which proposed the following update rule: $h_u^{(t+1)} =COM(h_u^t, AGG_{u,1},..., AGG_{u,k} )$. The main difference is that the proposed approach uses an RNN for the $COM$ function. Moreover, there is no proper discussion of other k-hop approaches such as [2]. The paper lacks a detailed comparison to methods that utilize similar k-hop aggregation strategies, such as those employing attention mechanisms or different forms of aggregation functions. The current discussion does not adequately differentiate GRED from these existing methods, making it difficult to assess the true novelty of the approach. The use of an RNN for the COM function, while a distinction, needs further justification as to why this specific choice provides a significant advantage over other aggregation techniques. 

2. Secondly, the experiments in the paper are conducted on a relatively limited set of datasets, focusing on long-rage benchmarks, and the absence of experiments on benchmark datasets like TUDatasets raises concerns about the generalizability of the proposed model. Expanding the experimental evaluation to a wider range of datasets would strengthen the paper's claims. The focus on long-range benchmarks is understandable given the motivation, but the lack of evaluation on more standard graph datasets makes it hard to assess the method's performance in more general scenarios. The paper should include experiments on datasets with varying graph sizes, densities, and structural properties to provide a more comprehensive evaluation. 

3. A notable weak point of the paper is the unavailability of the source code for the proposed model. This omission hinders the reproducibility and transparency of the research. Releasing the source code is not only a common practice in the research community but is also crucial for enabling other researchers to validate and build upon the work presented in the paper.

### Questions
1. Could the authors provide a more in-depth comparative analysis of their approach against existing methods that operate on k-hop neighborhoods? Highlighting specific strengths or weaknesses in comparison to these related approaches would help better position the novelty of this work.

2. Considering that experiments are conducted on a limited set of datasets, could the authors discuss the generalizability of their proposed architecture to a wider range of datasets, including TUDatasets?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposed a new architecture for the graph learning, aggregating nodes with different distance and using a parallelizable linear recurrent network to encode the information flow while keeping the weights from vanishing.

### Strengths
1. paper is well written and easy to follow
2. experiment is good

### Weaknesses
1. RNN here is strange, the assumption here is that the information flow from K-hop to K-1 hop. but information can also go "outward", from k-2 hop to k-1 hop. RNN is not good to model the graph information
2. I assume all the GNN drawback will also be here in this Model (over smoothing, etc). The model can be regarded as another interpretation of massage passing(even though the weight is different), for the target node, the model will aggregate all the K-hop node information

### Questions
1. how the performance like if we change LRU to the vanilla RNN. seems LRU for the long range information pass is the key factor to win against MPNN.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

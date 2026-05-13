# Random Walk Diffusion For Graph Generation

- Decision: Reject
- Scores: 6, 3, 6, 3

## Abstract
Graph generation addresses the problem of generating new graphs that have a data distribution similar to real-world graphs. Recently, the task of graph generation has gained increasing attention with applications ranging from data augmentation to constructing molecular graphs with specific properties. Previous diffusion-based approaches have shown promising results in terms of the quality of the generated graphs. However, most methods are designed for generating small graphs and do not scale well to large graphs. In this work, we introduce ARROW-Diff, a novel random walk-based diffusion approach for graph generation. It utilizes an order agnostic autoregressive diffusion model enabling us to generate graphs at a very large scale. ARROW-Diff encompasses an iterative procedure that builds the final graph from sampled random walks based on an edge classification task and directed by node degrees. Our method outperforms all baseline methods in terms of training and generation time and can be trained both on single- and multi-graph datasets. Moreover, it outperforms most baselines on multiple graph statistics reflecting the high quality of the generated graphs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Existing diffusion-based graph generation models are designed for generating small graphs and suffer from scaling to large-scale graphs. To scale diffusion-based models to generate large graphs, this work proposes ARROW-Diff, Auto Regressive RandOm Walk Diffusion, for graph generation based on random walk diffusion. ARROW-Diff leverages order-agnostic Autoregressive Diffusion Models (OA-ARDMs) to sample random walks from the training graphs, and further encompasses an iterative procedure that generates the final graph by utilizing a Graph Neural Network (GNN) model to filter out invalid edges from sampled random walks. Experiments on both a single, large-scale graph setting and the setting of multiple, small graphs demonstrate the efficiency and scalability of ARROW-Diff.

### Strengths
1. This work scales the diffusion-based approaches for large-scale graph generation in a random walk diffusion fashion. Inspired by node2vec, ARROW-Diff utilizes OA-ARDMs to sample random walks from training graphs, and then leverages an iterative procedure to construct the final graph based on an edge classification task directed by node degrees from the sampled random walks. The idea is natural and the ARROW-Diff framework is sound.

2. The authors did a great job of introducing the background and related work. The illustration of the ARROW-Diff procedure, especially Figure 1, is clear and easy to understand.

3. Regarding experiments on the single, large-scale graph setting, ARROW-Diff outperforms the existing graph generation baselines by a certain margin in terms of the runtime, and also generates graphs with higher quality than baselines in terms of relatively more complex graph metrics (e.g., triangle count, edge overlap).

### Weaknesses
1. The main contribution of this work is leveraging OA-ARDMs to generate large-scale graphs efficiently in a random walk diffusion fashion. Although ARROW-Diff demonstrates its efficiency and scalability empirically, the contribution in terms of the idea is not very novel, and the authors did not give any theoretical justification (e.g., time complexity analysis) for why ARROW-Diff is more efficient than existing graph generation methods. Specifically, the use of random walks, while inspired by node2vec, doesn't inherently guarantee better performance or efficiency without a formal analysis. The lack of such analysis makes it difficult to ascertain the true advantage of this approach over other diffusion-based methods, particularly in terms of computational cost and convergence properties.

2. Although ARROW-Diff is able to generate graphs much more efficiently than baselines in the setting of multiple, small graphs, the quality of generated graphs by ARROW-Diff does not outperform baselines in terms of all three metrics. It is concerning that while the method shows speed improvements, it does not consistently achieve superior graph quality across all metrics in the multiple small graph setting. This raises questions about the trade-off between efficiency and quality, and whether the proposed method is truly suitable for all graph generation tasks. The fact that it excels in the single large graph setting but not consistently in the multiple small graph setting suggests a potential bias or limitation in the method's design or training process.

3. (Minor) I did not find any appendix for this work in the supplementary materials. It would be great if the authors could further describe the details of the implementation of ARROW-Diff and the experiments.

### Questions
1. Regarding the first point in the Weaknesses, I wonder if the authors could provide a more theoretical analysis of the complexity of ARROW-Diff.

2. Regarding the second point in the Weaknesses, I wonder if the authors could discuss further whether ARROW-Diff is able to generate high-quality graphs in the single, large-scale graph setting while not outperforming baselines in the settings of multiple, small graphs.

3. Recently, there is another paper related to diffusion-based graph generation [1]. With empirical analysis revealing that permutation-invariant diffusion models are harder to learn than their non-permutation-invariant counterparts, [1] proposes a non-permutation-invariant diffusion model for graph generation. I wonder if the authors could discuss about permutation-invariant vs non-permutation-invariant models for the graph generation.

[1] Yan, Q., Liang, Z., Song, Y., Liao, R., \& Wang, L. (2023). Swingnn: Rethinking permutation invariance in diffusion models for graph generation. arXiv preprint arXiv:2307.01646.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a generative model to generate edges of a graph. It is based on Order Agnostic AutoRegressive Diffusion Models (OA-ARDM) that capture dependencies of the input and are robust to the order in which intermediate samples are generated. The approach is an adaptation of OA-ARDM (Hoogeboom et al., 2022) to graphs where each sample at some diffusion step t is a random path of size t in the graph. The model is trained by masking those paths and predicting them.

### Strengths
In terms of methodology, the proposed approach is a straigthforward adaptation of (Hoogeboom et al., 2022) to sequences made of random walks in a graph. The paper is well-written and the method seems to obtain train faster than baselines assuming that the number of iterations (i.e. sampled paths/random walks) is relatively small and their length is short.

### Weaknesses
1) At inference time, the method relies on generating a sufficient number of paths with appropriate length. Assuming that the training graphs are densely connected (i.e. a large number of pairs of nodes are connected by an edge), the number of edges in the graph is quadratic in the number of nodes, and the number of paths increases significantly as their length increases. It is unclear how the proposed method is robust and representative of all the possible paths in the graphs. In particular, the method would miss a lot of edges if it does not sample enough random walks. The paper does not provide a theoretical analysis or empirical study on how the number of sampled paths affects the quality of the generated graph, especially for large and dense graphs. It is also not clear how the method ensures that the sampled paths cover the diversity of the graph structure, rather than focusing on a few highly connected regions. The sampling strategy seems to prioritize densely connected nodes, potentially neglecting less connected but structurally important parts of the graph.

Similarly, during training, the method only considers local information in the graph (i.e. random edge sequences) and not its global structure. Therefore, for large dense graphs, the number of edges becomes quadratic in the number of nodes and it might be difficult to sample enough random walks to be representative of the connectivity in the graph. The method does not explicitly model long-range dependencies or global graph properties, which may limit its ability to generate graphs with complex structures. The reliance on short random walks might not capture the overall connectivity patterns of the graph, especially for graphs with high diameter.

2) In terms of evaluation, the purpose of the task described in Section 5.2 (graph generation from a single-graph dataset) is not clear to me. The purpose of graph generation is usually to generate multiple diverse graphs that follow the same distribution as the graphs forming a dataset. If the training set contains a single graph, then it is not clear what the distribution of the training set should be other than a singleton. A naive baseline for the task would be an autoencoder whose decoder always returns the same graph as the training graph. It also seems that the proposed method corresponds to a (denoising) autoencoder that simply tries to reconstruct the edges of a single graph in the setup of Section 5.2. This would explain why the proposed method outperforms the baselines in this setup. The evaluation seems to focus on reconstructing the training graph rather than generating novel graphs, which does not align with the typical goals of generative modeling. The reported metrics might be biased towards the method's ability to memorize the training graph rather than its generalization capability. The baselines are not designed for this single graph reconstruction task, making the comparison unfair.

The evaluation with the reported baselines then seems unfair since many baselines are trained to promote novelty and non-uniqueness (i.e., generating graphs that are not in the training set, and diverse). The scores reported in Table 2 seem to promote overfitting over a single sample/graph and does not really reflect the generative power of the different methods. The evaluation protocol needs to be revised to assess the ability of the method to generate diverse and realistic graphs, rather than simply overfitting to a single training instance.

3) The experiments in Section 5.3 and Table 3 are not convincing either. Digress and EDGE seem competitive with respect to all the evaluation metrics except training time (which may be reduced with more computing power). In generative models, an interesting metric is the inference time to generate new samples. The novelty and uniqueness score are not reported either. It is not clear if the reported training time advantage is significant enough to justify the limitations of the method. The paper does not provide a detailed analysis of the trade-off between training time and generation quality. The evaluation lacks a crucial metric, the inference time, which is important for practical applications. The absence of novelty and uniqueness scores makes it difficult to assess the diversity of the generated graphs.

4) The number of nodes of the generated graph is the same as the number of nodes of the training graph.

### Questions
1) What are the novelty and uniqueness scores of the different methods in Table 3?

2) How important is initialization for the generation process? Assuming that the number of steps L and the number of initial sampled random walks M are both large, do different sets of random walks tend to return the same value of p(n) in Step 11 of Algorithm 2?

3) The main purpose of using multiple GNN steps at inference time is to evaluate the degrees of nodes. Do you have ablation studies to see the impact of M and L for training? If M becomes large, then the training takes longer but does it improve generation scores? Same question for the length of the paths.

4) How does the method deal with permutation invariance? Assuming that the dataset contains multiple graphs that are all isomorphic (e.g. the graph with the edges (1, 2) and (2, 3) is isomorphic with the graph containing (3, 1) and (1, 2), or (1, 3) and (3,2)), will the values of p(n) converge to some canonical representation or will p(n) = 1/3 for all n in this case?

5) Same question for when the graph contains different nonisomorphic graphs, how does the method deal with permutation of nodes? How does the GNN differentiate the node IDs between different graphs?


Minor detail. The paper should mention that m in step 3 of Algorithm 1 is a Boolean mask.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a novel graph generation approach by designing the diffusion models on random walks. It uses an order agnostic autoregressive diffusion model to sample random walks from a given graph, and then uses a graph neural network to predict the edge set in the final graph. The paper claims that this approach can generate high-quality graphs that are similar to real-world graphs and can scale to very large graphs efficiently.

### Strengths
1.	The paper introduces a new perspective of applying diffusion models to graph generation by developing a diffusion process on the random walks.
2.	The paper demonstrates the scalability and flexibility of the proposed approach, which can handle both directed and undirected graphs, and both single-graph and multi-graph datasets.
3.	The paper provides extensive experiments and comparisons with several baselines on various graph metrics, showing the superiority of the proposed approach in terms of quality and speed.

### Weaknesses
1.	It is better for the authors to provide qualitative examples or visualizations of the generated graphs, which would help to illustrate the effectiveness and diversity of the proposed approach.
2.	Based on my understanding, the effectiveness and efficiency of the proposed methods are both sensitive to the parameter L. The authors should provide the necessary analysis on the selection of this parameter. Intuitively, when using the large L, the inference time would increase linearly. 
3.	In Table 2, the performance of the proposed method seems to vary a lot on graphs with different sparsity. It is better for the authors to provide more empirical analysis.

### Questions
Please provide several visualizations of the generated graphs. 
How does the parameter L influence the performance?
Is there a significant correlation between the performance of the proposed method and the sparsity of graphs? What is the relationship?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes a novel graph generative model for modeling very large graphs. The main idea is to sample random walks, which generate candidate edges for the current graph t, then a GNN will run on such a noisy graph and prune out some candidate edges. Such iteration is repeated until the graph is finalized. The key intuition of the paper is to use the sparsity of the graph obtained from the random walks, which can be handled properly by the GNN. To obtain those random walks, the paper proposes to use the BERT-like model to sample node id sequences.

### Strengths
The idea is pretty novel and it's interesting. The model tackles the dense graph generation problem elegantly by using two sets of model (random walk and GNN refinement.

### Weaknesses
1. Notation is unlcear. For example, it is not clear how equation 2 is computed, and what's the model like. When the authors say the random walks are sampled by the BERT-like model, it's not clear whether it's permutation-invariant or not since the BERT model doesn't come with the causal mask but with positional embedding.

2. it's not clear how the V_start is reset using node degree information.

3. In my understanding, the random walk sampling doesn't utilize any structural information of the (previous) generated graph. It must take the node feature information as input in order to work well. In this case, the proposed method can only generate graphs conditioning on node features. Since node features are not considered by NetGAN and EDGE, I suggest the author should highlight the difference.

4. Based on my comment 3, the author should also add graphite as one of the baselines.

5. I believe the Edge Overlap is the lower the better. If a model works well with high EO, it is simply because it memorizes the original graph structure. I don't think the comparison against the baseline is totally fair -- Arrow-diff has 50% EO while the others have ~1% EO

6. Is the result reported in EDGE and NetGAN trained with node features? if so, can you provide details about how the model is modified to do so?

7. Time complexity analysis is missing. It should be explicitly analyzed to demonstrate why the method is so efficient, this involves showing the detail of the used models (for random walk and GNN).

### Questions
See weakness, I'd like to change my rating if the concerns are addressed.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

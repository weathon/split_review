# Graph Transformers for Large Graphs

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
Transformers have recently emerged as powerful neural networks for graph learning, showcasing state-of-the-art performance on several graph property prediction tasks. However, these 
results have been limited to small-scale graphs, such as ligand molecules with fewer than a hundred atoms, where the computational feasibility of the global attention mechanism is possible. The next goal is to scale up these architectures to handle very large graphs on the scale of millions or even billions of nodes. With large-scale graphs, global attention learning is proven impractical due to its quadratic complexity w.r.t. the number of nodes. On the other hand, neighborhood sampling techniques become essential to manage large graph sizes, yet
finding the optimal trade-off between speed and accuracy with sampling techniques remains challenging.
This work advances representation learning on single large-scale graphs with a focus on identifying model characteristics and critical design constraints for developing scalable graph transformer (GT) architectures. We argue such GT requires layers that can adeptly learn both local and global graph representations while swiftly sampling the graph topology. 
As such, a key innovation of this work lies in the creation of a fast neighborhood sampling technique coupled with a local attention mechanism that encompasses a 4-hop reception field, but achieved through just 2-hop operations. This local node embedding is then integrated with a global node embedding, acquired via another self-attention layer with an approximate global codebook, before finally sent through a downstream layer for node predictions.
The proposed GT framework, named \frameworkname{}, overcomes previous computational bottlenecks 
and is validated on three large-scale node classification benchmarks.
We report a $3\times$ speedup and $16.8\%$ performance gain on \texttt{ogbn-products} and \texttt{snap-patents} compared to their nearest %or best 
baselines respectively, while we also scale \frameworkname{} on \texttt{ogbn-papers100M} with a $5.9\%$ improvement in performance

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes LargeGT for training graph transformers for large graphs. Neighborhood sampling usually samples at most 2-hop neighbors as in GOAT (Kong et al., 2023). The proposed method stores a matrix storing the sum of node features of 1-hop and 2-hop neighbors before training. Then sample 2-hop neighbors for a specific node and get the sum features from the matrix, which is at most 4-hop information for the node. It also adopts GOAT (Kong et al., 2023) as the global module. Experiments show it trains faster than GOAT.

### Strengths
1. The proposed neighbor sampling intuitively improves the model accuracy by getting information at most 4-hop away.
2. Extensive experiments are performed.
3. The writing of the proposed method is very clear.

### Weaknesses
1. The proposed neighbor sampling intuitively improves the model accuracy by getting information at most 4-hop away.
2. Extensive experiments are performed.
3. The writing of the proposed method is very clear.

1. The mechanism of why LargeGT runs faster than baselines like GOAT is unclear. Since the proposed neighbor sampling has a bigger input matrix than a simple 2-hop neighbor sampling method, does it run longer than the traditional method? The paper does not provide a clear analysis of the computational overhead of pre-computing and storing the neighbor feature sums, nor does it detail how this overhead compares to the runtime savings during training. It's unclear if the speedup is due to algorithmic efficiency or implementation details.
2. The runtime highly depends on the hyperparameter $K$, which is the number of nodes for sampling. Authors need to provide a fair and solid comparison with the traditional 2-hop neighbor sampling method. The paper lacks a detailed ablation study on the impact of $K$ on both runtime and model performance. A comparison with a standard 2-hop sampling method, with varying numbers of sampled nodes, would be crucial to understand the trade-offs. The current experiments do not sufficiently isolate the effect of the proposed sampling method from the choice of $K$.
3. Experiment performances are not explained well (see questions). The paper provides limited discussion on why certain baselines perform better on some datasets. For example, the superior performance of GOAT-local-δ on ogbn-products is not adequately addressed, nor is the significant performance boost of LargeGT on snap-patents fully explained. The lack of analysis makes it difficult to understand the strengths and weaknesses of the proposed method.

### Questions
1. In Table 2, why does GOAT-local-δ have better accuracy in ogbn-products?
2. For snap-patents in Table 2, why does LargeGT have much better model accuracy than all baselines?
3. For snap-patents in Table 3, why does the model accuracy drop when $K>50$?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes LargeGT, a scalable graph transformer for large-scale graphs. It uses fast neighborhood sampling and a local attention mechanism to learn local representations. These are integrated with global representations from an approximate global codebook. This framework overcomes previous computational bottlenecks, achieving 3x speedup and 16.8% better performance on benchmarks compared to baselines. LargeGT also scales to 100M nodes, advancing representation learning for single large graphs.

### Strengths
* The model's performance is thoroughly validated on large-scale graphs, demonstrating sufficient workload.
* Exploring base model architectures on graphs is a very valuable endeavor.

### Weaknesses
 * The efficiency analysis is incorrect. In Algorithm 1, it is required to gather 1/2-degree neighbors for each node, and then select k nodes. The process of selecting nodes is O(K), but if the graph is relatively dense, the complexity of gathering second-degree neighbors is O(N^2). This is a critical oversight, as the stated efficiency gains are predicated on a flawed analysis of the neighborhood sampling process. Specifically, the cost of identifying all 2-hop neighbors for a given node in a dense graph can approach O(N) for each node, leading to an overall complexity of O(N^2) for the entire graph, which is not accounted for in the paper's analysis.
* In Algorithm 1, some nodes are sampled with replacement, while some are sampled without replacement. It is uncertain whether this will introduce bias in the sampling. The inconsistent sampling strategy across nodes could lead to skewed representations, particularly if nodes with fewer neighbors are oversampled. This could lead to instability during training and impact the generalization performance of the model. The paper does not provide sufficient justification or analysis of the implications of this mixed sampling approach.
* It lacks some key baselines such as SGC[1], SIGN[2]. The absence of these baselines makes it difficult to contextualize the performance of the proposed method. SGC, with its simplified graph convolution approach, and SIGN, with its scalable inception architecture, represent important benchmarks in the field, and their exclusion limits the ability to assess the true novelty and effectiveness of LargeGT.

### Questions
See. Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
To scale graph models to large-scale graphs, MPNNs are often reduced to restricted receptive fields making them myopic, while Graph Transformers (GTs) fail because of their quadratic cost. This paper proposes a new framework for sampling sub-graphs to train a large GT that uses local and global modules to improve model performance and compute complexity.

### Strengths
- The authors propose a framework that leverage recent advances in graph transformer models, and address a critical challenge that limits the scalability of existing approaches, both MPNNs and GTs.  
- The introduction provides a great overview of the current challenges for large-scale graph learning, and does a great job at comparing MPNNs and GTs, while setting stage for key concepts like neighborhood sampling.

### Weaknesses
1. Baselines: LargeGT is compared to "constrained versions" of various baselines, notably all models are constrained to 2 hops only, while LargeGT has access to 4-hops worth of neighbors (in the local module). Including the non-constrained versions of these same baselines is critical for evaluation, even if they are more computationally demanding. Currently it is unclear whether adopting LargeGT leads to lower performance compared to state-of-the-art methods, at the expense of computational efficiency.
2. Additionally, no auxiliary label propagation or augmentations are used for the baseline methods, when they are used in methods reported in the OGB leaderboard. These enhancements are not altering the receptive field of the baselines, and thus shouldn't impact computational performance, but might improve classification performance. This should be taken into account when comparing with approaches that might still outperform the proposed method, even under constrained training (2-hop).
3. The main innovation can seemingly be credited to the use of the global codebook, so it is hard to define the main contribution of this work. If the focus of this work is combining all these different building blocks into a compute efficient framework, I would expect to see a more expansive breakdown of the computational costs of different components, memory usage and requirements. Notably, how is "Epoch time" defined in Figure 2? All models might be processing different amounts of data and thus might have different definitions of an "epoch" due to differences in sampling strategies. How many nodes does each model process in an epoch? Different models might require different numbers of epochs to converge, shouldn't total training time be more important?
4. [Minor] A lot of the content in the first 4 pages is repetitive.

### Questions
1. What are the memory constraints of using LargeGT compared to other baselines? How is the choice of batch size impacted by the choice of hyperparameter K? 
2. How important is the choice of a 4-hop neighborhood for the local module. Can the model still perform competitively given that it still has access to global information through the global module?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The author highlights that while transformers have demonstrated remarkable performance in tasks related to predicting graph properties, their application has been restricted to small-scale graphs due to computational limitations. Additionally, the author contends that the existing neighbor sampling method constrains the model's ability to consider more global information. Consequently, this paper introduces a comprehensive GT framework, with a focus on enhancing model capacity and scalability. The proposed framework, known as LargeGT, combines a rapid neighborhood sampling technique with a local attention mechanism and an approximate global codebook. Extensive experiments illustrate that by integrating local and global attention mechanisms, LargeGT achieves improved performance in node classification tasks. Notably, LargeGT demonstrates a 3× speedup and a 16.8% performance enhancement in specific node classification benchmarks when compared to their closest baseline models.

### Strengths
1. This paper is excellently composed, offering a straightforward narrative that's easy to follow. Notably, key terms and important experimental findings have been highlighted using various colors, resulting in an effective visual presentation.

2. The experimental results presented in this paper indicate that the proposed framework can achieve superior performance within a shorter training time.

3. The author introduces two significant challenges associated with handling large-scale graphs: scalability and constraints related to local information aggregation. These issues are prevalent and indeed worth discussing. As the author pointed out, computational resource requirements increase quadratically with the growing number of nodes. To address this, the author has proposed both a local and a global aggregation module. The former employs conventional sampling techniques to learn local representations, while the latter focuses on deriving insights from global node vector projections. Downstream predictions are then made based on both sets of representations. The problems raised, and the respective solutions are meaningful and coherent with each other.

### Weaknesses
Despite the fluent presentation, some concerns arise in this paper. Firstly, the level of novelty in this framework appears limited. It is apparent that this paper heavily relies on the previous work, GOAT, particularly the global module, which encodes mini-batch nodes using global graph nodes. This component was introduced in a prior paper. The other aspects are mainly focused on aligning local and global features. The framework appears more like an updated version of GOAT than a fundamentally new invention.

Moreover, in the experimental section, the comparison between the LG transformer and other baselines reveals that the proposed framework doesn't consistently outperform GOAT-local, especially in the ogbn-products dataset. Furthermore, in the ogbn-papers100M dataset, the framework is only compared to a single baseline. It's possible that other methods struggle with extremely large graphs, but there are likely additional viable solutions that should be explored.

Additionally, the fusion of transformers and Graph Neural Networks (GNNs) is a dynamic research area with various ongoing studies, such as TransGNN and Graphformers. It would be valuable to understand how these methods perform when confronted with similar tasks.

Lastly, the author emphasizes the significance of combining local and global representations. However, apart from GOAT, there are other techniques that can address this challenge, such as randomly selecting both nearby neighbors and global features. The author should offer further clarification on this matter.

### Questions
This paper commences with two important challenges that have attracted the attention of numerous researchers. Specific comments were provided in the previous section, and it is hoped that the author will consider improvements from the following viewpoints.

The framework appears to inherit many key components from previous papers, with limited significant modifications. It would be beneficial to include more in-depth discussions and comparisons with transformer-based Graph Neural Networks (GNNs). Additionally, it is important to address how other approaches perform in terms of extracting global information from the graph.

Expanding on these aspects would enhance the paper's contribution and provide a more comprehensive understanding of the research landscape in this domain.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

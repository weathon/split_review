# Solving Normalized Cut Problem with Constrained Action Space

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 3, 5, 6

## Abstract
We address the problem of Normalized Cut (NC) in weighted graphs where the shape of the partitions follow an apriori  pattern, namely they must approximately be shaped like rings and wedges on a planar graph. Classical methods like spectral clustering and METIS do not have a provision to specify such constraints and neither do newer methods that combine GNNs and Reinforcement Learning as they are based on initialization from classical methods. The key insight that underpins our approach, Wedge and Ring Transformers (WRT), is based on representing a graph using polar coordinates and then using a multi-head transformer with a PPO objective to optimize the non-differential NC objective.  To the best of our knowledge, WRT is the first method to explicitly constrain the shape of NC and opens up possibility of providing a principled approach for fine-grained shape-controlled generation of graph partitions. On the theoretical front we provide new Cheeger inequalities that connect the spectral properties of a graph with algebraic properties that capture the shape of the partitions. Comparisons with adaptations of strong baselines attest to the strength of WRT.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper describes a Reinforcement Learning strategy to solve an approximate minimum normalized cut on spider web-like planar graphs, like city street maps.  The idea is that the problem can be approximated by a circles-wedges clusterings, in which inner nodes (w.r.t. some central point o) can be grouped w.r.t. their distance from a center o, while outer nodes are further subdivided w.r.t. their angular polar coordinates. The actions to be performed will then be the radius of the outer circle and the (discrete) points where to split the outer nodes.
Some training strategies are defined to help the problem converge and refine the grouping. 
The method is tested on synthetic spider web-like graphs, and subgraphs extracted from a city map.

### Strengths
I like the idea of modeling the grouping of nodes according to the previous knowledge about the domain. This allows to simplify the minimum graph cut problem for the specific type of graphs considered, and obtain better results than other general-purpose grouping algorithms.

### Weaknesses
My main concern is about the quite demanding assumption of the algorithm, which is designed to work on spider-like planar graphs, where nodes are embedded (have coordinates) in R^2. In particular, my comments are:
- even if the proposed solution is sound for the specific problem, I’m not sure it is general enough to be of broad interest to this community. It looks more suited for a venue in the specific application. The restriction to spider-like graphs, with nodes embedded in R^2, severely limits the applicability of this method to a niche set of problems. The assumption that the graph structure can be approximated by concentric circles and wedges is a strong constraint that is not generally applicable to real-world graphs.
- it is not explained why the grouping in inner circles and outer wedges is a good modeling. Is it a pattern observable in other city map grouping algorithms? Does this pattern apply to all cities? The paper lacks a clear justification for why this specific ring-and-wedge structure is a suitable approximation for the normalized cut problem. There is no discussion of whether this pattern is observed in other graph partitioning algorithms or if it is a common characteristic across different city maps. The assumption that all cities follow this pattern is a significant limitation.

There is a drop in writing quality in section 5, which raised some doubts:
- It is incorrect to say that transformers work only on sequences, they work on any set of points but often benefit from a positional encoding. 
- Sections 5.2.1 and 5.2.2 are quite intricate and could be simplified. In practice, they define two different positional encodings for ings and wedges, where points for the ring are encoded with their distance from the center, and for wedges, they are projected into the unit circle (and possibly equispaced?). The description of the positional encoding is unclear and difficult to follow. The use of two different encodings for rings and wedges adds complexity without a clear justification. The projection of wedge points onto the unit circle and the potential use of equispaced points need further clarification.
- The optimal partitioning of circles (row 322) should be better introduced. The method for determining the optimal partitioning of circles is not clearly explained. The algorithm used and its computational complexity should be discussed.
- In 5.4 I don’t understand what the “Current Partition” is. It is represented by a binary mask? How is it converted into the colored square matrix in Figure 4? The concept of “Current Partition” is not well-defined. It is unclear how this binary mask is constructed and how it is used to generate the colored square matrix in Figure 4. The relationship between the binary mask and the visual representation is not explained.

To broaden the impact of the work, it would be worth trying to apply the proposed method to different families of graphs and different datasets. Also, graph cut methods seem to exist specifically designed for planar graphs (e.g. “Efficient Planar Graph Cuts with Applications in Computer Vision”) that would be worth considering in the comparison.

### Questions
- Your setting is much simpler than finding normalized min cut in general undirected graphs. Is it still a NP-Hard problem? For instance, polynomial algorithms for the min-cut on planar graphs exist (I just found a few, but I might be missing some fundamental details). Would they also apply to your definition of normalized cut?
- From reading the text, it sounds like you are providing a novel definition of normalized cut, but it looks like the standard definition to me. Am I missing something? My confusion is further increased by the statement at line 214: “Despite being a simpler class of graphs, these bounds give a theoretical justification of the normalized cut definition equation 2 and the ring-wedge shaped partition.”
- At row 283 you write “Note that this transformation does not change the order of the nodes or the partitions.” What do you mean by node order?
- How is the center of the graph defined?

### Soundness
3

### Presentation
2

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
This work tackles a special case of a normalized-cut problem: that of spider-web shaped weighted planar graphs.
The graph is partitioned into rings, and the outer ring is partitioned into wedges. The approach transforms the graph by:
a. projecting ring nodes onto an axis according to their distance from a center while maintaining node order
or by
b. projecting nodes onto a unit circle.
The transformation results in the partitioned nodes forming a sequence, which is encoded by a transformer.
Reinforcement learning is used to find the ring radius and number of outer ring wedges that result in a minimal normalized cut. 

Specifically, PPO is used, where the state, action, and rewards are encoded as: 
a. State is the graph, number of rings and wedges of the outer ring.
b. Actions are the ring radius or wedge angle.
c. Rewards are 0 in all steps, and the negative normalized cut at the end.
The wedge partition is trained using random ring partitions, followed by training of both ring and wedge partitions.
The ring partition is first inferred during testing, followed by the wedge partition.

This work demonstrates that this transformation is suitable for a specific case of road networks.
The transformation is applied as a preprocessing step, finding a minimal normalized cut with a lower value than other baselines.

The approach is evaluated using synthetic and real-world data.
a. 400k spider-web shape synthetic graphs with a 50 or 100 nodes, ring and wedge partitions, with unweighted and random edge weights.
b. Connected sub-graphs randomly extracted from real-world city maps with edge weight corresponding to traffic.

The performance of the approach is compared with a baseline partitioning method, METIS, and with spectral clustering.
The ring and wedge partitions are compared with brute force and random partitions.

### Strengths
1. The graph transformation is applied as a pre-processing step, aiming to utilize the specific graph structure.

2. The results are a minimal normalized cut with a lower value than other trivial baselines.

### Weaknesses
1. The decisions to apply the transformations to the graph are manual.
The method and its implementation details are ad-hoc and very specific.

2. Dynamic programming is used to compute the optimal partition given the maximum radius and ring count. Ablation studies of this algorithm and the reinforcement learning approach are missing.

3. The graphs are relatively small consisting of 50, 100 (for training), or 200 nodes (in testing).

### Questions
Can this approach be automated by classifying the graphs to automatically find which transformations should be applied as a preprocessing step?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes the Wedge Ring Transformer (WRT), an RL-based approach to minimize the Normalized Cut (NC) on planar weighted graphs. WRT leverages polar coordinates and employs a multi-head transformer with a Proximal Policy Optimization (PPO) objective to address the NC problem. The approach utilizes a two-stage training process to effectively learn both ring and wedge partitioning strategies. Experimental results indicate that WRT effectively reduces the NC.

### Strengths
The paper provides a clear definition of the Normalized Cut (NC) problem and the description of the Wedge Ring Transformer (WRT) is well-articulated.
The design of transformations specifically tailored for ring and wedge shapes appears effective.
Provide some theoretical analysis about cheeger bound for ring and wedge partition.

### Weaknesses
Ablation studies: The ablation studies primarily focus on the two-stage training process, but lack analysis on key components of the paper's main contribution, such as the wedge-ring transformer, PAMHA, and pre-calculation. Ablation studies on these components would provide a more comprehensive evaluation of the WRT architecture. Specifically, the impact of removing the polar coordinate transformation, the multi-head attention mechanism within the transformer, and the specific design choices within PAMHA are not explored. A more granular analysis is needed to understand the contribution of each of these elements to the overall performance.
Running Times:  The paper does not provide an analysis of the model's runtime, leaving the computational efficiency of WRT unaddressed. It is unclear how the runtime scales with the number of nodes and edges in the graph, and a comparison with other methods in terms of computational cost is missing. This is crucial for assessing the practical applicability of the proposed method.

### Questions
1.	The paper argues that GNNs were not used due to scalability issues. However, the proposed method also seems to require processing the entire graph at once, and experiments were conducted on data with a maximum of only 200 nodes. It remains unclear how WRT scales to larger graphs, and additional evidence of scalability would strengthen the paper's claims.
2.	What are the evaluation metrics in Table 1 and Table 2?
3.	Although WRT is designed for ring and wedge-shaped partitions, I am interested in understanding its performance on other types of datasets. For example, how does it perform on datasets that primarily feature extended ring shapes, such as the long-tail structures often found in knowledge graphs?

### Soundness
3

### Presentation
3

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
The manuscript presents Wedge and Ring Transformers (WRT), an RL-based method for solving the Normalized Cut (NC) problem in weighted graphs with shape-specific constraints. By transforming graphs into polar coordinates and using Transformers with Proximal Policy Optimization, WRT effectively handles both ring and wedge partition shapes, optimizing NC while adhering to these constraints.

### Strengths
1. The paper addresses the Normalized Cut problem in the context of real-world applications, such as road network simulations, where partition shape constraints are critical.
2. The introduction of the Wedge-Ring Transformer, tailored to handle specific shape constraints in graph partitioning, is innovative.

### Weaknesses
1. The paper includes a limited set of baseline methods for comparison. Adding more baselines, particularly those used in NeuroCUT, would strengthen the evaluation by providing a more comprehensive assessment of WRT's performance.
2. The baselines lack specialized adaptations for the "Ringness" and "Wedgeness" constraints, while WRT is explicitly designed with these constraints in mind. This discrepancy may lead to an unfair comparison, as the baselines are not optimized to meet these specific structural requirements. It is unclear if the baselines are even capable of producing ring or wedge shaped partitions, which makes direct comparison problematic.
3. The experiments use relatively small graph instances, whereas NeuroCUT and other methods operate on benchmarks with thousands of nodes, aligning more closely with real-world scales. The current experimental scale may limit the ability to assess WRT’s applicability to large-scale, practical scenarios. The paper does not provide sufficient evidence that the method would scale to real-world graphs.
4. Given the use of Transformers, I am concerned about the performance and computational cost of training and inference on large-scale datasets. The quadratic complexity of attention mechanisms could be a significant bottleneck, and the paper does not address this concern with any empirical analysis or theoretical discussion.

### Questions
1. Were NeuroCUT and ClusterNet evaluated by training on the same datasets as WRT? Ensuring consistent training conditions is crucial for fair comparison.
2. The Cheeger Bound presented appears to be a specific case of a more general result. How does this theoretical finding contribute to model design or provide insights for experimental evaluation?
3. What specific metrics are used in Tables 1 and 2? 
4. Why are there no generalization results for NeuroCUT and ClusterNet in Table 2? 
5. According to Fig. 6, it appears that RL training converges early (10–20k of 400k steps). Does the extended training beyond this point contribute to any performance improvements, or could training resources be optimized?

### Soundness
3

### Presentation
3

### Contribution
3

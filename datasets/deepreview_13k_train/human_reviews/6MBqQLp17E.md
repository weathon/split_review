# Linear Transformer Topological Masking with Graph Random Features

- Decision: Accept
- Scores: 6, 8, 6, 8, 8, 6

## Abstract
\vspace{-2mm}
 When training transformers on graph-structured data, incorporating information about the underlying topology is crucial for good performance. 
\emph{Topological masking}, a type of relative position encoding, achieves this by upweighting or downweighting attention depending on the relationship between the query and keys in a graph. 
In this paper, we propose to parameterise topological masks as a \emph{learnable function of a weighted adjacency matrix} -- a novel, flexible approach which incorporates a strong structural inductive bias.
By approximating this mask with \emph{graph random features} (for which we prove the first known concentration bounds), we show how this can be made fully compatible with linear attention, preserving $\mathcal{O}(N)$ time and space complexity with respect to the number of input tokens.
The fastest previous alternative was $\mathcal{O}(N \log N)$ and only suitable for specific graphs.
Our efficient masking algorithms provide strong performance gains for tasks on image %, video%
and point cloud data, including with $>30$k nodes.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper addresses the challenge of incorporating graph structural information into transformer attention mechanisms while maintaining computational efficiency. Their main focus is on topological masking, especially under the low-rank assumption of the attention matrix. The authors use graph random features (GRFs) to approximate topological masks for attention via importance sampling, which are parameterized as learnable functions of the weighted adjacency matrix. They propose a method to control transformer attention using graph node kernels based on random walks via power series of the adjacency matrix, with a random halting probability at each step. They provide concentration bounds in Theorem 3.1. Additionally, their empirical evaluation is carried out on diverse tasks like vision transformers on ImageNet, iNaturalist2021, Places365 and point cloud dynamics prediction for robotics applications.

While the experimental results show good promise, the paper’s theoretical complexity analysis and claims about O(1) GRF sparsity doesn’t hold true for all general graphs. Despite these theoretical issues, the paper introduces interesting ideas about using graph structure in attention mechanisms and provides novel empirical results, particularly in the robotics domain.

### Strengths
1. The paper provides strong theoretical foundations with proven concentration bounds and complexity guarantees for GRFs.
2. The method shows concrete performance improvements on real-world tasks and scales to large problems (>30k nodes) that would be intractable with quadratic approaches.
3. The approach can be implemented with both symmetric and asymmetric GRFs, offering different trade-offs between computational efficiency and variance in mask estimation.
4. The experiments cover diverse applications (images, point clouds, videos) and include detailed ablation studies.

### Weaknesses
The paper's central claim of O(N) complexity relies critically on the assertion that Graph Random Features (GRFs) have O(1) sparsity. This claim is mathematically incorrect for several reasons:
In Lemma 3.2, while the result doesn’t show an N term, it is still implicitly dependent on the size of the graph. O(1) complexity implies that your non-zero entries per row vector $\hat{\phi}G(vi)$ are bounded by a constant independent of input size. The bound in Lemma 3.2 is still dependent on multiple parameters like $n$, $p_halt$ and $\delta$. So, one can say that your complexity is like the complexity of a “parameterized algorithm”, i.e., $O(f(n,p_halt,\delta))$, where f is some function of the parameters. 
Let's consider a family of complete graphs ${G_N}{N \geq 1}$ where $G_N$ has N vertices and each vertex has degree N-1. Then all edge weights are equal, i.e., $1/ sqrt( (N-1)(N-1) )$. 
At any step, the walk can move to another vertex with probability 1/(N-1). 
For a given walk starting at an arbitrary vertex, if you assign a r.v. to count the number of “distinct vertices” visited, even with the inclusion of geometric termination, you will find that this r.v grows with N because it has (i) more possible vertices available at each step to visit, (ii) the probability of visiting a new vertex at each step increases with N, and (iii) each successful step before halting can easily reach O(N) vertices. Therefore, making O(N) non-zero entries in the row vector and hence your attention matrix. With more independent walks starting from v, you can fill up even more non-zero entries. Hence, the O(1) bound doesn’t hold here.

As a demonstrative simple counter-example, consider the following two cases with fixed parameters. Let’s fix the parameters as n=10 (walks), p_halt = 0.5 and \delta=0.1 

Case 1: Small complete graph
- N = 10 nodes
- Each node has degree 9
- Even a 1-hop walk can reach 9 other nodes
- A 2-hop walk can reach all nodes

Case 2: Larger complete graph
- N = 1000 nodes
- Each node has degree 999
- A 1-hop walk can reach 999 other nodes
- A 2-hop walk can reach all nodes

While their bound might be the same in both cases, as it depends only on $n$, $p_halt$ and $\delta$, but the number of non-zero entries in both cases ends up being very different from one another. In the second case, you are much more likely to get O(N) non-zero entries due to the reasons I mentioned earlier about each hop having many more options, more distinct nodes, thus more reachability and coverage of the underlying graph (or at least exploring a large portion of the graph before terminating). 

This demonstrates that actual sparsity heavily depends on the structure of the graph. 

This rigorous analysis shows that the number of non-zero entries cannot be independent of graph size without additional constraints on the graph structure. The analysis shows that the results proposed by the author hold only with some assumptions on the graph structure, for example sparse graphs of bounded-degree graphs. 

The authors make a significant assumption in their discussion of Theorem 3.1. (Lines 278-280), where they state that "assuming that c remains constant (i.e. we fix a maximum edge weight and node degree as the graph grows)...". 
This reveals that their theoretical analysis works only for graphs with a bounded maximum degree and hence contradicts the claims about working for general graphs (line 82 in Introduction). This algorithm cannot handle dense graphs, complete graphs (or almost complete graphs), graphs where node degrees grow with N and many real world graphs where there can be very high-degree nodes and no bounds on degrees. 

The authors should make this bounded-degree assumption explicit upfront in the introduction and modify their claims about general graphs. 

A complete graph (or almost complete graph) isn’t completely unusual especially in the context of attention mechanisms where in the final layers pretty much end up having all tokens attending to each other in a pairwise manner. The experiments done in the paper are done on very low-degree graphs like grid graphs, which doesn’t demonstrate the applicability of their method to general graphs, especially large dense ones. 

Inconsistent and confusing notation:
- $(f_k)_{k=0}^\infty$ is sometimes treated as a sequence of reals, sometimes as a function
- Incorrect set notation: claiming (f_k)_{k=0}^\infty \subset R when sequences are functions from N to R
- Weighted adjacency matrix definition issues:
  * Claim W is weighted but then suggest $w_{ij} = 1/sqrt(d_i d_j)$
  * This normalization discards meaningful edge weights in attention context

ii) Missing crucial assumptions:
- No explicit assumptions about graph structure
- No discussion of how graph density affects complexity
- No proper analysis of how maximum degree impacts sparsity

The paper's main contribution is focused specifically on making topological masking efficient, rather than improving linear attention in general. The paper makes empirical comparisons to only basic linear attention models and focuses solely on topological masking efficiency. 

In the experiments section, it would be interesting to compare against other major linear attention variants like (i) Performers (Choromanski et al., 2020) Favor+ which uses kernel approximations and (iii) Nyströmformer which uses Nystrom’s method to approximate attention.

### Questions
While the empirical results might be interesting, the fundamental theoretical claims that form the paper's main contribution are incorrect. A major revision would be needed to:
1. Correct the theoretical analysis
2. Properly characterize complexity and mention which category of graphs it can address
3. Either prove better bounds under specific assumptions or acknowledge limitations
4. Frame results in terms of parameterized complexity

The authors should consider addressing these fundamental issues during rebuttal, if possible.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper introduces a novel, efficient topological masking approach for transformers on graph-structured data, using learnable functions of the weighted adjacency matrix to adjust attention based on graph structure. By approximating with graph random features, this method supports linear attention, offering strong performance gains across diverse data types and large graphs.

### Strengths
1. The prposed method shares $O(n)$ time complexity and suitable for the relatively large scale input.

### Weaknesses
see question.

### Questions
I appreciate the authors’ valuable contributions in this area. As I am less familiar with applications in image, point cloud, or robotics contexts, I am particularly interested in understanding how Graph Random Features (GRFs) benefit graph neural networks on traditional graph datasets.

1. Could the authors provide examples or case studies that apply GRFs to commonly used graph datasets, such as Cora or Citeseer?
2. Could the authors also include a comparison of computational times between your methods and baseline approaches?

Thanks for this important work, and apologies for my gaps in my background knowledge.  I would also kindly request that the Area Chair reduce the weight of my review in the final evaluation.

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
This paper presents a method for integrating topological graph information into graph transformers through a learnable topological-masking mechanism, using graph random features (GRFs). The authors propose to approximate topological masks via Monte Carlo estimation via GRFs to represent structural biases while ensuring linear-time computation.

### Strengths
1. Their method is the first to achieve $\mathcal{O}(N)$-time complexity for computing masked attention for general graphs, $N$ being the number of vertices.
2. The paper provides the first known concentration bounds for GRFs and rigorous sparsity guarantees. These theoretical insights are valuable, potentially extending beyond transformers to other domains that rely on scalable graph-based representations. 
3. Their method demonstrates improved predictive performance in various learning tasks.

### Weaknesses
1. Dense and unclear presentation: 
   - While the method is theoretically sound, the presentation is mathematically dense and lacks clear explanations. This may pose a barrier to readers, particularly those less familiar with GRFs. In particular, the technical exposition in lines 184–254 is notation-heavy and unclear. The use of McDiarmid's inequality and the concentration bounds are presented without sufficient context, making it difficult to grasp their implications. The connection between the theoretical results and the practical implementation is not clearly established, leaving the reader to infer how the theoretical guarantees translate into concrete benefits.
   - Algorithmic descriptions, such as those in Algorithm 1, are highly abstract and may be difficult to follow. The algorithm lacks sufficient detail regarding the implementation of the random walks and the computation of the topological masks. The specific steps for generating the graph random features and how they are used to approximate the topological masks are not clearly delineated. Without clearer explanations, the accessibility of the paper is reduced.
2. The paper lacks discussion of the method limitations. For example:
   - The practical applicability of this method depends heavily on the specifics of the graph structure and the task requirements, since it relies on approximations with random walks. In  graphs where relevant information is distributed over long distances or requires traversing multiple nodes, random walks may fail to capture the full structure efficiently. The paper does not discuss how the length of the random walks or the halting probability affects the quality of the approximation, nor does it provide guidance on how to choose these parameters for different graph structures. The method's performance on graphs with varying degrees of connectivity and diameter is not explored.
   - For dynamic or evolving graphs, precomputing random walks is not feasible, and recomputing them on the fly could reduce efficiency. The paper does not address the computational overhead associated with recomputing random walks for dynamic graphs, nor does it discuss potential strategies for mitigating this cost. The impact of changes in the graph structure on the stability and accuracy of the topological masks is also not considered.
   - Since random walks introduce stochasticity, their effectiveness can vary based on the number of walks and the chosen halting probability. This means that the quality of topological masking may be sensitive to hyperparameters like the number of walks and the stopping probability, making it challenging to generalize the method across different graph structures. The paper does not provide a systematic analysis of the sensitivity of the method to these hyperparameters, nor does it offer guidelines for selecting appropriate values for different types of graphs and tasks.

### Questions
1. Eq. (4): The power series is generally not guaranteed to converge. It is better to specify clearly the underlying assumptions on W and alpha that guarantee convergence. Is $\alpha_0$ assumed here to equal 1, as in (Reid et al. 2024b)?
2. Remark 3.1: 
   - This remark is used as a lemma. Better state it as such.
   - It is in general not guaranteed that alpha has a deconvolution. Is it an assumption of Remark 3.1? Or is it guaranteed by some other assumption? Better clarify.
3. Ln. 115-116: "$\Phi_{Q,K} \in$" should probably be "$\Phi_Q, \Phi_K \in$"
4. Ln. 184-185: Statement is unclear. Why should it necessarily be faster?

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper proposes a topological masking method when training transformers on graph-structured data. By decomposing and approximating the graph mask with graph random features, the proposed method achieves linear time and space complexity w.r.t input size. The author shows that their masking algorithm is efficient and high-performance using experiment results.

### Strengths
1. The paper has a good motivation for introducing linear topological masking of low-rank attention. 

2. The author explains well from introducing the topological mask, using the graph feature to achieve low-rank attention, and leveraging GRF to approximate the graph feature.

3. The explanation is clear, the figures are illustrative, and the writing is well-structured.

### Weaknesses
1. While the author emphasizes a lot about the efficiency of the proposed method, the evaluation and experimental parts mainly show the accuracy achieved and lack the corresponding efficiency results like time and memory.



### Questions
1. While the author shows the test accuracies in Table 1, can the author also present other results, like the total training time or total flops, to validate the proposed method’s efficiency?

2. In Figure 5, it seems the accuracy improvement achieved by GRF Interlacer is on the starting timestep 0. After several timesteps, it’s becoming similar to MP Interlaced. Can the author explain the reason behind the accuracy improvement at the beginning and the drop? 

3. Besides GRF, are there other methods to do implicit graph masking in equation (8)? How's the performance?

If all my concerns are resolved properly, I will be happy to increase my score.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes to use the gram matrix of the graph node kernels as the masking matrix for the attention mechanism of Transformer. The fact that each element of the gram matrix can be written as the inner product of two feature vectors (kernel def), we can write the **attention mechanism with masking**  in the form of Equation 3 of the low-ranking setting by redefining $\Phi_Q$ and $\Phi_K$. graph random features are also further applied to reduce the complexity. The experiments are conducted on ViTs and the prediction of the particle dynamics for robotics.

### Strengths
* The paper is well-organized and well-written, it's a pleasure to read.
* The reasoning of the idea is clear. We can understand very well why we need to use kernel gram matrix as the masking matrix and why we need the graph random features.
* The experiments are well-presented, which show the relevance of the proposition for the situation where $N$ is large.

### Weaknesses
 * While the true time complexity of the proposed algo is $\mathcal{O}(Nmd)$, most part of the paper omit $m$ and $d$. I think the authors should make this point clear since in some cases where $m$ and $d$ can be large enough. Specifically, the paper should discuss the practical implications of large $m$ and $d$ values, such as increased memory consumption and computational cost, and how these might affect the scalability of the proposed method in real-world scenarios.
* The citation in line 161 (Borgwardt et al., 2005) is about graph kernels, not graph node kernels if I understand it well. While graph kernels and graph node kernels are related, the paper should clarify the specific connection and justify why the cited work is directly relevant to the proposed method, which uses node kernels. A more precise citation or a more detailed explanation of the relationship is needed.
* Though the paper shows experimentally the impact of the number of random walks $n$ on the performance, I would also like to see its impact on the computation time. This is crucial for understanding the trade-off between performance and computational cost. The paper should include an analysis of how the number of random walks affects the runtime and resource usage, especially when dealing with large graphs.
* In section 4, maybe it's better to use \textit{subsection} for each experiment instead of \textit{paragraph}.
* This question is not about the contribution of the paper, but the general idea of using structural graph masking for transformer. Isn't it a reinvention of the graph neural network by integrating a matrix representing the structure information into Transformer? Can author make a (possible) link between the two?

### Questions
* While the true time complexity of the proposed algo is $\mathcal{O}(Nmd)$, most part of the paper omit $m$ and $d$. I think the authors should make this point clear since in some cases where $m$ and $d$ can be large enough.
* The citation in line 161 (Borgwardt et al., 2005) is about graph kernels, not graph node kernels if I understand it well.
* Though the paper shows experimentally the impact of the number of random walks $n$ on the performance, I would also like to see its impact on the computation time.
* In section 4, maybe it's better to use \textit{subsection} for each experiment instead of \textit{paragraph}.
* This question is not about the contribution of the paper, but the general idea of using structural graph masking for transformer. Isn't it a reinvention of the graph neural network by integrating a matrix representing the structure information into Transformer? Can author make a (possible) link between the two?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents a novel approach by parameterizing topological masks as a learnable function of a weighted adjacency matrix. This method incorporates a strong structural inductive bias with rigorous concentration bounds, improving both time and space complexity.

### Strengths
1. The research topic is highly important and intriguing and the authors provide experimental results on some larger scale image and point-cloud datasets.
2. Generally, the notation and theorem in the paper is well defined and illustrated. 
3. The authors provide the theoretical analysis and ablation study to show the effectiveness of the proposed method.

### Weaknesses
#### Major problems
1. The background and related work section is limited. To my knowledge, this is not the first work to incorporate the inductive bias inherent in graph nodes into GNN and transformer-like models. Specifically, the paper fails to adequately discuss how its approach differs from methods that learn latent graph structures or those that use structural information through relative positional encodings. A more thorough comparison is needed to clarify the novelty of the proposed method.
2. Additionally, improved time and space complexity have been discussed in existing papers such as [A, B]. The paper needs to provide a more detailed analysis of the computational advantages of the proposed topological masking approach, especially when compared to linear attention mechanisms. The current discussion lacks a rigorous comparison of the computational costs and memory requirements, making it difficult to assess the practical benefits.
3. It's better to include more experiments and evaluations on traditional graph datasets. The current experiments focus on image and point cloud data, which are not standard benchmarks for graph-based methods. Evaluating the method on established graph datasets would provide a more comprehensive understanding of its performance and generalizability.

#### Minor issues
1. Confusing notations in line 148, the size of the graph N ($\mathcal{N}$)?

### Questions
See the weakness.

### Soundness
3

### Presentation
3

### Contribution
2

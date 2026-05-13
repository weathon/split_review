# Understanding Virtual Nodes: Oversquashing and Node Heterogeneity

- Decision: Accept
- Scores: 8, 6, 6, 3, 5

## Abstract
While message passing neural networks (MPNNs) have convincing success in a range of applications, they exhibit limitations such as the oversquashing problem and their inability to capture long-range interactions. Augmenting MPNNs with a virtual node (VN) removes the locality constraint of the layer aggregation and has been found to improve performance on a range of benchmarks. We provide a comprehensive theoretical analysis of the role of VNs and benefits thereof, through the lenses of oversquashing and sensitivity analysis. First, we characterize, precisely, how the improvement afforded by VNs on the mixing abilities of the network and hence in mitigating oversquashing, depends on the underlying topology. We then highlight that, unlike Graph-Transformers (GTs), classical instantiations of the VN are often constrained to assign uniform importance to different nodes. Consequently, we propose a variant of VN with the same computational complexity, which can have different sensitivity to nodes based on the graph structure. We show that this is an extremely effective and computationally efficient baseline for graph-level tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper contains a theoretical examination of VNs and their ability to counteract the oversquashing frequently present in MPNNs and a juxtaposition with GT methods, leading to a justification for an intermediate heterogeneous VN approach, VN_\textit{G}.
A novel analysis shows that VNs impact on the commute time between nodes of a graph, as a function of the graph spectrum, can reduce oversquashing. Empirically, VNs are shown to reduce commute time compared to MPNNs on real graphs, though is possible for it to increase. Commute time in turn affects mixing a model can induce after \textit{m} layers with mixing being the number of interactions between nodes needed to solve a task. When VNs reduce commute time, it is shown that strong mixing increases, reducing the size of \textit{m} and reducing oversquashing.

However, GTs can arbitrarily change commute time and further exceed the previous improvement, though they do incur significant overhead when compared to VNs. A novel sensitivity analysis of GTs and VNs follows which examines the Jacobian of both methods, showing that GTs allow for global heterogeneity via attention as each node depends on non-uniform functions of the values of all nodes at the previous layer. Contrary to this, VNs are independent for nodes further than 2 hops away and thus global information is applied homogeneously. It is worth noting that a full examination of the impact of GTs on commute time is left as a future research direction.
This leads to the proposal of VN_\textit{G} to bridge the gap between VNs and GTs. This takes the form of sequential updates. First a local update on nodes, then VN update leveraging the previous nodes, and a final node update as a function of both local and VN updates for each node. An examination of the Jacobian shows that the sensitivity of each node to non-neighbors becomes a function of the topology while appearing to maintain local bias.

The need for heterogeneity in VN_\textit{G} is empirically shown by examining the similarity of the attention matrix of a trained GT model on the nodes of several graphs. An increase in similarity implies reduced heterogeneity and therefore a reduced gap between the performance of GT and the (less) heterogeneous methods. The performance of models during experiments matches this observation.
In line with the discussion of the paper, experiments to compare MPNN + VN_\textit{G} with other baselines for graph-level tasks demonstrates improved performance over MPNN + VN on tasks requiring heterogeneity and matching performance of GT methods, which has some implication for the impact of long-range dependencies for tasks.

The appendix of the piece also includes an examination of MPNN + VN with PairNorm and demonstrates that, for the linear case, the benefits of MPNN + VN are not due to its ability to produce the results of PairNorm to reduce oversmoothing. In fact, when MPNN + VN replicates PairNorm, its expressivity is reduced.

### Strengths
The piece does an excellent job of addressing a shortcoming in the literature on when and why Virtual Node are helpful from a theoretical perspective. It provided an extensive juxtaposition with a competing method and identified a key component of the performance gap between the two in specific settings (graph-level tasks). An incremental approach that has begun to appear in other works is further discussed and the piece contains the first theoretical analysis to justify its use.
Additionally, with minimal additional work an appendix of the paper proving the benefit of VNs does not come from their ability to replicate PairNorm for the linear case, which is rather a hindrance.

### Weaknesses
I do not believe that there are any significant weaknesses to this paper and find it to be acceptable. Minor changes may improve the piece, but also to an undue amount of additional work and conflict with length requirements.

MPNN + VN can beat GTs as shown in Tables 1 and 3 with the observation that long-range dependencies may not play as large of a role for these tasks. This leads me to wonder about the role of the inductive bias from the locality of MPNN’s, though this is addressed Rampášek et al. which instead leads be to the impact of VN_\textit{G} on mixing.

I do not have a better alternative, but the empirical analysis to answer Q2 of Section 5.1 oddly seems self-justifying to me. In addition, GatedGCN+PE is shown in Table 2. to have superior performance to all the methods of Table 1. For Pept-Func while remaining competitive for Pept-Struct.

It seems that Appendix C concludes the proof of Theorem B.1 but only proves that there are filters which can be learned by MPNN but not MPNN-VN. The remainder in this seems mostly to be contained in Theorem C.1.

Beginning on line #1430 are what appear to be notes used to write Appendix C that were not removed. 

Line #373 refers to Theorem 3.4 and should instead be Corollary 3.4.

It would be nice to have the Jacobian of GT at least somewhere in the appendix.

In Table 1 what is the PE in GatedGCN+PE+VN? Also, in the text of 5.1 it is only referred to as GatedGCN+VN

I was not able to discern what the arrows in the heading of each of the tables indicated.

Appendix J seems unnecessary as Fig. 1 would be more useful in the main text, if it wasn’t so small.

### Questions
Beginning on line #1430 are what appear to be notes used to write Appendix C that were not removed. 

Line #373 refers to Theorem 3.4 and should instead be Corollary 3.4.

It would be nice to have the Jacobian of GT at least somewhere in the appendix.

In Table 1 what is the PE in GatedGCN+PE+VN? Also, in the text of 5.1 it is only referred to as GatedGCN+VN

I was not able to discern what the arrows in the heading of each of the tables indicated.

Appendix J seems unnecessary as Fig. 1 would be more useful in the main text, if it wasn’t so small.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The goal of this paper is to exploit the use of a virtual node to improve the performance of graph neural networks. The focus is specifically on the problem of oversquashing brought forward by the use of message passing neural networks (MPNNs). The authors first analyze the performance of MPNNs when virtual nodes are used and, then, they propose a new approach that can help improve performance and address the oversquashing problem.

### Strengths
+ The problem of oversquashing has been less studied in the prior art, and this work makes an important contribution towards this area
+ The analysis of oversquashing and the use of virtual nodes is important. The result connecting improvements to the graph spectrum is meaningful and helps in improving designs of graph neural networks.
+ The evaluation of performance compared to graph transformers is meaningful and shows how one can close the gap in performance.

### Weaknesses
 - The theoretical results, while relevant, seem to follow directly from prior works. It is not clear whether the contribution is significant theoretically, as opposed to being a merger of known prior results like those from Di Giovanni et al.
- The argument for using MPNNs with virtual nodes compared to graph transformers is rather weak. I believe graph transformers may in fact remain the architecture of choice. The authors' discussion on this issue is not very convincing.
- The cost of adding a virtual node is apparently assumed to be negligible or at least it is not discussed. The computational overhead, both in terms of memory and runtime, needs to be explicitly addressed, especially when considering large graphs.
- The performance gains do not seem significant enough. While the results show improvements over standard MPNNs with virtual nodes, the absolute gains compared to state-of-the-art methods, particularly graph transformers, appear marginal in many cases. The practical impact of these small improvements needs further justification.

### Questions
- What is the cost of adding a virtual node? Are there hidden computing or performance costs? Can you provide concrete run-time or memory usage results while comparing the cases with and without virtual nodes?
- How do you justify the significance of your final results given that the performance is very close to state of art? For example, can you discuss the practical implications of the performance improvements that you achieved.
- Can you better articulate why MPNNs with virtual nodes are more effective than graph transformers?
- What is the main theoretical contributions when it comes to your proofs? How does it differ from the papers from which you adapted the theory? Please provide a point-by-point comparison between your theoretical results and the most closely related prior works.

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
(1) This paper studies the impact of Virtual Nodes (VNs) on oversquashing, showing that their improvements in network mixing can be bounded by the graph's spectrum.
(2) This paper identifies a gap between VNs and GTs in capturing heterogeneous node importance, leading to the proposal of MPNN + VNG, which effectively learns heterogeneous node relevance without extra cost.
(3) This paper validates its insights through experiments, demonstrating that MPNN + VNG consistently outperforms MPNN + VN, particularly in tasks where node heterogeneity is crucial.

### Strengths
1. Theoretical Contributions are good: (1) It offers the first comprehensive study of the impact of Virtual Nodes (VNs) on the oversquashing phenomenon, providing a foundational understanding of their role in enhancing network performance. (2) By employing sensitivity analysis of node features, the study identifies a significant gap between VNs and GTs regarding their ability to capture heterogeneous node importance, leading to deeper insights into their comparative strengths.
2. It introduces a novel MPNN + VNG method, that effectively utilizes graph structure to learn a heterogeneous measure of node relevance without incurring additional computational costs.
3. The paper validates its theoretical insights through extensive ablations and experiments, demonstrating that MPNN + VNG consistently outperforms the MPNN + VN, particularly in tasks where node heterogeneity is crucial.

### Weaknesses
1. ‘To assess if and how a VN helps to mitigate oversquashing, we need to determine whether the commute time of Gvn is smaller than the commute time of the original graph G.’ So which Theorem below can prove this?
2. Theorem 3.1 highlights how the impact of adding a VN can be determined in terms of the spectrum of the input graph. According to Theorem 3.1, how can it derive the claim of ‘adding a VN reduces the overall commute time’? Theoretically prove this is important.
3. ‘The result in Corollary 3.4 shows that for real-world graphs where adding a VN significantly reduces the commute time—i.e., (5) is negative’. Please further explain this claim.
4. ‘In our sensitivity analysis we will show MPNN + VNG to fall in between the fully homogeneous
MPNN + VN and the potentially fully heterogeneous GTs.’ Please give a brief explain for this claim.
5. ‘nodes that are more relevant to each of their neighbors, are more likely to contribute more to the global update, instead of weighting each node the same as for MPNN + VN.’ Which part of MPNN + VNG shows this property?
6. The heterogeneity of nodes is important, for what kind of tasks?

### Questions
See the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Message passing neural networks (MPNNs) are known to be limited in their capability to capture long-range interactions between nodes, a problem known as oversquashing. This paper studies the effect of adding a virtual node (VN) on over-squashing, giving an exact characterization in terms of spectral properties of the network. 

Oversquashing is the problem of fitting information in a constant-sized embedding vector from a neighborhood growing exponentially in terms of radius. This problem is known to occur between nodes at a high commute time from each other. The paper calculates the change in commute time from adding a virtual node, as a function of eigenvectors of the network Laplacian. The change in commute time is verified empirically. 

Additionally, the paper does a brief comparison of MPNN + VN to Graph Transformers (GTs). In light of this comparison, the authors give (formalize) a slightly different VN architecture with interleaved node and VN updates. This architecture is claimed to be better because it incorporates graph structure before aggregating messages at the virtual node. This model is also tested in practice.

### Strengths
The paper gives a precise characterization of the difference in commute time when a virtual node is added. Combined with the results on commute time from previous work, this gives a clear insight into how VNs mitigate oversquashing. The difference in commute time is given for pairwise commute time, as well as the average commute time over the network. The result is also connected to the concept of mixing from earlier work, showing that MPNNs with a virtual node can require fewer layers to represent functions that require high mixing. 

The experimental results align with the theoretical findings. The paper is also well written and easy to follow.

### Weaknesses
The comparison of MPNN + VN to Graph Transformers (Section 4) feels somewhat superficial and does not offer significant new insights. The main observation is that graph transformer layer allows for heterogeneous node importance, while MPNN+VN treats nodes with homogeneous importance. This is a known limitation of MPNNs, and the discussion does not delve into the nuances of how this impacts performance on different graph structures or tasks. The analysis lacks a deeper investigation into the specific types of heterogeneity captured by GTs and how they differ from the implicit heterogeneity arising from node degrees in MPNN+VN. 

The authors propose MPNN + VN_G, a formulation with node updates interleaved with the VN update. This formulation is not new, and the authors also say it has been previously shown to improve performance in practice. The claim is that the update allows heterogeneous attention to different nodes, but this seems like a questionable claim. Heterogeneity is due to the different graph topologies: high-degree nodes affect a different number of neighbors proportional to their degree, before new states are aggregated to the VN. This is different from heterogeneity in GTs via the attention mechanism, where different importances can be learned. There is a note about this on line 349, but I feel like the section is still overselling its results. It is also worth mentioning that a traditional MPNN + VN is also capable of heterogeneous node importance in the weaker sense, just with at least 3 layers. The paper does not adequately explore the limitations of this degree-based heterogeneity compared to the learned attention of GTs, nor does it provide a clear justification for why the proposed interleaved update is superior to existing methods.

Overall, the primary contribution of the paper seems to be Theorem 3.1. A downside of this theorem is its practical application. The authors mention that the change in commute time from adding a virtual node can sometimes be negative (e.g. in a complete graph). The experiments show significant average commute time reduction for some graph datasets, but the paper does not make it clear whether these experimental results can be reliably generalized in practical applications. The theoretical result, while mathematically sound, lacks a clear connection to practical scenarios. Given that commute time was already introduced in previous work, all we have now seems to be a formula. The formula is complicated and without real practical use. Theory is best if it is actually usable, but I don't know how to use this theory.

### Questions
While the runtime of MPNN + VN_G is the same as MPNN + VN, could there be problems with vanishing gradients since the depth is essentially doubled? 

Minor comment: equation 14: ": j \in V" missing. same below on line 311

### Soundness
3

### Presentation
4

### Contribution
1

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper provides a comprehensive theoretical analysis of the role of virtual nodes in message passing neural networks, specifically addressing the oversquashing problem and long-range interaction limitations. The authors characterize how virtual nodes improve network mixing abilities and mitigate oversquashing based on underlying network topology. Additionally, they propose a variant of virtual nodes that can assign different importance to nodes based on graph structure, offering a more effective and computationally efficient solution for graph-level tasks compared to traditional approaches.

### Strengths
This paper provides a detailed theoretical analysis addressing the issues of "oversquashing and node heterogeneity". 
Each chapter of this paper presents a detailed problem statement, followed by a comprehensive theoretical analysis and the design of corresponding algorithms to tackle these issues.

### Weaknesses
1.Although this paper provides a lot of theoretical analysis and derivation, the conclusions are unclear. For example, Theorem 3.1. The conclusion is a complex expression. Can the author further simplify it through approximation or other means? The current presentation makes it difficult to grasp the practical implications of the theorem. Specifically, while the theorem quantifies the change in commute time, it does not provide an intuitive understanding of how this change directly translates to improved performance in graph neural networks. A more accessible interpretation or a simplified corollary would greatly enhance the clarity of the theoretical contribution.

2.The experimental results of this paper show almost no improvement compared to other methods (Tables 1-3). The reported gains are marginal, and in some cases, the proposed method does not outperform existing techniques. This raises concerns about the practical significance of the proposed approach. The lack of substantial improvement, especially when compared to computationally expensive methods, questions whether the added complexity of the proposed method is justified.

3.Although the content of this paper is substantial, it lacks a framework diagram. Readers find it difficult to intuitively understand what contributions this paper has and the relationships between the various contributions. The absence of a clear visual representation makes it challenging to grasp the overall architecture and the flow of information within the proposed model. A diagram illustrating the key components and their interactions would significantly improve the paper's accessibility.

4.This paper attempts to highlight its experimental results through bright colors, but the bright green color makes readers uncomfortable. In addition, the excessive use of different colors makes the experimental results appear somewhat messy, for example in Table 2.

### Questions
The MNIST and CIFAR10 datasets are both image datasets. Why are they being used in graph-related research or this paper?

### Soundness
3

### Presentation
3

### Contribution
2

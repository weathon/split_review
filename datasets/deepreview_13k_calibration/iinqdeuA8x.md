# Towards Dynamic Graph Neural Networks with Provably High-Order Expressive Power

- Decision: Reject
- Avg Score: 4.80
- Scores: 5, 5, 6, 5, 3

## Abstract
Dynamic Graph Neural Networks (DyGNNs) have garnered increasing research attention for learning representations on evolving graphs. 
Despite their effectiveness, the limited expressive power of existing DyGNNs hinders them from capturing important evolving patterns of dynamic graphs. 
Although some works attempt to enhance expressive capability with heuristic features, there remains a lack of DyGNN frameworks with provable and quantifiable high-order expressive power.
To address this research gap, we firstly propose the $k$-dimensional Dynamic WL tests ($k$-DWL) as the referencing algorithms to quantify the expressive power of DyGNNs.
We demonstrate that the expressive power of existing DyGNNs is upper bounded by the 1-DWL test. 
To enhance the expressive power, we propose \textbf{D}ynamic \textbf{G}raph Neural \textbf{N}etwork with \textbf{H}igh-\textbf{o}rder \textbf{e}xpressive \textbf{p}ower (\textbf{HopeDGN}), which updates the representation of central node pair by aggregating the interaction history with neighboring node pairs. 
Our theoretical results demonstrate that \modell can achieve expressive power equivalent to the 2-DWL test. 
We then present a Transformer-based implementation for the local variant of \model.
Experimental results show that \modell achieved performance improvements of up to 3.12\%, demonstrating the effectiveness of \model.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a k-dimensional dynamic Weisfeiler-Lehman (WL) test as a novel approach to quantify the expressiveness of dynamic graph neural networks (DyGNNs) and unifies simpler DyGNNs under the 1-Dimensional WL (1-DWL) framework. Additionally, the paper proposes HopeDGN, which employs a more granular encoding method to achieve the expressiveness of a 2-DWL test. Experimental results indicate the method’s effectiveness.

### Strengths
1. The paper is the first to propose a k-dimensional dynamic WL test to evaluate the expressiveness of DyGNNs, addressing a relatively underexplored area in DyGNN expressiveness.
2. The proposed framework theoretically attains 2-DWL expressiveness by introducing a novel encoding scheme, which also shows potential for generalization to other models.
3. The model includes an optimized local version for practical applications, demonstrating strong performance.

### Weaknesses
1. While prior DyGNNs may lack a unified framework, they have implemented numerous techniques to enhance expressiveness. Examples include DyGformer [1] with neighbor co-occurrence encoding, CAWN [2] with anonymous walk paths, and NAT [3] with neighborhood-aware encoding, etc. These methods are not addressed within the proposed framework, potentially making it appear somewhat isolated. Furthermore, the paper does not clearly articulate how the proposed k-dimensional dynamic WL test compares to these existing encoding techniques in terms of theoretical expressiveness or practical performance. A more detailed discussion of how the proposed framework relates to and potentially surpasses these methods is needed.
2. The theoretical time complexity of the k-DWL framework, especially over longer time spans, may be a concern, as noted by the authors. While local variants are proposed, the paper does not provide a rigorous analysis of the trade-offs between computational efficiency and the expressiveness of these local approximations. Specifically, it is unclear how the performance of the local variants scales with increasing time spans and how much expressiveness is sacrificed for the sake of computational feasibility. The practical usability could still be limited by these computational demands, especially in scenarios with very long temporal dependencies.

### Questions
1. In Table 2, integrating MITE with other baselines shows significant improvements. How is this integration implemented, and does MITE demonstrate clear benefits compared to other encoding approaches?
2. Figure 5 highlights a notable efficiency improvement when reducing the neighbor length. What are the corresponding performance metrics associated with these efficiency gains?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents a novel dynamic graph neural network that is theoretically inspired by a proposed dynamic-WL test. According to this framework, they show that existing DyGNNs are bounded by 1-DWL test and by using a multi-interaction time encoding (MITE), they can increase the expressiveness to up to 2-DWL test. Then, they propose HopeDGN, which updates the representation of a node pair by aggregating not just the historical interactions but also the elapsed times. Through a transformer-based implementation, they show improved performance across seven datasets, while demonstrating plug-and-play benefits.

### Strengths
- The proposed MITE matrix can be used in a plug-and-play fashion to provide gains in existing architectures. 
- Time complexity and efficiency analysis are provided.
- HopeDGN leverages the strengths of the transformer and a theoretically motivated WL-test to propose a more effective method.
- Empirical comparison is thorough in both transductive and inductive settings of link prediction against representative baselines.

### Weaknesses
 - The DWL test is almost identical to the temporal WL test in PINT [1]. This is not acknowledged in the main paper and thus, can be flagged as plagiarism. The 1-order variant of the proposed DWL test is functionally equivalent to the temporal WL test in PINT. Specifically, while the proposed method hashes a list of interaction times $(t_1, t_2, ...)$ associated with an edge, PINT hashes a list of tuples $(t_1, t_2, ...)$ where each tuple contains a single interaction time. However, these two representations are isomorphic and should not be considered distinct for the purpose of graph isomorphism testing. The authors should either prove the distinction or acknowledge the similarity.
- Discussion with existing related work is casual and not carefully positioned.
  - It is mentioned that it is not clear how relative positional features provide theoretical benefits even though it was shown theoretically in Souza et al., 2022 [1]. 
  - It is mentioned that "Souza et al. (2022) proves that adding a memory mechanism will not change the expressive power of DyGNNs. Therefore, the expressive power of DyGNNs can be fully characterized by the 1-DWL test." but this is wrong as they show that is true specifically when the architecture of the MP-GNN is deep enough. 
  - It is not clear whether what are the theoretical benefits of the proposed method as compared to [1] or [4]. It seems that the benefits are complementary but needs further discussion. Does the proposed method already provably reach the expressiveness of time-then-graph and PINT in their expressiveness tests.
- Space complexity is not provided nor computationally compared. The additional cost of storing B matrix along with the transformer architectures may be prohibitive in many cases and limit the scalability of the proposed method. 
- MITE encoding is similar to the time projection for staleness as done in JODIE [2] and TGN [3]. However, these similarities are neither acknowledged nor discussed in the paper. It seems like MITE is an extension of the time projection to the neighbors' encodings in addition to only the interacting node's embeddings. The paper should discuss the relationship between MITE and existing time projection methods, as both aim to capture the temporal aspect of interactions. While MITE extends this to neighbors, the core idea of projecting time information is shared.
- The proof of the main proposition 3 that shows the theoretical disadvantage of existing dyGNNs seems wrong. In particular, they only consider node b for graph (a) and node h in graph (b). On the other hand, Equation 9 denotes that they should have considered all historical neighbors w for both graphs. This would have meant considering nodes b, h, d for graph (a) and nodes b, h, f for graph (b). In that case, d and f seem to be the difference maker and not b and h. 
- Considering the MITE interactions for all historical neighbors seem unscalable as the size of the graph increases. 
- Running time of HopeDGN is not compared against the baselines, only the training time is compared.

### Questions
see above weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a novel Dynamic Graph Neural Network (DyGNN) framework called HopeDGN (Dynamic Graph Neural Network with High-order Expressive power). The primary focus of the paper is to address the limited expressive power of existing DyGNNs in capturing evolving patterns in dynamic graphs. The authors propose the k-dimensional Dynamic WL tests (k-DWL) as a theoretical framework to quantify the expressive power of DyGNNs, and introduce the Multi-Interacted Time Encoding (MITE) that captures the bi-interaction history of target node pairs with other nodes. MITE is integrated into the HopeDGN framework, and theoretical results show that HopeDGN can achieve expressive power equivalent to the 2-DWL test. Experimental results demonstrate that HopeDGN achieves superior performance on link prediction and node classification tasks compared to other baselines.

### Strengths
- The Multi-Interacted Time Encoding (MITE) allows the model to capture indirect dependencies between node pairs, which is crucial for tasks like link prediction. This module is a plug-and-play component that can be integrated into various models, enhancing their expressive power.

- The paper provides proofs that HopeDGN can achieve expressive power equivalent to the 2-DWL test, which is a significant improvement over existing DyGNNs. This theoretical grounding adds credibility to the practical results.

- The authors discuss multiple model design details including Neighborhood encoding, patching and Transformer encoder. The authors conduct extensive experiments on both link prediction and node classification tasks across multiple datasets. The results consistently show that HopeDGN outperforms existing baselines, demonstrating its effectiveness.

### Weaknesses
 - The paper could benefit from a detailed comparison with other high-order GNNs that have been proposed for static graphs since the basic idea of encoding node pairs comes from high-order WL tests, like https://arxiv.org/abs/1810.02244. Specifically, a discussion of how the proposed method relates to techniques that explicitly compute higher-order neighborhoods or use higher-order message passing would be beneficial. It is not clear how the proposed method's performance and computational complexity compare to these existing approaches.
- I am confused with the example in Figure 1. Suppose the graph is static, according to symmetry 1-WL test will give identical labels to C and D, then GNN cannot distinguish node pairs (A, C) and (A, D) using only node embeddings, which has no connection to graph dynamics. And since 2-WL works on node pairs, we can easily verify that (A, C) and (A, D) will get different labels in 2-WL test so methods derived from 2-WL can distinguish them (like MITE). Therefore I don’t think that this example can well explain the expressive limitations of 1-DWL since it also works in static graphs. Can the authors provide more explanations?

- Can the proposed method work on dynamic graphs in which edge interaction can both start and end?

### Questions
- I am confused with the example in Figure 1. Suppose the graph is static, according to symmetry 1-WL test will give identical labels to C and D, then GNN cannot distinguish node pairs (A, C) and (A, D) using only node embeddings, which has no connection to graph dynamics. And since 2-WL works on node pairs, we can easily verify that (A, C) and (A, D) will get different labels in 2-WL test so methods derived from 2-WL can distinguish them (like MITE). Therefore I don’t think that this example can well explain the expressive limitations of 1-DWL since it also works in static graphs. Can the authors provide more explanations?

- Can the proposed method work on dynamic graphs in which edge interaction can both start and end?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work aims to address the gap in dynamic graph learning research concerning the theory of expressive power. The authors first introduce the $k$-DWL test and argue that the expressive power of existing DGNN models is bounded by the 1-DWL test. To advance this, they propose a new DGNN model that works analogously to the 2-DWL test and prove that the proposed model, Global HopeDGN, is equivalent to the 2-DWL test. The experiments show the local variant of HepeDGN can achieve superior performance across several datasets.

### Strengths
1. This work is the first attempt at assessing the expressive power of dynamic graph learning and introduces the concept of the $k$-WL test. It intuitively points out the limitations of existing DGNN models and proves that the 1-WL test limits their expressive power.
2. This work proposes a new DGNN model, HopeDGN, inspired by the 2-WL test. This model has greater expressive power than vanilla DGNN models, and the experiments show its superiority.

### Weaknesses
1. Although no research exists on the expressive power theory of DGNN, a few studies have considered the correlations between historical neighbors of two terminal nodes, such as DyGFormer, HOT [R1], and CAWN. HopeDGN is somewhat of an incremental study compared to DyGFormer. HopeDGN exhibits higher performance in the experiments but may incur much larger training costs.
2. The discussions of the expressive power of existing DGNN models are not completely correct.
   1. The abstraction of DyGNNs in Section 3 cannot cover existing studies. For instance, CAWN can leverage the information from high-order neighbors in a single layer if the length of the random walk is larger than 1.   
   2. DyGFormer, HOT, and CAWN are able to distinguish AC and AD in Figure 1.
3. Some notations are confusing. $l$ is used to represent the layer of AGG and UPDATE in Line 167 and the node labeling function in Line 239. And the layer of AGG and UPDATE of local HopeDGN in the experiments is not specified. In addition, the MITE of $w$ is denoted as $X_{B,w}$ in Line 369 and $X_{M,w}$ in Line 289.

### Questions
1. The expressive power of the 1-WL test and the 2-WL test is the same in static graphs, as argued in [R2]. Is the 1-DWL test equivalent to the 2-DWL test? Intuitively, it is.
2. Could the authors provide the training cost of HopeDGN and the baselines?


[R2] A Short Tutorial on The Weisfeiler-Lehman Test And Its Variants.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors present a new dynamic GNN model, HopeDGN, designed to exceed the expressive power limitations of current DyGNNs, which are capped by the 1-DWL test. HopeDGN aims to achieve higher-order expressive power by leveraging the 2-WL test.

### Strengths
1. This paper investigates an important problem.

2. The paper thoroughly explores the expressive power of dynamic GNNs in relation to the 2-WL test.

### Weaknesses
1. Similarity to Existing Models: The model structure closely resembles DyGFormer, particularly in Section 4.4, where essential component, from node encoding to the patching-based transformer encoder, are almost identical. The authors describe their model as a general framework, but the specific implementation details provided heavily overlap with DyGFormer. The core difference highlighted, the MITE encoding, is not sufficiently distinct from the Neighbor Co-occurrence Encoding (NCOE) used in DyGFormer to justify the claim of a fundamentally different approach. The paper fails to adequately address the similarities in the overall architecture and the implications of these similarities on the novelty of the proposed method. Furthermore, the authors did not correctly cite DyGFormer, referencing only Dosovitskiy et al. (2021) instead.

2. Lack of Comprehensive 2-WL Analysis: While the paper’s primary contribution is introducing 2-WL testing for dynamic graphs, it falls short of a thorough examination of prior dynamic graph models’ failures under 2-WL. The claim that DyGNN cannot differentiate node pairs AC and AD in Figure 1 is misleading. While standard message-passing DyGNNs might struggle, the figure does not specify the exact type of DyGNN being referenced, and it is not clear that all DyGNNs would fail this test. Specifically, models employing NCOE, such as DyGFormer, can indeed distinguish between these pairs. The analysis lacks a precise definition of the class of DyGNNs being considered, and the authors did not address scenarios where their model might also fail under specific graph structures or dynamic patterns. A more rigorous analysis of the limitations of existing models and the specific conditions under which the proposed model provides an advantage is needed.

3. Limited Experiments: The experimental setup appears incomplete. According to the experimental setup in DyGFormer, there are three different negative sampling configurations. However, this paper appears to only conduct one configuration. This incomplete experimental setup raises concerns about the robustness and generalizability of the results. Additionally, the ablation study's removal of time encoding is questionable, as time encoding is a standard module in DyGNN frameworks and not a contribution introduced by this paper. The purpose of this ablation is unclear, and it does not provide meaningful insights into the proposed model's unique contributions.

4. Ambiguity in Notation: Certain symbols and terms are unclear, creating readability issues. For instance, the symbol S appears frequently in the complex analysis section (line 398) without definition. Similarly, i and j in Equation 3 lack clear explanations, and there are other instances of undefined notation throughout the paper. This lack of clarity makes it difficult to follow the technical arguments and reproduce the results.

5. Unclear Theoretical Framework: The authors state that they "establish a theoretical framework to quantify the expressive power of DyGNNs," but it is unclear how this quantification is achieved or where this analysis is elaborated upon in the paper. The connection between the proposed k-DWL test and the actual expressive power of the model is not clearly demonstrated. It is not sufficient to simply state that (k+1)-DWL is strictly stronger than k-DWL; the paper needs to show how this theoretical result translates into practical improvements in model performance and how it relates to the specific architecture of the proposed model.

### Questions
Please refer to the weakness

### Soundness
2

### Presentation
2

### Contribution
2

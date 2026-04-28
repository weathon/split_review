# Clifford Group Equivariant Simplicial Message Passing Networks

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
We introduce \aclp{csmpn}, a method for steerable $\mathrm{E}(n)$-equivariant message passing on simplicial complexes. 
    Our method integrates the expressivity of Clifford group-equivariant layers with simplicial message passing, which is topologically more intricate than regular graph message passing. 
    Clifford algebras include higher-order objects such as bivectors and trivectors, which express geometric features (e.g., areas, volumes) derived from vectors.
    Using this knowledge, we represent simplex features through geometric products of their vertices.
    To achieve efficient simplicial message passing, we share the parameters of the message network across different dimensions.
    Additionally, we restrict the final message to an aggregation of the incoming messages from different dimensions, leading to what we term \emph{shared} simplicial message passing.
    Experimental results show that our method is able to outperform both equivariant and simplicial graph neural networks on a variety of geometric tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces Clifford Group Equivariant Simplicial Message Passing Networks (CSMPNs), a method designed for steerable $E(n)$-equivariant message passing on simplicial complexes. The approach combines the expressivity of Clifford group-equivariant layers with simplicial message passing, which is more expressive than regular graph message passing. To implement it, the paper discusses methods for lifting a set of points to a simplicial complex and embedding simplicial data in the Clifford algebra, where various types of lifts like Vietoris-Rips and manual lifts are considered. The results and evaluations of the CSMPNs are across various domains showing the effectiveness of this method.

### Strengths
1. The paper introduces a combination of Clifford group-equivariant layers and simplicial message passing, providing a strong theoretical foundation for the method. The use of Clifford algebras to represent geometric features with simplices is natural and mathematically sound.
2. The model is designed to be applicable across various domains, from geometry to molecular dynamics. This broad applicability is a strong point, especially for a mathematical audience interested in universal structures.

### Weaknesses
1. I would like to see the detailed inference time of CSMPN compared to others, e.g., in the MD17 atomic motion dataset. I believe the time complexity of CSMPN is highly relevant to the number of simplices, and I would like to know if this is an issue in the implementation. Specifically, it would be beneficial to understand how the inference time scales with the size of the input simplicial complex, as the number of simplices can grow rapidly with the number of nodes, potentially making the method impractical for larger systems. A comparison with methods that do not use simplicial complexes, such as standard graph neural networks, would also be valuable to highlight the trade-offs in terms of computational cost versus expressiveness.
2. As the authors mention experiments on MD17 and QM9 are beyond the scope of their research; I hope the authors give a discussion or possible directions on how the manual lift could be implemented for small and medium-sized molecules to strengthen the paper's applicability, not just using H2O as an example. The current discussion on manual lifts is somewhat abstract, and it would be helpful to see concrete examples of how one might choose specific simplices for different types of molecules. For example, how would one decide which simplices to include for a molecule with multiple functional groups or a complex ring system? The paper would benefit from a more detailed exploration of the practical challenges and potential solutions for applying manual lifts in real-world molecular modeling scenarios.

### Questions
See weaknesses.

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
In this paper, the authors proposed a Graph Neural Networks method that combines both simplicity message passing and Clifford group equivariants neural networks. It is understood that this is an extension of the recent study of E(n) equivariant message passing simplicity networks, which has the limitation of manual initialization and restriction of updating methods. Numerical experiments show that the proposed method outperform existing methods in most cases.

### Strengths
As I have summarized above, the min contribution of this paper is to propose an alternative message passing network to the existing EMPSN method, and eliminate two main limitations of EMPSN. 

Although neither utilizing Clifford group in neural networks  nor simplicial message  passing is new, the authors combine them to achieve an advancement in GNN.

### Weaknesses
In the key technical session 3.2, embedding simiplicial data to Clifford algebra, the embedding of the simplices is not fully and clearly described, thus renders a full understanding of the proposed method difficult. The authors did point to Figure 1 for depiction of the method, but that is open for different interpretations. Specifically, the description lacks detail on how the Clifford features for higher-order simplices (beyond edges) are constructed and how the permutation invariance is achieved in practice. The geometric product is mentioned, but the exact procedure for aggregating these products to ensure permutation invariance is not clearly defined. It is unclear how the model handles different orderings of vertices within a simplex and how this impacts the final Clifford feature representation. 

While numerical results indeed show that new method, CSMPN, achieves the best performance in most experiments, the improvement over existing methods can not be characterized as significant, thus not leading to a convincing argument for its usage. The performance gains, while present, are not substantial enough to justify the added complexity of the Clifford algebra framework. A more thorough analysis of the computational cost and practical benefits compared to simpler alternatives is needed. The paper would benefit from a more detailed discussion of the trade-offs between performance gains and computational overhead.

### Questions
Maybe the authors can explain by "learn" the embedding through Clifford group-equivariant layers in Sec. 3.2.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
- The authors propose a new architecture for geometric graphs that combines simplical message-passing, Clifford algebras, and equivariance.
- On a high level, their approach is based on linking the expansion in the number of vertices that occurs in simplices with the expansion in grades in a Clifford algebra.
- A given geometric graph is first lifted to simplices, then the outputs are computed with a message-passing algorithm between the simplices. Different from Bodnar et al (2021), the proposed algorithm uses Clifford algebras as representations, the geometric product to compute simplex features, and Clifford Group Equivariant NNs (Ruhe et al, 2023) to construct messages. These changes add a geometric inductive bias to the algorithm and make it equivariant.
- The algorithm is demonstrated on experiments ranging from simple toy data to motion capture data, molecular dynamics, and even NBA data.

### Strengths
- The idea is novel and interesting. I like how the authors link two previously disjointed ways of describing expansions to multiple objects.
- The experimental evaluation on a range of different problems highlights the versatility of the approach. The results demonstrate that the method works.
- The paper is well-written, the structure clear, and the figures of a high quality.

### Weaknesses
 - The authors overstate the naturality of their method. While the approach feels intuitive at a quick glance, it mixes two different concepts: Simplices are a topological concept, while the geometric product is related to the geometric space that the graph is embedded in. This leads to a number of issues. Even in 3D space, one can construct 100-simplices, but the Clifford algebra only goes up to grade 4. While intuitively higher-order simplices encode more information, higher-order grades eventually become lower-dimensional. More specifically, the geometric product, when applied to vertex features to create simplex features, results in a multivector that represents relationships within the geometric space, but this representation is not unique. For instance, different sets of vertices forming distinct simplices could, after the geometric product and subsequent projection onto the Clifford algebra basis, result in the same multivector, leading to a loss of information about the specific simplex structure. This is a critical issue that needs to be addressed, as it implies that the method may not fully capture the topological information encoded in the simplicial complex. I wish the authors would acknowledge and discuss these issues, which to me seem central to this paper.
- While I like the experiments, it would be useful to see the performance on more standard benchmarks of geometric deep learning. The authors acknowledge that they do not achieve SOTA results on some of these tasks. That's fine, but it would still be useful to see how the method performs compared to other generic equivariant methods. It would be beneficial to see a more thorough comparison, including metrics such as parameter efficiency and training time, to fully understand the trade-offs of this approach.
- The paper's contributions are somewhat thin: the authors essentially plug together two existing ideas (simplical message passing and Clifford group equivariant networks). Of course, the same can be said about many other papers.

### Questions
- Could you comment on what I wrote in the first point in the Weaknesses section? It's well possible I missed something here.
- On page 2, what do you mean with "geometric products are meaningful in all such cases"?
- On page 7, you mention that you use an equal parameter count for CSMPN and the baselines. Is that really fair when compairing equivariant and non-equivariant baselines? Usually, equivariant methods have far less parameters for the same expressivity.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

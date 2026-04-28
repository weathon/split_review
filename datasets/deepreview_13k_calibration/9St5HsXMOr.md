# Long-range Meta-path Search through Progressive Sampling on Large-scale Heterogeneous Information Networks

- Decision: Reject
- Avg Score: 5.60
- Scores: 8, 5, 5, 5, 5

## Abstract
Utilizing long-range dependency, though extensively studied in homogeneous graphs, is rarely studied in large-scale heterogeneous information networks (HINs), whose main challenge is the high costs and the difficulty in utilizing effective information. To this end, we investigate the importance of different meta-paths and propose an automatic framework for utilizing long-range dependency in HINs, called Long-range Meta-path Search through Progressive Sampling (LMSPS). Specifically, to discover meta-paths for various datasets or tasks without prior, we develop a search space with all target-node-related meta-paths. With a progressive sampling algorithm, we dynamically shrink the search space with hop-independent time complexity, leading to a compact search space driven by the current HIN and task. Utilizing a sampling evaluation strategy as the guidance, we conduct a specialized and expressive meta-path selection. Extensive experiments on eight heterogeneous datasets demonstrate that LMSPS discovers effective long-range meta-paths and outperforms state-of-the-art models. Besides, it ranks top-1 on the leaderboards of ogbn-mag in Open Graph Benchmark.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aims to solve meta-path instance selection for heterogeneous graphs. Two observations of existing works trigger the model design, including (1) only several meta-path instances dominate the model performance, and (2) some meta-path instances cause a negative impact on the performance. Therefore, the paper proposes a search algorithm to search meta-path instances from all possible instances and use simple MLP to predict labels after finishing searching paths. Compared with meta-path-free models, meta-path-based models, and NAS-based models, the proposed model consistently performs the best.

### Strengths
1. Motivation is very clear and the experimental results on effectiveness and efficiency support major claims.
2. the architecture of the model is very simple.
3. the empirical results show a strong performance.

### Weaknesses
1. The maximum path length is pre-defined still.
2. Comparison with existing works on the number of parameters should be also added to show how powerful MLP is.
3. The contribution of each meta-path instance is not clear. Will the searched long-range path have a negative impact on performance?

### Questions
1. The embeddings of the target nodes are all learned from neighbors, why not use the node features of the target nodes?
2. How do you set up and learn $\alpha_k$ for all meta-path instances? 
3. Why do you think 2M is a good number for the candidates to be searched?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a study on the use of long-range dependencies in large-scale heterogeneous information networks (HINs). The authors address this by presenting an automatic framework named Long-range Meta-path Search through Progressive Sampling (LMSPS). LMSPS is designed to identify meta-paths within HINs effectively, without needing prior knowledge. It includes a search space that encompasses all meta-paths related to target nodes. Through a progressive sampling algorithm, the framework narrows this search space efficiently, achieving a reduced search space that is specific to the given HIN and task. A sampling evaluation strategy is used to select the most expressive and task-specific meta-paths. The results from experiments on eight different datasets indicate that LMSPS not only identifies effective long-range meta-paths but also surpasses existing models in performance.

### Strengths
1. The authors of the paper provided clear motivations for long-range metapath search. The experiments in Section 4 also provide useful insights into the problem.

2.  Experimental results not only show good performance, but also excellent efficiency: both GPU memory cost and computational is scalable. 

3. The methodology introduced is both intuitive and technically sound, suggesting a well-reasoned approach.

### Weaknesses
W1. Long-range dependencies in graph neural networks are often associated with oversmoothing and over-squashing issues. While these issues are typically associated with the number of GCN layers, long meta-paths used may bring in similar problem. Specifically, the paper does not address how the increased path length might lead to the dilution of relevant information or the homogenization of node representations. A more thorough discussion is needed on whether the proposed method, LMSPS, inherently mitigates these issues or if there are specific design choices that address them. For example, are there any mechanisms to ensure that the information from distant nodes is still relevant and distinguishable when aggregated?

W2. Transformers are becoming popular in graphs as well to capture long range dependencies, although they do suffer from scalability issues when the receptive field is too large. Hence, some methods, like HINormer, resorts to subgraph based sampling. By improving the sampling strategy beyond just subgraphs, I think transformers are promising in addressing these issues. However, the paper lacks a comparative analysis with transformer-based models. It would be beneficial to discuss the advantages and disadvantages of using transformers in the context of HINs compared to the proposed meta-path-based approach. This should include considerations of computational complexity, memory usage, and the ability to capture nuanced long-range interactions. For instance, how does the scalability of LMSPS compare to transformer models when dealing with very large graphs or very long meta-paths? Does the inherent structure of meta-paths provide any advantages in terms of interpretability or efficiency compared to the attention mechanism in transformers?

W3. Writing is not very clear, especially in Section 5.1. It is more like a step-by-step introduction of the pipeling, lacking a clear, high-level organization so that readers know which are the important contributions and focuses. The current presentation makes it difficult to discern the core innovations from the routine procedures. A more structured presentation, highlighting the novel aspects and their significance, would greatly improve the readability and impact of this section.

Minor issue: In Figure 2, search stage, i'm not sure if the example 0/1 values given (in the green block) is right?

### Questions
Please see weaknesses.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a novel approach called LMSPS for representation learning on heterogeneous information networks (HINs). LMSPS uses a progressive sampling algorithm to guide the selection of professional and expressive meta-paths, which capture the complex relationships between nodes in the HIN. The algorithm dynamically narrows down the search space by utilizing the characteristics of meta-paths, resulting in a compact search space that drives the current HIN and task. The authors demonstrate the effectiveness of LMSPS on several real-world datasets and show that it outperforms state-of-the-art methods in terms of both accuracy and efficiency. The main contribution of the paper is the development of a new approach for representation learning on HINs that achieves state-of-the-art performance while being computationally efficient.

### Strengths
(1) It propose a novel meta-path search framework for the first to utilize long-range dependency in large-scale HINs. 

(2) It ranks top-1 on the leaderboards of ogbn-mag in Open Graph Benchmark to prove the feasibility of the method.

### Weaknesses
(1) The writing of this article is somewhat difficult to understand. For example, there is no specific introduction to the meaning of meta-path.

(2) In the fourth part, you used DBLP as an example to illustrate that the length of the meta-path affects the experimental results. Currently, most experiments set the meta-path length to 2, and it is believed that longer paths will affect the experiments. However, in Table 9, the length of the meta-path has been It can reach 6, which is contrary to the initial statement.

(3) Figure 2 does not match well with Part 5. For example, it does not reflect progressive sampling search and sampling evaluation. At the same time, the calculation method of the initial weight is not well reflected in the figure.

(4) It is not explained clearly why some meta-paths are used as noise. I hope I can write down the specific reasons.

### Questions
In Figure 1, I found that the results obtained by using all paths are actually similar to the results obtained by only APV. I don't quite understand the meaning of using meta paths? Would it be much different from your experiment to only use a path length of 2 or 3?

### Soundness
3 good

### Presentation
2 fair

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
In this paper, the authors focused on the graph representation learning task on heterogenous information networks. A novel LMSPS method was introduced to automatically select the proper set of long-range metapaths via a progressive sampling algorithm that dynamically shrink the search space with hop-independent time complexity. The overall presentation is clear. The experiments are also sufficient, where the proposed LMSPS method achieved impressive results. Moreover, the authors provided their source code for review.

### Strengths
S1. The overall presentation of this paper is clear, which is easy to grasp the key ideas.

S2. Using progressive sampling algorithm to search for effective meta-paths seems interesting.
  
S3. The proposed method achieved impressive results in the experiments.
  
S4. The authors provided their source code for review.

### Weaknesses
**W1. Some of the statements in this paper seem to be inconsistent or need further clarification.**

The authors' claim regarding the exponential growth of the receptive field with increasing layers in metapath-free HGNNs, while also highlighting the benefits of exploring long-range dependencies, warrants a more nuanced discussion. Specifically, the analogy between the step/range of a path and the number of GNN layers needs careful consideration. While it is true that many real-world graphs exhibit the 'six degrees of separation' property, implying a relatively small average diameter, the behavior when path lengths or the number of GNN layers significantly exceed this (e.g., >>6) requires further investigation. In such scenarios, it is plausible that the receptive field centered at each node could encompass the entire graph, potentially leading to issues like over-smoothing or the dilution of node-specific information.

The paper does not explicitly mention the availability of graph attributes (node or edge attributes) in the problem statements of Section 2. However, Section 5.1 states that each node is associated with raw features. This discrepancy should be addressed, and details regarding graph attributes should be clearly described, perhaps in Table 8 for better clarity.

In Section 3, the authors state that existing methods like GTN, HGT, HAN, HPN, MEGNN, and GraphMSE, while attempting to automatically select a proper set of metapaths, are not as effective as using the full meta-path set. This statement seems to contradict the fact that the proposed method also does not utilize the full meta-path set. A more precise explanation of how the proposed method's metapath selection differs and why it is more effective is needed.

Regarding Eq. (2), the derivation of { \alpha_k } is unclear. Are these learnable parameters, or are they derived from { {\bf{X'}}_k }? If they are learnable parameters, their relationship to K and the potential for exponential growth with increasing path length should be explicitly addressed. If they are derived, the derivation process needs to be clearly explained.

The training loss in Eq. (6) includes both training and validation sets, which deviates from standard supervised learning. This unconventional approach should be formally introduced and justified early in the paper, ideally in the problem statement section (Section 2), using appropriate mathematical notation.

The paper does not clarify the training losses used for 'LMSPS' and 'LMSPS+label' in Table 2. Does 'LMSPS' imply unsupervised or self-supervised training? If so, what is the specific loss function used? Given that the proposed method is presented as supervised, relying on the loss in Eq. (6), it would be helpful to discuss whether and how the method could be adapted to unsupervised or self-supervised settings, where training is based solely on graph topology and attributes without labels.

Table 3 lacks results for 'LMSPS+label' and 'LMSPS+label+ms'. An explanation for their absence would be beneficial.

***

**W2. According to my understanding, the authors only tested the proposed method using the transductive setting of node classification. Its ability to handle the advanced inductive inference (e.g., for new unseen nodes and across graphs) was not validated in experiments.**

***

**W3. Some of the statements in the paper breaks the anonymity of this submission during the review period.**

The authors' claim regarding their method ranking 1st on the ogbn-mag leaderboard in OGB, along with the provided URL, inadvertently reveals the authors' identities and institutions, thus compromising the anonymity of the submission.

### Questions
See W1-W2

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper addresses the challenge of utilizing long-range dependencies in large-scale heterogeneous information networks (HINs). The authors introduce an automatic framework named Long-range Meta-path Search through Progressive Sampling (LMSPS). This framework aims to discover meta-paths for various datasets or tasks without prior knowledge. The method involves developing a search space with all target-node-related meta-paths and then progressively shrinking this space. The approach is guided by a sampling evaluation strategy, leading to specialized and expressive meta-path selection. Experimental results on eight heterogeneous datasets show that LMSPS effectively discovers long-range meta-paths and outperforms existing models.

### Strengths
1 The idea of searching long-range meta-paths by developing a search space with all target-node-related meta-paths and then progressively shrinking this space is technical sound.

2 The paper is well written and organized

### Weaknesses
1 Why is the search for long-range meta-paths essential? Meta-paths are crucial because they convey rich semantic details. As these paths extend, it's uncertain whether they maintain their clear semantic significance. Furthermore, the computational cost of processing very long meta-paths may outweigh the benefits, especially if the information they provide becomes increasingly noisy or redundant.
2 Long-range meta-paths can be segmented into shorter meta-paths. If we can grasp these short-range meta-paths, then by using a compositional approach, we can understand long-range meta-paths. It is not clear that the proposed method provides a significant advantage over methods that explicitly model compositions of short-range meta-paths, which may be more interpretable and computationally efficient.
3 Finding meta-structures that work effectively across various HGNNs is a tough task. It appears even more challenging to make long-range meta-path searches effective across different HGNNs. In contrast, short-range meta-paths might be more adaptable to various HGNNs, as they represent more fundamental, local relationships. The paper does not adequately address the potential for overfitting to specific network structures when searching for long-range meta-paths.
4 The core idea revolves around creating a search space filled with all target-node-related meta-paths, which is then gradually reduced. Given that RL is seen as a potent tool for searching large spaces, how does the proposed method outperform other RL-based strategies? The paper lacks a detailed comparison with RL-based methods, particularly in terms of computational efficiency and solution quality. It is unclear why the proposed progressive sampling approach is inherently superior to RL for this specific problem.

### Questions
1 Why is the search for long-range meta-paths essential?
2 Why the proposed method is superior to the RL based methods.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

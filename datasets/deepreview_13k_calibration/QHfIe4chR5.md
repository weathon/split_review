# Long-distance Targeted Poisoning Attacks on Graph Neural Networks

- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 3, 3, 6

## Abstract
GNNs are vulnerable to targeted poisoning in which an attacker manipulates the graph to cause a target node to be mis-classified to a label chosen by the attacker. However, most existing targeted attacks inject or modify nodes within the target node's $k$-hop neighborhood to poison a $k$-layer GNN model. In this paper, we investigate the feasibility of {\em long-distance} attacks, i.e., attacks where the injected nodes lie outside the target node's $k$-hop neighborhood. We show such attacks are feasible by developing a bilevel optimization-based approach, inspired by meta-learning. While this principled approach can successfully attack small graphs, scaling it to large graphs requires significant memory and computation resources, and is thus impractical. Therefore, we develop a much less expensive, but approximate, heuristic-based approach that can attack much larger graphs, albeit with lower attack success rate. Our evaluation shows that long-distance targeted poisoning is effective and difficult to detect by existing GNN defense mechanisms.  To the best of our knowledge, our work is the first to study long-distance targeted poisoning attacks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes and studies a new type of attack on GNNs that does not modify the target node’s k-hop neighborhood, which is called long-distance poisoning attack. To solve the problem, both a bilevel optimization-based approach inspired by meta-learning and an approximate heuristic-based approach are proposed. Extensive experiments are conducted on both small and large-scale graphs.

### Strengths
1. Exploring the attack performance of long-range targeted poisoning attacks is valuable and important.
2. The proposed MimicLDT is well-motivated based on the observation from MetaLDT.
3. The paper is easy-to-follow.

### Weaknesses
1. The comparison with short-distance attacks is valuable. However, the compared baselines lack more recent node injection attack methods. Specifically, the evaluation should include a broader range of state-of-the-art poisoning attacks, including those that utilize gradient-based or reinforcement learning techniques for node injection, to provide a more comprehensive understanding of the proposed method's effectiveness relative to the current landscape of adversarial attacks on GNNs.
2. Some claims lack further empirical or theoretical support. For example, the authors claim that 'there are many more potential attack points beyond the target’s K-hop neighborhood’. It would be better if authors could offer detailed support data analysis. This claim is critical to the motivation of the paper, and requires a more rigorous analysis, such as examining the distribution of node distances from a target node across various graph datasets and demonstrating that a significant proportion of nodes are indeed located beyond the k-hop neighborhood. Furthermore, it is important to show that these distant nodes can be effectively leveraged for poisoning attacks.
3. Some minor errors:
designe-> design
heuristicsc)Finally -> heuristics. c) Finally

### Questions
1. Whether the proposed method be generalized to unknown victim models?
2. Is there any data analysis supporting the claim that 'there are many more potential attack points beyond the target’s K-hop neighborhood’?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies targeted poisoning attacks on graph neural networks, which aims to cause misclassification of a single victim node. In order to increase the stealthiness of the attack, the injected poisoning points do not belong to the top-k neighbors of the target victim. The edges and node features of the fake injected nodes are optimized through meta-learning for small graphs and through feature-collision for larger graphs. Empirically, the proposed attack performs better compared to existing short-distance attacks, when the manipulatable nodes are far from the target nodes.

### Strengths
1. The attack performance is good compared to other baselines when the attackers can only manipulate nodes that are far from the target victim.
2. The approach of summarizing the attack patterns from expensive attacks (on small graphs) to design efficient attacks scalable for larger graphs is good.

### Weaknesses
1. The motivation of considering nodes that are outside the top-k neighbors of the target victim is unclear. The authors argued in the appendix that, using some graph explanation tools, the attached nodes can be retried relatively well in some settings. However, the authors made an implicit assumption that such a tool can be directly treated as a detection method, without distinguishing the differences between the influential nodes for the target victim and other nodes. Can we use some threshold to filter out suspicious looking influence nodes for the node under examination? Will this filtering step can be evaded by some adaptive attacks so that short-distance attacks can still survive without sacrificing the effective much? The argument of many potential attack points for the attacker to choose is not well-motivated.  The authors need to demonstrate empirically that short-distance attacks are indeed infeasible or easily detectable in a complete pipeline, before arguing for the necessity of long-distance attacks. Ideally, this would involve showing that a detector, with reported true positive and false positive rates, can effectively identify short-distance attacks, making them impractical. Without this, the motivation for focusing on long-distance attacks remains weak.
2. From the technical perspective, I did not find a significant (inherent) difference from the previously proposed Meta-Attack, as the major the differences are on optimizing a different loss function to encode the targeted attack objective and also to avoid making connections with nodes of top-k neighbors of the target victim during optimization.

### Questions
1. What is the value of $k$ to determine if an attack is short-distance or long distance. 
2. This is not a question, but rather a comment for the authors on proposing potentially stronger attacks. There is some interesting analogy between poisoning attacks on graphs and on images. The meta-learning approach is used to design poisoning attacks for both graphs (cited in the paper) and the images [1], the common drawback is the lack of scalability. The feature collusion attack is similar to the Shafahi et al.'s PoisonFrog paper cited in the paper. There might be some chance to rely on using the gradient alignment [2] technique to design stronger attacks in graph domains. 

[1] Huang et al., "MetaPoison: Practical General-purpose Clean-label Data Poisoning", ICML 2019.
[2] Geiping et al., "Witches' Brew: Industrial Scale Data Poisoning via Gradient Matching", ICLR 2021.
================

post-rebuttal: my concerns still remain and hence will maintain the current rating.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates targeted poisoning attacks on GNNs, in which an attacker injects nodes in a graph to cause a target node to be incorrectly classified to a label of the attacker’s choosing and considers that the attacked nodes are not within the targeted node’s k-neighborhood.  The proposed attack is then evaluated and tested against some empirical defenses.

### Strengths
+The studied problem is interesting

### Weaknesses
 -Threat model is strong
- Novelty is limited
-Missing many references

My major concern is that the problem has been extensively studied, and the novelty is not sufficient.

The authors claim that most of existing attacks on GNNs modify the target node’s k-hop neighborhood, but this is not accurate. For instance, most of the cited poisoning attacks focus on global structure attack, where the entire graph structure can be modified. 

The threat model assumes that the attacker has access to the training data, (including the original graph G, node features, and labels, and also knows the training procedure), which is a rather strong assumption. There exist (restricted) black-box attacks to GNNs, while the authors do not compare and discuss with them 

The evaluated empirical defenses are easy to be broken by stronger attacks, as demonstrated in [a]. Hence, it is not surprising that these defense cannot defend against the proposed attack. 

In fact, there exist many certified defenses against graph structure attacks, but the authors do not test them against the proposed attack.

### Questions
My major concern is that the problem has been extensively studied, and the novelty is not sufficient. 

The authors claim that most of existing attacks on GNNs modify the target node’s k-hop neighborhood, but this is not accurate. For instance, most of the cited poisoning attacks focus on global structure attack, where the entire graph structure can be modified. 
 
The threat model assumes that the attacker has access to the training data, (including the original graph G, node features, and labels, and also knows the training procedure), which is a rather strong assumption. There exist (restricted) black-box attacks to GNNs, while the authors do not compare and discuss with them 

The evaluated empirical defenses are easy to be broken by stronger attacks, as demonstrated in [a]. Hence, it is not surprising that these defense cannot defend against the proposed attack. 

[a] Felix Mujkanovic, Simon Geisler, Stephan Günnemann, and Aleksandar Bojchevski. Are defenses for graph neural networks robust? Advances in Neural Information Processing Systems 35 (NeurIPS2022), 2022.

In fact, there exist many certified defenses against graph structure attacks, but the authors do not test them against the proposed attack.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper discusses the vulnerability of Graph Neural Networks (GNNs) to targeted poisoning attacks, where an attacker manipulates the graph to misclassify a specific node. Most existing attacks focus on manipulating nodes within the node's neighborhood, but this paper explores "long-distance" attacks, where the manipulated nodes are outside this neighborhood. The paper presents a principled optimization-based approach for small graphs but also offers a more cost-effective heuristic-based approach for larger graphs. The findings indicate that long-distance targeted poisoning is effective and challenging to detect by existing GNN defense mechanisms.

### Strengths
+ The paper is well-written, offering a clear and easily understandable presentation of the research.
+ The approach and contributions made by the paper are noteworthy, particularly the exploration of long-distance targeted poisoning attacks in GNNs, even though the proposed method is primarily heuristic in nature.

### Weaknesses
 - The MetaLDT method, while promising, appears to demand significant time and computational resources, which may limit its practicality for larger graphs. Specifically, the paper does not provide a clear analysis of how the computational cost scales with the size of the graph, the number of nodes, or the number of edges, making it difficult to assess its applicability to real-world scenarios.
- The MimicLDT approach, while addressing the cost concerns, seems to compromise on the effectiveness of the attack. This trade-off between efficiency and success rate should be discussed better. The paper lacks a detailed analysis of the specific factors that cause this reduction in effectiveness, such as the limitations of the surrogate model or the heuristic choices made in the optimization process. It would benefit from a more thorough investigation into the performance of MimicLDT under varying conditions.
Some aspects of the paper's approach require further clarification. Additional details and explanations could help the reader better understand the methodology and its intricacies, enhancing the overall quality of the paper. For example, the precise mechanism by which the surrogate model in MimicLDT approximates the behavior of the target GNN is not fully explained, leaving the reader with questions about its accuracy and reliability.

### Questions
- The definition of "long distance" and the specific distance of the injected malicious nodes remain unclear in the current version of the paper.

- Have you taken into account the influence of robust methods during the poisoning process? If so, what are the results regarding the method's effectiveness when attackers lack knowledge of defense mechanisms, which is more practical in real-world scenarios?

- The rationale behind why MimicLDT is more efficient is not clearly articulated. Further elaboration on this aspect would be beneficial. Is it possible to discuss the trade-off between efficiency and effectiveness, such as exploring adjustments to hyperparameters to strike a balance between MimicLDT and MetaLDT?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

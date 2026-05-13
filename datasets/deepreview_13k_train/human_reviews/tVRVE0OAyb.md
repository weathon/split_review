# Precedence-Constrained Winter Value for Effective Graph Data Valuation

- Decision: Accept
- Scores: 6, 6, 5, 5

## Abstract
Data valuation is essential for quantifying data's worth, aiding in assessing data quality and determining fair compensation.
While existing data valuation methods have proven effective in evaluating the value of Euclidean data, they face limitations when applied to the increasingly popular graph-structured data. Particularly, graph data valuation introduces unique challenges, primarily stemming from the intricate dependencies among nodes and the exponential growth in value estimation costs. To address the challenging problem of graph data valuation, we put forth an innovative solution, {\bf P}recedence-{\bf C}onstrained {\bf Winter} (\method) Value, to account for the complex graph structure. Furthermore, we develop a variety of strategies to address the computational challenges and enable efficient approximation of \method. Extensive experiments demonstrate the effectiveness of \method across diverse datasets and tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper tackles the problem of modeling and computing the value of data in learning, when graphs are the data modality. The work is the first to consider this important topic. 

The authors introduce the precedence constrained Winter value model (PC-Winter). 

They also describe how to approximately compute such values, for either nodes or edges in a graph. 

Experiments on an inductive node classification task are done, using 6 real world datasets. 

Baselines (Random value, Degree value, Leave-one-out (LOO) value, and Data Shapley value) are used as baselines, by either removing high value nodes or adding high value edges. 

Clearly, efficiency is a major challenge in this framework, as emphasized by the authors as well.  

Moreover, it would have been interesting to include another prediction task.

### Strengths
First to study an important problem, data valuation for graphs. 

Clearly written paper. 

Clear development and description of the proposed valuation model. 

Reasonable experimental evaluation.

### Weaknesses
A second prediction task would have been a good addition to the experimental framework. 

Efficiency remains a bottleneck for valuation on large graphs.

### Questions
Can the authors comment on the data valuation performance based on other graph facets, such as graph density?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a novel Precedence-Constrained Winter (PC-Winter) value to evaluate graph data, aiming to cover the complex graph structures and unbearable estimation costs. It transfers graph data valuation into a cooperative game theory with pruning strategies and approximation. Experiments show that the PC-Winter value does pick nodes with more contribution.

### Strengths
S1: Interesting perspective. In this paper, the authors propose a novel view to transfer graph data valuation into a cooperative game theory, which gives the community a different insight into the problem.
S2: Sufficient motivation. Directly transferring existing data valuation methods to graph data is limited by the complex structures and dependencies between nodes. It is a valuable problem and a hot topic recently.
S3: Good organization. This paper has a sound representation and a reasonable layout.

### Weaknesses
W1: Lack of necessary explanations. For example, the concept of precedence-constrained calculates DFS along the contribution tree. By definition, the contribution tree is just a tree split of the message-passing mechanism. There seems to be no difference in the fine-tuned multi-layer GNN message passing. Specifically, the paper does not clarify how the precedence constraint fundamentally differs from the inherent message-passing in GNNs, where information propagates through the graph structure layer by layer. The authors need to articulate the unique aspects of their approach compared to simply using a GNN with a different weighting scheme. In another example, the authors argue that we need a fine-grained distinction between whether a node is labeled. However, in section 3.5, the authors sum the PC-Winter values of all duplicates to get the final value. It is contrary to the separation of labeled/unlabeled, which goes back to the aggregation of graph neural networks. The aggregation of duplicate values seems to negate the initial motivation for fine-grained distinction, and the paper does not provide a clear justification for this step. The absence of detail will not be able to prove the innovation of the design, which is not convincing enough.
W2: Flaws in the experimental settings. Firstly, datasets only contain certain types. Please increase the dataset types to evaluate the adaption ability of PC-Winter, such as OGB (bioinformatics) and Flickr (computer vision), which also need to implement graph data evaluation. The current datasets are primarily focused on citation and co-purchase networks, which may not fully represent the diversity of graph structures and applications. For instance, bioinformatics datasets often involve complex molecular structures, while computer vision datasets may have different graph characteristics. Secondly, the evaluation matrix may be biased. The authors propose fine-grained data valuation in this paper but adopt a relatively general matrix of the average. Please provide a more comprehensive perspective, such as for labeled/unlabeled classification performance, balanced accuracy (b-Acc), etc. The use of average accuracy may mask performance differences across different classes or node types. A more detailed analysis, such as class-specific accuracy or balanced accuracy, is needed to fully evaluate the method's effectiveness.

### Questions
Q1: As for W1, What is the essential difference between precedence-constrained PC-Winter and a fine-tuned multi-layer GNN?
Q2: As for W1, what is the basis for considering all duplicates? Does each duplicate contribute to the final score? 
Q3: As for W2, could you expand the categories of datasets? (e.g., bioinformatics, computer vision, etc.)
Q4: How does the hierarchical truncation work when it meets the long-range nodes interaction? For example, two similar nodes in two communities in more than K hops.
Q5: Could you explain the similarity between Data Shapley and PC-Winter on every plot? Especially for Figure 3, the plots of Data Shapley and PC-Winter are in a 'U' shape, and others are more like a '-' shape.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents a new method for graph data valuation based on precedence-constrained winter value. The proposed PC-winter value could help node classification tasks and allow efficient calculation. The experiments are conducted on several public datasets and the results showed that the proposed framework has outperformed mainstream solutions.

### Strengths
S1: The research topic of data valuation for graph-structured data is important, which breaks the assumption of being independent and distributing.
S2: The proposed techniques in Section III are solid.
S3: The evaluation is comprehensive and results are promising.

### Weaknesses
W1. The organization of this paper could be improved. Section III could be shorten and most of the less related contents should be stated in natural language. For example, in Section3.4, the analysis of Fig2(a) can be split into separate segments.
W2. The length of the article is beyond the space limit.
W3. The methodology in Section 3.3 needs further justification. The application of MC is not well-motivated. "Following Data Shapley Ghorbani & Zou (2019), we adopt Monte Carlo (MC) sampling to ...". SHAP uses MC in its implementation, but holds different assumptions with this paper. 
W4. Baselines in the Experiment are not SOTA. Data Valuation is a hot spot recently and many solutions have been proposed. Since you focus on node classification tasks, the following paper should also be added:
Haocheng Xia, Xiang Li, Junyuan Pang, Jinfei Liu, Kui Ren, Li Xiong: P-Shapley: Shapley Values on Probabilistic Classifiers. Proc. VLDB Endow. 17(7): 1737-1750 (2024)
I suggest authors should supplement more related baselines in the experiment and discuss them in the Related Work.

### Questions
Q1. There are many symbols in the paper, so it is recommended to provide a symbol table.
Q2. The Definition 1 needs further clarification. It is better to differentiate between Computation Tree and k-Computation Tree. That is, the name of Definition 1 should be k-Computation Tree.
Q3. The content in Table 2 is confused.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents PC-Winter, a novel method for efficient graph data valuation. Additionally, it proposes a range of strategies to reduce computational complexity, allowing for the effective approximation of PC-Winter. Comprehensive experiments validate the practicality and effectiveness of PC-Winter across diverse datasets and tasks.

### Strengths
S1: The valuation of data for nodes in graph-based tasks, particularly in Graph Neural Networks (GNNs), is a crucial and intriguing problem.
S2: This paper models the problem of graph data valuation as a distinctive form of a cooperative game.
S3: To address the computational challenges associated with calculating PC-Winter values, this paper introduces a set of strategies, such as hierarchical truncation and local propagation.

### Weaknesses
W1: This paper introduces a concept known as a "Level Coalition Structure," which represents a hierarchical organization, as illustrated in Figure 1. However, it imposes the constraint that, at the same level, the data are mutually disjoint. This property is also demonstrated in both Figure 1 and Figure 2.
For example, as depicted in Figure 2, node v_0 has three child nodes {w_0, w_1, w_2} while node v_2 has two child nodes {w_3, w_4}, suggesting that these two sets of child nodes do not share any common nodes. Nevertheless, it is typical for these sets of descendants to exhibit some overlap or shared nodes.
W2: In this paper, as outlined in Definition 2, the duplication’ referred to in W1 appears to be handled by decomposing it into distinct players, termed `duplicates’. However, it remains unclear whether the Shapley value of the original node is simply the sum of the values of these duplicates, as the paper does not explicitly address this point. Furthermore, the correctness of this computational approach is not supported by any formal proof in the text.
W3: In a unilateral dependency structure, a player's contribution depends on its ancestors, resembling the sharded structure setting in [1]. However, in [1], computing the exact Shapley value remains #P-complete despite the presence of the sharded structure. In contrast, the time complexity of PC-Winter, as mentioned in I.5, appears to be polynomial. This discrepancy warrants further explanation, as the paper does not clearly address why the PC-Winter approach would differ in computational complexity compared to the #P-completeness of the Shapley value in the sharded structure.
W4: The paper does not present any experimental results to demonstrate the scalability of the proposed algorithms.

### Questions
Q1: Does the assumption of decomposing a node into distinct duplicates hold? Please provide further evidence or proofs to support this assumption, as it is currently unclear whether this decomposition accurately reflects the original structure.
Q2: Why can the computation of PC-Winter be done in polynomial time, whereas calculating the original Shapley value remains #P-complete? Further clarification and justification of this distinction would be helpful to understand the computational efficiency of PC-Winter in comparison to the traditional Shapley value calculation.

### Soundness
3

### Presentation
3

### Contribution
2

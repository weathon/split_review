# Naturality-Guided Hyperedge Disentanglement for Message Passing Hypergraph Neural Network

- Decision: Reject
- Avg Score: 5.33
- Scores: 8, 3, 5

## Abstract
Hypergraph data structure has been widely used to store information or meaning derived from group interactions, meaning that each hyperedge inherently contains the context of their interactions. For example, a set of genes or a genetic pathway can be represented as a hyperedge to express the interaction of multiple genes that collaboratively perform a biological function (i.e., interaction context). However, most existing hypergraph neural networks cannot reflect the interaction context of each hyperedge due to their limited capability in capturing important or relevant factors therein. In this paper, we propose a \textbf{simple but effective} hyperedge disentangling method, \textbf{Natural-HNN}, that captures inherent hyperedge types or the interaction context of an hyperedge. We devised a novel guidance for hyperedge disentanglement based on the naturality condition in the category theory. In our experiments, we applied our model to hypergraphs of genetic pathways for the cancer subtype classification task, and showed that our model outperforms baselines by capturing the functional semantic similarity of genetic pathways.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a hyperedge disentangling method, called Natural-HNN, that captures the inherent hyperedge types or the interaction context of hyperedge, based on the naturality condition in category theory.

### Strengths
1. The authors have identified an interesting issue in hypergraph representations and the solution that guidance for disentanglement hyperedge is pretty novel. 
2. The experiments are comprehensive, including 8 clinical datasets, 8 benchmark datasets, and a synthetic dataset. 
3. This paper is well-organized and easy to follow.

### Weaknesses
1. I am  a little bit concern with the overfitting issue, as it contains $k$ MLP for each layer. Does the parameters shared across layers?
2. How does the heterophilic level for the clinial datasets look like? From the model design, it may works well for heterophilic hypergraphs. Can you also report performance for heterophilic hypergraphs, e.g. Congress, Senate, and Walmart in EDHNN [1]?

### Questions
Please see the weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents Natural-HNN, a hyperedge disentangling method designed to identify hyperedge types or interaction contexts within hypergraphs. Natural-HNN incorporates a message-passing layer that leverages node-to-hyperedge interactions, allowing it to capture the underlying structure of hyperedges more effectively. The authors validate their approach on a hypergraph of genetic pathways, showing that Natural-HNN outperforms established baseline methods.

### Strengths
- This paper addresses the novel and important problem of hyperedge disentangling
- The authors applied their method on a hypergraph of genetic pathway which is an interesting application.

### Weaknesses
 - The proposed method lacks novelty.
- The primary issue addressed by this paper—namely, that convolution-based methods cannot perform interaction context-dependent message passing—could be resolved by considering the bipartite representation of a hypergraph and applying a simple message-passing mechanism on it.
- The example provided in Figure 1 is confusing, and none of the datasets are related to it. It would be more compelling if Figure 1 were related to the genetic pathways experiment.
- The authors assert that a drawback of sheaf-based methods is that "there is no guidance that helps the transformation to be related to interaction context." However, they do not explain why this is a drawback or why such guidance is important.
- The introduction is verbose, and portions of it could be more appropriately placed in the related works section.
- Section 3 and Figure 2 are positioned too closely, making the text difficult to follow.
- In Section 5, the authors state, "there is no benchmark dataset verified to contain useful interaction context that is related to the task." If this is the case, the motivation for the proposed method is unclear.
- The model performance shown in Table 1 does not significantly surpass the other baselines.
- Although the authors claim to have an effective hyperedge disentangling method, they need to demonstrate that they have addressed the disentanglement problem in their experiments.

### Questions
- What is the motivation behind this work?
- Could this method be applied to standard hypergraph datasets (as presented in previous work), and could you provide results for those datasets as well?

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
The paper introduces Natural-HNN, a hypergraph neural network (HNN) designed to effectively capture the context of interactions within hyperedges. In experiments, it outperforms baseline models in cancer subtype classification.

### Strengths
The paper is clearly presented and easy to follow, with the proposed model demonstrating superior empirical performance compared to existing baseline methods.

### Weaknesses
This paper overlooks an important related work [1], which also discusses the idea that different hyperedges provide distinct contextual information to different nodes. In the introduction, the authors highlight one of their key contributions, stating, "To the best of our knowledge, we are the first to propose a hyperedge disentanglement-based method that is systematically designed to capture the context of multiway interaction." Therefore, it is crucial to clarify the differences and advantages of the proposed method compared to the approach presented in [1].

This paper applies the proposed method to a general node classification setting, which raises questions about the importance of modeling interaction context. While the authors claim that capturing interaction context is crucial for improving model performance, they do not provide sufficient justification for why this is the case in the specific context of the cancer subtype classification task. The connection between modeling hyperedge context and improved performance in this task remains unclear. The paper lacks a detailed explanation of how the disentangled representations of hyperedges lead to better node classification, especially when compared to methods that do not explicitly model this context. It is not clear what specific aspects of the hyperedge context are being captured and how these aspects are relevant to the classification task.

Furthermore, the novelty of the proposed method compared to WhatsNet [1] remains vague. The paper does not provide a clear explanation of the architectural differences that make the proposed model more effective at capturing background information. The authors need to provide a more detailed comparison of the two methods, including a discussion of the specific mechanisms by which each model captures contextual information. It is unclear what specific design choices in the proposed model allow it to capture the intended interaction context more effectively than WhatsNet.

### Questions
[1] applies the proposed method to the edge-dependent node classification task, where node labels are determined by the hyperedge context. This makes it clear and intuitive why modelling the hyperedge context is beneficial for enhancing model performance. However, in this paper, the authors apply their method to a more general node classification setting, which raises questions about the importance of modelling interaction context. It would be helpful if the authors included a dedicated section discussing why capturing interaction context is crucial for improving model performance.

Minor: It seems that the link to the code provided in the paper does not work. Could the authors please double-check the accessibility of the code?

[1] Choe, Minyoung, et al. "Classification of edge-dependent labels of nodes in hypergraphs." Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining. 2023.

### Soundness
2

### Presentation
3

### Contribution
2

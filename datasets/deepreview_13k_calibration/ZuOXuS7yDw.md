# GRAMA: Adaptive Graph Autoregressive Moving Average Models

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 8, 5, 6

## Abstract
Graph State Space Models (SSMs) have recently been introduced to enhance Graph Neural Networks (GNNs) in modeling long-range interactions. Despite their success, existing methods either compromise on permutation equivariance or limit their focus to pairwise interactions rather than sequences. Building on the connection between Autoregressive Moving Average (ARMA)  and SSM, in this paper, we introduce GRAMA, a Graph Adaptive method based on a learnable Autoregressive Moving Average (ARMA) framework that addresses these limitations. By transforming from static to sequential graph data, GRAMA leverages the strengths of the ARMA framework, while preserving permutation equivariance. Moreover, GRAMA incorporates a selective attention mechanism for dynamic learning of ARMA coefficients, enabling efficient and flexible long-range information propagation. We also establish theoretical connections between GRAMA and Selective SSMs, providing insights into its ability to capture long-range dependencies. Extensive experiments on 14 synthetic and real-world datasets demonstrate that GRAMA consistently outperforms backbone models and performs competitively with state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper shows a design that applies SSM model through ARMA to graph domain, and claims that it can solve the long-range interaction problem in graph domain. The author designs a simple deep ARMA framework with GNN backbone inside, to store many state representations for higher order long-range information. In experiments, the author shows certain improvement to baselines.

### Strengths
1. I agree that using more states that used in SSM can preserve more higher-order informations in long-range problem setting, which can be helpful for certain long-range multi-polynomial regression problems. Extending SSM to graph domain can be a good attemp. 
2. Overall the design is easy to follow.

### Weaknesses
1. The paper is like a naive design of a new model without clear motivation. It appears to just extend SSM/ARMA to graph domain for a new model or a new paper, without clear motivation from the graph problem side. While long-range problem is an issue in graph domain, adapting an existing model to this domain without domain-specific designs and motivations is not helpful for the domain. This is just like a "combine A and B" paper.

2. While the presented framework "claims" supporting any GNN backbone, it does not give particular support/explanation of what kind of functions/graph informations that can be obtained with adding this framework. Clearly, there should be a discussion about GNN backbone vs GNN + proposed framework, in terms of their computational cost, memory requirement, function approximation ability, long-range regression error analysis and so on. Without these, this paper does not provide good content/guidance for the development of this domain.

3. When looking at the result, I don't see a dramatic improvement comparing to simple baselines, although the proposed framework clearly use much more representations, memory, and computation.

### Questions
I suggest the author focus on what problem you want to solve, and clearly demonstrate why this can solve the graph problem you want to solve, with solid theoretical support.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper introduces GRAMA (Graph Adaptive Autoregressive Moving Average Models), a novel framework that enhances Graph Neural Networks (GNNs) by integrating adaptive neural Autoregressive Moving Average (ARMA) models. GRAMA addresses the limitations of existing Graph State Space Models (SSMs), which either compromise on permutation equivariance or focus only on pairwise interactions rather than sequences. The key innovation is the transformation of static graph data into sequential graph data, allowing GRAMA to leverage the strengths of the ARMA framework while preserving permutation equivariance. GRAMA also incorporates a selective attention mechanism for dynamic learning of ARMA coefficients, leading to efficient and flexible long-range information propagation.

### Strengths
1. This paper introduces a new way of combining ARMA with GNNs, addressing limitations in handling long-range interactions and permutation equivariance in graph data.
2. This paper provides a theoretical foundation that establishes connections between GRAMA and SSMs.
3. The authors have tested the proposed GRAMA on a wide range of tasks and benchmarks, and the overall paper is experimentally solid.

### Weaknesses
1. While I acknowledge that the authors conducted extensive experiments, several highly relevant baselines or benchmarks are notably absent. In Section 5.2, the graph property prediction datasets employed are not mainstream. Why not utilize more widely recognized real-world datasets such as ZINC or OGBG-MOLHIV/MOLPCBA? Additionally, the chosen heterophily GNNs in Table 4 do not represent the current state-of-the-art models; please refer to [1,2]. The absence of these established benchmarks and state-of-the-art models makes it difficult to assess the true performance and generalizability of the proposed method. Specifically, the graph property prediction tasks, while useful for demonstrating oversquashing, lack the real-world complexity found in datasets like ZINC, which is a standard benchmark for molecular property prediction, or OGBG-MOLHIV, which is widely used for assessing graph neural network performance on biological tasks. The heterophily GNNs used also do not reflect the current advancements in the field, potentially skewing the comparison against GRAMA.

2. The baselines selected by the authors across various tables exhibit significant variation. For instance, in Tables 2 and 3, despite both being graph-level tasks, the baseline choices for the graph transformer differ. Furthermore, Table 1 includes only a single GPS, contrasting sharply with the diverse graph transformer baselines in other tables. Figure 2 does not specify which GNN is combined with GRAMA, and Table 1 appears to lack results for GRAMA+GatedGCN. Such inconsistencies may confuse readers; I believe the authors should standardize baseline selections or provide detailed explanations in the main text. The lack of consistency in baseline selection makes it difficult to compare the performance of GRAMA across different tasks and against different models. For example, the graph transformer baselines in Tables 2 and 3 use different positional encodings, making it unclear whether performance differences are due to the model architecture or the encoding method. The absence of GRAMA+GatedGCN in Table 1 also leaves a gap in the evaluation, as GatedGCN is a commonly used GNN architecture.

3. (I am a non-expert of SSMs, and the following comment may be somewhat amateurish) My understanding is that the sequence of $L$ node features $\mathbf{F}^{(0)}$ is generated by MLPs, which somewhat artificially constructs a dynamic graph sequence where node features evolve over time. However, I fail to see how this leads to a performance gain; generating a length-$L$ node feature sequence seems equivalent to performing $L$ transformations on node embeddings in MPNN. Even with GRAMA block, it appears to be somewhat equivalent to MPNN's ego-node update. I feel (though I may be incorrect; please correct me if so) that this approach is better suited for real-world dynamic graph sequence modeling. The artificial generation of graph sequences through MLPs raises questions about the method's ability to capture meaningful temporal dynamics. The equivalence to $L$ transformations on node embeddings in MPNNs suggests that the method may not be fundamentally different from existing message-passing approaches. The connection to ego-node updates further reinforces the concern that the method may not be fully leveraging the sequential nature of the ARMA model.

### Questions
see weaknesses

### Soundness
3

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
The article presents GRAMA a novel framework designed to enhance Graph Neural Networks (GNNs) by addressing their limitations in handling long-range dependencies. Traditionally, GNNs struggle with issues like oversquashing, where distant node information is compressed, making it challenging to capture extensive interactions across the graph. 

GRAMA is built on the Autoregressive Moving Average (ARMA) model framework, allowing GNNs to convert static graphs into sequences of graphs, effectively enabling them to process autoregressively. GRAMA adapts SSM concepts to a graph setting while maintaining permutation invariance. GRAMA includes a selective attention mechanism that dynamically adjusts ARMA coefficients across nodes in the graph, which efficiently propagates long-range information across graph structures. 

GRAMA is built on blocks combining AR and MA framework. In these blocks, the graph representation is transform in a graph sequence. A GNN backbone is incorporated into each GRAMA block, allowing further information exchange between nodes based on graph structure.
The model stacks multiple GRAMA blocks to form a deep GRAMA network. 
GRAMA includes an attention mechanism, which adjusts the AR and MA coefficients.

The paper also present some theoretical basis about the model interpretation (equivalence between ARMA and SSM) and and its stability conditions. 
The model is evaluated on 4 datasets, including synthetic and real-world graphs, where it consistently outperforms its backbone models.

### Strengths
The paper presents an innovative approach for sequential learning on graphs, specifically adapting the ARMA/SSM framework to graph data while preserving permutation equivariance.

Experimental results demonstrate that GRAMA achieves strong performance, consistently outperforming its backbone model and competing effectively with state-of-the-art methods.

NB: These are shortly formulated but important strengths.

### Weaknesses
The paper has three main weaknesses: (1) model presentation readability, (2) lack of references and attributions, and (3) limited discussion on potential model limitations.

1) Model Presentation Readability
The model presentation is challenging to follow, and improvements in clarity are necessary for readers to grasp the structure and function of GRAMA fully.
  - For instance, in the caption of Figure 1, it is stated that the blocks are linear systems; however, they contain GNN layers, which are often nonlinear. Clarification is needed on what aspects are considered linear.
  - There is a lack of clarity on the non-linearity between blocks mentioned in caption of Figure 1, as they do not appear in the model presentation.
  - In Equations (4), (5), and (6), the notation involving $L$ is ambiguous; it is unclear when $L$ represents sequence length and when it is used as a superscript for varying position (i.e., $l$ in \{L, ... , S⋅L\}).
  - The distinction between GRAMA blocks and all possible moving-window remains unclear (i.e., between [\textbf{f}^0, \textbf{f}^{L-1}] and [\textbf{f}^a, \textbf{f}^{L-1+a}], with $a<L$) a more ordered presentation structure could help delineate their unique aspects.

2) Lack of References and Attributions
- The theoretical properties discussed in Section 4 are primarily inherited from the ARMA/SSM framework rather than novel contributions of the paper. It is necessary to explicitly acknowledge that these inherited properties are not original contributions of the paper and to ensure all relevant references are included in Section 4.

3) Lack of Discussion on Limitations
The paper does not adequately discuss potential limitations, which would be important to understand the broader applicability of the model.
- Computational Cost: While computational cost is briefly mentioned in Appendix E, it should be addressed directly in the main text as it appears as a clear limitation of GRAMA. Since GRAMA's may increase the parameter count and computational cost, an ablation study comparing models with equivalent computational budgets would be insightful.
- The experiments evaluate GRAMA on long-range dependency modeling, tasks for which it has been specifically designed. It would be interesting to assess how the model performs on other types of tasks. If not, the paper should at least explicitly state that the evaluation only focus on long-range task experiments.

### Questions
The questions relates to point (1) of 'weaknesses'

- In what blocks are linear systems, and in what they are not?

- How are implemented the non-linearity between blocks?

- More generally, what are the relations between blocks?

- More fundamentally, except to define the initiating and the readout blocks $F^{(0)}$ and $F^{(S)}$ in what blocks are relevant entities?

- In Equations (4), (5), and (6), does $L$ represents the sequence length? If not, please could you clarify. If yes, how to compute $\mathbf{f}^{L+1}$

### Soundness
3

### Presentation
1

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
The paper introduces an approach to enhance GNNs by modeling long-range interactions through a learnable ARMA framework. The proposed GRAMA transforms static graph data into sequential data, leveraging the strengths of ARMA while maintaining permutation equivariance. GRAMA incorporates a selective attention mechanism for dynamic learning of ARMA coefficients, enabling efficient and flexible long-range information propagation.

### Strengths
- GRAMA can see further in the graph data, capturing long-range interactions that traditional methods might miss.
- GRAMA works well with various GNN backbones, enhancing their capabilities without losing their original strengths.
- The paper is well-written and easy to understand.

### Weaknesses
 - How does the integration of the ARMA framework with GNNs affect the model's ability to capture long-range dependencies compared to traditional GNNs? Specifically, what are the limitations of standard message passing in capturing long-range dependencies, and how does the proposed method overcome these limitations? It would be beneficial to see a more detailed analysis of how the sequential processing of graph data enables the model to capture information across distant nodes, which is not easily achieved by standard GNNs.
- What insights can the authors provide on the design choices behind the selective attention mechanism for learning ARMA coefficients? What is the rationale for using attention, and how does it compare to other potential methods for learning these coefficients? A deeper discussion on the specific advantages of the chosen attention mechanism, including its computational cost and its impact on model performance, would be valuable.
- How do the theoretical connections to SSMs influence the model's architectural decisions and performance? What specific theoretical properties of SSMs are leveraged in the design of GRAMA, and how do these properties translate into practical benefits? A more detailed explanation of the theoretical underpinnings and their influence on the model's architecture would strengthen the paper.
- How do the results of GRAMA compare to other state-of-the-art methods in terms of accuracy and computational efficiency? While the paper presents some results, a more comprehensive comparison, including a wider range of state-of-the-art methods and a detailed analysis of computational costs (training and inference time, memory usage), would be beneficial.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
3

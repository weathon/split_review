# Query-Aware Learnable Graph Pooling Tokens as Prompt for Large Language Models

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 3, 5, 6

## Abstract
Graph-structured data plays a vital role in numerous domains, such as social networks, citation networks, commonsense reasoning graphs and knowledge graphs. While graph neural networks have been employed for graph processing, recent advancements have explored integrating large language models for graph-based tasks. In this paper, we propose a novel approach named Learnable Graph Pooling Token (LGPT), which addresses the limitations of the scalability issues in node-level projection and information loss in graph-level projection. LGPT enables flexible and efficient graph representation by introducing learnable parameters that act as tokens in large language models, balancing fine-grained and global graph information. Additionally, we investigate an Early Query Fusion technique, which fuses query context before constructing the graph representation, leading to more effective graph embeddings. Our method achieves a 4.13\% performance improvement on the GraphQA benchmark without training the large language model, demonstrating significant gains in handling complex textual-attributed graph data.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The paper presents a novel approach for integrating graph representations with large language models (LLMs), addressing the critical challenge of efficient graph-text interaction. The primary contributions are twofold: (1) an early fusion mechanism that performs message passing between sub-graph node representations and query text embeddings, and (2) a learnable pooling strategy utilizing dedicated tokens (LGPT) that act as information aggregators within the graph structure.
The early fusion mechanism is particularly noteworthy as it enables direct interaction between textual and structural information at the embedding level, potentially capturing more nuanced relationships compared to traditional late fusion approaches. The authors implement this through message passing operations that allow bidirectional information flow between the sub-graph nodes and query text representations.
The learnable pooling strategy introduces fully-connected LGPT tokens that serve as dynamic information hubs within the graph. These tokens effectively aggregate information from all nodes through message passing, potentially creating a more comprehensive and adaptable graph representation. This approach appears to offer more flexibility than static pooling methods.

### Strengths
1. The paper introduces an innovative early fusion mechanism that addresses a fundamental challenge in graph-language modeling: the seamless integration of structural and textual information; The learnable pooling tokens (LGPT) provide a flexible and adaptive approach to graph representation, offering advantages over traditional static pooling methods. 

2.The authors conduct extensive experiments across three diverse graph QA datasets, demonstrating the robustness and generalizability of their approach. The method achieves competitive performance compared to state-of-the-art baselines, while potentially offering improved computational efficiency.

### Weaknesses
1. The paper's scalability argument lacks sufficient comparative analysis against existing methods like G-retriever and GraphToken; The authors do not provide a detailed complexity analysis or empirical benchmarks to substantiate their efficiency claims; While the authors assert improved efficiency compared to Tian et al. 2024 (Line 210), this claim requires further scrutiny since: a). The dominant computational cost typically lies in the LLM inference; b). The relative improvement in message passing efficiency may be marginal in the overall computational pipeline; c) No concrete timing or memory usage comparisons are provided.
2. The evaluation is primarily confined to GraphQA tasks, leaving several important questions about generalization unexplored: a). The method's effectiveness on standard graph learning tasks (node classification, link prediction) remains unvalidated; b) The paper lacks a theoretical or empirical bridge between GraphQA performance and the claimed improvements in node-level and graph-level information integration. A broader evaluation across diverse graph-based tasks would strengthen the paper's contributions. 
3. The hyperparameter analysis in Section 4.4 shows significant gaps in the experimental design: The LGPT token count investigation only examines extreme values (8 and 32), omitting crucial intermediate points; The impact of other critical hyperparameters (e.g., message passing steps, fusion layer configurations) is not thoroughly explored. 
4. The paper should improve the methodological clarity from a). a more rigorous theoretical justification for the chosen LGPT architecture; b). Clear computational complexity analysis compared to baseline methods.

### Questions
1. How sensitive is the model's performance to the choice of text encoder in Equation 7?
2. Have the authors experimented with different text encoders (e.g., BERT variants, RoBERTa, T5) and observed any significant variations in performance?
3. Regarding Equation 5, how does the choice of graph encoder architecture impact the model's performance?
4. Can the authors provide case studies or visualization analysis demonstrating how LGPT addresses information loss compared to baseline methods?
5. In Equation 9, please clarify the definition and dimensionality of $S_g$
6. For Equation 10, please provide a detailed explanation of $S_p$ and its role in the architectur

### Soundness
2

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
This paper leverages graph neural networks and large language models for task of knowledge graph question answering. Based on recent proposed techniques include graph soft prompt and query-aware graph prompting. The author proposed query-aware graph pooling to overcome the limitations of node-level and graph-level representations. In experiments, it shows competitive performance on recent proposed graph QA benchmarks in different domains.

### Strengths
1. The paper identifies a critical disadvantage of graph pooling method; the granularity control is either graph-level or node-level. 
2. On this pain point, the proposed multiple tunrable prompt (LGPT) effecvtively imrpove the performance on benchmarks.

### Weaknesses
1. The novelty of the paper is questionable. As the author mentioned, recent work such as G-Retriever;Graph Token and GNP (Graph Neural Prompting) has covered most of the techniques used in the paper except the graph prompt paramters. However, the learnable graph prompt is proposed in multiple related work including [1] and supernodes (connect every node to a virtual node for pooling) in graph pooling [2] literature.

2. The proposed work re-uses most of the component of G-Retriever, which also causes my concern on cherry-picking hyperparameters given the performance improvements over G-retriever is subtle.

### Questions
1. What's the perfomance of LGPT in figure 1 without GNN and fine-tune lanaguage model (i.e. GraphToken with LLM fine-tuning)? It would be interesting to see whether design of graph pooling is still neccessary when LLM is tunable given that GNN introduces additional parameters.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper addresses the problem of Textual-Attributed Graph QA, divided into two main steps: sub-graph retrieval and answer generation. For answer generation, their approach transforms the sub-graph into textual embeddings through a prompt, generates embeddings, and then uses a graph encoder with learnable parameters to process them. The paper highlights scalability issues in node-level prompting (where each node is treated as a separate token in the language model) and information loss in graph-level projection (where the entire graph is compressed into a single vector). To address this, the authors propose Learnable Graph Pooling Tokens (LGPT), a pooling method that introduces learnable parameters (tokens) that connect to all nodes and perform message passing. This method allows for flexible, efficient graph representation that balances fine-grained and global information, achieving improved performance on Graph QA tasks.

### Strengths
The paper is easy to read and understand. Extensive experiments and analysis have been shown to prove the proposed method.

### Weaknesses
The idea of “early fusion” by forming an external node and fully connecting to other nodes in the graph is not novel to the field. The LGPT idea seems intuitive that increasing the number would increase the performance but would like to see more analysis here.

### Questions
1. “ However, the key difference from these methods is that, instead of pooling into a single graph embedding, our approach uses multiple learnable tokens for pooling, thereby reducing information loss” - Is there a pattern in the information loss. Is there a way to quantify this loss other than looking at the accuracy? What kind of data samples perform better when we increase the number of LGPT? 

2. How does the number of LGPT performance vary with the different datasets?

### Soundness
2

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
- This paper proposes a learnable graph pooling module to enhance LLM-based GraphQA.

### Strengths
- The combination of LLM and GNN is an important research topic.
- The design of this paper is reasonable.

### Weaknesses
 - The novelty seems to be limited in this paper because authors only made a new incremental design in the graph encoder. The core paradigm of graph QA is preserved compared with other baselines.
- Some important GNN+LLM baselines are missing in the experiments. For example, GNP [1].
- The training/inference efficiency of the method should be compared with other baselines.
- The detailed information about the graphs in each dataset is not reported.
- The original dataset and README instructions are not provided in the code, making it difficult to reproduce the performance.

### Questions
- What is the meaning of Sf in the author keywords?
- See weaknesses and make some revisions to the paper.

### Soundness
2

### Presentation
3

### Contribution
2

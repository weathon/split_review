# GL-Fusion: Rethinking the Combination of Graph Neural Network and Large Language model

- Decision: Reject
- Scores: 5, 6, 5, 5

## Abstract
Recent research on integrating Large Language Models (LLMs) with Graph Neural Networks (GNNs) typically follows two approaches: LLM-centered models, which convert graph data into tokens for LLM processing, and GNN-centered models, which use LLMs to encode text features into node and edge representations for GNN input. LLM-centered models often struggle to capture graph structures effectively, while GNN-centered models compress variable-length textual data into fixed-size vectors, limiting their ability to understand complex semantics. Additionally, GNN-centered approaches require converting tasks into a uniform, manually-designed format, restricting them to classification tasks and preventing language output. To address these limitations, we introduce a new architecture that deeply integrates GNN with LLM, featuring three key innovations: (1) Structure-Aware Transformers, which incorporate GNN’s message-passing capabilities directly into LLM’s transformer layers, allowing simultaneous processing of textual and structural information and generating outputs from both GNN and LLM; (2) Graph-Text Cross-Attention, which processes full, uncompressed text from graph nodes and edges, ensuring complete semantic integration; and (3) GNN-LLM Twin Predictor, enabling LLM’s flexible autoregressive generation alongside GNN’s scalable one-pass prediction. GL-Fusion achieves outstand performance on various tasks. Notably, it achieves state-of-the-art performance on OGBN-Arxiv and OGBG-Code2,

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposed a method to combine GNN and transformer architecture to learn the graph tasks. Specifically, the graph tokens and text tokens are learned together in a sequence, while the graph tokens are only attending to other graph tokens in the same graph. The graph structures are learned through integrating GNN into prediction layer. The graph tokens are learned by cross attention module over the text tokens.

### Strengths
1. The proposed architecture provides a feasible solution to combine transformer architecture and graph neural networks to learn on graph tasks.

2. The paper is well written and easy to follow.

3. The reported experimental results are good.

### Weaknesses
1. The proposed method is complex which includes three components: text and graph token transformers, text to graph token attention module, and GNN prediction module. The optimization process on three components seem non-trivial. However, the authors did not discuss any details on it. Specifically, it's unclear how the gradients are handled across the different modules, and whether there are any specific strategies employed to ensure stable training, given the different nature of these components (e.g., transformer layers vs. GNN layers). The lack of discussion on potential convergence issues or the need for specific initialization schemes is also a concern.

2. The method needs to train a new transformer architecture, which seems not easy to combine with existing pre-trained LLMs. It's not clear how the proposed architecture can leverage the vast knowledge encoded in existing pre-trained language models, which are typically trained on massive text corpora. The paper does not discuss the potential for transfer learning or fine-tuning strategies that could mitigate the need to train a new transformer from scratch, which would be computationally expensive and data-intensive.

3. The included datasets for node classification is limited (only two datasets). The reported results in link prediction table lacks most of the comparison results. The limited number of datasets makes it difficult to assess the generalizability of the proposed method. Furthermore, the lack of comprehensive comparison results in the link prediction table makes it hard to evaluate the performance of the proposed method against existing state-of-the-art approaches.

### Questions
For optimization process, is this method using back propagation to directly optimize all parameters?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents GL-Fusion, an architecture integrating the capabilities of graph neural networks (GNNs) and large language models (LLMs). The proposed architecture attempts to address limitations in existing methods for GNN-LLM fusion by carefully embedding GNN structure within LLMs to leverage both structural graph data and rich textual information. Components of the architecure include structure-aware Transformer layers, cross-attention between graph and text, and GNN-LLM integrated predictor, which together tries to enable simultaneous handling of textual and structural features while providing flexibility in output. GL-Fusion shows improvement across various tasks, outperforming baseline GNN-centered, LLM-centered, and hybrid models from the recent literature.

### Strengths
- the design of the architecture builds upon the recent research on LLMs for text attributed graphs and addresses some limitations, especially of the existing approaches which only rely on either GNN or LLM as the main model.
- the permutation invariance of graph node tokens is carefully modeled in the structure-aware transformer layer.
- both kinds of gnn based and text based tasks can be conceptually handled using the proposed method.

### Weaknesses
Limitations and questions:
1. if there is a common understanding that self attention is a form of message passing, why is there a need to incorporate a separate MPNN in the structure aware Transformer layer? This aspect is unclear and has not been empirically studied as well. Specifically, the paper does not provide a clear justification for why a standard self-attention mechanism, which can be viewed as a form of message passing, is insufficient for capturing graph structure. The authors should provide a more detailed analysis of the limitations of using self-attention alone for graph representation, and why a separate MPNN is necessary to overcome these limitations. It would be beneficial to see an ablation study comparing the performance of the model with and without the MPNN layer, to empirically demonstrate its importance.
2. in page 5, the positional encoding which would be ideal for both text and graph tokens is discussed. I am wondering if it is possible to have a unified structure based positional encoding which perceives both sequential structure and graph structure as 'arbitrary graph structure'? This is in context of recent works in graph transformer literature which show laplacian eigenvectors can generalize the text positional encoding of Transformers. The paper should explore the possibility of using a unified positional encoding scheme that can handle both sequential and graph structures, such as Laplacian eigenvectors. This could potentially simplify the architecture and improve its ability to generalize across different types of data. The authors should discuss the potential benefits and drawbacks of such an approach, and provide a rationale for their choice of separate positional encoding methods.
3. although the proposed  aims to reduce complexity, the integration of graph structures into LLM layers may still encounter scalability issues with large graphs or highly interconnected datasets. How does GL-Fusion handle memory usage and processing time for very large graph structures? The paper needs to address the practical limitations of the proposed architecture when dealing with large-scale graphs. The authors should discuss the computational complexity of their method and provide insights into how it scales with the size of the graph. It would be helpful to see experiments on larger datasets to demonstrate the scalability of the approach, or at least a discussion of the strategies that can be used to mitigate the computational challenges associated with large graphs.

### Questions
included with weaknesses

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
2

### Summary
The manuscript proposes a method that deeply integrates Large Language Models (LLMs) and Graph Neural Networks. The method features structure-aware transformers, graph-text cross attention, and GNN-LLM twin predictor, enabling it to perform tasks of various types related to graphs and language.

### Strengths
1. The method integrates LLMs and GNNs deeper than previous methods by introducing 3 key components.
2. The manuscript has conducted experiments on downstream tasks of various types, including traditional node classification, knowledge-related tasks and text generation, demonstrating the generalizability of the proposed method.

### Weaknesses
1. Experiments are not comprehensive. Baselines and benchmarks are missing. For example, for the node classification tasks, there are only two datasets considered. In Table 3, many entries in the table are missing, which makes the results less convincing. I suggest the author refer to [1] for benchmarking models on text-attributed graphs.

2. The manuscript proposes a twin predictor for node classification. However, edge-level and graph-level tasks should also be considered given their importance in graph-related tasks. Regression tasks should also be considered.

3. The method lacks novelty in terms of architecture innovation. There is a large body of related work in the LLM + Graph field that has not been discussed or included in the performance table. For example, methods like UniGLM, LLaGA, DGTL, and ENGINE, which also explore the integration of LLMs and GNNs, should be included for a more comprehensive comparison.

### Questions
In the Graph-text attention layer, the language tokens do not attend edges. Would the loss of the information affect performance?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper proposes a new architecture to address the limitations of LLM-centered models in capturing structural information and GNN-centered models in capturing textual semantics. This architecture includes three components: (1) Structure-Aware transformer, which integrates GNN and LLM into the same transformer layer, (2) Graph-Text Cross-Attention, allowing direct aggregation of node textual information, and (3) GNN-LLM Twin Predictor, which adds an additional layer to the output of LLMs to adapt to downstream tasks.

### Strengths
- The motivation is interesting.

### Weaknesses
1. The paper is not well written. 
- The use of notations presents a significant problem so that I could not understand the paper. In the preliminaries section, $L_n$ occurs only once. I think that $L$ describing the length of the node text in Line 129 should always be $L_n$. In section 3.2, Equation 3 and Equation 4 are very unclear. None of $T_i, W_q, W_k, X_v$ is defined. It is not clear to me whether $T_i$ in this context refers to the T_i of Equation 2. In line 238, the authors also admits to abusing the notations, and I don't understand why the authors didn't make further corrections.
- The order of Table 1 and Table 2 is also confusing.
- I am suspicious of the time complexity of the cross attention layer because of the confusion of the notations.
- The data format of the table is not aligned.
- There is a large amount of blank data in Table 3 with no further explanation as to why.

2. Lack of important ablation studies and hyperparameter sensitivity analysis. 

The paper proposes three modules, but in the experiments, only 'w/o cross-attention' is included in the graph property prediction task. In general, aggregators we will only use one way, such as max or sum. I'm not sure what the motivation was for designing all three and how they affected the final experimental results in the experiment? I would like to understand the difference between them and the type of information captured, especially the standard deviation. Moreover, the experiments did not indicate the need for a gating mechanism in Equation 2.

3. Detailed descriptions of the dataset and baseline methods are missing.

This paper covers a large number of experimental tasks, but in the appendix, detailed information on the datasets as well as information on the baseline methods are not listed.

4. Lack of important baseline methods. The baseline methods should be divided into three parts, (1) LLM-centered models, (2) GNN-centered models, and (3) combined LLMs and GNNs methods.

- [1] Huang, Qian, et al. "Prodigy: Enabling in-context learning over graphs." Advances in Neural Information Processing Systems 36 (2024).
- [2] Tan, Yanchao, et al. "MuseGraph: Graph-oriented Instruction Tuning of Large Language Models for Generic Graph Mining." arXiv preprint arXiv:2403.04780 (2024).
- [3] Chien, Eli, et al. "Node feature extraction by self-supervised multi-scale neighborhood prediction." arXiv preprint arXiv:2111.00064 (2021).
- [4] Huang, Xuanwen, et al. "Prompt-based node feature extractor for few-shot learning on text-attributed graphs." arXiv preprint arXiv:2309.02848 (2023).

5. I also doubt the reasonability of the proposed model. Consider that we want to do node classification task only. Given limited number of labeled nodes, the model has significant number of trainable parameters than standard GNNs. However, I do not think the proposed model can outperform GNNs under small labeled datasets. So is the model really needed? I do not think so.

### Questions
Please see the comments above.

### Soundness
2

### Presentation
2

### Contribution
3

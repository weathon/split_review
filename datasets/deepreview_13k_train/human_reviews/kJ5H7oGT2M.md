# Learning Long Range Dependencies on Graphs via Random Walks

- Decision: Accept
- Scores: 6, 8, 6, 8

## Abstract
Message-passing graph neural networks (GNNs) excel at capturing local relationships but struggle with long-range dependencies in graphs. 
    In contrast, graph transformers (GTs) enable global information exchange but often oversimplify the graph structure by representing graphs as sets of fixed-length vectors. 
    This work introduces a novel architecture that overcomes the shortcomings of both approaches by combining the long-range information of random walks with local message passing. 
    By treating random walks as sequences, our architecture leverages recent advances in sequence models to effectively capture long-range dependencies within these walks.  
    Based on this concept, we propose a framework that offers
    (1) more expressive graph representations through random walk sequences, 
    (2) the ability to utilize any sequence model for capturing long-range dependencies, and 
    (3) the flexibility by integrating various GNN and GT architectures. 
    Our experimental evaluations demonstrate that our approach achieves significant performance improvements on 19 graph and node benchmark datasets, notably outperforming existing methods by up to 13\% on the PascalVoc-SP and COCO-SP datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the challenge of capturing long-range dependencies in GNNs by combining random walks with local message passing. The authors utilize State Space Models (SSMs) to model random walk sequence. Theoretical analysis highlights the expressiveness of the proposed approach, and experimental results show that it outperforms the selected baselines.

### Strengths
1. The issue of long-range dependencies in GNNs is an important and valuable area of exploration.
2. The proposed method is versatile and can be integrated with various models.
3. The authors offer theoretical insights, including the expressiveness of the proposed method.

### Weaknesses
1. The novelty of this method is limited, as random walks, combining local and global information, and SSMs are established techniques. For example, Graph-Mamba [1] also uses random walks and Mamba on GNNs, and graph transformers typically combine global and local data.

2. The datasets selected for node classification are mainly heterophilic. Including commonly used datasets like OGB would provide a more comprehensive evaluation.

3. The source of the performance gains is unclear—whether they stem from pretraining, positional encodings, or SSMs. An ablation study would help clarify each component's impact.

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In order to learn long range dependencies, this paper presents NeuralWalker architecture that samples random walks from the graph, treats them as sequences, encode these sequences using a sequence layer and finally integrates this module with local and global message passing to better learn graph structure. It provides theoretical results to show the expressive power of NeuralWalker.

### Strengths
- The paper is overall well-written.   
- Incorporating random-walks in graph learning is an important direction mainly due to its efficiency and ability to learn the long-range dependencies.
- Theoretical results have provided detailed discussions about the expressive power of NeuralWalker and motivates its design.
- The training details for reproducibility are reported, which can help future studies to better understand the weaknesses/strengths of NeuralWalker.

### Weaknesses
 - My main concern is that there are several claims in the paper that have remained unsupported/unclear:
  - The authors claim that ``our approach achieves significant performance improvements on 19 graph and node benchmark datasets``. Based on the reported results NeuralWalker underperforms baselines and several missed state-of-the-art methods. Even looking at the current baselines NeuralWalker does not provide performance improvements in all the 19 datasets!
  -  The authors claim that ``CNNs present a compelling alternative for large datasets due to their faster computation (typically 2-3x faster than Mamba on A100)``. Where are the results for this? How is this trade-off between efficiency and performance?
  - The authors several times mentioned efficiency as the motivation of their method. I couldn’t find any comparison with baselines with respect to memory usage and speed. While training time is reported in Tables 9-12, the training time for baselines and also the memory usage of NeuralWalker and baselines are unclear.
  - Without local/global encoding the performance of NeuralWalker significantly drops. How the results can support the importance of using random walks for long-range dependencies?
  - Since the authors have claimed performance improvement over existing methods, it is important to choose the right baselines. For example, although the results of POLYNORMER (Deng et al., ICLR 2024) are reported in Table 5, their results are missing in other experiments. Also, the results for several recent efficient methods are missing: GSSC (Huang et al., 2024), GOAT (Kong et al., ICML 2023), and GRED (Ding et al., ICML 2024). It would be great if the authors could use consistent baselines across different experiments so the performance gain becomes clear. Also, I believe a comparison with random walk-based GNNs like GraphSAGE is required.
- There are several missing related articles. I suggest discussing these methods to further clarify the novelty of NeuralWalker. For example, there are several recent methods that also have used sequence layers for graphs GSSC (Huang et al., 2024), and GRED (Ding et al., ICML 2024).
- This paper has overlooked a version of graph-mamba (Behrouz et al., KDD 2024), which also uses random walks to learn long-range dependencies. I found NeuralWalker very similar to this method when the number of sampled walks per node is 1. It would be great if the authors clarify and discuss the differences.
- Based on the results in Table 6, without local and global message passing the performance of the proposed method drops significantly. This raises concerns about the significance of the proposed method as it seems the main reason for the competitive performance of NeuralWalker is the use of local/global message-passing modules.

### Questions
- Why Polynormer’s results are missing in LRGB and GNN benchmark experiments?
- What are the main differences between NeuralWalker with the tokenization module in graph-mamba (Behrouz et al., 2024), where the number of random walk samples ($M$) in their framework is 1?
- Although random walks can provide a natural sequence to learn long-range dependencies, they also can be sensitive to noisy connections. How does NeuralWalker perform in these cases?
- In the theoretical results, don’t you need to assume that your sequence model is a universal approximator? Without this assumption how one can compare the expressive power of NeuralWalker after encoding walks with the 1-WL test?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents NeuralWalker, which combines random walks and message-passing mechanisms to capture both local and long-range dependencies in graphs. The model processes graphs by treating random walks as sequences, thereby leveraging sequence models to handle long-range interactions.

### Strengths
1.	Existing graph transformers works typically incorporate random walks as positional encodings; directly integrating them into token design is an interesting approach.

2.	The theoretical analysis provided is thorough and comprehensive.

3.	Extensive experiments are conducted, with detailed results presented both in the main text and the appendix.

### Weaknesses
1. The primary concern is the unclear motivation. Why do the authors choose to integrate random walks into token design, and how could this approach benefit over graph transformers, which can already use positional encodings to capture structural information? A preliminary study exploring this choice would be helpful.

2. Building on this, the purpose of incorporating multiple techniques, such as the walk aggregator, also lacks clarity. For instance, why use average pooling in the walk aggregator? Do different random walks carry the same importance?

3. Another concern is the lack of technical innovation. It’s difficult to discern a clear distinction between NeuralWalker and graph transformers, as NeuralWalker appears to follow general design principles of graph transformers, treating the graph as a sequence and representing tokens as the combination of nodes, edges, and positional encodings, albeit based on random walks.

4. Could the authors clarify why SSE performs better than transformers? Since SSE and Mamba are designed based on RNNs, have bidirectional RNNs been tried as a sequence model?

5. I also question the motivation for including global message passing although the ablation study shows it could help. When the length of random walks is long, they should already capture global information inherently. Besides, the authors directly borrow existing graph transformer methods for this, could you provide an ablation study on the choice of graph transformer in this part?

6. Following this, an empirical efficiency comparison—specifically running time and memory usage—against current graph transformer baselines like Polynormer would be beneficial.

7. Another major issue is the absence of several recent baselines. In traditional GNNs, several works, like LazyGNN[1], aim to capture long-range dependencies. There are also state-of-the-art graph transformers, such as VCR-Graphormer[2] and GOAT[3], and crucially, since the authors use SSE as a sequence model, Graph Mamba[4] should be included as a baseline.

8. The datasets are not large enough, especially for node classification tasks. Commonly used datasets like the medium-sized ogbn-products or the large-sized ogbn-papers100m are not included. The current datasets are not common and cannot be considered as large-scale.

### Questions
1.	Is the motivation for using the random walk sampler driven by memory constraints? Additionally, in Figure 3, why does the ZINC dataset display a different trend compared to the other two datasets?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes the NeuralWalker architecture. This GNN processes sequential graph features obtained from random walks with sequence models such as SSMs. This process is interleaved with message passing modules. This construction aims to address the main weaknesses of prior random walk-based methods by encouraging longer-range information flow and utilizing breadth-first structural information.

The paper provides a theoretical analysis showing formally that NeuralWalker is more expressive than 1-WL and CNN-based random walk models like CRaWl. An experimental analysis further demonstrates strong overall performance on a range of standard benchmarks. The option of pertaining on the task of predicting the random walk features is explored. The experiments further show that random-walk-based methods like NeuralWalker can scale to large graphs with over 1M vertices.

### Strengths
* NeuralWalker successfully addresses several weaknesses in prior random-walk-based approaches by using SSMs in a novel context.
* The provided experiments and ablations are rather comprehensive.
* Pretraining a sequence model to predict the structural encodings of random walks is a novel idea, and the results presented here seem promising.

### Weaknesses
A weakness of this paper is a lack of discussion of "old" RNN architectures like LSTMs. While these have become less popular, it would be helpful to highlight why more modern long-sequence models like SSMs are preferable in the context of NeuralWalker. In fact, when compared to both Transformers and SSMs classical RNNs have been shown to have superior expressivity in terms of circuit complexity when the input sequence length is unbounded [1]. In a setting where the walk length is unbounded, an RNN-based NeuralWalker may therefore be more expressive than an SSM-based model. Exploring such a scenario in-depth is out of scope for the work presented here, but I do think a brief discussion of RNNs as an alternative sequence model choice is justified.

### Questions
* The result that SSMs outperform Transformers in the context of NeuralWalker is very interesting. Are there some theoretical insights as to why self-attention is not well-aligned with processing walk embeddings?

* I would also appreciate a comment on the point raised in "Weaknesses".

### Soundness
3

### Presentation
3

### Contribution
3

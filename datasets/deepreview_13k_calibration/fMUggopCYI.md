# Co-Representation Neural Hypergraph Diffusion for Edge-Dependent Node Classification

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 8, 3

## Abstract
Hypergraphs are widely employed to represent complex higher-order relations in real-world applications. Most hypergraph learning research focuses on node-level or edge-level tasks. A practically relevant but more challenging task, edge-dependent node classification (ENC), is only recently proposed. In ENC, a node can have different labels across different hyperedges, which requires the modeling of node-edge pairs instead of single nodes or hyperedges. Existing solutions for this task are based on message passing and model interactions in within-edge and within-node structures as \textit{multi-input single-output} functions. This brings \textbf{three limitations}: (1) non-adaptive representation size, (2) non-adaptive messages, and (3) insufficient direct interactions among nodes or edges. To tackle these limitations, we propose \textbf{CoNHD}, a new ENC solution that models both within-edge and within-node interactions as \textit{multi-input multi-output} functions. Specifically, we represent these interactions as a hypergraph diffusion process on node-edge co-representations. We further develop a neural implementation for this diffusion process, which can adapt to a specific ENC dataset. Extensive experiments demonstrate the effectiveness and efficiency of the proposed CoNHD method.}}\enlargethispage{1.5\baselineskip}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a new hypergraph diffusion-based neural network for edge-dependent node classification (ENC). The paper's main contribution is extending hypergraph diffusion using node-hyperedge co-representations to make hypergraph diffusion better to handle the ENC.

### Strengths
The authors propose a new approach to solving the ENC problem. The whole process sounds technical. Experiments show that the proposed method is highly competitive.

### Weaknesses
The contribution and novelty of the proposed methodology are limited. The paper applies hypergraph diffusion proposed by the previous method EG-GNN. The most significant difference lay in the input and output (single -> multi). The multi-input and multi-output are also explored in the previous message-passing works. Actually, the multi-output or multi-input function can not be an essential difference. e.g. you can concatenate multiple inputs to be a single input, and then use a single input function to process it (e.g. f(x,y) = g([x,y])).  So, combining the edge and node representation into the EG-GNN to improve ENC seems trivial.

The author should add a reference for problem 1.

minor: figure 3, UNP- > UNB

### Questions
Further, I am still concerned about the setting of this paper. In my understanding, the edge-dependence node classification problem can be equivalent to the equivalent star-expansion graph edge prediction problem. In this real-world problem, can it be directly modeled as a graph instead of a hypergraph, and directly use the graph neural network to process it? if so,  can you analyze the pros and cons of each approach?

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
4

### Summary
This paper proposes a method, called CoNHD to tackle edge-dependent node classification tasks (ENC). Unlike node-level or edge-level tasks, in ENC, each node may have a different label across different hyperedges. The authors identify three limitations for the existing models to handle ENC tasks: (1) non-adaptive representation size, (2) non-adaptive messages, and (3) insufficient direct interactions among nodes or edges. To tackle these challenges, this paper introduces CoNHD which models both within-edge and within-node interactions as multi-input multi-output functions.

### Strengths
1. The overall presentation is fair, and audiences can capture the key points in the paper. 
2.  The proposed task is intresting and remains underexplored within the research field.

### Weaknesses
1. The first concern is regarding the novelty of the proposed model. The proposed method is pretty similar to Line Expansion and MultiSet. Besides, the mini-batch strategy is also introduced in MultiSet. How do LEGCN and MultiSet perform on the benchmark ENC datasets?
2. Although the downstream task, i.e., ENC is interesting, can authors further discuss why this task and why this an important topic to study? Because I think the motivations in the paper are also applicable to general node-level/hyperedge-level tasks. 
3. I am still concerned about the efficiency issue, in terms of time and space compelxity, as the method expand every node-hyperedge pair if the node is in the hyperedge. Can authors further discuss the time complexity and space compleity with respect to the hypergraphs, i.e., number of nodes, number of hyperedges, and degrees.

### Questions
See weaknesses above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Traditional Hypergraph Neural Networks (HNNs) struggle with Edge dependent node classification (ENC) tasks, where nodes can have different labels across different hyperedges. To address this issue, the authors propose a new method called Co-Representation Neural Hypergraph Diffusion (CoNHD), which represents node-edge pairs as co-representations, which allows flexible and adaptive handling of ENC. Unlike traditional message-passing methods, CoNHD doesn't rely on fixed representation sizes or non-adaptive messages. The authors develop a hypergraph diffusion mechanism based on neural networks. Experimental results on ten real-world datasets demonstrate the effectiveness and computational efficiency of the proposed approach, with CoNHD consistently outperforming several baseline methods, including both traditional hypergraph neural networks (HGNNs) and edge-dependent methods.

### Strengths
1. The paper tackles an important but under-explored problem of edge-dependent node classification (ENC) on hypergraphs, where nodes can have different labels across different hyperedges. This has many real-world applications mentioned in the paper.
2. The proposed CoNHD model is theoretically grounded, with proofs provided for its increased expressiveness compared to message passing methods. It can also approximate traditional hypergraph diffusion processes. The proposed framework does not rely on a fixed representation size, but adapts based on the node or edge degree. This seems like an innovative mechanism, with potential applications beyond the mentioned problem. 
3. The authors provide a comprehensive experimental study, with results on ten datasets. The proposed CoNHD outperforms all the baselines, based on Micro-F1 and Macro-F1 metrics. CoNHD is also more efficient wrt training time, as shown in Figure 3. 
4. Ablation study provided in the paper compares the different neural operators namely UNB and ISAB, which provides insights into the the effectiveness of multi-output equivariant functions.

### Weaknesses
1. The writing is a bit dense, particularly in section 4, it can be made a bit more readable by providing high level intuition before directly jumping into the concepts. 
2. I don't think the part related to updates with ADMM is needed in the main paper, it can be moved into Appendix. Anyway, the results provided are for GD based implementation. Authors can use that extra space to improve readability. 
3. Authors mention over-smoothing as an issue with the traditional message passing frameworks, but do not provide any experimental evidence as why the proposed method is immune to over-smoothing.

### Questions
I have mentioned a few points in the Weakness section, I do not have more specific questions.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces Co-representation Neural Hypergraph Diffusion (CoNHD) as a novel solution for edge-dependent node classification (ENC) in hypergraphs. Experimental results demonstrate that CoNHD outperforms the selected baselines.

### Strengths
The paper is well-organized and easy to follow, and the proposed model demonstrates superior empirical performance compared to the baselines in the selected setting.

### Weaknesses
1. There is a lack of rigorous guarantees that the three main limitations mentioned in the introduction are thoroughly addressed. Regarding the non-adaptive representation size, to my understanding, the weight matrix W in the final classification layer of the proposed model appears to have fixed dimensions and does not adapt based on the node degree. Concerning the non-adaptive messages, there lack theoretical or empirical results to support that the proposed approach can indeed produce distinct features for the same node across different hyperedges. For example, how different are $h_{v1,e2}$ and $h_{v1,e2}$. As for the insufficient direct interactions, node-to-edge and edge-to-node message-passing operations indirectly exchange information between connected nodes and edges. What additional information gain does the proposed operation provide compared to these node-to-edge and edge-to-node message passing? Is this gain purely intuitive, or is there any theoretical support?

2. The real-world value of this paper remains unclear. To my knowledge, [1] is the first paper to study the hypergraph edge-dependent node classification (ENC) task. In [1], the authors present the ENC task as a benchmark dataset and suggest its primary real-world application lies in generating informative node features for problems such as ranking aggregation and clustering. Conversely, in this paper, the authors argue that the ENC task itself holds significant real-world importance, providing an example involving the classification of the order of authors within a paper. However, it is difficult to envision a scenario where classifying the order of authors for a given paper would be necessary, as both the co-authorship and the order of authors are typically provided alongside the paper. This raises the question: are there any real-world applications that can be naturally modelled as an ENC task?

### Questions
1. To my understanding, most hypergraph neural networks [1-3] are designed for hyperedge prediction and node classification tasks. The ENC task can be viewed as a sub-task of node classification. I was curious whether this method is effective only within this sub-task or if it could also be useful for other types of tasks.

2. Proposition 3 demonstrates that the proposed method can represent existing message-passing hypergraph neural networks. However, I was wondering if this property necessarily implies that the proposed method is more powerful than existing methods across all hypergraph-related tasks. For example, while an MLP is often considered a universal function approximator, there is no evidence to suggest that an MLP can outperform hypergraph neural networks on all hypergraph-related tasks.

[1] Chien, Eli, et al. "You are AllSet: A Multiset Function Framework for Hypergraph Neural Networks." International Conference on Learning Representations.

[2] Chen, Can, and Yang-Yu Liu. "A survey on hyperlink prediction." IEEE Transactions on Neural Networks and Learning Systems (2023).

[3] Antelmi, Alessia, et al. "A survey on hypergraph representation learning." ACM Computing Surveys 56.1 (2023): 1-38.

### Soundness
2

### Presentation
3

### Contribution
1

# CoRe-GD: A Hierarchical Framework for Scalable Graph Visualization with GNNs

- Decision: Accept
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Graph Visualization, also known as Graph Drawing, aims to find geometric embeddings of graphs that optimize certain criteria. Stress is a widely used metric; stress is minimized when every pair of nodes is positioned at their shortest path distance. However, stress optimization presents computational challenges due to its inherent complexity and is usually solved using heuristics in practice.
    We introduce a scalable Graph Neural Network (GNN) based Graph Drawing framework with sub-quadratic runtime that can learn to optimize stress. Inspired by classical stress optimization techniques and force-directed layout algorithms, we create a coarsening hierarchy for the input graph. Beginning at the coarsest level, we iteratively refine and un-coarsen the layout, until we generate an embedding for the original graph. To enhance information propagation within the network, we propose a novel positional rewiring technique based on intermediate node positions.
    Our empirical evaluation demonstrates that the framework achieves state-of-the-art performance while remaining scalable.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Stress is a widely used metric for graph visualization, which aims to find geometric embeddings of graphs that optimize certain criteria. As the stress optimization presents computional challenges due to its inherent complexity and is usually solved using heuristics in practice. The authors introduce a scalable Graph Neural Network based Graph Drawing framework with sub-quadratic runtime that can learn to optimize stress. Inspires by classical stress optimization techniques and force-directed layout algorithms, they create a coarsening hierarchy for the input graph. Beginning at the coarsest level, they iteratively refine and un-coarsen the layout, until generating an embedding for the original graph. The authors perform empirical evaluation demonstrating that their framework achieves SOTA while remaining scalable.

### Strengths
1.	Extensive examples, clear explanations,  step-by-step formulations, and open-sourced code make this research solid, convincing and reproducible. The presentation is obviously above the average.
2.	Extensive experiments demonstrate the effectiveness and the scalability of the proposed framework. 
3.	This research provide insights about cobining the GNN with the graph combinational optimization (i.e. graph visualization). I believe this paper would benifit to the graph mining community.

### Weaknesses
1. Some training details are put in the appendix. I found that after reading the main body of the paper, I couldn’t understand how the framework is applied for training and serving. I think the writing order of the paper needed to be improved. And the figure 2 is relatively hard to understand. Please give a more clear illustration about the graph after being processed by each module in your framework.

2. The work is related with graph condensation or graph summarization, and some baselines about graph condensation or summarizarion should be included.

### Questions
1. Please give a more clear illustration about the graph after being processed by each module in your framework.
2. Is this research related with graph condensation or graph summarization? I mean, maybe some baselines about graph condensation or summarizarion should be included if so.

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
CoRe-GD (CGD) is a effective novel graph drawing algorithm designed with scalability and computational efficiency in mind. The main block of CGD does recurrent layout optimization using two graph neural networks and a graph rewiring step. To achieve better scalability, CGD uses an iterative graph coarsening procedure. The procedure first learns a layout for the coarsest graph view and iteratively uncoarsens the graph and recomputes the optimal layout based on the prior, coarser graph layout. 

Experiments show CGD is effective on an array of datasets with both real and synthetic graphs. Results also show that CGD is effective even on graph sizes larger than those seen during training. 

CGD has scalability evidenced both in theoretical computational complexity as well as in experiments.

### Strengths
Originality - This work presents an original algorithm for learning graph drawing. The model also uses a recurrent GNN, enabled by memory replay. This itself is relatively original, though there are some similar related works. 
Quality - This work is high quality. The model is clear and based on a solid foundation. The results and experiments show significant improvement. 
Clarity - The work is clear, understandable, and well defined. Great clarity. 
Significance - Outside of the Graph Drawing community, it is hard to see this having a broader impact. While the authors claim in the conclusion that because it is embedding based, CGD could be expanded to other applications, there is no direct evidence of that presented. Perhaps it could be used as positional embeddings in graph transformers.

### Weaknesses
I am not heavily knowledgeable about the Graph Drawing community and am not fully aware of the larger impacts (if any) outside of visualizations. It seems to me like this might be a relatively niche community but would defer to other reviewers on that front.

Otherwise, this is a pretty strong, high quality paper.

Figure 6 seems to show that CGD does worse than neato and (sgd)2 for the larger graphs. This is a weakness given that CGD is designed with larger scale graphs in mind.

neato and (sgd)2 do better on larger graphs and PivotMDS does almost as well on larger graphs but is much, much faster. This means CGD is only occupying a kind of middle ground on large graphs.

In addition, while I am not highly familiar with neato and (sgd)2, the fact that they are training free makes me believe they are less complex than CGD from an engineering perspective.

### Questions
“For a cycle graph, this is clearly not desirable and will end in a drawing that is far from optimal.” This is a good example. Would be good to have a visualization (maybe can go in appendix)

The figure 9 visualizations are a very nice way to see the effect of the graph coarsening. 

Though I feel I understand it, a figure showing how the latent embeddings are transferred between supernodes and nodes in the uncoarsening step could be useful. 

Why is DNN^2 excluded from figure 6?

Why does Figure 6.A cutoff at 5000 while 6.B cuts out at 25000?

While I believe I have a strong understanding of the algorithm presented, I do not have a good sense of this field and the most important features, datasets, and related work.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes CoreGD, which is a graph drawing framework which uses GNN submodules.  CoreGD improves over alternative methods in stress metrics and demonstrates empirically better scalability properties.

### Strengths
S1. The point about scale-invariant stress is nuanced and an astute observation -- the authors' lemma 2 helps support the scaling choice.

S2. Performance in graph drawing benchmarks appears to be quite strong in terms of stress metrics compared to alternative approaches.  

S3. Authors were able to demonstrate better scaling performance than the next-best performing alternative (DeepGD it seems) in Figure 6 -- CoreGD seems to scale considerably better and with better stability.

### Weaknesses
W1. For the many readers unfamiliar with graph drawing benchmarks, it would be really helpful to have preliminaries as part of the main paper, and also discussions of the benchmarks to better understand the relative things being compared (I'd guess most GNN-familiar authors aren't familiar with graph drawing). Specifically, a more detailed explanation of the stress metric and its relation to graph drawing quality would be beneficial. The paper should also discuss the specific properties of the benchmark datasets used, such as their size, density, and underlying structure, to provide context for the results.

W2. An efficiency-stress curve would be great to understand relative runtimes and stress performances of the different methods in this landscape, as the authors' individual experiments suggest that CoreGD is the best performing and fastest. This curve should clearly show the trade-offs between runtime and stress for each method, allowing readers to understand the Pareto frontier and the relative advantages of CoreGD. It would also be helpful to see the variance in performance across different runs, not just the mean values.




### Questions
- 3.1 suggests the efficiency and effectiveness for CoreGD is largely influenced by the input feature choice.  Some of the features that offer high discriminability might be difficult/expensive to compute for large graphs (e.g. Laplacian PEs or beacons). 

- The random noise addition step in 3.2 is interesting: this would means the output drawing is stochastic, I guess.  How sensitive are output drawing configurations to the noise introduced here?  

- Section 3's overview of Core-GD is quite hard to understand.  Some design choices aren't obvious to the reader: (i) why do we need two convolutions (Conv_E and Conv_R), (ii) what's the purpose of the rewiring module?  How exactly does the GRU fit in?  Structuring this section with equations which the reader can follow from inputs to position coordinates would have probably helped understand the sequence of operations

- Table 1 suggests that Core-GD seems to achieve similar performance to DeepGD -- I'm not familiar with the differences with these methods, but some discussion regarding the speed advantages of CoreGD compared to DeepGD would be helpful to contextualize the added value of using the algorithm proposed by the authors.  

- Being able to coarsen aggressively before initializing input features seems like a great advantage for large graphs -- I'm curious what the largest graph the authors were able to visualize with CoreGD is given this benefit.  The graphs in Table 1 seem to be mostly small -- are other graph drawing approaches (non-neural or neural) better able to support larger graphs?  In general, a runtime-stress curve which shows the relative performance of multiple methods would be really helpful to see where CoreGD lies on the frontier.

---

Updated my score after reading the authors' responses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The manuscript presents a subquadratic graph drawing algorithm aimed at large-scale graph visualization. The authors propose a hierarchical optimization process to visualize node embeddings from coarse to fine. Additionally, a positional rewiring module is utilized to improve the connection between nodes with potential relationships. The experiments show that the proposed method not only accelerates computations but also improves the visualization quality.

### Strengths
* The paper is well-written with clear objectives and results.
* The algorithm detail is clearly defined and described.
* Alternative methods are discussed and compared for node initialization and positional rewiring step.
* The experimental section evaluates the state-of-the-art methods qualitatively and quantitatively.

### Weaknesses
 * The motivation of the hierarchical optimization and positional rewiring is not clearly introduced. I would recommend the authors discuss the computational complexity among the proposed CoReGD, DeepGD, and SmartGD. In addition, the authors should introduce why positional rewiring is important in hierarchical optimization.
* I found it a bit hard to follow the method section. A diagram of the whole algorithm should be carefully introduced in this section, which can make the readers clearer to the proposed algorithm before diving into the details. It is difficult to understand the pipeline of CoReGD from Figure 2, e.g., h_1^1, h_1^l, h_1^{c+1}.
* I find the effectiveness of the proposed hierarchical optimization in Table 2 and Figure 6. However, the proposed positional rewiring, scale-invariant stress, and replay buffer do not make a significant impact on the stress metric from A.3 Table 3.
* More graph drawing quality metrics can be reported, such as shape-based metrics and edge crossing.

### Questions
Please see my comments to paper weakness.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

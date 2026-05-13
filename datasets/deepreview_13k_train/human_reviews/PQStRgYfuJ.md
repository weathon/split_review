# Topology-aware Embedding Memory for Learning on Expanding Graphs

- Decision: Reject
- Scores: 6, 6, 3, 6, 6

## Abstract
Memory replay based techniques have shown great success for continual learning with incrementally accumulated Euclidean data. Directly applying them to continually expanding graphs, however, leads to the potential memory explosion problem due to the need to buffer representative nodes and their associated topological neighborhood structures. To this end, we systematically analyze the key challenges in the memory explosion problem, and present a general framework, i.e., Parameter Decoupled Graph Neural Networks (PDGNNs) with Topology-aware Embedding Memory (TEM), to tackle this issue. The proposed framework not only reduces the memory space complexity from $\mathcal{O}(nd^L)$ to $\mathcal{O}(n)$ ($n$: memory budget, $d$: average node degree, $L$: the radius of the GNN receptive field), but also fully utilizes the topological information for memory replay. Specifically, PDGNNs decouple trainable parameters from the computation ego-subgraph via Topology-aware Embeddings (TEs), which compress ego-subgraphs into compact vectors (i.e., TEs) to reduce the memory consumption. Based on this framework, we discover a unique \textit{pseudo-training effect} in continual learning on expanding graphs and this effect motivates us to develop a novel coverage maximization sampling strategy that can enhance the performance with a tight memory budget. Thorough empirical studies demonstrate that, by tackling the memory explosion problem and incorporating topological information into memory replay,  PDGNNs with TEM significantly outperform state-of-the-art techniques, especially in the challenging class-incremental setting.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a strategy for reducing the memory complexity from $O(nd^L)$ to $O(n)$ for continual learning (CL) on expanding
graphs. More specifically, the strategy removes the requirement of storing the entirety of ego-subgraphs which is normally needed for replay buffers. The framework, Parameter Decoupled Graph Neural Networks (PDGNNs) with Topology-aware
Embedding Memory (TEM), is competitive against several state-of-the-art baselines over various CL tasks. In addition to empirical evidence of efficacy, the authors contribute theory as well.

### Strengths
1. Addresses an important issue: memory complexity of GNN training is a major bottleneck. The proposed approach introduces a simple, yet effective technique for reducing the memory complexity while avoiding catastrophic forgetting.

2. The empirical evidence is strong. A wide variety of baselines are proposed and the authors' method uses significantly less memory in the replay buffer while outperforming most baselines across several tasks. Large datasets are also included to support the strategy.

### Weaknesses
1. The authors do not suggest a novel $f_{topo}$ (the embedding function) which limits the novelty of the work. Essentially, the authors are proposing to reduce the memory complexity of ego-subgraph topological information using known techniques. 

2. Some issues with theory: (a) I believe Definition 1 is both too strong and not rigorous enough, “if optimizing $\theta$ with $G_v^{sub}$ or $e_v$ are equivalent,” does this mean the same stationary points are achieved? Additionally, since $e_v$ is an embedding, this would be a highly unusual possibility as any type of compression leads to different solution spaces. (b) Theorem 1: “It is equivalent to training PDGNNs with each node w in $G_v^{sub}$ with $G_v^{sub}$ being a pseudo computation ego-subgraph and $y_v$ being a pseudo label,” in my opinion, this is a near circular outcome. You have defined the embedding as $e_v$ as being a representation of $G_v^{sub}$ such that optimization is equivalent, which is strong enough to allow all these results to naturally fall out. 

Minor:
Misformatted citations. Some examples: Section 2.2: misformatted citation Kipf & Welling (2016) 
Section 3.2: “prevent forgetting LopezPaz & Ranzato (2017); Rebuffi et al. (2017).” 

“Take the Reddit dataset (Hamilton et al., 2017) as a concrete example, its average degree is 492, and even with a 2 layer MPNN, the buffer size will be easily intractable.” This sentence was repeated in the intro.

### Questions
Please clarify my concerns regarding theory. In particular, the existence of a non-trivial topology-aware embedding as in Definition 1, as I think the definition refers to the existence of a very strong function.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new framework for continual learning of GNNs. Methods such as memory replay solve continuous learning issues such as catastrophic forgetting, but there are major problems from a memory perspective. The proposed method does not store all subgraphs, but instead stores vectors equivalent to key nodes in a topology-aware manner and utilizes them for training. This has been effective in reducing the amount of memory and the challenge of continuous learning.

### Strengths
A new framework that greatly improves the memory problem in continuous learning on expanding graphs and has high performance is proposed, and experiments have shown its effectiveness.

### Weaknesses
Basically, this paper is well written, but there is one thing that bothers me. This paper describes the avoidance of memory explosion as an issue, and specifically argues for a reduction from O(nd^L) to O(n). The reduction in memory order is almost trivial, and is also discussed in a simplified manner in the text. On the other hand, no experiments with actual memory perspectives have been conducted. Memory reduction may have contributed to the improved performance shown in the experiment, but not directly. For example, a comparison of the possible scale of response between ER-GNNs and PDGNNs should be mentioned in a clear manner.

### Questions
In addition to the WEAKNESS content, there are questions about the following:

I would like to know the impact of TEM sampler settings, I understand that coverage maximization sampling is recommended, but are there other sampling methods with catastrophic results? Does the sample size of coverage maximization sampling make a critical difference? If possible, experimental results would be useful for actual use.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a general framework, Parameter Decoupled Graph Neural Networks (PDGNNs) with Topology-aware
Embedding Memory (TEM) to tackle the memory explosion problem for continually expanding graphs.
The main contribution is the reduction of memory space complexity and improved model performance.

### Strengths
- The paper presents a good theoretical analysis of the PDGNN training
- The memory usage reduction of the proposed method is significant

### Weaknesses
 - The PDGNN and TEM definitions are vague. I hope the paper can include concrete algorithms to showcase how they are implemented. - - Overall, the formation of PDGNN looks overly complex to me. I hope the authors can showcase the true insights behind PDGNN, potentially via an ablation study, demonstrating which component really works.
- The experimental datasets are limited. First, it is not clear why Cora and OGB datasets are proper for the expanding graphs problem. I hope the authors can evaluate the methods on more practically useful expanding graph datasets.
- The main claim, memory cost reduction, is not validated. There is no memory analysis in the main paper. I found the discussions on the Appendix, but I think it should appear in the main paper and be more thoroughly discussed.
- Overall, the scope of the problem has limited value. There are not many practical use cases with this setting.

### Questions
It is confusing for readers to understand the relationships between PDGNN and TEM. What makes a PDGNN? Does it mean we combine any MPNN with TEM?

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a systematic analysis of the memory explosion problem in continual learning on expanding graphs and introduces the PDGNNs-TEM framework, which effectively reduces memory complexity while incorporating topological information for memory replay.
In scenarios where new nodes and edges are continually added to a graph, traditional models may experience catastrophic forgetting when adapting to new data while maintaining performance on old data. Memory replay techniques, successful in other domains, are applied to this problem, but they lead to a memory explosion issue due to the necessity of storing topological neighborhood structures.
To mitigate this problem, the PDGNNs-TEM framework reduces the memory space by decoupling trainable parameters from individual nodes/edges.

### Strengths
1.  The authors have provided a comprehensive and in-depth discussion of the relevant literature, encompassing various domains such as continual learning and graph neural networks.

2. The authors conduct comprehensive experiments on multiple datasets, evaluating their method against a range of baselines. The results show that PDGNNs-TEM outperforms existing techniques, achieving better average accuracy with less memory consumption.

### Weaknesses
1. A potential weak point of the paper is the perceived limitation in technical novelty. The paper could be interpreted as an application of decoupled GNNs to the continual learning domain, which has already been acknowledged for its computational efficiency benefits. However,  I believe that combining existing, well-established techniques that work efficiently is a valid approach in research. It's essential to leverage the best tools available to address complex problems effectively. In this case, applying decoupled GNNs to the continual learning context is a sensible choice, as it capitalizes on the advantages of both areas. However, it would be beneficial to describe clearly the paper's contribution, impact, and novel techniques.

2. Reproducibility and Open Access: It is not mentioned whether the authors plan to make their code, dataset, or pre-trained models available for the research community. This could be a weak point, as open access to these resources is essential for the reproducibility and widespread adoption of the proposed approach.

### Questions
See above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes to use topology-aware embedding to preserve the subgraph information in the buffer for the continual learning. the methods can reduce the memory usage for the memory replay. Experiments show that the approach is promising

### Strengths
1. the paper is well written and easy to follow
2. the experiments look good

### Weaknesses
From my understanding,  the Topology-aware Embedding Memory is to replace the dynamic message passing aggregation of the subgraph with the fixed representation, I have concern about the novelty.


### Questions
how does the subgraph size influence the quality of the topology-aware Embedding? and how to choose the subgraph size for computing?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

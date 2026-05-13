# HiGen: Hierarchical Graph Generative Networks

- Decision: Accept
- Scores: 8, 6, 6, 6, 6

## Abstract
Most real-world graphs exhibit a hierarchical structure, which is often overlooked by existing graph generation methods. To address this limitation, we propose a novel graph generative network that captures the hierarchical nature of graphs and successively generates the graph sub-structures in a coarse-to-fine fashion. 
At each level of hierarchy, this model generates communities in parallel, followed by the prediction of cross-edges between communities using separate neural networks. 
This modular approach enables scalable graph generation for large and complex graphs.  Moreover, we model the output distribution of edges in the hierarchical graph with a multinomial distribution and derive a recursive factorization for this distribution. This enables us to generate  community graphs with integer-valued edge weights in an autoregressive manner.
Empirical studies demonstrate the effectiveness and scalability of our proposed generative model, achieving state-of-the-art performance in terms of graph quality across various benchmark datasets.}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors mainly aim to propose a graph generative model that can capture hierarchical structures. To this end, the authors propose a coarse-to-fine manner method that generate the graph structures by modeling the distribution of connectivity as a recursive multinomial distribution and decomposing the graph generation process into the generation of communities and bipartites at each level. The proposed method is evaluated on the general graph generation task and 3D point cloud generation tasks.

### Strengths
* The proposed coarse-to-fine manner is an effective method to generate larger graphs as it can gradually recover the structure with the knowledge of the hierarchical clusters of the graphs.
* The performances of the proposed method are superior to the existing autoregressive and diffusion models.
* The authors provide an informative ablation study on the effect of the node ordering and the graph partitioning method.

### Weaknesses
 * The proposed method is effective in generating the graph structures. However, I am concerned that it requires an additional generator to generate the graph attributes for the realistic graph generation and it could be a harder problem to generate the graph attributes correctly only given the structures.
* To strengthen the contribution of the proposed method, it would be better to evaluate it on the molecular graphs.

### Questions
* How does the performance change depending on the partitioning algorithm?
* Could you elaborate why HiGen outperforms HiGen-m?

### Soundness
4 excellent

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors introduce Hierarchical Graph Generative Networks (HIGEN), a model designed to encapsulate the hierarchical characteristics of graphs through a progressive generation of graph sub-structures, transitioning from broader to more detailed aspects. At every hierarchical level, the model concurrently produces communities, subsequently generating bipartite graphs to represent cross-edges between these communities, utilizing distinct neural networks for each task. This compartmentalized strategy ensures that the graph generation process is both scalable and efficient, even when applied to large and intricate graphs. The method presented surpasses the performance of current leading techniques across a range of benchmark datasets.

### Strengths
1. HIGEN adeptly grasps the hierarchical nature of real-world graphs, facilitating the generation of sub-structures in a manner that is both scalable and efficient.

2. The authors conduct a comprehensive evaluation of the proposed method, utilizing a variety of benchmark datasets to showcase the method's capability in accurately generating graphs that reflect the statistical characteristics inherent to real-world graphs.

3. The manuscript offers an in-depth examination of the graphs produced by the HIGEN models, including a visual comparison of these generated graphs and a rigorous experimental assessment of diverse node ordering and partitioning functions.

4. The authors also present an analysis of computational complexity, alongside a comparison of sampling speeds, providing a holistic understanding of the method's performance and efficiency.

### Weaknesses
1. The proposed method assumes that the input graph is connected, which may not be the case for some real-world graphs.
2. Due to its hierarchical generation approach, particularly during the community generation phase, the proposed method might face challenges in maintaining control over the global distribution of the graph.

Minor Problem:
Typo: "Model Architecture n our experiments"

### Questions
Please refer to weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes HiGen, a novel graph generative network that captures the hierarchical nature of graphs and successively generates the graph sub-structures in a coarse-to-fine fashion. This method enables scalable graph generation for large and complex graphs, while generating community graphs with integer-valued edge weights in an autoregressive manner. Empirical studies demonstrate the effectiveness and scalability of the proposed method, achieving state-of- the-art performance in terms of graph quality across various benchmark datasets.

### Strengths
- The idea of generating real-world graphs hierarchically is novel and interesting.

- The resulting HiGen model can generate high-quality real-world graphs, with theoretical support on community generation.

- The experiments are convincing, showing that HiGen can outperform many graph generation models on a wide range of datasets.

### Weaknesses
 - The authors should include a complete analysis of complexity against previous methods, including the complexity of graph partitioning.

- Typo: Section 5, paragraph “Model Architecture”

### Questions
- See weakness above.
- Typo: Section 5, paragraph “Model Architecture”

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
The paper proposes a general hierarchical graph generation method, aiming to generate graph in a coarser-to-fine way. The proposed idea is quite reasonable for graph data. The proposed method learns the probability of connectivity of communities and the edges in each community conditioned on the graph of privious layer. Extensive results on several kinds of datasets well demonstrate the effectiveness of the proposed method that could generate graphs with desired properties.

### Strengths
1. The proposed method is novel, where the idea of generating graphs without prior knowledge has not been studied yet. And the idea is also reasonable for generating various kinds of real-world graphs.
2. The proposed method is sound.
3. The experiments validate the proposed method could generate a hierarchical graph structure.

### Weaknesses
1. The computation complexity of the proposed model is not clear. Specifically, the time and space complexity of both the training and generation phases should be analyzed in detail. It is unclear how the hierarchical structure affects the overall computational cost compared to flat graph generation models. For example, how does the number of layers and the number of nodes in each layer impact the runtime and memory usage? A breakdown of the complexity for each step of the algorithm would be beneficial.
2. Could the proposed method be applied to molecule generation and compared with HierVAE? (Jin et al. 2020) The current method focuses on generating graphs with community structures, but it's unclear how it would handle the specific constraints and properties of molecular graphs, such as atom types, bond types, and valency rules. A discussion on how the method could be adapted to handle attributed graphs and a comparison with existing methods like HierVAE would be necessary to assess its broader applicability.
3. How to identify the number of layers and the number of communities in each layer? The method currently assumes these parameters are predefined, but in real-world scenarios, these are often unknown. The paper should discuss methods for automatically determining the optimal number of layers and communities, perhaps by using a validation set or a heuristic based on the graph structure. The impact of these parameters on the quality of generated graphs should also be investigated.
4. The metric of novelty is also important for graph generation method. How about the novelty of the generated graphs by the proposed method? While the paper demonstrates the method's ability to generate graphs with desired structural properties, it does not address whether the generated graphs are novel or simply variations of the training data. A quantitative analysis of the novelty of the generated graphs is needed, using metrics such as the proportion of unique graphs or the distance to the nearest training graph.

### Questions
Please refer to the weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a new deep graph generative model, HiGen. HiGen generates a graph in a coarse-to-fine manner, wherein a small, "low-resolution" graph is generated, and at the next, higher-resolution level, each node at the prior level corresponds to the graph of a community of nodes, whereas each edge corresponds to a bipartite graph between two communities. The concept of this method promises greater scalability, parallelization, and graph quality than prior methods. Experiments on generating several classes of graphs, such as SBMs, proteins, enzymes, ego networks, and point clouds, indicate overall superiority of the quality of graphs produced by HiGen relative to some prior methods.

### Strengths
1) The introduction features an informative summary of recent work in graph generative deep networks. It positions the author's method well in the context of this prior work.
2) The topic of the paper, deep graph generation, is very popular in recent years.
3) The concept of the method is logical and promises better runtime than some prior methods. Experiments indicate better graph quality than prior methods as well.

### Weaknesses
1) There is limited theoretical advancement. The theorems in this work regard the correctness of an aspect of the graph generation (specifically, the correctness of a certain factorization of the multinomial distribution). The introduction alludes to challenges in graph generation like "difficulty capturing complex dependencies in graph structures," learning multi-scale structure, etc., but there is no theory addressing how well the proposed algorithm performs at this task relative to others. For example, while the factorization of the multinomial distribution is a necessary step, it does not, by itself, guarantee that the resulting generative model is capable of capturing the intricate structural properties of real-world graphs. The paper lacks theoretical analysis of the approximation error introduced by the hierarchical decomposition, or how the choice of the base-level graph affects the quality of the generated graphs at higher levels. There is no discussion of the limitations of the multinomial distribution in capturing complex edge dependencies, nor is there any analysis of the convergence properties of the training process.
2) Training / sampling from HiGen could be broken out into algorithms in the text for clearer presentation. At present, reviewing what the algorithms are requires going through several pages of text.

Typos:
- page 1: Jin et al. unparenthesized
- page 2: proposed *a* generative model
- page 7: Kong et al. unparenthesized
- page 7: "an analytically solution"
- page 7: "n our experiments,"
- page 8: "However, It’s important"

### Questions
1) As stated above, I suggest breaking out the training/sampling into algorithms to improve readability.

2) There is an abundance of papers proposing new deep graph generative models in recent years, as outlined in this paper's introduction, and these papers generally claim superior graph quality to prior methods. However, there are many degrees of freedom in measuring the quality of graph generation, so it is hard to tell whether there is real progress. With this in mind, how would the authors argue that there is a real advancement in the graph quality of HiGen? As I mentioned above, a theoretical framework is one possibility, but this paper goes in a more empirical direction.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

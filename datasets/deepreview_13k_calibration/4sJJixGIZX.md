# Online Continual Graph Learning

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 5, 3

## Abstract
The aim of Continual Learning (CL) is to learn new tasks incrementally while avoiding catastrophic forgetting. Online Continual Learning (OCL) specifically focuses on learning efficiently from a continuous stream of data with shifting distribution. While recent studies explore Continual Learning on graphs exploiting Graph Neural Networks (GNNs), only few of them focus on a streaming setting.  Many real-world graphs evolve over time and timely (online) predictions could be required. However, current approaches are not well aligned with the standard OCL literature, partly due to the lack of a clear definition of online continual learning on graphs. In this work, we propose a general formulation for online continual learning on graphs, emphasizing the efficiency of batch processing while accounting for graph topology, providing a grounded setting to analyze different methods. We present a set of benchmark datasets for online continual graph learning, together with the results of several methods in CL literature, adapted to our setting. Additionally, we address the challenge of GNN memory usage, as considering multiple hops of neighborhood aggregation can require access to the entire growing graph, resulting in prohibitive costs for the setting. We thus propose solutions to maintain bounded complexity for efficient online learning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a novel framework, OCGL, which addresses the challenges of applying continual learning principles to graph-structured data in an online setting. It innovatively formulates the problem of learning from a continuously evolving graph, emphasizing the necessity to manage computational complexity and avoid catastrophic forgetting—a common issue where a model loses previously learned information upon learning new data. To facilitate research in this area, the authors develop a benchmarking environment with tailored datasets to evaluate various continual learning methods adapted to graph settings. They also propose practical solutions such as neighborhood sampling to maintain computational efficiency as the graph grows.

### Strengths
1. One of the paper's main strengths is the formal introduction of the Online Continual Graph Learning (OCGL) framework.
2. The authors develop a benchmarking environment specifically for OCGL, including multiple datasets and evaluations of various continual learning methods. 
3. The experimental setup and the detailed analysis provided in the paper are thorough and well-constructed.

### Weaknesses
1. The proposed problem is novel, however, the detailed appliable scenario for such OCGL framework should be further explained, especially on graph data. Specifically, while the paper mentions the need for quick model adaptation, it does not provide concrete examples of real-world graph-based applications where such online continual learning is crucial. For instance, in social network analysis, how would this framework handle the continuous addition of new users and interactions, and what specific benefits would it offer over existing methods? The lack of such detailed scenarios makes it difficult to assess the practical relevance of the proposed framework.
2. The baselines chosen in this paper are all Continual learning methods. More methods for the online learning setting should be included. The paper should consider including online learning methods that do not explicitly focus on catastrophic forgetting, as these might be more suitable for the online setting. For example, methods that emphasize efficient adaptation to new data streams, even if they do not explicitly address forgetting, could provide a more comprehensive comparison.
3. Also, as a benchmark paper, it would be beneficial to introduce more new datasets. While the current datasets are well-established, they may not fully capture the complexities of real-world online graph learning scenarios. Introducing datasets with varying characteristics, such as different graph sizes, densities, and node/edge feature distributions, would make the benchmark more robust and applicable to a wider range of problems.
4. The contribution of this paper seems limited to me. The authors introduced a new problem setting OCGL for graph learning and presented a benchmarking environment for OCGL, but did not propose a novel method to solve this problem. Although I understand benchmarking papers are also important to the research community, I believe that the contribution in this case may not be significantly sufficient for inclusion in this conference. The paper's contribution is primarily in defining the problem and providing a benchmark, but it lacks a novel algorithmic contribution. The absence of a new method to address the challenges of OCGL limits the impact of the work, especially for a conference that typically values algorithmic innovation.
5. The third contribution, using random sampling to address the complexity of multi-hop aggregation, is a very easy-to-get idea, and seems trivial to me. The use of random sampling, while practical, is a very basic approach and does not offer any significant novelty. More sophisticated sampling techniques, such as importance sampling or adaptive sampling, could have been explored to address the computational challenges of multi-hop aggregation more effectively.

### Questions
see above.

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
This paper aims to formulate the setting of online continual graph learning considering the efficiency of batch processing and graph topology, and proposes a set of benchmark datasets for online continual graph learning. Additionally, from the technical perspective, the authors address the challenge of GNN memory usage.  

Within the context of online continual graph learning, the graphs are defined as a time series, in which the graph snapshot at each time stamp t contains the nodes and edges collected from the starting time till t. Each new snapshot is created when a new node is added. The newly attached information includes the new node, its neighbors, and the node features.

### Strengths
1. Online continual graph learning has not been fully explored, and this work makes some contribution in this direction. 

2. Compared to existing continual graph learning works, this work adopts a more practical hyperparameter selection strategy that only use a few tasks.

### Weaknesses
1. The main weakness is the inconsistence between the proposed setting and the actual experiments. Although the paper described an online learning setting, but the task construction in experiments is still same as the continual graph learning setting with task boundaries. As mentioned in the paper, 'the graph grow with nodes from two new classes at a time', then the incremental manner is same as a normal class incremental learning instead of an online learning setting. I would recommend that the experiments should be consistent with the proposed setting,in which each new snapshot could contain one node or a mini-batch of new nodes, but not necessarily a new task containing new classes.

2. The adopted baselines are a little bit out of date. Besides, only TWP is specially designed for graph data, while the others don't consider the graph structures. Admittedly the authors have discussed why some baselines are not adopted, but the mentioned ones are all proposed no later than 2021. Therefore, it is not convincing enough that the adopted methods can represent the state-of-the-art performance. I would recommend that the recent continual graph learning works proposed from 2022 to 2024 could be thoroughly investigated, discussed, and compared whenever appropriate.

### Questions
1. In the Mini-batching part of Section 3.1, what does it mean by 'L>1 is not in contrast with the growing mechanism of the graph'? I could understand what the authors want to express should be that the entire graph may be required for aggregating multi-hop information, but the writing here seems confusing.

2. It is a little bit confusing whether the proposed strategy allows the model to access the entire graph that contains previous nodes. It is stated that the up-to-date graph Gt is stored in a Past Information Store (PIS) system, but only allow limited use of information from PIS. It is unclear what kind of usage is deemed as 'limited'. Additionally, it is also stated that the PIS is different from a 'eventual memory buffer'. This is also confusing. If the PIS contains the completely graph with all previous information, then what is the role of the 'eventual memory buffer', and why we still need such a buffer?

3. In the 'training details' part in the experiment section, when talking about the batch size, how is each batch used? Given a new task with N data, will the model be trained on the N data for several epochs, and in each epoch, the batches are fed into the model sequentially?

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
4

### Summary
The paper introduces the Online Continual Graph Learning (OCGL) framework to handle non-stationary streaming data in graph structures. It benchmarks several continual learning methods on four datasets, adapting them for the online graph learning scenario. The authors propose a neighborhood sampling strategy to address the issue of neighborhood expansion in Graph Neural Networks (GNNs) and reduce computational complexity.

### Strengths
1. The introduction of the Online Continual Graph Learning (OCGL) framework extends continual learning to dynamic, graph-structured data.

2. The paper provides a thorough evaluation of multiple continual learning methods, adapting them for online graph learning.

3. The proposed neighborhood sampling strategy effectively addresses the computational and memory challenges of multi-hop neighborhood aggregation in GNNs.

### Weaknesses
1. The benchmarks focus mainly on node classification tasks, and extending the framework to more diverse graph-based applications (e.g., edge prediction, link prediction) could strengthen the paper's contributions.

2. The paper primarily compares traditional continual learning methods adapted for the Online Continual Graph Learning (OCGL) framework. It does not include comparisons with more recent state-of-the-art continual graph learning methods proposed in the recent three years, such as MSCGL[1] and UGCL[2].

    [1] J. Cai, X. Wang, C. Guan, Y. Tang, J. Xu, B. Zhong, and W. Zhu, ''Multimodal continual graph learning with neural architecture search,'' in Proceedings of the ACM Web Conference, 2022, pp.1292–1300.

    [2] T. D. Hoang, D. V. Tung, D.-H. Nguyen, B.-S. Nguyen, H. H.Nguyen, and H. Le, ''Universal graph continual learning,'' Transactions on Machine Learning Research, 2023.

3. While the sampling strategy improves computational efficiency, it can negatively impact model accuracy. 

4. The paper predominantly concentrates on experimental evaluation and lacks an in-depth theoretical analysis of the proposed method's properties, such as convergence, computational complexity, and theoretical bounds on forgetting.

### Questions
See weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces an Online Continual Graph Learning (OCGL) framework designed for learning in dynamic graph environments where data arrives in a streaming fashion. The authors address challenges of catastrophic forgetting in graph-based continual learning, particularly when working with graph neural networks (GNNs) that rely on neighborhood information, which can lead to high memory and computational costs. The proposed OCGL framework is evaluated on four node classification datasets, using modified continual learning methods suited for online learning. They propose neighborhood sampling as a strategy to address neighborhood expansion challenges, which could otherwise lead to prohibitive costs in dynamic graph settings.

### Strengths
- the studied problem is an important research question

- I like the attempts that the author tried to take a more systematic approach toward the problem

### Weaknesses
1. the technical content of the paper does not address the research question proposed by the authors. For example
    a. one of the claimed distributions is the formulation of the so-called online GCL. However, I do not see any formal formulation of the problem. Only a generic description is provided. For example, to fulfil the claim, one would naturally expect to see the data model, the definition and format of the leaner, and the properties and requirements for an effective learner in this scenario. None of these information is provided.
   b. another claim is that online GCL is a new learning paradigm and different from GCL. One would expect to see a detailed comparison between these two. How are they different exactly? How much is the difference?

2. there are some statements that are not factually correct. For example, continual learning is inherently an online setting. An ideal continual learning algorithm should adaptively learn from the new data without the need to access previous data. However, this can be proved theoretically impossible. Therefore, many continual learning algorithms compromise by allowing partial access to historical data. Even for online systems, storing historical data is also allowed. Regarding the task boundary, there have been many studies that looked at the continual learning setting without a clear task boundary. These studies have been under the terms such as "task-free continual learning" and "domain-free continual learning"[1]. Furthermore, it is not clear what exactly task-boundary means in the paper.

3. the proposed technique is standard and the paper has no conceivable novelty or contribution. The neighbourhood explosion problem is a standard issue in GNN training even for the case of training GNN on static graphs and neighborhood sampling has been de-facto in training GNN. The issue of changing graph structure in GCL has been documented and studied in [2].

### Questions
see weakness

### Soundness
2

### Presentation
2

### Contribution
1

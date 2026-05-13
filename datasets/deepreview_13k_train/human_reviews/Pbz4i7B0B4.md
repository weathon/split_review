# Towards Continuous Reuse of Graph Models via Holistic Memory Diversification

- Decision: Accept
- Scores: 6, 5, 6, 6

## Abstract
This paper addresses the challenge of incremental learning in growing graphs with increasingly complex tasks. The goal is to continually train a graph model to handle new tasks while retaining its inference ability on previous tasks. Existing methods usually neglect the importance of memory diversity, limiting in effectively selecting high-quality memory from previous tasks and remembering broad previous knowledge within the scarce memory on graphs. To address that, we introduce a novel holistic Diversified Memory Selection and Generation (DMSG) framework for incremental learning in graphs, which first introduces a buffer selection strategy that considers both intra-class and inter-class diversities, employing an efficient greedy algorithm for sampling representative training nodes from graphs into memory buffers after learning each new task. Then, to adequately rememorize the knowledge preserved in the memory buffer when learning new tasks, we propose a diversified memory generation replay method. This method first utilizes a variational layer to generate the distribution of buffer node embeddings and sample synthesized ones for replaying. Furthermore, an adversarial variational embedding learning method and a reconstruction-based decoder are proposed to maintain the integrity and consolidate the generalization of the synthesized node embeddings, respectively. Finally, we evaluate our model on node classification tasks involving increasing class numbers. Extensive experimental results on publicly accessible datasets demonstrate the superiority of DMSG over state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the problem of incremental learning in growing graphs with new-coming node classes. It introduces a novel holistic Diversified Memory Selection and Generation (DMSG) framework containing two modules: (1) a buffer selection strategy that considers both intra-class and inter-class diversities, with a greedy algorithm; and (2) a diversified memory generation replay method with variational generation, with integrity loss and reconstructed loss under adversarial learning. Experiments over evolving graphs on node classification tasks could verify its effectiveness, along with ablation study over memory generation replay module.

### Strengths
S1. [Clear Motivation & Descriptions] The paper provides a well-defined motivation for addressing continual learning on growing graphs, focusing on memory selection and memory reply effectiveness. The reason for developing the proposed method can be compelling, along with clear and detailed descriptions of the problem background and definition, making it accessible and understandable.

S2: [Rationale Methodology] The rationale for the DMSG approach is well-grounded, combining heuristic buffer selection and generative memory reply to broaden the replay capability. The methodology introduces two strategies: first, a buffer selection algorithm that maximizes intra-class and inter-class diversity; second, a variational generation layer that synthesizes embeddings for effective replay, which sounds rational and novel to me.

S3. [Theoretical and Empirical Experiments] The paper validates its approach with both theoretical and empirical support, for instance, theoretical analysis to demonstrate the importance of effective buffer selection. Experimentally, the DMSG framework is tested on multiple evolving graph datasets, a good improvement over the AF/% metric.

### Weaknesses
Here are still some questions mainly regarding the buffer selection part and the variational part:

W1: For the buffer node selection part, are the buffer nodes only node-set or graph-structural data, if graph data, how to connect these nodes? and if node-set, how to directly feed it into GNN in Figure 2?  Further clarification on this would be appreciated.

W2: How many nodes are typically selected in the buffer for each class? How experimental results would change along with the varying number of nodes in buffers?

W3: In the ablation study, the effectiveness of the buffer node selection is not verified. For instance, how to illustrate the effectiveness of the proposed heuristic greedy method?

W4: Why the variational layer in the memory replays could broaden knowledge from the buffer? Does that mean, it generates something new $\hat{Z}$ from the original Z? Additionally, the minimization term in equation (7) is difficult to interpret—could you provide a more detailed explanation or expanded expressions for this term?

W5: With the introduction of complex mechanisms for memory selection and replay, how do the time and computational costs of the proposed method compare to other baseline approaches in the experiments?

W6: Why have a direct assumption that "Let the loss function L(θ, x) be β-Lipschitz continuous in respect to the input x" in Theorem 1. ? And how can we evaluate whether the selected nodes in buffers are with diversity?

### Questions
See Weakness.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a novel approach called Diversified Memory Selection and Generation (DMSG) for incremental learning in growing graphs. The authors address the challenge of continually training graph models to handle new tasks while retaining knowledge from previous tasks.

### Strengths
The developed model is supported by a theoretical foundation. The authors provide a theoretical analysis to support the importance of buffer diversity in incremental learning scenarios.

The studied problem is important. The authors try to tackle the issues of limited buffer size and potential overfitting through their diversified memory generation approach.

clear visualization and presentation. The authors use well-structured figures to convey the incremental learning process, memory selection, and generative replay methods in a relatively straightforward approach.

### Weaknesses
Lack of novelty. This paper largely builds on existing concepts of memory replay and buffer selection strategies that are already well-established in incremental learning and continual learning literature. While the paper proposes a diversified memory selection and generative replay approach, the techniques, such as adversarial learning and variational embedding, have been previously applied in other contexts. The paper simply combines different losses to facilitate learning.

Lack of baselines. The following papers should be discussed and compared for experiments:
Towards robust graph incremental learning on evolving graphs. ICML 2023
Replay-and-Forget-Free Graph Class-Incremental Learning: A Task Profiling and Prompting Approach. NeurIPS 2024
On the Limitation and Experience Replay for GNNs in Continual Learning. CoLLAs 2024
Topology-aware Embedding Memory for Continual Learning on Expanding Networks. KDD 2024
PUMA: Efficient Continual Graph Learning for Node Classification With Graph Condensation. TKDE 2024
Graph Continual Learning with Debiased Lossless Memory Replay. ECAI 2024
Accordingly, it is encouraged that the authors discuss the difference between their proposed model and these baselines.

Lack of comprehensive datasets. What about the performance of the proposed model on Citeseer, Pubmed, and PPI? How about Collab, IMDB, Proteins, and NCI1?

Lack of hyperparameter sensitivity study. The method introduces several hyperparameters such as λ1, λ2, and λ3 for balancing the loss. A discussion on their impact and guidelines for tuning these hyperparameters would be valuable. More in-depth analyses about balancing these losses to understand the contribution and reasons for developing them are encouraged.

### Questions
see above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies incremental learning on growing graphs, aiming to continually train a model on new tasks without loosing the inference ability on previous tasks. The method proposed in this work, namely holistic diversified memory selection and generation (DMSG), is a memory based technique, with a focus on improving the data diversity in the memory, which is neglected by the existing works. The unique design of DMSG comes from two perspectives. First, it proposes a novel method to sample the data, second, instead of directly using the buffered data, DMSG train a generator to generate the data to replay.

Overall, this method proposes a novel memory based technique, and the experimental results justify the effectiveness of the method. However, there are also some major problems regarding the theoretical analysis, as listed below in the weakness part.

### Strengths
1. The paper is overall well written, and the main idea is clearly conveyed.

2. Experiments are comprehensively conducted on multiple benchmark datasets against multiple baselines.

3. According to the results, the proposed method consistently outperform the baselines, although the improvement on some datasets are negligible.

### Weaknesses
1. The theoretical analysis is not rigorous enough. Theorem 1 reveals that smaller distance between the memory data distribution and the full data distribution indicates that the loss computed based on memory can more closely mirrors the expected over the full previous data. This is a straightforward and reasonable conclusion. But what follows is not convincing enough. First, it is assumed that the distributions of the memory data and full data is Gaussian. I guess this is acceptable, although a little bit arbitrary. Next, it is stated that the buffered data is typically less diverse, therefore increasing its diversity could make it closer to the full data distribution. This is not convincing, since the 'diversity' here refers to the covariance. Why is the buffered data has a smaller variance than the real (full) distribution? This should depends on the sampling strategy instead of the size of the set. Moreover, although the diversity here refers to the covariance, in the following of the paper, the diversity is measured by the average distance among the data, which is inconsistent.

2. The implemented diversity maximization strategy is inconsistent with the theoretical motivation, as mentioned in the first weakness point.

### Questions
1. Please explain more on the probability distance used in Section 3.1, e.g. the specific formulation.

2. Is the replay data generator trained from scratch each time when a new task comes in? Or is the generator train each time when a new task comes in, but is initialized from the generator from the previous task?

3. If the generator is trained every time when a new task comes in, will this induce significant extra computational burden?

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
5

### Summary
This paper presents a memory replay approach to address the challenges of graph incremental learning. Specifically, the proposed method includes a diversified buffer selection module and a generative memory replay module to prevent the model from forgetting previous tasks when learning new tasks. The experimental results demonstrate the effectiveness of the proposed method.

### Strengths
The studied problem is practical and interesting.

The paper is well-written and easy to understand.

The proposed method introduces novel approaches for buffer selection and memory utilization.

### Weaknesses
1. The title presented on the website is not the same as the one in the paper
2. The citation style is not used appropriately. Most of the citations should be in parenthesis using \citep{}.
3. The authors are encouraged to include the time consumption of different memory selection strategies.
4. The statements in lines 178-181 are not clear. Please revise it to make it clearer.
5. The definition of L_{adv} is not clear in line 334. Moreover, there is no Eq.A.3.
6. The analysis of parameter sensitivity is missing.
7. The comparisons to more recent baselines are encouraged.

### Questions
Please see the weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

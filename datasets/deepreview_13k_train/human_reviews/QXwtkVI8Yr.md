# Swift-FedGNN: Federated Graph Learning with Low Communication and Sample Complexities

- Decision: Reject
- Scores: 5, 5, 6, 3

## Abstract
Graph neural networks (GNNs) have achieved great success in a wide variety of graph-based learning applications.
To expedite training for large-scale graphs,
distributed GNN training has been proposed using sampling-based mini-batch training.
However, such a traditional distributed GNN training approach is not applicable to emerging GNN learning applications with geo-distributed input graphs, which require the data to be kept within the site where it is generated to protect privacy.
On the other hand, federated learning (FL) has been widely used to enable privacy-preserving training under data parallelism.
However, because of cross-client links in the aforementioned geo-distributed graph data, applying federated learning directly to GNNs incurs expensive cross-client neighbor sampling and communication costs due to the large graph size and the dependencies between nodes among different clients. 
To overcome these challenges, we propose a new mini-batch and sampling-based federated GNN algorithmic framework called Swift-FedGNN that primarily performs efficient parallel local training and periodically conducts time-consuming cross-client training.
Specifically, in Swift-FedGNN, each client *primarily* trains a local GNN model using only its local graph data, and some randomly sampled clients *periodically* learn the local GNN models based on their local graph data and the dependent nodes across clients.
We theoretically establish the convergence performance of Swift-FedGNN and show that it enjoys a convergence rate of $\mathcal{O}\left( T^{-1/2} \right)$, matching the state-of-the-art (SOTA) rate of sampling-based GNN methods, despite operating in the challenging FL setting.
Extensive experiments on real-world datasets show that Swift-FedGNN significantly outperforms the SOTA federated GNN approaches with comparable accuracy in terms of efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes Swift-FedGNN. It aims to reduce the communication and sampling cost in federated graph learning. The framework is based on mini-batch training of GNNs. Clients in Swift-FedGNN do local training in most of time and periodically conduct cross-client training. The authors provide convergence theory of Swift-FedGNN.

### Strengths
S1: Writing is good.

S2: Related works are comprehensive.

S3: The results about the relationship between approximation errors and structure of GNNs are somewhat insightful.

### Weaknesses
W1: This paper claims to reduce the sampling and communication overhead, but comparison between Swift-FedGNN and most recent framework, e.g., FedGCN and FedSage+, is missing. It looks like FedGCN should has lower communication cost? The paper needs to clarify the specific communication costs of FedGCN, considering that it performs a one-time communication of the entire neighborhood. A detailed comparison of communication costs under different graph sizes and client numbers is necessary to justify the proposed method's advantage. The current analysis lacks a quantitative comparison with FedGCN, especially regarding the overhead of homomorphic encryption, which significantly impacts communication costs.

W2: The contribution seems a bit limited. Swift-FedGNN looks like a combination of FedGCN and [1]. I am not very sure about the novelty, I will check other reviewers’ comments. The paper needs to clearly articulate the novelty beyond combining existing techniques. The specific differences in the training process, such as the client selection strategy and the two-stage aggregation, need to be highlighted. The paper should also provide a more detailed analysis of how these differences lead to reduced communication costs and improved privacy compared to existing methods.

W3: The authors remove Homomorphic Encryption in FedGCN, and claim “send only the aggregated results…help 
preserve data privacy”. But according to FedGCN, the Homomorphic Encryption seems necessary for security. The paper needs to provide a more rigorous argument for the privacy claims without homomorphic encryption. Simply sending aggregated results might not be sufficient to prevent information leakage, especially if the aggregation process is not carefully designed. A more detailed analysis of the privacy risks and how the proposed method mitigates them is needed. The paper should also discuss the trade-offs between privacy and communication costs in more detail.

Minor issues: In line 104 to 109, it seems like a statement is repeated twice?

### Questions
Q1: In abstract and introduction, the authors motivate the federated graph learning with geo-distributed input graphs. But in experiments, graph partition is used for create multiple subgraphs. Is that a common practice? How do we know the subgraphs are distributed according to geo-information?

Q2: In line 182, the authors state “Note that this one-time communication only works for full graph training and is not suitable for the situations in  which clients sample different mini-batches of training nodes in each iteration since the cross-client neighbors of these training batches are different. ” I am not fully understand this, why the cross-client neighbors of these training batches are different? Can’t we just sample a training batch and acquire the aggregated representation of all their cross-neighbors?

### Soundness
2

### Presentation
2

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
This paper focuses on federated graph neural network training. Specifically, the clients share the same set of GNN model parameters, and each client holds a subgraph of the graph dataset (with partial non-overlapping nodes). The proposed algorithm aims to overcome the heavy communication burden in subgraph sampling for GNN training through 1) periodical inter-client training and multiple steps of local training and 2) client sampling for inter-client training. The authors provided a theoretical convergence analysis of the proposed algorithm with $O(1/\sqrt{T})$ rate. Experiments on the OGBN and Reddit datasets show that the proposed algorithm outperforms existing FL GNN algorithms under the same settings.

### Strengths
1. Originality: This paper provides a novel algorithm for (vertical) Federated Learning on Graph data. The algorithm analysis is also novel compared with existing FL and GNN algorithms.
2. Clarity: The paper is clearly written with rigorous definitions of the notations and assumptions, problem statements, algorithm descriptions, and experiment settings.

### Weaknesses
1. Missing ablation study: The numerical results cannot fully support its theoretical outcomes. The authors failed to conduct sufficient ablation study, including:
    1. The effect of $K, I$ on the final accuracy since they affect the residual error.
    2. Estimating the values of $B^f, B^l, B^r$ on how they changes with $L,B$'s in the assumptions.
    3. The experiments on models other than GraphSAGE, e.g., on GCN and GAT.
    4. Experiments on more datasets, e.g., other OGBN datasets, are also desirable.
2. Inaccurate theoretical statement:
    1. The claim of $O(1/\sqrt{T})$ convergence is inaccurate since Thm. 5.6 indicates that the algorithm only converges to a neighborhood of the exact solution.
    2. Further discussion on the convergence result compared with existing algorithms is missing. Specifically, how the residual error compares with SOTA algorithms, e.g., Chen et al., 2018; Cong et al., 2021; Ramezani et al., 2022; and Du & Wu, 2022.
    3. The remark (3) in lines 448-449 is not proved. Please refer to the place where this remark is proven.
3. Missing privacy analysis & statement
    The author claimed that aggregating the node embedding of layer $L$ is more private than communicating the node features. The authors should provide a more rigorous discussion on this claim, e.g., what privacy is protected (node feature? edge?) and how they link to real applications such as hospitals; how much "more" privacy is protected with the proposed algorithm?

### Questions
See the weaknesses above.

Specifically, please address weaknesses 1.1, 1.3, 2.2, 2.3

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
3

### Summary
1. The paper proposes a technique for federated learning in graph neural networks.
2. Thorough mathematical analysis shows that using this method reduces memory overhead.
3. Starting from mild assumptions the authors provide competitive convergence rate guarantees.
4. Some empirical evidence is presented to support theoretical results.

### Strengths
1. The theoretical derivations have clear assumptions that do not seem excessive. Bounded gradients (Lipschitz) is a mild assumption in general. Though the paper plus appendix are long and quote-dense (30 pages total) I believe that the theoretical derivations are correct and the claims are validated. Disclaimer: I read the proofs until page 23, Lemma D.5. All seemed correct. Glancing at the rest due to limited time for the review I believe that they are correct though I have not checked the details for the last 8 pages of the appendix.

2. The method does what it claims: it provides a new communication and sample-efficient mini-batch algorithm for Federated learning. It appears to outperform comparable SOTA approaches in terms of convergence.

3. Convincing experimental results. Though it is only tested on two datasets the algorithm is appears to have a clear edge, e.g., in Figure 4.

### Weaknesses
1. While the theoretical grounding is excellent, the experiments seem a little too narrow. The use of only 2 benchmarks raises doubts as to if the relative improvement to baselines is generalizable beyond the selected datasets. Can the authors explain the choice of datasets? Why not use other datasets that are in baselines such as Flickr, OGB-Products, OGB-Arxiv?.I suggest including these datasets for experiments.

2. We do not have hard metrics. How do the different methods perform at the end of training in the test set? Just because the validation loss converges faster in Fig. 4 does not mean that the test metric at the end of training will be better. Please provide a table comparing final test set performance across methods using standard metrics like accuracy, ROC-AUC, and F1 score

3. The paper is quite dense, I recommend rewriting parts of the introduction, contributions, and review to shorten them or to move part of that text to the appendix to make the text less dense. Some figures are hard to read, Figures 4,5,6 require zooming to 200% or more to be able to read clearly and this disrupts the flow of the paper.

### Questions
See questions in weaknesses. Additional questions:

1. Reported memory usage in Table 1 of LLCG (https://openreview.net/pdf?id=FndDxSz3LxQ) reports different Megabytes of node representation/feature communicated per round in Reddit than Table 2 of your paper. Why is that? Is there a way to make sure there is an apples to apples comparison here?.

2. It seems a little troubling that the baselines are 2-3 years old. Are there really no newer methods to compare to? It seems a little concerning if research interest in this setup is not very high from an impact perspective. Can the authors alleviate my concerns here? If not, please add and compare with recent state-of-the-art to strengthen the paper.

I will raise it to 6 if they can answer my questions about datasets and why so few baselines as to how it justifies motivation.

### Soundness
3

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
The paper presents Swift-FedGNN, a federated learning framework for graph neural networks that reduces sampling and communication overhead. It achieves this by focusing on local training with periodic cross-client updates to handle geo-distributed data while preserving privacy. Key contributions include efficient federated GNN training with minimal cross-client communication and a convergence rate that matches state-of-the-art methods.

### Strengths
1. The paper clearly explains the methodologies.
2. Swift-FedGNN achieves strong convergence rates comparable to state-of-the-art methods.

### Weaknesses
1. In Section 4, the basis for neighbor sampling is unclear. How are nodes chosen, and how is it confirmed that they are true neighbors? Additionally, it’s uncertain how cross-client neighbors are verified between clients. Are there any specific assumptions regarding this?
2. The novelty primarily lies in local training with periodic cross-client updates, which may limit the contributions, as periodic updates are not a particularly novel technical innovation.
3. Comparing Swift-FedGNN with more recent baselines, as well as classic methods like FedAvg, FedSage, etc., would strengthen the study.
4. What is the primary factor contributing to Swift-FedGNN’s fast convergence rate? In Figure 4, the x-axis shows Wall-Clock Time. Would Swift-FedGNN still converge the fastest if the x-axis were set to iterations? I recommend including an additional plot of convergence vs. iterations, along with a more detailed analysis of the factors contributing to fast wall-clock time convergence.

### Questions
Please see and address my concerns on the weaknesses above.

### Soundness
2

### Presentation
3

### Contribution
2

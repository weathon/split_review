# Scaling Probabilistic Circuits via Data Partitioning

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 8, 6, 3

## Abstract
Probabilistic circuits (PCs) enable us to learn joint distributions over a set of random variables and to perform various probabilistic queries in a tractable fashion. Though the tractability property allows PCs to scale beyond non-tractable models such as Bayesian Networks, scaling training and inference of PCs to larger, real-world datasets remains challenging. To remedy the situation, we show how PCs can be learned across multiple machines by recursively partitioning a distributed dataset, thereby unveiling a deep connection between PCs and federated learning (FL). This leads to federated circuits (FCs)---a novel and flexible federated learning (FL) framework that (1) allows one to scale PCs on distributed learning environments (2) train PCs faster and (3) unifies for the first time horizontal, vertical, and hybrid FL in one framework by re-framing FL as a density estimation problem over distributed datasets. We demonstrate FC's capability to scale PCs on various large-scale datasets. Also, we show FC's versatility in handling horizontal, vertical, and hybrid FL within a unified framework on multiple classification tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The author propose a federated learning framework for probabilistic circuits learning. FCs unify horizontal, vertical, and hybrid federated learning by partitioning data and models across multiple machines, enabling efficient training and inference on large datasets.

### Strengths
1. The paper introduces federated learning framework to probabilistic circuits and use it for scaling up model training.

### Weaknesses
1. The evaluation in Table 2 is unclear. Since Gaussian distributions are used as PC leaves, it is not specified whether the reported values represent log-likelihoods or log-densities. If they are log-densities, they cannot be directly compared to benchmark log-likelihoods. To ensure a fair comparison, the values should be adjusted for discretization by converting log-densities into log-likelihoods. Specifically, when evaluating a continuous density model on discrete data (such as images with pixel values), it is crucial to integrate the probability density function over the pixel's quantization bin to obtain a proper probability mass function, which can then be used to calculate the log-likelihood. Simply using the density value at the discrete pixel value is incorrect and leads to an apples-to-oranges comparison with methods that report log-likelihoods.

2. The contribution is limited. Similar data partitioning methods were introduced in [1], and the idea presented in this paper is to assign different partitions to different machines/clients/nodes in order to scale up. However, the author does not clarify the distinction between the proposed method and that in [1]. The paper needs to clearly articulate how the proposed federated approach differs fundamentally from the data partitioning strategy in [1], beyond simply distributing the partitions across different machines. The core novelty of the method needs to be more clearly defined and justified.

3. The writing is redundant and notations are unnecessarily heavy. For instance, the federated circuits in Section 3.2 simply rephrase probabilistic circuits, but with the circuit nodes distributed across different clients. The introduction of federated circuits as a separate concept seems to add unnecessary complexity without providing substantial new insights. The paper should streamline the notation and focus on clearly articulating the core contributions.

### Questions
See in [Weaknesses]
1. What is the inherent difference between your method and [1]
2. How do you evaluate performance in Table 2.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a PC-based approach for performing horizontal, vertical, and hybrid FL. To achieve this, each component of a partitioned data set is assigned to a leaf of a learned SPN. For those leaves sharing a common feature set, a sum node is introduced to aggregate the local distributions. Otherwise, a product node is utilized to combine distributions over disjointly featured random variables. 

Overall, the paper is clearly written, and the proposed method (FedPCs) seems to be quite effective in both density estimation and classification tasks. Also, to the best of my knowledge, this is the first work simultaneously addressing horizontal, vertical, and hybrid FL in a single framework. 

However, please keep in mind that I am mostly unfamiliar with the literature on probabilistic circuits. I look forward to engaging with the authors during the discussion period to potentially increase my score.

### Strengths
1. The proposed method is precisely described. Also, authors provide computer code for reproducing their experiments. 

2. Assumptions are clearly stated, and the work’s novelty is well-established. Limitations are also partially addressed. 

3. The demonstrated relationship between PCs and FL is insightful and may foster interesting future works in the field.
 
4. FedPCs lead to drastically faster learning while achieving comparable performance to a centralized approach. 

5. A rough analysis of the method’s communication cost is provided.

### Weaknesses
1. Is Figure 1 correct? If I understood Section 3.3 correctly, a sum node is attached for each feature (subspace) shared by more than one client (lines 262-264). However, the equally featured partitions $\mathcal{P}_{1}$ and $\mathcal{P}_{2}$ are joined by a *product node* in Figure 1. I believe an illustration of Algorithm 1 would greatly improve the readability of Section 3.3. 

2. It is trivial fact that conditional independence does not imply (marginal) independence, e.g., if $X_{i} = Y + \epsilon_{i}$ for some random variable $Y$ and white noise $\epsilon_{i}$, then $X_{1}$ and $X_{2}$ are conditionally (on $Y$) but not marginally independent. In this case, is Proposition 1 really necessary? 

3. Table 2 suggests that increasing the number of clients concomitantly decreases the running time and enhances the performance of the learned model. Conventional wisdom, however, suggests that there should be a trade-off between these quantities. I thus wonder how many clients would be considered excessive. From a distributed learning perspective, a (possibly empirical) discussion on how to select the number of partitions  (e.g., with a validation set) would significantly strengthen the work. 

4. Definitions 1 and 2, albeit standard, are somewhat cryptical. A concrete example of a distance metric $d$ would be helpful. Also, notations could be made clearer; although expressions such as $\mathbf{X}_{c} \cap \mathbf{X}_{c}$ and $\int_{\mathbf{X} \setminus \mathbf{X}_{c}} p(x)$ are understandable, authors should decide whether $\mathbf{X}_{c}$ is a set or a random variable. 

5. A more extensive discussion on the method’s limitations would be appropriate. When does it fail? Given sufficient data, can FedPCs be scaled to an arbitrary number of clients? In other words, is there a computational bottleneck? Section 4 (Q2) indicates that the only limitation to arbitrarily scaling the model is statistical (via overfitting), rather than computational. On the other hand, is it a better option than traditional neural-based density estimation?  

### Questions
See weaknesses above

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
This paper introduces a novel distributed probabilistic circuit model named Federated Circuits (FC). The authors propose a data-partitioning approach that allows probabilistic circuits to scale effectively within distributed environments, improving both scalability and training efficiency. FC unifies horizontal, vertical, and hybrid federated learning setups and reframes federated learning as a density estimation problem. The experimental results demonstrate the superiority of FC across multiple large-scale datasets, showing its effectiveness in density estimation and classification tasks compared to existing methods.

### Strengths
- The proposed Federated Circuits (FC) offers a fresh perspective by redefining federated learning within a density estimation framework, enabling probabilistic circuits to scale in distributed learning environments.
- This method naturally handles horizontal, vertical, and hybrid federated learning setups, providing a flexible and efficient model expansion pathway.
- Experimental results indicate that FC outperforms or is comparable to existing neural network and tree-based methods

### Weaknesses
Since I am not very familiar with this field, I will refrain from commenting on the weaknesses. My confidence rate is 1, so please feel free to disregard my review.

### Questions
NA

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
2

### Summary
This paper presents a novel method for scaling up probabilistic circuits (PC) by employing a divide-and-conquer framework. The approach involves training models locally on data subsets stored across multiple machines and subsequently aggregating these models through a tailored aggregation procedure. Unlike traditional parameterized neural networks, each model in PC represents a probabilistic distribution, necessitating the authors' development of a novel aggregation approach. Under certain assumptions, the proposed method can unify vertical and horizontal federated learning via a federated version of PC.

### Strengths
The approach of unifying federated learning (FL) through the lens of probabilistic circuits (PC) appears to be novel.

### Weaknesses
 - **Clarity**: The paper is not clearly written, particularly in Section 3.3 (see detailed questions below).
- **Validity of Assumptions**: The framework relies on two main assumptions (Assumptions 1 and 2), but their practical relevance and applicability are unclear.

- **Writing**
    - The definition of FC in Definition 3 is unclear. What is the specific difference between FC and PC based on this definition? In PC, the scope function corresponds to $\psi_{G}$, and the w function corresponds to either summation/product or density evaluation.
    - In Section 3.3, the communication network is not well-defined. How do the nodes N and their parent nodes correspond to different datasets? It’s therefore unclear how the proposed FedPC framework adapts to the FL framework.
    - Further clarification is needed in Section 3.3 on the following:
        - What does “all clients *share* their features with a server” mean?
        - What does “each random variable assumed to be *uniquely identifiable* across all clients” mean?
        - The notation used in Algorithm 1 is unconventional and confusing, for example, on Line 5.
        - What does it mean for “*the server to divide the joint feature space X into disjoint subspaces xxx using a unique descriptor vector u*”?
        - Overall, the description make it difficult to follow the proposed one-pass training approach.
- **Experiments**
    - In the experiment addressing Q1, it is unclear which density function is being estimated—is it the joint distribution of features and labels? Given the tractable inference property of PC, it might be more informative to leverage the estimated probabilities for conditional distribution P(y∣x) in order to perform classification on the image datasets. Without this, the motivation for applying PC to these tasks is less convincing.
    - The number of clients in the same experiment is quite small. How does the proposed method scale with an increasing number of clients?
    - In the experiment for Q3, is it appropriate to compare methods based on TabNet and FC? Could FedAvg show improved performance with an alternative architecture?
    - In the experiment for Q4, what is the rationale for considering only datasets split vertically and not horizontally?

### Questions
- **Writing**
    - The definition of FC in Definition 3 is unclear. What is the specific difference between FC and PC based on this definition? In PC, the scope function corresponds to $\psi_{G}$, and the w function corresponds to either summation/product or density evaluation.
    - In Section 3.3, the communication network is not well-defined. How do the nodes N and their parent nodes correspond to different datasets? It’s therefore unclear how the proposed FedPC framework adapts to the FL framework.
    - Further clarification is needed in Section 3.3 on the following:
        - What does “all clients *share* their features with a server” mean?
        - What does “each random variable assumed to be *uniquely identifiable* across all clients” mean?
        - The notation used in Algorithm 1 is unconventional and confusing, for example, on Line 5.
        - What does it mean for “*the server to divide the joint feature space X into disjoint subspaces xxx using a unique descriptor vector u*”?
        - Overall, the description make it difficult to follow the proposed one-pass training approach.
- **Experiments**
    - In the experiment addressing Q1, it is unclear which density function is being estimated—is it the joint distribution of features and labels? Given the tractable inference property of PC, it might be more informative to leverage the estimated probabilities for conditional distribution P(y∣x) in order to perform classification on the image datasets. Without this, the motivation for applying PC to these tasks is less convincing.
    - The number of clients in the same experiment is quite small. How does the proposed method scale with an increasing number of clients?
    - In the experiment for Q3, is it appropriate to compare methods based on TabNet and FC? Could FedAvg show improved performance with an alternative architecture?
    - In the experiment for Q4, what is the rationale for considering only datasets split vertically and not horizontally?

### Soundness
2

### Presentation
1

### Contribution
2
